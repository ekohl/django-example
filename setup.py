#!/usr/bin/env python

import os
from setuptools import setup

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

setup(
    name='{{ project_name }}',
    version='1.0',
    description='{{ project_name }}',
    author='Your Name',
    author_email='example@example.com',
    url='http://www.python.org/sigs/distutils-sig/',
    install_requires=open('%s/requirements.txt' %
        os.environ.get('OPENSHIFT_REPO_DIR', PROJECT_ROOT)).readlines(),
)
