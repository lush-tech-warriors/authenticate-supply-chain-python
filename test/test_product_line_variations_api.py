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
from authenticate_supply_chain.api.product_line_variations_api import ProductLineVariationsApi  # noqa: E501
from authenticate_supply_chain.rest import ApiException


class TestProductLineVariationsApi(unittest.TestCase):
    """ProductLineVariationsApi unit test stubs"""

    def setUp(self):
        self.api = ProductLineVariationsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_api_v1_product_line_variations_product_line_variation_id_delete(self):
        """Test case for api_v1_product_line_variations_product_line_variation_id_delete

        Delete a product line variation  # noqa: E501
        """
        pass

    def test_api_v1_product_line_variations_product_line_variation_id_put(self):
        """Test case for api_v1_product_line_variations_product_line_variation_id_put

        Fully update a product line variation. All elements must be supplied or fields will be updated to default values  # noqa: E501
        """
        pass

    def test_api_v1_product_lines_product_line_id_product_line_variations_post(self):
        """Test case for api_v1_product_lines_product_line_id_product_line_variations_post

        Create a new product line variation.  # noqa: E501
        """
        pass

    def test_list(self):
        """Test case for list

        Returns a list of all variations associated with your company's product lines.  # noqa: E501
        """
        pass

    def test_list_by_product_line(self):
        """Test case for list_by_product_line

        Returns a list of all variations associated with a product line.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
