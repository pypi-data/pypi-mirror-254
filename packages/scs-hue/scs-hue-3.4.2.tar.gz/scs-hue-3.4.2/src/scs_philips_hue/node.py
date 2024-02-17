#!/usr/bin/env python3

"""
Created on 11 Apr 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

source repo: scs_philips_hue

DESCRIPTION
The node utility is used to extract a node within a JSON document. Data is presented as a sequence of documents on
stdin, the node is passed to stdout. The extracted node may be a leaf node or an internal node.

The node path can be specified either on the command line, or by referencing the domain_conf.json document.
The node utility may be set to either ignore documents that do not contain the specified node, or to terminate if the
node is not present.

SYNOPSIS
node.py {-c | -t TOPIC_PATH } [-i] [-v]

EXAMPLES
./aws_mqtt_subscriber.py -vc | ./node.py -vc | ./chroma.py -v | ./desk.py -ve

FILES
~/SCS/hue/domain_conf.json

SEE ALSO
scs_philips_hue/aws_mqtt_subscriber
scs_philips_hue/domain_conf
"""

import sys

from scs_core.data.json import JSONify
from scs_core.data.path_dict import PathDict

from scs_core.sys.logging import Logging
from scs_core.sys.signalled_exit import SignalledExit

from scs_host.sys.host import Host

from scs_philips_hue.cmd.cmd_node import CmdNode
from scs_philips_hue.config.domain_conf import DomainConf, DomainConfSet


# --------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':

    # ----------------------------------------------------------------------------------------------------------------
    # cmd...

    cmd = CmdNode()

    if not cmd.is_valid():
        cmd.print_help(sys.stderr)
        exit(2)

    Logging.config('node', verbose=cmd.verbose)
    logger = Logging.getLogger()

    logger.info(cmd)

    try:
        # ------------------------------------------------------------------------------------------------------------
        # resources...

        # DomainConf...
        if cmd.use_domain_conf:
            domains = DomainConfSet.load(Host)

            if domains is None:
                logger.error("DomainConfSet not available.")
                exit(1)

        else:
            domains = DomainConfSet({cmd.topic_path[0]: DomainConf(cmd.topic_path[1], cmd.topic_path[2])})
            logger.info(domains)


        # ------------------------------------------------------------------------------------------------------------
        # run...

        # signal handler...
        SignalledExit.construct()

        node = None

        for line in sys.stdin:
            datum = PathDict.construct_from_jstr(line)

            if datum is None:
                continue

            for name, domain in domains.confs.items():
                if datum.has_sub_path(domain.topic_path):
                    print(JSONify.dumps({name: datum.node(domain.node_path)}))
                    sys.stdout.flush()


    # ----------------------------------------------------------------------------------------------------------------
    # end...

    except (KeyboardInterrupt, SystemExit):
        pass

    finally:
        logger.info("finishing")
