"""
Created on 27 Oct 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

header:
CURLOPT_HTTPHEADER => array('Accept: application/json')

https://developers.meethue.com/news/
"""

import json

from scs_core.client.http_client import HTTPClient
from scs_core.client.http_exception import HTTPException

from scs_core.sys.logging import Logging


# --------------------------------------------------------------------------------------------------------------------

class UPnPClient(object):
    """
    classdocs
    """

    __HOST = "discovery.meethue.com"            # hard-coded URL - was "www.meethue.com"
    __PATH = ""                                 # hard-coded URL - was "/api/nupnp"

    __HEADER_ACCEPT = "application/json"


    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self):
        """
        Constructor
        """
        self.__http_client = HTTPClient()
        self.__logger = Logging.getLogger()


    # ----------------------------------------------------------------------------------------------------------------

    def connect(self):
        self.__http_client.connect(self.__HOST)


    def close(self):
        self.__http_client.close()


    # ----------------------------------------------------------------------------------------------------------------

    def get(self):
        try:
            response_jstr = self.__http_client.get(self.__PATH, {}, self.__headers)
        except HTTPException as exc:
            self.__logger.info(exc)
            return tuple()

        return json.loads(response_jstr)


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def __headers(self):
        return {"Accept": self.__HEADER_ACCEPT}


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return "UPnPClient:{}"
