"""Memoize decorator for views.

Stores values in an annotation of the request. See view.rst.
"""
from functools import wraps
from zope.annotation.interfaces import IAnnotations
from zope.globalrequest import getRequest


class ViewMemo:
    key = "plone.memoize"

    def memoize(self, func):
        @wraps(func)
        def memogetter(*args, **kwargs):
            instance = args[0]

            context = getattr(instance, "context", None)
            try:
                request = instance.request
            except AttributeError:
                request = getRequest()

            annotations = IAnnotations(request, {})
            if self.key not in annotations:
                annotations[self.key] = dict()
            cache = annotations[self.key]

            # XXX: Not the most elegant thing in the world; in a Zope 2
            # context, the physical path is a better key, since the id could
            # change if the object is invalidated from the ZODB cache

            try:
                context_id = context.getPhysicalPath()
            except AttributeError:
                context_id = id(context)

            # Note: we don't use args[0] in the cache key, since args[0] ==
            # instance and the whole point is that we can cache different
            # requests

            key = (
                context_id,
                instance.__class__.__name__,
                func.__name__,
                args[1:],
                frozenset(kwargs.items()),
            )
            if key not in cache:
                cache[key] = func(*args, **kwargs)
            return cache[key]

        return memogetter

    def memoize_contextless(self, func):
        def memogetter(*args, **kwargs):
            if args:
                instance = args[0]
            else:
                instance = None

            try:
                request = instance.request
            except AttributeError:
                request = getRequest()

            annotations = IAnnotations(request, {})
            if self.key not in annotations:
                annotations[self.key] = dict()
            cache = annotations[self.key]

            key = (
                instance.__class__.__name__,
                func.__name__,
                args[1:],
                frozenset(kwargs.items()),
            )
            if key not in cache:
                cache[key] = func(*args, **kwargs)
            return cache[key]

        return memogetter


_m = ViewMemo()
memoize = _m.memoize
memoize_contextless = _m.memoize_contextless

__all__ = (memoize, memoize_contextless)
