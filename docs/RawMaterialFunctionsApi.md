# authenticate_supply_chain.RawMaterialFunctionsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_raw_materials_raw_material_id_raw_material_functions_get**](RawMaterialFunctionsApi.md#api_v1_raw_materials_raw_material_id_raw_material_functions_get) | **GET** /api/v1/RawMaterials/{rawMaterialId}/RawMaterialFunctions | Returns a material function for a given raw material
[**list_functions**](RawMaterialFunctionsApi.md#list_functions) | **GET** /api/v1/RawMaterialFunctions | Returns a list of raw material functions

# **api_v1_raw_materials_raw_material_id_raw_material_functions_get**
> RawMaterialFunctionDto api_v1_raw_materials_raw_material_id_raw_material_functions_get(raw_material_id)

Returns a material function for a given raw material

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.RawMaterialFunctionsApi()
raw_material_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Returns a material function for a given raw material
    api_response = api_instance.api_v1_raw_materials_raw_material_id_raw_material_functions_get(raw_material_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RawMaterialFunctionsApi->api_v1_raw_materials_raw_material_id_raw_material_functions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **raw_material_id** | [**str**](.md)|  | 

### Return type

[**RawMaterialFunctionDto**](RawMaterialFunctionDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_functions**
> list[RawMaterialFunctionDto] list_functions(search_query=search_query, page_number=page_number, page_size=page_size, order_by=order_by)

Returns a list of raw material functions

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.RawMaterialFunctionsApi()
search_query = 'search_query_example' # str |  (optional)
page_number = 56 # int |  (optional)
page_size = 56 # int |  (optional)
order_by = 'order_by_example' # str |  (optional)

try:
    # Returns a list of raw material functions
    api_response = api_instance.list_functions(search_query=search_query, page_number=page_number, page_size=page_size, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RawMaterialFunctionsApi->list_functions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_query** | **str**|  | [optional] 
 **page_number** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **order_by** | **str**|  | [optional] 

### Return type

[**list[RawMaterialFunctionDto]**](RawMaterialFunctionDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

