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
Module for nodes related to optimization.
"""
from typing import (
    List,
    Optional,
    Union,
)

import forge
import numpy as np
from qctrlcommons.node.base import Node
from qctrlcommons.preconditions import (
    check_argument,
    check_argument_integer,
    check_duration,
)

from . import node_data
from .documentation import Category
from .utils import (
    check_optimization_variable_parameters,
    validate_inputs_real_fourier_signal,
)


class OptimizationVariable(Node):
    r"""
    Create optimization variables, which can be bounded, semi-bounded, or unbounded.

    Use this function to create a sequence of variables that can be tuned by
    the optimizer (within specified bounds) in order to minimize the cost
    function.

    Parameters
    ----------
    count : int
        The number :math:`N` of individual real-valued variables to create.
    lower_bound : float
        The lower bound :math:`v_\mathrm{min}` for generating an initial value for the variables.
        This will also be used as lower bound if the variables are lower bounded.
        The same lower bound applies to all `count` individual variables.
    upper_bound : float
        The upper bound :math:`v_\mathrm{max}` for generating an initial value for the variables.
        This will also be used as upper bound if the variables are upper bounded.
        The same upper bound applies to all `count` individual variables.
    is_lower_unbounded : bool, optional
        Defaults to False. Set this flag to True to define a semi-bounded variable with
        lower bound :math:`-\infty`; in this case, the `lower_bound` parameter is used only for
        generating an initial value.
    is_upper_unbounded : bool, optional
        Defaults to False. Set this flag to True to define a semi-bounded variable with
        upper bound :math:`+\infty`; in this case, the `upper_bound` parameter is used only for
        generating an initial value.
    initial_values : np.ndarray or List[np.ndarray] or None, optional
        Initial values for optimization variable. You can either provide a single initial
        value, or a list of them. Note that all optimization variables in a graph with non-default
        initial values must have the same length. That is, you must set them either as a single
        array or a list of arrays of the same length. Defaults to None, meaning the optimizer
        initializes the variables with random values.
    name : str or None, optional
        The name of the node.

    Returns
    -------
    Tensor
        The sequence :math:`\{v_n\}` of :math:`N` optimization variables. If both
        `is_lower_unbounded` and `is_upper_unbounded` are False, these variables are
        bounded such that :math:`v_\mathrm{min}\leq v_n\leq v_\mathrm{max}`. If one of the
        flags is True (for example `is_lower_unbounded=True`), these variables are
        semi-bounded (for example :math:`-\infty \leq v_n \leq v_\mathrm{max}`).
        If both of them are True, then these variables are unbounded and satisfy that
        :math:`-\infty \leq v_n \leq +\infty`.

    See Also
    --------
    anchored_difference_bounded_variables :
        Create anchored optimization variables with a difference bound.
    :func:`~qctrl.dynamic.namespaces.FunctionNamespace.calculate_optimization` :
        Function to find the minimum of a generic function.
    :func:`.utils.complex_optimizable_pwc_signal` :
        Create a complex optimizable `Pwc` signal.
    :func:`.utils.real_optimizable_pwc_signal` :
        Create a real optimizable `Pwc` signal.

    Examples
    --------
    Perform a simple optimization task.

    >>> variables = graph.optimization_variable(
    ...     2, lower_bound=0, upper_bound=1, name="variables"
    ... )
    >>> x = variables[0]
    >>> y = variables[1]
    >>> cost = (x - 0.1) ** 2 + graph.sin(y) ** 2
    >>> cost.name = "cost"
    >>> result = qctrl.functions.calculate_optimization(
    ...     graph=graph, cost_node_name="cost", output_node_names=["variables"]
    ... )
    >>> result.cost
    0.0
    >>> result.output["variables"]["value"]
    array([0.1, 0.])

    See examples about optimal control of quantum systems in the
    `How to optimize controls in arbitrary quantum systems using graphs
    <https://docs.q-ctrl.com/boulder-opal/legacy/user-guides/how-to-optimize-controls-
    in-arbitrary-quantum-systems-using-graphs>`_ user guide.
    """

    name = "optimization_variable"
    optimizable_variable = True
    args = [
        forge.arg("count", type=int),
        forge.arg("lower_bound", type=float),
        forge.arg("upper_bound", type=float),
        forge.arg("is_lower_unbounded", type=bool, default=False),
        forge.arg("is_upper_unbounded", type=bool, default=False),
        forge.arg(
            "initial_values",
            type=Optional[Union[np.ndarray, List[np.ndarray]]],
            default=None,
        ),
    ]
    rtype = node_data.Tensor
    categories = [Category.OPTIMIZATION_VARIABLES]

    @classmethod
    def create_node_data(cls, _operation, **kwargs):
        count = kwargs["count"]
        lower_bound = kwargs["lower_bound"]
        upper_bound = kwargs["upper_bound"]
        initial_values = kwargs["initial_values"]
        check_optimization_variable_parameters(
            initial_values, count, lower_bound, upper_bound
        )
        return node_data.Tensor(_operation, shape=(count,))


class AnchoredDifferenceBoundedVariables(Node):
    r"""
    Create a sequence of optimizable variables with an anchored difference bound.

    Use this function to create a sequence of optimization variables that have
    a difference bound (each variable is constrained to be within a given
    distance of the adjacent variables) and are anchored to zero at the start
    and end (the initial and final variables are within a given distance of
    zero).

    Parameters
    ----------
    count : int
        The number :math:`N` of individual real-valued variables to create.
    lower_bound : float
        The lower bound :math:`v_\mathrm{min}` on the variables.
        The same lower bound applies to all `count` individual variables.
    upper_bound : float
        The upper bound :math:`v_\mathrm{max}` on the variables.
        The same upper bound applies to all `count` individual variables.
    difference_bound : float
        The difference bound :math:`\delta` to enforce between adjacent
        variables.
    initial_values : np.ndarray or List[np.ndarray] or None, optional
        Initial values for optimization variable. You can either provide a single initial
        value, or a list of them. Note that all optimization variables in a graph with non-default
        initial values must have the same length. That is, you must set them either as a single
        array or a list of arrays of the same length. Defaults to None, meaning the optimizer
        initializes the variables with random values.
    name : str or None, optional
        The name of the node.

    Returns
    -------
    Tensor
        The sequence :math:`\{v_n\}` of :math:`N` anchored difference-bounded
        optimization variables, satisfying
        :math:`v_\mathrm{min}\leq v_n\leq v_\mathrm{max}`,
        :math:`|v_{n-1}-v_n|\leq\delta` for :math:`2\leq n\leq N`,
        :math:`|v_1|\leq\delta`, and :math:`|v_N|\leq\delta`.

    See Also
    --------
    :func:`~qctrl.dynamic.namespaces.FunctionNamespace.calculate_optimization` :
        Function to find the minimum of generic deterministic functions.
    :func:`~qctrl.dynamic.namespaces.FunctionNamespace.calculate_stochastic_optimization` :
        Function to find the minimum of generic stochastic functions.
    optimization_variable : Create optimization variables.

    Examples
    --------
    Create optimizable PWC signal with anchored difference bound.

    >>> values = graph.anchored_difference_bounded_variables(
    ...     count=10, lower_bound=-1, upper_bound=1, difference_bound=0.1
    ... )
    >>> graph.pwc_signal(values=values, duration=1)
    <Pwc: name="pwc_signal_#1", operation_name="pwc_signal", value_shape=(), batch_shape=()>

    See the "Band-limited pulses with bounded slew rates" example in the
    `How to add smoothing and band-limits to optimized controls
    <https://docs.q-ctrl.com/boulder-opal/legacy/user-guides/how-to-add-smoothing-and-band-limits-to-
    optimized-controls#example-band-limited-pulses-with-bounded-slew-rates>`_ user guide.
    """

    name = "anchored_difference_bounded_variables"
    optimizable_variable = True
    args = [
        forge.arg("count", type=int),
        forge.arg("lower_bound", type=float),
        forge.arg("upper_bound", type=float),
        forge.arg("difference_bound", type=float),
        forge.arg(
            "initial_values",
            type=Optional[Union[np.ndarray, List[np.ndarray]]],
            default=None,
        ),
    ]
    rtype = node_data.Tensor
    categories = [Category.OPTIMIZATION_VARIABLES]

    @classmethod
    def create_node_data(cls, _operation, **kwargs):
        count = kwargs["count"]
        lower_bound = kwargs["lower_bound"]
        upper_bound = kwargs["upper_bound"]
        initial_values = kwargs["initial_values"]
        check_optimization_variable_parameters(
            initial_values, count, lower_bound, upper_bound
        )
        return node_data.Tensor(_operation, shape=(count,))


class RealFourierStfSignal(Node):
    r"""
    Create a real sampleable signal constructed from Fourier components.

    Use this function to create a signal defined in terms of Fourier (sine/cosine)
    basis signals that can be optimized by varying their coefficients and, optionally,
    their frequencies.

    Parameters
    ----------
    duration : float
        The total duration :math:`\tau` of the signal.
    initial_coefficient_lower_bound : float, optional
        The lower bound :math:`c_\mathrm{min}` on the initial coefficient
        values. Defaults to -1.
    initial_coefficient_upper_bound : float, optional
        The upper bound :math:`c_\mathrm{max}` on the initial coefficient
        values. Defaults to 1.
    fixed_frequencies : list[float] or None, optional
        The fixed non-zero frequencies :math:`\{f_m\}` to use for the Fourier
        basis. If provided, must be non-empty and specified in the inverse
        units of `duration` (for example if `duration` is in seconds, these
        values must be given in Hertz).
    optimizable_frequency_count : int or None, optional
        The number of non-zero frequencies :math:`M` to use, if the
        frequencies can be optimized. Defaults to 0.
    randomized_frequency_count : int or None, optional
        The number of non-zero frequencies :math:`M` to use, if the
        frequencies are to be randomized but fixed. Defaults to 0.

    Returns
    -------
    Stf(1D, real)
        The optimizable, real-valued, sampleable signal built from the
        appropriate Fourier components.

    Warnings
    --------
    You must provide exactly one of `fixed_frequencies`, `optimizable_variable`,
    or `randomized_frequency_count`.

    See Also
    --------
    real_fourier_pwc_signal : Corresponding operation for `Pwc`.

    Notes
    -----
    This function sets the basis signal frequencies :math:`\{f_m\}`
    depending on the chosen mode:

    * For fixed frequencies, you provide the frequencies directly.
    * For optimizable frequencies, you provide the number of frequencies
      :math:`M`, and this function creates :math:`M` unbounded optimizable
      variables :math:`\{f_m\}`, with initial values in the ranges
      :math:`\{[(m-1)/\tau, m/\tau]\}`.
    * For randomized frequencies, you provide the number of frequencies
      :math:`M`, and this function creates :math:`M` randomized constants
      :math:`\{f_m\}` in the ranges :math:`\{[(m-1)/\tau, m/\tau]\}`.

    After this function creates the :math:`M` frequencies :math:`\{f_m\}`, it
    produces the signal

    .. math::
        \alpha^\prime(t) = v_0 +
        \sum_{m=1}^M [ v_m \cos(2\pi t f_m) + w_m \sin(2\pi t f_m) ],

    where :math:`\{v_m,w_m\}` are (unbounded) optimizable variables, with
    initial values bounded by :math:`c_\mathrm{min}` and
    :math:`c_\mathrm{max}`. This function produces the final signal :math:`\alpha(t)`.

    You can use the signals created by this function for chopped random basis
    (CRAB) optimization [1]_.

    References
    ----------
    .. [1] `P. Doria, T. Calarco, and S. Montangero,
            Phys. Rev. Lett. 106, 190501 (2011).
            <https://doi.org/10.1103/PhysRevLett.106.190501>`_
    """

    name = "real_fourier_stf_signal"
    optimizable_variable = True
    args = [
        forge.arg("duration", type=float),
        forge.arg("initial_coefficient_lower_bound", type=float, default=-1),
        forge.arg("initial_coefficient_upper_bound", type=float, default=1),
        forge.arg("fixed_frequencies", type=Optional[List[float]], default=None),
        forge.arg("optimizable_frequency_count", type=Optional[int], default=None),
        forge.arg("randomized_frequency_count", type=Optional[int], default=None),
    ]
    kwargs = {}  # Stfs don't accept name as an argument.
    rtype = node_data.Stf
    categories = [
        Category.BUILDING_SMOOTH_HAMILTONIANS,
        Category.OPTIMIZATION_VARIABLES,
    ]

    @classmethod
    def create_node_data(cls, _operation, **kwargs):
        duration = kwargs.get("duration")
        check_duration(duration, "duration")

        fixed_frequencies = kwargs.get("fixed_frequencies")
        optimizable_frequency_count = kwargs.get("optimizable_frequency_count")
        randomized_frequency_count = kwargs.get("randomized_frequency_count")
        validate_inputs_real_fourier_signal(
            fixed_frequencies, optimizable_frequency_count, randomized_frequency_count
        )

        return node_data.Stf(_operation, value_shape=(), batch_shape=())


class RealFourierPwcSignal(Node):
    r"""
    Create a piecewise-constant signal constructed from Fourier components.

    Use this function to create a signal defined in terms of Fourier
    (sine/cosine) basis signals that can be optimized by varying their
    coefficients and, optionally, their frequencies.

    Parameters
    ----------
    duration : float
        The total duration :math:`\tau` of the signal.
    segment_count : int
        The number of segments :math:`N` to use for the piecewise-constant
        approximation.
    initial_coefficient_lower_bound : float, optional
        The lower bound :math:`c_\mathrm{min}` on the initial coefficient
        values. Defaults to -1.
    initial_coefficient_upper_bound : float, optional
        The upper bound :math:`c_\mathrm{max}` on the initial coefficient
        values. Defaults to 1.
    fixed_frequencies : list[float] or None, optional
        The fixed non-zero frequencies :math:`\{f_m\}` to use for the Fourier
        basis. If provided, must be non-empty and specified in the inverse
        units of `duration` (for example if `duration` is in seconds, these
        values must be given in Hertz).
    optimizable_frequency_count : int or None, optional
        The number of non-zero frequencies :math:`M` to use, if the
        frequencies can be optimized. Defaults to 0.
    randomized_frequency_count : int or None, optional
        The number of non-zero frequencies :math:`M` to use, if the
        frequencies are to be randomized but fixed. Defaults to 0.
    name : str or None, optional
        The name of the node.

    Returns
    -------
    Pwc(1D, real)
        The optimizable, real-valued, piecewise-constant signal built from the
        appropriate Fourier components.

    Warnings
    --------
    You must provide exactly one of `fixed_frequencies`, `optimizable_variable`,
    or `randomized_frequency_count`.

    See Also
    --------
    real_fourier_stf_signal : Corresponding operation for `Stf`.

    Notes
    -----
    This function sets the basis signal frequencies :math:`\{f_m\}`
    depending on the chosen mode:

    * For fixed frequencies, you provide the frequencies directly.
    * For optimizable frequencies, you provide the number of frequencies
      :math:`M`, and this function creates :math:`M` unbounded optimizable
      variables :math:`\{f_m\}`, with initial values in the ranges
      :math:`\{[(m-1)/\tau, m/\tau]\}`.
    * For randomized frequencies, you provide the number of frequencies
      :math:`M`, and this function creates :math:`M` randomized constants
      :math:`\{f_m\}` in the ranges :math:`\{[(m-1)/\tau, m/\tau]\}`.

    After this function creates the :math:`M` frequencies :math:`\{f_m\}`, it
    produces the signal

    .. math::
        \alpha^\prime(t) = v_0 +
        \sum_{m=1}^M [ v_m \cos(2\pi t f_m) + w_m \sin(2\pi t f_m) ],

    where :math:`\{v_m,w_m\}` are (unbounded) optimizable variables, with
    initial values bounded by :math:`c_\mathrm{min}` and
    :math:`c_\mathrm{max}`. This function produces the final
    piecewise-constant signal :math:`\alpha(t)` by sampling
    :math:`\alpha^\prime(t)` at :math:`N` equally spaced points along the
    duration :math:`\tau`, and using those sampled values as the constant
    segment values.

    You can use the signals created by this function for chopped random basis
    (CRAB) optimization [1]_.

    References
    ----------
    .. [1] `P. Doria, T. Calarco, and S. Montangero,
            Phys. Rev. Lett. 106, 190501 (2011).
            <https://doi.org/10.1103/PhysRevLett.106.190501>`_

    Examples
    --------
    See the "CRAB optimization on a qutrit" example in the
    `How to optimize controls using a Fourier basis
    <https://docs.q-ctrl.com/boulder-opal/legacy/user-guides/how-to-optimize-controls-using-
    a-fourier-basis#example-crab-optimization-on-a-qutrit>`_ user guide.
    """

    name = "real_fourier_pwc_signal"
    optimizable_variable = True
    args = [
        forge.arg("duration", type=float),
        forge.arg("segment_count", type=int),
        forge.arg("initial_coefficient_lower_bound", type=float, default=-1),
        forge.arg("initial_coefficient_upper_bound", type=float, default=1),
        forge.arg("fixed_frequencies", type=Optional[List[float]], default=None),
        forge.arg("optimizable_frequency_count", type=Optional[int], default=None),
        forge.arg("randomized_frequency_count", type=Optional[int], default=None),
    ]
    rtype = node_data.Pwc
    categories = [
        Category.BUILDING_PIECEWISE_CONSTANT_HAMILTONIANS,
        Category.OPTIMIZATION_VARIABLES,
    ]

    @classmethod
    def create_node_data(cls, _operation, **kwargs):
        duration = kwargs.get("duration")
        segment_count = kwargs.get("segment_count")
        check_duration(duration, "duration")

        check_argument_integer(segment_count, "segment_count")
        check_argument(
            segment_count > 0,
            "The number of segments must be greater than zero.",
            {"segment_count": segment_count},
        )

        fixed_frequencies = kwargs.get("fixed_frequencies")
        optimizable_frequency_count = kwargs.get("optimizable_frequency_count")
        randomized_frequency_count = kwargs.get("randomized_frequency_count")
        validate_inputs_real_fourier_signal(
            fixed_frequencies, optimizable_frequency_count, randomized_frequency_count
        )

        durations = duration / segment_count * np.ones(segment_count)

        return node_data.Pwc(
            _operation, value_shape=(), durations=durations, batch_shape=()
        )
