from setuptools import setup, find_packages
import sys, os

version = '1.0.4'

setup(name='plone.memoize',
      version=version,
      description="Decorators for caching the values of functions and methods",
      long_description="""\
plone.memoize provides Python function decorators for caching the
values of functions and methods.

The type of cache storage is freely configurable by the user, as is
the cache key, which is what the function's value depends on.

plone.memoize has support for memcached and is easily extended to use
other caching storages.  It also has specialized decorators for use
with Zope views.  However, plone.memoize can be used without Zope.
""",
      classifiers=[],
      keywords='plone memoize decorator cache',
      author='Martin Aspeli, David "Whit" Morriss and Daniel Nouri',
      author_email='optilude@gmx.net',
      url='http://svn.plone.org/svn/plone/plone.memoize',
      license='LGPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['plone'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'setuptools',
      ],
      )
