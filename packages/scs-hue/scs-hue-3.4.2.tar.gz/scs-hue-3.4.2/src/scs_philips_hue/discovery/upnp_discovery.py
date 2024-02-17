"""
Created on 30 Oct 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)
"""

from scs_core.sys.logging import Logging

from scs_philips_hue.client.upnp_client import UPnPClient
from scs_philips_hue.data.bridge.bridge_summary import BridgeSummary


# --------------------------------------------------------------------------------------------------------------------

class UPnPDiscovery(object):
    """
    classdocs
    """

    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self):
        """
        Constructor
        """
        self.__upnp_client = UPnPClient()
        self.__logger = Logging.getLogger()


    # ----------------------------------------------------------------------------------------------------------------

    def find(self, id):
        descriptions = self.find_all()

        for description in descriptions:
            self.__logger.info("found: %s" % description)

            if description.id.lower() == id.lower():
                return description

        return None


    def find_all(self):
        # request...
        try:
            self.__upnp_client.connect()
            response_jdict = self.__upnp_client.get()

        finally:
            self.__upnp_client.close()

        # response...
        return tuple(BridgeSummary.construct_from_jdict(jdict) for jdict in response_jdict)


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return "UPnPDiscovery:{upnp_client:%s}" % self.__upnp_client
