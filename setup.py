#!/usr/bin/env python3
## This file is part of the sconfparser application, released under
## GNU General Public License, Version 3.0
## See file COPYING for details.
##
## Author: Klementyev Mikhail <jollheef@riseup.net>
#

from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name='sconfparser',
    version='0.1',
    description='Simple config parser',
    author='Mikhail Klementyev',
    author_email='jollheef@riseup.net',
    url='https://github.com/jollheef/sconfparser/',
    packages=find_packages(),
    license='GPLv3'
)
