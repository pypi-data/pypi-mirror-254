"""
Created on 26 Apr 2022

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

source repo: scs_philips_hue

example document:
{"org-id": "south-coast-science-test-user", "api-key": "9fdfb841-3433-45b8-b223-3f5a283ceb8e"}
"""

import optparse

from scs_philips_hue import version


# --------------------------------------------------------------------------------------------------------------------

class CmdBridgeAddress(object):
    """unix command line handler"""

    def __init__(self):
        """
        Constructor
        """
        self.__parser = optparse.OptionParser(usage="%prog { -l | -r BRIDGE_NAME } [-i INDENT] [-v]",
                                              version=version())

        # operations...
        self.__parser.add_option("--remove", "-r", type="str", action="store", dest="remove",
                                 help="remove the named bridge")

        # output...
        self.__parser.add_option("--indent", "-i", type="int", action="store", dest="indent",
                                 help="pretty-print the output with INDENT")

        self.__parser.add_option("--verbose", "-v", action="store_true", dest="verbose", default=False,
                                 help="report narrative to stderr")

        self.__opts, self.__args = self.__parser.parse_args()


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def remove(self):
        return self.__opts.remove


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
        return "CmdBridgeAddress:{remove:%s, indent:%s, verbose:%s}" % \
               (self.remove, self.indent, self.verbose)
