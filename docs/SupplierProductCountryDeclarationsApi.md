# authenticate_supply_chain.SupplierProductCountryDeclarationsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_supplier_product_country_declarations_product_id_post**](SupplierProductCountryDeclarationsApi.md#api_v1_supplier_product_country_declarations_product_id_post) | **POST** /api/v1/SupplierProductCountryDeclarations/{productId} | Create country declaration for a specified product line
[**get_supplier_product_country_declarations**](SupplierProductCountryDeclarationsApi.md#get_supplier_product_country_declarations) | **GET** /api/v1/SupplierProductCountryDeclarations/{productId} | Returns declared countries for a specific product line

# **api_v1_supplier_product_country_declarations_product_id_post**
> ProductLineCountryDeclarationDto api_v1_supplier_product_country_declarations_product_id_post(product_id, body=body)

Create country declaration for a specified product line

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.SupplierProductCountryDeclarationsApi()
product_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = authenticate_supply_chain.ProductLineCountryDeclarationForCreationDto() # ProductLineCountryDeclarationForCreationDto |  (optional)

try:
    # Create country declaration for a specified product line
    api_response = api_instance.api_v1_supplier_product_country_declarations_product_id_post(product_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SupplierProductCountryDeclarationsApi->api_v1_supplier_product_country_declarations_product_id_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | [**str**](.md)|  | 
 **body** | [**ProductLineCountryDeclarationForCreationDto**](ProductLineCountryDeclarationForCreationDto.md)|  | [optional] 

### Return type

[**ProductLineCountryDeclarationDto**](ProductLineCountryDeclarationDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_supplier_product_country_declarations**
> CountryDto get_supplier_product_country_declarations(product_id, search_query=search_query, page_number=page_number, page_size=page_size, order_by=order_by)

Returns declared countries for a specific product line

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.SupplierProductCountryDeclarationsApi()
product_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The unique identifier for the product to return
search_query = 'search_query_example' # str |  (optional)
page_number = 56 # int |  (optional)
page_size = 56 # int |  (optional)
order_by = 'order_by_example' # str |  (optional)

try:
    # Returns declared countries for a specific product line
    api_response = api_instance.get_supplier_product_country_declarations(product_id, search_query=search_query, page_number=page_number, page_size=page_size, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SupplierProductCountryDeclarationsApi->get_supplier_product_country_declarations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | [**str**](.md)| The unique identifier for the product to return | 
 **search_query** | **str**|  | [optional] 
 **page_number** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **order_by** | **str**|  | [optional] 

### Return type

[**CountryDto**](CountryDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

