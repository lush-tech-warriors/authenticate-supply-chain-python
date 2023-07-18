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

class SupplierProductLinkDto(object):
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
        'id': 'str',
        'status': 'str',
        'status_message': 'str',
        'requested_product_reference': 'str',
        'requested_product_name': 'str',
        'request_message': 'str',
        'link_created_date': 'datetime',
        'status_updated_date': 'datetime',
        'raw_material_id': 'str',
        'my_product_id': 'str',
        'my_product_reference': 'str',
        'my_product_name': 'str',
        'supplier_id': 'str',
        'supplier_name': 'str',
        'supplier_product_id': 'str',
        'supplier_product_reference': 'str',
        'supplier_product_name': 'str',
        'supplier_sites': 'list[SupplierLinkSiteDto]'
    }

    attribute_map = {
        'id': 'id',
        'status': 'status',
        'status_message': 'statusMessage',
        'requested_product_reference': 'requestedProductReference',
        'requested_product_name': 'requestedProductName',
        'request_message': 'requestMessage',
        'link_created_date': 'linkCreatedDate',
        'status_updated_date': 'statusUpdatedDate',
        'raw_material_id': 'rawMaterialId',
        'my_product_id': 'myProductId',
        'my_product_reference': 'myProductReference',
        'my_product_name': 'myProductName',
        'supplier_id': 'supplierId',
        'supplier_name': 'supplierName',
        'supplier_product_id': 'supplierProductId',
        'supplier_product_reference': 'supplierProductReference',
        'supplier_product_name': 'supplierProductName',
        'supplier_sites': 'supplierSites'
    }

    def __init__(self, id=None, status=None, status_message=None, requested_product_reference=None, requested_product_name=None, request_message=None, link_created_date=None, status_updated_date=None, raw_material_id=None, my_product_id=None, my_product_reference=None, my_product_name=None, supplier_id=None, supplier_name=None, supplier_product_id=None, supplier_product_reference=None, supplier_product_name=None, supplier_sites=None):  # noqa: E501
        """SupplierProductLinkDto - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._status = None
        self._status_message = None
        self._requested_product_reference = None
        self._requested_product_name = None
        self._request_message = None
        self._link_created_date = None
        self._status_updated_date = None
        self._raw_material_id = None
        self._my_product_id = None
        self._my_product_reference = None
        self._my_product_name = None
        self._supplier_id = None
        self._supplier_name = None
        self._supplier_product_id = None
        self._supplier_product_reference = None
        self._supplier_product_name = None
        self._supplier_sites = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if status is not None:
            self.status = status
        if status_message is not None:
            self.status_message = status_message
        if requested_product_reference is not None:
            self.requested_product_reference = requested_product_reference
        if requested_product_name is not None:
            self.requested_product_name = requested_product_name
        if request_message is not None:
            self.request_message = request_message
        if link_created_date is not None:
            self.link_created_date = link_created_date
        if status_updated_date is not None:
            self.status_updated_date = status_updated_date
        if raw_material_id is not None:
            self.raw_material_id = raw_material_id
        if my_product_id is not None:
            self.my_product_id = my_product_id
        if my_product_reference is not None:
            self.my_product_reference = my_product_reference
        if my_product_name is not None:
            self.my_product_name = my_product_name
        if supplier_id is not None:
            self.supplier_id = supplier_id
        if supplier_name is not None:
            self.supplier_name = supplier_name
        if supplier_product_id is not None:
            self.supplier_product_id = supplier_product_id
        if supplier_product_reference is not None:
            self.supplier_product_reference = supplier_product_reference
        if supplier_product_name is not None:
            self.supplier_product_name = supplier_product_name
        if supplier_sites is not None:
            self.supplier_sites = supplier_sites

    @property
    def id(self):
        """Gets the id of this SupplierProductLinkDto.  # noqa: E501

        The unique identifier of the product link within the Authenticate platform  # noqa: E501

        :return: The id of this SupplierProductLinkDto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SupplierProductLinkDto.

        The unique identifier of the product link within the Authenticate platform  # noqa: E501

        :param id: The id of this SupplierProductLinkDto.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def status(self):
        """Gets the status of this SupplierProductLinkDto.  # noqa: E501

        The status of this link. Pending and Accepted are current \"Active\" links, any other value is no longer \"Active\"  # noqa: E501

        :return: The status of this SupplierProductLinkDto.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SupplierProductLinkDto.

        The status of this link. Pending and Accepted are current \"Active\" links, any other value is no longer \"Active\"  # noqa: E501

        :param status: The status of this SupplierProductLinkDto.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def status_message(self):
        """Gets the status_message of this SupplierProductLinkDto.  # noqa: E501

        The message included when setting the current status. Generally only included when rejecting, removing or rescinding a link request  # noqa: E501

        :return: The status_message of this SupplierProductLinkDto.  # noqa: E501
        :rtype: str
        """
        return self._status_message

    @status_message.setter
    def status_message(self, status_message):
        """Sets the status_message of this SupplierProductLinkDto.

        The message included when setting the current status. Generally only included when rejecting, removing or rescinding a link request  # noqa: E501

        :param status_message: The status_message of this SupplierProductLinkDto.  # noqa: E501
        :type: str
        """

        self._status_message = status_message

    @property
    def requested_product_reference(self):
        """Gets the requested_product_reference of this SupplierProductLinkDto.  # noqa: E501

        The product reference code specified in the original link request  # noqa: E501

        :return: The requested_product_reference of this SupplierProductLinkDto.  # noqa: E501
        :rtype: str
        """
        return self._requested_product_reference

    @requested_product_reference.setter
    def requested_product_reference(self, requested_product_reference):
        """Sets the requested_product_reference of this SupplierProductLinkDto.

        The product reference code specified in the original link request  # noqa: E501

        :param requested_product_reference: The requested_product_reference of this SupplierProductLinkDto.  # noqa: E501
        :type: str
        """

        self._requested_product_reference = requested_product_reference

    @property
    def requested_product_name(self):
        """Gets the requested_product_name of this SupplierProductLinkDto.  # noqa: E501

        The product name specified in the original link request  # noqa: E501

        :return: The requested_product_name of this SupplierProductLinkDto.  # noqa: E501
        :rtype: str
        """
        return self._requested_product_name

    @requested_product_name.setter
    def requested_product_name(self, requested_product_name):
        """Sets the requested_product_name of this SupplierProductLinkDto.

        The product name specified in the original link request  # noqa: E501

        :param requested_product_name: The requested_product_name of this SupplierProductLinkDto.  # noqa: E501
        :type: str
        """

        self._requested_product_name = requested_product_name

    @property
    def request_message(self):
        """Gets the request_message of this SupplierProductLinkDto.  # noqa: E501

        The message included in the original link request  # noqa: E501

        :return: The request_message of this SupplierProductLinkDto.  # noqa: E501
        :rtype: str
        """
        return self._request_message

    @request_message.setter
    def request_message(self, request_message):
        """Sets the request_message of this SupplierProductLinkDto.

        The message included in the original link request  # noqa: E501

        :param request_message: The request_message of this SupplierProductLinkDto.  # noqa: E501
        :type: str
        """

        self._request_message = request_message

    @property
    def link_created_date(self):
        """Gets the link_created_date of this SupplierProductLinkDto.  # noqa: E501

        The UTC date and time at which the link was initially created  # noqa: E501

        :return: The link_created_date of this SupplierProductLinkDto.  # noqa: E501
        :rtype: datetime
        """
        return self._link_created_date

    @link_created_date.setter
    def link_created_date(self, link_created_date):
        """Sets the link_created_date of this SupplierProductLinkDto.

        The UTC date and time at which the link was initially created  # noqa: E501

        :param link_created_date: The link_created_date of this SupplierProductLinkDto.  # noqa: E501
        :type: datetime
        """

        self._link_created_date = link_created_date

    @property
    def status_updated_date(self):
        """Gets the status_updated_date of this SupplierProductLinkDto.  # noqa: E501

        The UTC date and time at which the Status was changed (e.g. from Pending to Accepted)  # noqa: E501

        :return: The status_updated_date of this SupplierProductLinkDto.  # noqa: E501
        :rtype: datetime
        """
        return self._status_updated_date

    @status_updated_date.setter
    def status_updated_date(self, status_updated_date):
        """Sets the status_updated_date of this SupplierProductLinkDto.

        The UTC date and time at which the Status was changed (e.g. from Pending to Accepted)  # noqa: E501

        :param status_updated_date: The status_updated_date of this SupplierProductLinkDto.  # noqa: E501
        :type: datetime
        """

        self._status_updated_date = status_updated_date

    @property
    def raw_material_id(self):
        """Gets the raw_material_id of this SupplierProductLinkDto.  # noqa: E501

        the raw material associated with the product link  # noqa: E501

        :return: The raw_material_id of this SupplierProductLinkDto.  # noqa: E501
        :rtype: str
        """
        return self._raw_material_id

    @raw_material_id.setter
    def raw_material_id(self, raw_material_id):
        """Sets the raw_material_id of this SupplierProductLinkDto.

        the raw material associated with the product link  # noqa: E501

        :param raw_material_id: The raw_material_id of this SupplierProductLinkDto.  # noqa: E501
        :type: str
        """

        self._raw_material_id = raw_material_id

    @property
    def my_product_id(self):
        """Gets the my_product_id of this SupplierProductLinkDto.  # noqa: E501

        The unique identifier of my product.  # noqa: E501

        :return: The my_product_id of this SupplierProductLinkDto.  # noqa: E501
        :rtype: str
        """
        return self._my_product_id

    @my_product_id.setter
    def my_product_id(self, my_product_id):
        """Sets the my_product_id of this SupplierProductLinkDto.

        The unique identifier of my product.  # noqa: E501

        :param my_product_id: The my_product_id of this SupplierProductLinkDto.  # noqa: E501
        :type: str
        """

        self._my_product_id = my_product_id

    @property
    def my_product_reference(self):
        """Gets the my_product_reference of this SupplierProductLinkDto.  # noqa: E501

        The reference code of my product.  # noqa: E501

        :return: The my_product_reference of this SupplierProductLinkDto.  # noqa: E501
        :rtype: str
        """
        return self._my_product_reference

    @my_product_reference.setter
    def my_product_reference(self, my_product_reference):
        """Sets the my_product_reference of this SupplierProductLinkDto.

        The reference code of my product.  # noqa: E501

        :param my_product_reference: The my_product_reference of this SupplierProductLinkDto.  # noqa: E501
        :type: str
        """

        self._my_product_reference = my_product_reference

    @property
    def my_product_name(self):
        """Gets the my_product_name of this SupplierProductLinkDto.  # noqa: E501

        The name of my product.  # noqa: E501

        :return: The my_product_name of this SupplierProductLinkDto.  # noqa: E501
        :rtype: str
        """
        return self._my_product_name

    @my_product_name.setter
    def my_product_name(self, my_product_name):
        """Sets the my_product_name of this SupplierProductLinkDto.

        The name of my product.  # noqa: E501

        :param my_product_name: The my_product_name of this SupplierProductLinkDto.  # noqa: E501
        :type: str
        """

        self._my_product_name = my_product_name

    @property
    def supplier_id(self):
        """Gets the supplier_id of this SupplierProductLinkDto.  # noqa: E501

        The unique identifier of the supplier company.  # noqa: E501

        :return: The supplier_id of this SupplierProductLinkDto.  # noqa: E501
        :rtype: str
        """
        return self._supplier_id

    @supplier_id.setter
    def supplier_id(self, supplier_id):
        """Sets the supplier_id of this SupplierProductLinkDto.

        The unique identifier of the supplier company.  # noqa: E501

        :param supplier_id: The supplier_id of this SupplierProductLinkDto.  # noqa: E501
        :type: str
        """

        self._supplier_id = supplier_id

    @property
    def supplier_name(self):
        """Gets the supplier_name of this SupplierProductLinkDto.  # noqa: E501

        The name of the supplier company  # noqa: E501

        :return: The supplier_name of this SupplierProductLinkDto.  # noqa: E501
        :rtype: str
        """
        return self._supplier_name

    @supplier_name.setter
    def supplier_name(self, supplier_name):
        """Sets the supplier_name of this SupplierProductLinkDto.

        The name of the supplier company  # noqa: E501

        :param supplier_name: The supplier_name of this SupplierProductLinkDto.  # noqa: E501
        :type: str
        """

        self._supplier_name = supplier_name

    @property
    def supplier_product_id(self):
        """Gets the supplier_product_id of this SupplierProductLinkDto.  # noqa: E501

        The unique identifier of the supplier's product. Could be null if this is a Pending link request  # noqa: E501

        :return: The supplier_product_id of this SupplierProductLinkDto.  # noqa: E501
        :rtype: str
        """
        return self._supplier_product_id

    @supplier_product_id.setter
    def supplier_product_id(self, supplier_product_id):
        """Sets the supplier_product_id of this SupplierProductLinkDto.

        The unique identifier of the supplier's product. Could be null if this is a Pending link request  # noqa: E501

        :param supplier_product_id: The supplier_product_id of this SupplierProductLinkDto.  # noqa: E501
        :type: str
        """

        self._supplier_product_id = supplier_product_id

    @property
    def supplier_product_reference(self):
        """Gets the supplier_product_reference of this SupplierProductLinkDto.  # noqa: E501

        The reference code of the supplier's product. Could be null if this is a Pending link request  # noqa: E501

        :return: The supplier_product_reference of this SupplierProductLinkDto.  # noqa: E501
        :rtype: str
        """
        return self._supplier_product_reference

    @supplier_product_reference.setter
    def supplier_product_reference(self, supplier_product_reference):
        """Sets the supplier_product_reference of this SupplierProductLinkDto.

        The reference code of the supplier's product. Could be null if this is a Pending link request  # noqa: E501

        :param supplier_product_reference: The supplier_product_reference of this SupplierProductLinkDto.  # noqa: E501
        :type: str
        """

        self._supplier_product_reference = supplier_product_reference

    @property
    def supplier_product_name(self):
        """Gets the supplier_product_name of this SupplierProductLinkDto.  # noqa: E501

        The name of the supplier's product. Could be null if this is a Pending link request  # noqa: E501

        :return: The supplier_product_name of this SupplierProductLinkDto.  # noqa: E501
        :rtype: str
        """
        return self._supplier_product_name

    @supplier_product_name.setter
    def supplier_product_name(self, supplier_product_name):
        """Sets the supplier_product_name of this SupplierProductLinkDto.

        The name of the supplier's product. Could be null if this is a Pending link request  # noqa: E501

        :param supplier_product_name: The supplier_product_name of this SupplierProductLinkDto.  # noqa: E501
        :type: str
        """

        self._supplier_product_name = supplier_product_name

    @property
    def supplier_sites(self):
        """Gets the supplier_sites of this SupplierProductLinkDto.  # noqa: E501

        Supplier sites associated with the production of the supplied product  # noqa: E501

        :return: The supplier_sites of this SupplierProductLinkDto.  # noqa: E501
        :rtype: list[SupplierLinkSiteDto]
        """
        return self._supplier_sites

    @supplier_sites.setter
    def supplier_sites(self, supplier_sites):
        """Sets the supplier_sites of this SupplierProductLinkDto.

        Supplier sites associated with the production of the supplied product  # noqa: E501

        :param supplier_sites: The supplier_sites of this SupplierProductLinkDto.  # noqa: E501
        :type: list[SupplierLinkSiteDto]
        """

        self._supplier_sites = supplier_sites

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
        if issubclass(SupplierProductLinkDto, dict):
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
        if not isinstance(other, SupplierProductLinkDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other