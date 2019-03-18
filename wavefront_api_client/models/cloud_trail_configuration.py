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


class CloudTrailConfiguration(object):
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
        'prefix': 'str',
        'base_credentials': 'AWSBaseCredentials',
        'region': 'str',
        'filter_rule': 'str',
        'bucket_name': 'str'
    }

    attribute_map = {
        'prefix': 'prefix',
        'base_credentials': 'baseCredentials',
        'region': 'region',
        'filter_rule': 'filterRule',
        'bucket_name': 'bucketName'
    }

    def __init__(self, prefix=None, base_credentials=None, region=None, filter_rule=None, bucket_name=None):  # noqa: E501
        """CloudTrailConfiguration - a model defined in Swagger"""  # noqa: E501

        self._prefix = None
        self._base_credentials = None
        self._region = None
        self._filter_rule = None
        self._bucket_name = None
        self.discriminator = None

        if prefix is not None:
            self.prefix = prefix
        if base_credentials is not None:
            self.base_credentials = base_credentials
        self.region = region
        if filter_rule is not None:
            self.filter_rule = filter_rule
        self.bucket_name = bucket_name

    @property
    def prefix(self):
        """Gets the prefix of this CloudTrailConfiguration.  # noqa: E501

        The common prefix, if any, appended to all CloudTrail log files  # noqa: E501

        :return: The prefix of this CloudTrailConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        """Sets the prefix of this CloudTrailConfiguration.

        The common prefix, if any, appended to all CloudTrail log files  # noqa: E501

        :param prefix: The prefix of this CloudTrailConfiguration.  # noqa: E501
        :type: str
        """

        self._prefix = prefix

    @property
    def base_credentials(self):
        """Gets the base_credentials of this CloudTrailConfiguration.  # noqa: E501


        :return: The base_credentials of this CloudTrailConfiguration.  # noqa: E501
        :rtype: AWSBaseCredentials
        """
        return self._base_credentials

    @base_credentials.setter
    def base_credentials(self, base_credentials):
        """Sets the base_credentials of this CloudTrailConfiguration.


        :param base_credentials: The base_credentials of this CloudTrailConfiguration.  # noqa: E501
        :type: AWSBaseCredentials
        """

        self._base_credentials = base_credentials

    @property
    def region(self):
        """Gets the region of this CloudTrailConfiguration.  # noqa: E501

        The AWS region of the S3 bucket where CloudTrail logs are stored  # noqa: E501

        :return: The region of this CloudTrailConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this CloudTrailConfiguration.

        The AWS region of the S3 bucket where CloudTrail logs are stored  # noqa: E501

        :param region: The region of this CloudTrailConfiguration.  # noqa: E501
        :type: str
        """
        if region is None:
            raise ValueError("Invalid value for `region`, must not be `None`")  # noqa: E501

        self._region = region

    @property
    def filter_rule(self):
        """Gets the filter_rule of this CloudTrailConfiguration.  # noqa: E501

        Rule to filter cloud trail log event.  # noqa: E501

        :return: The filter_rule of this CloudTrailConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._filter_rule

    @filter_rule.setter
    def filter_rule(self, filter_rule):
        """Sets the filter_rule of this CloudTrailConfiguration.

        Rule to filter cloud trail log event.  # noqa: E501

        :param filter_rule: The filter_rule of this CloudTrailConfiguration.  # noqa: E501
        :type: str
        """

        self._filter_rule = filter_rule

    @property
    def bucket_name(self):
        """Gets the bucket_name of this CloudTrailConfiguration.  # noqa: E501

        Name of the S3 bucket where CloudTrail logs are stored  # noqa: E501

        :return: The bucket_name of this CloudTrailConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        """Sets the bucket_name of this CloudTrailConfiguration.

        Name of the S3 bucket where CloudTrail logs are stored  # noqa: E501

        :param bucket_name: The bucket_name of this CloudTrailConfiguration.  # noqa: E501
        :type: str
        """
        if bucket_name is None:
            raise ValueError("Invalid value for `bucket_name`, must not be `None`")  # noqa: E501

        self._bucket_name = bucket_name

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
        if issubclass(CloudTrailConfiguration, dict):
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
        if not isinstance(other, CloudTrailConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
