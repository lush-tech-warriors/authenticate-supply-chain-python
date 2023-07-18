# RawMaterialRecordForUpdateDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference** | **str** | Record reference | 
**received_date** | **datetime** | Date the raw material was received | 
**status** | [**RawMaterialRecordStatusEnum**](RawMaterialRecordStatusEnum.md) |  | [optional] 
**description** | **str** | Raw material record description | [optional] 
**contract_number** | **str** | Raw material record contract number | [optional] 
**quantity_loaded** | **str** | Raw material record quantity loaded | [optional] 
**quantity_received** | **str** | Raw material record quantity received | [optional] 
**assignee_user_id** | **str** | Raw material record assignee user Id | [optional] 
**site_ids** | **list[str]** | Raw material supplied site ids | [optional] 
**country_of_origin_ids** | **list[str]** | Raw material origin countryIds | [optional] 
**destination_country_ids** | **list[str]** | Raw material destination countryIds | [optional] 
**raw_material_record_documents** | [**list[RawMaterialRecordDocumentDto]**](RawMaterialRecordDocumentDto.md) | Raw material record documents | [optional] 
**record_is_complete** | **bool** | Indicate if the record is complete | [optional] 
**raw_material_record_sugar_data** | [**RawMaterialRecordSugarDataDto**](RawMaterialRecordSugarDataDto.md) |  | [optional] 
**id** | **str** | The unique identifier of the raw material Record | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

