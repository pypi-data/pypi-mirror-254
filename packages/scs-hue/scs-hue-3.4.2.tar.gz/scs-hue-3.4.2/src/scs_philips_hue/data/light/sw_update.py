"""
Created on 28 Oct 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

example:
{"state": "noupdates", "lastinstall": null}
"""

from collections import OrderedDict

from scs_core.data.json import JSONable


# --------------------------------------------------------------------------------------------------------------------

class SWUpdate(JSONable):
    """
    classdocs
    """

    # ----------------------------------------------------------------------------------------------------------------

    @classmethod
    def construct_from_jdict(cls, jdict):
        if not jdict:
            return None

        state = jdict.get('state')
        lastinstall = jdict.get('lastinstall')

        return cls(state, lastinstall)


    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, state, lastinstall):
        """
        Constructor
        """
        self.__state = state                            # string
        self.__lastinstall = lastinstall                # string (date / time)


    # ----------------------------------------------------------------------------------------------------------------

    def as_json(self):
        jdict = OrderedDict()

        jdict['state'] = self.state
        jdict['lastinstall'] = self.lastinstall

        return jdict


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def state(self):
        return self.__state


    @property
    def lastinstall(self):
        return self.__lastinstall


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return "SWUpdate:{state:%s, lastinstall:%s}" % (self.state, self.lastinstall)
