# authenticate_supply_chain.CertificatesApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_site_certificate**](CertificatesApi.md#get_site_certificate) | **GET** /api/v1/Suppliers/{supplierId}/Sites/{siteId}/Certificates/{certificateId} | Returns a specified certificate
[**get_site_certificates**](CertificatesApi.md#get_site_certificates) | **GET** /api/v1/Suppliers/{supplierId}/Sites/{siteId}/Certificates | Returns a list of all certificates for a site where the certificates meet the request criteria
[**get_site_certification_statuses**](CertificatesApi.md#get_site_certification_statuses) | **GET** /api/v1/Suppliers/{supplierId}/Sites/{siteId}/CertificateStatus | 

# **get_site_certificate**
> CertificateDto get_site_certificate(supplier_id, site_id, certificate_id)

Returns a specified certificate

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.CertificatesApi()
supplier_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
site_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The unique identifier for the certificate to return
certificate_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Returns a specified certificate
    api_response = api_instance.get_site_certificate(supplier_id, site_id, certificate_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CertificatesApi->get_site_certificate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supplier_id** | [**str**](.md)|  | 
 **site_id** | [**str**](.md)| The unique identifier for the certificate to return | 
 **certificate_id** | [**str**](.md)|  | 

### Return type

[**CertificateDto**](CertificateDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_site_certificates**
> list[CertificateDto] get_site_certificates(supplier_id, site_id, scheme_certificate_id=scheme_certificate_id, status=status, scheme_type=scheme_type, scheme_name=scheme_name, search_query=search_query, page_number=page_number, page_size=page_size, order_by=order_by)

Returns a list of all certificates for a site where the certificates meet the request criteria

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.CertificatesApi()
supplier_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
site_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
scheme_certificate_id = 'scheme_certificate_id_example' # str | Search by the Id assigned to the certificate by the scheme owner (optional)
status = 'status_example' # str | filter by certificate status (optional)
scheme_type = 'scheme_type_example' # str | filter by Scheme Type (optional)
scheme_name = 'scheme_name_example' # str | filter by Scheme name (optional)
search_query = 'search_query_example' # str |  (optional)
page_number = 56 # int |  (optional)
page_size = 56 # int |  (optional)
order_by = 'order_by_example' # str |  (optional)

try:
    # Returns a list of all certificates for a site where the certificates meet the request criteria
    api_response = api_instance.get_site_certificates(supplier_id, site_id, scheme_certificate_id=scheme_certificate_id, status=status, scheme_type=scheme_type, scheme_name=scheme_name, search_query=search_query, page_number=page_number, page_size=page_size, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CertificatesApi->get_site_certificates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supplier_id** | [**str**](.md)|  | 
 **site_id** | [**str**](.md)|  | 
 **scheme_certificate_id** | **str**| Search by the Id assigned to the certificate by the scheme owner | [optional] 
 **status** | **str**| filter by certificate status | [optional] 
 **scheme_type** | **str**| filter by Scheme Type | [optional] 
 **scheme_name** | **str**| filter by Scheme name | [optional] 
 **search_query** | **str**|  | [optional] 
 **page_number** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **order_by** | **str**|  | [optional] 

### Return type

[**list[CertificateDto]**](CertificateDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_site_certification_statuses**
> list[SiteCertificationStatusDto] get_site_certification_statuses(supplier_id, site_id, order_by=order_by, search_query=search_query, page_number=page_number, page_size=page_size)



### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.CertificatesApi()
supplier_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
site_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
order_by = 'order_by_example' # str | Specify order of results (optional)
search_query = 'search_query_example' # str |  (optional)
page_number = 56 # int |  (optional)
page_size = 56 # int |  (optional)

try:
    api_response = api_instance.get_site_certification_statuses(supplier_id, site_id, order_by=order_by, search_query=search_query, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CertificatesApi->get_site_certification_statuses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supplier_id** | [**str**](.md)|  | 
 **site_id** | [**str**](.md)|  | 
 **order_by** | **str**| Specify order of results | [optional] 
 **search_query** | **str**|  | [optional] 
 **page_number** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 

### Return type

[**list[SiteCertificationStatusDto]**](SiteCertificationStatusDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

