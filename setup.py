from pathlib import Path
from setuptools import find_packages
from setuptools import setup


version = "3.0.2"

long_description = (
    f"{Path('README.rst').read_text()}\n"
    f"{(Path('plone') / 'memoize' / 'README.rst').read_text()}\n"
    f"{Path('CHANGES.rst').read_text()}"
)

setup(
    name="plone.memoize",
    version=version,
    description="Decorators for caching the values of functions and methods",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    # Get more strings from
    # https://pypi.org/classifiers/
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 6.0",
        "Framework :: Plone :: Core",
        "Framework :: Zope :: 5",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
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
    python_requires=">=3.8",
    extras_require=dict(
        test=[
            "zope.configuration",
            "zope.publisher",
            "zope.testing",
        ],
    ),
    install_requires=[
        "setuptools",
        "zope.annotation",
        "zope.component",
        "zope.globalrequest",
        "zope.interface",
        "zope.ramcache",
    ],
)
