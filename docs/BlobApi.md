# authenticate_supply_chain.BlobApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_blob_post**](BlobApi.md#api_v1_blob_post) | **POST** /api/v1/Blob | Posts a file to the given folder path in the Documents storage account
[**get_blob**](BlobApi.md#get_blob) | **GET** /api/v1/Blob | Get a File identified by its external provider reference

# **api_v1_blob_post**
> api_v1_blob_post(file=file, storage_folder_path=storage_folder_path, storage_account=storage_account, use_real_file_name=use_real_file_name)

Posts a file to the given folder path in the Documents storage account

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.BlobApi()
file = 'file_example' # str |  (optional)
storage_folder_path = 'storage_folder_path_example' # str |  (optional)
storage_account = authenticate_supply_chain.StorageAccountEnum() # StorageAccountEnum |  (optional)
use_real_file_name = true # bool |  (optional)

try:
    # Posts a file to the given folder path in the Documents storage account
    api_instance.api_v1_blob_post(file=file, storage_folder_path=storage_folder_path, storage_account=storage_account, use_real_file_name=use_real_file_name)
except ApiException as e:
    print("Exception when calling BlobApi->api_v1_blob_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **str**|  | [optional] 
 **storage_folder_path** | **str**|  | [optional] 
 **storage_account** | [**StorageAccountEnum**](.md)|  | [optional] 
 **use_real_file_name** | **bool**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_blob**
> get_blob(external_provider_reference=external_provider_reference)

Get a File identified by its external provider reference

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.BlobApi()
external_provider_reference = 'external_provider_reference_example' # str |  (optional)

try:
    # Get a File identified by its external provider reference
    api_instance.get_blob(external_provider_reference=external_provider_reference)
except ApiException as e:
    print("Exception when calling BlobApi->get_blob: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_provider_reference** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

