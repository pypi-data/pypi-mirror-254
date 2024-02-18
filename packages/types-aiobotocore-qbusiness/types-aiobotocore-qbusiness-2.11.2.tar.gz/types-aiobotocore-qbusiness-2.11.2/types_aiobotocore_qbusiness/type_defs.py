"""
Type annotations for qbusiness service type definitions.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qbusiness/type_defs/)

Usage::

    ```python
    from types_aiobotocore_qbusiness.type_defs import ActionExecutionPayloadFieldPaginatorTypeDef

    data: ActionExecutionPayloadFieldPaginatorTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Mapping, Sequence, Union

from aiobotocore.response import StreamingBody

from .literals import (
    ActionPayloadFieldTypeType,
    ApplicationStatusType,
    AttachmentsControlModeType,
    AttachmentStatusType,
    AttributeTypeType,
    ContentTypeType,
    DataSourceStatusType,
    DataSourceSyncJobStatusType,
    DocumentEnrichmentConditionOperatorType,
    DocumentStatusType,
    ErrorCodeType,
    GroupStatusType,
    IndexStatusType,
    MemberRelationType,
    MembershipTypeType,
    MessageTypeType,
    MessageUsefulnessReasonType,
    MessageUsefulnessType,
    PluginStateType,
    PluginTypeType,
    ReadAccessTypeType,
    ResponseScopeType,
    RetrieverStatusType,
    RetrieverTypeType,
    RuleTypeType,
    StatusType,
    WebExperienceSamplePromptsControlModeType,
    WebExperienceStatusType,
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
    "ActionExecutionPayloadFieldPaginatorTypeDef",
    "ActionExecutionPayloadFieldTypeDef",
    "ActionReviewPayloadFieldAllowedValueTypeDef",
    "ApplicationTypeDef",
    "AppliedAttachmentsConfigurationTypeDef",
    "BlobTypeDef",
    "ErrorDetailTypeDef",
    "AttachmentsConfigurationTypeDef",
    "BasicAuthConfigurationTypeDef",
    "DeleteDocumentTypeDef",
    "ResponseMetadataTypeDef",
    "BlockedPhrasesConfigurationTypeDef",
    "BlockedPhrasesConfigurationUpdateTypeDef",
    "ContentBlockerRuleTypeDef",
    "EligibleDataSourceTypeDef",
    "ConversationTypeDef",
    "EncryptionConfigurationTypeDef",
    "TagTypeDef",
    "DataSourceVpcConfigurationTypeDef",
    "IndexCapacityConfigurationTypeDef",
    "UserAliasTypeDef",
    "DataSourceSyncJobMetricsTypeDef",
    "DataSourceTypeDef",
    "DeleteApplicationRequestRequestTypeDef",
    "DeleteChatControlsConfigurationRequestRequestTypeDef",
    "DeleteConversationRequestRequestTypeDef",
    "DeleteDataSourceRequestRequestTypeDef",
    "DeleteGroupRequestRequestTypeDef",
    "DeleteIndexRequestRequestTypeDef",
    "DeletePluginRequestRequestTypeDef",
    "DeleteRetrieverRequestRequestTypeDef",
    "DeleteUserRequestRequestTypeDef",
    "DeleteWebExperienceRequestRequestTypeDef",
    "DocumentAttributeConfigurationTypeDef",
    "TimestampTypeDef",
    "S3TypeDef",
    "GetApplicationRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "GetChatControlsConfigurationRequestRequestTypeDef",
    "GetDataSourceRequestRequestTypeDef",
    "GetGroupRequestRequestTypeDef",
    "GetIndexRequestRequestTypeDef",
    "GetPluginRequestRequestTypeDef",
    "GetRetrieverRequestRequestTypeDef",
    "GetUserRequestRequestTypeDef",
    "GetWebExperienceRequestRequestTypeDef",
    "MemberGroupTypeDef",
    "MemberUserTypeDef",
    "GroupSummaryTypeDef",
    "TextDocumentStatisticsTypeDef",
    "IndexTypeDef",
    "KendraIndexConfigurationTypeDef",
    "ListApplicationsRequestRequestTypeDef",
    "ListConversationsRequestRequestTypeDef",
    "ListDataSourcesRequestRequestTypeDef",
    "ListDocumentsRequestRequestTypeDef",
    "ListIndicesRequestRequestTypeDef",
    "ListMessagesRequestRequestTypeDef",
    "ListPluginsRequestRequestTypeDef",
    "PluginTypeDef",
    "ListRetrieversRequestRequestTypeDef",
    "RetrieverTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListWebExperiencesRequestRequestTypeDef",
    "WebExperienceTypeDef",
    "NativeIndexConfigurationTypeDef",
    "OAuth2ClientCredentialConfigurationTypeDef",
    "PrincipalGroupTypeDef",
    "PrincipalUserTypeDef",
    "UsersAndGroupsTypeDef",
    "SamlConfigurationTypeDef",
    "TextSegmentTypeDef",
    "StartDataSourceSyncJobRequestRequestTypeDef",
    "StopDataSourceSyncJobRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "ActionExecutionPaginatorTypeDef",
    "ActionExecutionTypeDef",
    "ActionReviewPayloadFieldTypeDef",
    "AttachmentInputTypeDef",
    "AttachmentOutputTypeDef",
    "DocumentDetailsTypeDef",
    "FailedDocumentTypeDef",
    "GroupStatusDetailTypeDef",
    "UpdateApplicationRequestRequestTypeDef",
    "BatchDeleteDocumentRequestRequestTypeDef",
    "CreateApplicationResponseTypeDef",
    "CreateDataSourceResponseTypeDef",
    "CreateIndexResponseTypeDef",
    "CreatePluginResponseTypeDef",
    "CreateRetrieverResponseTypeDef",
    "CreateWebExperienceResponseTypeDef",
    "EmptyResponseMetadataTypeDef",
    "ListApplicationsResponseTypeDef",
    "StartDataSourceSyncJobResponseTypeDef",
    "ContentRetrievalRuleTypeDef",
    "ListConversationsResponseTypeDef",
    "GetApplicationResponseTypeDef",
    "CreateApplicationRequestRequestTypeDef",
    "CreateWebExperienceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "CreateIndexRequestRequestTypeDef",
    "CreateUserRequestRequestTypeDef",
    "GetUserResponseTypeDef",
    "UpdateUserRequestRequestTypeDef",
    "UpdateUserResponseTypeDef",
    "DataSourceSyncJobTypeDef",
    "ListDataSourcesResponseTypeDef",
    "UpdateIndexRequestRequestTypeDef",
    "DocumentAttributeValueTypeDef",
    "ListDataSourceSyncJobsRequestRequestTypeDef",
    "ListGroupsRequestRequestTypeDef",
    "MessageUsefulnessFeedbackTypeDef",
    "DocumentContentTypeDef",
    "GetChatControlsConfigurationRequestGetChatControlsConfigurationPaginateTypeDef",
    "ListApplicationsRequestListApplicationsPaginateTypeDef",
    "ListConversationsRequestListConversationsPaginateTypeDef",
    "ListDataSourceSyncJobsRequestListDataSourceSyncJobsPaginateTypeDef",
    "ListDataSourcesRequestListDataSourcesPaginateTypeDef",
    "ListDocumentsRequestListDocumentsPaginateTypeDef",
    "ListGroupsRequestListGroupsPaginateTypeDef",
    "ListIndicesRequestListIndicesPaginateTypeDef",
    "ListMessagesRequestListMessagesPaginateTypeDef",
    "ListPluginsRequestListPluginsPaginateTypeDef",
    "ListRetrieversRequestListRetrieversPaginateTypeDef",
    "ListWebExperiencesRequestListWebExperiencesPaginateTypeDef",
    "GroupMembersTypeDef",
    "ListGroupsResponseTypeDef",
    "IndexStatisticsTypeDef",
    "ListIndicesResponseTypeDef",
    "ListPluginsResponseTypeDef",
    "ListRetrieversResponseTypeDef",
    "ListWebExperiencesResponseTypeDef",
    "RetrieverConfigurationTypeDef",
    "PluginAuthConfigurationTypeDef",
    "PrincipalTypeDef",
    "WebExperienceAuthConfigurationTypeDef",
    "SourceAttributionTypeDef",
    "ActionReviewTypeDef",
    "ChatSyncInputRequestTypeDef",
    "ListDocumentsResponseTypeDef",
    "BatchDeleteDocumentResponseTypeDef",
    "BatchPutDocumentResponseTypeDef",
    "GetGroupResponseTypeDef",
    "RuleConfigurationTypeDef",
    "ListDataSourceSyncJobsResponseTypeDef",
    "DocumentAttributeConditionTypeDef",
    "DocumentAttributeTargetTypeDef",
    "DocumentAttributeTypeDef",
    "PutFeedbackRequestRequestTypeDef",
    "PutGroupRequestRequestTypeDef",
    "GetIndexResponseTypeDef",
    "CreateRetrieverRequestRequestTypeDef",
    "GetRetrieverResponseTypeDef",
    "UpdateRetrieverRequestRequestTypeDef",
    "CreatePluginRequestRequestTypeDef",
    "GetPluginResponseTypeDef",
    "UpdatePluginRequestRequestTypeDef",
    "AccessControlTypeDef",
    "GetWebExperienceResponseTypeDef",
    "UpdateWebExperienceRequestRequestTypeDef",
    "ChatSyncOutputTypeDef",
    "MessagePaginatorTypeDef",
    "MessageTypeDef",
    "RuleTypeDef",
    "HookConfigurationTypeDef",
    "InlineDocumentEnrichmentConfigurationTypeDef",
    "AttributeFilterTypeDef",
    "AccessConfigurationTypeDef",
    "ListMessagesResponsePaginatorTypeDef",
    "ListMessagesResponseTypeDef",
    "TopicConfigurationTypeDef",
    "DocumentEnrichmentConfigurationTypeDef",
    "GetChatControlsConfigurationResponseTypeDef",
    "UpdateChatControlsConfigurationRequestRequestTypeDef",
    "CreateDataSourceRequestRequestTypeDef",
    "DocumentTypeDef",
    "GetDataSourceResponseTypeDef",
    "UpdateDataSourceRequestRequestTypeDef",
    "BatchPutDocumentRequestRequestTypeDef",
)

ActionExecutionPayloadFieldPaginatorTypeDef = TypedDict(
    "ActionExecutionPayloadFieldPaginatorTypeDef",
    {
        "value": Dict[str, Any],
    },
)
ActionExecutionPayloadFieldTypeDef = TypedDict(
    "ActionExecutionPayloadFieldTypeDef",
    {
        "value": Mapping[str, Any],
    },
)
ActionReviewPayloadFieldAllowedValueTypeDef = TypedDict(
    "ActionReviewPayloadFieldAllowedValueTypeDef",
    {
        "displayValue": NotRequired[Dict[str, Any]],
        "value": NotRequired[Dict[str, Any]],
    },
)
ApplicationTypeDef = TypedDict(
    "ApplicationTypeDef",
    {
        "applicationId": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "displayName": NotRequired[str],
        "status": NotRequired[ApplicationStatusType],
        "updatedAt": NotRequired[datetime],
    },
)
AppliedAttachmentsConfigurationTypeDef = TypedDict(
    "AppliedAttachmentsConfigurationTypeDef",
    {
        "attachmentsControlMode": NotRequired[AttachmentsControlModeType],
    },
)
BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]
ErrorDetailTypeDef = TypedDict(
    "ErrorDetailTypeDef",
    {
        "errorCode": NotRequired[ErrorCodeType],
        "errorMessage": NotRequired[str],
    },
)
AttachmentsConfigurationTypeDef = TypedDict(
    "AttachmentsConfigurationTypeDef",
    {
        "attachmentsControlMode": AttachmentsControlModeType,
    },
)
BasicAuthConfigurationTypeDef = TypedDict(
    "BasicAuthConfigurationTypeDef",
    {
        "roleArn": str,
        "secretArn": str,
    },
)
DeleteDocumentTypeDef = TypedDict(
    "DeleteDocumentTypeDef",
    {
        "documentId": str,
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
BlockedPhrasesConfigurationTypeDef = TypedDict(
    "BlockedPhrasesConfigurationTypeDef",
    {
        "blockedPhrases": NotRequired[List[str]],
        "systemMessageOverride": NotRequired[str],
    },
)
BlockedPhrasesConfigurationUpdateTypeDef = TypedDict(
    "BlockedPhrasesConfigurationUpdateTypeDef",
    {
        "blockedPhrasesToCreateOrUpdate": NotRequired[Sequence[str]],
        "blockedPhrasesToDelete": NotRequired[Sequence[str]],
        "systemMessageOverride": NotRequired[str],
    },
)
ContentBlockerRuleTypeDef = TypedDict(
    "ContentBlockerRuleTypeDef",
    {
        "systemMessageOverride": NotRequired[str],
    },
)
EligibleDataSourceTypeDef = TypedDict(
    "EligibleDataSourceTypeDef",
    {
        "dataSourceId": NotRequired[str],
        "indexId": NotRequired[str],
    },
)
ConversationTypeDef = TypedDict(
    "ConversationTypeDef",
    {
        "conversationId": NotRequired[str],
        "startTime": NotRequired[datetime],
        "title": NotRequired[str],
    },
)
EncryptionConfigurationTypeDef = TypedDict(
    "EncryptionConfigurationTypeDef",
    {
        "kmsKeyId": NotRequired[str],
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "key": str,
        "value": str,
    },
)
DataSourceVpcConfigurationTypeDef = TypedDict(
    "DataSourceVpcConfigurationTypeDef",
    {
        "securityGroupIds": Sequence[str],
        "subnetIds": Sequence[str],
    },
)
IndexCapacityConfigurationTypeDef = TypedDict(
    "IndexCapacityConfigurationTypeDef",
    {
        "units": NotRequired[int],
    },
)
UserAliasTypeDef = TypedDict(
    "UserAliasTypeDef",
    {
        "userId": str,
        "dataSourceId": NotRequired[str],
        "indexId": NotRequired[str],
    },
)
DataSourceSyncJobMetricsTypeDef = TypedDict(
    "DataSourceSyncJobMetricsTypeDef",
    {
        "documentsAdded": NotRequired[str],
        "documentsDeleted": NotRequired[str],
        "documentsFailed": NotRequired[str],
        "documentsModified": NotRequired[str],
        "documentsScanned": NotRequired[str],
    },
)
DataSourceTypeDef = TypedDict(
    "DataSourceTypeDef",
    {
        "createdAt": NotRequired[datetime],
        "dataSourceId": NotRequired[str],
        "displayName": NotRequired[str],
        "status": NotRequired[DataSourceStatusType],
        "type": NotRequired[str],
        "updatedAt": NotRequired[datetime],
    },
)
DeleteApplicationRequestRequestTypeDef = TypedDict(
    "DeleteApplicationRequestRequestTypeDef",
    {
        "applicationId": str,
    },
)
DeleteChatControlsConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteChatControlsConfigurationRequestRequestTypeDef",
    {
        "applicationId": str,
    },
)
DeleteConversationRequestRequestTypeDef = TypedDict(
    "DeleteConversationRequestRequestTypeDef",
    {
        "applicationId": str,
        "conversationId": str,
        "userId": str,
    },
)
DeleteDataSourceRequestRequestTypeDef = TypedDict(
    "DeleteDataSourceRequestRequestTypeDef",
    {
        "applicationId": str,
        "dataSourceId": str,
        "indexId": str,
    },
)
DeleteGroupRequestRequestTypeDef = TypedDict(
    "DeleteGroupRequestRequestTypeDef",
    {
        "applicationId": str,
        "groupName": str,
        "indexId": str,
        "dataSourceId": NotRequired[str],
    },
)
DeleteIndexRequestRequestTypeDef = TypedDict(
    "DeleteIndexRequestRequestTypeDef",
    {
        "applicationId": str,
        "indexId": str,
    },
)
DeletePluginRequestRequestTypeDef = TypedDict(
    "DeletePluginRequestRequestTypeDef",
    {
        "applicationId": str,
        "pluginId": str,
    },
)
DeleteRetrieverRequestRequestTypeDef = TypedDict(
    "DeleteRetrieverRequestRequestTypeDef",
    {
        "applicationId": str,
        "retrieverId": str,
    },
)
DeleteUserRequestRequestTypeDef = TypedDict(
    "DeleteUserRequestRequestTypeDef",
    {
        "applicationId": str,
        "userId": str,
    },
)
DeleteWebExperienceRequestRequestTypeDef = TypedDict(
    "DeleteWebExperienceRequestRequestTypeDef",
    {
        "applicationId": str,
        "webExperienceId": str,
    },
)
DocumentAttributeConfigurationTypeDef = TypedDict(
    "DocumentAttributeConfigurationTypeDef",
    {
        "name": NotRequired[str],
        "search": NotRequired[StatusType],
        "type": NotRequired[AttributeTypeType],
    },
)
TimestampTypeDef = Union[datetime, str]
S3TypeDef = TypedDict(
    "S3TypeDef",
    {
        "bucket": str,
        "key": str,
    },
)
GetApplicationRequestRequestTypeDef = TypedDict(
    "GetApplicationRequestRequestTypeDef",
    {
        "applicationId": str,
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
GetChatControlsConfigurationRequestRequestTypeDef = TypedDict(
    "GetChatControlsConfigurationRequestRequestTypeDef",
    {
        "applicationId": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
GetDataSourceRequestRequestTypeDef = TypedDict(
    "GetDataSourceRequestRequestTypeDef",
    {
        "applicationId": str,
        "dataSourceId": str,
        "indexId": str,
    },
)
GetGroupRequestRequestTypeDef = TypedDict(
    "GetGroupRequestRequestTypeDef",
    {
        "applicationId": str,
        "groupName": str,
        "indexId": str,
        "dataSourceId": NotRequired[str],
    },
)
GetIndexRequestRequestTypeDef = TypedDict(
    "GetIndexRequestRequestTypeDef",
    {
        "applicationId": str,
        "indexId": str,
    },
)
GetPluginRequestRequestTypeDef = TypedDict(
    "GetPluginRequestRequestTypeDef",
    {
        "applicationId": str,
        "pluginId": str,
    },
)
GetRetrieverRequestRequestTypeDef = TypedDict(
    "GetRetrieverRequestRequestTypeDef",
    {
        "applicationId": str,
        "retrieverId": str,
    },
)
GetUserRequestRequestTypeDef = TypedDict(
    "GetUserRequestRequestTypeDef",
    {
        "applicationId": str,
        "userId": str,
    },
)
GetWebExperienceRequestRequestTypeDef = TypedDict(
    "GetWebExperienceRequestRequestTypeDef",
    {
        "applicationId": str,
        "webExperienceId": str,
    },
)
MemberGroupTypeDef = TypedDict(
    "MemberGroupTypeDef",
    {
        "groupName": str,
        "type": NotRequired[MembershipTypeType],
    },
)
MemberUserTypeDef = TypedDict(
    "MemberUserTypeDef",
    {
        "userId": str,
        "type": NotRequired[MembershipTypeType],
    },
)
GroupSummaryTypeDef = TypedDict(
    "GroupSummaryTypeDef",
    {
        "groupName": NotRequired[str],
    },
)
TextDocumentStatisticsTypeDef = TypedDict(
    "TextDocumentStatisticsTypeDef",
    {
        "indexedTextBytes": NotRequired[int],
        "indexedTextDocumentCount": NotRequired[int],
    },
)
IndexTypeDef = TypedDict(
    "IndexTypeDef",
    {
        "createdAt": NotRequired[datetime],
        "displayName": NotRequired[str],
        "indexId": NotRequired[str],
        "status": NotRequired[IndexStatusType],
        "updatedAt": NotRequired[datetime],
    },
)
KendraIndexConfigurationTypeDef = TypedDict(
    "KendraIndexConfigurationTypeDef",
    {
        "indexId": str,
    },
)
ListApplicationsRequestRequestTypeDef = TypedDict(
    "ListApplicationsRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListConversationsRequestRequestTypeDef = TypedDict(
    "ListConversationsRequestRequestTypeDef",
    {
        "applicationId": str,
        "userId": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListDataSourcesRequestRequestTypeDef = TypedDict(
    "ListDataSourcesRequestRequestTypeDef",
    {
        "applicationId": str,
        "indexId": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListDocumentsRequestRequestTypeDef = TypedDict(
    "ListDocumentsRequestRequestTypeDef",
    {
        "applicationId": str,
        "indexId": str,
        "dataSourceIds": NotRequired[Sequence[str]],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListIndicesRequestRequestTypeDef = TypedDict(
    "ListIndicesRequestRequestTypeDef",
    {
        "applicationId": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListMessagesRequestRequestTypeDef = TypedDict(
    "ListMessagesRequestRequestTypeDef",
    {
        "applicationId": str,
        "conversationId": str,
        "userId": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListPluginsRequestRequestTypeDef = TypedDict(
    "ListPluginsRequestRequestTypeDef",
    {
        "applicationId": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
PluginTypeDef = TypedDict(
    "PluginTypeDef",
    {
        "createdAt": NotRequired[datetime],
        "displayName": NotRequired[str],
        "pluginId": NotRequired[str],
        "serverUrl": NotRequired[str],
        "state": NotRequired[PluginStateType],
        "type": NotRequired[PluginTypeType],
        "updatedAt": NotRequired[datetime],
    },
)
ListRetrieversRequestRequestTypeDef = TypedDict(
    "ListRetrieversRequestRequestTypeDef",
    {
        "applicationId": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
RetrieverTypeDef = TypedDict(
    "RetrieverTypeDef",
    {
        "applicationId": NotRequired[str],
        "displayName": NotRequired[str],
        "retrieverId": NotRequired[str],
        "status": NotRequired[RetrieverStatusType],
        "type": NotRequired[RetrieverTypeType],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceARN": str,
    },
)
ListWebExperiencesRequestRequestTypeDef = TypedDict(
    "ListWebExperiencesRequestRequestTypeDef",
    {
        "applicationId": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
WebExperienceTypeDef = TypedDict(
    "WebExperienceTypeDef",
    {
        "createdAt": NotRequired[datetime],
        "defaultEndpoint": NotRequired[str],
        "status": NotRequired[WebExperienceStatusType],
        "updatedAt": NotRequired[datetime],
        "webExperienceId": NotRequired[str],
    },
)
NativeIndexConfigurationTypeDef = TypedDict(
    "NativeIndexConfigurationTypeDef",
    {
        "indexId": str,
    },
)
OAuth2ClientCredentialConfigurationTypeDef = TypedDict(
    "OAuth2ClientCredentialConfigurationTypeDef",
    {
        "roleArn": str,
        "secretArn": str,
    },
)
PrincipalGroupTypeDef = TypedDict(
    "PrincipalGroupTypeDef",
    {
        "access": ReadAccessTypeType,
        "membershipType": NotRequired[MembershipTypeType],
        "name": NotRequired[str],
    },
)
PrincipalUserTypeDef = TypedDict(
    "PrincipalUserTypeDef",
    {
        "access": ReadAccessTypeType,
        "id": NotRequired[str],
        "membershipType": NotRequired[MembershipTypeType],
    },
)
UsersAndGroupsTypeDef = TypedDict(
    "UsersAndGroupsTypeDef",
    {
        "userGroups": NotRequired[List[str]],
        "userIds": NotRequired[List[str]],
    },
)
SamlConfigurationTypeDef = TypedDict(
    "SamlConfigurationTypeDef",
    {
        "metadataXML": str,
        "roleArn": str,
        "userIdAttribute": str,
        "userGroupAttribute": NotRequired[str],
    },
)
TextSegmentTypeDef = TypedDict(
    "TextSegmentTypeDef",
    {
        "beginOffset": NotRequired[int],
        "endOffset": NotRequired[int],
    },
)
StartDataSourceSyncJobRequestRequestTypeDef = TypedDict(
    "StartDataSourceSyncJobRequestRequestTypeDef",
    {
        "applicationId": str,
        "dataSourceId": str,
        "indexId": str,
    },
)
StopDataSourceSyncJobRequestRequestTypeDef = TypedDict(
    "StopDataSourceSyncJobRequestRequestTypeDef",
    {
        "applicationId": str,
        "dataSourceId": str,
        "indexId": str,
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceARN": str,
        "tagKeys": Sequence[str],
    },
)
ActionExecutionPaginatorTypeDef = TypedDict(
    "ActionExecutionPaginatorTypeDef",
    {
        "payload": Dict[str, ActionExecutionPayloadFieldPaginatorTypeDef],
        "payloadFieldNameSeparator": str,
        "pluginId": str,
    },
)
ActionExecutionTypeDef = TypedDict(
    "ActionExecutionTypeDef",
    {
        "payload": Mapping[str, ActionExecutionPayloadFieldTypeDef],
        "payloadFieldNameSeparator": str,
        "pluginId": str,
    },
)
ActionReviewPayloadFieldTypeDef = TypedDict(
    "ActionReviewPayloadFieldTypeDef",
    {
        "allowedValues": NotRequired[List[ActionReviewPayloadFieldAllowedValueTypeDef]],
        "displayName": NotRequired[str],
        "displayOrder": NotRequired[int],
        "required": NotRequired[bool],
        "type": NotRequired[ActionPayloadFieldTypeType],
        "value": NotRequired[Dict[str, Any]],
    },
)
AttachmentInputTypeDef = TypedDict(
    "AttachmentInputTypeDef",
    {
        "data": BlobTypeDef,
        "name": str,
    },
)
AttachmentOutputTypeDef = TypedDict(
    "AttachmentOutputTypeDef",
    {
        "error": NotRequired[ErrorDetailTypeDef],
        "name": NotRequired[str],
        "status": NotRequired[AttachmentStatusType],
    },
)
DocumentDetailsTypeDef = TypedDict(
    "DocumentDetailsTypeDef",
    {
        "createdAt": NotRequired[datetime],
        "documentId": NotRequired[str],
        "error": NotRequired[ErrorDetailTypeDef],
        "status": NotRequired[DocumentStatusType],
        "updatedAt": NotRequired[datetime],
    },
)
FailedDocumentTypeDef = TypedDict(
    "FailedDocumentTypeDef",
    {
        "dataSourceId": NotRequired[str],
        "error": NotRequired[ErrorDetailTypeDef],
        "id": NotRequired[str],
    },
)
GroupStatusDetailTypeDef = TypedDict(
    "GroupStatusDetailTypeDef",
    {
        "errorDetail": NotRequired[ErrorDetailTypeDef],
        "lastUpdatedAt": NotRequired[datetime],
        "status": NotRequired[GroupStatusType],
    },
)
UpdateApplicationRequestRequestTypeDef = TypedDict(
    "UpdateApplicationRequestRequestTypeDef",
    {
        "applicationId": str,
        "attachmentsConfiguration": NotRequired[AttachmentsConfigurationTypeDef],
        "description": NotRequired[str],
        "displayName": NotRequired[str],
        "roleArn": NotRequired[str],
    },
)
BatchDeleteDocumentRequestRequestTypeDef = TypedDict(
    "BatchDeleteDocumentRequestRequestTypeDef",
    {
        "applicationId": str,
        "documents": Sequence[DeleteDocumentTypeDef],
        "indexId": str,
        "dataSourceSyncId": NotRequired[str],
    },
)
CreateApplicationResponseTypeDef = TypedDict(
    "CreateApplicationResponseTypeDef",
    {
        "applicationArn": str,
        "applicationId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDataSourceResponseTypeDef = TypedDict(
    "CreateDataSourceResponseTypeDef",
    {
        "dataSourceArn": str,
        "dataSourceId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateIndexResponseTypeDef = TypedDict(
    "CreateIndexResponseTypeDef",
    {
        "indexArn": str,
        "indexId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreatePluginResponseTypeDef = TypedDict(
    "CreatePluginResponseTypeDef",
    {
        "pluginArn": str,
        "pluginId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateRetrieverResponseTypeDef = TypedDict(
    "CreateRetrieverResponseTypeDef",
    {
        "retrieverArn": str,
        "retrieverId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateWebExperienceResponseTypeDef = TypedDict(
    "CreateWebExperienceResponseTypeDef",
    {
        "webExperienceArn": str,
        "webExperienceId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListApplicationsResponseTypeDef = TypedDict(
    "ListApplicationsResponseTypeDef",
    {
        "applications": List[ApplicationTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartDataSourceSyncJobResponseTypeDef = TypedDict(
    "StartDataSourceSyncJobResponseTypeDef",
    {
        "executionId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ContentRetrievalRuleTypeDef = TypedDict(
    "ContentRetrievalRuleTypeDef",
    {
        "eligibleDataSources": NotRequired[List[EligibleDataSourceTypeDef]],
    },
)
ListConversationsResponseTypeDef = TypedDict(
    "ListConversationsResponseTypeDef",
    {
        "conversations": List[ConversationTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetApplicationResponseTypeDef = TypedDict(
    "GetApplicationResponseTypeDef",
    {
        "applicationArn": str,
        "applicationId": str,
        "attachmentsConfiguration": AppliedAttachmentsConfigurationTypeDef,
        "createdAt": datetime,
        "description": str,
        "displayName": str,
        "encryptionConfiguration": EncryptionConfigurationTypeDef,
        "error": ErrorDetailTypeDef,
        "roleArn": str,
        "status": ApplicationStatusType,
        "updatedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateApplicationRequestRequestTypeDef = TypedDict(
    "CreateApplicationRequestRequestTypeDef",
    {
        "displayName": str,
        "roleArn": str,
        "attachmentsConfiguration": NotRequired[AttachmentsConfigurationTypeDef],
        "clientToken": NotRequired[str],
        "description": NotRequired[str],
        "encryptionConfiguration": NotRequired[EncryptionConfigurationTypeDef],
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateWebExperienceRequestRequestTypeDef = TypedDict(
    "CreateWebExperienceRequestRequestTypeDef",
    {
        "applicationId": str,
        "clientToken": NotRequired[str],
        "samplePromptsControlMode": NotRequired[WebExperienceSamplePromptsControlModeType],
        "subtitle": NotRequired[str],
        "tags": NotRequired[Sequence[TagTypeDef]],
        "title": NotRequired[str],
        "welcomeMessage": NotRequired[str],
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceARN": str,
        "tags": Sequence[TagTypeDef],
    },
)
CreateIndexRequestRequestTypeDef = TypedDict(
    "CreateIndexRequestRequestTypeDef",
    {
        "applicationId": str,
        "displayName": str,
        "capacityConfiguration": NotRequired[IndexCapacityConfigurationTypeDef],
        "clientToken": NotRequired[str],
        "description": NotRequired[str],
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateUserRequestRequestTypeDef = TypedDict(
    "CreateUserRequestRequestTypeDef",
    {
        "applicationId": str,
        "userId": str,
        "clientToken": NotRequired[str],
        "userAliases": NotRequired[Sequence[UserAliasTypeDef]],
    },
)
GetUserResponseTypeDef = TypedDict(
    "GetUserResponseTypeDef",
    {
        "userAliases": List[UserAliasTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateUserRequestRequestTypeDef = TypedDict(
    "UpdateUserRequestRequestTypeDef",
    {
        "applicationId": str,
        "userId": str,
        "userAliasesToDelete": NotRequired[Sequence[UserAliasTypeDef]],
        "userAliasesToUpdate": NotRequired[Sequence[UserAliasTypeDef]],
    },
)
UpdateUserResponseTypeDef = TypedDict(
    "UpdateUserResponseTypeDef",
    {
        "userAliasesAdded": List[UserAliasTypeDef],
        "userAliasesDeleted": List[UserAliasTypeDef],
        "userAliasesUpdated": List[UserAliasTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DataSourceSyncJobTypeDef = TypedDict(
    "DataSourceSyncJobTypeDef",
    {
        "dataSourceErrorCode": NotRequired[str],
        "endTime": NotRequired[datetime],
        "error": NotRequired[ErrorDetailTypeDef],
        "executionId": NotRequired[str],
        "metrics": NotRequired[DataSourceSyncJobMetricsTypeDef],
        "startTime": NotRequired[datetime],
        "status": NotRequired[DataSourceSyncJobStatusType],
    },
)
ListDataSourcesResponseTypeDef = TypedDict(
    "ListDataSourcesResponseTypeDef",
    {
        "dataSources": List[DataSourceTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateIndexRequestRequestTypeDef = TypedDict(
    "UpdateIndexRequestRequestTypeDef",
    {
        "applicationId": str,
        "indexId": str,
        "capacityConfiguration": NotRequired[IndexCapacityConfigurationTypeDef],
        "description": NotRequired[str],
        "displayName": NotRequired[str],
        "documentAttributeConfigurations": NotRequired[
            Sequence[DocumentAttributeConfigurationTypeDef]
        ],
    },
)
DocumentAttributeValueTypeDef = TypedDict(
    "DocumentAttributeValueTypeDef",
    {
        "dateValue": NotRequired[TimestampTypeDef],
        "longValue": NotRequired[int],
        "stringListValue": NotRequired[Sequence[str]],
        "stringValue": NotRequired[str],
    },
)
ListDataSourceSyncJobsRequestRequestTypeDef = TypedDict(
    "ListDataSourceSyncJobsRequestRequestTypeDef",
    {
        "applicationId": str,
        "dataSourceId": str,
        "indexId": str,
        "endTime": NotRequired[TimestampTypeDef],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "startTime": NotRequired[TimestampTypeDef],
        "statusFilter": NotRequired[DataSourceSyncJobStatusType],
    },
)
ListGroupsRequestRequestTypeDef = TypedDict(
    "ListGroupsRequestRequestTypeDef",
    {
        "applicationId": str,
        "indexId": str,
        "updatedEarlierThan": TimestampTypeDef,
        "dataSourceId": NotRequired[str],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
MessageUsefulnessFeedbackTypeDef = TypedDict(
    "MessageUsefulnessFeedbackTypeDef",
    {
        "submittedAt": TimestampTypeDef,
        "usefulness": MessageUsefulnessType,
        "comment": NotRequired[str],
        "reason": NotRequired[MessageUsefulnessReasonType],
    },
)
DocumentContentTypeDef = TypedDict(
    "DocumentContentTypeDef",
    {
        "blob": NotRequired[BlobTypeDef],
        "s3": NotRequired[S3TypeDef],
    },
)
GetChatControlsConfigurationRequestGetChatControlsConfigurationPaginateTypeDef = TypedDict(
    "GetChatControlsConfigurationRequestGetChatControlsConfigurationPaginateTypeDef",
    {
        "applicationId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListApplicationsRequestListApplicationsPaginateTypeDef = TypedDict(
    "ListApplicationsRequestListApplicationsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListConversationsRequestListConversationsPaginateTypeDef = TypedDict(
    "ListConversationsRequestListConversationsPaginateTypeDef",
    {
        "applicationId": str,
        "userId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDataSourceSyncJobsRequestListDataSourceSyncJobsPaginateTypeDef = TypedDict(
    "ListDataSourceSyncJobsRequestListDataSourceSyncJobsPaginateTypeDef",
    {
        "applicationId": str,
        "dataSourceId": str,
        "indexId": str,
        "endTime": NotRequired[TimestampTypeDef],
        "startTime": NotRequired[TimestampTypeDef],
        "statusFilter": NotRequired[DataSourceSyncJobStatusType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDataSourcesRequestListDataSourcesPaginateTypeDef = TypedDict(
    "ListDataSourcesRequestListDataSourcesPaginateTypeDef",
    {
        "applicationId": str,
        "indexId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDocumentsRequestListDocumentsPaginateTypeDef = TypedDict(
    "ListDocumentsRequestListDocumentsPaginateTypeDef",
    {
        "applicationId": str,
        "indexId": str,
        "dataSourceIds": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListGroupsRequestListGroupsPaginateTypeDef = TypedDict(
    "ListGroupsRequestListGroupsPaginateTypeDef",
    {
        "applicationId": str,
        "indexId": str,
        "updatedEarlierThan": TimestampTypeDef,
        "dataSourceId": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListIndicesRequestListIndicesPaginateTypeDef = TypedDict(
    "ListIndicesRequestListIndicesPaginateTypeDef",
    {
        "applicationId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListMessagesRequestListMessagesPaginateTypeDef = TypedDict(
    "ListMessagesRequestListMessagesPaginateTypeDef",
    {
        "applicationId": str,
        "conversationId": str,
        "userId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListPluginsRequestListPluginsPaginateTypeDef = TypedDict(
    "ListPluginsRequestListPluginsPaginateTypeDef",
    {
        "applicationId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListRetrieversRequestListRetrieversPaginateTypeDef = TypedDict(
    "ListRetrieversRequestListRetrieversPaginateTypeDef",
    {
        "applicationId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListWebExperiencesRequestListWebExperiencesPaginateTypeDef = TypedDict(
    "ListWebExperiencesRequestListWebExperiencesPaginateTypeDef",
    {
        "applicationId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GroupMembersTypeDef = TypedDict(
    "GroupMembersTypeDef",
    {
        "memberGroups": NotRequired[Sequence[MemberGroupTypeDef]],
        "memberUsers": NotRequired[Sequence[MemberUserTypeDef]],
    },
)
ListGroupsResponseTypeDef = TypedDict(
    "ListGroupsResponseTypeDef",
    {
        "items": List[GroupSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
IndexStatisticsTypeDef = TypedDict(
    "IndexStatisticsTypeDef",
    {
        "textDocumentStatistics": NotRequired[TextDocumentStatisticsTypeDef],
    },
)
ListIndicesResponseTypeDef = TypedDict(
    "ListIndicesResponseTypeDef",
    {
        "indices": List[IndexTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListPluginsResponseTypeDef = TypedDict(
    "ListPluginsResponseTypeDef",
    {
        "nextToken": str,
        "plugins": List[PluginTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListRetrieversResponseTypeDef = TypedDict(
    "ListRetrieversResponseTypeDef",
    {
        "nextToken": str,
        "retrievers": List[RetrieverTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListWebExperiencesResponseTypeDef = TypedDict(
    "ListWebExperiencesResponseTypeDef",
    {
        "nextToken": str,
        "webExperiences": List[WebExperienceTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RetrieverConfigurationTypeDef = TypedDict(
    "RetrieverConfigurationTypeDef",
    {
        "kendraIndexConfiguration": NotRequired[KendraIndexConfigurationTypeDef],
        "nativeIndexConfiguration": NotRequired[NativeIndexConfigurationTypeDef],
    },
)
PluginAuthConfigurationTypeDef = TypedDict(
    "PluginAuthConfigurationTypeDef",
    {
        "basicAuthConfiguration": NotRequired[BasicAuthConfigurationTypeDef],
        "oAuth2ClientCredentialConfiguration": NotRequired[
            OAuth2ClientCredentialConfigurationTypeDef
        ],
    },
)
PrincipalTypeDef = TypedDict(
    "PrincipalTypeDef",
    {
        "group": NotRequired[PrincipalGroupTypeDef],
        "user": NotRequired[PrincipalUserTypeDef],
    },
)
WebExperienceAuthConfigurationTypeDef = TypedDict(
    "WebExperienceAuthConfigurationTypeDef",
    {
        "samlConfiguration": NotRequired[SamlConfigurationTypeDef],
    },
)
SourceAttributionTypeDef = TypedDict(
    "SourceAttributionTypeDef",
    {
        "citationNumber": NotRequired[int],
        "snippet": NotRequired[str],
        "textMessageSegments": NotRequired[List[TextSegmentTypeDef]],
        "title": NotRequired[str],
        "updatedAt": NotRequired[datetime],
        "url": NotRequired[str],
    },
)
ActionReviewTypeDef = TypedDict(
    "ActionReviewTypeDef",
    {
        "payload": NotRequired[Dict[str, ActionReviewPayloadFieldTypeDef]],
        "payloadFieldNameSeparator": NotRequired[str],
        "pluginId": NotRequired[str],
        "pluginType": NotRequired[PluginTypeType],
    },
)
ChatSyncInputRequestTypeDef = TypedDict(
    "ChatSyncInputRequestTypeDef",
    {
        "applicationId": str,
        "userId": str,
        "actionExecution": NotRequired[ActionExecutionTypeDef],
        "attachments": NotRequired[Sequence[AttachmentInputTypeDef]],
        "attributeFilter": NotRequired["AttributeFilterTypeDef"],
        "clientToken": NotRequired[str],
        "conversationId": NotRequired[str],
        "parentMessageId": NotRequired[str],
        "userGroups": NotRequired[Sequence[str]],
        "userMessage": NotRequired[str],
    },
)
ListDocumentsResponseTypeDef = TypedDict(
    "ListDocumentsResponseTypeDef",
    {
        "documentDetailList": List[DocumentDetailsTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchDeleteDocumentResponseTypeDef = TypedDict(
    "BatchDeleteDocumentResponseTypeDef",
    {
        "failedDocuments": List[FailedDocumentTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchPutDocumentResponseTypeDef = TypedDict(
    "BatchPutDocumentResponseTypeDef",
    {
        "failedDocuments": List[FailedDocumentTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetGroupResponseTypeDef = TypedDict(
    "GetGroupResponseTypeDef",
    {
        "status": GroupStatusDetailTypeDef,
        "statusHistory": List[GroupStatusDetailTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RuleConfigurationTypeDef = TypedDict(
    "RuleConfigurationTypeDef",
    {
        "contentBlockerRule": NotRequired[ContentBlockerRuleTypeDef],
        "contentRetrievalRule": NotRequired[ContentRetrievalRuleTypeDef],
    },
)
ListDataSourceSyncJobsResponseTypeDef = TypedDict(
    "ListDataSourceSyncJobsResponseTypeDef",
    {
        "history": List[DataSourceSyncJobTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DocumentAttributeConditionTypeDef = TypedDict(
    "DocumentAttributeConditionTypeDef",
    {
        "key": str,
        "operator": DocumentEnrichmentConditionOperatorType,
        "value": NotRequired[DocumentAttributeValueTypeDef],
    },
)
DocumentAttributeTargetTypeDef = TypedDict(
    "DocumentAttributeTargetTypeDef",
    {
        "key": str,
        "attributeValueOperator": NotRequired[Literal["DELETE"]],
        "value": NotRequired[DocumentAttributeValueTypeDef],
    },
)
DocumentAttributeTypeDef = TypedDict(
    "DocumentAttributeTypeDef",
    {
        "name": str,
        "value": DocumentAttributeValueTypeDef,
    },
)
PutFeedbackRequestRequestTypeDef = TypedDict(
    "PutFeedbackRequestRequestTypeDef",
    {
        "applicationId": str,
        "conversationId": str,
        "messageId": str,
        "userId": str,
        "messageCopiedAt": NotRequired[TimestampTypeDef],
        "messageUsefulness": NotRequired[MessageUsefulnessFeedbackTypeDef],
    },
)
PutGroupRequestRequestTypeDef = TypedDict(
    "PutGroupRequestRequestTypeDef",
    {
        "applicationId": str,
        "groupMembers": GroupMembersTypeDef,
        "groupName": str,
        "indexId": str,
        "type": MembershipTypeType,
        "dataSourceId": NotRequired[str],
    },
)
GetIndexResponseTypeDef = TypedDict(
    "GetIndexResponseTypeDef",
    {
        "applicationId": str,
        "capacityConfiguration": IndexCapacityConfigurationTypeDef,
        "createdAt": datetime,
        "description": str,
        "displayName": str,
        "documentAttributeConfigurations": List[DocumentAttributeConfigurationTypeDef],
        "error": ErrorDetailTypeDef,
        "indexArn": str,
        "indexId": str,
        "indexStatistics": IndexStatisticsTypeDef,
        "status": IndexStatusType,
        "updatedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateRetrieverRequestRequestTypeDef = TypedDict(
    "CreateRetrieverRequestRequestTypeDef",
    {
        "applicationId": str,
        "configuration": RetrieverConfigurationTypeDef,
        "displayName": str,
        "type": RetrieverTypeType,
        "clientToken": NotRequired[str],
        "roleArn": NotRequired[str],
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
GetRetrieverResponseTypeDef = TypedDict(
    "GetRetrieverResponseTypeDef",
    {
        "applicationId": str,
        "configuration": RetrieverConfigurationTypeDef,
        "createdAt": datetime,
        "displayName": str,
        "retrieverArn": str,
        "retrieverId": str,
        "roleArn": str,
        "status": RetrieverStatusType,
        "type": RetrieverTypeType,
        "updatedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateRetrieverRequestRequestTypeDef = TypedDict(
    "UpdateRetrieverRequestRequestTypeDef",
    {
        "applicationId": str,
        "retrieverId": str,
        "configuration": NotRequired[RetrieverConfigurationTypeDef],
        "displayName": NotRequired[str],
        "roleArn": NotRequired[str],
    },
)
CreatePluginRequestRequestTypeDef = TypedDict(
    "CreatePluginRequestRequestTypeDef",
    {
        "applicationId": str,
        "authConfiguration": PluginAuthConfigurationTypeDef,
        "displayName": str,
        "serverUrl": str,
        "type": PluginTypeType,
        "clientToken": NotRequired[str],
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
GetPluginResponseTypeDef = TypedDict(
    "GetPluginResponseTypeDef",
    {
        "applicationId": str,
        "authConfiguration": PluginAuthConfigurationTypeDef,
        "createdAt": datetime,
        "displayName": str,
        "pluginArn": str,
        "pluginId": str,
        "serverUrl": str,
        "state": PluginStateType,
        "type": PluginTypeType,
        "updatedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdatePluginRequestRequestTypeDef = TypedDict(
    "UpdatePluginRequestRequestTypeDef",
    {
        "applicationId": str,
        "pluginId": str,
        "authConfiguration": NotRequired[PluginAuthConfigurationTypeDef],
        "displayName": NotRequired[str],
        "serverUrl": NotRequired[str],
        "state": NotRequired[PluginStateType],
    },
)
AccessControlTypeDef = TypedDict(
    "AccessControlTypeDef",
    {
        "principals": Sequence[PrincipalTypeDef],
        "memberRelation": NotRequired[MemberRelationType],
    },
)
GetWebExperienceResponseTypeDef = TypedDict(
    "GetWebExperienceResponseTypeDef",
    {
        "applicationId": str,
        "authenticationConfiguration": WebExperienceAuthConfigurationTypeDef,
        "createdAt": datetime,
        "defaultEndpoint": str,
        "error": ErrorDetailTypeDef,
        "samplePromptsControlMode": WebExperienceSamplePromptsControlModeType,
        "status": WebExperienceStatusType,
        "subtitle": str,
        "title": str,
        "updatedAt": datetime,
        "webExperienceArn": str,
        "webExperienceId": str,
        "welcomeMessage": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateWebExperienceRequestRequestTypeDef = TypedDict(
    "UpdateWebExperienceRequestRequestTypeDef",
    {
        "applicationId": str,
        "webExperienceId": str,
        "authenticationConfiguration": NotRequired[WebExperienceAuthConfigurationTypeDef],
        "samplePromptsControlMode": NotRequired[WebExperienceSamplePromptsControlModeType],
        "subtitle": NotRequired[str],
        "title": NotRequired[str],
        "welcomeMessage": NotRequired[str],
    },
)
ChatSyncOutputTypeDef = TypedDict(
    "ChatSyncOutputTypeDef",
    {
        "actionReview": ActionReviewTypeDef,
        "conversationId": str,
        "failedAttachments": List[AttachmentOutputTypeDef],
        "sourceAttributions": List[SourceAttributionTypeDef],
        "systemMessage": str,
        "systemMessageId": str,
        "userMessageId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
MessagePaginatorTypeDef = TypedDict(
    "MessagePaginatorTypeDef",
    {
        "actionExecution": NotRequired[ActionExecutionPaginatorTypeDef],
        "actionReview": NotRequired[ActionReviewTypeDef],
        "attachments": NotRequired[List[AttachmentOutputTypeDef]],
        "body": NotRequired[str],
        "messageId": NotRequired[str],
        "sourceAttribution": NotRequired[List[SourceAttributionTypeDef]],
        "time": NotRequired[datetime],
        "type": NotRequired[MessageTypeType],
    },
)
MessageTypeDef = TypedDict(
    "MessageTypeDef",
    {
        "actionExecution": NotRequired[ActionExecutionTypeDef],
        "actionReview": NotRequired[ActionReviewTypeDef],
        "attachments": NotRequired[List[AttachmentOutputTypeDef]],
        "body": NotRequired[str],
        "messageId": NotRequired[str],
        "sourceAttribution": NotRequired[List[SourceAttributionTypeDef]],
        "time": NotRequired[datetime],
        "type": NotRequired[MessageTypeType],
    },
)
RuleTypeDef = TypedDict(
    "RuleTypeDef",
    {
        "ruleType": RuleTypeType,
        "excludedUsersAndGroups": NotRequired[UsersAndGroupsTypeDef],
        "includedUsersAndGroups": NotRequired[UsersAndGroupsTypeDef],
        "ruleConfiguration": NotRequired[RuleConfigurationTypeDef],
    },
)
HookConfigurationTypeDef = TypedDict(
    "HookConfigurationTypeDef",
    {
        "invocationCondition": NotRequired[DocumentAttributeConditionTypeDef],
        "lambdaArn": NotRequired[str],
        "roleArn": NotRequired[str],
        "s3BucketName": NotRequired[str],
    },
)
InlineDocumentEnrichmentConfigurationTypeDef = TypedDict(
    "InlineDocumentEnrichmentConfigurationTypeDef",
    {
        "condition": NotRequired[DocumentAttributeConditionTypeDef],
        "documentContentOperator": NotRequired[Literal["DELETE"]],
        "target": NotRequired[DocumentAttributeTargetTypeDef],
    },
)
AttributeFilterTypeDef = TypedDict(
    "AttributeFilterTypeDef",
    {
        "andAllFilters": NotRequired[Sequence[Dict[str, Any]]],
        "containsAll": NotRequired[DocumentAttributeTypeDef],
        "containsAny": NotRequired[DocumentAttributeTypeDef],
        "equalsTo": NotRequired[DocumentAttributeTypeDef],
        "greaterThan": NotRequired[DocumentAttributeTypeDef],
        "greaterThanOrEquals": NotRequired[DocumentAttributeTypeDef],
        "lessThan": NotRequired[DocumentAttributeTypeDef],
        "lessThanOrEquals": NotRequired[DocumentAttributeTypeDef],
        "notFilter": NotRequired[Dict[str, Any]],
        "orAllFilters": NotRequired[Sequence[Dict[str, Any]]],
    },
)
AccessConfigurationTypeDef = TypedDict(
    "AccessConfigurationTypeDef",
    {
        "accessControls": Sequence[AccessControlTypeDef],
        "memberRelation": NotRequired[MemberRelationType],
    },
)
ListMessagesResponsePaginatorTypeDef = TypedDict(
    "ListMessagesResponsePaginatorTypeDef",
    {
        "messages": List[MessagePaginatorTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListMessagesResponseTypeDef = TypedDict(
    "ListMessagesResponseTypeDef",
    {
        "messages": List[MessageTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TopicConfigurationTypeDef = TypedDict(
    "TopicConfigurationTypeDef",
    {
        "name": str,
        "rules": List[RuleTypeDef],
        "description": NotRequired[str],
        "exampleChatMessages": NotRequired[List[str]],
    },
)
DocumentEnrichmentConfigurationTypeDef = TypedDict(
    "DocumentEnrichmentConfigurationTypeDef",
    {
        "inlineConfigurations": NotRequired[Sequence[InlineDocumentEnrichmentConfigurationTypeDef]],
        "postExtractionHookConfiguration": NotRequired[HookConfigurationTypeDef],
        "preExtractionHookConfiguration": NotRequired[HookConfigurationTypeDef],
    },
)
GetChatControlsConfigurationResponseTypeDef = TypedDict(
    "GetChatControlsConfigurationResponseTypeDef",
    {
        "blockedPhrases": BlockedPhrasesConfigurationTypeDef,
        "nextToken": str,
        "responseScope": ResponseScopeType,
        "topicConfigurations": List[TopicConfigurationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateChatControlsConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateChatControlsConfigurationRequestRequestTypeDef",
    {
        "applicationId": str,
        "blockedPhrasesConfigurationUpdate": NotRequired[BlockedPhrasesConfigurationUpdateTypeDef],
        "clientToken": NotRequired[str],
        "responseScope": NotRequired[ResponseScopeType],
        "topicConfigurationsToCreateOrUpdate": NotRequired[Sequence[TopicConfigurationTypeDef]],
        "topicConfigurationsToDelete": NotRequired[Sequence[TopicConfigurationTypeDef]],
    },
)
CreateDataSourceRequestRequestTypeDef = TypedDict(
    "CreateDataSourceRequestRequestTypeDef",
    {
        "applicationId": str,
        "configuration": Mapping[str, Any],
        "displayName": str,
        "indexId": str,
        "clientToken": NotRequired[str],
        "description": NotRequired[str],
        "documentEnrichmentConfiguration": NotRequired[DocumentEnrichmentConfigurationTypeDef],
        "roleArn": NotRequired[str],
        "syncSchedule": NotRequired[str],
        "tags": NotRequired[Sequence[TagTypeDef]],
        "vpcConfiguration": NotRequired[DataSourceVpcConfigurationTypeDef],
    },
)
DocumentTypeDef = TypedDict(
    "DocumentTypeDef",
    {
        "id": str,
        "accessConfiguration": NotRequired[AccessConfigurationTypeDef],
        "attributes": NotRequired[Sequence[DocumentAttributeTypeDef]],
        "content": NotRequired[DocumentContentTypeDef],
        "contentType": NotRequired[ContentTypeType],
        "documentEnrichmentConfiguration": NotRequired[DocumentEnrichmentConfigurationTypeDef],
        "title": NotRequired[str],
    },
)
GetDataSourceResponseTypeDef = TypedDict(
    "GetDataSourceResponseTypeDef",
    {
        "applicationId": str,
        "configuration": Dict[str, Any],
        "createdAt": datetime,
        "dataSourceArn": str,
        "dataSourceId": str,
        "description": str,
        "displayName": str,
        "documentEnrichmentConfiguration": DocumentEnrichmentConfigurationTypeDef,
        "error": ErrorDetailTypeDef,
        "indexId": str,
        "roleArn": str,
        "status": DataSourceStatusType,
        "syncSchedule": str,
        "type": str,
        "updatedAt": datetime,
        "vpcConfiguration": DataSourceVpcConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateDataSourceRequestRequestTypeDef = TypedDict(
    "UpdateDataSourceRequestRequestTypeDef",
    {
        "applicationId": str,
        "dataSourceId": str,
        "indexId": str,
        "configuration": NotRequired[Mapping[str, Any]],
        "description": NotRequired[str],
        "displayName": NotRequired[str],
        "documentEnrichmentConfiguration": NotRequired[DocumentEnrichmentConfigurationTypeDef],
        "roleArn": NotRequired[str],
        "syncSchedule": NotRequired[str],
        "vpcConfiguration": NotRequired[DataSourceVpcConfigurationTypeDef],
    },
)
BatchPutDocumentRequestRequestTypeDef = TypedDict(
    "BatchPutDocumentRequestRequestTypeDef",
    {
        "applicationId": str,
        "documents": Sequence[DocumentTypeDef],
        "indexId": str,
        "dataSourceSyncId": NotRequired[str],
        "roleArn": NotRequired[str],
    },
)
