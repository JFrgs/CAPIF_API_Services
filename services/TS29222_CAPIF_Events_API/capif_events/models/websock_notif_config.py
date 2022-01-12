# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from capif_events.models.base_model_ import Model
from capif_events import util


class WebsockNotifConfig(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, websocket_uri=None, request_websocket_uri=None):  # noqa: E501
        """WebsockNotifConfig - a model defined in OpenAPI

        :param websocket_uri: The websocket_uri of this WebsockNotifConfig.  # noqa: E501
        :type websocket_uri: str
        :param request_websocket_uri: The request_websocket_uri of this WebsockNotifConfig.  # noqa: E501
        :type request_websocket_uri: bool
        """
        self.openapi_types = {
            'websocket_uri': str,
            'request_websocket_uri': bool
        }

        self.attribute_map = {
            'websocket_uri': 'websocketUri',
            'request_websocket_uri': 'requestWebsocketUri'
        }

        self._websocket_uri = websocket_uri
        self._request_websocket_uri = request_websocket_uri

    @classmethod
    def from_dict(cls, dikt) -> 'WebsockNotifConfig':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The WebsockNotifConfig of this WebsockNotifConfig.  # noqa: E501
        :rtype: WebsockNotifConfig
        """
        return util.deserialize_model(dikt, cls)

    @property
    def websocket_uri(self):
        """Gets the websocket_uri of this WebsockNotifConfig.

        string formatted according to IETF RFC 3986 identifying a referenced resource.  # noqa: E501

        :return: The websocket_uri of this WebsockNotifConfig.
        :rtype: str
        """
        return self._websocket_uri

    @websocket_uri.setter
    def websocket_uri(self, websocket_uri):
        """Sets the websocket_uri of this WebsockNotifConfig.

        string formatted according to IETF RFC 3986 identifying a referenced resource.  # noqa: E501

        :param websocket_uri: The websocket_uri of this WebsockNotifConfig.
        :type websocket_uri: str
        """

        self._websocket_uri = websocket_uri

    @property
    def request_websocket_uri(self):
        """Gets the request_websocket_uri of this WebsockNotifConfig.

        Set by the SCS/AS to indicate that the Websocket delivery is requested.  # noqa: E501

        :return: The request_websocket_uri of this WebsockNotifConfig.
        :rtype: bool
        """
        return self._request_websocket_uri

    @request_websocket_uri.setter
    def request_websocket_uri(self, request_websocket_uri):
        """Sets the request_websocket_uri of this WebsockNotifConfig.

        Set by the SCS/AS to indicate that the Websocket delivery is requested.  # noqa: E501

        :param request_websocket_uri: The request_websocket_uri of this WebsockNotifConfig.
        :type request_websocket_uri: bool
        """

        self._request_websocket_uri = request_websocket_uri