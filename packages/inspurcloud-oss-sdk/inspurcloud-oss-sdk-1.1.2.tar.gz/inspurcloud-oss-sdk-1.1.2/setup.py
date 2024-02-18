#!/usr/bin/env python


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('README.md', 'rb') as f:
    readme = f.read().decode('utf-8')

setup(
    name='inspurcloud-oss-sdk',
    version='1.1.2',
    description='Inspur OSS Python SDK',
    author='Inspur Cloud',
    author_email='',
    long_description=readme,
    packages=['oss'],
    install_requires=['requests!=2.9.0', 'crcmod>=1.7'],
    include_package_data=True,
    url='https://cloud.inspur.com/'
)
