#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Benjamin Vial
# This file is part of klove
# License: GPLv3
# See the documentation at benvial.gitlab.io/klove


def test_qnms():
    from math import pi

    import klove as kl

    bk = kl.backend
    Nres = 3
    alternative = True
    a = 1
    plate = kl.ElasticPlate(a / 10, 1, 1, 0.3)
    omega_plate0 = plate.omega0(a)
    m_plate = plate.rho * a**2 * plate.h
    omegar0 = 1
    m0 = m_plate / 10
    k0 = omegar0**2 * m0
    positionsx = bk.linspace(-Nres * a / 2, Nres * a / 2, Nres)
    positions = [(_x, 0) for _x in positionsx]
    masses = bk.ones(Nres) * m0
    stiffnesses = bk.ones(Nres) * k0
    res_array = []
    for i in range(Nres):
        res_array.append(kl.Resonator(masses[i], stiffnesses[i], positions[i]))
    simu = kl.ScatteringSimulation(plate, res_array, alternative=alternative)

    singularity_Talpha = simu.get_strength_poles()
    omega0 = 0.1 - 1.13 * 1j
    omega1 = 1.91 - 1e-14 * 1j

    N_guess_loc = 3
    lambda_tol = 1e-12
    max_iter = 100
    evs, eigenvectors = simu.eigensolve(
        omega0,
        omega1,
        lambda_tol=lambda_tol,
        max_iter=max_iter,
        N_guess_loc=N_guess_loc,
        Rloc=0.01,
    )

    Nmodes = len(evs)

    M = [simu.build_matrix(omega) for omega in evs]
    dM = [simu.build_matrix_derivative(omega) for omega in evs]

    multiplicities = simu.get_multiplicities(evs, M)

    evs, eigenvectors = simu.update_eig(evs, eigenvectors, multiplicities)
