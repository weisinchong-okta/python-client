# coding: utf-8

"""
    Wavefront REST API

    <p>The Wavefront REST API enables you to interact with Wavefront servers using standard REST API tools. You can use the REST API to automate commonly executed operations such as automatically tagging sources.</p><p>When you make REST API calls outside the Wavefront REST API documentation you must add the header \"Authorization: Bearer &lt;&lt;API-TOKEN&gt;&gt;\" to your HTTP requests.</p>  # noqa: E501

    OpenAPI spec version: v2
    Contact: support@wavefront.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class SearchQuery(object):
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
        'key': 'str',
        'value': 'str',
        'matching_method': 'str'
    }

    attribute_map = {
        'key': 'key',
        'value': 'value',
        'matching_method': 'matchingMethod'
    }

    def __init__(self, key=None, value=None, matching_method=None):  # noqa: E501
        """SearchQuery - a model defined in Swagger"""  # noqa: E501

        self._key = None
        self._value = None
        self._matching_method = None
        self.discriminator = None

        self.key = key
        self.value = value
        if matching_method is not None:
            self.matching_method = matching_method

    @property
    def key(self):
        """Gets the key of this SearchQuery.  # noqa: E501

        The entity facet (key) by which to search.  Valid keys are any property keys returned by the JSON representation of the entity.  Examples are 'creatorId', 'name', etc.  The following special key keywords are also valid:  'tags' performs a search on entity tags, 'tagpath' performs a hierarchical search on tags, with  periods (.) as path level separators.  'freetext' performs a free text search across many fields of the entity  # noqa: E501

        :return: The key of this SearchQuery.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this SearchQuery.

        The entity facet (key) by which to search.  Valid keys are any property keys returned by the JSON representation of the entity.  Examples are 'creatorId', 'name', etc.  The following special key keywords are also valid:  'tags' performs a search on entity tags, 'tagpath' performs a hierarchical search on tags, with  periods (.) as path level separators.  'freetext' performs a free text search across many fields of the entity  # noqa: E501

        :param key: The key of this SearchQuery.  # noqa: E501
        :type: str
        """
        if key is None:
            raise ValueError("Invalid value for `key`, must not be `None`")  # noqa: E501

        self._key = key

    @property
    def value(self):
        """Gets the value of this SearchQuery.  # noqa: E501

        The entity facet value for which to search  # noqa: E501

        :return: The value of this SearchQuery.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this SearchQuery.

        The entity facet value for which to search  # noqa: E501

        :param value: The value of this SearchQuery.  # noqa: E501
        :type: str
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    @property
    def matching_method(self):
        """Gets the matching_method of this SearchQuery.  # noqa: E501

        The method by which search matching is performed.  Default: CONTAINS  # noqa: E501

        :return: The matching_method of this SearchQuery.  # noqa: E501
        :rtype: str
        """
        return self._matching_method

    @matching_method.setter
    def matching_method(self, matching_method):
        """Sets the matching_method of this SearchQuery.

        The method by which search matching is performed.  Default: CONTAINS  # noqa: E501

        :param matching_method: The matching_method of this SearchQuery.  # noqa: E501
        :type: str
        """
        allowed_values = ["CONTAINS", "STARTSWITH", "EXACT", "TAGPATH"]  # noqa: E501
        if matching_method not in allowed_values:
            raise ValueError(
                "Invalid value for `matching_method` ({0}), must be one of {1}"  # noqa: E501
                .format(matching_method, allowed_values)
            )

        self._matching_method = matching_method

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
        if issubclass(SearchQuery, dict):
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
        if not isinstance(other, SearchQuery):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
