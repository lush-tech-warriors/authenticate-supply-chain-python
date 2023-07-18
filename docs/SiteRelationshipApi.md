# authenticate_supply_chain.SiteRelationshipApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_site_relationship_site_id_patch**](SiteRelationshipApi.md#api_v1_site_relationship_site_id_patch) | **PATCH** /api/v1/SiteRelationship/{siteId} | Partially update a site relationship. Only provided fields will be updated
[**api_v1_site_relationship_site_id_post**](SiteRelationshipApi.md#api_v1_site_relationship_site_id_post) | **POST** /api/v1/SiteRelationship/{siteId} | Create a new site relationship
[**api_v1_site_relationship_site_id_put**](SiteRelationshipApi.md#api_v1_site_relationship_site_id_put) | **PUT** /api/v1/SiteRelationship/{siteId} | Update an existing site relationship
[**get_all_site_relationship_values**](SiteRelationshipApi.md#get_all_site_relationship_values) | **GET** /api/v1/SiteRelationship/{siteId}/History | Returns a specified site relationship&#x27;s values based on viewing company
[**get_site_relationship**](SiteRelationshipApi.md#get_site_relationship) | **GET** /api/v1/SiteRelationship/{siteId} | Returns a specified site relationship based on viewing company

# **api_v1_site_relationship_site_id_patch**
> SiteRelationshipDto api_v1_site_relationship_site_id_patch(site_id, body=body)

Partially update a site relationship. Only provided fields will be updated

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.SiteRelationshipApi()
site_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = [authenticate_supply_chain.Operation()] # list[Operation] |  (optional)

try:
    # Partially update a site relationship. Only provided fields will be updated
    api_response = api_instance.api_v1_site_relationship_site_id_patch(site_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteRelationshipApi->api_v1_site_relationship_site_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | [**str**](.md)|  | 
 **body** | [**list[Operation]**](Operation.md)|  | [optional] 

### Return type

[**SiteRelationshipDto**](SiteRelationshipDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_site_relationship_site_id_post**
> SiteRelationshipDto api_v1_site_relationship_site_id_post(site_id, body=body)

Create a new site relationship

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.SiteRelationshipApi()
site_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = authenticate_supply_chain.SiteRelationshipForManipulationDto() # SiteRelationshipForManipulationDto |  (optional)

try:
    # Create a new site relationship
    api_response = api_instance.api_v1_site_relationship_site_id_post(site_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteRelationshipApi->api_v1_site_relationship_site_id_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | [**str**](.md)|  | 
 **body** | [**SiteRelationshipForManipulationDto**](SiteRelationshipForManipulationDto.md)|  | [optional] 

### Return type

[**SiteRelationshipDto**](SiteRelationshipDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_site_relationship_site_id_put**
> SiteRelationshipDto api_v1_site_relationship_site_id_put(site_id, body=body)

Update an existing site relationship

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.SiteRelationshipApi()
site_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = authenticate_supply_chain.SiteRelationshipForManipulationDto() # SiteRelationshipForManipulationDto |  (optional)

try:
    # Update an existing site relationship
    api_response = api_instance.api_v1_site_relationship_site_id_put(site_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteRelationshipApi->api_v1_site_relationship_site_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | [**str**](.md)|  | 
 **body** | [**SiteRelationshipForManipulationDto**](SiteRelationshipForManipulationDto.md)|  | [optional] 

### Return type

[**SiteRelationshipDto**](SiteRelationshipDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_site_relationship_values**
> list[SiteRelationshipValuesDto] get_all_site_relationship_values(site_id, order_by=order_by, search_query=search_query, page_number=page_number, page_size=page_size)

Returns a specified site relationship's values based on viewing company

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.SiteRelationshipApi()
site_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The unique identifier for the company to site relationship to return
order_by = 'order_by_example' # str | Order the results (optional)
search_query = 'search_query_example' # str |  (optional)
page_number = 56 # int |  (optional)
page_size = 56 # int |  (optional)

try:
    # Returns a specified site relationship's values based on viewing company
    api_response = api_instance.get_all_site_relationship_values(site_id, order_by=order_by, search_query=search_query, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteRelationshipApi->get_all_site_relationship_values: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | [**str**](.md)| The unique identifier for the company to site relationship to return | 
 **order_by** | **str**| Order the results | [optional] 
 **search_query** | **str**|  | [optional] 
 **page_number** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 

### Return type

[**list[SiteRelationshipValuesDto]**](SiteRelationshipValuesDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_site_relationship**
> SiteRelationshipDto get_site_relationship(site_id)

Returns a specified site relationship based on viewing company

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.SiteRelationshipApi()
site_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The unique identifier for the company to site relationship to return

try:
    # Returns a specified site relationship based on viewing company
    api_response = api_instance.get_site_relationship(site_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteRelationshipApi->get_site_relationship: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | [**str**](.md)| The unique identifier for the company to site relationship to return | 

### Return type

[**SiteRelationshipDto**](SiteRelationshipDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

