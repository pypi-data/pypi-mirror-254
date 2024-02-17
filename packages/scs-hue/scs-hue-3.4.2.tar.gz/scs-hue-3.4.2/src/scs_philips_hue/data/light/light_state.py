"""
Created on 28 Oct 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

example:
{
    "on": true,
    "bri": 254,
    "hue": 8418,
    "sat": 140,
    "effect": "none",
    "xy": [0.4573, 0.41],
    "ct": 366,
    "alert": "select",
    "color_mode": "ct",
    "reachable": true
}
"""

from collections import OrderedDict

from scs_core.data.json import JSONable

from scs_philips_hue.data.light.chroma import ChromaPoint


# --------------------------------------------------------------------------------------------------------------------

class LightState(JSONable):
    """
    classdocs
    """

    ALERT_NONE =        'none'
    ALERT_SELECT =      'select'
    ALERT_L_SELECT =    'lselect'

    # ----------------------------------------------------------------------------------------------------------------

    @classmethod
    def white(cls, bri=254):
        return cls(on=True, bri=bri, hue=8418, sat=140, transition_time=1.0)


    # ----------------------------------------------------------------------------------------------------------------

    @classmethod
    def construct_from_jdict(cls, jdict):
        if not jdict:
            return None

        on = jdict.get('on')
        bri = jdict.get('bri')
        hue = jdict.get('hue')
        sat = jdict.get('sat')
        effect = jdict.get('effect')

        transition_time_tenths = jdict.get('transitiontime')
        transition_time = None if transition_time_tenths is None else round(transition_time_tenths / 10.0, 1)

        xy = ChromaPoint.construct_from_jdict(jdict.get('xy'))

        ct = jdict.get('ct')
        alert = jdict.get('alert')

        return cls(on=on, bri=bri, hue=hue, sat=sat, effect=effect, transition_time=transition_time, xy=xy, ct=ct,
                   alert=alert)


    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, on=None, bri=None, hue=None, sat=None, effect=None, transition_time=None,
                 xy=None, ct=None, alert=None):
        """
        Constructor
        """
        self.__on = on                                  # bool
        self.__bri = bri                                # uint8
        self.__hue = hue                                # uint16
        self.__sat = sat                                # uint8
        self.__effect = effect                          # string
        self.__transition_time = transition_time        # uint16 (seconds x 10)

        self.__xy = xy                                  # ChromaPoint

        self.__ct = ct                                  # uint16
        self.__alert = alert                            # string


    # ----------------------------------------------------------------------------------------------------------------

    def as_json(self):
        jdict = OrderedDict()

        if self.on is not None:
            jdict['on'] = self.on

        if self.bri is not None:
            jdict['bri'] = self.bri

        if self.hue is not None:
            jdict['hue'] = self.hue

        if self.sat is not None:
            jdict['sat'] = self.sat

        if self.effect is not None:
            jdict['effect'] = self.effect

        if self.transition_time is not None:
            jdict['transitiontime'] = int(self.transition_time * 10.0)

        if self.xy is not None:
            jdict['xy'] = self.xy

        if self.ct is not None:
            jdict['ct'] = self.ct

        if self.alert is not None:
            jdict['alert'] = self.alert

        return jdict


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def on(self):
        return self.__on


    @property
    def bri(self):
        return self.__bri


    @property
    def hue(self):
        return self.__hue


    @property
    def sat(self):
        return self.__sat


    @property
    def effect(self):
        return self.__effect


    @property
    def transition_time(self):
        return self.__transition_time


    @property
    def xy(self):
        return self.__xy


    @property
    def ct(self):
        return self.__ct


    @property
    def alert(self):
        return self.__alert


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return "LightState:{on:%s, bri:%s, hue:%s, sat:%s, effect:%s, transition_time:%s, " \
               "xy:%s, ct:%s, alert:%s}" %  \
               (self.on, self.bri, self.hue, self.sat, self.effect, self.transition_time,
                self.xy, self.ct, self.alert)


# --------------------------------------------------------------------------------------------------------------------

class ReportedLightState(LightState):
    """
    classdocs
    """

    # ----------------------------------------------------------------------------------------------------------------

    @classmethod
    def construct_from_jdict(cls, jdict):
        if not jdict:
            return None

        on = jdict.get('on')
        bri = jdict.get('bri')
        hue = jdict.get('hue')
        sat = jdict.get('sat')

        effect = jdict.get('effect')
        transition_time = jdict.get('transitiontime')

        xy = ChromaPoint.construct_from_jdict(jdict.get('xy'))

        ct = jdict.get('ct')
        alert = jdict.get('alert')

        color_mode = jdict.get('colormode')
        reachable = jdict.get('reachable')

        return ReportedLightState(on=on, bri=bri, hue=hue, sat=sat, effect=effect, transition_time=transition_time,
                                  xy=xy, ct=ct, alert=alert, color_mode=color_mode, reachable=reachable)


    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, on=None, bri=None, hue=None, sat=None, effect=None, transition_time=None,
                 xy=None, ct=None, alert=None, color_mode=None, reachable=None):
        """
        Constructor
        """
        super().__init__(on=on, bri=bri, hue=hue, sat=sat, effect=effect, transition_time=transition_time,
                         xy=xy, ct=ct, alert=alert)

        self.__color_mode = color_mode              # string
        self.__reachable = reachable                # bool


    # ----------------------------------------------------------------------------------------------------------------

    def as_json(self):
        jdict = OrderedDict()

        jdict['on'] = self.on
        jdict['bri'] = self.bri
        jdict['hue'] = self.hue
        jdict['sat'] = self.sat

        jdict['effect'] = self.effect
        jdict['transitiontime'] = self.transition_time

        jdict['xy'] = self.xy

        jdict['ct'] = self.ct
        jdict['alert'] = self.alert

        jdict['colormode'] = self.color_mode
        jdict['reachable'] = self.reachable

        return jdict


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def color_mode(self):
        return self.__color_mode


    @property
    def reachable(self):
        return self.__reachable


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return "ReportedLightState:{on:%s, bri:%s, hue:%s, sat:%s, effect:%s, transition_time:%s, " \
               "xy:%s, ct:%s, alert:%s, color_mode:%s, reachable:%s}" %  \
               (self.on, self.bri, self.hue, self.sat, self.effect, self.transition_time,
                self.xy, self.ct, self.alert, self.color_mode, self.reachable)
