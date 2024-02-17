"""
Created on 29 Oct 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)
"""

from scs_core.client.resource_unavailable_exception import ResourceUnavailableException

from scs_core.data.json import JSONable
from scs_core.data.str import Str

from scs_philips_hue.client.client_exception import ClientException
from scs_philips_hue.client.rest_client import RESTClient

from scs_philips_hue.data.bridge.bridge_config import ReportedBridgeConfig
from scs_philips_hue.data.bridge.response import Response

from scs_philips_hue.manager.manager import Manager


# --------------------------------------------------------------------------------------------------------------------

class BridgeManager(Manager):
    """
    classdocs
    """

    __TIMEOUT = 5               # seconds

    # ----------------------------------------------------------------------------------------------------------------

    @classmethod
    def is_bridge(cls, ip_address):
        rest_client = RESTClient()

        try:
            # request...
            rest_client.connect(ip_address, None, timeout=cls.__TIMEOUT)
            jdict = rest_client.get('/api')

            if jdict is None:
                return False

            # response...
            return Response.construct_from_jdict(jdict) is not None

        except (ClientException, ResourceUnavailableException):
            return False

        finally:
            rest_client.close()


    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, host, username):
        """
        Constructor
        """
        super().__init__(host, username)


    # ----------------------------------------------------------------------------------------------------------------

    def find(self):
        request_path = '/config'

        # request...
        self._rest_client.connect(self._host, self._username, timeout=self.__TIMEOUT)

        try:
            jdict = self._rest_client.get(request_path)
        finally:
            self._rest_client.close()

        # response...
        config = ReportedBridgeConfig.construct_from_jdict(jdict)

        return config


    def set_config(self, config):
        request_path = '/config'

        # request...
        self._rest_client.connect(self._host, self._username, timeout=self.__TIMEOUT)

        try:
            jdict = self._rest_client.put(request_path, config.as_json())
        finally:
            self._rest_client.close()

        # response...
        response = Response.construct_from_jdict(jdict)

        return response


    # ----------------------------------------------------------------------------------------------------------------

    def register(self, device):
        # request...
        self._rest_client.connect(self._host, None, timeout=self.__TIMEOUT)

        try:
            jdict = self._rest_client.post('', device.as_json())
        finally:
            self._rest_client.close()

        # response...
        response = Response.construct_from_jdict(jdict)

        return response


# --------------------------------------------------------------------------------------------------------------------

class BridgeManagerGroup(JSONable):
    """
    classdocs
    """

    # ----------------------------------------------------------------------------------------------------------------

    @classmethod
    def construct_from_jdict(cls, jdict):
        if not jdict:
            return None

        bridge_managers = {bridge_name: BridgeManager.construct_from_jdict(manager_jdict)
                           for bridge_name, manager_jdict in jdict}

        return cls(bridge_managers)


    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, bridge_managers):
        """
        Constructor
        """
        self.__bridge_managers = bridge_managers            # dict of bridge_name: BridgeManager


    def __bool__(self):
        return len(self.__bridge_managers) > 0


    # ----------------------------------------------------------------------------------------------------------------

    def is_complete(self):
        for manager in self.__bridge_managers.values():
            if manager is None:
                return False

        return True


    # ----------------------------------------------------------------------------------------------------------------

    def as_json(self):
        return self.__bridge_managers


    # ----------------------------------------------------------------------------------------------------------------

    def items(self):
        return dict(sorted(self.__bridge_managers.items())).items()


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return "BridgeManagerGroup:{bridge_managers:%s}" % Str.collection(self.__bridge_managers)
