"""
Type annotations for kinesisanalyticsv2 service type definitions.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kinesisanalyticsv2/type_defs/)

Usage::

    ```python
    from types_aiobotocore_kinesisanalyticsv2.type_defs import CloudWatchLoggingOptionTypeDef

    data: CloudWatchLoggingOptionTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Mapping, Sequence, Union

from aiobotocore.response import StreamingBody

from .literals import (
    ApplicationModeType,
    ApplicationRestoreTypeType,
    ApplicationStatusType,
    ArtifactTypeType,
    CodeContentTypeType,
    ConfigurationTypeType,
    InputStartingPositionType,
    LogLevelType,
    MetricsLevelType,
    RecordFormatTypeType,
    RuntimeEnvironmentType,
    SnapshotStatusType,
    UrlTypeType,
)

if sys.version_info >= (3, 12):
    from typing import NotRequired
else:
    from typing_extensions import NotRequired
if sys.version_info >= (3, 12):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "CloudWatchLoggingOptionTypeDef",
    "CloudWatchLoggingOptionDescriptionTypeDef",
    "ResponseMetadataTypeDef",
    "VpcConfigurationTypeDef",
    "VpcConfigurationDescriptionTypeDef",
    "ApplicationSnapshotConfigurationDescriptionTypeDef",
    "ApplicationSnapshotConfigurationTypeDef",
    "ApplicationSnapshotConfigurationUpdateTypeDef",
    "VpcConfigurationUpdateTypeDef",
    "ApplicationMaintenanceConfigurationDescriptionTypeDef",
    "ApplicationMaintenanceConfigurationUpdateTypeDef",
    "ApplicationRestoreConfigurationTypeDef",
    "ApplicationSummaryTypeDef",
    "ApplicationVersionSummaryTypeDef",
    "BlobTypeDef",
    "CSVMappingParametersTypeDef",
    "GlueDataCatalogConfigurationDescriptionTypeDef",
    "GlueDataCatalogConfigurationTypeDef",
    "GlueDataCatalogConfigurationUpdateTypeDef",
    "CheckpointConfigurationDescriptionTypeDef",
    "CheckpointConfigurationTypeDef",
    "CheckpointConfigurationUpdateTypeDef",
    "CloudWatchLoggingOptionUpdateTypeDef",
    "S3ApplicationCodeLocationDescriptionTypeDef",
    "S3ContentLocationTypeDef",
    "S3ContentLocationUpdateTypeDef",
    "CreateApplicationPresignedUrlRequestRequestTypeDef",
    "TagTypeDef",
    "CreateApplicationSnapshotRequestRequestTypeDef",
    "MavenReferenceTypeDef",
    "DeleteApplicationCloudWatchLoggingOptionRequestRequestTypeDef",
    "DeleteApplicationInputProcessingConfigurationRequestRequestTypeDef",
    "DeleteApplicationOutputRequestRequestTypeDef",
    "DeleteApplicationReferenceDataSourceRequestRequestTypeDef",
    "TimestampTypeDef",
    "DeleteApplicationVpcConfigurationRequestRequestTypeDef",
    "S3ContentBaseLocationDescriptionTypeDef",
    "S3ContentBaseLocationTypeDef",
    "S3ContentBaseLocationUpdateTypeDef",
    "DescribeApplicationRequestRequestTypeDef",
    "DescribeApplicationSnapshotRequestRequestTypeDef",
    "SnapshotDetailsTypeDef",
    "DescribeApplicationVersionRequestRequestTypeDef",
    "DestinationSchemaTypeDef",
    "InputStartingPositionConfigurationTypeDef",
    "S3ConfigurationTypeDef",
    "PropertyGroupTypeDef",
    "MonitoringConfigurationDescriptionTypeDef",
    "ParallelismConfigurationDescriptionTypeDef",
    "MonitoringConfigurationTypeDef",
    "ParallelismConfigurationTypeDef",
    "MonitoringConfigurationUpdateTypeDef",
    "ParallelismConfigurationUpdateTypeDef",
    "FlinkRunConfigurationTypeDef",
    "InputParallelismTypeDef",
    "KinesisFirehoseInputDescriptionTypeDef",
    "KinesisStreamsInputDescriptionTypeDef",
    "InputLambdaProcessorDescriptionTypeDef",
    "InputLambdaProcessorTypeDef",
    "InputLambdaProcessorUpdateTypeDef",
    "InputParallelismUpdateTypeDef",
    "RecordColumnTypeDef",
    "KinesisFirehoseInputTypeDef",
    "KinesisStreamsInputTypeDef",
    "KinesisFirehoseInputUpdateTypeDef",
    "KinesisStreamsInputUpdateTypeDef",
    "JSONMappingParametersTypeDef",
    "KinesisFirehoseOutputDescriptionTypeDef",
    "KinesisFirehoseOutputTypeDef",
    "KinesisFirehoseOutputUpdateTypeDef",
    "KinesisStreamsOutputDescriptionTypeDef",
    "KinesisStreamsOutputTypeDef",
    "KinesisStreamsOutputUpdateTypeDef",
    "LambdaOutputDescriptionTypeDef",
    "LambdaOutputTypeDef",
    "LambdaOutputUpdateTypeDef",
    "PaginatorConfigTypeDef",
    "ListApplicationSnapshotsRequestRequestTypeDef",
    "ListApplicationVersionsRequestRequestTypeDef",
    "ListApplicationsRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "S3ReferenceDataSourceDescriptionTypeDef",
    "S3ReferenceDataSourceTypeDef",
    "S3ReferenceDataSourceUpdateTypeDef",
    "RollbackApplicationRequestRequestTypeDef",
    "StopApplicationRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "ZeppelinMonitoringConfigurationDescriptionTypeDef",
    "ZeppelinMonitoringConfigurationTypeDef",
    "ZeppelinMonitoringConfigurationUpdateTypeDef",
    "AddApplicationCloudWatchLoggingOptionRequestRequestTypeDef",
    "AddApplicationCloudWatchLoggingOptionResponseTypeDef",
    "CreateApplicationPresignedUrlResponseTypeDef",
    "DeleteApplicationCloudWatchLoggingOptionResponseTypeDef",
    "DeleteApplicationInputProcessingConfigurationResponseTypeDef",
    "DeleteApplicationOutputResponseTypeDef",
    "DeleteApplicationReferenceDataSourceResponseTypeDef",
    "DeleteApplicationVpcConfigurationResponseTypeDef",
    "AddApplicationVpcConfigurationRequestRequestTypeDef",
    "AddApplicationVpcConfigurationResponseTypeDef",
    "UpdateApplicationMaintenanceConfigurationResponseTypeDef",
    "UpdateApplicationMaintenanceConfigurationRequestRequestTypeDef",
    "ListApplicationsResponseTypeDef",
    "ListApplicationVersionsResponseTypeDef",
    "CatalogConfigurationDescriptionTypeDef",
    "CatalogConfigurationTypeDef",
    "CatalogConfigurationUpdateTypeDef",
    "CodeContentDescriptionTypeDef",
    "CodeContentTypeDef",
    "CodeContentUpdateTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "CustomArtifactConfigurationDescriptionTypeDef",
    "CustomArtifactConfigurationTypeDef",
    "DeleteApplicationRequestRequestTypeDef",
    "DeleteApplicationSnapshotRequestRequestTypeDef",
    "DeployAsApplicationConfigurationDescriptionTypeDef",
    "DeployAsApplicationConfigurationTypeDef",
    "DeployAsApplicationConfigurationUpdateTypeDef",
    "DescribeApplicationSnapshotResponseTypeDef",
    "ListApplicationSnapshotsResponseTypeDef",
    "SqlRunConfigurationTypeDef",
    "EnvironmentPropertiesTypeDef",
    "EnvironmentPropertyDescriptionsTypeDef",
    "EnvironmentPropertyUpdatesTypeDef",
    "FlinkApplicationConfigurationDescriptionTypeDef",
    "FlinkApplicationConfigurationTypeDef",
    "FlinkApplicationConfigurationUpdateTypeDef",
    "RunConfigurationDescriptionTypeDef",
    "RunConfigurationUpdateTypeDef",
    "InputProcessingConfigurationDescriptionTypeDef",
    "InputProcessingConfigurationTypeDef",
    "InputProcessingConfigurationUpdateTypeDef",
    "MappingParametersTypeDef",
    "OutputDescriptionTypeDef",
    "OutputTypeDef",
    "OutputUpdateTypeDef",
    "ListApplicationSnapshotsRequestListApplicationSnapshotsPaginateTypeDef",
    "ListApplicationsRequestListApplicationsPaginateTypeDef",
    "ApplicationCodeConfigurationDescriptionTypeDef",
    "ApplicationCodeConfigurationTypeDef",
    "ApplicationCodeConfigurationUpdateTypeDef",
    "ZeppelinApplicationConfigurationDescriptionTypeDef",
    "ZeppelinApplicationConfigurationTypeDef",
    "ZeppelinApplicationConfigurationUpdateTypeDef",
    "RunConfigurationTypeDef",
    "AddApplicationInputProcessingConfigurationResponseTypeDef",
    "AddApplicationInputProcessingConfigurationRequestRequestTypeDef",
    "DiscoverInputSchemaRequestRequestTypeDef",
    "RecordFormatTypeDef",
    "AddApplicationOutputResponseTypeDef",
    "AddApplicationOutputRequestRequestTypeDef",
    "StartApplicationRequestRequestTypeDef",
    "InputSchemaUpdateTypeDef",
    "SourceSchemaTypeDef",
    "InputUpdateTypeDef",
    "DiscoverInputSchemaResponseTypeDef",
    "InputDescriptionTypeDef",
    "InputTypeDef",
    "ReferenceDataSourceDescriptionTypeDef",
    "ReferenceDataSourceTypeDef",
    "ReferenceDataSourceUpdateTypeDef",
    "AddApplicationInputResponseTypeDef",
    "AddApplicationInputRequestRequestTypeDef",
    "AddApplicationReferenceDataSourceResponseTypeDef",
    "SqlApplicationConfigurationDescriptionTypeDef",
    "AddApplicationReferenceDataSourceRequestRequestTypeDef",
    "SqlApplicationConfigurationTypeDef",
    "SqlApplicationConfigurationUpdateTypeDef",
    "ApplicationConfigurationDescriptionTypeDef",
    "ApplicationConfigurationTypeDef",
    "ApplicationConfigurationUpdateTypeDef",
    "ApplicationDetailTypeDef",
    "CreateApplicationRequestRequestTypeDef",
    "UpdateApplicationRequestRequestTypeDef",
    "CreateApplicationResponseTypeDef",
    "DescribeApplicationResponseTypeDef",
    "DescribeApplicationVersionResponseTypeDef",
    "RollbackApplicationResponseTypeDef",
    "UpdateApplicationResponseTypeDef",
)

CloudWatchLoggingOptionTypeDef = TypedDict(
    "CloudWatchLoggingOptionTypeDef",
    {
        "LogStreamARN": str,
    },
)
CloudWatchLoggingOptionDescriptionTypeDef = TypedDict(
    "CloudWatchLoggingOptionDescriptionTypeDef",
    {
        "LogStreamARN": str,
        "CloudWatchLoggingOptionId": NotRequired[str],
        "RoleARN": NotRequired[str],
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
VpcConfigurationTypeDef = TypedDict(
    "VpcConfigurationTypeDef",
    {
        "SubnetIds": Sequence[str],
        "SecurityGroupIds": Sequence[str],
    },
)
VpcConfigurationDescriptionTypeDef = TypedDict(
    "VpcConfigurationDescriptionTypeDef",
    {
        "VpcConfigurationId": str,
        "VpcId": str,
        "SubnetIds": List[str],
        "SecurityGroupIds": List[str],
    },
)
ApplicationSnapshotConfigurationDescriptionTypeDef = TypedDict(
    "ApplicationSnapshotConfigurationDescriptionTypeDef",
    {
        "SnapshotsEnabled": bool,
    },
)
ApplicationSnapshotConfigurationTypeDef = TypedDict(
    "ApplicationSnapshotConfigurationTypeDef",
    {
        "SnapshotsEnabled": bool,
    },
)
ApplicationSnapshotConfigurationUpdateTypeDef = TypedDict(
    "ApplicationSnapshotConfigurationUpdateTypeDef",
    {
        "SnapshotsEnabledUpdate": bool,
    },
)
VpcConfigurationUpdateTypeDef = TypedDict(
    "VpcConfigurationUpdateTypeDef",
    {
        "VpcConfigurationId": str,
        "SubnetIdUpdates": NotRequired[Sequence[str]],
        "SecurityGroupIdUpdates": NotRequired[Sequence[str]],
    },
)
ApplicationMaintenanceConfigurationDescriptionTypeDef = TypedDict(
    "ApplicationMaintenanceConfigurationDescriptionTypeDef",
    {
        "ApplicationMaintenanceWindowStartTime": str,
        "ApplicationMaintenanceWindowEndTime": str,
    },
)
ApplicationMaintenanceConfigurationUpdateTypeDef = TypedDict(
    "ApplicationMaintenanceConfigurationUpdateTypeDef",
    {
        "ApplicationMaintenanceWindowStartTimeUpdate": str,
    },
)
ApplicationRestoreConfigurationTypeDef = TypedDict(
    "ApplicationRestoreConfigurationTypeDef",
    {
        "ApplicationRestoreType": ApplicationRestoreTypeType,
        "SnapshotName": NotRequired[str],
    },
)
ApplicationSummaryTypeDef = TypedDict(
    "ApplicationSummaryTypeDef",
    {
        "ApplicationName": str,
        "ApplicationARN": str,
        "ApplicationStatus": ApplicationStatusType,
        "ApplicationVersionId": int,
        "RuntimeEnvironment": RuntimeEnvironmentType,
        "ApplicationMode": NotRequired[ApplicationModeType],
    },
)
ApplicationVersionSummaryTypeDef = TypedDict(
    "ApplicationVersionSummaryTypeDef",
    {
        "ApplicationVersionId": int,
        "ApplicationStatus": ApplicationStatusType,
    },
)
BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]
CSVMappingParametersTypeDef = TypedDict(
    "CSVMappingParametersTypeDef",
    {
        "RecordRowDelimiter": str,
        "RecordColumnDelimiter": str,
    },
)
GlueDataCatalogConfigurationDescriptionTypeDef = TypedDict(
    "GlueDataCatalogConfigurationDescriptionTypeDef",
    {
        "DatabaseARN": str,
    },
)
GlueDataCatalogConfigurationTypeDef = TypedDict(
    "GlueDataCatalogConfigurationTypeDef",
    {
        "DatabaseARN": str,
    },
)
GlueDataCatalogConfigurationUpdateTypeDef = TypedDict(
    "GlueDataCatalogConfigurationUpdateTypeDef",
    {
        "DatabaseARNUpdate": str,
    },
)
CheckpointConfigurationDescriptionTypeDef = TypedDict(
    "CheckpointConfigurationDescriptionTypeDef",
    {
        "ConfigurationType": NotRequired[ConfigurationTypeType],
        "CheckpointingEnabled": NotRequired[bool],
        "CheckpointInterval": NotRequired[int],
        "MinPauseBetweenCheckpoints": NotRequired[int],
    },
)
CheckpointConfigurationTypeDef = TypedDict(
    "CheckpointConfigurationTypeDef",
    {
        "ConfigurationType": ConfigurationTypeType,
        "CheckpointingEnabled": NotRequired[bool],
        "CheckpointInterval": NotRequired[int],
        "MinPauseBetweenCheckpoints": NotRequired[int],
    },
)
CheckpointConfigurationUpdateTypeDef = TypedDict(
    "CheckpointConfigurationUpdateTypeDef",
    {
        "ConfigurationTypeUpdate": NotRequired[ConfigurationTypeType],
        "CheckpointingEnabledUpdate": NotRequired[bool],
        "CheckpointIntervalUpdate": NotRequired[int],
        "MinPauseBetweenCheckpointsUpdate": NotRequired[int],
    },
)
CloudWatchLoggingOptionUpdateTypeDef = TypedDict(
    "CloudWatchLoggingOptionUpdateTypeDef",
    {
        "CloudWatchLoggingOptionId": str,
        "LogStreamARNUpdate": NotRequired[str],
    },
)
S3ApplicationCodeLocationDescriptionTypeDef = TypedDict(
    "S3ApplicationCodeLocationDescriptionTypeDef",
    {
        "BucketARN": str,
        "FileKey": str,
        "ObjectVersion": NotRequired[str],
    },
)
S3ContentLocationTypeDef = TypedDict(
    "S3ContentLocationTypeDef",
    {
        "BucketARN": str,
        "FileKey": str,
        "ObjectVersion": NotRequired[str],
    },
)
S3ContentLocationUpdateTypeDef = TypedDict(
    "S3ContentLocationUpdateTypeDef",
    {
        "BucketARNUpdate": NotRequired[str],
        "FileKeyUpdate": NotRequired[str],
        "ObjectVersionUpdate": NotRequired[str],
    },
)
CreateApplicationPresignedUrlRequestRequestTypeDef = TypedDict(
    "CreateApplicationPresignedUrlRequestRequestTypeDef",
    {
        "ApplicationName": str,
        "UrlType": UrlTypeType,
        "SessionExpirationDurationInSeconds": NotRequired[int],
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": NotRequired[str],
    },
)
CreateApplicationSnapshotRequestRequestTypeDef = TypedDict(
    "CreateApplicationSnapshotRequestRequestTypeDef",
    {
        "ApplicationName": str,
        "SnapshotName": str,
    },
)
MavenReferenceTypeDef = TypedDict(
    "MavenReferenceTypeDef",
    {
        "GroupId": str,
        "ArtifactId": str,
        "Version": str,
    },
)
DeleteApplicationCloudWatchLoggingOptionRequestRequestTypeDef = TypedDict(
    "DeleteApplicationCloudWatchLoggingOptionRequestRequestTypeDef",
    {
        "ApplicationName": str,
        "CloudWatchLoggingOptionId": str,
        "CurrentApplicationVersionId": NotRequired[int],
        "ConditionalToken": NotRequired[str],
    },
)
DeleteApplicationInputProcessingConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteApplicationInputProcessingConfigurationRequestRequestTypeDef",
    {
        "ApplicationName": str,
        "CurrentApplicationVersionId": int,
        "InputId": str,
    },
)
DeleteApplicationOutputRequestRequestTypeDef = TypedDict(
    "DeleteApplicationOutputRequestRequestTypeDef",
    {
        "ApplicationName": str,
        "CurrentApplicationVersionId": int,
        "OutputId": str,
    },
)
DeleteApplicationReferenceDataSourceRequestRequestTypeDef = TypedDict(
    "DeleteApplicationReferenceDataSourceRequestRequestTypeDef",
    {
        "ApplicationName": str,
        "CurrentApplicationVersionId": int,
        "ReferenceId": str,
    },
)
TimestampTypeDef = Union[datetime, str]
DeleteApplicationVpcConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteApplicationVpcConfigurationRequestRequestTypeDef",
    {
        "ApplicationName": str,
        "VpcConfigurationId": str,
        "CurrentApplicationVersionId": NotRequired[int],
        "ConditionalToken": NotRequired[str],
    },
)
S3ContentBaseLocationDescriptionTypeDef = TypedDict(
    "S3ContentBaseLocationDescriptionTypeDef",
    {
        "BucketARN": str,
        "BasePath": NotRequired[str],
    },
)
S3ContentBaseLocationTypeDef = TypedDict(
    "S3ContentBaseLocationTypeDef",
    {
        "BucketARN": str,
        "BasePath": NotRequired[str],
    },
)
S3ContentBaseLocationUpdateTypeDef = TypedDict(
    "S3ContentBaseLocationUpdateTypeDef",
    {
        "BucketARNUpdate": NotRequired[str],
        "BasePathUpdate": NotRequired[str],
    },
)
DescribeApplicationRequestRequestTypeDef = TypedDict(
    "DescribeApplicationRequestRequestTypeDef",
    {
        "ApplicationName": str,
        "IncludeAdditionalDetails": NotRequired[bool],
    },
)
DescribeApplicationSnapshotRequestRequestTypeDef = TypedDict(
    "DescribeApplicationSnapshotRequestRequestTypeDef",
    {
        "ApplicationName": str,
        "SnapshotName": str,
    },
)
SnapshotDetailsTypeDef = TypedDict(
    "SnapshotDetailsTypeDef",
    {
        "SnapshotName": str,
        "SnapshotStatus": SnapshotStatusType,
        "ApplicationVersionId": int,
        "SnapshotCreationTimestamp": NotRequired[datetime],
    },
)
DescribeApplicationVersionRequestRequestTypeDef = TypedDict(
    "DescribeApplicationVersionRequestRequestTypeDef",
    {
        "ApplicationName": str,
        "ApplicationVersionId": int,
    },
)
DestinationSchemaTypeDef = TypedDict(
    "DestinationSchemaTypeDef",
    {
        "RecordFormatType": RecordFormatTypeType,
    },
)
InputStartingPositionConfigurationTypeDef = TypedDict(
    "InputStartingPositionConfigurationTypeDef",
    {
        "InputStartingPosition": NotRequired[InputStartingPositionType],
    },
)
S3ConfigurationTypeDef = TypedDict(
    "S3ConfigurationTypeDef",
    {
        "BucketARN": str,
        "FileKey": str,
    },
)
PropertyGroupTypeDef = TypedDict(
    "PropertyGroupTypeDef",
    {
        "PropertyGroupId": str,
        "PropertyMap": Mapping[str, str],
    },
)
MonitoringConfigurationDescriptionTypeDef = TypedDict(
    "MonitoringConfigurationDescriptionTypeDef",
    {
        "ConfigurationType": NotRequired[ConfigurationTypeType],
        "MetricsLevel": NotRequired[MetricsLevelType],
        "LogLevel": NotRequired[LogLevelType],
    },
)
ParallelismConfigurationDescriptionTypeDef = TypedDict(
    "ParallelismConfigurationDescriptionTypeDef",
    {
        "ConfigurationType": NotRequired[ConfigurationTypeType],
        "Parallelism": NotRequired[int],
        "ParallelismPerKPU": NotRequired[int],
        "CurrentParallelism": NotRequired[int],
        "AutoScalingEnabled": NotRequired[bool],
    },
)
MonitoringConfigurationTypeDef = TypedDict(
    "MonitoringConfigurationTypeDef",
    {
        "ConfigurationType": ConfigurationTypeType,
        "MetricsLevel": NotRequired[MetricsLevelType],
        "LogLevel": NotRequired[LogLevelType],
    },
)
ParallelismConfigurationTypeDef = TypedDict(
    "ParallelismConfigurationTypeDef",
    {
        "ConfigurationType": ConfigurationTypeType,
        "Parallelism": NotRequired[int],
        "ParallelismPerKPU": NotRequired[int],
        "AutoScalingEnabled": NotRequired[bool],
    },
)
MonitoringConfigurationUpdateTypeDef = TypedDict(
    "MonitoringConfigurationUpdateTypeDef",
    {
        "ConfigurationTypeUpdate": NotRequired[ConfigurationTypeType],
        "MetricsLevelUpdate": NotRequired[MetricsLevelType],
        "LogLevelUpdate": NotRequired[LogLevelType],
    },
)
ParallelismConfigurationUpdateTypeDef = TypedDict(
    "ParallelismConfigurationUpdateTypeDef",
    {
        "ConfigurationTypeUpdate": NotRequired[ConfigurationTypeType],
        "ParallelismUpdate": NotRequired[int],
        "ParallelismPerKPUUpdate": NotRequired[int],
        "AutoScalingEnabledUpdate": NotRequired[bool],
    },
)
FlinkRunConfigurationTypeDef = TypedDict(
    "FlinkRunConfigurationTypeDef",
    {
        "AllowNonRestoredState": NotRequired[bool],
    },
)
InputParallelismTypeDef = TypedDict(
    "InputParallelismTypeDef",
    {
        "Count": NotRequired[int],
    },
)
KinesisFirehoseInputDescriptionTypeDef = TypedDict(
    "KinesisFirehoseInputDescriptionTypeDef",
    {
        "ResourceARN": str,
        "RoleARN": NotRequired[str],
    },
)
KinesisStreamsInputDescriptionTypeDef = TypedDict(
    "KinesisStreamsInputDescriptionTypeDef",
    {
        "ResourceARN": str,
        "RoleARN": NotRequired[str],
    },
)
InputLambdaProcessorDescriptionTypeDef = TypedDict(
    "InputLambdaProcessorDescriptionTypeDef",
    {
        "ResourceARN": str,
        "RoleARN": NotRequired[str],
    },
)
InputLambdaProcessorTypeDef = TypedDict(
    "InputLambdaProcessorTypeDef",
    {
        "ResourceARN": str,
    },
)
InputLambdaProcessorUpdateTypeDef = TypedDict(
    "InputLambdaProcessorUpdateTypeDef",
    {
        "ResourceARNUpdate": str,
    },
)
InputParallelismUpdateTypeDef = TypedDict(
    "InputParallelismUpdateTypeDef",
    {
        "CountUpdate": int,
    },
)
RecordColumnTypeDef = TypedDict(
    "RecordColumnTypeDef",
    {
        "Name": str,
        "SqlType": str,
        "Mapping": NotRequired[str],
    },
)
KinesisFirehoseInputTypeDef = TypedDict(
    "KinesisFirehoseInputTypeDef",
    {
        "ResourceARN": str,
    },
)
KinesisStreamsInputTypeDef = TypedDict(
    "KinesisStreamsInputTypeDef",
    {
        "ResourceARN": str,
    },
)
KinesisFirehoseInputUpdateTypeDef = TypedDict(
    "KinesisFirehoseInputUpdateTypeDef",
    {
        "ResourceARNUpdate": str,
    },
)
KinesisStreamsInputUpdateTypeDef = TypedDict(
    "KinesisStreamsInputUpdateTypeDef",
    {
        "ResourceARNUpdate": str,
    },
)
JSONMappingParametersTypeDef = TypedDict(
    "JSONMappingParametersTypeDef",
    {
        "RecordRowPath": str,
    },
)
KinesisFirehoseOutputDescriptionTypeDef = TypedDict(
    "KinesisFirehoseOutputDescriptionTypeDef",
    {
        "ResourceARN": str,
        "RoleARN": NotRequired[str],
    },
)
KinesisFirehoseOutputTypeDef = TypedDict(
    "KinesisFirehoseOutputTypeDef",
    {
        "ResourceARN": str,
    },
)
KinesisFirehoseOutputUpdateTypeDef = TypedDict(
    "KinesisFirehoseOutputUpdateTypeDef",
    {
        "ResourceARNUpdate": str,
    },
)
KinesisStreamsOutputDescriptionTypeDef = TypedDict(
    "KinesisStreamsOutputDescriptionTypeDef",
    {
        "ResourceARN": str,
        "RoleARN": NotRequired[str],
    },
)
KinesisStreamsOutputTypeDef = TypedDict(
    "KinesisStreamsOutputTypeDef",
    {
        "ResourceARN": str,
    },
)
KinesisStreamsOutputUpdateTypeDef = TypedDict(
    "KinesisStreamsOutputUpdateTypeDef",
    {
        "ResourceARNUpdate": str,
    },
)
LambdaOutputDescriptionTypeDef = TypedDict(
    "LambdaOutputDescriptionTypeDef",
    {
        "ResourceARN": str,
        "RoleARN": NotRequired[str],
    },
)
LambdaOutputTypeDef = TypedDict(
    "LambdaOutputTypeDef",
    {
        "ResourceARN": str,
    },
)
LambdaOutputUpdateTypeDef = TypedDict(
    "LambdaOutputUpdateTypeDef",
    {
        "ResourceARNUpdate": str,
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
ListApplicationSnapshotsRequestRequestTypeDef = TypedDict(
    "ListApplicationSnapshotsRequestRequestTypeDef",
    {
        "ApplicationName": str,
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListApplicationVersionsRequestRequestTypeDef = TypedDict(
    "ListApplicationVersionsRequestRequestTypeDef",
    {
        "ApplicationName": str,
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListApplicationsRequestRequestTypeDef = TypedDict(
    "ListApplicationsRequestRequestTypeDef",
    {
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
    },
)
S3ReferenceDataSourceDescriptionTypeDef = TypedDict(
    "S3ReferenceDataSourceDescriptionTypeDef",
    {
        "BucketARN": str,
        "FileKey": str,
        "ReferenceRoleARN": NotRequired[str],
    },
)
S3ReferenceDataSourceTypeDef = TypedDict(
    "S3ReferenceDataSourceTypeDef",
    {
        "BucketARN": NotRequired[str],
        "FileKey": NotRequired[str],
    },
)
S3ReferenceDataSourceUpdateTypeDef = TypedDict(
    "S3ReferenceDataSourceUpdateTypeDef",
    {
        "BucketARNUpdate": NotRequired[str],
        "FileKeyUpdate": NotRequired[str],
    },
)
RollbackApplicationRequestRequestTypeDef = TypedDict(
    "RollbackApplicationRequestRequestTypeDef",
    {
        "ApplicationName": str,
        "CurrentApplicationVersionId": int,
    },
)
StopApplicationRequestRequestTypeDef = TypedDict(
    "StopApplicationRequestRequestTypeDef",
    {
        "ApplicationName": str,
        "Force": NotRequired[bool],
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": Sequence[str],
    },
)
ZeppelinMonitoringConfigurationDescriptionTypeDef = TypedDict(
    "ZeppelinMonitoringConfigurationDescriptionTypeDef",
    {
        "LogLevel": NotRequired[LogLevelType],
    },
)
ZeppelinMonitoringConfigurationTypeDef = TypedDict(
    "ZeppelinMonitoringConfigurationTypeDef",
    {
        "LogLevel": LogLevelType,
    },
)
ZeppelinMonitoringConfigurationUpdateTypeDef = TypedDict(
    "ZeppelinMonitoringConfigurationUpdateTypeDef",
    {
        "LogLevelUpdate": LogLevelType,
    },
)
AddApplicationCloudWatchLoggingOptionRequestRequestTypeDef = TypedDict(
    "AddApplicationCloudWatchLoggingOptionRequestRequestTypeDef",
    {
        "ApplicationName": str,
        "CloudWatchLoggingOption": CloudWatchLoggingOptionTypeDef,
        "CurrentApplicationVersionId": NotRequired[int],
        "ConditionalToken": NotRequired[str],
    },
)
AddApplicationCloudWatchLoggingOptionResponseTypeDef = TypedDict(
    "AddApplicationCloudWatchLoggingOptionResponseTypeDef",
    {
        "ApplicationARN": str,
        "ApplicationVersionId": int,
        "CloudWatchLoggingOptionDescriptions": List[CloudWatchLoggingOptionDescriptionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateApplicationPresignedUrlResponseTypeDef = TypedDict(
    "CreateApplicationPresignedUrlResponseTypeDef",
    {
        "AuthorizedUrl": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteApplicationCloudWatchLoggingOptionResponseTypeDef = TypedDict(
    "DeleteApplicationCloudWatchLoggingOptionResponseTypeDef",
    {
        "ApplicationARN": str,
        "ApplicationVersionId": int,
        "CloudWatchLoggingOptionDescriptions": List[CloudWatchLoggingOptionDescriptionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteApplicationInputProcessingConfigurationResponseTypeDef = TypedDict(
    "DeleteApplicationInputProcessingConfigurationResponseTypeDef",
    {
        "ApplicationARN": str,
        "ApplicationVersionId": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteApplicationOutputResponseTypeDef = TypedDict(
    "DeleteApplicationOutputResponseTypeDef",
    {
        "ApplicationARN": str,
        "ApplicationVersionId": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteApplicationReferenceDataSourceResponseTypeDef = TypedDict(
    "DeleteApplicationReferenceDataSourceResponseTypeDef",
    {
        "ApplicationARN": str,
        "ApplicationVersionId": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteApplicationVpcConfigurationResponseTypeDef = TypedDict(
    "DeleteApplicationVpcConfigurationResponseTypeDef",
    {
        "ApplicationARN": str,
        "ApplicationVersionId": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AddApplicationVpcConfigurationRequestRequestTypeDef = TypedDict(
    "AddApplicationVpcConfigurationRequestRequestTypeDef",
    {
        "ApplicationName": str,
        "VpcConfiguration": VpcConfigurationTypeDef,
        "CurrentApplicationVersionId": NotRequired[int],
        "ConditionalToken": NotRequired[str],
    },
)
AddApplicationVpcConfigurationResponseTypeDef = TypedDict(
    "AddApplicationVpcConfigurationResponseTypeDef",
    {
        "ApplicationARN": str,
        "ApplicationVersionId": int,
        "VpcConfigurationDescription": VpcConfigurationDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateApplicationMaintenanceConfigurationResponseTypeDef = TypedDict(
    "UpdateApplicationMaintenanceConfigurationResponseTypeDef",
    {
        "ApplicationARN": str,
        "ApplicationMaintenanceConfigurationDescription": ApplicationMaintenanceConfigurationDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateApplicationMaintenanceConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateApplicationMaintenanceConfigurationRequestRequestTypeDef",
    {
        "ApplicationName": str,
        "ApplicationMaintenanceConfigurationUpdate": ApplicationMaintenanceConfigurationUpdateTypeDef,
    },
)
ListApplicationsResponseTypeDef = TypedDict(
    "ListApplicationsResponseTypeDef",
    {
        "ApplicationSummaries": List[ApplicationSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListApplicationVersionsResponseTypeDef = TypedDict(
    "ListApplicationVersionsResponseTypeDef",
    {
        "ApplicationVersionSummaries": List[ApplicationVersionSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CatalogConfigurationDescriptionTypeDef = TypedDict(
    "CatalogConfigurationDescriptionTypeDef",
    {
        "GlueDataCatalogConfigurationDescription": GlueDataCatalogConfigurationDescriptionTypeDef,
    },
)
CatalogConfigurationTypeDef = TypedDict(
    "CatalogConfigurationTypeDef",
    {
        "GlueDataCatalogConfiguration": GlueDataCatalogConfigurationTypeDef,
    },
)
CatalogConfigurationUpdateTypeDef = TypedDict(
    "CatalogConfigurationUpdateTypeDef",
    {
        "GlueDataCatalogConfigurationUpdate": GlueDataCatalogConfigurationUpdateTypeDef,
    },
)
CodeContentDescriptionTypeDef = TypedDict(
    "CodeContentDescriptionTypeDef",
    {
        "TextContent": NotRequired[str],
        "CodeMD5": NotRequired[str],
        "CodeSize": NotRequired[int],
        "S3ApplicationCodeLocationDescription": NotRequired[
            S3ApplicationCodeLocationDescriptionTypeDef
        ],
    },
)
CodeContentTypeDef = TypedDict(
    "CodeContentTypeDef",
    {
        "TextContent": NotRequired[str],
        "ZipFileContent": NotRequired[BlobTypeDef],
        "S3ContentLocation": NotRequired[S3ContentLocationTypeDef],
    },
)
CodeContentUpdateTypeDef = TypedDict(
    "CodeContentUpdateTypeDef",
    {
        "TextContentUpdate": NotRequired[str],
        "ZipFileContentUpdate": NotRequired[BlobTypeDef],
        "S3ContentLocationUpdate": NotRequired[S3ContentLocationUpdateTypeDef],
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "Tags": Sequence[TagTypeDef],
    },
)
CustomArtifactConfigurationDescriptionTypeDef = TypedDict(
    "CustomArtifactConfigurationDescriptionTypeDef",
    {
        "ArtifactType": NotRequired[ArtifactTypeType],
        "S3ContentLocationDescription": NotRequired[S3ContentLocationTypeDef],
        "MavenReferenceDescription": NotRequired[MavenReferenceTypeDef],
    },
)
CustomArtifactConfigurationTypeDef = TypedDict(
    "CustomArtifactConfigurationTypeDef",
    {
        "ArtifactType": ArtifactTypeType,
        "S3ContentLocation": NotRequired[S3ContentLocationTypeDef],
        "MavenReference": NotRequired[MavenReferenceTypeDef],
    },
)
DeleteApplicationRequestRequestTypeDef = TypedDict(
    "DeleteApplicationRequestRequestTypeDef",
    {
        "ApplicationName": str,
        "CreateTimestamp": TimestampTypeDef,
    },
)
DeleteApplicationSnapshotRequestRequestTypeDef = TypedDict(
    "DeleteApplicationSnapshotRequestRequestTypeDef",
    {
        "ApplicationName": str,
        "SnapshotName": str,
        "SnapshotCreationTimestamp": TimestampTypeDef,
    },
)
DeployAsApplicationConfigurationDescriptionTypeDef = TypedDict(
    "DeployAsApplicationConfigurationDescriptionTypeDef",
    {
        "S3ContentLocationDescription": S3ContentBaseLocationDescriptionTypeDef,
    },
)
DeployAsApplicationConfigurationTypeDef = TypedDict(
    "DeployAsApplicationConfigurationTypeDef",
    {
        "S3ContentLocation": S3ContentBaseLocationTypeDef,
    },
)
DeployAsApplicationConfigurationUpdateTypeDef = TypedDict(
    "DeployAsApplicationConfigurationUpdateTypeDef",
    {
        "S3ContentLocationUpdate": NotRequired[S3ContentBaseLocationUpdateTypeDef],
    },
)
DescribeApplicationSnapshotResponseTypeDef = TypedDict(
    "DescribeApplicationSnapshotResponseTypeDef",
    {
        "SnapshotDetails": SnapshotDetailsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListApplicationSnapshotsResponseTypeDef = TypedDict(
    "ListApplicationSnapshotsResponseTypeDef",
    {
        "SnapshotSummaries": List[SnapshotDetailsTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SqlRunConfigurationTypeDef = TypedDict(
    "SqlRunConfigurationTypeDef",
    {
        "InputId": str,
        "InputStartingPositionConfiguration": InputStartingPositionConfigurationTypeDef,
    },
)
EnvironmentPropertiesTypeDef = TypedDict(
    "EnvironmentPropertiesTypeDef",
    {
        "PropertyGroups": Sequence[PropertyGroupTypeDef],
    },
)
EnvironmentPropertyDescriptionsTypeDef = TypedDict(
    "EnvironmentPropertyDescriptionsTypeDef",
    {
        "PropertyGroupDescriptions": NotRequired[List[PropertyGroupTypeDef]],
    },
)
EnvironmentPropertyUpdatesTypeDef = TypedDict(
    "EnvironmentPropertyUpdatesTypeDef",
    {
        "PropertyGroups": Sequence[PropertyGroupTypeDef],
    },
)
FlinkApplicationConfigurationDescriptionTypeDef = TypedDict(
    "FlinkApplicationConfigurationDescriptionTypeDef",
    {
        "CheckpointConfigurationDescription": NotRequired[
            CheckpointConfigurationDescriptionTypeDef
        ],
        "MonitoringConfigurationDescription": NotRequired[
            MonitoringConfigurationDescriptionTypeDef
        ],
        "ParallelismConfigurationDescription": NotRequired[
            ParallelismConfigurationDescriptionTypeDef
        ],
        "JobPlanDescription": NotRequired[str],
    },
)
FlinkApplicationConfigurationTypeDef = TypedDict(
    "FlinkApplicationConfigurationTypeDef",
    {
        "CheckpointConfiguration": NotRequired[CheckpointConfigurationTypeDef],
        "MonitoringConfiguration": NotRequired[MonitoringConfigurationTypeDef],
        "ParallelismConfiguration": NotRequired[ParallelismConfigurationTypeDef],
    },
)
FlinkApplicationConfigurationUpdateTypeDef = TypedDict(
    "FlinkApplicationConfigurationUpdateTypeDef",
    {
        "CheckpointConfigurationUpdate": NotRequired[CheckpointConfigurationUpdateTypeDef],
        "MonitoringConfigurationUpdate": NotRequired[MonitoringConfigurationUpdateTypeDef],
        "ParallelismConfigurationUpdate": NotRequired[ParallelismConfigurationUpdateTypeDef],
    },
)
RunConfigurationDescriptionTypeDef = TypedDict(
    "RunConfigurationDescriptionTypeDef",
    {
        "ApplicationRestoreConfigurationDescription": NotRequired[
            ApplicationRestoreConfigurationTypeDef
        ],
        "FlinkRunConfigurationDescription": NotRequired[FlinkRunConfigurationTypeDef],
    },
)
RunConfigurationUpdateTypeDef = TypedDict(
    "RunConfigurationUpdateTypeDef",
    {
        "FlinkRunConfiguration": NotRequired[FlinkRunConfigurationTypeDef],
        "ApplicationRestoreConfiguration": NotRequired[ApplicationRestoreConfigurationTypeDef],
    },
)
InputProcessingConfigurationDescriptionTypeDef = TypedDict(
    "InputProcessingConfigurationDescriptionTypeDef",
    {
        "InputLambdaProcessorDescription": NotRequired[InputLambdaProcessorDescriptionTypeDef],
    },
)
InputProcessingConfigurationTypeDef = TypedDict(
    "InputProcessingConfigurationTypeDef",
    {
        "InputLambdaProcessor": InputLambdaProcessorTypeDef,
    },
)
InputProcessingConfigurationUpdateTypeDef = TypedDict(
    "InputProcessingConfigurationUpdateTypeDef",
    {
        "InputLambdaProcessorUpdate": InputLambdaProcessorUpdateTypeDef,
    },
)
MappingParametersTypeDef = TypedDict(
    "MappingParametersTypeDef",
    {
        "JSONMappingParameters": NotRequired[JSONMappingParametersTypeDef],
        "CSVMappingParameters": NotRequired[CSVMappingParametersTypeDef],
    },
)
OutputDescriptionTypeDef = TypedDict(
    "OutputDescriptionTypeDef",
    {
        "OutputId": NotRequired[str],
        "Name": NotRequired[str],
        "KinesisStreamsOutputDescription": NotRequired[KinesisStreamsOutputDescriptionTypeDef],
        "KinesisFirehoseOutputDescription": NotRequired[KinesisFirehoseOutputDescriptionTypeDef],
        "LambdaOutputDescription": NotRequired[LambdaOutputDescriptionTypeDef],
        "DestinationSchema": NotRequired[DestinationSchemaTypeDef],
    },
)
OutputTypeDef = TypedDict(
    "OutputTypeDef",
    {
        "Name": str,
        "DestinationSchema": DestinationSchemaTypeDef,
        "KinesisStreamsOutput": NotRequired[KinesisStreamsOutputTypeDef],
        "KinesisFirehoseOutput": NotRequired[KinesisFirehoseOutputTypeDef],
        "LambdaOutput": NotRequired[LambdaOutputTypeDef],
    },
)
OutputUpdateTypeDef = TypedDict(
    "OutputUpdateTypeDef",
    {
        "OutputId": str,
        "NameUpdate": NotRequired[str],
        "KinesisStreamsOutputUpdate": NotRequired[KinesisStreamsOutputUpdateTypeDef],
        "KinesisFirehoseOutputUpdate": NotRequired[KinesisFirehoseOutputUpdateTypeDef],
        "LambdaOutputUpdate": NotRequired[LambdaOutputUpdateTypeDef],
        "DestinationSchemaUpdate": NotRequired[DestinationSchemaTypeDef],
    },
)
ListApplicationSnapshotsRequestListApplicationSnapshotsPaginateTypeDef = TypedDict(
    "ListApplicationSnapshotsRequestListApplicationSnapshotsPaginateTypeDef",
    {
        "ApplicationName": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListApplicationsRequestListApplicationsPaginateTypeDef = TypedDict(
    "ListApplicationsRequestListApplicationsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ApplicationCodeConfigurationDescriptionTypeDef = TypedDict(
    "ApplicationCodeConfigurationDescriptionTypeDef",
    {
        "CodeContentType": CodeContentTypeType,
        "CodeContentDescription": NotRequired[CodeContentDescriptionTypeDef],
    },
)
ApplicationCodeConfigurationTypeDef = TypedDict(
    "ApplicationCodeConfigurationTypeDef",
    {
        "CodeContentType": CodeContentTypeType,
        "CodeContent": NotRequired[CodeContentTypeDef],
    },
)
ApplicationCodeConfigurationUpdateTypeDef = TypedDict(
    "ApplicationCodeConfigurationUpdateTypeDef",
    {
        "CodeContentTypeUpdate": NotRequired[CodeContentTypeType],
        "CodeContentUpdate": NotRequired[CodeContentUpdateTypeDef],
    },
)
ZeppelinApplicationConfigurationDescriptionTypeDef = TypedDict(
    "ZeppelinApplicationConfigurationDescriptionTypeDef",
    {
        "MonitoringConfigurationDescription": ZeppelinMonitoringConfigurationDescriptionTypeDef,
        "CatalogConfigurationDescription": NotRequired[CatalogConfigurationDescriptionTypeDef],
        "DeployAsApplicationConfigurationDescription": NotRequired[
            DeployAsApplicationConfigurationDescriptionTypeDef
        ],
        "CustomArtifactsConfigurationDescription": NotRequired[
            List[CustomArtifactConfigurationDescriptionTypeDef]
        ],
    },
)
ZeppelinApplicationConfigurationTypeDef = TypedDict(
    "ZeppelinApplicationConfigurationTypeDef",
    {
        "MonitoringConfiguration": NotRequired[ZeppelinMonitoringConfigurationTypeDef],
        "CatalogConfiguration": NotRequired[CatalogConfigurationTypeDef],
        "DeployAsApplicationConfiguration": NotRequired[DeployAsApplicationConfigurationTypeDef],
        "CustomArtifactsConfiguration": NotRequired[Sequence[CustomArtifactConfigurationTypeDef]],
    },
)
ZeppelinApplicationConfigurationUpdateTypeDef = TypedDict(
    "ZeppelinApplicationConfigurationUpdateTypeDef",
    {
        "MonitoringConfigurationUpdate": NotRequired[ZeppelinMonitoringConfigurationUpdateTypeDef],
        "CatalogConfigurationUpdate": NotRequired[CatalogConfigurationUpdateTypeDef],
        "DeployAsApplicationConfigurationUpdate": NotRequired[
            DeployAsApplicationConfigurationUpdateTypeDef
        ],
        "CustomArtifactsConfigurationUpdate": NotRequired[
            Sequence[CustomArtifactConfigurationTypeDef]
        ],
    },
)
RunConfigurationTypeDef = TypedDict(
    "RunConfigurationTypeDef",
    {
        "FlinkRunConfiguration": NotRequired[FlinkRunConfigurationTypeDef],
        "SqlRunConfigurations": NotRequired[Sequence[SqlRunConfigurationTypeDef]],
        "ApplicationRestoreConfiguration": NotRequired[ApplicationRestoreConfigurationTypeDef],
    },
)
AddApplicationInputProcessingConfigurationResponseTypeDef = TypedDict(
    "AddApplicationInputProcessingConfigurationResponseTypeDef",
    {
        "ApplicationARN": str,
        "ApplicationVersionId": int,
        "InputId": str,
        "InputProcessingConfigurationDescription": InputProcessingConfigurationDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AddApplicationInputProcessingConfigurationRequestRequestTypeDef = TypedDict(
    "AddApplicationInputProcessingConfigurationRequestRequestTypeDef",
    {
        "ApplicationName": str,
        "CurrentApplicationVersionId": int,
        "InputId": str,
        "InputProcessingConfiguration": InputProcessingConfigurationTypeDef,
    },
)
DiscoverInputSchemaRequestRequestTypeDef = TypedDict(
    "DiscoverInputSchemaRequestRequestTypeDef",
    {
        "ServiceExecutionRole": str,
        "ResourceARN": NotRequired[str],
        "InputStartingPositionConfiguration": NotRequired[
            InputStartingPositionConfigurationTypeDef
        ],
        "S3Configuration": NotRequired[S3ConfigurationTypeDef],
        "InputProcessingConfiguration": NotRequired[InputProcessingConfigurationTypeDef],
    },
)
RecordFormatTypeDef = TypedDict(
    "RecordFormatTypeDef",
    {
        "RecordFormatType": RecordFormatTypeType,
        "MappingParameters": NotRequired[MappingParametersTypeDef],
    },
)
AddApplicationOutputResponseTypeDef = TypedDict(
    "AddApplicationOutputResponseTypeDef",
    {
        "ApplicationARN": str,
        "ApplicationVersionId": int,
        "OutputDescriptions": List[OutputDescriptionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AddApplicationOutputRequestRequestTypeDef = TypedDict(
    "AddApplicationOutputRequestRequestTypeDef",
    {
        "ApplicationName": str,
        "CurrentApplicationVersionId": int,
        "Output": OutputTypeDef,
    },
)
StartApplicationRequestRequestTypeDef = TypedDict(
    "StartApplicationRequestRequestTypeDef",
    {
        "ApplicationName": str,
        "RunConfiguration": NotRequired[RunConfigurationTypeDef],
    },
)
InputSchemaUpdateTypeDef = TypedDict(
    "InputSchemaUpdateTypeDef",
    {
        "RecordFormatUpdate": NotRequired[RecordFormatTypeDef],
        "RecordEncodingUpdate": NotRequired[str],
        "RecordColumnUpdates": NotRequired[Sequence[RecordColumnTypeDef]],
    },
)
SourceSchemaTypeDef = TypedDict(
    "SourceSchemaTypeDef",
    {
        "RecordFormat": RecordFormatTypeDef,
        "RecordColumns": Sequence[RecordColumnTypeDef],
        "RecordEncoding": NotRequired[str],
    },
)
InputUpdateTypeDef = TypedDict(
    "InputUpdateTypeDef",
    {
        "InputId": str,
        "NamePrefixUpdate": NotRequired[str],
        "InputProcessingConfigurationUpdate": NotRequired[
            InputProcessingConfigurationUpdateTypeDef
        ],
        "KinesisStreamsInputUpdate": NotRequired[KinesisStreamsInputUpdateTypeDef],
        "KinesisFirehoseInputUpdate": NotRequired[KinesisFirehoseInputUpdateTypeDef],
        "InputSchemaUpdate": NotRequired[InputSchemaUpdateTypeDef],
        "InputParallelismUpdate": NotRequired[InputParallelismUpdateTypeDef],
    },
)
DiscoverInputSchemaResponseTypeDef = TypedDict(
    "DiscoverInputSchemaResponseTypeDef",
    {
        "InputSchema": SourceSchemaTypeDef,
        "ParsedInputRecords": List[List[str]],
        "ProcessedInputRecords": List[str],
        "RawInputRecords": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
InputDescriptionTypeDef = TypedDict(
    "InputDescriptionTypeDef",
    {
        "InputId": NotRequired[str],
        "NamePrefix": NotRequired[str],
        "InAppStreamNames": NotRequired[List[str]],
        "InputProcessingConfigurationDescription": NotRequired[
            InputProcessingConfigurationDescriptionTypeDef
        ],
        "KinesisStreamsInputDescription": NotRequired[KinesisStreamsInputDescriptionTypeDef],
        "KinesisFirehoseInputDescription": NotRequired[KinesisFirehoseInputDescriptionTypeDef],
        "InputSchema": NotRequired[SourceSchemaTypeDef],
        "InputParallelism": NotRequired[InputParallelismTypeDef],
        "InputStartingPositionConfiguration": NotRequired[
            InputStartingPositionConfigurationTypeDef
        ],
    },
)
InputTypeDef = TypedDict(
    "InputTypeDef",
    {
        "NamePrefix": str,
        "InputSchema": SourceSchemaTypeDef,
        "InputProcessingConfiguration": NotRequired[InputProcessingConfigurationTypeDef],
        "KinesisStreamsInput": NotRequired[KinesisStreamsInputTypeDef],
        "KinesisFirehoseInput": NotRequired[KinesisFirehoseInputTypeDef],
        "InputParallelism": NotRequired[InputParallelismTypeDef],
    },
)
ReferenceDataSourceDescriptionTypeDef = TypedDict(
    "ReferenceDataSourceDescriptionTypeDef",
    {
        "ReferenceId": str,
        "TableName": str,
        "S3ReferenceDataSourceDescription": S3ReferenceDataSourceDescriptionTypeDef,
        "ReferenceSchema": NotRequired[SourceSchemaTypeDef],
    },
)
ReferenceDataSourceTypeDef = TypedDict(
    "ReferenceDataSourceTypeDef",
    {
        "TableName": str,
        "ReferenceSchema": SourceSchemaTypeDef,
        "S3ReferenceDataSource": NotRequired[S3ReferenceDataSourceTypeDef],
    },
)
ReferenceDataSourceUpdateTypeDef = TypedDict(
    "ReferenceDataSourceUpdateTypeDef",
    {
        "ReferenceId": str,
        "TableNameUpdate": NotRequired[str],
        "S3ReferenceDataSourceUpdate": NotRequired[S3ReferenceDataSourceUpdateTypeDef],
        "ReferenceSchemaUpdate": NotRequired[SourceSchemaTypeDef],
    },
)
AddApplicationInputResponseTypeDef = TypedDict(
    "AddApplicationInputResponseTypeDef",
    {
        "ApplicationARN": str,
        "ApplicationVersionId": int,
        "InputDescriptions": List[InputDescriptionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AddApplicationInputRequestRequestTypeDef = TypedDict(
    "AddApplicationInputRequestRequestTypeDef",
    {
        "ApplicationName": str,
        "CurrentApplicationVersionId": int,
        "Input": InputTypeDef,
    },
)
AddApplicationReferenceDataSourceResponseTypeDef = TypedDict(
    "AddApplicationReferenceDataSourceResponseTypeDef",
    {
        "ApplicationARN": str,
        "ApplicationVersionId": int,
        "ReferenceDataSourceDescriptions": List[ReferenceDataSourceDescriptionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SqlApplicationConfigurationDescriptionTypeDef = TypedDict(
    "SqlApplicationConfigurationDescriptionTypeDef",
    {
        "InputDescriptions": NotRequired[List[InputDescriptionTypeDef]],
        "OutputDescriptions": NotRequired[List[OutputDescriptionTypeDef]],
        "ReferenceDataSourceDescriptions": NotRequired[List[ReferenceDataSourceDescriptionTypeDef]],
    },
)
AddApplicationReferenceDataSourceRequestRequestTypeDef = TypedDict(
    "AddApplicationReferenceDataSourceRequestRequestTypeDef",
    {
        "ApplicationName": str,
        "CurrentApplicationVersionId": int,
        "ReferenceDataSource": ReferenceDataSourceTypeDef,
    },
)
SqlApplicationConfigurationTypeDef = TypedDict(
    "SqlApplicationConfigurationTypeDef",
    {
        "Inputs": NotRequired[Sequence[InputTypeDef]],
        "Outputs": NotRequired[Sequence[OutputTypeDef]],
        "ReferenceDataSources": NotRequired[Sequence[ReferenceDataSourceTypeDef]],
    },
)
SqlApplicationConfigurationUpdateTypeDef = TypedDict(
    "SqlApplicationConfigurationUpdateTypeDef",
    {
        "InputUpdates": NotRequired[Sequence[InputUpdateTypeDef]],
        "OutputUpdates": NotRequired[Sequence[OutputUpdateTypeDef]],
        "ReferenceDataSourceUpdates": NotRequired[Sequence[ReferenceDataSourceUpdateTypeDef]],
    },
)
ApplicationConfigurationDescriptionTypeDef = TypedDict(
    "ApplicationConfigurationDescriptionTypeDef",
    {
        "SqlApplicationConfigurationDescription": NotRequired[
            SqlApplicationConfigurationDescriptionTypeDef
        ],
        "ApplicationCodeConfigurationDescription": NotRequired[
            ApplicationCodeConfigurationDescriptionTypeDef
        ],
        "RunConfigurationDescription": NotRequired[RunConfigurationDescriptionTypeDef],
        "FlinkApplicationConfigurationDescription": NotRequired[
            FlinkApplicationConfigurationDescriptionTypeDef
        ],
        "EnvironmentPropertyDescriptions": NotRequired[EnvironmentPropertyDescriptionsTypeDef],
        "ApplicationSnapshotConfigurationDescription": NotRequired[
            ApplicationSnapshotConfigurationDescriptionTypeDef
        ],
        "VpcConfigurationDescriptions": NotRequired[List[VpcConfigurationDescriptionTypeDef]],
        "ZeppelinApplicationConfigurationDescription": NotRequired[
            ZeppelinApplicationConfigurationDescriptionTypeDef
        ],
    },
)
ApplicationConfigurationTypeDef = TypedDict(
    "ApplicationConfigurationTypeDef",
    {
        "SqlApplicationConfiguration": NotRequired[SqlApplicationConfigurationTypeDef],
        "FlinkApplicationConfiguration": NotRequired[FlinkApplicationConfigurationTypeDef],
        "EnvironmentProperties": NotRequired[EnvironmentPropertiesTypeDef],
        "ApplicationCodeConfiguration": NotRequired[ApplicationCodeConfigurationTypeDef],
        "ApplicationSnapshotConfiguration": NotRequired[ApplicationSnapshotConfigurationTypeDef],
        "VpcConfigurations": NotRequired[Sequence[VpcConfigurationTypeDef]],
        "ZeppelinApplicationConfiguration": NotRequired[ZeppelinApplicationConfigurationTypeDef],
    },
)
ApplicationConfigurationUpdateTypeDef = TypedDict(
    "ApplicationConfigurationUpdateTypeDef",
    {
        "SqlApplicationConfigurationUpdate": NotRequired[SqlApplicationConfigurationUpdateTypeDef],
        "ApplicationCodeConfigurationUpdate": NotRequired[
            ApplicationCodeConfigurationUpdateTypeDef
        ],
        "FlinkApplicationConfigurationUpdate": NotRequired[
            FlinkApplicationConfigurationUpdateTypeDef
        ],
        "EnvironmentPropertyUpdates": NotRequired[EnvironmentPropertyUpdatesTypeDef],
        "ApplicationSnapshotConfigurationUpdate": NotRequired[
            ApplicationSnapshotConfigurationUpdateTypeDef
        ],
        "VpcConfigurationUpdates": NotRequired[Sequence[VpcConfigurationUpdateTypeDef]],
        "ZeppelinApplicationConfigurationUpdate": NotRequired[
            ZeppelinApplicationConfigurationUpdateTypeDef
        ],
    },
)
ApplicationDetailTypeDef = TypedDict(
    "ApplicationDetailTypeDef",
    {
        "ApplicationARN": str,
        "ApplicationName": str,
        "RuntimeEnvironment": RuntimeEnvironmentType,
        "ApplicationStatus": ApplicationStatusType,
        "ApplicationVersionId": int,
        "ApplicationDescription": NotRequired[str],
        "ServiceExecutionRole": NotRequired[str],
        "CreateTimestamp": NotRequired[datetime],
        "LastUpdateTimestamp": NotRequired[datetime],
        "ApplicationConfigurationDescription": NotRequired[
            ApplicationConfigurationDescriptionTypeDef
        ],
        "CloudWatchLoggingOptionDescriptions": NotRequired[
            List[CloudWatchLoggingOptionDescriptionTypeDef]
        ],
        "ApplicationMaintenanceConfigurationDescription": NotRequired[
            ApplicationMaintenanceConfigurationDescriptionTypeDef
        ],
        "ApplicationVersionUpdatedFrom": NotRequired[int],
        "ApplicationVersionRolledBackFrom": NotRequired[int],
        "ConditionalToken": NotRequired[str],
        "ApplicationVersionRolledBackTo": NotRequired[int],
        "ApplicationMode": NotRequired[ApplicationModeType],
    },
)
CreateApplicationRequestRequestTypeDef = TypedDict(
    "CreateApplicationRequestRequestTypeDef",
    {
        "ApplicationName": str,
        "RuntimeEnvironment": RuntimeEnvironmentType,
        "ServiceExecutionRole": str,
        "ApplicationDescription": NotRequired[str],
        "ApplicationConfiguration": NotRequired[ApplicationConfigurationTypeDef],
        "CloudWatchLoggingOptions": NotRequired[Sequence[CloudWatchLoggingOptionTypeDef]],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "ApplicationMode": NotRequired[ApplicationModeType],
    },
)
UpdateApplicationRequestRequestTypeDef = TypedDict(
    "UpdateApplicationRequestRequestTypeDef",
    {
        "ApplicationName": str,
        "CurrentApplicationVersionId": NotRequired[int],
        "ApplicationConfigurationUpdate": NotRequired[ApplicationConfigurationUpdateTypeDef],
        "ServiceExecutionRoleUpdate": NotRequired[str],
        "RunConfigurationUpdate": NotRequired[RunConfigurationUpdateTypeDef],
        "CloudWatchLoggingOptionUpdates": NotRequired[
            Sequence[CloudWatchLoggingOptionUpdateTypeDef]
        ],
        "ConditionalToken": NotRequired[str],
    },
)
CreateApplicationResponseTypeDef = TypedDict(
    "CreateApplicationResponseTypeDef",
    {
        "ApplicationDetail": ApplicationDetailTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeApplicationResponseTypeDef = TypedDict(
    "DescribeApplicationResponseTypeDef",
    {
        "ApplicationDetail": ApplicationDetailTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeApplicationVersionResponseTypeDef = TypedDict(
    "DescribeApplicationVersionResponseTypeDef",
    {
        "ApplicationVersionDetail": ApplicationDetailTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RollbackApplicationResponseTypeDef = TypedDict(
    "RollbackApplicationResponseTypeDef",
    {
        "ApplicationDetail": ApplicationDetailTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateApplicationResponseTypeDef = TypedDict(
    "UpdateApplicationResponseTypeDef",
    {
        "ApplicationDetail": ApplicationDetailTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
