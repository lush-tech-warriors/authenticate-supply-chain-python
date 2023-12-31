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

class V1BlobBody1(object):
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
        'file': 'str',
        'storage_folder_path': 'str',
        'storage_account': 'StorageAccountEnum',
        'use_real_file_name': 'bool'
    }

    attribute_map = {
        'file': 'File',
        'storage_folder_path': 'StorageFolderPath',
        'storage_account': 'StorageAccount',
        'use_real_file_name': 'UseRealFileName'
    }

    def __init__(self, file=None, storage_folder_path=None, storage_account=None, use_real_file_name=None):  # noqa: E501
        """V1BlobBody1 - a model defined in Swagger"""  # noqa: E501
        self._file = None
        self._storage_folder_path = None
        self._storage_account = None
        self._use_real_file_name = None
        self.discriminator = None
        if file is not None:
            self.file = file
        if storage_folder_path is not None:
            self.storage_folder_path = storage_folder_path
        self.storage_account = storage_account
        if use_real_file_name is not None:
            self.use_real_file_name = use_real_file_name

    @property
    def file(self):
        """Gets the file of this V1BlobBody1.  # noqa: E501


        :return: The file of this V1BlobBody1.  # noqa: E501
        :rtype: str
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this V1BlobBody1.


        :param file: The file of this V1BlobBody1.  # noqa: E501
        :type: str
        """

        self._file = file

    @property
    def storage_folder_path(self):
        """Gets the storage_folder_path of this V1BlobBody1.  # noqa: E501


        :return: The storage_folder_path of this V1BlobBody1.  # noqa: E501
        :rtype: str
        """
        return self._storage_folder_path

    @storage_folder_path.setter
    def storage_folder_path(self, storage_folder_path):
        """Sets the storage_folder_path of this V1BlobBody1.


        :param storage_folder_path: The storage_folder_path of this V1BlobBody1.  # noqa: E501
        :type: str
        """

        self._storage_folder_path = storage_folder_path

    @property
    def storage_account(self):
        """Gets the storage_account of this V1BlobBody1.  # noqa: E501


        :return: The storage_account of this V1BlobBody1.  # noqa: E501
        :rtype: StorageAccountEnum
        """
        return self._storage_account

    @storage_account.setter
    def storage_account(self, storage_account):
        """Sets the storage_account of this V1BlobBody1.


        :param storage_account: The storage_account of this V1BlobBody1.  # noqa: E501
        :type: StorageAccountEnum
        """
        if storage_account is None:
            raise ValueError("Invalid value for `storage_account`, must not be `None`")  # noqa: E501

        self._storage_account = storage_account

    @property
    def use_real_file_name(self):
        """Gets the use_real_file_name of this V1BlobBody1.  # noqa: E501


        :return: The use_real_file_name of this V1BlobBody1.  # noqa: E501
        :rtype: bool
        """
        return self._use_real_file_name

    @use_real_file_name.setter
    def use_real_file_name(self, use_real_file_name):
        """Sets the use_real_file_name of this V1BlobBody1.


        :param use_real_file_name: The use_real_file_name of this V1BlobBody1.  # noqa: E501
        :type: bool
        """

        self._use_real_file_name = use_real_file_name

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
        if issubclass(V1BlobBody1, dict):
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
        if not isinstance(other, V1BlobBody1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
