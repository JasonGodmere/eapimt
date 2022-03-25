# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='eapimt',
    version='0.1.0',
    description='Enphase API Management Tool',
    long_description=readme,
    author='Jason Godmere',
    #author_email='na',
    url='https://github.com/JasonGodmere/eapimt',
    license=license,
    package_dir={"": "/Users/jasongodmere/Desktop/dev/Kumukit Support/Microservices/enphase_viewer/eapimt"},
    packages=find_packages(
        exclude=('tests', 'docs')),
    install_requires=['requests']
)

