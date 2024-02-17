"""
Created on 16 Mar 2018

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

document example:
{"NO2": {"path-channel": "risk_level", "domain-min": 0.0, "domain-max": 50.0, "brightness": 254, "transition-time": 9}}
"""

import optparse

from scs_philips_hue import version
from scs_philips_hue.config.chroma_path import ChromaPath


# --------------------------------------------------------------------------------------------------------------------

class CmdChromaConf(object):
    """unix command line handler"""

    def __init__(self):
        """
        Constructor
        """
        path_names = ' | '.join(ChromaPath.list())

        self.__parser = optparse.OptionParser(usage="%prog [-c CHANNEL { [-p PATH_NAME] [-l DOMAIN_MIN] "
                                                    "[-u DOMAIN_MAX] [-b BRIGHTNESS] [-t TRANSITION] | -r }] "
                                                    "[-i INDENT] [-v]",
                                              version=version())

        # configuration...
        self.__parser.add_option("--channel", "-c", type="string", action="store", dest="channel",
                                 help="the name of the information channel")

        # fields...
        self.__parser.add_option("--path", "-p", type="string", action="store", dest="path_name",
                                 help="the chroma path { %s }" % path_names)

        self.__parser.add_option("--lower", "-l", type="float", action="store", dest="domain_min",
                                 help="specify the domain lower bound")

        self.__parser.add_option("--upper", "-u", type="float", action="store", dest="domain_max",
                                 help="specify the domain upper bound")

        self.__parser.add_option("--bright", "-b", type="int", action="store", dest="brightness",
                                 help="set the lamp brightness (max 254)")

        self.__parser.add_option("--trans", "-t", type="float", action="store", dest="transition_time",
                                 help="set the lamp transition time (seconds)")

        # operations...
        self.__parser.add_option("--remove", "-r", action="store_true", dest="remove", default=False,
                                 help="remove the given configuration")

        # output...
        self.__parser.add_option("--indent", "-i", type="int", action="store", dest="indent",
                                 help="pretty-print the output with INDENT")

        self.__parser.add_option("--verbose", "-v", action="store_true", dest="verbose", default=False,
                                 help="report narrative to stderr")

        self.__opts, self.__args = self.__parser.parse_args()


    # ----------------------------------------------------------------------------------------------------------------

    def is_valid(self):
        if self.set() and self.channel is None:
            return False

        if self.set() and self.remove:
            return False

        if self.path_name is not None and self.path_name not in ChromaPath.list():
            return False

        if self.brightness is not None and (self.brightness < 0 or self.brightness > 254):
            return False

        return True


    def is_complete(self):
        if self.path_name is None or self.domain_min is None or self.domain_max is None or \
                self.brightness is None or self.transition_time is None:
            return False

        return True


    def set(self):
        return self.path_name is not None or self.domain_min is not None or self.domain_max is not None or \
               self.brightness is not None or self.transition_time is not None


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def channel(self):
        return self.__opts.channel


    @property
    def path_name(self):
        return self.__opts.path_name


    @property
    def domain_min(self):
        return self.__opts.domain_min


    @property
    def domain_max(self):
        return self.__opts.domain_max


    @property
    def brightness(self):
        return self.__opts.brightness


    @property
    def transition_time(self):
        return self.__opts.transition_time


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
        return "CmdChromaConf:{channel:%s, path_name:%s, domain_min:%s, domain_max:%s, " \
               "brightness:%s, transition_time:%s, remove:%s, indent:%s, verbose:%s}" % \
                    (self.channel, self.path_name, self.domain_min, self.domain_max,
                     self.brightness, self.transition_time, self.remove, self.indent, self.verbose)
