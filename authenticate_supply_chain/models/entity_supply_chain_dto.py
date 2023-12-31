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

class EntitySupplyChainDto(object):
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
        'company_id': 'str',
        'company_name': 'str',
        'company_country_name': 'str',
        'authenticate_member': 'bool',
        'is_farm': 'bool',
        'link_id': 'str',
        'parent_link_id': 'str',
        'item_id': 'str',
        'name': 'str',
        'reference': 'str',
        'not_mapped_reason': 'NotMappingProductLineReasonEnum',
        'tier': 'int',
        'status': 'str',
        'created_by_company_id': 'str',
        'created_by_user_id': 'str',
        'raw_material_id': 'str',
        'supplier_sites': 'list[EntitySupplyChainSiteDto]',
        'customer_sites': 'list[EntitySupplyChainSiteDto]'
    }

    attribute_map = {
        'company_id': 'companyId',
        'company_name': 'companyName',
        'company_country_name': 'companyCountryName',
        'authenticate_member': 'authenticateMember',
        'is_farm': 'isFarm',
        'link_id': 'linkId',
        'parent_link_id': 'parentLinkId',
        'item_id': 'itemId',
        'name': 'name',
        'reference': 'reference',
        'not_mapped_reason': 'notMappedReason',
        'tier': 'tier',
        'status': 'status',
        'created_by_company_id': 'createdByCompanyId',
        'created_by_user_id': 'createdByUserId',
        'raw_material_id': 'rawMaterialId',
        'supplier_sites': 'supplierSites',
        'customer_sites': 'customerSites'
    }

    def __init__(self, company_id=None, company_name=None, company_country_name=None, authenticate_member=None, is_farm=None, link_id=None, parent_link_id=None, item_id=None, name=None, reference=None, not_mapped_reason=None, tier=None, status=None, created_by_company_id=None, created_by_user_id=None, raw_material_id=None, supplier_sites=None, customer_sites=None):  # noqa: E501
        """EntitySupplyChainDto - a model defined in Swagger"""  # noqa: E501
        self._company_id = None
        self._company_name = None
        self._company_country_name = None
        self._authenticate_member = None
        self._is_farm = None
        self._link_id = None
        self._parent_link_id = None
        self._item_id = None
        self._name = None
        self._reference = None
        self._not_mapped_reason = None
        self._tier = None
        self._status = None
        self._created_by_company_id = None
        self._created_by_user_id = None
        self._raw_material_id = None
        self._supplier_sites = None
        self._customer_sites = None
        self.discriminator = None
        if company_id is not None:
            self.company_id = company_id
        if company_name is not None:
            self.company_name = company_name
        if company_country_name is not None:
            self.company_country_name = company_country_name
        if authenticate_member is not None:
            self.authenticate_member = authenticate_member
        if is_farm is not None:
            self.is_farm = is_farm
        if link_id is not None:
            self.link_id = link_id
        if parent_link_id is not None:
            self.parent_link_id = parent_link_id
        if item_id is not None:
            self.item_id = item_id
        if name is not None:
            self.name = name
        if reference is not None:
            self.reference = reference
        if not_mapped_reason is not None:
            self.not_mapped_reason = not_mapped_reason
        if tier is not None:
            self.tier = tier
        if status is not None:
            self.status = status
        if created_by_company_id is not None:
            self.created_by_company_id = created_by_company_id
        if created_by_user_id is not None:
            self.created_by_user_id = created_by_user_id
        if raw_material_id is not None:
            self.raw_material_id = raw_material_id
        if supplier_sites is not None:
            self.supplier_sites = supplier_sites
        if customer_sites is not None:
            self.customer_sites = customer_sites

    @property
    def company_id(self):
        """Gets the company_id of this EntitySupplyChainDto.  # noqa: E501


        :return: The company_id of this EntitySupplyChainDto.  # noqa: E501
        :rtype: str
        """
        return self._company_id

    @company_id.setter
    def company_id(self, company_id):
        """Sets the company_id of this EntitySupplyChainDto.


        :param company_id: The company_id of this EntitySupplyChainDto.  # noqa: E501
        :type: str
        """

        self._company_id = company_id

    @property
    def company_name(self):
        """Gets the company_name of this EntitySupplyChainDto.  # noqa: E501


        :return: The company_name of this EntitySupplyChainDto.  # noqa: E501
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """Sets the company_name of this EntitySupplyChainDto.


        :param company_name: The company_name of this EntitySupplyChainDto.  # noqa: E501
        :type: str
        """

        self._company_name = company_name

    @property
    def company_country_name(self):
        """Gets the company_country_name of this EntitySupplyChainDto.  # noqa: E501


        :return: The company_country_name of this EntitySupplyChainDto.  # noqa: E501
        :rtype: str
        """
        return self._company_country_name

    @company_country_name.setter
    def company_country_name(self, company_country_name):
        """Sets the company_country_name of this EntitySupplyChainDto.


        :param company_country_name: The company_country_name of this EntitySupplyChainDto.  # noqa: E501
        :type: str
        """

        self._company_country_name = company_country_name

    @property
    def authenticate_member(self):
        """Gets the authenticate_member of this EntitySupplyChainDto.  # noqa: E501


        :return: The authenticate_member of this EntitySupplyChainDto.  # noqa: E501
        :rtype: bool
        """
        return self._authenticate_member

    @authenticate_member.setter
    def authenticate_member(self, authenticate_member):
        """Sets the authenticate_member of this EntitySupplyChainDto.


        :param authenticate_member: The authenticate_member of this EntitySupplyChainDto.  # noqa: E501
        :type: bool
        """

        self._authenticate_member = authenticate_member

    @property
    def is_farm(self):
        """Gets the is_farm of this EntitySupplyChainDto.  # noqa: E501


        :return: The is_farm of this EntitySupplyChainDto.  # noqa: E501
        :rtype: bool
        """
        return self._is_farm

    @is_farm.setter
    def is_farm(self, is_farm):
        """Sets the is_farm of this EntitySupplyChainDto.


        :param is_farm: The is_farm of this EntitySupplyChainDto.  # noqa: E501
        :type: bool
        """

        self._is_farm = is_farm

    @property
    def link_id(self):
        """Gets the link_id of this EntitySupplyChainDto.  # noqa: E501


        :return: The link_id of this EntitySupplyChainDto.  # noqa: E501
        :rtype: str
        """
        return self._link_id

    @link_id.setter
    def link_id(self, link_id):
        """Sets the link_id of this EntitySupplyChainDto.


        :param link_id: The link_id of this EntitySupplyChainDto.  # noqa: E501
        :type: str
        """

        self._link_id = link_id

    @property
    def parent_link_id(self):
        """Gets the parent_link_id of this EntitySupplyChainDto.  # noqa: E501


        :return: The parent_link_id of this EntitySupplyChainDto.  # noqa: E501
        :rtype: str
        """
        return self._parent_link_id

    @parent_link_id.setter
    def parent_link_id(self, parent_link_id):
        """Sets the parent_link_id of this EntitySupplyChainDto.


        :param parent_link_id: The parent_link_id of this EntitySupplyChainDto.  # noqa: E501
        :type: str
        """

        self._parent_link_id = parent_link_id

    @property
    def item_id(self):
        """Gets the item_id of this EntitySupplyChainDto.  # noqa: E501


        :return: The item_id of this EntitySupplyChainDto.  # noqa: E501
        :rtype: str
        """
        return self._item_id

    @item_id.setter
    def item_id(self, item_id):
        """Sets the item_id of this EntitySupplyChainDto.


        :param item_id: The item_id of this EntitySupplyChainDto.  # noqa: E501
        :type: str
        """

        self._item_id = item_id

    @property
    def name(self):
        """Gets the name of this EntitySupplyChainDto.  # noqa: E501


        :return: The name of this EntitySupplyChainDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EntitySupplyChainDto.


        :param name: The name of this EntitySupplyChainDto.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def reference(self):
        """Gets the reference of this EntitySupplyChainDto.  # noqa: E501


        :return: The reference of this EntitySupplyChainDto.  # noqa: E501
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this EntitySupplyChainDto.


        :param reference: The reference of this EntitySupplyChainDto.  # noqa: E501
        :type: str
        """

        self._reference = reference

    @property
    def not_mapped_reason(self):
        """Gets the not_mapped_reason of this EntitySupplyChainDto.  # noqa: E501


        :return: The not_mapped_reason of this EntitySupplyChainDto.  # noqa: E501
        :rtype: NotMappingProductLineReasonEnum
        """
        return self._not_mapped_reason

    @not_mapped_reason.setter
    def not_mapped_reason(self, not_mapped_reason):
        """Sets the not_mapped_reason of this EntitySupplyChainDto.


        :param not_mapped_reason: The not_mapped_reason of this EntitySupplyChainDto.  # noqa: E501
        :type: NotMappingProductLineReasonEnum
        """

        self._not_mapped_reason = not_mapped_reason

    @property
    def tier(self):
        """Gets the tier of this EntitySupplyChainDto.  # noqa: E501


        :return: The tier of this EntitySupplyChainDto.  # noqa: E501
        :rtype: int
        """
        return self._tier

    @tier.setter
    def tier(self, tier):
        """Sets the tier of this EntitySupplyChainDto.


        :param tier: The tier of this EntitySupplyChainDto.  # noqa: E501
        :type: int
        """

        self._tier = tier

    @property
    def status(self):
        """Gets the status of this EntitySupplyChainDto.  # noqa: E501


        :return: The status of this EntitySupplyChainDto.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this EntitySupplyChainDto.


        :param status: The status of this EntitySupplyChainDto.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def created_by_company_id(self):
        """Gets the created_by_company_id of this EntitySupplyChainDto.  # noqa: E501


        :return: The created_by_company_id of this EntitySupplyChainDto.  # noqa: E501
        :rtype: str
        """
        return self._created_by_company_id

    @created_by_company_id.setter
    def created_by_company_id(self, created_by_company_id):
        """Sets the created_by_company_id of this EntitySupplyChainDto.


        :param created_by_company_id: The created_by_company_id of this EntitySupplyChainDto.  # noqa: E501
        :type: str
        """

        self._created_by_company_id = created_by_company_id

    @property
    def created_by_user_id(self):
        """Gets the created_by_user_id of this EntitySupplyChainDto.  # noqa: E501


        :return: The created_by_user_id of this EntitySupplyChainDto.  # noqa: E501
        :rtype: str
        """
        return self._created_by_user_id

    @created_by_user_id.setter
    def created_by_user_id(self, created_by_user_id):
        """Sets the created_by_user_id of this EntitySupplyChainDto.


        :param created_by_user_id: The created_by_user_id of this EntitySupplyChainDto.  # noqa: E501
        :type: str
        """

        self._created_by_user_id = created_by_user_id

    @property
    def raw_material_id(self):
        """Gets the raw_material_id of this EntitySupplyChainDto.  # noqa: E501


        :return: The raw_material_id of this EntitySupplyChainDto.  # noqa: E501
        :rtype: str
        """
        return self._raw_material_id

    @raw_material_id.setter
    def raw_material_id(self, raw_material_id):
        """Sets the raw_material_id of this EntitySupplyChainDto.


        :param raw_material_id: The raw_material_id of this EntitySupplyChainDto.  # noqa: E501
        :type: str
        """

        self._raw_material_id = raw_material_id

    @property
    def supplier_sites(self):
        """Gets the supplier_sites of this EntitySupplyChainDto.  # noqa: E501


        :return: The supplier_sites of this EntitySupplyChainDto.  # noqa: E501
        :rtype: list[EntitySupplyChainSiteDto]
        """
        return self._supplier_sites

    @supplier_sites.setter
    def supplier_sites(self, supplier_sites):
        """Sets the supplier_sites of this EntitySupplyChainDto.


        :param supplier_sites: The supplier_sites of this EntitySupplyChainDto.  # noqa: E501
        :type: list[EntitySupplyChainSiteDto]
        """

        self._supplier_sites = supplier_sites

    @property
    def customer_sites(self):
        """Gets the customer_sites of this EntitySupplyChainDto.  # noqa: E501


        :return: The customer_sites of this EntitySupplyChainDto.  # noqa: E501
        :rtype: list[EntitySupplyChainSiteDto]
        """
        return self._customer_sites

    @customer_sites.setter
    def customer_sites(self, customer_sites):
        """Sets the customer_sites of this EntitySupplyChainDto.


        :param customer_sites: The customer_sites of this EntitySupplyChainDto.  # noqa: E501
        :type: list[EntitySupplyChainSiteDto]
        """

        self._customer_sites = customer_sites

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
        if issubclass(EntitySupplyChainDto, dict):
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
        if not isinstance(other, EntitySupplyChainDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
