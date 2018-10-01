#!/usr/bin/env python
"""The installation script."""

import setuptools


setuptools.setup(
    name='domainstemmer',
    description="Reduces domain names to a form that is directly under a public suffix.",
    author='John Lawrence M. Penafiel',
    url='https://github.com/penafieljlm/domainstemmer',
    download_url='https://github.com/penafieljlm/domainstemmer',
    py_modules=['domainstemmer'],
    packages=setuptools.find_packages(),
    include_package_data=True,
)
