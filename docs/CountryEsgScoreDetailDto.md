# CountryEsgScoreDetailDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | URl of the resource that generated the score | [optional] 
**name** | **str** | Name of the resource that generated the score | [optional] 
**unit** | **str** | Unit of the score if applicable | [optional] 
**source** | **str** | Name of the source of the data that generated the score | [optional] 
**currency** | **str** | Currency fo the data if applicable | [optional] 
**frequency** | **str** | Frequency of the acquisition of the data | [optional] 
**description** | **str** | Description of the resource | [optional] 
**last_updated** | **str** | Optional last updated text | [optional] 
**last_updated_date** | **datetime** | The date the data was last updated | [optional] 
**risk_points** | **int** | The Score Risk | [optional] 
**maximum_risk_points** | **int** | The maximum risk for this score | [optional] 
**score** | **str** | The Score for the score | [optional] 
**thresholds** | [**list[CountryEsgScoreThresholdDto]**](CountryEsgScoreThresholdDto.md) | Thresholds associated with this score. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

