# authenticate_supply_chain.SupplyChainSnapshotApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**synchronise_supply_chain_snapshots_for_product**](SupplyChainSnapshotApi.md#synchronise_supply_chain_snapshots_for_product) | **GET** /api/v1/SupplyChainSnapshot/Synchronise/Product/{productId} | Update the supply chain using a specific product id
[**synchronise_supply_chain_snapshots_for_product_link**](SupplyChainSnapshotApi.md#synchronise_supply_chain_snapshots_for_product_link) | **GET** /api/v1/SupplyChainSnapshot/Synchronise/ProductLink/{productLinkId} | Update the supply chain using a specific product link id

# **synchronise_supply_chain_snapshots_for_product**
> synchronise_supply_chain_snapshots_for_product(product_id)

Update the supply chain using a specific product id

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.SupplyChainSnapshotApi()
product_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Update the supply chain using a specific product id
    api_instance.synchronise_supply_chain_snapshots_for_product(product_id)
except ApiException as e:
    print("Exception when calling SupplyChainSnapshotApi->synchronise_supply_chain_snapshots_for_product: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | [**str**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **synchronise_supply_chain_snapshots_for_product_link**
> synchronise_supply_chain_snapshots_for_product_link(product_link_id)

Update the supply chain using a specific product link id

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.SupplyChainSnapshotApi()
product_link_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Update the supply chain using a specific product link id
    api_instance.synchronise_supply_chain_snapshots_for_product_link(product_link_id)
except ApiException as e:
    print("Exception when calling SupplyChainSnapshotApi->synchronise_supply_chain_snapshots_for_product_link: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_link_id** | [**str**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

