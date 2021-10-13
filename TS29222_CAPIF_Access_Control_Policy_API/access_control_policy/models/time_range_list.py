# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from access_control_policy.models.base_model_ import Model
from access_control_policy import util


class TimeRangeList(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, start_time=None, stop_time=None):  # noqa: E501
        """TimeRangeList - a model defined in OpenAPI

        :param start_time: The start_time of this TimeRangeList.  # noqa: E501
        :type start_time: datetime
        :param stop_time: The stop_time of this TimeRangeList.  # noqa: E501
        :type stop_time: datetime
        """
        self.openapi_types = {
            'start_time': datetime,
            'stop_time': datetime
        }

        self.attribute_map = {
            'start_time': 'startTime',
            'stop_time': 'stopTime'
        }

        self._start_time = start_time
        self._stop_time = stop_time

    @classmethod
    def from_dict(cls, dikt) -> 'TimeRangeList':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The TimeRangeList of this TimeRangeList.  # noqa: E501
        :rtype: TimeRangeList
        """
        return util.deserialize_model(dikt, cls)

    @property
    def start_time(self):
        """Gets the start_time of this TimeRangeList.

        string with format \"date-time\" as defined in OpenAPI.  # noqa: E501

        :return: The start_time of this TimeRangeList.
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this TimeRangeList.

        string with format \"date-time\" as defined in OpenAPI.  # noqa: E501

        :param start_time: The start_time of this TimeRangeList.
        :type start_time: datetime
        """

        self._start_time = start_time

    @property
    def stop_time(self):
        """Gets the stop_time of this TimeRangeList.

        string with format \"date-time\" as defined in OpenAPI.  # noqa: E501

        :return: The stop_time of this TimeRangeList.
        :rtype: datetime
        """
        return self._stop_time

    @stop_time.setter
    def stop_time(self, stop_time):
        """Sets the stop_time of this TimeRangeList.

        string with format \"date-time\" as defined in OpenAPI.  # noqa: E501

        :param stop_time: The stop_time of this TimeRangeList.
        :type stop_time: datetime
        """

        self._stop_time = stop_time
