#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Benjamin Vial
# This file is part of klove
# License: GPLv3
# See the documentation at benvial.gitlab.io/klove


def test_gif():
    import os

    import matplotlib.pyplot as plt

    from klove.viz import GifMaker

    plt.figure()

    gmk = GifMaker()

    for i in range(3):
        plt.plot(i, i**2, "or")
        gmk.snap()

    outfile = gmk.save()
    os.remove(outfile)
