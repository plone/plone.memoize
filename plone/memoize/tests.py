# -*- coding: utf-8 -*-
from zope.component.testing import setUp, tearDown
from zope.configuration.xmlconfig import XMLConfig
from zope.testing import doctest
import unittest

optionflags = doctest.REPORT_ONLY_FIRST_FAILURE | doctest.ELLIPSIS


def configurationSetUp(test):
    setUp()
    import zope.component
    XMLConfig('meta.zcml', zope.component)()
    import plone.memoize
    XMLConfig('configure.zcml', plone.memoize)()


def test_suite():
    tests = (
        doctest.DocTestSuite('README.rst',
                             package="plone.memoize",
                             setUp=configurationSetUp,
                             tearDown=tearDown,
                             optionflags=optionflags),
        doctest.DocTestSuite('compress.rst',
                             package="plone.memoize",
                             setUp=configurationSetUp,
                             tearDown=tearDown,
                             optionflags=optionflags),
        doctest.DocTestSuite('forever.rst',
                             package="plone.memoize",
                             setUp=configurationSetUp,
                             tearDown=tearDown,
                             optionflags=optionflags),
        doctest.DocTestSuite('instance.rst',
                             package="plone.memoize",
                             setUp=configurationSetUp,
                             tearDown=tearDown,
                             optionflags=optionflags),
        doctest.DocTestSuite('ram.rst',
                             package="plone.memoize",
                             setUp=configurationSetUp,
                             tearDown=tearDown,
                             optionflags=optionflags),
        doctest.DocTestSuite('request.rst',
                             package="plone.memoize",
                             setUp=configurationSetUp,
                             tearDown=tearDown,
                             optionflags=optionflags),
        doctest.DocTestSuite('view.rst',
                             package="plone.memoize",
                             setUp=configurationSetUp,
                             tearDown=tearDown,
                             optionflags=optionflags),
        doctest.DocTestSuite('volatile.rst',
                             package="plone.memoize",
                             setUp=configurationSetUp,
                             tearDown=tearDown,
                             optionflags=optionflags),
    )

    return unittest.TestSuite(tests)
