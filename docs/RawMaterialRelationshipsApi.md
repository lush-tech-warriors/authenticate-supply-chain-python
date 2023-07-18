# authenticate_supply_chain.RawMaterialRelationshipsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_raw_materials_raw_material_id_raw_material_relationships_get**](RawMaterialRelationshipsApi.md#api_v1_raw_materials_raw_material_id_raw_material_relationships_get) | **GET** /api/v1/RawMaterials/{rawMaterialId}/RawMaterialRelationships | Returns the raw material relationship for the given raw material
[**save_raw_material_relationship**](RawMaterialRelationshipsApi.md#save_raw_material_relationship) | **POST** /api/v1/RawMaterials/{rawMaterialId}/RawMaterialRelationships | Creates a raw material relationship for the given raw material id

# **api_v1_raw_materials_raw_material_id_raw_material_relationships_get**
> RawMaterialRelationshipDto api_v1_raw_materials_raw_material_id_raw_material_relationships_get(raw_material_id)

Returns the raw material relationship for the given raw material

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.RawMaterialRelationshipsApi()
raw_material_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The unique identifier of the raw material

try:
    # Returns the raw material relationship for the given raw material
    api_response = api_instance.api_v1_raw_materials_raw_material_id_raw_material_relationships_get(raw_material_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RawMaterialRelationshipsApi->api_v1_raw_materials_raw_material_id_raw_material_relationships_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **raw_material_id** | [**str**](.md)| The unique identifier of the raw material | 

### Return type

[**RawMaterialRelationshipDto**](RawMaterialRelationshipDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_raw_material_relationship**
> RawMaterialRelationshipDto save_raw_material_relationship(raw_material_id, body=body)

Creates a raw material relationship for the given raw material id

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.RawMaterialRelationshipsApi()
raw_material_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The unique identifier of the raw material
body = authenticate_supply_chain.RawMaterialRelationshipDto() # RawMaterialRelationshipDto |  (optional)

try:
    # Creates a raw material relationship for the given raw material id
    api_response = api_instance.save_raw_material_relationship(raw_material_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RawMaterialRelationshipsApi->save_raw_material_relationship: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **raw_material_id** | [**str**](.md)| The unique identifier of the raw material | 
 **body** | [**RawMaterialRelationshipDto**](RawMaterialRelationshipDto.md)|  | [optional] 

### Return type

[**RawMaterialRelationshipDto**](RawMaterialRelationshipDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

