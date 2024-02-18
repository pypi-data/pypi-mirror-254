#!/usr/bin/env python

"""The setup script."""

from setuptools import setup
from setuptools.command.install import install
import sys

class CustomInstall(install):
    def run(self):
        print("ERROR: You have attempted to install 'equaliser'. This package should not be installed.")
        print("Please install 'equalizer' instead.")
        sys.exit(1)

setup(
    author="FairNLP",
    author_email="info@fairnlp.com",
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    license="Apache Software License 2.0",
    name="equaliser",
    url="https://github.com/FairNLP/equalizer",
    version="0.0.0",
    zip_safe=False,
)
