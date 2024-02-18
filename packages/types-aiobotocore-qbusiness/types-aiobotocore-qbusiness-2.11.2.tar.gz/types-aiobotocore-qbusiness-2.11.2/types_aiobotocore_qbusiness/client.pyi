"""
Type annotations for qbusiness service client.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qbusiness/client/)

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_qbusiness.client import QBusinessClient

    session = get_session()
    async with session.create_client("qbusiness") as client:
        client: QBusinessClient
    ```
"""

import sys
from typing import Any, Dict, Mapping, Sequence, Type, overload

from aiobotocore.client import AioBaseClient
from botocore.client import ClientMeta

from .literals import (
    DataSourceSyncJobStatusType,
    MembershipTypeType,
    PluginStateType,
    PluginTypeType,
    ResponseScopeType,
    RetrieverTypeType,
    WebExperienceSamplePromptsControlModeType,
)
from .paginator import (
    GetChatControlsConfigurationPaginator,
    ListApplicationsPaginator,
    ListConversationsPaginator,
    ListDataSourcesPaginator,
    ListDataSourceSyncJobsPaginator,
    ListDocumentsPaginator,
    ListGroupsPaginator,
    ListIndicesPaginator,
    ListMessagesPaginator,
    ListPluginsPaginator,
    ListRetrieversPaginator,
    ListWebExperiencesPaginator,
)
from .type_defs import (
    ActionExecutionTypeDef,
    AttachmentInputTypeDef,
    AttachmentsConfigurationTypeDef,
    AttributeFilterTypeDef,
    BatchDeleteDocumentResponseTypeDef,
    BatchPutDocumentResponseTypeDef,
    BlockedPhrasesConfigurationUpdateTypeDef,
    ChatSyncOutputTypeDef,
    CreateApplicationResponseTypeDef,
    CreateDataSourceResponseTypeDef,
    CreateIndexResponseTypeDef,
    CreatePluginResponseTypeDef,
    CreateRetrieverResponseTypeDef,
    CreateWebExperienceResponseTypeDef,
    DataSourceVpcConfigurationTypeDef,
    DeleteDocumentTypeDef,
    DocumentAttributeConfigurationTypeDef,
    DocumentEnrichmentConfigurationTypeDef,
    DocumentTypeDef,
    EmptyResponseMetadataTypeDef,
    EncryptionConfigurationTypeDef,
    GetApplicationResponseTypeDef,
    GetChatControlsConfigurationResponseTypeDef,
    GetDataSourceResponseTypeDef,
    GetGroupResponseTypeDef,
    GetIndexResponseTypeDef,
    GetPluginResponseTypeDef,
    GetRetrieverResponseTypeDef,
    GetUserResponseTypeDef,
    GetWebExperienceResponseTypeDef,
    GroupMembersTypeDef,
    IndexCapacityConfigurationTypeDef,
    ListApplicationsResponseTypeDef,
    ListConversationsResponseTypeDef,
    ListDataSourcesResponseTypeDef,
    ListDataSourceSyncJobsResponseTypeDef,
    ListDocumentsResponseTypeDef,
    ListGroupsResponseTypeDef,
    ListIndicesResponseTypeDef,
    ListMessagesResponseTypeDef,
    ListPluginsResponseTypeDef,
    ListRetrieversResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListWebExperiencesResponseTypeDef,
    MessageUsefulnessFeedbackTypeDef,
    PluginAuthConfigurationTypeDef,
    RetrieverConfigurationTypeDef,
    StartDataSourceSyncJobResponseTypeDef,
    TagTypeDef,
    TimestampTypeDef,
    TopicConfigurationTypeDef,
    UpdateUserResponseTypeDef,
    UserAliasTypeDef,
    WebExperienceAuthConfigurationTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("QBusinessClient",)

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
    LicenseNotFoundException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class QBusinessClient(AioBaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness.html#QBusiness.Client)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qbusiness/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        QBusinessClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness.html#QBusiness.Client.exceptions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qbusiness/client/#exceptions)
        """

    async def batch_delete_document(
        self,
        *,
        applicationId: str,
        documents: Sequence[DeleteDocumentTypeDef],
        indexId: str,
        dataSourceSyncId: str = ...,
    ) -> BatchDeleteDocumentResponseTypeDef:
        """
        Asynchronously deletes one or more documents added using the `BatchPutDocument`
        API from an Amazon Q
        index.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness.html#QBusiness.Client.batch_delete_document)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qbusiness/client/#batch_delete_document)
        """

    async def batch_put_document(
        self,
        *,
        applicationId: str,
        documents: Sequence[DocumentTypeDef],
        indexId: str,
        dataSourceSyncId: str = ...,
        roleArn: str = ...,
    ) -> BatchPutDocumentResponseTypeDef:
        """
        Adds one or more documents to an Amazon Q index.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness.html#QBusiness.Client.batch_put_document)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qbusiness/client/#batch_put_document)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness.html#QBusiness.Client.can_paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qbusiness/client/#can_paginate)
        """

    async def chat_sync(
        self,
        *,
        applicationId: str,
        userId: str,
        actionExecution: ActionExecutionTypeDef = ...,
        attachments: Sequence[AttachmentInputTypeDef] = ...,
        attributeFilter: "AttributeFilterTypeDef" = ...,
        clientToken: str = ...,
        conversationId: str = ...,
        parentMessageId: str = ...,
        userGroups: Sequence[str] = ...,
        userMessage: str = ...,
    ) -> ChatSyncOutputTypeDef:
        """
        Starts or continues a non-streaming Amazon Q conversation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness.html#QBusiness.Client.chat_sync)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qbusiness/client/#chat_sync)
        """

    async def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness.html#QBusiness.Client.close)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qbusiness/client/#close)
        """

    async def create_application(
        self,
        *,
        displayName: str,
        roleArn: str,
        attachmentsConfiguration: AttachmentsConfigurationTypeDef = ...,
        clientToken: str = ...,
        description: str = ...,
        encryptionConfiguration: EncryptionConfigurationTypeDef = ...,
        tags: Sequence[TagTypeDef] = ...,
    ) -> CreateApplicationResponseTypeDef:
        """
        Creates an Amazon Q application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness.html#QBusiness.Client.create_application)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qbusiness/client/#create_application)
        """

    async def create_data_source(
        self,
        *,
        applicationId: str,
        configuration: Mapping[str, Any],
        displayName: str,
        indexId: str,
        clientToken: str = ...,
        description: str = ...,
        documentEnrichmentConfiguration: DocumentEnrichmentConfigurationTypeDef = ...,
        roleArn: str = ...,
        syncSchedule: str = ...,
        tags: Sequence[TagTypeDef] = ...,
        vpcConfiguration: DataSourceVpcConfigurationTypeDef = ...,
    ) -> CreateDataSourceResponseTypeDef:
        """
        Creates a data source connector for an Amazon Q application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness.html#QBusiness.Client.create_data_source)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qbusiness/client/#create_data_source)
        """

    async def create_index(
        self,
        *,
        applicationId: str,
        displayName: str,
        capacityConfiguration: IndexCapacityConfigurationTypeDef = ...,
        clientToken: str = ...,
        description: str = ...,
        tags: Sequence[TagTypeDef] = ...,
    ) -> CreateIndexResponseTypeDef:
        """
        Creates an Amazon Q index.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness.html#QBusiness.Client.create_index)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qbusiness/client/#create_index)
        """

    async def create_plugin(
        self,
        *,
        applicationId: str,
        authConfiguration: PluginAuthConfigurationTypeDef,
        displayName: str,
        serverUrl: str,
        type: PluginTypeType,
        clientToken: str = ...,
        tags: Sequence[TagTypeDef] = ...,
    ) -> CreatePluginResponseTypeDef:
        """
        Creates an Amazon Q plugin.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness.html#QBusiness.Client.create_plugin)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qbusiness/client/#create_plugin)
        """

    async def create_retriever(
        self,
        *,
        applicationId: str,
        configuration: RetrieverConfigurationTypeDef,
        displayName: str,
        type: RetrieverTypeType,
        clientToken: str = ...,
        roleArn: str = ...,
        tags: Sequence[TagTypeDef] = ...,
    ) -> CreateRetrieverResponseTypeDef:
        """
        Adds a retriever to your Amazon Q application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness.html#QBusiness.Client.create_retriever)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qbusiness/client/#create_retriever)
        """

    async def create_user(
        self,
        *,
        applicationId: str,
        userId: str,
        clientToken: str = ...,
        userAliases: Sequence[UserAliasTypeDef] = ...,
    ) -> Dict[str, Any]:
        """
        Creates a universally unique identifier (UUID) mapped to a list of local user
        ids within an
        application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness.html#QBusiness.Client.create_user)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qbusiness/client/#create_user)
        """

    async def create_web_experience(
        self,
        *,
        applicationId: str,
        clientToken: str = ...,
        samplePromptsControlMode: WebExperienceSamplePromptsControlModeType = ...,
        subtitle: str = ...,
        tags: Sequence[TagTypeDef] = ...,
        title: str = ...,
        welcomeMessage: str = ...,
    ) -> CreateWebExperienceResponseTypeDef:
        """
        Creates an Amazon Q web experience.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness.html#QBusiness.Client.create_web_experience)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qbusiness/client/#create_web_experience)
        """

    async def delete_application(self, *, applicationId: str) -> Dict[str, Any]:
        """
        Deletes an Amazon Q application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness.html#QBusiness.Client.delete_application)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qbusiness/client/#delete_application)
        """

    async def delete_chat_controls_configuration(self, *, applicationId: str) -> Dict[str, Any]:
        """
        Deletes chat controls configured for an existing Amazon Q application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness.html#QBusiness.Client.delete_chat_controls_configuration)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qbusiness/client/#delete_chat_controls_configuration)
        """

    async def delete_conversation(
        self, *, applicationId: str, conversationId: str, userId: str
    ) -> Dict[str, Any]:
        """
        Deletes an Amazon Q web experience conversation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness.html#QBusiness.Client.delete_conversation)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qbusiness/client/#delete_conversation)
        """

    async def delete_data_source(
        self, *, applicationId: str, dataSourceId: str, indexId: str
    ) -> Dict[str, Any]:
        """
        Deletes an Amazon Q data source connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness.html#QBusiness.Client.delete_data_source)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qbusiness/client/#delete_data_source)
        """

    async def delete_group(
        self, *, applicationId: str, groupName: str, indexId: str, dataSourceId: str = ...
    ) -> Dict[str, Any]:
        """
        Deletes a group so that all users and sub groups that belong to the group can
        no longer access documents only available to that
        group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness.html#QBusiness.Client.delete_group)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qbusiness/client/#delete_group)
        """

    async def delete_index(self, *, applicationId: str, indexId: str) -> Dict[str, Any]:
        """
        Deletes an Amazon Q index.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness.html#QBusiness.Client.delete_index)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qbusiness/client/#delete_index)
        """

    async def delete_plugin(self, *, applicationId: str, pluginId: str) -> Dict[str, Any]:
        """
        Deletes an Amazon Q plugin.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness.html#QBusiness.Client.delete_plugin)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qbusiness/client/#delete_plugin)
        """

    async def delete_retriever(self, *, applicationId: str, retrieverId: str) -> Dict[str, Any]:
        """
        Deletes the retriever used by an Amazon Q application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness.html#QBusiness.Client.delete_retriever)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qbusiness/client/#delete_retriever)
        """

    async def delete_user(self, *, applicationId: str, userId: str) -> Dict[str, Any]:
        """
        Deletes a user by email id.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness.html#QBusiness.Client.delete_user)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qbusiness/client/#delete_user)
        """

    async def delete_web_experience(
        self, *, applicationId: str, webExperienceId: str
    ) -> Dict[str, Any]:
        """
        Deletes an Amazon Q web experience.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness.html#QBusiness.Client.delete_web_experience)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qbusiness/client/#delete_web_experience)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness.html#QBusiness.Client.generate_presigned_url)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qbusiness/client/#generate_presigned_url)
        """

    async def get_application(self, *, applicationId: str) -> GetApplicationResponseTypeDef:
        """
        Gets information about an existing Amazon Q application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness.html#QBusiness.Client.get_application)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qbusiness/client/#get_application)
        """

    async def get_chat_controls_configuration(
        self, *, applicationId: str, maxResults: int = ..., nextToken: str = ...
    ) -> GetChatControlsConfigurationResponseTypeDef:
        """
        Gets information about an chat controls configured for an existing Amazon Q
        application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness.html#QBusiness.Client.get_chat_controls_configuration)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qbusiness/client/#get_chat_controls_configuration)
        """

    async def get_data_source(
        self, *, applicationId: str, dataSourceId: str, indexId: str
    ) -> GetDataSourceResponseTypeDef:
        """
        Gets information about an existing Amazon Q data source connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness.html#QBusiness.Client.get_data_source)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qbusiness/client/#get_data_source)
        """

    async def get_group(
        self, *, applicationId: str, groupName: str, indexId: str, dataSourceId: str = ...
    ) -> GetGroupResponseTypeDef:
        """
        Describes a group by group name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness.html#QBusiness.Client.get_group)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qbusiness/client/#get_group)
        """

    async def get_index(self, *, applicationId: str, indexId: str) -> GetIndexResponseTypeDef:
        """
        Gets information about an existing Amazon Q index.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness.html#QBusiness.Client.get_index)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qbusiness/client/#get_index)
        """

    async def get_plugin(self, *, applicationId: str, pluginId: str) -> GetPluginResponseTypeDef:
        """
        Gets information about an existing Amazon Q plugin.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness.html#QBusiness.Client.get_plugin)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qbusiness/client/#get_plugin)
        """

    async def get_retriever(
        self, *, applicationId: str, retrieverId: str
    ) -> GetRetrieverResponseTypeDef:
        """
        Gets information about an existing retriever used by an Amazon Q application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness.html#QBusiness.Client.get_retriever)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qbusiness/client/#get_retriever)
        """

    async def get_user(self, *, applicationId: str, userId: str) -> GetUserResponseTypeDef:
        """
        Describes the universally unique identifier (UUID) associated with a local user
        in a data
        source.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness.html#QBusiness.Client.get_user)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qbusiness/client/#get_user)
        """

    async def get_web_experience(
        self, *, applicationId: str, webExperienceId: str
    ) -> GetWebExperienceResponseTypeDef:
        """
        Gets information about an existing Amazon Q web experience.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness.html#QBusiness.Client.get_web_experience)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qbusiness/client/#get_web_experience)
        """

    async def list_applications(
        self, *, maxResults: int = ..., nextToken: str = ...
    ) -> ListApplicationsResponseTypeDef:
        """
        Lists Amazon Q applications.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness.html#QBusiness.Client.list_applications)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qbusiness/client/#list_applications)
        """

    async def list_conversations(
        self, *, applicationId: str, userId: str, maxResults: int = ..., nextToken: str = ...
    ) -> ListConversationsResponseTypeDef:
        """
        Lists one or more Amazon Q conversations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness.html#QBusiness.Client.list_conversations)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qbusiness/client/#list_conversations)
        """

    async def list_data_source_sync_jobs(
        self,
        *,
        applicationId: str,
        dataSourceId: str,
        indexId: str,
        endTime: TimestampTypeDef = ...,
        maxResults: int = ...,
        nextToken: str = ...,
        startTime: TimestampTypeDef = ...,
        statusFilter: DataSourceSyncJobStatusType = ...,
    ) -> ListDataSourceSyncJobsResponseTypeDef:
        """
        Get information about an Amazon Q data source connector synchronization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness.html#QBusiness.Client.list_data_source_sync_jobs)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qbusiness/client/#list_data_source_sync_jobs)
        """

    async def list_data_sources(
        self, *, applicationId: str, indexId: str, maxResults: int = ..., nextToken: str = ...
    ) -> ListDataSourcesResponseTypeDef:
        """
        Lists the Amazon Q data source connectors that you have created.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness.html#QBusiness.Client.list_data_sources)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qbusiness/client/#list_data_sources)
        """

    async def list_documents(
        self,
        *,
        applicationId: str,
        indexId: str,
        dataSourceIds: Sequence[str] = ...,
        maxResults: int = ...,
        nextToken: str = ...,
    ) -> ListDocumentsResponseTypeDef:
        """
        A list of documents attached to an index.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness.html#QBusiness.Client.list_documents)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qbusiness/client/#list_documents)
        """

    async def list_groups(
        self,
        *,
        applicationId: str,
        indexId: str,
        updatedEarlierThan: TimestampTypeDef,
        dataSourceId: str = ...,
        maxResults: int = ...,
        nextToken: str = ...,
    ) -> ListGroupsResponseTypeDef:
        """
        Provides a list of groups that are mapped to users.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness.html#QBusiness.Client.list_groups)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qbusiness/client/#list_groups)
        """

    async def list_indices(
        self, *, applicationId: str, maxResults: int = ..., nextToken: str = ...
    ) -> ListIndicesResponseTypeDef:
        """
        Lists the Amazon Q indices you have created.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness.html#QBusiness.Client.list_indices)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qbusiness/client/#list_indices)
        """

    async def list_messages(
        self,
        *,
        applicationId: str,
        conversationId: str,
        userId: str,
        maxResults: int = ...,
        nextToken: str = ...,
    ) -> ListMessagesResponseTypeDef:
        """
        Gets a list of messages associated with an Amazon Q web experience.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness.html#QBusiness.Client.list_messages)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qbusiness/client/#list_messages)
        """

    async def list_plugins(
        self, *, applicationId: str, maxResults: int = ..., nextToken: str = ...
    ) -> ListPluginsResponseTypeDef:
        """
        Lists configured Amazon Q plugins.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness.html#QBusiness.Client.list_plugins)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qbusiness/client/#list_plugins)
        """

    async def list_retrievers(
        self, *, applicationId: str, maxResults: int = ..., nextToken: str = ...
    ) -> ListRetrieversResponseTypeDef:
        """
        Lists the retriever used by an Amazon Q application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness.html#QBusiness.Client.list_retrievers)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qbusiness/client/#list_retrievers)
        """

    async def list_tags_for_resource(
        self, *, resourceARN: str
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Gets a list of tags associated with a specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness.html#QBusiness.Client.list_tags_for_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qbusiness/client/#list_tags_for_resource)
        """

    async def list_web_experiences(
        self, *, applicationId: str, maxResults: int = ..., nextToken: str = ...
    ) -> ListWebExperiencesResponseTypeDef:
        """
        Lists one or more Amazon Q Web Experiences.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness.html#QBusiness.Client.list_web_experiences)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qbusiness/client/#list_web_experiences)
        """

    async def put_feedback(
        self,
        *,
        applicationId: str,
        conversationId: str,
        messageId: str,
        userId: str,
        messageCopiedAt: TimestampTypeDef = ...,
        messageUsefulness: MessageUsefulnessFeedbackTypeDef = ...,
    ) -> EmptyResponseMetadataTypeDef:
        """
        Enables your end user to to provide feedback on their Amazon Q generated chat
        responses.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness.html#QBusiness.Client.put_feedback)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qbusiness/client/#put_feedback)
        """

    async def put_group(
        self,
        *,
        applicationId: str,
        groupMembers: GroupMembersTypeDef,
        groupName: str,
        indexId: str,
        type: MembershipTypeType,
        dataSourceId: str = ...,
    ) -> Dict[str, Any]:
        """
        Create, or updates, a mapping of users—who have access to a document—to groups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness.html#QBusiness.Client.put_group)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qbusiness/client/#put_group)
        """

    async def start_data_source_sync_job(
        self, *, applicationId: str, dataSourceId: str, indexId: str
    ) -> StartDataSourceSyncJobResponseTypeDef:
        """
        Starts a data source connector synchronization job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness.html#QBusiness.Client.start_data_source_sync_job)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qbusiness/client/#start_data_source_sync_job)
        """

    async def stop_data_source_sync_job(
        self, *, applicationId: str, dataSourceId: str, indexId: str
    ) -> Dict[str, Any]:
        """
        Stops an Amazon Q data source connector synchronization job already in progress.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness.html#QBusiness.Client.stop_data_source_sync_job)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qbusiness/client/#stop_data_source_sync_job)
        """

    async def tag_resource(self, *, resourceARN: str, tags: Sequence[TagTypeDef]) -> Dict[str, Any]:
        """
        Adds the specified tag to the specified Amazon Q application or data source
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness.html#QBusiness.Client.tag_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qbusiness/client/#tag_resource)
        """

    async def untag_resource(self, *, resourceARN: str, tagKeys: Sequence[str]) -> Dict[str, Any]:
        """
        Removes a tag from an Amazon Q application or a data source.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness.html#QBusiness.Client.untag_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qbusiness/client/#untag_resource)
        """

    async def update_application(
        self,
        *,
        applicationId: str,
        attachmentsConfiguration: AttachmentsConfigurationTypeDef = ...,
        description: str = ...,
        displayName: str = ...,
        roleArn: str = ...,
    ) -> Dict[str, Any]:
        """
        Updates an existing Amazon Q application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness.html#QBusiness.Client.update_application)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qbusiness/client/#update_application)
        """

    async def update_chat_controls_configuration(
        self,
        *,
        applicationId: str,
        blockedPhrasesConfigurationUpdate: BlockedPhrasesConfigurationUpdateTypeDef = ...,
        clientToken: str = ...,
        responseScope: ResponseScopeType = ...,
        topicConfigurationsToCreateOrUpdate: Sequence[TopicConfigurationTypeDef] = ...,
        topicConfigurationsToDelete: Sequence[TopicConfigurationTypeDef] = ...,
    ) -> Dict[str, Any]:
        """
        Updates an set of chat controls configured for an existing Amazon Q application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness.html#QBusiness.Client.update_chat_controls_configuration)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qbusiness/client/#update_chat_controls_configuration)
        """

    async def update_data_source(
        self,
        *,
        applicationId: str,
        dataSourceId: str,
        indexId: str,
        configuration: Mapping[str, Any] = ...,
        description: str = ...,
        displayName: str = ...,
        documentEnrichmentConfiguration: DocumentEnrichmentConfigurationTypeDef = ...,
        roleArn: str = ...,
        syncSchedule: str = ...,
        vpcConfiguration: DataSourceVpcConfigurationTypeDef = ...,
    ) -> Dict[str, Any]:
        """
        Updates an existing Amazon Q data source connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness.html#QBusiness.Client.update_data_source)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qbusiness/client/#update_data_source)
        """

    async def update_index(
        self,
        *,
        applicationId: str,
        indexId: str,
        capacityConfiguration: IndexCapacityConfigurationTypeDef = ...,
        description: str = ...,
        displayName: str = ...,
        documentAttributeConfigurations: Sequence[DocumentAttributeConfigurationTypeDef] = ...,
    ) -> Dict[str, Any]:
        """
        Updates an Amazon Q index.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness.html#QBusiness.Client.update_index)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qbusiness/client/#update_index)
        """

    async def update_plugin(
        self,
        *,
        applicationId: str,
        pluginId: str,
        authConfiguration: PluginAuthConfigurationTypeDef = ...,
        displayName: str = ...,
        serverUrl: str = ...,
        state: PluginStateType = ...,
    ) -> Dict[str, Any]:
        """
        Updates an Amazon Q plugin.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness.html#QBusiness.Client.update_plugin)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qbusiness/client/#update_plugin)
        """

    async def update_retriever(
        self,
        *,
        applicationId: str,
        retrieverId: str,
        configuration: RetrieverConfigurationTypeDef = ...,
        displayName: str = ...,
        roleArn: str = ...,
    ) -> Dict[str, Any]:
        """
        Updates the retriever used for your Amazon Q application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness.html#QBusiness.Client.update_retriever)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qbusiness/client/#update_retriever)
        """

    async def update_user(
        self,
        *,
        applicationId: str,
        userId: str,
        userAliasesToDelete: Sequence[UserAliasTypeDef] = ...,
        userAliasesToUpdate: Sequence[UserAliasTypeDef] = ...,
    ) -> UpdateUserResponseTypeDef:
        """
        Updates a information associated with a user id.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness.html#QBusiness.Client.update_user)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qbusiness/client/#update_user)
        """

    async def update_web_experience(
        self,
        *,
        applicationId: str,
        webExperienceId: str,
        authenticationConfiguration: WebExperienceAuthConfigurationTypeDef = ...,
        samplePromptsControlMode: WebExperienceSamplePromptsControlModeType = ...,
        subtitle: str = ...,
        title: str = ...,
        welcomeMessage: str = ...,
    ) -> Dict[str, Any]:
        """
        Updates an Amazon Q web experience.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness.html#QBusiness.Client.update_web_experience)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qbusiness/client/#update_web_experience)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_chat_controls_configuration"]
    ) -> GetChatControlsConfigurationPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness.html#QBusiness.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qbusiness/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_applications"]
    ) -> ListApplicationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness.html#QBusiness.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qbusiness/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_conversations"]
    ) -> ListConversationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness.html#QBusiness.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qbusiness/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_data_source_sync_jobs"]
    ) -> ListDataSourceSyncJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness.html#QBusiness.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qbusiness/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_data_sources"]
    ) -> ListDataSourcesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness.html#QBusiness.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qbusiness/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_documents"]) -> ListDocumentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness.html#QBusiness.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qbusiness/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_groups"]) -> ListGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness.html#QBusiness.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qbusiness/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_indices"]) -> ListIndicesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness.html#QBusiness.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qbusiness/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_messages"]) -> ListMessagesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness.html#QBusiness.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qbusiness/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_plugins"]) -> ListPluginsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness.html#QBusiness.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qbusiness/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_retrievers"]) -> ListRetrieversPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness.html#QBusiness.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qbusiness/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_web_experiences"]
    ) -> ListWebExperiencesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness.html#QBusiness.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qbusiness/client/#get_paginator)
        """

    async def __aenter__(self) -> "QBusinessClient":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness.html#QBusiness.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qbusiness/client/)
        """

    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> Any:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness.html#QBusiness.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qbusiness/client/)
        """
