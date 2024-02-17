#!/usr/bin/env python3

"""
Created on 2 Apr 2018

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

source repo: scs_analysis

DESCRIPTION
If the Philips Hue bridge has a known, fixed IP address and / or an IP scan is impractical, the bridge_address utility
may be used to record its IPv4 address. (The address can usually be found with a ZeroConf browser.)

SYNOPSIS
bridge_address.py { -l | -r BRIDGE_NAME } [-i INDENT] [-v]

EXAMPLES
./bridge_address.py -s 192.168.2.29

FILES
~/SCS/hue/bridge_address_set.json
~/SCS/hue/bridge_credentials_set.json

DOCUMENT EXAMPLE
{
    "hue-br1-001": {
        "ipv4": "192.168.1.16"
    },
    "hue-br1-002": {
        "ipv4": "192.168.1.8"
    }
}

SEE ALSO
scs_philips_hue/bridge
"""

from scs_core.data.json import JSONify
from scs_core.sys.logging import Logging

from scs_host.sys.host import Host

from scs_philips_hue.cmd.cmd_bridge_address import CmdBridgeAddress
from scs_philips_hue.config.bridge_address import BridgeAddressSet


# --------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':

    # ----------------------------------------------------------------------------------------------------------------
    # cmd...

    cmd = CmdBridgeAddress()

    Logging.config('bridge_address', verbose=cmd.verbose)
    logger = Logging.getLogger()

    logger.info(cmd)


    # ----------------------------------------------------------------------------------------------------------------
    # resources...

    # BridgeAddressSet...
    address_set = BridgeAddressSet.load(Host, skeleton=True)


    # ----------------------------------------------------------------------------------------------------------------
    # run...

    if cmd.remove:
        address_set.delete(cmd.remove)
        address_set.save(Host)

    print(JSONify.dumps(address_set, indent=cmd.indent))
