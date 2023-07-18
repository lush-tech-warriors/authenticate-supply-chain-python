# authenticate_supply_chain.CountryEsgScoreDetailsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_country_esg_score_details**](CountryEsgScoreDetailsApi.md#get_country_esg_score_details) | **GET** /api/v1/Countries/{countryId}/CountryEsgSummaries/{summaryId}/CountryEsgScores/{scoreId}/CountryEsgScoreDetails | Returns a list of the esg score details associated with the country esg score

# **get_country_esg_score_details**
> list[CountryEsgScoreDetailDto] get_country_esg_score_details(country_id, summary_id, score_id)

Returns a list of the esg score details associated with the country esg score

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.CountryEsgScoreDetailsApi()
country_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
summary_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
score_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Returns a list of the esg score details associated with the country esg score
    api_response = api_instance.get_country_esg_score_details(country_id, summary_id, score_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CountryEsgScoreDetailsApi->get_country_esg_score_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_id** | [**str**](.md)|  | 
 **summary_id** | [**str**](.md)|  | 
 **score_id** | [**str**](.md)|  | 

### Return type

[**list[CountryEsgScoreDetailDto]**](CountryEsgScoreDetailDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

