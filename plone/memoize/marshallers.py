"""A few general-purpose marshallers you can use to generate cache keys.

See README.txt for more details.

  >>> from ram import cache
  >>> @cache(args_marshaller())
  ... def pow(first, second):
  ...     print 'Someone or something called me'
  ...     return first ** second

  >>> pow(3, 2)
  Someone or something called me
  9
  >>> pow(3, 2)
  9

Let's cache another function:

  >>> @cache(args_marshaller())
  ... def add(first, second):
  ...     print 'Someone or something called me'
  ...     return first + second

  >>> add(3, 2)
  Someone or something called me
  5
  >>> add(3, 2)
  5

Now let's cache a function that requires hashing:

  >>> try:
  ...     from hashlib import sha1 as sha
  ... except ImportError:
  ...     import sha
  >>> @cache(args_marshaller(hashing = sha))
  ... def count_words(text):
  ...     print 'Someone or something called me'
  ...     return len(text.split())

  >>> count_words('foo ' * 100)
  Someone or something called me
  100
  >>> count_words('foo ' * 102)
  Someone or something called me
  102
  >>> count_words('foo ' * 100)
  100

And now one function that uses a global variable:

  >>> counter = 0
  >>> def get_counter(*args, **kwargs):
  ...     return (counter, )
  >>> @cache(args_marshaller(extra = get_counter))
  ... def increase(nb):
  ...     print 'Someone or something called me'
  ...     return counter + nb

  >>> counter = increase(2)
  Someone or something called me
  >>> counter
  2
  >>> counter = increase(2)
  Someone or something called me
  >>> counter
  4
  >>> counter = increase(-4)
  Someone or something called me
  >>> counter
  0
  >>> counter = increase(2)
  >>> counter
  2
  >>> counter = increase(2)
  >>> counter
  4

"""

def args_marshaller(hashing = None, extra = None):
    """
    Creates a args-based marshaller
    Can specify hashing type if wanted (use a hash module, like md5 or sha).
    The hashing type needs to be either a factory returning a new hash value
    or has a new function that does so.

    Can also sepcify extra arguments, which can must be a callable object,
    receiving (func, *args, **kwargs) as paramaters and returning a tuple
    """
    def marshaller(func, *args, **kwargs):    
        key =  (func.__module__, func.__name__, tuple(args),
                tuple(kwargs.items()))

        if callable(extra):
            key += tuple(extra(func, *args, **kwargs))

        if hashing:
            if hasattr(hashing, 'new'):
                new = hashing.new
            else:
                new = hashing

            key = new(str(key)).hexdigest()
        return key
    
    return marshaller

