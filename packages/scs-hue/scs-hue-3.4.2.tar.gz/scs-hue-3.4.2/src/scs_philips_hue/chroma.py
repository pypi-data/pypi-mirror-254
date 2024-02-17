#!/usr/bin/env python3

"""
Created on 4 Nov 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

source repo: scs_philips_hue

DESCRIPTION
The chroma utility is used to map environmental data domain values to chromaticity locations. Input data is received
from stdin, and is interpreted as a float value. The mapped value is written to stdout in the form of a JSON
scs_philips_hue.data.light.LightState document.

The chroma utility requires the chroma_conf.json document, specifying the parameters for the mapping.

SYNOPSIS
chroma.py [-v]

EXAMPLES
./aws_mqtt_subscriber.py -vce | ./node.py -c | ./chroma.py -v

FILES
~/SCS/hue/chroma_conf_set.json

DOCUMENT EXAMPLE - OUTPUT
{"PM10": {"bri": 254, "transitiontime": 90, "xy": [0.3521, 0.6198]}}

SEE ALSO
scs_philips_hue/chroma_conf
scs_philips_hue/desk

RESOURCES
https://en.wikipedia.org/wiki/Chromaticity
https://developers.meethue.com/documentation/core-concepts
"""

import json
import sys

from scs_core.data.json import JSONify

from scs_core.sys.logging import Logging
from scs_core.sys.signalled_exit import SignalledExit

from scs_host.sys.host import Host

from scs_philips_hue.cmd.cmd_chroma import CmdChroma

from scs_philips_hue.config.chroma_conf import ChromaConfSet

from scs_philips_hue.data.light.light_state import LightState


# --------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':

    # ----------------------------------------------------------------------------------------------------------------
    # cmd...

    cmd = CmdChroma()

    Logging.config('chroma', verbose=cmd.verbose)
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

        # ChromaMapping...
        mappings = {}
        for name, chroma_conf in chroma_confs.confs.items():
            path = chroma_conf.path()

            if path is None:
                logger.error("%s: ChromaPath not available." % name)
                exit(1)

            logger.info("%s: %s" % (name, path))

            mappings[name] = chroma_conf.mapping(path)


        # ------------------------------------------------------------------------------------------------------------
        # run...

        # signal handler...
        SignalledExit.construct()

        # read stdin...
        for line in sys.stdin:
            datum = json.loads(line)

            if datum is None:
                break

            for name, chroma_conf in chroma_confs.confs.items():
                if name not in datum:
                    continue

                try:
                    value = float(datum[name])
                except (TypeError, ValueError) as ex:
                    logger.error("%s: %s" % (ex.__class__.__name__, datum))
                    continue

                logger.info("%s: domain value: %s" % (name, value))

                # interpolate...
                interpolation = mappings[name].interpolate(value)
                state = LightState(bri=chroma_conf.brightness, xy=interpolation,
                                   transition_time=chroma_conf.transition_time)

                print(JSONify.dumps({name: state}))
                sys.stdout.flush()

                break


    # ----------------------------------------------------------------------------------------------------------------
    # end...

    except KeyboardInterrupt:
        print(file=sys.stderr)

    except SystemExit:
        pass

    finally:
        logger.info("finishing")
