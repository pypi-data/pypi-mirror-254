# Copyright 2024 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0

#!/usr/bin/env python

import os
from setuptools import setup

README = """
See the README on `GitHub
<https://github.com/uw-it-aca/commonconf>`_.
"""

version_path = 'commonconf/VERSION'
VERSION = open(os.path.join(os.path.dirname(__file__), version_path)).read()
VERSION = VERSION.replace("\n", "")

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

url = "https://github.com/uw-it-aca/commonconf"
setup(
    name='CommonConf',
    version=VERSION,
    packages=['commonconf'],
    author="UW-IT AXDD",
    author_email="aca-it@uw.edu",
    include_package_data=True,
    install_requires=[],
    license='Apache License, Version 2.0',
    description=('An interface for getting settings from a variety '
                 'of configuration libraries.'),
    long_description=README,
    url=url,
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.8',
    ],
)
