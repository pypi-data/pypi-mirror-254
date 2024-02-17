#!/usr/bin/env python3

"""
Created on 1 Dec 2024

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

source repo: scs_philips_hue

DESCRIPTION
The channel_test utility is used to test both the channel chroma conf and desk configuration - both must be
configured before using this utility.

SYNOPSIS
channel_test.py -c CHANNEL [-i INTERVAL] [-f] [-v]

EXAMPLES
./channel_test.py -v -c channel-1 -t 2 -f | ./desk.py -v

DOCUMENT EXAMPLE - OUTPUT
{"channel-1": {"bri": 254, "transitiontime": 20, "xy": [0.05, 0.5]}}
...

SEE ALSO
scs_philips_hue/chroma_conf
scs_philips_hue/desk
scs_philips_hue/desk_conf

RESOURCES
https://en.wikipedia.org/wiki/Chromaticity
"""

import sys
import time

from scs_core.data.json import JSONify
from scs_core.sys.logging import Logging

from scs_host.sys.host import Host

from scs_philips_hue.cmd.cmd_channel_test import CmdChannelTest

from scs_philips_hue.config.chroma_conf import ChromaConfSet

from scs_philips_hue.data.light.chroma import ChromaPoint
from scs_philips_hue.data.light.light_state import LightState


# --------------------------------------------------------------------------------------------------------------------

def print_state(state, pause):
    print(JSONify.dumps({cmd.channel: state}))
    sys.stdout.flush()

    time.sleep(transition_time + pause)


# --------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':

    # ----------------------------------------------------------------------------------------------------------------
    # cmd...

    cmd = CmdChannelTest()

    Logging.config('channel_test', verbose=cmd.verbose)
    logger = Logging.getLogger()

    logger.info(cmd)

    try:
        # ------------------------------------------------------------------------------------------------------------
        # resources...

        # ChromaConf...
        chroma_confs = ChromaConfSet.load(Host)

        if chroma_confs is None:
            logger.error("ChromaConfSet not available.")
            exit(1)

        logger.info(chroma_confs)

        chroma_conf = chroma_confs.conf(cmd.channel)

        if chroma_conf is None:
            logger.error("ChromaConf not available for channel '%s'." % cmd.channel)
            exit(1)

        logger.info(chroma_conf)

        path = chroma_conf.path()
        logger.info(path)

        brightness = chroma_conf.brightness
        transition_time = chroma_conf.transition_time if cmd.transition_time is None else cmd.transition_time


        # ------------------------------------------------------------------------------------------------------------
        # run...

        while True:
            # path points...
            for point in path.points:
                print_state(LightState(bri=brightness, xy=point, transition_time=transition_time), 1)

            if not cmd.forever:
                break

            # white interval...
            print_state(LightState(bri=brightness, xy=ChromaPoint.white_3000k(), transition_time=transition_time), 3)


    # ----------------------------------------------------------------------------------------------------------------
    # end...

    except KeyboardInterrupt:
        print(file=sys.stderr)
