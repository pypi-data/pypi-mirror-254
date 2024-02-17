"""
Created on 4 Nov 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)
"""

import optparse

from scs_philips_hue import version


# --------------------------------------------------------------------------------------------------------------------

class CmdJoin(object):
    """unix command line handler"""

    def __init__(self):
        """
        Constructor
        """
        self.__parser = optparse.OptionParser(usage="%prog [-i INDENT] [-v] BRIDGE_NAME", version=version())

        # output...
        self.__parser.add_option("--indent", "-i", type="int", action="store", dest="indent",
                                 help="pretty-print the output with INDENT")

        self.__parser.add_option("--verbose", "-v", action="store_true", dest="verbose", default=False,
                                 help="report narrative to stderr")

        self.__opts, self.__args = self.__parser.parse_args()


    # ----------------------------------------------------------------------------------------------------------------

    def is_valid(self):
        if self.bridge_name is None:
            return False

        # TODO: if len(self.bridge_name) < BridgeConfig.NAME_MIN_LENGTH or
        #  len(self.bridge_name) > BridgeConfig.NAME_MAX_LENGTH:

        return True


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def indent(self):
        return self.__opts.indent


    @property
    def verbose(self):
        return self.__opts.verbose


    @property
    def bridge_name(self):
        return self.__args[0] if self.__args else None


    # ----------------------------------------------------------------------------------------------------------------

    def print_help(self, file):
        self.__parser.print_help(file)


    def __str__(self, *args, **kwargs):
        return "CmdJoin:{bridge_name:%s, indent:%s, verbose:%s}" % \
            (self.bridge_name, self.indent, self.verbose)
