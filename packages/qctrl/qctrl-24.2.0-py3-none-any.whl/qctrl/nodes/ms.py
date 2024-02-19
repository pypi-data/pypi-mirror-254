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
"""Module for all the Mølmer–Sørensen related nodes."""
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
    check_argument_iterable,
    check_numeric_numpy_array,
)

from .documentation import Category
from .node_data import (
    Pwc,
    Tensor,
)
from .utils import (
    TensorLike,
    check_sample_times_with_bounds,
    validate_ms_shapes,
    validate_shape,
)


class MsPhases(Node):
    r"""
    Calculate the relative phases for all pairs of ions described by a Mølmer–Sørensen-type
    interaction when single-tone individually-addressed laser beams are used.

    Use this function to calculate the acquired phases for all ion pairs
    at the final time of the drives, or at the sample times that you provide.

    Parameters
    ----------
    drives : list[Pwc(1D, complex)]
        A list of piecewise-constant drives :math:`\{\gamma_j\}`.
        The number of drives must be the same as the number of ions :math:`N`.
        Drive values must be one-dimensional arrays and in rad/s. Drive durations must be
        in seconds. All drives must have the same total duration, but can have different numbers
        of segments. This list must contain at least two elements. In other words,
        your system must contain at least two ions.
    lamb_dicke_parameters : np.ndarray
        A 3D array of parameters :math:`\{\eta_{jkl}\}` specifying the laser-ion coupling strength.
        Its shape must be ``(3, N, N)`` where the first dimension :math:`j` indicates the axis,
        the second dimension :math:`k` indicates the collective
        mode number, and the third dimension :math:`l` indicates the ion.
    relative_detunings : np.ndarray
        A 2D array :math:`\{\delta_{jk} = \nu_{jk} - \delta\}` specifying the difference (in Hz)
        between each motional mode frequency :math:`\nu_{jk}` and the laser detuning :math:`\delta`
        (the detuning from the qubit transition frequency :math:`\omega_0`).
        Its shape must be ``(3, N)`` where the first dimension :math:`j` indicates the axis and the
        second dimension :math:`k` indicates the collective mode number.
    sample_times : list or tuple or np.ndarray or None, optional
        A 1D array of length :math:`T` specifying the times :math:`\{t_i\}` (in seconds) at which
        this function calculates the relative phases.
        If you omit it, this function calculates the phases only at the final time of the drives.
        If provided, it must be ordered and contain at least one element.
    name : str or None, optional
        The name of the node.

    Returns
    -------
    Tensor(real)
        Acquired phases :math:`\{\phi_{jk}(t_i) + \phi_{kj}(t_i)\}` for all ion pairs.
        If you provide `sample_times`, the shape of the returned value is ``(T, N, N)``,
        where the first dimension indicates the time; the second and the third dimensions
        indicate the ion. Otherwise, the shape is ``(N, N)`` where both dimensions indicate
        the ion. The relative phases are stored as a strictly lower triangular matrix. See
        the notes part for details.

    See Also
    --------
    :func:`~qctrl.dynamic.namespaces.FunctionNamespace.calculate_ion_chain_properties` :
        Function to calculate the properties of an ion chain.
    ms_infidelity : Final operational infidelity of a Mølmer–Sørensen gate.
    ms_phases_multitone : Corresponding operation for a global multitone beam.

    Notes
    -----
    The internal and motional Hamiltonian of :math:`N` ions is

    .. math::
        H_0 = \sum_{p = 1}^{3N} \hbar\nu_p \left(a_p^\dagger a_p + \frac{1}{2}\right)
            + \sum_{j = 1}^N \frac{\hbar \omega_0}{2} \sigma_{z,j} ,

    where the axis dimension and collective mode dimension are combined into a single index
    :math:`p` for simplicity, :math:`a_p` is the annihilation operator for the mode :math:`p`,
    and :math:`\sigma_{z,j}` is the Pauli :math:`Z` operator for the ion :math:`j`.
    The interaction Hamiltonian for Mølmer–Sørensen-type
    operations in the rotating frame with respect to :math:`H_0` is:

    .. math::
        H_I(t) = i\hbar\sum_{j = 1}^N \sigma_{x, j} \sum_{p = 1}^{3N} (-\beta_{pj}^*(t)a_p +
                \beta_{pj}(t) a_p^\dagger) ,

    where :math:`\sigma_{x, j}` is the Pauli :math:`X` operator for the ion :math:`j` and
    :math:`\beta_{pj}(t) = \eta_{pj} \frac{\gamma_j(t)}{2} e^{i\delta_p t}`,
    indicating the coupling of the ion :math:`j` to the motional mode :math:`p`.
    Note that :math:`\delta_p` is the angular relative detuning, which corresponds to
    :math:`2 \pi` times the `relative_detuning` parameter that you passed.
    The corresponding unitary operation is given by [1]_

    .. math::
        U(t) = \exp\left[ \sum_{j=1}^N \sigma_{x, j} B_j(t)
                + i\sum_{j=1}^N\sum_{k=1}^{j - 1} (\phi_{jk}(t) + \phi_{kj}(t))
                \sigma_{x, j} \sigma_{x, k} \right] ,

    where

    .. math::
        B_j(t) &\equiv \sum_{p = 1}^{3N}  \left(\eta_{pj}\alpha_{pj}(t)a_p^\dagger
             - \eta_{pj}^{\ast}\alpha_{pj}^\ast(t)a_p \right) ,

        \phi_{jk}(t) &\equiv \mathrm{Im} \left[ \sum_{p=1}^{3N} \int_{0}^{t} d \tau_1
            \int_{0}^{\tau_1} d \tau_2 \beta_{pj}(\tau_1)\beta_{pk}^{\ast}(\tau_2) \right] ,

    and

    .. math::
        \alpha_{pj}(t) = \int_0^t d\tau \frac{\gamma_j(\tau)}{2} e^{i \delta_p \tau} .

    This function calculates the relative phases
    :math:`\Phi_{jk}(t_i) = \phi_{jk}(t_i) + \phi_{kj}(t_i)`
    for all ions pairs at time :math:`t_i` and stores the result in the form of a strictly
    lower triangular matrix. That is, the :math:`jk`-th element of
    that matrix records the relative phase between the ion :math:`j` and :math:`k`,
    while the elements with indices :math:`j \leq k` are zeros.

    References
    ----------
    .. [1] `C. D. B. Bentley, H. Ball, M. J. Biercuk, A. R. R. Carvalho,
            M. R. Hush, and H. J. Slatyer,
            Adv. Quantum Technol. 3, 2000044 (2020).
            <https://doi.org/10.1002/qute.202000044>`_

    Examples
    --------
    Refer to the `How to optimize error-robust Mølmer–Sørensen gates for trapped ions
    <https://docs.q-ctrl.com/boulder-opal/legacy/user-guides/how-to-optimize-error-robust-molmer-
    sorensen-gates-for-trapped-ions>`_ user guide to find how to use this and related nodes.
    """

    name = "ms_phases"
    args = [
        forge.arg("drives", type=List[Pwc]),
        forge.arg("lamb_dicke_parameters", type=np.ndarray),
        forge.arg("relative_detunings", type=np.ndarray),
        forge.arg(
            "sample_times", type=Optional[Union[list, tuple, np.ndarray]], default=None
        ),
    ]
    rtype = Tensor
    categories = [Category.MOLMER_SORENSEN]

    @classmethod
    def create_node_data(cls, _operation, **kwargs):
        drives = kwargs.get("drives")
        sample_times = kwargs.get("sample_times")
        lamb_dicke_parameters = kwargs.get("lamb_dicke_parameters")
        relative_detunings = kwargs.get("relative_detunings")
        check_argument_iterable(drives, "drives")
        check_argument(
            len(drives) > 1, "At least two drives must be provided.", {"drives": drives}
        )
        check_argument(
            all(isinstance(drive, Pwc) for drive in drives),
            "Each of the drives must be a Pwc.",
            {"drives": drives},
        )
        check_argument(
            all(len(drive.values.shape) == 1 for drive in drives),
            "The value of each drive must be 1D.",
            {"drives": drives},
        )
        ion_count = len(drives)
        shape = (ion_count, ion_count)
        validate_ms_shapes(
            ion_count=ion_count,
            ld_values=lamb_dicke_parameters,
            ld_name="lamb_dicke_parameters",
            rd_values=relative_detunings,
            rd_name="relative_detunings",
        )
        if sample_times is not None:
            sample_times = np.asarray(sample_times)
            check_sample_times_with_bounds(
                sample_times, "sample_times", drives[0], "drives[0]"
            )
            time_count = len(sample_times)
            shape = (time_count,) + tuple(shape)
        return Tensor(_operation, shape=shape)


class MsPhasesMultitone(Node):
    r"""
    Calculate the relative phases for all pairs of ions described by a
    Mølmer–Sørensen-type interaction where the ions are being addressed by
    a multitone global beam.

    Use this function to calculate the acquired phases for all ion pairs
    at the final time of the drives, or at the sample times that you provide.

    Parameters
    ----------
    drives : list[Pwc(1D, complex)]
        A list of piecewise-constant drives :math:`\{\gamma_\xi\}` for
        each of the tones of the global beam.
        The number of drives must be the same as the number of tones of
        the global beam, :math:`M`.
        Drive values must be one-dimensional arrays and in rad/s. Drive durations must be
        in seconds. All drives must have the same total duration, but can have different numbers
        of segments.
    lamb_dicke_parameters : np.ndarray
        A 4D array of parameters :math:`\{\eta_{\xi jkl}\}` specifying
        the laser-ion coupling strength. Its shape must be ``(M, 3, N, N)``
        where the first dimension :math:`\xi` indicates the tone of
        the global beam, the second dimension :math:`j` indicates the axis,
        the third dimension :math:`k` indicates the collective
        mode number, and the fourth dimension :math:`l` indicates the ion.
    relative_detunings : np.ndarray
        A 3D array :math:`\{\delta_{\xi jk} = \nu_{jk} - \delta_\xi \}`
        specifying the difference (in Hz) between each motional mode frequency
        :math:`\nu_{jk}` and the laser detunings for each tone,
        :math:`\delta_\xi` (the detuning from the qubit transition frequency
        :math:`\omega_0`). Its shape must be ``(M, 3, N)`` where the first
        dimension :math:`\xi` indicates the tone of the global beam,
        the second dimension :math:`j` indicates the axis and the third
        dimension :math:`k` indicates the collective mode number.
    sample_times : list or tuple or np.ndarray or None, optional
        A 1D array of length :math:`T` specifying the times :math:`\{t_i\}` (in seconds) at which
        this function calculates the relative phases.
        If you omit it, this function calculates the phases only at the final time of the drives.
        If provided, it must be ordered and contain at least one element.
    name : str or None, optional
        The name of the node.

    Returns
    -------
    Tensor(real)
        Acquired phases :math:`\{\phi_{jk}(t_i) + \phi_{kj}(t_i)\}` for all ion pairs.
        If you provide `sample_times`, the shape of the returned value is ``(T, N, N)``,
        where the first dimension indicates the time; the second and the third dimensions
        indicate the ion. Otherwise, the shape is ``(N, N)`` where both dimensions indicate
        the ion. The relative phases are stored as a strictly lower triangular matrix. See
        the notes part for details.

    See Also
    --------
    :func:`~qctrl.dynamic.namespaces.FunctionNamespace.calculate_ion_chain_properties` :
        Function to calculate the properties of an ion chain.
    ms_infidelity : Final operational infidelity of a Mølmer–Sørensen gate.
    ms_phases: Corresponding operation for single-tone individually-addressed beams.

    Notes
    -----
    The interaction Hamiltonian for Mølmer–Sørensen-type
    operations in the rotating frame for a multitone global beam is:

    .. math::
        H_I(t) = i\hbar\sum_{j = 1}^N \sigma_{x, j} \sum_{p = 1}^{3N} \sum_{\xi = 1}^M
                 (-\beta_{\xi pj}^*(t)a_p + \beta_{\xi pj}(t) a_p^\dagger) ,

    where :math:`\sigma_{x, j}` is the Pauli :math:`X` operator for the ion :math:`j` and
    :math:`\beta_{\xi pj}(t) = \eta_{\xi pj} \frac{\gamma_\xi(t)}{2} e^{i\delta_{\xi p} t}`,
    indicating the coupling of the ion :math:`j` to the motional mode :math:`p`.
    Note that :math:`\delta_p` is the angular relative detuning, which corresponds to
    :math:`2 \pi` times the `relative_detuning` parameter that you passed.
    The corresponding unitary operation is given by:

    .. math::
        U(t) = \exp\left[ \sum_{j=1}^N \sigma_{x, j} B_j(t)
                + i\sum_{j=1}^N \sum_{k=1}^{j - 1} (\phi_{jk}(t) + \phi_{kj}(t))
                \sigma_{x, j} \sigma_{x, k} \right] ,

    where

    .. math::
        B_j(t) &\equiv \sum_{p = 1}^{3N} \sum_{\xi = 1}^M
             \left(\eta_{\xi pj}\alpha_{\xi pj}(t)a_p^\dagger
             - \eta_{\xi pj}^{\ast}\alpha_{\xi pj}^\ast(t)a_p \right) ,

        \phi_{jk}(t) &\equiv \mathrm{Im} \left[ \sum_{p=1}^{3N} \sum_{\xi_1 = 1}^M
            \sum_{\xi_2 = 1}^M \int_{0}^{t} d \tau_1 \int_{0}^{\tau_1} d \tau_2
            \beta_{\xi_1 pj}(\tau_1)\beta_{\xi_2 pk}^{\ast}(\tau_2) \right] ,

    with :math:`\alpha_{\xi pj}(t) = \int_0^t d\tau \frac{\gamma_\xi(\tau)}{2}
    e^{i \delta_{\xi p} \tau}`.

    This function calculates the relative phases :math:`\phi_{jk}(t_i) + \phi_{kj}(t_i)`
    for all ions pairs at time :math:`t_i` and stores the result in the form of a strictly
    lower triangular matrix. That is, the :math:`jk`-th element of
    that matrix records the relative phase between the ion :math:`j` and :math:`k`,
    while the elements with indices :math:`j \leq k` are zeros.
    """

    name = "ms_phases_multitone"
    args = [
        forge.arg("drives", type=List[Pwc]),
        forge.arg("lamb_dicke_parameters", type=np.ndarray),
        forge.arg("relative_detunings", type=np.ndarray),
        forge.arg(
            "sample_times", type=Optional[Union[list, tuple, np.ndarray]], default=None
        ),
    ]
    rtype = Tensor
    categories = [Category.MOLMER_SORENSEN]

    @classmethod
    def create_node_data(cls, _operation, **kwargs):
        drives = kwargs.get("drives")
        sample_times = kwargs.get("sample_times")
        lamb_dicke_parameters = kwargs.get("lamb_dicke_parameters")
        relative_detunings = kwargs.get("relative_detunings")
        check_argument_iterable(drives, "drives")
        check_argument(
            len(drives) > 0, "At least one drive must be provided.", {"drives": drives}
        )
        check_argument(
            all(isinstance(drive, Pwc) for drive in drives),
            "Each of the drives must be a Pwc.",
            {"drives": drives},
        )
        check_argument(
            all(len(drive.values.shape) == 1 for drive in drives),
            "The value of each drive must be 1D.",
            {"drives": drives},
        )

        check_numeric_numpy_array(lamb_dicke_parameters, "lamb_dicke_parameters")
        check_numeric_numpy_array(relative_detunings, "relative_detunings")

        ld_shape = validate_shape(lamb_dicke_parameters, "lamb_dicke_parameters")
        rd_shape = validate_shape(relative_detunings, "relative_detunings")

        tone_count = len(drives)
        ion_count = ld_shape[-1]
        check_argument(
            ld_shape == (tone_count, 3, ion_count, ion_count),
            "The Lamb-Dicke parameters must have shape (tone_count, 3, ion_count, ion_count).",
            {"lamb_dicke_parameters": lamb_dicke_parameters},
            extras={
                "ion_count": ion_count,
                "tone_count": tone_count,
                "lamb_dicke_parameters.shape": ld_shape,
            },
        )
        check_argument(
            rd_shape == (tone_count, 3, ion_count),
            "The relative detunings must have shape (tone_count, 3, ion_count).",
            {"relative_detunings": relative_detunings},
            extras={
                "ion_count": ion_count,
                "tone_count": tone_count,
                "relative_detunings.shape": rd_shape,
            },
        )

        shape = (ion_count, ion_count)
        if sample_times is not None:
            sample_times = np.asarray(sample_times)
            check_sample_times_with_bounds(
                sample_times, "sample_times", drives[0], "drives[0]"
            )
            time_count = len(sample_times)
            shape = (time_count,) + shape

        return Tensor(_operation, shape=shape)


class MsDisplacements(Node):
    r"""
    Calculate the displacements for each mode and ion combination where ions are described by
    a Mølmer–Sørensen-type interaction.

    Use this function to calculate the displacements for each ion and each mode
    at the final time of the drives, or at the sample times that you provide.

    Parameters
    ----------
    drives : list[Pwc(1D, complex)]
        A list of piecewise-constant drives :math:`\{\gamma_j\}`.
        The number of drives must be the same as the number of ions :math:`N`.
        Drive values must be one-dimensional arrays and in rad/s.
        Drive durations must be in seconds.
        All drives must have the same total duration, but can have different numbers of segments.
    lamb_dicke_parameters : np.ndarray
        A 3D array of parameters :math:`\{\eta_{jkl}\}` specifying the laser-ion coupling strength.
        Its shape must be ``(3, N, N)`` where the first dimension :math:`j` indicates the axis,
        the second dimension :math:`k` indicates the collective
        mode number, and the third dimension :math:`l` indicates the ion.
    relative_detunings : np.ndarray
        A 2D array :math:`\{\delta_{jk} = \nu_{jk} - \delta\}` specifying the difference (in Hz)
        between each motional mode frequency :math:`\nu_{jk}` and the laser detuning :math:`\delta`
        (the detuning from the qubit transition frequency :math:`\omega_0`).
        Its shape must be ``(3, N)`` where the first dimension :math:`j` indicates the axis and the
        second dimension :math:`k` indicates the collective mode number.
    sample_times : list or tuple or np.ndarray or None, optional
        A 1D array of length :math:`T` specifying the times :math:`\{t_i\}` (in seconds) at which
        this function calculates the displacements.
        If you omit it, this function calculates the phases only at the final time of the drives.
        If provided, it must be ordered and contain at least one element.
    name : str or None, optional
        The name of the node.

    Returns
    -------
    Tensor(complex)
        Displacements :math:`\{\eta_{pj}\alpha_{pj}(t_i)\}` for all mode-ion combinations.
        If you provide `sample_times`, the shape of the returned value is ``(T, 3, N, N)``
        where the first dimension indicates the time, the second dimension indicates the axis,
        the third dimension indicates the collective mode number, and the last dimension indicates
        the ion. Otherwise, the shape is ``(3, N, N)`` with the outer time dimension removed.

    See Also
    --------
    :func:`~qctrl.dynamic.namespaces.FunctionNamespace.calculate_ion_chain_properties` :
        Function to calculate the properties of an ion chain.
    ms_infidelity : Final operational infidelity of a Mølmer–Sørensen gate.

    Notes
    -----
    The internal and motional Hamiltonian of :math:`N` ions is

    .. math::
        H_0 = \sum_{p = 1}^{3N} \hbar\nu_p \left(a_p^\dagger a_p + \frac{1}{2}\right)
            + \sum_{j = 1}^N \frac{\hbar \omega_0}{2} \sigma_{z,j} ,

    where the axis dimension and collective mode dimension are combined into a single index
    :math:`p` for simplicity, :math:`a_p` is the annihilation operator for the mode :math:`p`,
    and :math:`\sigma_{z,j}` is the Pauli :math:`Z` operator for the ion :math:`j`.
    The interaction Hamiltonian for Mølmer–Sørensen-type
    operations in the rotating frame with respect to :math:`H_0` is:

    .. math::
        H_I(t) = i\hbar\sum_{j = 1}^N \sigma_{x, j} \sum_{p = 1}^{3N} (-\beta_{pj}^*(t)a_p +
                \beta_{pj}(t) a_p^\dagger) ,

    where :math:`\sigma_{x, j}` is the Pauli :math:`X` operator for the ion :math:`j` and
    :math:`\beta_{pj}(t) = \eta_{pj} \frac{\gamma_j(t)}{2} e^{i\delta_p t}`,
    indicating the coupling of the ion :math:`j` to the motional mode :math:`p`.
    Note that :math:`\delta_p` is the angular relative detuning, which corresponds to
    :math:`2 \pi` times the `relative_detuning` parameter that you passed.
    The corresponding unitary operation is given by [1]_

    .. math::
        U(t) = \exp\left[ \sum_{j=1}^N \sigma_{x, j} B_j(t)
                + i\sum_{j=1}^N\sum_{k=1}^{j - 1} (\phi_{jk}(t) + \phi_{kj}(t))
                \sigma_{x, j} \sigma_{x, k} \right] ,

    where

    .. math::
        B_j(t) &\equiv \sum_{p = 1}^{3N}  \left(\eta_{pj}\alpha_{pj}(t)a_p^\dagger
             - \eta_{pj}^{\ast}\alpha_{pj}^\ast(t)a_p \right) ,

        \phi_{jk}(t) &\equiv \mathrm{Im} \left[ \sum_{p=1}^{3N} \int_{0}^{t} d \tau_1
            \int_{0}^{\tau_1} d \tau_2 \beta_{pj}(\tau_1)\beta_{pk}^{\ast}(\tau_2) \right] ,

    and

    .. math::
        \alpha_{pj}(t) = \int_0^t d\tau \frac{\gamma_j(\tau)}{2} e^{i \delta_p \tau} .

    This function calculates, for each time :math:`t_i`, the contribution to the displacement of
    mode :math:`p` from the ion :math:`j`, namely :math:`\eta_{pj}\alpha_{pj}(t_i)`. You can
    calculate the state-dependent displacement for the mode :math:`p` by summing over the
    contributions from all ions. That is, using the displacement superoperator
    :math:`\mathcal{D}_p`, the displacement in phase space for mode :math:`p` at time
    :math:`t_i` is:

    .. math::
        \mathcal{D}_p \left(\sum_{j = 1}^N \sigma_{x, j}\eta_{pj}\alpha_{pj}(t_i) \right) .

    References
    ----------
    .. [1] `C. D. B. Bentley, H. Ball, M. J. Biercuk, A. R. R. Carvalho,
            M. R. Hush, and H. J. Slatyer,
            Adv. Quantum Technol. 3, 2000044 (2020).
            <https://doi.org/10.1002/qute.202000044>`_

    Examples
    --------
    Refer to the `How to optimize error-robust Mølmer–Sørensen gates for trapped ions
    <https://docs.q-ctrl.com/boulder-opal/legacy/user-guides/how-to-optimize-error-robust-molmer-sorensen
    -gates-for-trapped-ions>`_ user guide to find how to use this and related nodes.
    """

    name = "ms_displacements"
    args = [
        forge.arg("drives", type=List[Pwc]),
        forge.arg("lamb_dicke_parameters", type=np.ndarray),
        forge.arg("relative_detunings", type=np.ndarray),
        forge.arg(
            "sample_times", type=Optional[Union[list, tuple, np.ndarray]], default=None
        ),
    ]
    rtype = Tensor
    categories = [Category.MOLMER_SORENSEN]

    @classmethod
    def create_node_data(cls, _operation, **kwargs):
        drives = kwargs.get("drives")
        sample_times = kwargs.get("sample_times")
        lamb_dicke_parameters = kwargs.get("lamb_dicke_parameters")
        relative_detunings = kwargs.get("relative_detunings")
        check_argument_iterable(drives, "drives")
        check_argument(
            len(drives) > 0, "At least one drive must be provided.", {"drives": drives}
        )
        check_argument(
            all(isinstance(drive, Pwc) for drive in drives),
            "Each of the drives must be a Pwc.",
            {"drives": drives},
        )
        check_argument(
            all(len(drive.values.shape) == 1 for drive in drives),
            "The value of each drive must be 1D.",
            {"drives": drives},
        )
        ion_count = len(drives)
        shape = (3, ion_count, ion_count)
        validate_ms_shapes(
            ion_count=ion_count,
            ld_values=lamb_dicke_parameters,
            ld_name="lamb_dicke_parameters",
            rd_values=relative_detunings,
            rd_name="relative_detunings",
        )
        if sample_times is not None:
            sample_times = np.asarray(sample_times)
            check_sample_times_with_bounds(
                sample_times, "sample_times", drives[0], "drives[0]"
            )
            time_count = len(sample_times)
            shape = (time_count,) + tuple(shape)
        return Tensor(_operation, shape=shape)


class MsInfidelity(Node):
    r"""
    Calculate the final operational infidelity of the Mølmer–Sørensen gate.

    This function calculates the operational infidelity with respect to the target phases
    that you specify in the `target_phases` array. It can use the tensors returned from
    :func:`ms_phases` and :func:`ms_displacements` to calculate the infidelity tensor.

    Parameters
    ----------
    phases : np.ndarray(real) or Tensor(real)
        Acquired phases :math:`\{\Phi_{kl}\}` for all ion pairs with shape ``(N, N)`` without time
        samples or ``(T, N, N)``, where ``T`` is the number of samples and ``N`` is the
        number of ions. For each sample the `phases` array must be a strictly lower
        triangular matrix.
    displacements : np.ndarray(complex) or Tensor(complex)
        Motional displacements :math:`\{\eta_{jkl} \alpha_{jkl}\}` in phase-space with shape
        ``(3, N, N)`` without time samples or ``(T, 3, N, N)``, where ``T`` is the number
        of samples, ``3`` is the number of spatial axes, and ``N`` is the number of ions
        that is equal to the number of modes along an axis. The first dimension :math:`j` indicates
        the axis, the second dimension :math:`k` indicates the mode number along the axis,
        and the third dimension :math:`l` indicates the ion.
    target_phases : np.ndarray
        2D array containing target relative phases :math:`\{\psi_{kl}\}` between ion pairs.
        For ions :math:`k` and :math:`l`, with :math:`k > l`, the total relative phase target is
        the :math:`(k, l)`-th element.
        The `target_phases` must be a strictly lower triangular matrix.
    mean_phonon_numbers : np.ndarray or None, optional
        2D array with shape ``(3, N)`` of positive real numbers for each motional mode
        which corresponds to the mean phonon occupation :math:`\{\bar{n}_{jk}\}` of the given
        mode, where ``3`` is the number of spatial axes and ``N`` is the number of ions.
        If not provided, :math:`\bar{n}_{jk} = 0`, meaning no occupation of each mode.
    name : str or None, optional
        The name of the node.

    Returns
    -------
    Tensor(real)
        A scalar or 1D tensor of infidelities with shape ``(T,)`` where ``T`` is
        the number of samples and one infidelity value per sample.

    See Also
    --------
    ms_dephasing_robust_cost : Cost for robust optimization of a Mølmer–Sørensen gate.
    ms_displacements : Displacements for each mode/ion combination.
    ms_phases : Relative phases for all pairs of ions.

    Notes
    -----
    The infidelity is calculated according to [1]_

    .. math::
        1 - \mathcal{F}_\mathrm{av} = 1 - \left| \left( \prod_{\substack{k=1 \\ l<k}}^N \cos (
            \Phi_{kl} - \psi_{kl}) \right)
            \left( 1 - \sum_{j=1}^3 \sum_{k,l=1}^N \left[ |\eta_{jkl}|^2
            |\alpha_{jkl}|^2 \left(\bar{n}_{jk}+\frac{1}{2} \right) \right] \right) \right|^2 ,

    which assumes that the displacements :math:`\alpha_{jkl}` are
    small and eliminates terms of the fourth or higher order in them.

    References
    ----------
    .. [1] `C. D. B. Bentley, H. Ball, M. J. Biercuk, A. R. R. Carvalho,
            M. R. Hush, and H. J. Slatyer,
            Adv. Quantum Technol. 3, 2000044 (2020).
            <https://doi.org/10.1002/qute.202000044>`_

    Examples
    --------
    Refer to the `How to optimize error-robust Mølmer–Sørensen gates for trapped ions
    <https://docs.q-ctrl.com/boulder-opal/legacy/user-guides/how-to-optimize-error-robust-molmer-
    sorensen-gates-for-trapped-ions>`_ user guide to find how to use this and related nodes.
    """

    name = "ms_infidelity"
    args = [
        forge.arg("phases", type=TensorLike),
        forge.arg("displacements", type=TensorLike),
        forge.arg("target_phases", type=np.ndarray),
        forge.arg("mean_phonon_numbers", type=Optional[np.ndarray], default=None),
    ]
    rtype = Tensor
    categories = [Category.MOLMER_SORENSEN]

    @classmethod
    def create_node_data(cls, _operation, **kwargs):
        phases = kwargs.get("phases")
        displacements = kwargs.get("displacements")
        target_phases = kwargs.get("target_phases")
        mean_phonon_numbers = kwargs.get("mean_phonon_numbers")
        check_numeric_numpy_array(phases, "phases")
        check_numeric_numpy_array(displacements, "displacements")
        check_numeric_numpy_array(target_phases, "target_phases")
        check_numeric_numpy_array(mean_phonon_numbers, "mean_phonon_numbers")
        phases_shape = validate_shape(phases, "phases")
        displacements_shape = validate_shape(displacements, "displacements")
        target_shape = validate_shape(target_phases, "target_phases")
        ion_count = target_shape[-1]
        check_argument(
            phases_shape[-2:] == (ion_count, ion_count),
            "The shape of phases must be (ion_count, ion_count) or"
            " (sample_count, ion_count, ion_count).",
            {"phases": phases},
            extras={"ion_count": ion_count, "phases.shape": phases_shape},
        )
        check_argument(
            len(phases_shape) <= 3,
            "The shape of phases must have at most 3 dimensions.",
            {"phases": phases},
            extras={"phases.shape": phases_shape},
        )
        check_argument(
            displacements_shape[-3:] == (3, ion_count, ion_count),
            "The shape of displacements must be (3, ion_count, ion_count) or"
            " (sample_count, 3, ion_count, ion_count).",
            {"displacements": displacements},
            extras={"ion_count": ion_count, "displacements.shape": displacements_shape},
        )
        check_argument(
            phases_shape[:-2] == displacements_shape[:-3],
            "If the shape of phases is (sample_count, ion_count, ion_count), then"
            " the shape of displacements must be (sample_count, 3, ion_count, ion_count).",
            {"phases": phases, "displacements": displacements},
            extras={
                "phases.shape": phases_shape,
                "displacements.shape": displacements_shape,
            },
        )
        check_argument(
            target_shape == (ion_count, ion_count),
            "The shape of target_phases must be (ion_count, ion_count).",
            {"target_phases": target_phases},
            extras={"ion_count": ion_count, "target_phases.shape": target_shape},
        )
        check_argument(
            np.allclose(target_phases, np.tril(target_phases, k=-1)),
            "The target_phases matrix must be strictly lower-triangular.",
            {"target_phases": target_phases},
        )
        if mean_phonon_numbers is not None:
            phonon_shape = validate_shape(mean_phonon_numbers, "mean_phonon_numbers")
            check_argument(
                phonon_shape == (3, ion_count),
                "The shape of mean_phonon_numbers must be (3, ion_count).",
                {"mean_phonon_numbers": mean_phonon_numbers},
                extras={
                    "ion_count": ion_count,
                    "mean_phonon_number.shape": phonon_shape,
                },
            )
        shape = phases_shape[:-2]
        return Tensor(_operation, shape=shape)


class MsDephasingRobustCost(Node):
    r"""
    Calculate the cost for robust optimization of a Mølmer–Sørensen gate.

    Add the tensor that this function returns to the infidelity of your
    target operation to obtain a cost that you can use to create a
    Mølmer–Sørensen gate that is robust against dephasing noise. You can
    further multiply the robust cost by a scaling factor to weigh how much
    importance you give to the robustness compared to the original cost.

    Parameters
    ----------
    drives : list[Pwc(1D, complex)]
        The list of piecewise-constant drives :math:`\{\gamma_j\}`. The
        number of drives must be the same as the number of ions :math:`N`.
        Drive values must be one-dimensional arrays and in rad/s. Drive durations must be in
        seconds. All drives must have the same total duration, but they can
        have different numbers of segments.
    lamb_dicke_parameters : np.ndarray
        A ``(3, N, N)`` :math:`\{ \eta_{jkn} \}` array of parameters
        specifying the laser-ion coupling strength, where :math:`N` equals
        the number of ions. The first dimension :math:`j` indicates the
        axis, the second dimension :math:`k` indicates the collective mode
        number, and the third dimension :math:`n` indicates the ion.
    relative_detunings : np.ndarray
        The 2D array :math:`\{\delta_{jk} = \nu_{jk} - \delta\}` specifying
        the difference (in Hz) between each motional mode frequency
        :math:`\nu_{jk}` and the laser detuning :math:`\delta` (the
        detuning from the qubit transition frequency). Its shape must be
        ``(3, N)`` where the first dimension :math:`j` indicates the axis
        and the second dimension :math:`k` indicates the collective mode
        number.
    name : str or None, optional
        The name of the node.

    Returns
    -------
    Tensor(scalar, real)
        The cost term that you can use to optimize a Mølmer–Sørensen gate
        that is robust against dephasing noise. The cost is the sum of the
        square moduli of the time-averaged positions of the phase-space
        trajectories, weighted by the corresponding Lamb–Dicke parameters.

    See Also
    --------
    :func:`~qctrl.dynamic.namespaces.FunctionNamespace.calculate_ion_chain_properties` :
        Function to calculate the properties of an ion chain.
    ms_infidelity : Final operational infidelity of a Mølmer–Sørensen gate.

    Notes
    -----
    You can construct a Mølmer–Sørensen gate that is robust against
    dephasing noise by a combination of minimizing the time-averaged
    positions of the phase-space trajectories and imposing a symmetry in
    each ion's drive [1]_.

    The displacement of the :math:`j`-th ion in the :math:`p`-th mode of
    oscillation is the following [2]_:

    .. math::
        \alpha_{pj}(t) = \int_0^t d\tau \frac{\gamma_j(\tau)}{2}
        e^{i \delta_p \tau} .

    where the axis dimension and the collective mode dimension are combined
    into a single index :math:`p` for simplicity. For a gate of duration
    :math:`t_\text{gate}`, the time-averaged position is:

    .. math::
        \langle \alpha_{pj} \rangle = \frac{1}{t_\text{gate}}
        \int_0^{t_\text{gate}} \alpha_{pj}(t) \mathrm{d} t .

    This function returns the sum of the square moduli of the time-averaged
    positions multiplied by the corresponding Lamb–Dicke parameters. These
    parameters weight the time-averaged positions in the same way that the
    :math:`\alpha_{pj}(t)` are weighted in the formula for the infidelity
    of a Mølmer–Sørensen gate.

    In other words, the robust cost that this function returns is:

    .. math::
        C_\text{robust} = \sum_{p,j} \left| \eta_{pj} \langle \alpha_{pj}
        \rangle \right|^2.

    You can add this to the infidelity with the respect to the target gate
    to create the cost function that optimizes a gate that is also robust
    against dephasing. You can further multiply :math:`C_\text{robust}` by
    a scaling factor to weigh how much importance you give to robustness.

    References
    ----------
    .. [1] `A. R. Milne, C. L. Edmunds, C. Hempel, F. Roy, S. Mavadia,
            and M. J. Biercuk,
            Phys. Rev. Appl. 13, 024022 (2020).
            <https://doi.org/10.1103/PhysRevApplied.13.024022>`_
    .. [2] `C. D. B. Bentley, H. Ball, M. J. Biercuk, A. R. R. Carvalho,
            M. R. Hush, and H. J. Slatyer,
            Adv. Quantum Technol. 3, 2000044 (2020).
            <https://doi.org/10.1002/qute.202000044>`_

    Examples
    --------
    Refer to the `How to optimize error-robust Mølmer–Sørensen gates for trapped ions
    <https://docs.q-ctrl.com/boulder-opal/legacy/user-guides/how-to-optimize-error-robust-molmer-
    sorensen-gates-for-trapped-ions>`_ user guide to find how to use this and related nodes.
    """

    name = "ms_dephasing_robust_cost"
    args = [
        forge.arg("drives", type=List[Pwc]),
        forge.arg("lamb_dicke_parameters", type=np.ndarray),
        forge.arg("relative_detunings", type=np.ndarray),
    ]
    rtype = Tensor
    categories = [Category.MOLMER_SORENSEN]

    @classmethod
    def create_node_data(cls, _operation, **kwargs):
        drives = kwargs.get("drives")
        lamb_dicke_parameters = kwargs.get("lamb_dicke_parameters")
        relative_detunings = kwargs.get("relative_detunings")
        check_argument_iterable(drives, "drives")
        check_argument(
            len(drives) > 0, "At least one drive must be provided.", {"drives": drives}
        )
        check_argument(
            all(isinstance(drive, Pwc) for drive in drives),
            "Each of the drives must be a Pwc.",
            {"drives": drives},
        )
        check_argument(
            all(len(drive.values.shape) == 1 for drive in drives),
            "The value of each drive must be 1D.",
            {"drives": drives},
        )
        ion_count = len(drives)
        validate_ms_shapes(
            ion_count=ion_count,
            ld_values=lamb_dicke_parameters,
            ld_name="lamb_dicke_parameters",
            rd_values=relative_detunings,
            rd_name="relative_detunings",
        )
        return Tensor(_operation, shape=())
