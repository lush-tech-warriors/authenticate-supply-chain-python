# authenticate_supply_chain.CompanyLicenceRequestsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_companies_company_id_licence_requests_licence_request_id_complete_post**](CompanyLicenceRequestsApi.md#api_v1_companies_company_id_licence_requests_licence_request_id_complete_post) | **POST** /api/v1/Companies/{companyId}/LicenceRequests/{licenceRequestId}/Complete | Sets a company licence request as completed
[**api_v1_companies_company_id_licence_requests_licence_request_id_reject_post**](CompanyLicenceRequestsApi.md#api_v1_companies_company_id_licence_requests_licence_request_id_reject_post) | **POST** /api/v1/Companies/{companyId}/LicenceRequests/{licenceRequestId}/Reject | Sets a company licence request as rejected and sets a reason
[**api_v1_companies_licence_requests_get**](CompanyLicenceRequestsApi.md#api_v1_companies_licence_requests_get) | **GET** /api/v1/Companies/LicenceRequests | Returns a list of licence requests for your company
[**api_v1_companies_licence_requests_licence_request_id_get**](CompanyLicenceRequestsApi.md#api_v1_companies_licence_requests_licence_request_id_get) | **GET** /api/v1/Companies/LicenceRequests/{licenceRequestId} | Returns a licence request assigned to your company
[**create_company_licence_request**](CompanyLicenceRequestsApi.md#create_company_licence_request) | **POST** /api/v1/Companies/{companyId}/LicenceRequests | Create a company licence request

# **api_v1_companies_company_id_licence_requests_licence_request_id_complete_post**
> LicenceRequestDto api_v1_companies_company_id_licence_requests_licence_request_id_complete_post(company_id, licence_request_id)

Sets a company licence request as completed

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.CompanyLicenceRequestsApi()
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
licence_request_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Sets a company licence request as completed
    api_response = api_instance.api_v1_companies_company_id_licence_requests_licence_request_id_complete_post(company_id, licence_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyLicenceRequestsApi->api_v1_companies_company_id_licence_requests_licence_request_id_complete_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
 **licence_request_id** | [**str**](.md)|  | 

### Return type

[**LicenceRequestDto**](LicenceRequestDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_companies_company_id_licence_requests_licence_request_id_reject_post**
> LicenceRequestDto api_v1_companies_company_id_licence_requests_licence_request_id_reject_post(company_id, licence_request_id, body=body)

Sets a company licence request as rejected and sets a reason

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.CompanyLicenceRequestsApi()
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
licence_request_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = authenticate_supply_chain.LicenceRequestReasonDto() # LicenceRequestReasonDto |  (optional)

try:
    # Sets a company licence request as rejected and sets a reason
    api_response = api_instance.api_v1_companies_company_id_licence_requests_licence_request_id_reject_post(company_id, licence_request_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyLicenceRequestsApi->api_v1_companies_company_id_licence_requests_licence_request_id_reject_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
 **licence_request_id** | [**str**](.md)|  | 
 **body** | [**LicenceRequestReasonDto**](LicenceRequestReasonDto.md)|  | [optional] 

### Return type

[**LicenceRequestDto**](LicenceRequestDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_companies_licence_requests_get**
> list[LicenceRequestDto] api_v1_companies_licence_requests_get(include_completed=include_completed, status=status, created_date_from=created_date_from, created_date_to=created_date_to, requested_for_company_id=requested_for_company_id)

Returns a list of licence requests for your company

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.CompanyLicenceRequestsApi()
include_completed = true # bool | Include completed licence requests (optional)
status = authenticate_supply_chain.LicenceRequestEnum() # LicenceRequestEnum | Filter licence requests by status (optional)
created_date_from = '2013-10-20T19:20:30+01:00' # datetime | Filter licence requests by created date, specifying a from date (optional)
created_date_to = '2013-10-20T19:20:30+01:00' # datetime | Filter licence requests by created date, specifying a to date (optional)
requested_for_company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Filter licence requests by a specific requesting company id (optional)

try:
    # Returns a list of licence requests for your company
    api_response = api_instance.api_v1_companies_licence_requests_get(include_completed=include_completed, status=status, created_date_from=created_date_from, created_date_to=created_date_to, requested_for_company_id=requested_for_company_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyLicenceRequestsApi->api_v1_companies_licence_requests_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_completed** | **bool**| Include completed licence requests | [optional] 
 **status** | [**LicenceRequestEnum**](.md)| Filter licence requests by status | [optional] 
 **created_date_from** | **datetime**| Filter licence requests by created date, specifying a from date | [optional] 
 **created_date_to** | **datetime**| Filter licence requests by created date, specifying a to date | [optional] 
 **requested_for_company_id** | [**str**](.md)| Filter licence requests by a specific requesting company id | [optional] 

### Return type

[**list[LicenceRequestDto]**](LicenceRequestDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_companies_licence_requests_licence_request_id_get**
> LicenceRequestDto api_v1_companies_licence_requests_licence_request_id_get(licence_request_id)

Returns a licence request assigned to your company

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.CompanyLicenceRequestsApi()
licence_request_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Returns a licence request assigned to your company
    api_response = api_instance.api_v1_companies_licence_requests_licence_request_id_get(licence_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyLicenceRequestsApi->api_v1_companies_licence_requests_licence_request_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **licence_request_id** | [**str**](.md)|  | 

### Return type

[**LicenceRequestDto**](LicenceRequestDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_company_licence_request**
> LicenceRequestDto create_company_licence_request(company_id, body=body)

Create a company licence request

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.CompanyLicenceRequestsApi()
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = authenticate_supply_chain.LicenceRequestDtoForCreation() # LicenceRequestDtoForCreation |  (optional)

try:
    # Create a company licence request
    api_response = api_instance.create_company_licence_request(company_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyLicenceRequestsApi->create_company_licence_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
 **body** | [**LicenceRequestDtoForCreation**](LicenceRequestDtoForCreation.md)|  | [optional] 

### Return type

[**LicenceRequestDto**](LicenceRequestDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

