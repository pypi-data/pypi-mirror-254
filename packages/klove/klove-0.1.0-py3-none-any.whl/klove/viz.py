#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Benjamin Vial
# This file is part of klove
# License: GPLv3
# See the documentation at benvial.gitlab.io/klove


__all__ = ["GifMaker", "plot_bands"]


import glob
import os
import tempfile
from itertools import accumulate

import matplotlib.pyplot as plt
from PIL import Image

from . import backend as bk
from .bztools import init_bands_plot


def save_frame(i, folder=".frames"):
    _name = f"{i}".zfill(3)
    filename = f"{folder}/{_name}.png"
    plt.savefig(filename)


def make_gif(folder=".frames", fps=10, name="animation"):
    imgs = sorted(glob.glob(f"{folder}/*.png"))
    img, *imgs = [Image.open(f, mode="r").convert("RGB") for f in imgs]
    out = img.save(
        f"{name}.gif",
        format="GIF",
        append_images=imgs,
        save_all=True,
        duration=1000 / fps,
        loop=0,
    )
    return os.path.abspath(f"{name}.gif")


class GifMaker:
    def __init__(self, folder=".frames"):
        self.folder = folder
        self.iteration = 0
        self.folder = tempfile.mkdtemp()

    def snap(self):
        self.iteration += 1
        save_frame(self.iteration, self.folder)

    def save(self, *args, **kwargs):
        return make_gif(self.folder, *args, **kwargs)


def plot_bands(
    sym_points,
    nband,
    eigenvalues,
    xtickslabels=[r"$\Gamma$", r"$X$", r"$M$", r"$\Gamma$"],
    color=None,
    **kwargs,
):
    # nband = int((len(eigenvalues)-2)/3)

    if color == None:
        color = "#4d63c5"
        if "color" in kwargs:
            kwargs.pop("colors")
        if "c" in kwargs:
            kwargs.pop("c")

    ksplot, kdist = init_bands_plot(sym_points, nband)
    plt.plot(ksplot, eigenvalues, color=color, **kwargs)
    # xticks = bk.cumsum(bk.array([0] + kdist))
    xticks = list(accumulate([0] + kdist))
    plt.xticks(xticks, xtickslabels)
    for x in xticks:
        plt.axvline(x, c="#8a8a8a")

    plt.xlim(xticks[0], xticks[-1])

    plt.ylabel(r"$\omega$")
