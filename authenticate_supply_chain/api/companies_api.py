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


class CompaniesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def api_v1_companies_post(self, **kwargs):  # noqa: E501
        """Create a new Companies  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v1_companies_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CompanyForCreationDto body:
        :return: CompanyDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_v1_companies_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.api_v1_companies_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def api_v1_companies_post_with_http_info(self, **kwargs):  # noqa: E501
        """Create a new Companies  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v1_companies_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CompanyForCreationDto body:
        :return: CompanyDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v1_companies_post" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

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
            '/api/v1/Companies', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CompanyDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_companies(self, **kwargs):  # noqa: E501
        """Returns a list of all Companies meeting the request criteria  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_companies(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str country: Filter supplier by country
        :param str postcode: Filter supplier by postcode
        :param bool authenticate_member: Filter by whether the company is a member of the authenticate platform or not
        :param str company_type: Filter by ONS Company Type
        :param list[str] company_ids: Filter by list of company id's
        :param list[str] supplier_codes: Filter by supplier codes
        :param list[str] licence_numbers: Filter by licence numbers
        :param str search_query:
        :param int page_number:
        :param int page_size:
        :param str order_by:
        :return: list[CompanyDto]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_companies_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_companies_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_companies_with_http_info(self, **kwargs):  # noqa: E501
        """Returns a list of all Companies meeting the request criteria  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_companies_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str country: Filter supplier by country
        :param str postcode: Filter supplier by postcode
        :param bool authenticate_member: Filter by whether the company is a member of the authenticate platform or not
        :param str company_type: Filter by ONS Company Type
        :param list[str] company_ids: Filter by list of company id's
        :param list[str] supplier_codes: Filter by supplier codes
        :param list[str] licence_numbers: Filter by licence numbers
        :param str search_query:
        :param int page_number:
        :param int page_size:
        :param str order_by:
        :return: list[CompanyDto]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['country', 'postcode', 'authenticate_member', 'company_type', 'company_ids', 'supplier_codes', 'licence_numbers', 'search_query', 'page_number', 'page_size', 'order_by']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_companies" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'country' in params:
            query_params.append(('Country', params['country']))  # noqa: E501
        if 'postcode' in params:
            query_params.append(('Postcode', params['postcode']))  # noqa: E501
        if 'authenticate_member' in params:
            query_params.append(('AuthenticateMember', params['authenticate_member']))  # noqa: E501
        if 'company_type' in params:
            query_params.append(('CompanyType', params['company_type']))  # noqa: E501
        if 'company_ids' in params:
            query_params.append(('CompanyIds', params['company_ids']))  # noqa: E501
            collection_formats['CompanyIds'] = 'multi'  # noqa: E501
        if 'supplier_codes' in params:
            query_params.append(('SupplierCodes', params['supplier_codes']))  # noqa: E501
            collection_formats['SupplierCodes'] = 'multi'  # noqa: E501
        if 'licence_numbers' in params:
            query_params.append(('LicenceNumbers', params['licence_numbers']))  # noqa: E501
            collection_formats['LicenceNumbers'] = 'multi'  # noqa: E501
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
            '/api/v1/Companies', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[CompanyDto]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_company(self, company_id, **kwargs):  # noqa: E501
        """Returns a specified Companies  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_company(company_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str company_id: The unique identifier for the Companies to return (required)
        :return: CompanyDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_company_with_http_info(company_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_company_with_http_info(company_id, **kwargs)  # noqa: E501
            return data

    def get_company_with_http_info(self, company_id, **kwargs):  # noqa: E501
        """Returns a specified Companies  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_company_with_http_info(company_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str company_id: The unique identifier for the Companies to return (required)
        :return: CompanyDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['company_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_company" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'company_id' is set
        if ('company_id' not in params or
                params['company_id'] is None):
            raise ValueError("Missing the required parameter `company_id` when calling `get_company`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'company_id' in params:
            path_params['companyId'] = params['company_id']  # noqa: E501

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
            '/api/v1/Companies/{companyId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CompanyDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def search_companies_from_supply_chain(self, **kwargs):  # noqa: E501
        """search_companies_from_supply_chain  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_companies_from_supply_chain(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CompanyResourceParameters body:
        :return: list[CompanyDto]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.search_companies_from_supply_chain_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.search_companies_from_supply_chain_with_http_info(**kwargs)  # noqa: E501
            return data

    def search_companies_from_supply_chain_with_http_info(self, **kwargs):  # noqa: E501
        """search_companies_from_supply_chain  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_companies_from_supply_chain_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CompanyResourceParameters body:
        :return: list[CompanyDto]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_companies_from_supply_chain" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

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
            '/api/v1/Companies/Suppliers/Search', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[CompanyDto]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
