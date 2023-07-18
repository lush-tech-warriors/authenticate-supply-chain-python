# authenticate_supply_chain.DocumentsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_document_id_put**](DocumentsApi.md#api_v1_document_id_put) | **PUT** /api/v1/{documentId} | Fully update a document. All elements must be supplied or fields will be updated to default values
[**api_v1_notes_note_id_documents_post**](DocumentsApi.md#api_v1_notes_note_id_documents_post) | **POST** /api/v1/Notes/{noteId}/Documents | Associate a document with a given note

# **api_v1_document_id_put**
> DocumentDto api_v1_document_id_put(document_id, body=body)

Fully update a document. All elements must be supplied or fields will be updated to default values

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.DocumentsApi()
document_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = authenticate_supply_chain.DocumentForUpdateDto() # DocumentForUpdateDto |  (optional)

try:
    # Fully update a document. All elements must be supplied or fields will be updated to default values
    api_response = api_instance.api_v1_document_id_put(document_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->api_v1_document_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | [**str**](.md)|  | 
 **body** | [**DocumentForUpdateDto**](DocumentForUpdateDto.md)|  | [optional] 

### Return type

[**DocumentDto**](DocumentDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_notes_note_id_documents_post**
> DocumentDto api_v1_notes_note_id_documents_post(note_id, body=body)

Associate a document with a given note

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.DocumentsApi()
note_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = authenticate_supply_chain.DocumentForCreationDto() # DocumentForCreationDto |  (optional)

try:
    # Associate a document with a given note
    api_response = api_instance.api_v1_notes_note_id_documents_post(note_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->api_v1_notes_note_id_documents_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **note_id** | [**str**](.md)|  | 
 **body** | [**DocumentForCreationDto**](DocumentForCreationDto.md)|  | [optional] 

### Return type

[**DocumentDto**](DocumentDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

