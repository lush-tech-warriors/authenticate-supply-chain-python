# authenticate_supply_chain.DeclaredSupplyChainStatusApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_declared_supply_chain_declared_supply_chain_id_declared_supply_chain_status_get**](DeclaredSupplyChainStatusApi.md#api_v1_declared_supply_chain_declared_supply_chain_id_declared_supply_chain_status_get) | **GET** /api/v1/DeclaredSupplyChain/{declaredSupplyChainId}/DeclaredSupplyChainStatus | Returns a list of all declared supply chains statuses by declared supply chain id.
[**api_v1_declared_supply_chain_declared_supply_chain_id_declared_supply_chain_status_post**](DeclaredSupplyChainStatusApi.md#api_v1_declared_supply_chain_declared_supply_chain_id_declared_supply_chain_status_post) | **POST** /api/v1/DeclaredSupplyChain/{declaredSupplyChainId}/DeclaredSupplyChainStatus | Create a new Declared Supply Chain Status

# **api_v1_declared_supply_chain_declared_supply_chain_id_declared_supply_chain_status_get**
> list[DeclaredSupplyChainDto] api_v1_declared_supply_chain_declared_supply_chain_id_declared_supply_chain_status_get(declared_supply_chain_id)

Returns a list of all declared supply chains statuses by declared supply chain id.

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.DeclaredSupplyChainStatusApi()
declared_supply_chain_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Returns a list of all declared supply chains statuses by declared supply chain id.
    api_response = api_instance.api_v1_declared_supply_chain_declared_supply_chain_id_declared_supply_chain_status_get(declared_supply_chain_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeclaredSupplyChainStatusApi->api_v1_declared_supply_chain_declared_supply_chain_id_declared_supply_chain_status_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **declared_supply_chain_id** | [**str**](.md)|  | 

### Return type

[**list[DeclaredSupplyChainDto]**](DeclaredSupplyChainDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_declared_supply_chain_declared_supply_chain_id_declared_supply_chain_status_post**
> DeclaredSupplyChainStatusDto api_v1_declared_supply_chain_declared_supply_chain_id_declared_supply_chain_status_post(declared_supply_chain_id, body=body)

Create a new Declared Supply Chain Status

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.DeclaredSupplyChainStatusApi()
declared_supply_chain_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = authenticate_supply_chain.DeclaredSupplyChainStatusDto() # DeclaredSupplyChainStatusDto |  (optional)

try:
    # Create a new Declared Supply Chain Status
    api_response = api_instance.api_v1_declared_supply_chain_declared_supply_chain_id_declared_supply_chain_status_post(declared_supply_chain_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeclaredSupplyChainStatusApi->api_v1_declared_supply_chain_declared_supply_chain_id_declared_supply_chain_status_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **declared_supply_chain_id** | [**str**](.md)|  | 
 **body** | [**DeclaredSupplyChainStatusDto**](DeclaredSupplyChainStatusDto.md)|  | [optional] 

### Return type

[**DeclaredSupplyChainStatusDto**](DeclaredSupplyChainStatusDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

