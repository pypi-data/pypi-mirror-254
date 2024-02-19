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
"""
Utilities for commons nodes.
"""
from numbers import Number
from typing import Union

import numpy as np
from qctrlcommons.exceptions import QctrlArgumentsValueError
from qctrlcommons.preconditions import (
    check_argument,
    check_argument_integer,
    check_argument_iterable,
    check_argument_operator,
    check_argument_orthogonal_projection_operator,
    check_argument_real_vector,
    check_numeric_numpy_array,
    check_sample_times,
)
from scipy.sparse import spmatrix

from .node_data import (
    Pwc,
    Stf,
    Tensor,
)

TensorLike = Union[np.ndarray, Tensor]
TensorLikeOrFunction = Union[np.ndarray, Tensor, Pwc, Stf]
NumericOrFunction = Union[float, complex, np.ndarray, Tensor, Pwc, Stf]
_IntType = (int, np.integer)


def get_broadcasted_shape(*shapes):
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

    Raises
    ------
    QctrlArgumentsValueError
        If the two shapes aren't broadcastable.
    """

    shape = get_broadcasted_shape(x_shape, y_shape)
    check_argument(
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

    Raises
    ------
    QctrlArgumentsValueError
        if the two objects aren't compatible.
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

    Raises
    ------
    QctrlArgumentsValueError
        if the two objects aren't compatible.
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

    Raises
    ------
    QctrlArgumentsValueError
        if the input is neither a scalar, a NumPy array, nor a Tensor.
    """

    if hasattr(tensor_like, "shape"):
        return tuple(tensor_like.shape)

    if np.isscalar(tensor_like):
        return ()

    raise QctrlArgumentsValueError(
        f"The type of {tensor_like_name} is not valid.", {tensor_like_name: tensor_like}
    )


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

    Raises
    ------
    QctrlArgumentsValueError
        if the input is neither a scalar, a Pwc, nor an Stf
    """

    if hasattr(tensor, "value_shape") and hasattr(tensor, "batch_shape"):
        return tuple(tensor.batch_shape), tuple(tensor.value_shape)

    if hasattr(tensor, "value_shape"):
        return (), tuple(tensor.value_shape)

    raise QctrlArgumentsValueError(
        f"The type of {tensor_name}={tensor} must be Pwc or Stf.", {tensor_name: tensor}
    )


def validate_hamiltonian(hamiltonian, hamiltonian_name):
    """
    Check whether a Pwc, Stf or SparsePwc contains values that are Hamiltonians.

    Hamiltonians are two-dimensional and square.

    Parameters
    ----------
    hamiltonian : Pwc or Stf or SparsePwc
        The Hamiltonian to be tested.
    hamiltonian_name : str
        The name of the Hamiltonian, used in the error message.
    """
    value_shape = getattr(hamiltonian, "value_shape", ())

    check_argument(
        len(value_shape) == 2,
        "The shape of the Hamiltonian must have 2 dimensions.",
        {hamiltonian_name: hamiltonian},
        extras={f"{hamiltonian_name}.value_shape": value_shape},
    )
    check_argument(
        value_shape[-1] == value_shape[-2],
        "The dimensions of the Hamiltonian must have equal sizes.",
        {hamiltonian_name: hamiltonian},
        extras={f"{hamiltonian_name}.value_shape": value_shape},
    )


def validate_ms_shapes(ion_count, ld_values, ld_name, rd_values, rd_name):
    """
    Check if the shapes of the Mølmer–Sørensen parameters are correct.

    The correct shapes for the input parameters of Mølmer–Sørensen gate are
    ``(3, ion_count, ion_count)`` for the Lamb–Dicke parameters and
    ``(3, ion_count)`` for the relative detunings.

    Parameters
    ----------
    ion_count : int
        The number of ions in the chain.
    ld_values : np.ndarray
        The input values of the Lamb–Dicke parameters.
    ld_name : str
        The name of the argument that holds the Lamb–Dicke parameters.
    rd_values : np.ndarray
        The input values of the relative detunings.
    rd_name : str
        The name of the argument that holds the relative detunings.
    """
    check_numeric_numpy_array(ld_values, ld_name)
    check_numeric_numpy_array(rd_values, rd_name)

    ld_shape = validate_shape(ld_values, ld_name)
    rd_shape = validate_shape(rd_values, rd_name)

    check_argument(
        ld_shape == (3, ion_count, ion_count),
        "The Lamb–Dicke parameters must have shape (3, ion_count, ion_count).",
        {ld_name: ld_values},
        extras={"ion_count": ion_count, f"{ld_name}.shape": ld_shape},
    )
    check_argument(
        rd_shape == (3, ion_count),
        "The relative detunings must have shape (3, ion_count).",
        {rd_name: rd_values},
        extras={"ion_count": ion_count, f"{rd_name}.shape": rd_shape},
    )


def validate_batched_operator(operator, name):
    """
    Check if the input is a valid batched operator.

    Parameters
    ----------
    operator : Tensor or np.ndarray
        An operator.
    name : str
        Name of the operator.

    Returns
    -------
    tuple[int], tuple[int]
        The batch shape and value shape of the operator, if all checks are passed.

    Raises
    ------
    QctrlArgumentsValueError
        If operator doesn't have numeric element, or is not square.
    """
    check_numeric_numpy_array(operator, name)
    operator_shape = validate_shape(operator, name)
    check_argument(
        len(operator_shape) >= 2,
        f"The {name} must be at least two dimensional.",
        {name: operator},
    )
    check_argument(
        operator_shape[-1] == operator_shape[-2],
        f"The {name} must be a square in the last two dimensions.",
        {name: operator},
        extras={f"{name} shape": operator_shape},
    )
    return operator_shape[:-2], operator_shape[-2:]


def check_density_matrix_shape(density_matrix, name):
    """
    Check the shape of the input density matrix.

    Parameters
    ----------
    density_matrix : Tensor or np.ndarray
        A density matrix.
    name : str
        Name of the density matrix.
    """
    batch_shape, value_shape = validate_batched_operator(density_matrix, name)
    check_argument(
        len(batch_shape) in [0, 1],
        f"The {name} must be 2D or 3D with the first axis as the batch dimension.",
        {name: density_matrix},
        extras={"density matrix shape": batch_shape + value_shape},
    )


def check_oqs_hamiltonian(hamiltonian, system_dimension, system_name):
    """
    Check whether an open quantum system (OQS) Hamiltonian is valid.

    Parameters
    ----------
    hamiltonian : Pwc or SparsePwc
        Effective system Hamiltonian.
    system_dimension : int
        The dimension of the system.
    system_name : str
        The name of the system for error message.
    """
    check_argument(
        hamiltonian.value_shape == (system_dimension, system_dimension),
        f"The dimension of the Hamiltonian must be compatible with the dimension of {system_name}.",
        {"hamiltonian": hamiltonian},
        extras={
            "hamiltonian dimension": hamiltonian.value_shape,
            "system dimension": system_dimension,
        },
    )


def check_lindblad_terms(lindblad_terms, system_dimension, system_name):
    """
    Check whether Lindblad terms are valid, and whether the number of terms
    is greater than zero.

    Parameters
    ----------
    lindblad_terms : list[tuple[float, np.ndarray or spmatrix]]
        The list of Lindblad terms.
    system_dimension : int
        The dimension of the system.
    system_name : str
        The name of the system for error message.
    """
    check_argument_iterable(lindblad_terms, "lindblad_terms")
    check_argument(
        len(lindblad_terms) > 0,
        "You must provide at least one Lindblad term.",
        {"lindblad_terms": lindblad_terms},
    )

    for index, term in enumerate(lindblad_terms):
        check_argument(
            isinstance(term, tuple) and len(term) == 2,
            "Lindblad terms must be a list of tuples and each tuple must have decay rate and "
            "operator as the elements.",
            {"lindblad_terms": lindblad_terms},
        )
        rate, operator = term
        check_argument(
            rate > 0,
            "The decay rate must be positive.",
            {"lindblad_terms": lindblad_terms},
        )
        check_argument(
            isinstance(operator, (spmatrix, np.ndarray, Tensor)),
            "Lindblad operator must either be a NumPy array, scipy sparse matrix, or Tensor.",
            {"lindblad_terms": lindblad_terms},
        )
        # Extra check for array.
        check_numeric_numpy_array(operator, f"lindblad_terms[{index}][1]")
        _ = validate_shape(operator, f"lindblad_terms[{index}][1]")
        check_argument_operator(operator, f"lindblad_terms[{index}][1]")
        check_argument(
            operator.shape[0] == system_dimension,
            "The dimension of Lindblad operator must be compatible with the dimension "
            f"of {system_name}.",
            {"lindblad_terms": lindblad_terms},
            extras={
                "Lindblad operator shape": operator.shape,
                "system dimension": system_dimension,
            },
        )


def validate_inputs_real_fourier_signal(
    fixed_frequencies, optimizable_frequency_count, randomized_frequency_count
):
    """
    Check if the inputs of real_fourier_pwc/stf_signal function are valid.
    """
    check_argument(
        (fixed_frequencies is not None)
        + (optimizable_frequency_count is not None)
        + (randomized_frequency_count is not None)
        == 1,
        "Exactly one of `fixed_frequencies`, `optimizable_frequency_count` and "
        "`randomized_frequency_count` must be provided.",
        {
            "fixed_frequencies": fixed_frequencies,
            "optimizable_frequency_count": optimizable_frequency_count,
            "randomized_frequency_count": randomized_frequency_count,
        },
    )
    if optimizable_frequency_count is not None:
        check_argument_integer(
            optimizable_frequency_count, "optimizable_frequency_count"
        )
        check_argument(
            optimizable_frequency_count > 0,
            "The number of optimizable frequencies (if provided) must be greater than zero.",
            {"optimizable_frequency_count": optimizable_frequency_count},
        )
    if randomized_frequency_count is not None:
        check_argument_integer(randomized_frequency_count, "randomized_frequency_count")
        check_argument(
            randomized_frequency_count > 0,
            "The number of randomized frequencies (if provided) must be greater than zero.",
            {"randomized_frequency_count": randomized_frequency_count},
        )


def validate_fock_state_input(dimension, level, offset):
    """
    Validate the input for the Fock state node.
    If all input are valid, this function returns the shape of the Fock state.
    """
    from_subsystem = not isinstance(dimension, _IntType)

    if from_subsystem:
        # when from subsystems
        # dimension must be a list of integers
        check_argument(
            _validate_list(dimension, _IntType),
            "Dimension must either be an integer or a list of integers.",
            {"dimension": dimension},
        )
        _dimension_arr = np.asarray(dimension)

        # offset must be a list of non-negative integers of the size len(dimension)
        if offset is not None:
            check_argument(
                isinstance(offset, list)
                and _validate_list(offset, _IntType, len(dimension)),
                "When constructed from subsystems, a non-default offset must be a list of integers "
                "and have the same size as dimension.",
                {"dimension": dimension, "offset": offset},
            )

        _offset_arr = (
            np.zeros_like(_dimension_arr) if offset is None else np.asarray(offset)
        )
        check_argument(
            np.all(_offset_arr >= 0), "Offset must be non-negative.", {"offset": offset}
        )

        # level must be List[int] or List[List[int]] or int
        if isinstance(level, list):
            check_level_list(level, dimension)
            _level_arr = np.asarray(level)
        elif isinstance(level, _IntType):
            _level_arr = np.repeat(level, len(dimension))
        else:
            raise QctrlArgumentsValueError(
                "Level must be an integer, a list of integers, or a list of lists of integers.",
                {"level": level},
            )

        check_argument(
            np.all(_level_arr >= _offset_arr),
            "Level must not be smaller than offset.",
            {"level": level, "offset": offset},
        )
        check_argument(
            np.all(_level_arr < (_dimension_arr + _offset_arr)),
            "Level must be smaller than dimension+offset.",
            {"level": level, "dimension": dimension, "offset": offset},
        )

        return _level_arr.shape[:-1] + (int(np.prod(dimension)),)

    # when direct setup
    # only integer is allowed for dimension
    check_argument(
        isinstance(dimension, _IntType),
        "Dimension must either be an integer or a list of integers.",
        {"dimension": dimension},
    )
    # offset must be non-negative integers if set
    _offset = 0 if offset is None else offset
    check_argument(
        isinstance(_offset, _IntType),
        "Dimension and offset must be the same type. They should either be "
        "integers or a list of integers.",
        {"dimension": dimension, "offset": offset},
    )
    check_argument(_offset >= 0, "Offset must be non-negative.", {"offset": offset})

    # level must be an integer or list of integers that are in [offset, dim+offset)
    check_argument(
        isinstance(level, _IntType) or _validate_list(level, _IntType, None),
        "If the Fock state is not constructed from subsystems, "
        "level must either be an integer or a list of integers.",
        {"dimension": dimension, "level": level},
    )
    level_arr = np.asarray(level)
    check_argument(
        np.all(level_arr >= _offset),
        "Level must not be smaller than offset.",
        {"offset": _offset, "level": level},
    )
    check_argument(
        np.all(level_arr < dimension + _offset),
        "Level must be smaller than dimension + offset.",
        {"dimension": dimension, "offset": _offset, "level": level},
    )

    return level_arr.shape + (dimension,)


def validate_field_operator_input(parameter, lower_bound, name):
    """
    Check the input parameter for creation/annihilation/number operator.
    """
    check_argument(
        isinstance(parameter, _IntType) and parameter >= lower_bound,
        f"{name} must be an integer and not less than {lower_bound}.",
        {name: parameter},
    )


def validate_coherent_state_alpha(alpha):
    """
    Check whether alpha is valid for generating coherent state and
    return the batch shape if alpha is valid. Otherwise, raise an error.
    """

    if isinstance(alpha, list):
        check_argument(
            _validate_list(alpha, Number),
            "Alpha must be either a number, a list of them, or a 1D NumPy array.",
            {"alpha": alpha},
        )
        return (len(alpha),)
    if isinstance(alpha, np.ndarray):
        check_argument(
            alpha.ndim == 1,
            "Alpha must be either a number, a list of them, or a 1D NumPy array.",
            {"alpha": alpha},
        )
        check_numeric_numpy_array(alpha, "alpha")
        return (len(alpha),)
    if isinstance(alpha, Number):
        return ()
    raise QctrlArgumentsValueError(
        "Alpha must be either a number, a list of them, or a 1D NumPy array.",
        {"alpha": alpha},
    )


def check_level_list(level, dimension):
    """
    If level is a list, it must be a list of integers and len(level) == len(dimension).
    If it's a nested list, each element can only be a list of integers of the size len(dimension).
    """
    if isinstance(level[0], _IntType):
        check_argument(
            _validate_list(level, _IntType, len(dimension)),
            "Level must be a list of integers with the same length as dimension.",
            {"level": level, "dimension": dimension},
        )
    elif isinstance(level[0], list):
        for item in level:
            check_argument(
                isinstance(item, list)
                and _validate_list(item, _IntType, len(dimension)),
                "Each batch of level must be a list of integers with the same "
                "length as dimension.",
                {"level": level, "dimension": dimension},
            )
    else:
        raise QctrlArgumentsValueError(
            "Level must be an integer, a list of integers, or a list of lists of integers.",
            {"level": level},
        )


def _validate_list(list_, type_, length=None) -> bool:
    """
    Check list size and elements all have the same type.
    """
    if not isinstance(list_, list):
        return False
    if length is not None and len(list_) != length:
        return False
    for item in list_:
        if not isinstance(item, type_):
            return False
    return True


def check_operation_axis(axis, shape, tensor, tensor_name):
    """
    Certain Tensor operations are applied along the axis of the Tensor.
    The function checks
    1. whether the axis is consistent with the shape of Tensor.
    2. whether there is any repeated item in axis
    """

    if axis is None:
        return list(range(len(shape)))

    if isinstance(axis, _IntType):
        axis = [axis]
    else:
        check_argument(
            isinstance(axis, (list, tuple)),
            "Non-default axis must be an integer, or a list (tuple) of integers.",
            {"axis": axis},
        )
        for item in axis:
            check_argument(
                isinstance(item, _IntType),
                "Elements of axis must be integers.",
                {"axis": axis},
            )
        axis = list(axis)

    for i, dimension in enumerate(axis):
        check_argument(
            -len(shape) <= dimension < len(shape),
            f"Elements of axis must be valid axes of {tensor_name} (between {-len(shape)} "
            f"and {len(shape)-1}, inclusive).",
            {tensor_name: tensor, "axis": axis},
        )
        if dimension < 0:
            axis[i] = dimension + len(shape)

    check_argument(
        len(set(axis)) == len(axis),
        f"Elements of axis must refer to unique dimensions of {tensor_name}.",
        {tensor_name: tensor, "axis": axis},
    )

    return axis


def get_keepdims_operation_shape(shape, axis, keepdims):
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


def mesh_pwc_durations(pwcs):
    """
    Return an array with the durations resulting of meshing the durations
    of the input PWC functions.

    Parameters
    ----------
    pwcs : list[Pwc or SparsePwc]
        The PWC functions whose durations should be meshed.

    Returns
    -------
    np.array
        The array with meshed durations.
    """

    times = np.unique(np.concatenate([np.cumsum(pwc.durations) for pwc in pwcs]))
    return np.diff(np.insert(times, 0, 0))


def validate_filter_function_input(
    control_hamiltonian, noise_operator, frequencies, sample_count, projection_operator
):
    """
    Validate the input of a filter function calculation and
    return the dimension of a Hamiltonian subject to noise.

    Parameters
    ----------
    control_hamiltonian : Pwc
        The control Hamiltonian,
    noise_operator : Pwc
        The noise operator,
    frequencies : np.ndarray
        The frequencies.
    sample_count : int, optional
        The number of samples for the Fourier transform.
    projection_operator : np.ndarray, optional
        The projection operator.

    Returns
    -------
    int
        The dimension of the system.
    """

    validate_hamiltonian(control_hamiltonian, "control_hamiltonian")
    batch_shape, value_shape = validate_batch_and_value_shapes(
        control_hamiltonian, "control_hamiltonian"
    )
    check_argument(
        len(batch_shape) == 0,
        "Batches in control Hamiltonian are not supported.",
        {"control_hamiltonian": control_hamiltonian},
    )
    batch_shape_noise, value_shape_noise = validate_batch_and_value_shapes(
        noise_operator, "noise_operator"
    )
    check_argument(
        len(batch_shape_noise) == 0,
        "Batches in noise operator are not supported.",
        {"noise_operator": noise_operator},
    )
    check_argument(
        value_shape_noise == value_shape,
        "Control Hamiltonian and noise operator must have same value shape.",
        {"control_hamiltonian": control_hamiltonian, "noise_operator": noise_operator},
    )
    dimension = value_shape[-1]

    check_argument_real_vector(frequencies, "frequencies")
    if sample_count is not None:
        check_argument_integer(sample_count, "sample_count")
        check_argument(
            sample_count > 1,
            "If provided, the number of samples must be larger than one.",
            {"sample_count": sample_count},
        )
    if projection_operator is not None:
        check_numeric_numpy_array(projection_operator, "projection_operator")
        check_argument_orthogonal_projection_operator(
            projection_operator, "projection_operator"
        )
        projection_operator_shape = validate_shape(
            projection_operator, "projection_operator"
        )
        check_argument(
            projection_operator_shape == (dimension, dimension),
            "The projection operator must have the same dimension as the control Hamiltonian.",
            {
                "projection_operator": projection_operator,
                "control_hamiltonian": control_hamiltonian,
            },
        )

    return dimension


def check_square_pwc_or_stf(pwc_or_stf, pwc_or_stf_name):
    """
    Checks that the Pwc or Stf is a square matrix, or batch of square matrices.

    Parameters
    ----------
    pwc_or_stf : Pwc or Stf
        The pwc_or_stf to be tested.
    pwc_or_stf_name : str
        The name of the `pwc_or_stf`, used for error messages.
    """
    check_argument(
        isinstance(pwc_or_stf, (Pwc, Stf)),
        f"The {pwc_or_stf_name} must be a Pwc or an Stf.",
        {pwc_or_stf_name: pwc_or_stf},
    )

    check_argument(
        len(pwc_or_stf.value_shape) == 2,
        f"The value of {pwc_or_stf_name} must be a matrix, or batch of matrices.",
        {pwc_or_stf_name: pwc_or_stf},
    )
    check_argument(
        pwc_or_stf.value_shape[0] == pwc_or_stf.value_shape[1],
        f"The value of {pwc_or_stf_name} must be a square matrix, or batch of square matrices.",
        {pwc_or_stf_name: pwc_or_stf},
    )


def check_optimization_variable_parameters(
    initial_values, count, lower_bound, upper_bound
):
    """
    Checks that the initial values for optimization variables are valid.

    Parameters
    ----------
    initial_values : list[np.ndarray] or np.ndarray
        Initial values to be checked.
    count : int
        The number of optimization variables.
    lower_bound : float
        The lower bound of initial values.
    upper_bound : float
        The upper bound of initial values.
    """
    check_argument(count > 0, "count must be positive.", {"count": count})
    check_argument(
        upper_bound > lower_bound,
        "lower_bound must be less than upper_bound.",
        {"lower_bound": lower_bound, "upper_bound": upper_bound},
    )

    def _check_value_array(value_array):
        check_argument(
            isinstance(value_array, np.ndarray) and len(value_array.shape) == 1,
            "Initial values must be a 1D array or a list of 1D arrays.",
            {"initial_values": initial_values, "upper bound": upper_bound},
        )
        check_argument(
            value_array.shape[0] == count,
            "Initial values must have the same length as count.",
            {"initial_values": initial_values, "count": count},
        )

        check_argument(
            np.all(value_array >= lower_bound),
            "Initial values must not be smaller than the lower bound.",
            {"initial_values": initial_values, "lower_bound": lower_bound},
        )
        check_argument(
            np.all(value_array <= upper_bound),
            "Initial values must not be greater than the upper bound.",
            {"initial_values": initial_values, "upper_bound": upper_bound},
        )

    if initial_values is not None:
        if isinstance(initial_values, list):
            for value in initial_values:
                _check_value_array(value)
        else:
            _check_value_array(initial_values)


def check_sample_times_with_bounds(sample_times, sample_times_name, pwc, pwc_name):
    """
    Checks that the sample_times array is valid (see check_sample_times) and
    that its values lie between 0 and sum(pwc.durations) (included).

    Parameters
    ----------
    sample_times : np.ndarray
        The array to be tested.
    sample_times_name : str
        The name of the array.
    pwc : Union[Pwc, SparsePwc]
        The PWC function whose duration bounds the values of the sample times.
    pwc_name : str
        The name of the PWC function.
    """
    check_sample_times(sample_times, sample_times_name)

    duration = np.sum(pwc.durations)
    check_argument(
        (sample_times[0] >= 0.0 or np.isclose(sample_times[0], 0.0))
        and (sample_times[-1] <= duration or np.isclose(sample_times[-1], duration)),
        f"{sample_times_name} must be between 0 and the duration of {pwc_name}.",
        {sample_times_name: sample_times, pwc_name: pwc},
        extras={"sum({duration_pwc_name}.durations)": duration},
    )
