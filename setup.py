# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages
import os


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

ROOT_DIR = os.path.abspath(os.curdir)

setup(
    name='eapimt',
    version='0.1.0',
    description='Enphase API Management Tool',
    long_description=readme,
    author='Jason Godmere',
    #author_email='na',
    url='https://github.com/JasonGodmere/eapimt',
    license=license,
    package_dir={"": ROOT_DIR},
    packages=find_packages(
        exclude=('tests', 'docs', 'resources')),
    install_requires=['requests']
)

