#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Benjamin Vial
# This file is part of klove
# License: GPLv3
# See the documentation at benvial.gitlab.io/klove


"""klove: a Python module for studying resonators on thin elastic plates.
"""


from .__about__ import __author__, __description__, __version__

try:
    import numdiff
    from numdiff import *
    from numdiff import _reload_package

    def set_backend(BACKEND):
        numdiff.set_backend(BACKEND)
        _reload_package("klove")

    def get_backend():
        return numdiff.get_backend()

    BACKEND = numdiff.BACKEND

except:
    import numpy as backend

    def set_backend(BACKEND):
        pass

    def get_backend():
        return "numpy"

    BACKEND = "numpy"


from .bztools import *
from .core import *
from .viz import *
