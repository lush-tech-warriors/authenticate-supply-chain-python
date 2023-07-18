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
from authenticate_supply_chain.api.categories_api import CategoriesApi  # noqa: E501
from authenticate_supply_chain.rest import ApiException


class TestCategoriesApi(unittest.TestCase):
    """CategoriesApi unit test stubs"""

    def setUp(self):
        self.api = CategoriesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_api_v1_categories_post(self):
        """Test case for api_v1_categories_post

        Create a new Categories  # noqa: E501
        """
        pass

    def test_delete_category(self):
        """Test case for delete_category

        Delete a Categories. Only empty categories can be deleted. If the Categories contains products or other categories the delete will fail  # noqa: E501
        """
        pass

    def test_get_categories(self):
        """Test case for get_categories

        Returns a list of all categories meeting the request criteria  # noqa: E501
        """
        pass

    def test_get_category(self):
        """Test case for get_category

        Returns a specified Categories  # noqa: E501
        """
        pass

    def test_patch_category(self):
        """Test case for patch_category

        Partially update a Categories. Only provided fields will be updated  # noqa: E501
        """
        pass

    def test_update_category(self):
        """Test case for update_category

        Fully update a Categories. All elements must be supplied or fields will be updated to default values  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
