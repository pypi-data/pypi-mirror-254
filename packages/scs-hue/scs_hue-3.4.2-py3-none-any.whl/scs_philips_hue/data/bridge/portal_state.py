"""
Created on 28 Oct 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

example:
{"signedon": true, "incoming": false, "outgoing": true, "communication": "disconnected"}
"""

from collections import OrderedDict

from scs_core.data.json import JSONable


# --------------------------------------------------------------------------------------------------------------------

class PortalState(JSONable):
    """
    classdocs
    """

    # ----------------------------------------------------------------------------------------------------------------

    @classmethod
    def construct_from_jdict(cls, jdict):
        if not jdict:
            return None

        signed_on = jdict.get('signedon')
        incoming = jdict.get('incoming')
        outgoing = jdict.get('outgoing')

        communication = jdict.get('communication')

        return PortalState(signed_on, incoming, outgoing, communication)


    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, signed_on, incoming, outgoing, communication):
        """
        Constructor
        """
        self.__signed_on = bool(signed_on)                  # bool
        self.__incoming = bool(incoming)                    # bool
        self.__outgoing = bool(outgoing)                    # bool

        self.__communication = communication                # string


    # ----------------------------------------------------------------------------------------------------------------

    def as_json(self):
        jdict = OrderedDict()

        jdict['signedon'] = self.signed_on
        jdict['incoming'] = self.incoming
        jdict['outgoing'] = self.outgoing

        jdict['communication'] = self.communication

        return jdict


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def signed_on(self):
        return self.__signed_on


    @property
    def incoming(self):
        return self.__incoming


    @property
    def outgoing(self):
        return self.__outgoing


    @property
    def communication(self):
        return self.__communication


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return "PortalState:{signed_on:%s, incoming:%s, outgoing:%s, communication:%s}" %  \
               (self.signed_on, self.incoming, self.outgoing, self.communication)
