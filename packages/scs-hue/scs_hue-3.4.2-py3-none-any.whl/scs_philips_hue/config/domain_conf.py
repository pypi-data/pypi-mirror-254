"""
Created on 16 Mar 2018

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

document example:
[{"topic-path": "south-coast-science-demo/brighton/loc/1/particulates", "document-node": "exg.val.pm10"},
{"topic-path": "south-coast-science-demo/brighton/loc/1/particulates", "document-node": "exg.val.pm2p5"}]
"""

from collections import OrderedDict

from scs_core.data.json import JSONable

from scs_philips_hue.config.conf_set import ConfSet


# --------------------------------------------------------------------------------------------------------------------

class DomainConfSet(ConfSet):
    """
    classdocs
    """

    __FILENAME =        "domain_conf_set.json"

    @classmethod
    def persistence_location(cls):
        return cls.hue_dir(), cls.__FILENAME


    # ----------------------------------------------------------------------------------------------------------------

    @classmethod
    def construct_from_jdict(cls, jdict, skeleton=False):
        if not jdict:
            return cls({}) if skeleton else None

        confs = {}

        for name, conf_jdict in jdict.items():
            confs[name] = DomainConf.construct_from_jdict(conf_jdict)

        return cls(confs)


    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, confs):
        """
        Constructor
        """
        super().__init__(confs)


    # ----------------------------------------------------------------------------------------------------------------

    def add(self, name, topic_path, document_node):
        self._confs[name] = DomainConf(topic_path, document_node)


    def topic_paths(self):
        topic_path_set = set((conf.topic_path for conf in self._confs.values()))

        return topic_path_set


# --------------------------------------------------------------------------------------------------------------------

class DomainConf(JSONable):
    """
    classdocs
    """

    # ----------------------------------------------------------------------------------------------------------------

    @classmethod
    def construct_from_jdict(cls, jdict):
        if not jdict:
            return None

        topic_path = jdict.get('topic-path')
        document_node = jdict.get('document-node')

        return cls(topic_path, document_node)


    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, topic_path, document_node):
        """
        Constructor
        """
        self.__topic_path = topic_path                          # string
        self.__document_node = document_node                    # string


    def __lt__(self, other):
        if self.topic_path < other.topic_path:
            return True

        if self.topic_path > other.topic_path:
            return False

        if self.document_node < other.document_node:
            return True

        if self.document_node > other.document_node:
            return False

        return False


    # ----------------------------------------------------------------------------------------------------------------

    def as_json(self):
        jdict = OrderedDict()

        jdict['topic-path'] = self.topic_path
        jdict['document-node'] = self.document_node

        return jdict


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def node_path(self):
        return '.'.join((self.topic_path, self.document_node))


    @property
    def topic_path(self):
        return self.__topic_path


    @property
    def document_node(self):
        return self.__document_node


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return "DomainConf:{topic_path:%s, document_node:%s}" % (self.topic_path, self.document_node)
