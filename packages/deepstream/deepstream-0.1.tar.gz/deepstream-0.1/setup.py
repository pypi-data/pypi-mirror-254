#! /usr/bin/env python
"""Toolbox for open set recognition."""
from __future__ import absolute_import

import os
# read the contents of your README file
from os import path

from setuptools import find_packages, setup

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

# get __version__ from _version.py
ver_file = os.path.join("deepstream", "_version.py")
with open(ver_file) as f:
    exec(f.read())

DISTNAME = "deepstream"
DESCRIPTION = "Python module to prepare data streams from torch training procedure."
MAINTAINER = "P. Ksieniewicz"
MAINTAINER_EMAIL = "pawel.ksieniewicz@pwr.edu.pl"
URL = "https://github.com/w4k2/deepstream"
LICENSE = "GPL-3.0"
DOWNLOAD_URL = "https://github.com/w4k2/deepstream"
VERSION = __version__
INSTALL_REQUIRES = ["numpy", "torch", "torchvision", "tqdm"]
CLASSIFIERS = [
    "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    "Programming Language :: Python",
    "Topic :: Scientific/Engineering",
    "Topic :: Scientific/Engineering :: Artificial Intelligence",
    "Topic :: Software Development :: Libraries",
    "Topic :: Software Development :: Libraries :: Python Modules",
]


setup(
    name=DISTNAME,
    maintainer=MAINTAINER,
    maintainer_email=MAINTAINER_EMAIL,
    description=DESCRIPTION,
    license=LICENSE,
    url=URL,
    version=VERSION,
    download_url=DOWNLOAD_URL,
    packages=find_packages(),
    install_requires=INSTALL_REQUIRES,
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=CLASSIFIERS,
)
