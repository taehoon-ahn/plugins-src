#!/usr/bin/env python
# coding=utf8
"""
====================================


====================================
.. moduleauthor:: Jerry Chae <mcchae@argos-labs.com>
.. note:: ARGOS-LABS License

Description
===========
ARGOS LABS plugin module : unittest
"""
# Authors
# ===========
#
# * taehoon ahn
#
# Change Log
# --------

#  * [2023/08/22]
#     - starting

################################################################################
import sys
from unittest import TestCase
from argoslabs.string.randomalphabet import _main as main
from contextlib import contextmanager
from io import StringIO

################################################################################
@contextmanager
def captured_output():
    new_out, new_err = StringIO(), StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err


################################################################################
class TU(TestCase):
    """
    TestCase for argoslabs.demo.helloworld
    """
    # ==========================================================================
    def setUp(self) -> None:
        ...

    # ==========================================================================
    def tearDown(self) -> None:
        ...

    # ==========================================================================
    def test0000_init(self):
        self.assertTrue(True)

    # ==========================================================================
    def test0010_invalid_length(self):
        stderr = None
        try:
            _ = main('unknown')
            self.assertTrue(False)
        except Exception as e:
            sys.stderr.write('%s\n' % str(e))
            self.assertTrue(True)

    # ==========================================================================
    def test0110_success(self):
        try:
            with captured_output() as (out, err):
                r = main('a','z')
            self.assertTrue(r == 0)
            stdout = out.getvalue().strip()
            if stdout:
                print(stdout)
        except Exception as e:
            sys.stderr.write('%s\n' % str(e))
            self.assertTrue(False)

    # ==========================================================================
