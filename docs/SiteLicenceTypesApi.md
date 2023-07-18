# authenticate_supply_chain.SiteLicenceTypesApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_site_licence_types_get**](SiteLicenceTypesApi.md#api_v1_site_licence_types_get) | **GET** /api/v1/SiteLicenceTypes | Returns a list of site licence types

# **api_v1_site_licence_types_get**
> list[LicenceTypeDto] api_v1_site_licence_types_get()

Returns a list of site licence types

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.SiteLicenceTypesApi()

try:
    # Returns a list of site licence types
    api_response = api_instance.api_v1_site_licence_types_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteLicenceTypesApi->api_v1_site_licence_types_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[LicenceTypeDto]**](LicenceTypeDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

