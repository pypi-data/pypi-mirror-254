"""
Created on 7 Nov 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

example:
{"lastscan": "2017-11-07T12:10:47", "1": {"name": "Hue color lamp 1"}}
"""

from collections import OrderedDict

from scs_core.data.json import JSONable
from scs_core.data.str import Str

from scs_philips_hue.data.light.light_name import LightName


# --------------------------------------------------------------------------------------------------------------------

class LightScan(JSONable):
    """
    classdocs
    """

    # ----------------------------------------------------------------------------------------------------------------

    @classmethod
    def construct_from_jdict(cls, jdict):
        if not jdict:
            return None

        last_scan = None
        entries = []

        for index, value in jdict.items():
            if index == 'lastscan':
                last_scan = value
            else:
                entries.append(LightScanEntry.construct_from_jdict(index, value))

        return cls(last_scan, entries)


    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, last_scan, entries):
        """
        Constructor
        """
        self.__last_scan = last_scan                # string (may be date / time)
        self.__entries = entries                    # array of LightScanEntry


    # ----------------------------------------------------------------------------------------------------------------

    def is_active(self):
        return self.last_scan == 'active'


    # ----------------------------------------------------------------------------------------------------------------

    def as_json(self):
        jdict = OrderedDict()

        jdict['lastscan'] = self.last_scan

        for index, light in self.entries.items():
            jdict[index] = light

        return jdict


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def last_scan(self):
        return self.__last_scan


    @property
    def entries(self):
        return self.__entries


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return "LightScan:{last_scan:%s, entries:%s}" %  (self.last_scan, Str.collection(self.entries))


# --------------------------------------------------------------------------------------------------------------------

class LightScanEntry(JSONable):
    """
    classdocs
    """

    # ----------------------------------------------------------------------------------------------------------------

    @classmethod
    def construct_from_jdict(cls, index, jdict):
        if not jdict:
            return None

        name = LightName.construct_from_jdict(jdict)

        return LightScanEntry(index, name)


    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, index, name):
        """
        Constructor
        """
        self.__index = index                            # index
        self.__name = name                              # LightName


    # ----------------------------------------------------------------------------------------------------------------

    def as_json(self):
        jdict = OrderedDict()

        jdict[self.index] = self.name

        return jdict


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def index(self):
        return self.__index


    @property
    def name(self):
        return self.__name


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return "LightScanEntry:{index:%s, name:%s}" %  (self.index, self.name)
