# authenticate_supply_chain.RawMaterialApprovalApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_approval**](RawMaterialApprovalApi.md#delete_approval) | **DELETE** /api/v1/RawMaterials/{rawMaterialId}/Approval | Deletes the approval for the given raw material
[**get_approval**](RawMaterialApprovalApi.md#get_approval) | **GET** /api/v1/RawMaterials/{rawMaterialId}/Approval | Returns the approval for the given raw material
[**get_approvals**](RawMaterialApprovalApi.md#get_approvals) | **POST** /api/v1/RawMaterials/Approvals | Returns a list of raw material approvals for a list of given raw material ids
[**save_approval**](RawMaterialApprovalApi.md#save_approval) | **POST** /api/v1/RawMaterials/{rawMaterialId}/Approval | Creates an approval for the given raw material

# **delete_approval**
> RawMaterialApprovalDto delete_approval(raw_material_id)

Deletes the approval for the given raw material

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.RawMaterialApprovalApi()
raw_material_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The unique identifier of the raw material

try:
    # Deletes the approval for the given raw material
    api_response = api_instance.delete_approval(raw_material_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RawMaterialApprovalApi->delete_approval: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **raw_material_id** | [**str**](.md)| The unique identifier of the raw material | 

### Return type

[**RawMaterialApprovalDto**](RawMaterialApprovalDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_approval**
> RawMaterialApprovalDto get_approval(raw_material_id)

Returns the approval for the given raw material

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.RawMaterialApprovalApi()
raw_material_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The unique identifier of the raw material

try:
    # Returns the approval for the given raw material
    api_response = api_instance.get_approval(raw_material_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RawMaterialApprovalApi->get_approval: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **raw_material_id** | [**str**](.md)| The unique identifier of the raw material | 

### Return type

[**RawMaterialApprovalDto**](RawMaterialApprovalDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_approvals**
> list[RawMaterialApprovalDto] get_approvals(body=body)

Returns a list of raw material approvals for a list of given raw material ids

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.RawMaterialApprovalApi()
body = authenticate_supply_chain.RawMaterialResourceParameters() # RawMaterialResourceParameters |  (optional)

try:
    # Returns a list of raw material approvals for a list of given raw material ids
    api_response = api_instance.get_approvals(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RawMaterialApprovalApi->get_approvals: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RawMaterialResourceParameters**](RawMaterialResourceParameters.md)|  | [optional] 

### Return type

[**list[RawMaterialApprovalDto]**](RawMaterialApprovalDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_approval**
> list[RawMaterialApprovalDto] save_approval(raw_material_id)

Creates an approval for the given raw material

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.RawMaterialApprovalApi()
raw_material_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The unique identifier of the raw material

try:
    # Creates an approval for the given raw material
    api_response = api_instance.save_approval(raw_material_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RawMaterialApprovalApi->save_approval: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **raw_material_id** | [**str**](.md)| The unique identifier of the raw material | 

### Return type

[**list[RawMaterialApprovalDto]**](RawMaterialApprovalDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

