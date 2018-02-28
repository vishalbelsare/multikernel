#!/usr/bin/python
"""mkl setup script.

Author: Federico Tomasi
Copyright (c) 2017, Federico Tomasi.
Licensed under the BSD 3-Clause License (see LICENSE.txt).
"""

from setuptools import setup, find_packages
# import numpy as np

# Package Version
from mkl import __version__ as version
# alignment_module = Extension('icing.align.align',
#                              sources=['icing/align/alignment.c'])
setup(
    name='mkl',
    version=version,

    description=('MKL (Multiple Kernel Learning)'),
    long_description=open('README.md').read(),
    author='Federico Tomasi',
    author_email='federico.tomasi@dibris.unige.it',
    maintainer='Federico Tomasi',
    maintainer_email='federico.tomasi@dibris.unige.it',
    url='https://github.com/fdtomasi/mkl',
    download_url='https://github.com/fdtomasi/mkl/archive/'
                 'v%s.tar.gz' % version,
    keywords=['kernel', 'learning'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'License :: OSI Approved :: BSD License',
        'Topic :: Software Development',
        'Topic :: Scientific/Engineering',
        'Natural Language :: English',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Operating System :: MacOS',
        'Programming Language :: Python'
    ],
    license='FreeBSD',
    packages=find_packages(exclude=["*.__old", "*.tests"]),
    include_package_data=True,
    requires=['numpy (>=1.11)',
              'scipy (>=0.16.1,>=1.0)',
              'sklearn (>=0.17)',
              'six'],
)
