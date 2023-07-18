# authenticate_supply_chain.RawMaterialRecordsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_raw_material_records_status_count_get**](RawMaterialRecordsApi.md#api_v1_raw_material_records_status_count_get) | **GET** /api/v1/RawMaterialRecords/StatusCount | Returns counts of Raw material records based on the resource parameters
[**api_v1_raw_materials_raw_material_id_records_post**](RawMaterialRecordsApi.md#api_v1_raw_materials_raw_material_id_records_post) | **POST** /api/v1/RawMaterials/{rawMaterialId}/Records | Create a raw material record for a raw material
[**api_v1_raw_materials_raw_material_id_records_raw_material_record_id_delete**](RawMaterialRecordsApi.md#api_v1_raw_materials_raw_material_id_records_raw_material_record_id_delete) | **DELETE** /api/v1/RawMaterials/{rawMaterialId}/Records/{rawMaterialRecordId} | Delete a raw material record.
[**api_v1_raw_materials_raw_material_id_records_raw_material_record_id_get**](RawMaterialRecordsApi.md#api_v1_raw_materials_raw_material_id_records_raw_material_record_id_get) | **GET** /api/v1/RawMaterials/{rawMaterialId}/Records/{rawMaterialRecordId} | Returns a specified raw material record
[**api_v1_raw_materials_raw_material_id_records_raw_material_record_id_put**](RawMaterialRecordsApi.md#api_v1_raw_materials_raw_material_id_records_raw_material_record_id_put) | **PUT** /api/v1/RawMaterials/{rawMaterialId}/Records/{rawMaterialRecordId} | Fully update a raw material record. All elements must be supplied or fields will be updated to default values
[**list_all_raw_material_records**](RawMaterialRecordsApi.md#list_all_raw_material_records) | **GET** /api/v1/RawMaterialRecords | Returns a list of Raw material records for the requesting company
[**list_raw_material_records**](RawMaterialRecordsApi.md#list_raw_material_records) | **GET** /api/v1/RawMaterials/{rawMaterialId}/Records | Returns a list of Raw material records for a raw material

# **api_v1_raw_material_records_status_count_get**
> list[RawMaterialRecordDto] api_v1_raw_material_records_status_count_get(supplier_id=supplier_id, status=status, no_status=no_status, search_query=search_query, page_number=page_number, page_size=page_size, order_by=order_by)

Returns counts of Raw material records based on the resource parameters

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.RawMaterialRecordsApi()
supplier_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Limit results to a single supplier. (optional)
status = authenticate_supply_chain.RawMaterialRecordStatusEnum() # RawMaterialRecordStatusEnum | Limit results to a status (optional)
no_status = true # bool | Limit results to records without a status (optional)
search_query = 'search_query_example' # str |  (optional)
page_number = 56 # int |  (optional)
page_size = 56 # int |  (optional)
order_by = 'order_by_example' # str |  (optional)

try:
    # Returns counts of Raw material records based on the resource parameters
    api_response = api_instance.api_v1_raw_material_records_status_count_get(supplier_id=supplier_id, status=status, no_status=no_status, search_query=search_query, page_number=page_number, page_size=page_size, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RawMaterialRecordsApi->api_v1_raw_material_records_status_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supplier_id** | [**str**](.md)| Limit results to a single supplier. | [optional] 
 **status** | [**RawMaterialRecordStatusEnum**](.md)| Limit results to a status | [optional] 
 **no_status** | **bool**| Limit results to records without a status | [optional] 
 **search_query** | **str**|  | [optional] 
 **page_number** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **order_by** | **str**|  | [optional] 

### Return type

[**list[RawMaterialRecordDto]**](RawMaterialRecordDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_raw_materials_raw_material_id_records_post**
> RawMaterialRecordDto api_v1_raw_materials_raw_material_id_records_post(raw_material_id, body=body)

Create a raw material record for a raw material

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.RawMaterialRecordsApi()
raw_material_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = authenticate_supply_chain.RawMaterialRecordForCreationDto() # RawMaterialRecordForCreationDto |  (optional)

try:
    # Create a raw material record for a raw material
    api_response = api_instance.api_v1_raw_materials_raw_material_id_records_post(raw_material_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RawMaterialRecordsApi->api_v1_raw_materials_raw_material_id_records_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **raw_material_id** | [**str**](.md)|  | 
 **body** | [**RawMaterialRecordForCreationDto**](RawMaterialRecordForCreationDto.md)|  | [optional] 

### Return type

[**RawMaterialRecordDto**](RawMaterialRecordDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_raw_materials_raw_material_id_records_raw_material_record_id_delete**
> api_v1_raw_materials_raw_material_id_records_raw_material_record_id_delete(raw_material_id, raw_material_record_id)

Delete a raw material record.

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.RawMaterialRecordsApi()
raw_material_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
raw_material_record_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Delete a raw material record.
    api_instance.api_v1_raw_materials_raw_material_id_records_raw_material_record_id_delete(raw_material_id, raw_material_record_id)
except ApiException as e:
    print("Exception when calling RawMaterialRecordsApi->api_v1_raw_materials_raw_material_id_records_raw_material_record_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **raw_material_id** | [**str**](.md)|  | 
 **raw_material_record_id** | [**str**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_raw_materials_raw_material_id_records_raw_material_record_id_get**
> list[RawMaterialRecordDto] api_v1_raw_materials_raw_material_id_records_raw_material_record_id_get(raw_material_id, raw_material_record_id)

Returns a specified raw material record

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.RawMaterialRecordsApi()
raw_material_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The unique identifier of the raw material
raw_material_record_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The unique identifier of the raw material record to return

try:
    # Returns a specified raw material record
    api_response = api_instance.api_v1_raw_materials_raw_material_id_records_raw_material_record_id_get(raw_material_id, raw_material_record_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RawMaterialRecordsApi->api_v1_raw_materials_raw_material_id_records_raw_material_record_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **raw_material_id** | [**str**](.md)| The unique identifier of the raw material | 
 **raw_material_record_id** | [**str**](.md)| The unique identifier of the raw material record to return | 

### Return type

[**list[RawMaterialRecordDto]**](RawMaterialRecordDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_raw_materials_raw_material_id_records_raw_material_record_id_put**
> RawMaterialRecordDto api_v1_raw_materials_raw_material_id_records_raw_material_record_id_put(raw_material_id, raw_material_record_id, body=body)

Fully update a raw material record. All elements must be supplied or fields will be updated to default values

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.RawMaterialRecordsApi()
raw_material_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
raw_material_record_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = authenticate_supply_chain.RawMaterialRecordForUpdateDto() # RawMaterialRecordForUpdateDto |  (optional)

try:
    # Fully update a raw material record. All elements must be supplied or fields will be updated to default values
    api_response = api_instance.api_v1_raw_materials_raw_material_id_records_raw_material_record_id_put(raw_material_id, raw_material_record_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RawMaterialRecordsApi->api_v1_raw_materials_raw_material_id_records_raw_material_record_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **raw_material_id** | [**str**](.md)|  | 
 **raw_material_record_id** | [**str**](.md)|  | 
 **body** | [**RawMaterialRecordForUpdateDto**](RawMaterialRecordForUpdateDto.md)|  | [optional] 

### Return type

[**RawMaterialRecordDto**](RawMaterialRecordDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all_raw_material_records**
> list[RawMaterialRecordDto] list_all_raw_material_records(supplier_id=supplier_id, status=status, no_status=no_status, search_query=search_query, page_number=page_number, page_size=page_size, order_by=order_by)

Returns a list of Raw material records for the requesting company

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.RawMaterialRecordsApi()
supplier_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Limit results to a single supplier. (optional)
status = authenticate_supply_chain.RawMaterialRecordStatusEnum() # RawMaterialRecordStatusEnum | Limit results to a status (optional)
no_status = true # bool | Limit results to records without a status (optional)
search_query = 'search_query_example' # str |  (optional)
page_number = 56 # int |  (optional)
page_size = 56 # int |  (optional)
order_by = 'order_by_example' # str |  (optional)

try:
    # Returns a list of Raw material records for the requesting company
    api_response = api_instance.list_all_raw_material_records(supplier_id=supplier_id, status=status, no_status=no_status, search_query=search_query, page_number=page_number, page_size=page_size, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RawMaterialRecordsApi->list_all_raw_material_records: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supplier_id** | [**str**](.md)| Limit results to a single supplier. | [optional] 
 **status** | [**RawMaterialRecordStatusEnum**](.md)| Limit results to a status | [optional] 
 **no_status** | **bool**| Limit results to records without a status | [optional] 
 **search_query** | **str**|  | [optional] 
 **page_number** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **order_by** | **str**|  | [optional] 

### Return type

[**list[RawMaterialRecordDto]**](RawMaterialRecordDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_raw_material_records**
> list[RawMaterialRecordDto] list_raw_material_records(raw_material_id, supplier_id=supplier_id, status=status, no_status=no_status, search_query=search_query, page_number=page_number, page_size=page_size, order_by=order_by)

Returns a list of Raw material records for a raw material

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.RawMaterialRecordsApi()
raw_material_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
supplier_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Limit results to a single supplier. (optional)
status = authenticate_supply_chain.RawMaterialRecordStatusEnum() # RawMaterialRecordStatusEnum | Limit results to a status (optional)
no_status = true # bool | Limit results to records without a status (optional)
search_query = 'search_query_example' # str |  (optional)
page_number = 56 # int |  (optional)
page_size = 56 # int |  (optional)
order_by = 'order_by_example' # str |  (optional)

try:
    # Returns a list of Raw material records for a raw material
    api_response = api_instance.list_raw_material_records(raw_material_id, supplier_id=supplier_id, status=status, no_status=no_status, search_query=search_query, page_number=page_number, page_size=page_size, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RawMaterialRecordsApi->list_raw_material_records: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **raw_material_id** | [**str**](.md)|  | 
 **supplier_id** | [**str**](.md)| Limit results to a single supplier. | [optional] 
 **status** | [**RawMaterialRecordStatusEnum**](.md)| Limit results to a status | [optional] 
 **no_status** | **bool**| Limit results to records without a status | [optional] 
 **search_query** | **str**|  | [optional] 
 **page_number** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **order_by** | **str**|  | [optional] 

### Return type

[**list[RawMaterialRecordDto]**](RawMaterialRecordDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

