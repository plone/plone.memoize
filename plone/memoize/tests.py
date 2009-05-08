import unittest

from zope.component.testing import setUp, tearDown
from zope.configuration.xmlconfig import XMLConfig
from zope.testing import doctest

import plone.memoize

optionflags = doctest.REPORT_ONLY_FIRST_FAILURE | doctest.ELLIPSIS


def configurationSetUp(test):
    setUp()
    XMLConfig('configure.zcml', plone.memoize)()


def test_suite():
    tests = (
        doctest.DocTestSuite('plone.memoize.compress',
                             setUp=configurationSetUp,
                             tearDown=tearDown),
        doctest.DocFileSuite('instance.txt', 
                             package="plone.memoize",
                             setUp=configurationSetUp,
                             tearDown=tearDown,
                             optionflags=optionflags,
                             globs=locals()),
        doctest.DocFileSuite('view.txt', 
                             package="plone.memoize",
                             setUp=configurationSetUp,
                             tearDown=tearDown,
                             optionflags=optionflags,
                             globs=locals()),
        doctest.DocFileSuite('forever.txt', 
                             package="plone.memoize",
                             setUp=configurationSetUp,
                             tearDown=tearDown,
                             optionflags=optionflags,
                             globs=locals()),
        doctest.DocFileSuite('README.txt'),
        doctest.DocTestSuite('plone.memoize.request',
                             setUp=configurationSetUp,
                             tearDown=tearDown),
        doctest.DocTestSuite('plone.memoize.volatile'),
        doctest.DocTestSuite('plone.memoize.ram',
                             setUp=configurationSetUp,
                             tearDown=tearDown),
        )

    return unittest.TestSuite(tests)
