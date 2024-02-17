#!python

"""
Created on 3 Nov 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

source repo: scs_philips_hue

DESCRIPTION
The join utility is used to pair a controller device - the device hosting this software - with a Philips Hue Bridge.
Once running join, the big button on the top of the Philips Hue Bridge must be pressed!

The bridge_credentials.json document created by the join utility is used by the bridge, desk, light, and user utilities.

SYNOPSIS
join.py [-i INDENT] [-v] BRIDGE_NAME

EXAMPLES
./join.py -v

FILES
~/SCS/hue/bridge_address_set.json
~/SCS/hue/bridge_credentials_set.json

DOCUMENT EXAMPLE
{
    "hue-br1-001": {
        "bridge-id": "001788FFFEAF8430",
        "username": "DN5YzKBncC6n69gjlKZqa6SRqZofXTmhZkrdnqG2"
    },
    "hue-br1-002": {
        "bridge-id": "001788FFFE795620",
        "username": "suLJJv6OgxG0UjwB9Uz7e1j08Xj36MOfFdxNNUmR"
    }
}

SEE ALSO
scs_philips_hue/bridge
scs_philips_hue/desk
scs_philips_hue/light
scs_philips_hue/user
"""

import sys

from scs_core.client.http_exception import HTTPException
from scs_core.client.network import Network
from scs_core.client.resource_unavailable_exception import ResourceUnavailableException

from scs_core.data.json import JSONify

from scs_core.sys.logging import Logging

from scs_host.comms.stdio import StdIO
from scs_host.sys.host import Host

from scs_philips_hue.cmd.cmd_join import CmdJoin

from scs_philips_hue.config.bridge_address import BridgeAddress, BridgeAddressSet
from scs_philips_hue.config.bridge_credentials import BridgeCredentials, BridgeCredentialsSet

from scs_philips_hue.data.bridge.bridge_config import BridgeConfig

from scs_philips_hue.discovery.discovery import Discovery

from scs_philips_hue.manager.bridge_manager import BridgeManager
from scs_philips_hue.manager.user_manager import UserManager

from scs_philips_hue.data.client.client_description import ClientDescription
from scs_philips_hue.data.client.device_description import DeviceDescription


# --------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':

    bridge = None

    # ----------------------------------------------------------------------------------------------------------------
    # cmd...

    cmd = CmdJoin()

    if not cmd.is_valid():
        cmd.print_help(sys.stderr)
        exit(2)

    Logging.config('join', verbose=cmd.verbose)
    logger = Logging.getLogger()

    logger.info(cmd)

    try:
        # ------------------------------------------------------------------------------------------------------------
        # check...

        if not Network.is_available():
            logger.info("waiting for network")
            Network.wait()


        # ----------------------------------------------------------------------------------------------------------------
        # resources...

        # BridgeCredentialsSet...
        credentials_set = BridgeCredentialsSet.load(Host, skeleton=True)
        credentials_set.delete(cmd.bridge_name)
        credentials_set.save(Host)

        logger.info(credentials_set)

        # BridgeAddressSet...
        address_set = BridgeAddressSet.load(Host, skeleton=True)
        address_set.delete(cmd.bridge_name)
        address_set.save(Host)

        logger.info(address_set)

        # device...
        client = ClientDescription(ClientDescription.APP, Host.name())

        device = DeviceDescription(client)
        logger.info(device)

        # bridges...
        discovery = Discovery(Host)
        bridges = list(discovery.find_all())

        if len(bridges) == 0:
            logger.error("no bridge found.")
            exit(1)


        # ----------------------------------------------------------------------------------------------------------------
        # find bridge with button pressed...

        StdIO.prompt('Press the button! (Then hit RETURN)')

        success = None

        for bridge in bridges:
            logger.info(bridge)

            # manager...
            bridge_manager = BridgeManager(bridge.ip_address, None)

            # register...
            try:
                response = bridge_manager.register(device)
            except TimeoutError:
                logger.error("no response from bridge.")
                continue

            if response.has_errors():
                for error in response.errors:
                    logger.error(error.description)
                continue

            # get credentials...
            success = response.successes.pop()
            break

        if success is None:
            exit(1)


        # ----------------------------------------------------------------------------------------------------------------
        # run...

        # get bridge...
        bridge_manager = BridgeManager(bridge.ip_address, success.value)
        config = bridge_manager.find()

        # build credentials...
        credentials = BridgeCredentials(cmd.bridge_name, config.bridge_id, success.value)

        # delete old whitelist entries for this user (non-functional API)...
        user_manager = UserManager(bridge.ip_address, credentials.username)
        users = user_manager.find_all()

        for user in users:
            if user.description.user == Host.name() and user.username != credentials.username:
                response = user_manager.delete(user.username)

        # set bridge name...
        response = bridge_manager.set_config(BridgeConfig(name=cmd.bridge_name))

        # save address...
        address = BridgeAddress.construct(cmd.bridge_name, config.ip_address)
        address_set.add(address)
        address_set.save(Host)

        # save credentials...
        credentials_set.add(credentials)
        credentials_set.save(Host)

        # report...
        bridge_manager = BridgeManager(bridge.ip_address, credentials.username)
        config = bridge_manager.find()

        print(JSONify.dumps(config, indent=cmd.indent))


    # ----------------------------------------------------------------------------------------------------------------
    # end...

    except KeyboardInterrupt:
        print(file=sys.stderr)

    except (ConnectionError, HTTPException, ResourceUnavailableException) as ex:
        logger.error(repr(ex))
        exit(1)

