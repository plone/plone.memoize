"""XHTML Compressor
"""

from plone.memoize.interfaces import IXHTMLCompressor
from zope.component import queryUtility


def xhtml_compress(string):
    util = queryUtility(IXHTMLCompressor)
    if util is not None:
        return util.compress(string)
    return string
