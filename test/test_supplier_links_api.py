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
from authenticate_supply_chain.api.supplier_links_api import SupplierLinksApi  # noqa: E501
from authenticate_supply_chain.rest import ApiException


class TestSupplierLinksApi(unittest.TestCase):
    """SupplierLinksApi unit test stubs"""

    def setUp(self):
        self.api = SupplierLinksApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_supplier_product_link(self):
        """Test case for create_supplier_product_link

        Create a new product link request  # noqa: E501
        """
        pass

    def test_create_supplier_product_link_for_product(self):
        """Test case for create_supplier_product_link_for_product

        Create a new product link request  # noqa: E501
        """
        pass

    def test_delete_supplier_product_link(self):
        """Test case for delete_supplier_product_link

        Delete a product link. Active product links (Pending, Accepted) cannot be deleted  # noqa: E501
        """
        pass

    def test_delete_supplier_product_link_for_product(self):
        """Test case for delete_supplier_product_link_for_product

        Delete a product link. Active product links (Pending, Accepted) cannot be deleted  # noqa: E501
        """
        pass

    def test_get_supplier_product_link(self):
        """Test case for get_supplier_product_link

        Returns a specified supplier product link  # noqa: E501
        """
        pass

    def test_get_supplier_product_link_for_product(self):
        """Test case for get_supplier_product_link_for_product

        For the product with Id {productId}, return a specified supplier product link  # noqa: E501
        """
        pass

    def test_get_supplier_product_links(self):
        """Test case for get_supplier_product_links

        Returns a list of all supplier product links meeting the request criteria  # noqa: E501
        """
        pass

    def test_get_supplier_product_links_for_product(self):
        """Test case for get_supplier_product_links_for_product

        For the product with Id {productId}, return a list of all supplier product links for meeting the request criteria  # noqa: E501
        """
        pass

    def test_remove_supplier_product_link(self):
        """Test case for remove_supplier_product_link

        Remove an active product link request  # noqa: E501
        """
        pass

    def test_remove_supplier_product_link_for_product(self):
        """Test case for remove_supplier_product_link_for_product

        Remove an active product link request  # noqa: E501
        """
        pass

    def test_rescind_supplier_product_link(self):
        """Test case for rescind_supplier_product_link

        Rescind an active product link request  # noqa: E501
        """
        pass

    def test_rescind_supplier_product_link_for_product(self):
        """Test case for rescind_supplier_product_link_for_product

        Rescind an active product link request  # noqa: E501
        """
        pass

    def test_update_supplier_product_link(self):
        """Test case for update_supplier_product_link

        Update a product link  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
