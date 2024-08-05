"""
====================================
 :mod:`argoslabs.text.figlet`
====================================
.. moduleauthor:: Jerry Chae <mcchae@argos-labs.com>
.. note:: ARGOS-LABS License

Description
===========
ARGOS LABS plugin module to use Selenium
"""
# Authors
# ===========
#
# * taehoon ahn
#
# Change Log
# --------
#
#  * [2022/08/22]
#     - starting

################################################################################
import os
import sys
from unittest import TestCase
from argoslabs.text.figlet import _main as main


################################################################################
class TU(TestCase):
    # ==========================================================================
    def setUp(self) -> None:
        os.chdir(os.path.dirname(__file__))

    # ==========================================================================
    def test0000_init(self):
        ...

    # ==========================================================================
    def test0010_fail_empty(self):
        # sg = sys.gettrace()
        # if sg is None:  # Not in debug mode
        #     print('Skip testing at test/build time')
        #     return
        try:
            _ = main('')
            self.assertTrue(False)
        except Exception as e:
            sys.stderr.write('\n%s\n' % str(e))
            self.assertTrue(True)

    # ==========================================================================
    def test0110_success(self):
        of = 'stdout.txt'
        try:
            r = main('standard',
                     'Hello world?',
                     '--outfile', of)
            self.assertTrue(r == 0)
            with open(of) as ifp:
                rs = ifp.read()
                print(rs)
            self.assertTrue(True)
        except Exception as e:
            sys.stderr.write('\n%s\n' % str(e))
            self.assertTrue(False)
        finally:
            if os.path.exists(of):
                os.remove(of)
    # ==========================================================================
    def test9999_quit(self):
        self.assertTrue(True)
