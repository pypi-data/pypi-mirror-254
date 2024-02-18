"""
Type annotations for cleanroomsml service type definitions.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cleanroomsml/type_defs/)

Usage::

    ```python
    from types_aiobotocore_cleanroomsml.type_defs import S3ConfigMapTypeDef

    data: S3ConfigMapTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from .literals import (
    AudienceExportJobStatusType,
    AudienceGenerationJobStatusType,
    AudienceModelMetricTypeType,
    AudienceModelStatusType,
    AudienceSizeTypeType,
    ColumnTypeType,
    PolicyExistenceConditionType,
    SharedAudienceMetricsType,
    TagOnCreatePolicyType,
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
    "S3ConfigMapTypeDef",
    "AudienceSizeTypeDef",
    "StatusDetailsTypeDef",
    "AudienceGenerationJobSummaryTypeDef",
    "AudienceModelMetricTypeDef",
    "AudienceModelSummaryTypeDef",
    "AudienceSizeConfigTypeDef",
    "ColumnSchemaTypeDef",
    "TimestampTypeDef",
    "ResponseMetadataTypeDef",
    "GlueDataSourceTypeDef",
    "DeleteAudienceGenerationJobRequestRequestTypeDef",
    "DeleteAudienceModelRequestRequestTypeDef",
    "DeleteConfiguredAudienceModelPolicyRequestRequestTypeDef",
    "DeleteConfiguredAudienceModelRequestRequestTypeDef",
    "DeleteTrainingDatasetRequestRequestTypeDef",
    "GetAudienceGenerationJobRequestRequestTypeDef",
    "GetAudienceModelRequestRequestTypeDef",
    "GetConfiguredAudienceModelPolicyRequestRequestTypeDef",
    "GetConfiguredAudienceModelRequestRequestTypeDef",
    "GetTrainingDatasetRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "ListAudienceExportJobsRequestRequestTypeDef",
    "ListAudienceGenerationJobsRequestRequestTypeDef",
    "ListAudienceModelsRequestRequestTypeDef",
    "ListConfiguredAudienceModelsRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTrainingDatasetsRequestRequestTypeDef",
    "TrainingDatasetSummaryTypeDef",
    "PutConfiguredAudienceModelPolicyRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "AudienceDestinationTypeDef",
    "AudienceGenerationJobDataSourceTypeDef",
    "RelevanceMetricTypeDef",
    "StartAudienceExportJobRequestRequestTypeDef",
    "AudienceExportJobSummaryTypeDef",
    "CreateAudienceModelRequestRequestTypeDef",
    "CreateAudienceModelResponseTypeDef",
    "CreateConfiguredAudienceModelResponseTypeDef",
    "CreateTrainingDatasetResponseTypeDef",
    "EmptyResponseMetadataTypeDef",
    "GetAudienceModelResponseTypeDef",
    "GetConfiguredAudienceModelPolicyResponseTypeDef",
    "ListAudienceGenerationJobsResponseTypeDef",
    "ListAudienceModelsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PutConfiguredAudienceModelPolicyResponseTypeDef",
    "StartAudienceGenerationJobResponseTypeDef",
    "UpdateConfiguredAudienceModelResponseTypeDef",
    "DataSourceTypeDef",
    "ListAudienceExportJobsRequestListAudienceExportJobsPaginateTypeDef",
    "ListAudienceGenerationJobsRequestListAudienceGenerationJobsPaginateTypeDef",
    "ListAudienceModelsRequestListAudienceModelsPaginateTypeDef",
    "ListConfiguredAudienceModelsRequestListConfiguredAudienceModelsPaginateTypeDef",
    "ListTrainingDatasetsRequestListTrainingDatasetsPaginateTypeDef",
    "ListTrainingDatasetsResponseTypeDef",
    "ConfiguredAudienceModelOutputConfigTypeDef",
    "StartAudienceGenerationJobRequestRequestTypeDef",
    "AudienceQualityMetricsTypeDef",
    "ListAudienceExportJobsResponseTypeDef",
    "DatasetInputConfigTypeDef",
    "ConfiguredAudienceModelSummaryTypeDef",
    "CreateConfiguredAudienceModelRequestRequestTypeDef",
    "GetConfiguredAudienceModelResponseTypeDef",
    "UpdateConfiguredAudienceModelRequestRequestTypeDef",
    "GetAudienceGenerationJobResponseTypeDef",
    "DatasetTypeDef",
    "ListConfiguredAudienceModelsResponseTypeDef",
    "CreateTrainingDatasetRequestRequestTypeDef",
    "GetTrainingDatasetResponseTypeDef",
)

S3ConfigMapTypeDef = TypedDict(
    "S3ConfigMapTypeDef",
    {
        "s3Uri": str,
    },
)
AudienceSizeTypeDef = TypedDict(
    "AudienceSizeTypeDef",
    {
        "type": AudienceSizeTypeType,
        "value": int,
    },
)
StatusDetailsTypeDef = TypedDict(
    "StatusDetailsTypeDef",
    {
        "message": NotRequired[str],
        "statusCode": NotRequired[str],
    },
)
AudienceGenerationJobSummaryTypeDef = TypedDict(
    "AudienceGenerationJobSummaryTypeDef",
    {
        "audienceGenerationJobArn": str,
        "configuredAudienceModelArn": str,
        "createTime": datetime,
        "name": str,
        "status": AudienceGenerationJobStatusType,
        "updateTime": datetime,
        "collaborationId": NotRequired[str],
        "description": NotRequired[str],
        "startedBy": NotRequired[str],
    },
)
AudienceModelMetricTypeDef = TypedDict(
    "AudienceModelMetricTypeDef",
    {
        "forTopKItemPredictions": int,
        "type": AudienceModelMetricTypeType,
        "value": float,
    },
)
AudienceModelSummaryTypeDef = TypedDict(
    "AudienceModelSummaryTypeDef",
    {
        "audienceModelArn": str,
        "createTime": datetime,
        "name": str,
        "status": AudienceModelStatusType,
        "trainingDatasetArn": str,
        "updateTime": datetime,
        "description": NotRequired[str],
    },
)
AudienceSizeConfigTypeDef = TypedDict(
    "AudienceSizeConfigTypeDef",
    {
        "audienceSizeBins": Sequence[int],
        "audienceSizeType": AudienceSizeTypeType,
    },
)
ColumnSchemaTypeDef = TypedDict(
    "ColumnSchemaTypeDef",
    {
        "columnName": str,
        "columnTypes": Sequence[ColumnTypeType],
    },
)
TimestampTypeDef = Union[datetime, str]
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
GlueDataSourceTypeDef = TypedDict(
    "GlueDataSourceTypeDef",
    {
        "databaseName": str,
        "tableName": str,
        "catalogId": NotRequired[str],
    },
)
DeleteAudienceGenerationJobRequestRequestTypeDef = TypedDict(
    "DeleteAudienceGenerationJobRequestRequestTypeDef",
    {
        "audienceGenerationJobArn": str,
    },
)
DeleteAudienceModelRequestRequestTypeDef = TypedDict(
    "DeleteAudienceModelRequestRequestTypeDef",
    {
        "audienceModelArn": str,
    },
)
DeleteConfiguredAudienceModelPolicyRequestRequestTypeDef = TypedDict(
    "DeleteConfiguredAudienceModelPolicyRequestRequestTypeDef",
    {
        "configuredAudienceModelArn": str,
    },
)
DeleteConfiguredAudienceModelRequestRequestTypeDef = TypedDict(
    "DeleteConfiguredAudienceModelRequestRequestTypeDef",
    {
        "configuredAudienceModelArn": str,
    },
)
DeleteTrainingDatasetRequestRequestTypeDef = TypedDict(
    "DeleteTrainingDatasetRequestRequestTypeDef",
    {
        "trainingDatasetArn": str,
    },
)
GetAudienceGenerationJobRequestRequestTypeDef = TypedDict(
    "GetAudienceGenerationJobRequestRequestTypeDef",
    {
        "audienceGenerationJobArn": str,
    },
)
GetAudienceModelRequestRequestTypeDef = TypedDict(
    "GetAudienceModelRequestRequestTypeDef",
    {
        "audienceModelArn": str,
    },
)
GetConfiguredAudienceModelPolicyRequestRequestTypeDef = TypedDict(
    "GetConfiguredAudienceModelPolicyRequestRequestTypeDef",
    {
        "configuredAudienceModelArn": str,
    },
)
GetConfiguredAudienceModelRequestRequestTypeDef = TypedDict(
    "GetConfiguredAudienceModelRequestRequestTypeDef",
    {
        "configuredAudienceModelArn": str,
    },
)
GetTrainingDatasetRequestRequestTypeDef = TypedDict(
    "GetTrainingDatasetRequestRequestTypeDef",
    {
        "trainingDatasetArn": str,
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
ListAudienceExportJobsRequestRequestTypeDef = TypedDict(
    "ListAudienceExportJobsRequestRequestTypeDef",
    {
        "audienceGenerationJobArn": NotRequired[str],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListAudienceGenerationJobsRequestRequestTypeDef = TypedDict(
    "ListAudienceGenerationJobsRequestRequestTypeDef",
    {
        "collaborationId": NotRequired[str],
        "configuredAudienceModelArn": NotRequired[str],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListAudienceModelsRequestRequestTypeDef = TypedDict(
    "ListAudienceModelsRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListConfiguredAudienceModelsRequestRequestTypeDef = TypedDict(
    "ListConfiguredAudienceModelsRequestRequestTypeDef",
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
ListTrainingDatasetsRequestRequestTypeDef = TypedDict(
    "ListTrainingDatasetsRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
TrainingDatasetSummaryTypeDef = TypedDict(
    "TrainingDatasetSummaryTypeDef",
    {
        "createTime": datetime,
        "name": str,
        "status": Literal["ACTIVE"],
        "trainingDatasetArn": str,
        "updateTime": datetime,
        "description": NotRequired[str],
    },
)
PutConfiguredAudienceModelPolicyRequestRequestTypeDef = TypedDict(
    "PutConfiguredAudienceModelPolicyRequestRequestTypeDef",
    {
        "configuredAudienceModelArn": str,
        "configuredAudienceModelPolicy": str,
        "policyExistenceCondition": NotRequired[PolicyExistenceConditionType],
        "previousPolicyHash": NotRequired[str],
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
AudienceDestinationTypeDef = TypedDict(
    "AudienceDestinationTypeDef",
    {
        "s3Destination": S3ConfigMapTypeDef,
    },
)
AudienceGenerationJobDataSourceTypeDef = TypedDict(
    "AudienceGenerationJobDataSourceTypeDef",
    {
        "dataSource": S3ConfigMapTypeDef,
        "roleArn": str,
    },
)
RelevanceMetricTypeDef = TypedDict(
    "RelevanceMetricTypeDef",
    {
        "audienceSize": AudienceSizeTypeDef,
        "score": NotRequired[float],
    },
)
StartAudienceExportJobRequestRequestTypeDef = TypedDict(
    "StartAudienceExportJobRequestRequestTypeDef",
    {
        "audienceGenerationJobArn": str,
        "audienceSize": AudienceSizeTypeDef,
        "name": str,
        "description": NotRequired[str],
    },
)
AudienceExportJobSummaryTypeDef = TypedDict(
    "AudienceExportJobSummaryTypeDef",
    {
        "audienceGenerationJobArn": str,
        "audienceSize": AudienceSizeTypeDef,
        "createTime": datetime,
        "name": str,
        "status": AudienceExportJobStatusType,
        "updateTime": datetime,
        "description": NotRequired[str],
        "outputLocation": NotRequired[str],
        "statusDetails": NotRequired[StatusDetailsTypeDef],
    },
)
CreateAudienceModelRequestRequestTypeDef = TypedDict(
    "CreateAudienceModelRequestRequestTypeDef",
    {
        "name": str,
        "trainingDatasetArn": str,
        "description": NotRequired[str],
        "kmsKeyArn": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
        "trainingDataEndTime": NotRequired[TimestampTypeDef],
        "trainingDataStartTime": NotRequired[TimestampTypeDef],
    },
)
CreateAudienceModelResponseTypeDef = TypedDict(
    "CreateAudienceModelResponseTypeDef",
    {
        "audienceModelArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateConfiguredAudienceModelResponseTypeDef = TypedDict(
    "CreateConfiguredAudienceModelResponseTypeDef",
    {
        "configuredAudienceModelArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateTrainingDatasetResponseTypeDef = TypedDict(
    "CreateTrainingDatasetResponseTypeDef",
    {
        "trainingDatasetArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAudienceModelResponseTypeDef = TypedDict(
    "GetAudienceModelResponseTypeDef",
    {
        "audienceModelArn": str,
        "createTime": datetime,
        "description": str,
        "kmsKeyArn": str,
        "metrics": List[AudienceModelMetricTypeDef],
        "name": str,
        "status": AudienceModelStatusType,
        "statusDetails": StatusDetailsTypeDef,
        "tags": Dict[str, str],
        "trainingDataEndTime": datetime,
        "trainingDataStartTime": datetime,
        "trainingDatasetArn": str,
        "updateTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetConfiguredAudienceModelPolicyResponseTypeDef = TypedDict(
    "GetConfiguredAudienceModelPolicyResponseTypeDef",
    {
        "configuredAudienceModelArn": str,
        "configuredAudienceModelPolicy": str,
        "policyHash": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAudienceGenerationJobsResponseTypeDef = TypedDict(
    "ListAudienceGenerationJobsResponseTypeDef",
    {
        "audienceGenerationJobs": List[AudienceGenerationJobSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAudienceModelsResponseTypeDef = TypedDict(
    "ListAudienceModelsResponseTypeDef",
    {
        "audienceModels": List[AudienceModelSummaryTypeDef],
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
PutConfiguredAudienceModelPolicyResponseTypeDef = TypedDict(
    "PutConfiguredAudienceModelPolicyResponseTypeDef",
    {
        "configuredAudienceModelPolicy": str,
        "policyHash": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartAudienceGenerationJobResponseTypeDef = TypedDict(
    "StartAudienceGenerationJobResponseTypeDef",
    {
        "audienceGenerationJobArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateConfiguredAudienceModelResponseTypeDef = TypedDict(
    "UpdateConfiguredAudienceModelResponseTypeDef",
    {
        "configuredAudienceModelArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DataSourceTypeDef = TypedDict(
    "DataSourceTypeDef",
    {
        "glueDataSource": GlueDataSourceTypeDef,
    },
)
ListAudienceExportJobsRequestListAudienceExportJobsPaginateTypeDef = TypedDict(
    "ListAudienceExportJobsRequestListAudienceExportJobsPaginateTypeDef",
    {
        "audienceGenerationJobArn": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListAudienceGenerationJobsRequestListAudienceGenerationJobsPaginateTypeDef = TypedDict(
    "ListAudienceGenerationJobsRequestListAudienceGenerationJobsPaginateTypeDef",
    {
        "collaborationId": NotRequired[str],
        "configuredAudienceModelArn": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListAudienceModelsRequestListAudienceModelsPaginateTypeDef = TypedDict(
    "ListAudienceModelsRequestListAudienceModelsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListConfiguredAudienceModelsRequestListConfiguredAudienceModelsPaginateTypeDef = TypedDict(
    "ListConfiguredAudienceModelsRequestListConfiguredAudienceModelsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListTrainingDatasetsRequestListTrainingDatasetsPaginateTypeDef = TypedDict(
    "ListTrainingDatasetsRequestListTrainingDatasetsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListTrainingDatasetsResponseTypeDef = TypedDict(
    "ListTrainingDatasetsResponseTypeDef",
    {
        "nextToken": str,
        "trainingDatasets": List[TrainingDatasetSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ConfiguredAudienceModelOutputConfigTypeDef = TypedDict(
    "ConfiguredAudienceModelOutputConfigTypeDef",
    {
        "destination": AudienceDestinationTypeDef,
        "roleArn": str,
    },
)
StartAudienceGenerationJobRequestRequestTypeDef = TypedDict(
    "StartAudienceGenerationJobRequestRequestTypeDef",
    {
        "configuredAudienceModelArn": str,
        "name": str,
        "seedAudience": AudienceGenerationJobDataSourceTypeDef,
        "collaborationId": NotRequired[str],
        "description": NotRequired[str],
        "includeSeedInOutput": NotRequired[bool],
        "tags": NotRequired[Mapping[str, str]],
    },
)
AudienceQualityMetricsTypeDef = TypedDict(
    "AudienceQualityMetricsTypeDef",
    {
        "relevanceMetrics": List[RelevanceMetricTypeDef],
    },
)
ListAudienceExportJobsResponseTypeDef = TypedDict(
    "ListAudienceExportJobsResponseTypeDef",
    {
        "audienceExportJobs": List[AudienceExportJobSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DatasetInputConfigTypeDef = TypedDict(
    "DatasetInputConfigTypeDef",
    {
        "dataSource": DataSourceTypeDef,
        "schema": Sequence[ColumnSchemaTypeDef],
    },
)
ConfiguredAudienceModelSummaryTypeDef = TypedDict(
    "ConfiguredAudienceModelSummaryTypeDef",
    {
        "audienceModelArn": str,
        "configuredAudienceModelArn": str,
        "createTime": datetime,
        "name": str,
        "outputConfig": ConfiguredAudienceModelOutputConfigTypeDef,
        "status": Literal["ACTIVE"],
        "updateTime": datetime,
        "description": NotRequired[str],
    },
)
CreateConfiguredAudienceModelRequestRequestTypeDef = TypedDict(
    "CreateConfiguredAudienceModelRequestRequestTypeDef",
    {
        "audienceModelArn": str,
        "name": str,
        "outputConfig": ConfiguredAudienceModelOutputConfigTypeDef,
        "sharedAudienceMetrics": Sequence[SharedAudienceMetricsType],
        "audienceSizeConfig": NotRequired[AudienceSizeConfigTypeDef],
        "childResourceTagOnCreatePolicy": NotRequired[TagOnCreatePolicyType],
        "description": NotRequired[str],
        "minMatchingSeedSize": NotRequired[int],
        "tags": NotRequired[Mapping[str, str]],
    },
)
GetConfiguredAudienceModelResponseTypeDef = TypedDict(
    "GetConfiguredAudienceModelResponseTypeDef",
    {
        "audienceModelArn": str,
        "audienceSizeConfig": AudienceSizeConfigTypeDef,
        "childResourceTagOnCreatePolicy": TagOnCreatePolicyType,
        "configuredAudienceModelArn": str,
        "createTime": datetime,
        "description": str,
        "minMatchingSeedSize": int,
        "name": str,
        "outputConfig": ConfiguredAudienceModelOutputConfigTypeDef,
        "sharedAudienceMetrics": List[SharedAudienceMetricsType],
        "status": Literal["ACTIVE"],
        "tags": Dict[str, str],
        "updateTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateConfiguredAudienceModelRequestRequestTypeDef = TypedDict(
    "UpdateConfiguredAudienceModelRequestRequestTypeDef",
    {
        "configuredAudienceModelArn": str,
        "audienceModelArn": NotRequired[str],
        "audienceSizeConfig": NotRequired[AudienceSizeConfigTypeDef],
        "description": NotRequired[str],
        "minMatchingSeedSize": NotRequired[int],
        "outputConfig": NotRequired[ConfiguredAudienceModelOutputConfigTypeDef],
        "sharedAudienceMetrics": NotRequired[Sequence[SharedAudienceMetricsType]],
    },
)
GetAudienceGenerationJobResponseTypeDef = TypedDict(
    "GetAudienceGenerationJobResponseTypeDef",
    {
        "audienceGenerationJobArn": str,
        "collaborationId": str,
        "configuredAudienceModelArn": str,
        "createTime": datetime,
        "description": str,
        "includeSeedInOutput": bool,
        "metrics": AudienceQualityMetricsTypeDef,
        "name": str,
        "seedAudience": AudienceGenerationJobDataSourceTypeDef,
        "startedBy": str,
        "status": AudienceGenerationJobStatusType,
        "statusDetails": StatusDetailsTypeDef,
        "tags": Dict[str, str],
        "updateTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DatasetTypeDef = TypedDict(
    "DatasetTypeDef",
    {
        "inputConfig": DatasetInputConfigTypeDef,
        "type": Literal["INTERACTIONS"],
    },
)
ListConfiguredAudienceModelsResponseTypeDef = TypedDict(
    "ListConfiguredAudienceModelsResponseTypeDef",
    {
        "configuredAudienceModels": List[ConfiguredAudienceModelSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateTrainingDatasetRequestRequestTypeDef = TypedDict(
    "CreateTrainingDatasetRequestRequestTypeDef",
    {
        "name": str,
        "roleArn": str,
        "trainingData": Sequence[DatasetTypeDef],
        "description": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)
GetTrainingDatasetResponseTypeDef = TypedDict(
    "GetTrainingDatasetResponseTypeDef",
    {
        "createTime": datetime,
        "description": str,
        "name": str,
        "roleArn": str,
        "status": Literal["ACTIVE"],
        "tags": Dict[str, str],
        "trainingData": List[DatasetTypeDef],
        "trainingDatasetArn": str,
        "updateTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
