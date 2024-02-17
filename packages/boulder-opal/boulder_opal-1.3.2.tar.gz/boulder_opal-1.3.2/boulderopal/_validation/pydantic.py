# Copyright 2024 Q-CTRL. All rights reserved.
#
# Licensed under the Q-CTRL Terms of service (the "License"). Unauthorized
# copying or use of this file, via any medium, is strictly prohibited.
# Proprietary and confidential. You may not use this file except in compliance
# with the License. You may obtain a copy of the License at
#
#    https://q-ctrl.com/terms
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS. See the
# License for the specific language.

from __future__ import annotations

from collections.abc import Sequence as Sequence_
from functools import (
    partial,
    wraps,
)
from itertools import chain
from typing import (
    Any,
    Callable,
    Iterator,
    List,
    Literal,
    Optional,
    Protocol,
    Sequence,
    TypeVar,
    Union,
)

import pydantic

from boulderopal._typing import (
    Annotated,
    ParamSpec,
    get_args,
    get_origin,
)
from boulderopal._validation.exceptions import Checker

USE_PYDANTIC_V1 = (pydantic.__version__.split(".", maxsplit=1)[0]) == "1"


def _dummy() -> tuple[list, list]:
    """
    `SkipValidation` is not available in V1.
    Define a dummy helper to serve the purpose of skipping validation.
    """
    return [], []


if USE_PYDANTIC_V1:
    from pydantic import (  # pylint: disable=no-name-in-module
        ConfigDict,
        validate_arguments,
    )

    SkipValidation = _dummy
else:
    from pydantic import (  # pylint: disable=unused-import,no-name-in-module
        ConfigDict,
        SkipValidation,
        ValidationInfo,
        ValidatorFunctionWrapHandler,
        WrapValidator,
        validate_call,
    )


T = TypeVar("T")


class _ValidatorT(Protocol):
    """
    All validator function should satisfy this protocol.
    """

    def __call__(self, value: Any, *, name: str) -> Any:
        ...


_ValidatorPipe = Optional[Union[List[_ValidatorT], _ValidatorT]]


def _validated_type(arg: Any, _type: Any, name: str) -> Any:  # pylint: disable=R0911
    """
    A helper function to mimic the behavior of Pydantic V2 by running validator/convertor
    with the raw inputs from users.

    This is not meant to cover all supported types in Python, but only for those in
    Boulder Opal (and also handle them according to how they are used in Boulder Opal).
    """
    # We treat Sequence type as list as we only use them for list with mixed types.
    if get_origin(_type) in (list, Sequence_):
        Checker.TYPE(isinstance(arg, (list, tuple)), f"{name} must be a list.")
        _t = get_args(_type)
        assert len(_t) == 1, "List must have the type defined for its element."
        return [
            _validated_type(_v, _t[0], f"{name}[{idx}]") for idx, _v in enumerate(arg)
        ]
    if get_origin(_type) is tuple:
        Checker.TYPE(isinstance(arg, (list, tuple)), f"{name} must be a tuple.")
        tuple_types = get_args(_type)
        assert (
            len(tuple_types) >= 1
        ), "Tuple must have the type defined for its element."
        # when the tuple has a single type.
        if len(tuple_types) == 2 and tuple_types[1] is ...:
            return tuple(
                _validated_type(_v, tuple_types[0], f"{name}[{idx}]")
                for idx, _v in enumerate(arg)
            )
        assert len(tuple_types) > 0, "Tuple must have a type defined for each element."
        Checker.TYPE(
            len(tuple_types) == len(arg),
            "Tuple must have the same number of elements as defined for its type.",
        )
        return tuple(
            _validated_type(_v, tuple_types[idx], f"{name}[{idx}]")
            for idx, _v in enumerate(arg)
        )

    if get_origin(_type) is Union:
        for _t in get_args(_type):
            # Recall arg could be one of those defined in `_type`.
            try:
                return _validated_type(arg, _t, name)
            except TypeError:
                pass
        raise TypeError(f"{name} must be {_type}.")

    if get_origin(_type) is Literal:
        Checker.TYPE(arg in get_args(_type), f"{name} must be {_type}.")
        return arg

    if get_origin(_type) is Annotated:
        _validators = _type.__metadata__
        # _validators contains what we normally define as pipe.
        assert (
            len(_validators) == 1
        ), "Annotated is expected to only have one validator."
        _validator = _validators[0]
        # Recall for V1, pipe returns two lists of validators.
        before, after = _validator()
        for _func in before:
            arg = _func(arg, name=name)
        _expected_type = get_args(_type)[0]
        arg = _validated_type(arg, _expected_type, name)
        for _func in after:
            arg = _func(arg, name=name)
        return arg

    # allow float type to accept int
    if isinstance(arg, int) and issubclass(float, _type):
        return arg
    # allow str Enum to accept str
    if issubclass(_type, str) and isinstance(arg, str):
        return arg
    Checker.TYPE(isinstance(arg, _type), f"{name} must be {_type}.")
    return arg


def pipe(before: _ValidatorPipe = None, *, after: _ValidatorPipe = None) -> Any:
    """
    The if branch is for using Pydantic V1. In that case, the pipe simply returns a callable
    which then returns the before/after validators as two lists. If there is no validator,
    the list would be empty.
    """
    if USE_PYDANTIC_V1:

        def _normalize(x: Any) -> list:
            if x is None:
                return []
            if isinstance(x, list):
                return x
            return [x]

        def _inner() -> tuple[list, list]:
            return _normalize(before), _normalize(after)

        return _inner
    return _pipe(before, after=after)


def _pipe(
    before: _ValidatorPipe = None, *, after: _ValidatorPipe = None
) -> WrapValidator:
    """
    This function is to mimic the behavior of the `Before/AfterValidator` with the `WrapValidator`
    such that one doesn't need to pass the name of the variable to be checked, and provide
    a simpler interface to define execution order.

    `before` and `after` are either a single validator or a list of them.
    All validators must be a callable with a signature like `func(value, *, name)`.

    The execution order is to run validators in the before list in the order as they are
    inserted, then invoke the Pydantic handler, and finally run all validators in the after list
    in the order they are inserted.
    """

    def inner_validator(
        value: T, handler: ValidatorFunctionWrapHandler, info: ValidationInfo
    ) -> T:
        assert isinstance(info.field_name, str)

        def _normalize(validator: _ValidatorPipe) -> Iterator[Callable[[T], T]]:
            if validator is None:
                return iter(())
            if callable(validator):
                return iter([partial(validator, name=info.field_name)])
            return (partial(func, name=info.field_name) for func in validator)

        for _func in chain(_normalize(before), [handler], _normalize(after)):  # type: ignore
            value = _func(value)  # type: ignore
        return value

    return WrapValidator(inner_validator)


P = ParamSpec("P")
R = TypeVar("R")


def validated(func: Callable[P, R]) -> Callable[P, R]:
    """
    Wrap validate for V1 and V2.
    """

    if USE_PYDANTIC_V1:
        return _v1_validated(func)
    return _v2_validated(func)


def _v1_validated(func: Callable[P, R]) -> Callable[P, R]:
    """
    A validator when using Pydantic V1, which is mainly to call the validators
    defined in the type annotations.
    """

    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        pydantic_object = validate_arguments(
            config={"arbitrary_types_allowed": True}
        )(  # type:ignore
            func
        )
        _annotations = pydantic_object.model.__annotations__
        assert isinstance(_annotations, dict)
        validated_args = [
            arg
            if idx == 0  # skip checking `self` (args[0])
            else _validated_type(
                arg,
                _annotations[pydantic_object.vd.arg_mapping[idx]],
                pydantic_object.vd.arg_mapping[idx],
            )
            for idx, arg in enumerate(args)
        ]
        validated_kwargs = {
            key: _validated_type(val, _annotations[key], key) if key != "name" else val
            for key, val in kwargs.items()
        }
        return func(*validated_args, **validated_kwargs)

    return wrapper


def _v2_validated(func: Callable[P, R]) -> Callable[P, R]:
    """
    Decorator to mark a callable as validated by Pydantic (V2) and in-house validators.

    The function wraps `validate_call` and `func` so that we can use Pydantic
    to validate inputs for the callable and also maintain its signature
    and docstring.

    Note that we enable the `arbitrary_types_allowed` flag to support the
    customized/flexible types in Boulder Opal.
    """

    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        return validate_call(func, config=ConfigDict(arbitrary_types_allowed=True))(  # type: ignore
            *args, **kwargs
        )

    return wrapper


def type_pipe(
    validators: list[_ValidatorT], messenger: Callable[[str], str]
) -> _ValidatorT:
    """
    Run the validators in the `validators` list sequentially until the value is resolved.
    Otherwise, throw a TypeError with the message customized by the `messenger` callable.

    This could be useful when resolving union types like scalar | Tensor.
    Similarly, all validators must have a signature like `func(value, * , name)`.
    """

    def _inner(value: T, *, name: str) -> T:
        for _validator in validators:
            try:
                return _validator(value, name=name)
            except TypeError:
                pass
        raise TypeError(messenger(name))

    return _inner


def sequence_like(
    validator: _ValidatorT, normalizer: Optional[type] = None, min_length: int = 1
) -> _ValidatorT:
    """
    Validate a single element or a list/tuple of elements with the same type.
    The element validator must have a signature like `func(value, * , name)`.

    This is useful in the case we want to perform validation for input type like `T | list[T]`,
    where we need to apply the same validator either to `T` or `list[T]`.

    Type like `T | list[T]` is often introduced for UX. If we want to normalize internally
    (i.e., to only handle `list[T]`), we can pass the optional `normalizer`. This parameter
    is expected to either be `list` or `tuple`.

    Note that similar to other utility Pydantic functions, this helper assumes that input
    can only be 1D sequence and doesn't support types other than list and tuple. Such
    type-checking is done by Pydantic.
    """

    def _inner(value: T, *, name: str) -> list[T] | tuple[T, ...] | T:
        if isinstance(value, (list, tuple)):
            Checker.VALUE(
                len(value) >= min_length,
                f"The {name} must have at least length {min_length}.",
            )
            return type(value)(
                validator(item, name=f"{name}[{idx}]") for idx, item in enumerate(value)
            )
        if normalizer is not None:
            return normalizer([validator(value, name=name)])
        return validator(value, name=name)

    return _inner


_S = TypeVar("_S", bound=Sequence)


def minimum_length(length: int) -> _ValidatorT:
    """
    Impose the length constraints of sequence-like input.
    """

    def _inner(value: _S, *, name: str) -> _S:
        Checker.VALUE(
            len(value) >= length, f"The {name} must at least have {length} elements."
        )
        return value

    return _inner
