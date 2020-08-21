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


class EventSearchRequest(object):
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
        'cursor': 'str',
        'limit': 'int',
        'query': 'list[SearchQuery]',
        'related_event_time_range': 'RelatedEventTimeRange',
        'sort_score_method': 'str',
        'sort_time_ascending': 'bool',
        'time_range': 'EventTimeRange'
    }

    attribute_map = {
        'cursor': 'cursor',
        'limit': 'limit',
        'query': 'query',
        'related_event_time_range': 'relatedEventTimeRange',
        'sort_score_method': 'sortScoreMethod',
        'sort_time_ascending': 'sortTimeAscending',
        'time_range': 'timeRange'
    }

    def __init__(self, cursor=None, limit=None, query=None, related_event_time_range=None, sort_score_method=None, sort_time_ascending=None, time_range=None):  # noqa: E501
        """EventSearchRequest - a model defined in Swagger"""  # noqa: E501

        self._cursor = None
        self._limit = None
        self._query = None
        self._related_event_time_range = None
        self._sort_score_method = None
        self._sort_time_ascending = None
        self._time_range = None
        self.discriminator = None

        if cursor is not None:
            self.cursor = cursor
        if limit is not None:
            self.limit = limit
        if query is not None:
            self.query = query
        if related_event_time_range is not None:
            self.related_event_time_range = related_event_time_range
        if sort_score_method is not None:
            self.sort_score_method = sort_score_method
        if sort_time_ascending is not None:
            self.sort_time_ascending = sort_time_ascending
        if time_range is not None:
            self.time_range = time_range

    @property
    def cursor(self):
        """Gets the cursor of this EventSearchRequest.  # noqa: E501

        The id (exclusive) from which search results resume returning.  Users should supply an entity 'id' to this property.  Its main purpose is to resume where a previous search left off because of the 'limit' parameter.  If a user supplies the last id in a set of results to cursor, while keeping the query the same, the system will return the next page of results  # noqa: E501

        :return: The cursor of this EventSearchRequest.  # noqa: E501
        :rtype: str
        """
        return self._cursor

    @cursor.setter
    def cursor(self, cursor):
        """Sets the cursor of this EventSearchRequest.

        The id (exclusive) from which search results resume returning.  Users should supply an entity 'id' to this property.  Its main purpose is to resume where a previous search left off because of the 'limit' parameter.  If a user supplies the last id in a set of results to cursor, while keeping the query the same, the system will return the next page of results  # noqa: E501

        :param cursor: The cursor of this EventSearchRequest.  # noqa: E501
        :type: str
        """

        self._cursor = cursor

    @property
    def limit(self):
        """Gets the limit of this EventSearchRequest.  # noqa: E501

        The number of results to return.  Default: 100  # noqa: E501

        :return: The limit of this EventSearchRequest.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this EventSearchRequest.

        The number of results to return.  Default: 100  # noqa: E501

        :param limit: The limit of this EventSearchRequest.  # noqa: E501
        :type: int
        """

        self._limit = limit

    @property
    def query(self):
        """Gets the query of this EventSearchRequest.  # noqa: E501

        A list of queries by which to limit the search results  # noqa: E501

        :return: The query of this EventSearchRequest.  # noqa: E501
        :rtype: list[SearchQuery]
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this EventSearchRequest.

        A list of queries by which to limit the search results  # noqa: E501

        :param query: The query of this EventSearchRequest.  # noqa: E501
        :type: list[SearchQuery]
        """

        self._query = query

    @property
    def related_event_time_range(self):
        """Gets the related_event_time_range of this EventSearchRequest.  # noqa: E501


        :return: The related_event_time_range of this EventSearchRequest.  # noqa: E501
        :rtype: RelatedEventTimeRange
        """
        return self._related_event_time_range

    @related_event_time_range.setter
    def related_event_time_range(self, related_event_time_range):
        """Sets the related_event_time_range of this EventSearchRequest.


        :param related_event_time_range: The related_event_time_range of this EventSearchRequest.  # noqa: E501
        :type: RelatedEventTimeRange
        """

        self._related_event_time_range = related_event_time_range

    @property
    def sort_score_method(self):
        """Gets the sort_score_method of this EventSearchRequest.  # noqa: E501

        Whether to sort events on similarity score : {NONE, SCORE_ASC, SCORE_DES}. Default: NONE. If sortScoreMethod is set to SCORE_ASC or SCORE_DES, it will override time sort  # noqa: E501

        :return: The sort_score_method of this EventSearchRequest.  # noqa: E501
        :rtype: str
        """
        return self._sort_score_method

    @sort_score_method.setter
    def sort_score_method(self, sort_score_method):
        """Sets the sort_score_method of this EventSearchRequest.

        Whether to sort events on similarity score : {NONE, SCORE_ASC, SCORE_DES}. Default: NONE. If sortScoreMethod is set to SCORE_ASC or SCORE_DES, it will override time sort  # noqa: E501

        :param sort_score_method: The sort_score_method of this EventSearchRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["SCORE_ASC", "SCORE_DES", "NONE"]  # noqa: E501
        if sort_score_method not in allowed_values:
            raise ValueError(
                "Invalid value for `sort_score_method` ({0}), must be one of {1}"  # noqa: E501
                .format(sort_score_method, allowed_values)
            )

        self._sort_score_method = sort_score_method

    @property
    def sort_time_ascending(self):
        """Gets the sort_time_ascending of this EventSearchRequest.  # noqa: E501

        Whether to sort event results ascending in start time.  Default: false  # noqa: E501

        :return: The sort_time_ascending of this EventSearchRequest.  # noqa: E501
        :rtype: bool
        """
        return self._sort_time_ascending

    @sort_time_ascending.setter
    def sort_time_ascending(self, sort_time_ascending):
        """Sets the sort_time_ascending of this EventSearchRequest.

        Whether to sort event results ascending in start time.  Default: false  # noqa: E501

        :param sort_time_ascending: The sort_time_ascending of this EventSearchRequest.  # noqa: E501
        :type: bool
        """

        self._sort_time_ascending = sort_time_ascending

    @property
    def time_range(self):
        """Gets the time_range of this EventSearchRequest.  # noqa: E501


        :return: The time_range of this EventSearchRequest.  # noqa: E501
        :rtype: EventTimeRange
        """
        return self._time_range

    @time_range.setter
    def time_range(self, time_range):
        """Sets the time_range of this EventSearchRequest.


        :param time_range: The time_range of this EventSearchRequest.  # noqa: E501
        :type: EventTimeRange
        """

        self._time_range = time_range

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
        if issubclass(EventSearchRequest, dict):
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
        if not isinstance(other, EventSearchRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
