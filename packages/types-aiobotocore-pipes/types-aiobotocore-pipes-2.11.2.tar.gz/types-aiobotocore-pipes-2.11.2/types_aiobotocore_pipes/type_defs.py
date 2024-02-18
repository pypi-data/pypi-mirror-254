"""
Type annotations for pipes service type definitions.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pipes/type_defs/)

Usage::

    ```python
    from types_aiobotocore_pipes.type_defs import AwsVpcConfigurationTypeDef

    data: AwsVpcConfigurationTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from .literals import (
    AssignPublicIpType,
    BatchJobDependencyTypeType,
    BatchResourceRequirementTypeType,
    DynamoDBStreamStartPositionType,
    EcsResourceRequirementTypeType,
    KinesisStreamStartPositionType,
    LaunchTypeType,
    LogLevelType,
    MSKStartPositionType,
    PipeStateType,
    PipeTargetInvocationTypeType,
    PlacementConstraintTypeType,
    PlacementStrategyTypeType,
    RequestedPipeStateDescribeResponseType,
    RequestedPipeStateType,
    S3OutputFormatType,
    SelfManagedKafkaStartPositionType,
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
    "AwsVpcConfigurationTypeDef",
    "BatchArrayPropertiesTypeDef",
    "BatchEnvironmentVariableTypeDef",
    "BatchResourceRequirementTypeDef",
    "BatchJobDependencyTypeDef",
    "BatchRetryStrategyTypeDef",
    "CapacityProviderStrategyItemTypeDef",
    "CloudwatchLogsLogDestinationParametersTypeDef",
    "CloudwatchLogsLogDestinationTypeDef",
    "ResponseMetadataTypeDef",
    "DeadLetterConfigTypeDef",
    "DeletePipeRequestRequestTypeDef",
    "DescribePipeRequestRequestTypeDef",
    "EcsEnvironmentFileTypeDef",
    "EcsEnvironmentVariableTypeDef",
    "EcsResourceRequirementTypeDef",
    "EcsEphemeralStorageTypeDef",
    "EcsInferenceAcceleratorOverrideTypeDef",
    "FilterTypeDef",
    "FirehoseLogDestinationParametersTypeDef",
    "FirehoseLogDestinationTypeDef",
    "PaginatorConfigTypeDef",
    "ListPipesRequestRequestTypeDef",
    "PipeTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "MQBrokerAccessCredentialsTypeDef",
    "MSKAccessCredentialsTypeDef",
    "PipeEnrichmentHttpParametersTypeDef",
    "S3LogDestinationParametersTypeDef",
    "S3LogDestinationTypeDef",
    "TimestampTypeDef",
    "PipeSourceSqsQueueParametersTypeDef",
    "SelfManagedKafkaAccessConfigurationCredentialsTypeDef",
    "SelfManagedKafkaAccessConfigurationVpcTypeDef",
    "PipeTargetCloudWatchLogsParametersTypeDef",
    "PlacementConstraintTypeDef",
    "PlacementStrategyTypeDef",
    "TagTypeDef",
    "PipeTargetEventBridgeEventBusParametersTypeDef",
    "PipeTargetHttpParametersTypeDef",
    "PipeTargetKinesisStreamParametersTypeDef",
    "PipeTargetLambdaFunctionParametersTypeDef",
    "PipeTargetRedshiftDataParametersTypeDef",
    "PipeTargetSqsQueueParametersTypeDef",
    "PipeTargetStateMachineParametersTypeDef",
    "SageMakerPipelineParameterTypeDef",
    "StartPipeRequestRequestTypeDef",
    "StopPipeRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdatePipeSourceSqsQueueParametersTypeDef",
    "NetworkConfigurationTypeDef",
    "BatchContainerOverridesTypeDef",
    "CreatePipeResponseTypeDef",
    "DeletePipeResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "StartPipeResponseTypeDef",
    "StopPipeResponseTypeDef",
    "UpdatePipeResponseTypeDef",
    "PipeSourceDynamoDBStreamParametersTypeDef",
    "UpdatePipeSourceDynamoDBStreamParametersTypeDef",
    "UpdatePipeSourceKinesisStreamParametersTypeDef",
    "EcsContainerOverrideTypeDef",
    "FilterCriteriaTypeDef",
    "ListPipesRequestListPipesPaginateTypeDef",
    "ListPipesResponseTypeDef",
    "PipeSourceActiveMQBrokerParametersTypeDef",
    "PipeSourceRabbitMQBrokerParametersTypeDef",
    "UpdatePipeSourceActiveMQBrokerParametersTypeDef",
    "UpdatePipeSourceRabbitMQBrokerParametersTypeDef",
    "PipeSourceManagedStreamingKafkaParametersTypeDef",
    "UpdatePipeSourceManagedStreamingKafkaParametersTypeDef",
    "PipeEnrichmentParametersTypeDef",
    "PipeLogConfigurationParametersTypeDef",
    "PipeLogConfigurationTypeDef",
    "PipeSourceKinesisStreamParametersTypeDef",
    "PipeSourceSelfManagedKafkaParametersTypeDef",
    "UpdatePipeSourceSelfManagedKafkaParametersTypeDef",
    "PipeTargetSageMakerPipelineParametersTypeDef",
    "PipeTargetBatchJobParametersTypeDef",
    "EcsTaskOverrideTypeDef",
    "PipeSourceParametersTypeDef",
    "UpdatePipeSourceParametersTypeDef",
    "PipeTargetEcsTaskParametersTypeDef",
    "PipeTargetParametersTypeDef",
    "CreatePipeRequestRequestTypeDef",
    "DescribePipeResponseTypeDef",
    "UpdatePipeRequestRequestTypeDef",
)

AwsVpcConfigurationTypeDef = TypedDict(
    "AwsVpcConfigurationTypeDef",
    {
        "Subnets": Sequence[str],
        "AssignPublicIp": NotRequired[AssignPublicIpType],
        "SecurityGroups": NotRequired[Sequence[str]],
    },
)
BatchArrayPropertiesTypeDef = TypedDict(
    "BatchArrayPropertiesTypeDef",
    {
        "Size": NotRequired[int],
    },
)
BatchEnvironmentVariableTypeDef = TypedDict(
    "BatchEnvironmentVariableTypeDef",
    {
        "Name": NotRequired[str],
        "Value": NotRequired[str],
    },
)
BatchResourceRequirementTypeDef = TypedDict(
    "BatchResourceRequirementTypeDef",
    {
        "Type": BatchResourceRequirementTypeType,
        "Value": str,
    },
)
BatchJobDependencyTypeDef = TypedDict(
    "BatchJobDependencyTypeDef",
    {
        "JobId": NotRequired[str],
        "Type": NotRequired[BatchJobDependencyTypeType],
    },
)
BatchRetryStrategyTypeDef = TypedDict(
    "BatchRetryStrategyTypeDef",
    {
        "Attempts": NotRequired[int],
    },
)
CapacityProviderStrategyItemTypeDef = TypedDict(
    "CapacityProviderStrategyItemTypeDef",
    {
        "capacityProvider": str,
        "base": NotRequired[int],
        "weight": NotRequired[int],
    },
)
CloudwatchLogsLogDestinationParametersTypeDef = TypedDict(
    "CloudwatchLogsLogDestinationParametersTypeDef",
    {
        "LogGroupArn": str,
    },
)
CloudwatchLogsLogDestinationTypeDef = TypedDict(
    "CloudwatchLogsLogDestinationTypeDef",
    {
        "LogGroupArn": NotRequired[str],
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
DeadLetterConfigTypeDef = TypedDict(
    "DeadLetterConfigTypeDef",
    {
        "Arn": NotRequired[str],
    },
)
DeletePipeRequestRequestTypeDef = TypedDict(
    "DeletePipeRequestRequestTypeDef",
    {
        "Name": str,
    },
)
DescribePipeRequestRequestTypeDef = TypedDict(
    "DescribePipeRequestRequestTypeDef",
    {
        "Name": str,
    },
)
EcsEnvironmentFileTypeDef = TypedDict(
    "EcsEnvironmentFileTypeDef",
    {
        "type": Literal["s3"],
        "value": str,
    },
)
EcsEnvironmentVariableTypeDef = TypedDict(
    "EcsEnvironmentVariableTypeDef",
    {
        "name": NotRequired[str],
        "value": NotRequired[str],
    },
)
EcsResourceRequirementTypeDef = TypedDict(
    "EcsResourceRequirementTypeDef",
    {
        "type": EcsResourceRequirementTypeType,
        "value": str,
    },
)
EcsEphemeralStorageTypeDef = TypedDict(
    "EcsEphemeralStorageTypeDef",
    {
        "sizeInGiB": int,
    },
)
EcsInferenceAcceleratorOverrideTypeDef = TypedDict(
    "EcsInferenceAcceleratorOverrideTypeDef",
    {
        "deviceName": NotRequired[str],
        "deviceType": NotRequired[str],
    },
)
FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "Pattern": NotRequired[str],
    },
)
FirehoseLogDestinationParametersTypeDef = TypedDict(
    "FirehoseLogDestinationParametersTypeDef",
    {
        "DeliveryStreamArn": str,
    },
)
FirehoseLogDestinationTypeDef = TypedDict(
    "FirehoseLogDestinationTypeDef",
    {
        "DeliveryStreamArn": NotRequired[str],
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
ListPipesRequestRequestTypeDef = TypedDict(
    "ListPipesRequestRequestTypeDef",
    {
        "CurrentState": NotRequired[PipeStateType],
        "DesiredState": NotRequired[RequestedPipeStateType],
        "Limit": NotRequired[int],
        "NamePrefix": NotRequired[str],
        "NextToken": NotRequired[str],
        "SourcePrefix": NotRequired[str],
        "TargetPrefix": NotRequired[str],
    },
)
PipeTypeDef = TypedDict(
    "PipeTypeDef",
    {
        "Arn": NotRequired[str],
        "CreationTime": NotRequired[datetime],
        "CurrentState": NotRequired[PipeStateType],
        "DesiredState": NotRequired[RequestedPipeStateType],
        "Enrichment": NotRequired[str],
        "LastModifiedTime": NotRequired[datetime],
        "Name": NotRequired[str],
        "Source": NotRequired[str],
        "StateReason": NotRequired[str],
        "Target": NotRequired[str],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)
MQBrokerAccessCredentialsTypeDef = TypedDict(
    "MQBrokerAccessCredentialsTypeDef",
    {
        "BasicAuth": NotRequired[str],
    },
)
MSKAccessCredentialsTypeDef = TypedDict(
    "MSKAccessCredentialsTypeDef",
    {
        "ClientCertificateTlsAuth": NotRequired[str],
        "SaslScram512Auth": NotRequired[str],
    },
)
PipeEnrichmentHttpParametersTypeDef = TypedDict(
    "PipeEnrichmentHttpParametersTypeDef",
    {
        "HeaderParameters": NotRequired[Mapping[str, str]],
        "PathParameterValues": NotRequired[Sequence[str]],
        "QueryStringParameters": NotRequired[Mapping[str, str]],
    },
)
S3LogDestinationParametersTypeDef = TypedDict(
    "S3LogDestinationParametersTypeDef",
    {
        "BucketName": str,
        "BucketOwner": str,
        "OutputFormat": NotRequired[S3OutputFormatType],
        "Prefix": NotRequired[str],
    },
)
S3LogDestinationTypeDef = TypedDict(
    "S3LogDestinationTypeDef",
    {
        "BucketName": NotRequired[str],
        "BucketOwner": NotRequired[str],
        "OutputFormat": NotRequired[S3OutputFormatType],
        "Prefix": NotRequired[str],
    },
)
TimestampTypeDef = Union[datetime, str]
PipeSourceSqsQueueParametersTypeDef = TypedDict(
    "PipeSourceSqsQueueParametersTypeDef",
    {
        "BatchSize": NotRequired[int],
        "MaximumBatchingWindowInSeconds": NotRequired[int],
    },
)
SelfManagedKafkaAccessConfigurationCredentialsTypeDef = TypedDict(
    "SelfManagedKafkaAccessConfigurationCredentialsTypeDef",
    {
        "BasicAuth": NotRequired[str],
        "ClientCertificateTlsAuth": NotRequired[str],
        "SaslScram256Auth": NotRequired[str],
        "SaslScram512Auth": NotRequired[str],
    },
)
SelfManagedKafkaAccessConfigurationVpcTypeDef = TypedDict(
    "SelfManagedKafkaAccessConfigurationVpcTypeDef",
    {
        "SecurityGroup": NotRequired[Sequence[str]],
        "Subnets": NotRequired[Sequence[str]],
    },
)
PipeTargetCloudWatchLogsParametersTypeDef = TypedDict(
    "PipeTargetCloudWatchLogsParametersTypeDef",
    {
        "LogStreamName": NotRequired[str],
        "Timestamp": NotRequired[str],
    },
)
PlacementConstraintTypeDef = TypedDict(
    "PlacementConstraintTypeDef",
    {
        "expression": NotRequired[str],
        "type": NotRequired[PlacementConstraintTypeType],
    },
)
PlacementStrategyTypeDef = TypedDict(
    "PlacementStrategyTypeDef",
    {
        "field": NotRequired[str],
        "type": NotRequired[PlacementStrategyTypeType],
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)
PipeTargetEventBridgeEventBusParametersTypeDef = TypedDict(
    "PipeTargetEventBridgeEventBusParametersTypeDef",
    {
        "DetailType": NotRequired[str],
        "EndpointId": NotRequired[str],
        "Resources": NotRequired[Sequence[str]],
        "Source": NotRequired[str],
        "Time": NotRequired[str],
    },
)
PipeTargetHttpParametersTypeDef = TypedDict(
    "PipeTargetHttpParametersTypeDef",
    {
        "HeaderParameters": NotRequired[Mapping[str, str]],
        "PathParameterValues": NotRequired[Sequence[str]],
        "QueryStringParameters": NotRequired[Mapping[str, str]],
    },
)
PipeTargetKinesisStreamParametersTypeDef = TypedDict(
    "PipeTargetKinesisStreamParametersTypeDef",
    {
        "PartitionKey": str,
    },
)
PipeTargetLambdaFunctionParametersTypeDef = TypedDict(
    "PipeTargetLambdaFunctionParametersTypeDef",
    {
        "InvocationType": NotRequired[PipeTargetInvocationTypeType],
    },
)
PipeTargetRedshiftDataParametersTypeDef = TypedDict(
    "PipeTargetRedshiftDataParametersTypeDef",
    {
        "Database": str,
        "Sqls": Sequence[str],
        "DbUser": NotRequired[str],
        "SecretManagerArn": NotRequired[str],
        "StatementName": NotRequired[str],
        "WithEvent": NotRequired[bool],
    },
)
PipeTargetSqsQueueParametersTypeDef = TypedDict(
    "PipeTargetSqsQueueParametersTypeDef",
    {
        "MessageDeduplicationId": NotRequired[str],
        "MessageGroupId": NotRequired[str],
    },
)
PipeTargetStateMachineParametersTypeDef = TypedDict(
    "PipeTargetStateMachineParametersTypeDef",
    {
        "InvocationType": NotRequired[PipeTargetInvocationTypeType],
    },
)
SageMakerPipelineParameterTypeDef = TypedDict(
    "SageMakerPipelineParameterTypeDef",
    {
        "Name": str,
        "Value": str,
    },
)
StartPipeRequestRequestTypeDef = TypedDict(
    "StartPipeRequestRequestTypeDef",
    {
        "Name": str,
    },
)
StopPipeRequestRequestTypeDef = TypedDict(
    "StopPipeRequestRequestTypeDef",
    {
        "Name": str,
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
UpdatePipeSourceSqsQueueParametersTypeDef = TypedDict(
    "UpdatePipeSourceSqsQueueParametersTypeDef",
    {
        "BatchSize": NotRequired[int],
        "MaximumBatchingWindowInSeconds": NotRequired[int],
    },
)
NetworkConfigurationTypeDef = TypedDict(
    "NetworkConfigurationTypeDef",
    {
        "awsvpcConfiguration": NotRequired[AwsVpcConfigurationTypeDef],
    },
)
BatchContainerOverridesTypeDef = TypedDict(
    "BatchContainerOverridesTypeDef",
    {
        "Command": NotRequired[Sequence[str]],
        "Environment": NotRequired[Sequence[BatchEnvironmentVariableTypeDef]],
        "InstanceType": NotRequired[str],
        "ResourceRequirements": NotRequired[Sequence[BatchResourceRequirementTypeDef]],
    },
)
CreatePipeResponseTypeDef = TypedDict(
    "CreatePipeResponseTypeDef",
    {
        "Arn": str,
        "CreationTime": datetime,
        "CurrentState": PipeStateType,
        "DesiredState": RequestedPipeStateType,
        "LastModifiedTime": datetime,
        "Name": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeletePipeResponseTypeDef = TypedDict(
    "DeletePipeResponseTypeDef",
    {
        "Arn": str,
        "CreationTime": datetime,
        "CurrentState": PipeStateType,
        "DesiredState": RequestedPipeStateDescribeResponseType,
        "LastModifiedTime": datetime,
        "Name": str,
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
StartPipeResponseTypeDef = TypedDict(
    "StartPipeResponseTypeDef",
    {
        "Arn": str,
        "CreationTime": datetime,
        "CurrentState": PipeStateType,
        "DesiredState": RequestedPipeStateType,
        "LastModifiedTime": datetime,
        "Name": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StopPipeResponseTypeDef = TypedDict(
    "StopPipeResponseTypeDef",
    {
        "Arn": str,
        "CreationTime": datetime,
        "CurrentState": PipeStateType,
        "DesiredState": RequestedPipeStateType,
        "LastModifiedTime": datetime,
        "Name": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdatePipeResponseTypeDef = TypedDict(
    "UpdatePipeResponseTypeDef",
    {
        "Arn": str,
        "CreationTime": datetime,
        "CurrentState": PipeStateType,
        "DesiredState": RequestedPipeStateType,
        "LastModifiedTime": datetime,
        "Name": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PipeSourceDynamoDBStreamParametersTypeDef = TypedDict(
    "PipeSourceDynamoDBStreamParametersTypeDef",
    {
        "StartingPosition": DynamoDBStreamStartPositionType,
        "BatchSize": NotRequired[int],
        "DeadLetterConfig": NotRequired[DeadLetterConfigTypeDef],
        "MaximumBatchingWindowInSeconds": NotRequired[int],
        "MaximumRecordAgeInSeconds": NotRequired[int],
        "MaximumRetryAttempts": NotRequired[int],
        "OnPartialBatchItemFailure": NotRequired[Literal["AUTOMATIC_BISECT"]],
        "ParallelizationFactor": NotRequired[int],
    },
)
UpdatePipeSourceDynamoDBStreamParametersTypeDef = TypedDict(
    "UpdatePipeSourceDynamoDBStreamParametersTypeDef",
    {
        "BatchSize": NotRequired[int],
        "DeadLetterConfig": NotRequired[DeadLetterConfigTypeDef],
        "MaximumBatchingWindowInSeconds": NotRequired[int],
        "MaximumRecordAgeInSeconds": NotRequired[int],
        "MaximumRetryAttempts": NotRequired[int],
        "OnPartialBatchItemFailure": NotRequired[Literal["AUTOMATIC_BISECT"]],
        "ParallelizationFactor": NotRequired[int],
    },
)
UpdatePipeSourceKinesisStreamParametersTypeDef = TypedDict(
    "UpdatePipeSourceKinesisStreamParametersTypeDef",
    {
        "BatchSize": NotRequired[int],
        "DeadLetterConfig": NotRequired[DeadLetterConfigTypeDef],
        "MaximumBatchingWindowInSeconds": NotRequired[int],
        "MaximumRecordAgeInSeconds": NotRequired[int],
        "MaximumRetryAttempts": NotRequired[int],
        "OnPartialBatchItemFailure": NotRequired[Literal["AUTOMATIC_BISECT"]],
        "ParallelizationFactor": NotRequired[int],
    },
)
EcsContainerOverrideTypeDef = TypedDict(
    "EcsContainerOverrideTypeDef",
    {
        "Command": NotRequired[Sequence[str]],
        "Cpu": NotRequired[int],
        "Environment": NotRequired[Sequence[EcsEnvironmentVariableTypeDef]],
        "EnvironmentFiles": NotRequired[Sequence[EcsEnvironmentFileTypeDef]],
        "Memory": NotRequired[int],
        "MemoryReservation": NotRequired[int],
        "Name": NotRequired[str],
        "ResourceRequirements": NotRequired[Sequence[EcsResourceRequirementTypeDef]],
    },
)
FilterCriteriaTypeDef = TypedDict(
    "FilterCriteriaTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
    },
)
ListPipesRequestListPipesPaginateTypeDef = TypedDict(
    "ListPipesRequestListPipesPaginateTypeDef",
    {
        "CurrentState": NotRequired[PipeStateType],
        "DesiredState": NotRequired[RequestedPipeStateType],
        "NamePrefix": NotRequired[str],
        "SourcePrefix": NotRequired[str],
        "TargetPrefix": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListPipesResponseTypeDef = TypedDict(
    "ListPipesResponseTypeDef",
    {
        "NextToken": str,
        "Pipes": List[PipeTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PipeSourceActiveMQBrokerParametersTypeDef = TypedDict(
    "PipeSourceActiveMQBrokerParametersTypeDef",
    {
        "Credentials": MQBrokerAccessCredentialsTypeDef,
        "QueueName": str,
        "BatchSize": NotRequired[int],
        "MaximumBatchingWindowInSeconds": NotRequired[int],
    },
)
PipeSourceRabbitMQBrokerParametersTypeDef = TypedDict(
    "PipeSourceRabbitMQBrokerParametersTypeDef",
    {
        "Credentials": MQBrokerAccessCredentialsTypeDef,
        "QueueName": str,
        "BatchSize": NotRequired[int],
        "MaximumBatchingWindowInSeconds": NotRequired[int],
        "VirtualHost": NotRequired[str],
    },
)
UpdatePipeSourceActiveMQBrokerParametersTypeDef = TypedDict(
    "UpdatePipeSourceActiveMQBrokerParametersTypeDef",
    {
        "Credentials": MQBrokerAccessCredentialsTypeDef,
        "BatchSize": NotRequired[int],
        "MaximumBatchingWindowInSeconds": NotRequired[int],
    },
)
UpdatePipeSourceRabbitMQBrokerParametersTypeDef = TypedDict(
    "UpdatePipeSourceRabbitMQBrokerParametersTypeDef",
    {
        "Credentials": MQBrokerAccessCredentialsTypeDef,
        "BatchSize": NotRequired[int],
        "MaximumBatchingWindowInSeconds": NotRequired[int],
    },
)
PipeSourceManagedStreamingKafkaParametersTypeDef = TypedDict(
    "PipeSourceManagedStreamingKafkaParametersTypeDef",
    {
        "TopicName": str,
        "BatchSize": NotRequired[int],
        "ConsumerGroupID": NotRequired[str],
        "Credentials": NotRequired[MSKAccessCredentialsTypeDef],
        "MaximumBatchingWindowInSeconds": NotRequired[int],
        "StartingPosition": NotRequired[MSKStartPositionType],
    },
)
UpdatePipeSourceManagedStreamingKafkaParametersTypeDef = TypedDict(
    "UpdatePipeSourceManagedStreamingKafkaParametersTypeDef",
    {
        "BatchSize": NotRequired[int],
        "Credentials": NotRequired[MSKAccessCredentialsTypeDef],
        "MaximumBatchingWindowInSeconds": NotRequired[int],
    },
)
PipeEnrichmentParametersTypeDef = TypedDict(
    "PipeEnrichmentParametersTypeDef",
    {
        "HttpParameters": NotRequired[PipeEnrichmentHttpParametersTypeDef],
        "InputTemplate": NotRequired[str],
    },
)
PipeLogConfigurationParametersTypeDef = TypedDict(
    "PipeLogConfigurationParametersTypeDef",
    {
        "Level": LogLevelType,
        "CloudwatchLogsLogDestination": NotRequired[CloudwatchLogsLogDestinationParametersTypeDef],
        "FirehoseLogDestination": NotRequired[FirehoseLogDestinationParametersTypeDef],
        "IncludeExecutionData": NotRequired[Sequence[Literal["ALL"]]],
        "S3LogDestination": NotRequired[S3LogDestinationParametersTypeDef],
    },
)
PipeLogConfigurationTypeDef = TypedDict(
    "PipeLogConfigurationTypeDef",
    {
        "CloudwatchLogsLogDestination": NotRequired[CloudwatchLogsLogDestinationTypeDef],
        "FirehoseLogDestination": NotRequired[FirehoseLogDestinationTypeDef],
        "IncludeExecutionData": NotRequired[List[Literal["ALL"]]],
        "Level": NotRequired[LogLevelType],
        "S3LogDestination": NotRequired[S3LogDestinationTypeDef],
    },
)
PipeSourceKinesisStreamParametersTypeDef = TypedDict(
    "PipeSourceKinesisStreamParametersTypeDef",
    {
        "StartingPosition": KinesisStreamStartPositionType,
        "BatchSize": NotRequired[int],
        "DeadLetterConfig": NotRequired[DeadLetterConfigTypeDef],
        "MaximumBatchingWindowInSeconds": NotRequired[int],
        "MaximumRecordAgeInSeconds": NotRequired[int],
        "MaximumRetryAttempts": NotRequired[int],
        "OnPartialBatchItemFailure": NotRequired[Literal["AUTOMATIC_BISECT"]],
        "ParallelizationFactor": NotRequired[int],
        "StartingPositionTimestamp": NotRequired[TimestampTypeDef],
    },
)
PipeSourceSelfManagedKafkaParametersTypeDef = TypedDict(
    "PipeSourceSelfManagedKafkaParametersTypeDef",
    {
        "TopicName": str,
        "AdditionalBootstrapServers": NotRequired[Sequence[str]],
        "BatchSize": NotRequired[int],
        "ConsumerGroupID": NotRequired[str],
        "Credentials": NotRequired[SelfManagedKafkaAccessConfigurationCredentialsTypeDef],
        "MaximumBatchingWindowInSeconds": NotRequired[int],
        "ServerRootCaCertificate": NotRequired[str],
        "StartingPosition": NotRequired[SelfManagedKafkaStartPositionType],
        "Vpc": NotRequired[SelfManagedKafkaAccessConfigurationVpcTypeDef],
    },
)
UpdatePipeSourceSelfManagedKafkaParametersTypeDef = TypedDict(
    "UpdatePipeSourceSelfManagedKafkaParametersTypeDef",
    {
        "BatchSize": NotRequired[int],
        "Credentials": NotRequired[SelfManagedKafkaAccessConfigurationCredentialsTypeDef],
        "MaximumBatchingWindowInSeconds": NotRequired[int],
        "ServerRootCaCertificate": NotRequired[str],
        "Vpc": NotRequired[SelfManagedKafkaAccessConfigurationVpcTypeDef],
    },
)
PipeTargetSageMakerPipelineParametersTypeDef = TypedDict(
    "PipeTargetSageMakerPipelineParametersTypeDef",
    {
        "PipelineParameterList": NotRequired[Sequence[SageMakerPipelineParameterTypeDef]],
    },
)
PipeTargetBatchJobParametersTypeDef = TypedDict(
    "PipeTargetBatchJobParametersTypeDef",
    {
        "JobDefinition": str,
        "JobName": str,
        "ArrayProperties": NotRequired[BatchArrayPropertiesTypeDef],
        "ContainerOverrides": NotRequired[BatchContainerOverridesTypeDef],
        "DependsOn": NotRequired[Sequence[BatchJobDependencyTypeDef]],
        "Parameters": NotRequired[Mapping[str, str]],
        "RetryStrategy": NotRequired[BatchRetryStrategyTypeDef],
    },
)
EcsTaskOverrideTypeDef = TypedDict(
    "EcsTaskOverrideTypeDef",
    {
        "ContainerOverrides": NotRequired[Sequence[EcsContainerOverrideTypeDef]],
        "Cpu": NotRequired[str],
        "EphemeralStorage": NotRequired[EcsEphemeralStorageTypeDef],
        "ExecutionRoleArn": NotRequired[str],
        "InferenceAcceleratorOverrides": NotRequired[
            Sequence[EcsInferenceAcceleratorOverrideTypeDef]
        ],
        "Memory": NotRequired[str],
        "TaskRoleArn": NotRequired[str],
    },
)
PipeSourceParametersTypeDef = TypedDict(
    "PipeSourceParametersTypeDef",
    {
        "ActiveMQBrokerParameters": NotRequired[PipeSourceActiveMQBrokerParametersTypeDef],
        "DynamoDBStreamParameters": NotRequired[PipeSourceDynamoDBStreamParametersTypeDef],
        "FilterCriteria": NotRequired[FilterCriteriaTypeDef],
        "KinesisStreamParameters": NotRequired[PipeSourceKinesisStreamParametersTypeDef],
        "ManagedStreamingKafkaParameters": NotRequired[
            PipeSourceManagedStreamingKafkaParametersTypeDef
        ],
        "RabbitMQBrokerParameters": NotRequired[PipeSourceRabbitMQBrokerParametersTypeDef],
        "SelfManagedKafkaParameters": NotRequired[PipeSourceSelfManagedKafkaParametersTypeDef],
        "SqsQueueParameters": NotRequired[PipeSourceSqsQueueParametersTypeDef],
    },
)
UpdatePipeSourceParametersTypeDef = TypedDict(
    "UpdatePipeSourceParametersTypeDef",
    {
        "ActiveMQBrokerParameters": NotRequired[UpdatePipeSourceActiveMQBrokerParametersTypeDef],
        "DynamoDBStreamParameters": NotRequired[UpdatePipeSourceDynamoDBStreamParametersTypeDef],
        "FilterCriteria": NotRequired[FilterCriteriaTypeDef],
        "KinesisStreamParameters": NotRequired[UpdatePipeSourceKinesisStreamParametersTypeDef],
        "ManagedStreamingKafkaParameters": NotRequired[
            UpdatePipeSourceManagedStreamingKafkaParametersTypeDef
        ],
        "RabbitMQBrokerParameters": NotRequired[UpdatePipeSourceRabbitMQBrokerParametersTypeDef],
        "SelfManagedKafkaParameters": NotRequired[
            UpdatePipeSourceSelfManagedKafkaParametersTypeDef
        ],
        "SqsQueueParameters": NotRequired[UpdatePipeSourceSqsQueueParametersTypeDef],
    },
)
PipeTargetEcsTaskParametersTypeDef = TypedDict(
    "PipeTargetEcsTaskParametersTypeDef",
    {
        "TaskDefinitionArn": str,
        "CapacityProviderStrategy": NotRequired[Sequence[CapacityProviderStrategyItemTypeDef]],
        "EnableECSManagedTags": NotRequired[bool],
        "EnableExecuteCommand": NotRequired[bool],
        "Group": NotRequired[str],
        "LaunchType": NotRequired[LaunchTypeType],
        "NetworkConfiguration": NotRequired[NetworkConfigurationTypeDef],
        "Overrides": NotRequired[EcsTaskOverrideTypeDef],
        "PlacementConstraints": NotRequired[Sequence[PlacementConstraintTypeDef]],
        "PlacementStrategy": NotRequired[Sequence[PlacementStrategyTypeDef]],
        "PlatformVersion": NotRequired[str],
        "PropagateTags": NotRequired[Literal["TASK_DEFINITION"]],
        "ReferenceId": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "TaskCount": NotRequired[int],
    },
)
PipeTargetParametersTypeDef = TypedDict(
    "PipeTargetParametersTypeDef",
    {
        "BatchJobParameters": NotRequired[PipeTargetBatchJobParametersTypeDef],
        "CloudWatchLogsParameters": NotRequired[PipeTargetCloudWatchLogsParametersTypeDef],
        "EcsTaskParameters": NotRequired[PipeTargetEcsTaskParametersTypeDef],
        "EventBridgeEventBusParameters": NotRequired[
            PipeTargetEventBridgeEventBusParametersTypeDef
        ],
        "HttpParameters": NotRequired[PipeTargetHttpParametersTypeDef],
        "InputTemplate": NotRequired[str],
        "KinesisStreamParameters": NotRequired[PipeTargetKinesisStreamParametersTypeDef],
        "LambdaFunctionParameters": NotRequired[PipeTargetLambdaFunctionParametersTypeDef],
        "RedshiftDataParameters": NotRequired[PipeTargetRedshiftDataParametersTypeDef],
        "SageMakerPipelineParameters": NotRequired[PipeTargetSageMakerPipelineParametersTypeDef],
        "SqsQueueParameters": NotRequired[PipeTargetSqsQueueParametersTypeDef],
        "StepFunctionStateMachineParameters": NotRequired[PipeTargetStateMachineParametersTypeDef],
    },
)
CreatePipeRequestRequestTypeDef = TypedDict(
    "CreatePipeRequestRequestTypeDef",
    {
        "Name": str,
        "RoleArn": str,
        "Source": str,
        "Target": str,
        "Description": NotRequired[str],
        "DesiredState": NotRequired[RequestedPipeStateType],
        "Enrichment": NotRequired[str],
        "EnrichmentParameters": NotRequired[PipeEnrichmentParametersTypeDef],
        "LogConfiguration": NotRequired[PipeLogConfigurationParametersTypeDef],
        "SourceParameters": NotRequired[PipeSourceParametersTypeDef],
        "Tags": NotRequired[Mapping[str, str]],
        "TargetParameters": NotRequired[PipeTargetParametersTypeDef],
    },
)
DescribePipeResponseTypeDef = TypedDict(
    "DescribePipeResponseTypeDef",
    {
        "Arn": str,
        "CreationTime": datetime,
        "CurrentState": PipeStateType,
        "Description": str,
        "DesiredState": RequestedPipeStateDescribeResponseType,
        "Enrichment": str,
        "EnrichmentParameters": PipeEnrichmentParametersTypeDef,
        "LastModifiedTime": datetime,
        "LogConfiguration": PipeLogConfigurationTypeDef,
        "Name": str,
        "RoleArn": str,
        "Source": str,
        "SourceParameters": PipeSourceParametersTypeDef,
        "StateReason": str,
        "Tags": Dict[str, str],
        "Target": str,
        "TargetParameters": PipeTargetParametersTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdatePipeRequestRequestTypeDef = TypedDict(
    "UpdatePipeRequestRequestTypeDef",
    {
        "Name": str,
        "RoleArn": str,
        "Description": NotRequired[str],
        "DesiredState": NotRequired[RequestedPipeStateType],
        "Enrichment": NotRequired[str],
        "EnrichmentParameters": NotRequired[PipeEnrichmentParametersTypeDef],
        "LogConfiguration": NotRequired[PipeLogConfigurationParametersTypeDef],
        "SourceParameters": NotRequired[UpdatePipeSourceParametersTypeDef],
        "Target": NotRequired[str],
        "TargetParameters": NotRequired[PipeTargetParametersTypeDef],
    },
)
