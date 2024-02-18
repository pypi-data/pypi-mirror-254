#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Benjamin Vial
# This file is part of klove
# License: GPLv3
# See the documentation at benvial.gitlab.io/klove


def test_bands():
    from math import pi

    import matplotlib.pyplot as plt

    import klove as kl

    bk = kl.backend
    a = 1
    q = a / (2 * 3**0.5)
    gamma = bk.array(pi / 6)
    positions = [
        (q * bk.cos(gamma), q * bk.sin(gamma)),
        (-q * bk.cos(gamma), -q * bk.sin(gamma)),
    ]
    lattice_vectors = (a, 0), (a * bk.cos(gamma * 2), a * bk.sin(gamma * 2))
    plate = kl.ElasticPlate(1, 0.1, 1, 0.0)
    k = (4 * pi) ** 2 * plate.omega0(a)
    m = 1
    masses = [m, m]
    stiff = [k, k]
    res_array = []
    for m, k, pos in zip(masses, stiff, positions):
        res_array.append(kl.Resonator(m, k, pos))

    bs = kl.BandsSimulation(plate, res_array, lattice_vectors)

    Npw = 4
    Nk = 5

    b0 = bk.pi / a
    Gamma_point = 0, 0
    K_point = 2 * b0 / 3, 2 * b0 / 3**0.5
    M_point = 0, 2 * b0 / 3**0.5
    sym_points = [Gamma_point, M_point, K_point]
    ks = kl.init_bands(sym_points, Nk)
    bands = []
    for K in ks:
        omegans = bs.eigensolve(K, Npw, return_modes=False, hermitian=False)
        bands.append(omegans)

    bands = bk.stack(bands).real
    plt.figure()
    kl.plot_bands(
        sym_points, Nk, bands, xtickslabels=[r"$\Gamma$", r"$M$", r"$K$", r"$\Gamma$"]
    )
