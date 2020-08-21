# coding: utf-8

"""
    Wavefront REST API

    <p>The Wavefront REST API enables you to interact with Wavefront servers using standard REST API tools. You can use the REST API to automate commonly executed operations such as automatically tagging sources.</p><p>When you make REST API calls outside the Wavefront REST API documentation you must add the header \"Authorization: Bearer &lt;&lt;API-TOKEN&gt;&gt;\" to your HTTP requests.</p>  # noqa: E501

    OpenAPI spec version: v2
    Contact: chitimba@wavefront.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class RelatedEventTimeRange(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'earliest_start_time_epoch_millis': 'int',
        'latest_start_time_epoch_millis': 'int'
    }

    attribute_map = {
        'earliest_start_time_epoch_millis': 'earliestStartTimeEpochMillis',
        'latest_start_time_epoch_millis': 'latestStartTimeEpochMillis'
    }

    def __init__(self, earliest_start_time_epoch_millis=None, latest_start_time_epoch_millis=None):  # noqa: E501
        """RelatedEventTimeRange - a model defined in Swagger"""  # noqa: E501

        self._earliest_start_time_epoch_millis = None
        self._latest_start_time_epoch_millis = None
        self.discriminator = None

        if earliest_start_time_epoch_millis is not None:
            self.earliest_start_time_epoch_millis = earliest_start_time_epoch_millis
        if latest_start_time_epoch_millis is not None:
            self.latest_start_time_epoch_millis = latest_start_time_epoch_millis

    @property
    def earliest_start_time_epoch_millis(self):
        """Gets the earliest_start_time_epoch_millis of this RelatedEventTimeRange.  # noqa: E501

        Start of search time window, in milliseconds since the Unix Epoch. Events whose start time occurs after this value will be returned.  If no value is supplied, will return null  # noqa: E501

        :return: The earliest_start_time_epoch_millis of this RelatedEventTimeRange.  # noqa: E501
        :rtype: int
        """
        return self._earliest_start_time_epoch_millis

    @earliest_start_time_epoch_millis.setter
    def earliest_start_time_epoch_millis(self, earliest_start_time_epoch_millis):
        """Sets the earliest_start_time_epoch_millis of this RelatedEventTimeRange.

        Start of search time window, in milliseconds since the Unix Epoch. Events whose start time occurs after this value will be returned.  If no value is supplied, will return null  # noqa: E501

        :param earliest_start_time_epoch_millis: The earliest_start_time_epoch_millis of this RelatedEventTimeRange.  # noqa: E501
        :type: int
        """

        self._earliest_start_time_epoch_millis = earliest_start_time_epoch_millis

    @property
    def latest_start_time_epoch_millis(self):
        """Gets the latest_start_time_epoch_millis of this RelatedEventTimeRange.  # noqa: E501

        End of the search time window, in milliseconds since the Unix Epoch. Events whose start time occurs before this value will be returned.  If no value is supplied, will return null  # noqa: E501

        :return: The latest_start_time_epoch_millis of this RelatedEventTimeRange.  # noqa: E501
        :rtype: int
        """
        return self._latest_start_time_epoch_millis

    @latest_start_time_epoch_millis.setter
    def latest_start_time_epoch_millis(self, latest_start_time_epoch_millis):
        """Sets the latest_start_time_epoch_millis of this RelatedEventTimeRange.

        End of the search time window, in milliseconds since the Unix Epoch. Events whose start time occurs before this value will be returned.  If no value is supplied, will return null  # noqa: E501

        :param latest_start_time_epoch_millis: The latest_start_time_epoch_millis of this RelatedEventTimeRange.  # noqa: E501
        :type: int
        """

        self._latest_start_time_epoch_millis = latest_start_time_epoch_millis

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(RelatedEventTimeRange, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RelatedEventTimeRange):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
