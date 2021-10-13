# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from api_invocation_logs.models.base_model_ import Model
from api_invocation_logs import util


class SecurityMethodAnyOf(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    PSK = "PSK"
    PKI = "PKI"
    OAUTH = "OAUTH"
    def __init__(self):  # noqa: E501
        """SecurityMethodAnyOf - a model defined in OpenAPI

        """
        self.openapi_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt) -> 'SecurityMethodAnyOf':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SecurityMethod_anyOf of this SecurityMethodAnyOf.  # noqa: E501
        :rtype: SecurityMethodAnyOf
        """
        return util.deserialize_model(dikt, cls)
