#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup

setup(install_requires=[
    "numpy",
    "zarr",
    "magicgui",
    "bioimageio.core @ git+https://github.com/bioimage-io/core-bioimage-io-python",
    "gunpowder @ git+https://github.com/funkey/gunpowder.git@patch-1.2.3",
    "matplotlib",
    "torch",
])
