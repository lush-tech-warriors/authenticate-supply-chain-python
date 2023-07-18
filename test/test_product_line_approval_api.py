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
from authenticate_supply_chain.api.product_line_approval_api import ProductLineApprovalApi  # noqa: E501
from authenticate_supply_chain.rest import ApiException


class TestProductLineApprovalApi(unittest.TestCase):
    """ProductLineApprovalApi unit test stubs"""

    def setUp(self):
        self.api = ProductLineApprovalApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_api_v1_product_line_approval_post(self):
        """Test case for api_v1_product_line_approval_post

        Save a new approval record for a product line  # noqa: E501
        """
        pass

    def test_api_v1_product_line_approval_product_line_approval_id_put(self):
        """Test case for api_v1_product_line_approval_product_line_approval_id_put

        Updates a product line approval record.  # noqa: E501
        """
        pass

    def test_api_v1_product_line_approval_product_line_id_get(self):
        """Test case for api_v1_product_line_approval_product_line_id_get

        Returns a list of all approval records for a product, meeting the request criteria  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()