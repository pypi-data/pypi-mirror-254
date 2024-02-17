"""
Created on 29 Oct 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)
"""

from scs_philips_hue.data.bridge.bridge_config import ReportedBridgeConfig
from scs_philips_hue.data.bridge.response import Response

from scs_philips_hue.manager.manager import Manager


# --------------------------------------------------------------------------------------------------------------------

class UserManager(Manager):
    """
    classdocs
    """

    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, host, username):
        """
        Constructor
        """
        super().__init__(host, username)


    # ----------------------------------------------------------------------------------------------------------------

    def find(self, username):
        entries = self.find_all()

        for entry in entries:
            if entry.username == username:
                return entry

        return None


    def find_all(self):
        request_path = '/config'

        # request...
        self._rest_client.connect(self._host, self._username)

        try:
            jdict = self._rest_client.get(request_path)
        finally:
            self._rest_client.close()

        # response...
        config = ReportedBridgeConfig.construct_from_jdict(jdict)
        whitelist = config.whitelist

        return whitelist.entries if whitelist else []


    # ----------------------------------------------------------------------------------------------------------------

    def delete(self, username):
        request_path = '/config/whitelist/' + username

        # request...
        self._rest_client.connect(self._host, self._username)

        try:
            jdict = self._rest_client.delete(request_path)
        finally:
            self._rest_client.close()

        # response...
        response = Response.construct_from_jdict(jdict)

        return response
