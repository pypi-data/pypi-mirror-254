"""
Created on 16 Mar 2018

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

document example:
{"NO2": {"path-name": "risk-level", "domain-min": 0.0, "domain-max": 50.0, "brightness": 254, "transition-time": 9},
"PM10": {"path-name": "risk-level", "domain-min": 0.0, "domain-max": 100.0, "brightness": 254, "transition-time": 9}}
"""

from collections import OrderedDict

from scs_core.data.datum import Datum
from scs_core.data.json import JSONable

from scs_philips_hue.config.chroma_path import ChromaPath
from scs_philips_hue.config.conf_set import ConfSet

from scs_philips_hue.data.light.chroma import ChromaMapping


# --------------------------------------------------------------------------------------------------------------------

class ChromaConfSet(ConfSet):
    """
    classdocs
    """

    __FILENAME =        "chroma_conf_set.json"

    @classmethod
    def persistence_location(cls):
        return cls.hue_dir(), cls.__FILENAME


    # ----------------------------------------------------------------------------------------------------------------

    @classmethod
    def construct_from_jdict(cls, jdict, skeleton=False):
        if not jdict:
            return cls({}) if skeleton else None

        confs = {}

        for channel, conf_jdict in jdict.items():
            confs[channel] = ChromaConf.construct_from_jdict(conf_jdict)

        return cls(confs)


    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, confs):
        """
        Constructor
        """
        super().__init__(confs)


    # ----------------------------------------------------------------------------------------------------------------

    def add(self, channel, path_name, domain_min, domain_max, brightness, transition_time):
        self._confs[channel] = ChromaConf(path_name, domain_min, domain_max, brightness, transition_time)


# --------------------------------------------------------------------------------------------------------------------

class ChromaConf(JSONable):
    """
    classdocs
    """

    # ----------------------------------------------------------------------------------------------------------------

    @classmethod
    def construct_from_jdict(cls, jdict):
        if not jdict:
            return None

        path_name = jdict.get('path-name')

        domain_min = jdict.get('domain-min')
        domain_max = jdict.get('domain-max')

        brightness = jdict.get('brightness')
        transition_time = jdict.get('transition-time')

        return cls(path_name, domain_min, domain_max, brightness, transition_time)


    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, path_name, domain_min, domain_max, brightness, transition_time):
        """
        Constructor
        """
        self.__path_name = path_name                                # string

        self.__domain_min = domain_min                              # float
        self.__domain_max = domain_max                              # float

        self.__brightness = Datum.int(brightness)                   # int
        self.__transition_time = Datum.int(transition_time)         # int


    # ----------------------------------------------------------------------------------------------------------------

    def path(self):
        return ChromaPath.retrieve(self.path_name)


    def mapping(self, path):
        return ChromaMapping.construct(self, path)


    # ----------------------------------------------------------------------------------------------------------------

    def as_json(self):
        jdict = OrderedDict()

        jdict['path-name'] = self.path_name

        jdict['domain-min'] = self.domain_min
        jdict['domain-max'] = self.domain_max

        jdict['brightness'] = self.brightness
        jdict['transition-time'] = self.transition_time

        return jdict


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def path_name(self):
        return self.__path_name


    @property
    def domain_min(self):
        return self.__domain_min


    @property
    def domain_max(self):
        return self.__domain_max


    @property
    def brightness(self):
        return self.__brightness


    @property
    def transition_time(self):
        return self.__transition_time


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return "ChromaConf:{path_name:%s, domain_min:%s, domain_max:%s, brightness:%s, transition_time:%s}" % \
               (self.path_name, self.domain_min, self.domain_max, self.brightness, self.transition_time)
