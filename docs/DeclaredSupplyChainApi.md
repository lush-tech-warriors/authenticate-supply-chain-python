# authenticate_supply_chain.DeclaredSupplyChainApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_declared_supply_chain**](DeclaredSupplyChainApi.md#create_declared_supply_chain) | **POST** /api/v1/DeclaredSupplyChain/{topLevelProductId} | Create a new Declared Supply Chain
[**get_declared_supply_chain**](DeclaredSupplyChainApi.md#get_declared_supply_chain) | **GET** /api/v1/DeclaredSupplyChain/{topLevelProductId} | Returns the declared supply chain for a given top level product id
[**update_declared_supply_chain**](DeclaredSupplyChainApi.md#update_declared_supply_chain) | **PUT** /api/v1/DeclaredSupplyChain/{declaredSupplyChainId} | Update a Declared Supply Chain

# **create_declared_supply_chain**
> DeclaredSupplyChainDto create_declared_supply_chain(top_level_product_id, body=body)

Create a new Declared Supply Chain

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.DeclaredSupplyChainApi()
top_level_product_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = authenticate_supply_chain.DeclaredSupplyChainForCreationDto() # DeclaredSupplyChainForCreationDto |  (optional)

try:
    # Create a new Declared Supply Chain
    api_response = api_instance.create_declared_supply_chain(top_level_product_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeclaredSupplyChainApi->create_declared_supply_chain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **top_level_product_id** | [**str**](.md)|  | 
 **body** | [**DeclaredSupplyChainForCreationDto**](DeclaredSupplyChainForCreationDto.md)|  | [optional] 

### Return type

[**DeclaredSupplyChainDto**](DeclaredSupplyChainDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_declared_supply_chain**
> list[DeclaredSupplyChainDto] get_declared_supply_chain(top_level_product_id, search_query=search_query, page_number=page_number, page_size=page_size, order_by=order_by)

Returns the declared supply chain for a given top level product id

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.DeclaredSupplyChainApi()
top_level_product_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
search_query = 'search_query_example' # str |  (optional)
page_number = 56 # int |  (optional)
page_size = 56 # int |  (optional)
order_by = 'order_by_example' # str |  (optional)

try:
    # Returns the declared supply chain for a given top level product id
    api_response = api_instance.get_declared_supply_chain(top_level_product_id, search_query=search_query, page_number=page_number, page_size=page_size, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeclaredSupplyChainApi->get_declared_supply_chain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **top_level_product_id** | [**str**](.md)|  | 
 **search_query** | **str**|  | [optional] 
 **page_number** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **order_by** | **str**|  | [optional] 

### Return type

[**list[DeclaredSupplyChainDto]**](DeclaredSupplyChainDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_declared_supply_chain**
> DeclaredSupplyChainDto update_declared_supply_chain(declared_supply_chain_id, body=body)

Update a Declared Supply Chain

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.DeclaredSupplyChainApi()
declared_supply_chain_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = authenticate_supply_chain.DeclaredSupplyChainForUpdateDto() # DeclaredSupplyChainForUpdateDto |  (optional)

try:
    # Update a Declared Supply Chain
    api_response = api_instance.update_declared_supply_chain(declared_supply_chain_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeclaredSupplyChainApi->update_declared_supply_chain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **declared_supply_chain_id** | [**str**](.md)|  | 
 **body** | [**DeclaredSupplyChainForUpdateDto**](DeclaredSupplyChainForUpdateDto.md)|  | [optional] 

### Return type

[**DeclaredSupplyChainDto**](DeclaredSupplyChainDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

