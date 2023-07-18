# authenticate_supply_chain.AttachmentsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_attachment**](AttachmentsApi.md#get_attachment) | **GET** /api/v1/GetAttachment/{attachmentId} | Returns a specified attachment

# **get_attachment**
> get_attachment(attachment_id)

Returns a specified attachment

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.AttachmentsApi()
attachment_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Returns a specified attachment
    api_instance.get_attachment(attachment_id)
except ApiException as e:
    print("Exception when calling AttachmentsApi->get_attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attachment_id** | [**str**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

