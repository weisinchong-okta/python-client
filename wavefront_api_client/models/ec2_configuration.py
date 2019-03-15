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

from wavefront_api_client.models.aws_base_credentials import AWSBaseCredentials  # noqa: F401,E501


class EC2Configuration(object):
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
        'host_name_tags': 'list[str]',
        'base_credentials': 'AWSBaseCredentials'
    }

    attribute_map = {
        'host_name_tags': 'hostNameTags',
        'base_credentials': 'baseCredentials'
    }

    def __init__(self, host_name_tags=None, base_credentials=None):  # noqa: E501
        """EC2Configuration - a model defined in Swagger"""  # noqa: E501

        self._host_name_tags = None
        self._base_credentials = None
        self.discriminator = None

        if host_name_tags is not None:
            self.host_name_tags = host_name_tags
        if base_credentials is not None:
            self.base_credentials = base_credentials

    @property
    def host_name_tags(self):
        """Gets the host_name_tags of this EC2Configuration.  # noqa: E501

        A list of AWS instance tags that, when found, will be used as the \"source\" name in a series.  Default: [\"hostname\", \"host\", \"name\"].  If no tag in this list is found, the series source is set to the instance id.  # noqa: E501

        :return: The host_name_tags of this EC2Configuration.  # noqa: E501
        :rtype: list[str]
        """
        return self._host_name_tags

    @host_name_tags.setter
    def host_name_tags(self, host_name_tags):
        """Sets the host_name_tags of this EC2Configuration.

        A list of AWS instance tags that, when found, will be used as the \"source\" name in a series.  Default: [\"hostname\", \"host\", \"name\"].  If no tag in this list is found, the series source is set to the instance id.  # noqa: E501

        :param host_name_tags: The host_name_tags of this EC2Configuration.  # noqa: E501
        :type: list[str]
        """

        self._host_name_tags = host_name_tags

    @property
    def base_credentials(self):
        """Gets the base_credentials of this EC2Configuration.  # noqa: E501


        :return: The base_credentials of this EC2Configuration.  # noqa: E501
        :rtype: AWSBaseCredentials
        """
        return self._base_credentials

    @base_credentials.setter
    def base_credentials(self, base_credentials):
        """Sets the base_credentials of this EC2Configuration.


        :param base_credentials: The base_credentials of this EC2Configuration.  # noqa: E501
        :type: AWSBaseCredentials
        """

        self._base_credentials = base_credentials

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
        if issubclass(EC2Configuration, dict):
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
        if not isinstance(other, EC2Configuration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
