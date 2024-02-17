#!/usr/bin/env python3

"""
Created on 4 Nov 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

source repo: scs_philips_hue

DESCRIPTION
The light utility is used to shifter a Philips Hue light bulb with a Philips Hue bridge device, to update bulb
settings.

If a bridge address has been stored, this is used to find the bridge. Otherwise a UPnP or IP scan is attempted.

SYNOPSIS
light.py { -c | -l BRIDGE_NAME | -s BRIDGE_NAME | -a BRIDGE_NAME SERIAL_NUMBER | -n BRIDGE_NAME INDEX LIGHT_NAME |
-r BRIDGE_NAME INDEX } [-i INDENT] [-v]

EXAMPLES
./light.py -vi4 -n hue-br1-001 1 "r&d"

FILES
~/SCS/hue/bridge_address_set.json
~/SCS/hue/bridge_credentials_set.json

DOCUMENT EXAMPLE - OUTPUT
{"5": {"state": {"on": false, "bri": 0, "hue": 0, "sat": 0, "effect": "none", "transitiontime": null, "xy": [0.0, 0.0],
"ct": 0, "alert": "none", "colormode": "hs", "reachable": false}, "swupdate": {"state": "transferring",
"lastinstall": null}, "type": "Extended color light", "name": "scs-hcl-001", "modelid": "LCT015",
"manufacturername": "Philips", "uniqueid": "00:17:88:01:03:54:25:66-0b", "swversion": "1.19.0_r19755",
"swconfigid": "A724919D", "productid": "Philips-LCT015-1-A19ECLv5"}}

SEE ALSO
scs_philips_hue/bridge
scs_philips_hue/join

BUGS
The light search function is not always successful if lights have been previously registered on the bridge. If a search
does not find the light, then the light should be acquired with -a BRIDGE_NAME SERIAL_NUMBER.
"""

import sys
import time

from scs_core.client.http_exception import HTTPException
from scs_core.client.network import Network
from scs_core.client.resource_unavailable_exception import ResourceUnavailableException

from scs_core.data.json import JSONify

from scs_core.sys.logging import Logging

from scs_host.sys.host import Host

from scs_philips_hue.cmd.cmd_light import CmdLight

from scs_philips_hue.config.bridge_credentials import BridgeCredentialsSet

from scs_philips_hue.manager.bridge_builder import BridgeBuilder

from scs_philips_hue.data.light.light_catalogue import LightCatalogue
from scs_philips_hue.data.light.light_device import LightDevice

from scs_philips_hue.manager.light_manager import LightManager


# --------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':

    manager = None

    # ----------------------------------------------------------------------------------------------------------------
    # cmd...

    cmd = CmdLight()

    if not cmd.is_valid():
        cmd.print_help(sys.stderr)
        exit(2)

    Logging.config('light', verbose=cmd.verbose)
    logger = Logging.getLogger()

    logger.info(cmd)

    try:
        # ------------------------------------------------------------------------------------------------------------
        # check...

        if not Network.is_available():
            logger.info("waiting for network")
            Network.wait()


        # ------------------------------------------------------------------------------------------------------------
        # resources...

        # BridgeCredentials...
        credentials_set = BridgeCredentialsSet.load(Host, skeleton=True)

        if len(credentials_set) < 1:
            logger.error("BridgeCredentials not available.")
            exit(1)

        # Managers...
        builder = BridgeBuilder(Host)

        bridge_managers = builder.construct_dict_for_credentials(credentials_set[cmd.bridge_name]) if cmd.bridge_name \
            else builder.construct_all(credentials_set)

        light_managers = LightManager.construct_all(bridge_managers)

        # LightCatalogue...
        light_catalogue = LightCatalogue.construct(light_managers)

        try:
            if cmd.bridge_name:
                manager = light_managers[cmd.bridge_name]
        except KeyError:
            logger.error("bridge '%s' was not found." % cmd.bridge_name)
            exit(1)


        # ------------------------------------------------------------------------------------------------------------
        # run...

        if cmd.name and cmd.light_name in light_catalogue:
            logger.error("name '%s' is already in use." % cmd.light_name)
            exit(2)


        # ------------------------------------------------------------------------------------------------------------
        # run...

        # search...
        if cmd.search:
            response = manager.search()
            logger.info("searching...")

            while True:
                time.sleep(2)
                scan = manager.find_new()
                if not scan.is_active():
                    break

            for entry in scan.entries:
                print(JSONify.dumps(entry, indent=cmd.indent))

        # add...
        if cmd.add:
            device = LightDevice(cmd.serial_number)
            response = manager.search(device=device)
            logger.info("adding...")

            while True:
                time.sleep(2.0)
                scan = manager.find_new()
                if not scan.is_active():
                    break

            for entry in scan.entries:
                print(JSONify.dumps(entry, indent=cmd.indent))

        # name...
        if cmd.name:
            response = manager.rename(cmd.index, cmd.light_name)

        # delete...
        if cmd.remove:
            response = manager.delete(cmd.index)

        # result...
        if cmd.catalogue:
            print(JSONify.dumps(light_catalogue, indent=cmd.indent))

        if cmd.name or cmd.remove or cmd.list:
            lights = manager.find_all()

            for light in lights:
                print(JSONify.dumps(light, indent=cmd.indent))


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
