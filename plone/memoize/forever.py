"""
Memo decorators for globals - memoized values survive for as long as the
process lives.

Stores values in a module-level variable.
"""

_marker = object()
_memos = {} # dict of dotted names to dict of cached values

class ForeverMemo(object):
    
    def memoize(self, func):
        def memogetter(*args, **kwargs):
            global _memos
            
            object_key = self.object_key(func)
            cache = _memos.setdefault(object_key, {})
            
            # XXX this could be improved to unfold unhashables
            # and optimized with pyrex

            key = hash((args, frozenset(kwargs.items()),))
            val = cache.get(key, _marker)
            
            if val is _marker:
                val=func(*args, **kwargs)
                cache[key]=val
            return val
        return memogetter
        
    def object_key(self, func):
        method = hasattr(func, 'im_class')
        if method:
            return "%s.%s.%s" % (func.__module__, func.im_class.__name__, func.__name__,)
        else:
            return "%s.%s" % (func.__module__, func.__name__,)

_m = ForeverMemo()
memoize = _m.memoize

def memoizedproperty(func):
    return property(_m.memoize(func))

__all__ = (memoize, memoizedproperty)
