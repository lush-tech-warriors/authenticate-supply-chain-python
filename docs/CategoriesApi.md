# authenticate_supply_chain.CategoriesApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_categories_post**](CategoriesApi.md#api_v1_categories_post) | **POST** /api/v1/Categories | Create a new Categories
[**delete_category**](CategoriesApi.md#delete_category) | **DELETE** /api/v1/Categories/{categoryId} | Delete a Categories. Only empty categories can be deleted. If the Categories contains products or other categories the delete will fail
[**get_categories**](CategoriesApi.md#get_categories) | **GET** /api/v1/Categories | Returns a list of all categories meeting the request criteria
[**get_category**](CategoriesApi.md#get_category) | **GET** /api/v1/Categories/{categoryId} | Returns a specified Categories
[**patch_category**](CategoriesApi.md#patch_category) | **PATCH** /api/v1/Categories/{categoryId} | Partially update a Categories. Only provided fields will be updated
[**update_category**](CategoriesApi.md#update_category) | **PUT** /api/v1/Categories/{categoryId} | Fully update a Categories. All elements must be supplied or fields will be updated to default values

# **api_v1_categories_post**
> CategoryDto api_v1_categories_post(body=body)

Create a new Categories

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.CategoriesApi()
body = authenticate_supply_chain.CategoryForCreationDto() # CategoryForCreationDto |  (optional)

try:
    # Create a new Categories
    api_response = api_instance.api_v1_categories_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoriesApi->api_v1_categories_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CategoryForCreationDto**](CategoryForCreationDto.md)|  | [optional] 

### Return type

[**CategoryDto**](CategoryDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_category**
> delete_category(category_id)

Delete a Categories. Only empty categories can be deleted. If the Categories contains products or other categories the delete will fail

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.CategoriesApi()
category_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Delete a Categories. Only empty categories can be deleted. If the Categories contains products or other categories the delete will fail
    api_instance.delete_category(category_id)
except ApiException as e:
    print("Exception when calling CategoriesApi->delete_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | [**str**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_categories**
> list[CategoryDto] get_categories(search_query=search_query, page_number=page_number, page_size=page_size, order_by=order_by)

Returns a list of all categories meeting the request criteria

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.CategoriesApi()
search_query = 'search_query_example' # str |  (optional)
page_number = 56 # int |  (optional)
page_size = 56 # int |  (optional)
order_by = 'order_by_example' # str |  (optional)

try:
    # Returns a list of all categories meeting the request criteria
    api_response = api_instance.get_categories(search_query=search_query, page_number=page_number, page_size=page_size, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoriesApi->get_categories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_query** | **str**|  | [optional] 
 **page_number** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **order_by** | **str**|  | [optional] 

### Return type

[**list[CategoryDto]**](CategoryDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_category**
> CategoryDto get_category(category_id)

Returns a specified Categories

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.CategoriesApi()
category_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The unique identifier for the Categories to return

try:
    # Returns a specified Categories
    api_response = api_instance.get_category(category_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoriesApi->get_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | [**str**](.md)| The unique identifier for the Categories to return | 

### Return type

[**CategoryDto**](CategoryDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_category**
> CategoryDto patch_category(category_id, body=body)

Partially update a Categories. Only provided fields will be updated

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.CategoriesApi()
category_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = [authenticate_supply_chain.Operation()] # list[Operation] |  (optional)

try:
    # Partially update a Categories. Only provided fields will be updated
    api_response = api_instance.patch_category(category_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoriesApi->patch_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | [**str**](.md)|  | 
 **body** | [**list[Operation]**](Operation.md)|  | [optional] 

### Return type

[**CategoryDto**](CategoryDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_category**
> CategoryDto update_category(category_id, body=body)

Fully update a Categories. All elements must be supplied or fields will be updated to default values

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.CategoriesApi()
category_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = authenticate_supply_chain.CategoryForUpdateDto() # CategoryForUpdateDto |  (optional)

try:
    # Fully update a Categories. All elements must be supplied or fields will be updated to default values
    api_response = api_instance.update_category(category_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoriesApi->update_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | [**str**](.md)|  | 
 **body** | [**CategoryForUpdateDto**](CategoryForUpdateDto.md)|  | [optional] 

### Return type

[**CategoryDto**](CategoryDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

