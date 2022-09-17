# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

from src import pytime

setup(
    name="pytime",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    version=pytime.__version__,
    description="timer tool",
    author="kevin hillairet",
)
