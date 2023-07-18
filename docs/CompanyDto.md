# CompanyDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier for the company | [optional] 
**name** | **str** | The company name | [optional] 
**registered_address** | [**AddressDto**](AddressDto.md) |  | [optional] 
**company_types** | [**list[OnsCompanyTypeDto]**](OnsCompanyTypeDto.md) | UK Office for National Statistics (ONS) Company types    A descriptor of the business function | [optional] 
**authenticate_member** | **bool** | Indicates whether the company is a member of the authenticate platform | [optional] 
**is_farm** | **bool** | Indicates whether the company is a farm type | [optional] 
**background** | **str** | General background information about the company | [optional] 
**phone** | **str** | The company phone number | [optional] 
**web** | **str** | The company web address | [optional] 
**number_of_operating_sites** | **str** | The number of operating sites | [optional] 
**number_of_employees** | **str** | Number of employees | [optional] 
**turnover_currency_code** | **str** | The currency that the estimated turnover is recorded in | [optional] 
**estimated_turnover** | **str** | Estimated company annual turnover | [optional] 
**ownership** | **str** | Company ownership type | [optional] 
**established_year** | **int** | The year that the company was established | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

