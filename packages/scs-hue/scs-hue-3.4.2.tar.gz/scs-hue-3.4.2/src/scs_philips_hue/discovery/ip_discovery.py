"""
Created on 4 Mar 2020

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)
"""

from scs_core.client.resource_unavailable_exception import ResourceUnavailableException
from scs_core.sys.logging import Logging

from scs_philips_hue.manager.bridge_manager import BridgeManager


# TODO: https://github.com/flyte/upnpclient
# --------------------------------------------------------------------------------------------------------------------

class IPDiscovery(object):
    """
    classdocs
    """

    __BRIDGE_DEFAULT_TIMEOUT = 2            # seconds

    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, host):
        """
        Constructor
        """
        self.__host = host                                          # PersistenceManager
        self.__logger = Logging.getLogger()


    # ----------------------------------------------------------------------------------------------------------------

    def find(self, credentials):
        # find...
        for bridge in self.find_all():
            # config...
            manager = BridgeManager(bridge.ip_address, credentials.username)

            try:
                config = manager.find()
            except ResourceUnavailableException:
                continue

            # check...
            if config.bridge_id == credentials.bridge_id:
                return config

        return None


    def find_all(self):
        for ip_address in self.__host.scan_accessible_subnets():
            self.__logger.info("checking %s" % ip_address)

            if BridgeManager.is_bridge(ip_address):
                yield IPHost(ip_address)


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return "IPDiscovery:{host:%s}" % self.__host


# --------------------------------------------------------------------------------------------------------------------

class IPHost(object):
    """
    classdocs
    """

    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, ip_address):
        """
        Constructor
        """
        self.__ip_address = ip_address


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def ip_address(self):
        return self.__ip_address


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return "IPHost:{ip_address:%s}" % self.ip_address
