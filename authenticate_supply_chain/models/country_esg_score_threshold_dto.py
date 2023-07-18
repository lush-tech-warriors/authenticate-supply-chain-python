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

class CountryEsgScoreThresholdDto(object):
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
        'risk_points': 'int',
        'threshold': 'str'
    }

    attribute_map = {
        'risk_points': 'riskPoints',
        'threshold': 'threshold'
    }

    def __init__(self, risk_points=None, threshold=None):  # noqa: E501
        """CountryEsgScoreThresholdDto - a model defined in Swagger"""  # noqa: E501
        self._risk_points = None
        self._threshold = None
        self.discriminator = None
        if risk_points is not None:
            self.risk_points = risk_points
        if threshold is not None:
            self.threshold = threshold

    @property
    def risk_points(self):
        """Gets the risk_points of this CountryEsgScoreThresholdDto.  # noqa: E501

        the risk points cored for the threshold.  # noqa: E501

        :return: The risk_points of this CountryEsgScoreThresholdDto.  # noqa: E501
        :rtype: int
        """
        return self._risk_points

    @risk_points.setter
    def risk_points(self, risk_points):
        """Sets the risk_points of this CountryEsgScoreThresholdDto.

        the risk points cored for the threshold.  # noqa: E501

        :param risk_points: The risk_points of this CountryEsgScoreThresholdDto.  # noqa: E501
        :type: int
        """

        self._risk_points = risk_points

    @property
    def threshold(self):
        """Gets the threshold of this CountryEsgScoreThresholdDto.  # noqa: E501

        The risk threshold.  # noqa: E501

        :return: The threshold of this CountryEsgScoreThresholdDto.  # noqa: E501
        :rtype: str
        """
        return self._threshold

    @threshold.setter
    def threshold(self, threshold):
        """Sets the threshold of this CountryEsgScoreThresholdDto.

        The risk threshold.  # noqa: E501

        :param threshold: The threshold of this CountryEsgScoreThresholdDto.  # noqa: E501
        :type: str
        """

        self._threshold = threshold

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
        if issubclass(CountryEsgScoreThresholdDto, dict):
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
        if not isinstance(other, CountryEsgScoreThresholdDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
