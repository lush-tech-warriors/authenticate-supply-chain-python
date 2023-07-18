# SupplierProductLinkDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the product link within the Authenticate platform | [optional] 
**status** | **str** | The status of this link. Pending and Accepted are current \&quot;Active\&quot; links, any other value is no longer \&quot;Active\&quot; | [optional] 
**status_message** | **str** | The message included when setting the current status. Generally only included when rejecting, removing or rescinding a link request | [optional] 
**requested_product_reference** | **str** | The product reference code specified in the original link request | [optional] 
**requested_product_name** | **str** | The product name specified in the original link request | [optional] 
**request_message** | **str** | The message included in the original link request | [optional] 
**link_created_date** | **datetime** | The UTC date and time at which the link was initially created | [optional] 
**status_updated_date** | **datetime** | The UTC date and time at which the Status was changed (e.g. from Pending to Accepted) | [optional] 
**raw_material_id** | **str** | the raw material associated with the product link | [optional] 
**my_product_id** | **str** | The unique identifier of my product. | [optional] 
**my_product_reference** | **str** | The reference code of my product. | [optional] 
**my_product_name** | **str** | The name of my product. | [optional] 
**supplier_id** | **str** | The unique identifier of the supplier company. | [optional] 
**supplier_name** | **str** | The name of the supplier company | [optional] 
**supplier_product_id** | **str** | The unique identifier of the supplier&#x27;s product. Could be null if this is a Pending link request | [optional] 
**supplier_product_reference** | **str** | The reference code of the supplier&#x27;s product. Could be null if this is a Pending link request | [optional] 
**supplier_product_name** | **str** | The name of the supplier&#x27;s product. Could be null if this is a Pending link request | [optional] 
**supplier_sites** | [**list[SupplierLinkSiteDto]**](SupplierLinkSiteDto.md) | Supplier sites associated with the production of the supplied product | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

