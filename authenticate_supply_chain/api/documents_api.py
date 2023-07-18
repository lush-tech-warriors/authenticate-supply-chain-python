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


class DocumentsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def api_v1_document_id_put(self, document_id, **kwargs):  # noqa: E501
        """Fully update a document. All elements must be supplied or fields will be updated to default values  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v1_document_id_put(document_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str document_id: (required)
        :param DocumentForUpdateDto body:
        :return: DocumentDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_v1_document_id_put_with_http_info(document_id, **kwargs)  # noqa: E501
        else:
            (data) = self.api_v1_document_id_put_with_http_info(document_id, **kwargs)  # noqa: E501
            return data

    def api_v1_document_id_put_with_http_info(self, document_id, **kwargs):  # noqa: E501
        """Fully update a document. All elements must be supplied or fields will be updated to default values  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v1_document_id_put_with_http_info(document_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str document_id: (required)
        :param DocumentForUpdateDto body:
        :return: DocumentDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['document_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v1_document_id_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'document_id' is set
        if ('document_id' not in params or
                params['document_id'] is None):
            raise ValueError("Missing the required parameter `document_id` when calling `api_v1_document_id_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'document_id' in params:
            path_params['documentId'] = params['document_id']  # noqa: E501

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
            '/api/v1/{documentId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DocumentDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_v1_notes_note_id_documents_post(self, note_id, **kwargs):  # noqa: E501
        """Associate a document with a given note  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v1_notes_note_id_documents_post(note_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str note_id: (required)
        :param DocumentForCreationDto body:
        :return: DocumentDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_v1_notes_note_id_documents_post_with_http_info(note_id, **kwargs)  # noqa: E501
        else:
            (data) = self.api_v1_notes_note_id_documents_post_with_http_info(note_id, **kwargs)  # noqa: E501
            return data

    def api_v1_notes_note_id_documents_post_with_http_info(self, note_id, **kwargs):  # noqa: E501
        """Associate a document with a given note  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v1_notes_note_id_documents_post_with_http_info(note_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str note_id: (required)
        :param DocumentForCreationDto body:
        :return: DocumentDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['note_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v1_notes_note_id_documents_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'note_id' is set
        if ('note_id' not in params or
                params['note_id'] is None):
            raise ValueError("Missing the required parameter `note_id` when calling `api_v1_notes_note_id_documents_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'note_id' in params:
            path_params['noteId'] = params['note_id']  # noqa: E501

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
            '/api/v1/Notes/{noteId}/Documents', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DocumentDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)