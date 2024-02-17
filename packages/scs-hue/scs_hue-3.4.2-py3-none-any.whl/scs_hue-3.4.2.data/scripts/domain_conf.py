#!python

"""
Created on 16 Mar 2018

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

source repo: scs_philips_hue

DESCRIPTION
The domain_conf utility is used to specify an environmental data messaging topic path, plus a leaf node within
documents delivered on that messaging topic. Together, these two parameters yield a scalar value that can be
accepted by a mapping utility such as chroma.

The domain_conf.json document managed by the domain_conf utility is used by the aws_mqtt_subscriber and node utilities.

SYNOPSIS
domain_conf.py [-c CHANNEL { -a TOPIC_PATH DOMAIN_NODE | -r }] [-i INDENT] [-v]

EXAMPLES
./domain_conf.py -vi4 -c assembly-co2 -a south-coast-science-production/freshfield-environment/loc/1/gases val.CO2.cnc

FILES
~/SCS/hue/domain_conf_set.json

DOCUMENT EXAMPLE
{"NO2": {"topic-path": "south-coast-science-demo/brighton/loc/1/gases", "document-node": "exg.val.NO2.cnc"},
"PM10": {"topic-path": "south-coast-science-demo/brighton/loc/1/particulates", "document-node": "exg.val.pm10"}}

SEE ALSO
scs_philips_hue/aws_mqtt_subscriber
scs_philips_hue/node
"""

import sys

from scs_core.data.json import JSONify
from scs_core.sys.logging import Logging

from scs_host.sys.host import Host

from scs_philips_hue.cmd.cmd_domain_conf import CmdDomainConf
from scs_philips_hue.config.domain_conf import DomainConfSet


# --------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':

    # ----------------------------------------------------------------------------------------------------------------
    # cmd...

    cmd = CmdDomainConf()

    if not cmd.is_valid():
        cmd.print_help(sys.stderr)
        exit(2)

    Logging.config('domain_conf', verbose=cmd.verbose)
    logger = Logging.getLogger()

    logger.info(cmd)


    # ----------------------------------------------------------------------------------------------------------------
    # resources...

    # ChromaConf...
    domains = DomainConfSet.load(Host, skeleton=True)


    # ----------------------------------------------------------------------------------------------------------------
    # run...

    if cmd.add:
        domains.add(cmd.channel, cmd.add[0], cmd.add[1])
        domains.save(Host)

    if cmd.remove:
        domains.remove(cmd.channel)
        domains.save(Host)

    if domains:
        print(JSONify.dumps(domains, indent=cmd.indent))
