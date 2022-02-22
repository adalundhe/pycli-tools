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
    name="zebra-python-cli",
    version="0.2.4",
    author="Zebra.com",
    author_email="scorbett@thezebra.com",
    description="A library for writing consistent CLI interfaces.",
    long_description=package_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/thezebra/libraries/zebra-python-cli",
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
