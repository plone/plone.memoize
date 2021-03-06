Volatile Decorators
===================

A flexible caching decorator.

Make necessary imports::

    >>> from plone.memoize.volatile import ATTR
    >>> from plone.memoize.volatile import cache
    >>> from plone.memoize.volatile import DontCache
    >>> from plone.memoize.volatile import CleanupDict

This module provides a cache decorator `cache` that you can use to cache results of your functions or methods.
Let's say we have a class with an expensive method `pow` that we want to cache::

    >>> class MyClass:
    ...     def pow(self, first, second):
    ...         """Returns the number 'first' to the power of 'second'."""
    ...         print('Someone or something called me')
    ...         return first ** second

Okay, we know that if the `first` and `second` arguments are the same, the result is going to be the same, always.
We'll use a cache key calculator to tell the `cache` decorator about this assertion.
What's this cache key calculator?
It's a function that takes the original function plus the same arguments as the original function that we're caching::

    >>> def cache_key(method, self, first, second):
    ...     return (first, second)

For performances and security reasons, no hash is done on the key in this example.
You may consider using a cryptographic hash (MD5 or even better SHA1) if your parameters can hold big amount of data.

The cache decorator is really simple to use.
Let's define our first class again, this time with a cached `pow` method::

    >>> class MyClass:
    ...     @cache(cache_key)
    ...     def pow(self, first, second):
    ...         """Returns the number 'first' to the power of 'second'."""
    ...         print('Someone or something called me')
    ...         return first ** second

The results::

    >>> obj = MyClass()
    >>> obj.pow(3, 2)
    Someone or something called me
    9
    >>> obj.pow(3, 2)
    9

Did you see that?  The method was called only once.

You can also see, that the method's docstring is still intact::

    >>> obj.pow.__doc__
    "Returns the number 'first' to the power of 'second'."

Now to where this cache is stored: That's actually variable.
The cache decorator takes an optional second argument with which you can define the where the cache is stored to.

By default, the cache stores its values on the first argument to the function.
For our method, this is self, which is perfectly fine.
For normal functions, the first argument is maybe not the best place to store the cache.

The default cache container function stores a dictionary on the instance as a *volatile* attribute.
That is, it's prefixed with ``_v_``.
In Zope, this means that the cache is not persisted::

    >>> ATTR
    '_v_memoize_cache'
    >>> cache_container = getattr(obj, ATTR)

This cache container maps our key, including the function's dotted name, to the return value::

    >>> cache_container # doctest: +ELLIPSIS
    {'None.pow:...': 9}
    >>> len(cache_container)
    1
    >>> k = 'None.pow:%s' % str(cache_key(MyClass.pow, None, 3, 2))
    >>> cache_container[k]
    9

Okay, on to storing the cache somewhere else.
The function we'll have to provide is really similar to the cache key function we defined earlier.

Like the cache key function, the storage function takes the same amount of arguments as the original cached function.
We'll use a global for caching this time::

    >>> my_cache = {}
    >>> def cache_storage(fun, *args, **kwargs):
    ...     return my_cache

This time, instead of caching a method, we'll cache a normal function.
For this, we'll need to change our cache key function to take the correct number of arguments::

    >>> def cache_key(fun, first, second):
    ...     return (first, second)

Note how we provide both the cache key generator and the cache storage as arguments to the `cache` decorator::

    >>> @cache(cache_key, cache_storage)
    ... def pow(first, second):
    ...     print('Someone or something called me')
    ...     return first ** second

Let's try it out::

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
    >>> my_cache.clear()

It works!

A cache key generator may also raise DontCache to indicate that no caching should be applied::

    >>> def cache_key(fun, first, second):
    ...     if first == second:
    ...         raise DontCache
    ...     else:
    ...         return (first, second)
    >>> @cache(cache_key, cache_storage)
    ... def pow(first, second):
    ...     print('Someone or something called me')
    ...     return first ** second

    >>> pow(3, 2)
    Someone or something called me
    9
    >>> pow(3, 2)
    9
    >>> pow(3, 3)
    Someone or something called me
    27
    >>> pow(3, 3)
    Someone or something called me
    27

Caveats
-------

Be careful when you have multiple methods with the same name in a single module::

    >>> def cache_key(fun, instance, *args):
    ...     return args
    >>> cache_container = {}
    >>> class A:
    ...     @cache(cache_key, lambda *args: cache_container)
    ...     def somemet(self, one, two):
    ...         return one + two
    >>> class B:
    ...     @cache(cache_key, lambda *args: cache_container)
    ...     def somemet(self, one, two):
    ...         return one - two
    >>> a = A()
    >>> a.somemet(1, 2)
    3
    >>> cache_container
    {'None.somemet:(1, 2)': 3}

The following call should really return -1, but since the default cache key isn't clever enough to include the function's name, it'll return 3::

    >>> B().somemet(1, 2)
    3
    >>> len(cache_container)
    1
    >>> cache_container.clear()

Ouch!
The fix for this is to e.g. include your class' name in the key when you create it::

    >>> def cache_key(fun, instance, *args):
    ...     return (instance.__class__,) + args
    >>> class A:
    ...     @cache(cache_key, lambda *args: cache_container)
    ...     def somemet(self, one, two):
    ...         return one + two
    >>> class B:
    ...     @cache(cache_key, lambda *args: cache_container)
    ...     def somemet(self, one, two):
    ...         return one - two
    >>> a = A()
    >>> a.somemet(1, 2)
    3
    >>> B().somemet(1, 2)
    -1
    >>> len(cache_container)
    2


Cleanup Dict
------------

CleanupDict is a dict that automatically cleans up items that haven't been accessed in a given timespan on *set*.

This implementation is a bit naive, since it's not associated with any policy that the user can configure, and it doesn't provide statistics like RAMCache, but at least it helps make sure our volatile attribute doesn't grow stale entries indefinitely.

::

    >>> d = CleanupDict()
    >>> d['spam'] = 'bar'
    >>> d['spam']
    'bar'

Setting the cleanup period to 0 (or a negative number) means the values are thrown away immediately.
(Note that we do not test with exactly zero, as running the tests can go too fast.)

::

    >>> d = CleanupDict(-0.00001)
    >>> d['spam'] = 'bar'
    >>> d['spam'] # doctest: +ELLIPSIS
    Traceback (most recent call last):
    ...
    KeyError: 'spam'

