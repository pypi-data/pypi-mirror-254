"""
Created on 16 Mar 2018

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

document example:
{"lamp-channels": ["scs-hcl-001", "scs-hcl-002"]}
"""

import optparse

from scs_philips_hue import version


# --------------------------------------------------------------------------------------------------------------------

class CmdDeskConf(object):
    """unix command line handler"""

    def __init__(self):
        """
        Constructor
        """
        self.__parser = optparse.OptionParser(usage="%prog [-c CHANNEL { -a LAMP_NAME | -r LAMP_NAME | -d }] "
                                                    "[-i INDENT] [-v]", version=version())

        # configuration...
        self.__parser.add_option("--channel", "-c", type="string", action="store", dest="channel",
                                 help="the name of the information channel")

        # operations...
        self.__parser.add_option("--add", "-a", type="string", action="store", dest="add_lamp",
                                 help="add the given lamp")

        self.__parser.add_option("--remove", "-r", type="string", action="store", dest="remove_lamp",
                                 help="remove the given lamp")

        self.__parser.add_option("--delete", "-d", action="store_true", dest="delete",
                                 help="delete the desk configuration")

        # output...
        self.__parser.add_option("--indent", "-i", type="int", action="store", dest="indent",
                                 help="pretty-print the output with INDENT")

        self.__parser.add_option("--verbose", "-v", action="store_true", dest="verbose", default=False,
                                 help="report narrative to stderr")

        self.__opts, self.__args = self.__parser.parse_args()


    # ----------------------------------------------------------------------------------------------------------------

    def is_valid(self):
        if self.add_lamp is not None and self.remove_lamp is not None:
            return False

        if self.set() and self.channel is None:
            return False

        if not self.set() and self.channel is not None:
            return False

        return True


    def set(self):
        return self.add_lamp is not None or self.remove_lamp is not None


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def channel(self):
        return self.__opts.channel


    @property
    def add_lamp(self):
        return self.__opts.add_lamp


    @property
    def remove_lamp(self):
        return self.__opts.remove_lamp


    @property
    def delete(self):
        return self.__opts.delete


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
        return "CmdDeskConf:{channel:%s, add_lamp:%s, remove_lamp:%s, delete:%s, indent:%s, verbose:%s}" % \
                    (self.channel, self.add_lamp, self.remove_lamp, self.delete, self.indent, self.verbose)
