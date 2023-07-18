# SupplierResourceParameters

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search_query** | **str** |  | [optional] 
**page_number** | **int** |  | [optional] 
**page_size** | **int** |  | [optional] 
**country** | **str** | Filter supplier by country | [optional] 
**postcode** | **str** | Filter supplier by postcode | [optional] 
**authenticate_member** | **bool** | Filter by whether the company is a member of the authenticate platform or not | [optional] 
**company_type** | **str** | Filter by ONS Company Type | [optional] 
**company_ids** | **list[str]** | Filter by list of company id&#x27;s | [optional] 
**supplier_codes** | **list[str]** | Filter by supplier codes | [optional] 
**licence_numbers** | **list[str]** | Filter by licence numbers | [optional] 
**supplier_id** | **str** | Filter by a specific supplier id | [optional] 
**supplier_code** | **str** | Filter by the supplier code you have assigned | [optional] 
**supplier_status** | **str** | Filter by the supplier status you have assigned  Status values are: Approved, Pending, Suspended, Rejected | [optional] 
**supplier_risk** | **str** | Filter by the supplier risk  you have assigned  Risks are: Low, Medium, High | [optional] 
**tier** | **list[int]** | Filter supplier by supply chain tier (NB: viewing suppliers at Tier 2+ is not available for all membership levels) | [optional] 
**start_date** | **datetime** | Limit the returned suppliers to those where a recorded change event occurred on or after this date  Change events include updates to supplier status, risk etc or when a company first appeared in your supply chain | [optional] 
**end_date** | **datetime** | Limit the returned suppliers to those where a recorded change event occurred before this date    Change events include updates to supplier status, risk etc or when a company first appeared in your supply chain | [optional] 
**order_by** | **str** | Order the results | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

