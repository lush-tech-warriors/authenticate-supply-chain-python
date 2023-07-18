# SiteDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier for the site in the Authenticate platform | [optional] 
**name** | **str** | The Site Name | [optional] 
**company_id** | **str** | The unique identifier for the owning company in the Authenticate platform | [optional] 
**company_name** | **str** | The name of the company to which the site belongs | [optional] 
**address** | [**AddressDto**](AddressDto.md) |  | [optional] 
**supplier_codes** | [**list[SupplierCodeDto]**](SupplierCodeDto.md) | One or more codes, assigned by you, that uniquely identify this site. | [optional] 
**site_operations** | [**list[OnsSiteOperationDto]**](OnsSiteOperationDto.md) | none or more ONS site Operations | [optional] 
**company_site_name** | **str** | Company and site name display property. If the company name matches the site name return just the company name,  otherwise return company name | site name | [optional] 
**primary_site** | **bool** | Indicates whether the site is the primary site | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

