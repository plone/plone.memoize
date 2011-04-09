plone.memoize
=============

plone.memoize provides Python function decorators for caching the
values of functions and methods.

The type of cache storage is freely configurable by the user, as is
the cache key, which is what the function's value depends on.

plone.memoize has support for memcached and is easily extended to use
other caching storages.  It also has specialized decorators for use
with Zope views.  However, plone.memoize can be used without Zope.
