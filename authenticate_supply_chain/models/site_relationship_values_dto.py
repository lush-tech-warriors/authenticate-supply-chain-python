# coding: utf-8

"""
    Authenticate Platform Supply Chain API

    Through this API you can Manage products and suppliers. Access to this API is restricted to authenticated users. Before accessing this API, first authenticate via the \"Account\" API. (https://uat-account.authenticateis.com/)  # noqa: E501

    OpenAPI spec version: 1.0
    Contact: platform-support@authenticateis.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class SiteRelationshipValuesDto(object):
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
        'status': 'RelationshipStatusEnum',
        'status_details': 'str',
        'risk': 'RelationshipRiskEnum',
        'risk_details': 'str',
        'review_date': 'datetime',
        'review_details': 'str',
        'utc_date_last_updated': 'datetime',
        'last_updated_user': 'ContactDto'
    }

    attribute_map = {
        'status': 'status',
        'status_details': 'statusDetails',
        'risk': 'risk',
        'risk_details': 'riskDetails',
        'review_date': 'reviewDate',
        'review_details': 'reviewDetails',
        'utc_date_last_updated': 'utcDateLastUpdated',
        'last_updated_user': 'lastUpdatedUser'
    }

    def __init__(self, status=None, status_details=None, risk=None, risk_details=None, review_date=None, review_details=None, utc_date_last_updated=None, last_updated_user=None):  # noqa: E501
        """SiteRelationshipValuesDto - a model defined in Swagger"""  # noqa: E501
        self._status = None
        self._status_details = None
        self._risk = None
        self._risk_details = None
        self._review_date = None
        self._review_details = None
        self._utc_date_last_updated = None
        self._last_updated_user = None
        self.discriminator = None
        if status is not None:
            self.status = status
        if status_details is not None:
            self.status_details = status_details
        if risk is not None:
            self.risk = risk
        if risk_details is not None:
            self.risk_details = risk_details
        if review_date is not None:
            self.review_date = review_date
        if review_details is not None:
            self.review_details = review_details
        if utc_date_last_updated is not None:
            self.utc_date_last_updated = utc_date_last_updated
        if last_updated_user is not None:
            self.last_updated_user = last_updated_user

    @property
    def status(self):
        """Gets the status of this SiteRelationshipValuesDto.  # noqa: E501


        :return: The status of this SiteRelationshipValuesDto.  # noqa: E501
        :rtype: RelationshipStatusEnum
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SiteRelationshipValuesDto.


        :param status: The status of this SiteRelationshipValuesDto.  # noqa: E501
        :type: RelationshipStatusEnum
        """

        self._status = status

    @property
    def status_details(self):
        """Gets the status_details of this SiteRelationshipValuesDto.  # noqa: E501

        The further information regarding the status you have assigned to this site  # noqa: E501

        :return: The status_details of this SiteRelationshipValuesDto.  # noqa: E501
        :rtype: str
        """
        return self._status_details

    @status_details.setter
    def status_details(self, status_details):
        """Sets the status_details of this SiteRelationshipValuesDto.

        The further information regarding the status you have assigned to this site  # noqa: E501

        :param status_details: The status_details of this SiteRelationshipValuesDto.  # noqa: E501
        :type: str
        """

        self._status_details = status_details

    @property
    def risk(self):
        """Gets the risk of this SiteRelationshipValuesDto.  # noqa: E501


        :return: The risk of this SiteRelationshipValuesDto.  # noqa: E501
        :rtype: RelationshipRiskEnum
        """
        return self._risk

    @risk.setter
    def risk(self, risk):
        """Sets the risk of this SiteRelationshipValuesDto.


        :param risk: The risk of this SiteRelationshipValuesDto.  # noqa: E501
        :type: RelationshipRiskEnum
        """

        self._risk = risk

    @property
    def risk_details(self):
        """Gets the risk_details of this SiteRelationshipValuesDto.  # noqa: E501

        The further information regarding the risk you have assigned to this site  # noqa: E501

        :return: The risk_details of this SiteRelationshipValuesDto.  # noqa: E501
        :rtype: str
        """
        return self._risk_details

    @risk_details.setter
    def risk_details(self, risk_details):
        """Sets the risk_details of this SiteRelationshipValuesDto.

        The further information regarding the risk you have assigned to this site  # noqa: E501

        :param risk_details: The risk_details of this SiteRelationshipValuesDto.  # noqa: E501
        :type: str
        """

        self._risk_details = risk_details

    @property
    def review_date(self):
        """Gets the review_date of this SiteRelationshipValuesDto.  # noqa: E501

        The review date you have assigned to this site  # noqa: E501

        :return: The review_date of this SiteRelationshipValuesDto.  # noqa: E501
        :rtype: datetime
        """
        return self._review_date

    @review_date.setter
    def review_date(self, review_date):
        """Sets the review_date of this SiteRelationshipValuesDto.

        The review date you have assigned to this site  # noqa: E501

        :param review_date: The review_date of this SiteRelationshipValuesDto.  # noqa: E501
        :type: datetime
        """

        self._review_date = review_date

    @property
    def review_details(self):
        """Gets the review_details of this SiteRelationshipValuesDto.  # noqa: E501

        The review details you have assigned to this site  # noqa: E501

        :return: The review_details of this SiteRelationshipValuesDto.  # noqa: E501
        :rtype: str
        """
        return self._review_details

    @review_details.setter
    def review_details(self, review_details):
        """Sets the review_details of this SiteRelationshipValuesDto.

        The review details you have assigned to this site  # noqa: E501

        :param review_details: The review_details of this SiteRelationshipValuesDto.  # noqa: E501
        :type: str
        """

        self._review_details = review_details

    @property
    def utc_date_last_updated(self):
        """Gets the utc_date_last_updated of this SiteRelationshipValuesDto.  # noqa: E501

        The date the status/risk or review details were last updated (UTC)  # noqa: E501

        :return: The utc_date_last_updated of this SiteRelationshipValuesDto.  # noqa: E501
        :rtype: datetime
        """
        return self._utc_date_last_updated

    @utc_date_last_updated.setter
    def utc_date_last_updated(self, utc_date_last_updated):
        """Sets the utc_date_last_updated of this SiteRelationshipValuesDto.

        The date the status/risk or review details were last updated (UTC)  # noqa: E501

        :param utc_date_last_updated: The utc_date_last_updated of this SiteRelationshipValuesDto.  # noqa: E501
        :type: datetime
        """

        self._utc_date_last_updated = utc_date_last_updated

    @property
    def last_updated_user(self):
        """Gets the last_updated_user of this SiteRelationshipValuesDto.  # noqa: E501


        :return: The last_updated_user of this SiteRelationshipValuesDto.  # noqa: E501
        :rtype: ContactDto
        """
        return self._last_updated_user

    @last_updated_user.setter
    def last_updated_user(self, last_updated_user):
        """Sets the last_updated_user of this SiteRelationshipValuesDto.


        :param last_updated_user: The last_updated_user of this SiteRelationshipValuesDto.  # noqa: E501
        :type: ContactDto
        """

        self._last_updated_user = last_updated_user

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
        if issubclass(SiteRelationshipValuesDto, dict):
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
        if not isinstance(other, SiteRelationshipValuesDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
