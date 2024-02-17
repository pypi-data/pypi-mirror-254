"""
Created on 5 Nov 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

https://en.wikipedia.org/wiki/Chromaticity
https://developers.meethue.com/documentation/core-concepts
"""

from collections import OrderedDict

from scs_core.data.json import JSONable
from scs_core.data.str import Str


# --------------------------------------------------------------------------------------------------------------------

class ChromaMapping(object):
    """
    classdocs
    """

    # ----------------------------------------------------------------------------------------------------------------

    @classmethod
    def construct(cls, conf, path):
        if len(path) < 2:
            raise ValueError("path too short: %s" % path)

        # initialise...
        interval_domain_max = conf.domain_min
        domain_delta = (conf.domain_max - conf.domain_min) / (len(path) - 1)

        # build segments...
        prev_point = None
        segments = OrderedDict()

        for point in path.points:
            if prev_point is not None:
                key = round(interval_domain_max, 1)
                segments[key] = ChromaSegment.construct(prev_point, point)

            prev_point = point
            interval_domain_max += domain_delta

        return cls(conf.domain_min, conf.domain_max, segments)


    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, domain_min, domain_max, segments):
        """
        Constructor
        """
        self.__domain_min = domain_min                  # int
        self.__domain_max = domain_max                  # int

        self.__segments = segments                      # OrderedDict of int domain_max: ChromaSegment


    def __len__(self):
        return len(self.segments)


    # ----------------------------------------------------------------------------------------------------------------

    def interpolate(self, domain_value):
        # adjust for out-of-range...
        domain_value = self.domain_min if domain_value < self.domain_min else domain_value
        domain_value = self.domain_max if domain_value > self.domain_max else domain_value

        domain_min = self.domain_min

        # find segment for interpolation...
        for domain_max, segment in self.segments.items():
            if domain_value <= domain_max:
                return segment.interpolate(domain_min, domain_max, domain_value)

            domain_min = domain_max


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def domain_min(self):
        return self.__domain_min


    @property
    def domain_max(self):
        return self.__domain_max


    @property
    def segments(self):
        return self.__segments


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return "ChromaMapping:{domain_min:%s, domain_max:%s, segments:%s}" % \
               (self.domain_min, self.domain_max, Str.collection(self.__segments))


# --------------------------------------------------------------------------------------------------------------------

class ChromaSegment(object):
    """
    classdocs
    """

    # ----------------------------------------------------------------------------------------------------------------

    @classmethod
    def construct(cls, start, end):
        delta_x = end.x - start.x
        delta_y = end.y - start.y

        return ChromaSegment(start, end, delta_x, delta_y)

    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, start, end, delta_x, delta_y):
        """
        Constructor
        """
        self.__start = start                        # ChromaPoint
        self.__end = end                            # ChromaPoint

        self.__delta_x = delta_x
        self.__delta_y = delta_y


    # ----------------------------------------------------------------------------------------------------------------

    def interpolate(self, domain_min, domain_max, domain_value):
        intermediate = (domain_value - domain_min) / (domain_max - domain_min)

        if not (0.0 <= intermediate <= 1.0):
            raise ValueError(domain_value)

        x = self.start.x + (self.__delta_x * intermediate)
        y = self.start.y + (self.__delta_y * intermediate)

        return ChromaPoint(x, y)


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def start(self):
        return self.__start


    @property
    def end(self):
        return self.__end


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return "ChromaSegment:{start:%s, end:%s, delta_x:%0.4f, delta_y:%0.4f}" %  \
               (self.start, self.end, self.__delta_x, self.__delta_y)


# --------------------------------------------------------------------------------------------------------------------

class ChromaPoint(JSONable):
    """
    classdocs
    """

    # ----------------------------------------------------------------------------------------------------------------

    @classmethod
    def red(cls):
        return ChromaPoint(0.74, 0.26)


    @classmethod
    def green(cls):
        return ChromaPoint(0.08, 0.84)


    @classmethod
    def blue(cls):
        return ChromaPoint(0.17, 0.01)


    @classmethod
    def white_3000k(cls):
        return ChromaPoint(0.48, 0.41)


    @classmethod
    def white_6000k(cls):
        return ChromaPoint(0.32, 0.26)


    # ----------------------------------------------------------------------------------------------------------------

    @classmethod
    def construct_from_jdict(cls, jarray):
        if not jarray:
            return None

        x = jarray[0]
        y = jarray[1]

        return ChromaPoint(x, y)


    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, x, y):
        """
        Constructor
        """
        self.__x = round(float(x), 4)                   # float
        self.__y = round(float(y), 4)                   # float


    # ----------------------------------------------------------------------------------------------------------------

    def as_json(self):
        return self.x, self.y


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def x(self):
        return self.__x


    @property
    def y(self):
        return self.__y


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return "ChromaPoint:{x:%0.4f, y:%0.4f}" %  (self.x, self.y)
