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


class UserGroupPropertiesDTO(object):
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
        'name_editable': 'bool',
        'permissions_editable': 'bool',
        'roles_editable': 'bool',
        'users_editable': 'bool'
    }

    attribute_map = {
        'name_editable': 'nameEditable',
        'permissions_editable': 'permissionsEditable',
        'roles_editable': 'rolesEditable',
        'users_editable': 'usersEditable'
    }

    def __init__(self, name_editable=None, permissions_editable=None, roles_editable=None, users_editable=None):  # noqa: E501
        """UserGroupPropertiesDTO - a model defined in Swagger"""  # noqa: E501

        self._name_editable = None
        self._permissions_editable = None
        self._roles_editable = None
        self._users_editable = None
        self.discriminator = None

        if name_editable is not None:
            self.name_editable = name_editable
        if permissions_editable is not None:
            self.permissions_editable = permissions_editable
        if roles_editable is not None:
            self.roles_editable = roles_editable
        if users_editable is not None:
            self.users_editable = users_editable

    @property
    def name_editable(self):
        """Gets the name_editable of this UserGroupPropertiesDTO.  # noqa: E501


        :return: The name_editable of this UserGroupPropertiesDTO.  # noqa: E501
        :rtype: bool
        """
        return self._name_editable

    @name_editable.setter
    def name_editable(self, name_editable):
        """Sets the name_editable of this UserGroupPropertiesDTO.


        :param name_editable: The name_editable of this UserGroupPropertiesDTO.  # noqa: E501
        :type: bool
        """

        self._name_editable = name_editable

    @property
    def permissions_editable(self):
        """Gets the permissions_editable of this UserGroupPropertiesDTO.  # noqa: E501


        :return: The permissions_editable of this UserGroupPropertiesDTO.  # noqa: E501
        :rtype: bool
        """
        return self._permissions_editable

    @permissions_editable.setter
    def permissions_editable(self, permissions_editable):
        """Sets the permissions_editable of this UserGroupPropertiesDTO.


        :param permissions_editable: The permissions_editable of this UserGroupPropertiesDTO.  # noqa: E501
        :type: bool
        """

        self._permissions_editable = permissions_editable

    @property
    def roles_editable(self):
        """Gets the roles_editable of this UserGroupPropertiesDTO.  # noqa: E501


        :return: The roles_editable of this UserGroupPropertiesDTO.  # noqa: E501
        :rtype: bool
        """
        return self._roles_editable

    @roles_editable.setter
    def roles_editable(self, roles_editable):
        """Sets the roles_editable of this UserGroupPropertiesDTO.


        :param roles_editable: The roles_editable of this UserGroupPropertiesDTO.  # noqa: E501
        :type: bool
        """

        self._roles_editable = roles_editable

    @property
    def users_editable(self):
        """Gets the users_editable of this UserGroupPropertiesDTO.  # noqa: E501


        :return: The users_editable of this UserGroupPropertiesDTO.  # noqa: E501
        :rtype: bool
        """
        return self._users_editable

    @users_editable.setter
    def users_editable(self, users_editable):
        """Sets the users_editable of this UserGroupPropertiesDTO.


        :param users_editable: The users_editable of this UserGroupPropertiesDTO.  # noqa: E501
        :type: bool
        """

        self._users_editable = users_editable

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
        if issubclass(UserGroupPropertiesDTO, dict):
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
        if not isinstance(other, UserGroupPropertiesDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
