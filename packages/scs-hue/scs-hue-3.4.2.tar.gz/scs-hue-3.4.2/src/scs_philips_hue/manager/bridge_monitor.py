"""
Created on 9 Nov 2023

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)
"""

import time

from multiprocessing import Manager

from scs_core.sync.synchronised_process import SynchronisedProcess
from scs_core.sys.logging import Logging

from scs_philips_hue.manager.bridge_builder import BridgeBuilder
from scs_philips_hue.manager.bridge_manager import BridgeManagerGroup


# --------------------------------------------------------------------------------------------------------------------

class BridgeMonitor(SynchronisedProcess):
    """
    classdocs
    """
    __MONITOR_INTERVAL =        60              # seconds

    # ----------------------------------------------------------------------------------------------------------------

    @classmethod
    def construct(cls, host, credentials_set):
        return cls(BridgeBuilder(host), credentials_set)


    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, builder: BridgeBuilder, credentials_set):
        """
        Constructor
        """
        self.__logger = Logging.getLogger()
        self.__logging_specification = Logging.specification()

        manager = Manager()

        SynchronisedProcess.__init__(self, value=manager.list())

        self.__builder = builder                                        # BridgeBuilder
        self.__credentials_set = credentials_set                        # BridgeCredentialsSet


    # ----------------------------------------------------------------------------------------------------------------
    # SynchronisedProcess implementation...

    def run(self):
        Logging.replicate(self.__logging_specification)

        try:
            while True:
                group = self.__builder.construct_all(self.__credentials_set)

                # report...
                with self._lock:
                    group.as_list(self._value)

                time.sleep(self.__MONITOR_INTERVAL)

        except (KeyboardInterrupt, SystemExit):
            return


    # ----------------------------------------------------------------------------------------------------------------
    # data retrieval for client process...

    @property
    def bridge_manager_group(self):
        with self._lock:
            group = BridgeManagerGroup.construct_from_jdict(self._value)

        return group


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return "BridgeMonitor:{builder:%s, credentials_set:%s}" % (self.__builder, self.__credentials_set)
