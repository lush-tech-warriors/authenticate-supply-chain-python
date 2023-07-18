# authenticate_supply_chain.CountryEsgSummariesApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_country_esg_summaries**](CountryEsgSummariesApi.md#get_country_esg_summaries) | **GET** /api/v1/CountryEsgSummaries | Returns the latest country esg summaries for all countries
[**get_country_esg_summary**](CountryEsgSummariesApi.md#get_country_esg_summary) | **GET** /api/v1/Countries/{countryId}/CountryEsgSummaries | Returns a the latest esg summary associated with the country

# **get_country_esg_summaries**
> list[CountryEsgSummaryDto] get_country_esg_summaries(order_by=order_by, ranked_countries_only=ranked_countries_only, search_query=search_query, page_number=page_number, page_size=page_size)

Returns the latest country esg summaries for all countries

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.CountryEsgSummariesApi()
order_by = 'order_by_example' # str | Specify order of results (optional)
ranked_countries_only = true # bool | Only include ranked companies (optional)
search_query = 'search_query_example' # str |  (optional)
page_number = 56 # int |  (optional)
page_size = 56 # int |  (optional)

try:
    # Returns the latest country esg summaries for all countries
    api_response = api_instance.get_country_esg_summaries(order_by=order_by, ranked_countries_only=ranked_countries_only, search_query=search_query, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CountryEsgSummariesApi->get_country_esg_summaries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_by** | **str**| Specify order of results | [optional] 
 **ranked_countries_only** | **bool**| Only include ranked companies | [optional] 
 **search_query** | **str**|  | [optional] 
 **page_number** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 

### Return type

[**list[CountryEsgSummaryDto]**](CountryEsgSummaryDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_country_esg_summary**
> CountryEsgSummaryDto get_country_esg_summary(country_id)

Returns a the latest esg summary associated with the country

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.CountryEsgSummariesApi()
country_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Returns a the latest esg summary associated with the country
    api_response = api_instance.get_country_esg_summary(country_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CountryEsgSummariesApi->get_country_esg_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_id** | [**str**](.md)|  | 

### Return type

[**CountryEsgSummaryDto**](CountryEsgSummaryDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

