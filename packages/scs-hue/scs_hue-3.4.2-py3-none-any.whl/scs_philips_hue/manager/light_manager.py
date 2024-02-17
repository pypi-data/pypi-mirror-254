"""
Created on 30 Oct 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)
"""

from scs_philips_hue.data.bridge.response import Response
from scs_philips_hue.data.light.light import Light, LightListEntry
from scs_philips_hue.data.light.light_name import LightName
from scs_philips_hue.data.light.light_scan import LightScan

from scs_philips_hue.manager.manager import Manager


# --------------------------------------------------------------------------------------------------------------------

class LightManager(Manager):
    """
    classdocs
    """

    __REQUEST_TIMEOUT = 5               # seconds

    # ----------------------------------------------------------------------------------------------------------------

    @classmethod
    def construct_all_from_jdict(cls, jdict):
        if not jdict:
            return None

        return {bridge_name: cls.construct_from_jdict(lm_jdict)
                for bridge_name, lm_jdict in jdict.items()}


    @classmethod
    def construct_all(cls, bridge_manager_group):
        return {bridge_name: cls(bridge_manager.host, bridge_manager.username)
                for bridge_name, bridge_manager in bridge_manager_group.items() if bridge_manager is not None}


    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, host, username):
        """
        Constructor
        """
        super().__init__(host, username)


    # ----------------------------------------------------------------------------------------------------------------

    def find_index_for_uid(self, unique_id):
        lights = self.find_all()

        for entry in lights:
            if entry.light.unique_id == unique_id:
                return entry.index

        return None


    def find_indices_for_name(self, name):
        lights = self.find_all()

        indices = []

        for entry in lights:
            if entry.light.name == name:
                indices.append(entry.index)

        return indices


    def find(self, index):
        request_path = '/lights/' + str(index)

        # request...
        self._rest_client.connect(self._host, self._username)

        try:
            jdict = self._rest_client.get(request_path)
        finally:
            self._rest_client.close()

        # response...
        return Light.construct_from_jdict(jdict)


    def find_new(self):
        request_path = '/lights/new'

        # request...
        self._rest_client.connect(self._host, self._username)

        try:
            jdict = self._rest_client.get(request_path)
        finally:
            self._rest_client.close()

        # response...
        report = LightScan.construct_from_jdict(jdict)

        return report


    def find_all(self):
        request_path = '/lights'

        # request...
        self._rest_client.connect(self._host, self._username)

        try:
            jdict = self._rest_client.get(request_path)
        finally:
            self._rest_client.close()

        # response...
        lights = []

        # TODO: handle error case

        for index, light_jdict in jdict.items():
            lights.append(LightListEntry.construct_from_jdict(index, light_jdict))

        return lights


    # ----------------------------------------------------------------------------------------------------------------

    def search(self, device=None):
        request_path = '/lights'
        payload = device.as_json() if device else {}

        # request...
        self._rest_client.connect(self._host, self._username)

        try:
            jdict = self._rest_client.post(request_path, payload)
        finally:
            self._rest_client.close()

        # response...
        response = Response.construct_from_jdict(jdict)

        return response


    # ----------------------------------------------------------------------------------------------------------------

    def rename(self, index, name):
        request_path = '/lights/' + str(index)
        payload = LightName(name)

        # request...
        self._rest_client.connect(self._host, self._username, timeout=self.__REQUEST_TIMEOUT)

        try:
            jdict = self._rest_client.put(request_path, payload.as_json())
        finally:
            self._rest_client.close()

        # response...
        response = Response.construct_from_jdict(jdict)

        return response


    def set_state(self, index, state):
        request_path = '/lights/' + str(index) + '/state'

        # request...
        self._rest_client.connect(self._host, self._username, timeout=self.__REQUEST_TIMEOUT)

        try:
            jdict = self._rest_client.put(request_path, state.as_json())
        finally:
            self._rest_client.close()

        # response...
        response = Response.construct_from_jdict(jdict)

        return response


    def delete(self, index):
        request_path = '/lights/' + str(index)

        # request...
        self._rest_client.connect(self._host, self._username, timeout=self.__REQUEST_TIMEOUT)

        try:
            jdict = self._rest_client.delete(request_path)
        finally:
            self._rest_client.close()

        # response...
        response = Response.construct_from_jdict(jdict)

        return response
