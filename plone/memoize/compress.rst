XHTML Compressor
================

In order to use Peter Bengtsson's slimmer library available from http://www.issuetrackerproduct.com/Download#slimmer you need to register the XHTMLSlimmer utility like this:

::
  <utility component="plone.memoize.compress.xhtmlslimmer"
           provides="plone.memoize.interfaces.IXHTMLCompressor" />

You can register other XHTML-whitespace removal libraries as well.

Per default there is no compressor available and we get the same string back:

::
    >>> html_string = u"<html><body><SPAN>Hello.</SPAN></body><html>"
    >>> xhtml_compress(html_string) is html_string
    True

Make a stupid lowercasing compressor.
This is not safe as it would lowercase all text outside of tags as well:

::
    >>> class LowerCaser(object):
    ...     implements(IXHTMLCompressor)
    ...
    ...     def compress(self, string):
    ...         return string.lower()

    >>> lower = LowerCaser()

Register our new compressor:

::
    >>> from zope.component import getSiteManager
    >>> sm = getSiteManager()
    >>> sm.registerUtility(lower)

    >>> xhtml_compress(html_string)
    u'<html><body><span>hello.</span></body><html>'

