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
from authenticate_supply_chain.api.site_licences_api import SiteLicencesApi  # noqa: E501
from authenticate_supply_chain.rest import ApiException


class TestSiteLicencesApi(unittest.TestCase):
    """SiteLicencesApi unit test stubs"""

    def setUp(self):
        self.api = SiteLicencesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_api_v1_sites_site_id_licences_get(self):
        """Test case for api_v1_sites_site_id_licences_get

        Returns a list of licences for a site  # noqa: E501
        """
        pass

    def test_api_v1_sites_site_id_licences_licence_id_put(self):
        """Test case for api_v1_sites_site_id_licences_licence_id_put

        Fully update a site licence  # noqa: E501
        """
        pass

    def test_create_site_licence(self):
        """Test case for create_site_licence

        Create a site licence  # noqa: E501
        """
        pass

    def test_delete_site_licence(self):
        """Test case for delete_site_licence

        Delete a site licence  # noqa: E501
        """
        pass

    def test_patch_site_licence(self):
        """Test case for patch_site_licence

        Partially update a site licence. Only provided fields will be updated  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
