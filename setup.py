import os
import glob
from stat import (
    S_IEXEC
)
from sys import (
    platform,
    executable
)
from setuptools import (
    setup,
    find_packages
)
from distutils.sysconfig import get_python_lib
from setuptools.command.install import install

current_directory = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(current_directory, 'README.md'), "r") as readme:
    package_description = readme.read()

setup(
    name="pycli-tools",
    version="0.1.0",
    author="Sean Corbett",
    author_email="sean.corbett@umontana.edu",
    description="A library for writing consistent CLI interfaces.",
    long_description=package_description,
    long_description_content_type="text/markdown",
    url="https://github.com/scorbettUM/pycli-tools",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    install_requires=[
        'configargparse',
        'zebra-automate-py-logging'
    ],
    python_requires='>=3.6'
)
