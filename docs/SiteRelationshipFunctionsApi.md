# authenticate_supply_chain.SiteRelationshipFunctionsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_site_relationship_functions_get**](SiteRelationshipFunctionsApi.md#api_v1_site_relationship_functions_get) | **GET** /api/v1/SiteRelationshipFunctions | Returns a list of site relationship functions based on viewing company
[**api_v1_site_relationship_functions_post**](SiteRelationshipFunctionsApi.md#api_v1_site_relationship_functions_post) | **POST** /api/v1/SiteRelationshipFunctions | Create a new site relationship function

# **api_v1_site_relationship_functions_get**
> list[str] api_v1_site_relationship_functions_get()

Returns a list of site relationship functions based on viewing company

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.SiteRelationshipFunctionsApi()

try:
    # Returns a list of site relationship functions based on viewing company
    api_response = api_instance.api_v1_site_relationship_functions_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteRelationshipFunctionsApi->api_v1_site_relationship_functions_get: %s\n" % e)
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

# **api_v1_site_relationship_functions_post**
> str api_v1_site_relationship_functions_post(body=body)

Create a new site relationship function

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.SiteRelationshipFunctionsApi()
body = authenticate_supply_chain.SiteRelationshipFunctionDto() # SiteRelationshipFunctionDto |  (optional)

try:
    # Create a new site relationship function
    api_response = api_instance.api_v1_site_relationship_functions_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteRelationshipFunctionsApi->api_v1_site_relationship_functions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SiteRelationshipFunctionDto**](SiteRelationshipFunctionDto.md)|  | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

