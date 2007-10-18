"""
Decorator using GenericCache as a back-end store.

By default, it uses a global GenericCache, with a default policy of
storing 1000 objects for at most one hour (3600 seconds). You can
reconfigure the policy of the default cache, or use your own cache.

Only a few tests were added in this docstring, there is a full test
suite inside the GenericCache module itself.

  >>> from plone.memoize.marshallers import args_marshaller
  >>> @cache(args_marshaller())
  ... def pow(first, second):
  ...     print 'Someone or something called me'
  ...     return first ** second

  >>> pow(3, 2)
  Someone or something called me
  9
  >>> pow(3, 2)
  9
  >>> global_cache.clear()
  >>> pow(3, 2)
  Someone or something called me
  9
  >>> pow(3, 2)
  9

Create a new local cache that can hold only two objects:

  >>> storage = new_storage(maxsize = 2)
  >>> @cache(args_marshaller(), storage)
  ... def pow(first, second):
  ...     print 'Someone or something called me'
  ...     return first ** second

  >>> pow(3, 2)
  Someone or something called me
  9
  >>> pow(3, 2)
  9
  >>> pow(2, 2)
  Someone or something called me
  4
  >>> pow(2, 3)
  Someone or something called me
  8
  >>> pow(3, 2)
  Someone or something called me
  9
  >>> pow(2, 3)
  8


"""

from plone.memoize import volatile
from GenericCache import GenericCache

def new_storage(maxsize = 1000, expiry = 3600):
    """
    Get a new storage area
    """
    return GenericCache(maxsize = maxsize, expiry = expiry, default_fail = True)

global_cache = new_storage()

def cache(get_key, storage=global_cache):
    """
    The cache decorator
    """
    def decorator(fun):
        def get_cache(fun, *args, **kwargs):
            return storage
        return volatile.cache(get_key, get_cache)(fun)
    return decorator

__all__ = (new_storage, cache, global_cache)
