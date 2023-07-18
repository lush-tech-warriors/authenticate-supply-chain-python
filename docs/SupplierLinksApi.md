# authenticate_supply_chain.SupplierLinksApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_supplier_product_link**](SupplierLinksApi.md#create_supplier_product_link) | **POST** /api/v1/SupplierLinks | Create a new product link request
[**create_supplier_product_link_for_product**](SupplierLinksApi.md#create_supplier_product_link_for_product) | **POST** /api/v1/Products/{productId}/SupplierLinks | Create a new product link request
[**delete_supplier_product_link**](SupplierLinksApi.md#delete_supplier_product_link) | **DELETE** /api/v1/SupplierLinks/{productLinkId} | Delete a product link. Active product links (Pending, Accepted) cannot be deleted
[**delete_supplier_product_link_for_product**](SupplierLinksApi.md#delete_supplier_product_link_for_product) | **DELETE** /api/v1/Products/{productId}/SupplierLinks/{productLinkId} | Delete a product link. Active product links (Pending, Accepted) cannot be deleted
[**get_supplier_product_link**](SupplierLinksApi.md#get_supplier_product_link) | **GET** /api/v1/SupplierLinks/{productLinkId} | Returns a specified supplier product link
[**get_supplier_product_link_for_product**](SupplierLinksApi.md#get_supplier_product_link_for_product) | **GET** /api/v1/Products/{productId}/SupplierLinks/{productLinkId} | For the product with Id {productId}, return a specified supplier product link
[**get_supplier_product_links**](SupplierLinksApi.md#get_supplier_product_links) | **GET** /api/v1/SupplierLinks | Returns a list of all supplier product links meeting the request criteria
[**get_supplier_product_links_for_product**](SupplierLinksApi.md#get_supplier_product_links_for_product) | **GET** /api/v1/Products/{productId}/SupplierLinks | For the product with Id {productId}, return a list of all supplier product links for meeting the request criteria
[**remove_supplier_product_link**](SupplierLinksApi.md#remove_supplier_product_link) | **POST** /api/v1/SupplierLinks/{productLinkId}/Remove | Remove an active product link request
[**remove_supplier_product_link_for_product**](SupplierLinksApi.md#remove_supplier_product_link_for_product) | **POST** /api/v1/Products/{productId}/SupplierLinks/{productLinkId}/Remove | Remove an active product link request
[**rescind_supplier_product_link**](SupplierLinksApi.md#rescind_supplier_product_link) | **POST** /api/v1/SupplierLinks/{productLinkId}/Rescind | Rescind an active product link request
[**rescind_supplier_product_link_for_product**](SupplierLinksApi.md#rescind_supplier_product_link_for_product) | **POST** /api/v1/Products/{productId}/SupplierLinks/{productLinkId}/Rescind | Rescind an active product link request
[**update_supplier_product_link**](SupplierLinksApi.md#update_supplier_product_link) | **PUT** /api/v1/SupplierLinks/{productLinkId} | Update a product link

# **create_supplier_product_link**
> SupplierProductLinkDto create_supplier_product_link(body=body)

Create a new product link request

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.SupplierLinksApi()
body = authenticate_supply_chain.SupplierProductLinkForCreationDto() # SupplierProductLinkForCreationDto |  (optional)

try:
    # Create a new product link request
    api_response = api_instance.create_supplier_product_link(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SupplierLinksApi->create_supplier_product_link: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SupplierProductLinkForCreationDto**](SupplierProductLinkForCreationDto.md)|  | [optional] 

### Return type

[**SupplierProductLinkDto**](SupplierProductLinkDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_supplier_product_link_for_product**
> SupplierProductLinkDto create_supplier_product_link_for_product(product_id, body=body)

Create a new product link request

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.SupplierLinksApi()
product_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = authenticate_supply_chain.SupplierProductLinkForCreationDto() # SupplierProductLinkForCreationDto |  (optional)

try:
    # Create a new product link request
    api_response = api_instance.create_supplier_product_link_for_product(product_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SupplierLinksApi->create_supplier_product_link_for_product: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | [**str**](.md)|  | 
 **body** | [**SupplierProductLinkForCreationDto**](SupplierProductLinkForCreationDto.md)|  | [optional] 

### Return type

[**SupplierProductLinkDto**](SupplierProductLinkDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_supplier_product_link**
> delete_supplier_product_link(product_link_id)

Delete a product link. Active product links (Pending, Accepted) cannot be deleted

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.SupplierLinksApi()
product_link_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Delete a product link. Active product links (Pending, Accepted) cannot be deleted
    api_instance.delete_supplier_product_link(product_link_id)
except ApiException as e:
    print("Exception when calling SupplierLinksApi->delete_supplier_product_link: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_link_id** | [**str**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_supplier_product_link_for_product**
> delete_supplier_product_link_for_product(product_id, product_link_id)

Delete a product link. Active product links (Pending, Accepted) cannot be deleted

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.SupplierLinksApi()
product_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
product_link_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Delete a product link. Active product links (Pending, Accepted) cannot be deleted
    api_instance.delete_supplier_product_link_for_product(product_id, product_link_id)
except ApiException as e:
    print("Exception when calling SupplierLinksApi->delete_supplier_product_link_for_product: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | [**str**](.md)|  | 
 **product_link_id** | [**str**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_supplier_product_link**
> SupplierProductLinkDto get_supplier_product_link(product_link_id)

Returns a specified supplier product link

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.SupplierLinksApi()
product_link_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The unique identifier for the product link to return

try:
    # Returns a specified supplier product link
    api_response = api_instance.get_supplier_product_link(product_link_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SupplierLinksApi->get_supplier_product_link: %s\n" % e)
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

# **get_supplier_product_link_for_product**
> SupplierProductLinkDto get_supplier_product_link_for_product(product_id, product_link_id)

For the product with Id {productId}, return a specified supplier product link

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.SupplierLinksApi()
product_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The unique identifier for the product whose links we are querying
product_link_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The unique identifier for the product link to return

try:
    # For the product with Id {productId}, return a specified supplier product link
    api_response = api_instance.get_supplier_product_link_for_product(product_id, product_link_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SupplierLinksApi->get_supplier_product_link_for_product: %s\n" % e)
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

# **get_supplier_product_links**
> list[SupplierProductLinkDto] get_supplier_product_links(supplier_id=supplier_id, supplier_name=supplier_name, order_by=order_by, status=status, start_date=start_date, end_date=end_date, search_query=search_query, page_number=page_number, page_size=page_size)

Returns a list of all supplier product links meeting the request criteria

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.SupplierLinksApi()
supplier_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Limit the returned links to those for a specific supplier Id (optional)
supplier_name = 'supplier_name_example' # str | Limit the returned links to those for a specific supplier name (optional)
order_by = 'order_by_example' # str | Order the results (optional)
status = 'status_example' # str | Limit the returned links by link status (optional)
start_date = '2013-10-20T19:20:30+01:00' # datetime | Limit the returned link to those where the status was updated on or after this date (optional)
end_date = '2013-10-20T19:20:30+01:00' # datetime | Limit the returned link to those where the status updated before this date (optional)
search_query = 'search_query_example' # str |  (optional)
page_number = 56 # int |  (optional)
page_size = 56 # int |  (optional)

try:
    # Returns a list of all supplier product links meeting the request criteria
    api_response = api_instance.get_supplier_product_links(supplier_id=supplier_id, supplier_name=supplier_name, order_by=order_by, status=status, start_date=start_date, end_date=end_date, search_query=search_query, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SupplierLinksApi->get_supplier_product_links: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supplier_id** | [**str**](.md)| Limit the returned links to those for a specific supplier Id | [optional] 
 **supplier_name** | **str**| Limit the returned links to those for a specific supplier name | [optional] 
 **order_by** | **str**| Order the results | [optional] 
 **status** | **str**| Limit the returned links by link status | [optional] 
 **start_date** | **datetime**| Limit the returned link to those where the status was updated on or after this date | [optional] 
 **end_date** | **datetime**| Limit the returned link to those where the status updated before this date | [optional] 
 **search_query** | **str**|  | [optional] 
 **page_number** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 

### Return type

[**list[SupplierProductLinkDto]**](SupplierProductLinkDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_supplier_product_links_for_product**
> list[SupplierProductLinkDto] get_supplier_product_links_for_product(product_id, supplier_id=supplier_id, supplier_name=supplier_name, order_by=order_by, status=status, start_date=start_date, end_date=end_date, search_query=search_query, page_number=page_number, page_size=page_size)

For the product with Id {productId}, return a list of all supplier product links for meeting the request criteria

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.SupplierLinksApi()
product_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
supplier_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Limit the returned links to those for a specific supplier Id (optional)
supplier_name = 'supplier_name_example' # str | Limit the returned links to those for a specific supplier name (optional)
order_by = 'order_by_example' # str | Order the results (optional)
status = 'status_example' # str | Limit the returned links by link status (optional)
start_date = '2013-10-20T19:20:30+01:00' # datetime | Limit the returned link to those where the status was updated on or after this date (optional)
end_date = '2013-10-20T19:20:30+01:00' # datetime | Limit the returned link to those where the status updated before this date (optional)
search_query = 'search_query_example' # str |  (optional)
page_number = 56 # int |  (optional)
page_size = 56 # int |  (optional)

try:
    # For the product with Id {productId}, return a list of all supplier product links for meeting the request criteria
    api_response = api_instance.get_supplier_product_links_for_product(product_id, supplier_id=supplier_id, supplier_name=supplier_name, order_by=order_by, status=status, start_date=start_date, end_date=end_date, search_query=search_query, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SupplierLinksApi->get_supplier_product_links_for_product: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | [**str**](.md)|  | 
 **supplier_id** | [**str**](.md)| Limit the returned links to those for a specific supplier Id | [optional] 
 **supplier_name** | **str**| Limit the returned links to those for a specific supplier name | [optional] 
 **order_by** | **str**| Order the results | [optional] 
 **status** | **str**| Limit the returned links by link status | [optional] 
 **start_date** | **datetime**| Limit the returned link to those where the status was updated on or after this date | [optional] 
 **end_date** | **datetime**| Limit the returned link to those where the status updated before this date | [optional] 
 **search_query** | **str**|  | [optional] 
 **page_number** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 

### Return type

[**list[SupplierProductLinkDto]**](SupplierProductLinkDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_supplier_product_link**
> SupplierProductLinkDto remove_supplier_product_link(product_link_id, body=body)

Remove an active product link request

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.SupplierLinksApi()
product_link_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = authenticate_supply_chain.ProductLinkRemovalDto() # ProductLinkRemovalDto |  (optional)

try:
    # Remove an active product link request
    api_response = api_instance.remove_supplier_product_link(product_link_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SupplierLinksApi->remove_supplier_product_link: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **remove_supplier_product_link_for_product**
> SupplierProductLinkDto remove_supplier_product_link_for_product(product_id, product_link_id, body=body)

Remove an active product link request

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.SupplierLinksApi()
product_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
product_link_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = authenticate_supply_chain.ProductLinkRemovalDto() # ProductLinkRemovalDto |  (optional)

try:
    # Remove an active product link request
    api_response = api_instance.remove_supplier_product_link_for_product(product_id, product_link_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SupplierLinksApi->remove_supplier_product_link_for_product: %s\n" % e)
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

# **rescind_supplier_product_link**
> SupplierProductLinkDto rescind_supplier_product_link(product_link_id, body=body)

Rescind an active product link request

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.SupplierLinksApi()
product_link_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = authenticate_supply_chain.ProductLinkRemovalDto() # ProductLinkRemovalDto |  (optional)

try:
    # Rescind an active product link request
    api_response = api_instance.rescind_supplier_product_link(product_link_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SupplierLinksApi->rescind_supplier_product_link: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **rescind_supplier_product_link_for_product**
> SupplierProductLinkDto rescind_supplier_product_link_for_product(product_id, product_link_id, body=body)

Rescind an active product link request

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.SupplierLinksApi()
product_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
product_link_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = authenticate_supply_chain.ProductLinkRemovalDto() # ProductLinkRemovalDto |  (optional)

try:
    # Rescind an active product link request
    api_response = api_instance.rescind_supplier_product_link_for_product(product_id, product_link_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SupplierLinksApi->rescind_supplier_product_link_for_product: %s\n" % e)
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

# **update_supplier_product_link**
> SupplierProductLinkDto update_supplier_product_link(product_link_id, body=body)

Update a product link

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.SupplierLinksApi()
product_link_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = authenticate_supply_chain.SupplierProductLinkForUpdateDto() # SupplierProductLinkForUpdateDto |  (optional)

try:
    # Update a product link
    api_response = api_instance.update_supplier_product_link(product_link_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SupplierLinksApi->update_supplier_product_link: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_link_id** | [**str**](.md)|  | 
 **body** | [**SupplierProductLinkForUpdateDto**](SupplierProductLinkForUpdateDto.md)|  | [optional] 

### Return type

[**SupplierProductLinkDto**](SupplierProductLinkDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

