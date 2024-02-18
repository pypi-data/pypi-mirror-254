"""
Type annotations for connectcases service type definitions.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connectcases/type_defs/)

Usage::

    ```python
    from types_aiobotocore_connectcases.type_defs import AuditEventFieldValueUnionTypeDef

    data: AuditEventFieldValueUnionTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List, Mapping, Sequence

from .literals import (
    AuditEventTypeType,
    DomainStatusType,
    FieldNamespaceType,
    FieldTypeType,
    OrderType,
    RelatedItemTypeType,
    TemplateStatusType,
)

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 12):
    from typing import NotRequired
else:
    from typing_extensions import NotRequired
if sys.version_info >= (3, 12):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AuditEventFieldValueUnionTypeDef",
    "UserUnionTypeDef",
    "FieldIdentifierTypeDef",
    "FieldErrorTypeDef",
    "GetFieldResponseTypeDef",
    "ResponseMetadataTypeDef",
    "FieldOptionTypeDef",
    "FieldOptionErrorTypeDef",
    "CaseSummaryTypeDef",
    "CommentContentTypeDef",
    "ContactContentTypeDef",
    "ContactFilterTypeDef",
    "ContactTypeDef",
    "CreateDomainRequestRequestTypeDef",
    "CreateFieldRequestRequestTypeDef",
    "LayoutConfigurationTypeDef",
    "RequiredFieldTypeDef",
    "DeleteDomainRequestRequestTypeDef",
    "DomainSummaryTypeDef",
    "RelatedItemEventIncludedDataTypeDef",
    "FieldItemTypeDef",
    "FieldSummaryTypeDef",
    "FieldValueUnionTypeDef",
    "GetCaseAuditEventsRequestRequestTypeDef",
    "GetCaseEventConfigurationRequestRequestTypeDef",
    "GetDomainRequestRequestTypeDef",
    "GetLayoutRequestRequestTypeDef",
    "GetTemplateRequestRequestTypeDef",
    "LayoutSummaryTypeDef",
    "ListCasesForContactRequestRequestTypeDef",
    "ListDomainsRequestRequestTypeDef",
    "ListFieldOptionsRequestRequestTypeDef",
    "ListFieldsRequestRequestTypeDef",
    "ListLayoutsRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTemplatesRequestRequestTypeDef",
    "TemplateSummaryTypeDef",
    "PaginatorConfigTypeDef",
    "SortTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateFieldRequestRequestTypeDef",
    "AuditEventFieldTypeDef",
    "AuditEventPerformedByTypeDef",
    "BatchGetFieldRequestRequestTypeDef",
    "CaseEventIncludedDataTypeDef",
    "GetCaseRequestRequestTypeDef",
    "BatchGetFieldResponseTypeDef",
    "CreateCaseResponseTypeDef",
    "CreateDomainResponseTypeDef",
    "CreateFieldResponseTypeDef",
    "CreateLayoutResponseTypeDef",
    "CreateRelatedItemResponseTypeDef",
    "CreateTemplateResponseTypeDef",
    "EmptyResponseMetadataTypeDef",
    "GetDomainResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "BatchPutFieldOptionsRequestRequestTypeDef",
    "ListFieldOptionsResponseTypeDef",
    "BatchPutFieldOptionsResponseTypeDef",
    "ListCasesForContactResponseTypeDef",
    "RelatedItemContentTypeDef",
    "RelatedItemTypeFilterTypeDef",
    "RelatedItemInputContentTypeDef",
    "CreateTemplateRequestRequestTypeDef",
    "GetTemplateResponseTypeDef",
    "UpdateTemplateRequestRequestTypeDef",
    "ListDomainsResponseTypeDef",
    "FieldGroupTypeDef",
    "ListFieldsResponseTypeDef",
    "FieldValueTypeDef",
    "ListLayoutsResponseTypeDef",
    "ListTemplatesResponseTypeDef",
    "SearchCasesRequestRequestTypeDef",
    "AuditEventTypeDef",
    "EventIncludedDataTypeDef",
    "SearchRelatedItemsResponseItemTypeDef",
    "SearchRelatedItemsRequestRequestTypeDef",
    "SearchRelatedItemsRequestSearchRelatedItemsPaginateTypeDef",
    "CreateRelatedItemRequestRequestTypeDef",
    "SectionTypeDef",
    "CreateCaseRequestRequestTypeDef",
    "FieldFilterTypeDef",
    "GetCaseResponseTypeDef",
    "SearchCasesResponseItemTypeDef",
    "UpdateCaseRequestRequestTypeDef",
    "GetCaseAuditEventsResponseTypeDef",
    "EventBridgeConfigurationTypeDef",
    "SearchRelatedItemsResponseTypeDef",
    "LayoutSectionsTypeDef",
    "CaseFilterTypeDef",
    "SearchCasesResponseTypeDef",
    "GetCaseEventConfigurationResponseTypeDef",
    "PutCaseEventConfigurationRequestRequestTypeDef",
    "BasicLayoutTypeDef",
    "SearchCasesRequestSearchCasesPaginateTypeDef",
    "LayoutContentTypeDef",
    "CreateLayoutRequestRequestTypeDef",
    "GetLayoutResponseTypeDef",
    "UpdateLayoutRequestRequestTypeDef",
)

AuditEventFieldValueUnionTypeDef = TypedDict(
    "AuditEventFieldValueUnionTypeDef",
    {
        "booleanValue": NotRequired[bool],
        "doubleValue": NotRequired[float],
        "emptyValue": NotRequired[Dict[str, Any]],
        "stringValue": NotRequired[str],
        "userArnValue": NotRequired[str],
    },
)
UserUnionTypeDef = TypedDict(
    "UserUnionTypeDef",
    {
        "userArn": NotRequired[str],
    },
)
FieldIdentifierTypeDef = TypedDict(
    "FieldIdentifierTypeDef",
    {
        "id": str,
    },
)
FieldErrorTypeDef = TypedDict(
    "FieldErrorTypeDef",
    {
        "errorCode": str,
        "id": str,
        "message": NotRequired[str],
    },
)
GetFieldResponseTypeDef = TypedDict(
    "GetFieldResponseTypeDef",
    {
        "fieldArn": str,
        "fieldId": str,
        "name": str,
        "namespace": FieldNamespaceType,
        "type": FieldTypeType,
        "description": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
    },
)
ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, str],
        "RetryAttempts": int,
    },
)
FieldOptionTypeDef = TypedDict(
    "FieldOptionTypeDef",
    {
        "active": bool,
        "name": str,
        "value": str,
    },
)
FieldOptionErrorTypeDef = TypedDict(
    "FieldOptionErrorTypeDef",
    {
        "errorCode": str,
        "message": str,
        "value": str,
    },
)
CaseSummaryTypeDef = TypedDict(
    "CaseSummaryTypeDef",
    {
        "caseId": str,
        "templateId": str,
    },
)
CommentContentTypeDef = TypedDict(
    "CommentContentTypeDef",
    {
        "body": str,
        "contentType": Literal["Text/Plain"],
    },
)
ContactContentTypeDef = TypedDict(
    "ContactContentTypeDef",
    {
        "channel": str,
        "connectedToSystemTime": datetime,
        "contactArn": str,
    },
)
ContactFilterTypeDef = TypedDict(
    "ContactFilterTypeDef",
    {
        "channel": NotRequired[Sequence[str]],
        "contactArn": NotRequired[str],
    },
)
ContactTypeDef = TypedDict(
    "ContactTypeDef",
    {
        "contactArn": str,
    },
)
CreateDomainRequestRequestTypeDef = TypedDict(
    "CreateDomainRequestRequestTypeDef",
    {
        "name": str,
    },
)
CreateFieldRequestRequestTypeDef = TypedDict(
    "CreateFieldRequestRequestTypeDef",
    {
        "domainId": str,
        "name": str,
        "type": FieldTypeType,
        "description": NotRequired[str],
    },
)
LayoutConfigurationTypeDef = TypedDict(
    "LayoutConfigurationTypeDef",
    {
        "defaultLayout": NotRequired[str],
    },
)
RequiredFieldTypeDef = TypedDict(
    "RequiredFieldTypeDef",
    {
        "fieldId": str,
    },
)
DeleteDomainRequestRequestTypeDef = TypedDict(
    "DeleteDomainRequestRequestTypeDef",
    {
        "domainId": str,
    },
)
DomainSummaryTypeDef = TypedDict(
    "DomainSummaryTypeDef",
    {
        "domainArn": str,
        "domainId": str,
        "name": str,
    },
)
RelatedItemEventIncludedDataTypeDef = TypedDict(
    "RelatedItemEventIncludedDataTypeDef",
    {
        "includeContent": bool,
    },
)
FieldItemTypeDef = TypedDict(
    "FieldItemTypeDef",
    {
        "id": str,
    },
)
FieldSummaryTypeDef = TypedDict(
    "FieldSummaryTypeDef",
    {
        "fieldArn": str,
        "fieldId": str,
        "name": str,
        "namespace": FieldNamespaceType,
        "type": FieldTypeType,
    },
)
FieldValueUnionTypeDef = TypedDict(
    "FieldValueUnionTypeDef",
    {
        "booleanValue": NotRequired[bool],
        "doubleValue": NotRequired[float],
        "emptyValue": NotRequired[Mapping[str, Any]],
        "stringValue": NotRequired[str],
        "userArnValue": NotRequired[str],
    },
)
GetCaseAuditEventsRequestRequestTypeDef = TypedDict(
    "GetCaseAuditEventsRequestRequestTypeDef",
    {
        "caseId": str,
        "domainId": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
GetCaseEventConfigurationRequestRequestTypeDef = TypedDict(
    "GetCaseEventConfigurationRequestRequestTypeDef",
    {
        "domainId": str,
    },
)
GetDomainRequestRequestTypeDef = TypedDict(
    "GetDomainRequestRequestTypeDef",
    {
        "domainId": str,
    },
)
GetLayoutRequestRequestTypeDef = TypedDict(
    "GetLayoutRequestRequestTypeDef",
    {
        "domainId": str,
        "layoutId": str,
    },
)
GetTemplateRequestRequestTypeDef = TypedDict(
    "GetTemplateRequestRequestTypeDef",
    {
        "domainId": str,
        "templateId": str,
    },
)
LayoutSummaryTypeDef = TypedDict(
    "LayoutSummaryTypeDef",
    {
        "layoutArn": str,
        "layoutId": str,
        "name": str,
    },
)
ListCasesForContactRequestRequestTypeDef = TypedDict(
    "ListCasesForContactRequestRequestTypeDef",
    {
        "contactArn": str,
        "domainId": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListDomainsRequestRequestTypeDef = TypedDict(
    "ListDomainsRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListFieldOptionsRequestRequestTypeDef = TypedDict(
    "ListFieldOptionsRequestRequestTypeDef",
    {
        "domainId": str,
        "fieldId": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "values": NotRequired[Sequence[str]],
    },
)
ListFieldsRequestRequestTypeDef = TypedDict(
    "ListFieldsRequestRequestTypeDef",
    {
        "domainId": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListLayoutsRequestRequestTypeDef = TypedDict(
    "ListLayoutsRequestRequestTypeDef",
    {
        "domainId": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "arn": str,
    },
)
ListTemplatesRequestRequestTypeDef = TypedDict(
    "ListTemplatesRequestRequestTypeDef",
    {
        "domainId": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "status": NotRequired[Sequence[TemplateStatusType]],
    },
)
TemplateSummaryTypeDef = TypedDict(
    "TemplateSummaryTypeDef",
    {
        "name": str,
        "status": TemplateStatusType,
        "templateArn": str,
        "templateId": str,
    },
)
PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": NotRequired[int],
        "PageSize": NotRequired[int],
        "StartingToken": NotRequired[str],
    },
)
SortTypeDef = TypedDict(
    "SortTypeDef",
    {
        "fieldId": str,
        "sortOrder": OrderType,
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "arn": str,
        "tags": Mapping[str, str],
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "arn": str,
        "tagKeys": Sequence[str],
    },
)
UpdateFieldRequestRequestTypeDef = TypedDict(
    "UpdateFieldRequestRequestTypeDef",
    {
        "domainId": str,
        "fieldId": str,
        "description": NotRequired[str],
        "name": NotRequired[str],
    },
)
AuditEventFieldTypeDef = TypedDict(
    "AuditEventFieldTypeDef",
    {
        "eventFieldId": str,
        "newValue": AuditEventFieldValueUnionTypeDef,
        "oldValue": NotRequired[AuditEventFieldValueUnionTypeDef],
    },
)
AuditEventPerformedByTypeDef = TypedDict(
    "AuditEventPerformedByTypeDef",
    {
        "iamPrincipalArn": str,
        "user": NotRequired[UserUnionTypeDef],
    },
)
BatchGetFieldRequestRequestTypeDef = TypedDict(
    "BatchGetFieldRequestRequestTypeDef",
    {
        "domainId": str,
        "fields": Sequence[FieldIdentifierTypeDef],
    },
)
CaseEventIncludedDataTypeDef = TypedDict(
    "CaseEventIncludedDataTypeDef",
    {
        "fields": List[FieldIdentifierTypeDef],
    },
)
GetCaseRequestRequestTypeDef = TypedDict(
    "GetCaseRequestRequestTypeDef",
    {
        "caseId": str,
        "domainId": str,
        "fields": Sequence[FieldIdentifierTypeDef],
        "nextToken": NotRequired[str],
    },
)
BatchGetFieldResponseTypeDef = TypedDict(
    "BatchGetFieldResponseTypeDef",
    {
        "errors": List[FieldErrorTypeDef],
        "fields": List[GetFieldResponseTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateCaseResponseTypeDef = TypedDict(
    "CreateCaseResponseTypeDef",
    {
        "caseArn": str,
        "caseId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDomainResponseTypeDef = TypedDict(
    "CreateDomainResponseTypeDef",
    {
        "domainArn": str,
        "domainId": str,
        "domainStatus": DomainStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateFieldResponseTypeDef = TypedDict(
    "CreateFieldResponseTypeDef",
    {
        "fieldArn": str,
        "fieldId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateLayoutResponseTypeDef = TypedDict(
    "CreateLayoutResponseTypeDef",
    {
        "layoutArn": str,
        "layoutId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateRelatedItemResponseTypeDef = TypedDict(
    "CreateRelatedItemResponseTypeDef",
    {
        "relatedItemArn": str,
        "relatedItemId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateTemplateResponseTypeDef = TypedDict(
    "CreateTemplateResponseTypeDef",
    {
        "templateArn": str,
        "templateId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetDomainResponseTypeDef = TypedDict(
    "GetDomainResponseTypeDef",
    {
        "createdTime": datetime,
        "domainArn": str,
        "domainId": str,
        "domainStatus": DomainStatusType,
        "name": str,
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchPutFieldOptionsRequestRequestTypeDef = TypedDict(
    "BatchPutFieldOptionsRequestRequestTypeDef",
    {
        "domainId": str,
        "fieldId": str,
        "options": Sequence[FieldOptionTypeDef],
    },
)
ListFieldOptionsResponseTypeDef = TypedDict(
    "ListFieldOptionsResponseTypeDef",
    {
        "nextToken": str,
        "options": List[FieldOptionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchPutFieldOptionsResponseTypeDef = TypedDict(
    "BatchPutFieldOptionsResponseTypeDef",
    {
        "errors": List[FieldOptionErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListCasesForContactResponseTypeDef = TypedDict(
    "ListCasesForContactResponseTypeDef",
    {
        "cases": List[CaseSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RelatedItemContentTypeDef = TypedDict(
    "RelatedItemContentTypeDef",
    {
        "comment": NotRequired[CommentContentTypeDef],
        "contact": NotRequired[ContactContentTypeDef],
    },
)
RelatedItemTypeFilterTypeDef = TypedDict(
    "RelatedItemTypeFilterTypeDef",
    {
        "comment": NotRequired[Mapping[str, Any]],
        "contact": NotRequired[ContactFilterTypeDef],
    },
)
RelatedItemInputContentTypeDef = TypedDict(
    "RelatedItemInputContentTypeDef",
    {
        "comment": NotRequired[CommentContentTypeDef],
        "contact": NotRequired[ContactTypeDef],
    },
)
CreateTemplateRequestRequestTypeDef = TypedDict(
    "CreateTemplateRequestRequestTypeDef",
    {
        "domainId": str,
        "name": str,
        "description": NotRequired[str],
        "layoutConfiguration": NotRequired[LayoutConfigurationTypeDef],
        "requiredFields": NotRequired[Sequence[RequiredFieldTypeDef]],
        "status": NotRequired[TemplateStatusType],
    },
)
GetTemplateResponseTypeDef = TypedDict(
    "GetTemplateResponseTypeDef",
    {
        "description": str,
        "layoutConfiguration": LayoutConfigurationTypeDef,
        "name": str,
        "requiredFields": List[RequiredFieldTypeDef],
        "status": TemplateStatusType,
        "tags": Dict[str, str],
        "templateArn": str,
        "templateId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateTemplateRequestRequestTypeDef = TypedDict(
    "UpdateTemplateRequestRequestTypeDef",
    {
        "domainId": str,
        "templateId": str,
        "description": NotRequired[str],
        "layoutConfiguration": NotRequired[LayoutConfigurationTypeDef],
        "name": NotRequired[str],
        "requiredFields": NotRequired[Sequence[RequiredFieldTypeDef]],
        "status": NotRequired[TemplateStatusType],
    },
)
ListDomainsResponseTypeDef = TypedDict(
    "ListDomainsResponseTypeDef",
    {
        "domains": List[DomainSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
FieldGroupTypeDef = TypedDict(
    "FieldGroupTypeDef",
    {
        "fields": Sequence[FieldItemTypeDef],
        "name": NotRequired[str],
    },
)
ListFieldsResponseTypeDef = TypedDict(
    "ListFieldsResponseTypeDef",
    {
        "fields": List[FieldSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
FieldValueTypeDef = TypedDict(
    "FieldValueTypeDef",
    {
        "id": str,
        "value": FieldValueUnionTypeDef,
    },
)
ListLayoutsResponseTypeDef = TypedDict(
    "ListLayoutsResponseTypeDef",
    {
        "layouts": List[LayoutSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTemplatesResponseTypeDef = TypedDict(
    "ListTemplatesResponseTypeDef",
    {
        "nextToken": str,
        "templates": List[TemplateSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SearchCasesRequestRequestTypeDef = TypedDict(
    "SearchCasesRequestRequestTypeDef",
    {
        "domainId": str,
        "fields": NotRequired[Sequence[FieldIdentifierTypeDef]],
        "filter": NotRequired["CaseFilterTypeDef"],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "searchTerm": NotRequired[str],
        "sorts": NotRequired[Sequence[SortTypeDef]],
    },
)
AuditEventTypeDef = TypedDict(
    "AuditEventTypeDef",
    {
        "eventId": str,
        "fields": List[AuditEventFieldTypeDef],
        "performedTime": datetime,
        "type": AuditEventTypeType,
        "performedBy": NotRequired[AuditEventPerformedByTypeDef],
        "relatedItemType": NotRequired[RelatedItemTypeType],
    },
)
EventIncludedDataTypeDef = TypedDict(
    "EventIncludedDataTypeDef",
    {
        "caseData": NotRequired[CaseEventIncludedDataTypeDef],
        "relatedItemData": NotRequired[RelatedItemEventIncludedDataTypeDef],
    },
)
SearchRelatedItemsResponseItemTypeDef = TypedDict(
    "SearchRelatedItemsResponseItemTypeDef",
    {
        "associationTime": datetime,
        "content": RelatedItemContentTypeDef,
        "relatedItemId": str,
        "type": RelatedItemTypeType,
        "performedBy": NotRequired[UserUnionTypeDef],
        "tags": NotRequired[Dict[str, str]],
    },
)
SearchRelatedItemsRequestRequestTypeDef = TypedDict(
    "SearchRelatedItemsRequestRequestTypeDef",
    {
        "caseId": str,
        "domainId": str,
        "filters": NotRequired[Sequence[RelatedItemTypeFilterTypeDef]],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
SearchRelatedItemsRequestSearchRelatedItemsPaginateTypeDef = TypedDict(
    "SearchRelatedItemsRequestSearchRelatedItemsPaginateTypeDef",
    {
        "caseId": str,
        "domainId": str,
        "filters": NotRequired[Sequence[RelatedItemTypeFilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
CreateRelatedItemRequestRequestTypeDef = TypedDict(
    "CreateRelatedItemRequestRequestTypeDef",
    {
        "caseId": str,
        "content": RelatedItemInputContentTypeDef,
        "domainId": str,
        "type": RelatedItemTypeType,
        "performedBy": NotRequired[UserUnionTypeDef],
    },
)
SectionTypeDef = TypedDict(
    "SectionTypeDef",
    {
        "fieldGroup": NotRequired[FieldGroupTypeDef],
    },
)
CreateCaseRequestRequestTypeDef = TypedDict(
    "CreateCaseRequestRequestTypeDef",
    {
        "domainId": str,
        "fields": Sequence[FieldValueTypeDef],
        "templateId": str,
        "clientToken": NotRequired[str],
        "performedBy": NotRequired[UserUnionTypeDef],
    },
)
FieldFilterTypeDef = TypedDict(
    "FieldFilterTypeDef",
    {
        "contains": NotRequired[FieldValueTypeDef],
        "equalTo": NotRequired[FieldValueTypeDef],
        "greaterThan": NotRequired[FieldValueTypeDef],
        "greaterThanOrEqualTo": NotRequired[FieldValueTypeDef],
        "lessThan": NotRequired[FieldValueTypeDef],
        "lessThanOrEqualTo": NotRequired[FieldValueTypeDef],
    },
)
GetCaseResponseTypeDef = TypedDict(
    "GetCaseResponseTypeDef",
    {
        "fields": List[FieldValueTypeDef],
        "nextToken": str,
        "tags": Dict[str, str],
        "templateId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SearchCasesResponseItemTypeDef = TypedDict(
    "SearchCasesResponseItemTypeDef",
    {
        "caseId": str,
        "fields": List[FieldValueTypeDef],
        "templateId": str,
        "tags": NotRequired[Dict[str, str]],
    },
)
UpdateCaseRequestRequestTypeDef = TypedDict(
    "UpdateCaseRequestRequestTypeDef",
    {
        "caseId": str,
        "domainId": str,
        "fields": Sequence[FieldValueTypeDef],
        "performedBy": NotRequired[UserUnionTypeDef],
    },
)
GetCaseAuditEventsResponseTypeDef = TypedDict(
    "GetCaseAuditEventsResponseTypeDef",
    {
        "auditEvents": List[AuditEventTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EventBridgeConfigurationTypeDef = TypedDict(
    "EventBridgeConfigurationTypeDef",
    {
        "enabled": bool,
        "includedData": NotRequired[EventIncludedDataTypeDef],
    },
)
SearchRelatedItemsResponseTypeDef = TypedDict(
    "SearchRelatedItemsResponseTypeDef",
    {
        "nextToken": str,
        "relatedItems": List[SearchRelatedItemsResponseItemTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
LayoutSectionsTypeDef = TypedDict(
    "LayoutSectionsTypeDef",
    {
        "sections": NotRequired[Sequence[SectionTypeDef]],
    },
)
CaseFilterTypeDef = TypedDict(
    "CaseFilterTypeDef",
    {
        "andAll": NotRequired[Sequence[Dict[str, Any]]],
        "field": NotRequired[FieldFilterTypeDef],
        "not": NotRequired[Dict[str, Any]],
        "orAll": NotRequired[Sequence[Dict[str, Any]]],
    },
)
SearchCasesResponseTypeDef = TypedDict(
    "SearchCasesResponseTypeDef",
    {
        "cases": List[SearchCasesResponseItemTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetCaseEventConfigurationResponseTypeDef = TypedDict(
    "GetCaseEventConfigurationResponseTypeDef",
    {
        "eventBridge": EventBridgeConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutCaseEventConfigurationRequestRequestTypeDef = TypedDict(
    "PutCaseEventConfigurationRequestRequestTypeDef",
    {
        "domainId": str,
        "eventBridge": EventBridgeConfigurationTypeDef,
    },
)
BasicLayoutTypeDef = TypedDict(
    "BasicLayoutTypeDef",
    {
        "moreInfo": NotRequired[LayoutSectionsTypeDef],
        "topPanel": NotRequired[LayoutSectionsTypeDef],
    },
)
SearchCasesRequestSearchCasesPaginateTypeDef = TypedDict(
    "SearchCasesRequestSearchCasesPaginateTypeDef",
    {
        "domainId": str,
        "fields": NotRequired[Sequence[FieldIdentifierTypeDef]],
        "filter": NotRequired[CaseFilterTypeDef],
        "searchTerm": NotRequired[str],
        "sorts": NotRequired[Sequence[SortTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
LayoutContentTypeDef = TypedDict(
    "LayoutContentTypeDef",
    {
        "basic": NotRequired[BasicLayoutTypeDef],
    },
)
CreateLayoutRequestRequestTypeDef = TypedDict(
    "CreateLayoutRequestRequestTypeDef",
    {
        "content": LayoutContentTypeDef,
        "domainId": str,
        "name": str,
    },
)
GetLayoutResponseTypeDef = TypedDict(
    "GetLayoutResponseTypeDef",
    {
        "content": LayoutContentTypeDef,
        "layoutArn": str,
        "layoutId": str,
        "name": str,
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateLayoutRequestRequestTypeDef = TypedDict(
    "UpdateLayoutRequestRequestTypeDef",
    {
        "domainId": str,
        "layoutId": str,
        "content": NotRequired[LayoutContentTypeDef],
        "name": NotRequired[str],
    },
)
