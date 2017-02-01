#!/usr/bin/env python3

from setuptools import setup

setup(name='sysmonitor',
      version='0.1',
      description='System monitor',
      author='Lukas Wutschitz',
      author_email='lw@wulu.eu',
      license='MIT',
      test_suite='nose.collector',
      tests_require=['nose'],
      packages=['sysmonitor'],
      scripts=['bin/monitor'],
      zip_safe=False)

