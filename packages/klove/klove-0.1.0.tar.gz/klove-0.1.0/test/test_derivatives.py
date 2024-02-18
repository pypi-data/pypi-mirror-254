#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Benjamin Vial
# This file is part of klove
# License: GPLv3
# See the documentation at benvial.gitlab.io/klove


def test_derivatives():
    import klove as kl

    def _gradient(f):
        df = bk.gradient(f)
        return df[0] if kl.get_backend() == "torch" else df

    bk = kl.backend

    res = kl.Resonator(1, 1, (0, 0))

    nf = 1000
    omega = bk.linspace(0.1, 0.9, nf)

    f = res.strength(omega)
    domega = _gradient(omega)

    fd = _gradient(f) / domega
    df = res.dstrength_domega(omega)

    nres = 5
    res_array = [kl.Resonator(1, 1, (i, 0)) for i in range(nres)]

    shift = 2
    tol = 1e-3
    assert bk.allclose(df[shift:-shift], fd[shift:-shift], rtol=tol)

    plate = kl.ElasticPlate(1, 2, 3, 0.1)

    for alternative in [True, False]:
        simu = kl.ScatteringSimulation(plate, res_array, alternative)

        k = simu.wavenumber(omega)
        fd = _gradient(k) / domega

        df = simu.dwavenumber_domega(omega)

        assert bk.allclose(df[shift:-shift], fd[shift:-shift], rtol=tol)

        s = simu._strength(omega, res)
        fd = _gradient(s) / domega

        df = simu._dstrength_domega(omega, res)
        assert bk.allclose(df[shift:-shift], fd[shift:-shift], rtol=tol)

        r = 0.1

        dk = _gradient(k)
        g = kl.special.greens_function(k, r)
        fd = _gradient(g) / dk

        df = kl.special.dgreens_function_dk(k, r)

        assert bk.allclose(df[shift:-shift], fd[shift:-shift], rtol=tol)

        M = simu.build_matrix(omega)
        dM = simu.build_matrix_derivative(omega)

        for i in range(simu.n_res):
            for j in range(simu.n_res):
                print(i, j)
                f = M[i, j]
                fd = _gradient(f) / domega
                df = dM[i, j]
                print(bk.mean(abs(df[shift:-shift] - fd[shift:-shift])))
                assert bk.allclose(df[shift:-shift], fd[shift:-shift], rtol=tol)
