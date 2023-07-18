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

class SupplierResourceParameters(object):
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
        'search_query': 'str',
        'page_number': 'int',
        'page_size': 'int',
        'country': 'str',
        'postcode': 'str',
        'authenticate_member': 'bool',
        'company_type': 'str',
        'company_ids': 'list[str]',
        'supplier_codes': 'list[str]',
        'licence_numbers': 'list[str]',
        'supplier_id': 'str',
        'supplier_code': 'str',
        'supplier_status': 'str',
        'supplier_risk': 'str',
        'tier': 'list[int]',
        'start_date': 'datetime',
        'end_date': 'datetime',
        'order_by': 'str'
    }

    attribute_map = {
        'search_query': 'searchQuery',
        'page_number': 'pageNumber',
        'page_size': 'pageSize',
        'country': 'country',
        'postcode': 'postcode',
        'authenticate_member': 'authenticateMember',
        'company_type': 'companyType',
        'company_ids': 'companyIds',
        'supplier_codes': 'supplierCodes',
        'licence_numbers': 'licenceNumbers',
        'supplier_id': 'supplierId',
        'supplier_code': 'supplierCode',
        'supplier_status': 'supplierStatus',
        'supplier_risk': 'supplierRisk',
        'tier': 'tier',
        'start_date': 'startDate',
        'end_date': 'endDate',
        'order_by': 'orderBy'
    }

    def __init__(self, search_query=None, page_number=None, page_size=None, country=None, postcode=None, authenticate_member=None, company_type=None, company_ids=None, supplier_codes=None, licence_numbers=None, supplier_id=None, supplier_code=None, supplier_status=None, supplier_risk=None, tier=None, start_date=None, end_date=None, order_by=None):  # noqa: E501
        """SupplierResourceParameters - a model defined in Swagger"""  # noqa: E501
        self._search_query = None
        self._page_number = None
        self._page_size = None
        self._country = None
        self._postcode = None
        self._authenticate_member = None
        self._company_type = None
        self._company_ids = None
        self._supplier_codes = None
        self._licence_numbers = None
        self._supplier_id = None
        self._supplier_code = None
        self._supplier_status = None
        self._supplier_risk = None
        self._tier = None
        self._start_date = None
        self._end_date = None
        self._order_by = None
        self.discriminator = None
        if search_query is not None:
            self.search_query = search_query
        if page_number is not None:
            self.page_number = page_number
        if page_size is not None:
            self.page_size = page_size
        if country is not None:
            self.country = country
        if postcode is not None:
            self.postcode = postcode
        if authenticate_member is not None:
            self.authenticate_member = authenticate_member
        if company_type is not None:
            self.company_type = company_type
        if company_ids is not None:
            self.company_ids = company_ids
        if supplier_codes is not None:
            self.supplier_codes = supplier_codes
        if licence_numbers is not None:
            self.licence_numbers = licence_numbers
        if supplier_id is not None:
            self.supplier_id = supplier_id
        if supplier_code is not None:
            self.supplier_code = supplier_code
        if supplier_status is not None:
            self.supplier_status = supplier_status
        if supplier_risk is not None:
            self.supplier_risk = supplier_risk
        if tier is not None:
            self.tier = tier
        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date
        if order_by is not None:
            self.order_by = order_by

    @property
    def search_query(self):
        """Gets the search_query of this SupplierResourceParameters.  # noqa: E501


        :return: The search_query of this SupplierResourceParameters.  # noqa: E501
        :rtype: str
        """
        return self._search_query

    @search_query.setter
    def search_query(self, search_query):
        """Sets the search_query of this SupplierResourceParameters.


        :param search_query: The search_query of this SupplierResourceParameters.  # noqa: E501
        :type: str
        """

        self._search_query = search_query

    @property
    def page_number(self):
        """Gets the page_number of this SupplierResourceParameters.  # noqa: E501


        :return: The page_number of this SupplierResourceParameters.  # noqa: E501
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this SupplierResourceParameters.


        :param page_number: The page_number of this SupplierResourceParameters.  # noqa: E501
        :type: int
        """

        self._page_number = page_number

    @property
    def page_size(self):
        """Gets the page_size of this SupplierResourceParameters.  # noqa: E501


        :return: The page_size of this SupplierResourceParameters.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this SupplierResourceParameters.


        :param page_size: The page_size of this SupplierResourceParameters.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

    @property
    def country(self):
        """Gets the country of this SupplierResourceParameters.  # noqa: E501

        Filter supplier by country  # noqa: E501

        :return: The country of this SupplierResourceParameters.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this SupplierResourceParameters.

        Filter supplier by country  # noqa: E501

        :param country: The country of this SupplierResourceParameters.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def postcode(self):
        """Gets the postcode of this SupplierResourceParameters.  # noqa: E501

        Filter supplier by postcode  # noqa: E501

        :return: The postcode of this SupplierResourceParameters.  # noqa: E501
        :rtype: str
        """
        return self._postcode

    @postcode.setter
    def postcode(self, postcode):
        """Sets the postcode of this SupplierResourceParameters.

        Filter supplier by postcode  # noqa: E501

        :param postcode: The postcode of this SupplierResourceParameters.  # noqa: E501
        :type: str
        """

        self._postcode = postcode

    @property
    def authenticate_member(self):
        """Gets the authenticate_member of this SupplierResourceParameters.  # noqa: E501

        Filter by whether the company is a member of the authenticate platform or not  # noqa: E501

        :return: The authenticate_member of this SupplierResourceParameters.  # noqa: E501
        :rtype: bool
        """
        return self._authenticate_member

    @authenticate_member.setter
    def authenticate_member(self, authenticate_member):
        """Sets the authenticate_member of this SupplierResourceParameters.

        Filter by whether the company is a member of the authenticate platform or not  # noqa: E501

        :param authenticate_member: The authenticate_member of this SupplierResourceParameters.  # noqa: E501
        :type: bool
        """

        self._authenticate_member = authenticate_member

    @property
    def company_type(self):
        """Gets the company_type of this SupplierResourceParameters.  # noqa: E501

        Filter by ONS Company Type  # noqa: E501

        :return: The company_type of this SupplierResourceParameters.  # noqa: E501
        :rtype: str
        """
        return self._company_type

    @company_type.setter
    def company_type(self, company_type):
        """Sets the company_type of this SupplierResourceParameters.

        Filter by ONS Company Type  # noqa: E501

        :param company_type: The company_type of this SupplierResourceParameters.  # noqa: E501
        :type: str
        """

        self._company_type = company_type

    @property
    def company_ids(self):
        """Gets the company_ids of this SupplierResourceParameters.  # noqa: E501

        Filter by list of company id's  # noqa: E501

        :return: The company_ids of this SupplierResourceParameters.  # noqa: E501
        :rtype: list[str]
        """
        return self._company_ids

    @company_ids.setter
    def company_ids(self, company_ids):
        """Sets the company_ids of this SupplierResourceParameters.

        Filter by list of company id's  # noqa: E501

        :param company_ids: The company_ids of this SupplierResourceParameters.  # noqa: E501
        :type: list[str]
        """

        self._company_ids = company_ids

    @property
    def supplier_codes(self):
        """Gets the supplier_codes of this SupplierResourceParameters.  # noqa: E501

        Filter by supplier codes  # noqa: E501

        :return: The supplier_codes of this SupplierResourceParameters.  # noqa: E501
        :rtype: list[str]
        """
        return self._supplier_codes

    @supplier_codes.setter
    def supplier_codes(self, supplier_codes):
        """Sets the supplier_codes of this SupplierResourceParameters.

        Filter by supplier codes  # noqa: E501

        :param supplier_codes: The supplier_codes of this SupplierResourceParameters.  # noqa: E501
        :type: list[str]
        """

        self._supplier_codes = supplier_codes

    @property
    def licence_numbers(self):
        """Gets the licence_numbers of this SupplierResourceParameters.  # noqa: E501

        Filter by licence numbers  # noqa: E501

        :return: The licence_numbers of this SupplierResourceParameters.  # noqa: E501
        :rtype: list[str]
        """
        return self._licence_numbers

    @licence_numbers.setter
    def licence_numbers(self, licence_numbers):
        """Sets the licence_numbers of this SupplierResourceParameters.

        Filter by licence numbers  # noqa: E501

        :param licence_numbers: The licence_numbers of this SupplierResourceParameters.  # noqa: E501
        :type: list[str]
        """

        self._licence_numbers = licence_numbers

    @property
    def supplier_id(self):
        """Gets the supplier_id of this SupplierResourceParameters.  # noqa: E501

        Filter by a specific supplier id  # noqa: E501

        :return: The supplier_id of this SupplierResourceParameters.  # noqa: E501
        :rtype: str
        """
        return self._supplier_id

    @supplier_id.setter
    def supplier_id(self, supplier_id):
        """Sets the supplier_id of this SupplierResourceParameters.

        Filter by a specific supplier id  # noqa: E501

        :param supplier_id: The supplier_id of this SupplierResourceParameters.  # noqa: E501
        :type: str
        """

        self._supplier_id = supplier_id

    @property
    def supplier_code(self):
        """Gets the supplier_code of this SupplierResourceParameters.  # noqa: E501

        Filter by the supplier code you have assigned  # noqa: E501

        :return: The supplier_code of this SupplierResourceParameters.  # noqa: E501
        :rtype: str
        """
        return self._supplier_code

    @supplier_code.setter
    def supplier_code(self, supplier_code):
        """Sets the supplier_code of this SupplierResourceParameters.

        Filter by the supplier code you have assigned  # noqa: E501

        :param supplier_code: The supplier_code of this SupplierResourceParameters.  # noqa: E501
        :type: str
        """

        self._supplier_code = supplier_code

    @property
    def supplier_status(self):
        """Gets the supplier_status of this SupplierResourceParameters.  # noqa: E501

        Filter by the supplier status you have assigned  Status values are: Approved, Pending, Suspended, Rejected  # noqa: E501

        :return: The supplier_status of this SupplierResourceParameters.  # noqa: E501
        :rtype: str
        """
        return self._supplier_status

    @supplier_status.setter
    def supplier_status(self, supplier_status):
        """Sets the supplier_status of this SupplierResourceParameters.

        Filter by the supplier status you have assigned  Status values are: Approved, Pending, Suspended, Rejected  # noqa: E501

        :param supplier_status: The supplier_status of this SupplierResourceParameters.  # noqa: E501
        :type: str
        """

        self._supplier_status = supplier_status

    @property
    def supplier_risk(self):
        """Gets the supplier_risk of this SupplierResourceParameters.  # noqa: E501

        Filter by the supplier risk  you have assigned  Risks are: Low, Medium, High  # noqa: E501

        :return: The supplier_risk of this SupplierResourceParameters.  # noqa: E501
        :rtype: str
        """
        return self._supplier_risk

    @supplier_risk.setter
    def supplier_risk(self, supplier_risk):
        """Sets the supplier_risk of this SupplierResourceParameters.

        Filter by the supplier risk  you have assigned  Risks are: Low, Medium, High  # noqa: E501

        :param supplier_risk: The supplier_risk of this SupplierResourceParameters.  # noqa: E501
        :type: str
        """

        self._supplier_risk = supplier_risk

    @property
    def tier(self):
        """Gets the tier of this SupplierResourceParameters.  # noqa: E501

        Filter supplier by supply chain tier (NB: viewing suppliers at Tier 2+ is not available for all membership levels)  # noqa: E501

        :return: The tier of this SupplierResourceParameters.  # noqa: E501
        :rtype: list[int]
        """
        return self._tier

    @tier.setter
    def tier(self, tier):
        """Sets the tier of this SupplierResourceParameters.

        Filter supplier by supply chain tier (NB: viewing suppliers at Tier 2+ is not available for all membership levels)  # noqa: E501

        :param tier: The tier of this SupplierResourceParameters.  # noqa: E501
        :type: list[int]
        """

        self._tier = tier

    @property
    def start_date(self):
        """Gets the start_date of this SupplierResourceParameters.  # noqa: E501

        Limit the returned suppliers to those where a recorded change event occurred on or after this date  Change events include updates to supplier status, risk etc or when a company first appeared in your supply chain  # noqa: E501

        :return: The start_date of this SupplierResourceParameters.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this SupplierResourceParameters.

        Limit the returned suppliers to those where a recorded change event occurred on or after this date  Change events include updates to supplier status, risk etc or when a company first appeared in your supply chain  # noqa: E501

        :param start_date: The start_date of this SupplierResourceParameters.  # noqa: E501
        :type: datetime
        """

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this SupplierResourceParameters.  # noqa: E501

        Limit the returned suppliers to those where a recorded change event occurred before this date    Change events include updates to supplier status, risk etc or when a company first appeared in your supply chain  # noqa: E501

        :return: The end_date of this SupplierResourceParameters.  # noqa: E501
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this SupplierResourceParameters.

        Limit the returned suppliers to those where a recorded change event occurred before this date    Change events include updates to supplier status, risk etc or when a company first appeared in your supply chain  # noqa: E501

        :param end_date: The end_date of this SupplierResourceParameters.  # noqa: E501
        :type: datetime
        """

        self._end_date = end_date

    @property
    def order_by(self):
        """Gets the order_by of this SupplierResourceParameters.  # noqa: E501

        Order the results  # noqa: E501

        :return: The order_by of this SupplierResourceParameters.  # noqa: E501
        :rtype: str
        """
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        """Sets the order_by of this SupplierResourceParameters.

        Order the results  # noqa: E501

        :param order_by: The order_by of this SupplierResourceParameters.  # noqa: E501
        :type: str
        """

        self._order_by = order_by

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
        if issubclass(SupplierResourceParameters, dict):
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
        if not isinstance(other, SupplierResourceParameters):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other