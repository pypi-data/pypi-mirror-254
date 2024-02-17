"""
Created on 31 Oct 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

example:
[
    {"error":{"type":6,"address":"/lights/1/state/reachable","description":"parameter, reachable, not available"}},
    {"success":{"/lights/1/state/on":true}}
]
"""

from collections import OrderedDict

from scs_core.data.json import JSONable
from scs_core.data.str import Str


# --------------------------------------------------------------------------------------------------------------------

class Response(JSONable):
    """
    classdocs
    """

    # ----------------------------------------------------------------------------------------------------------------

    @classmethod
    def construct_from_jdict(cls, jdict):
        if not jdict:
            return None

        errors = []
        successes = []

        for entry in jdict:
            entry_type, entry_jdict = entry.popitem()

            if entry_type == 'error':
                errors.append(Error.construct_from_jdict(entry_jdict))

            elif entry_type == 'success':
                successes.append(Success.construct_from_jdict(entry_jdict))

            else:
                raise ValueError(entry_type)

        return Response(errors, successes)


    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, errors, successes):
        """
        Constructor
        """
        self.__errors = errors                      # array of Error
        self.__successes = successes                # array of Success


    # ----------------------------------------------------------------------------------------------------------------

    def has_errors(self):
        return len(self.errors) > 0


    # ----------------------------------------------------------------------------------------------------------------

    def as_json(self):
        jdict = []

        for error in self.errors:
            jdict.append(error)

        for success in self.successes:
            jdict.append(success)

        return jdict


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def errors(self):
        return self.__errors


    @property
    def successes(self):
        return self.__successes


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return "Response:{err:%s, succ:%s}" %  (Str.collection(self.errors), Str.collection(self.successes))


# --------------------------------------------------------------------------------------------------------------------

class Success(JSONable):
    """
    classdocs
    """

    # ----------------------------------------------------------------------------------------------------------------

    @classmethod
    def construct_from_jdict(cls, jdict):
        if not jdict:
            return None

        try:
            cmd, value = jdict.popitem()
        except AttributeError:
            cmd, value = (jdict, None)

        return Success(cmd, value)


    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, cmd, value):
        """
        Constructor
        """
        self.__cmd = cmd                            # string
        self.__value = value                        # *


    # ----------------------------------------------------------------------------------------------------------------

    def as_json(self):
        return {'success': {self.cmd: self.value}}


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def cmd(self):
        return self.__cmd


    @property
    def value(self):
        return self.__value


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return "Success:{cmd:%s, value:%s}" % (self.cmd, self.value)


# --------------------------------------------------------------------------------------------------------------------

class Error(JSONable):
    """
    classdocs
    """

    # ----------------------------------------------------------------------------------------------------------------

    @classmethod
    def construct_from_jdict(cls, jdict):
        if not jdict:
            return None

        code = jdict.get('type')
        address = jdict.get('address')
        description = jdict.get('description')


        return Error(code, address, description)


    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, code, address, description):
        """
        Constructor
        """
        self.__code = code                          # int
        self.__address = address                    # string
        self.__description = description            # string


    # ----------------------------------------------------------------------------------------------------------------

    def as_json(self):
        jdict = OrderedDict()

        jdict['type'] = self.code
        jdict['address'] = self.address
        jdict['description'] = self.description

        return {'error': jdict}


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def code(self):
        return self.__code


    @property
    def address(self):
        return self.__address


    @property
    def description(self):
        return self.__description


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return "Error:{code:%s, address:%s, description:%s}" % (self.code, self.address, self.description)
