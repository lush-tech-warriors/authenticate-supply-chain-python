# authenticate_supply_chain.CompanyLicencesApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_companies_company_id_licences_get**](CompanyLicencesApi.md#api_v1_companies_company_id_licences_get) | **GET** /api/v1/Companies/{companyId}/Licences | Returns a list of licences for a company
[**api_v1_companies_company_id_licences_licence_id_put**](CompanyLicencesApi.md#api_v1_companies_company_id_licences_licence_id_put) | **PUT** /api/v1/Companies/{companyId}/Licences/{licenceId} | Fully update a company licence
[**create_company_licence**](CompanyLicencesApi.md#create_company_licence) | **POST** /api/v1/Companies/{companyId}/Licences | Create a company licence
[**delete_company_licence**](CompanyLicencesApi.md#delete_company_licence) | **DELETE** /api/v1/Companies/{companyId}/Licences/{licenceId} | Delete a company licence
[**patch_company_licence**](CompanyLicencesApi.md#patch_company_licence) | **PATCH** /api/v1/Companies/{companyId}/Licences/{licenceId} | Partially update a company licence. Only provided fields will be updated

# **api_v1_companies_company_id_licences_get**
> list[LicenceDto] api_v1_companies_company_id_licences_get(company_id)

Returns a list of licences for a company

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.CompanyLicencesApi()
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Returns a list of licences for a company
    api_response = api_instance.api_v1_companies_company_id_licences_get(company_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyLicencesApi->api_v1_companies_company_id_licences_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 

### Return type

[**list[LicenceDto]**](LicenceDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_companies_company_id_licences_licence_id_put**
> LicenceDto api_v1_companies_company_id_licences_licence_id_put(company_id, licence_id, body=body)

Fully update a company licence

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.CompanyLicencesApi()
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
licence_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = authenticate_supply_chain.LicenceDto() # LicenceDto |  (optional)

try:
    # Fully update a company licence
    api_response = api_instance.api_v1_companies_company_id_licences_licence_id_put(company_id, licence_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyLicencesApi->api_v1_companies_company_id_licences_licence_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
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

# **create_company_licence**
> LicenceDto create_company_licence(company_id, body=body)

Create a company licence

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.CompanyLicencesApi()
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = authenticate_supply_chain.LicenceDto() # LicenceDto |  (optional)

try:
    # Create a company licence
    api_response = api_instance.create_company_licence(company_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyLicencesApi->create_company_licence: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
 **body** | [**LicenceDto**](LicenceDto.md)|  | [optional] 

### Return type

[**LicenceDto**](LicenceDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_company_licence**
> delete_company_licence(company_id, licence_id)

Delete a company licence

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.CompanyLicencesApi()
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
licence_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Delete a company licence
    api_instance.delete_company_licence(company_id, licence_id)
except ApiException as e:
    print("Exception when calling CompanyLicencesApi->delete_company_licence: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
 **licence_id** | [**str**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_company_licence**
> LicenceDto patch_company_licence(company_id, licence_id, body=body)

Partially update a company licence. Only provided fields will be updated

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.CompanyLicencesApi()
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
licence_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = [authenticate_supply_chain.Operation()] # list[Operation] |  (optional)

try:
    # Partially update a company licence. Only provided fields will be updated
    api_response = api_instance.patch_company_licence(company_id, licence_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyLicencesApi->patch_company_licence: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
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

