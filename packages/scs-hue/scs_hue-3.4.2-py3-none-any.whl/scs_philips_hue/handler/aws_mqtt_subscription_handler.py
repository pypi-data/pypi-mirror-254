"""
Created on 27 Sep 2018

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)
"""

import json

from scs_core.data.json import JSONify
from scs_core.data.publication import Publication

from scs_core.sys.logging import Logging


# --------------------------------------------------------------------------------------------------------------------
# subscription handler...

class AWSMQTTSubscriptionHandler(object):
    """
    classdocs
    """

    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, comms=None):
        """
        Constructor
        """
        self.__comms = comms                            # UDSWriter
        self.__logger = Logging.getLogger()


    # ----------------------------------------------------------------------------------------------------------------

    # noinspection PyUnusedLocal

    def handle(self, client, userdata, message):
        payload = message.payload.decode()
        payload_jdict = json.loads(payload)

        publication = Publication(message.topic, payload_jdict)

        try:
            self.__comms.connect()
            self.__comms.write(JSONify.dumps(publication), False)

        except ConnectionError:
            self.__logger.info("ConnectionError: %s" % self.__comms)

        finally:
            self.__comms.close()

        self.__logger.info(JSONify.dumps(publication))


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return "AWSMQTTSubscriptionHandler:{comms:%s}" % self.__comms


