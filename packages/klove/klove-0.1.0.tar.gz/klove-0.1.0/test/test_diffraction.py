#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Benjamin Vial
# This file is part of klove
# License: GPLv3
# See the documentation at benvial.gitlab.io/klove


def test_diff():
    import matplotlib.pyplot as plt

    import klove as kl

    plt.ion()
    plt.close("all")

    bk = kl.backend

    or0 = 0.91
    m0 = 3e-4
    k0 = or0**2 * m0
    Nres = 10
    period = 1.0
    t = bk.linspace(0, 2 * bk.pi, Nres + 1)[:-1]
    R0 = period / 2 * 0.8
    xpos = period / 2 + R0 * bk.cos(t)
    ypos = R0 * bk.sin(t)
    resarray = []
    for xp, yp in zip(xpos, ypos):
        res = kl.Resonator(m0, k0, (xp, yp))
        resarray.append(res)
    plate = kl.ElasticPlate(0.1, 10, 1, 0.1)

    nh = 0

    simu = kl.DiffractionSimulation(plate, resarray, period, nh)

    omega = 0.3
    angle = bk.pi / 2  # - bk.pi / 6

    simu.nh = simu.get_min_harmonics(omega, angle)

    sol = simu.solve(omega, angle)
    print(sol)

    ny = 4
    npx = 100
    npy = npx * ny
    x1 = bk.linspace(0, period, npx)
    y1 = bk.linspace(-ny * period, ny * period, npy)
    x, y = bk.meshgrid(x1, y1, indexing="xy")
    W = simu.get_field(x, y, sol, omega, angle)
    Ws = simu.get_scattered_field(x, y, sol, omega, angle)

    # fig,ax=plt.subplots(1)
    # field = bk.abs(W)
    # plt.pcolormesh(x, y,field , cmap="inferno")
    # plt.gca().set_aspect("equal")
    # for res in resarray:
    #     plt.plot(*res.position, ".w")
    # plt.colorbar()
    # plt.suptitle("total")

    # fig,ax=plt.subplots(1)
    # field = bk.abs(Ws)
    # plt.pcolormesh(x, y,field , cmap="inferno")
    # plt.gca().set_aspect("equal")
    # for res in resarray:
    #     plt.plot(*res.position, ".w")
    # plt.colorbar()
    # plt.suptitle("scattered")

    # fig,ax=plt.subplots(1,2)
    # for i in range(2):
    #     plt.sca(ax[i])
    #     field = bk.real(W) if i==0 else bk.imag(W)
    #     plt.pcolormesh(x, y,field , cmap="RdBu_r")
    #     plt.gca().set_aspect("equal")
    #     for res in resarray:
    #         plt.plot(*res.position, ".k")
    #     plt.colorbar()

    # plt.suptitle("total")

    # fig,ax=plt.subplots(1,2)
    # for i in range(2):
    #     plt.sca(ax[i])
    #     field = bk.real(Ws) if i==0 else bk.imag(Ws)
    #     plt.pcolormesh(x, y, field, cmap="RdBu_r")
    #     plt.gca().set_aspect("equal")
    #     for res in resarray:
    #         plt.plot(*res.position, ".k")
    #     plt.colorbar()

    # plt.suptitle("scattered")

    R, T = simu.get_efficiencies(sol, omega, angle)
    print("Reflection")
    print("----------")
    print(R["energy"])
    print(R["total"])
    print("Transmission")
    print("----------")
    print(T["energy"])
    print(T["total"])
    print("Balance")
    print("----------")
    balance = R["total"] + T["total"]
    print(balance)
    assert abs(balance - 1) < 1e-4

    omega_max = 0.4

    nh_ = simu.get_min_harmonics(omega_max, angle)
    print("max nh", nh_)
    simu.nh = nh
    simu.nh = 1
    # sys.exit(0)

    omegas = bk.linspace(0.01, omega_max, 100)
    Rs = []
    Ts = []
    for omega in omegas:
        sol = simu.solve(omega, angle)
        R, T = simu.get_efficiencies(sol, omega, angle)
        Rs.append(bk.array(list(R["energy"].values())))
        Ts.append(bk.array(list(T["energy"].values())))

    # plt.figure()
    # plt.plot(omegas, Rs)
    # plt.plot(omegas, Ts, "--")
    Rtot = bk.array([sum(_) for _ in Rs])
    Ttot = bk.array([sum(_) for _ in Ts])
    Balance = Rtot + Ttot
    # plt.plot(omegas, Rtot, "b")
    # plt.plot(omegas, Ttot, "--r")
    # plt.plot(omegas, Balance, "-k")

    for b in Balance:
        assert abs(b - 1) < 1e-4
