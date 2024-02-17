"""
Created on 27 Oct 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

example:
{"id":"001788fffe795620","internalipaddress":"192.168.1.10"}
"""

from collections import OrderedDict

from scs_core.data.json import JSONable


# --------------------------------------------------------------------------------------------------------------------

class BridgeSummary(JSONable):
    """
    classdocs
    """

    # ----------------------------------------------------------------------------------------------------------------

    @classmethod
    def construct_from_jdict(cls, jdict):
        if not jdict:
            return None

        id = jdict.get('id')
        ip_address = jdict.get('internalipaddress')

        return BridgeSummary(id, ip_address)


    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, id, ip_address):
        """
        Constructor
        """
        self.__id = id                                  # string
        self.__ip_address = ip_address                  # string (IPv4 address)


    # ----------------------------------------------------------------------------------------------------------------

    def as_json(self):
        jdict = OrderedDict()

        jdict['id'] = self.id
        jdict['internalipaddress'] = self.ip_address

        return jdict


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def id(self):
        return self.__id


    @property
    def ip_address(self):
        return self.__ip_address


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return "BridgeSummary:{id:%s, ip_address:%s}" %  (self.id, self.ip_address)
