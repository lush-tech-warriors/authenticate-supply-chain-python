# authenticate_supply_chain.SuppliersApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_supplier**](SuppliersApi.md#get_supplier) | **GET** /api/v1/Suppliers/{supplierId} | Returns a specified supplier
[**get_suppliers**](SuppliersApi.md#get_suppliers) | **GET** /api/v1/Suppliers | Returns a list of all Suppliers meeting the request criteria
[**search_suppliers**](SuppliersApi.md#search_suppliers) | **POST** /api/v1/Suppliers/Search | Returns a list of all Suppliers meeting the request criteria

# **get_supplier**
> SupplierDto get_supplier(supplier_id)

Returns a specified supplier

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.SuppliersApi()
supplier_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The unique identifier for the supplier to return

try:
    # Returns a specified supplier
    api_response = api_instance.get_supplier(supplier_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SuppliersApi->get_supplier: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supplier_id** | [**str**](.md)| The unique identifier for the supplier to return | 

### Return type

[**SupplierDto**](SupplierDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_suppliers**
> list[SupplierDto] get_suppliers(supplier_id=supplier_id, supplier_code=supplier_code, supplier_status=supplier_status, supplier_risk=supplier_risk, tier=tier, start_date=start_date, end_date=end_date, order_by=order_by, country=country, postcode=postcode, authenticate_member=authenticate_member, company_type=company_type, company_ids=company_ids, supplier_codes=supplier_codes, licence_numbers=licence_numbers, search_query=search_query, page_number=page_number, page_size=page_size)

Returns a list of all Suppliers meeting the request criteria

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.SuppliersApi()
supplier_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Filter by a specific supplier id (optional)
supplier_code = 'supplier_code_example' # str | Filter by the supplier code you have assigned (optional)
supplier_status = 'supplier_status_example' # str | Filter by the supplier status you have assigned  Status values are: Approved, Pending, Suspended, Rejected (optional)
supplier_risk = 'supplier_risk_example' # str | Filter by the supplier risk  you have assigned  Risks are: Low, Medium, High (optional)
tier = [56] # list[int] | Filter supplier by supply chain tier (NB: viewing suppliers at Tier 2+ is not available for all membership levels) (optional)
start_date = '2013-10-20T19:20:30+01:00' # datetime | Limit the returned suppliers to those where a recorded change event occurred on or after this date  Change events include updates to supplier status, risk etc or when a company first appeared in your supply chain (optional)
end_date = '2013-10-20T19:20:30+01:00' # datetime | Limit the returned suppliers to those where a recorded change event occurred before this date    Change events include updates to supplier status, risk etc or when a company first appeared in your supply chain (optional)
order_by = 'order_by_example' # str | Order the results (optional)
country = 'country_example' # str | Filter supplier by country (optional)
postcode = 'postcode_example' # str | Filter supplier by postcode (optional)
authenticate_member = true # bool | Filter by whether the company is a member of the authenticate platform or not (optional)
company_type = 'company_type_example' # str | Filter by ONS Company Type (optional)
company_ids = ['company_ids_example'] # list[str] | Filter by list of company id's (optional)
supplier_codes = ['supplier_codes_example'] # list[str] | Filter by supplier codes (optional)
licence_numbers = ['licence_numbers_example'] # list[str] | Filter by licence numbers (optional)
search_query = 'search_query_example' # str |  (optional)
page_number = 56 # int |  (optional)
page_size = 56 # int |  (optional)

try:
    # Returns a list of all Suppliers meeting the request criteria
    api_response = api_instance.get_suppliers(supplier_id=supplier_id, supplier_code=supplier_code, supplier_status=supplier_status, supplier_risk=supplier_risk, tier=tier, start_date=start_date, end_date=end_date, order_by=order_by, country=country, postcode=postcode, authenticate_member=authenticate_member, company_type=company_type, company_ids=company_ids, supplier_codes=supplier_codes, licence_numbers=licence_numbers, search_query=search_query, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SuppliersApi->get_suppliers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supplier_id** | [**str**](.md)| Filter by a specific supplier id | [optional] 
 **supplier_code** | **str**| Filter by the supplier code you have assigned | [optional] 
 **supplier_status** | **str**| Filter by the supplier status you have assigned  Status values are: Approved, Pending, Suspended, Rejected | [optional] 
 **supplier_risk** | **str**| Filter by the supplier risk  you have assigned  Risks are: Low, Medium, High | [optional] 
 **tier** | [**list[int]**](int.md)| Filter supplier by supply chain tier (NB: viewing suppliers at Tier 2+ is not available for all membership levels) | [optional] 
 **start_date** | **datetime**| Limit the returned suppliers to those where a recorded change event occurred on or after this date  Change events include updates to supplier status, risk etc or when a company first appeared in your supply chain | [optional] 
 **end_date** | **datetime**| Limit the returned suppliers to those where a recorded change event occurred before this date    Change events include updates to supplier status, risk etc or when a company first appeared in your supply chain | [optional] 
 **order_by** | **str**| Order the results | [optional] 
 **country** | **str**| Filter supplier by country | [optional] 
 **postcode** | **str**| Filter supplier by postcode | [optional] 
 **authenticate_member** | **bool**| Filter by whether the company is a member of the authenticate platform or not | [optional] 
 **company_type** | **str**| Filter by ONS Company Type | [optional] 
 **company_ids** | [**list[str]**](str.md)| Filter by list of company id&#x27;s | [optional] 
 **supplier_codes** | [**list[str]**](str.md)| Filter by supplier codes | [optional] 
 **licence_numbers** | [**list[str]**](str.md)| Filter by licence numbers | [optional] 
 **search_query** | **str**|  | [optional] 
 **page_number** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 

### Return type

[**list[SupplierDto]**](SupplierDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_suppliers**
> list[SupplierDto] search_suppliers(body=body)

Returns a list of all Suppliers meeting the request criteria

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.SuppliersApi()
body = authenticate_supply_chain.SupplierResourceParameters() # SupplierResourceParameters |  (optional)

try:
    # Returns a list of all Suppliers meeting the request criteria
    api_response = api_instance.search_suppliers(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SuppliersApi->search_suppliers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SupplierResourceParameters**](SupplierResourceParameters.md)|  | [optional] 

### Return type

[**list[SupplierDto]**](SupplierDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

