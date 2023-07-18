# authenticate_supply_chain.RawMaterialsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_raw_materials_raw_material_id_get**](RawMaterialsApi.md#api_v1_raw_materials_raw_material_id_get) | **GET** /api/v1/RawMaterials/{rawMaterialId} | Returns a specified raw material
[**api_v1_raw_materials_raw_material_id_patch**](RawMaterialsApi.md#api_v1_raw_materials_raw_material_id_patch) | **PATCH** /api/v1/RawMaterials/{rawMaterialId} | Partially update a raw material. Only provided fields will be updated
[**list_raw_materials**](RawMaterialsApi.md#list_raw_materials) | **GET** /api/v1/RawMaterials | Returns a list of Raw materials

# **api_v1_raw_materials_raw_material_id_get**
> list[RawMaterialDto] api_v1_raw_materials_raw_material_id_get(raw_material_id)

Returns a specified raw material

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.RawMaterialsApi()
raw_material_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The unique identifier of the raw material to return

try:
    # Returns a specified raw material
    api_response = api_instance.api_v1_raw_materials_raw_material_id_get(raw_material_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RawMaterialsApi->api_v1_raw_materials_raw_material_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **raw_material_id** | [**str**](.md)| The unique identifier of the raw material to return | 

### Return type

[**list[RawMaterialDto]**](RawMaterialDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_raw_materials_raw_material_id_patch**
> ProductDto api_v1_raw_materials_raw_material_id_patch(raw_material_id, body=body)

Partially update a raw material. Only provided fields will be updated

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.RawMaterialsApi()
raw_material_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = [authenticate_supply_chain.Operation()] # list[Operation] |  (optional)

try:
    # Partially update a raw material. Only provided fields will be updated
    api_response = api_instance.api_v1_raw_materials_raw_material_id_patch(raw_material_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RawMaterialsApi->api_v1_raw_materials_raw_material_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **raw_material_id** | [**str**](.md)|  | 
 **body** | [**list[Operation]**](Operation.md)|  | [optional] 

### Return type

[**ProductDto**](ProductDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_raw_materials**
> list[RawMaterialDto] list_raw_materials(raw_material_ids=raw_material_ids, supplier_id=supplier_id, search_query=search_query, page_number=page_number, page_size=page_size, order_by=order_by)

Returns a list of Raw materials

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.RawMaterialsApi()
raw_material_ids = ['raw_material_ids_example'] # list[str] |  (optional)
supplier_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str |  (optional)
search_query = 'search_query_example' # str |  (optional)
page_number = 56 # int |  (optional)
page_size = 56 # int |  (optional)
order_by = 'order_by_example' # str |  (optional)

try:
    # Returns a list of Raw materials
    api_response = api_instance.list_raw_materials(raw_material_ids=raw_material_ids, supplier_id=supplier_id, search_query=search_query, page_number=page_number, page_size=page_size, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RawMaterialsApi->list_raw_materials: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **raw_material_ids** | [**list[str]**](str.md)|  | [optional] 
 **supplier_id** | [**str**](.md)|  | [optional] 
 **search_query** | **str**|  | [optional] 
 **page_number** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **order_by** | **str**|  | [optional] 

### Return type

[**list[RawMaterialDto]**](RawMaterialDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

