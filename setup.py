#!/usr/bin/env python
# coding: utf-8

from setuptools import setup, find_packages

version = {}

with open("aws_acl_helper/version.py") as fp:
    exec(fp.read(), version)

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

with open('requirements.txt') as f:
requirements = f.read().splitlines()

setup(
    name='requests_negotiate',
    version=version['__version__'],
    packages=find_packages(exclude=('docs')),
    install_requires=requirements,
    provides=[ 'requests_negotiate' ],
    author='Brad Davidson',
    url='https://github.com/requests/requests-ntlm',
    description='This package allows for Single-Sign On HTTP Negotiate authentication using the requests library on Windows.',
    long_description=readme,
    license=license,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4'
    ],
)