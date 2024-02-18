#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Benjamin Vial
# This file is part of klove
# License: GPLv3
# See the documentation at benvial.gitlab.io/klove


def test_import_nonumdiff():
    import sys

    import klove

    sys.modules["numdiff"] = None
    import importlib

    importlib.reload(klove)

    assert klove.set_backend("Whatever") is None
    assert klove.get_backend() == "numpy"

    del sys.modules["numdiff"]
    import numdiff

    importlib.reload(klove)

    # klove.set_backend("numpy")
