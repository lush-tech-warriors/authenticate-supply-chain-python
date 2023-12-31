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

class SupplierDto(object):
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
        'name': 'str',
        'registered_address': 'AddressDto',
        'company_types': 'list[OnsCompanyTypeDto]',
        'authenticate_member': 'bool',
        'is_farm': 'bool',
        'background': 'str',
        'phone': 'str',
        'web': 'str',
        'number_of_operating_sites': 'str',
        'number_of_employees': 'str',
        'turnover_currency_code': 'str',
        'estimated_turnover': 'str',
        'ownership': 'str',
        'established_year': 'int',
        'tiers': 'list[int]',
        'company_relationship_information': 'CompanyRelationshipDto',
        'company_functions': 'list[CompanyFunctionDto]',
        'supplier_codes': 'list[SupplierCodeDto]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'registered_address': 'registeredAddress',
        'company_types': 'companyTypes',
        'authenticate_member': 'authenticateMember',
        'is_farm': 'isFarm',
        'background': 'background',
        'phone': 'phone',
        'web': 'web',
        'number_of_operating_sites': 'numberOfOperatingSites',
        'number_of_employees': 'numberOfEmployees',
        'turnover_currency_code': 'turnoverCurrencyCode',
        'estimated_turnover': 'estimatedTurnover',
        'ownership': 'ownership',
        'established_year': 'establishedYear',
        'tiers': 'tiers',
        'company_relationship_information': 'companyRelationshipInformation',
        'company_functions': 'companyFunctions',
        'supplier_codes': 'supplierCodes'
    }

    def __init__(self, id=None, name=None, registered_address=None, company_types=None, authenticate_member=None, is_farm=None, background=None, phone=None, web=None, number_of_operating_sites=None, number_of_employees=None, turnover_currency_code=None, estimated_turnover=None, ownership=None, established_year=None, tiers=None, company_relationship_information=None, company_functions=None, supplier_codes=None):  # noqa: E501
        """SupplierDto - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._registered_address = None
        self._company_types = None
        self._authenticate_member = None
        self._is_farm = None
        self._background = None
        self._phone = None
        self._web = None
        self._number_of_operating_sites = None
        self._number_of_employees = None
        self._turnover_currency_code = None
        self._estimated_turnover = None
        self._ownership = None
        self._established_year = None
        self._tiers = None
        self._company_relationship_information = None
        self._company_functions = None
        self._supplier_codes = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if registered_address is not None:
            self.registered_address = registered_address
        if company_types is not None:
            self.company_types = company_types
        if authenticate_member is not None:
            self.authenticate_member = authenticate_member
        if is_farm is not None:
            self.is_farm = is_farm
        if background is not None:
            self.background = background
        if phone is not None:
            self.phone = phone
        if web is not None:
            self.web = web
        if number_of_operating_sites is not None:
            self.number_of_operating_sites = number_of_operating_sites
        if number_of_employees is not None:
            self.number_of_employees = number_of_employees
        if turnover_currency_code is not None:
            self.turnover_currency_code = turnover_currency_code
        if estimated_turnover is not None:
            self.estimated_turnover = estimated_turnover
        if ownership is not None:
            self.ownership = ownership
        if established_year is not None:
            self.established_year = established_year
        if tiers is not None:
            self.tiers = tiers
        if company_relationship_information is not None:
            self.company_relationship_information = company_relationship_information
        if company_functions is not None:
            self.company_functions = company_functions
        if supplier_codes is not None:
            self.supplier_codes = supplier_codes

    @property
    def id(self):
        """Gets the id of this SupplierDto.  # noqa: E501

        The unique identifier for the company  # noqa: E501

        :return: The id of this SupplierDto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SupplierDto.

        The unique identifier for the company  # noqa: E501

        :param id: The id of this SupplierDto.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this SupplierDto.  # noqa: E501

        The company name  # noqa: E501

        :return: The name of this SupplierDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SupplierDto.

        The company name  # noqa: E501

        :param name: The name of this SupplierDto.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def registered_address(self):
        """Gets the registered_address of this SupplierDto.  # noqa: E501


        :return: The registered_address of this SupplierDto.  # noqa: E501
        :rtype: AddressDto
        """
        return self._registered_address

    @registered_address.setter
    def registered_address(self, registered_address):
        """Sets the registered_address of this SupplierDto.


        :param registered_address: The registered_address of this SupplierDto.  # noqa: E501
        :type: AddressDto
        """

        self._registered_address = registered_address

    @property
    def company_types(self):
        """Gets the company_types of this SupplierDto.  # noqa: E501

        UK Office for National Statistics (ONS) Company types    A descriptor of the business function  # noqa: E501

        :return: The company_types of this SupplierDto.  # noqa: E501
        :rtype: list[OnsCompanyTypeDto]
        """
        return self._company_types

    @company_types.setter
    def company_types(self, company_types):
        """Sets the company_types of this SupplierDto.

        UK Office for National Statistics (ONS) Company types    A descriptor of the business function  # noqa: E501

        :param company_types: The company_types of this SupplierDto.  # noqa: E501
        :type: list[OnsCompanyTypeDto]
        """

        self._company_types = company_types

    @property
    def authenticate_member(self):
        """Gets the authenticate_member of this SupplierDto.  # noqa: E501

        Indicates whether the company is a member of the authenticate platform  # noqa: E501

        :return: The authenticate_member of this SupplierDto.  # noqa: E501
        :rtype: bool
        """
        return self._authenticate_member

    @authenticate_member.setter
    def authenticate_member(self, authenticate_member):
        """Sets the authenticate_member of this SupplierDto.

        Indicates whether the company is a member of the authenticate platform  # noqa: E501

        :param authenticate_member: The authenticate_member of this SupplierDto.  # noqa: E501
        :type: bool
        """

        self._authenticate_member = authenticate_member

    @property
    def is_farm(self):
        """Gets the is_farm of this SupplierDto.  # noqa: E501

        Indicates whether the company is a farm type  # noqa: E501

        :return: The is_farm of this SupplierDto.  # noqa: E501
        :rtype: bool
        """
        return self._is_farm

    @is_farm.setter
    def is_farm(self, is_farm):
        """Sets the is_farm of this SupplierDto.

        Indicates whether the company is a farm type  # noqa: E501

        :param is_farm: The is_farm of this SupplierDto.  # noqa: E501
        :type: bool
        """

        self._is_farm = is_farm

    @property
    def background(self):
        """Gets the background of this SupplierDto.  # noqa: E501

        General background information about the company  # noqa: E501

        :return: The background of this SupplierDto.  # noqa: E501
        :rtype: str
        """
        return self._background

    @background.setter
    def background(self, background):
        """Sets the background of this SupplierDto.

        General background information about the company  # noqa: E501

        :param background: The background of this SupplierDto.  # noqa: E501
        :type: str
        """

        self._background = background

    @property
    def phone(self):
        """Gets the phone of this SupplierDto.  # noqa: E501

        The company phone number  # noqa: E501

        :return: The phone of this SupplierDto.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this SupplierDto.

        The company phone number  # noqa: E501

        :param phone: The phone of this SupplierDto.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def web(self):
        """Gets the web of this SupplierDto.  # noqa: E501

        The company web address  # noqa: E501

        :return: The web of this SupplierDto.  # noqa: E501
        :rtype: str
        """
        return self._web

    @web.setter
    def web(self, web):
        """Sets the web of this SupplierDto.

        The company web address  # noqa: E501

        :param web: The web of this SupplierDto.  # noqa: E501
        :type: str
        """

        self._web = web

    @property
    def number_of_operating_sites(self):
        """Gets the number_of_operating_sites of this SupplierDto.  # noqa: E501

        The number of operating sites  # noqa: E501

        :return: The number_of_operating_sites of this SupplierDto.  # noqa: E501
        :rtype: str
        """
        return self._number_of_operating_sites

    @number_of_operating_sites.setter
    def number_of_operating_sites(self, number_of_operating_sites):
        """Sets the number_of_operating_sites of this SupplierDto.

        The number of operating sites  # noqa: E501

        :param number_of_operating_sites: The number_of_operating_sites of this SupplierDto.  # noqa: E501
        :type: str
        """

        self._number_of_operating_sites = number_of_operating_sites

    @property
    def number_of_employees(self):
        """Gets the number_of_employees of this SupplierDto.  # noqa: E501

        Number of employees  # noqa: E501

        :return: The number_of_employees of this SupplierDto.  # noqa: E501
        :rtype: str
        """
        return self._number_of_employees

    @number_of_employees.setter
    def number_of_employees(self, number_of_employees):
        """Sets the number_of_employees of this SupplierDto.

        Number of employees  # noqa: E501

        :param number_of_employees: The number_of_employees of this SupplierDto.  # noqa: E501
        :type: str
        """

        self._number_of_employees = number_of_employees

    @property
    def turnover_currency_code(self):
        """Gets the turnover_currency_code of this SupplierDto.  # noqa: E501

        The currency that the estimated turnover is recorded in  # noqa: E501

        :return: The turnover_currency_code of this SupplierDto.  # noqa: E501
        :rtype: str
        """
        return self._turnover_currency_code

    @turnover_currency_code.setter
    def turnover_currency_code(self, turnover_currency_code):
        """Sets the turnover_currency_code of this SupplierDto.

        The currency that the estimated turnover is recorded in  # noqa: E501

        :param turnover_currency_code: The turnover_currency_code of this SupplierDto.  # noqa: E501
        :type: str
        """

        self._turnover_currency_code = turnover_currency_code

    @property
    def estimated_turnover(self):
        """Gets the estimated_turnover of this SupplierDto.  # noqa: E501

        Estimated company annual turnover  # noqa: E501

        :return: The estimated_turnover of this SupplierDto.  # noqa: E501
        :rtype: str
        """
        return self._estimated_turnover

    @estimated_turnover.setter
    def estimated_turnover(self, estimated_turnover):
        """Sets the estimated_turnover of this SupplierDto.

        Estimated company annual turnover  # noqa: E501

        :param estimated_turnover: The estimated_turnover of this SupplierDto.  # noqa: E501
        :type: str
        """

        self._estimated_turnover = estimated_turnover

    @property
    def ownership(self):
        """Gets the ownership of this SupplierDto.  # noqa: E501

        Company ownership type  # noqa: E501

        :return: The ownership of this SupplierDto.  # noqa: E501
        :rtype: str
        """
        return self._ownership

    @ownership.setter
    def ownership(self, ownership):
        """Sets the ownership of this SupplierDto.

        Company ownership type  # noqa: E501

        :param ownership: The ownership of this SupplierDto.  # noqa: E501
        :type: str
        """

        self._ownership = ownership

    @property
    def established_year(self):
        """Gets the established_year of this SupplierDto.  # noqa: E501

        The year that the company was established  # noqa: E501

        :return: The established_year of this SupplierDto.  # noqa: E501
        :rtype: int
        """
        return self._established_year

    @established_year.setter
    def established_year(self, established_year):
        """Sets the established_year of this SupplierDto.

        The year that the company was established  # noqa: E501

        :param established_year: The established_year of this SupplierDto.  # noqa: E501
        :type: int
        """

        self._established_year = established_year

    @property
    def tiers(self):
        """Gets the tiers of this SupplierDto.  # noqa: E501

        Tiers at which this company appears in your supply chain(s)  # noqa: E501

        :return: The tiers of this SupplierDto.  # noqa: E501
        :rtype: list[int]
        """
        return self._tiers

    @tiers.setter
    def tiers(self, tiers):
        """Sets the tiers of this SupplierDto.

        Tiers at which this company appears in your supply chain(s)  # noqa: E501

        :param tiers: The tiers of this SupplierDto.  # noqa: E501
        :type: list[int]
        """

        self._tiers = tiers

    @property
    def company_relationship_information(self):
        """Gets the company_relationship_information of this SupplierDto.  # noqa: E501


        :return: The company_relationship_information of this SupplierDto.  # noqa: E501
        :rtype: CompanyRelationshipDto
        """
        return self._company_relationship_information

    @company_relationship_information.setter
    def company_relationship_information(self, company_relationship_information):
        """Sets the company_relationship_information of this SupplierDto.


        :param company_relationship_information: The company_relationship_information of this SupplierDto.  # noqa: E501
        :type: CompanyRelationshipDto
        """

        self._company_relationship_information = company_relationship_information

    @property
    def company_functions(self):
        """Gets the company_functions of this SupplierDto.  # noqa: E501

        The function(s) that the supplier provides to your company  # noqa: E501

        :return: The company_functions of this SupplierDto.  # noqa: E501
        :rtype: list[CompanyFunctionDto]
        """
        return self._company_functions

    @company_functions.setter
    def company_functions(self, company_functions):
        """Sets the company_functions of this SupplierDto.

        The function(s) that the supplier provides to your company  # noqa: E501

        :param company_functions: The company_functions of this SupplierDto.  # noqa: E501
        :type: list[CompanyFunctionDto]
        """

        self._company_functions = company_functions

    @property
    def supplier_codes(self):
        """Gets the supplier_codes of this SupplierDto.  # noqa: E501

        One or more codes, assigned by you, that uniquely identify this supplier.  # noqa: E501

        :return: The supplier_codes of this SupplierDto.  # noqa: E501
        :rtype: list[SupplierCodeDto]
        """
        return self._supplier_codes

    @supplier_codes.setter
    def supplier_codes(self, supplier_codes):
        """Sets the supplier_codes of this SupplierDto.

        One or more codes, assigned by you, that uniquely identify this supplier.  # noqa: E501

        :param supplier_codes: The supplier_codes of this SupplierDto.  # noqa: E501
        :type: list[SupplierCodeDto]
        """

        self._supplier_codes = supplier_codes

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
        if issubclass(SupplierDto, dict):
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
        if not isinstance(other, SupplierDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
