#!/usr/bin/env python

from os import path
from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

def read(fname):
    return open(path.join(here, fname)).read()

setup(
    name="webfaction_helpers",
    version="0.0.1",
    description=("Scripts to help provision, configure and deply to"
                 "webfaction using Python and Fabric 2"),
    url="https://github.com/moaxey/WebfactionHelpers",
    packages=find_packages(exclude=['tests']),
    package_data={
        '': ['*.txt', '*.rst'],
    },
    author="Mathew Oakes",
    author_email="open@mathewoak.es",
    license="MIT",
    long_description=read("README.rst"),
    classifiers=[
        "Development Status :: 3 - Alpha",
        'Intended Audience :: Developers',
        "Topic :: Software Developemnt",
        "Topic :: Software Developemnt :: Build Tools",
        "Topic :: Software Developemnt",
        "Topic :: System :: System Administration",
        "License :: OSI Approved :: MIT License",
    ],
)
