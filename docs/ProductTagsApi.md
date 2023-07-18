# authenticate_supply_chain.ProductTagsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_product_tags_get**](ProductTagsApi.md#api_v1_product_tags_get) | **GET** /api/v1/ProductTags | Returns a list of all product tags meeting the request criteria
[**api_v1_product_tags_post**](ProductTagsApi.md#api_v1_product_tags_post) | **POST** /api/v1/ProductTags | 
[**api_v1_product_tags_product_line_id_get**](ProductTagsApi.md#api_v1_product_tags_product_line_id_get) | **GET** /api/v1/ProductTags/{productLineId} | Returns a list of all product tags for a product, meeting the request criteria
[**api_v1_product_tags_product_line_id_post**](ProductTagsApi.md#api_v1_product_tags_product_line_id_post) | **POST** /api/v1/ProductTags/{productLineId} | 
[**delete_tag**](ProductTagsApi.md#delete_tag) | **DELETE** /api/v1/ProductLine/{productLineId}/ProductTags/{tagId} | Deletes a tag associated with a product line.

# **api_v1_product_tags_get**
> list[TagDto] api_v1_product_tags_get(search_query=search_query, page_number=page_number, page_size=page_size, order_by=order_by)

Returns a list of all product tags meeting the request criteria

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.ProductTagsApi()
search_query = 'search_query_example' # str |  (optional)
page_number = 56 # int |  (optional)
page_size = 56 # int |  (optional)
order_by = 'order_by_example' # str |  (optional)

try:
    # Returns a list of all product tags meeting the request criteria
    api_response = api_instance.api_v1_product_tags_get(search_query=search_query, page_number=page_number, page_size=page_size, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductTagsApi->api_v1_product_tags_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_query** | **str**|  | [optional] 
 **page_number** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **order_by** | **str**|  | [optional] 

### Return type

[**list[TagDto]**](TagDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_product_tags_post**
> TagDto api_v1_product_tags_post()



### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.ProductTagsApi()

try:
    api_response = api_instance.api_v1_product_tags_post()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductTagsApi->api_v1_product_tags_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TagDto**](TagDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_product_tags_product_line_id_get**
> list[TagDto] api_v1_product_tags_product_line_id_get(product_line_id, search_query=search_query, page_number=page_number, page_size=page_size, order_by=order_by)

Returns a list of all product tags for a product, meeting the request criteria

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.ProductTagsApi()
product_line_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
search_query = 'search_query_example' # str |  (optional)
page_number = 56 # int |  (optional)
page_size = 56 # int |  (optional)
order_by = 'order_by_example' # str |  (optional)

try:
    # Returns a list of all product tags for a product, meeting the request criteria
    api_response = api_instance.api_v1_product_tags_product_line_id_get(product_line_id, search_query=search_query, page_number=page_number, page_size=page_size, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductTagsApi->api_v1_product_tags_product_line_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_line_id** | [**str**](.md)|  | 
 **search_query** | **str**|  | [optional] 
 **page_number** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **order_by** | **str**|  | [optional] 

### Return type

[**list[TagDto]**](TagDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_product_tags_product_line_id_post**
> ProductTagDto api_v1_product_tags_product_line_id_post(product_line_id, body=body)



### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.ProductTagsApi()
product_line_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = 56 # int |  (optional)

try:
    api_response = api_instance.api_v1_product_tags_product_line_id_post(product_line_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductTagsApi->api_v1_product_tags_product_line_id_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_line_id** | [**str**](.md)|  | 
 **body** | [**int**](int.md)|  | [optional] 

### Return type

[**ProductTagDto**](ProductTagDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tag**
> delete_tag(product_line_id, tag_id)

Deletes a tag associated with a product line.

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.ProductTagsApi()
product_line_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
tag_id = 56 # int | 

try:
    # Deletes a tag associated with a product line.
    api_instance.delete_tag(product_line_id, tag_id)
except ApiException as e:
    print("Exception when calling ProductTagsApi->delete_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_line_id** | [**str**](.md)|  | 
 **tag_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

