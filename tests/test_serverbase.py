##############################################################################
#
# Copyright (c) 2005 Zope Corporation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""Tests for zope.server.serverbase

$Id$
"""
import unittest

from zope.testing import doctest


def doctest_ServerBase():
    r"""Regression test for ServerBase

    Bug: if the `ip` argument of ServerBase is a string containing a numberic
    IP address, and the verbose argument is enabled, ServerBase.__init__
    would try to use self.logger before it was initialized.

    We will use a subclass of ServerBase so that unit tests do not actually try
    to bind to ports.

        >>> from zope.server.serverbase import ServerBase
        >>> class ServerBaseForTest(ServerBase):
        ...     def bind(self, (ip, port)):
        ...         print "Listening on %s:%d" % (ip or '*', port)
        >>> sb = ServerBaseForTest('127.0.0.1', 80, start=False, verbose=True)
        Listening on 127.0.0.1:80

    """


def test_suite():
    return doctest.DocTestSuite()


if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
