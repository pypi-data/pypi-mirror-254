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

from typing import Optional

import numpy as np

from boulderopal._nodes.node_data import (
    Pwc,
    SparsePwc,
)
from boulderopal._validation import Checker


def get_broadcasted_shape(*shapes) -> Optional[tuple[int, ...]]:
    """
    Return the shape resulting of broadcasting multiple shapes,
    or None if they're not broadcastable.

    The shapes are broadcastable if, for each dimension starting from the end,
    they all have either the same size or a size 1.

    Parameters
    ----------
    *shapes : tuple[int]
        Shapes of the objects.

    Returns
    -------
    tuple[int] or None
        The resulting broadcasted shape if the shapes are broadcastable, otherwise None.
    """

    # Obtain largest length of shapes.
    max_shape_len = max(len(shape) for shape in shapes)

    # Prepend ones to shorter shapes.
    extended_shapes = [(1,) * (max_shape_len - len(shape)) + shape for shape in shapes]

    # Check that the shapes are broadcastable:
    # for each position, all shapes hold either the same value or a 1 and another value.
    broadcasted_shape = []
    for dimensions in zip(*extended_shapes):
        dim_set = set(dimensions)
        if len(dim_set) > 2 or (len(dim_set) == 2 and 1 not in dim_set):
            return None
        # The product of each valid set will be either 1 or the non-1 value.
        broadcasted_shape.append(int(np.prod(list(dim_set))))

    return tuple(broadcasted_shape)


def validate_broadcasted_shape(x_shape, y_shape, x_name, y_name):
    """
    Get the resulting broadcasted shape for two input shapes,
    throwing an error if they're not broadcastable.

    Parameters
    ----------
    x_shape : tuple[int]
        One of the shapes to be broadcasted.
    y_shape : tuple[int]
        The other of the shapes to be broadcasted.
    x_name : str
        The name of the variable whose shape is `x_shape`, used for the error
        message in case the shapes aren't broadcastable.
    y_name : str
        The name of the variable whose shape is `y_shape`, used for the error
        message in case the shapes aren't broadcastable.

    Returns
    -------
    tuple[int]
        The shape of the broadcasted array.
    """

    shape = get_broadcasted_shape(x_shape, y_shape)
    Checker.VALUE(
        shape is not None,
        f"The shapes of {x_name} and {y_name} must be broadcastable.",
        {f"{x_name} shape": x_shape, f"{y_name} shape": y_shape},
    )
    return shape


def validate_function_output_shapes(
    x_batch_shape, x_value_shape, y_batch_shape, y_value_shape, validate_value_shape
):
    """
    Get the output batch and value shape for two input shapes of Pwcs/Stfs.
    The names of the variables are assumed to be x and y when reporting errors.

    Parameters
    ----------
    x_batch_shape : tuple[int]
        The batch shape of the first object.
    x_value_shape : tuple[int]
        The value shape of the first object.
    y_batch_shape : tuple[int]
        The batch shape of the second object.
    y_value_shape : tuple[int]
        The value shape of the second object.
    validate_value_shape : Callable[[tuple, tuple, str, str], tuple]
        Function that takes the value shapes of two Tensors, Pwcs,
        or Stfs (as well as their names), and returns the expected values
        shape of the output Tensor, Pwc, or Stf. The function
        shouldn't assume that the shapes are compatible, and raise an
        exception if they aren't. The names provided should be used to
        generate the error message.

    Returns
    -------
    tuple[int], tuple[int]
        The batch and value shapes of the output Pwc/Stf.
    """
    batch_shape = validate_broadcasted_shape(
        x_batch_shape, y_batch_shape, "x (batch)", "y (batch)"
    )
    value_shape = validate_value_shape(x_value_shape, y_value_shape, "x", "y")

    return batch_shape, value_shape


def validate_tensor_and_function_output_shapes(
    t_shape,
    f_batch_shape,
    f_value_shape,
    t_name,
    f_name,
    validate_value_shape,
    tensor_first=True,
):
    """
    Get the output batch and value shape for an input tensor and an input Pwc/Stf.

    Parameters
    ----------
    t_shape : tuple[int]
        The shape of the tensor.
    f_batch_shape : tuple[int]
        The batch shape of the Pwc/Stf.
    f_value_shape : tuple[int]
        The value shape of the Pwc/Stf.
    t_name : str
        The name of the tensor variable, used for the error message in case the shapes aren't
        compatible.
    f_name : str
        The name of the function variable, used for the error message in case the shapes aren't
        compatible.
    validate_value_shape : Callable[[tuple, tuple, str, str], tuple]
        Function that takes the value shapes of two Tensors, Pwcs,
        or Stfs (as well as their names), and returns the expected values
        shape of the output Tensor, Pwc, or Stf. The function
        shouldn't assume that the shapes are compatible, and raise an
        exception if they aren't. The names provided should be used to
        generate the error message.
    tensor_first : bool, optional
        Whether the Tensor is the leftmost parameter. Defaults to True.

    Returns
    -------
    tuple[int], tuple[int]
        The batch and value shapes of the output Pwc/Stf.
    """
    if tensor_first:
        value_shape = validate_value_shape(t_shape, f_value_shape, t_name, f_name)
    else:
        value_shape = validate_value_shape(f_value_shape, t_shape, f_name, t_name)

    return f_batch_shape, value_shape


def validate_shape(tensor_like, tensor_like_name):
    """
    Return the shape of a scalar, np.ndarray, scipy.sparse.spmatrix, or Tensor node.

    Parameters
    ----------
    tensor_like : number or np.ndarray or scipy.sparse.spmatrix or Tensor
        The object whose shape you want to obtain.
    tensor_like_name : str
        The name of the `tensor_like`, used for error message in case the
        input object is not valid.

    Returns
    -------
    tuple[int]
        The tuple with the size of each dimension of `tensor_like`.
    """
    Checker.VALUE(
        hasattr(tensor_like, "shape") or np.isscalar(tensor_like),
        f"The type of {tensor_like_name} is not valid.",
        {tensor_like_name: tensor_like},
    )
    return getattr(tensor_like, "shape", None) or ()


def validate_batch_and_value_shapes(tensor, tensor_name):
    """
    Return the batch and value shapes of Pwc or Stf.

    Parameters
    ----------
    tensor : Pwc or Stf
        The NodeData for the Pwc or Stf whose batch and value shapes
        you want to obtain.
    tensor_name : str
        The name of the Pwc or Stf, used for the error message in
        case `tensor` doesn't have a value shape.

    Returns
    -------
    tuple[tuple[int]]
        A tuple with a tuple that represents the batch shape, and a tuple
        that represents the value shape, in this sequence.
    """
    Checker.VALUE(
        hasattr(tensor, "value_shape"),
        f"The type of {tensor_name}={tensor} must be Pwc or Stf.",
        {tensor_name: tensor},
    )

    if hasattr(tensor, "value_shape") and hasattr(tensor, "batch_shape"):
        return tuple(tensor.batch_shape), tuple(tensor.value_shape)

    return (), tuple(tensor.value_shape)


def check_operation_axis(
    axis: Optional[list[int] | int], shape: tuple[int, ...], tensor_name: str
) -> list[int]:
    """
    Certain Tensor operations are applied along the axis of the Tensor.
    The function checks
    1. whether the axis is consistent with the shape of the tensor.
    2. whether there are any repeated items in axis.
    """

    if axis is None:
        return list(range(len(shape)))

    if not isinstance(axis, list):
        axis = [axis]

    for i, dimension in enumerate(axis):
        Checker.VALUE(
            -len(shape) <= dimension < len(shape),
            f"Elements of axis must be valid axes of {tensor_name} (between {-len(shape)} "
            f"and {len(shape)-1}, inclusive).",
            {f"axis[{i}]": dimension, f"len({tensor_name}.shape)": len(shape)},
        )
        if dimension < 0:
            axis[i] = dimension + len(shape)

    Checker.VALUE(
        len(set(axis)) == len(axis), "Elements of axis must be unique.", {"axis": axis}
    )

    return axis


def get_keepdims_operation_shape(
    shape: tuple[int, ...], axis: list[int], keepdims: bool
) -> tuple[int, ...]:
    """
    Return the shape of the operations that can keep the dimension of the input tensor.
    """
    output_shape = []
    for i, size in enumerate(shape):
        if i not in axis:
            output_shape.append(size)
        elif keepdims:
            output_shape.append(1)
    return tuple(output_shape)


def mesh_pwc_durations(pwcs: list[Pwc] | list[SparsePwc]) -> np.ndarray:
    """
    Return an array with the durations resulting of meshing the durations
    of the input PWC functions.

    Parameters
    ----------
    pwcs : list[Pwc] or list[SparsePwc]
        The Pwc functions whose durations should be meshed.

    Returns
    -------
    np.array
        The array with meshed durations.
    """
    _durations = [sum(pwc.durations) for pwc in pwcs]
    Checker.VALUE(
        np.allclose(_durations[0], _durations, atol=0.0),
        "All Pwc must have the same duration.",
    )

    times = np.unique(np.concatenate([np.cumsum(pwc.durations) for pwc in pwcs]))
    return np.diff(np.insert(times, 0, 0))
