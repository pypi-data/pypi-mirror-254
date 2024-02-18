"""
Type annotations for qconnect service client.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qconnect/client/)

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_qconnect.client import QConnectClient

    session = get_session()
    async with session.create_client("qconnect") as client:
        client: QConnectClient
    ```
"""

import sys
from typing import Any, Dict, Mapping, Sequence, Type, overload

from aiobotocore.client import AioBaseClient
from botocore.client import ClientMeta

from .literals import KnowledgeBaseTypeType, TargetTypeType
from .paginator import (
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
from .type_defs import (
    AssistantAssociationInputDataTypeDef,
    ContentFeedbackDataTypeDef,
    CreateAssistantAssociationResponseTypeDef,
    CreateAssistantResponseTypeDef,
    CreateContentResponseTypeDef,
    CreateKnowledgeBaseResponseTypeDef,
    CreateQuickResponseResponseTypeDef,
    CreateSessionResponseTypeDef,
    ExternalSourceConfigurationTypeDef,
    GetAssistantAssociationResponseTypeDef,
    GetAssistantResponseTypeDef,
    GetContentResponseTypeDef,
    GetContentSummaryResponseTypeDef,
    GetImportJobResponseTypeDef,
    GetKnowledgeBaseResponseTypeDef,
    GetQuickResponseResponseTypeDef,
    GetRecommendationsResponseTypeDef,
    GetSessionResponseTypeDef,
    GroupingConfigurationTypeDef,
    ListAssistantAssociationsResponseTypeDef,
    ListAssistantsResponseTypeDef,
    ListContentsResponseTypeDef,
    ListImportJobsResponseTypeDef,
    ListKnowledgeBasesResponseTypeDef,
    ListQuickResponsesResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    NotifyRecommendationsReceivedResponseTypeDef,
    PutFeedbackResponseTypeDef,
    QueryAssistantResponseTypeDef,
    QueryConditionTypeDef,
    QuickResponseDataProviderTypeDef,
    QuickResponseSearchExpressionTypeDef,
    RenderingConfigurationTypeDef,
    SearchContentResponseTypeDef,
    SearchExpressionTypeDef,
    SearchQuickResponsesResponseTypeDef,
    SearchSessionsResponseTypeDef,
    ServerSideEncryptionConfigurationTypeDef,
    SourceConfigurationTypeDef,
    StartContentUploadResponseTypeDef,
    StartImportJobResponseTypeDef,
    UpdateContentResponseTypeDef,
    UpdateKnowledgeBaseTemplateUriResponseTypeDef,
    UpdateQuickResponseResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("QConnectClient",)

class BotocoreClientError(Exception):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    PreconditionFailedException: Type[BotocoreClientError]
    RequestTimeoutException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    TooManyTagsException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class QConnectClient(AioBaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qconnect/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        QConnectClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.exceptions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qconnect/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.can_paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qconnect/client/#can_paginate)
        """

    async def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.close)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qconnect/client/#close)
        """

    async def create_assistant(
        self,
        *,
        name: str,
        type: Literal["AGENT"],
        clientToken: str = ...,
        description: str = ...,
        serverSideEncryptionConfiguration: ServerSideEncryptionConfigurationTypeDef = ...,
        tags: Mapping[str, str] = ...,
    ) -> CreateAssistantResponseTypeDef:
        """
        Creates an Amazon Q in Connect assistant.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.create_assistant)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qconnect/client/#create_assistant)
        """

    async def create_assistant_association(
        self,
        *,
        assistantId: str,
        association: AssistantAssociationInputDataTypeDef,
        associationType: Literal["KNOWLEDGE_BASE"],
        clientToken: str = ...,
        tags: Mapping[str, str] = ...,
    ) -> CreateAssistantAssociationResponseTypeDef:
        """
        Creates an association between an Amazon Q in Connect assistant and another
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.create_assistant_association)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qconnect/client/#create_assistant_association)
        """

    async def create_content(
        self,
        *,
        knowledgeBaseId: str,
        name: str,
        uploadId: str,
        clientToken: str = ...,
        metadata: Mapping[str, str] = ...,
        overrideLinkOutUri: str = ...,
        tags: Mapping[str, str] = ...,
        title: str = ...,
    ) -> CreateContentResponseTypeDef:
        """
        Creates Amazon Q content.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.create_content)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qconnect/client/#create_content)
        """

    async def create_knowledge_base(
        self,
        *,
        knowledgeBaseType: KnowledgeBaseTypeType,
        name: str,
        clientToken: str = ...,
        description: str = ...,
        renderingConfiguration: RenderingConfigurationTypeDef = ...,
        serverSideEncryptionConfiguration: ServerSideEncryptionConfigurationTypeDef = ...,
        sourceConfiguration: SourceConfigurationTypeDef = ...,
        tags: Mapping[str, str] = ...,
    ) -> CreateKnowledgeBaseResponseTypeDef:
        """
        Creates a knowledge base.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.create_knowledge_base)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qconnect/client/#create_knowledge_base)
        """

    async def create_quick_response(
        self,
        *,
        content: QuickResponseDataProviderTypeDef,
        knowledgeBaseId: str,
        name: str,
        channels: Sequence[str] = ...,
        clientToken: str = ...,
        contentType: str = ...,
        description: str = ...,
        groupingConfiguration: GroupingConfigurationTypeDef = ...,
        isActive: bool = ...,
        language: str = ...,
        shortcutKey: str = ...,
        tags: Mapping[str, str] = ...,
    ) -> CreateQuickResponseResponseTypeDef:
        """
        Creates an Amazon Q quick response.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.create_quick_response)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qconnect/client/#create_quick_response)
        """

    async def create_session(
        self,
        *,
        assistantId: str,
        name: str,
        clientToken: str = ...,
        description: str = ...,
        tags: Mapping[str, str] = ...,
    ) -> CreateSessionResponseTypeDef:
        """
        Creates a session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.create_session)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qconnect/client/#create_session)
        """

    async def delete_assistant(self, *, assistantId: str) -> Dict[str, Any]:
        """
        Deletes an assistant.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.delete_assistant)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qconnect/client/#delete_assistant)
        """

    async def delete_assistant_association(
        self, *, assistantAssociationId: str, assistantId: str
    ) -> Dict[str, Any]:
        """
        Deletes an assistant association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.delete_assistant_association)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qconnect/client/#delete_assistant_association)
        """

    async def delete_content(self, *, contentId: str, knowledgeBaseId: str) -> Dict[str, Any]:
        """
        Deletes the content.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.delete_content)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qconnect/client/#delete_content)
        """

    async def delete_import_job(self, *, importJobId: str, knowledgeBaseId: str) -> Dict[str, Any]:
        """
        Deletes the quick response import job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.delete_import_job)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qconnect/client/#delete_import_job)
        """

    async def delete_knowledge_base(self, *, knowledgeBaseId: str) -> Dict[str, Any]:
        """
        Deletes the knowledge base.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.delete_knowledge_base)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qconnect/client/#delete_knowledge_base)
        """

    async def delete_quick_response(
        self, *, knowledgeBaseId: str, quickResponseId: str
    ) -> Dict[str, Any]:
        """
        Deletes a quick response.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.delete_quick_response)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qconnect/client/#delete_quick_response)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.generate_presigned_url)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qconnect/client/#generate_presigned_url)
        """

    async def get_assistant(self, *, assistantId: str) -> GetAssistantResponseTypeDef:
        """
        Retrieves information about an assistant.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.get_assistant)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qconnect/client/#get_assistant)
        """

    async def get_assistant_association(
        self, *, assistantAssociationId: str, assistantId: str
    ) -> GetAssistantAssociationResponseTypeDef:
        """
        Retrieves information about an assistant association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.get_assistant_association)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qconnect/client/#get_assistant_association)
        """

    async def get_content(
        self, *, contentId: str, knowledgeBaseId: str
    ) -> GetContentResponseTypeDef:
        """
        Retrieves content, including a pre-signed URL to download the content.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.get_content)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qconnect/client/#get_content)
        """

    async def get_content_summary(
        self, *, contentId: str, knowledgeBaseId: str
    ) -> GetContentSummaryResponseTypeDef:
        """
        Retrieves summary information about the content.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.get_content_summary)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qconnect/client/#get_content_summary)
        """

    async def get_import_job(
        self, *, importJobId: str, knowledgeBaseId: str
    ) -> GetImportJobResponseTypeDef:
        """
        Retrieves the started import job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.get_import_job)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qconnect/client/#get_import_job)
        """

    async def get_knowledge_base(self, *, knowledgeBaseId: str) -> GetKnowledgeBaseResponseTypeDef:
        """
        Retrieves information about the knowledge base.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.get_knowledge_base)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qconnect/client/#get_knowledge_base)
        """

    async def get_quick_response(
        self, *, knowledgeBaseId: str, quickResponseId: str
    ) -> GetQuickResponseResponseTypeDef:
        """
        Retrieves the quick response.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.get_quick_response)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qconnect/client/#get_quick_response)
        """

    async def get_recommendations(
        self, *, assistantId: str, sessionId: str, maxResults: int = ..., waitTimeSeconds: int = ...
    ) -> GetRecommendationsResponseTypeDef:
        """
        Retrieves recommendations for the specified session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.get_recommendations)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qconnect/client/#get_recommendations)
        """

    async def get_session(self, *, assistantId: str, sessionId: str) -> GetSessionResponseTypeDef:
        """
        Retrieves information for a specified session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.get_session)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qconnect/client/#get_session)
        """

    async def list_assistant_associations(
        self, *, assistantId: str, maxResults: int = ..., nextToken: str = ...
    ) -> ListAssistantAssociationsResponseTypeDef:
        """
        Lists information about assistant associations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.list_assistant_associations)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qconnect/client/#list_assistant_associations)
        """

    async def list_assistants(
        self, *, maxResults: int = ..., nextToken: str = ...
    ) -> ListAssistantsResponseTypeDef:
        """
        Lists information about assistants.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.list_assistants)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qconnect/client/#list_assistants)
        """

    async def list_contents(
        self, *, knowledgeBaseId: str, maxResults: int = ..., nextToken: str = ...
    ) -> ListContentsResponseTypeDef:
        """
        Lists the content.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.list_contents)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qconnect/client/#list_contents)
        """

    async def list_import_jobs(
        self, *, knowledgeBaseId: str, maxResults: int = ..., nextToken: str = ...
    ) -> ListImportJobsResponseTypeDef:
        """
        Lists information about import jobs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.list_import_jobs)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qconnect/client/#list_import_jobs)
        """

    async def list_knowledge_bases(
        self, *, maxResults: int = ..., nextToken: str = ...
    ) -> ListKnowledgeBasesResponseTypeDef:
        """
        Lists the knowledge bases.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.list_knowledge_bases)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qconnect/client/#list_knowledge_bases)
        """

    async def list_quick_responses(
        self, *, knowledgeBaseId: str, maxResults: int = ..., nextToken: str = ...
    ) -> ListQuickResponsesResponseTypeDef:
        """
        Lists information about quick response.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.list_quick_responses)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qconnect/client/#list_quick_responses)
        """

    async def list_tags_for_resource(
        self, *, resourceArn: str
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists the tags for the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.list_tags_for_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qconnect/client/#list_tags_for_resource)
        """

    async def notify_recommendations_received(
        self, *, assistantId: str, recommendationIds: Sequence[str], sessionId: str
    ) -> NotifyRecommendationsReceivedResponseTypeDef:
        """
        Removes the specified recommendations from the specified assistant's queue of
        newly available
        recommendations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.notify_recommendations_received)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qconnect/client/#notify_recommendations_received)
        """

    async def put_feedback(
        self,
        *,
        assistantId: str,
        contentFeedback: ContentFeedbackDataTypeDef,
        targetId: str,
        targetType: TargetTypeType,
    ) -> PutFeedbackResponseTypeDef:
        """
        Provides feedback against the specified assistant for the specified target.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.put_feedback)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qconnect/client/#put_feedback)
        """

    async def query_assistant(
        self,
        *,
        assistantId: str,
        queryText: str,
        maxResults: int = ...,
        nextToken: str = ...,
        queryCondition: Sequence[QueryConditionTypeDef] = ...,
        sessionId: str = ...,
    ) -> QueryAssistantResponseTypeDef:
        """
        Performs a manual search against the specified assistant.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.query_assistant)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qconnect/client/#query_assistant)
        """

    async def remove_knowledge_base_template_uri(self, *, knowledgeBaseId: str) -> Dict[str, Any]:
        """
        Removes a URI template from a knowledge base.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.remove_knowledge_base_template_uri)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qconnect/client/#remove_knowledge_base_template_uri)
        """

    async def search_content(
        self,
        *,
        knowledgeBaseId: str,
        searchExpression: SearchExpressionTypeDef,
        maxResults: int = ...,
        nextToken: str = ...,
    ) -> SearchContentResponseTypeDef:
        """
        Searches for content in a specified knowledge base.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.search_content)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qconnect/client/#search_content)
        """

    async def search_quick_responses(
        self,
        *,
        knowledgeBaseId: str,
        searchExpression: QuickResponseSearchExpressionTypeDef,
        attributes: Mapping[str, str] = ...,
        maxResults: int = ...,
        nextToken: str = ...,
    ) -> SearchQuickResponsesResponseTypeDef:
        """
        Searches existing Amazon Q quick responses in an Amazon Q knowledge base.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.search_quick_responses)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qconnect/client/#search_quick_responses)
        """

    async def search_sessions(
        self,
        *,
        assistantId: str,
        searchExpression: SearchExpressionTypeDef,
        maxResults: int = ...,
        nextToken: str = ...,
    ) -> SearchSessionsResponseTypeDef:
        """
        Searches for sessions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.search_sessions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qconnect/client/#search_sessions)
        """

    async def start_content_upload(
        self, *, contentType: str, knowledgeBaseId: str, presignedUrlTimeToLive: int = ...
    ) -> StartContentUploadResponseTypeDef:
        """
        Get a URL to upload content to a knowledge base.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.start_content_upload)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qconnect/client/#start_content_upload)
        """

    async def start_import_job(
        self,
        *,
        importJobType: Literal["QUICK_RESPONSES"],
        knowledgeBaseId: str,
        uploadId: str,
        clientToken: str = ...,
        externalSourceConfiguration: ExternalSourceConfigurationTypeDef = ...,
        metadata: Mapping[str, str] = ...,
    ) -> StartImportJobResponseTypeDef:
        """
        Start an asynchronous job to import Amazon Q resources from an uploaded source
        file.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.start_import_job)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qconnect/client/#start_import_job)
        """

    async def tag_resource(self, *, resourceArn: str, tags: Mapping[str, str]) -> Dict[str, Any]:
        """
        Adds the specified tags to the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.tag_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qconnect/client/#tag_resource)
        """

    async def untag_resource(self, *, resourceArn: str, tagKeys: Sequence[str]) -> Dict[str, Any]:
        """
        Removes the specified tags from the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.untag_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qconnect/client/#untag_resource)
        """

    async def update_content(
        self,
        *,
        contentId: str,
        knowledgeBaseId: str,
        metadata: Mapping[str, str] = ...,
        overrideLinkOutUri: str = ...,
        removeOverrideLinkOutUri: bool = ...,
        revisionId: str = ...,
        title: str = ...,
        uploadId: str = ...,
    ) -> UpdateContentResponseTypeDef:
        """
        Updates information about the content.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.update_content)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qconnect/client/#update_content)
        """

    async def update_knowledge_base_template_uri(
        self, *, knowledgeBaseId: str, templateUri: str
    ) -> UpdateKnowledgeBaseTemplateUriResponseTypeDef:
        """
        Updates the template URI of a knowledge base.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.update_knowledge_base_template_uri)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qconnect/client/#update_knowledge_base_template_uri)
        """

    async def update_quick_response(
        self,
        *,
        knowledgeBaseId: str,
        quickResponseId: str,
        channels: Sequence[str] = ...,
        content: QuickResponseDataProviderTypeDef = ...,
        contentType: str = ...,
        description: str = ...,
        groupingConfiguration: GroupingConfigurationTypeDef = ...,
        isActive: bool = ...,
        language: str = ...,
        name: str = ...,
        removeDescription: bool = ...,
        removeGroupingConfiguration: bool = ...,
        removeShortcutKey: bool = ...,
        shortcutKey: str = ...,
    ) -> UpdateQuickResponseResponseTypeDef:
        """
        Updates an existing Amazon Q quick response.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.update_quick_response)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qconnect/client/#update_quick_response)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_assistant_associations"]
    ) -> ListAssistantAssociationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qconnect/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_assistants"]) -> ListAssistantsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qconnect/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_contents"]) -> ListContentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qconnect/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_import_jobs"]) -> ListImportJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qconnect/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_knowledge_bases"]
    ) -> ListKnowledgeBasesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qconnect/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_quick_responses"]
    ) -> ListQuickResponsesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qconnect/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["query_assistant"]) -> QueryAssistantPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qconnect/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["search_content"]) -> SearchContentPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qconnect/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["search_quick_responses"]
    ) -> SearchQuickResponsesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qconnect/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["search_sessions"]) -> SearchSessionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qconnect/client/#get_paginator)
        """

    async def __aenter__(self) -> "QConnectClient":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qconnect/client/)
        """

    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> Any:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect.html#QConnect.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qconnect/client/)
        """
