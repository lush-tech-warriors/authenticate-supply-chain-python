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

class RawMaterialRecordDto(object):
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
        'reference': 'str',
        'received_date': 'datetime',
        'status': 'RawMaterialRecordStatusEnum',
        'description': 'str',
        'contract_number': 'str',
        'quantity_loaded': 'str',
        'quantity_received': 'str',
        'assignee_user_id': 'str',
        'site_ids': 'list[str]',
        'country_of_origin_ids': 'list[str]',
        'destination_country_ids': 'list[str]',
        'raw_material_record_documents': 'list[RawMaterialRecordDocumentDto]',
        'record_is_complete': 'bool',
        'raw_material_record_sugar_data': 'RawMaterialRecordSugarDataDto',
        'id': 'str',
        'created_by_company_id': 'str',
        'created_by_user_id': 'str',
        'utc_created_date': 'datetime',
        'raw_material_id': 'str',
        'completed_by_user_id': 'str',
        'utc_completed_date': 'datetime'
    }

    attribute_map = {
        'reference': 'reference',
        'received_date': 'receivedDate',
        'status': 'status',
        'description': 'description',
        'contract_number': 'contractNumber',
        'quantity_loaded': 'quantityLoaded',
        'quantity_received': 'quantityReceived',
        'assignee_user_id': 'assigneeUserId',
        'site_ids': 'siteIds',
        'country_of_origin_ids': 'countryOfOriginIds',
        'destination_country_ids': 'destinationCountryIds',
        'raw_material_record_documents': 'rawMaterialRecordDocuments',
        'record_is_complete': 'recordIsComplete',
        'raw_material_record_sugar_data': 'rawMaterialRecordSugarData',
        'id': 'id',
        'created_by_company_id': 'createdByCompanyId',
        'created_by_user_id': 'createdByUserId',
        'utc_created_date': 'utcCreatedDate',
        'raw_material_id': 'rawMaterialId',
        'completed_by_user_id': 'completedByUserId',
        'utc_completed_date': 'utcCompletedDate'
    }

    def __init__(self, reference=None, received_date=None, status=None, description=None, contract_number=None, quantity_loaded=None, quantity_received=None, assignee_user_id=None, site_ids=None, country_of_origin_ids=None, destination_country_ids=None, raw_material_record_documents=None, record_is_complete=None, raw_material_record_sugar_data=None, id=None, created_by_company_id=None, created_by_user_id=None, utc_created_date=None, raw_material_id=None, completed_by_user_id=None, utc_completed_date=None):  # noqa: E501
        """RawMaterialRecordDto - a model defined in Swagger"""  # noqa: E501
        self._reference = None
        self._received_date = None
        self._status = None
        self._description = None
        self._contract_number = None
        self._quantity_loaded = None
        self._quantity_received = None
        self._assignee_user_id = None
        self._site_ids = None
        self._country_of_origin_ids = None
        self._destination_country_ids = None
        self._raw_material_record_documents = None
        self._record_is_complete = None
        self._raw_material_record_sugar_data = None
        self._id = None
        self._created_by_company_id = None
        self._created_by_user_id = None
        self._utc_created_date = None
        self._raw_material_id = None
        self._completed_by_user_id = None
        self._utc_completed_date = None
        self.discriminator = None
        self.reference = reference
        self.received_date = received_date
        if status is not None:
            self.status = status
        if description is not None:
            self.description = description
        if contract_number is not None:
            self.contract_number = contract_number
        if quantity_loaded is not None:
            self.quantity_loaded = quantity_loaded
        if quantity_received is not None:
            self.quantity_received = quantity_received
        if assignee_user_id is not None:
            self.assignee_user_id = assignee_user_id
        if site_ids is not None:
            self.site_ids = site_ids
        if country_of_origin_ids is not None:
            self.country_of_origin_ids = country_of_origin_ids
        if destination_country_ids is not None:
            self.destination_country_ids = destination_country_ids
        if raw_material_record_documents is not None:
            self.raw_material_record_documents = raw_material_record_documents
        if record_is_complete is not None:
            self.record_is_complete = record_is_complete
        if raw_material_record_sugar_data is not None:
            self.raw_material_record_sugar_data = raw_material_record_sugar_data
        if id is not None:
            self.id = id
        if created_by_company_id is not None:
            self.created_by_company_id = created_by_company_id
        if created_by_user_id is not None:
            self.created_by_user_id = created_by_user_id
        if utc_created_date is not None:
            self.utc_created_date = utc_created_date
        if raw_material_id is not None:
            self.raw_material_id = raw_material_id
        if completed_by_user_id is not None:
            self.completed_by_user_id = completed_by_user_id
        if utc_completed_date is not None:
            self.utc_completed_date = utc_completed_date

    @property
    def reference(self):
        """Gets the reference of this RawMaterialRecordDto.  # noqa: E501

        Record reference  # noqa: E501

        :return: The reference of this RawMaterialRecordDto.  # noqa: E501
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this RawMaterialRecordDto.

        Record reference  # noqa: E501

        :param reference: The reference of this RawMaterialRecordDto.  # noqa: E501
        :type: str
        """
        if reference is None:
            raise ValueError("Invalid value for `reference`, must not be `None`")  # noqa: E501

        self._reference = reference

    @property
    def received_date(self):
        """Gets the received_date of this RawMaterialRecordDto.  # noqa: E501

        Date the raw material was received  # noqa: E501

        :return: The received_date of this RawMaterialRecordDto.  # noqa: E501
        :rtype: datetime
        """
        return self._received_date

    @received_date.setter
    def received_date(self, received_date):
        """Sets the received_date of this RawMaterialRecordDto.

        Date the raw material was received  # noqa: E501

        :param received_date: The received_date of this RawMaterialRecordDto.  # noqa: E501
        :type: datetime
        """
        if received_date is None:
            raise ValueError("Invalid value for `received_date`, must not be `None`")  # noqa: E501

        self._received_date = received_date

    @property
    def status(self):
        """Gets the status of this RawMaterialRecordDto.  # noqa: E501


        :return: The status of this RawMaterialRecordDto.  # noqa: E501
        :rtype: RawMaterialRecordStatusEnum
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this RawMaterialRecordDto.


        :param status: The status of this RawMaterialRecordDto.  # noqa: E501
        :type: RawMaterialRecordStatusEnum
        """

        self._status = status

    @property
    def description(self):
        """Gets the description of this RawMaterialRecordDto.  # noqa: E501

        Raw material record description  # noqa: E501

        :return: The description of this RawMaterialRecordDto.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this RawMaterialRecordDto.

        Raw material record description  # noqa: E501

        :param description: The description of this RawMaterialRecordDto.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def contract_number(self):
        """Gets the contract_number of this RawMaterialRecordDto.  # noqa: E501

        Raw material record contract number  # noqa: E501

        :return: The contract_number of this RawMaterialRecordDto.  # noqa: E501
        :rtype: str
        """
        return self._contract_number

    @contract_number.setter
    def contract_number(self, contract_number):
        """Sets the contract_number of this RawMaterialRecordDto.

        Raw material record contract number  # noqa: E501

        :param contract_number: The contract_number of this RawMaterialRecordDto.  # noqa: E501
        :type: str
        """

        self._contract_number = contract_number

    @property
    def quantity_loaded(self):
        """Gets the quantity_loaded of this RawMaterialRecordDto.  # noqa: E501

        Raw material record quantity loaded  # noqa: E501

        :return: The quantity_loaded of this RawMaterialRecordDto.  # noqa: E501
        :rtype: str
        """
        return self._quantity_loaded

    @quantity_loaded.setter
    def quantity_loaded(self, quantity_loaded):
        """Sets the quantity_loaded of this RawMaterialRecordDto.

        Raw material record quantity loaded  # noqa: E501

        :param quantity_loaded: The quantity_loaded of this RawMaterialRecordDto.  # noqa: E501
        :type: str
        """

        self._quantity_loaded = quantity_loaded

    @property
    def quantity_received(self):
        """Gets the quantity_received of this RawMaterialRecordDto.  # noqa: E501

        Raw material record quantity received  # noqa: E501

        :return: The quantity_received of this RawMaterialRecordDto.  # noqa: E501
        :rtype: str
        """
        return self._quantity_received

    @quantity_received.setter
    def quantity_received(self, quantity_received):
        """Sets the quantity_received of this RawMaterialRecordDto.

        Raw material record quantity received  # noqa: E501

        :param quantity_received: The quantity_received of this RawMaterialRecordDto.  # noqa: E501
        :type: str
        """

        self._quantity_received = quantity_received

    @property
    def assignee_user_id(self):
        """Gets the assignee_user_id of this RawMaterialRecordDto.  # noqa: E501

        Raw material record assignee user Id  # noqa: E501

        :return: The assignee_user_id of this RawMaterialRecordDto.  # noqa: E501
        :rtype: str
        """
        return self._assignee_user_id

    @assignee_user_id.setter
    def assignee_user_id(self, assignee_user_id):
        """Sets the assignee_user_id of this RawMaterialRecordDto.

        Raw material record assignee user Id  # noqa: E501

        :param assignee_user_id: The assignee_user_id of this RawMaterialRecordDto.  # noqa: E501
        :type: str
        """

        self._assignee_user_id = assignee_user_id

    @property
    def site_ids(self):
        """Gets the site_ids of this RawMaterialRecordDto.  # noqa: E501

        Raw material supplied site ids  # noqa: E501

        :return: The site_ids of this RawMaterialRecordDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._site_ids

    @site_ids.setter
    def site_ids(self, site_ids):
        """Sets the site_ids of this RawMaterialRecordDto.

        Raw material supplied site ids  # noqa: E501

        :param site_ids: The site_ids of this RawMaterialRecordDto.  # noqa: E501
        :type: list[str]
        """

        self._site_ids = site_ids

    @property
    def country_of_origin_ids(self):
        """Gets the country_of_origin_ids of this RawMaterialRecordDto.  # noqa: E501

        Raw material origin countryIds  # noqa: E501

        :return: The country_of_origin_ids of this RawMaterialRecordDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._country_of_origin_ids

    @country_of_origin_ids.setter
    def country_of_origin_ids(self, country_of_origin_ids):
        """Sets the country_of_origin_ids of this RawMaterialRecordDto.

        Raw material origin countryIds  # noqa: E501

        :param country_of_origin_ids: The country_of_origin_ids of this RawMaterialRecordDto.  # noqa: E501
        :type: list[str]
        """

        self._country_of_origin_ids = country_of_origin_ids

    @property
    def destination_country_ids(self):
        """Gets the destination_country_ids of this RawMaterialRecordDto.  # noqa: E501

        Raw material destination countryIds  # noqa: E501

        :return: The destination_country_ids of this RawMaterialRecordDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._destination_country_ids

    @destination_country_ids.setter
    def destination_country_ids(self, destination_country_ids):
        """Sets the destination_country_ids of this RawMaterialRecordDto.

        Raw material destination countryIds  # noqa: E501

        :param destination_country_ids: The destination_country_ids of this RawMaterialRecordDto.  # noqa: E501
        :type: list[str]
        """

        self._destination_country_ids = destination_country_ids

    @property
    def raw_material_record_documents(self):
        """Gets the raw_material_record_documents of this RawMaterialRecordDto.  # noqa: E501

        Raw material record documents  # noqa: E501

        :return: The raw_material_record_documents of this RawMaterialRecordDto.  # noqa: E501
        :rtype: list[RawMaterialRecordDocumentDto]
        """
        return self._raw_material_record_documents

    @raw_material_record_documents.setter
    def raw_material_record_documents(self, raw_material_record_documents):
        """Sets the raw_material_record_documents of this RawMaterialRecordDto.

        Raw material record documents  # noqa: E501

        :param raw_material_record_documents: The raw_material_record_documents of this RawMaterialRecordDto.  # noqa: E501
        :type: list[RawMaterialRecordDocumentDto]
        """

        self._raw_material_record_documents = raw_material_record_documents

    @property
    def record_is_complete(self):
        """Gets the record_is_complete of this RawMaterialRecordDto.  # noqa: E501

        Indicate if the record is complete  # noqa: E501

        :return: The record_is_complete of this RawMaterialRecordDto.  # noqa: E501
        :rtype: bool
        """
        return self._record_is_complete

    @record_is_complete.setter
    def record_is_complete(self, record_is_complete):
        """Sets the record_is_complete of this RawMaterialRecordDto.

        Indicate if the record is complete  # noqa: E501

        :param record_is_complete: The record_is_complete of this RawMaterialRecordDto.  # noqa: E501
        :type: bool
        """

        self._record_is_complete = record_is_complete

    @property
    def raw_material_record_sugar_data(self):
        """Gets the raw_material_record_sugar_data of this RawMaterialRecordDto.  # noqa: E501


        :return: The raw_material_record_sugar_data of this RawMaterialRecordDto.  # noqa: E501
        :rtype: RawMaterialRecordSugarDataDto
        """
        return self._raw_material_record_sugar_data

    @raw_material_record_sugar_data.setter
    def raw_material_record_sugar_data(self, raw_material_record_sugar_data):
        """Sets the raw_material_record_sugar_data of this RawMaterialRecordDto.


        :param raw_material_record_sugar_data: The raw_material_record_sugar_data of this RawMaterialRecordDto.  # noqa: E501
        :type: RawMaterialRecordSugarDataDto
        """

        self._raw_material_record_sugar_data = raw_material_record_sugar_data

    @property
    def id(self):
        """Gets the id of this RawMaterialRecordDto.  # noqa: E501

        The unique identifier of the raw material Record  # noqa: E501

        :return: The id of this RawMaterialRecordDto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RawMaterialRecordDto.

        The unique identifier of the raw material Record  # noqa: E501

        :param id: The id of this RawMaterialRecordDto.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def created_by_company_id(self):
        """Gets the created_by_company_id of this RawMaterialRecordDto.  # noqa: E501

        The Id for the company that created the record  # noqa: E501

        :return: The created_by_company_id of this RawMaterialRecordDto.  # noqa: E501
        :rtype: str
        """
        return self._created_by_company_id

    @created_by_company_id.setter
    def created_by_company_id(self, created_by_company_id):
        """Sets the created_by_company_id of this RawMaterialRecordDto.

        The Id for the company that created the record  # noqa: E501

        :param created_by_company_id: The created_by_company_id of this RawMaterialRecordDto.  # noqa: E501
        :type: str
        """

        self._created_by_company_id = created_by_company_id

    @property
    def created_by_user_id(self):
        """Gets the created_by_user_id of this RawMaterialRecordDto.  # noqa: E501

        The Id for the user that created the record  # noqa: E501

        :return: The created_by_user_id of this RawMaterialRecordDto.  # noqa: E501
        :rtype: str
        """
        return self._created_by_user_id

    @created_by_user_id.setter
    def created_by_user_id(self, created_by_user_id):
        """Sets the created_by_user_id of this RawMaterialRecordDto.

        The Id for the user that created the record  # noqa: E501

        :param created_by_user_id: The created_by_user_id of this RawMaterialRecordDto.  # noqa: E501
        :type: str
        """

        self._created_by_user_id = created_by_user_id

    @property
    def utc_created_date(self):
        """Gets the utc_created_date of this RawMaterialRecordDto.  # noqa: E501

        The datetime of when the record was created.  # noqa: E501

        :return: The utc_created_date of this RawMaterialRecordDto.  # noqa: E501
        :rtype: datetime
        """
        return self._utc_created_date

    @utc_created_date.setter
    def utc_created_date(self, utc_created_date):
        """Sets the utc_created_date of this RawMaterialRecordDto.

        The datetime of when the record was created.  # noqa: E501

        :param utc_created_date: The utc_created_date of this RawMaterialRecordDto.  # noqa: E501
        :type: datetime
        """

        self._utc_created_date = utc_created_date

    @property
    def raw_material_id(self):
        """Gets the raw_material_id of this RawMaterialRecordDto.  # noqa: E501

        The raw material Id for the record.  # noqa: E501

        :return: The raw_material_id of this RawMaterialRecordDto.  # noqa: E501
        :rtype: str
        """
        return self._raw_material_id

    @raw_material_id.setter
    def raw_material_id(self, raw_material_id):
        """Sets the raw_material_id of this RawMaterialRecordDto.

        The raw material Id for the record.  # noqa: E501

        :param raw_material_id: The raw_material_id of this RawMaterialRecordDto.  # noqa: E501
        :type: str
        """

        self._raw_material_id = raw_material_id

    @property
    def completed_by_user_id(self):
        """Gets the completed_by_user_id of this RawMaterialRecordDto.  # noqa: E501

        The id of the user that completed the record raw material Id for the record.  # noqa: E501

        :return: The completed_by_user_id of this RawMaterialRecordDto.  # noqa: E501
        :rtype: str
        """
        return self._completed_by_user_id

    @completed_by_user_id.setter
    def completed_by_user_id(self, completed_by_user_id):
        """Sets the completed_by_user_id of this RawMaterialRecordDto.

        The id of the user that completed the record raw material Id for the record.  # noqa: E501

        :param completed_by_user_id: The completed_by_user_id of this RawMaterialRecordDto.  # noqa: E501
        :type: str
        """

        self._completed_by_user_id = completed_by_user_id

    @property
    def utc_completed_date(self):
        """Gets the utc_completed_date of this RawMaterialRecordDto.  # noqa: E501

        The datetime of when the record was completed.  # noqa: E501

        :return: The utc_completed_date of this RawMaterialRecordDto.  # noqa: E501
        :rtype: datetime
        """
        return self._utc_completed_date

    @utc_completed_date.setter
    def utc_completed_date(self, utc_completed_date):
        """Sets the utc_completed_date of this RawMaterialRecordDto.

        The datetime of when the record was completed.  # noqa: E501

        :param utc_completed_date: The utc_completed_date of this RawMaterialRecordDto.  # noqa: E501
        :type: datetime
        """

        self._utc_completed_date = utc_completed_date

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
        if issubclass(RawMaterialRecordDto, dict):
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
        if not isinstance(other, RawMaterialRecordDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
