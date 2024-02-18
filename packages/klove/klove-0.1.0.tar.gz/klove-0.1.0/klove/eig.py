#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Benjamin Vial
# This file is part of klove
# License: GPLv3
# See the documentation at benvial.gitlab.io/klove

__all__ = ["nonlinear_eigensolver"]

import logging

import matplotlib.pyplot as plt
import scipy.linalg as la
from skimage.feature import peak_local_max

from . import backend as bk
from . import get_backend


def get_residual(M, phi):
    return bk.abs(phi @ M @ phi)


def eig(C, D):
    if get_backend() == "torch":
        invD = bk.linalg.inv(D)
        return bk.linalg.eig(invD @ C)
    return la.eig(C, D)


class ConvergenceError(Exception):
    pass


class EigenvalueError(Exception):
    pass


def null(M, mult=1):
    e, v = bk.linalg.eig(M)
    srt = bk.argsort(bk.abs(e))
    return v[:, srt[0:mult]]


def block(matrices):
    if get_backend() == "torch":
        return bk.cat([bk.cat(m, dim=1) for m in matrices], dim=0)
    return bk.block(matrices)


def _dot(a, b):
    if get_backend() == "torch":
        return bk.matmul(a, b)
    else:
        return bk.dot(a, b)


def eig_newton(
    func,
    lambda_0,
    x_0,
    lambda_tol=1e-8,
    max_iter=20,
    func_gives_der=False,
    G=None,
    args=[],
    weight="rayleigh symmetric",
    y_0=None,
):
    """Solve a nonlinear eigenvalue problem by Newton iteration

    Parameters
    ----------
    func : function
        The function with input `lambda` which returns the matrix
    lambda_0 : complex
        The starting guess for the eigenvalue
    x_0 : ndarray
        The starting guess for the eigenvector
    lambda_tol : float
        The relative tolerance in the eigenvalue for convergence
    max_iter : int
        The maximum number of iterations to perform
    func_gives_der : boolean, optional
        If `True`, then the function also returns the derivative as the second
        returned value. If `False` finite differences will be used instead,
        which will have reduced accuracy
    args : list, optional
        Any additional arguments to be supplied to `func`
    weight : string, optional
        How to perform the weighting of the eigenvector

        'max element' : The element with largest magnitude will be preserved

        'rayleigh' : Rayleigh iteration for Hermitian matrices will be used

        'rayleigh symmetric' : Rayleigh iteration for complex symmetric
        (i.e. non-Hermitian) matrices will be used

        'rayleigh asymmetric' : Rayleigh iteration for general matrices

    y_0 : ndarray, optional
        For 'rayleigh asymmetric weighting', this is required as the initial
        guess for the left eigenvector

    Returns
    -------
    res : dictionary
        A dictionary containing the following members:

        `eigval` : the eigenvalue

        'eigvec' : the eigenvector

        'iter_count' : the number of iterations performed

        'delta_lambda' : the change in the eigenvalue on the final iteration


    See:
    1.  P. Lancaster, Lambda Matrices and Vibrating Systems.
        Oxford: Pergamon, 1966.

    2.  A. Ruhe, “Algorithms for the Nonlinear Eigenvalue Problem,”
        SIAM J. Numer. Anal., vol. 10, no. 4, pp. 674–689, Sep. 1973.

    """

    x_s = x_0
    lambda_s = lambda_0

    if weight.lower() == "rayleigh asymmetric":
        if y_0 is None:
            raise ValueError("Parameter y_0 must be supplied for asymmetric " "case")
        y_s = y_0

    logging.debug("Searching for zeros with eig_newton")
    logging.debug("Starting guess %+.4e %+.4ej" % (lambda_0.real, lambda_0.imag))

    converged = False

    if not func_gives_der:
        # evaluate at an arbitrary nearby starting point to allow finite
        # differences to be taken
        # lambda_sm = lambda_0*(1+10j*lambda_tol)
        step = bk.max(1e-6, lambda_tol * 10)
        step = lambda_tol * 10
        lambda_sm = lambda_0 * (1 + (1 + 1j) * step)
        T_sm = func(lambda_sm, *args)

    for iter_count in range(max_iter):
        if func_gives_der:
            T_s, T_ds = func(lambda_s, *args)
        else:
            T_s = func(lambda_s, *args)
            T_ds = (T_s - T_sm) / (lambda_s - lambda_sm)

        # print(T_ds)
        w = _dot(T_ds, x_s)
        if get_backend() == "torch":
            T_s_lu = bk.linalg.lu_factor(T_s)

            u = bk.linalg.lu_solve(*T_s_lu, bk.stack([w]).T).flatten()

        else:
            T_s_lu = la.lu_factor(T_s)

            u = la.lu_solve(T_s_lu, _dot(T_ds, x_s))

        # if known_vects is supplied, we should take this into account when
        # finding v
        if weight.lower() == "max element":
            v_s = bk.zeros_like(x_s)
            v_s[bk.argmax(bk.abs(x_s))] = 1.0
        # elif weight.lower() == "rayleigh":
        #     v_s = _dot(T_s.T, x_s.conj())
        # elif weight.lower() == "rayleigh symmetric":
        #     v_s = _dot(T_s.T, x_s)
        # elif weight.lower() == "rayleigh asymmetric":
        #     y_s = bk.linalg.lu_solve(T_s_lu, _dot(T_ds.T, y_s), trans=1)

        #     y_s /= bk.sqrt(bk.sum(bk.abs(y_s) ** 2))
        #     v_s = _dot(T_s.T, y_s)
        else:
            raise ValueError("Unknown weighting method %s" % weight)

        delta_lambda_abs = _dot(v_s, x_s) / _dot(v_s, u)

        delta_lambda = bk.abs(delta_lambda_abs / lambda_s)
        converged = delta_lambda < lambda_tol

        if converged:
            break

        lambda_s1 = lambda_s - delta_lambda_abs
        x_s1 = u / bk.sqrt(bk.sum(bk.abs(u) ** 2))

        # update variables for next iteration
        if not func_gives_der:
            lambda_sm = lambda_s
            T_sm = T_s

        lambda_s = lambda_s1
        x_s = x_s1
        logging.debug("%+.4e %+.4ej" % (lambda_s.real, lambda_s.imag))

    if not converged:
        return
        # raise ConvergenceError("maximum iterations reached, no convergence")

    res = {
        "eigval": lambda_s,
        "iter_count": iter_count + 1,
        "delta_lambda": delta_lambda,
    }

    if weight.lower() == "rayleigh asymmetric":
        # Scale both the left and right eigenvector identically first
        y_s /= bk.sqrt(bk.vdot(y_s, y_s) / bk.vdot(x_s, x_s))

        # Then scale both to match the eigenvalue derivative
        dz_ds = _dot(y_s, _dot(T_ds, x_s))
        y_s /= bk.sqrt(dz_ds)
        res["eigvec_left"] = y_s

        x_s /= bk.sqrt(dz_ds)
        res["eigvec"] = x_s

    else:
        # scale the eigenvector so that the eigenvalue derivative is 1
        dz_ds = _dot(x_s, _dot(T_ds, x_s))
        x_s /= bk.sqrt(dz_ds)
        res["eigvec"] = x_s
        res["eigvec_left"] = x_s

    return res


def polyeig(*A):
    """Solve the polynomial eigenvalue problem: (A0 + e A1 +...+  e**p Ap)x=0

    Parameters
    ----------
    A : list of arrays
        The arrays for each power of the polynomial (in increasing order)

    Returns
    -------
    tuple of arrays
        eigenvalues e and eigenvectors x

    """
    if len(A) <= 0:
        raise Exception("Provide at least one matrix")
    for Ai in A:
        if Ai.shape[0] != Ai.shape[1]:
            raise Exception("Matrices must be square")
        if Ai.shape != A[0].shape:
            raise Exception("All matrices must have the same shapes")

    n = A[0].shape[0]
    l = len(A) - 1
    # Assemble matrices for generalized problem
    C = block(
        [[bk.zeros((n * (l - 1), n)), bk.eye(n * (l - 1))], [-bk.column_stack(A[0:-1])]]
    )
    D = block(
        [
            [bk.eye(n * (l - 1)), bk.zeros((n * (l - 1), n))],
            [bk.zeros((n, n * (l - 1))), A[-1]],
        ]
    )
    # Solve generalized eigenvalue problem
    e, X = eig(C, D)
    if bk.all(bk.isreal(e)):
        e = bk.real(e)
    X = X[:n, :]

    # Sort eigenvalues/vectors
    # I = bk.argsort(e)
    # X = X[:,I]
    # e = e[I]

    # Scaling each mode by max
    maxi = bk.max(bk.abs(X), axis=0)

    if get_backend() == "torch":
        maxi = maxi[0]
    X /= bk.tile(maxi, (n, 1))

    return e, X


def nonlinear_eigensolver(
    simu,
    omega0,
    omega1,
    guesses=None,
    weight="max element",
    init_vect="eig",
    strategy="peaks",
    func_gives_der="True",
    lambda_tol=1e-6,
    max_iter=100,
    N_grid=(10, 10),
    N_guess_loc=1,
    Rloc=0.1,
    plot_solver=False,
    peak_ref=10,
    verbose=False,
):
    Nguess_re, Nguess_im = N_grid

    if func_gives_der:

        def func_eig(omega):
            return simu.build_matrix(omega), simu.build_matrix_derivative(omega)

    else:

        def func_eig(omega):
            return simu.build_matrix(omega)

    if guesses is None:
        if strategy == "grid":
            guesses_re = bk.linspace(omega0.real, omega1.real, Nguess_re)
            guesses_im = bk.linspace(omega0.imag, omega1.imag, Nguess_im)
            guesses_re, guesses_im = bk.meshgrid(guesses_re, guesses_im)
            guesses = guesses_re + 1j * guesses_im
            guesses = guesses.flatten()
        else:
            Nre, Nim = Nguess_re * peak_ref, Nguess_im * peak_ref
            omegas_re = bk.linspace(omega0.real, omega1.real, Nre)
            omegas_im = bk.linspace(omega1.imag, omega0.imag, Nim)
            omegas_re_, omegas_im_ = bk.meshgrid(omegas_re, omegas_im, indexing="ij")

            #################################################################
            # Compute complex plane quantities

            omegas_complex = omegas_re_ + 1j * omegas_im_
            Mc = simu.build_matrix(omegas_complex)
            if get_backend() == "torch":
                Mc = bk.permute(Mc, (2, 3, 0, 1))
            else:
                Mc = bk.transpose(Mc, axes=(2, 3, 0, 1))
            evs = bk.linalg.eigvals(Mc)
            srt = bk.argsort(bk.abs(evs), axis=-1)
            if get_backend() == "torch":
                min_evs = bk.gather(evs, -1, srt)[:, :, 0]
            else:
                min_evs = bk.take_along_axis(evs, srt, axis=-1)[:, :, 0]

            im = -bk.log10(bk.abs(min_evs))
            if get_backend() == "torch":
                im = im.numpy()

            coordinates = peak_local_max(im, min_distance=1)

            guess_peak = bk.array([omegas_complex[*coord] for coord in coordinates])

            tloc = bk.linspace(0, 2 * bk.pi, N_guess_loc + 1)[:-1]
            guesses = []
            for guess_loc in guess_peak:
                guesses_ = (
                    guess_loc.real
                    + Rloc * bk.cos(tloc)
                    + 1j * (guess_loc.imag + Rloc * bk.sin(tloc))
                )
                guesses_ = bk.hstack([guesses_, guess_loc])
                guesses.append(guesses_)
            guesses = bk.stack(guesses).flatten()

    if plot_solver:
        plt.plot(guesses.real, guesses.imag, ".k")
        plt.pause(0.001)

    def compute_eigenvalues(guesses, lambda_tol, max_iter, filter=True):
        evs = []
        modes = []
        residuals = []
        for guess in guesses:
            if init_vect == "eig":
                vect_init = null(simu.build_matrix(guess))[:, 0]
            else:
                vect_init = bk.random.rand(simu.n_res)

            res = eig_newton(
                func_eig,
                guess,
                vect_init,
                lambda_tol=lambda_tol,
                max_iter=max_iter,
                func_gives_der=func_gives_der,
                weight=weight,
            )
            if res is not None:
                ev = res["eigval"]
                # print(res["iter_count"],res["delta_lambda"])
                if (
                    ev.real > omega0.real
                    and ev.real < omega1.real
                    and ev.imag < omega1.imag
                    and ev.imag > omega0.imag
                ):
                    evs.append(ev)
                    modes.append(res["eigvec"])
                    residuals.append(res["delta_lambda"])
                    if plot_solver:
                        plt.plot(ev.real, ev.imag, ".r")
                        plt.xlim(omega0.real, omega1.real)
                        plt.ylim(omega0.imag, omega1.imag)
                        plt.pause(0.001)

        if evs == []:
            raise EigenvalueError("No eigenvalues found")
        evs = bk.array(evs)
        modes = bk.stack(modes).T
        residuals = bk.array(residuals)
        if filter:
            precision = lambda_tol * 100
            res_unique = []
            evs_unique = []
            modes_unique = []
            for i, ev in enumerate(evs):
                evfloor = (
                    bk.floor(ev.real / precision) + 1j * bk.floor(ev.imag / precision)
                ) * precision
                if not (evfloor in evs_unique):
                    evs_unique.append(evfloor)
                    res_unique.append(residuals[i])
                    modes_unique.append(modes[:, i])

            modes = bk.stack(modes_unique).T
            evs = bk.array(evs_unique)
            residuals = bk.array(res_unique)
        if verbose:
            print_results(evs, residuals)
        return evs, modes, residuals

    evs, modes, residuals = compute_eigenvalues(
        guesses, lambda_tol, max_iter, filter=True
    )
    return evs, modes


def print_results(evs0, res0, message=None):
    print("")
    print("----------------------------------------------------")
    if message is not None:
        print(message)
    print(f"Found {len(evs0)} eigenvalues")
    print("----------------------------------------------------")
    print("              eigenvalue                 residual")
    print("----------------------------------------------------")
    for z0, r0 in zip(evs0, res0):
        space = " " if z0.real > 0 else ""
        print(f"{space}{z0:.14f}     {r0:.3e}")


# def gram_schmidt(A):
#     """Orthogonalize a set of vectors stored as the columns of matrix A."""
#     # Get the number of vectors.
#     n = A.shape[1]
#     for j in range(n):
#         # To orthogonalize the vector in column j with respect to the
#         # previous vectors, subtract from it its projection onto
#         # each of the previous vectors.
#         for k in range(j):
#             A[:, j] -= bk.dot(A[:, k], A[:, j]) * A[:, k]
#         A[:, j] = A[:, j] / bk.linalg.norm(A[:, j])
#     return A


# def _from_basis_to_project_matrix(B):
#     """Formula page 87 book 'Maths For ML'"""
#     inv_Bt_B = bk.linalg.inv(bk.dot(B.T, B))
#     proj_matrix = bk.dot(B, bk.dot(inv_Bt_B, B.T))
#     return proj_matrix


# def _projec(x, basis):
#     """project `x` in the new vector space defined by `basis`"""
#     proj_matrix = _from_basis_to_project_matrix(basis)
#     proj_x = bk.dot(proj_matrix, x)
#     return proj_x


# def _get_col(x, col_id):
#     """return column `col_id` from matrix `x`"""
#     raw_col_val = x[:, col_id]
#     col_as_row = bk.array([raw_col_val]).T
#     return col_as_row


# def gram_schmidt(B):
#     nb_col = B.shape[1]
#     first_col = _get_col(B, 0)

#     U_vecs = [first_col]

#     for i in range(1, nb_col):
#         B_i = _get_col(B, i)
#         U_i_1 = bk.concatenate(U_vecs, axis=1)
#         p = _projec(B_i, U_i_1)
#         U_i = B_i - p
#         U_vecs.append(U_i)

#     return U_vecs
