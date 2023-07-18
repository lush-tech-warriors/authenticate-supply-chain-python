# authenticate_supply_chain.ProductLineApprovalApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_product_line_approval_post**](ProductLineApprovalApi.md#api_v1_product_line_approval_post) | **POST** /api/v1/ProductLineApproval | Save a new approval record for a product line
[**api_v1_product_line_approval_product_line_approval_id_put**](ProductLineApprovalApi.md#api_v1_product_line_approval_product_line_approval_id_put) | **PUT** /api/v1/ProductLineApproval/{productLineApprovalId} | Updates a product line approval record.
[**api_v1_product_line_approval_product_line_id_get**](ProductLineApprovalApi.md#api_v1_product_line_approval_product_line_id_get) | **GET** /api/v1/ProductLineApproval/{productLineId} | Returns a list of all approval records for a product, meeting the request criteria

# **api_v1_product_line_approval_post**
> ProductLineApprovalDto api_v1_product_line_approval_post(body=body)

Save a new approval record for a product line

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.ProductLineApprovalApi()
body = authenticate_supply_chain.ProductLineApprovalDto() # ProductLineApprovalDto |  (optional)

try:
    # Save a new approval record for a product line
    api_response = api_instance.api_v1_product_line_approval_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductLineApprovalApi->api_v1_product_line_approval_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProductLineApprovalDto**](ProductLineApprovalDto.md)|  | [optional] 

### Return type

[**ProductLineApprovalDto**](ProductLineApprovalDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_product_line_approval_product_line_approval_id_put**
> ProductLineApprovalDto api_v1_product_line_approval_product_line_approval_id_put(product_line_approval_id, body=body)

Updates a product line approval record.

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.ProductLineApprovalApi()
product_line_approval_id = 56 # int | 
body = authenticate_supply_chain.ProductLineApprovalDto() # ProductLineApprovalDto |  (optional)

try:
    # Updates a product line approval record.
    api_response = api_instance.api_v1_product_line_approval_product_line_approval_id_put(product_line_approval_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductLineApprovalApi->api_v1_product_line_approval_product_line_approval_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_line_approval_id** | **int**|  | 
 **body** | [**ProductLineApprovalDto**](ProductLineApprovalDto.md)|  | [optional] 

### Return type

[**ProductLineApprovalDto**](ProductLineApprovalDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_product_line_approval_product_line_id_get**
> list[ProductLineApprovalDto] api_v1_product_line_approval_product_line_id_get(product_line_id, search_query=search_query, page_number=page_number, page_size=page_size, order_by=order_by)

Returns a list of all approval records for a product, meeting the request criteria

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.ProductLineApprovalApi()
product_line_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
search_query = 'search_query_example' # str |  (optional)
page_number = 56 # int |  (optional)
page_size = 56 # int |  (optional)
order_by = 'order_by_example' # str |  (optional)

try:
    # Returns a list of all approval records for a product, meeting the request criteria
    api_response = api_instance.api_v1_product_line_approval_product_line_id_get(product_line_id, search_query=search_query, page_number=page_number, page_size=page_size, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductLineApprovalApi->api_v1_product_line_approval_product_line_id_get: %s\n" % e)
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

[**list[ProductLineApprovalDto]**](ProductLineApprovalDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

