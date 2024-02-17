"""
Created on 19 Nov 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)
"""

import optparse

from scs_philips_hue import version


# --------------------------------------------------------------------------------------------------------------------

class CmdChannelTest(object):
    """unix command line handler"""

    def __init__(self):
        """
        Constructor
        """
        self.__parser = optparse.OptionParser(usage="%prog -c CHANNEL [-i INTERVAL] [-f] [-v]", version=version())

        # input...
        self.__parser.add_option("--channel", "-c", type="string", action="store", dest="channel",
                                 help="the name of the information channel")

        # operation...
        self.__parser.add_option("--transition-time", "-t", type="int", action="store", dest="transition_time",
                                 help="override chroma conf transition time")

        self.__parser.add_option("--forever", "-f", action="store_true", dest="forever", default=False,
                                 help="run until Control-C")

        # output...
        self.__parser.add_option("--verbose", "-v", action="store_true", dest="verbose", default=False,
                                 help="report narrative to stderr")

        self.__opts, self.__args = self.__parser.parse_args()


    # ----------------------------------------------------------------------------------------------------------------

    def is_valid(self):
        if self.channel is None:
            return False

        return True


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def channel(self):
        return self.__opts.channel


    @property
    def transition_time(self):
        return self.__opts.transition_time


    @property
    def forever(self):
        return self.__opts.forever


    @property
    def verbose(self):
        return self.__opts.verbose


    # ----------------------------------------------------------------------------------------------------------------

    def print_help(self, file):
        self.__parser.print_help(file)


    def __str__(self, *args, **kwargs):
        return "CmdChannelTest:{channel:%s, transition_time:%s, forever:%s, verbose:%s}" %  \
            (self.channel, self.transition_time, self.forever, self.verbose)
