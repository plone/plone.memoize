import os
from setuptools import setup, find_packages


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()


version = '1.1.1'

long_description = (
    read('README.txt')
    + '\n' +
    read('plone', 'memoize', 'README.txt')
    + '\n' +
    read('CHANGES.txt')
    + '\n'
    )

setup(name='plone.memoize',
      version=version,
      description="Decorators for caching the values of functions and methods",
      long_description=long_description,
      classifiers=[
          "Development Status :: 5 - Production/Stable",
          "Environment :: Web Environment",
          "Framework :: Plone",
          "Framework :: Zope2",
          "License :: OSI Approved :: GNU General Public License (GPL)",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
        ],
      keywords='plone memoize decorator cache',
      author='Plone Foundation',
      author_email='plone-developers@lists.sourceforge.net',
      url='http://pypi.python.org/pypi/plone.memoize',
      license='GPL version 2',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['plone'],
      include_package_data=True,
      zip_safe=False,
      extras_require=dict(
          test=[
            'zope.configuration',
            'zope.publisher',
            'zope.testing',
          ]
      ),
      install_requires=[
        'setuptools',
        'zope.annotation',
        'zope.component',
        'zope.interface',
        'zope.ramcache',
      ],
      )
