# authenticate_supply_chain.ProductLineApprovalRequestApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_product_line_approval_request_post**](ProductLineApprovalRequestApi.md#api_v1_product_line_approval_request_post) | **POST** /api/v1/ProductLineApprovalRequest | Save a new approval request for a product line approval
[**api_v1_product_line_approval_request_product_line_approval_id_get**](ProductLineApprovalRequestApi.md#api_v1_product_line_approval_request_product_line_approval_id_get) | **GET** /api/v1/ProductLineApprovalRequest/{productLineApprovalId} | Returns a list of all approval requests for a product line approval, meeting the request criteria

# **api_v1_product_line_approval_request_post**
> ProductLineApprovalDto api_v1_product_line_approval_request_post(body=body)

Save a new approval request for a product line approval

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.ProductLineApprovalRequestApi()
body = authenticate_supply_chain.ProductLineApprovalRequestDto() # ProductLineApprovalRequestDto |  (optional)

try:
    # Save a new approval request for a product line approval
    api_response = api_instance.api_v1_product_line_approval_request_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductLineApprovalRequestApi->api_v1_product_line_approval_request_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProductLineApprovalRequestDto**](ProductLineApprovalRequestDto.md)|  | [optional] 

### Return type

[**ProductLineApprovalDto**](ProductLineApprovalDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_product_line_approval_request_product_line_approval_id_get**
> list[ProductLineApprovalRequestDto] api_v1_product_line_approval_request_product_line_approval_id_get(product_line_approval_id, search_query=search_query, page_number=page_number, page_size=page_size, order_by=order_by)

Returns a list of all approval requests for a product line approval, meeting the request criteria

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.ProductLineApprovalRequestApi()
product_line_approval_id = 56 # int | 
search_query = 'search_query_example' # str |  (optional)
page_number = 56 # int |  (optional)
page_size = 56 # int |  (optional)
order_by = 'order_by_example' # str |  (optional)

try:
    # Returns a list of all approval requests for a product line approval, meeting the request criteria
    api_response = api_instance.api_v1_product_line_approval_request_product_line_approval_id_get(product_line_approval_id, search_query=search_query, page_number=page_number, page_size=page_size, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductLineApprovalRequestApi->api_v1_product_line_approval_request_product_line_approval_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_line_approval_id** | **int**|  | 
 **search_query** | **str**|  | [optional] 
 **page_number** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **order_by** | **str**|  | [optional] 

### Return type

[**list[ProductLineApprovalRequestDto]**](ProductLineApprovalRequestDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

