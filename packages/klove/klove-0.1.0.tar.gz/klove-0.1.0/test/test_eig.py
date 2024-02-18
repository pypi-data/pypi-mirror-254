#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Benjamin Vial
# This file is part of klove
# License: GPLv3
# See the documentation at benvial.gitlab.io/klove


def test_eig():
    import numpy as np

    from klove import backend as bk
    from klove import get_backend
    from klove.eig import polyeig

    np.random.seed(1234)
    N = 10
    P = 5
    A = bk.array(np.random.rand(P, N, N))
    e, X = polyeig(*A)
    # Test that eigenvector and value satisfy eigenvalue problem:
    for i in range(N):
        s = e[i]
        x = X[:, i]
        M = 0
        for p in range(P):
            M *= A[p] * s**p

        res = M @ x  # residuals
        assert bk.all(np.abs(res) < 1e-12)
