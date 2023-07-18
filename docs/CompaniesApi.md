# authenticate_supply_chain.CompaniesApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_companies_post**](CompaniesApi.md#api_v1_companies_post) | **POST** /api/v1/Companies | Create a new Companies
[**get_companies**](CompaniesApi.md#get_companies) | **GET** /api/v1/Companies | Returns a list of all Companies meeting the request criteria
[**get_company**](CompaniesApi.md#get_company) | **GET** /api/v1/Companies/{companyId} | Returns a specified Companies
[**search_companies_from_supply_chain**](CompaniesApi.md#search_companies_from_supply_chain) | **POST** /api/v1/Companies/Suppliers/Search | 

# **api_v1_companies_post**
> CompanyDto api_v1_companies_post(body=body)

Create a new Companies

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.CompaniesApi()
body = authenticate_supply_chain.CompanyForCreationDto() # CompanyForCreationDto |  (optional)

try:
    # Create a new Companies
    api_response = api_instance.api_v1_companies_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompaniesApi->api_v1_companies_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CompanyForCreationDto**](CompanyForCreationDto.md)|  | [optional] 

### Return type

[**CompanyDto**](CompanyDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_companies**
> list[CompanyDto] get_companies(country=country, postcode=postcode, authenticate_member=authenticate_member, company_type=company_type, company_ids=company_ids, supplier_codes=supplier_codes, licence_numbers=licence_numbers, search_query=search_query, page_number=page_number, page_size=page_size, order_by=order_by)

Returns a list of all Companies meeting the request criteria

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.CompaniesApi()
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
order_by = 'order_by_example' # str |  (optional)

try:
    # Returns a list of all Companies meeting the request criteria
    api_response = api_instance.get_companies(country=country, postcode=postcode, authenticate_member=authenticate_member, company_type=company_type, company_ids=company_ids, supplier_codes=supplier_codes, licence_numbers=licence_numbers, search_query=search_query, page_number=page_number, page_size=page_size, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompaniesApi->get_companies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
 **order_by** | **str**|  | [optional] 

### Return type

[**list[CompanyDto]**](CompanyDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company**
> CompanyDto get_company(company_id)

Returns a specified Companies

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.CompaniesApi()
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The unique identifier for the Companies to return

try:
    # Returns a specified Companies
    api_response = api_instance.get_company(company_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompaniesApi->get_company: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)| The unique identifier for the Companies to return | 

### Return type

[**CompanyDto**](CompanyDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_companies_from_supply_chain**
> list[CompanyDto] search_companies_from_supply_chain(body=body)



### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.CompaniesApi()
body = authenticate_supply_chain.CompanyResourceParameters() # CompanyResourceParameters |  (optional)

try:
    api_response = api_instance.search_companies_from_supply_chain(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompaniesApi->search_companies_from_supply_chain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CompanyResourceParameters**](CompanyResourceParameters.md)|  | [optional] 

### Return type

[**list[CompanyDto]**](CompanyDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

