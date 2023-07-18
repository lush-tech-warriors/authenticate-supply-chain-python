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

class SearchLookupDto(object):
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
        'statuses': 'list[str]',
        'risks': 'list[str]',
        'company_functions': 'list[str]',
        'tiers': 'list[int]'
    }

    attribute_map = {
        'statuses': 'statuses',
        'risks': 'risks',
        'company_functions': 'companyFunctions',
        'tiers': 'tiers'
    }

    def __init__(self, statuses=None, risks=None, company_functions=None, tiers=None):  # noqa: E501
        """SearchLookupDto - a model defined in Swagger"""  # noqa: E501
        self._statuses = None
        self._risks = None
        self._company_functions = None
        self._tiers = None
        self.discriminator = None
        if statuses is not None:
            self.statuses = statuses
        if risks is not None:
            self.risks = risks
        if company_functions is not None:
            self.company_functions = company_functions
        if tiers is not None:
            self.tiers = tiers

    @property
    def statuses(self):
        """Gets the statuses of this SearchLookupDto.  # noqa: E501

        The status you have assigned to this supplier  # noqa: E501

        :return: The statuses of this SearchLookupDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._statuses

    @statuses.setter
    def statuses(self, statuses):
        """Sets the statuses of this SearchLookupDto.

        The status you have assigned to this supplier  # noqa: E501

        :param statuses: The statuses of this SearchLookupDto.  # noqa: E501
        :type: list[str]
        """

        self._statuses = statuses

    @property
    def risks(self):
        """Gets the risks of this SearchLookupDto.  # noqa: E501

        The risk you have assigned to this supplier  # noqa: E501

        :return: The risks of this SearchLookupDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._risks

    @risks.setter
    def risks(self, risks):
        """Sets the risks of this SearchLookupDto.

        The risk you have assigned to this supplier  # noqa: E501

        :param risks: The risks of this SearchLookupDto.  # noqa: E501
        :type: list[str]
        """

        self._risks = risks

    @property
    def company_functions(self):
        """Gets the company_functions of this SearchLookupDto.  # noqa: E501

        The function(s) that the supplier provides to your site  # noqa: E501

        :return: The company_functions of this SearchLookupDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._company_functions

    @company_functions.setter
    def company_functions(self, company_functions):
        """Sets the company_functions of this SearchLookupDto.

        The function(s) that the supplier provides to your site  # noqa: E501

        :param company_functions: The company_functions of this SearchLookupDto.  # noqa: E501
        :type: list[str]
        """

        self._company_functions = company_functions

    @property
    def tiers(self):
        """Gets the tiers of this SearchLookupDto.  # noqa: E501

        Tiers at which this company appears in your supply chain(s)  # noqa: E501

        :return: The tiers of this SearchLookupDto.  # noqa: E501
        :rtype: list[int]
        """
        return self._tiers

    @tiers.setter
    def tiers(self, tiers):
        """Sets the tiers of this SearchLookupDto.

        Tiers at which this company appears in your supply chain(s)  # noqa: E501

        :param tiers: The tiers of this SearchLookupDto.  # noqa: E501
        :type: list[int]
        """

        self._tiers = tiers

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
        if issubclass(SearchLookupDto, dict):
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
        if not isinstance(other, SearchLookupDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other