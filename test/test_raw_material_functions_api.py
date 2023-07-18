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
from authenticate_supply_chain.api.raw_material_functions_api import RawMaterialFunctionsApi  # noqa: E501
from authenticate_supply_chain.rest import ApiException


class TestRawMaterialFunctionsApi(unittest.TestCase):
    """RawMaterialFunctionsApi unit test stubs"""

    def setUp(self):
        self.api = RawMaterialFunctionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_api_v1_raw_materials_raw_material_id_raw_material_functions_get(self):
        """Test case for api_v1_raw_materials_raw_material_id_raw_material_functions_get

        Returns a material function for a given raw material  # noqa: E501
        """
        pass

    def test_list_functions(self):
        """Test case for list_functions

        Returns a list of raw material functions  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
