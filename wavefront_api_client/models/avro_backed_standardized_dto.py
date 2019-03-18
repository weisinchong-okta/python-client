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


class AvroBackedStandardizedDTO(object):
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
        'created_epoch_millis': 'int',
        'creator_id': 'str',
        'deleted': 'bool',
        'id': 'str',
        'updated_epoch_millis': 'int',
        'updater_id': 'str'
    }

    attribute_map = {
        'created_epoch_millis': 'createdEpochMillis',
        'creator_id': 'creatorId',
        'deleted': 'deleted',
        'id': 'id',
        'updated_epoch_millis': 'updatedEpochMillis',
        'updater_id': 'updaterId'
    }

    def __init__(self, created_epoch_millis=None, creator_id=None, deleted=None, id=None, updated_epoch_millis=None, updater_id=None):  # noqa: E501
        """AvroBackedStandardizedDTO - a model defined in Swagger"""  # noqa: E501

        self._created_epoch_millis = None
        self._creator_id = None
        self._deleted = None
        self._id = None
        self._updated_epoch_millis = None
        self._updater_id = None
        self.discriminator = None

        if created_epoch_millis is not None:
            self.created_epoch_millis = created_epoch_millis
        if creator_id is not None:
            self.creator_id = creator_id
        if deleted is not None:
            self.deleted = deleted
        if id is not None:
            self.id = id
        if updated_epoch_millis is not None:
            self.updated_epoch_millis = updated_epoch_millis
        if updater_id is not None:
            self.updater_id = updater_id

    @property
    def created_epoch_millis(self):
        """Gets the created_epoch_millis of this AvroBackedStandardizedDTO.  # noqa: E501


        :return: The created_epoch_millis of this AvroBackedStandardizedDTO.  # noqa: E501
        :rtype: int
        """
        return self._created_epoch_millis

    @created_epoch_millis.setter
    def created_epoch_millis(self, created_epoch_millis):
        """Sets the created_epoch_millis of this AvroBackedStandardizedDTO.


        :param created_epoch_millis: The created_epoch_millis of this AvroBackedStandardizedDTO.  # noqa: E501
        :type: int
        """

        self._created_epoch_millis = created_epoch_millis

    @property
    def creator_id(self):
        """Gets the creator_id of this AvroBackedStandardizedDTO.  # noqa: E501


        :return: The creator_id of this AvroBackedStandardizedDTO.  # noqa: E501
        :rtype: str
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        """Sets the creator_id of this AvroBackedStandardizedDTO.


        :param creator_id: The creator_id of this AvroBackedStandardizedDTO.  # noqa: E501
        :type: str
        """

        self._creator_id = creator_id

    @property
    def deleted(self):
        """Gets the deleted of this AvroBackedStandardizedDTO.  # noqa: E501


        :return: The deleted of this AvroBackedStandardizedDTO.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this AvroBackedStandardizedDTO.


        :param deleted: The deleted of this AvroBackedStandardizedDTO.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def id(self):
        """Gets the id of this AvroBackedStandardizedDTO.  # noqa: E501


        :return: The id of this AvroBackedStandardizedDTO.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AvroBackedStandardizedDTO.


        :param id: The id of this AvroBackedStandardizedDTO.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def updated_epoch_millis(self):
        """Gets the updated_epoch_millis of this AvroBackedStandardizedDTO.  # noqa: E501


        :return: The updated_epoch_millis of this AvroBackedStandardizedDTO.  # noqa: E501
        :rtype: int
        """
        return self._updated_epoch_millis

    @updated_epoch_millis.setter
    def updated_epoch_millis(self, updated_epoch_millis):
        """Sets the updated_epoch_millis of this AvroBackedStandardizedDTO.


        :param updated_epoch_millis: The updated_epoch_millis of this AvroBackedStandardizedDTO.  # noqa: E501
        :type: int
        """

        self._updated_epoch_millis = updated_epoch_millis

    @property
    def updater_id(self):
        """Gets the updater_id of this AvroBackedStandardizedDTO.  # noqa: E501


        :return: The updater_id of this AvroBackedStandardizedDTO.  # noqa: E501
        :rtype: str
        """
        return self._updater_id

    @updater_id.setter
    def updater_id(self, updater_id):
        """Sets the updater_id of this AvroBackedStandardizedDTO.


        :param updater_id: The updater_id of this AvroBackedStandardizedDTO.  # noqa: E501
        :type: str
        """

        self._updater_id = updater_id

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
        if issubclass(AvroBackedStandardizedDTO, dict):
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
        if not isinstance(other, AvroBackedStandardizedDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
