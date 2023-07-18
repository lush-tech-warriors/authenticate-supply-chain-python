# authenticate_supply_chain.RawMaterialLogisticsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_raw_materials_raw_material_id_logistics_logistic_id_delete**](RawMaterialLogisticsApi.md#api_v1_raw_materials_raw_material_id_logistics_logistic_id_delete) | **DELETE** /api/v1/RawMaterials/{rawMaterialId}/Logistics/{logisticId} | Delete a raw material logistic
[**api_v1_raw_materials_raw_material_id_logistics_post**](RawMaterialLogisticsApi.md#api_v1_raw_materials_raw_material_id_logistics_post) | **POST** /api/v1/RawMaterials/{rawMaterialId}/Logistics | Create a new logistic for a raw material
[**list_logistics**](RawMaterialLogisticsApi.md#list_logistics) | **POST** /api/v1/RawMaterials/Logistics | Returns a list of all logistics for the given raw material

# **api_v1_raw_materials_raw_material_id_logistics_logistic_id_delete**
> api_v1_raw_materials_raw_material_id_logistics_logistic_id_delete(raw_material_id, logistic_id)

Delete a raw material logistic

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.RawMaterialLogisticsApi()
raw_material_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
logistic_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Delete a raw material logistic
    api_instance.api_v1_raw_materials_raw_material_id_logistics_logistic_id_delete(raw_material_id, logistic_id)
except ApiException as e:
    print("Exception when calling RawMaterialLogisticsApi->api_v1_raw_materials_raw_material_id_logistics_logistic_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **raw_material_id** | [**str**](.md)|  | 
 **logistic_id** | [**str**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_raw_materials_raw_material_id_logistics_post**
> RawMaterialLogisticDto api_v1_raw_materials_raw_material_id_logistics_post(raw_material_id, body=body)

Create a new logistic for a raw material

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.RawMaterialLogisticsApi()
raw_material_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = authenticate_supply_chain.RawMaterialLogisticForCreationDto() # RawMaterialLogisticForCreationDto |  (optional)

try:
    # Create a new logistic for a raw material
    api_response = api_instance.api_v1_raw_materials_raw_material_id_logistics_post(raw_material_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RawMaterialLogisticsApi->api_v1_raw_materials_raw_material_id_logistics_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **raw_material_id** | [**str**](.md)|  | 
 **body** | [**RawMaterialLogisticForCreationDto**](RawMaterialLogisticForCreationDto.md)|  | [optional] 

### Return type

[**RawMaterialLogisticDto**](RawMaterialLogisticDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_logistics**
> list[RawMaterialLogisticDto] list_logistics(body=body)

Returns a list of all logistics for the given raw material

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.RawMaterialLogisticsApi()
body = authenticate_supply_chain.RawMaterialResourceParameters() # RawMaterialResourceParameters |  (optional)

try:
    # Returns a list of all logistics for the given raw material
    api_response = api_instance.list_logistics(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RawMaterialLogisticsApi->list_logistics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RawMaterialResourceParameters**](RawMaterialResourceParameters.md)|  | [optional] 

### Return type

[**list[RawMaterialLogisticDto]**](RawMaterialLogisticDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

