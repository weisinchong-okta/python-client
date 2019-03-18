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

from wavefront_api_client.models.chart_settings import ChartSettings  # noqa: F401,E501
from wavefront_api_client.models.chart_source_query import ChartSourceQuery  # noqa: F401,E501
from wavefront_api_client.models.json_node import JsonNode  # noqa: F401,E501


class Chart(object):
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
        'base': 'int',
        'chart_attributes': 'JsonNode',
        'chart_settings': 'ChartSettings',
        'description': 'str',
        'include_obsolete_metrics': 'bool',
        'interpolate_points': 'bool',
        'name': 'str',
        'no_default_events': 'bool',
        'sources': 'list[ChartSourceQuery]',
        'summarization': 'str',
        'units': 'str'
    }

    attribute_map = {
        'base': 'base',
        'chart_attributes': 'chartAttributes',
        'chart_settings': 'chartSettings',
        'description': 'description',
        'include_obsolete_metrics': 'includeObsoleteMetrics',
        'interpolate_points': 'interpolatePoints',
        'name': 'name',
        'no_default_events': 'noDefaultEvents',
        'sources': 'sources',
        'summarization': 'summarization',
        'units': 'units'
    }

    def __init__(self, base=None, chart_attributes=None, chart_settings=None, description=None, include_obsolete_metrics=None, interpolate_points=None, name=None, no_default_events=None, sources=None, summarization=None, units=None):  # noqa: E501
        """Chart - a model defined in Swagger"""  # noqa: E501

        self._base = None
        self._chart_attributes = None
        self._chart_settings = None
        self._description = None
        self._include_obsolete_metrics = None
        self._interpolate_points = None
        self._name = None
        self._no_default_events = None
        self._sources = None
        self._summarization = None
        self._units = None
        self.discriminator = None

        if base is not None:
            self.base = base
        if chart_attributes is not None:
            self.chart_attributes = chart_attributes
        if chart_settings is not None:
            self.chart_settings = chart_settings
        if description is not None:
            self.description = description
        if include_obsolete_metrics is not None:
            self.include_obsolete_metrics = include_obsolete_metrics
        if interpolate_points is not None:
            self.interpolate_points = interpolate_points
        self.name = name
        if no_default_events is not None:
            self.no_default_events = no_default_events
        self.sources = sources
        if summarization is not None:
            self.summarization = summarization
        if units is not None:
            self.units = units

    @property
    def base(self):
        """Gets the base of this Chart.  # noqa: E501

        If the chart has a log-scale Y-axis, the base for the logarithms  # noqa: E501

        :return: The base of this Chart.  # noqa: E501
        :rtype: int
        """
        return self._base

    @base.setter
    def base(self, base):
        """Sets the base of this Chart.

        If the chart has a log-scale Y-axis, the base for the logarithms  # noqa: E501

        :param base: The base of this Chart.  # noqa: E501
        :type: int
        """

        self._base = base

    @property
    def chart_attributes(self):
        """Gets the chart_attributes of this Chart.  # noqa: E501

        Experimental field for chart attributes  # noqa: E501

        :return: The chart_attributes of this Chart.  # noqa: E501
        :rtype: JsonNode
        """
        return self._chart_attributes

    @chart_attributes.setter
    def chart_attributes(self, chart_attributes):
        """Sets the chart_attributes of this Chart.

        Experimental field for chart attributes  # noqa: E501

        :param chart_attributes: The chart_attributes of this Chart.  # noqa: E501
        :type: JsonNode
        """

        self._chart_attributes = chart_attributes

    @property
    def chart_settings(self):
        """Gets the chart_settings of this Chart.  # noqa: E501


        :return: The chart_settings of this Chart.  # noqa: E501
        :rtype: ChartSettings
        """
        return self._chart_settings

    @chart_settings.setter
    def chart_settings(self, chart_settings):
        """Sets the chart_settings of this Chart.


        :param chart_settings: The chart_settings of this Chart.  # noqa: E501
        :type: ChartSettings
        """

        self._chart_settings = chart_settings

    @property
    def description(self):
        """Gets the description of this Chart.  # noqa: E501

        Description of the chart  # noqa: E501

        :return: The description of this Chart.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Chart.

        Description of the chart  # noqa: E501

        :param description: The description of this Chart.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def include_obsolete_metrics(self):
        """Gets the include_obsolete_metrics of this Chart.  # noqa: E501

        Whether to show obsolete metrics.  Default: false  # noqa: E501

        :return: The include_obsolete_metrics of this Chart.  # noqa: E501
        :rtype: bool
        """
        return self._include_obsolete_metrics

    @include_obsolete_metrics.setter
    def include_obsolete_metrics(self, include_obsolete_metrics):
        """Sets the include_obsolete_metrics of this Chart.

        Whether to show obsolete metrics.  Default: false  # noqa: E501

        :param include_obsolete_metrics: The include_obsolete_metrics of this Chart.  # noqa: E501
        :type: bool
        """

        self._include_obsolete_metrics = include_obsolete_metrics

    @property
    def interpolate_points(self):
        """Gets the interpolate_points of this Chart.  # noqa: E501

        Whether to interpolate points in the charts produced. Default: true  # noqa: E501

        :return: The interpolate_points of this Chart.  # noqa: E501
        :rtype: bool
        """
        return self._interpolate_points

    @interpolate_points.setter
    def interpolate_points(self, interpolate_points):
        """Sets the interpolate_points of this Chart.

        Whether to interpolate points in the charts produced. Default: true  # noqa: E501

        :param interpolate_points: The interpolate_points of this Chart.  # noqa: E501
        :type: bool
        """

        self._interpolate_points = interpolate_points

    @property
    def name(self):
        """Gets the name of this Chart.  # noqa: E501

        Name of the source  # noqa: E501

        :return: The name of this Chart.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Chart.

        Name of the source  # noqa: E501

        :param name: The name of this Chart.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def no_default_events(self):
        """Gets the no_default_events of this Chart.  # noqa: E501

        Whether to hide events related to the sources in the charts produced. Default false (i.e. shows events)  # noqa: E501

        :return: The no_default_events of this Chart.  # noqa: E501
        :rtype: bool
        """
        return self._no_default_events

    @no_default_events.setter
    def no_default_events(self, no_default_events):
        """Sets the no_default_events of this Chart.

        Whether to hide events related to the sources in the charts produced. Default false (i.e. shows events)  # noqa: E501

        :param no_default_events: The no_default_events of this Chart.  # noqa: E501
        :type: bool
        """

        self._no_default_events = no_default_events

    @property
    def sources(self):
        """Gets the sources of this Chart.  # noqa: E501

        Query expression to plot on the chart  # noqa: E501

        :return: The sources of this Chart.  # noqa: E501
        :rtype: list[ChartSourceQuery]
        """
        return self._sources

    @sources.setter
    def sources(self, sources):
        """Sets the sources of this Chart.

        Query expression to plot on the chart  # noqa: E501

        :param sources: The sources of this Chart.  # noqa: E501
        :type: list[ChartSourceQuery]
        """
        if sources is None:
            raise ValueError("Invalid value for `sources`, must not be `None`")  # noqa: E501

        self._sources = sources

    @property
    def summarization(self):
        """Gets the summarization of this Chart.  # noqa: E501

        Summarization strategy for the chart.  MEAN is default  # noqa: E501

        :return: The summarization of this Chart.  # noqa: E501
        :rtype: str
        """
        return self._summarization

    @summarization.setter
    def summarization(self, summarization):
        """Sets the summarization of this Chart.

        Summarization strategy for the chart.  MEAN is default  # noqa: E501

        :param summarization: The summarization of this Chart.  # noqa: E501
        :type: str
        """
        allowed_values = ["MEAN", "MEDIAN", "MIN", "MAX", "SUM", "COUNT", "LAST", "FIRST"]  # noqa: E501
        if summarization not in allowed_values:
            raise ValueError(
                "Invalid value for `summarization` ({0}), must be one of {1}"  # noqa: E501
                .format(summarization, allowed_values)
            )

        self._summarization = summarization

    @property
    def units(self):
        """Gets the units of this Chart.  # noqa: E501

        String to label the units of the chart on the Y-axis  # noqa: E501

        :return: The units of this Chart.  # noqa: E501
        :rtype: str
        """
        return self._units

    @units.setter
    def units(self, units):
        """Sets the units of this Chart.

        String to label the units of the chart on the Y-axis  # noqa: E501

        :param units: The units of this Chart.  # noqa: E501
        :type: str
        """

        self._units = units

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
        if issubclass(Chart, dict):
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
        if not isinstance(other, Chart):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
