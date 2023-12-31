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

class SupplierProductDto(object):
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
        'product_id': 'str',
        'supply_status': 'str',
        'reference_code': 'str',
        'name': 'str',
        'sites': 'list[ProductSiteDto]'
    }

    attribute_map = {
        'product_id': 'productId',
        'supply_status': 'supplyStatus',
        'reference_code': 'referenceCode',
        'name': 'name',
        'sites': 'sites'
    }

    def __init__(self, product_id=None, supply_status=None, reference_code=None, name=None, sites=None):  # noqa: E501
        """SupplierProductDto - a model defined in Swagger"""  # noqa: E501
        self._product_id = None
        self._supply_status = None
        self._reference_code = None
        self._name = None
        self._sites = None
        self.discriminator = None
        if product_id is not None:
            self.product_id = product_id
        if supply_status is not None:
            self.supply_status = supply_status
        if reference_code is not None:
            self.reference_code = reference_code
        if name is not None:
            self.name = name
        if sites is not None:
            self.sites = sites

    @property
    def product_id(self):
        """Gets the product_id of this SupplierProductDto.  # noqa: E501

        The unique identifier of the product within the Authenticate platform (only relevant for an accepted product)  # noqa: E501

        :return: The product_id of this SupplierProductDto.  # noqa: E501
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this SupplierProductDto.

        The unique identifier of the product within the Authenticate platform (only relevant for an accepted product)  # noqa: E501

        :param product_id: The product_id of this SupplierProductDto.  # noqa: E501
        :type: str
        """

        self._product_id = product_id

    @property
    def supply_status(self):
        """Gets the supply_status of this SupplierProductDto.  # noqa: E501

        Indicates whether the product supplied is confirmed (Accepted) or requested (Pending)  # noqa: E501

        :return: The supply_status of this SupplierProductDto.  # noqa: E501
        :rtype: str
        """
        return self._supply_status

    @supply_status.setter
    def supply_status(self, supply_status):
        """Sets the supply_status of this SupplierProductDto.

        Indicates whether the product supplied is confirmed (Accepted) or requested (Pending)  # noqa: E501

        :param supply_status: The supply_status of this SupplierProductDto.  # noqa: E501
        :type: str
        """

        self._supply_status = supply_status

    @property
    def reference_code(self):
        """Gets the reference_code of this SupplierProductDto.  # noqa: E501

        The product reference code  # noqa: E501

        :return: The reference_code of this SupplierProductDto.  # noqa: E501
        :rtype: str
        """
        return self._reference_code

    @reference_code.setter
    def reference_code(self, reference_code):
        """Sets the reference_code of this SupplierProductDto.

        The product reference code  # noqa: E501

        :param reference_code: The reference_code of this SupplierProductDto.  # noqa: E501
        :type: str
        """

        self._reference_code = reference_code

    @property
    def name(self):
        """Gets the name of this SupplierProductDto.  # noqa: E501

        The product name  # noqa: E501

        :return: The name of this SupplierProductDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SupplierProductDto.

        The product name  # noqa: E501

        :param name: The name of this SupplierProductDto.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def sites(self):
        """Gets the sites of this SupplierProductDto.  # noqa: E501

        The sites from which the product is known to be supplied  # noqa: E501

        :return: The sites of this SupplierProductDto.  # noqa: E501
        :rtype: list[ProductSiteDto]
        """
        return self._sites

    @sites.setter
    def sites(self, sites):
        """Sets the sites of this SupplierProductDto.

        The sites from which the product is known to be supplied  # noqa: E501

        :param sites: The sites of this SupplierProductDto.  # noqa: E501
        :type: list[ProductSiteDto]
        """

        self._sites = sites

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
        if issubclass(SupplierProductDto, dict):
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
        if not isinstance(other, SupplierProductDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
