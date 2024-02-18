#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Benjamin Vial
# This file is part of klove
# License: GPLv3
# See the documentation at benvial.gitlab.io/klove


import scipy.special as sp

from . import backend as bk
from . import get_backend

BACKEND = get_backend()

EPS = 1e-12


def j0(kr):
    return sp.jn(0, kr)


def j1(kr):
    return sp.jn(1, kr)


def y0(kr):
    return sp.yv(0, kr)


def y1(kr):
    return sp.yv(1, kr)


def k0(kr):
    return sp.kv(0, kr)


def k1(kr):
    return sp.kv(1, kr)


def j2(kr):
    return sp.jn(2, kr)


def y2(kr):
    return sp.yv(2, kr)


def k2(kr):
    return sp.kv(2, kr)


def j3(kr):
    return sp.jn(3, kr)


def y3(kr):
    return sp.yv(3, kr)


def k3(kr):
    return sp.kv(3, kr)


def torch_j2(kr):
    return 2 / kr * bk.special.bessel_j1(kr) - bk.special.bessel_j0(kr)


def torch_y2(kr):
    return 2 / kr * bk.special.bessel_y1(kr) - bk.special.bessel_y0(kr)


def torch_k2(kr):
    return 2 / kr * bk.special.modified_bessel_k1(kr) + bk.special.modified_bessel_k0(
        kr
    )


def torch_j3(kr):
    return 4 / kr * torch_j2(kr) - bk.special.bessel_j1(kr)


def torch_y3(kr):
    return 4 / kr * torch_y2(kr) - bk.special.bessel_y1(kr)


def torch_k3(kr):
    return 4 / kr * torch_k2(kr) + bk.special.modified_bessel_k1(kr)


bessel_j0 = bk.special.bessel_j0 if BACKEND == "torch" else sp.j0
bessel_y0 = bk.special.bessel_y0 if BACKEND == "torch" else sp.y0
bessel_k0 = bk.special.modified_bessel_k0 if BACKEND == "torch" else sp.k0
bessel_j1 = bk.special.bessel_j1 if BACKEND == "torch" else sp.j1
bessel_y1 = bk.special.bessel_y1 if BACKEND == "torch" else sp.y1
bessel_k1 = bk.special.modified_bessel_k1 if BACKEND == "torch" else sp.k1
bessel_j2 = torch_j2 if BACKEND == "torch" else j2
bessel_y2 = torch_y2 if BACKEND == "torch" else y2
bessel_k2 = torch_k2 if BACKEND == "torch" else k2
bessel_j3 = torch_j3 if BACKEND == "torch" else j3
bessel_y3 = torch_y3 if BACKEND == "torch" else y3
bessel_k3 = torch_k3 if BACKEND == "torch" else k3


def switch_complex(f1, f2):
    def wrapper(z):
        z = bk.array(z)
        cond = bk.is_complex(z) if BACKEND == "torch" else bk.any(bk.iscomplex(z))
        if cond:
            return f2(z)
        return f1(z.real)

    return wrapper


bessel_j0 = switch_complex(bessel_j0, j0)
bessel_y0 = switch_complex(bessel_y0, y0)
bessel_k0 = switch_complex(bessel_k0, k0)
bessel_j1 = switch_complex(bessel_j1, j1)
bessel_y1 = switch_complex(bessel_y1, y1)
bessel_k1 = switch_complex(bessel_k1, k1)
bessel_j2 = switch_complex(bessel_j2, j2)
bessel_y2 = switch_complex(bessel_y2, y2)
bessel_k2 = switch_complex(bessel_k2, k2)
bessel_j3 = switch_complex(bessel_j3, j3)
bessel_y3 = switch_complex(bessel_y3, y3)
bessel_k3 = switch_complex(bessel_k3, k3)


def _gfreal(kr):
    return bk.where(bk.abs(bk.array(kr)) < EPS, 1.0, bessel_j0(kr))


def _gfimag(kr):
    return bk.where(
        bk.abs(bk.array(kr)) < EPS,
        0.0,
        bessel_y0(kr) + 2 / bk.pi * bessel_k0(kr),
    )


def _dgfreal(kr):
    return bk.where(bk.abs(bk.array(kr)) < EPS, 0.0, -bessel_j1(kr))


def _dgfimag(kr):
    return bk.where(
        bk.abs(bk.array(kr)) < EPS,
        0.0,
        -bessel_y1(kr) - 2 / bk.pi * bessel_k1(kr),
    )


if BACKEND == "torch":

    class _GFreal(bk.autograd.Function):
        @staticmethod
        def forward(ctx, kr):
            ctx.save_for_backward(kr)
            return _gfreal(kr)

        @staticmethod
        def backward(ctx, grad_output):
            (kr,) = ctx.saved_tensors
            return grad_output * _dgfreal(kr)

    class _GFimag(bk.autograd.Function):
        @staticmethod
        def forward(ctx, kr):
            ctx.save_for_backward(kr)
            return _gfimag(kr)

        @staticmethod
        def backward(ctx, grad_output):
            (kr,) = ctx.saved_tensors
            return grad_output * _dgfimag(kr)

    gfreal = _GFreal.apply
    gfimag = _GFimag.apply


else:
    gfreal = _gfreal
    gfimag = _gfimag


def _norma_gf(k):
    return 1j / (8 * k**2)


def greens_function(k, r):
    kr = k * r
    norm = _norma_gf(k)
    return norm * (gfreal(kr) + 1j * gfimag(kr))


def dgreens_function_dk(k, r):
    G0 = greens_function(k, r)
    G1 = _gf_fun(k, r, bessel_j1, bessel_y1, bessel_k1)
    return -2 / k * G0 - G1 * r


def greens_function_cartesian(k, x, y):
    r = radial_coordinates(x, y)
    return greens_function(k, r)


def radial_coordinates(x, y):
    return (EPS + x**2 + y**2) ** 0.5


def _gf_fun(k, r, jfun, yfun, kfun):
    kr = k * r
    re = jfun(kr)
    im = yfun(kr) + 2 / bk.pi * kfun(kr)
    norm = _norma_gf(k)
    return norm * (re + 1j * im)


def grad_greens_function_cartesian(k, x, y):
    r = radial_coordinates(x, y)
    out = -k / r * _gf_fun(k, r, bessel_j1, bessel_y1, bessel_k1)
    out = bk.where(bk.abs(k * r) < EPS, 0.0 + 0.0 * 1j, out)
    return x * out, y * out


def laplacian_greens_function_cartesian(k, x, y):
    r = radial_coordinates(x, y)
    G1 = _gf_fun(k, r, bessel_j1, bessel_y1, bessel_k1)
    G2 = _gf_fun(k, r, bessel_j2, bessel_y2, bessel_k2)
    out = -2 * k / r * G1 + k**2 * G2
    out = bk.where(bk.abs(k * r) < EPS, 0.0 + 0.0 * 1j, out)
    return out


def grad_laplacian_greens_function_cartesian(k, x, y):
    r = radial_coordinates(x, y)
    G2 = _gf_fun(k, r, bessel_j2, bessel_y2, bessel_k2)
    G3 = _gf_fun(k, r, bessel_j3, bessel_y3, bessel_k3)

    def tmp(x):
        out = 4 * k**2 * x / r**2 * G2 - k**3 * x / r * G3
        out = bk.where(bk.abs(k * r) < EPS, 0.0 + 0.0 * 1j, out)
        return out

    return tmp(x), tmp(y)
