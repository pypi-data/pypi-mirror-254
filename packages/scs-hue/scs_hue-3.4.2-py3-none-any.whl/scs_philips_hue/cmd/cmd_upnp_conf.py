"""
Created on 4 Nov 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)
"""

import optparse

from scs_philips_hue import version


# --------------------------------------------------------------------------------------------------------------------

class CmdUPnPConf(object):
    """unix command line handler"""

    def __init__(self):
        """
        Constructor
        """
        self.__parser = optparse.OptionParser(usage="%prog [-e { 0 | 1 }] [-i INDENT] [-v]", version=version())

        # functionality
        self.__parser.add_option("--enable", "-e", type="int", action="store", dest="enable",
                                 help="enable UPnP discovery")

        # output...
        self.__parser.add_option("--indent", "-i", type="int", action="store", dest="indent",
                                 help="pretty-print the output with INDENT")

        self.__parser.add_option("--verbose", "-v", action="store_true", dest="verbose", default=False,
                                 help="report narrative to stderr")

        self.__opts, self.__args = self.__parser.parse_args()


    # ----------------------------------------------------------------------------------------------------------------

    def is_valid(self):
        if self.__opts.enable is not None and self.__opts.enable not in [0, 1]:
            return False

        if self.__args:
            return False

        return True


    def set(self):
        return self.__opts.enable is not None


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def enable(self):
        return None if self.__opts.enable is None else bool(self.__opts.enable)


    @property
    def indent(self):
        return self.__opts.indent


    @property
    def verbose(self):
        return self.__opts.verbose


    # ----------------------------------------------------------------------------------------------------------------

    def print_help(self, file):
        self.__parser.print_help(file)


    def __str__(self, *args, **kwargs):
        return "CmdUPnPConf:{enable:%s, indent:%s, verbose:%s}" % \
            (self.__opts.enable, self.indent, self.verbose)
