"""
Created on 6 Apr 2022

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)
"""

from abc import ABC

from collections import OrderedDict

from scs_core.data.json import PersistentJSONable
from scs_core.data.str import Str


# --------------------------------------------------------------------------------------------------------------------

class ConfSet(PersistentJSONable, ABC):
    """
    classdocs
    """

    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, confs):
        """
        Constructor
        """
        super().__init__()

        self._confs = confs                          # dict of name: *Conf


    def __contains__(self, item):
        return item in self._confs


    def __len__(self):
        return len(self._confs)


    # ----------------------------------------------------------------------------------------------------------------

    def remove(self, name):
        try:
            del self._confs[name]
        except KeyError:
            pass


    # ----------------------------------------------------------------------------------------------------------------

    def as_json(self):
        return self.confs


    # ----------------------------------------------------------------------------------------------------------------

    def conf(self, name):
        try:
            return self._confs[name]
        except KeyError:
            return None


    @property
    def confs(self):
        jdict = OrderedDict()

        for name in sorted(self._confs.keys()):
            jdict[name] = self._confs[name]

        return jdict


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        name = self.__class__.__name__

        return name + ":%s" % Str.collection(self.confs)
