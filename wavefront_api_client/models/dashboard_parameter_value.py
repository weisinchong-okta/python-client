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


class DashboardParameterValue(object):
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
        'label': 'str',
        'description': 'str',
        'default_value': 'str',
        'parameter_type': 'str',
        'values_to_readable_strings': 'dict(str, str)',
        'dynamic_field_type': 'str',
        'query_value': 'str',
        'hide_from_view': 'bool',
        'tag_key': 'str',
        'multivalue': 'bool',
        'reverse_dyn_sort': 'bool',
        'allow_all': 'bool'
    }

    attribute_map = {
        'label': 'label',
        'description': 'description',
        'default_value': 'defaultValue',
        'parameter_type': 'parameterType',
        'values_to_readable_strings': 'valuesToReadableStrings',
        'dynamic_field_type': 'dynamicFieldType',
        'query_value': 'queryValue',
        'hide_from_view': 'hideFromView',
        'tag_key': 'tagKey',
        'multivalue': 'multivalue',
        'reverse_dyn_sort': 'reverseDynSort',
        'allow_all': 'allowAll'
    }

    def __init__(self, label=None, description=None, default_value=None, parameter_type=None, values_to_readable_strings=None, dynamic_field_type=None, query_value=None, hide_from_view=None, tag_key=None, multivalue=None, reverse_dyn_sort=None, allow_all=None):  # noqa: E501
        """DashboardParameterValue - a model defined in Swagger"""  # noqa: E501

        self._label = None
        self._description = None
        self._default_value = None
        self._parameter_type = None
        self._values_to_readable_strings = None
        self._dynamic_field_type = None
        self._query_value = None
        self._hide_from_view = None
        self._tag_key = None
        self._multivalue = None
        self._reverse_dyn_sort = None
        self._allow_all = None
        self.discriminator = None

        if label is not None:
            self.label = label
        if description is not None:
            self.description = description
        if default_value is not None:
            self.default_value = default_value
        if parameter_type is not None:
            self.parameter_type = parameter_type
        if values_to_readable_strings is not None:
            self.values_to_readable_strings = values_to_readable_strings
        if dynamic_field_type is not None:
            self.dynamic_field_type = dynamic_field_type
        if query_value is not None:
            self.query_value = query_value
        if hide_from_view is not None:
            self.hide_from_view = hide_from_view
        if tag_key is not None:
            self.tag_key = tag_key
        if multivalue is not None:
            self.multivalue = multivalue
        if reverse_dyn_sort is not None:
            self.reverse_dyn_sort = reverse_dyn_sort
        if allow_all is not None:
            self.allow_all = allow_all

    @property
    def label(self):
        """Gets the label of this DashboardParameterValue.  # noqa: E501


        :return: The label of this DashboardParameterValue.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this DashboardParameterValue.


        :param label: The label of this DashboardParameterValue.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def description(self):
        """Gets the description of this DashboardParameterValue.  # noqa: E501


        :return: The description of this DashboardParameterValue.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DashboardParameterValue.


        :param description: The description of this DashboardParameterValue.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def default_value(self):
        """Gets the default_value of this DashboardParameterValue.  # noqa: E501


        :return: The default_value of this DashboardParameterValue.  # noqa: E501
        :rtype: str
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        """Sets the default_value of this DashboardParameterValue.


        :param default_value: The default_value of this DashboardParameterValue.  # noqa: E501
        :type: str
        """

        self._default_value = default_value

    @property
    def parameter_type(self):
        """Gets the parameter_type of this DashboardParameterValue.  # noqa: E501


        :return: The parameter_type of this DashboardParameterValue.  # noqa: E501
        :rtype: str
        """
        return self._parameter_type

    @parameter_type.setter
    def parameter_type(self, parameter_type):
        """Sets the parameter_type of this DashboardParameterValue.


        :param parameter_type: The parameter_type of this DashboardParameterValue.  # noqa: E501
        :type: str
        """
        allowed_values = ["SIMPLE", "LIST", "DYNAMIC"]  # noqa: E501
        if parameter_type not in allowed_values:
            raise ValueError(
                "Invalid value for `parameter_type` ({0}), must be one of {1}"  # noqa: E501
                .format(parameter_type, allowed_values)
            )

        self._parameter_type = parameter_type

    @property
    def values_to_readable_strings(self):
        """Gets the values_to_readable_strings of this DashboardParameterValue.  # noqa: E501


        :return: The values_to_readable_strings of this DashboardParameterValue.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._values_to_readable_strings

    @values_to_readable_strings.setter
    def values_to_readable_strings(self, values_to_readable_strings):
        """Sets the values_to_readable_strings of this DashboardParameterValue.


        :param values_to_readable_strings: The values_to_readable_strings of this DashboardParameterValue.  # noqa: E501
        :type: dict(str, str)
        """

        self._values_to_readable_strings = values_to_readable_strings

    @property
    def dynamic_field_type(self):
        """Gets the dynamic_field_type of this DashboardParameterValue.  # noqa: E501


        :return: The dynamic_field_type of this DashboardParameterValue.  # noqa: E501
        :rtype: str
        """
        return self._dynamic_field_type

    @dynamic_field_type.setter
    def dynamic_field_type(self, dynamic_field_type):
        """Sets the dynamic_field_type of this DashboardParameterValue.


        :param dynamic_field_type: The dynamic_field_type of this DashboardParameterValue.  # noqa: E501
        :type: str
        """
        allowed_values = ["SOURCE", "SOURCE_TAG", "METRIC_NAME", "TAG_KEY", "MATCHING_SOURCE_TAG"]  # noqa: E501
        if dynamic_field_type not in allowed_values:
            raise ValueError(
                "Invalid value for `dynamic_field_type` ({0}), must be one of {1}"  # noqa: E501
                .format(dynamic_field_type, allowed_values)
            )

        self._dynamic_field_type = dynamic_field_type

    @property
    def query_value(self):
        """Gets the query_value of this DashboardParameterValue.  # noqa: E501


        :return: The query_value of this DashboardParameterValue.  # noqa: E501
        :rtype: str
        """
        return self._query_value

    @query_value.setter
    def query_value(self, query_value):
        """Sets the query_value of this DashboardParameterValue.


        :param query_value: The query_value of this DashboardParameterValue.  # noqa: E501
        :type: str
        """

        self._query_value = query_value

    @property
    def hide_from_view(self):
        """Gets the hide_from_view of this DashboardParameterValue.  # noqa: E501


        :return: The hide_from_view of this DashboardParameterValue.  # noqa: E501
        :rtype: bool
        """
        return self._hide_from_view

    @hide_from_view.setter
    def hide_from_view(self, hide_from_view):
        """Sets the hide_from_view of this DashboardParameterValue.


        :param hide_from_view: The hide_from_view of this DashboardParameterValue.  # noqa: E501
        :type: bool
        """

        self._hide_from_view = hide_from_view

    @property
    def tag_key(self):
        """Gets the tag_key of this DashboardParameterValue.  # noqa: E501


        :return: The tag_key of this DashboardParameterValue.  # noqa: E501
        :rtype: str
        """
        return self._tag_key

    @tag_key.setter
    def tag_key(self, tag_key):
        """Sets the tag_key of this DashboardParameterValue.


        :param tag_key: The tag_key of this DashboardParameterValue.  # noqa: E501
        :type: str
        """

        self._tag_key = tag_key

    @property
    def multivalue(self):
        """Gets the multivalue of this DashboardParameterValue.  # noqa: E501


        :return: The multivalue of this DashboardParameterValue.  # noqa: E501
        :rtype: bool
        """
        return self._multivalue

    @multivalue.setter
    def multivalue(self, multivalue):
        """Sets the multivalue of this DashboardParameterValue.


        :param multivalue: The multivalue of this DashboardParameterValue.  # noqa: E501
        :type: bool
        """

        self._multivalue = multivalue

    @property
    def reverse_dyn_sort(self):
        """Gets the reverse_dyn_sort of this DashboardParameterValue.  # noqa: E501

        Whether to reverse alphabetically sort the returned result.  # noqa: E501

        :return: The reverse_dyn_sort of this DashboardParameterValue.  # noqa: E501
        :rtype: bool
        """
        return self._reverse_dyn_sort

    @reverse_dyn_sort.setter
    def reverse_dyn_sort(self, reverse_dyn_sort):
        """Sets the reverse_dyn_sort of this DashboardParameterValue.

        Whether to reverse alphabetically sort the returned result.  # noqa: E501

        :param reverse_dyn_sort: The reverse_dyn_sort of this DashboardParameterValue.  # noqa: E501
        :type: bool
        """

        self._reverse_dyn_sort = reverse_dyn_sort

    @property
    def allow_all(self):
        """Gets the allow_all of this DashboardParameterValue.  # noqa: E501


        :return: The allow_all of this DashboardParameterValue.  # noqa: E501
        :rtype: bool
        """
        return self._allow_all

    @allow_all.setter
    def allow_all(self, allow_all):
        """Sets the allow_all of this DashboardParameterValue.


        :param allow_all: The allow_all of this DashboardParameterValue.  # noqa: E501
        :type: bool
        """

        self._allow_all = allow_all

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
        if issubclass(DashboardParameterValue, dict):
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
        if not isinstance(other, DashboardParameterValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
