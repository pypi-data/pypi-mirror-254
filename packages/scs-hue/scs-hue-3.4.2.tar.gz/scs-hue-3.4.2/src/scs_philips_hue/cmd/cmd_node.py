"""
Created on 25 Apr 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)
"""

import optparse

from scs_philips_hue import version


# --------------------------------------------------------------------------------------------------------------------

class CmdNode(object):
    """unix command line handler"""

    def __init__(self):
        """
        Constructor
        """
        self.__parser = optparse.OptionParser(usage="%prog { -c | -t NAME TOPIC_PATH DOMAIN_NODE } [-i] [-v]",
                                              version=version())

        # input...
        self.__parser.add_option("--conf", "-c", action="store_true", dest="use_domain_conf", default=False,
                                 help="get topic.node from the domain conf")

        self.__parser.add_option("--topic", "-t", type="string", nargs=3, action="store", dest="topic_path",
                                 help="use the given name, topic and node")

        # output...
        self.__parser.add_option("--verbose", "-v", action="store_true", dest="verbose", default=False,
                                 help="report narrative to stderr")

        self.__opts, self.__args = self.__parser.parse_args()


    # ----------------------------------------------------------------------------------------------------------------

    def is_valid(self):
        if self.use_domain_conf and self.topic_path is not None:
            return False

        if not self.use_domain_conf and self.topic_path is None:
            return False

        return True


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def use_domain_conf(self):
        return self.__opts.use_domain_conf


    @property
    def topic_path(self):
        return self.__opts.topic_path


    @property
    def verbose(self):
        return self.__opts.verbose


    # ----------------------------------------------------------------------------------------------------------------

    def print_help(self, file):
        self.__parser.print_help(file)


    def __str__(self, *args, **kwargs):
        return "CmdNode:{use_domain_conf:%s, topic_path:%s, verbose:%s}" %  \
               (self.use_domain_conf, self.topic_path, self.verbose)
