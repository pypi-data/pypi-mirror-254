"""
Created on 28 Oct 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

example:
{
    "name": "scs-hb-001",
    "zigbeechannel": 20,
    "bridgeid": "001788FFFE795620",
    "mac": "00:17:88:79:56:20",
    "dhcp": true,
    "ipaddress": "192.168.1.10",
    "netmask": "255.255.255.0",
    "gateway": "192.168.1.1",
    "proxyaddress": "none",
    "proxyport": 0,
    "UTC": "2017-10-28T14:16:10",
    "localtime": "2017-10-28T15:16:10",
    "timezone": "Europe/London",
    "modelid": "BSB002",
    "datastoreversion": "63",
    "swversion": "1709131301",
    "apiversion": "1.21.0",
    "swupdate": {
        "updatestate": 0,
        "checkforupdate": false,
        "devicetypes": {
            "bridge": false,
            "lights": [],
            "sensors": []
        },
        "url": "",
        "text": "",
        "notify": false
    },
    "swupdate2": {
        "checkforupdate": false,
        "lastchange": "2017-10-27T15:10:38",
        "bridge": {
            "state": "noupdates",
            "lastinstall": null
        },
        "state": "noupdates",
        "autoinstall": {
            "updatetime": "T14:00:00",
            "on": false
        }
    },
    "linkbutton": false,
    "portalservices": true,
    "portalconnection": "connected",
    "portalstate": {
        "signedon": true,
        "incoming": false,
        "outgoing": true,
        "communication": "disconnected"
    },
    "internetservices": {
        "internet": "connected",
        "remoteaccess": "connected",
        "time": "connected",
        "swupdate": "connected"
    },
    "factorynew": false,
    "replacesbridgeid": null,
    "backup": {
        "status": "idle",
        "errorcode": 0
    },
    "starterkitid": "",
    "whitelist": {
        "kakoh96DKsic6XGC9-v07nVIUig1naMOgv849i1r": {
            "last use date": "2017-10-27T20:02:32",
            "create date": "2017-10-27T15:04:55",
            "name": "scs_hue#bruno"
        },
        "11uK-QDNOytTk7UW6smCBYBVZXxKaFy3b72b7Qdv": {
            "last use date": "2017-10-27T15:17:32",
            "create date": "2017-10-27T15:10:10",
            "name": "Hue 2#HTC U11"
        }
    }
}
"""

from collections import OrderedDict

# from scs_core.data.json import JSONify

from scs_core.data.datum import Datum
from scs_core.data.json import JSONable

from scs_philips_hue.data.bridge.backup import Backup
from scs_philips_hue.data.bridge.internet_services import InternetServices
from scs_philips_hue.data.bridge.portal_state import PortalState
from scs_philips_hue.data.bridge.sw_update import SWUpdate
from scs_philips_hue.data.bridge.sw_update_2 import SWUpdate2
from scs_philips_hue.data.bridge.whitelist import WhitelistGroup


# --------------------------------------------------------------------------------------------------------------------

class BridgeConfig(JSONable):
    """
    classdocs
    """

    NAME_MIN_LENGTH =        4
    NAME_MAX_LENGTH =       16

    ZIGBEE_CHANNELS =       ("11", "15", "20", "25")


    # ----------------------------------------------------------------------------------------------------------------

    @classmethod
    def construct_from_jdict(cls, jdict):
        if not jdict:
            return None

        name = jdict.get('name')
        zigbee_channel = jdict.get('zigbeechannel')

        dhcp = jdict.get('dhcp')
        ip_address = jdict.get('ipaddress')
        netmask = jdict.get('netmask')
        gateway = jdict.get('gateway')

        proxy_address = jdict.get('proxyaddress')
        proxy_port = jdict.get('proxyport')

        utc = jdict.get('UTC')
        timezone = jdict.get('timezone')

        sw_update = SWUpdate.construct_from_jdict(jdict.get('swupdate'))

        link_button = jdict.get('linkbutton')
        portal_services = jdict.get('portalservices')

        return BridgeConfig(name=name, zigbee_channel=zigbee_channel,
                            dhcp=dhcp, ip_address=ip_address, netmask=netmask, gateway=gateway,
                            proxy_address=proxy_address, proxy_port=proxy_port,
                            utc=utc, timezone=timezone, sw_update=sw_update,
                            link_button=link_button, portal_services=portal_services)


    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, name=None, zigbee_channel=None,
                 dhcp=None, ip_address=None, netmask=None, gateway=None,
                 proxy_address=None, proxy_port=None,
                 utc=None, timezone=None, sw_update=None,
                 link_button=None, portal_services=None):
        """
        Constructor
        """
        self.__name = name                                                  # string
        self.__zigbee_channel = Datum.int(zigbee_channel)                   # int

        self.__dhcp = Datum.bool(dhcp)                                      # bool
        self.__ip_address = ip_address                                      # string
        self.__netmask = netmask                                            # string
        self.__gateway = gateway                                            # string

        self.__proxy_address = proxy_address                                # string
        self.__proxy_port = Datum.int(proxy_port)                           # int

        self.__utc = utc                                                    # string (date / time)
        self.__timezone = timezone                                          # string (timezone ID)

        self.__sw_update = sw_update                                        # SWUpdate

        self.__link_button = Datum.bool(link_button)                        # bool
        self.__portal_services = Datum.bool(portal_services)                # bool


    # ----------------------------------------------------------------------------------------------------------------

    def as_json(self):
        jdict = OrderedDict()

        if self.name is not None:
            jdict['name'] = self.name

        if self.zigbee_channel is not None:
            jdict['zigbeechannel'] = self.zigbee_channel


        if self.dhcp is not None:
            jdict['dhcp'] = self.dhcp

        if self.ip_address is not None:
            jdict['ipaddress'] = self.ip_address

        if self.netmask is not None:
            jdict['netmask'] = self.netmask

        if self.gateway is not None:
            jdict['gateway'] = self.gateway


        if self.proxy_address is not None:
            jdict['proxyaddress'] = self.proxy_address

        if self.proxy_port is not None:
            jdict['proxyport'] = self.proxy_port


        if self.utc is not None:
            jdict['UTC'] = self.utc

        if self.timezone is not None:
            jdict['timezone'] = self.timezone


        if self.sw_update is not None:
            jdict['swupdate'] = self.sw_update


        if self.link_button is not None:
            jdict['linkbutton'] = self.link_button

        if self.portal_services is not None:
            jdict['portalservices'] = self.portal_services

        return jdict


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def name(self):
        return self.__name


    @property
    def zigbee_channel(self):
        return self.__zigbee_channel


    @property
    def dhcp(self):
        return self.__dhcp


    @property
    def ip_address(self):
        return self.__ip_address


    @property
    def netmask(self):
        return self.__netmask


    @property
    def gateway(self):
        return self.__gateway


    @property
    def proxy_address(self):
        return self.__proxy_address


    @property
    def proxy_port(self):
        return self.__proxy_port


    @property
    def utc(self):
        return self.__utc


    @property
    def timezone(self):
        return self.__timezone


    @property
    def sw_update(self):
        return self.__sw_update


    @property
    def link_button(self):
        return self.__link_button


    @property
    def portal_services(self):
        return self.__portal_services


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return "BridgeConfig:{name:%s, zigbee_channel:%s, " \
               "dhcp:%s, ip_address:%s, netmask:%s, " \
               "gateway:%s, proxy_address:%s, proxy_port:%s," \
               "utc:%s, timezone:%s, sw_update:%s," \
               "link_button:%s, portal_services:%s}" %  \
               (self.name, self.zigbee_channel,
                self.dhcp, self.ip_address, self.netmask,
                self.gateway, self.proxy_address, self.proxy_port,
                self.utc, self.timezone, self.sw_update,
                self.link_button, self.portal_services)


# --------------------------------------------------------------------------------------------------------------------

class ReportedBridgeConfig(BridgeConfig):
    """
    classdocs
    """

    # ----------------------------------------------------------------------------------------------------------------

    @classmethod
    def construct_from_jdict(cls, jdict):
        # print(JSONify.dumps(jdict))

        if not jdict:
            return None

        name = jdict.get('name')
        zigbee_channel = jdict.get('zigbeechannel')
        bridge_id = jdict.get('bridgeid')
        mac = jdict.get('mac')

        dhcp = jdict.get('dhcp')
        ip_address = jdict.get('ipaddress')
        netmask = jdict.get('netmask')
        gateway = jdict.get('gateway')

        proxy_address = jdict.get('proxyaddress')
        proxy_port = jdict.get('proxyport')

        utc = jdict.get('UTC')
        localtime = jdict.get('localtime')
        timezone = jdict.get('timezone')

        model_id = jdict.get('modelid')
        datastore_version = jdict.get('datastoreversion')
        sw_version = jdict.get('swversion')
        api_version = jdict.get('apiversion')

        sw_update = SWUpdate.construct_from_jdict(jdict.get('swupdate'))
        sw_update_2 = SWUpdate2.construct_from_jdict(jdict.get('swupdate2'))

        link_button = jdict.get('linkbutton')

        portal_services = jdict.get('portalservices')
        portal_connection = jdict.get('portalconnection')
        portal_state = PortalState.construct_from_jdict(jdict.get('portalstate'))

        internet_services = InternetServices.construct_from_jdict(jdict.get('internetservices'))
        factory_new = jdict.get('factorynew')
        replaces_bridge_id = jdict.get('replacesbridgeid')
        backup = Backup.construct_from_jdict(jdict.get('backup'))
        starterkit_id = jdict.get('starterkitid')

        whitelist = WhitelistGroup.construct_from_jdict(jdict.get('whitelist'))

        return ReportedBridgeConfig(name=name, zigbee_channel=zigbee_channel, bridge_id=bridge_id,
                                    mac=mac, dhcp=dhcp, ip_address=ip_address, netmask=netmask, gateway=gateway,
                                    proxy_address=proxy_address, proxy_port=proxy_port,
                                    utc=utc, localtime=localtime, timezone=timezone,
                                    model_id=model_id, datastore_version=datastore_version, sw_version=sw_version,
                                    api_version=api_version, sw_update=sw_update, sw_update_2=sw_update_2,
                                    link_button=link_button,
                                    portal_services=portal_services, portal_connection=portal_connection,
                                    portal_state=portal_state,
                                    internet_services=internet_services, factory_new=factory_new,
                                    replaces_bridge_id=replaces_bridge_id, backup=backup, starterkit_id=starterkit_id,
                                    whitelist=whitelist)


    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, name=None, zigbee_channel=None, bridge_id=None,
                 mac=None, dhcp=None, ip_address=None, netmask=None, gateway=None,
                 proxy_address=None, proxy_port=None,
                 utc=None, localtime=None, timezone=None,
                 model_id=None, datastore_version=None, sw_version=None,
                 api_version=None, sw_update=None, sw_update_2=None,
                 link_button=None,
                 portal_services=None, portal_connection=None,
                 portal_state=None,
                 internet_services=None, factory_new=None,
                 replaces_bridge_id=None, backup=None, starterkit_id=None,
                 whitelist=None):
        """
        Constructor
        """
        super().__init__(name=name, zigbee_channel=zigbee_channel,
                         dhcp=dhcp, ip_address=ip_address, netmask=netmask, gateway=gateway,
                         proxy_address=proxy_address, proxy_port=proxy_port,
                         utc=utc, timezone=timezone, sw_update=sw_update,
                         link_button=link_button)

        self.__bridge_id = bridge_id                                        # string
        self.__mac = mac                                                    # string

        self.__localtime = localtime                                        # string (date / time)

        self.__model_id = model_id                                          # string
        self.__datastore_version = datastore_version                        # string

        self.__sw_version = sw_version                                      # string
        self.__api_version = api_version                                    # string

        self.__sw_update_2 = sw_update_2                                    # SWUpdate2

        self.__portal_services = Datum.bool(portal_services)                # bool
        self.__portal_connection = portal_connection                        # string
        self.__portal_state = portal_state                                  # PortalState

        self.__internet_services = internet_services                        # InternetServices
        self.__factory_new = Datum.bool(factory_new)                        # bool
        self.__replaces_bridge_id = replaces_bridge_id                      # string
        self.__backup = backup                                              # Backup
        self.__starterkit_id = starterkit_id                                # string

        self.__whitelist = whitelist                                        # WhitelistGroup


    # ----------------------------------------------------------------------------------------------------------------

    def as_json(self):
        jdict = OrderedDict()

        jdict['name'] = self.name
        jdict['zigbeechannel'] = self.zigbee_channel
        jdict['bridgeid'] = self.bridge_id
        jdict['mac'] = self.mac

        jdict['dhcp'] = self.dhcp
        jdict['ipaddress'] = self.ip_address
        jdict['netmask'] = self.netmask
        jdict['gateway'] = self.gateway

        jdict['proxyaddress'] = self.proxy_address
        jdict['proxyport'] = self.proxy_port

        jdict['UTC'] = self.utc
        jdict['localtime'] = self.localtime
        jdict['timezone'] = self.timezone

        jdict['modelid'] = self.model_id
        jdict['datastoreversion'] = self.datastore_version
        jdict['swversion'] = self.sw_version
        jdict['apiversion'] = self.api_version

        jdict['swupdate'] = self.sw_update
        jdict['swupdate2'] = self.sw_update_2

        jdict['linkbutton'] = self.link_button

        jdict['portalservices'] = self.portal_services
        jdict['portalconnection'] = self.portal_connection
        jdict['portalstate'] = self.portal_state

        jdict['internetservices'] = self.internet_services
        jdict['factorynew'] = self.factory_new
        jdict['replacesbridgeid'] = self.replaces_bridge_id
        jdict['backup'] = self.backup

        jdict['starterkitid'] = self.starterkit_id
        jdict['whitelist'] = self.whitelist

        return jdict


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def bridge_id(self):
        return self.__bridge_id


    @property
    def mac(self):
        return self.__mac


    @property
    def localtime(self):
        return self.__localtime


    @property
    def model_id(self):
        return self.__model_id


    @property
    def datastore_version(self):
        return self.__datastore_version


    @property
    def sw_version(self):
        return self.__sw_version


    @property
    def api_version(self):
        return self.__api_version


    @property
    def sw_update_2(self):
        return self.__sw_update_2


    @property
    def portal_services(self):
        return self.__portal_services


    @property
    def portal_connection(self):
        return self.__portal_connection


    @property
    def portal_state(self):
        return self.__portal_state


    @property
    def internet_services(self):
        return self.__internet_services


    @property
    def factory_new(self):
        return self.__factory_new


    @property
    def replaces_bridge_id(self):
        return self.__replaces_bridge_id


    @property
    def backup(self):
        return self.__backup


    @property
    def starterkit_id(self):
        return self.__starterkit_id


    @property
    def whitelist(self):
        return self.__whitelist


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return "ReportedBridgeConfig:{name:%s, zigbee_channel:%s, bridge_id:%s, mac:%s, " \
               "dhcp:%s, ip_address:%s, netmask:%s, " \
               "gateway:%s, proxy_address:%s, proxy_port:%s," \
               "utc:%s, localtime:%s, timezone:%s, " \
               "model_id:%s, datastore_version:%s, sw_version:%s, api_version:%s, " \
               "sw_update:%s, sw_update_2:%s, link_button:%s," \
               "portal_services:%s, portal_connection:%s, portal_state:%s, internet_services:%s, " \
               "factory_new:%s, replaces_bridge_id:%s, backup:%s, starterkit_id:%s, " \
               "whitelist:%s}" %  \
               (self.name, self.zigbee_channel, self.bridge_id, self.mac, self.dhcp, self.ip_address, self.netmask,
                self.gateway, self.proxy_address, self.proxy_port,
                self.utc, self.localtime, self.timezone,
                self.model_id, self.datastore_version, self.sw_version, self.api_version,
                self.sw_update, self.sw_update_2, self.link_button,
                self.portal_services, self.portal_connection, self.portal_state, self.internet_services,
                self.factory_new, self.replaces_bridge_id, self.backup, self.starterkit_id,
                self.whitelist)
