# authenticate_supply_chain.SiteLicencesApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_sites_site_id_licences_get**](SiteLicencesApi.md#api_v1_sites_site_id_licences_get) | **GET** /api/v1/Sites/{siteId}/Licences | Returns a list of licences for a site
[**api_v1_sites_site_id_licences_licence_id_put**](SiteLicencesApi.md#api_v1_sites_site_id_licences_licence_id_put) | **PUT** /api/v1/Sites/{siteId}/Licences/{licenceId} | Fully update a site licence
[**create_site_licence**](SiteLicencesApi.md#create_site_licence) | **POST** /api/v1/Sites/{siteId}/Licences | Create a site licence
[**delete_site_licence**](SiteLicencesApi.md#delete_site_licence) | **DELETE** /api/v1/Sites/{siteId}/Licences/{licenceId} | Delete a site licence
[**patch_site_licence**](SiteLicencesApi.md#patch_site_licence) | **PATCH** /api/v1/Sites/{siteId}/Licences/{licenceId} | Partially update a site licence. Only provided fields will be updated

# **api_v1_sites_site_id_licences_get**
> list[LicenceDto] api_v1_sites_site_id_licences_get(site_id)

Returns a list of licences for a site

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.SiteLicencesApi()
site_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Returns a list of licences for a site
    api_response = api_instance.api_v1_sites_site_id_licences_get(site_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteLicencesApi->api_v1_sites_site_id_licences_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | [**str**](.md)|  | 

### Return type

[**list[LicenceDto]**](LicenceDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_sites_site_id_licences_licence_id_put**
> LicenceDto api_v1_sites_site_id_licences_licence_id_put(site_id, licence_id, body=body)

Fully update a site licence

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.SiteLicencesApi()
site_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
licence_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = authenticate_supply_chain.LicenceDto() # LicenceDto |  (optional)

try:
    # Fully update a site licence
    api_response = api_instance.api_v1_sites_site_id_licences_licence_id_put(site_id, licence_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteLicencesApi->api_v1_sites_site_id_licences_licence_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | [**str**](.md)|  | 
 **licence_id** | [**str**](.md)|  | 
 **body** | [**LicenceDto**](LicenceDto.md)|  | [optional] 

### Return type

[**LicenceDto**](LicenceDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_site_licence**
> LicenceDto create_site_licence(site_id, body=body)

Create a site licence

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.SiteLicencesApi()
site_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = authenticate_supply_chain.LicenceDto() # LicenceDto |  (optional)

try:
    # Create a site licence
    api_response = api_instance.create_site_licence(site_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteLicencesApi->create_site_licence: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | [**str**](.md)|  | 
 **body** | [**LicenceDto**](LicenceDto.md)|  | [optional] 

### Return type

[**LicenceDto**](LicenceDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_site_licence**
> delete_site_licence(site_id, licence_id)

Delete a site licence

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.SiteLicencesApi()
site_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
licence_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Delete a site licence
    api_instance.delete_site_licence(site_id, licence_id)
except ApiException as e:
    print("Exception when calling SiteLicencesApi->delete_site_licence: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | [**str**](.md)|  | 
 **licence_id** | [**str**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_site_licence**
> LicenceDto patch_site_licence(site_id, licence_id, body=body)

Partially update a site licence. Only provided fields will be updated

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.SiteLicencesApi()
site_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
licence_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = [authenticate_supply_chain.Operation()] # list[Operation] |  (optional)

try:
    # Partially update a site licence. Only provided fields will be updated
    api_response = api_instance.patch_site_licence(site_id, licence_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteLicencesApi->patch_site_licence: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | [**str**](.md)|  | 
 **licence_id** | [**str**](.md)|  | 
 **body** | [**list[Operation]**](Operation.md)|  | [optional] 

### Return type

[**LicenceDto**](LicenceDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

