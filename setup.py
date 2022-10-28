# -*- coding: utf-8 -*-
from setuptools import find_packages
from setuptools import setup

import os


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()


version = "3.0.0"

long_description = u"\n".join(
    [read("README.rst"), read("plone", "memoize", "README.rst"), read("CHANGES.rst"),]
)


setup(
    name="plone.memoize",
    version=version,
    description="Decorators for caching the values of functions and methods",
    long_description=long_description,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 5.2",
        "Framework :: Plone :: 6.0",
        "Framework :: Plone :: Core",
        "Framework :: Zope :: 4",
        "Framework :: Zope :: 5",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
    keywords="plone memoize decorator cache",
    author="Plone Foundation",
    author_email="plone-developers@lists.sourceforge.net",
    url="https://pypi.org/project/plone.memoize",
    license="BSD",
    packages=find_packages(),
    namespace_packages=["plone"],
    include_package_data=True,
    zip_safe=False,
    test_suite="plone.memoize.tests.test_suite",
    extras_require=dict(
        test=[
            "zope.configuration",
            "zope.globalrequest",
            "zope.publisher",
            "zope.testrunner",
            "zope.testing",
        ],
    ),
    install_requires=[
        "setuptools",
        "six",
        "zope.annotation",
        "zope.component",
        "zope.interface",
        "zope.ramcache",
    ],
)
