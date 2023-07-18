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

class Stream(object):
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
        'can_read': 'bool',
        'can_write': 'bool',
        'can_seek': 'bool',
        'can_timeout': 'bool',
        'length': 'int',
        'position': 'int',
        'read_timeout': 'int',
        'write_timeout': 'int'
    }

    attribute_map = {
        'can_read': 'canRead',
        'can_write': 'canWrite',
        'can_seek': 'canSeek',
        'can_timeout': 'canTimeout',
        'length': 'length',
        'position': 'position',
        'read_timeout': 'readTimeout',
        'write_timeout': 'writeTimeout'
    }

    def __init__(self, can_read=None, can_write=None, can_seek=None, can_timeout=None, length=None, position=None, read_timeout=None, write_timeout=None):  # noqa: E501
        """Stream - a model defined in Swagger"""  # noqa: E501
        self._can_read = None
        self._can_write = None
        self._can_seek = None
        self._can_timeout = None
        self._length = None
        self._position = None
        self._read_timeout = None
        self._write_timeout = None
        self.discriminator = None
        if can_read is not None:
            self.can_read = can_read
        if can_write is not None:
            self.can_write = can_write
        if can_seek is not None:
            self.can_seek = can_seek
        if can_timeout is not None:
            self.can_timeout = can_timeout
        if length is not None:
            self.length = length
        if position is not None:
            self.position = position
        if read_timeout is not None:
            self.read_timeout = read_timeout
        if write_timeout is not None:
            self.write_timeout = write_timeout

    @property
    def can_read(self):
        """Gets the can_read of this Stream.  # noqa: E501


        :return: The can_read of this Stream.  # noqa: E501
        :rtype: bool
        """
        return self._can_read

    @can_read.setter
    def can_read(self, can_read):
        """Sets the can_read of this Stream.


        :param can_read: The can_read of this Stream.  # noqa: E501
        :type: bool
        """

        self._can_read = can_read

    @property
    def can_write(self):
        """Gets the can_write of this Stream.  # noqa: E501


        :return: The can_write of this Stream.  # noqa: E501
        :rtype: bool
        """
        return self._can_write

    @can_write.setter
    def can_write(self, can_write):
        """Sets the can_write of this Stream.


        :param can_write: The can_write of this Stream.  # noqa: E501
        :type: bool
        """

        self._can_write = can_write

    @property
    def can_seek(self):
        """Gets the can_seek of this Stream.  # noqa: E501


        :return: The can_seek of this Stream.  # noqa: E501
        :rtype: bool
        """
        return self._can_seek

    @can_seek.setter
    def can_seek(self, can_seek):
        """Sets the can_seek of this Stream.


        :param can_seek: The can_seek of this Stream.  # noqa: E501
        :type: bool
        """

        self._can_seek = can_seek

    @property
    def can_timeout(self):
        """Gets the can_timeout of this Stream.  # noqa: E501


        :return: The can_timeout of this Stream.  # noqa: E501
        :rtype: bool
        """
        return self._can_timeout

    @can_timeout.setter
    def can_timeout(self, can_timeout):
        """Sets the can_timeout of this Stream.


        :param can_timeout: The can_timeout of this Stream.  # noqa: E501
        :type: bool
        """

        self._can_timeout = can_timeout

    @property
    def length(self):
        """Gets the length of this Stream.  # noqa: E501


        :return: The length of this Stream.  # noqa: E501
        :rtype: int
        """
        return self._length

    @length.setter
    def length(self, length):
        """Sets the length of this Stream.


        :param length: The length of this Stream.  # noqa: E501
        :type: int
        """

        self._length = length

    @property
    def position(self):
        """Gets the position of this Stream.  # noqa: E501


        :return: The position of this Stream.  # noqa: E501
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this Stream.


        :param position: The position of this Stream.  # noqa: E501
        :type: int
        """

        self._position = position

    @property
    def read_timeout(self):
        """Gets the read_timeout of this Stream.  # noqa: E501


        :return: The read_timeout of this Stream.  # noqa: E501
        :rtype: int
        """
        return self._read_timeout

    @read_timeout.setter
    def read_timeout(self, read_timeout):
        """Sets the read_timeout of this Stream.


        :param read_timeout: The read_timeout of this Stream.  # noqa: E501
        :type: int
        """

        self._read_timeout = read_timeout

    @property
    def write_timeout(self):
        """Gets the write_timeout of this Stream.  # noqa: E501


        :return: The write_timeout of this Stream.  # noqa: E501
        :rtype: int
        """
        return self._write_timeout

    @write_timeout.setter
    def write_timeout(self, write_timeout):
        """Sets the write_timeout of this Stream.


        :param write_timeout: The write_timeout of this Stream.  # noqa: E501
        :type: int
        """

        self._write_timeout = write_timeout

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
        if issubclass(Stream, dict):
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
        if not isinstance(other, Stream):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
