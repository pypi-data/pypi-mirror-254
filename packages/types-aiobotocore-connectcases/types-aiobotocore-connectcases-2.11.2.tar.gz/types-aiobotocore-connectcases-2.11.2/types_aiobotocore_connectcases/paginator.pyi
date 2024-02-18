"""
Type annotations for connectcases service client paginators.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connectcases/paginators/)

Usage::

    ```python
    from aiobotocore.session import get_session

    from types_aiobotocore_connectcases.client import ConnectCasesClient
    from types_aiobotocore_connectcases.paginator import (
        SearchCasesPaginator,
        SearchRelatedItemsPaginator,
    )

    session = get_session()
    with session.create_client("connectcases") as client:
        client: ConnectCasesClient

        search_cases_paginator: SearchCasesPaginator = client.get_paginator("search_cases")
        search_related_items_paginator: SearchRelatedItemsPaginator = client.get_paginator("search_related_items")
    ```
"""

from typing import AsyncIterator, Generic, Iterator, Sequence, TypeVar

from aiobotocore.paginate import AioPaginator
from botocore.paginate import PageIterator

from .type_defs import (
    CaseFilterTypeDef,
    FieldIdentifierTypeDef,
    PaginatorConfigTypeDef,
    RelatedItemTypeFilterTypeDef,
    SearchCasesResponseTypeDef,
    SearchRelatedItemsResponseTypeDef,
    SortTypeDef,
)

__all__ = ("SearchCasesPaginator", "SearchRelatedItemsPaginator")

_ItemTypeDef = TypeVar("_ItemTypeDef")

class _PageIterator(Generic[_ItemTypeDef], PageIterator):
    def __iter__(self) -> Iterator[_ItemTypeDef]:
        """
        Proxy method to specify iterator item type.
        """

class SearchCasesPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases.html#ConnectCases.Paginator.SearchCases)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connectcases/paginators/#searchcasespaginator)
    """

    def paginate(
        self,
        *,
        domainId: str,
        fields: Sequence[FieldIdentifierTypeDef] = ...,
        filter: CaseFilterTypeDef = ...,
        searchTerm: str = ...,
        sorts: Sequence[SortTypeDef] = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[SearchCasesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases.html#ConnectCases.Paginator.SearchCases.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connectcases/paginators/#searchcasespaginator)
        """

class SearchRelatedItemsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases.html#ConnectCases.Paginator.SearchRelatedItems)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connectcases/paginators/#searchrelateditemspaginator)
    """

    def paginate(
        self,
        *,
        caseId: str,
        domainId: str,
        filters: Sequence[RelatedItemTypeFilterTypeDef] = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[SearchRelatedItemsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases.html#ConnectCases.Paginator.SearchRelatedItems.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connectcases/paginators/#searchrelateditemspaginator)
        """
