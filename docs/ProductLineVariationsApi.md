# authenticate_supply_chain.ProductLineVariationsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_product_line_variations_product_line_variation_id_delete**](ProductLineVariationsApi.md#api_v1_product_line_variations_product_line_variation_id_delete) | **DELETE** /api/v1/ProductLineVariations/{productLineVariationId} | Delete a product line variation
[**api_v1_product_line_variations_product_line_variation_id_put**](ProductLineVariationsApi.md#api_v1_product_line_variations_product_line_variation_id_put) | **PUT** /api/v1/ProductLineVariations/{productLineVariationId} | Fully update a product line variation. All elements must be supplied or fields will be updated to default values
[**api_v1_product_lines_product_line_id_product_line_variations_post**](ProductLineVariationsApi.md#api_v1_product_lines_product_line_id_product_line_variations_post) | **POST** /api/v1/ProductLines/{productLineId}/ProductLineVariations | Create a new product line variation.
[**list**](ProductLineVariationsApi.md#list) | **GET** /api/v1/ProductLineVariations | Returns a list of all variations associated with your company&#x27;s product lines.
[**list_by_product_line**](ProductLineVariationsApi.md#list_by_product_line) | **GET** /api/v1/ProductLines/{productLineId}/ProductLineVariations | Returns a list of all variations associated with a product line.

# **api_v1_product_line_variations_product_line_variation_id_delete**
> api_v1_product_line_variations_product_line_variation_id_delete(product_line_variation_id)

Delete a product line variation

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.ProductLineVariationsApi()
product_line_variation_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Delete a product line variation
    api_instance.api_v1_product_line_variations_product_line_variation_id_delete(product_line_variation_id)
except ApiException as e:
    print("Exception when calling ProductLineVariationsApi->api_v1_product_line_variations_product_line_variation_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_line_variation_id** | [**str**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_product_line_variations_product_line_variation_id_put**
> ProductLineVariationDto api_v1_product_line_variations_product_line_variation_id_put(product_line_variation_id, body=body)

Fully update a product line variation. All elements must be supplied or fields will be updated to default values

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.ProductLineVariationsApi()
product_line_variation_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = authenticate_supply_chain.ProductLineVariationForManipulationDto() # ProductLineVariationForManipulationDto |  (optional)

try:
    # Fully update a product line variation. All elements must be supplied or fields will be updated to default values
    api_response = api_instance.api_v1_product_line_variations_product_line_variation_id_put(product_line_variation_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductLineVariationsApi->api_v1_product_line_variations_product_line_variation_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_line_variation_id** | [**str**](.md)|  | 
 **body** | [**ProductLineVariationForManipulationDto**](ProductLineVariationForManipulationDto.md)|  | [optional] 

### Return type

[**ProductLineVariationDto**](ProductLineVariationDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_product_lines_product_line_id_product_line_variations_post**
> ProductLineVariationDto api_v1_product_lines_product_line_id_product_line_variations_post(product_line_id, body=body)

Create a new product line variation.

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.ProductLineVariationsApi()
product_line_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = authenticate_supply_chain.ProductLineVariationForManipulationDto() # ProductLineVariationForManipulationDto |  (optional)

try:
    # Create a new product line variation.
    api_response = api_instance.api_v1_product_lines_product_line_id_product_line_variations_post(product_line_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductLineVariationsApi->api_v1_product_lines_product_line_id_product_line_variations_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_line_id** | [**str**](.md)|  | 
 **body** | [**ProductLineVariationForManipulationDto**](ProductLineVariationForManipulationDto.md)|  | [optional] 

### Return type

[**ProductLineVariationDto**](ProductLineVariationDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> list[ProductLineVariationDto] list(product_line_id=product_line_id, name=name, sku=sku, pack_size=pack_size, legal_name=legal_name, language=language, search_query=search_query, page_number=page_number, page_size=page_size, order_by=order_by)

Returns a list of all variations associated with your company's product lines.

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.ProductLineVariationsApi()
product_line_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Limit the returned variations based on a product line (optional)
name = 'name_example' # str | Limit the returned variations based on name (optional)
sku = 'sku_example' # str | Limit the returned variations based on SKU (optional)
pack_size = 'pack_size_example' # str | Limit the returned variations based on pack size (optional)
legal_name = 'legal_name_example' # str | Limit the returned variations based on legal name (optional)
language = 'language_example' # str | Limit the returned variations based on language (optional)
search_query = 'search_query_example' # str |  (optional)
page_number = 56 # int |  (optional)
page_size = 56 # int |  (optional)
order_by = 'order_by_example' # str |  (optional)

try:
    # Returns a list of all variations associated with your company's product lines.
    api_response = api_instance.list(product_line_id=product_line_id, name=name, sku=sku, pack_size=pack_size, legal_name=legal_name, language=language, search_query=search_query, page_number=page_number, page_size=page_size, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductLineVariationsApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_line_id** | [**str**](.md)| Limit the returned variations based on a product line | [optional] 
 **name** | **str**| Limit the returned variations based on name | [optional] 
 **sku** | **str**| Limit the returned variations based on SKU | [optional] 
 **pack_size** | **str**| Limit the returned variations based on pack size | [optional] 
 **legal_name** | **str**| Limit the returned variations based on legal name | [optional] 
 **language** | **str**| Limit the returned variations based on language | [optional] 
 **search_query** | **str**|  | [optional] 
 **page_number** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **order_by** | **str**|  | [optional] 

### Return type

[**list[ProductLineVariationDto]**](ProductLineVariationDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_by_product_line**
> list[ProductLineVariationDto] list_by_product_line(product_line_id, product_line_id=product_line_id, name=name, sku=sku, pack_size=pack_size, legal_name=legal_name, language=language, search_query=search_query, page_number=page_number, page_size=page_size, order_by=order_by)

Returns a list of all variations associated with a product line.

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.ProductLineVariationsApi()
product_line_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The product line id
product_line_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Limit the returned variations based on a product line (optional)
name = 'name_example' # str | Limit the returned variations based on name (optional)
sku = 'sku_example' # str | Limit the returned variations based on SKU (optional)
pack_size = 'pack_size_example' # str | Limit the returned variations based on pack size (optional)
legal_name = 'legal_name_example' # str | Limit the returned variations based on legal name (optional)
language = 'language_example' # str | Limit the returned variations based on language (optional)
search_query = 'search_query_example' # str |  (optional)
page_number = 56 # int |  (optional)
page_size = 56 # int |  (optional)
order_by = 'order_by_example' # str |  (optional)

try:
    # Returns a list of all variations associated with a product line.
    api_response = api_instance.list_by_product_line(product_line_id, product_line_id=product_line_id, name=name, sku=sku, pack_size=pack_size, legal_name=legal_name, language=language, search_query=search_query, page_number=page_number, page_size=page_size, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductLineVariationsApi->list_by_product_line: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_line_id** | [**str**](.md)| The product line id | 
 **product_line_id** | [**str**](.md)| Limit the returned variations based on a product line | [optional] 
 **name** | **str**| Limit the returned variations based on name | [optional] 
 **sku** | **str**| Limit the returned variations based on SKU | [optional] 
 **pack_size** | **str**| Limit the returned variations based on pack size | [optional] 
 **legal_name** | **str**| Limit the returned variations based on legal name | [optional] 
 **language** | **str**| Limit the returned variations based on language | [optional] 
 **search_query** | **str**|  | [optional] 
 **page_number** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **order_by** | **str**|  | [optional] 

### Return type

[**list[ProductLineVariationDto]**](ProductLineVariationDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

