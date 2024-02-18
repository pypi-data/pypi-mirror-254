"""
Type annotations for connectcases service client.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connectcases/client/)

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_connectcases.client import ConnectCasesClient

    session = get_session()
    async with session.create_client("connectcases") as client:
        client: ConnectCasesClient
    ```
"""

import sys
from typing import Any, Dict, Mapping, Sequence, Type, overload

from aiobotocore.client import AioBaseClient
from botocore.client import ClientMeta

from .literals import FieldTypeType, RelatedItemTypeType, TemplateStatusType
from .paginator import SearchCasesPaginator, SearchRelatedItemsPaginator
from .type_defs import (
    BatchGetFieldResponseTypeDef,
    BatchPutFieldOptionsResponseTypeDef,
    CaseFilterTypeDef,
    CreateCaseResponseTypeDef,
    CreateDomainResponseTypeDef,
    CreateFieldResponseTypeDef,
    CreateLayoutResponseTypeDef,
    CreateRelatedItemResponseTypeDef,
    CreateTemplateResponseTypeDef,
    EmptyResponseMetadataTypeDef,
    EventBridgeConfigurationTypeDef,
    FieldIdentifierTypeDef,
    FieldOptionTypeDef,
    FieldValueTypeDef,
    GetCaseAuditEventsResponseTypeDef,
    GetCaseEventConfigurationResponseTypeDef,
    GetCaseResponseTypeDef,
    GetDomainResponseTypeDef,
    GetLayoutResponseTypeDef,
    GetTemplateResponseTypeDef,
    LayoutConfigurationTypeDef,
    LayoutContentTypeDef,
    ListCasesForContactResponseTypeDef,
    ListDomainsResponseTypeDef,
    ListFieldOptionsResponseTypeDef,
    ListFieldsResponseTypeDef,
    ListLayoutsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTemplatesResponseTypeDef,
    RelatedItemInputContentTypeDef,
    RelatedItemTypeFilterTypeDef,
    RequiredFieldTypeDef,
    SearchCasesResponseTypeDef,
    SearchRelatedItemsResponseTypeDef,
    SortTypeDef,
    UserUnionTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("ConnectCasesClient",)

class BotocoreClientError(Exception):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class ConnectCasesClient(AioBaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases.html#ConnectCases.Client)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connectcases/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        ConnectCasesClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases.html#ConnectCases.Client.exceptions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connectcases/client/#exceptions)
        """

    async def batch_get_field(
        self, *, domainId: str, fields: Sequence[FieldIdentifierTypeDef]
    ) -> BatchGetFieldResponseTypeDef:
        """
        Returns the description for the list of fields in the request parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases.html#ConnectCases.Client.batch_get_field)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connectcases/client/#batch_get_field)
        """

    async def batch_put_field_options(
        self, *, domainId: str, fieldId: str, options: Sequence[FieldOptionTypeDef]
    ) -> BatchPutFieldOptionsResponseTypeDef:
        """
        Creates and updates a set of field options for a single select field in a Cases
        domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases.html#ConnectCases.Client.batch_put_field_options)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connectcases/client/#batch_put_field_options)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases.html#ConnectCases.Client.can_paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connectcases/client/#can_paginate)
        """

    async def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases.html#ConnectCases.Client.close)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connectcases/client/#close)
        """

    async def create_case(
        self,
        *,
        domainId: str,
        fields: Sequence[FieldValueTypeDef],
        templateId: str,
        clientToken: str = ...,
        performedBy: UserUnionTypeDef = ...,
    ) -> CreateCaseResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases.html#ConnectCases.Client.create_case)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connectcases/client/#create_case)
        """

    async def create_domain(self, *, name: str) -> CreateDomainResponseTypeDef:
        """
        Creates a domain, which is a container for all case data, such as cases,
        fields, templates and
        layouts.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases.html#ConnectCases.Client.create_domain)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connectcases/client/#create_domain)
        """

    async def create_field(
        self, *, domainId: str, name: str, type: FieldTypeType, description: str = ...
    ) -> CreateFieldResponseTypeDef:
        """
        Creates a field in the Cases domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases.html#ConnectCases.Client.create_field)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connectcases/client/#create_field)
        """

    async def create_layout(
        self, *, content: LayoutContentTypeDef, domainId: str, name: str
    ) -> CreateLayoutResponseTypeDef:
        """
        Creates a layout in the Cases domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases.html#ConnectCases.Client.create_layout)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connectcases/client/#create_layout)
        """

    async def create_related_item(
        self,
        *,
        caseId: str,
        content: RelatedItemInputContentTypeDef,
        domainId: str,
        type: RelatedItemTypeType,
        performedBy: UserUnionTypeDef = ...,
    ) -> CreateRelatedItemResponseTypeDef:
        """
        Creates a related item (comments, tasks, and contacts) and associates it with a
        case.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases.html#ConnectCases.Client.create_related_item)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connectcases/client/#create_related_item)
        """

    async def create_template(
        self,
        *,
        domainId: str,
        name: str,
        description: str = ...,
        layoutConfiguration: LayoutConfigurationTypeDef = ...,
        requiredFields: Sequence[RequiredFieldTypeDef] = ...,
        status: TemplateStatusType = ...,
    ) -> CreateTemplateResponseTypeDef:
        """
        Creates a template in the Cases domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases.html#ConnectCases.Client.create_template)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connectcases/client/#create_template)
        """

    async def delete_domain(self, *, domainId: str) -> Dict[str, Any]:
        """
        Deletes a Cases domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases.html#ConnectCases.Client.delete_domain)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connectcases/client/#delete_domain)
        """

    async def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases.html#ConnectCases.Client.generate_presigned_url)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connectcases/client/#generate_presigned_url)
        """

    async def get_case(
        self,
        *,
        caseId: str,
        domainId: str,
        fields: Sequence[FieldIdentifierTypeDef],
        nextToken: str = ...,
    ) -> GetCaseResponseTypeDef:
        """
        Returns information about a specific case if it exists.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases.html#ConnectCases.Client.get_case)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connectcases/client/#get_case)
        """

    async def get_case_audit_events(
        self, *, caseId: str, domainId: str, maxResults: int = ..., nextToken: str = ...
    ) -> GetCaseAuditEventsResponseTypeDef:
        """
        Returns the audit history about a specific case if it exists.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases.html#ConnectCases.Client.get_case_audit_events)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connectcases/client/#get_case_audit_events)
        """

    async def get_case_event_configuration(
        self, *, domainId: str
    ) -> GetCaseEventConfigurationResponseTypeDef:
        """
        Returns the case event publishing configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases.html#ConnectCases.Client.get_case_event_configuration)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connectcases/client/#get_case_event_configuration)
        """

    async def get_domain(self, *, domainId: str) -> GetDomainResponseTypeDef:
        """
        Returns information about a specific domain if it exists.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases.html#ConnectCases.Client.get_domain)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connectcases/client/#get_domain)
        """

    async def get_layout(self, *, domainId: str, layoutId: str) -> GetLayoutResponseTypeDef:
        """
        Returns the details for the requested layout.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases.html#ConnectCases.Client.get_layout)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connectcases/client/#get_layout)
        """

    async def get_template(self, *, domainId: str, templateId: str) -> GetTemplateResponseTypeDef:
        """
        Returns the details for the requested template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases.html#ConnectCases.Client.get_template)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connectcases/client/#get_template)
        """

    async def list_cases_for_contact(
        self, *, contactArn: str, domainId: str, maxResults: int = ..., nextToken: str = ...
    ) -> ListCasesForContactResponseTypeDef:
        """
        Lists cases for a given contact.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases.html#ConnectCases.Client.list_cases_for_contact)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connectcases/client/#list_cases_for_contact)
        """

    async def list_domains(
        self, *, maxResults: int = ..., nextToken: str = ...
    ) -> ListDomainsResponseTypeDef:
        """
        Lists all cases domains in the Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases.html#ConnectCases.Client.list_domains)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connectcases/client/#list_domains)
        """

    async def list_field_options(
        self,
        *,
        domainId: str,
        fieldId: str,
        maxResults: int = ...,
        nextToken: str = ...,
        values: Sequence[str] = ...,
    ) -> ListFieldOptionsResponseTypeDef:
        """
        Lists all of the field options for a field identifier in the domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases.html#ConnectCases.Client.list_field_options)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connectcases/client/#list_field_options)
        """

    async def list_fields(
        self, *, domainId: str, maxResults: int = ..., nextToken: str = ...
    ) -> ListFieldsResponseTypeDef:
        """
        Lists all fields in a Cases domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases.html#ConnectCases.Client.list_fields)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connectcases/client/#list_fields)
        """

    async def list_layouts(
        self, *, domainId: str, maxResults: int = ..., nextToken: str = ...
    ) -> ListLayoutsResponseTypeDef:
        """
        Lists all layouts in the given cases domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases.html#ConnectCases.Client.list_layouts)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connectcases/client/#list_layouts)
        """

    async def list_tags_for_resource(self, *, arn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Lists tags for a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases.html#ConnectCases.Client.list_tags_for_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connectcases/client/#list_tags_for_resource)
        """

    async def list_templates(
        self,
        *,
        domainId: str,
        maxResults: int = ...,
        nextToken: str = ...,
        status: Sequence[TemplateStatusType] = ...,
    ) -> ListTemplatesResponseTypeDef:
        """
        Lists all of the templates in a Cases domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases.html#ConnectCases.Client.list_templates)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connectcases/client/#list_templates)
        """

    async def put_case_event_configuration(
        self, *, domainId: str, eventBridge: EventBridgeConfigurationTypeDef
    ) -> Dict[str, Any]:
        """
        Adds case event publishing configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases.html#ConnectCases.Client.put_case_event_configuration)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connectcases/client/#put_case_event_configuration)
        """

    async def search_cases(
        self,
        *,
        domainId: str,
        fields: Sequence[FieldIdentifierTypeDef] = ...,
        filter: "CaseFilterTypeDef" = ...,
        maxResults: int = ...,
        nextToken: str = ...,
        searchTerm: str = ...,
        sorts: Sequence[SortTypeDef] = ...,
    ) -> SearchCasesResponseTypeDef:
        """
        Searches for cases within their associated Cases domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases.html#ConnectCases.Client.search_cases)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connectcases/client/#search_cases)
        """

    async def search_related_items(
        self,
        *,
        caseId: str,
        domainId: str,
        filters: Sequence[RelatedItemTypeFilterTypeDef] = ...,
        maxResults: int = ...,
        nextToken: str = ...,
    ) -> SearchRelatedItemsResponseTypeDef:
        """
        Searches for related items that are associated with a case.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases.html#ConnectCases.Client.search_related_items)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connectcases/client/#search_related_items)
        """

    async def tag_resource(
        self, *, arn: str, tags: Mapping[str, str]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Adds tags to a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases.html#ConnectCases.Client.tag_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connectcases/client/#tag_resource)
        """

    async def untag_resource(
        self, *, arn: str, tagKeys: Sequence[str]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Untags a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases.html#ConnectCases.Client.untag_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connectcases/client/#untag_resource)
        """

    async def update_case(
        self,
        *,
        caseId: str,
        domainId: str,
        fields: Sequence[FieldValueTypeDef],
        performedBy: UserUnionTypeDef = ...,
    ) -> Dict[str, Any]:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases.html#ConnectCases.Client.update_case)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connectcases/client/#update_case)
        """

    async def update_field(
        self, *, domainId: str, fieldId: str, description: str = ..., name: str = ...
    ) -> Dict[str, Any]:
        """
        Updates the properties of an existing field.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases.html#ConnectCases.Client.update_field)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connectcases/client/#update_field)
        """

    async def update_layout(
        self, *, domainId: str, layoutId: str, content: LayoutContentTypeDef = ..., name: str = ...
    ) -> Dict[str, Any]:
        """
        Updates the attributes of an existing layout.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases.html#ConnectCases.Client.update_layout)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connectcases/client/#update_layout)
        """

    async def update_template(
        self,
        *,
        domainId: str,
        templateId: str,
        description: str = ...,
        layoutConfiguration: LayoutConfigurationTypeDef = ...,
        name: str = ...,
        requiredFields: Sequence[RequiredFieldTypeDef] = ...,
        status: TemplateStatusType = ...,
    ) -> Dict[str, Any]:
        """
        Updates the attributes of an existing template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases.html#ConnectCases.Client.update_template)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connectcases/client/#update_template)
        """

    @overload
    def get_paginator(self, operation_name: Literal["search_cases"]) -> SearchCasesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases.html#ConnectCases.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connectcases/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["search_related_items"]
    ) -> SearchRelatedItemsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases.html#ConnectCases.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connectcases/client/#get_paginator)
        """

    async def __aenter__(self) -> "ConnectCasesClient":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases.html#ConnectCases.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connectcases/client/)
        """

    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> Any:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases.html#ConnectCases.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connectcases/client/)
        """
