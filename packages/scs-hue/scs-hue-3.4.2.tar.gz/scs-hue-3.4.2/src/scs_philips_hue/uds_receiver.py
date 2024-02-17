#!/usr/bin/env python3

"""
Created on 11 Apr 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

source repo: scs_philips_hue

DESCRIPTION
The uds_receiver utility is used to accept data via a Unix domain socket, with data sourced from the same host, or
another host on the same local area network.

SYNOPSIS
uds_receiver.py [-v] UDS_SUB

EXAMPLES
./uds_receiver.py scs-particulates.uds

SEE ALSO
scs_analysis/socket_receiver
"""

import sys

from scs_core.comms.uds_reader import UDSReader

from scs_core.sys.logging import Logging
from scs_core.sys.signalled_exit import SignalledExit

from scs_host.comms.domain_socket import DomainSocket

from scs_philips_hue.cmd.cmd_uds import CmdUDS


# --------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':

    # ----------------------------------------------------------------------------------------------------------------
    # cmd...

    cmd = CmdUDS()

    if not cmd.is_valid():
        cmd.print_help(sys.stderr)
        exit(2)

    Logging.config('uds_receiver', verbose=cmd.verbose)
    logger = Logging.getLogger()

    logger.info(cmd)


    # ----------------------------------------------------------------------------------------------------------------
    # resources...

    uds = UDSReader(DomainSocket, cmd.path)
    logger.info(uds)

    try:
        # ------------------------------------------------------------------------------------------------------------
        # run...

        # signal handler...
        SignalledExit.construct()

        uds.connect()

        for message in uds.messages():
            print(message)
            sys.stdout.flush()


    # ----------------------------------------------------------------------------------------------------------------
    # end...

    except (KeyboardInterrupt, SystemExit):
        pass

    finally:
        logger.info("finishing")
        uds.close()
