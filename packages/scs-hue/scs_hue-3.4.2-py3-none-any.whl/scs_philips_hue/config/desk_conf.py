"""
Created on 16 Mar 2018

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

Lamp names form an ordered set. The most-recently added lamp is at the end of the list.

document example:
{
    "preston_circus": [
        "black"
    ]
}
"""

from scs_core.data.json import JSONable

from scs_philips_hue.config.conf_set import ConfSet


# --------------------------------------------------------------------------------------------------------------------

class DeskConfSet(ConfSet):
    """
    classdocs
    """

    __FILENAME =        "desk_conf_set.json"

    @classmethod
    def persistence_location(cls):
        return cls.hue_dir(), cls.__FILENAME


    # ----------------------------------------------------------------------------------------------------------------

    @classmethod
    def construct_from_jdict(cls, jdict, skeleton=False):
        if not jdict:
            return cls({}) if skeleton else None

        confs = {}

        for channel, conf_jdict in jdict.items():
            confs[channel] = DeskConf.construct_from_jdict(conf_jdict)

        return cls(confs)


    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, confs):
        """
        Constructor
        """
        super().__init__(confs)


    # ----------------------------------------------------------------------------------------------------------------

    def add(self, channel, lamp_names):
        self._confs[channel] = DeskConf(lamp_names)


# --------------------------------------------------------------------------------------------------------------------

class DeskConf(JSONable):
    """
    classdocs
    """

    # ----------------------------------------------------------------------------------------------------------------

    @classmethod
    def construct_from_jdict(cls, jdict):
        if not jdict:
            return None

        lamp_names = [lamp_name for lamp_name in jdict]

        return cls(lamp_names)


    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, lamp_names):
        """
        Constructor
        """
        self.__lamp_names = lamp_names                  # list of string


    def __len__(self):
        return len(self.lamp_names)


    # ----------------------------------------------------------------------------------------------------------------

    def add_lamp(self, lamp_name):
        if lamp_name in self.__lamp_names:
            return

        self.__lamp_names.append(lamp_name)


    def remove_lamp(self, lamp_name):
        if lamp_name not in self.__lamp_names:
            return

        self.__lamp_names.remove(lamp_name)


    # ----------------------------------------------------------------------------------------------------------------

    def as_json(self):
        return self.lamp_names


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def lamp_names(self):
        return self.__lamp_names


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return "DeskConf:{lamp_names:%s}" % self.lamp_names
