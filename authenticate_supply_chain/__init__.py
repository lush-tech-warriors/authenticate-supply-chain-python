# coding: utf-8

# flake8: noqa

"""
    Authenticate Platform Supply Chain API

    Through this API you can Manage products and suppliers. Access to this API is restricted to authenticated users. Before accessing this API, first authenticate via the \"Account\" API. (https://uat-account.authenticateis.com/)  # noqa: E501

    OpenAPI spec version: 1.0
    Contact: platform-support@authenticateis.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import apis into sdk package
from authenticate_supply_chain.api.attachments_api import AttachmentsApi
from authenticate_supply_chain.api.blob_api import BlobApi
from authenticate_supply_chain.api.categories_api import CategoriesApi
from authenticate_supply_chain.api.certificates_api import CertificatesApi
from authenticate_supply_chain.api.companies_api import CompaniesApi
from authenticate_supply_chain.api.company_licence_requests_api import CompanyLicenceRequestsApi
from authenticate_supply_chain.api.company_licence_types_api import CompanyLicenceTypesApi
from authenticate_supply_chain.api.company_licences_api import CompanyLicencesApi
from authenticate_supply_chain.api.company_relationships_api import CompanyRelationshipsApi
from authenticate_supply_chain.api.contacts_api import ContactsApi
from authenticate_supply_chain.api.countries_api import CountriesApi
from authenticate_supply_chain.api.country_esg_score_details_api import CountryEsgScoreDetailsApi
from authenticate_supply_chain.api.country_esg_scores_api import CountryEsgScoresApi
from authenticate_supply_chain.api.country_esg_summaries_api import CountryEsgSummariesApi
from authenticate_supply_chain.api.customer_links_api import CustomerLinksApi
from authenticate_supply_chain.api.declared_supply_chain_api import DeclaredSupplyChainApi
from authenticate_supply_chain.api.declared_supply_chain_status_api import DeclaredSupplyChainStatusApi
from authenticate_supply_chain.api.documents_api import DocumentsApi
from authenticate_supply_chain.api.notes_api import NotesApi
from authenticate_supply_chain.api.ons_company_types_api import OnsCompanyTypesApi
from authenticate_supply_chain.api.product_line_approval_api import ProductLineApprovalApi
from authenticate_supply_chain.api.product_line_approval_request_api import ProductLineApprovalRequestApi
from authenticate_supply_chain.api.product_line_document_association_api import ProductLineDocumentAssociationApi
from authenticate_supply_chain.api.product_line_owners_api import ProductLineOwnersApi
from authenticate_supply_chain.api.product_line_status_api import ProductLineStatusApi
from authenticate_supply_chain.api.product_line_variations_api import ProductLineVariationsApi
from authenticate_supply_chain.api.product_line_version_api import ProductLineVersionApi
from authenticate_supply_chain.api.product_tags_api import ProductTagsApi
from authenticate_supply_chain.api.products_api import ProductsApi
from authenticate_supply_chain.api.raw_material_additional_informations_api import RawMaterialAdditionalInformationsApi
from authenticate_supply_chain.api.raw_material_approval_api import RawMaterialApprovalApi
from authenticate_supply_chain.api.raw_material_functions_api import RawMaterialFunctionsApi
from authenticate_supply_chain.api.raw_material_logistics_api import RawMaterialLogisticsApi
from authenticate_supply_chain.api.raw_material_records_api import RawMaterialRecordsApi
from authenticate_supply_chain.api.raw_material_relationships_api import RawMaterialRelationshipsApi
from authenticate_supply_chain.api.raw_materials_api import RawMaterialsApi
from authenticate_supply_chain.api.search_lookup_api import SearchLookupApi
from authenticate_supply_chain.api.site_licence_requests_api import SiteLicenceRequestsApi
from authenticate_supply_chain.api.site_licence_types_api import SiteLicenceTypesApi
from authenticate_supply_chain.api.site_licences_api import SiteLicencesApi
from authenticate_supply_chain.api.site_relationship_api import SiteRelationshipApi
from authenticate_supply_chain.api.site_relationship_categories_api import SiteRelationshipCategoriesApi
from authenticate_supply_chain.api.site_relationship_functions_api import SiteRelationshipFunctionsApi
from authenticate_supply_chain.api.sites_api import SitesApi
from authenticate_supply_chain.api.supplier_codes_api import SupplierCodesApi
from authenticate_supply_chain.api.supplier_links_api import SupplierLinksApi
from authenticate_supply_chain.api.supplier_product_country_declarations_api import SupplierProductCountryDeclarationsApi
from authenticate_supply_chain.api.supplier_products_api import SupplierProductsApi
from authenticate_supply_chain.api.suppliers_api import SuppliersApi
from authenticate_supply_chain.api.supply_chain_api import SupplyChainApi
from authenticate_supply_chain.api.supply_chain_snapshot_api import SupplyChainSnapshotApi
from authenticate_supply_chain.api.users_api import UsersApi
# import ApiClient
from authenticate_supply_chain.api_client import ApiClient
from authenticate_supply_chain.configuration import Configuration
# import models into sdk package
from authenticate_supply_chain.models.address_dto import AddressDto
from authenticate_supply_chain.models.category_dto import CategoryDto
from authenticate_supply_chain.models.category_for_creation_dto import CategoryForCreationDto
from authenticate_supply_chain.models.category_for_update_dto import CategoryForUpdateDto
from authenticate_supply_chain.models.certificate_dto import CertificateDto
from authenticate_supply_chain.models.company_dto import CompanyDto
from authenticate_supply_chain.models.company_for_creation_dto import CompanyForCreationDto
from authenticate_supply_chain.models.company_function_dto import CompanyFunctionDto
from authenticate_supply_chain.models.company_relationship_dto import CompanyRelationshipDto
from authenticate_supply_chain.models.company_resource_parameters import CompanyResourceParameters
from authenticate_supply_chain.models.company_site_relationship_currency_enum import CompanySiteRelationshipCurrencyEnum
from authenticate_supply_chain.models.contact_dto import ContactDto
from authenticate_supply_chain.models.contact_for_creation_dto import ContactForCreationDto
from authenticate_supply_chain.models.country_dto import CountryDto
from authenticate_supply_chain.models.country_esg_score_detail_dto import CountryEsgScoreDetailDto
from authenticate_supply_chain.models.country_esg_score_dto import CountryEsgScoreDto
from authenticate_supply_chain.models.country_esg_score_threshold_dto import CountryEsgScoreThresholdDto
from authenticate_supply_chain.models.country_esg_summary_dto import CountryEsgSummaryDto
from authenticate_supply_chain.models.customer_product_link_dto import CustomerProductLinkDto
from authenticate_supply_chain.models.declared_supply_chain_dto import DeclaredSupplyChainDto
from authenticate_supply_chain.models.declared_supply_chain_for_creation_dto import DeclaredSupplyChainForCreationDto
from authenticate_supply_chain.models.declared_supply_chain_for_update_dto import DeclaredSupplyChainForUpdateDto
from authenticate_supply_chain.models.declared_supply_chain_status_dto import DeclaredSupplyChainStatusDto
from authenticate_supply_chain.models.declared_supply_chain_status_enum import DeclaredSupplyChainStatusEnum
from authenticate_supply_chain.models.document_dto import DocumentDto
from authenticate_supply_chain.models.document_for_creation_dto import DocumentForCreationDto
from authenticate_supply_chain.models.document_for_update_dto import DocumentForUpdateDto
from authenticate_supply_chain.models.entity_supply_chain_dto import EntitySupplyChainDto
from authenticate_supply_chain.models.entity_supply_chain_site_dto import EntitySupplyChainSiteDto
from authenticate_supply_chain.models.entity_supply_chain_site_location_dto import EntitySupplyChainSiteLocationDto
from authenticate_supply_chain.models.esg_outcome_enum import EsgOutcomeEnum
from authenticate_supply_chain.models.esg_status_enum import EsgStatusEnum
from authenticate_supply_chain.models.job_title_enum import JobTitleEnum
from authenticate_supply_chain.models.licence_dto import LicenceDto
from authenticate_supply_chain.models.licence_request_dto import LicenceRequestDto
from authenticate_supply_chain.models.licence_request_dto_for_creation import LicenceRequestDtoForCreation
from authenticate_supply_chain.models.licence_request_enum import LicenceRequestEnum
from authenticate_supply_chain.models.licence_request_reason_dto import LicenceRequestReasonDto
from authenticate_supply_chain.models.licence_request_reason_enum import LicenceRequestReasonEnum
from authenticate_supply_chain.models.licence_type_dto import LicenceTypeDto
from authenticate_supply_chain.models.not_mapping_product_line_reason_enum import NotMappingProductLineReasonEnum
from authenticate_supply_chain.models.note_dto import NoteDto
from authenticate_supply_chain.models.ons_company_type_dto import OnsCompanyTypeDto
from authenticate_supply_chain.models.ons_sector_dto import OnsSectorDto
from authenticate_supply_chain.models.ons_site_operation_dto import OnsSiteOperationDto
from authenticate_supply_chain.models.operation import Operation
from authenticate_supply_chain.models.operation_type import OperationType
from authenticate_supply_chain.models.parent_type_enum import ParentTypeEnum
from authenticate_supply_chain.models.problem_details import ProblemDetails
from authenticate_supply_chain.models.product_dto import ProductDto
from authenticate_supply_chain.models.product_for_creation_dto import ProductForCreationDto
from authenticate_supply_chain.models.product_for_update_dto import ProductForUpdateDto
from authenticate_supply_chain.models.product_line_approval_dto import ProductLineApprovalDto
from authenticate_supply_chain.models.product_line_approval_request_dto import ProductLineApprovalRequestDto
from authenticate_supply_chain.models.product_line_approval_request_response_enum import ProductLineApprovalRequestResponseEnum
from authenticate_supply_chain.models.product_line_country_declaration_dto import ProductLineCountryDeclarationDto
from authenticate_supply_chain.models.product_line_country_declaration_for_creation_dto import ProductLineCountryDeclarationForCreationDto
from authenticate_supply_chain.models.product_line_document_association_dto import ProductLineDocumentAssociationDto
from authenticate_supply_chain.models.product_line_owner_dto import ProductLineOwnerDto
from authenticate_supply_chain.models.product_line_status_dto import ProductLineStatusDto
from authenticate_supply_chain.models.product_line_status_enum import ProductLineStatusEnum
from authenticate_supply_chain.models.product_line_status_for_creation_dto import ProductLineStatusForCreationDto
from authenticate_supply_chain.models.product_line_variation_dto import ProductLineVariationDto
from authenticate_supply_chain.models.product_line_variation_for_manipulation_dto import ProductLineVariationForManipulationDto
from authenticate_supply_chain.models.product_link_accept_dto import ProductLinkAcceptDto
from authenticate_supply_chain.models.product_link_removal_dto import ProductLinkRemovalDto
from authenticate_supply_chain.models.product_site_dto import ProductSiteDto
from authenticate_supply_chain.models.product_site_for_manipulation_dto import ProductSiteForManipulationDto
from authenticate_supply_chain.models.product_tag_dto import ProductTagDto
from authenticate_supply_chain.models.raw_material_additional_information_dto import RawMaterialAdditionalInformationDto
from authenticate_supply_chain.models.raw_material_approval_dto import RawMaterialApprovalDto
from authenticate_supply_chain.models.raw_material_dto import RawMaterialDto
from authenticate_supply_chain.models.raw_material_function_dto import RawMaterialFunctionDto
from authenticate_supply_chain.models.raw_material_logistic_dto import RawMaterialLogisticDto
from authenticate_supply_chain.models.raw_material_logistic_for_creation_dto import RawMaterialLogisticForCreationDto
from authenticate_supply_chain.models.raw_material_logistics_type_enum import RawMaterialLogisticsTypeEnum
from authenticate_supply_chain.models.raw_material_record_document_dto import RawMaterialRecordDocumentDto
from authenticate_supply_chain.models.raw_material_record_dto import RawMaterialRecordDto
from authenticate_supply_chain.models.raw_material_record_for_creation_dto import RawMaterialRecordForCreationDto
from authenticate_supply_chain.models.raw_material_record_for_update_dto import RawMaterialRecordForUpdateDto
from authenticate_supply_chain.models.raw_material_record_status_enum import RawMaterialRecordStatusEnum
from authenticate_supply_chain.models.raw_material_record_sugar_data_dto import RawMaterialRecordSugarDataDto
from authenticate_supply_chain.models.raw_material_relationship_dto import RawMaterialRelationshipDto
from authenticate_supply_chain.models.raw_material_resource_parameters import RawMaterialResourceParameters
from authenticate_supply_chain.models.region_dto import RegionDto
from authenticate_supply_chain.models.relationship_risk_enum import RelationshipRiskEnum
from authenticate_supply_chain.models.relationship_status_enum import RelationshipStatusEnum
from authenticate_supply_chain.models.search_lookup_dto import SearchLookupDto
from authenticate_supply_chain.models.site_certification_status_dto import SiteCertificationStatusDto
from authenticate_supply_chain.models.site_dto import SiteDto
from authenticate_supply_chain.models.site_relationship_category_dto import SiteRelationshipCategoryDto
from authenticate_supply_chain.models.site_relationship_dto import SiteRelationshipDto
from authenticate_supply_chain.models.site_relationship_for_manipulation_dto import SiteRelationshipForManipulationDto
from authenticate_supply_chain.models.site_relationship_function_dto import SiteRelationshipFunctionDto
from authenticate_supply_chain.models.site_relationship_values_dto import SiteRelationshipValuesDto
from authenticate_supply_chain.models.site_resource_parameters_extended import SiteResourceParametersExtended
from authenticate_supply_chain.models.site_search_type_enum import SiteSearchTypeEnum
from authenticate_supply_chain.models.site_supply_chain_resource_parameters import SiteSupplyChainResourceParameters
from authenticate_supply_chain.models.storage_account_enum import StorageAccountEnum
from authenticate_supply_chain.models.stream import Stream
from authenticate_supply_chain.models.supplier_code_dto import SupplierCodeDto
from authenticate_supply_chain.models.supplier_code_for_creation_dto import SupplierCodeForCreationDto
from authenticate_supply_chain.models.supplier_dto import SupplierDto
from authenticate_supply_chain.models.supplier_link_site_dto import SupplierLinkSiteDto
from authenticate_supply_chain.models.supplier_product_dto import SupplierProductDto
from authenticate_supply_chain.models.supplier_product_link_dto import SupplierProductLinkDto
from authenticate_supply_chain.models.supplier_product_link_for_creation_dto import SupplierProductLinkForCreationDto
from authenticate_supply_chain.models.supplier_product_link_for_update_dto import SupplierProductLinkForUpdateDto
from authenticate_supply_chain.models.supplier_resource_parameters import SupplierResourceParameters
from authenticate_supply_chain.models.tag_dto import TagDto
from authenticate_supply_chain.models.user_dto import UserDto
from authenticate_supply_chain.models.v1_blob_body import V1BlobBody
from authenticate_supply_chain.models.v1_blob_body1 import V1BlobBody1