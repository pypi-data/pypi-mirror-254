"""
Created on 25 Nov 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

example:
{"deviceid":["45AF34","543636"]}
"""

from collections import OrderedDict

from scs_core.data.json import JSONable


# --------------------------------------------------------------------------------------------------------------------

class LightDevice(JSONable):
    """
    classdocs
    """

    # ----------------------------------------------------------------------------------------------------------------

    @classmethod
    def construct_from_jdict(cls, jdict):
        if not jdict:
            return None

        name = jdict.get('name')

        return cls(name)


    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, *ids):
        """
        Constructor
        """
        self.__ids = ids                        # list of string


    # ----------------------------------------------------------------------------------------------------------------

    def as_json(self):
        jdict = OrderedDict()

        jdict['deviceid'] = self.ids

        return jdict


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def ids(self):
        return self.__ids


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return "LightDevice:{ids:%s}" % self.ids
