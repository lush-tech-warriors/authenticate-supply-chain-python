# authenticate_supply_chain.CompanyRelationshipsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_company_company_relationship**](CompanyRelationshipsApi.md#get_company_company_relationship) | **GET** /api/v1/CompanyRelationships/{companyId} | Returns a specified company relationship based on viewing company

# **get_company_company_relationship**
> CompanyRelationshipDto get_company_company_relationship(company_id)

Returns a specified company relationship based on viewing company

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.CompanyRelationshipsApi()
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The unique identifier for the company to company relationship to return

try:
    # Returns a specified company relationship based on viewing company
    api_response = api_instance.get_company_company_relationship(company_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyRelationshipsApi->get_company_company_relationship: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)| The unique identifier for the company to company relationship to return | 

### Return type

[**CompanyRelationshipDto**](CompanyRelationshipDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

