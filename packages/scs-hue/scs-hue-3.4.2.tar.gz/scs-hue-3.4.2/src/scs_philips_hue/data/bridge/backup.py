"""
Created on 28 Oct 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

example:
{"status": "idle", "error_code": 0}
"""

from collections import OrderedDict

from scs_core.data.json import JSONable


# --------------------------------------------------------------------------------------------------------------------

class Backup(JSONable):
    """
    classdocs
    """

    # ----------------------------------------------------------------------------------------------------------------

    @classmethod
    def construct_from_jdict(cls, jdict):
        if not jdict:
            return None

        status = jdict.get('status')
        error_code = jdict.get('errorcode')

        return Backup(status, error_code)


    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, status, error_code):
        """
        Constructor
        """
        self.__status = status                          # string
        self.__error_code = int(error_code)             # int


    # ----------------------------------------------------------------------------------------------------------------

    def as_json(self):
        jdict = OrderedDict()

        jdict['status'] = self.status
        jdict['errorcode'] = self.error_code

        return jdict


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def status(self):
        return self.__status


    @property
    def error_code(self):
        return self.__error_code


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return "Backup:{status:%s, error_code:%s}" %  (self.status, self.error_code)
