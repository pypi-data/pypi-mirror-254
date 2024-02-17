#!/usr/bin/env python3

"""
Created on 4 Nov 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

source repo: scs_philips_hue

DESCRIPTION
The user utility is used to manage user accounts or "whitelist entries" on a Philips Hue Bridge device.

Note that the user JSON document presented by the user utility has a description field of the form
app#user-name. When a delete command is performed, only the user-name component should be used to identify
the user.

SYNOPSIS
user.py { -l | -r USER } [-i INDENT] [-v] BRIDGE_NAME

EXAMPLES
./user.py -vi4 -l hue-br1-001

FILES
~/SCS/hue/bridge_address_set.json
~/SCS/hue/bridge_credentials_set.json

DOCUMENT EXAMPLE - OUTPUT
[{"username": "JuA71dSBcObSJi255VatGFEQxOFDu6lOzDqCtjtI", "last use date": "2023-04-21T10:21:34",
"create date": "2023-04-21T08:10:33", "description": "scs-hue-connector#bruno16"}]


SEE ALSO
scs_philips_hue/join
scs_philips_hue/bridge
scs_philips_hue/desk
"""

import sys

from scs_core.client.http_exception import HTTPException
from scs_core.client.resource_unavailable_exception import ResourceUnavailableException

from scs_core.data.json import JSONify

from scs_core.sys.logging import Logging

from scs_host.sys.host import Host

from scs_philips_hue.cmd.cmd_user import CmdUser

from scs_philips_hue.config.bridge_credentials import BridgeCredentialsSet

from scs_philips_hue.manager.bridge_builder import BridgeBuilder
from scs_philips_hue.manager.user_manager import UserManager


# --------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':

    application_key = ''

    bridge = None

    # ----------------------------------------------------------------------------------------------------------------
    # cmd...

    cmd = CmdUser()

    if not cmd.is_valid():
        cmd.print_help(sys.stderr)
        exit(2)

    Logging.config('user', verbose=cmd.verbose)
    logger = Logging.getLogger()

    logger.info(cmd)

    try:

        # -------------------------------------------------------------------------------------------------------------
        # resource...


        # credentials...
        credentials_set = BridgeCredentialsSet.load(Host, skeleton=True)

        try:
            credentials = credentials_set.credentials(cmd.bridge_name)
            logger.info(credentials)

        except KeyError:
            logger.error("no stored credentials for bridge '%s'." % cmd.bridge_name)
            exit(1)

        # manager...
        bridge_manager = BridgeBuilder(Host).construct_manager_for_credentials(credentials)
        bridge = bridge_manager.find()

        # manager...
        manager = UserManager(bridge.ip_address, credentials.username)


        # ------------------------------------------------------------------------------------------------------------
        # run...

        users = manager.find_all()

        if cmd.remove:
            for user in users:
                if user.description.user == cmd.remove:
                    response = manager.delete(user.username)
                    logger.info(response)

        else:
            print(JSONify.dumps(users, indent=cmd.indent))


    # ----------------------------------------------------------------------------------------------------------------
    # end...

    except KeyboardInterrupt:
        print(file=sys.stderr)

    except (ConnectionError, HTTPException, ResourceUnavailableException) as ex:
        logger.error(repr(ex))
        exit(1)
