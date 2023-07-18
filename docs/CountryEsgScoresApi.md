# authenticate_supply_chain.CountryEsgScoresApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_country_esg_scores**](CountryEsgScoresApi.md#get_country_esg_scores) | **GET** /api/v1/Countries/{countryId}/CountryEsgSummaries/{summaryId}/CountryEsgScores | Returns a list of the esg scores associated with the country esg summary

# **get_country_esg_scores**
> list[CountryEsgScoreDto] get_country_esg_scores(country_id, summary_id)

Returns a list of the esg scores associated with the country esg summary

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.CountryEsgScoresApi()
country_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
summary_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Returns a list of the esg scores associated with the country esg summary
    api_response = api_instance.get_country_esg_scores(country_id, summary_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CountryEsgScoresApi->get_country_esg_scores: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_id** | [**str**](.md)|  | 
 **summary_id** | [**str**](.md)|  | 

### Return type

[**list[CountryEsgScoreDto]**](CountryEsgScoreDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

