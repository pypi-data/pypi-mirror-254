"""
Created on 4 Nov 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)
"""

import optparse

from scs_philips_hue import version


# --------------------------------------------------------------------------------------------------------------------

class CmdLight(object):
    """unix command line handler"""

    def __init__(self):
        """
        Constructor
        """
        self.__parser = optparse.OptionParser(usage="%prog { -c | -l BRIDGE_NAME | -s BRIDGE_NAME | "
                                                    "-a BRIDGE_NAME SERIAL_NUMBER | -n BRIDGE_NAME INDEX LIGHT_NAME | "
                                                    "-r BRIDGE_NAME INDEX } [-i INDENT] [-v]",
                                              version=version())

        # operations...
        self.__parser.add_option("--catalogue", "-c", action="store_true", dest="catalogue",
                                 help="catalogue of all light names")

        self.__parser.add_option("--list", "-l", type="string", action="store", dest="list",
                                 help="list lights attached to BRIDGE")

        self.__parser.add_option("--search", "-s", type="string", action="store", dest="search",
                                 help="search for new lights using BRIDGE")

        self.__parser.add_option("--add", "-a", type="string", nargs=2, action="store", dest="add",
                                 help="add the light with SERIAL_NUMBER to BRIDGE")

        self.__parser.add_option("--name", "-n", type="string", nargs=3, action="store", dest="name",
                                 help="set the name of the light with INDEX to NAME on BRIDGE")

        self.__parser.add_option("--remove", "-r", type="string", nargs=2, action="store", dest="remove",
                                 help="delete the light with INDEX from BRIDGE")

        # output...
        self.__parser.add_option("--indent", "-i", type="int", action="store", dest="indent",
                                 help="pretty-print the output with INDENT")

        self.__parser.add_option("--verbose", "-v", action="store_true", dest="verbose", default=False,
                                 help="report narrative to stderr")

        self.__opts, self.__args = self.__parser.parse_args()


    # ----------------------------------------------------------------------------------------------------------------

    def is_valid(self):
        count = 0

        if self.catalogue:
            count += 1

        if self.list:
            count += 1

        if self.search:
            count += 1

        if self.add:
            count += 1

        if self.name:
            count += 1

        if self.remove:
            count += 1

        if count != 1:
            return False

        try:
            _ = self.index
        except ValueError:
            return False

        return True


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def catalogue(self):
        return self.__opts.catalogue


    @property
    def list(self):
        return self.__opts.list


    @property
    def search(self):
        return self.__opts.search is not None


    @property
    def add(self):
        return self.__opts.add is not None


    @property
    def name(self):
        return self.__opts.name is not None


    @property
    def remove(self):
        return self.__opts.remove is not None


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def bridge_name(self):
        if self.list:
            return self.__opts.list

        if self.search:
            return self.__opts.search

        if self.add:
            return self.__opts.add[0]

        if self.name:
            return self.__opts.name[0]

        if self.remove:
            return self.__opts.remove[0]

        return None


    @property
    def serial_number(self):
        if self.add:
            return self.__opts.add[1]

        return None


    @property
    def index(self):
        if self.name:
            return int(self.__opts.name[1])

        if self.remove:
            return int(self.__opts.remove[1])

        return None


    @property
    def light_name(self):
        if self.name:
            return self.__opts.name[2]

        return None


    # ----------------------------------------------------------------------------------------------------------------

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
        return "CmdLight:{catalogue:%s, list:%s, search:%s, add:%s, name:%s, " \
               "remove:%s, indent:%s, verbose:%s}" %  \
               (self.__opts.catalogue, self.__opts.list, self.__opts.search, self.__opts.add, self.__opts.name,
                self.__opts.remove, self.indent, self.verbose)
