"""
Created on 3 Nov 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)
"""

import optparse

from scs_philips_hue import version


# --------------------------------------------------------------------------------------------------------------------

class CmdUser(object):
    """unix command line handler"""

    def __init__(self):
        """
        Constructor
        """
        self.__parser = optparse.OptionParser(usage="%prog { -l | -r USER } [-i INDENT] [-v] BRIDGE_NAME",
                                              version=version())

        # operations...
        self.__parser.add_option("--list", "-l", action="store_true", dest="list",
                                 help="list all users")

        self.__parser.add_option("--remove", "-r", type="string", action="store", dest="remove",
                                 help="remove the user from the bridge")

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

        if self.remove is None and not self.list:
            return False

        if self.remove is not None and self.list:
            return False

        return True


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def list(self):
        return self.__opts.list


    @property
    def remove(self):
        return self.__opts.remove


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
        return "CmdUser:{bridge_name:%s, list:%s, remove:%s, indent:%s, verbose:%s}" % \
            (self.bridge_name, self.list, self.remove, self.indent, self.verbose)
