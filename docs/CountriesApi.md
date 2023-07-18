# authenticate_supply_chain.CountriesApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_countries**](CountriesApi.md#get_countries) | **GET** /api/v1/Countries | Returns a list of all categories meeting the request criteria
[**get_country**](CountriesApi.md#get_country) | **GET** /api/v1/Countries/{countryId} | Returns a specified country

# **get_countries**
> list[CountryDto] get_countries(country_code=country_code, country_name=country_name, search_query=search_query, page_number=page_number, page_size=page_size, order_by=order_by)

Returns a list of all categories meeting the request criteria

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.CountriesApi()
country_code = 'country_code_example' # str | Filter by the two or three digit country code (optional)
country_name = 'country_name_example' # str | Filter by the country Name (optional)
search_query = 'search_query_example' # str |  (optional)
page_number = 56 # int |  (optional)
page_size = 56 # int |  (optional)
order_by = 'order_by_example' # str |  (optional)

try:
    # Returns a list of all categories meeting the request criteria
    api_response = api_instance.get_countries(country_code=country_code, country_name=country_name, search_query=search_query, page_number=page_number, page_size=page_size, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CountriesApi->get_countries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_code** | **str**| Filter by the two or three digit country code | [optional] 
 **country_name** | **str**| Filter by the country Name | [optional] 
 **search_query** | **str**|  | [optional] 
 **page_number** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **order_by** | **str**|  | [optional] 

### Return type

[**list[CountryDto]**](CountryDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_country**
> CountryDto get_country(country_id)

Returns a specified country

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.CountriesApi()
country_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The unique identifier for the country to return

try:
    # Returns a specified country
    api_response = api_instance.get_country(country_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CountriesApi->get_country: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_id** | [**str**](.md)| The unique identifier for the country to return | 

### Return type

[**CountryDto**](CountryDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

