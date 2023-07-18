# authenticate_supply_chain.SitesApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_company_company_id_sites_post**](SitesApi.md#api_v1_company_company_id_sites_post) | **POST** /api/v1/Company/{companyId}/Sites | Add a new site to a company.
[**get_company_sites**](SitesApi.md#get_company_sites) | **GET** /api/v1/Company/{companyId}/Sites | Returns a list of all sites for a company - not using supply chain
[**get_site**](SitesApi.md#get_site) | **GET** /api/v1/Suppliers/{supplierId}/Sites/{siteId} | Returns a specified site
[**get_sites**](SitesApi.md#get_sites) | **GET** /api/v1/Sites | Returns a list of all sites meeting the request criteria - not using the supply chain
[**get_sites_from_supply_chain**](SitesApi.md#get_sites_from_supply_chain) | **GET** /api/v1/Suppliers/Sites | Returns a list of all sites meeting the request criteria
[**get_supplier_sites**](SitesApi.md#get_supplier_sites) | **GET** /api/v1/Suppliers/{supplierId}/Sites | Returns a list of all sites meeting the request criteria
[**search_sites**](SitesApi.md#search_sites) | **POST** /api/v1/Sites/Search | Returns a list of all sites meeting the request criteria - not using the supply chain
[**search_sites_from_supply_chain**](SitesApi.md#search_sites_from_supply_chain) | **POST** /api/v1/Suppliers/Sites/Search | Returns a list of all sites meeting the request criteria

# **api_v1_company_company_id_sites_post**
> SiteDto api_v1_company_company_id_sites_post(company_id, body=body)

Add a new site to a company.

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.SitesApi()
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = authenticate_supply_chain.SiteDto() # SiteDto |  (optional)

try:
    # Add a new site to a company.
    api_response = api_instance.api_v1_company_company_id_sites_post(company_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SitesApi->api_v1_company_company_id_sites_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
 **body** | [**SiteDto**](SiteDto.md)|  | [optional] 

### Return type

[**SiteDto**](SiteDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_sites**
> list[SiteDto] get_company_sites(company_id)

Returns a list of all sites for a company - not using supply chain

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.SitesApi()
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Returns a list of all sites for a company - not using supply chain
    api_response = api_instance.get_company_sites(company_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SitesApi->get_company_sites: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 

### Return type

[**list[SiteDto]**](SiteDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_site**
> SiteDto get_site(supplier_id, site_id)

Returns a specified site

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.SitesApi()
supplier_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
site_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The unique identifier for the site to return

try:
    # Returns a specified site
    api_response = api_instance.get_site(supplier_id, site_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SitesApi->get_site: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supplier_id** | [**str**](.md)|  | 
 **site_id** | [**str**](.md)| The unique identifier for the site to return | 

### Return type

[**SiteDto**](SiteDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sites**
> list[SiteDto] get_sites(search_query=search_query, page_number=page_number, page_size=page_size, order_by=order_by, function_values=function_values, status_values=status_values, risk_values=risk_values, country_ids=country_ids, site_ids=site_ids, primary_site=primary_site, company_id=company_id, supplier_codes=supplier_codes, licence_numbers=licence_numbers, esg_assessment_outcome=esg_assessment_outcome, esg_assessment_status=esg_assessment_status)

Returns a list of all sites meeting the request criteria - not using the supply chain

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.SitesApi()
search_query = 'search_query_example' # str |  (optional)
page_number = 56 # int |  (optional)
page_size = 56 # int |  (optional)
order_by = 'order_by_example' # str |  (optional)
function_values = ['function_values_example'] # list[str] |  (optional)
status_values = ['status_values_example'] # list[str] |  (optional)
risk_values = ['risk_values_example'] # list[str] |  (optional)
country_ids = ['country_ids_example'] # list[str] |  (optional)
site_ids = ['site_ids_example'] # list[str] |  (optional)
primary_site = true # bool |  (optional)
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str |  (optional)
supplier_codes = ['supplier_codes_example'] # list[str] |  (optional)
licence_numbers = ['licence_numbers_example'] # list[str] |  (optional)
esg_assessment_outcome = authenticate_supply_chain.EsgOutcomeEnum() # EsgOutcomeEnum | Filter by ESG Assessment outcome score (optional)
esg_assessment_status = authenticate_supply_chain.EsgStatusEnum() # EsgStatusEnum | Filter by ESG Assessment status score (optional)

try:
    # Returns a list of all sites meeting the request criteria - not using the supply chain
    api_response = api_instance.get_sites(search_query=search_query, page_number=page_number, page_size=page_size, order_by=order_by, function_values=function_values, status_values=status_values, risk_values=risk_values, country_ids=country_ids, site_ids=site_ids, primary_site=primary_site, company_id=company_id, supplier_codes=supplier_codes, licence_numbers=licence_numbers, esg_assessment_outcome=esg_assessment_outcome, esg_assessment_status=esg_assessment_status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SitesApi->get_sites: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_query** | **str**|  | [optional] 
 **page_number** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **order_by** | **str**|  | [optional] 
 **function_values** | [**list[str]**](str.md)|  | [optional] 
 **status_values** | [**list[str]**](str.md)|  | [optional] 
 **risk_values** | [**list[str]**](str.md)|  | [optional] 
 **country_ids** | [**list[str]**](str.md)|  | [optional] 
 **site_ids** | [**list[str]**](str.md)|  | [optional] 
 **primary_site** | **bool**|  | [optional] 
 **company_id** | [**str**](.md)|  | [optional] 
 **supplier_codes** | [**list[str]**](str.md)|  | [optional] 
 **licence_numbers** | [**list[str]**](str.md)|  | [optional] 
 **esg_assessment_outcome** | [**EsgOutcomeEnum**](.md)| Filter by ESG Assessment outcome score | [optional] 
 **esg_assessment_status** | [**EsgStatusEnum**](.md)| Filter by ESG Assessment status score | [optional] 

### Return type

[**list[SiteDto]**](SiteDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sites_from_supply_chain**
> list[SiteDto] get_sites_from_supply_chain(supplier_tiers=supplier_tiers, category_ids=category_ids, supplier_codes=supplier_codes, search_type=search_type, search_term=search_term, function_values=function_values, status_values=status_values, risk_values=risk_values, country_ids=country_ids, site_ids=site_ids, primary_site=primary_site, company_id=company_id, licence_numbers=licence_numbers, esg_assessment_outcome=esg_assessment_outcome, esg_assessment_status=esg_assessment_status, search_query=search_query, page_number=page_number, page_size=page_size, order_by=order_by)

Returns a list of all sites meeting the request criteria

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.SitesApi()
supplier_tiers = [56] # list[int] |  (optional)
category_ids = ['category_ids_example'] # list[str] |  (optional)
supplier_codes = ['supplier_codes_example'] # list[str] |  (optional)
search_type = authenticate_supply_chain.SiteSearchTypeEnum() # SiteSearchTypeEnum |  (optional)
search_term = 'search_term_example' # str |  (optional)
function_values = ['function_values_example'] # list[str] |  (optional)
status_values = ['status_values_example'] # list[str] |  (optional)
risk_values = ['risk_values_example'] # list[str] |  (optional)
country_ids = ['country_ids_example'] # list[str] |  (optional)
site_ids = ['site_ids_example'] # list[str] |  (optional)
primary_site = true # bool |  (optional)
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str |  (optional)
licence_numbers = ['licence_numbers_example'] # list[str] |  (optional)
esg_assessment_outcome = authenticate_supply_chain.EsgOutcomeEnum() # EsgOutcomeEnum | Filter by ESG Assessment outcome score (optional)
esg_assessment_status = authenticate_supply_chain.EsgStatusEnum() # EsgStatusEnum | Filter by ESG Assessment status score (optional)
search_query = 'search_query_example' # str |  (optional)
page_number = 56 # int |  (optional)
page_size = 56 # int |  (optional)
order_by = 'order_by_example' # str |  (optional)

try:
    # Returns a list of all sites meeting the request criteria
    api_response = api_instance.get_sites_from_supply_chain(supplier_tiers=supplier_tiers, category_ids=category_ids, supplier_codes=supplier_codes, search_type=search_type, search_term=search_term, function_values=function_values, status_values=status_values, risk_values=risk_values, country_ids=country_ids, site_ids=site_ids, primary_site=primary_site, company_id=company_id, licence_numbers=licence_numbers, esg_assessment_outcome=esg_assessment_outcome, esg_assessment_status=esg_assessment_status, search_query=search_query, page_number=page_number, page_size=page_size, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SitesApi->get_sites_from_supply_chain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supplier_tiers** | [**list[int]**](int.md)|  | [optional] 
 **category_ids** | [**list[str]**](str.md)|  | [optional] 
 **supplier_codes** | [**list[str]**](str.md)|  | [optional] 
 **search_type** | [**SiteSearchTypeEnum**](.md)|  | [optional] 
 **search_term** | **str**|  | [optional] 
 **function_values** | [**list[str]**](str.md)|  | [optional] 
 **status_values** | [**list[str]**](str.md)|  | [optional] 
 **risk_values** | [**list[str]**](str.md)|  | [optional] 
 **country_ids** | [**list[str]**](str.md)|  | [optional] 
 **site_ids** | [**list[str]**](str.md)|  | [optional] 
 **primary_site** | **bool**|  | [optional] 
 **company_id** | [**str**](.md)|  | [optional] 
 **licence_numbers** | [**list[str]**](str.md)|  | [optional] 
 **esg_assessment_outcome** | [**EsgOutcomeEnum**](.md)| Filter by ESG Assessment outcome score | [optional] 
 **esg_assessment_status** | [**EsgStatusEnum**](.md)| Filter by ESG Assessment status score | [optional] 
 **search_query** | **str**|  | [optional] 
 **page_number** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **order_by** | **str**|  | [optional] 

### Return type

[**list[SiteDto]**](SiteDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_supplier_sites**
> list[SiteDto] get_supplier_sites(supplier_id, supplier_code=supplier_code, country=country, postcode=postcode, search_query=search_query, page_number=page_number, page_size=page_size, order_by=order_by)

Returns a list of all sites meeting the request criteria

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.SitesApi()
supplier_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
supplier_code = 'supplier_code_example' # str | Filter by the site code you have assigned (optional)
country = 'country_example' # str | Filter site by country (optional)
postcode = 'postcode_example' # str | Filter site by postcode (optional)
search_query = 'search_query_example' # str |  (optional)
page_number = 56 # int |  (optional)
page_size = 56 # int |  (optional)
order_by = 'order_by_example' # str |  (optional)

try:
    # Returns a list of all sites meeting the request criteria
    api_response = api_instance.get_supplier_sites(supplier_id, supplier_code=supplier_code, country=country, postcode=postcode, search_query=search_query, page_number=page_number, page_size=page_size, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SitesApi->get_supplier_sites: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supplier_id** | [**str**](.md)|  | 
 **supplier_code** | **str**| Filter by the site code you have assigned | [optional] 
 **country** | **str**| Filter site by country | [optional] 
 **postcode** | **str**| Filter site by postcode | [optional] 
 **search_query** | **str**|  | [optional] 
 **page_number** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **order_by** | **str**|  | [optional] 

### Return type

[**list[SiteDto]**](SiteDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_sites**
> list[SiteDto] search_sites(body=body)

Returns a list of all sites meeting the request criteria - not using the supply chain

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.SitesApi()
body = authenticate_supply_chain.SiteResourceParametersExtended() # SiteResourceParametersExtended |  (optional)

try:
    # Returns a list of all sites meeting the request criteria - not using the supply chain
    api_response = api_instance.search_sites(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SitesApi->search_sites: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SiteResourceParametersExtended**](SiteResourceParametersExtended.md)|  | [optional] 

### Return type

[**list[SiteDto]**](SiteDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_sites_from_supply_chain**
> list[SiteDto] search_sites_from_supply_chain(body=body)

Returns a list of all sites meeting the request criteria

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.SitesApi()
body = authenticate_supply_chain.SiteSupplyChainResourceParameters() # SiteSupplyChainResourceParameters |  (optional)

try:
    # Returns a list of all sites meeting the request criteria
    api_response = api_instance.search_sites_from_supply_chain(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SitesApi->search_sites_from_supply_chain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SiteSupplyChainResourceParameters**](SiteSupplyChainResourceParameters.md)|  | [optional] 

### Return type

[**list[SiteDto]**](SiteDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

