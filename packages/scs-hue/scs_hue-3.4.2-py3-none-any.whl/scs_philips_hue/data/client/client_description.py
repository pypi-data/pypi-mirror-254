"""
Created on 27 Oct 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

example:
"scs_hue_connector#bruno.local"
"""

from scs_core.data.json import JSONable


# --------------------------------------------------------------------------------------------------------------------

class ClientDescription(JSONable):
    """
    classdocs
    """

    APP = 'scs-hue-connector'

    __SEPARATOR = '#'                         # as used by Philips apps


    # ----------------------------------------------------------------------------------------------------------------

    @classmethod
    def construct_from_jstr(cls, jstr):
        if not jstr:
            return None

        pieces = jstr.split(cls.__SEPARATOR)

        if len(pieces) != 2:
            raise ValueError(jstr)

        app = pieces[0]
        user = pieces[1]

        return ClientDescription(app, user)


    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, app, user):
        """
        Constructor
        """
        self.__app = app                    # string
        self.__user = user                  # string


    # ----------------------------------------------------------------------------------------------------------------

    def as_json(self):
        return self.app + self.__SEPARATOR + self.user


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def app(self):
        return self.__app


    @property
    def user(self):
        return self.__user


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return "ClientDescription:{app:%s, user:%s}" %  (self.app, self.user)
