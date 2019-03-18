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

from wavefront_api_client.models.dashboard_section_row import DashboardSectionRow  # noqa: F401,E501


class DashboardSection(object):
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
        'rows': 'list[DashboardSectionRow]',
        'name': 'str'
    }

    attribute_map = {
        'rows': 'rows',
        'name': 'name'
    }

    def __init__(self, rows=None, name=None):  # noqa: E501
        """DashboardSection - a model defined in Swagger"""  # noqa: E501

        self._rows = None
        self._name = None
        self.discriminator = None

        self.rows = rows
        self.name = name

    @property
    def rows(self):
        """Gets the rows of this DashboardSection.  # noqa: E501

        Rows of this section  # noqa: E501

        :return: The rows of this DashboardSection.  # noqa: E501
        :rtype: list[DashboardSectionRow]
        """
        return self._rows

    @rows.setter
    def rows(self, rows):
        """Sets the rows of this DashboardSection.

        Rows of this section  # noqa: E501

        :param rows: The rows of this DashboardSection.  # noqa: E501
        :type: list[DashboardSectionRow]
        """
        if rows is None:
            raise ValueError("Invalid value for `rows`, must not be `None`")  # noqa: E501

        self._rows = rows

    @property
    def name(self):
        """Gets the name of this DashboardSection.  # noqa: E501

        Name of this section  # noqa: E501

        :return: The name of this DashboardSection.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DashboardSection.

        Name of this section  # noqa: E501

        :param name: The name of this DashboardSection.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

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
        if issubclass(DashboardSection, dict):
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
        if not isinstance(other, DashboardSection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
