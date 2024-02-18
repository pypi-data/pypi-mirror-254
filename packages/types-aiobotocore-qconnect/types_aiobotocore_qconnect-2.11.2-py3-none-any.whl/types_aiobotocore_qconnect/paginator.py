"""
Type annotations for qconnect service client paginators.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qconnect/paginators/)

Usage::

    ```python
    from aiobotocore.session import get_session

    from types_aiobotocore_qconnect.client import QConnectClient
    from types_aiobotocore_qconnect.paginator import (
        ListAssistantAssociationsPaginator,
        ListAssistantsPaginator,
        ListContentsPaginator,
        ListImportJobsPaginator,
        ListKnowledgeBasesPaginator,
        ListQuickResponsesPaginator,
        QueryAssistantPaginator,
        SearchContentPaginator,
        SearchQuickResponsesPaginator,
        SearchSessionsPaginator,
    )

    session = get_session()
    with session.create_client("qconnect") as client:
        client: QConnectClient

        list_assistant_associations_paginator: ListAssistantAssociationsPaginator = client.get_paginator("list_assistant_associations")
        list_assistants_paginator: ListAssistantsPaginator = client.get_paginator("list_assistants")
        list_contents_paginator: ListContentsPaginator = client.get_paginator("list_contents")
        list_import_jobs_paginator: ListImportJobsPaginator = client.get_paginator("list_import_jobs")
        list_knowledge_bases_paginator: ListKnowledgeBasesPaginator = client.get_paginator("list_knowledge_bases")
        list_quick_responses_paginator: ListQuickResponsesPaginator = client.get_paginator("list_quick_responses")
        query_assistant_paginator: QueryAssistantPaginator = client.get_paginator("query_assistant")
        search_content_paginator: SearchContentPaginator = client.get_paginator("search_content")
        search_quick_responses_paginator: SearchQuickResponsesPaginator = client.get_paginator("search_quick_responses")
        search_sessions_paginator: SearchSessionsPaginator = client.get_paginator("search_sessions")
    ```
"""

from typing import AsyncIterator, Generic, Iterator, Mapping, Sequence, TypeVar

from aiobotocore.paginate import AioPaginator
from botocore.paginate import PageIterator

from .type_defs import (
    ListAssistantAssociationsResponseTypeDef,
    ListAssistantsResponseTypeDef,
    ListContentsResponseTypeDef,
    ListImportJobsResponseTypeDef,
    ListKnowledgeBasesResponsePaginatorTypeDef,
    ListQuickResponsesResponseTypeDef,
    PaginatorConfigTypeDef,
    QueryAssistantResponseTypeDef,
    QueryConditionTypeDef,
    QuickResponseSearchExpressionTypeDef,
    SearchContentResponseTypeDef,
    SearchExpressionTypeDef,
    SearchQuickResponsesResponsePaginatorTypeDef,
    SearchSessionsResponseTypeDef,
)

__all__ = (
    "ListAssistantAssociationsPaginator",
    "ListAssistantsPaginator",
    "ListContentsPaginator",
    "ListImportJobsPaginator",
    "ListKnowledgeBasesPaginator",
    "ListQuickResponsesPaginator",
    "QueryAssistantPaginator",
    "SearchContentPaginator",
    "SearchQuickResponsesPaginator",
    "SearchSessionsPaginator",
)

_ItemTypeDef = TypeVar("_ItemTypeDef")


class _PageIterator(Generic[_ItemTypeDef], PageIterator):
    def __iter__(self) -> Iterator[_ItemTypeDef]:
        """
        Proxy method to specify iterator item type.
        """


class ListAssistantAssociationsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Paginator.ListAssistantAssociations)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qconnect/paginators/#listassistantassociationspaginator)
    """

    def paginate(
        self, *, assistantId: str, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListAssistantAssociationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Paginator.ListAssistantAssociations.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qconnect/paginators/#listassistantassociationspaginator)
        """


class ListAssistantsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Paginator.ListAssistants)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qconnect/paginators/#listassistantspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListAssistantsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Paginator.ListAssistants.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qconnect/paginators/#listassistantspaginator)
        """


class ListContentsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Paginator.ListContents)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qconnect/paginators/#listcontentspaginator)
    """

    def paginate(
        self, *, knowledgeBaseId: str, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListContentsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Paginator.ListContents.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qconnect/paginators/#listcontentspaginator)
        """


class ListImportJobsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Paginator.ListImportJobs)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qconnect/paginators/#listimportjobspaginator)
    """

    def paginate(
        self, *, knowledgeBaseId: str, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListImportJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Paginator.ListImportJobs.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qconnect/paginators/#listimportjobspaginator)
        """


class ListKnowledgeBasesPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Paginator.ListKnowledgeBases)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qconnect/paginators/#listknowledgebasespaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListKnowledgeBasesResponsePaginatorTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Paginator.ListKnowledgeBases.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qconnect/paginators/#listknowledgebasespaginator)
        """


class ListQuickResponsesPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Paginator.ListQuickResponses)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qconnect/paginators/#listquickresponsespaginator)
    """

    def paginate(
        self, *, knowledgeBaseId: str, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListQuickResponsesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Paginator.ListQuickResponses.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qconnect/paginators/#listquickresponsespaginator)
        """


class QueryAssistantPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Paginator.QueryAssistant)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qconnect/paginators/#queryassistantpaginator)
    """

    def paginate(
        self,
        *,
        assistantId: str,
        queryText: str,
        queryCondition: Sequence[QueryConditionTypeDef] = ...,
        sessionId: str = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[QueryAssistantResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Paginator.QueryAssistant.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qconnect/paginators/#queryassistantpaginator)
        """


class SearchContentPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Paginator.SearchContent)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qconnect/paginators/#searchcontentpaginator)
    """

    def paginate(
        self,
        *,
        knowledgeBaseId: str,
        searchExpression: SearchExpressionTypeDef,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[SearchContentResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Paginator.SearchContent.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qconnect/paginators/#searchcontentpaginator)
        """


class SearchQuickResponsesPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Paginator.SearchQuickResponses)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qconnect/paginators/#searchquickresponsespaginator)
    """

    def paginate(
        self,
        *,
        knowledgeBaseId: str,
        searchExpression: QuickResponseSearchExpressionTypeDef,
        attributes: Mapping[str, str] = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[SearchQuickResponsesResponsePaginatorTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Paginator.SearchQuickResponses.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qconnect/paginators/#searchquickresponsespaginator)
        """


class SearchSessionsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Paginator.SearchSessions)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qconnect/paginators/#searchsessionspaginator)
    """

    def paginate(
        self,
        *,
        assistantId: str,
        searchExpression: SearchExpressionTypeDef,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[SearchSessionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Paginator.SearchSessions.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qconnect/paginators/#searchsessionspaginator)
        """
