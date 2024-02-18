"""
Type annotations for bedrock service type definitions.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_bedrock/type_defs/)

Usage::

    ```python
    from types_aiobotocore_bedrock.type_defs import S3ConfigTypeDef

    data: S3ConfigTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from .literals import (
    CommitmentDurationType,
    CustomizationTypeType,
    FineTuningJobStatusType,
    FoundationModelLifecycleStatusType,
    InferenceTypeType,
    ModelCustomizationJobStatusType,
    ModelCustomizationType,
    ModelModalityType,
    ProvisionedModelStatusType,
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
    "S3ConfigTypeDef",
    "OutputDataConfigTypeDef",
    "TagTypeDef",
    "TrainingDataConfigTypeDef",
    "VpcConfigTypeDef",
    "ResponseMetadataTypeDef",
    "CustomModelSummaryTypeDef",
    "DeleteCustomModelRequestRequestTypeDef",
    "DeleteProvisionedModelThroughputRequestRequestTypeDef",
    "FoundationModelLifecycleTypeDef",
    "GetCustomModelRequestRequestTypeDef",
    "TrainingMetricsTypeDef",
    "ValidatorMetricTypeDef",
    "GetFoundationModelRequestRequestTypeDef",
    "GetModelCustomizationJobRequestRequestTypeDef",
    "GetProvisionedModelThroughputRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "TimestampTypeDef",
    "ListFoundationModelsRequestRequestTypeDef",
    "ModelCustomizationJobSummaryTypeDef",
    "ProvisionedModelSummaryTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "StopModelCustomizationJobRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateProvisionedModelThroughputRequestRequestTypeDef",
    "ValidatorTypeDef",
    "CloudWatchConfigTypeDef",
    "CreateProvisionedModelThroughputRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "CreateModelCustomizationJobResponseTypeDef",
    "CreateProvisionedModelThroughputResponseTypeDef",
    "GetProvisionedModelThroughputResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListCustomModelsResponseTypeDef",
    "FoundationModelDetailsTypeDef",
    "FoundationModelSummaryTypeDef",
    "ListCustomModelsRequestListCustomModelsPaginateTypeDef",
    "ListCustomModelsRequestRequestTypeDef",
    "ListModelCustomizationJobsRequestListModelCustomizationJobsPaginateTypeDef",
    "ListModelCustomizationJobsRequestRequestTypeDef",
    "ListProvisionedModelThroughputsRequestListProvisionedModelThroughputsPaginateTypeDef",
    "ListProvisionedModelThroughputsRequestRequestTypeDef",
    "ListModelCustomizationJobsResponseTypeDef",
    "ListProvisionedModelThroughputsResponseTypeDef",
    "ValidationDataConfigTypeDef",
    "LoggingConfigTypeDef",
    "GetFoundationModelResponseTypeDef",
    "ListFoundationModelsResponseTypeDef",
    "CreateModelCustomizationJobRequestRequestTypeDef",
    "GetCustomModelResponseTypeDef",
    "GetModelCustomizationJobResponseTypeDef",
    "GetModelInvocationLoggingConfigurationResponseTypeDef",
    "PutModelInvocationLoggingConfigurationRequestRequestTypeDef",
)

S3ConfigTypeDef = TypedDict(
    "S3ConfigTypeDef",
    {
        "bucketName": str,
        "keyPrefix": NotRequired[str],
    },
)
OutputDataConfigTypeDef = TypedDict(
    "OutputDataConfigTypeDef",
    {
        "s3Uri": str,
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "key": str,
        "value": str,
    },
)
TrainingDataConfigTypeDef = TypedDict(
    "TrainingDataConfigTypeDef",
    {
        "s3Uri": str,
    },
)
VpcConfigTypeDef = TypedDict(
    "VpcConfigTypeDef",
    {
        "subnetIds": Sequence[str],
        "securityGroupIds": Sequence[str],
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
CustomModelSummaryTypeDef = TypedDict(
    "CustomModelSummaryTypeDef",
    {
        "modelArn": str,
        "modelName": str,
        "creationTime": datetime,
        "baseModelArn": str,
        "baseModelName": str,
        "customizationType": NotRequired[CustomizationTypeType],
    },
)
DeleteCustomModelRequestRequestTypeDef = TypedDict(
    "DeleteCustomModelRequestRequestTypeDef",
    {
        "modelIdentifier": str,
    },
)
DeleteProvisionedModelThroughputRequestRequestTypeDef = TypedDict(
    "DeleteProvisionedModelThroughputRequestRequestTypeDef",
    {
        "provisionedModelId": str,
    },
)
FoundationModelLifecycleTypeDef = TypedDict(
    "FoundationModelLifecycleTypeDef",
    {
        "status": FoundationModelLifecycleStatusType,
    },
)
GetCustomModelRequestRequestTypeDef = TypedDict(
    "GetCustomModelRequestRequestTypeDef",
    {
        "modelIdentifier": str,
    },
)
TrainingMetricsTypeDef = TypedDict(
    "TrainingMetricsTypeDef",
    {
        "trainingLoss": NotRequired[float],
    },
)
ValidatorMetricTypeDef = TypedDict(
    "ValidatorMetricTypeDef",
    {
        "validationLoss": NotRequired[float],
    },
)
GetFoundationModelRequestRequestTypeDef = TypedDict(
    "GetFoundationModelRequestRequestTypeDef",
    {
        "modelIdentifier": str,
    },
)
GetModelCustomizationJobRequestRequestTypeDef = TypedDict(
    "GetModelCustomizationJobRequestRequestTypeDef",
    {
        "jobIdentifier": str,
    },
)
GetProvisionedModelThroughputRequestRequestTypeDef = TypedDict(
    "GetProvisionedModelThroughputRequestRequestTypeDef",
    {
        "provisionedModelId": str,
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
TimestampTypeDef = Union[datetime, str]
ListFoundationModelsRequestRequestTypeDef = TypedDict(
    "ListFoundationModelsRequestRequestTypeDef",
    {
        "byProvider": NotRequired[str],
        "byCustomizationType": NotRequired[ModelCustomizationType],
        "byOutputModality": NotRequired[ModelModalityType],
        "byInferenceType": NotRequired[InferenceTypeType],
    },
)
ModelCustomizationJobSummaryTypeDef = TypedDict(
    "ModelCustomizationJobSummaryTypeDef",
    {
        "jobArn": str,
        "baseModelArn": str,
        "jobName": str,
        "status": ModelCustomizationJobStatusType,
        "creationTime": datetime,
        "lastModifiedTime": NotRequired[datetime],
        "endTime": NotRequired[datetime],
        "customModelArn": NotRequired[str],
        "customModelName": NotRequired[str],
        "customizationType": NotRequired[CustomizationTypeType],
    },
)
ProvisionedModelSummaryTypeDef = TypedDict(
    "ProvisionedModelSummaryTypeDef",
    {
        "provisionedModelName": str,
        "provisionedModelArn": str,
        "modelArn": str,
        "desiredModelArn": str,
        "foundationModelArn": str,
        "modelUnits": int,
        "desiredModelUnits": int,
        "status": ProvisionedModelStatusType,
        "creationTime": datetime,
        "lastModifiedTime": datetime,
        "commitmentDuration": NotRequired[CommitmentDurationType],
        "commitmentExpirationTime": NotRequired[datetime],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceARN": str,
    },
)
StopModelCustomizationJobRequestRequestTypeDef = TypedDict(
    "StopModelCustomizationJobRequestRequestTypeDef",
    {
        "jobIdentifier": str,
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceARN": str,
        "tagKeys": Sequence[str],
    },
)
UpdateProvisionedModelThroughputRequestRequestTypeDef = TypedDict(
    "UpdateProvisionedModelThroughputRequestRequestTypeDef",
    {
        "provisionedModelId": str,
        "desiredProvisionedModelName": NotRequired[str],
        "desiredModelId": NotRequired[str],
    },
)
ValidatorTypeDef = TypedDict(
    "ValidatorTypeDef",
    {
        "s3Uri": str,
    },
)
CloudWatchConfigTypeDef = TypedDict(
    "CloudWatchConfigTypeDef",
    {
        "logGroupName": str,
        "roleArn": str,
        "largeDataDeliveryS3Config": NotRequired[S3ConfigTypeDef],
    },
)
CreateProvisionedModelThroughputRequestRequestTypeDef = TypedDict(
    "CreateProvisionedModelThroughputRequestRequestTypeDef",
    {
        "modelUnits": int,
        "provisionedModelName": str,
        "modelId": str,
        "clientRequestToken": NotRequired[str],
        "commitmentDuration": NotRequired[CommitmentDurationType],
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceARN": str,
        "tags": Sequence[TagTypeDef],
    },
)
CreateModelCustomizationJobResponseTypeDef = TypedDict(
    "CreateModelCustomizationJobResponseTypeDef",
    {
        "jobArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateProvisionedModelThroughputResponseTypeDef = TypedDict(
    "CreateProvisionedModelThroughputResponseTypeDef",
    {
        "provisionedModelArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetProvisionedModelThroughputResponseTypeDef = TypedDict(
    "GetProvisionedModelThroughputResponseTypeDef",
    {
        "modelUnits": int,
        "desiredModelUnits": int,
        "provisionedModelName": str,
        "provisionedModelArn": str,
        "modelArn": str,
        "desiredModelArn": str,
        "foundationModelArn": str,
        "status": ProvisionedModelStatusType,
        "creationTime": datetime,
        "lastModifiedTime": datetime,
        "failureMessage": str,
        "commitmentDuration": CommitmentDurationType,
        "commitmentExpirationTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListCustomModelsResponseTypeDef = TypedDict(
    "ListCustomModelsResponseTypeDef",
    {
        "nextToken": str,
        "modelSummaries": List[CustomModelSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
FoundationModelDetailsTypeDef = TypedDict(
    "FoundationModelDetailsTypeDef",
    {
        "modelArn": str,
        "modelId": str,
        "modelName": NotRequired[str],
        "providerName": NotRequired[str],
        "inputModalities": NotRequired[List[ModelModalityType]],
        "outputModalities": NotRequired[List[ModelModalityType]],
        "responseStreamingSupported": NotRequired[bool],
        "customizationsSupported": NotRequired[List[ModelCustomizationType]],
        "inferenceTypesSupported": NotRequired[List[InferenceTypeType]],
        "modelLifecycle": NotRequired[FoundationModelLifecycleTypeDef],
    },
)
FoundationModelSummaryTypeDef = TypedDict(
    "FoundationModelSummaryTypeDef",
    {
        "modelArn": str,
        "modelId": str,
        "modelName": NotRequired[str],
        "providerName": NotRequired[str],
        "inputModalities": NotRequired[List[ModelModalityType]],
        "outputModalities": NotRequired[List[ModelModalityType]],
        "responseStreamingSupported": NotRequired[bool],
        "customizationsSupported": NotRequired[List[ModelCustomizationType]],
        "inferenceTypesSupported": NotRequired[List[InferenceTypeType]],
        "modelLifecycle": NotRequired[FoundationModelLifecycleTypeDef],
    },
)
ListCustomModelsRequestListCustomModelsPaginateTypeDef = TypedDict(
    "ListCustomModelsRequestListCustomModelsPaginateTypeDef",
    {
        "creationTimeBefore": NotRequired[TimestampTypeDef],
        "creationTimeAfter": NotRequired[TimestampTypeDef],
        "nameContains": NotRequired[str],
        "baseModelArnEquals": NotRequired[str],
        "foundationModelArnEquals": NotRequired[str],
        "sortBy": NotRequired[Literal["CreationTime"]],
        "sortOrder": NotRequired[SortOrderType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListCustomModelsRequestRequestTypeDef = TypedDict(
    "ListCustomModelsRequestRequestTypeDef",
    {
        "creationTimeBefore": NotRequired[TimestampTypeDef],
        "creationTimeAfter": NotRequired[TimestampTypeDef],
        "nameContains": NotRequired[str],
        "baseModelArnEquals": NotRequired[str],
        "foundationModelArnEquals": NotRequired[str],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "sortBy": NotRequired[Literal["CreationTime"]],
        "sortOrder": NotRequired[SortOrderType],
    },
)
ListModelCustomizationJobsRequestListModelCustomizationJobsPaginateTypeDef = TypedDict(
    "ListModelCustomizationJobsRequestListModelCustomizationJobsPaginateTypeDef",
    {
        "creationTimeAfter": NotRequired[TimestampTypeDef],
        "creationTimeBefore": NotRequired[TimestampTypeDef],
        "statusEquals": NotRequired[FineTuningJobStatusType],
        "nameContains": NotRequired[str],
        "sortBy": NotRequired[Literal["CreationTime"]],
        "sortOrder": NotRequired[SortOrderType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListModelCustomizationJobsRequestRequestTypeDef = TypedDict(
    "ListModelCustomizationJobsRequestRequestTypeDef",
    {
        "creationTimeAfter": NotRequired[TimestampTypeDef],
        "creationTimeBefore": NotRequired[TimestampTypeDef],
        "statusEquals": NotRequired[FineTuningJobStatusType],
        "nameContains": NotRequired[str],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "sortBy": NotRequired[Literal["CreationTime"]],
        "sortOrder": NotRequired[SortOrderType],
    },
)
ListProvisionedModelThroughputsRequestListProvisionedModelThroughputsPaginateTypeDef = TypedDict(
    "ListProvisionedModelThroughputsRequestListProvisionedModelThroughputsPaginateTypeDef",
    {
        "creationTimeAfter": NotRequired[TimestampTypeDef],
        "creationTimeBefore": NotRequired[TimestampTypeDef],
        "statusEquals": NotRequired[ProvisionedModelStatusType],
        "modelArnEquals": NotRequired[str],
        "nameContains": NotRequired[str],
        "sortBy": NotRequired[Literal["CreationTime"]],
        "sortOrder": NotRequired[SortOrderType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListProvisionedModelThroughputsRequestRequestTypeDef = TypedDict(
    "ListProvisionedModelThroughputsRequestRequestTypeDef",
    {
        "creationTimeAfter": NotRequired[TimestampTypeDef],
        "creationTimeBefore": NotRequired[TimestampTypeDef],
        "statusEquals": NotRequired[ProvisionedModelStatusType],
        "modelArnEquals": NotRequired[str],
        "nameContains": NotRequired[str],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "sortBy": NotRequired[Literal["CreationTime"]],
        "sortOrder": NotRequired[SortOrderType],
    },
)
ListModelCustomizationJobsResponseTypeDef = TypedDict(
    "ListModelCustomizationJobsResponseTypeDef",
    {
        "nextToken": str,
        "modelCustomizationJobSummaries": List[ModelCustomizationJobSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListProvisionedModelThroughputsResponseTypeDef = TypedDict(
    "ListProvisionedModelThroughputsResponseTypeDef",
    {
        "nextToken": str,
        "provisionedModelSummaries": List[ProvisionedModelSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ValidationDataConfigTypeDef = TypedDict(
    "ValidationDataConfigTypeDef",
    {
        "validators": Sequence[ValidatorTypeDef],
    },
)
LoggingConfigTypeDef = TypedDict(
    "LoggingConfigTypeDef",
    {
        "cloudWatchConfig": NotRequired[CloudWatchConfigTypeDef],
        "s3Config": NotRequired[S3ConfigTypeDef],
        "textDataDeliveryEnabled": NotRequired[bool],
        "imageDataDeliveryEnabled": NotRequired[bool],
        "embeddingDataDeliveryEnabled": NotRequired[bool],
    },
)
GetFoundationModelResponseTypeDef = TypedDict(
    "GetFoundationModelResponseTypeDef",
    {
        "modelDetails": FoundationModelDetailsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListFoundationModelsResponseTypeDef = TypedDict(
    "ListFoundationModelsResponseTypeDef",
    {
        "modelSummaries": List[FoundationModelSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateModelCustomizationJobRequestRequestTypeDef = TypedDict(
    "CreateModelCustomizationJobRequestRequestTypeDef",
    {
        "jobName": str,
        "customModelName": str,
        "roleArn": str,
        "baseModelIdentifier": str,
        "trainingDataConfig": TrainingDataConfigTypeDef,
        "outputDataConfig": OutputDataConfigTypeDef,
        "hyperParameters": Mapping[str, str],
        "clientRequestToken": NotRequired[str],
        "customizationType": NotRequired[CustomizationTypeType],
        "customModelKmsKeyId": NotRequired[str],
        "jobTags": NotRequired[Sequence[TagTypeDef]],
        "customModelTags": NotRequired[Sequence[TagTypeDef]],
        "validationDataConfig": NotRequired[ValidationDataConfigTypeDef],
        "vpcConfig": NotRequired[VpcConfigTypeDef],
    },
)
GetCustomModelResponseTypeDef = TypedDict(
    "GetCustomModelResponseTypeDef",
    {
        "modelArn": str,
        "modelName": str,
        "jobName": str,
        "jobArn": str,
        "baseModelArn": str,
        "customizationType": CustomizationTypeType,
        "modelKmsKeyArn": str,
        "hyperParameters": Dict[str, str],
        "trainingDataConfig": TrainingDataConfigTypeDef,
        "validationDataConfig": ValidationDataConfigTypeDef,
        "outputDataConfig": OutputDataConfigTypeDef,
        "trainingMetrics": TrainingMetricsTypeDef,
        "validationMetrics": List[ValidatorMetricTypeDef],
        "creationTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetModelCustomizationJobResponseTypeDef = TypedDict(
    "GetModelCustomizationJobResponseTypeDef",
    {
        "jobArn": str,
        "jobName": str,
        "outputModelName": str,
        "outputModelArn": str,
        "clientRequestToken": str,
        "roleArn": str,
        "status": ModelCustomizationJobStatusType,
        "failureMessage": str,
        "creationTime": datetime,
        "lastModifiedTime": datetime,
        "endTime": datetime,
        "baseModelArn": str,
        "hyperParameters": Dict[str, str],
        "trainingDataConfig": TrainingDataConfigTypeDef,
        "validationDataConfig": ValidationDataConfigTypeDef,
        "outputDataConfig": OutputDataConfigTypeDef,
        "customizationType": CustomizationTypeType,
        "outputModelKmsKeyArn": str,
        "trainingMetrics": TrainingMetricsTypeDef,
        "validationMetrics": List[ValidatorMetricTypeDef],
        "vpcConfig": VpcConfigTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetModelInvocationLoggingConfigurationResponseTypeDef = TypedDict(
    "GetModelInvocationLoggingConfigurationResponseTypeDef",
    {
        "loggingConfig": LoggingConfigTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutModelInvocationLoggingConfigurationRequestRequestTypeDef = TypedDict(
    "PutModelInvocationLoggingConfigurationRequestRequestTypeDef",
    {
        "loggingConfig": LoggingConfigTypeDef,
    },
)
