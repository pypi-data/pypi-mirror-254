"""
Created on 8 Nov 2023

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)
"""

from collections import OrderedDict

from scs_core.data.json import JSONable

from scs_philips_hue.client.rest_client import RESTClient


# --------------------------------------------------------------------------------------------------------------------

class Manager(JSONable):
    """
    classdocs
    """

    # ----------------------------------------------------------------------------------------------------------------

    @classmethod
    def construct_from_jdict(cls, jdict):
        if not jdict:
            return None

        host = jdict.get('host')
        username = jdict.get('username')

        return cls(host, username)


    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, host, username):
        """
        Constructor
        """
        self._rest_client = RESTClient()

        self._host = host
        self._username = username


    # ----------------------------------------------------------------------------------------------------------------

    def as_json(self):
        jdict = OrderedDict()

        jdict['host'] = self.host
        jdict['username'] = self.username

        return jdict


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def host(self):
        return self._host


    @property
    def username(self):
        return self._username


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        classname = self.__class__.__name__

        return classname + ":{rest_client:%s, host:%s, username:%s}" % \
            (self._rest_client, self._host, self._username)
