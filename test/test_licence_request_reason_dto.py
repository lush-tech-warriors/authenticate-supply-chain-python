# coding: utf-8

"""
    Authenticate Platform Supply Chain API

    Through this API you can Manage products and suppliers. Access to this API is restricted to authenticated users. Before accessing this API, first authenticate via the \"Account\" API. (https://uat-account.authenticateis.com/)  # noqa: E501

    OpenAPI spec version: 1.0
    Contact: platform-support@authenticateis.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import authenticate_supply_chain
from authenticate_supply_chain.models.licence_request_reason_dto import LicenceRequestReasonDto  # noqa: E501
from authenticate_supply_chain.rest import ApiException


class TestLicenceRequestReasonDto(unittest.TestCase):
    """LicenceRequestReasonDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testLicenceRequestReasonDto(self):
        """Test LicenceRequestReasonDto"""
        # FIXME: construct object with mandatory attributes with example values
        # model = authenticate_supply_chain.models.licence_request_reason_dto.LicenceRequestReasonDto()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
