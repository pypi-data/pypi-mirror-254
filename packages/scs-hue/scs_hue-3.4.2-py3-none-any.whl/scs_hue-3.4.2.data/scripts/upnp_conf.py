#!python

"""
Created on 22 Nov 2023

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

source repo: scs_philips_hue

DESCRIPTION
The upnp_conf utility is used to enable or disable networking UPnP discovery for all relevant SCS Philips Hue utilities.

Note: by default, UPnP discovery is not enabled.

SYNOPSIS
Usage: upnp_conf.py [-e { 0 | 1 }] [-i INDENT] [-v]

EXAMPLES
./upnp_conf.py -v

FILES
~/SCS/hue/upnp_conf.json

DOCUMENT EXAMPLE
{"upnp-enabled": false}

SEE ALSO
scs_philips_hue/bridge
scs_philips_hue/join
scs_philips_hue/light
scs_philips_hue/user
"""

import sys

from scs_core.data.json import JSONify
from scs_core.sys.logging import Logging

from scs_host.sys.host import Host

from scs_philips_hue.cmd.cmd_upnp_conf import CmdUPnPConf
from scs_philips_hue.discovery.upnp_conf import UPnPConf


# --------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':

    bridge = None

    # ----------------------------------------------------------------------------------------------------------------
    # cmd...

    cmd = CmdUPnPConf()

    if not cmd.is_valid():
        cmd.print_help(sys.stderr)
        exit(2)

    Logging.config('upnp_conf', verbose=cmd.verbose)
    logger = Logging.getLogger()

    logger.info(cmd)

    try:
        # ----------------------------------------------------------------------------------------------------------------
        # resources...

        config = UPnPConf.load(Host, skeleton=True)


        # ----------------------------------------------------------------------------------------------------------------
        # run...

        if cmd.set():
            config = UPnPConf(cmd.enable)
            config.save(Host)

        # report...
        print(JSONify.dumps(config, indent=cmd.indent))


    # ----------------------------------------------------------------------------------------------------------------
    # end...

    except KeyboardInterrupt:
        print(file=sys.stderr)

