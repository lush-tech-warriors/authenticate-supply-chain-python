# authenticate_supply_chain.ProductLineOwnersApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_owner**](ProductLineOwnersApi.md#add_owner) | **POST** /api/v1/ProductLine/{productLineId}/ProductLineOwners/{userId} | Associates an Owner with an Inventory Item.
[**delete_owner**](ProductLineOwnersApi.md#delete_owner) | **DELETE** /api/v1/ProductLine/{productLineId}/ProductLineOwners/{userId} | Deletes an Inventory Item Owner

# **add_owner**
> ProductLineOwnerDto add_owner(product_line_id, user_id)

Associates an Owner with an Inventory Item.

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.ProductLineOwnersApi()
product_line_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
user_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Associates an Owner with an Inventory Item.
    api_response = api_instance.add_owner(product_line_id, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductLineOwnersApi->add_owner: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_line_id** | [**str**](.md)|  | 
 **user_id** | [**str**](.md)|  | 

### Return type

[**ProductLineOwnerDto**](ProductLineOwnerDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_owner**
> ProductLineOwnerDto delete_owner(product_line_id, user_id)

Deletes an Inventory Item Owner

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.ProductLineOwnersApi()
product_line_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
user_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Deletes an Inventory Item Owner
    api_response = api_instance.delete_owner(product_line_id, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductLineOwnersApi->delete_owner: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_line_id** | [**str**](.md)|  | 
 **user_id** | [**str**](.md)|  | 

### Return type

[**ProductLineOwnerDto**](ProductLineOwnerDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

