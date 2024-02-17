"""
Created on 28 Oct 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

example:
{
    "state": {
        "on": true,
        "bri": 254,
        "hue": 8418,
        "sat": 140,
        "effect": "none",
        "xy": [0.4573, 0.41],
        "ct": 366,
        "alert": "select",
        "colormode": "ct",
        "reachable": true
    },
    "swupdate": {
        "state": "noupdates",
        "lastinstall": null
    },
    "light_type": "Extended color light",
    "name": "Hue color lamp 1",
    "modelid": "LCT015",
    "manufacturername": "Philips",
    "uniqueid": "00:17:88:01:03:54:25:66-0b",
    "swversion": "1.19.0_r19755",
    "swconfigid": "A724919D",
    "productid": "Philips-LCT015-1-A19ECLv5"
}
"""

# from scs_core.data.json import JSONify

from collections import OrderedDict

from scs_core.data.json import JSONable

from scs_philips_hue.data.light.light_state import ReportedLightState
from scs_philips_hue.data.light.sw_update import SWUpdate


# --------------------------------------------------------------------------------------------------------------------

class Light(JSONable):
    """
    classdocs
    """

    # ----------------------------------------------------------------------------------------------------------------

    @classmethod
    def construct_from_jdict(cls, jdict):
        # print(JSONify.dumps(jdict))

        if not jdict:
            return None

        state = ReportedLightState.construct_from_jdict(jdict.get('state'))
        swupdate = SWUpdate.construct_from_jdict(jdict.get('swupdate'))

        light_type = jdict.get('type')
        name = jdict.get('name')
        model_id = jdict.get('modelid')
        manufacturer_name = jdict.get('manufacturername')
        unique_id = jdict.get('uniqueid')

        sw_version = jdict.get('swversion')
        sw_config_id = jdict.get('swconfigid')
        product_id = jdict.get('productid')

        return cls(state, swupdate, light_type, name, model_id, manufacturer_name, unique_id,
                   sw_version, sw_config_id, product_id)


    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, state, swupdate, light_type, name, model_id, manufacturer_name,
                 unique_id, sw_version, sw_config_id, product_id):
        """
        Constructor
        """
        self.__state = state                                    # ReportedLightState
        self.__swupdate = swupdate                              # SWUpdate

        self.__light_type = light_type                          # string
        self.__name = name                                      # string
        self.__model_id = model_id                              # string
        self.__manufacturer_name = manufacturer_name            # string
        self.__unique_id = unique_id                            # string

        self.__sw_version = sw_version                          # string
        self.__sw_config_id = sw_config_id                      # string
        self.__product_id = product_id                          # string


    # ----------------------------------------------------------------------------------------------------------------

    def as_json(self):
        jdict = OrderedDict()

        jdict['state'] = self.state
        jdict['swupdate'] = self.swupdate

        jdict['type'] = self.light_type
        jdict['name'] = self.name
        jdict['modelid'] = self.model_id
        jdict['manufacturername'] = self.manufacturer_name
        jdict['uniqueid'] = self.unique_id

        jdict['swversion'] = self.sw_version
        jdict['swconfigid'] = self.sw_config_id
        jdict['productid'] = self.product_id

        return jdict


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def state(self):
        return self.__state


    @property
    def swupdate(self):
        return self.__swupdate


    @property
    def light_type(self):
        return self.__light_type


    @property
    def name(self):
        return self.__name


    @property
    def model_id(self):
        return self.__model_id


    @property
    def manufacturer_name(self):
        return self.__manufacturer_name


    @property
    def unique_id(self):
        return self.__unique_id


    @property
    def sw_version(self):
        return self.__sw_version


    @property
    def sw_config_id(self):
        return self.__sw_config_id


    @property
    def product_id(self):
        return self.__product_id


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return "Light:{state:%s, swupdate:%s, light_type:%s, name:%s, model_id:%s, manufacturer_name:%s, " \
               "unique_id:%s, sw_version:%s, sw_config_id:%s, product_id:%s}" %  \
               (self.state, self.swupdate, self.light_type, self.name, self.model_id, self.manufacturer_name,
                self.unique_id, self.sw_version, self.sw_config_id, self.product_id)


# --------------------------------------------------------------------------------------------------------------------

class LightListEntry(JSONable):
    """
    classdocs
    """

    # ----------------------------------------------------------------------------------------------------------------

    @classmethod
    def construct_from_jdict(cls, index, jdict):
        if not jdict:
            return None

        light = Light.construct_from_jdict(jdict)

        return LightListEntry(index, light)


    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, index, light):
        """
        Constructor
        """
        self.__index = index                            # index
        self.__light = light                            # Light


    # ----------------------------------------------------------------------------------------------------------------

    def as_json(self):
        jdict = OrderedDict()

        jdict[self.index] = self.light

        return jdict


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def index(self):
        return self.__index


    @property
    def light(self):
        return self.__light


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return "LightListEntry:{index:%s, light:%s}" %  (self.index, self.light)
