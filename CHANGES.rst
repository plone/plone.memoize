Changelog
=========

.. You should *NOT* be adding new change log entries to this file.
   You should create a file in the news directory instead.
   For helpful instructions, please see:
   https://github.com/plone/plone.releaser/blob/master/ADD-A-NEWS-ITEM.rst

.. towncrier release notes start

3.0.2 (2023-06-23)
------------------

Internal:


- Update configuration files.
  [plone devs] (237ff4c8)


3.0.1 (2023-04-14)
------------------

Internal:


- Update configuration files.
  [plone devs] (93e1ab65)
- Removed more Python 2 compatibility code.
  [maurits] (#55)


3.0.0 (2022-10-28)
------------------

Breaking changes:


- Drop support for Python 3.5 and 3.6.
  Add support for Python 3.9, 3.10, and 3.11. [davisagli] (#27)


2.1.1 (2021-07-28)
------------------

Bug fixes:


- Work in a FIPS enabled environment by using SHA1 instead of MD5 for computing the cache key. [frapell] (#25)


2.1.0 (2020-04-20)
------------------

New features:


- Drop 3.4 support, add 3.7, 3.8, PyPy, PyPy3 support.
  [maurits] (#16)
- Use the zope global request if available as a fallback if the context does not have it [ale-rt] (#17)


Bug fixes:


- Make code black [ale-rt] (#17)
- Improve speed when getting resources from the cache [ale-rt] (#19)
- Remove ``bootstrap-buildout.py``. If you use buildout, use virtualenv and pip install zc.buildout instead.
  Add [isort] and [flake8] config sections into setup.cfg.
  Sort all imports in Python files.
  [thet] (#21)


2.0.1 (2019-04-29)
------------------

Bug fixes:


- Fix broken tests in TravisCI
  (`#12 <https://github.com/plone/plone.memoize/issues/12>`_)
  [andbag] (#12)


2.0.0 (2019-02-08)
------------------

Breaking changes:


- Relicensed under BSD (documented September 2010,
  https://plone.org/foundation/materials/foundation-resolutions/plone-framework-components-relicensing-policy)
  [andbag] (#12)


Bug fixes:


- Clean up package here and there. [gforcada] [mauritsvanrees] (#15)


1.2.3 (2018-09-26)
------------------

Bug fixes:

- Re-enable Travis-CI.
  This package can be used outside Plone so it should be tested outside, too.
  [howitz]


1.2.2 (2018-02-23)
------------------

Bug fixes:

- Drop travis and tox. A solution that works at one point does not necessarily work later.
  plone.memoize is being tested on jenkins.plone.org.
  [gforcada]

- Clean up dependencies.
  [gforcada]


1.2.1 (2017-07-03)
------------------

New:

- Keep docstrings intact in decorators.
  [pgrunewald]

Fixes:

- Update Travis setup (drop Python2.6, tolerate failing pypy3)
  [pgrunewald]


1.2.0 (2016-02-12)
------------------

New:

- Dropped official support for Plone 4 and Python 2.6.  [maurits]

- Python 3 compatibility.  [tomgross]

Fixes:

- Replace deprecated ``zope.testing.doctest`` import with ``doctest`` module
  from stdlib.
  [thet]


1.1.2 (2016-01-08)
------------------

Fixes:

- Restructure docs.
  [thet]

- Minor PEP 8.
  [thet]


1.1.1 (2011-05-12)
------------------

- Add MANIFEST.in.
  [WouterVH]


1.1 (2010-07-18)
----------------

- Update license to GPL version 2 only.
  [hannosch]

- Solve intermittent error during testing of CleanupDict class, as a
  cleanup period of zero seconds would not always result in a cleanup,
  if the tests were run fast.
  [maurits]


1.1b1 (2009-11-13
------------------

- Updated package documentation.
  [hannosch]


1.1a4 (2009-07-23)
------------------

- Use the new `zope.ramcache` package instead of `zope.app.cache`. This
  reduces our dependencies by quite a bit.
  [hannosch]


1.1a3 (2009-05-10)
------------------

- Modernized and cleaned up the code a bit. Also drop BBB support for
  `zope.app.annotation` and made the tests work again.
  [hannosch]


1.1a2 (2009-05-08)
------------------

- Removed all testing dependencies on zope.app packages.
  [hannosch]

- Changed a test to use zope.publisher instead of a Five BrowserView. This
  removes the entire Zope2 dependency.
  [hannosch]

- Correct Zope2 dependency, it's indeed only a test dependency.
  [hannosch]


1.1a1 (2009-04-04)
------------------

- Clarified license statements.
  [hannosch]

- Moved declaration of test dependencies into a test extra.
  [hannosch]

- Avoid deprecation warnings for the md5 and sha modules in Python 2.6.
  [hannosch]

- Specify package dependencies.
  [hannosch]

- Added check for Unicode values in cache keys before calculating md5
  checksums, as the md5 module doesn't seem to like Unicode.
  [hannosch]

- Removed BBB code for zope.app.annotation.
  [hannosch]

- The clearbefore decorator was mistakenly not tested.
  [maurits]


1.0.4 (2008-03-31)
------------------

- Documentation and release notes cleanup.
  [hannosch]


1.0.3 (2007-11-09)
------------------

- Remove features from Plone 3.0 branch.
  [nouri]

- Maintenance branch for Plone 3.0.
  [nouri]

- Get rid of sys.modules hack, which according to this changeset:
  http://dev.plone.org/plone/changeset/15030
  was added because I advised it generally.  With help from Kapil for
  the PloneGetPaid project I figured out a better way.
  [maurits]

- Revise docs and project description.
  [nouri]

- Merge patch from Gael Le Mignot:

    - Do not use hash anymore when making cache keys. This is to
      avoid cache collisions, and to avoid a potential security
      problem where an attacker could manually craft collisions.
      Also, stop recommending the use of hash() in tests.

    - Add support for using Pilot System's GenericCache as a backend
      for 'plone.memoize.volatile.cache'.

    - Add an arguments marshaller that gives you a more convenient
      way to declare that your cache is dependent on arguments.
      See 'plone.memoize.marshallers'.

  [nouri, gael]


1.0.1 (2007-09-10)
------------------

- Simplify forever by reuse of stuff from plone.memoize.volatile.
  [nouri]


1.0 (2007-08-17)
----------------

- Add a forever memo - lives until Zope restart.
  [optilude]

- hash((1, 2)) returns something different on ree's 64-bit Python :)
  [nouri]

- Don't treat None in a special way. Avoid one dict lookup.
  [nouri]

- Extended the xhtml_compress method to use a utility lookup for
  IXHTMLCompressor utilities instead. Now you can turn the slimmer based
  compression on via a simple utility registration. See compress.py.
  [hannosch, fschulze]


1.0rc2 (2007-07-27)
-------------------

- Added simple xhtml_compress method which can be used to plug in
  whitespace removal libraries. Peter Bengtsson's slimmer library is
  configured but not enabled by default.
  [hannosch]


1.0b4 (2007-07-09)
------------------

- Use a md5 hash of the provided key in RAMCacheAdapter, reducing the
  memory footprint and speeding up lookup time.
  [hannosch]

- Reword the volatile section a bit to indicate why the example does not
  use anything from the volatile module.
  [wichert]

- Use an exception `DontCache` instead of the DONT_CACHE marker return
  value. Allow for no `ICacheChooser` to be registered.
  [nouri]

- Add cache decorator for request (which can in fact be used for all
  sorts of annotatable objects).
  [nouri]

- Added decorator for storing cache values on the request as annotations.
  [nouri]

- Always include the function's dotted name in the key.
  [nouri]

- Added a new cache decorator which can memoize a the result of a method
  call on the request and lets you specify which argument on the function
  is the request.
  [hannosch]

- Add MemcacheAdapter as an alternative to RAMCacheAdapter.
  [nouri]

- Generalize `IRAMCacheChooser` to `ICacheChooser`, which doesn't return
  an IRAMCache but a simple dict.
  [nouri]

- Use a more sensible default for the maxAge of the new RAMCache.
  [hannosch]

- Add cache storage for `plone.memoize.volatile` for use with
  `zope.app.cache.ram.RAMCache`.
  [nouri]

- Rolled in changes from memojito to fix recursively memoized
  methods(fix by Rob Miller and Whit Morriss)
  [whit]

- Made plone.memoize backwardly compatible with zope2.9 and remain
  usable w/out zope.annotation. Minor wording changes to some docs.
  [whit]

- Per default, use a volatile dict that cleans up after itself.
  [nouri]

- This 'volatile' module defines a versatile caching decorator that
  gives you total control of how the cache key is calculated and where
  it is stored.
  [nouri]


1.0b3 (2007-05-05)
------------------

- Initial package structure and implementation.
  [hannosch, nouri, optilude, whit, zopeskel]
