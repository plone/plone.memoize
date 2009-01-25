from setuptools import setup, find_packages

version = '1.1'

setup(name='plone.memoize',
      version=version,
      description="Decorators for caching the values of functions and methods",
      long_description=open("README.txt").read() + '\n' + \
                       open("docs/HISTORY.txt").read(),
      classifiers=[
          "Environment :: Web Environment",
          "Framework :: Plone",
          "Framework :: Zope2",
          "Framework :: Zope3",
          "License :: OSI Approved :: GNU General Public License (GPL)",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
      ],
      keywords='plone memoize decorator cache',
      author='Plone Foundation',
      author_email='plone-developers@lists.sourceforge.net',
      url='http://svn.plone.org/svn/plone/plone.memoize',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['plone'],
      include_package_data=True,
      zip_safe=False,
      extras_require=dict(
          test=[
            'zope.configuration',
            'zope.publisher',
            'zope.testing',
            'zope.app.component',
            'zope.app.testing',
          ]
      ),
      install_requires=[
        'setuptools',
        'zope.annotation',
        'zope.component',
        'zope.interface',
        'zope.app.cache',
        # 'Zope2',
      ],
      )
