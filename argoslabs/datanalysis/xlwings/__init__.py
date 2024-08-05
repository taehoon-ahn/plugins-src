#!/usr/bin/env python
# coding=utf8
"""
====================================
 :mod:`argoslabs.datanlaysis.xlwings`
====================================
.. moduleauthor:: Kyobong An <akb0930@argos-labs.com>
.. note:: ARGOS-LABS License

Description
===========
ARGOS LABS Data Visualization Tool using xlwings
"""
# Authors
# ===========
#
# * taehoon ahn
#  * [2023/07/31]
#     - starting

################################################################################
import os
import sys
import pandas as pd
from alabs.common.util.vvargs import ModuleContext, func_log, \
    ArgsError, ArgsExit, get_icon_path


################################################################################
# noinspection PyBroadException
class xlwings(object):
    def __init__(self, argspec):
        self.argspec = argspec
        self.data = self.get_data(argspec.filename, argspec.sheet_name, argspec.encoding)
        self.output = argspec.output

    # ==========================================================================
    @staticmethod
    def get_data(filename, sheet_name=None, encoding=None):
        if not os.path.exists(filename):
            raise IOError('Cannot read excel filename "%s"' % filename)
        ext = os.path.splitext(filename)[1]
        if ext.lower() in ('.csv', '.tsv'):
            df = pd.read_csv(filename, encoding=encoding)
        elif ext.lower() in ('.xls', '.xlsx'):
            if sheet_name:
                df = pd.read_excel(filename, sheet_name=sheet_name, engine='openpyxl')
            else:
                df = pd.read_excel(filename, engine='openpyxl')
        else:
            raise ReferenceError(
                f'Not supported file extension "{ext}" for input. '
                f'One of ".xls", ".xlsx", ".xlsm", ".csv", ".tsv"')
        return df

    def plot(self):
        if self.argspec.x == "":
            self.argspec.x = None

        if not self.output:
            self.output = os.path.dirname(self.argspec.filename) + '\\output.png'
        plt.savefig(self.output)
        print(self.output, end='')
        return 0


################################################################################
@func_log
def func(mcxt, argspec):
    mcxt.logger.info('>>>starting...')
    try:
        mat = xlwings(argspec)
        mat.plot()

        return 0
    except Exception as err:
        msg = str(err)
        mcxt.logger.error(msg)
        sys.stderr.write('%s%s' % (msg, os.linesep))
        return 1
    finally:
        sys.stdout.flush()
        mcxt.logger.info('>>>end...')


################################################################################
def _main(*args):
    with ModuleContext(
            owner='ARGOS-LABS',
            group='4',
            version='1.0',
            platform=['windows', 'darwin', 'linux'],
            output_type='csv',
            display_name='Taehoon Practice',
            icon_path=get_icon_path(__file__),
            description='Taehoon practice plugin',
    ) as mcxt:
        # #####################################  for app dependent parameters
        # ----------------------------------------------------------------------
        mcxt.add_argument('filename', display_name='Excel File',
                          input_method='fileread',
                          help='Excel or CSV filename to handle for reading. '
                               '(Note. CSV is converted to excel first. Too big'
                               ' CSV input can take time.)')
        # ----------------------------------------------------------------------
        # ######################################  for app optional parameters
        # ----------------------------------------------------------------------
        mcxt.add_argument('--output',
                          display_name='Output Path',
                          input_method='filewrite',
                          help='An absolute filepath to save a file')
        # ----------------------------------------------------------------------
        mcxt.add_argument('--sheet-name',
                          default=None,
                          display_name='Sheet Name',
                          help='Choose sheet name.')
        # ----------------------------------------------------------------------
        mcxt.add_argument('--encoding',
                          default='utf-8',
                          display_name='Encoding',
                          help='Encoding for CSV file, default is [[utf-8]]')
        argspec = mcxt.parse_args(args)
        return func(mcxt, argspec)


################################################################################
def main(*args):
    try:
        return _main(*args)
    except ArgsError as err:
        sys.stderr.write('Error: %s\nPlease -h to print help\n' % str(err))
    except ArgsExit as _:
        pass
