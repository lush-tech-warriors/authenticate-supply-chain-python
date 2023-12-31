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


class OnsCompanyTypesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_company_type(self, ons_company_type_id, **kwargs):  # noqa: E501
        """Returns a specified ONS company type  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_company_type(ons_company_type_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ons_company_type_id: The unique identifier for the company type to return (required)
        :return: OnsCompanyTypeDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_company_type_with_http_info(ons_company_type_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_company_type_with_http_info(ons_company_type_id, **kwargs)  # noqa: E501
            return data

    def get_company_type_with_http_info(self, ons_company_type_id, **kwargs):  # noqa: E501
        """Returns a specified ONS company type  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_company_type_with_http_info(ons_company_type_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ons_company_type_id: The unique identifier for the company type to return (required)
        :return: OnsCompanyTypeDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['ons_company_type_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_company_type" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'ons_company_type_id' is set
        if ('ons_company_type_id' not in params or
                params['ons_company_type_id'] is None):
            raise ValueError("Missing the required parameter `ons_company_type_id` when calling `get_company_type`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'ons_company_type_id' in params:
            path_params['onsCompanyTypeId'] = params['ons_company_type_id']  # noqa: E501

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
            '/api/v1/OnsCompanyTypes/{onsCompanyTypeId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OnsCompanyTypeDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_company_types(self, **kwargs):  # noqa: E501
        """Returns a list of all ONS company types meeting the request criteria  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_company_types(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str search_query:
        :param int page_number:
        :param int page_size:
        :param str order_by:
        :return: list[OnsCompanyTypeDto]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_company_types_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_company_types_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_company_types_with_http_info(self, **kwargs):  # noqa: E501
        """Returns a list of all ONS company types meeting the request criteria  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_company_types_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str search_query:
        :param int page_number:
        :param int page_size:
        :param str order_by:
        :return: list[OnsCompanyTypeDto]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['search_query', 'page_number', 'page_size', 'order_by']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_company_types" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

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
            '/api/v1/OnsCompanyTypes', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[OnsCompanyTypeDto]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_company_types_for_sector(self, ons_sector_id, **kwargs):  # noqa: E501
        """Returns a list of all ONS company types meeting the request criteria for a give ONS sector  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_company_types_for_sector(ons_sector_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ons_sector_id: (required)
        :param str search_query:
        :param int page_number:
        :param int page_size:
        :param str order_by:
        :return: list[OnsCompanyTypeDto]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_company_types_for_sector_with_http_info(ons_sector_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_company_types_for_sector_with_http_info(ons_sector_id, **kwargs)  # noqa: E501
            return data

    def get_company_types_for_sector_with_http_info(self, ons_sector_id, **kwargs):  # noqa: E501
        """Returns a list of all ONS company types meeting the request criteria for a give ONS sector  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_company_types_for_sector_with_http_info(ons_sector_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ons_sector_id: (required)
        :param str search_query:
        :param int page_number:
        :param int page_size:
        :param str order_by:
        :return: list[OnsCompanyTypeDto]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['ons_sector_id', 'search_query', 'page_number', 'page_size', 'order_by']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_company_types_for_sector" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'ons_sector_id' is set
        if ('ons_sector_id' not in params or
                params['ons_sector_id'] is None):
            raise ValueError("Missing the required parameter `ons_sector_id` when calling `get_company_types_for_sector`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'ons_sector_id' in params:
            path_params['onsSectorId'] = params['ons_sector_id']  # noqa: E501

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
            '/api/v1/OnsSectors/{onsSectorId}/OnsCompanyTypes', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[OnsCompanyTypeDto]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_ons_sectors(self, **kwargs):  # noqa: E501
        """Returns a list of all ONS business sectors meeting the request criteria  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_ons_sectors(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str search_query:
        :param int page_number:
        :param int page_size:
        :param str order_by:
        :return: list[OnsSectorDto]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_ons_sectors_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_ons_sectors_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_ons_sectors_with_http_info(self, **kwargs):  # noqa: E501
        """Returns a list of all ONS business sectors meeting the request criteria  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_ons_sectors_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str search_query:
        :param int page_number:
        :param int page_size:
        :param str order_by:
        :return: list[OnsSectorDto]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['search_query', 'page_number', 'page_size', 'order_by']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_ons_sectors" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

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
            '/api/v1/OnsSectors', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[OnsSectorDto]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
