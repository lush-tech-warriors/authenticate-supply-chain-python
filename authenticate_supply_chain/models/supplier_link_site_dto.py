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

class SupplierLinkSiteDto(object):
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
        'site_id': 'str',
        'site_name': 'str'
    }

    attribute_map = {
        'site_id': 'siteId',
        'site_name': 'siteName'
    }

    def __init__(self, site_id=None, site_name=None):  # noqa: E501
        """SupplierLinkSiteDto - a model defined in Swagger"""  # noqa: E501
        self._site_id = None
        self._site_name = None
        self.discriminator = None
        if site_id is not None:
            self.site_id = site_id
        if site_name is not None:
            self.site_name = site_name

    @property
    def site_id(self):
        """Gets the site_id of this SupplierLinkSiteDto.  # noqa: E501

        The unique identifier for the supplier site in the Authenticate platform  # noqa: E501

        :return: The site_id of this SupplierLinkSiteDto.  # noqa: E501
        :rtype: str
        """
        return self._site_id

    @site_id.setter
    def site_id(self, site_id):
        """Sets the site_id of this SupplierLinkSiteDto.

        The unique identifier for the supplier site in the Authenticate platform  # noqa: E501

        :param site_id: The site_id of this SupplierLinkSiteDto.  # noqa: E501
        :type: str
        """

        self._site_id = site_id

    @property
    def site_name(self):
        """Gets the site_name of this SupplierLinkSiteDto.  # noqa: E501

        The name of the site in the Authenticate platform  # noqa: E501

        :return: The site_name of this SupplierLinkSiteDto.  # noqa: E501
        :rtype: str
        """
        return self._site_name

    @site_name.setter
    def site_name(self, site_name):
        """Sets the site_name of this SupplierLinkSiteDto.

        The name of the site in the Authenticate platform  # noqa: E501

        :param site_name: The site_name of this SupplierLinkSiteDto.  # noqa: E501
        :type: str
        """

        self._site_name = site_name

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
        if issubclass(SupplierLinkSiteDto, dict):
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
        if not isinstance(other, SupplierLinkSiteDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other