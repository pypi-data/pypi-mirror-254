"""
Type annotations for bedrock-agent service type definitions.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_bedrock_agent/type_defs/)

Usage::

    ```python
    from types_aiobotocore_bedrock_agent.type_defs import S3IdentifierTypeDef

    data: S3IdentifierTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from .literals import (
    ActionGroupStateType,
    AgentAliasStatusType,
    AgentStatusType,
    ChunkingStrategyType,
    CreationModeType,
    DataSourceStatusType,
    IngestionJobSortByAttributeType,
    IngestionJobStatusType,
    KnowledgeBaseStateType,
    KnowledgeBaseStatusType,
    KnowledgeBaseStorageTypeType,
    PromptStateType,
    PromptTypeType,
    SortOrderType,
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
    "S3IdentifierTypeDef",
    "ActionGroupExecutorTypeDef",
    "ActionGroupSummaryTypeDef",
    "AgentAliasRoutingConfigurationListItemTypeDef",
    "AgentKnowledgeBaseSummaryTypeDef",
    "AgentKnowledgeBaseTypeDef",
    "AgentSummaryTypeDef",
    "AgentVersionSummaryTypeDef",
    "AssociateAgentKnowledgeBaseRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "FixedSizeChunkingConfigurationTypeDef",
    "ServerSideEncryptionConfigurationTypeDef",
    "S3DataSourceConfigurationTypeDef",
    "DataSourceSummaryTypeDef",
    "DeleteAgentActionGroupRequestRequestTypeDef",
    "DeleteAgentAliasRequestRequestTypeDef",
    "DeleteAgentRequestRequestTypeDef",
    "DeleteAgentVersionRequestRequestTypeDef",
    "DeleteDataSourceRequestRequestTypeDef",
    "DeleteKnowledgeBaseRequestRequestTypeDef",
    "DisassociateAgentKnowledgeBaseRequestRequestTypeDef",
    "GetAgentActionGroupRequestRequestTypeDef",
    "GetAgentAliasRequestRequestTypeDef",
    "GetAgentKnowledgeBaseRequestRequestTypeDef",
    "GetAgentRequestRequestTypeDef",
    "GetAgentVersionRequestRequestTypeDef",
    "GetDataSourceRequestRequestTypeDef",
    "GetIngestionJobRequestRequestTypeDef",
    "GetKnowledgeBaseRequestRequestTypeDef",
    "InferenceConfigurationTypeDef",
    "IngestionJobFilterTypeDef",
    "IngestionJobSortByTypeDef",
    "IngestionJobStatisticsTypeDef",
    "VectorKnowledgeBaseConfigurationTypeDef",
    "KnowledgeBaseSummaryTypeDef",
    "PaginatorConfigTypeDef",
    "ListAgentActionGroupsRequestRequestTypeDef",
    "ListAgentAliasesRequestRequestTypeDef",
    "ListAgentKnowledgeBasesRequestRequestTypeDef",
    "ListAgentVersionsRequestRequestTypeDef",
    "ListAgentsRequestRequestTypeDef",
    "ListDataSourcesRequestRequestTypeDef",
    "ListKnowledgeBasesRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "OpenSearchServerlessFieldMappingTypeDef",
    "PineconeFieldMappingTypeDef",
    "PrepareAgentRequestRequestTypeDef",
    "RdsFieldMappingTypeDef",
    "RedisEnterpriseCloudFieldMappingTypeDef",
    "StartIngestionJobRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateAgentKnowledgeBaseRequestRequestTypeDef",
    "APISchemaTypeDef",
    "AgentAliasHistoryEventTypeDef",
    "AgentAliasSummaryTypeDef",
    "CreateAgentAliasRequestRequestTypeDef",
    "UpdateAgentAliasRequestRequestTypeDef",
    "AssociateAgentKnowledgeBaseResponseTypeDef",
    "DeleteAgentAliasResponseTypeDef",
    "DeleteAgentResponseTypeDef",
    "DeleteAgentVersionResponseTypeDef",
    "DeleteDataSourceResponseTypeDef",
    "DeleteKnowledgeBaseResponseTypeDef",
    "GetAgentKnowledgeBaseResponseTypeDef",
    "ListAgentActionGroupsResponseTypeDef",
    "ListAgentKnowledgeBasesResponseTypeDef",
    "ListAgentVersionsResponseTypeDef",
    "ListAgentsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PrepareAgentResponseTypeDef",
    "UpdateAgentKnowledgeBaseResponseTypeDef",
    "ChunkingConfigurationTypeDef",
    "DataSourceConfigurationTypeDef",
    "ListDataSourcesResponseTypeDef",
    "PromptConfigurationTypeDef",
    "ListIngestionJobsRequestRequestTypeDef",
    "IngestionJobSummaryTypeDef",
    "IngestionJobTypeDef",
    "KnowledgeBaseConfigurationTypeDef",
    "ListKnowledgeBasesResponseTypeDef",
    "ListAgentActionGroupsRequestListAgentActionGroupsPaginateTypeDef",
    "ListAgentAliasesRequestListAgentAliasesPaginateTypeDef",
    "ListAgentKnowledgeBasesRequestListAgentKnowledgeBasesPaginateTypeDef",
    "ListAgentVersionsRequestListAgentVersionsPaginateTypeDef",
    "ListAgentsRequestListAgentsPaginateTypeDef",
    "ListDataSourcesRequestListDataSourcesPaginateTypeDef",
    "ListIngestionJobsRequestListIngestionJobsPaginateTypeDef",
    "ListKnowledgeBasesRequestListKnowledgeBasesPaginateTypeDef",
    "OpenSearchServerlessConfigurationTypeDef",
    "PineconeConfigurationTypeDef",
    "RdsConfigurationTypeDef",
    "RedisEnterpriseCloudConfigurationTypeDef",
    "AgentActionGroupTypeDef",
    "CreateAgentActionGroupRequestRequestTypeDef",
    "UpdateAgentActionGroupRequestRequestTypeDef",
    "AgentAliasTypeDef",
    "ListAgentAliasesResponseTypeDef",
    "VectorIngestionConfigurationTypeDef",
    "PromptOverrideConfigurationTypeDef",
    "ListIngestionJobsResponseTypeDef",
    "GetIngestionJobResponseTypeDef",
    "StartIngestionJobResponseTypeDef",
    "StorageConfigurationTypeDef",
    "CreateAgentActionGroupResponseTypeDef",
    "GetAgentActionGroupResponseTypeDef",
    "UpdateAgentActionGroupResponseTypeDef",
    "CreateAgentAliasResponseTypeDef",
    "GetAgentAliasResponseTypeDef",
    "UpdateAgentAliasResponseTypeDef",
    "CreateDataSourceRequestRequestTypeDef",
    "DataSourceTypeDef",
    "UpdateDataSourceRequestRequestTypeDef",
    "AgentTypeDef",
    "AgentVersionTypeDef",
    "CreateAgentRequestRequestTypeDef",
    "UpdateAgentRequestRequestTypeDef",
    "CreateKnowledgeBaseRequestRequestTypeDef",
    "KnowledgeBaseTypeDef",
    "UpdateKnowledgeBaseRequestRequestTypeDef",
    "CreateDataSourceResponseTypeDef",
    "GetDataSourceResponseTypeDef",
    "UpdateDataSourceResponseTypeDef",
    "CreateAgentResponseTypeDef",
    "GetAgentResponseTypeDef",
    "UpdateAgentResponseTypeDef",
    "GetAgentVersionResponseTypeDef",
    "CreateKnowledgeBaseResponseTypeDef",
    "GetKnowledgeBaseResponseTypeDef",
    "UpdateKnowledgeBaseResponseTypeDef",
)

S3IdentifierTypeDef = TypedDict(
    "S3IdentifierTypeDef",
    {
        "s3BucketName": NotRequired[str],
        "s3ObjectKey": NotRequired[str],
    },
)
ActionGroupExecutorTypeDef = TypedDict(
    "ActionGroupExecutorTypeDef",
    {
        "lambda": NotRequired[str],
    },
)
ActionGroupSummaryTypeDef = TypedDict(
    "ActionGroupSummaryTypeDef",
    {
        "actionGroupId": str,
        "actionGroupName": str,
        "actionGroupState": ActionGroupStateType,
        "updatedAt": datetime,
        "description": NotRequired[str],
    },
)
AgentAliasRoutingConfigurationListItemTypeDef = TypedDict(
    "AgentAliasRoutingConfigurationListItemTypeDef",
    {
        "agentVersion": str,
    },
)
AgentKnowledgeBaseSummaryTypeDef = TypedDict(
    "AgentKnowledgeBaseSummaryTypeDef",
    {
        "knowledgeBaseId": str,
        "knowledgeBaseState": KnowledgeBaseStateType,
        "updatedAt": datetime,
        "description": NotRequired[str],
    },
)
AgentKnowledgeBaseTypeDef = TypedDict(
    "AgentKnowledgeBaseTypeDef",
    {
        "agentId": str,
        "agentVersion": str,
        "knowledgeBaseId": str,
        "description": str,
        "createdAt": datetime,
        "updatedAt": datetime,
        "knowledgeBaseState": KnowledgeBaseStateType,
    },
)
AgentSummaryTypeDef = TypedDict(
    "AgentSummaryTypeDef",
    {
        "agentId": str,
        "agentName": str,
        "agentStatus": AgentStatusType,
        "updatedAt": datetime,
        "description": NotRequired[str],
        "latestAgentVersion": NotRequired[str],
    },
)
AgentVersionSummaryTypeDef = TypedDict(
    "AgentVersionSummaryTypeDef",
    {
        "agentName": str,
        "agentStatus": AgentStatusType,
        "agentVersion": str,
        "createdAt": datetime,
        "updatedAt": datetime,
        "description": NotRequired[str],
    },
)
AssociateAgentKnowledgeBaseRequestRequestTypeDef = TypedDict(
    "AssociateAgentKnowledgeBaseRequestRequestTypeDef",
    {
        "agentId": str,
        "agentVersion": str,
        "knowledgeBaseId": str,
        "description": str,
        "knowledgeBaseState": NotRequired[KnowledgeBaseStateType],
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
FixedSizeChunkingConfigurationTypeDef = TypedDict(
    "FixedSizeChunkingConfigurationTypeDef",
    {
        "maxTokens": int,
        "overlapPercentage": int,
    },
)
ServerSideEncryptionConfigurationTypeDef = TypedDict(
    "ServerSideEncryptionConfigurationTypeDef",
    {
        "kmsKeyArn": NotRequired[str],
    },
)
S3DataSourceConfigurationTypeDef = TypedDict(
    "S3DataSourceConfigurationTypeDef",
    {
        "bucketArn": str,
        "inclusionPrefixes": NotRequired[Sequence[str]],
    },
)
DataSourceSummaryTypeDef = TypedDict(
    "DataSourceSummaryTypeDef",
    {
        "knowledgeBaseId": str,
        "dataSourceId": str,
        "name": str,
        "status": DataSourceStatusType,
        "updatedAt": datetime,
        "description": NotRequired[str],
    },
)
DeleteAgentActionGroupRequestRequestTypeDef = TypedDict(
    "DeleteAgentActionGroupRequestRequestTypeDef",
    {
        "agentId": str,
        "agentVersion": str,
        "actionGroupId": str,
        "skipResourceInUseCheck": NotRequired[bool],
    },
)
DeleteAgentAliasRequestRequestTypeDef = TypedDict(
    "DeleteAgentAliasRequestRequestTypeDef",
    {
        "agentId": str,
        "agentAliasId": str,
    },
)
DeleteAgentRequestRequestTypeDef = TypedDict(
    "DeleteAgentRequestRequestTypeDef",
    {
        "agentId": str,
        "skipResourceInUseCheck": NotRequired[bool],
    },
)
DeleteAgentVersionRequestRequestTypeDef = TypedDict(
    "DeleteAgentVersionRequestRequestTypeDef",
    {
        "agentId": str,
        "agentVersion": str,
        "skipResourceInUseCheck": NotRequired[bool],
    },
)
DeleteDataSourceRequestRequestTypeDef = TypedDict(
    "DeleteDataSourceRequestRequestTypeDef",
    {
        "knowledgeBaseId": str,
        "dataSourceId": str,
    },
)
DeleteKnowledgeBaseRequestRequestTypeDef = TypedDict(
    "DeleteKnowledgeBaseRequestRequestTypeDef",
    {
        "knowledgeBaseId": str,
    },
)
DisassociateAgentKnowledgeBaseRequestRequestTypeDef = TypedDict(
    "DisassociateAgentKnowledgeBaseRequestRequestTypeDef",
    {
        "agentId": str,
        "agentVersion": str,
        "knowledgeBaseId": str,
    },
)
GetAgentActionGroupRequestRequestTypeDef = TypedDict(
    "GetAgentActionGroupRequestRequestTypeDef",
    {
        "agentId": str,
        "agentVersion": str,
        "actionGroupId": str,
    },
)
GetAgentAliasRequestRequestTypeDef = TypedDict(
    "GetAgentAliasRequestRequestTypeDef",
    {
        "agentId": str,
        "agentAliasId": str,
    },
)
GetAgentKnowledgeBaseRequestRequestTypeDef = TypedDict(
    "GetAgentKnowledgeBaseRequestRequestTypeDef",
    {
        "agentId": str,
        "agentVersion": str,
        "knowledgeBaseId": str,
    },
)
GetAgentRequestRequestTypeDef = TypedDict(
    "GetAgentRequestRequestTypeDef",
    {
        "agentId": str,
    },
)
GetAgentVersionRequestRequestTypeDef = TypedDict(
    "GetAgentVersionRequestRequestTypeDef",
    {
        "agentId": str,
        "agentVersion": str,
    },
)
GetDataSourceRequestRequestTypeDef = TypedDict(
    "GetDataSourceRequestRequestTypeDef",
    {
        "knowledgeBaseId": str,
        "dataSourceId": str,
    },
)
GetIngestionJobRequestRequestTypeDef = TypedDict(
    "GetIngestionJobRequestRequestTypeDef",
    {
        "knowledgeBaseId": str,
        "dataSourceId": str,
        "ingestionJobId": str,
    },
)
GetKnowledgeBaseRequestRequestTypeDef = TypedDict(
    "GetKnowledgeBaseRequestRequestTypeDef",
    {
        "knowledgeBaseId": str,
    },
)
InferenceConfigurationTypeDef = TypedDict(
    "InferenceConfigurationTypeDef",
    {
        "temperature": NotRequired[float],
        "topP": NotRequired[float],
        "topK": NotRequired[int],
        "maximumLength": NotRequired[int],
        "stopSequences": NotRequired[Sequence[str]],
    },
)
IngestionJobFilterTypeDef = TypedDict(
    "IngestionJobFilterTypeDef",
    {
        "attribute": Literal["STATUS"],
        "operator": Literal["EQ"],
        "values": Sequence[str],
    },
)
IngestionJobSortByTypeDef = TypedDict(
    "IngestionJobSortByTypeDef",
    {
        "attribute": IngestionJobSortByAttributeType,
        "order": SortOrderType,
    },
)
IngestionJobStatisticsTypeDef = TypedDict(
    "IngestionJobStatisticsTypeDef",
    {
        "numberOfDocumentsScanned": NotRequired[int],
        "numberOfNewDocumentsIndexed": NotRequired[int],
        "numberOfModifiedDocumentsIndexed": NotRequired[int],
        "numberOfDocumentsDeleted": NotRequired[int],
        "numberOfDocumentsFailed": NotRequired[int],
    },
)
VectorKnowledgeBaseConfigurationTypeDef = TypedDict(
    "VectorKnowledgeBaseConfigurationTypeDef",
    {
        "embeddingModelArn": str,
    },
)
KnowledgeBaseSummaryTypeDef = TypedDict(
    "KnowledgeBaseSummaryTypeDef",
    {
        "knowledgeBaseId": str,
        "name": str,
        "status": KnowledgeBaseStatusType,
        "updatedAt": datetime,
        "description": NotRequired[str],
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
ListAgentActionGroupsRequestRequestTypeDef = TypedDict(
    "ListAgentActionGroupsRequestRequestTypeDef",
    {
        "agentId": str,
        "agentVersion": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListAgentAliasesRequestRequestTypeDef = TypedDict(
    "ListAgentAliasesRequestRequestTypeDef",
    {
        "agentId": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListAgentKnowledgeBasesRequestRequestTypeDef = TypedDict(
    "ListAgentKnowledgeBasesRequestRequestTypeDef",
    {
        "agentId": str,
        "agentVersion": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListAgentVersionsRequestRequestTypeDef = TypedDict(
    "ListAgentVersionsRequestRequestTypeDef",
    {
        "agentId": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListAgentsRequestRequestTypeDef = TypedDict(
    "ListAgentsRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListDataSourcesRequestRequestTypeDef = TypedDict(
    "ListDataSourcesRequestRequestTypeDef",
    {
        "knowledgeBaseId": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListKnowledgeBasesRequestRequestTypeDef = TypedDict(
    "ListKnowledgeBasesRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)
OpenSearchServerlessFieldMappingTypeDef = TypedDict(
    "OpenSearchServerlessFieldMappingTypeDef",
    {
        "vectorField": str,
        "textField": str,
        "metadataField": str,
    },
)
PineconeFieldMappingTypeDef = TypedDict(
    "PineconeFieldMappingTypeDef",
    {
        "textField": str,
        "metadataField": str,
    },
)
PrepareAgentRequestRequestTypeDef = TypedDict(
    "PrepareAgentRequestRequestTypeDef",
    {
        "agentId": str,
    },
)
RdsFieldMappingTypeDef = TypedDict(
    "RdsFieldMappingTypeDef",
    {
        "primaryKeyField": str,
        "vectorField": str,
        "textField": str,
        "metadataField": str,
    },
)
RedisEnterpriseCloudFieldMappingTypeDef = TypedDict(
    "RedisEnterpriseCloudFieldMappingTypeDef",
    {
        "vectorField": str,
        "textField": str,
        "metadataField": str,
    },
)
StartIngestionJobRequestRequestTypeDef = TypedDict(
    "StartIngestionJobRequestRequestTypeDef",
    {
        "knowledgeBaseId": str,
        "dataSourceId": str,
        "clientToken": NotRequired[str],
        "description": NotRequired[str],
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Mapping[str, str],
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)
UpdateAgentKnowledgeBaseRequestRequestTypeDef = TypedDict(
    "UpdateAgentKnowledgeBaseRequestRequestTypeDef",
    {
        "agentId": str,
        "agentVersion": str,
        "knowledgeBaseId": str,
        "description": NotRequired[str],
        "knowledgeBaseState": NotRequired[KnowledgeBaseStateType],
    },
)
APISchemaTypeDef = TypedDict(
    "APISchemaTypeDef",
    {
        "s3": NotRequired[S3IdentifierTypeDef],
        "payload": NotRequired[str],
    },
)
AgentAliasHistoryEventTypeDef = TypedDict(
    "AgentAliasHistoryEventTypeDef",
    {
        "routingConfiguration": NotRequired[List[AgentAliasRoutingConfigurationListItemTypeDef]],
        "endDate": NotRequired[datetime],
        "startDate": NotRequired[datetime],
    },
)
AgentAliasSummaryTypeDef = TypedDict(
    "AgentAliasSummaryTypeDef",
    {
        "agentAliasId": str,
        "agentAliasName": str,
        "agentAliasStatus": AgentAliasStatusType,
        "createdAt": datetime,
        "updatedAt": datetime,
        "description": NotRequired[str],
        "routingConfiguration": NotRequired[List[AgentAliasRoutingConfigurationListItemTypeDef]],
    },
)
CreateAgentAliasRequestRequestTypeDef = TypedDict(
    "CreateAgentAliasRequestRequestTypeDef",
    {
        "agentId": str,
        "agentAliasName": str,
        "clientToken": NotRequired[str],
        "description": NotRequired[str],
        "routingConfiguration": NotRequired[
            Sequence[AgentAliasRoutingConfigurationListItemTypeDef]
        ],
        "tags": NotRequired[Mapping[str, str]],
    },
)
UpdateAgentAliasRequestRequestTypeDef = TypedDict(
    "UpdateAgentAliasRequestRequestTypeDef",
    {
        "agentId": str,
        "agentAliasId": str,
        "agentAliasName": str,
        "description": NotRequired[str],
        "routingConfiguration": NotRequired[
            Sequence[AgentAliasRoutingConfigurationListItemTypeDef]
        ],
    },
)
AssociateAgentKnowledgeBaseResponseTypeDef = TypedDict(
    "AssociateAgentKnowledgeBaseResponseTypeDef",
    {
        "agentKnowledgeBase": AgentKnowledgeBaseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteAgentAliasResponseTypeDef = TypedDict(
    "DeleteAgentAliasResponseTypeDef",
    {
        "agentId": str,
        "agentAliasId": str,
        "agentAliasStatus": AgentAliasStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteAgentResponseTypeDef = TypedDict(
    "DeleteAgentResponseTypeDef",
    {
        "agentId": str,
        "agentStatus": AgentStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteAgentVersionResponseTypeDef = TypedDict(
    "DeleteAgentVersionResponseTypeDef",
    {
        "agentId": str,
        "agentVersion": str,
        "agentStatus": AgentStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteDataSourceResponseTypeDef = TypedDict(
    "DeleteDataSourceResponseTypeDef",
    {
        "knowledgeBaseId": str,
        "dataSourceId": str,
        "status": DataSourceStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteKnowledgeBaseResponseTypeDef = TypedDict(
    "DeleteKnowledgeBaseResponseTypeDef",
    {
        "knowledgeBaseId": str,
        "status": KnowledgeBaseStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAgentKnowledgeBaseResponseTypeDef = TypedDict(
    "GetAgentKnowledgeBaseResponseTypeDef",
    {
        "agentKnowledgeBase": AgentKnowledgeBaseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAgentActionGroupsResponseTypeDef = TypedDict(
    "ListAgentActionGroupsResponseTypeDef",
    {
        "actionGroupSummaries": List[ActionGroupSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAgentKnowledgeBasesResponseTypeDef = TypedDict(
    "ListAgentKnowledgeBasesResponseTypeDef",
    {
        "agentKnowledgeBaseSummaries": List[AgentKnowledgeBaseSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAgentVersionsResponseTypeDef = TypedDict(
    "ListAgentVersionsResponseTypeDef",
    {
        "agentVersionSummaries": List[AgentVersionSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAgentsResponseTypeDef = TypedDict(
    "ListAgentsResponseTypeDef",
    {
        "agentSummaries": List[AgentSummaryTypeDef],
        "nextToken": str,
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
PrepareAgentResponseTypeDef = TypedDict(
    "PrepareAgentResponseTypeDef",
    {
        "agentId": str,
        "agentStatus": AgentStatusType,
        "agentVersion": str,
        "preparedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateAgentKnowledgeBaseResponseTypeDef = TypedDict(
    "UpdateAgentKnowledgeBaseResponseTypeDef",
    {
        "agentKnowledgeBase": AgentKnowledgeBaseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ChunkingConfigurationTypeDef = TypedDict(
    "ChunkingConfigurationTypeDef",
    {
        "chunkingStrategy": ChunkingStrategyType,
        "fixedSizeChunkingConfiguration": NotRequired[FixedSizeChunkingConfigurationTypeDef],
    },
)
DataSourceConfigurationTypeDef = TypedDict(
    "DataSourceConfigurationTypeDef",
    {
        "type": Literal["S3"],
        "s3Configuration": NotRequired[S3DataSourceConfigurationTypeDef],
    },
)
ListDataSourcesResponseTypeDef = TypedDict(
    "ListDataSourcesResponseTypeDef",
    {
        "dataSourceSummaries": List[DataSourceSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PromptConfigurationTypeDef = TypedDict(
    "PromptConfigurationTypeDef",
    {
        "promptType": NotRequired[PromptTypeType],
        "promptCreationMode": NotRequired[CreationModeType],
        "promptState": NotRequired[PromptStateType],
        "basePromptTemplate": NotRequired[str],
        "inferenceConfiguration": NotRequired[InferenceConfigurationTypeDef],
        "parserMode": NotRequired[CreationModeType],
    },
)
ListIngestionJobsRequestRequestTypeDef = TypedDict(
    "ListIngestionJobsRequestRequestTypeDef",
    {
        "knowledgeBaseId": str,
        "dataSourceId": str,
        "filters": NotRequired[Sequence[IngestionJobFilterTypeDef]],
        "sortBy": NotRequired[IngestionJobSortByTypeDef],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
IngestionJobSummaryTypeDef = TypedDict(
    "IngestionJobSummaryTypeDef",
    {
        "knowledgeBaseId": str,
        "dataSourceId": str,
        "ingestionJobId": str,
        "status": IngestionJobStatusType,
        "startedAt": datetime,
        "updatedAt": datetime,
        "description": NotRequired[str],
        "statistics": NotRequired[IngestionJobStatisticsTypeDef],
    },
)
IngestionJobTypeDef = TypedDict(
    "IngestionJobTypeDef",
    {
        "knowledgeBaseId": str,
        "dataSourceId": str,
        "ingestionJobId": str,
        "status": IngestionJobStatusType,
        "startedAt": datetime,
        "updatedAt": datetime,
        "description": NotRequired[str],
        "statistics": NotRequired[IngestionJobStatisticsTypeDef],
        "failureReasons": NotRequired[List[str]],
    },
)
KnowledgeBaseConfigurationTypeDef = TypedDict(
    "KnowledgeBaseConfigurationTypeDef",
    {
        "type": Literal["VECTOR"],
        "vectorKnowledgeBaseConfiguration": NotRequired[VectorKnowledgeBaseConfigurationTypeDef],
    },
)
ListKnowledgeBasesResponseTypeDef = TypedDict(
    "ListKnowledgeBasesResponseTypeDef",
    {
        "knowledgeBaseSummaries": List[KnowledgeBaseSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAgentActionGroupsRequestListAgentActionGroupsPaginateTypeDef = TypedDict(
    "ListAgentActionGroupsRequestListAgentActionGroupsPaginateTypeDef",
    {
        "agentId": str,
        "agentVersion": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListAgentAliasesRequestListAgentAliasesPaginateTypeDef = TypedDict(
    "ListAgentAliasesRequestListAgentAliasesPaginateTypeDef",
    {
        "agentId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListAgentKnowledgeBasesRequestListAgentKnowledgeBasesPaginateTypeDef = TypedDict(
    "ListAgentKnowledgeBasesRequestListAgentKnowledgeBasesPaginateTypeDef",
    {
        "agentId": str,
        "agentVersion": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListAgentVersionsRequestListAgentVersionsPaginateTypeDef = TypedDict(
    "ListAgentVersionsRequestListAgentVersionsPaginateTypeDef",
    {
        "agentId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListAgentsRequestListAgentsPaginateTypeDef = TypedDict(
    "ListAgentsRequestListAgentsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDataSourcesRequestListDataSourcesPaginateTypeDef = TypedDict(
    "ListDataSourcesRequestListDataSourcesPaginateTypeDef",
    {
        "knowledgeBaseId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListIngestionJobsRequestListIngestionJobsPaginateTypeDef = TypedDict(
    "ListIngestionJobsRequestListIngestionJobsPaginateTypeDef",
    {
        "knowledgeBaseId": str,
        "dataSourceId": str,
        "filters": NotRequired[Sequence[IngestionJobFilterTypeDef]],
        "sortBy": NotRequired[IngestionJobSortByTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListKnowledgeBasesRequestListKnowledgeBasesPaginateTypeDef = TypedDict(
    "ListKnowledgeBasesRequestListKnowledgeBasesPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
OpenSearchServerlessConfigurationTypeDef = TypedDict(
    "OpenSearchServerlessConfigurationTypeDef",
    {
        "collectionArn": str,
        "vectorIndexName": str,
        "fieldMapping": OpenSearchServerlessFieldMappingTypeDef,
    },
)
PineconeConfigurationTypeDef = TypedDict(
    "PineconeConfigurationTypeDef",
    {
        "connectionString": str,
        "credentialsSecretArn": str,
        "fieldMapping": PineconeFieldMappingTypeDef,
        "namespace": NotRequired[str],
    },
)
RdsConfigurationTypeDef = TypedDict(
    "RdsConfigurationTypeDef",
    {
        "resourceArn": str,
        "credentialsSecretArn": str,
        "databaseName": str,
        "tableName": str,
        "fieldMapping": RdsFieldMappingTypeDef,
    },
)
RedisEnterpriseCloudConfigurationTypeDef = TypedDict(
    "RedisEnterpriseCloudConfigurationTypeDef",
    {
        "endpoint": str,
        "vectorIndexName": str,
        "credentialsSecretArn": str,
        "fieldMapping": RedisEnterpriseCloudFieldMappingTypeDef,
    },
)
AgentActionGroupTypeDef = TypedDict(
    "AgentActionGroupTypeDef",
    {
        "agentId": str,
        "agentVersion": str,
        "actionGroupId": str,
        "actionGroupName": str,
        "createdAt": datetime,
        "updatedAt": datetime,
        "actionGroupState": ActionGroupStateType,
        "clientToken": NotRequired[str],
        "description": NotRequired[str],
        "parentActionSignature": NotRequired[Literal["AMAZON.UserInput"]],
        "actionGroupExecutor": NotRequired[ActionGroupExecutorTypeDef],
        "apiSchema": NotRequired[APISchemaTypeDef],
    },
)
CreateAgentActionGroupRequestRequestTypeDef = TypedDict(
    "CreateAgentActionGroupRequestRequestTypeDef",
    {
        "agentId": str,
        "agentVersion": str,
        "actionGroupName": str,
        "clientToken": NotRequired[str],
        "description": NotRequired[str],
        "parentActionGroupSignature": NotRequired[Literal["AMAZON.UserInput"]],
        "actionGroupExecutor": NotRequired[ActionGroupExecutorTypeDef],
        "apiSchema": NotRequired[APISchemaTypeDef],
        "actionGroupState": NotRequired[ActionGroupStateType],
    },
)
UpdateAgentActionGroupRequestRequestTypeDef = TypedDict(
    "UpdateAgentActionGroupRequestRequestTypeDef",
    {
        "agentId": str,
        "agentVersion": str,
        "actionGroupId": str,
        "actionGroupName": str,
        "description": NotRequired[str],
        "parentActionGroupSignature": NotRequired[Literal["AMAZON.UserInput"]],
        "actionGroupExecutor": NotRequired[ActionGroupExecutorTypeDef],
        "actionGroupState": NotRequired[ActionGroupStateType],
        "apiSchema": NotRequired[APISchemaTypeDef],
    },
)
AgentAliasTypeDef = TypedDict(
    "AgentAliasTypeDef",
    {
        "agentId": str,
        "agentAliasId": str,
        "agentAliasName": str,
        "agentAliasArn": str,
        "routingConfiguration": List[AgentAliasRoutingConfigurationListItemTypeDef],
        "createdAt": datetime,
        "updatedAt": datetime,
        "agentAliasStatus": AgentAliasStatusType,
        "clientToken": NotRequired[str],
        "description": NotRequired[str],
        "agentAliasHistoryEvents": NotRequired[List[AgentAliasHistoryEventTypeDef]],
    },
)
ListAgentAliasesResponseTypeDef = TypedDict(
    "ListAgentAliasesResponseTypeDef",
    {
        "agentAliasSummaries": List[AgentAliasSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
VectorIngestionConfigurationTypeDef = TypedDict(
    "VectorIngestionConfigurationTypeDef",
    {
        "chunkingConfiguration": NotRequired[ChunkingConfigurationTypeDef],
    },
)
PromptOverrideConfigurationTypeDef = TypedDict(
    "PromptOverrideConfigurationTypeDef",
    {
        "promptConfigurations": Sequence[PromptConfigurationTypeDef],
        "overrideLambda": NotRequired[str],
    },
)
ListIngestionJobsResponseTypeDef = TypedDict(
    "ListIngestionJobsResponseTypeDef",
    {
        "ingestionJobSummaries": List[IngestionJobSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetIngestionJobResponseTypeDef = TypedDict(
    "GetIngestionJobResponseTypeDef",
    {
        "ingestionJob": IngestionJobTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartIngestionJobResponseTypeDef = TypedDict(
    "StartIngestionJobResponseTypeDef",
    {
        "ingestionJob": IngestionJobTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StorageConfigurationTypeDef = TypedDict(
    "StorageConfigurationTypeDef",
    {
        "type": KnowledgeBaseStorageTypeType,
        "opensearchServerlessConfiguration": NotRequired[OpenSearchServerlessConfigurationTypeDef],
        "pineconeConfiguration": NotRequired[PineconeConfigurationTypeDef],
        "redisEnterpriseCloudConfiguration": NotRequired[RedisEnterpriseCloudConfigurationTypeDef],
        "rdsConfiguration": NotRequired[RdsConfigurationTypeDef],
    },
)
CreateAgentActionGroupResponseTypeDef = TypedDict(
    "CreateAgentActionGroupResponseTypeDef",
    {
        "agentActionGroup": AgentActionGroupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAgentActionGroupResponseTypeDef = TypedDict(
    "GetAgentActionGroupResponseTypeDef",
    {
        "agentActionGroup": AgentActionGroupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateAgentActionGroupResponseTypeDef = TypedDict(
    "UpdateAgentActionGroupResponseTypeDef",
    {
        "agentActionGroup": AgentActionGroupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateAgentAliasResponseTypeDef = TypedDict(
    "CreateAgentAliasResponseTypeDef",
    {
        "agentAlias": AgentAliasTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAgentAliasResponseTypeDef = TypedDict(
    "GetAgentAliasResponseTypeDef",
    {
        "agentAlias": AgentAliasTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateAgentAliasResponseTypeDef = TypedDict(
    "UpdateAgentAliasResponseTypeDef",
    {
        "agentAlias": AgentAliasTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDataSourceRequestRequestTypeDef = TypedDict(
    "CreateDataSourceRequestRequestTypeDef",
    {
        "knowledgeBaseId": str,
        "name": str,
        "dataSourceConfiguration": DataSourceConfigurationTypeDef,
        "clientToken": NotRequired[str],
        "description": NotRequired[str],
        "serverSideEncryptionConfiguration": NotRequired[ServerSideEncryptionConfigurationTypeDef],
        "vectorIngestionConfiguration": NotRequired[VectorIngestionConfigurationTypeDef],
    },
)
DataSourceTypeDef = TypedDict(
    "DataSourceTypeDef",
    {
        "knowledgeBaseId": str,
        "dataSourceId": str,
        "name": str,
        "status": DataSourceStatusType,
        "dataSourceConfiguration": DataSourceConfigurationTypeDef,
        "createdAt": datetime,
        "updatedAt": datetime,
        "description": NotRequired[str],
        "serverSideEncryptionConfiguration": NotRequired[ServerSideEncryptionConfigurationTypeDef],
        "vectorIngestionConfiguration": NotRequired[VectorIngestionConfigurationTypeDef],
    },
)
UpdateDataSourceRequestRequestTypeDef = TypedDict(
    "UpdateDataSourceRequestRequestTypeDef",
    {
        "knowledgeBaseId": str,
        "dataSourceId": str,
        "name": str,
        "dataSourceConfiguration": DataSourceConfigurationTypeDef,
        "description": NotRequired[str],
        "serverSideEncryptionConfiguration": NotRequired[ServerSideEncryptionConfigurationTypeDef],
        "vectorIngestionConfiguration": NotRequired[VectorIngestionConfigurationTypeDef],
    },
)
AgentTypeDef = TypedDict(
    "AgentTypeDef",
    {
        "agentId": str,
        "agentName": str,
        "agentArn": str,
        "agentVersion": str,
        "agentStatus": AgentStatusType,
        "idleSessionTTLInSeconds": int,
        "agentResourceRoleArn": str,
        "createdAt": datetime,
        "updatedAt": datetime,
        "clientToken": NotRequired[str],
        "instruction": NotRequired[str],
        "foundationModel": NotRequired[str],
        "description": NotRequired[str],
        "customerEncryptionKeyArn": NotRequired[str],
        "preparedAt": NotRequired[datetime],
        "failureReasons": NotRequired[List[str]],
        "recommendedActions": NotRequired[List[str]],
        "promptOverrideConfiguration": NotRequired[PromptOverrideConfigurationTypeDef],
    },
)
AgentVersionTypeDef = TypedDict(
    "AgentVersionTypeDef",
    {
        "agentId": str,
        "agentName": str,
        "agentArn": str,
        "version": str,
        "agentStatus": AgentStatusType,
        "idleSessionTTLInSeconds": int,
        "agentResourceRoleArn": str,
        "createdAt": datetime,
        "updatedAt": datetime,
        "instruction": NotRequired[str],
        "foundationModel": NotRequired[str],
        "description": NotRequired[str],
        "customerEncryptionKeyArn": NotRequired[str],
        "failureReasons": NotRequired[List[str]],
        "recommendedActions": NotRequired[List[str]],
        "promptOverrideConfiguration": NotRequired[PromptOverrideConfigurationTypeDef],
    },
)
CreateAgentRequestRequestTypeDef = TypedDict(
    "CreateAgentRequestRequestTypeDef",
    {
        "agentName": str,
        "agentResourceRoleArn": str,
        "clientToken": NotRequired[str],
        "instruction": NotRequired[str],
        "foundationModel": NotRequired[str],
        "description": NotRequired[str],
        "idleSessionTTLInSeconds": NotRequired[int],
        "customerEncryptionKeyArn": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
        "promptOverrideConfiguration": NotRequired[PromptOverrideConfigurationTypeDef],
    },
)
UpdateAgentRequestRequestTypeDef = TypedDict(
    "UpdateAgentRequestRequestTypeDef",
    {
        "agentId": str,
        "agentName": str,
        "agentResourceRoleArn": str,
        "instruction": NotRequired[str],
        "foundationModel": NotRequired[str],
        "description": NotRequired[str],
        "idleSessionTTLInSeconds": NotRequired[int],
        "customerEncryptionKeyArn": NotRequired[str],
        "promptOverrideConfiguration": NotRequired[PromptOverrideConfigurationTypeDef],
    },
)
CreateKnowledgeBaseRequestRequestTypeDef = TypedDict(
    "CreateKnowledgeBaseRequestRequestTypeDef",
    {
        "name": str,
        "roleArn": str,
        "knowledgeBaseConfiguration": KnowledgeBaseConfigurationTypeDef,
        "storageConfiguration": StorageConfigurationTypeDef,
        "clientToken": NotRequired[str],
        "description": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)
KnowledgeBaseTypeDef = TypedDict(
    "KnowledgeBaseTypeDef",
    {
        "knowledgeBaseId": str,
        "name": str,
        "knowledgeBaseArn": str,
        "roleArn": str,
        "knowledgeBaseConfiguration": KnowledgeBaseConfigurationTypeDef,
        "storageConfiguration": StorageConfigurationTypeDef,
        "status": KnowledgeBaseStatusType,
        "createdAt": datetime,
        "updatedAt": datetime,
        "description": NotRequired[str],
        "failureReasons": NotRequired[List[str]],
    },
)
UpdateKnowledgeBaseRequestRequestTypeDef = TypedDict(
    "UpdateKnowledgeBaseRequestRequestTypeDef",
    {
        "knowledgeBaseId": str,
        "name": str,
        "roleArn": str,
        "knowledgeBaseConfiguration": KnowledgeBaseConfigurationTypeDef,
        "storageConfiguration": StorageConfigurationTypeDef,
        "description": NotRequired[str],
    },
)
CreateDataSourceResponseTypeDef = TypedDict(
    "CreateDataSourceResponseTypeDef",
    {
        "dataSource": DataSourceTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetDataSourceResponseTypeDef = TypedDict(
    "GetDataSourceResponseTypeDef",
    {
        "dataSource": DataSourceTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateDataSourceResponseTypeDef = TypedDict(
    "UpdateDataSourceResponseTypeDef",
    {
        "dataSource": DataSourceTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateAgentResponseTypeDef = TypedDict(
    "CreateAgentResponseTypeDef",
    {
        "agent": AgentTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAgentResponseTypeDef = TypedDict(
    "GetAgentResponseTypeDef",
    {
        "agent": AgentTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateAgentResponseTypeDef = TypedDict(
    "UpdateAgentResponseTypeDef",
    {
        "agent": AgentTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAgentVersionResponseTypeDef = TypedDict(
    "GetAgentVersionResponseTypeDef",
    {
        "agentVersion": AgentVersionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateKnowledgeBaseResponseTypeDef = TypedDict(
    "CreateKnowledgeBaseResponseTypeDef",
    {
        "knowledgeBase": KnowledgeBaseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetKnowledgeBaseResponseTypeDef = TypedDict(
    "GetKnowledgeBaseResponseTypeDef",
    {
        "knowledgeBase": KnowledgeBaseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateKnowledgeBaseResponseTypeDef = TypedDict(
    "UpdateKnowledgeBaseResponseTypeDef",
    {
        "knowledgeBase": KnowledgeBaseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
