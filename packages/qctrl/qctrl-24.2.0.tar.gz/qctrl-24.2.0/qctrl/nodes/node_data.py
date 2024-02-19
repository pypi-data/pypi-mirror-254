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
Module for inherited wrapper class.
"""

from dataclasses import (
    dataclass,
    field,
)
from typing import (
    Callable,
    List,
    Tuple,
)

import numpy as np
from qctrlcommons.node.wrapper import (
    NamedNodeData,
    NodeData,
)


class ArithmeticMixin:
    """
    Mixin to be used by NodeData that support binary arithmetic operations with
    number/array/Tensor/Pwc/Stf objects.

    By default ``arr + graph.op()`` throws an error, since NumPy doesn't know how to add
    `graph.op()` objects to arrays. Even the fact that the func ops override `__radd__` doesn't
    help, since the NumPy addition takes precedence. We can instead tell NumPy to delegate all
    binary operations to the other operand, by explicitly clearing the `__array_ufunc__`
    attribute.
    """

    __array_ufunc__ = None

    def __add__(self, other):
        return self.operation.graph.add(self, other)

    def __radd__(self, other):
        return self.operation.graph.add(other, self)

    def __sub__(self, other):
        return self.operation.graph.subtract(self, other)

    def __rsub__(self, other):
        return self.operation.graph.subtract(other, self)

    def __matmul__(self, other):
        return self.operation.graph.matmul(self, other)

    def __rmatmul__(self, other):
        return self.operation.graph.matmul(other, self)

    def __mul__(self, other):
        return self.operation.graph.multiply(self, other)

    def __rmul__(self, other):
        return self.operation.graph.multiply(other, self)

    def __floordiv__(self, other):
        return self.operation.graph.floordiv(self, other)

    def __rfloordiv__(self, other):
        return self.operation.graph.floordiv(other, self)

    def __pow__(self, power):
        return self.operation.graph.pow(self, power)

    def __rpow__(self, other):
        return self.operation.graph.pow(other, self)

    def __truediv__(self, other):
        return self.operation.graph.truediv(self, other)

    def __rtruediv__(self, other):
        return self.operation.graph.truediv(other, self)

    def __abs__(self):
        return self.operation.graph.abs(self)

    def __neg__(self):
        return self.operation.graph.negative(self)


@dataclass
class Tensor(NamedNodeData, ArithmeticMixin):
    """
    A multi-dimensional array of data.

    Most functions accepting a :obj:`.Tensor` object can alternatively accept a NumPy array.

    You can use the arithmetic operators ``+``, ``-``, ``*``, ``**``, ``/``, ``//``, and ``@``
    to perform operations between two `Tensor` objects.

    Attributes
    ----------
    shape : tuple
        The shape of the tensor.
    name : str
        The name assigned to the node.

    See Also
    --------
    ~Graph.tensor : Create a real or complex Tensor with the data provided.

    Notes
    -----
    The value of a `Tensor` node can be fetched in a graph calculation
    by adding its `name` in the `output_node_names` parameter for the function call.
    This will add an item to the output dictionary in the calculation result object,
    whose key is `name`. The item's value will be a dictionary
    with the "value" of the Tensor as a NumPy array.
    """

    shape: Tuple[int, ...]

    def __post_init__(self):
        self.operation.is_scalar_tensor = np.prod(self.shape) == 1

    def __getitem__(self, item) -> "Operation":
        """
        refer to item in operation.

        Returns
        -------
        Operation
            getitem operation.
        """
        node_data = self.operation.graph.getitem(self, item)
        shape = np.empty(self.shape)[item].shape
        return Tensor(node_data.operation, shape=shape)

    def __iter__(self):
        # Disable iteration for now. Even though this should work fine in theory (since all client
        # tensors have fully-defined shapes), allowing iterability on the client causes tensors to
        # pass checks that will fail in the backend (for example, if tensors are iterable on the
        # client, a multi-dimensional tensor can be passed to a function that expects a list of
        # tensors; such an input will fail in the backend though). This could be revisited in the
        # future if we're more strict about client-side validation of iterable inputs, or if we
        # update the backend to be able to iterate over tensors.
        raise TypeError(
            "You cannot iterate over Tensors directly. Instead you can iterate over the indices "
            "and extract elements of the tensor using `tensor[index]`."
        )

    def __repr__(self):
        return (
            f'<Tensor: name="{self.name}", '
            f'operation_name="{self.operation.operation_name}", '
            f"shape={self.shape}>"
        )


@dataclass
class Pwc(NamedNodeData, ArithmeticMixin):
    """
    A piecewise-constant tensor-valued function of time (or batch of such functions).

    You can use the arithmetic operators ``+``, ``-``, ``*``, ``**``, ``/``, ``//``, and ``@``
    to perform operations between two `Pwc` objects or between a `Pwc` and a `Tensor`.

    Attributes
    ----------
    values : Tensor
        The values of the function on the piecewise-constant segments.
    durations : np.ndarray
        The durations of the constant segments.
    value_shape : tuple
        The shape of the function value.
    batch_shape : tuple
        The shape of the batch in the function.
    name : str
        The name assigned to the node.

    See Also
    --------
    ~Graph.pwc : Operation to create piecewise-constant functions.

    Notes
    -----
    The value of a `Pwc` node can be fetched in a graph calculation
    by adding its `name` in the `output_node_names` parameter for the function call.
    This will add an item to the output dictionary in the calculation result object,
    whose key is `name`. The item's value will be a list of dictionaries,
    with the "duration" and "value" of the piecewise-constant function at each segment.
    Batch dimensions of the function will be represented as outer lists.

    For more information on `Pwc` nodes see the `Working with time-dependent functions in
    Boulder Opal <https://docs.q-ctrl.com/boulder-opal/legacy/topics/working-with-time-dependent-
    functions-in-boulder-opal>`_ topic.
    """

    value_shape: Tuple[int, ...]
    durations: np.ndarray
    batch_shape: Tuple[int, ...]

    @property
    def values(self):
        """
        Access to the values in Pwc.
        """
        node_data = self.operation.graph.getattr(self, "values")
        shape = (
            tuple(self.batch_shape) + (len(self.durations),) + tuple(self.value_shape)
        )
        return Tensor(node_data.operation, shape=shape)

    def __repr__(self):
        return (
            f'<Pwc: name="{self.name}", '
            f'operation_name="{self.operation.operation_name}", '
            f"value_shape={self.value_shape}, batch_shape={self.batch_shape}>"
        )


@dataclass
class Stf(NodeData, ArithmeticMixin):
    """
    A sampleable tensor-valued function of time (or batch of such functions).

    You can use the arithmetic operators ``+``, ``-``, ``*``, ``**``, ``/``, ``//``, and ``@``
    to perform operations between two `Stf` objects or between an `Stf` and a `Tensor`.

    Attributes
    ----------
    value_shape : tuple
        The shape of the function value.
    batch_shape : tuple
        The shape of the batch in the function.

    See Also
    --------
    ~Graph.identity_stf : Operation to create an `Stf` representing the identity function.

    Notes
    -----
    Stf nodes represent arbitrary functions of time. Piecewise-constant (PWC) or constant functions
    are special cases of Stfs and the Q-CTRL Python package provides specific APIs to support them.
    Note that as the PWC property can simplify the calculation, you should always consider using
    PWC-related APIs if your system parameters or controls are described by PWC functions.

    The value of `Stf` nodes is not fetchable from graphs.
    Therefore, they do not have a `name` attribute.

    For more information on `Stf` nodes see the `Working with time-dependent functions in
    Boulder Opal <https://docs.q-ctrl.com/boulder-opal/legacy/topics/working-with-time-dependent-
    functions-in-boulder-opal>`_ topic.
    """

    value_shape: Tuple[int, ...]
    batch_shape: Tuple[int, ...]

    def __repr__(self):
        return (
            f'<Stf: operation_name="{self.operation.operation_name}", '
            f"value_shape={self.value_shape}, batch_shape={self.batch_shape}>"
        )


@dataclass
class SparsePwc(NodeData):
    """
    A piecewise-constant sparse-matrix-valued function of time.

    Attributes
    ----------
    value_shape : tuple
        The shape of the function value.
    durations : np.ndarray
        The durations of the constant segments.

    See Also
    --------
    ~Graph.sparse_pwc_operator : Operation to create `SparsePwc` operators.

    Notes
    -----
    The value of `SparsePwc` nodes is not fetchable from graphs.
    Therefore, they do not have a `name` attribute.
    """

    value_shape: Tuple[int, ...]
    durations: np.ndarray

    def __repr__(self):
        return (
            f'<SparsePwc: operation_name="{self.operation.operation_name}", '
            f"value_shape={self.value_shape}>"
        )


@dataclass
class Target(NodeData):
    """
    A target gate for an infidelity calculation.

    Attributes
    ----------
    value_shape : tuple
        The shape of the target gate operation.

    See Also
    --------
    ~Graph.target : Operation to define the target operation of a time evolution.

    Notes
    -----
    The value of `Target` nodes is not fetchable from graphs.
    Therefore, they do not have a `name` attribute.
    """

    value_shape: Tuple[int, ...]

    def __repr__(self):
        return (
            f'<Target: operation_name="{self.operation.operation_name}", '
            f"value_shape={self.value_shape}>"
        )


@dataclass
class ConvolutionKernel(NodeData):
    """
    A kernel to be used in a convolution.

    See Also
    --------
    ~Graph.convolve_pwc : Operation to create an `Stf` by convolving a `Pwc` with a kernel.
    ~Graph.gaussian_convolution_kernel : Operation to create a convolution kernel representing a
        normalized Gaussian.
    ~Graph.sinc_convolution_kernel : Operation to create a convolution kernel representing the sinc
        function.

    Notes
    -----
    The value of `ConvolutionKernel` nodes is not fetchable from graphs.
    Therefore, they do not have a `name` attribute.
    """

    def __repr__(self):
        return f'<ConvolutionKernel: operation_name="{self.operation.operation_name}">'


@dataclass
class Sequence(NamedNodeData):
    """
    Wrapper class for creating a sequence of Nodes.
    """

    items: List = field(default_factory=list)

    def create_sequence(self, node_constructor: Callable, size: int) -> "Sequence":
        """
        Populate the `items` of the sequence from the operation.

        Parameters
        ----------
        node_constructor : Callable
            A callable to generate the node data for the sequence.
        size : int
            Size of the sequence.

        Returns
        -------
        Sequence
            The sequence itself.
        """

        def get_item_op(item):
            return self.operation.graph.getitem(self, item).operation

        self.items = [
            node_constructor(get_item_op(index), index) for index in range(size)
        ]

        return self

    def __getitem__(self, index) -> "Operation":
        return self.items[index]

    def __iter__(self):
        return iter(self.items)

    def __len__(self):
        return len(self.items)

    def __repr__(self):
        return (
            f'<Sequence: operation_name="{self.operation.operation_name}", '
            f"items={self.items}>"
        )


@dataclass
class FilterFunction(NamedNodeData):
    """
    A tensor-valued filter function result.

    Attributes
    ----------
    inverse_powers : Tensor
        The values of the filter function at the given frequencies.
    uncertainties : Tensor, optional
        The uncertainties of the filter function values.
        This field is None when the exact method is used for computing the filter function.
    frequencies : np.ndarray
        The frequencies at which the filter function has been evaluated.
    value_shape : tuple[int]
        The shape of the function value.
    exact : bool
        Indicates whether filter function is exact.
    name : str
        The name assigned to the node.

    See Also
    --------
    ~Graph.filter_function :
        Evaluate the filter function for a control Hamiltonian and a noise operator at the given
        frequency elements.

    Notes
    -----
    The value of a `FilterFunction` node can be fetched in a graph calculation
    by adding its `name` in the `output_node_names` parameter for the function call.
    This will add an item to the output dictionary in the calculation result object,
    whose key is `name`. The item's value will be a dictionary
    with NumPy arrays with the "frequencies" and "inverse_powers" values.
    If the filter function calculation is not exact, the dictionary also
    contains an array with the filter function "uncertainties".
    """

    frequencies: np.ndarray
    exact: bool

    @property
    def value_shape(self):
        """
        Access the value shape.
        """
        return (len(self.frequencies),)

    @property
    def inverse_powers(self):
        """
        Access to the inverse powers in FilterFunction.
        """
        node_data = self.operation.graph.getattr(self, "inverse_powers")
        return Tensor(node_data.operation, shape=self.value_shape)

    @property
    def uncertainties(self):
        """
        Access to the uncertainties in FilterFunction.
        """
        if self.exact is False:
            node_data = self.operation.graph.getattr(self, "uncertainties")
            return Tensor(node_data.operation, shape=self.value_shape)
        return None

    def __repr__(self):
        return (
            f'<FilterFunction: name="{self.name}", '
            f'operation_name="{self.operation.operation_name}", '
            f"value_shape={self.value_shape}>"
        )
