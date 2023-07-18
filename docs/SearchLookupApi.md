# authenticate_supply_chain.SearchLookupApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_sites_relationships_values**](SearchLookupApi.md#get_sites_relationships_values) | **GET** /api/v1/SearchLookup/GetSitesRelationshipsValues | Returns a list of all site to company relationships

# **get_sites_relationships_values**
> SearchLookupDto get_sites_relationships_values()

Returns a list of all site to company relationships

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.SearchLookupApi()

try:
    # Returns a list of all site to company relationships
    api_response = api_instance.get_sites_relationships_values()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchLookupApi->get_sites_relationships_values: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SearchLookupDto**](SearchLookupDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

