"""
Created on 3 Nov 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

example:
{"devicetype": "scs_hue_connector#bruno.local"}
"""

from collections import OrderedDict

from scs_core.data.json import JSONable

from scs_philips_hue.data.client.client_description import ClientDescription


# --------------------------------------------------------------------------------------------------------------------

class DeviceDescription(JSONable):
    """
    classdocs
    """

    # ----------------------------------------------------------------------------------------------------------------

    @classmethod
    def construct_from_jdict(cls, jdict):
        if not jdict:
            return None

        device_type = ClientDescription.construct_from_jstr(jdict.get('devicetype'))

        return DeviceDescription(device_type)


    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, device_type):
        """
        Constructor
        """
        self.__device_type = device_type                # ClientDescription


    # ----------------------------------------------------------------------------------------------------------------

    def as_json(self):
        jdict = OrderedDict()

        jdict['devicetype'] = self.device_type

        return jdict


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def device_type(self):
        return self.__device_type


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return "DeviceDescription:{device_type:%s}" %  self.device_type
