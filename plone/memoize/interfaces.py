from zope import interface

class IRAMCacheChooser(interface.Interface):
    def __call__(fun_name):
        """Return an IRAMCache based on a dotted function name
        `fun_name`.
        """
