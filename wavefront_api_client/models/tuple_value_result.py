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


class TupleValueResult(object):
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
        'count': 'int',
        'value': 'Tuple'
    }

    attribute_map = {
        'count': 'count',
        'value': 'value'
    }

    def __init__(self, count=None, value=None):  # noqa: E501
        """TupleValueResult - a model defined in Swagger"""  # noqa: E501

        self._count = None
        self._value = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if value is not None:
            self.value = value

    @property
    def count(self):
        """Gets the count of this TupleValueResult.  # noqa: E501

        The count of the values appearing in the query keys.  # noqa: E501

        :return: The count of this TupleValueResult.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this TupleValueResult.

        The count of the values appearing in the query keys.  # noqa: E501

        :param count: The count of this TupleValueResult.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def value(self):
        """Gets the value of this TupleValueResult.  # noqa: E501

        The possible values for a given key tuple.  # noqa: E501

        :return: The value of this TupleValueResult.  # noqa: E501
        :rtype: Tuple
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this TupleValueResult.

        The possible values for a given key tuple.  # noqa: E501

        :param value: The value of this TupleValueResult.  # noqa: E501
        :type: Tuple
        """

        self._value = value

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
        if issubclass(TupleValueResult, dict):
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
        if not isinstance(other, TupleValueResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other