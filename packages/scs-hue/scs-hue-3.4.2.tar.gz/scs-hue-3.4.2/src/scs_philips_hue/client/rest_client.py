"""
Created on 27 Oct 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

header:
CURLOPT_HTTPHEADER => array('Accept: application/json'),
"""

import json

from http.client import IncompleteRead

from scs_core.data.json import JSONify

from scs_core.client.http_client import HTTPClient
from scs_core.client.http_exception import HTTPException
from scs_core.client.http_status import HTTPStatus

from scs_philips_hue.client.client_exception import ClientException


# --------------------------------------------------------------------------------------------------------------------

class RESTClient(object):
    """
    classdocs
    """

    __HEADER_ACCEPT = "application/json"

    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self):
        """
        Constructor
        """
        self.__http_client = HTTPClient()
        self.__username = None


    # ----------------------------------------------------------------------------------------------------------------

    def connect(self, host, username, timeout=None):
        self.__http_client.connect(host, secure=False, timeout=timeout)
        self.__username = username


    def close(self):
        self.__http_client.close()


    # ----------------------------------------------------------------------------------------------------------------

    def get(self, path, params=None):
        # print("RESTClient.get: path: %s" % self.__http_path(path))

        try:
            response_jstr = self.__http_client.get(self.__http_path(path), params, self.__headers)

        except (ConnectionRefusedError, IncompleteRead):
            return None

        except HTTPException as exc:
            if exc.status == HTTPStatus.NOT_FOUND:
                return None
            else:
                raise ClientException.construct(exc) from exc

        try:
            response = json.loads(response_jstr)
        except ValueError:
            response = None

        return response


    def post(self, path, payload_jdict):
        payload_jstr = JSONify.dumps(payload_jdict)

        try:
            response_jstr = self.__http_client.post(self.__http_path(path), payload_jstr, self.__headers)

        except (ConnectionRefusedError, IncompleteRead):
            return None

        except HTTPException as ex:
            raise ClientException.construct(ex) from ex

        try:
            response = json.loads(response_jstr)
        except ValueError:
            response = None

        return response


    def put(self, path, payload_jdict):                # TODO: make the jdict here?
        payload_jstr = JSONify.dumps(payload_jdict)

        # print("RESTClient.put: path: %s payload: %s" % (path, payload_jstr))

        try:
            response_jstr = self.__http_client.put(self.__http_path(path), payload_jstr, self.__headers)

        except (ConnectionRefusedError, IncompleteRead):
            return None

        except HTTPException as ex:
            raise ClientException.construct(ex) from ex

        try:
            response = json.loads(response_jstr)
        except ValueError:
            response = None

        return response


    def delete(self, path):
        try:
            response_jstr = self.__http_client.delete(self.__http_path(path), self.__headers)

        except (ConnectionRefusedError, IncompleteRead):
            return None

        except HTTPException as ex:
            raise ClientException.construct(ex) from ex

        try:
            response = json.loads(response_jstr)
        except ValueError:
            response = None

        return response


    # ----------------------------------------------------------------------------------------------------------------

    def __http_path(self, path):
        if self.__username is None:
            return '/api' + path

        return '/api/' + self.__username + path


    @property
    def __headers(self):
        return {"Accept": self.__HEADER_ACCEPT}


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return "RESTClient:{username:%s}" % self.__username
