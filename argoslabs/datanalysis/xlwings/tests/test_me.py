#!/usr/bin/env python
# coding=utf8
"""
====================================
 :mod:argoslabs.datanalysis.seaborn
====================================
.. moduleauthor:: Kyobong An <akb0930@argos-labs.com>
.. note:: ARGOS-LABS License

Description
===========
ARGOS LABS plugin module : unittest
"""

################################################################################
import os
import sys
from unittest import TestCase
from argoslabs.datanalysis.xlwings import _main as main


################################################################################
class TU(TestCase):
    # ==========================================================================
    @classmethod
    def setUpClass(cls) -> None:
        os.chdir(os.path.dirname(__file__))

    # ==========================================================================
    def test0001_failure(self):
        try:
            r = main()
            self.assertTrue(False)
        except Exception as e:
            sys.stderr.write('\n%s\n' % str(e))
            self.assertTrue(True)
    # ==========================================================================
    def test0110_relplot_sheet(self):
        try:
            r = main('anscombe.csv',
                     '--sheet-name', 'Sheet2',
                     '--output', 'relplot1.png')
            self.assertTrue(r == 0)
        except Exception as e:
            sys.stderr.write('\n%s\n' % str(e))
            self.assertTrue(False)

    # ==========================================================================