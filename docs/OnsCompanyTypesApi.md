# authenticate_supply_chain.OnsCompanyTypesApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_company_type**](OnsCompanyTypesApi.md#get_company_type) | **GET** /api/v1/OnsCompanyTypes/{onsCompanyTypeId} | Returns a specified ONS company type
[**get_company_types**](OnsCompanyTypesApi.md#get_company_types) | **GET** /api/v1/OnsCompanyTypes | Returns a list of all ONS company types meeting the request criteria
[**get_company_types_for_sector**](OnsCompanyTypesApi.md#get_company_types_for_sector) | **GET** /api/v1/OnsSectors/{onsSectorId}/OnsCompanyTypes | Returns a list of all ONS company types meeting the request criteria for a give ONS sector
[**get_ons_sectors**](OnsCompanyTypesApi.md#get_ons_sectors) | **GET** /api/v1/OnsSectors | Returns a list of all ONS business sectors meeting the request criteria

# **get_company_type**
> OnsCompanyTypeDto get_company_type(ons_company_type_id)

Returns a specified ONS company type

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.OnsCompanyTypesApi()
ons_company_type_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The unique identifier for the company type to return

try:
    # Returns a specified ONS company type
    api_response = api_instance.get_company_type(ons_company_type_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OnsCompanyTypesApi->get_company_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ons_company_type_id** | [**str**](.md)| The unique identifier for the company type to return | 

### Return type

[**OnsCompanyTypeDto**](OnsCompanyTypeDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_types**
> list[OnsCompanyTypeDto] get_company_types(search_query=search_query, page_number=page_number, page_size=page_size, order_by=order_by)

Returns a list of all ONS company types meeting the request criteria

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.OnsCompanyTypesApi()
search_query = 'search_query_example' # str |  (optional)
page_number = 56 # int |  (optional)
page_size = 56 # int |  (optional)
order_by = 'order_by_example' # str |  (optional)

try:
    # Returns a list of all ONS company types meeting the request criteria
    api_response = api_instance.get_company_types(search_query=search_query, page_number=page_number, page_size=page_size, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OnsCompanyTypesApi->get_company_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_query** | **str**|  | [optional] 
 **page_number** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **order_by** | **str**|  | [optional] 

### Return type

[**list[OnsCompanyTypeDto]**](OnsCompanyTypeDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_types_for_sector**
> list[OnsCompanyTypeDto] get_company_types_for_sector(ons_sector_id, search_query=search_query, page_number=page_number, page_size=page_size, order_by=order_by)

Returns a list of all ONS company types meeting the request criteria for a give ONS sector

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.OnsCompanyTypesApi()
ons_sector_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
search_query = 'search_query_example' # str |  (optional)
page_number = 56 # int |  (optional)
page_size = 56 # int |  (optional)
order_by = 'order_by_example' # str |  (optional)

try:
    # Returns a list of all ONS company types meeting the request criteria for a give ONS sector
    api_response = api_instance.get_company_types_for_sector(ons_sector_id, search_query=search_query, page_number=page_number, page_size=page_size, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OnsCompanyTypesApi->get_company_types_for_sector: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ons_sector_id** | [**str**](.md)|  | 
 **search_query** | **str**|  | [optional] 
 **page_number** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **order_by** | **str**|  | [optional] 

### Return type

[**list[OnsCompanyTypeDto]**](OnsCompanyTypeDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ons_sectors**
> list[OnsSectorDto] get_ons_sectors(search_query=search_query, page_number=page_number, page_size=page_size, order_by=order_by)

Returns a list of all ONS business sectors meeting the request criteria

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.OnsCompanyTypesApi()
search_query = 'search_query_example' # str |  (optional)
page_number = 56 # int |  (optional)
page_size = 56 # int |  (optional)
order_by = 'order_by_example' # str |  (optional)

try:
    # Returns a list of all ONS business sectors meeting the request criteria
    api_response = api_instance.get_ons_sectors(search_query=search_query, page_number=page_number, page_size=page_size, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OnsCompanyTypesApi->get_ons_sectors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_query** | **str**|  | [optional] 
 **page_number** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **order_by** | **str**|  | [optional] 

### Return type

[**list[OnsSectorDto]**](OnsSectorDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

