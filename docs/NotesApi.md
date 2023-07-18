# authenticate_supply_chain.NotesApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_site_note**](NotesApi.md#get_site_note) | **GET** /api/v1/Suppliers/{supplierId}/Sites/{siteId}/Notes/{noteId} | Returns a specified note
[**get_site_note_count**](NotesApi.md#get_site_note_count) | **GET** /api/v1/Suppliers/{supplierId}/Sites/{siteId}/Notes/Count | Returns a list of all notes for the given supplier and site
[**get_site_notes**](NotesApi.md#get_site_notes) | **GET** /api/v1/Suppliers/{supplierId}/Sites/{siteId}/Notes | Returns a list of all notes meeting the request criteria
[**get_supplier_note**](NotesApi.md#get_supplier_note) | **GET** /api/v1/Suppliers/{supplierId}/Notes/{noteId} | Returns a specified note
[**get_supplier_notes**](NotesApi.md#get_supplier_notes) | **GET** /api/v1/Suppliers/{supplierId}/Notes | Returns a list of all notes meeting the request criteria

# **get_site_note**
> NoteDto get_site_note(supplier_id, site_id, note_id)

Returns a specified note

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.NotesApi()
supplier_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
site_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
note_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The unique identifier for the note to return

try:
    # Returns a specified note
    api_response = api_instance.get_site_note(supplier_id, site_id, note_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotesApi->get_site_note: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supplier_id** | [**str**](.md)|  | 
 **site_id** | [**str**](.md)|  | 
 **note_id** | [**str**](.md)| The unique identifier for the note to return | 

### Return type

[**NoteDto**](NoteDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_site_note_count**
> int get_site_note_count(supplier_id, site_id)

Returns a list of all notes for the given supplier and site

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.NotesApi()
supplier_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
site_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Returns a list of all notes for the given supplier and site
    api_response = api_instance.get_site_note_count(supplier_id, site_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotesApi->get_site_note_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supplier_id** | [**str**](.md)|  | 
 **site_id** | [**str**](.md)|  | 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_site_notes**
> list[NoteDto] get_site_notes(supplier_id, site_id, title=title, type=type, type_id=type_id, created_by_company_id=created_by_company_id, order_by=order_by, search_query=search_query, page_number=page_number, page_size=page_size)

Returns a list of all notes meeting the request criteria

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.NotesApi()
supplier_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
site_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
title = 'title_example' # str |  (optional)
type = authenticate_supply_chain.ParentTypeEnum() # ParentTypeEnum |  (optional)
type_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str |  (optional)
created_by_company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str |  (optional)
order_by = 'order_by_example' # str |  (optional)
search_query = 'search_query_example' # str |  (optional)
page_number = 56 # int |  (optional)
page_size = 56 # int |  (optional)

try:
    # Returns a list of all notes meeting the request criteria
    api_response = api_instance.get_site_notes(supplier_id, site_id, title=title, type=type, type_id=type_id, created_by_company_id=created_by_company_id, order_by=order_by, search_query=search_query, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotesApi->get_site_notes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supplier_id** | [**str**](.md)|  | 
 **site_id** | [**str**](.md)|  | 
 **title** | **str**|  | [optional] 
 **type** | [**ParentTypeEnum**](.md)|  | [optional] 
 **type_id** | [**str**](.md)|  | [optional] 
 **created_by_company_id** | [**str**](.md)|  | [optional] 
 **order_by** | **str**|  | [optional] 
 **search_query** | **str**|  | [optional] 
 **page_number** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 

### Return type

[**list[NoteDto]**](NoteDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_supplier_note**
> NoteDto get_supplier_note(supplier_id, note_id)

Returns a specified note

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.NotesApi()
supplier_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
note_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The unique identifier for the note to return

try:
    # Returns a specified note
    api_response = api_instance.get_supplier_note(supplier_id, note_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotesApi->get_supplier_note: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supplier_id** | [**str**](.md)|  | 
 **note_id** | [**str**](.md)| The unique identifier for the note to return | 

### Return type

[**NoteDto**](NoteDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_supplier_notes**
> list[NoteDto] get_supplier_notes(supplier_id, title=title, type=type, type_id=type_id, created_by_company_id=created_by_company_id, order_by=order_by, search_query=search_query, page_number=page_number, page_size=page_size)

Returns a list of all notes meeting the request criteria

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.NotesApi()
supplier_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
title = 'title_example' # str |  (optional)
type = authenticate_supply_chain.ParentTypeEnum() # ParentTypeEnum |  (optional)
type_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str |  (optional)
created_by_company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str |  (optional)
order_by = 'order_by_example' # str |  (optional)
search_query = 'search_query_example' # str |  (optional)
page_number = 56 # int |  (optional)
page_size = 56 # int |  (optional)

try:
    # Returns a list of all notes meeting the request criteria
    api_response = api_instance.get_supplier_notes(supplier_id, title=title, type=type, type_id=type_id, created_by_company_id=created_by_company_id, order_by=order_by, search_query=search_query, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotesApi->get_supplier_notes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supplier_id** | [**str**](.md)|  | 
 **title** | **str**|  | [optional] 
 **type** | [**ParentTypeEnum**](.md)|  | [optional] 
 **type_id** | [**str**](.md)|  | [optional] 
 **created_by_company_id** | [**str**](.md)|  | [optional] 
 **order_by** | **str**|  | [optional] 
 **search_query** | **str**|  | [optional] 
 **page_number** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 

### Return type

[**list[NoteDto]**](NoteDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

