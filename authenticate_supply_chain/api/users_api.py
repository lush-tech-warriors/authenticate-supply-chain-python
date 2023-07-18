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


class UsersApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_company_user(self, supplier_id, user_id, **kwargs):  # noqa: E501
        """Returns a specified user  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_company_user(supplier_id, user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str supplier_id: (required)
        :param str user_id: The unique identifier for the user to return (required)
        :return: UserDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_company_user_with_http_info(supplier_id, user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_company_user_with_http_info(supplier_id, user_id, **kwargs)  # noqa: E501
            return data

    def get_company_user_with_http_info(self, supplier_id, user_id, **kwargs):  # noqa: E501
        """Returns a specified user  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_company_user_with_http_info(supplier_id, user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str supplier_id: (required)
        :param str user_id: The unique identifier for the user to return (required)
        :return: UserDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['supplier_id', 'user_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_company_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'supplier_id' is set
        if ('supplier_id' not in params or
                params['supplier_id'] is None):
            raise ValueError("Missing the required parameter `supplier_id` when calling `get_company_user`")  # noqa: E501
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params or
                params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `get_company_user`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'supplier_id' in params:
            path_params['supplierId'] = params['supplier_id']  # noqa: E501
        if 'user_id' in params:
            path_params['userId'] = params['user_id']  # noqa: E501

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
            '/api/v1/Suppliers/{supplierId}/Users/{userId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UserDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_company_users(self, supplier_id, **kwargs):  # noqa: E501
        """Returns a list of all users meeting the request criteria  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_company_users(supplier_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str supplier_id: (required)
        :param list[str] user_ids:
        :param bool include_linked_users: Include users with active linked access to a company
        :param bool include_denied_users: Include users which have a latest status of denied
        :param str search_query:
        :param int page_number:
        :param int page_size:
        :param str order_by:
        :return: list[UserDto]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_company_users_with_http_info(supplier_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_company_users_with_http_info(supplier_id, **kwargs)  # noqa: E501
            return data

    def get_company_users_with_http_info(self, supplier_id, **kwargs):  # noqa: E501
        """Returns a list of all users meeting the request criteria  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_company_users_with_http_info(supplier_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str supplier_id: (required)
        :param list[str] user_ids:
        :param bool include_linked_users: Include users with active linked access to a company
        :param bool include_denied_users: Include users which have a latest status of denied
        :param str search_query:
        :param int page_number:
        :param int page_size:
        :param str order_by:
        :return: list[UserDto]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['supplier_id', 'user_ids', 'include_linked_users', 'include_denied_users', 'search_query', 'page_number', 'page_size', 'order_by']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_company_users" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'supplier_id' is set
        if ('supplier_id' not in params or
                params['supplier_id'] is None):
            raise ValueError("Missing the required parameter `supplier_id` when calling `get_company_users`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'supplier_id' in params:
            path_params['supplierId'] = params['supplier_id']  # noqa: E501

        query_params = []
        if 'user_ids' in params:
            query_params.append(('UserIds', params['user_ids']))  # noqa: E501
            collection_formats['UserIds'] = 'multi'  # noqa: E501
        if 'include_linked_users' in params:
            query_params.append(('IncludeLinkedUsers', params['include_linked_users']))  # noqa: E501
        if 'include_denied_users' in params:
            query_params.append(('IncludeDeniedUsers', params['include_denied_users']))  # noqa: E501
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
            '/api/v1/Suppliers/{supplierId}/Users', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[UserDto]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_users(self, **kwargs):  # noqa: E501
        """Returns a list of users meeting the request criteria  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_users(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] user_ids:
        :param bool include_linked_users: Include users with active linked access to a company
        :param bool include_denied_users: Include users which have a latest status of denied
        :param str search_query:
        :param int page_number:
        :param int page_size:
        :param str order_by:
        :return: list[UserDto]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_users_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_users_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_users_with_http_info(self, **kwargs):  # noqa: E501
        """Returns a list of users meeting the request criteria  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_users_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] user_ids:
        :param bool include_linked_users: Include users with active linked access to a company
        :param bool include_denied_users: Include users which have a latest status of denied
        :param str search_query:
        :param int page_number:
        :param int page_size:
        :param str order_by:
        :return: list[UserDto]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_ids', 'include_linked_users', 'include_denied_users', 'search_query', 'page_number', 'page_size', 'order_by']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_users" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_ids' in params:
            query_params.append(('UserIds', params['user_ids']))  # noqa: E501
            collection_formats['UserIds'] = 'multi'  # noqa: E501
        if 'include_linked_users' in params:
            query_params.append(('IncludeLinkedUsers', params['include_linked_users']))  # noqa: E501
        if 'include_denied_users' in params:
            query_params.append(('IncludeDeniedUsers', params['include_denied_users']))  # noqa: E501
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
            '/api/v1/Users', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[UserDto]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
