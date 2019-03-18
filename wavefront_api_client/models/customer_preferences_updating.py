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


class CustomerPreferencesUpdating(object):
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
        'default_user_groups': 'list[str]',
        'grant_modify_access_to_everyone': 'bool',
        'hide_ts_when_querybuilder_shown': 'bool',
        'invite_permissions': 'list[str]',
        'landing_dashboard_slug': 'str',
        'show_onboarding': 'bool',
        'show_querybuilder_by_default': 'bool'
    }

    attribute_map = {
        'default_user_groups': 'defaultUserGroups',
        'grant_modify_access_to_everyone': 'grantModifyAccessToEveryone',
        'hide_ts_when_querybuilder_shown': 'hideTSWhenQuerybuilderShown',
        'invite_permissions': 'invitePermissions',
        'landing_dashboard_slug': 'landingDashboardSlug',
        'show_onboarding': 'showOnboarding',
        'show_querybuilder_by_default': 'showQuerybuilderByDefault'
    }

    def __init__(self, default_user_groups=None, grant_modify_access_to_everyone=None, hide_ts_when_querybuilder_shown=None, invite_permissions=None, landing_dashboard_slug=None, show_onboarding=None, show_querybuilder_by_default=None):  # noqa: E501
        """CustomerPreferencesUpdating - a model defined in Swagger"""  # noqa: E501

        self._default_user_groups = None
        self._grant_modify_access_to_everyone = None
        self._hide_ts_when_querybuilder_shown = None
        self._invite_permissions = None
        self._landing_dashboard_slug = None
        self._show_onboarding = None
        self._show_querybuilder_by_default = None
        self.discriminator = None

        if default_user_groups is not None:
            self.default_user_groups = default_user_groups
        self.grant_modify_access_to_everyone = grant_modify_access_to_everyone
        self.hide_ts_when_querybuilder_shown = hide_ts_when_querybuilder_shown
        if invite_permissions is not None:
            self.invite_permissions = invite_permissions
        if landing_dashboard_slug is not None:
            self.landing_dashboard_slug = landing_dashboard_slug
        self.show_onboarding = show_onboarding
        self.show_querybuilder_by_default = show_querybuilder_by_default

    @property
    def default_user_groups(self):
        """Gets the default_user_groups of this CustomerPreferencesUpdating.  # noqa: E501

        List of default user groups of the customer  # noqa: E501

        :return: The default_user_groups of this CustomerPreferencesUpdating.  # noqa: E501
        :rtype: list[str]
        """
        return self._default_user_groups

    @default_user_groups.setter
    def default_user_groups(self, default_user_groups):
        """Sets the default_user_groups of this CustomerPreferencesUpdating.

        List of default user groups of the customer  # noqa: E501

        :param default_user_groups: The default_user_groups of this CustomerPreferencesUpdating.  # noqa: E501
        :type: list[str]
        """

        self._default_user_groups = default_user_groups

    @property
    def grant_modify_access_to_everyone(self):
        """Gets the grant_modify_access_to_everyone of this CustomerPreferencesUpdating.  # noqa: E501

        Whether modify access of new entites is granted to Everyone or to the Creator  # noqa: E501

        :return: The grant_modify_access_to_everyone of this CustomerPreferencesUpdating.  # noqa: E501
        :rtype: bool
        """
        return self._grant_modify_access_to_everyone

    @grant_modify_access_to_everyone.setter
    def grant_modify_access_to_everyone(self, grant_modify_access_to_everyone):
        """Sets the grant_modify_access_to_everyone of this CustomerPreferencesUpdating.

        Whether modify access of new entites is granted to Everyone or to the Creator  # noqa: E501

        :param grant_modify_access_to_everyone: The grant_modify_access_to_everyone of this CustomerPreferencesUpdating.  # noqa: E501
        :type: bool
        """
        if grant_modify_access_to_everyone is None:
            raise ValueError("Invalid value for `grant_modify_access_to_everyone`, must not be `None`")  # noqa: E501

        self._grant_modify_access_to_everyone = grant_modify_access_to_everyone

    @property
    def hide_ts_when_querybuilder_shown(self):
        """Gets the hide_ts_when_querybuilder_shown of this CustomerPreferencesUpdating.  # noqa: E501

        Whether to hide TS source input when Querybuilder is shown  # noqa: E501

        :return: The hide_ts_when_querybuilder_shown of this CustomerPreferencesUpdating.  # noqa: E501
        :rtype: bool
        """
        return self._hide_ts_when_querybuilder_shown

    @hide_ts_when_querybuilder_shown.setter
    def hide_ts_when_querybuilder_shown(self, hide_ts_when_querybuilder_shown):
        """Sets the hide_ts_when_querybuilder_shown of this CustomerPreferencesUpdating.

        Whether to hide TS source input when Querybuilder is shown  # noqa: E501

        :param hide_ts_when_querybuilder_shown: The hide_ts_when_querybuilder_shown of this CustomerPreferencesUpdating.  # noqa: E501
        :type: bool
        """
        if hide_ts_when_querybuilder_shown is None:
            raise ValueError("Invalid value for `hide_ts_when_querybuilder_shown`, must not be `None`")  # noqa: E501

        self._hide_ts_when_querybuilder_shown = hide_ts_when_querybuilder_shown

    @property
    def invite_permissions(self):
        """Gets the invite_permissions of this CustomerPreferencesUpdating.  # noqa: E501

        List of invite permissions to apply for each new user  # noqa: E501

        :return: The invite_permissions of this CustomerPreferencesUpdating.  # noqa: E501
        :rtype: list[str]
        """
        return self._invite_permissions

    @invite_permissions.setter
    def invite_permissions(self, invite_permissions):
        """Sets the invite_permissions of this CustomerPreferencesUpdating.

        List of invite permissions to apply for each new user  # noqa: E501

        :param invite_permissions: The invite_permissions of this CustomerPreferencesUpdating.  # noqa: E501
        :type: list[str]
        """

        self._invite_permissions = invite_permissions

    @property
    def landing_dashboard_slug(self):
        """Gets the landing_dashboard_slug of this CustomerPreferencesUpdating.  # noqa: E501

        Dashboard where user will be redirected from landing page  # noqa: E501

        :return: The landing_dashboard_slug of this CustomerPreferencesUpdating.  # noqa: E501
        :rtype: str
        """
        return self._landing_dashboard_slug

    @landing_dashboard_slug.setter
    def landing_dashboard_slug(self, landing_dashboard_slug):
        """Sets the landing_dashboard_slug of this CustomerPreferencesUpdating.

        Dashboard where user will be redirected from landing page  # noqa: E501

        :param landing_dashboard_slug: The landing_dashboard_slug of this CustomerPreferencesUpdating.  # noqa: E501
        :type: str
        """

        self._landing_dashboard_slug = landing_dashboard_slug

    @property
    def show_onboarding(self):
        """Gets the show_onboarding of this CustomerPreferencesUpdating.  # noqa: E501

        Whether to show onboarding for any new user without an override  # noqa: E501

        :return: The show_onboarding of this CustomerPreferencesUpdating.  # noqa: E501
        :rtype: bool
        """
        return self._show_onboarding

    @show_onboarding.setter
    def show_onboarding(self, show_onboarding):
        """Sets the show_onboarding of this CustomerPreferencesUpdating.

        Whether to show onboarding for any new user without an override  # noqa: E501

        :param show_onboarding: The show_onboarding of this CustomerPreferencesUpdating.  # noqa: E501
        :type: bool
        """
        if show_onboarding is None:
            raise ValueError("Invalid value for `show_onboarding`, must not be `None`")  # noqa: E501

        self._show_onboarding = show_onboarding

    @property
    def show_querybuilder_by_default(self):
        """Gets the show_querybuilder_by_default of this CustomerPreferencesUpdating.  # noqa: E501

        Whether the Querybuilder is shown by default  # noqa: E501

        :return: The show_querybuilder_by_default of this CustomerPreferencesUpdating.  # noqa: E501
        :rtype: bool
        """
        return self._show_querybuilder_by_default

    @show_querybuilder_by_default.setter
    def show_querybuilder_by_default(self, show_querybuilder_by_default):
        """Sets the show_querybuilder_by_default of this CustomerPreferencesUpdating.

        Whether the Querybuilder is shown by default  # noqa: E501

        :param show_querybuilder_by_default: The show_querybuilder_by_default of this CustomerPreferencesUpdating.  # noqa: E501
        :type: bool
        """
        if show_querybuilder_by_default is None:
            raise ValueError("Invalid value for `show_querybuilder_by_default`, must not be `None`")  # noqa: E501

        self._show_querybuilder_by_default = show_querybuilder_by_default

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
        if issubclass(CustomerPreferencesUpdating, dict):
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
        if not isinstance(other, CustomerPreferencesUpdating):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
