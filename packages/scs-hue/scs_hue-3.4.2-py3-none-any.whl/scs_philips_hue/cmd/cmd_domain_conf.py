"""
Created on 16 Mar 2018

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

document example:
{"topic-path": "/orgs/south-coast-science-demo/brighton/loc/1/particulates", "document-node": "val.pm10"}
"""

import optparse

from scs_philips_hue import version


# --------------------------------------------------------------------------------------------------------------------

class CmdDomainConf(object):
    """unix command line handler"""

    def __init__(self):
        """
        Constructor
        """
        self.__parser = optparse.OptionParser(usage="%prog [-c CHANNEL { -a TOPIC_PATH DOMAIN_NODE | -r }] "
                                                    "[-i INDENT] [-v]", version=version())

        # configuration...
        self.__parser.add_option("--channel", "-c", type="string", action="store", dest="channel",
                                 help="the name of the information channel")

        # operations...
        self.__parser.add_option("--add", "-a", type="string", nargs=2, action="store", dest="add",
                                 help="add the domain configuration")

        self.__parser.add_option("--remove", "-r", action="store_true", dest="remove", default=False,
                                 help="remove the domain configuration")

        # output...
        self.__parser.add_option("--indent", "-i", type="int", action="store", dest="indent",
                                 help="pretty-print the output with INDENT")

        self.__parser.add_option("--verbose", "-v", action="store_true", dest="verbose", default=False,
                                 help="report narrative to stderr")

        self.__opts, self.__args = self.__parser.parse_args()


    # ----------------------------------------------------------------------------------------------------------------

    def is_valid(self):
        if self.add is not None and self.remove:
            return False

        if self.set() and self.channel is None:
            return False

        if not self.set() and self.channel is not None:
            return False

        return True


    def set(self):
        return self.add is not None or self.remove


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def channel(self):
        return self.__opts.channel


    @property
    def add(self):
        return self.__opts.add


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
        return "CmdDomainConf:{channel:%s, add:%s, remove:%s, indent:%s, verbose:%s}" % \
                    (self.channel, self.add, self.remove, self.indent, self.verbose)
