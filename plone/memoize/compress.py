# -*- coding: utf-8 -*-
"""XHTML Compressor
"""

from plone.memoize.interfaces import IXHTMLCompressor
from zope.component import queryUtility
from zope.interface import implements

SLIMMER = True
try:
    from slimmer import xhtml_slimmer
except ImportError:
    SLIMMER = False


def xhtml_compress(string):
    util = queryUtility(IXHTMLCompressor)
    if util is not None:
        return util.compress(string)
    return string


class XHTMLSlimmer(object):

    implements(IXHTMLCompressor)

    def compress(self, string):
        if SLIMMER:
            return xhtml_slimmer(string)
        return string

xhtmlslimmer = XHTMLSlimmer()
