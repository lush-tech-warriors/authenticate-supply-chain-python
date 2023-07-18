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

class Operation(object):
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
        'operation_type': 'OperationType',
        'path': 'str',
        'op': 'str',
        '_from': 'str',
        'value': 'object'
    }

    attribute_map = {
        'operation_type': 'operationType',
        'path': 'path',
        'op': 'op',
        '_from': 'from',
        'value': 'value'
    }

    def __init__(self, operation_type=None, path=None, op=None, _from=None, value=None):  # noqa: E501
        """Operation - a model defined in Swagger"""  # noqa: E501
        self._operation_type = None
        self._path = None
        self._op = None
        self.__from = None
        self._value = None
        self.discriminator = None
        if operation_type is not None:
            self.operation_type = operation_type
        if path is not None:
            self.path = path
        if op is not None:
            self.op = op
        if _from is not None:
            self._from = _from
        if value is not None:
            self.value = value

    @property
    def operation_type(self):
        """Gets the operation_type of this Operation.  # noqa: E501


        :return: The operation_type of this Operation.  # noqa: E501
        :rtype: OperationType
        """
        return self._operation_type

    @operation_type.setter
    def operation_type(self, operation_type):
        """Sets the operation_type of this Operation.


        :param operation_type: The operation_type of this Operation.  # noqa: E501
        :type: OperationType
        """

        self._operation_type = operation_type

    @property
    def path(self):
        """Gets the path of this Operation.  # noqa: E501


        :return: The path of this Operation.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this Operation.


        :param path: The path of this Operation.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def op(self):
        """Gets the op of this Operation.  # noqa: E501


        :return: The op of this Operation.  # noqa: E501
        :rtype: str
        """
        return self._op

    @op.setter
    def op(self, op):
        """Sets the op of this Operation.


        :param op: The op of this Operation.  # noqa: E501
        :type: str
        """

        self._op = op

    @property
    def _from(self):
        """Gets the _from of this Operation.  # noqa: E501


        :return: The _from of this Operation.  # noqa: E501
        :rtype: str
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this Operation.


        :param _from: The _from of this Operation.  # noqa: E501
        :type: str
        """

        self.__from = _from

    @property
    def value(self):
        """Gets the value of this Operation.  # noqa: E501


        :return: The value of this Operation.  # noqa: E501
        :rtype: object
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this Operation.


        :param value: The value of this Operation.  # noqa: E501
        :type: object
        """

        self._value = value

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
        if issubclass(Operation, dict):
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
        if not isinstance(other, Operation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
