# coding: utf-8

"""
    Authenticate Platform Supply Chain API

    Through this API you can Manage products and suppliers. Access to this API is restricted to authenticated users. Before accessing this API, first authenticate via the \"Account\" API. (https://uat-account.authenticateis.com/)  # noqa: E501

    OpenAPI spec version: 1.0
    Contact: platform-support@authenticateis.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from authenticate_supply_chain.api_client import ApiClient


class RawMaterialRelationshipsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def api_v1_raw_materials_raw_material_id_raw_material_relationships_get(self, raw_material_id, **kwargs):  # noqa: E501
        """Returns the raw material relationship for the given raw material  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v1_raw_materials_raw_material_id_raw_material_relationships_get(raw_material_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str raw_material_id: The unique identifier of the raw material (required)
        :return: RawMaterialRelationshipDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_v1_raw_materials_raw_material_id_raw_material_relationships_get_with_http_info(raw_material_id, **kwargs)  # noqa: E501
        else:
            (data) = self.api_v1_raw_materials_raw_material_id_raw_material_relationships_get_with_http_info(raw_material_id, **kwargs)  # noqa: E501
            return data

    def api_v1_raw_materials_raw_material_id_raw_material_relationships_get_with_http_info(self, raw_material_id, **kwargs):  # noqa: E501
        """Returns the raw material relationship for the given raw material  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v1_raw_materials_raw_material_id_raw_material_relationships_get_with_http_info(raw_material_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str raw_material_id: The unique identifier of the raw material (required)
        :return: RawMaterialRelationshipDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['raw_material_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v1_raw_materials_raw_material_id_raw_material_relationships_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'raw_material_id' is set
        if ('raw_material_id' not in params or
                params['raw_material_id'] is None):
            raise ValueError("Missing the required parameter `raw_material_id` when calling `api_v1_raw_materials_raw_material_id_raw_material_relationships_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'raw_material_id' in params:
            path_params['rawMaterialId'] = params['raw_material_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/RawMaterials/{rawMaterialId}/RawMaterialRelationships', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RawMaterialRelationshipDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def save_raw_material_relationship(self, raw_material_id, **kwargs):  # noqa: E501
        """Creates a raw material relationship for the given raw material id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.save_raw_material_relationship(raw_material_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str raw_material_id: The unique identifier of the raw material (required)
        :param RawMaterialRelationshipDto body:
        :return: RawMaterialRelationshipDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.save_raw_material_relationship_with_http_info(raw_material_id, **kwargs)  # noqa: E501
        else:
            (data) = self.save_raw_material_relationship_with_http_info(raw_material_id, **kwargs)  # noqa: E501
            return data

    def save_raw_material_relationship_with_http_info(self, raw_material_id, **kwargs):  # noqa: E501
        """Creates a raw material relationship for the given raw material id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.save_raw_material_relationship_with_http_info(raw_material_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str raw_material_id: The unique identifier of the raw material (required)
        :param RawMaterialRelationshipDto body:
        :return: RawMaterialRelationshipDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['raw_material_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method save_raw_material_relationship" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'raw_material_id' is set
        if ('raw_material_id' not in params or
                params['raw_material_id'] is None):
            raise ValueError("Missing the required parameter `raw_material_id` when calling `save_raw_material_relationship`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'raw_material_id' in params:
            path_params['rawMaterialId'] = params['raw_material_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/RawMaterials/{rawMaterialId}/RawMaterialRelationships', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RawMaterialRelationshipDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
