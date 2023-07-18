# authenticate_supply_chain.CustomerLinksApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_customer_links_product_link_id_accept_post**](CustomerLinksApi.md#api_v1_customer_links_product_link_id_accept_post) | **POST** /api/v1/CustomerLinks/{productLinkId}/Accept | Accept an active product link request to your product (also accepts requests for the same product from the same customer)
[**get_customer_product_link**](CustomerLinksApi.md#get_customer_product_link) | **GET** /api/v1/CustomerLinks/{productLinkId} | Returns a specified customer product link
[**get_customer_product_link_for_product**](CustomerLinksApi.md#get_customer_product_link_for_product) | **GET** /api/v1/Products/{productId}/CustomerLinks/{productLinkId} | For the product with Id {productId}, return a specified customer product link
[**get_customer_product_links**](CustomerLinksApi.md#get_customer_product_links) | **GET** /api/v1/CustomerLinks | Returns a list of all customer product links meeting the request criteria
[**get_customer_product_links_for_product**](CustomerLinksApi.md#get_customer_product_links_for_product) | **GET** /api/v1/Products/{productId}/CustomerLinks | For the product with Id {productId}, return a list of all customer product links meeting the request criteria
[**remove_customer_product_link_for_product**](CustomerLinksApi.md#remove_customer_product_link_for_product) | **POST** /api/v1/Products/{productId}/CustomerLinks/{productLinkId}/Remove | Remove an active product link request to your product

# **api_v1_customer_links_product_link_id_accept_post**
> list[CustomerProductLinkDto] api_v1_customer_links_product_link_id_accept_post(product_link_id, body=body)

Accept an active product link request to your product (also accepts requests for the same product from the same customer)

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.CustomerLinksApi()
product_link_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = authenticate_supply_chain.ProductLinkAcceptDto() # ProductLinkAcceptDto |  (optional)

try:
    # Accept an active product link request to your product (also accepts requests for the same product from the same customer)
    api_response = api_instance.api_v1_customer_links_product_link_id_accept_post(product_link_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerLinksApi->api_v1_customer_links_product_link_id_accept_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_link_id** | [**str**](.md)|  | 
 **body** | [**ProductLinkAcceptDto**](ProductLinkAcceptDto.md)|  | [optional] 

### Return type

[**list[CustomerProductLinkDto]**](CustomerProductLinkDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer_product_link**
> SupplierProductLinkDto get_customer_product_link(product_link_id)

Returns a specified customer product link

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.CustomerLinksApi()
product_link_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The unique identifier for the product link to return

try:
    # Returns a specified customer product link
    api_response = api_instance.get_customer_product_link(product_link_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerLinksApi->get_customer_product_link: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_link_id** | [**str**](.md)| The unique identifier for the product link to return | 

### Return type

[**SupplierProductLinkDto**](SupplierProductLinkDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer_product_link_for_product**
> SupplierProductLinkDto get_customer_product_link_for_product(product_id, product_link_id)

For the product with Id {productId}, return a specified customer product link

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.CustomerLinksApi()
product_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The unique identifier for the product whose links we are querying
product_link_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The unique identifier for the product link to return

try:
    # For the product with Id {productId}, return a specified customer product link
    api_response = api_instance.get_customer_product_link_for_product(product_id, product_link_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerLinksApi->get_customer_product_link_for_product: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | [**str**](.md)| The unique identifier for the product whose links we are querying | 
 **product_link_id** | [**str**](.md)| The unique identifier for the product link to return | 

### Return type

[**SupplierProductLinkDto**](SupplierProductLinkDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer_product_links**
> list[CustomerProductLinkDto] get_customer_product_links(customer_id=customer_id, customer_name=customer_name, raw_material_id=raw_material_id, order_by=order_by, status=status, start_date=start_date, end_date=end_date, search_query=search_query, page_number=page_number, page_size=page_size)

Returns a list of all customer product links meeting the request criteria

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.CustomerLinksApi()
customer_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Limit the returned links to those for a specific customer Id (optional)
customer_name = 'customer_name_example' # str | Limit the returned links to those for a specific customer name (optional)
raw_material_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Limit the returned links to those for a specific raw material Id (optional)
order_by = 'order_by_example' # str | Order the results (optional)
status = 'status_example' # str | Limit the returned links by link status (optional)
start_date = '2013-10-20T19:20:30+01:00' # datetime | Limit the returned link to those where the status was updated on or after this date (optional)
end_date = '2013-10-20T19:20:30+01:00' # datetime | Limit the returned link to those where the status updated before this date (optional)
search_query = 'search_query_example' # str |  (optional)
page_number = 56 # int |  (optional)
page_size = 56 # int |  (optional)

try:
    # Returns a list of all customer product links meeting the request criteria
    api_response = api_instance.get_customer_product_links(customer_id=customer_id, customer_name=customer_name, raw_material_id=raw_material_id, order_by=order_by, status=status, start_date=start_date, end_date=end_date, search_query=search_query, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerLinksApi->get_customer_product_links: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | [**str**](.md)| Limit the returned links to those for a specific customer Id | [optional] 
 **customer_name** | **str**| Limit the returned links to those for a specific customer name | [optional] 
 **raw_material_id** | [**str**](.md)| Limit the returned links to those for a specific raw material Id | [optional] 
 **order_by** | **str**| Order the results | [optional] 
 **status** | **str**| Limit the returned links by link status | [optional] 
 **start_date** | **datetime**| Limit the returned link to those where the status was updated on or after this date | [optional] 
 **end_date** | **datetime**| Limit the returned link to those where the status updated before this date | [optional] 
 **search_query** | **str**|  | [optional] 
 **page_number** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 

### Return type

[**list[CustomerProductLinkDto]**](CustomerProductLinkDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer_product_links_for_product**
> list[CustomerProductLinkDto] get_customer_product_links_for_product(product_id, customer_id=customer_id, customer_name=customer_name, raw_material_id=raw_material_id, order_by=order_by, status=status, start_date=start_date, end_date=end_date, search_query=search_query, page_number=page_number, page_size=page_size)

For the product with Id {productId}, return a list of all customer product links meeting the request criteria

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.CustomerLinksApi()
product_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
customer_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Limit the returned links to those for a specific customer Id (optional)
customer_name = 'customer_name_example' # str | Limit the returned links to those for a specific customer name (optional)
raw_material_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Limit the returned links to those for a specific raw material Id (optional)
order_by = 'order_by_example' # str | Order the results (optional)
status = 'status_example' # str | Limit the returned links by link status (optional)
start_date = '2013-10-20T19:20:30+01:00' # datetime | Limit the returned link to those where the status was updated on or after this date (optional)
end_date = '2013-10-20T19:20:30+01:00' # datetime | Limit the returned link to those where the status updated before this date (optional)
search_query = 'search_query_example' # str |  (optional)
page_number = 56 # int |  (optional)
page_size = 56 # int |  (optional)

try:
    # For the product with Id {productId}, return a list of all customer product links meeting the request criteria
    api_response = api_instance.get_customer_product_links_for_product(product_id, customer_id=customer_id, customer_name=customer_name, raw_material_id=raw_material_id, order_by=order_by, status=status, start_date=start_date, end_date=end_date, search_query=search_query, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerLinksApi->get_customer_product_links_for_product: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | [**str**](.md)|  | 
 **customer_id** | [**str**](.md)| Limit the returned links to those for a specific customer Id | [optional] 
 **customer_name** | **str**| Limit the returned links to those for a specific customer name | [optional] 
 **raw_material_id** | [**str**](.md)| Limit the returned links to those for a specific raw material Id | [optional] 
 **order_by** | **str**| Order the results | [optional] 
 **status** | **str**| Limit the returned links by link status | [optional] 
 **start_date** | **datetime**| Limit the returned link to those where the status was updated on or after this date | [optional] 
 **end_date** | **datetime**| Limit the returned link to those where the status updated before this date | [optional] 
 **search_query** | **str**|  | [optional] 
 **page_number** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 

### Return type

[**list[CustomerProductLinkDto]**](CustomerProductLinkDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_customer_product_link_for_product**
> SupplierProductLinkDto remove_customer_product_link_for_product(product_id, product_link_id, body=body)

Remove an active product link request to your product

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.CustomerLinksApi()
product_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
product_link_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = authenticate_supply_chain.ProductLinkRemovalDto() # ProductLinkRemovalDto |  (optional)

try:
    # Remove an active product link request to your product
    api_response = api_instance.remove_customer_product_link_for_product(product_id, product_link_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerLinksApi->remove_customer_product_link_for_product: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | [**str**](.md)|  | 
 **product_link_id** | [**str**](.md)|  | 
 **body** | [**ProductLinkRemovalDto**](ProductLinkRemovalDto.md)|  | [optional] 

### Return type

[**SupplierProductLinkDto**](SupplierProductLinkDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

