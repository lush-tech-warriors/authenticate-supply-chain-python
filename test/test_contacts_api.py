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
from authenticate_supply_chain.api.contacts_api import ContactsApi  # noqa: E501
from authenticate_supply_chain.rest import ApiException


class TestContactsApi(unittest.TestCase):
    """ContactsApi unit test stubs"""

    def setUp(self):
        self.api = ContactsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_contact(self):
        """Test case for create_contact

        Create a new contact  # noqa: E501
        """
        pass

    def test_create_contact_v2(self):
        """Test case for create_contact_v2

        Create a new contact  # noqa: E501
        """
        pass

    def test_get_company_contact(self):
        """Test case for get_company_contact

        Returns a specified contact  # noqa: E501
        """
        pass

    def test_get_company_contacts(self):
        """Test case for get_company_contacts

        Returns a list of all contacts meeting the request criteria  # noqa: E501
        """
        pass

    def test_get_contacts(self):
        """Test case for get_contacts

        Returns a list of contacts meeting the request criteria  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
