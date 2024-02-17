"""
Created on 20 Apr 2023

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

example:
{
    "black": {
        "bridge-name": "hue-br1-001",
        "index": 1
    },
    "wyndham": {
        "bridge-name": "hue-br1-002",
        "index": 1
    }
}
"""

from collections import OrderedDict

from scs_core.data.json import JSONable
from scs_core.sys.logging import Logging


# --------------------------------------------------------------------------------------------------------------------

class LightCatalogue(JSONable):
    """
    classdocs
    """

    # ----------------------------------------------------------------------------------------------------------------

    @classmethod
    def construct_from_jdict(cls, jdict):
        if not jdict:
            return None

        entries = {bulb_name: LightCatalogueEntry.construct_from_jdict(entry_jdict)
                   for bulb_name, entry_jdict in jdict.items()}

        return cls(entries)


    @classmethod
    def construct(cls, light_managers):
        logger = Logging.getLogger()
        entries = OrderedDict()

        for bridge_name, manager in light_managers.items():
            lights = manager.find_all()

            for list_entry in lights:
                if list_entry.light.name in entries:
                    logger.error("WARNING: duplicate light: '%s'." % list_entry.light.name)

                entries[list_entry.light.name] = LightCatalogueEntry(bridge_name, list_entry.index)

        return cls(entries)


    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, entries):
        """
        Constructor
        """
        self.__entries = entries                    # dict of bulb_name: LightCatalogueEntry


    def __contains__(self, item):
        return item in self.__entries



    # ----------------------------------------------------------------------------------------------------------------

    def light(self, name):
        return self.__entries[name]                 # may raise KeyError


    # ----------------------------------------------------------------------------------------------------------------

    def as_json(self):
        return self.sorted_entries


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def sorted_entries(self):
        return OrderedDict(sorted(self.__entries.items()))


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return "LightCatalogue:{entries:%s}" % self.sorted_entries


# --------------------------------------------------------------------------------------------------------------------

class LightCatalogueEntry(JSONable):
    """
    classdocs
    """

    # ----------------------------------------------------------------------------------------------------------------

    @classmethod
    def construct_from_jdict(cls, jdict):
        if not jdict:
            return None

        bridge_name = jdict.get('bridge-name')
        index = jdict.get('index')

        return cls(bridge_name, index)


    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, bridge_name, index):
        """
        Constructor
        """
        self.__bridge_name = bridge_name                # string
        self.__index = int(index)                       # int


    # ----------------------------------------------------------------------------------------------------------------

    def as_json(self):
        jdict = OrderedDict()

        jdict['bridge-name'] = self.bridge_name
        jdict['index'] = self.index

        return jdict


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def bridge_name(self):
        return self.__bridge_name


    @property
    def index(self):
        return self.__index


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return "LightCatalogueEntry:{bridge_name:%s, index:%s}" % (self.bridge_name, self.index)
