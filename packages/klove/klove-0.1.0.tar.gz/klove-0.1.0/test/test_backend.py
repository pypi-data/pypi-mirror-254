#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Benjamin Vial
# This file is part of klove
# License: GPLv3
# See the documentation at benvial.gitlab.io/klove


def test_env_var():
    import klove as kl

    backend = kl.get_backend()
    print(backend)


def run(kl, backend):
    res0 = kl.Resonator(1, 1, (0, 0))
    res1 = kl.Resonator(3, 2, (-1, -3))
    plate = kl.ElasticPlate(0.7, 22, 3, 0.1)
    resarray = [res0, res1]
    simu0 = kl.ScatteringSimulation(plate, resarray, alternative=False)
    omega = 2
    pos_src = (1, 1)
    sol0 = simu0.solve(simu0.point_source, omega, pos_src)
    pos_probe = (0.2, 0.4)
    w0 = simu0.get_scattered_field(*pos_probe, sol0, omega)
    return sol0, w0


# def test_backends():
#     import numpy as npo

#     import klove as kl

#     for backend in kl.numdiff.available_backends:
#         print(backend)
#         kl.set_backend(backend)

#         bk = kl.backend
#         assert kl.get_backend() == backend

#         if backend != "jax":
#             sol, w = run(kl, backend)

#             if backend == "numpy":
#                 sol0 = sol.copy()
#                 w0 = w.copy()
#             else:
#                 assert bk.allclose(bk.array(w0), w)
#                 assert bk.allclose(bk.array(sol0), sol)
#             # TODO: Implement jax version

#     kl.set_backend("numpy")
