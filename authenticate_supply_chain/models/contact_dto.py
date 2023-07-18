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

class ContactDto(object):
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
        'first_name': 'str',
        'last_name': 'str',
        'job_role': 'str',
        'mobile': 'str',
        'fax': 'str',
        'telephone': 'str',
        'email': 'str'
    }

    attribute_map = {
        'id': 'id',
        'first_name': 'firstName',
        'last_name': 'lastName',
        'job_role': 'jobRole',
        'mobile': 'mobile',
        'fax': 'fax',
        'telephone': 'telephone',
        'email': 'email'
    }

    def __init__(self, id=None, first_name=None, last_name=None, job_role=None, mobile=None, fax=None, telephone=None, email=None):  # noqa: E501
        """ContactDto - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._first_name = None
        self._last_name = None
        self._job_role = None
        self._mobile = None
        self._fax = None
        self._telephone = None
        self._email = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if job_role is not None:
            self.job_role = job_role
        if mobile is not None:
            self.mobile = mobile
        if fax is not None:
            self.fax = fax
        if telephone is not None:
            self.telephone = telephone
        if email is not None:
            self.email = email

    @property
    def id(self):
        """Gets the id of this ContactDto.  # noqa: E501

        The unique identifier of the contact within the Authenticate platform  # noqa: E501

        :return: The id of this ContactDto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ContactDto.

        The unique identifier of the contact within the Authenticate platform  # noqa: E501

        :param id: The id of this ContactDto.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def first_name(self):
        """Gets the first_name of this ContactDto.  # noqa: E501

        The contact's first name  # noqa: E501

        :return: The first_name of this ContactDto.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this ContactDto.

        The contact's first name  # noqa: E501

        :param first_name: The first_name of this ContactDto.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this ContactDto.  # noqa: E501

        The contact's last name  # noqa: E501

        :return: The last_name of this ContactDto.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this ContactDto.

        The contact's last name  # noqa: E501

        :param last_name: The last_name of this ContactDto.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def job_role(self):
        """Gets the job_role of this ContactDto.  # noqa: E501

        The contact's job role  # noqa: E501

        :return: The job_role of this ContactDto.  # noqa: E501
        :rtype: str
        """
        return self._job_role

    @job_role.setter
    def job_role(self, job_role):
        """Sets the job_role of this ContactDto.

        The contact's job role  # noqa: E501

        :param job_role: The job_role of this ContactDto.  # noqa: E501
        :type: str
        """

        self._job_role = job_role

    @property
    def mobile(self):
        """Gets the mobile of this ContactDto.  # noqa: E501

        The contact's mobile telephone number  # noqa: E501

        :return: The mobile of this ContactDto.  # noqa: E501
        :rtype: str
        """
        return self._mobile

    @mobile.setter
    def mobile(self, mobile):
        """Sets the mobile of this ContactDto.

        The contact's mobile telephone number  # noqa: E501

        :param mobile: The mobile of this ContactDto.  # noqa: E501
        :type: str
        """

        self._mobile = mobile

    @property
    def fax(self):
        """Gets the fax of this ContactDto.  # noqa: E501

        The contact's fax number  # noqa: E501

        :return: The fax of this ContactDto.  # noqa: E501
        :rtype: str
        """
        return self._fax

    @fax.setter
    def fax(self, fax):
        """Sets the fax of this ContactDto.

        The contact's fax number  # noqa: E501

        :param fax: The fax of this ContactDto.  # noqa: E501
        :type: str
        """

        self._fax = fax

    @property
    def telephone(self):
        """Gets the telephone of this ContactDto.  # noqa: E501

        The contact's telephone number  # noqa: E501

        :return: The telephone of this ContactDto.  # noqa: E501
        :rtype: str
        """
        return self._telephone

    @telephone.setter
    def telephone(self, telephone):
        """Sets the telephone of this ContactDto.

        The contact's telephone number  # noqa: E501

        :param telephone: The telephone of this ContactDto.  # noqa: E501
        :type: str
        """

        self._telephone = telephone

    @property
    def email(self):
        """Gets the email of this ContactDto.  # noqa: E501

        The contact's email address  # noqa: E501

        :return: The email of this ContactDto.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this ContactDto.

        The contact's email address  # noqa: E501

        :param email: The email of this ContactDto.  # noqa: E501
        :type: str
        """

        self._email = email

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
        if issubclass(ContactDto, dict):
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
        if not isinstance(other, ContactDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
