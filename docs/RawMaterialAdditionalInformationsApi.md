# authenticate_supply_chain.RawMaterialAdditionalInformationsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_raw_materials_raw_material_id_raw_material_additional_informations_patch**](RawMaterialAdditionalInformationsApi.md#api_v1_raw_materials_raw_material_id_raw_material_additional_informations_patch) | **PATCH** /api/v1/RawMaterials/{rawMaterialId}/RawMaterialAdditionalInformations | Partially update an existing raw material additional information. Only provided fields will be updated
[**api_v1_raw_materials_raw_material_id_raw_material_additional_informations_put**](RawMaterialAdditionalInformationsApi.md#api_v1_raw_materials_raw_material_id_raw_material_additional_informations_put) | **PUT** /api/v1/RawMaterials/{rawMaterialId}/RawMaterialAdditionalInformations | Update an existing raw material additional information
[**get_raw_material_additional_information**](RawMaterialAdditionalInformationsApi.md#get_raw_material_additional_information) | **GET** /api/v1/RawMaterials/{rawMaterialId}/RawMaterialAdditionalInformations | Returns the rawMaterial additional information for the given raw material
[**save_raw_material_additional_information**](RawMaterialAdditionalInformationsApi.md#save_raw_material_additional_information) | **POST** /api/v1/RawMaterials/{rawMaterialId}/RawMaterialAdditionalInformations | Creates raw material additional information for the given raw material id

# **api_v1_raw_materials_raw_material_id_raw_material_additional_informations_patch**
> RawMaterialAdditionalInformationDto api_v1_raw_materials_raw_material_id_raw_material_additional_informations_patch(raw_material_id, body=body)

Partially update an existing raw material additional information. Only provided fields will be updated

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.RawMaterialAdditionalInformationsApi()
raw_material_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = [authenticate_supply_chain.Operation()] # list[Operation] |  (optional)

try:
    # Partially update an existing raw material additional information. Only provided fields will be updated
    api_response = api_instance.api_v1_raw_materials_raw_material_id_raw_material_additional_informations_patch(raw_material_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RawMaterialAdditionalInformationsApi->api_v1_raw_materials_raw_material_id_raw_material_additional_informations_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **raw_material_id** | [**str**](.md)|  | 
 **body** | [**list[Operation]**](Operation.md)|  | [optional] 

### Return type

[**RawMaterialAdditionalInformationDto**](RawMaterialAdditionalInformationDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_raw_materials_raw_material_id_raw_material_additional_informations_put**
> RawMaterialAdditionalInformationDto api_v1_raw_materials_raw_material_id_raw_material_additional_informations_put(raw_material_id, body=body)

Update an existing raw material additional information

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.RawMaterialAdditionalInformationsApi()
raw_material_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = authenticate_supply_chain.RawMaterialAdditionalInformationDto() # RawMaterialAdditionalInformationDto |  (optional)

try:
    # Update an existing raw material additional information
    api_response = api_instance.api_v1_raw_materials_raw_material_id_raw_material_additional_informations_put(raw_material_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RawMaterialAdditionalInformationsApi->api_v1_raw_materials_raw_material_id_raw_material_additional_informations_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **raw_material_id** | [**str**](.md)|  | 
 **body** | [**RawMaterialAdditionalInformationDto**](RawMaterialAdditionalInformationDto.md)|  | [optional] 

### Return type

[**RawMaterialAdditionalInformationDto**](RawMaterialAdditionalInformationDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_raw_material_additional_information**
> RawMaterialAdditionalInformationDto get_raw_material_additional_information(raw_material_id)

Returns the rawMaterial additional information for the given raw material

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.RawMaterialAdditionalInformationsApi()
raw_material_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The unique identifier of the raw material

try:
    # Returns the rawMaterial additional information for the given raw material
    api_response = api_instance.get_raw_material_additional_information(raw_material_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RawMaterialAdditionalInformationsApi->get_raw_material_additional_information: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **raw_material_id** | [**str**](.md)| The unique identifier of the raw material | 

### Return type

[**RawMaterialAdditionalInformationDto**](RawMaterialAdditionalInformationDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_raw_material_additional_information**
> RawMaterialAdditionalInformationDto save_raw_material_additional_information(raw_material_id, body=body)

Creates raw material additional information for the given raw material id

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.RawMaterialAdditionalInformationsApi()
raw_material_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The unique identifier of the raw material
body = authenticate_supply_chain.RawMaterialAdditionalInformationDto() # RawMaterialAdditionalInformationDto |  (optional)

try:
    # Creates raw material additional information for the given raw material id
    api_response = api_instance.save_raw_material_additional_information(raw_material_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RawMaterialAdditionalInformationsApi->save_raw_material_additional_information: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **raw_material_id** | [**str**](.md)| The unique identifier of the raw material | 
 **body** | [**RawMaterialAdditionalInformationDto**](RawMaterialAdditionalInformationDto.md)|  | [optional] 

### Return type

[**RawMaterialAdditionalInformationDto**](RawMaterialAdditionalInformationDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

