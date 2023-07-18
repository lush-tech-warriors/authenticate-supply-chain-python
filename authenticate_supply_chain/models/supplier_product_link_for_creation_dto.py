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

class SupplierProductLinkForCreationDto(object):
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
        'supplier_id': 'str',
        'my_product_id': 'str',
        'supplier_site_ids': 'list[str]',
        'customer_site_ids': 'list[str]',
        'requested_product_reference': 'str',
        'requested_product_name': 'str',
        'raw_material_function_id': 'str'
    }

    attribute_map = {
        'supplier_id': 'supplierId',
        'my_product_id': 'myProductId',
        'supplier_site_ids': 'supplierSiteIds',
        'customer_site_ids': 'customerSiteIds',
        'requested_product_reference': 'requestedProductReference',
        'requested_product_name': 'requestedProductName',
        'raw_material_function_id': 'rawMaterialFunctionId'
    }

    def __init__(self, supplier_id=None, my_product_id=None, supplier_site_ids=None, customer_site_ids=None, requested_product_reference=None, requested_product_name=None, raw_material_function_id=None):  # noqa: E501
        """SupplierProductLinkForCreationDto - a model defined in Swagger"""  # noqa: E501
        self._supplier_id = None
        self._my_product_id = None
        self._supplier_site_ids = None
        self._customer_site_ids = None
        self._requested_product_reference = None
        self._requested_product_name = None
        self._raw_material_function_id = None
        self.discriminator = None
        self.supplier_id = supplier_id
        self.my_product_id = my_product_id
        if supplier_site_ids is not None:
            self.supplier_site_ids = supplier_site_ids
        if customer_site_ids is not None:
            self.customer_site_ids = customer_site_ids
        self.requested_product_reference = requested_product_reference
        self.requested_product_name = requested_product_name
        if raw_material_function_id is not None:
            self.raw_material_function_id = raw_material_function_id

    @property
    def supplier_id(self):
        """Gets the supplier_id of this SupplierProductLinkForCreationDto.  # noqa: E501

        The unique identifier for the supplier in the Authenticate platform  # noqa: E501

        :return: The supplier_id of this SupplierProductLinkForCreationDto.  # noqa: E501
        :rtype: str
        """
        return self._supplier_id

    @supplier_id.setter
    def supplier_id(self, supplier_id):
        """Sets the supplier_id of this SupplierProductLinkForCreationDto.

        The unique identifier for the supplier in the Authenticate platform  # noqa: E501

        :param supplier_id: The supplier_id of this SupplierProductLinkForCreationDto.  # noqa: E501
        :type: str
        """
        if supplier_id is None:
            raise ValueError("Invalid value for `supplier_id`, must not be `None`")  # noqa: E501

        self._supplier_id = supplier_id

    @property
    def my_product_id(self):
        """Gets the my_product_id of this SupplierProductLinkForCreationDto.  # noqa: E501

        The unique identifier for your product for which the link is being requested  # noqa: E501

        :return: The my_product_id of this SupplierProductLinkForCreationDto.  # noqa: E501
        :rtype: str
        """
        return self._my_product_id

    @my_product_id.setter
    def my_product_id(self, my_product_id):
        """Sets the my_product_id of this SupplierProductLinkForCreationDto.

        The unique identifier for your product for which the link is being requested  # noqa: E501

        :param my_product_id: The my_product_id of this SupplierProductLinkForCreationDto.  # noqa: E501
        :type: str
        """
        if my_product_id is None:
            raise ValueError("Invalid value for `my_product_id`, must not be `None`")  # noqa: E501

        self._my_product_id = my_product_id

    @property
    def supplier_site_ids(self):
        """Gets the supplier_site_ids of this SupplierProductLinkForCreationDto.  # noqa: E501

        The supplier sites to associated with the link request  # noqa: E501

        :return: The supplier_site_ids of this SupplierProductLinkForCreationDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._supplier_site_ids

    @supplier_site_ids.setter
    def supplier_site_ids(self, supplier_site_ids):
        """Sets the supplier_site_ids of this SupplierProductLinkForCreationDto.

        The supplier sites to associated with the link request  # noqa: E501

        :param supplier_site_ids: The supplier_site_ids of this SupplierProductLinkForCreationDto.  # noqa: E501
        :type: list[str]
        """

        self._supplier_site_ids = supplier_site_ids

    @property
    def customer_site_ids(self):
        """Gets the customer_site_ids of this SupplierProductLinkForCreationDto.  # noqa: E501

        The customer sites to associated with the link request  # noqa: E501

        :return: The customer_site_ids of this SupplierProductLinkForCreationDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._customer_site_ids

    @customer_site_ids.setter
    def customer_site_ids(self, customer_site_ids):
        """Sets the customer_site_ids of this SupplierProductLinkForCreationDto.

        The customer sites to associated with the link request  # noqa: E501

        :param customer_site_ids: The customer_site_ids of this SupplierProductLinkForCreationDto.  # noqa: E501
        :type: list[str]
        """

        self._customer_site_ids = customer_site_ids

    @property
    def requested_product_reference(self):
        """Gets the requested_product_reference of this SupplierProductLinkForCreationDto.  # noqa: E501

        The reference code that will help your supplier identify the product to which you are requesting a link  # noqa: E501

        :return: The requested_product_reference of this SupplierProductLinkForCreationDto.  # noqa: E501
        :rtype: str
        """
        return self._requested_product_reference

    @requested_product_reference.setter
    def requested_product_reference(self, requested_product_reference):
        """Sets the requested_product_reference of this SupplierProductLinkForCreationDto.

        The reference code that will help your supplier identify the product to which you are requesting a link  # noqa: E501

        :param requested_product_reference: The requested_product_reference of this SupplierProductLinkForCreationDto.  # noqa: E501
        :type: str
        """
        if requested_product_reference is None:
            raise ValueError("Invalid value for `requested_product_reference`, must not be `None`")  # noqa: E501

        self._requested_product_reference = requested_product_reference

    @property
    def requested_product_name(self):
        """Gets the requested_product_name of this SupplierProductLinkForCreationDto.  # noqa: E501

        The product name that will help your supplier identify the product to which you are requesting a link  # noqa: E501

        :return: The requested_product_name of this SupplierProductLinkForCreationDto.  # noqa: E501
        :rtype: str
        """
        return self._requested_product_name

    @requested_product_name.setter
    def requested_product_name(self, requested_product_name):
        """Sets the requested_product_name of this SupplierProductLinkForCreationDto.

        The product name that will help your supplier identify the product to which you are requesting a link  # noqa: E501

        :param requested_product_name: The requested_product_name of this SupplierProductLinkForCreationDto.  # noqa: E501
        :type: str
        """
        if requested_product_name is None:
            raise ValueError("Invalid value for `requested_product_name`, must not be `None`")  # noqa: E501

        self._requested_product_name = requested_product_name

    @property
    def raw_material_function_id(self):
        """Gets the raw_material_function_id of this SupplierProductLinkForCreationDto.  # noqa: E501

        The function unique identifier for the requested product raw material, if none provided, the default will be 'Supplier'  # noqa: E501

        :return: The raw_material_function_id of this SupplierProductLinkForCreationDto.  # noqa: E501
        :rtype: str
        """
        return self._raw_material_function_id

    @raw_material_function_id.setter
    def raw_material_function_id(self, raw_material_function_id):
        """Sets the raw_material_function_id of this SupplierProductLinkForCreationDto.

        The function unique identifier for the requested product raw material, if none provided, the default will be 'Supplier'  # noqa: E501

        :param raw_material_function_id: The raw_material_function_id of this SupplierProductLinkForCreationDto.  # noqa: E501
        :type: str
        """

        self._raw_material_function_id = raw_material_function_id

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
        if issubclass(SupplierProductLinkForCreationDto, dict):
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
        if not isinstance(other, SupplierProductLinkForCreationDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other