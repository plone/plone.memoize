==============================
 plone memoization decorators
==============================

Used to memoize the return values of functions and properties of classes
or views.

See view.txt and instance.txt for usage, but the most common usage pattern
is:

 from plone.memoize import instance

 class MyClass(object):
 
    @instance.memoize
    def some_expensive_function(self, arg1, arg2):
        ...

The first time some_expensive_function() is called, the return value will
be saved. On subsequent calls with the same arguments, the cached version
will be returned. Passing in different arguments will cause the function to
be called again.

Note that this only works if the arguments are hashable!

If you are writing a Zope 3 view, you can do:

 from plone.memoize import view

 class MyView(BrowserView):
 
    @view.memoize
    def some_expensive_function(self, arg1, arg2):
        ...

This has the same effect, but subsequent lookup of the same view in the
same context will be memoized as well.

You can also use @view.memoize_contextless to have the memoization not
take the context into account - the same view looked up during the same
request (but possibly on another context) with the same parameters will 
be memoized.

Note that this requires that the request is annotatable using zope.annotation!