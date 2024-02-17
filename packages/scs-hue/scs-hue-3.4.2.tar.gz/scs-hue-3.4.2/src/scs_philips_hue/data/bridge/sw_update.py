"""
Created on 28 Oct 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

example:
{
    "updatestate": 0,
    "checkforupdate": false,
    "devicetypes": {"device_types": false, "lights": [], "sensors": []},
    "url": "",
    "text": "",
    "notify": false
}
"""

from collections import OrderedDict

from scs_core.data.datum import Datum
from scs_core.data.json import JSONable


# --------------------------------------------------------------------------------------------------------------------

class SWUpdate(JSONable):
    """
    classdocs
    """

    UPDATE_UNAVAILABLE =        1
    UPDATE_AVAILABLE =          2
    UPDATE_PERFORM =            3

    # ----------------------------------------------------------------------------------------------------------------

    @classmethod
    def construct_from_jdict(cls, jdict):
        if not jdict:
            return None

        update_state = jdict.get('updatestate')
        check_for_update = jdict.get('checkforupdate')
        device_types = DeviceTypes.construct_from_jdict(jdict.get('devicetypes'))

        url = jdict.get('url')
        text = jdict.get('text')
        notify = jdict.get('notify')

        return SWUpdate(update_state=update_state, check_for_update=check_for_update, device_types=device_types,
                        url=url, text=text, notify=notify)


    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, update_state=None, check_for_update=None, device_types=None,
                 url=None, text=None, notify=None):
        """
        Constructor
        """
        self.__update_state = Datum.int(update_state)                   # int
        self.__check_for_update = Datum.bool(check_for_update)          # bool
        self.__device_types = device_types                              # DeviceTypes

        self.__url = url                                                # string

        self.__text = text                                              # string
        self.__notify = Datum.bool(notify)                              # bool


    # ----------------------------------------------------------------------------------------------------------------

    def as_json(self):
        jdict = OrderedDict()

        if self.update_state is not None:
            jdict['updatestate'] = self.update_state

        if self.check_for_update is not None:
            jdict['checkforupdate'] = self.check_for_update

        if self.device_types is not None:
            jdict['devicetypes'] = self.device_types

        if self.url is not None:
            jdict['url'] = self.url

        if self.text is not None:
            jdict['text'] = self.text

        if self.notify is not None:
            jdict['notify'] = self.notify

        return jdict


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def update_state(self):
        return self.__update_state


    @property
    def check_for_update(self):
        return self.__check_for_update


    @property
    def device_types(self):
        return self.__device_types


    @property
    def url(self):
        return self.__url


    @property
    def text(self):
        return self.__text


    @property
    def notify(self):
        return self.__notify


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return "SWUpdate:{update_state:%s, check_for_update:%s, device_types:%s, url:%s, text:%s, notify:%s}" %  \
               (self.update_state, self.check_for_update, self.device_types, self.url, self.text, self.notify)


# --------------------------------------------------------------------------------------------------------------------

class DeviceTypes(JSONable):
    """
    classdocs
    """

    # ----------------------------------------------------------------------------------------------------------------

    @classmethod
    def construct_from_jdict(cls, jdict):
        if not jdict:
            return None

        bridge = jdict.get('bridge')
        lights = jdict.get('lights')
        sensors = jdict.get('sensors')

        return DeviceTypes(bridge, lights, sensors)


    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, bridge, lights, sensors):
        """
        Constructor
        """
        self.__bridge = bool(bridge)                # bool
        self.__lights = lights                      # array
        self.__sensors = sensors                    # array


    # ----------------------------------------------------------------------------------------------------------------

    def as_json(self):
        jdict = OrderedDict()

        jdict['bridge'] = self.bridge
        jdict['lights'] = self.lights
        jdict['sensors'] = self.sensors

        return jdict


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def bridge(self):
        return self.__bridge


    @property
    def lights(self):
        return self.__lights


    @property
    def sensors(self):
        return self.__sensors


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return "DeviceTypes:{bridge:%s, lights:%s, sensors:%s}" %  \
               (self.bridge, self.lights, self.sensors)
