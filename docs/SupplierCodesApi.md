# authenticate_supply_chain.SupplierCodesApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**companies_create_company_supplier_code**](SupplierCodesApi.md#companies_create_company_supplier_code) | **POST** /api/v1/Companies/{companyId}/SupplierCodes | Create a new supplier code
[**companies_create_site_supplier_code**](SupplierCodesApi.md#companies_create_site_supplier_code) | **POST** /api/v1/Companies/{companyId}/Sites/{siteId}/SupplierCodes | Create a new site supplier code
[**companies_delete_company_supplier_code**](SupplierCodesApi.md#companies_delete_company_supplier_code) | **DELETE** /api/v1/Companies/{companyId}/SupplierCodes/{supplierCodeId} | Delete a supplier code.
[**companies_delete_site_supplier_code**](SupplierCodesApi.md#companies_delete_site_supplier_code) | **DELETE** /api/v1/Companies/{companyId}/Sites/{siteId}/SupplierCodes/{supplierCodeId} | Delete a site supplier code.
[**companies_get_company_supplier_code**](SupplierCodesApi.md#companies_get_company_supplier_code) | **GET** /api/v1/Companies/{companyId}/SupplierCodes/{supplierCodeId} | Returns a specified supplier code
[**companies_get_company_supplier_codes**](SupplierCodesApi.md#companies_get_company_supplier_codes) | **GET** /api/v1/Companies/{companyId}/SupplierCodes | Returns a list of all Supplier Codes meeting the request criteria
[**companies_get_site_supplier_code**](SupplierCodesApi.md#companies_get_site_supplier_code) | **GET** /api/v1/Companies/{companyId}/Sites/{siteId}/SupplierCodes/{supplierCodeId} | Returns a specified site supplier code
[**companies_get_site_supplier_codes**](SupplierCodesApi.md#companies_get_site_supplier_codes) | **GET** /api/v1/Companies/{companyId}/Sites/{siteId}/SupplierCodes | Returns a list of all site Supplier Codes meeting the request criteria
[**suppliers_create_company_supplier_code**](SupplierCodesApi.md#suppliers_create_company_supplier_code) | **POST** /api/v1/Suppliers/{supplierId}/SupplierCodes | Create a new supplier code
[**suppliers_create_site_supplier_code**](SupplierCodesApi.md#suppliers_create_site_supplier_code) | **POST** /api/v1/Suppliers/{supplierId}/Sites/{siteId}/SupplierCodes | Create a new site supplier code
[**suppliers_delete_company_supplier_code**](SupplierCodesApi.md#suppliers_delete_company_supplier_code) | **DELETE** /api/v1/Suppliers/{supplierId}/SupplierCodes/{supplierCodeId} | Delete a supplier code.
[**suppliers_delete_site_supplier_code**](SupplierCodesApi.md#suppliers_delete_site_supplier_code) | **DELETE** /api/v1/Suppliers/{supplierId}/Sites/{siteId}/SupplierCodes/{supplierCodeId} | Delete a site supplier code.
[**suppliers_get_company_supplier_code**](SupplierCodesApi.md#suppliers_get_company_supplier_code) | **GET** /api/v1/Suppliers/{supplierId}/SupplierCodes/{supplierCodeId} | Returns a specified supplier code
[**suppliers_get_company_supplier_codes**](SupplierCodesApi.md#suppliers_get_company_supplier_codes) | **GET** /api/v1/Suppliers/{supplierId}/SupplierCodes | Returns a list of all Supplier Codes meeting the request criteria
[**suppliers_get_site_supplier_code**](SupplierCodesApi.md#suppliers_get_site_supplier_code) | **GET** /api/v1/Suppliers/{supplierId}/Sites/{siteId}/SupplierCodes/{supplierCodeId} | Returns a specified site supplier code
[**suppliers_get_site_supplier_codes**](SupplierCodesApi.md#suppliers_get_site_supplier_codes) | **GET** /api/v1/Suppliers/{supplierId}/Sites/{siteId}/SupplierCodes | Returns a list of all site Supplier Codes meeting the request criteria

# **companies_create_company_supplier_code**
> SupplierCodeDto companies_create_company_supplier_code(company_id, body=body)

Create a new supplier code

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.SupplierCodesApi()
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = authenticate_supply_chain.SupplierCodeForCreationDto() # SupplierCodeForCreationDto |  (optional)

try:
    # Create a new supplier code
    api_response = api_instance.companies_create_company_supplier_code(company_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SupplierCodesApi->companies_create_company_supplier_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
 **body** | [**SupplierCodeForCreationDto**](SupplierCodeForCreationDto.md)|  | [optional] 

### Return type

[**SupplierCodeDto**](SupplierCodeDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_create_site_supplier_code**
> SupplierCodeDto companies_create_site_supplier_code(company_id, site_id, body=body)

Create a new site supplier code

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.SupplierCodesApi()
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
site_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The unique identifier for the supplier site
body = authenticate_supply_chain.SupplierCodeForCreationDto() # SupplierCodeForCreationDto |  (optional)

try:
    # Create a new site supplier code
    api_response = api_instance.companies_create_site_supplier_code(company_id, site_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SupplierCodesApi->companies_create_site_supplier_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
 **site_id** | [**str**](.md)| The unique identifier for the supplier site | 
 **body** | [**SupplierCodeForCreationDto**](SupplierCodeForCreationDto.md)|  | [optional] 

### Return type

[**SupplierCodeDto**](SupplierCodeDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_delete_company_supplier_code**
> companies_delete_company_supplier_code(company_id, supplier_code_id)

Delete a supplier code.

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.SupplierCodesApi()
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
supplier_code_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Delete a supplier code.
    api_instance.companies_delete_company_supplier_code(company_id, supplier_code_id)
except ApiException as e:
    print("Exception when calling SupplierCodesApi->companies_delete_company_supplier_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
 **supplier_code_id** | [**str**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_delete_site_supplier_code**
> companies_delete_site_supplier_code(company_id, site_id, supplier_code_id)

Delete a site supplier code.

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.SupplierCodesApi()
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
site_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The unique identifier for the supplier site
supplier_code_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Delete a site supplier code.
    api_instance.companies_delete_site_supplier_code(company_id, site_id, supplier_code_id)
except ApiException as e:
    print("Exception when calling SupplierCodesApi->companies_delete_site_supplier_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
 **site_id** | [**str**](.md)| The unique identifier for the supplier site | 
 **supplier_code_id** | [**str**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_get_company_supplier_code**
> SupplierCodeDto companies_get_company_supplier_code(company_id, supplier_code_id)

Returns a specified supplier code

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.SupplierCodesApi()
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The unique identifier of the company
supplier_code_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The unique identifier for the supplier code to return

try:
    # Returns a specified supplier code
    api_response = api_instance.companies_get_company_supplier_code(company_id, supplier_code_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SupplierCodesApi->companies_get_company_supplier_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)| The unique identifier of the company | 
 **supplier_code_id** | [**str**](.md)| The unique identifier for the supplier code to return | 

### Return type

[**SupplierCodeDto**](SupplierCodeDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_get_company_supplier_codes**
> list[SupplierCodeDto] companies_get_company_supplier_codes(company_id, search_query=search_query, page_number=page_number, page_size=page_size, order_by=order_by)

Returns a list of all Supplier Codes meeting the request criteria

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.SupplierCodesApi()
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The unique identifier of the company
search_query = 'search_query_example' # str |  (optional)
page_number = 56 # int |  (optional)
page_size = 56 # int |  (optional)
order_by = 'order_by_example' # str |  (optional)

try:
    # Returns a list of all Supplier Codes meeting the request criteria
    api_response = api_instance.companies_get_company_supplier_codes(company_id, search_query=search_query, page_number=page_number, page_size=page_size, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SupplierCodesApi->companies_get_company_supplier_codes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)| The unique identifier of the company | 
 **search_query** | **str**|  | [optional] 
 **page_number** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **order_by** | **str**|  | [optional] 

### Return type

[**list[SupplierCodeDto]**](SupplierCodeDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_get_site_supplier_code**
> SupplierCodeDto companies_get_site_supplier_code(company_id, site_id, supplier_code_id)

Returns a specified site supplier code

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.SupplierCodesApi()
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The unique identifier of the company
site_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The unique identifier for the supplier site
supplier_code_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The unique identifier for the supplier code to return

try:
    # Returns a specified site supplier code
    api_response = api_instance.companies_get_site_supplier_code(company_id, site_id, supplier_code_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SupplierCodesApi->companies_get_site_supplier_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)| The unique identifier of the company | 
 **site_id** | [**str**](.md)| The unique identifier for the supplier site | 
 **supplier_code_id** | [**str**](.md)| The unique identifier for the supplier code to return | 

### Return type

[**SupplierCodeDto**](SupplierCodeDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_get_site_supplier_codes**
> list[SupplierCodeDto] companies_get_site_supplier_codes(company_id, site_id, search_query=search_query, page_number=page_number, page_size=page_size, order_by=order_by)

Returns a list of all site Supplier Codes meeting the request criteria

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.SupplierCodesApi()
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The unique identifier of the company
site_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The unique identifier for the supplier site
search_query = 'search_query_example' # str |  (optional)
page_number = 56 # int |  (optional)
page_size = 56 # int |  (optional)
order_by = 'order_by_example' # str |  (optional)

try:
    # Returns a list of all site Supplier Codes meeting the request criteria
    api_response = api_instance.companies_get_site_supplier_codes(company_id, site_id, search_query=search_query, page_number=page_number, page_size=page_size, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SupplierCodesApi->companies_get_site_supplier_codes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)| The unique identifier of the company | 
 **site_id** | [**str**](.md)| The unique identifier for the supplier site | 
 **search_query** | **str**|  | [optional] 
 **page_number** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **order_by** | **str**|  | [optional] 

### Return type

[**list[SupplierCodeDto]**](SupplierCodeDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **suppliers_create_company_supplier_code**
> SupplierCodeDto suppliers_create_company_supplier_code(supplier_id, body=body)

Create a new supplier code

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.SupplierCodesApi()
supplier_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = authenticate_supply_chain.SupplierCodeForCreationDto() # SupplierCodeForCreationDto |  (optional)

try:
    # Create a new supplier code
    api_response = api_instance.suppliers_create_company_supplier_code(supplier_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SupplierCodesApi->suppliers_create_company_supplier_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supplier_id** | [**str**](.md)|  | 
 **body** | [**SupplierCodeForCreationDto**](SupplierCodeForCreationDto.md)|  | [optional] 

### Return type

[**SupplierCodeDto**](SupplierCodeDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **suppliers_create_site_supplier_code**
> SupplierCodeDto suppliers_create_site_supplier_code(supplier_id, site_id, body=body)

Create a new site supplier code

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.SupplierCodesApi()
supplier_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
site_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The unique identifier for the supplier site
body = authenticate_supply_chain.SupplierCodeForCreationDto() # SupplierCodeForCreationDto |  (optional)

try:
    # Create a new site supplier code
    api_response = api_instance.suppliers_create_site_supplier_code(supplier_id, site_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SupplierCodesApi->suppliers_create_site_supplier_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supplier_id** | [**str**](.md)|  | 
 **site_id** | [**str**](.md)| The unique identifier for the supplier site | 
 **body** | [**SupplierCodeForCreationDto**](SupplierCodeForCreationDto.md)|  | [optional] 

### Return type

[**SupplierCodeDto**](SupplierCodeDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **suppliers_delete_company_supplier_code**
> suppliers_delete_company_supplier_code(supplier_id, supplier_code_id)

Delete a supplier code.

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.SupplierCodesApi()
supplier_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
supplier_code_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Delete a supplier code.
    api_instance.suppliers_delete_company_supplier_code(supplier_id, supplier_code_id)
except ApiException as e:
    print("Exception when calling SupplierCodesApi->suppliers_delete_company_supplier_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supplier_id** | [**str**](.md)|  | 
 **supplier_code_id** | [**str**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **suppliers_delete_site_supplier_code**
> suppliers_delete_site_supplier_code(supplier_id, site_id, supplier_code_id)

Delete a site supplier code.

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.SupplierCodesApi()
supplier_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
site_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The unique identifier for the supplier site
supplier_code_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Delete a site supplier code.
    api_instance.suppliers_delete_site_supplier_code(supplier_id, site_id, supplier_code_id)
except ApiException as e:
    print("Exception when calling SupplierCodesApi->suppliers_delete_site_supplier_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supplier_id** | [**str**](.md)|  | 
 **site_id** | [**str**](.md)| The unique identifier for the supplier site | 
 **supplier_code_id** | [**str**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **suppliers_get_company_supplier_code**
> SupplierCodeDto suppliers_get_company_supplier_code(supplier_id, supplier_code_id)

Returns a specified supplier code

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.SupplierCodesApi()
supplier_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The unique identifier of the supplier company
supplier_code_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The unique identifier for the supplier code to return

try:
    # Returns a specified supplier code
    api_response = api_instance.suppliers_get_company_supplier_code(supplier_id, supplier_code_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SupplierCodesApi->suppliers_get_company_supplier_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supplier_id** | [**str**](.md)| The unique identifier of the supplier company | 
 **supplier_code_id** | [**str**](.md)| The unique identifier for the supplier code to return | 

### Return type

[**SupplierCodeDto**](SupplierCodeDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **suppliers_get_company_supplier_codes**
> list[SupplierCodeDto] suppliers_get_company_supplier_codes(supplier_id, search_query=search_query, page_number=page_number, page_size=page_size, order_by=order_by)

Returns a list of all Supplier Codes meeting the request criteria

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.SupplierCodesApi()
supplier_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The unique identifier of the supplier company
search_query = 'search_query_example' # str |  (optional)
page_number = 56 # int |  (optional)
page_size = 56 # int |  (optional)
order_by = 'order_by_example' # str |  (optional)

try:
    # Returns a list of all Supplier Codes meeting the request criteria
    api_response = api_instance.suppliers_get_company_supplier_codes(supplier_id, search_query=search_query, page_number=page_number, page_size=page_size, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SupplierCodesApi->suppliers_get_company_supplier_codes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supplier_id** | [**str**](.md)| The unique identifier of the supplier company | 
 **search_query** | **str**|  | [optional] 
 **page_number** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **order_by** | **str**|  | [optional] 

### Return type

[**list[SupplierCodeDto]**](SupplierCodeDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **suppliers_get_site_supplier_code**
> SupplierCodeDto suppliers_get_site_supplier_code(supplier_id, site_id, supplier_code_id)

Returns a specified site supplier code

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.SupplierCodesApi()
supplier_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The unique identifier of the supplier company
site_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The unique identifier for the supplier site
supplier_code_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The unique identifier for the supplier code to return

try:
    # Returns a specified site supplier code
    api_response = api_instance.suppliers_get_site_supplier_code(supplier_id, site_id, supplier_code_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SupplierCodesApi->suppliers_get_site_supplier_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supplier_id** | [**str**](.md)| The unique identifier of the supplier company | 
 **site_id** | [**str**](.md)| The unique identifier for the supplier site | 
 **supplier_code_id** | [**str**](.md)| The unique identifier for the supplier code to return | 

### Return type

[**SupplierCodeDto**](SupplierCodeDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **suppliers_get_site_supplier_codes**
> list[SupplierCodeDto] suppliers_get_site_supplier_codes(supplier_id, site_id, search_query=search_query, page_number=page_number, page_size=page_size, order_by=order_by)

Returns a list of all site Supplier Codes meeting the request criteria

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.SupplierCodesApi()
supplier_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The unique identifier of the supplier company
site_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The unique identifier for the supplier site
search_query = 'search_query_example' # str |  (optional)
page_number = 56 # int |  (optional)
page_size = 56 # int |  (optional)
order_by = 'order_by_example' # str |  (optional)

try:
    # Returns a list of all site Supplier Codes meeting the request criteria
    api_response = api_instance.suppliers_get_site_supplier_codes(supplier_id, site_id, search_query=search_query, page_number=page_number, page_size=page_size, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SupplierCodesApi->suppliers_get_site_supplier_codes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supplier_id** | [**str**](.md)| The unique identifier of the supplier company | 
 **site_id** | [**str**](.md)| The unique identifier for the supplier site | 
 **search_query** | **str**|  | [optional] 
 **page_number** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **order_by** | **str**|  | [optional] 

### Return type

[**list[SupplierCodeDto]**](SupplierCodeDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

