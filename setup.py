#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Setup file for osc2rtmidi."""

import sys

from os.path import join

from setuptools import setup  # needs to stay before the imports below!
from distutils.dist import DistributionMetadata
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    """Custom setup command to run tests via pytest."""

    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


# source package structure
PKG_DIR = "osc2rtmidi"

# Add custom distribution meta-data, avoids warning when running setup
DistributionMetadata.repository = None

# read meta-data from release.py
setup_opts = {}
release_info = join(PKG_DIR, 'release.py')
exec(compile(open(release_info).read(), release_info, 'exec'), {}, setup_opts)

# Add custom test command
setup_opts.setdefault('cmdclass', {})['test'] = PyTest

setup(
    packages=['osc2rtmidi'],
    install_requires=[
        'pyliblo',
        'python-rtmidi',
        'PyYAML'
    ],
    entry_points={
        'console_scripts': [
            'osc2rtmidi = osc2rtmidi.main:main',
        ]
    },
    tests_require=['pytest'],
    # On systems without a RTC (e.g. Raspberry Pi), system time will be the
    # Unix epoch when booted without network connection, which makes zip fail,
    # because it does not support dates < 1980-01-01.
    zip_safe=False,
    **setup_opts
)
