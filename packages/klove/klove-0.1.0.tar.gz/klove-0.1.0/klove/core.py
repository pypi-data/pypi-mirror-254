#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Benjamin Vial
# This file is part of klove
# License: GPLv3
# See the documentation at benvial.gitlab.io/klove


"""Core functions and classes.
"""


__all__ = [
    "Pin",
    "Mass",
    "Resonator",
    "ConstantStrength",
    "Beam",
    "ElasticPlate",
    "DiffractionSimulation",
    "ScatteringSimulation",
    "BandsSimulation",
]


from abc import ABC, abstractmethod
from dataclasses import dataclass

from . import backend as bk
from .eig import nonlinear_eigensolver
from .special import (
    dgreens_function_dk,
    greens_function,
    greens_function_cartesian,
    radial_coordinates,
)

_BIG = 1e12


class Scatterer(ABC):
    """Base class representing a scatterer."""

    @abstractmethod
    def strength(self):
        pass

    @abstractmethod
    def dstrength_domega(self):
        pass


@dataclass
class Pin(Scatterer):
    """Class representing a pin.

    Parameters
    ----------
    position : tuple
        The position of the pin on the plate.

    """

    position: tuple  #: The position

    def strength(self, omega) -> float:
        """Strength function of frequency `omega`"""
        # t_alpha * D in [Torrent2013]
        return _BIG

    def dstrength_domega(self, omega) -> float:
        """Derivative of strength function w.r.t. `omega`"""
        return 0


@dataclass
class Mass(Scatterer):
    """Class representing a mass.

    Parameters
    ----------
    mass : float
        Value of the mass.
    position : tuple
        The position of the mass on the plate.

    """

    mass: float
    position: tuple

    def strength(self, omega) -> float:
        """Strength function of frequency `omega`"""
        # t_alpha * D in [Torrent2013]
        return self.mass * omega**2

    def dstrength_domega(self, omega) -> float:
        """Derivative of strength function w.r.t. `omega`"""
        return self.mass * omega * 2


@dataclass
class Resonator(Scatterer):
    """Class representing a resonator.

    Parameters
    ----------
    mass : float
        Value of the mass.
    stiffness : float
        Stiffness constant of the spring.
    position : tuple
        The position of the resonator on the plate.

    """

    mass: float
    stiffness: float
    position: tuple

    @property
    def omega_r(self) -> float:
        """Resonant frequency."""
        return (self.stiffness / self.mass) ** 0.5

    def strength(self, omega) -> float:
        """Strength function of frequency `omega`"""
        # t_alpha * D in [Torrent2013]
        return (
            self.mass
            * self.omega_r**2
            * omega**2
            / (self.omega_r**2 - omega**2)
        )

    def dstrength_domega(self, omega) -> float:
        """Derivative of strength function w.r.t. `omega`"""
        return (
            2
            * self.mass
            * self.omega_r**4
            * omega
            / (self.omega_r**2 - omega**2) ** 2
        )


@dataclass
class ConstantStrength:
    """Class representing a scatterer with constant strength.

    Parameters
    ----------
    strength : float
        Value of the strength.
    position : tuple
        The position of the resonator on the plate.

    """

    impedance: float
    position: tuple

    # @property
    def strength(self, omega=0) -> float:
        # t_alpha * D in [Torrent2013]
        return self.impedance

    def dstrength_domega(self, omega=0) -> float:
        """Derivative of strength function w.r.t. `omega`"""
        return 0


@dataclass
class Beam:
    """Class representing a beam.

    Parameters
    ----------
    length : float
        Length of the beam.
    area : float
        Area of the cross section.
    rho : float
        Mass density.
    E : float
        Young's modulus
    position : tuple
        The position of the beam on the plate.

    """

    length: float
    area: float
    rho: float
    E: float
    position: tuple

    def strength(self, omega) -> float:
        """Strength function of frequency `omega`"""
        c = (self.E / self.rho) ** 0.5
        k = omega / c

        return self.rho * self.area * k * c**2 * bk.tan(bk.array(k * self.length))

    def dstrength_domega(self, omega) -> float:
        """Strength function of frequency `omega`"""
        c = (self.E / self.rho) ** 0.5
        k = omega / c
        kl = bk.array(k * self.length)

        return (
            self.rho
            * self.area
            * c**2
            * (bk.tan(kl) + k * self.length / cos(kl) ** 2)
        )


@dataclass
class ElasticPlate:
    """Class representing a thin elastic plate.

    Parameters
    ----------
    h : float
        Thickness
    rho : float
        Mass density
    E : float
        Young's modulus
    nu: float
        Poisson ratio
    """

    h: float  #: thickness
    rho: float  #: mass density
    E: float  #: Young's modulus
    nu: float  #: Poisson ratio

    @property
    def bending_stiffness(self) -> float:
        r"""The bending stiffness of the plate defined
        as :math:`D = E h^3 /(12 (1-\nu^2))`
        """
        return self.E * self.h**3 / (12 * (1 - self.nu**2))

    @property
    def D(self) -> float:
        """Alias for :class:`ElasticPlate.bending_stiffness`"""
        return self.bending_stiffness

    def omega0(self, a) -> float:
        return (self.bending_stiffness / (self.rho * a**2 * self.h)) ** 0.5


class _Simulation:
    def __init__(self, plate, res_array):
        self.plate = plate
        self.res_array = res_array

    @property
    def n_res(self):
        return len(self.res_array)

    def _strength(self, omega, resonator):
        # T_alpha in [Torrent2013]
        k = self.wavenumber(omega)
        # if isinstance(resonator, Pin):
        #     return 1j * 8 * k**2
        t_alpha = resonator.strength(omega) / self.plate.bending_stiffness
        return t_alpha / (1 - 1j * t_alpha / (8 * k**2))

    def _dstrength_domega(self, omega, resonator):
        k = self.wavenumber(omega)
        dk = self.dwavenumber_domega(omega)
        t_alpha = resonator.strength(omega) / self.plate.bending_stiffness
        dt_alpha_domega = (
            resonator.dstrength_domega(omega) / self.plate.bending_stiffness
        )
        Q = t_alpha / (8 * k**2)
        dQ = dt_alpha_domega / (8 * k**2)
        return 16 * k * (k / 2 * dQ - 1j * dk * Q**2) / (1 - 1j * Q) ** 2

    def wavenumber(self, omega):
        """Gives the wavenumber of the bare plate as a function of frequency `omega`

        Parameters
        ----------
        omega : float
            Frequency

        """
        return (
            omega**0.5
            * (self.plate.rho * self.plate.h / self.plate.bending_stiffness) ** 0.25
        )

    def dwavenumber_domega(self, omega):
        """Gives the derivative of the wavenumber with respect to the frequency `omega`

        Parameters
        ----------
        omega : float
            Frequency

        """
        k = self.wavenumber(omega)
        return (
            omega
            / (2 * k**3)
            * (self.plate.rho * self.plate.h / self.plate.bending_stiffness)
        )

    def plane_wave(self, x, y, omega, angle):
        """A plane wave

        Parameters
        ----------
        x : array
            x coordinates
        y : array
            y coordinates
        omega : float
            Frequency
        angle : float
            Angle in radians

        Returns
        -------
        array
            The plane wave field
        """
        k = self.wavenumber(omega)
        angle = bk.array(angle)
        return bk.exp(1j * k * (bk.cos(angle) * x + bk.sin(angle) * y))

    def point_source(self, x, y, omega, position):
        """A point source.

        Parameters
        ----------
        x : array
            x coordinates
        y : array
            y coordinates
        omega : float
            Frequency
        position : tuple
            Position of the source.


        Returns
        -------
        array
            The field from a line source
        """
        k = self.wavenumber(omega)
        xs, ys = position
        r = radial_coordinates(x - xs, y - ys)
        return greens_function(k, r)


class ScatteringSimulation(_Simulation):
    """Class to run a scattering simulation.

    Parameters
    ----------
    plate : :class:`ElasticPlate`
        The plate
    res_array : array of :class:`Pin`, :class:`Mass` or :class:`Resonator`
        An array containing the scatterers, it can be a mixture of pins, masses or resonators.
    alternative : bool
        Use an alternative formulation to solve for the scattering coefficients.

    """

    def __init__(self, plate, res_array, alternative=False):
        super().__init__(plate, res_array)

        self.alternative = alternative

        dists = bk.array(bk.zeros((self.n_res, self.n_res), dtype=bk.float64))
        for alpha, res_alpha in enumerate(self.res_array):
            xalpha, yalpha = res_alpha.position
            for beta, res_beta in enumerate(self.res_array):
                xbeta, ybeta = res_beta.position
                dists[alpha, beta] = radial_coordinates(xalpha - xbeta, yalpha - ybeta)

        self._dr = dists

    def build_rhs(self, phi0, omega, *args, **kwargs):
        phi0_vec = bk.array(bk.zeros((self.n_res), dtype=bk.complex128))
        for alpha, res_alpha in enumerate(self.res_array):
            xalpha, yalpha = res_alpha.position
            phi0_vec[alpha] = phi0(xalpha, yalpha, omega, *args, **kwargs)

        return phi0_vec

    def build_matrix(self, omega):
        omega = bk.array(omega)
        k = self.wavenumber(omega)
        matrix = bk.array(
            bk.zeros((self.n_res, self.n_res, *omega.shape), dtype=bk.complex128)
        )
        for alpha, res_alpha in enumerate(self.res_array):
            for beta, res_beta in enumerate(self.res_array):
                delta = 1 if alpha == beta else 0
                dr = self._dr[alpha, beta]
                G0 = greens_function(k, dr)
                if self.alternative:
                    t_beta = res_beta.strength(omega) / self.plate.D
                    mat = delta / t_beta - G0
                else:
                    T_beta = self._strength(omega, res_beta)
                    mat = delta - (1 - delta) * T_beta * G0
                matrix[alpha, beta] = mat
        return matrix

    def build_matrix_derivative(self, omega):
        omega = bk.array(omega)
        k = self.wavenumber(omega)
        matrix = bk.array(
            bk.zeros((self.n_res, self.n_res, *omega.shape), dtype=bk.complex128)
        )
        for alpha, res_alpha in enumerate(self.res_array):
            for beta, res_beta in enumerate(self.res_array):
                delta = 1 if alpha == beta else 0
                dr = self._dr[alpha, beta]
                dG0 = dgreens_function_dk(k, dr) * self.dwavenumber_domega(omega)

                if self.alternative:
                    t_beta = res_beta.strength(omega) / self.plate.D
                    dt_beta = res_beta.dstrength_domega(omega) / self.plate.D
                    mat = -dt_beta / t_beta**2 * delta - dG0
                else:
                    dT_beta = self._dstrength_domega(omega, res_beta)
                    G0 = greens_function(k, dr)
                    T_beta = self._strength(omega, res_beta)
                    mat = -(1 - delta) * (dT_beta * G0 + T_beta * dG0)
                matrix[alpha, beta] = mat
        return matrix

    # def get_eigenvector(self, omega):
    #     M = self.build_matrix(omega)
    #     return null(M)

    def solve(self, incident, omega, *args, **kwargs):
        """Solve the multiple scattering problem

        Parameters
        ----------
        incident : callable
            The incident field. Signature should be ``incident(x, y, omega, *args, **kwargs)``.
        omega: float
            Frequency
        Returns
        -------
        array
            The solution vector
        """
        matrix = self.build_matrix(omega)
        rhs = self.build_rhs(incident, omega, *args, **kwargs)
        return bk.linalg.solve(matrix, rhs)

    def _get_field(
        self, x, y, incident, kernel, solution_vector, omega, *args, **kwargs
    ):
        k = self.wavenumber(omega)
        if incident is None:
            W = 0
        else:
            W = incident(x, y, omega, *args, **kwargs)
        for alpha, res_alpha in enumerate(self.res_array):
            xalpha, yalpha = res_alpha.position
            G0 = kernel(k, x - xalpha, y - yalpha)
            coeff = 1 if self.alternative else self._strength(omega, res_alpha)
            W += coeff * solution_vector[alpha] * G0
        return W

    def get_field(self, x, y, incident, solution_vector, omega, *args, **kwargs):
        """Get the total field.

        Parameters
        ----------
        x : array
            x coordinates
        y : array
            y coordinates
        incident : callable
            The incident field. Signature should be ``incident(x, y, omega, *args, **kwargs)``.
        solution_vector: array
            The solution vector as returned by :class:`ScatteringSimulation.solve`
        omega: float or complex
            Frequency

        Returns
        -------
        array
            The total field
        """
        return self._get_field(
            x,
            y,
            incident,
            greens_function_cartesian,
            solution_vector,
            omega,
            *args,
            **kwargs
        )

    def get_scattered_field(self, x, y, solution_vector, omega):
        """Get the scattered field.

        Parameters
        ----------
        x : array
            x coordinates
        y : array
            y coordinates
        solution_vector: array
            The solution vector as returned by :class:`ScatteringSimulation.solve`
        omega: float or complex
            Frequency


        Returns
        -------
        array
            The scattered field
        """
        return self._get_field(
            x, y, None, greens_function_cartesian, solution_vector, omega
        )

    def eigensolve(self, *args, **kwargs):
        return nonlinear_eigensolver(self, *args, **kwargs)

    def get_mode(self, x, y, eigenvector, eigenvalue):
        return self.get_scattered_field(x, y, eigenvector, eigenvalue)

    def get_strength_poles(self):
        singularity_Talpha = []
        plate = self.plate
        for res in self.res_array:
            q = (
                1
                / 16
                * (res.mass * res.stiffness / (plate.rho * plate.h * plate.D)) ** 0.5
                + 0j
            )
            pole = res.omega_r * (-1j * q + (1 - q**2 + 0j) ** 0.5)
            singularity_Talpha.append(pole)
            pole = res.omega_r * (-1j * q - (1 - q**2) ** 0.5)
            singularity_Talpha.append(pole)
        return bk.array(singularity_Talpha)

    # FAR FIELD QUANTITIES

    def get_far_field_radiation(self, phi_n, omega, angle):
        """
        Compute the far field radiation pattern.

        Equation (12) in :cite:p:`marti2023bound`

        Parameters
        ----------
        phi_n : array
            The scattering coefficients at the position of the scatterers by using
            the second definition of the M matrix
        omega : float
            The frequency
        angle: array
            Angle(s) in radian

        Returns
        -------
        F : array
             The far field radiation pattern
        """

        k = self.wavenumber(omega)

        F = bk.zeros(len(angle), dtype=bk.complex64)
        for thetaIterator, theta in enumerate(angle):
            for alpha, res_alpha in enumerate(self.res_array):
                xalpha, yalpha = res_alpha.position
                angleScatterer = bk.arctan2(yalpha, xalpha)
                moduleDistance = bk.sqrt(xalpha**2 + yalpha**2)
                F[thetaIterator] += phi_n[alpha] * bk.exp(
                    -1j * k * moduleDistance * bk.cos(theta - angleScatterer)
                )
        return F

    def get_scattering_cross_section(self, phi_n, omega):
        """Compute the scattering cross section of the cluster in the farfield.

        Equation (A6b) in :cite:p:`packo2021metaclusters`

        Parameters
        ----------
        phi_n : array
            The scattering coefficients at the position of the scatterers by using
            the second definition of the M matrix#
        omega : float
            The frequency

        Returns
        -------
        sigma_sc : float
             Scattering cross section
        """
        k = self.wavenumber(omega)
        sigma_sc = (
            1 / (8 * self.plate.bending_stiffness * k**2) * bk.sum(bk.abs(phi_n) ** 2)
        )
        return sigma_sc

    def get_absorption_cross_section(self, phi_n, omega, sum=True):
        """Compute the absorption cross section of the cluster in the farfield.

        Equation (A6c) in :cite:p:`packo2021metaclusters`

        Parameters
        ----------
        phi_n : array
            The scattering coefficients at the position of the scatterers by using
            the second definition of the M matrix#
        omega : float
            The frequency
        sum: bool
            Wether to return the sum of all resonator contributions

        Returns
        -------
        sigma_abs : float or array
             Absorption cross section (total if sum=True, else array with value for each resonator)
        """
        sigma_abs = bk.zeros(self.n_res)
        for resIterator, res in enumerate(self.res_array):
            if self.alternative == False:
                acs = bk.imag(res.strength(omega)) * bk.abs(phi_n) ** 2
            else:
                acs = (
                    bk.imag(res.strength(omega))
                    * bk.abs(phi_n / self._strength(omega, res)) ** 2
                )
            sigma_abs[resIterator] = acs

        if sum:
            return bk.sum(sigma_abs)
        return sigma_abs

    def get_extintion_cross_section(self, phi_n, omega):
        """Compute the extintion cross section of the cluster in the farfield

        Equation (A6a) in :cite:p:`packo2021metaclusters`

        Parameters
        ----------
        phi_n : array
            The scattering coefficients at the position of the scatterers by using
            the second definition of the M matrix#
        omega : float
            The frequency

        Returns
        -------
        sigma_ext : float
             Extintion cross section
        """
        k = self.wavenumber(omega)
        F = self.get_far_field_radiation(phi_n, omega, [0])
        return bk.imag(F[0])

    def get_energy_efficiency(self, phi_n, omega):
        """
        Equation (17) in :cite:p:`packo2021metaclusters`
        """
        sigma_sc = self.get_scattering_cross_section(self, phi_n, omega)
        sigma_abs = self.get_extintion_cross_section(self, phi_n, omega)
        return sigma_sc / sigma_abs

    def get_multiplicities(self, eigenvalues, M=None, tol=1e-6):
        if M is None:
            M = [self.build_matrix(omega) for omega in eigenvalues]
        multiplicities = [self.n_res - bk.linalg.matrix_rank(m, tol=tol) for m in M]
        return multiplicities

    def update_eig(self, evs, eigenvectors, multiplicities):
        Nmodes = len(evs)
        eigvals = []
        eigmodes = []
        for i in range(Nmodes):
            mult = multiplicities[i]
            if mult > 1:
                # vs = kl.eig.null(M[i], mult=mult)
                v = eigenvectors[:, i]
                # _A = [v for l in range(mult)]
                # A = bk.vstack(_A).T
                # vs = kl.eig.gram_schmidt(A)
                # vs = [_.flatten() for _ in vs]
                vs = bk.vstack([v] * mult)
                for jm in range(mult):
                    eigvals.append(evs[i])
                    # eigmodes.append(vs[jm])
                    eigmodes.append(bk.roll(vs[jm], 2 * jm))
            else:
                eigvals.append(evs[i])
                eigmodes.append(eigenvectors[:, i])

        eigenvectors = bk.stack(eigmodes).T
        evs = bk.array(eigvals)
        return evs, eigenvectors


class BandsSimulation(_Simulation):
    """Class to compute phononic bands.

    Parameters
    ----------
    plate : :class:`ElasticPlate`
        The plate
    res_array : list
        Array of scatterers. This can be :class:`Pin`, :class:`Mass` or :class:`Resonator` or a mix of those.
    lattice_vectors : tuple of tuples
        The two vectors `(v1x, v1y), (v2x, v2y)` defining the lattice.

    """

    def __init__(self, plate, res_array, lattice_vectors):
        super().__init__(plate, res_array)

        self.lattice_vectors = bk.array(
            lattice_vectors, dtype=bk.float64
        )  #: The lattice vectors
        self.reciprocal = 2 * bk.pi * bk.linalg.inv(self.lattice_vectors).T

        self.a = min([bk.linalg.norm(v) for v in self.lattice_vectors])
        self.omega0 = plate.omega0(self.a)
        v0, v1 = self.lattice_vectors
        self.area = bk.abs(v0[0] * v1[1] - v0[1] * v1[0])

    def _reciprocal_sum(self, Omega, K, alpha, beta, M):
        out = 0
        for m in range(-M, M + 1):
            for n in range(-M, M + 1):
                G = m * self.reciprocal[0] + n * self.reciprocal[1]
                Rab = bk.array(self.res_array[beta].position) - bk.array(
                    self.res_array[alpha].position
                )
                out += bk.exp(-1j * G @ Rab) / (
                    bk.linalg.norm(K + G) ** 4 * self.a**4 - Omega**2 * self.a**2
                )
        return out

    def _gamma(self, beta):
        return self.res_array[beta].mass / (self.plate.rho * self.plate.h * self.area)

    def _matrix_element(self, Omega, K, alpha, beta, M):
        S = self._reciprocal_sum(Omega, K, alpha, beta, M)
        Omega_beta = self.res_array[beta].omega_r / self.omega0
        return (
            self._gamma(beta)
            * Omega**2
            * self.a**2
            / (1 - Omega**2 / Omega_beta**2)
        ) * S

    def _build_matrix(self, Omega, K, M):
        matrix = bk.array(bk.zeros((self.n_res, self.n_res), dtype=bk.complex128))
        for alpha in range(self.n_res):
            for beta in range(self.n_res):
                matrix[alpha, beta] = self._matrix_element(Omega, K, alpha, beta, M)
        return bk.eye(self.n_res) - matrix

    def _getP(self, alpha, M):
        P = []
        for m in range(-M, M + 1):
            for n in range(-M, M + 1):
                G = bk.array(
                    m * self.reciprocal[0] + n * self.reciprocal[1], dtype=bk.float64
                )
                Ra = bk.array(self.res_array[alpha].position, dtype=bk.float64)
                ph = bk.exp(1j * (Ra @ G))
                P.append(ph)
        return bk.array(P) if P == [] else bk.stack(P)

    def _getK(self, K, M):
        K = bk.array(K)
        P = []
        for m in range(-M, M + 1):
            for n in range(-M, M + 1):
                G = bk.array(
                    m * self.reciprocal[0] + n * self.reciprocal[1], dtype=bk.float64
                )
                P.append(bk.linalg.norm(K + G) ** 4)
        return bk.diag(bk.array(P, dtype=bk.float64))

    def eigensolve(self, k, Npw, return_modes=True, hermitian=False):
        """Solve the eigenvalue problem.

        Parameters
        ----------
        k : tuple
            Wavevector
        Npw : int
            Number of plane waves in each direction (from `-Npw` to `Npw`)
        return_modes : bool, optional
            Compute eigenmodes?
        hermitian : bool, optional
            Is the problem Hermitian?

        Returns
        -------
        array or tuple of arrays
            Eigenvalues (and eigenmodes if `return_modes` is `True`)
        """
        N = (2 * Npw + 1) ** 2

        Ps = []
        for alpha in range(self.n_res):
            P = self._getP(alpha, Npw)
            Ps.append(P)
        Ps = bk.array(Ps) if Ps == [] else bk.stack(Ps)

        Kmat0 = self._getK(k, Npw)

        Nmat = self.n_res + N
        Kmat = bk.zeros((Nmat, Nmat), dtype=bk.complex128)
        Q = 0
        stiffnesses = []
        masses = []
        gamma_inf = _BIG
        for alpha, res in enumerate(self.res_array):
            Omega_inf_square = _BIG if isinstance(res, Mass) else 1
            mass = (
                self.plate.rho * self.plate.h * self.area * gamma_inf
                if isinstance(res, Pin)
                else res.mass
            )
            stiffness = (
                res.stiffness
                if isinstance(res, Resonator)
                else Omega_inf_square
                / self.plate.D
                * mass
                / (self.plate.rho * self.plate.h)
            )

            stiffnesses.append(stiffness)
            masses.append(mass)
            P = bk.stack([Ps[alpha]]).T
            Q += P @ bk.conj(P).T * stiffness
            Kmat[N + alpha, :N] = -stiffness * bk.conj(Ps[alpha])
            Kmat[:N, N + alpha] = -stiffness * (Ps[alpha])

        Kmat[:N, :N] = self.plate.bending_stiffness * self.area * Kmat0 + Q
        Kmat[N:, N:] = bk.diag(bk.array(stiffnesses, dtype=bk.float64))

        Mmat = bk.zeros((Nmat), dtype=bk.complex128)
        Mmat[:N] = self.plate.rho * self.plate.h * self.area
        Mmat[N:] = bk.array(masses)

        self.Kmat = Kmat
        self.Mmat = Mmat
        Amat = Kmat / Mmat

        if return_modes:
            eigensolve = bk.linalg.eigh if hermitian else bk.linalg.eig
            eigvals, modes = eigensolve(Amat)
        else:
            eigensolve = bk.linalg.eigvalsh if hermitian else bk.linalg.eigvals
            eigvals = eigensolve(Amat)
        omegans = eigvals**0.5
        isort = bk.argsort(omegans.real)
        if return_modes:
            return omegans[isort], modes[:, isort]
        return omegans[isort]

    def get_field(self, mode_coeffs, x, y):
        """Get the mode field

        Parameters
        ----------
        mode_coeffs : array
            Fourrier coefficients of the mode
        x : array
            x coordinates
        y : array
            y coordinates

        Returns
        -------
        array
            Modal field in real space
        """
        M = int(((len(mode_coeffs) - self.n_res) ** 0.5 - 1) / 2)
        field = 0
        i = 0
        for m in range(-M, M + 1):
            for n in range(-M, M + 1):
                G = m * self.reciprocal[0] + n * self.reciprocal[1]
                kr = G[0] * x + G[1] * y
                field += mode_coeffs[i] * bk.exp(-1j * kr)
                i += 1
        return field


class DiffractionSimulation(_Simulation):
    """Class to run a diffraction simulation.

    Parameters
    ----------
    plate : :class:`ElasticPlate`
        The plate
    res_array : array of :class:`Pin`, :class:`Mass` or :class:`Resonator`
        An array containing the scatterers, it can be a mixture of pins, masses or resonators.
    period : float
        Period of the grating
    nh : int
        Number of harmonics such that the calculations use orders [-nh,...0, ...,nh]

    """

    def __init__(self, plate, res_array, period, nh=0):
        super().__init__(plate, res_array)

        for res in self.res_array:
            if not (0 < res.position[0] < period):
                raise ValueError("Resonator x position must be between 0 and period")

        self.period = period
        self.nh = nh

    @property
    def harmonics(self):
        return bk.array(range(-self.nh, self.nh + 1))

    def _G0(self, k):
        return 1 / (4 * self.period * k**2)

    def _g(self, n):
        return 2 * n * bk.pi / self.period

    def _get_xis(self, k, kx, n):
        qn = kx + self._g(n)
        xip = (qn**2 + k**2 + 0j) ** 0.5
        xim = (qn**2 - k**2 + 0j) ** 0.5
        return xip.conj(), xim.conj()

    def is_propagative(self, k, kx, n):
        return bk.abs(kx + self._g(n)) < k

    def _lattice_sum(self, k, kx, xa, ya, xb, yb, harmonics=None):
        harmonics = harmonics or self.harmonics

        dx = xa - xb
        abs_dy = bk.abs(ya - yb)
        lat_sum = 0
        for n in harmonics:
            xip, xim = self._get_xis(k, kx, n)
            t = bk.exp(-xim * abs_dy) / xim
            t -= bk.exp(-xip * abs_dy) / xip
            t *= bk.exp(1j * (kx + self._g(n)) * dx)
            lat_sum += t
        return lat_sum

    def build_matrix(self, omega, kx):
        omega = bk.array(omega)
        k = self.wavenumber(omega)
        G0 = self._G0(k)
        matrix = bk.array(
            bk.zeros((self.n_res, self.n_res, *omega.shape), dtype=bk.complex128)
        )
        for alpha, res_alpha in enumerate(self.res_array):
            for beta, res_beta in enumerate(self.res_array):
                delta = 1 if alpha == beta else 0
                t_beta = res_beta.strength(omega) / self.plate.D
                chi = G0 * self._lattice_sum(
                    k, kx, *res_alpha.position, *res_beta.position
                )
                matrix[alpha, beta] = delta / t_beta - chi
        return matrix

    def build_rhs(self, omega, angle):
        phi0_vec = bk.array(bk.zeros((self.n_res), dtype=bk.complex128))
        for alpha, res_alpha in enumerate(self.res_array):
            phi0_vec[alpha] = self.plane_wave(*res_alpha.position, omega, angle)

        return phi0_vec

    def solve(self, omega, angle):
        """Solve the diffraction problem

        Parameters
        ----------
        omega: float
            Frequency
        angle: float
            Incident angle (in radians)
        Returns
        -------
        array
            The solution vector
        """
        k = self.wavenumber(omega)
        angle = bk.array(angle)
        kx = k * bk.cos(angle)
        matrix = self.build_matrix(omega, kx)
        rhs = self.build_rhs(omega, angle)
        return bk.linalg.solve(matrix, rhs)

    def _get_field(self, x, y, incident, solution_vector, omega, angle):
        k = self.wavenumber(omega)
        angle = bk.array(angle)
        kx = k * bk.cos(angle)
        G0 = self._G0(k)
        if incident is None:
            W = 0
        else:
            W = incident(x, y, omega, angle)
        for alpha, res_alpha in enumerate(self.res_array):
            chi = G0 * self._lattice_sum(k, kx, x, y, *res_alpha.position)
            W += solution_vector[alpha] * chi
        return W

    def get_field(self, x, y, solution_vector, omega, angle):
        """Get the total field.

        Parameters
        ----------
        x : array
            x coordinates
        y : array
            y coordinates
        solution_vector: array
            The solution vector as returned by :class:`ScatteringSimulation.solve`
        omega: float or complex
            Frequency
        angle: float
            Incident angle (in radians)

        Returns
        -------
        array
            The total field
        """
        return self._get_field(
            x,
            y,
            self.plane_wave,
            solution_vector,
            omega,
            angle,
        )

    def get_scattered_field(self, x, y, solution_vector, omega, angle):
        """Get the scattered field.

        Parameters
        ----------
        x : array
            x coordinates
        y : array
            y coordinates
        solution_vector: array
            The solution vector as returned by :class:`ScatteringSimulation.solve`
        omega: float or complex
            Frequency
        angle: float
            Incident angle (in radians)


        Returns
        -------
        array
            The scattered field
        """
        return self._get_field(
            x,
            y,
            None,
            solution_vector,
            omega,
            angle,
        )

    def orders_angle(self, k, angle, n):
        angle = bk.array(angle)
        return bk.arccos(bk.cos(angle) + 2 * n * bk.pi / (self.period * k))

    @staticmethod
    def _wavevector_orders(k, thetan):
        thetan = bk.array(thetan)
        kx, ky = k * bk.cos(thetan), k * bk.sin(thetan)
        return bk.array([kx, ky]), bk.array([kx, -ky])

    def get_propagative_harmonics(self):
        propa = [self.is_propagative(k, kx, n) for n in self.harmonics]
        propagative = []
        for i, prop in enumerate(propa):
            if prop:
                propagative.append(self.harmonics[i])
        return propagative

    def get_efficiencies(self, sol, omega, angle):
        angle = bk.array(angle)
        k = self.wavenumber(omega)
        kx = k * bk.cos(angle)
        G0 = self._G0(k)

        propa = [self.is_propagative(k, kx, n) for n in self.harmonics]
        t, r, T, R = {}, {}, {}, {}
        sumT = sumR = 0

        for n in self.harmonics:
            if self.is_propagative(k, kx, n):
                thetan = self.orders_angle(k, angle, n)
                cst = 1j * G0 / (k * bk.sin(thetan))
                knp, knm = self._wavevector_orders(k, thetan)
                rn = tn = 0
                for beta, res in enumerate(self.res_array):
                    pos = bk.array(res.position)
                    tn += sol[beta] * bk.exp(-1j * (knp @ pos))
                    rn += sol[beta] * bk.exp(-1j * (knm @ pos))
                rn *= cst
                tn *= cst
                if n == 0:
                    tn += 1

                nrm_ = bk.sin(thetan) / bk.sin(angle)
                Rn = bk.abs(rn) ** 2 * nrm_
                Tn = bk.abs(tn) ** 2 * nrm_

                sumR += Rn
                sumT += Tn

            else:
                rn = tn = Rn = Tn = 0

            key = str(int(n))
            r[key] = rn
            t[key] = tn
            R[key] = Rn
            T[key] = Tn
        Rdict = dict(amplitude=r, energy=R, total=sumR)
        Tdict = dict(amplitude=t, energy=T, total=sumT)
        return Rdict, Tdict

    def get_min_harmonics(self, omega_max, angle, nhmax=100):
        k = self.wavenumber(omega_max)
        angle = bk.array(angle)
        kx = k * bk.cos(angle)
        nh_ = 0
        propa = True

        while propa:
            nh_ += 1
            propa1 = self.is_propagative(k, kx, -nh_)
            propa2 = self.is_propagative(k, kx, nh_)
            propa = propa1 or propa2
            if nh_ > nhmax:
                break
        nh_ -= 1

        return nh_
