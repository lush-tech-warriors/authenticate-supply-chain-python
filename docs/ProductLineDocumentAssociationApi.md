# authenticate_supply_chain.ProductLineDocumentAssociationApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_product_line_document_association_get**](ProductLineDocumentAssociationApi.md#api_v1_product_line_document_association_get) | **GET** /api/v1/ProductLineDocumentAssociation | Returns a list of product line document associations.
[**api_v1_product_line_document_association_product_line_document_association_id_delete**](ProductLineDocumentAssociationApi.md#api_v1_product_line_document_association_product_line_document_association_id_delete) | **DELETE** /api/v1/ProductLineDocumentAssociation/{productLineDocumentAssociationId} | Deletes a product line document association.
[**api_v1_product_line_product_line_id_product_line_document_association_post**](ProductLineDocumentAssociationApi.md#api_v1_product_line_product_line_id_product_line_document_association_post) | **POST** /api/v1/ProductLine/{productLineId}/ProductLineDocumentAssociation | Saves a new product line document association.

# **api_v1_product_line_document_association_get**
> list[ProductLineDocumentAssociationDto] api_v1_product_line_document_association_get(product_line_id=product_line_id)

Returns a list of product line document associations.

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.ProductLineDocumentAssociationApi()
product_line_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The product line id. (optional)

try:
    # Returns a list of product line document associations.
    api_response = api_instance.api_v1_product_line_document_association_get(product_line_id=product_line_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductLineDocumentAssociationApi->api_v1_product_line_document_association_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_line_id** | [**str**](.md)| The product line id. | [optional] 

### Return type

[**list[ProductLineDocumentAssociationDto]**](ProductLineDocumentAssociationDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_product_line_document_association_product_line_document_association_id_delete**
> ProductLineDocumentAssociationDto api_v1_product_line_document_association_product_line_document_association_id_delete(product_line_document_association_id)

Deletes a product line document association.

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.ProductLineDocumentAssociationApi()
product_line_document_association_id = 56 # int | The id of the product line document association to delete.

try:
    # Deletes a product line document association.
    api_response = api_instance.api_v1_product_line_document_association_product_line_document_association_id_delete(product_line_document_association_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductLineDocumentAssociationApi->api_v1_product_line_document_association_product_line_document_association_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_line_document_association_id** | **int**| The id of the product line document association to delete. | 

### Return type

[**ProductLineDocumentAssociationDto**](ProductLineDocumentAssociationDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_product_line_product_line_id_product_line_document_association_post**
> ProductLineDocumentAssociationDto api_v1_product_line_product_line_id_product_line_document_association_post(product_line_id, body=body)

Saves a new product line document association.

### Example
```python
from __future__ import print_function
import time
import authenticate_supply_chain
from authenticate_supply_chain.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_supply_chain.ProductLineDocumentAssociationApi()
product_line_id = 'product_line_id_example' # str | 
body = authenticate_supply_chain.ProductLineDocumentAssociationDto() # ProductLineDocumentAssociationDto | The product line association dto. (optional)

try:
    # Saves a new product line document association.
    api_response = api_instance.api_v1_product_line_product_line_id_product_line_document_association_post(product_line_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductLineDocumentAssociationApi->api_v1_product_line_product_line_id_product_line_document_association_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_line_id** | **str**|  | 
 **body** | [**ProductLineDocumentAssociationDto**](ProductLineDocumentAssociationDto.md)| The product line association dto. | [optional] 

### Return type

[**ProductLineDocumentAssociationDto**](ProductLineDocumentAssociationDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

