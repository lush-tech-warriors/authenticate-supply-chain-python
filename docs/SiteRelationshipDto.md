# SiteRelationshipDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**RelationshipStatusEnum**](RelationshipStatusEnum.md) |  | [optional] 
**status_details** | **str** | The further information regarding the status you have assigned to this site | [optional] 
**risk** | [**RelationshipRiskEnum**](RelationshipRiskEnum.md) |  | [optional] 
**risk_details** | **str** | The further information regarding the risk you have assigned to this site | [optional] 
**review_date** | **datetime** | The review date you have assigned to this site | [optional] 
**review_details** | **str** | The review details you have assigned to this site | [optional] 
**utc_date_last_updated** | **datetime** | The date the status/risk or review details were last updated (UTC) | [optional] 
**last_updated_user** | [**ContactDto**](ContactDto.md) |  | [optional] 
**site_id** | **str** | The site id | [optional] 
**supplier_spend** | **str** | The value you have assigned to this site | [optional] 
**supplier_spend_currency_code** | [**CompanySiteRelationshipCurrencyEnum**](CompanySiteRelationshipCurrencyEnum.md) |  | [optional] 
**functions** | **list[str]** | The functions you have assigned to the site | [optional] 
**categories** | **list[str]** | The categories you have assigned to the site | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

