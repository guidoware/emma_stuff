# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.readlines()
    install_requires = [line for line in requirements if not line.startswith('#')]

with open('requirements-testing.txt') as f:
    test_reqs = f.readlines()
    tests_require = [line for line in test_reqs if not line.startswith('#')]

setup(
    name='emma-stuff',
    version='0.0.1',
    description='Emma Stuff',
    long_description='Check list of URLs. Sample for Emma',
    author='Nick Guidoux',
    packages=find_packages(),
    include_package_data=True,
    install_requires = install_requires,
    tests_require = tests_require,
)

