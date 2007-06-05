"""
Memoize decorator for methods.

Stores values in an annotation of the request.
"""

from zope.annotation.interfaces import IAnnotations

_marker = object()
class RequestMemo(object):
    
    key = 'plone.memoize_request'

    def __init__(self, arg=0):
        self.arg = arg

    def __call__(self, func):
        def memogetter(*args, **kwargs):
            request = None
            if isinstance(self.arg, int):
                request = args[self.arg]
            else:
                request = kwargs[self.arg]

            annotations = IAnnotations(request)
            cache = annotations.get(self.key, _marker)
        
            if cache is _marker:
                cache = annotations[self.key] = dict()
        
            key = hash((func.__module__, func.__name__, 
                        args, frozenset(kwargs.items())),)
            value = cache.get(key, _marker)
            if value is _marker:
                value = cache[key] = func(*args, **kwargs)
            return value
        return memogetter

memoize_diy_request = RequestMemo

__all__ = (memoize_diy_request)
