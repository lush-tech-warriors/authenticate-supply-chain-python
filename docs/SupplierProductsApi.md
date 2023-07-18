# authenticate_supply_chain.SupplierProductsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_supplier_product**](SupplierProductsApi.md#get_supplier_product) | **GET** /api/v1/Suppliers/{supplierId}/Products/{productId} | Returns a specified supplier product
[**get_supplier_products**](SupplierProductsApi.md#get_supplier_products) | **GET** /api/v1/Suppliers/{supplierId}/Products | Returns a list of all products meeting the request criteria

# **get_supplier_product**
> SupplierProductDto get_supplier_product(supplier_id, product_id)

Returns a specified supplier product

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.SupplierProductsApi()
supplier_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The unique identifier of the supplier
product_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The unique identifier for the product to return

try:
    # Returns a specified supplier product
    api_response = api_instance.get_supplier_product(supplier_id, product_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SupplierProductsApi->get_supplier_product: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supplier_id** | [**str**](.md)| The unique identifier of the supplier | 
 **product_id** | [**str**](.md)| The unique identifier for the product to return | 

### Return type

[**SupplierProductDto**](SupplierProductDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_supplier_products**
> list[SupplierProductDto] get_supplier_products(supplier_id, start_date=start_date, end_date=end_date, search_query=search_query, page_number=page_number, page_size=page_size, order_by=order_by)

Returns a list of all products meeting the request criteria

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.SupplierProductsApi()
supplier_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The unique identifier of the supplier
start_date = '2013-10-20T19:20:30+01:00' # datetime | Limit the returned products to those where the supply chain was updated on or after this date (optional)
end_date = '2013-10-20T19:20:30+01:00' # datetime | Limit the returned products to those where the supply chain was updated before this date (optional)
search_query = 'search_query_example' # str |  (optional)
page_number = 56 # int |  (optional)
page_size = 56 # int |  (optional)
order_by = 'order_by_example' # str |  (optional)

try:
    # Returns a list of all products meeting the request criteria
    api_response = api_instance.get_supplier_products(supplier_id, start_date=start_date, end_date=end_date, search_query=search_query, page_number=page_number, page_size=page_size, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SupplierProductsApi->get_supplier_products: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supplier_id** | [**str**](.md)| The unique identifier of the supplier | 
 **start_date** | **datetime**| Limit the returned products to those where the supply chain was updated on or after this date | [optional] 
 **end_date** | **datetime**| Limit the returned products to those where the supply chain was updated before this date | [optional] 
 **search_query** | **str**|  | [optional] 
 **page_number** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **order_by** | **str**|  | [optional] 

### Return type

[**list[SupplierProductDto]**](SupplierProductDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

