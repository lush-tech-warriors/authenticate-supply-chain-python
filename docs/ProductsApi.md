# authenticate_supply_chain.ProductsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_products_post**](ProductsApi.md#api_v1_products_post) | **POST** /api/v1/Products | Create a new product.      Product Name and product reference together must be unique
[**api_v1_products_product_id_image_get**](ProductsApi.md#api_v1_products_product_id_image_get) | **GET** /api/v1/Products/{productId}/Image | Returns the image for the product
[**delete_product**](ProductsApi.md#delete_product) | **DELETE** /api/v1/Products/{productId} | Delete a product. Only products with no accepted or pending product links can be deleted.
[**get_product**](ProductsApi.md#get_product) | **GET** /api/v1/Products/{productId} | Returns a specified product
[**get_product_for_category**](ProductsApi.md#get_product_for_category) | **GET** /api/v1/Categories/{categoryId}/Products/{productId} | Returns a specified product in a given category
[**get_product_status**](ProductsApi.md#get_product_status) | **GET** /api/v1/Products/{productId}/Status | Returns the latest status for the product
[**get_products**](ProductsApi.md#get_products) | **GET** /api/v1/Products | Returns a list of all products meeting the request criteria
[**get_products_for_category**](ProductsApi.md#get_products_for_category) | **GET** /api/v1/Categories/{categoryId}/Products | Returns a list of all products meeting the request criteria in this category
[**patch_product**](ProductsApi.md#patch_product) | **PATCH** /api/v1/Products/{productId} | Partially update a product. Only provided fields will be updated
[**update_product**](ProductsApi.md#update_product) | **PUT** /api/v1/Products/{productId} | Fully update a product. All elements must be supplied or fields will be updated to default values

# **api_v1_products_post**
> ProductDto api_v1_products_post(body=body)

Create a new product.      Product Name and product reference together must be unique

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.ProductsApi()
body = authenticate_supply_chain.ProductForCreationDto() # ProductForCreationDto |  (optional)

try:
    # Create a new product.      Product Name and product reference together must be unique
    api_response = api_instance.api_v1_products_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->api_v1_products_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProductForCreationDto**](ProductForCreationDto.md)|  | [optional] 

### Return type

[**ProductDto**](ProductDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_products_product_id_image_get**
> Stream api_v1_products_product_id_image_get(product_id)

Returns the image for the product

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.ProductsApi()
product_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The unique identifier for the product

try:
    # Returns the image for the product
    api_response = api_instance.api_v1_products_product_id_image_get(product_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->api_v1_products_product_id_image_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | [**str**](.md)| The unique identifier for the product | 

### Return type

[**Stream**](Stream.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_product**
> delete_product(product_id)

Delete a product. Only products with no accepted or pending product links can be deleted.

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.ProductsApi()
product_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Delete a product. Only products with no accepted or pending product links can be deleted.
    api_instance.delete_product(product_id)
except ApiException as e:
    print("Exception when calling ProductsApi->delete_product: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | [**str**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product**
> ProductDto get_product(product_id)

Returns a specified product

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.ProductsApi()
product_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The unique identifier for the product to return

try:
    # Returns a specified product
    api_response = api_instance.get_product(product_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->get_product: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | [**str**](.md)| The unique identifier for the product to return | 

### Return type

[**ProductDto**](ProductDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product_for_category**
> ProductDto get_product_for_category(category_id, product_id)

Returns a specified product in a given category

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.ProductsApi()
category_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The unique identifier for the category
product_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The unique identifier for the product to return

try:
    # Returns a specified product in a given category
    api_response = api_instance.get_product_for_category(category_id, product_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->get_product_for_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | [**str**](.md)| The unique identifier for the category | 
 **product_id** | [**str**](.md)| The unique identifier for the product to return | 

### Return type

[**ProductDto**](ProductDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product_status**
> int get_product_status(product_id)

Returns the latest status for the product

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.ProductsApi()
product_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The unique identifier for the product

try:
    # Returns the latest status for the product
    api_response = api_instance.get_product_status(product_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->get_product_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | [**str**](.md)| The unique identifier for the product | 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_products**
> list[ProductDto] get_products(start_date=start_date, end_date=end_date, search_query=search_query, page_number=page_number, page_size=page_size, order_by=order_by)

Returns a list of all products meeting the request criteria

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.ProductsApi()
start_date = '2013-10-20T19:20:30+01:00' # datetime | Limit the returned products to those where the supply chain was updated on or after this date (optional)
end_date = '2013-10-20T19:20:30+01:00' # datetime | Limit the returned products to those where the supply chain was updated before this date (optional)
search_query = 'search_query_example' # str |  (optional)
page_number = 56 # int |  (optional)
page_size = 56 # int |  (optional)
order_by = 'order_by_example' # str |  (optional)

try:
    # Returns a list of all products meeting the request criteria
    api_response = api_instance.get_products(start_date=start_date, end_date=end_date, search_query=search_query, page_number=page_number, page_size=page_size, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->get_products: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**| Limit the returned products to those where the supply chain was updated on or after this date | [optional] 
 **end_date** | **datetime**| Limit the returned products to those where the supply chain was updated before this date | [optional] 
 **search_query** | **str**|  | [optional] 
 **page_number** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **order_by** | **str**|  | [optional] 

### Return type

[**list[ProductDto]**](ProductDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_products_for_category**
> list[ProductDto] get_products_for_category(category_id, start_date=start_date, end_date=end_date, search_query=search_query, page_number=page_number, page_size=page_size, order_by=order_by)

Returns a list of all products meeting the request criteria in this category

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.ProductsApi()
category_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The unique identifier for the category
start_date = '2013-10-20T19:20:30+01:00' # datetime | Limit the returned products to those where the supply chain was updated on or after this date (optional)
end_date = '2013-10-20T19:20:30+01:00' # datetime | Limit the returned products to those where the supply chain was updated before this date (optional)
search_query = 'search_query_example' # str |  (optional)
page_number = 56 # int |  (optional)
page_size = 56 # int |  (optional)
order_by = 'order_by_example' # str |  (optional)

try:
    # Returns a list of all products meeting the request criteria in this category
    api_response = api_instance.get_products_for_category(category_id, start_date=start_date, end_date=end_date, search_query=search_query, page_number=page_number, page_size=page_size, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->get_products_for_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | [**str**](.md)| The unique identifier for the category | 
 **start_date** | **datetime**| Limit the returned products to those where the supply chain was updated on or after this date | [optional] 
 **end_date** | **datetime**| Limit the returned products to those where the supply chain was updated before this date | [optional] 
 **search_query** | **str**|  | [optional] 
 **page_number** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **order_by** | **str**|  | [optional] 

### Return type

[**list[ProductDto]**](ProductDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_product**
> ProductDto patch_product(product_id, body=body)

Partially update a product. Only provided fields will be updated

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.ProductsApi()
product_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = [authenticate_supply_chain.Operation()] # list[Operation] |  (optional)

try:
    # Partially update a product. Only provided fields will be updated
    api_response = api_instance.patch_product(product_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->patch_product: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | [**str**](.md)|  | 
 **body** | [**list[Operation]**](Operation.md)|  | [optional] 

### Return type

[**ProductDto**](ProductDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_product**
> ProductDto update_product(product_id, body=body)

Fully update a product. All elements must be supplied or fields will be updated to default values

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.ProductsApi()
product_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = authenticate_supply_chain.ProductForUpdateDto() # ProductForUpdateDto |  (optional)

try:
    # Fully update a product. All elements must be supplied or fields will be updated to default values
    api_response = api_instance.update_product(product_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->update_product: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | [**str**](.md)|  | 
 **body** | [**ProductForUpdateDto**](ProductForUpdateDto.md)|  | [optional] 

### Return type

[**ProductDto**](ProductDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

