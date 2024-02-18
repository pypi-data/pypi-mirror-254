#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Benjamin Vial
# This file is part of klove
# License: GPLv3
# See the documentation at benvial.gitlab.io/klove


def test_far_field():
    from math import pi

    import klove as kl

    bk = kl.backend

    plate = kl.ElasticPlate(h=1, rho=1, E=1, nu=0.21)

    omega0 = 2e3
    a = 1
    R = 1
    Nres = 6

    m0 = plate.rho * a**2 * plate.h
    ms = bk.ones(Nres) * m0
    alpha = 2
    dist = bk.linspace(0.5, 1.5, Nres)
    ks = m0 * omega0**2 * dist**2
    t0 = -69.81 * bk.ones(Nres) * plate.bending_stiffness

    resarray = []
    for alpha in range(Nres):
        q = bk.array(2 * pi * alpha / Nres)
        xalpha = R * bk.cos(q)
        yalpha = R * bk.sin(q)
        resarray.append(kl.ConstantStrength(t0[alpha], (xalpha, yalpha)))

    sim = kl.ScatteringSimulation(plate, resarray, alternative=True)

    Nomegas = 5
    k = bk.linspace(0.001, 8, Nomegas)
    omegas = k**2 / (plate.rho * plate.h / plate.bending_stiffness) ** 0.5
    Ntheta = 3
    angles = bk.linspace(0, 2 * pi, Ntheta)
    far_field = bk.zeros([Nomegas, Ntheta], dtype=bk.complex64)
    sigma_sc = bk.zeros(Nomegas)
    for omegaIterator, omega in enumerate(omegas):
        incident = sim.plane_wave
        phi_n = sim.solve(incident, omega, angle=0)
        far_field[omegaIterator, :] = sim.get_far_field_radiation(phi_n, omega, angles)
        sigma_sc[omegaIterator] = sim.get_scattering_cross_section(phi_n, omega)
