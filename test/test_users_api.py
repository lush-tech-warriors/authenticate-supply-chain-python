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
from authenticate_supply_chain.api.users_api import UsersApi  # noqa: E501
from authenticate_supply_chain.rest import ApiException


class TestUsersApi(unittest.TestCase):
    """UsersApi unit test stubs"""

    def setUp(self):
        self.api = UsersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_company_user(self):
        """Test case for get_company_user

        Returns a specified user  # noqa: E501
        """
        pass

    def test_get_company_users(self):
        """Test case for get_company_users

        Returns a list of all users meeting the request criteria  # noqa: E501
        """
        pass

    def test_get_users(self):
        """Test case for get_users

        Returns a list of users meeting the request criteria  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
