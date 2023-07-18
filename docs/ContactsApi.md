# authenticate_supply_chain.ContactsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_contact**](ContactsApi.md#create_contact) | **POST** /api/v1/Suppliers/{supplierId}/Sites/{siteId}/Contacts | Create a new contact
[**create_contact_v2**](ContactsApi.md#create_contact_v2) | **POST** /api/v1/Suppliers/{supplierId}/Contacts | Create a new contact
[**get_company_contact**](ContactsApi.md#get_company_contact) | **GET** /api/v1/Suppliers/{supplierId}/Contacts/{contactId} | Returns a specified contact
[**get_company_contacts**](ContactsApi.md#get_company_contacts) | **GET** /api/v1/Suppliers/{supplierId}/Contacts | Returns a list of all contacts meeting the request criteria
[**get_contacts**](ContactsApi.md#get_contacts) | **GET** /api/v1/Contacts | Returns a list of contacts meeting the request criteria

# **create_contact**
> ContactDto create_contact(supplier_id, site_id, body=body)

Create a new contact

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.ContactsApi()
supplier_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
site_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = authenticate_supply_chain.ContactForCreationDto() # ContactForCreationDto |  (optional)

try:
    # Create a new contact
    api_response = api_instance.create_contact(supplier_id, site_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->create_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supplier_id** | [**str**](.md)|  | 
 **site_id** | [**str**](.md)|  | 
 **body** | [**ContactForCreationDto**](ContactForCreationDto.md)|  | [optional] 

### Return type

[**ContactDto**](ContactDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_contact_v2**
> ContactDto create_contact_v2(supplier_id, body=body)

Create a new contact

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.ContactsApi()
supplier_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = authenticate_supply_chain.ContactForCreationDto() # ContactForCreationDto |  (optional)

try:
    # Create a new contact
    api_response = api_instance.create_contact_v2(supplier_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->create_contact_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supplier_id** | [**str**](.md)|  | 
 **body** | [**ContactForCreationDto**](ContactForCreationDto.md)|  | [optional] 

### Return type

[**ContactDto**](ContactDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_contact**
> ContactDto get_company_contact(supplier_id, contact_id)

Returns a specified contact

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.ContactsApi()
supplier_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
contact_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The unique identifier for the contact to return

try:
    # Returns a specified contact
    api_response = api_instance.get_company_contact(supplier_id, contact_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->get_company_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supplier_id** | [**str**](.md)|  | 
 **contact_id** | [**str**](.md)| The unique identifier for the contact to return | 

### Return type

[**ContactDto**](ContactDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_contacts**
> list[ContactDto] get_company_contacts(supplier_id, first_name=first_name, last_name=last_name, job_role=job_role, contact_ids=contact_ids, search_query=search_query, page_number=page_number, page_size=page_size, order_by=order_by)

Returns a list of all contacts meeting the request criteria

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.ContactsApi()
supplier_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
first_name = 'first_name_example' # str | The contact's first name (optional)
last_name = 'last_name_example' # str | The contact's last name (optional)
job_role = 'job_role_example' # str | The contact's job role (optional)
contact_ids = ['contact_ids_example'] # list[str] |  (optional)
search_query = 'search_query_example' # str |  (optional)
page_number = 56 # int |  (optional)
page_size = 56 # int |  (optional)
order_by = 'order_by_example' # str |  (optional)

try:
    # Returns a list of all contacts meeting the request criteria
    api_response = api_instance.get_company_contacts(supplier_id, first_name=first_name, last_name=last_name, job_role=job_role, contact_ids=contact_ids, search_query=search_query, page_number=page_number, page_size=page_size, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->get_company_contacts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supplier_id** | [**str**](.md)|  | 
 **first_name** | **str**| The contact&#x27;s first name | [optional] 
 **last_name** | **str**| The contact&#x27;s last name | [optional] 
 **job_role** | **str**| The contact&#x27;s job role | [optional] 
 **contact_ids** | [**list[str]**](str.md)|  | [optional] 
 **search_query** | **str**|  | [optional] 
 **page_number** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **order_by** | **str**|  | [optional] 

### Return type

[**list[ContactDto]**](ContactDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contacts**
> list[ContactDto] get_contacts(first_name=first_name, last_name=last_name, job_role=job_role, contact_ids=contact_ids, search_query=search_query, page_number=page_number, page_size=page_size, order_by=order_by)

Returns a list of contacts meeting the request criteria

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.ContactsApi()
first_name = 'first_name_example' # str | The contact's first name (optional)
last_name = 'last_name_example' # str | The contact's last name (optional)
job_role = 'job_role_example' # str | The contact's job role (optional)
contact_ids = ['contact_ids_example'] # list[str] |  (optional)
search_query = 'search_query_example' # str |  (optional)
page_number = 56 # int |  (optional)
page_size = 56 # int |  (optional)
order_by = 'order_by_example' # str |  (optional)

try:
    # Returns a list of contacts meeting the request criteria
    api_response = api_instance.get_contacts(first_name=first_name, last_name=last_name, job_role=job_role, contact_ids=contact_ids, search_query=search_query, page_number=page_number, page_size=page_size, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->get_contacts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **first_name** | **str**| The contact&#x27;s first name | [optional] 
 **last_name** | **str**| The contact&#x27;s last name | [optional] 
 **job_role** | **str**| The contact&#x27;s job role | [optional] 
 **contact_ids** | [**list[str]**](str.md)|  | [optional] 
 **search_query** | **str**|  | [optional] 
 **page_number** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **order_by** | **str**|  | [optional] 

### Return type

[**list[ContactDto]**](ContactDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

