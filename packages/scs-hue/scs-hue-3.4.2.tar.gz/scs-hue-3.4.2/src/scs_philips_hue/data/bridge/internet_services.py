"""
Created on 28 Oct 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

example:
{"internet": "connected", "remoteaccess": "connected", "time": "connected", "swupdate": "connected"}
"""

from collections import OrderedDict

from scs_core.data.json import JSONable


# --------------------------------------------------------------------------------------------------------------------

class InternetServices(JSONable):
    """
    classdocs
    """

    # ----------------------------------------------------------------------------------------------------------------

    @classmethod
    def construct_from_jdict(cls, jdict):
        if not jdict:
            return None

        internet = jdict.get('internet')
        remote_access = jdict.get('remoteaccess')
        time = jdict.get('time')
        sw_update = jdict.get('swupdate')

        return InternetServices(internet, remote_access, time, sw_update)


    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, internet, remote_access, time, sw_update):
        """
        Constructor
        """
        self.__internet = internet                      # string
        self.__remote_access = remote_access            # string
        self.__time = time                              # string
        self.__sw_update = sw_update                    # string


    # ----------------------------------------------------------------------------------------------------------------

    def as_json(self):
        jdict = OrderedDict()

        jdict['internet'] = self.internet
        jdict['remoteaccess'] = self.remote_access
        jdict['time'] = self.time
        jdict['swupdate'] = self.sw_update

        return jdict


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def internet(self):
        return self.__internet


    @property
    def remote_access(self):
        return self.__remote_access


    @property
    def time(self):
        return self.__time


    @property
    def sw_update(self):
        return self.__sw_update


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return "InternetServices:{internet:%s, remote_access:%s, time:%s, sw_update:%s}" %  \
               (self.internet, self.remote_access, self.time, self.sw_update)
