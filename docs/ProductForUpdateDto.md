# ProductForUpdateDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category_fk** | **str** | The unique identifier for the category in which the product will be stored | 
**reference_code** | **str** | The product reference code | 
**name** | **str** | The product name | 
**sites** | [**list[ProductSiteForManipulationDto]**](ProductSiteForManipulationDto.md) | The sites from which the product is supplied    If a list of sites is not provided. The product will be associated with all of your    sites on platform | [optional] 
**share_declared_countries** | **bool** | If any countries are declared on this product, allow customers to see the declaration | [optional] 
**not_mapped_reason** | [**NotMappingProductLineReasonEnum**](NotMappingProductLineReasonEnum.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

