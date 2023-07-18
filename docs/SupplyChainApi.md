# authenticate_supply_chain.SupplyChainApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_supply_chain**](SupplyChainApi.md#get_supply_chain) | **GET** /api/v1/SupplyChain/{entityId} | Returns the supply chain for a given entity id e.g. product line id
[**get_supply_chain_site_locations**](SupplyChainApi.md#get_supply_chain_site_locations) | **GET** /api/v1/SupplyChain/{entityId}/SiteLocations | Returns the supply chain site locations for a given entity id e.g. product line id

# **get_supply_chain**
> list[EntitySupplyChainDto] get_supply_chain(entity_id, country_ids=country_ids, product_link_id=product_link_id, declared_supply_chain_id=declared_supply_chain_id, search_query=search_query, page_number=page_number, page_size=page_size, order_by=order_by)

Returns the supply chain for a given entity id e.g. product line id

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.SupplyChainApi()
entity_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
country_ids = ['country_ids_example'] # list[str] | Return results where supplier site addresses are in the given countries (optional)
product_link_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Return results for a specific product link (optional)
declared_supply_chain_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Return results for a specific declared supply chain item (optional)
search_query = 'search_query_example' # str |  (optional)
page_number = 56 # int |  (optional)
page_size = 56 # int |  (optional)
order_by = 'order_by_example' # str |  (optional)

try:
    # Returns the supply chain for a given entity id e.g. product line id
    api_response = api_instance.get_supply_chain(entity_id, country_ids=country_ids, product_link_id=product_link_id, declared_supply_chain_id=declared_supply_chain_id, search_query=search_query, page_number=page_number, page_size=page_size, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SupplyChainApi->get_supply_chain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | [**str**](.md)|  | 
 **country_ids** | [**list[str]**](str.md)| Return results where supplier site addresses are in the given countries | [optional] 
 **product_link_id** | [**str**](.md)| Return results for a specific product link | [optional] 
 **declared_supply_chain_id** | [**str**](.md)| Return results for a specific declared supply chain item | [optional] 
 **search_query** | **str**|  | [optional] 
 **page_number** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **order_by** | **str**|  | [optional] 

### Return type

[**list[EntitySupplyChainDto]**](EntitySupplyChainDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_supply_chain_site_locations**
> list[EntitySupplyChainSiteLocationDto] get_supply_chain_site_locations(entity_id)

Returns the supply chain site locations for a given entity id e.g. product line id

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.SupplyChainApi()
entity_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Returns the supply chain site locations for a given entity id e.g. product line id
    api_response = api_instance.get_supply_chain_site_locations(entity_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SupplyChainApi->get_supply_chain_site_locations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | [**str**](.md)|  | 

### Return type

[**list[EntitySupplyChainSiteLocationDto]**](EntitySupplyChainSiteLocationDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

