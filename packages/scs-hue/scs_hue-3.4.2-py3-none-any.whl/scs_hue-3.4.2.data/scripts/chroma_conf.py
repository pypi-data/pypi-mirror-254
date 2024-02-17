#!python

"""
Created on 16 Mar 2018

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

source repo: scs_philips_hue

DESCRIPTION
The chroma_conf utility is used to specify the parameters of a mapping from environmental data domain values to
locations in a chromaticity space. In addition to chromaticity mapping, the configuration includes lamp brightness and
transition time.

A chromaticity chart is available at: https://developers.meethue.com/documentation/core-concepts

The chroma_conf utility works in conjunction with a chroma path: the path specifies two or more ordered points in
chroma space, indicating a progression through different colours as a domain value changes. The chroma path
specifies the shape of this route, the chroma conf specifies the minimum and maximum domain values associated
with a progression though the chroma space.

Note that - currently - there is no command line utility to edit chroma paths, and only default paths can be used.

SYNOPSIS
chroma_conf.py [-c CHANNEL { [-p PATH_NAME] [-l DOMAIN_MIN] [-u DOMAIN_MAX] [-b BRIGHTNESS] [-t TRANSITION] | -r }]
[-i INDENT] [-v]

EXAMPLES
./chroma_conf.py -vi4 -c preston-circus-pm10 -p risk_level -l 0 -u 50 -b 254 -t 9

FILES
~/SCS/hue/chroma_conf_set.json

DOCUMENT EXAMPLE
{
    "preston_circus": {
        "path-name": "risk_level",
        "domain-min": 0.0,
        "domain-max": 50.0,
        "brightness": 254,
        "transition-time": 9
    }
}

SEE ALSO
scs_philips_hue/chroma

RESOURCES
https://en.wikipedia.org/wiki/Chromaticity
https://developers.meethue.com/documentation/core-concepts
"""

import sys

from scs_core.data.json import JSONify
from scs_core.sys.logging import Logging

from scs_host.sys.host import Host

from scs_philips_hue.cmd.cmd_chroma_conf import CmdChromaConf
from scs_philips_hue.config.chroma_conf import ChromaConfSet


# --------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':

    # ----------------------------------------------------------------------------------------------------------------
    # cmd...

    cmd = CmdChromaConf()

    if not cmd.is_valid():
        cmd.print_help(sys.stderr)
        exit(2)

    Logging.config('chroma_conf', verbose=cmd.verbose)
    logger = Logging.getLogger()

    logger.info(cmd)


    # ----------------------------------------------------------------------------------------------------------------
    # resources...

    # ChromaConf...
    chromas = ChromaConfSet.load(Host, skeleton=True)


    # ----------------------------------------------------------------------------------------------------------------
    # run...

    if cmd.set():
        chroma = chromas.conf(cmd.channel)

        if chroma is None:
            if not cmd.is_complete():
                logger.error("no configuration is stored - you must therefore set all fields.")
                exit(2)

            chromas.add(cmd.channel, cmd.path_name, cmd.domain_min, cmd.domain_max, cmd.brightness, cmd.transition_time)

        else:
            path_name = chroma.path_name if cmd.path_name is None else cmd.path_name
            domain_min = chroma.domain_min if cmd.domain_min is None else cmd.domain_min
            domain_max = chroma.domain_max if cmd.domain_max is None else cmd.domain_max
            brightness = chroma.brightness if cmd.brightness is None else cmd.brightness
            transition_time = chroma.transition_time if cmd.transition_time is None else cmd.transition_time

            chromas.add(cmd.channel, path_name, domain_min, domain_max, brightness, transition_time)

        chromas.save(Host)

    if cmd.remove:
        chromas.remove(cmd.channel)
        chromas.save(Host)


    if chromas:
        print(JSONify.dumps(chromas, indent=cmd.indent))
