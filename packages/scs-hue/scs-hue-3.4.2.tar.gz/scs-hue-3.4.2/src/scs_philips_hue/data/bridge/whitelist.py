"""
Created on 27 Oct 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

example:
"blah":
{"last use date": "2017-10-27T20:02:32", "create date": "2017-10-27T15:04:55", "name": "scs_hue#bruno"}
"""

from collections import OrderedDict

from scs_core.data.json import JSONable
from scs_core.data.str import Str

from scs_philips_hue.data.client.client_description import ClientDescription


# --------------------------------------------------------------------------------------------------------------------

class WhitelistGroup(JSONable):
    """
    classdocs
    """

    # ----------------------------------------------------------------------------------------------------------------

    @classmethod
    def construct_from_jdict(cls, jdict):
        if not jdict:
            return None

        entries = []

        for username, entry_jdict in jdict.items():
            entries.append(WhitelistEntry.construct_from_jdict(username, entry_jdict))

        return WhitelistGroup(entries)


    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, entries):
        """
        Constructor
        """
        self.__entries = entries                    # array of WhitelistEntry


    # ----------------------------------------------------------------------------------------------------------------

    def as_json(self):
        jdict = OrderedDict()

        for entry in self.entries:
            jdict[entry.username] = entry

        return jdict


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def entries(self):
        return self.__entries


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return "WhitelistGroup:{entries:%s}" % Str.collection(self.entries)


# --------------------------------------------------------------------------------------------------------------------

class WhitelistEntry(JSONable):
    """
    classdocs
    """

    # ----------------------------------------------------------------------------------------------------------------

    @classmethod
    def construct_from_jdict(cls, username, jdict):
        if not jdict:
            return None

        last_use_datetime = jdict.get('last use date')
        create_datetime = jdict.get('create date')

        description = ClientDescription.construct_from_jstr(jdict.get('name'))

        return WhitelistEntry(username, last_use_datetime, create_datetime, description)


    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, username, last_use_datetime, create_datetime, description):
        """
        Constructor
        """
        self.__username = username                                  # string

        self.__last_use_datetime = last_use_datetime                # string (date / time)
        self.__create_datetime = create_datetime                    # string (date / time)

        self.__description = description                            # ClientDescription


    # ----------------------------------------------------------------------------------------------------------------

    def as_json(self):
        jdict = OrderedDict()

        jdict['username'] = self.username
        jdict['last use date'] = self.last_use_datetime
        jdict['create date'] = self.create_datetime

        jdict['description'] = self.description

        return jdict


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def username(self):
        return self.__username


    @property
    def last_use_datetime(self):
        return self.__last_use_datetime


    @property
    def create_datetime(self):
        return self.__create_datetime


    @property
    def description(self):
        return self.__description


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return "WhitelistEntry:{username:%s, last_use_datetime:%s, create_datetime:%s, description:%s}" %  \
               (self.username, self.last_use_datetime, self.create_datetime, self.description)
