import os, sys, unittest

from zope.testing import doctest

from zope.app.testing.placelesssetup import setUp, tearDown
from zope.configuration.xmlconfig import XMLConfig

optionflags = doctest.REPORT_ONLY_FIRST_FAILURE | doctest.ELLIPSIS

import zope.app.component
import plone.memoize

def configurationSetUp(test):
    setUp()    
    
    XMLConfig('meta.zcml', zope.app.component)()
    XMLConfig('configure.zcml', plone.memoize)()

def configurationTearDown(test):
    tearDown()

def test_suite():
    return unittest.TestSuite((
        doctest.DocFileSuite('instance.txt', 
                             package="plone.memoize",
                             setUp=configurationSetUp,
                             tearDown=configurationTearDown,
                             optionflags=optionflags),
        doctest.DocFileSuite('view.txt', 
                             package="plone.memoize",
                             setUp=configurationSetUp,
                             tearDown=configurationTearDown,
                             optionflags=optionflags),
        ))

if __name__=="__main__":
    import unittest
    unittest.TextTestRunner().run(test_suite())