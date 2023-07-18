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
from authenticate_supply_chain.api.customer_links_api import CustomerLinksApi  # noqa: E501
from authenticate_supply_chain.rest import ApiException


class TestCustomerLinksApi(unittest.TestCase):
    """CustomerLinksApi unit test stubs"""

    def setUp(self):
        self.api = CustomerLinksApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_api_v1_customer_links_product_link_id_accept_post(self):
        """Test case for api_v1_customer_links_product_link_id_accept_post

        Accept an active product link request to your product (also accepts requests for the same product from the same customer)  # noqa: E501
        """
        pass

    def test_get_customer_product_link(self):
        """Test case for get_customer_product_link

        Returns a specified customer product link  # noqa: E501
        """
        pass

    def test_get_customer_product_link_for_product(self):
        """Test case for get_customer_product_link_for_product

        For the product with Id {productId}, return a specified customer product link  # noqa: E501
        """
        pass

    def test_get_customer_product_links(self):
        """Test case for get_customer_product_links

        Returns a list of all customer product links meeting the request criteria  # noqa: E501
        """
        pass

    def test_get_customer_product_links_for_product(self):
        """Test case for get_customer_product_links_for_product

        For the product with Id {productId}, return a list of all customer product links meeting the request criteria  # noqa: E501
        """
        pass

    def test_remove_customer_product_link_for_product(self):
        """Test case for remove_customer_product_link_for_product

        Remove an active product link request to your product  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
