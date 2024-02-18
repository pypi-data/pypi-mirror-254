#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Benjamin Vial
# This file is part of klove
# License: GPLv3
# See the documentation at benvial.gitlab.io/klove


import importlib.metadata as metadata


def get_meta(metadata):
    data = metadata.metadata("klove")
    __version__ = metadata.version("klove")
    __author__ = data.get("author")
    __description__ = data.get("summary")
    return __version__, __author__, __description__, data


__version__, __author__, __description__, data = get_meta(metadata)
