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


class DeclaredSupplyChainApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_declared_supply_chain(self, top_level_product_id, **kwargs):  # noqa: E501
        """Create a new Declared Supply Chain  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_declared_supply_chain(top_level_product_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str top_level_product_id: (required)
        :param DeclaredSupplyChainForCreationDto body:
        :return: DeclaredSupplyChainDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_declared_supply_chain_with_http_info(top_level_product_id, **kwargs)  # noqa: E501
        else:
            (data) = self.create_declared_supply_chain_with_http_info(top_level_product_id, **kwargs)  # noqa: E501
            return data

    def create_declared_supply_chain_with_http_info(self, top_level_product_id, **kwargs):  # noqa: E501
        """Create a new Declared Supply Chain  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_declared_supply_chain_with_http_info(top_level_product_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str top_level_product_id: (required)
        :param DeclaredSupplyChainForCreationDto body:
        :return: DeclaredSupplyChainDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['top_level_product_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_declared_supply_chain" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'top_level_product_id' is set
        if ('top_level_product_id' not in params or
                params['top_level_product_id'] is None):
            raise ValueError("Missing the required parameter `top_level_product_id` when calling `create_declared_supply_chain`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'top_level_product_id' in params:
            path_params['topLevelProductId'] = params['top_level_product_id']  # noqa: E501

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
            '/api/v1/DeclaredSupplyChain/{topLevelProductId}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeclaredSupplyChainDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_declared_supply_chain(self, top_level_product_id, **kwargs):  # noqa: E501
        """Returns the declared supply chain for a given top level product id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_declared_supply_chain(top_level_product_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str top_level_product_id: (required)
        :param str search_query:
        :param int page_number:
        :param int page_size:
        :param str order_by:
        :return: list[DeclaredSupplyChainDto]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_declared_supply_chain_with_http_info(top_level_product_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_declared_supply_chain_with_http_info(top_level_product_id, **kwargs)  # noqa: E501
            return data

    def get_declared_supply_chain_with_http_info(self, top_level_product_id, **kwargs):  # noqa: E501
        """Returns the declared supply chain for a given top level product id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_declared_supply_chain_with_http_info(top_level_product_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str top_level_product_id: (required)
        :param str search_query:
        :param int page_number:
        :param int page_size:
        :param str order_by:
        :return: list[DeclaredSupplyChainDto]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['top_level_product_id', 'search_query', 'page_number', 'page_size', 'order_by']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_declared_supply_chain" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'top_level_product_id' is set
        if ('top_level_product_id' not in params or
                params['top_level_product_id'] is None):
            raise ValueError("Missing the required parameter `top_level_product_id` when calling `get_declared_supply_chain`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'top_level_product_id' in params:
            path_params['topLevelProductId'] = params['top_level_product_id']  # noqa: E501

        query_params = []
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
            '/api/v1/DeclaredSupplyChain/{topLevelProductId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[DeclaredSupplyChainDto]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_declared_supply_chain(self, declared_supply_chain_id, **kwargs):  # noqa: E501
        """Update a Declared Supply Chain  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_declared_supply_chain(declared_supply_chain_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str declared_supply_chain_id: (required)
        :param DeclaredSupplyChainForUpdateDto body:
        :return: DeclaredSupplyChainDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_declared_supply_chain_with_http_info(declared_supply_chain_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_declared_supply_chain_with_http_info(declared_supply_chain_id, **kwargs)  # noqa: E501
            return data

    def update_declared_supply_chain_with_http_info(self, declared_supply_chain_id, **kwargs):  # noqa: E501
        """Update a Declared Supply Chain  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_declared_supply_chain_with_http_info(declared_supply_chain_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str declared_supply_chain_id: (required)
        :param DeclaredSupplyChainForUpdateDto body:
        :return: DeclaredSupplyChainDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['declared_supply_chain_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_declared_supply_chain" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'declared_supply_chain_id' is set
        if ('declared_supply_chain_id' not in params or
                params['declared_supply_chain_id'] is None):
            raise ValueError("Missing the required parameter `declared_supply_chain_id` when calling `update_declared_supply_chain`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'declared_supply_chain_id' in params:
            path_params['declaredSupplyChainId'] = params['declared_supply_chain_id']  # noqa: E501

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
            '/api/v1/DeclaredSupplyChain/{declaredSupplyChainId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeclaredSupplyChainDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
