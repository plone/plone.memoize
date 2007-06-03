from zope import interface

class ICacheChooser(interface.Interface):
    def __call__(fun_name):
        """Return a cache with a dict interface based on a dotted
        function name `fun_name`.

        May return None to indicate that there is no cache available.
        """
