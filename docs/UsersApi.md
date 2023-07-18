# authenticate_supply_chain.UsersApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_company_user**](UsersApi.md#get_company_user) | **GET** /api/v1/Suppliers/{supplierId}/Users/{userId} | Returns a specified user
[**get_company_users**](UsersApi.md#get_company_users) | **GET** /api/v1/Suppliers/{supplierId}/Users | Returns a list of all users meeting the request criteria
[**get_users**](UsersApi.md#get_users) | **GET** /api/v1/Users | Returns a list of users meeting the request criteria

# **get_company_user**
> UserDto get_company_user(supplier_id, user_id)

Returns a specified user

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.UsersApi()
supplier_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
user_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The unique identifier for the user to return

try:
    # Returns a specified user
    api_response = api_instance.get_company_user(supplier_id, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_company_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supplier_id** | [**str**](.md)|  | 
 **user_id** | [**str**](.md)| The unique identifier for the user to return | 

### Return type

[**UserDto**](UserDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_users**
> list[UserDto] get_company_users(supplier_id, user_ids=user_ids, include_linked_users=include_linked_users, include_denied_users=include_denied_users, search_query=search_query, page_number=page_number, page_size=page_size, order_by=order_by)

Returns a list of all users meeting the request criteria

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.UsersApi()
supplier_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
user_ids = ['user_ids_example'] # list[str] |  (optional)
include_linked_users = true # bool | Include users with active linked access to a company (optional)
include_denied_users = true # bool | Include users which have a latest status of denied (optional)
search_query = 'search_query_example' # str |  (optional)
page_number = 56 # int |  (optional)
page_size = 56 # int |  (optional)
order_by = 'order_by_example' # str |  (optional)

try:
    # Returns a list of all users meeting the request criteria
    api_response = api_instance.get_company_users(supplier_id, user_ids=user_ids, include_linked_users=include_linked_users, include_denied_users=include_denied_users, search_query=search_query, page_number=page_number, page_size=page_size, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_company_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supplier_id** | [**str**](.md)|  | 
 **user_ids** | [**list[str]**](str.md)|  | [optional] 
 **include_linked_users** | **bool**| Include users with active linked access to a company | [optional] 
 **include_denied_users** | **bool**| Include users which have a latest status of denied | [optional] 
 **search_query** | **str**|  | [optional] 
 **page_number** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **order_by** | **str**|  | [optional] 

### Return type

[**list[UserDto]**](UserDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users**
> list[UserDto] get_users(user_ids=user_ids, include_linked_users=include_linked_users, include_denied_users=include_denied_users, search_query=search_query, page_number=page_number, page_size=page_size, order_by=order_by)

Returns a list of users meeting the request criteria

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.UsersApi()
user_ids = ['user_ids_example'] # list[str] |  (optional)
include_linked_users = true # bool | Include users with active linked access to a company (optional)
include_denied_users = true # bool | Include users which have a latest status of denied (optional)
search_query = 'search_query_example' # str |  (optional)
page_number = 56 # int |  (optional)
page_size = 56 # int |  (optional)
order_by = 'order_by_example' # str |  (optional)

try:
    # Returns a list of users meeting the request criteria
    api_response = api_instance.get_users(user_ids=user_ids, include_linked_users=include_linked_users, include_denied_users=include_denied_users, search_query=search_query, page_number=page_number, page_size=page_size, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_ids** | [**list[str]**](str.md)|  | [optional] 
 **include_linked_users** | **bool**| Include users with active linked access to a company | [optional] 
 **include_denied_users** | **bool**| Include users which have a latest status of denied | [optional] 
 **search_query** | **str**|  | [optional] 
 **page_number** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **order_by** | **str**|  | [optional] 

### Return type

[**list[UserDto]**](UserDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

