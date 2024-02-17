"""
Created on 26 Apr 2022

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

document example:
{
    "hue-br1-001": {
        "ipv4": "192.168.1.16"
    },
    "hue-br1-002": {
        "ipv4": "192.168.1.8"
    }
}
"""

from collections import OrderedDict

from scs_core.data.json import JSONable, PersistentJSONable
from scs_core.data.str import Str

from scs_core.sys.ipv4_address import IPv4Address


# --------------------------------------------------------------------------------------------------------------------

class BridgeAddress(JSONable):
    """
    classdocs
    """

    # ----------------------------------------------------------------------------------------------------------------

    @classmethod
    def construct_from_jdict(cls, name, jdict):
        if not jdict:
            return None

        ipv4 = IPv4Address.construct(jdict.get('ipv4'))

        return cls(name, ipv4)


    @classmethod
    def construct(cls, name, ipv4_str):
        ipv4 = IPv4Address.construct(ipv4_str)

        return cls(name, ipv4)


    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, name, ipv4):
        """
        Constructor
        """
        super().__init__()

        self.__name = name                                  # string
        self.__ipv4 = ipv4                                  # IPv4Address


    # ----------------------------------------------------------------------------------------------------------------

    def as_json(self):
        jdict = OrderedDict()

        jdict['ipv4'] = None if self.ipv4 is None else self.ipv4.dot_decimal()

        return jdict


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def name(self):
        return self.__name


    @property
    def ipv4(self):
        return self.__ipv4


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return "BridgeAddress:{name:%s, ipv4:%s}" % (self.name, self.ipv4)


# --------------------------------------------------------------------------------------------------------------------

class BridgeAddressSet(PersistentJSONable):
    """
    classdocs
    """

    # TODO: put bridge finder here

    __FILENAME = "bridge_address_set.json"

    @classmethod
    def persistence_location(cls):
        return cls.hue_dir(), cls.__FILENAME


    # ----------------------------------------------------------------------------------------------------------------

    @classmethod
    def construct_from_jdict(cls, jdict, skeleton=False):
        if not jdict:
            return cls(OrderedDict()) if skeleton else None

        addresses = OrderedDict()
        for name, credentials_jdict in jdict.items():
            addresses[name] = BridgeAddress.construct_from_jdict(name, credentials_jdict)

        return cls(addresses)


    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, addresses):
        """
        Constructor
        """
        super().__init__()

        self.__addresses = addresses                    # dict of name: BridgeAddress


    def __len__(self):
        return len(self.__addresses)


    # ----------------------------------------------------------------------------------------------------------------

    def add(self, address: BridgeAddress):
        self.__addresses[address.name] = address


    def delete(self, name):
        try:
            del self.__addresses[name]
            return True

        except KeyError:
            return False


    def address(self, name):
        return self.__addresses[name]                           # may raise KeyError


    # ----------------------------------------------------------------------------------------------------------------

    def as_json(self):
        return self.sorted_addresses


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def sorted_addresses(self):
        return OrderedDict(sorted(self.__addresses.items()))


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return "BridgeAddressSet:{addresses:%s}" % Str.collection(self.sorted_addresses)
