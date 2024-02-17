"""
Created on 4 Oct 2020

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

document example:
{"name": "test", "points": [[0.74, 0.26], [0.48, 0.41], [0.08, 0.84]]}
"""

import os

from collections import OrderedDict

from scs_core.data.json import JSONCatalogueEntry
from scs_core.data.str import Str

from scs_philips_hue.data.light.chroma import ChromaPoint


# --------------------------------------------------------------------------------------------------------------------

class ChromaPath(JSONCatalogueEntry):
    """
    classdocs
    """

    __CATALOGUE_NAME = 'paths'

    @classmethod
    def catalogue_location(cls):
        return os.path.join(os.path.dirname(os.path.realpath(__file__)), cls.__CATALOGUE_NAME)


    CANONICAL_CHROMAS = {
        'R': ChromaPoint.red(),
        'G': ChromaPoint.green(),
        'B': ChromaPoint.blue(),
        'W': ChromaPoint.white_3000k()
    }

    # ----------------------------------------------------------------------------------------------------------------

    @classmethod
    def construct_from_jdict(cls, jdict, skeleton=False):
        if not jdict:
            return None

        name = jdict.get('name')
        points = [ChromaPoint.construct_from_jdict(point_jdict) for point_jdict in jdict.get('points')]

        return cls(name, points)


    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, name, points):
        """
        Constructor
        """
        self.__name = name                          # string
        self.__points = points                      # array of ChromaPoint


    def __len__(self):
        return len(self.points)


    # ----------------------------------------------------------------------------------------------------------------

    def range_min(self):
        if not len(self):
            return None

        return self.__points[0]


    # ----------------------------------------------------------------------------------------------------------------

    def has_point(self, index):
        return index in range(len(self))


    def insert_point(self, index, point):
        self.__points.insert(index, point)          # may raise IndexError


    def remove_point(self, index):
        self.__points.pop(index)                    # may raise IndexError


    # ----------------------------------------------------------------------------------------------------------------

    def as_json(self):
        jdict = OrderedDict()

        jdict['name'] = self.name
        jdict['points'] = self.points

        return jdict


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def name(self):
        return self.__name


    @property
    def points(self):
        return self.__points


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return "ChromaPath:{name:%s, points:%s}" % (self.name, Str.collection(self.__points))
