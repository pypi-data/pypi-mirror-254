#!/usr/bin/env python3

"""
Created on 11 Nov 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

source repo: scs_philips_hue

DESCRIPTION
The bridge utility is used to interrogate and update the Philips Hue Bridge device.

If a bridge address has been stored, this is used to find the bridge. Otherwise a UPnP or IP scan is attempted.

SYNOPSIS
bridge.py [-p PORTAL_SERVICES] [-c CHECK_UPDATE] [-u DO_UPDATE] [-z CHANNEL] [-i INDENT] [-v] BRIDGE_NAME

EXAMPLES
./bridge.py -vi4 hue-br1-002

FILES
~/SCS/hue/bridge_address_set.json
~/SCS/hue/bridge_credentials_set.json

DOCUMENT EXAMPLE
{"bridge-id": "001788fffe795620", "username": "TIYoqrnwkvyODu8xE9zvRxjIJSRSde0qUzUqqIr7"}

SEE ALSO
scs_philips_hue/bridge_address
scs_philips_hue/join
scs_philips_hue/user

RESOURCES
https://developers.meethue.com/content/configuring-hue-without-phone-app-unable-update-software
"""

import sys

from scs_core.client.http_exception import HTTPException
from scs_core.client.network import Network
from scs_core.client.resource_unavailable_exception import ResourceUnavailableException

from scs_core.data.json import JSONify

from scs_core.sys.logging import Logging

from scs_host.sys.host import Host

from scs_philips_hue.cmd.cmd_bridge import CmdBridge

from scs_philips_hue.config.bridge_credentials import BridgeCredentialsSet

from scs_philips_hue.data.bridge.bridge_config import BridgeConfig
from scs_philips_hue.data.bridge.sw_update import SWUpdate

from scs_philips_hue.manager.bridge_builder import BridgeBuilder


# --------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':

    response = None

    # ----------------------------------------------------------------------------------------------------------------
    # cmd...

    cmd = CmdBridge()

    if not cmd.is_valid():
        cmd.print_help(sys.stderr)
        exit(2)

    Logging.config('bridge', verbose=cmd.verbose)
    logger = Logging.getLogger()

    logger.info(cmd)

    try:
        # ------------------------------------------------------------------------------------------------------------
        # check...

        if not Network.is_available():
            logger.info("waiting for network.")
            Network.wait()


        # ------------------------------------------------------------------------------------------------------------
        # resources...

        # BridgeCredentials...
        credentials_set = BridgeCredentialsSet.load(Host, skeleton=True)

        if len(credentials_set) < 1:
            logger.error("BridgeCredentials not available.")
            exit(1)

        try:
            credentials = credentials_set.credentials(cmd.bridge_name)
            logger.info(credentials)

        except KeyError:
            logger.error("no stored credentials for bridge '%s'." % cmd.bridge_name)
            exit(1)

        # manager...
        manager = BridgeBuilder(Host).construct_manager_for_credentials(credentials)


        # ------------------------------------------------------------------------------------------------------------
        # run...

        # initial state...
        config = manager.find()

        # portal services...
        if cmd.portal_services:
            config = BridgeConfig(portal_services=cmd.portal_services)
            response = manager.set_config(config)

        # check for update...
        if cmd.check_update:
            config = BridgeConfig(sw_update=SWUpdate(check_for_update=cmd.check_update))
            response = manager.set_config(config)

        # do update...
        if cmd.do_update:
            if config.sw_update.update_state != SWUpdate.UPDATE_AVAILABLE:
                logger.error("no software update available.")
                exit(1)

            config = BridgeConfig(sw_update=SWUpdate(update_state=SWUpdate.UPDATE_PERFORM))
            response = manager.set_config(config)

        # zigbee...
        if cmd.zigbee_channel:
            config = BridgeConfig(zigbee_channel=cmd.zigbee_channel)
            response = manager.set_config(config)

        if response:
            logger.info(response)

        config = manager.find()
        print(JSONify.dumps(config, indent=cmd.indent))


    # ----------------------------------------------------------------------------------------------------------------
    # end...

    except KeyboardInterrupt:
        print(file=sys.stderr)

    except (ConnectionError, HTTPException, ResourceUnavailableException) as ex:
        logger.error(repr(ex))
        exit(1)

    except TimeoutError:
        logger.error("Timeout")
        exit(1)
