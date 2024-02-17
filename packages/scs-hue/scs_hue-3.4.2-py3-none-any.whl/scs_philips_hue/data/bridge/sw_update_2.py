"""
Created on 28 Oct 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

example:
{
    "checkforupdate": false,
    "lastchange": "2017-10-27T15:10:38",
    "bridge": {"state": "noupdates", "lastinstall": null},
    "state": "noupdates",
    "autoinstall": {"updatetime": "T14:00:00", "on": false}
}
"""

from collections import OrderedDict

from scs_core.data.json import JSONable


# --------------------------------------------------------------------------------------------------------------------

class SWUpdate2(JSONable):
    """
    classdocs
    """

    # ----------------------------------------------------------------------------------------------------------------

    @classmethod
    def construct_from_jdict(cls, jdict):
        if not jdict:
            return None

        check_for_update = jdict.get('checkforupdate')
        last_change = jdict.get('lastchange')
        state = jdict.get('state')

        bridge = Bridge.construct_from_jdict(jdict.get('bridge'))
        auto_install = AutoInstall.construct_from_jdict(jdict.get('autoinstall'))

        return SWUpdate2(check_for_update, last_change, bridge, state, auto_install)


    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, check_for_update, last_change, bridge, state, auto_install):
        """
        Constructor
        """
        self.__check_for_update = bool(check_for_update)            # bool
        self.__last_change = last_change                            # string (date / time)
        self.__state = state                                        # bool

        self.__bridge = bridge                                      # Bridge
        self.__auto_install = auto_install                          # AutoInstall


    # ----------------------------------------------------------------------------------------------------------------

    def as_json(self):
        jdict = OrderedDict()

        jdict['checkforupdate'] = self.check_for_update
        jdict['lastchange'] = self.last_change
        jdict['bridge'] = self.bridge
        jdict['state'] = self.state
        jdict['autoinstall'] = self.auto_install

        return jdict


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def check_for_update(self):
        return self.__check_for_update


    @property
    def last_change(self):
        return self.__last_change


    @property
    def state(self):
        return self.__state


    @property
    def bridge(self):
        return self.__bridge


    @property
    def auto_install(self):
        return self.__auto_install


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return "SWUpdate2:{check_for_update:%s, last_change:%s, state:%s, bridge:%s, auto_install:%s}" %  \
               (self.check_for_update, self.last_change, self.state, self.bridge, self.auto_install)


# --------------------------------------------------------------------------------------------------------------------

class Bridge(JSONable):
    """
    classdocs
    """

    # ----------------------------------------------------------------------------------------------------------------

    @classmethod
    def construct_from_jdict(cls, jdict):
        if not jdict:
            return None

        state = jdict.get('state')
        last_install = jdict.get('lastinstall')

        return Bridge(state, last_install)


    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, state, last_install):
        """
        Constructor
        """
        self.__state = state                                # string
        self.__last_install = last_install                  # string (date / time)


    # ----------------------------------------------------------------------------------------------------------------

    def as_json(self):
        jdict = OrderedDict()

        jdict['state'] = self.state
        jdict['lastinstall'] = self.last_install

        return jdict


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def state(self):
        return self.__state


    @property
    def last_install(self):
        return self.__last_install


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return "Bridge:{state:%s, last_install:%s}" %  (self.state, self.last_install)


# --------------------------------------------------------------------------------------------------------------------

class AutoInstall(JSONable):
    """
    classdocs
    """

    # ----------------------------------------------------------------------------------------------------------------

    @classmethod
    def construct_from_jdict(cls, jdict):
        if not jdict:
            return None

        update_time = jdict.get('updatetime')
        on = jdict.get('on')

        return AutoInstall(update_time, on)


    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, update_time, on):
        """
        Constructor
        """
        self.__update_time = update_time                    # string (time)
        self.__on = bool(on)                                # bool


    # ----------------------------------------------------------------------------------------------------------------

    def as_json(self):
        jdict = OrderedDict()

        jdict['updatetime'] = self.update_time
        jdict['on'] = self.on

        return jdict


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def update_time(self):
        return self.__update_time


    @property
    def on(self):
        return self.__on


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return "AutoInstall:{update_time:%s, on:%s}" %  (self.update_time, self.on)
