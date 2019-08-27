#!/usr/bin/env python

from setuptools import setup

setup(name='python_server_simple',
      version='1.0',
      description='simple server in python',
      author='Nikolaj Majorov',
      author_email='nikolaj@majorov.biz',
      url='https://www.majorov.biz',
      license='MIT',
      test_suite='nose.collector',
      tests_require=['nose', 'nose-cover3','requests'],
      entry_points={
          'console_scripts': ['python_server_simple=server:main'],
      },
     )
