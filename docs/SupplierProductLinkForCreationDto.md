# SupplierProductLinkForCreationDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**supplier_id** | **str** | The unique identifier for the supplier in the Authenticate platform | 
**my_product_id** | **str** | The unique identifier for your product for which the link is being requested | 
**supplier_site_ids** | **list[str]** | The supplier sites to associated with the link request | [optional] 
**customer_site_ids** | **list[str]** | The customer sites to associated with the link request | [optional] 
**requested_product_reference** | **str** | The reference code that will help your supplier identify the product to which you are requesting a link | 
**requested_product_name** | **str** | The product name that will help your supplier identify the product to which you are requesting a link | 
**raw_material_function_id** | **str** | The function unique identifier for the requested product raw material, if none provided, the default will be &#x27;Supplier&#x27; | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

