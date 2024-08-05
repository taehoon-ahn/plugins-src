#!/usr/bin/env python
# coding=utf8
"""
====================================


====================================
.. moduleauthor:: taehoon ahn <highlugh@vivans.net>
.. note:: ARGOS-LABS License

Description
===========
ARGOS LABS plugin module for string regular-expression operation
"""
# Authors
# ===========
#
# * Taehoon ahn
#
# Change Log
# --------
#
#  * [2023/08/22]
#     - starting

################################################################################
import os
import sys
import random
from alabs.common.util.vvargs import ModuleContext, func_log, \
    ArgsError, ArgsExit, get_icon_path


################################################################################
@func_log
def do_passwdgen(mcxt, argspec):
    """
    plugin job function
    :param mcxt: module context
    :param argspec: argument spec
    :return: 0 for success
    """
    try:
        mcxt.logger.info('>>>starting...')

        start_letter = argspec.first_alphabet.lower()
        end_letter = argspec.last_alphabet.lower()

        start_ord = ord(start_letter)
        end_ord = ord(end_letter)
        random_ord = random.randint(start_ord, end_ord)
        random_letter = chr(random_ord)
        print(random_letter)
        return 0
    except Exception as e:
        msg = str(e)
        mcxt.logger.error(msg)
        sys.stderr.write('%s%s' % (msg, os.linesep))
        return 1
    finally:
        sys.stdout.flush()
        mcxt.logger.info('>>>end...')


################################################################################
def _main(*args):
    """
    Build user argument and options and call plugin job function
    :param args: user arguments
    :return: return value from plugin job function
    """
    with ModuleContext(
        owner='ARGOS-LABS',
        group='9',  # Utility Tools
        version='1.0',
        platform=['windows', 'darwin', 'linux'],
        output_type= 'text',
        display_name='Random Alphabet',
        icon_path=get_icon_path(__file__),
        description='This plugin is for randomalphabet',
    ) as mcxt:
        # ##################################### for app dependent parameters
        mcxt.add_argument('first_alphabet',
                          display_name='First_alphabet',
                          default=0, type=str,
                          help='Random alphabet. First_num [[a]]')
        mcxt.add_argument('last_alphabet',
                          display_name='Last_alphabet', type=str,
                          help='last_Random alphabet.')
        # ##################################### for app dependent options


        argspec = mcxt.parse_args(args)
        return do_passwdgen(mcxt, argspec)


################################################################################
def main(*args):
    try:
        return _main(*args)
    except ArgsError as err:
        sys.stderr.write('Error: %s\nPlease -h to print help\n' % str(err))
    except ArgsExit as _:
        pass
