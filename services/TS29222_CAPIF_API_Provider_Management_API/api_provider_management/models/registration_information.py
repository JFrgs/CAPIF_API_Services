# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from api_provider_management.models.base_model_ import Model
from api_provider_management import util


class RegistrationInformation(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, api_prov_pub_key=None, api_prov_cert=None):  # noqa: E501
        """RegistrationInformation - a model defined in OpenAPI

        :param api_prov_pub_key: The api_prov_pub_key of this RegistrationInformation.  # noqa: E501
        :type api_prov_pub_key: str
        :param api_prov_cert: The api_prov_cert of this RegistrationInformation.  # noqa: E501
        :type api_prov_cert: str
        """
        self.openapi_types = {
            'api_prov_pub_key': str,
            'api_prov_cert': str
        }

        self.attribute_map = {
            'api_prov_pub_key': 'apiProvPubKey',
            'api_prov_cert': 'apiProvCert'
        }

        self._api_prov_pub_key = api_prov_pub_key
        self._api_prov_cert = api_prov_cert

    @classmethod
    def from_dict(cls, dikt) -> 'RegistrationInformation':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The RegistrationInformation of this RegistrationInformation.  # noqa: E501
        :rtype: RegistrationInformation
        """
        return util.deserialize_model(dikt, cls)

    @property
    def api_prov_pub_key(self):
        """Gets the api_prov_pub_key of this RegistrationInformation.

        Public Key of API Provider domain function.  # noqa: E501

        :return: The api_prov_pub_key of this RegistrationInformation.
        :rtype: str
        """
        return self._api_prov_pub_key

    @api_prov_pub_key.setter
    def api_prov_pub_key(self, api_prov_pub_key):
        """Sets the api_prov_pub_key of this RegistrationInformation.

        Public Key of API Provider domain function.  # noqa: E501

        :param api_prov_pub_key: The api_prov_pub_key of this RegistrationInformation.
        :type api_prov_pub_key: str
        """
        if api_prov_pub_key is None:
            raise ValueError("Invalid value for `api_prov_pub_key`, must not be `None`")  # noqa: E501

        self._api_prov_pub_key = api_prov_pub_key

    @property
    def api_prov_cert(self):
        """Gets the api_prov_cert of this RegistrationInformation.

        API provider domain function's client certificate  # noqa: E501

        :return: The api_prov_cert of this RegistrationInformation.
        :rtype: str
        """
        return self._api_prov_cert

    @api_prov_cert.setter
    def api_prov_cert(self, api_prov_cert):
        """Sets the api_prov_cert of this RegistrationInformation.

        API provider domain function's client certificate  # noqa: E501

        :param api_prov_cert: The api_prov_cert of this RegistrationInformation.
        :type api_prov_cert: str
        """

        self._api_prov_cert = api_prov_cert