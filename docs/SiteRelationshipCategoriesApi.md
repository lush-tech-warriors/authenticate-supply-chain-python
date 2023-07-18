# authenticate_supply_chain.SiteRelationshipCategoriesApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_site_relationship_categories_get**](SiteRelationshipCategoriesApi.md#api_v1_site_relationship_categories_get) | **GET** /api/v1/SiteRelationshipCategories | Returns a list of site relationship categories based on viewing company
[**api_v1_site_relationship_categories_post**](SiteRelationshipCategoriesApi.md#api_v1_site_relationship_categories_post) | **POST** /api/v1/SiteRelationshipCategories | Create a new site relationship category

# **api_v1_site_relationship_categories_get**
> list[str] api_v1_site_relationship_categories_get()

Returns a list of site relationship categories based on viewing company

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.SiteRelationshipCategoriesApi()

try:
    # Returns a list of site relationship categories based on viewing company
    api_response = api_instance.api_v1_site_relationship_categories_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteRelationshipCategoriesApi->api_v1_site_relationship_categories_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_site_relationship_categories_post**
> str api_v1_site_relationship_categories_post(body=body)

Create a new site relationship category

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.SiteRelationshipCategoriesApi()
body = authenticate_supply_chain.SiteRelationshipCategoryDto() # SiteRelationshipCategoryDto |  (optional)

try:
    # Create a new site relationship category
    api_response = api_instance.api_v1_site_relationship_categories_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteRelationshipCategoriesApi->api_v1_site_relationship_categories_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SiteRelationshipCategoryDto**](SiteRelationshipCategoryDto.md)|  | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

