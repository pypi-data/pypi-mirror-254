"""
Created on 22 Nov 2023

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

document example:
{"upnp-enabled": false}
"""

from collections import OrderedDict

from scs_core.data.json import PersistentJSONable


# --------------------------------------------------------------------------------------------------------------------

class UPnPConf(PersistentJSONable):
    """
    classdocs
    """

    __FILENAME = "upnp_conf.json"

    @classmethod
    def persistence_location(cls):
        return cls.hue_dir(), cls.__FILENAME


    # ----------------------------------------------------------------------------------------------------------------

    @classmethod
    def construct_from_jdict(cls, jdict, skeleton=False):
        if not jdict:
            return cls(False) if skeleton else None

        upnp_enabled = jdict.get('upnp-enabled', False)

        return cls(upnp_enabled)


    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, upnp_enabled):
        """
        Constructor
        """
        super().__init__()

        self.__upnp_enabled = bool(upnp_enabled)


    # ----------------------------------------------------------------------------------------------------------------

    def as_json(self):
        jdict = OrderedDict()

        jdict['upnp-enabled'] = self.upnp_enabled

        return jdict


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def upnp_enabled(self):
        return self.__upnp_enabled


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return "UPnPConf:{upnp_enabled:%s}" % self.upnp_enabled
