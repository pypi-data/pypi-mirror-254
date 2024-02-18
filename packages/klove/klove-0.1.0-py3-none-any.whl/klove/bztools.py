#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Benjamin Vial
# This file is part of klove
# License: GPLv3
# See the documentation at benvial.gitlab.io/klove

__all__ = ["init_bands", "init_bands_plot"]


from . import backend as bk


def init_bands(sym_points, nband):
    Gamma_point, X_point, M_point = sym_points
    _kx = bk.linspace(Gamma_point[0], X_point[0], nband)
    _ky = bk.linspace(Gamma_point[1], X_point[1], nband)
    kGammaX = bk.vstack([_kx, _ky])
    _kx = bk.linspace(X_point[0], M_point[0], nband)
    _ky = bk.linspace(X_point[1], M_point[1], nband)
    kXM = bk.vstack([_kx, _ky])
    _kx = bk.linspace(M_point[0], Gamma_point[0], nband)
    _ky = bk.linspace(M_point[1], Gamma_point[1], nband)
    kMGamma = bk.vstack([_kx, _ky])
    ks = bk.vstack([kGammaX[:, :-1].T, kXM[:, :-1].T, kMGamma.T])
    return ks


def init_bands_plot(sym_points, nband):
    Gamma_point, X_point, M_point = sym_points
    dMGamma = bk.linalg.norm(bk.array(Gamma_point) - bk.array(M_point))
    dGammaX = bk.linalg.norm(bk.array(X_point) - bk.array(Gamma_point))
    dXM = bk.linalg.norm(bk.array(M_point) - bk.array(X_point))
    _kx = bk.linspace(0, dGammaX, nband)[:-1]
    _kx1 = dGammaX + bk.linspace(0, dXM, nband)[:-1]
    _kx2 = dXM + dGammaX + bk.linspace(0, dMGamma, nband)
    ksplot = bk.hstack([_kx, _kx1, _kx2])
    kdist = [dGammaX, dXM, dMGamma]
    return ksplot, kdist
