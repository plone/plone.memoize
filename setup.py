from setuptools import setup, find_packages
import os

version = '1.0.5'

setup(name='plone.memoize',
      version=version,
      description="Decorators for caching the values of functions and methods",
      long_description=open(os.path.join("plone", "memoize", "README.txt")).read() + '\n' + \
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[
          "Development Status :: 5 - Production/Stable",
          "Framework :: Zope3",
          "Intended Audience :: Developers",
          "License :: OSI Approved :: GNU General Public License (GPL)",
          "Programming Language :: Python",
          "Topic :: Software Development :: Libraries :: Python Modules",
          ],
      keywords='plone memoize decorator cache',
      author='Martin Aspeli, David "Whit" Morriss and Daniel Nouri',
      author_email='optilude@gmx.net',
      url='http://svn.plone.org/svn/plone/plone.memoize',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['plone'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'setuptools',
      ],
      )
