# authenticate_supply_chain.ProductLineVersionApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_product_line_product_line_id_product_line_version_post**](ProductLineVersionApi.md#api_v1_product_line_product_line_id_product_line_version_post) | **POST** /api/v1/ProductLine/{productLineId}/ProductLineVersion | Set a product line as versioned

# **api_v1_product_line_product_line_id_product_line_version_post**
> ProductLineStatusForCreationDto api_v1_product_line_product_line_id_product_line_version_post(product_line_id)

Set a product line as versioned

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.ProductLineVersionApi()
product_line_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Set a product line as versioned
    api_response = api_instance.api_v1_product_line_product_line_id_product_line_version_post(product_line_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductLineVersionApi->api_v1_product_line_product_line_id_product_line_version_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_line_id** | [**str**](.md)|  | 

### Return type

[**ProductLineStatusForCreationDto**](ProductLineStatusForCreationDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

