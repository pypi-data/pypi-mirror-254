#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Benjamin Vial
# This file is part of klove
# License: GPLv3
# See the documentation at benvial.gitlab.io/klove


def test_alt():
    import klove as kl

    res0 = kl.Resonator(1, 1, (0, 0))
    res1 = kl.Resonator(3, 2, (-1, -3))
    plate = kl.ElasticPlate(0.7, 22, 3, 0.1)
    resarray = [res0, res1]
    simu0 = kl.ScatteringSimulation(plate, resarray, alternative=False)

    omega = 2
    pos_src = (1, 1)

    sol0 = simu0.solve(simu0.point_source, omega, pos_src)

    simu1 = kl.ScatteringSimulation(plate, resarray, alternative=True)
    sol1 = simu1.solve(simu1.point_source, omega, pos_src)

    pos_probe = (0.2, 0.4)

    w0 = simu0.get_scattered_field(*pos_probe, sol0, omega)

    w1 = simu1.get_scattered_field(*pos_probe, sol1, omega)

    assert abs(w0 - w1) < 1e-6
