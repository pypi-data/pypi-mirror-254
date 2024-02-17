"""
Created on 19 Nov 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)
"""

import optparse

from scs_core.data.datum import Datum

from scs_philips_hue import version
from scs_philips_hue.data.bridge.bridge_config import BridgeConfig


# --------------------------------------------------------------------------------------------------------------------

class CmdBridge(object):
    """unix command line handler"""

    def __init__(self):
        """
        Constructor
        """
        self.__parser = optparse.OptionParser(usage="%prog [-p PORTAL_SERVICES] [-c CHECK_UPDATE] [-u DO_UPDATE] "
                                                    "[-z CHANNEL] [-i INDENT] [-v] BRIDGE_NAME", version=version())

        # operations...
        self.__parser.add_option("--portal", "-p", type="int", action="store", dest="portal_services",
                                 help="enable portal services (1 or 0)")

        self.__parser.add_option("--check", "-c", type="int", action="store", dest="check_update",
                                 help="check for software update (1 or 0)")

        self.__parser.add_option("--update", "-u", type="int", action="store", dest="do_update",
                                 help="perform software update, if available (1 or 0)")

        self.__parser.add_option("--zigbee", "-z", type="string", action="store", dest="zigbee_channel",
                                 help="set zigbee channel (11, 15, 20 or 25)")

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

        if self.__opts.check_update is not None:
            if self.__opts.check_update != 0 and self.__opts.check_update != 1:
                return False

        if self.__opts.do_update is not None:
            if self.__opts.do_update != 0 and self.__opts.do_update != 1:
                return False

        if self.zigbee_channel is not None:
            if self.__opts.zigbee not in BridgeConfig.ZIGBEE_CHANNELS:
                return False

        return True


    def set(self):
        return self.__opts.update is not None


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def portal_services(self):
        return Datum.bool(self.__opts.portal_services)


    @property
    def check_update(self):
        return Datum.bool(self.__opts.check_update)


    @property
    def do_update(self):
        return Datum.bool(self.__opts.do_update)


    @property
    def zigbee_channel(self):
        return self.__opts.zigbee_channel


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
        return "CmdBridge:{bridge_name:%s, portal_services:%s, check_update:%s, do_update:%s, zigbee_channel:%s, " \
               "indent:%s, verbose:%s}" %  \
               (self.bridge_name, self.portal_services, self.check_update, self.do_update, self.zigbee_channel,
                self.indent, self.verbose)
