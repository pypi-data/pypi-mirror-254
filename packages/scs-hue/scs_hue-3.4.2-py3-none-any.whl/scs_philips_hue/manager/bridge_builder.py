"""
Created on 17 Apr 2023

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)
"""

from scs_core.sys.logging import Logging

from scs_philips_hue.config.bridge_address import BridgeAddress, BridgeAddressSet
from scs_philips_hue.discovery.discovery import Discovery
from scs_philips_hue.manager.bridge_manager import BridgeManager, BridgeManagerGroup


# --------------------------------------------------------------------------------------------------------------------

class BridgeBuilder(object):
    """
    classdocs
    """

    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, host):
        self.__host = host                                          # PersistenceManager
        self.__logger = Logging.getLogger()                         # logger


    # ----------------------------------------------------------------------------------------------------------------

    def construct_all(self, credentials_set):
        bridge_managers = {}

        for bridge_name, credentials in credentials_set.sorted_credentials.items():
            manager = self.construct_manager_for_credentials(credentials)

            bridge_managers[bridge_name] = manager                  # includes 'None' managers

        return BridgeManagerGroup(bridge_managers)


    def construct_dict_for_credentials(self, credentials):
        manager = self.construct_manager_for_credentials(credentials)

        return {} if manager is None else {credentials.bridge_name: manager}


    def construct_manager_for_credentials(self, credentials):
        address_set = BridgeAddressSet.load(self.__host, skeleton=True)

        self.__logger.info("looking for '%s'..." % credentials.bridge_name)

        # cached address..
        manager = self.__find_by_cached_address(address_set, credentials)

        # find bridge...
        if manager is None:
            manager = self.__find_by_scan(address_set, credentials)

        self.__logger.info("%s: %s" % (credentials.bridge_name, manager))

        return manager


    # ----------------------------------------------------------------------------------------------------------------

    def __find_by_cached_address(self, address_set, credentials):
        try:
            address = address_set.address(credentials.bridge_name)

            if BridgeManager.is_bridge(address.ipv4.dot_decimal()):
                return BridgeManager(address.ipv4.dot_decimal(), credentials.username)

            # remove invalid address...
            self.__logger.info("invalid cached IP address")
            address_set.delete(credentials.bridge_name)
            address_set.save(self.__host)

        except KeyError:
            self.__logger.info("no cached IP address")

        return None


    def __find_by_scan(self, address_set, credentials):
        discovery = Discovery(self.__host)
        bridge = discovery.find(credentials)

        if bridge is None:
            self.__logger.error("bridge '%s' not found." % credentials.bridge_name)
            return None
            # exit(1)

        if bridge.ip_address is None:
            self.__logger.error("stored credentials are not valid for bridge '%s'." % credentials.bridge_name)
            return None
            # exit(1)

        # add address...
        address_set.add(BridgeAddress.construct(credentials.bridge_name, bridge.ip_address))
        address_set.save(self.__host)

        return BridgeManager(bridge.ip_address, credentials.username)


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return "BridgeBuilder:{}"
