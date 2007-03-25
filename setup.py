from setuptools import setup, find_packages
import sys, os

version = '1.0b1.1'

setup(name='plone.memoize',
      version=version,
      description="Decorator to memoize properties bound to a request",
      long_description="""\
plone.memoize provides memo decorators for Zope 3 views and regular 
classes. For views, a memo will last as long as the request, even
if the view is looked up several times. This requires the request
to be marked as annotatable.
""",
      classifiers=[], # Get strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      keywords='plone memoize decorator',
      author='Martin Aspeli and David "Whit" Morriss',
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
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
