"""A flexible caching decorator.

This module provides a cache decorator `cache` that you can use to
cache results of your functions or methods.  Let's say we have a class
with an expensive method `pow` that we want to cache:

  >>> class MyClass:
  ...     def pow(self, first, second):
  ...         print 'Someone or something called me'
  ...         return first ** second

Okay, we know that if the `first` and `second` arguments are the same,
the result is going to be the same, always.  We'll use a cache key
calculator to tell the `cache` decorator about this assertion.  What's
this cache key calculator?  It's a function that takes exactly the
same arguments as the original function that we're caching:

  >>> def cache_key(self, first, second):
  ...     return hash((first, second))

The cache decorator is really simple to use.  Let's define our first
class again, this time with a cached `pow` method:

  >>> class MyClass:
  ...     @cache(cache_key)
  ...     def pow(self, first, second):
  ...         print 'Someone or something called me'
  ...         return first ** second

The results:

  >>> obj = MyClass()
  >>> obj.pow(3, 2)
  Someone or something called me
  9
  >>> obj.pow(3, 2)
  9

Did you see that?  The method was called only once.

Now to where this cache is stored: That's actually variable.  The
cache decorator takes an optional second argument with which you can
define the where the cache is stored to.

By default, the cache stores its values on the first argument to the
function.  For our method, this is self, which is perfectly fine.  For
normal functions, the first argument is maybe not the best place to
store the cache.

The default cache container function stores a dictionary on the
instance as a *volatile* attribute.  That is, it's prefixed with
``_v_``.  In Zope, this means that the cache is not persisted.

  >>> ATTR
  '_v_memoize_cache'
  >>> cache_container = getattr(obj, ATTR)

This cache container maps our key to the return value.

  >>> cache_container[cache_key(None, 3, 2)]
  9
  >>> len(cache_container)
  1

Okay, on to storing the cache somewhere else.  The function we'll have
to provide is really similar to the cache key function we defined
earlier.

Like the cache key function, the storage function takes the same
amount of arguments as the original cached function.  We'll use a
global for caching this time:

  >>> my_cache = {}
  >>> def cache_storage(*args, **kwargs):
  ...     return my_cache

This time, instead of caching a method, we'll cache a normal function.
For this, we'll need to change our cache key function to take the
correct number of arguments:

  >>> def cache_key(first, second):
  ...     return hash((first, second))    

Note how we provide both the cache key generator and the cache storage
as arguments to the `cache` decorator:

  >>> @cache(cache_key, cache_storage)
  ... def pow(first, second):
  ...     print 'Someone or something called me'
  ...     return first ** second

Let's try it out:

  >>> pow(3, 2)
  Someone or something called me
  9
  >>> pow(3, 2)
  9
  >>> pow(3, 2)
  9
  >>> pow(3, 3)
  Someone or something called me
  27
  >>> pow(3, 3)
  27

It works!
"""

ATTR = '_v_memoize_cache'

def store_on_self(obj, *args, **kwargs):
    return obj.__dict__.setdefault(ATTR, {})

def store_on_context(obj, *args, **kwargs):
    return obj.context.__dict__.setdefault(ATTR, {})

def cache(get_key, get_cache=store_on_self):
    def decorator(fun):
        def replacement(*args, **kwargs):
            key = get_key(*args, **kwargs)
            cache = get_cache(*args, **kwargs)
            cached_value = cache.get(key)
            if cached_value is None:
                cache[key] = fun(*args, **kwargs)
            return cache[key]
        return replacement
    return decorator
