# authenticate_supply_chain.ProductLineStatusApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_product_line_product_line_id_product_line_status_get**](ProductLineStatusApi.md#api_v1_product_line_product_line_id_product_line_status_get) | **GET** /api/v1/ProductLine/{productLineId}/ProductLineStatus | Returns a list of all statuses for a product, meeting the request criteria
[**api_v1_product_line_product_line_id_product_line_status_post**](ProductLineStatusApi.md#api_v1_product_line_product_line_id_product_line_status_post) | **POST** /api/v1/ProductLine/{productLineId}/ProductLineStatus | Create a new Product Line Status

# **api_v1_product_line_product_line_id_product_line_status_get**
> list[ProductLineStatusDto] api_v1_product_line_product_line_id_product_line_status_get(product_line_id, search_query=search_query, page_number=page_number, page_size=page_size, order_by=order_by)

Returns a list of all statuses for a product, meeting the request criteria

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.ProductLineStatusApi()
product_line_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
search_query = 'search_query_example' # str |  (optional)
page_number = 56 # int |  (optional)
page_size = 56 # int |  (optional)
order_by = 'order_by_example' # str |  (optional)

try:
    # Returns a list of all statuses for a product, meeting the request criteria
    api_response = api_instance.api_v1_product_line_product_line_id_product_line_status_get(product_line_id, search_query=search_query, page_number=page_number, page_size=page_size, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductLineStatusApi->api_v1_product_line_product_line_id_product_line_status_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_line_id** | [**str**](.md)|  | 
 **search_query** | **str**|  | [optional] 
 **page_number** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **order_by** | **str**|  | [optional] 

### Return type

[**list[ProductLineStatusDto]**](ProductLineStatusDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_product_line_product_line_id_product_line_status_post**
> ProductLineStatusForCreationDto api_v1_product_line_product_line_id_product_line_status_post(product_line_id, body=body)

Create a new Product Line Status

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.ProductLineStatusApi()
product_line_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = authenticate_supply_chain.ProductLineStatusForCreationDto() # ProductLineStatusForCreationDto |  (optional)

try:
    # Create a new Product Line Status
    api_response = api_instance.api_v1_product_line_product_line_id_product_line_status_post(product_line_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductLineStatusApi->api_v1_product_line_product_line_id_product_line_status_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_line_id** | [**str**](.md)|  | 
 **body** | [**ProductLineStatusForCreationDto**](ProductLineStatusForCreationDto.md)|  | [optional] 

### Return type

[**ProductLineStatusForCreationDto**](ProductLineStatusForCreationDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

