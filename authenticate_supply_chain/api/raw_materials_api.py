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


class RawMaterialsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def api_v1_raw_materials_raw_material_id_get(self, raw_material_id, **kwargs):  # noqa: E501
        """Returns a specified raw material  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v1_raw_materials_raw_material_id_get(raw_material_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str raw_material_id: The unique identifier of the raw material to return (required)
        :return: list[RawMaterialDto]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_v1_raw_materials_raw_material_id_get_with_http_info(raw_material_id, **kwargs)  # noqa: E501
        else:
            (data) = self.api_v1_raw_materials_raw_material_id_get_with_http_info(raw_material_id, **kwargs)  # noqa: E501
            return data

    def api_v1_raw_materials_raw_material_id_get_with_http_info(self, raw_material_id, **kwargs):  # noqa: E501
        """Returns a specified raw material  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v1_raw_materials_raw_material_id_get_with_http_info(raw_material_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str raw_material_id: The unique identifier of the raw material to return (required)
        :return: list[RawMaterialDto]
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
                    " to method api_v1_raw_materials_raw_material_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'raw_material_id' is set
        if ('raw_material_id' not in params or
                params['raw_material_id'] is None):
            raise ValueError("Missing the required parameter `raw_material_id` when calling `api_v1_raw_materials_raw_material_id_get`")  # noqa: E501

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
            '/api/v1/RawMaterials/{rawMaterialId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[RawMaterialDto]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_v1_raw_materials_raw_material_id_patch(self, raw_material_id, **kwargs):  # noqa: E501
        """Partially update a raw material. Only provided fields will be updated  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v1_raw_materials_raw_material_id_patch(raw_material_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str raw_material_id: (required)
        :param list[Operation] body:
        :return: ProductDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_v1_raw_materials_raw_material_id_patch_with_http_info(raw_material_id, **kwargs)  # noqa: E501
        else:
            (data) = self.api_v1_raw_materials_raw_material_id_patch_with_http_info(raw_material_id, **kwargs)  # noqa: E501
            return data

    def api_v1_raw_materials_raw_material_id_patch_with_http_info(self, raw_material_id, **kwargs):  # noqa: E501
        """Partially update a raw material. Only provided fields will be updated  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v1_raw_materials_raw_material_id_patch_with_http_info(raw_material_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str raw_material_id: (required)
        :param list[Operation] body:
        :return: ProductDto
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
                    " to method api_v1_raw_materials_raw_material_id_patch" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'raw_material_id' is set
        if ('raw_material_id' not in params or
                params['raw_material_id'] is None):
            raise ValueError("Missing the required parameter `raw_material_id` when calling `api_v1_raw_materials_raw_material_id_patch`")  # noqa: E501

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
            ['application/json-patch+json', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/RawMaterials/{rawMaterialId}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ProductDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_raw_materials(self, **kwargs):  # noqa: E501
        """Returns a list of Raw materials  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_raw_materials(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] raw_material_ids:
        :param str supplier_id:
        :param str search_query:
        :param int page_number:
        :param int page_size:
        :param str order_by:
        :return: list[RawMaterialDto]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_raw_materials_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_raw_materials_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_raw_materials_with_http_info(self, **kwargs):  # noqa: E501
        """Returns a list of Raw materials  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_raw_materials_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] raw_material_ids:
        :param str supplier_id:
        :param str search_query:
        :param int page_number:
        :param int page_size:
        :param str order_by:
        :return: list[RawMaterialDto]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['raw_material_ids', 'supplier_id', 'search_query', 'page_number', 'page_size', 'order_by']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_raw_materials" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'raw_material_ids' in params:
            query_params.append(('RawMaterialIds', params['raw_material_ids']))  # noqa: E501
            collection_formats['RawMaterialIds'] = 'multi'  # noqa: E501
        if 'supplier_id' in params:
            query_params.append(('SupplierId', params['supplier_id']))  # noqa: E501
        if 'search_query' in params:
            query_params.append(('SearchQuery', params['search_query']))  # noqa: E501
        if 'page_number' in params:
            query_params.append(('PageNumber', params['page_number']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('PageSize', params['page_size']))  # noqa: E501
        if 'order_by' in params:
            query_params.append(('OrderBy', params['order_by']))  # noqa: E501

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
            '/api/v1/RawMaterials', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[RawMaterialDto]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
