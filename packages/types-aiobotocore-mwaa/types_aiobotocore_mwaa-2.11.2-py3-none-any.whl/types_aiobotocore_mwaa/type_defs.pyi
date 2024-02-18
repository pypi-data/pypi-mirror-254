"""
Type annotations for mwaa service type definitions.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mwaa/type_defs/)

Usage::

    ```python
    from types_aiobotocore_mwaa.type_defs import CreateCliTokenRequestRequestTypeDef

    data: CreateCliTokenRequestRequestTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from .literals import (
    EndpointManagementType,
    EnvironmentStatusType,
    LoggingLevelType,
    UnitType,
    UpdateStatusType,
    WebserverAccessModeType,
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
    "CreateCliTokenRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "NetworkConfigurationTypeDef",
    "CreateWebLoginTokenRequestRequestTypeDef",
    "DeleteEnvironmentInputRequestTypeDef",
    "DimensionTypeDef",
    "GetEnvironmentInputRequestTypeDef",
    "UpdateErrorTypeDef",
    "PaginatorConfigTypeDef",
    "ListEnvironmentsInputRequestTypeDef",
    "ListTagsForResourceInputRequestTypeDef",
    "ModuleLoggingConfigurationInputTypeDef",
    "ModuleLoggingConfigurationTypeDef",
    "StatisticSetTypeDef",
    "TimestampTypeDef",
    "TagResourceInputRequestTypeDef",
    "UntagResourceInputRequestTypeDef",
    "UpdateNetworkConfigurationInputTypeDef",
    "CreateCliTokenResponseTypeDef",
    "CreateEnvironmentOutputTypeDef",
    "CreateWebLoginTokenResponseTypeDef",
    "ListEnvironmentsOutputTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "UpdateEnvironmentOutputTypeDef",
    "LastUpdateTypeDef",
    "ListEnvironmentsInputListEnvironmentsPaginateTypeDef",
    "LoggingConfigurationInputTypeDef",
    "LoggingConfigurationTypeDef",
    "MetricDatumTypeDef",
    "CreateEnvironmentInputRequestTypeDef",
    "UpdateEnvironmentInputRequestTypeDef",
    "EnvironmentTypeDef",
    "PublishMetricsInputRequestTypeDef",
    "GetEnvironmentOutputTypeDef",
)

CreateCliTokenRequestRequestTypeDef = TypedDict(
    "CreateCliTokenRequestRequestTypeDef",
    {
        "Name": str,
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
NetworkConfigurationTypeDef = TypedDict(
    "NetworkConfigurationTypeDef",
    {
        "SecurityGroupIds": NotRequired[Sequence[str]],
        "SubnetIds": NotRequired[Sequence[str]],
    },
)
CreateWebLoginTokenRequestRequestTypeDef = TypedDict(
    "CreateWebLoginTokenRequestRequestTypeDef",
    {
        "Name": str,
    },
)
DeleteEnvironmentInputRequestTypeDef = TypedDict(
    "DeleteEnvironmentInputRequestTypeDef",
    {
        "Name": str,
    },
)
DimensionTypeDef = TypedDict(
    "DimensionTypeDef",
    {
        "Name": str,
        "Value": str,
    },
)
GetEnvironmentInputRequestTypeDef = TypedDict(
    "GetEnvironmentInputRequestTypeDef",
    {
        "Name": str,
    },
)
UpdateErrorTypeDef = TypedDict(
    "UpdateErrorTypeDef",
    {
        "ErrorCode": NotRequired[str],
        "ErrorMessage": NotRequired[str],
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
ListEnvironmentsInputRequestTypeDef = TypedDict(
    "ListEnvironmentsInputRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListTagsForResourceInputRequestTypeDef = TypedDict(
    "ListTagsForResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
ModuleLoggingConfigurationInputTypeDef = TypedDict(
    "ModuleLoggingConfigurationInputTypeDef",
    {
        "Enabled": bool,
        "LogLevel": LoggingLevelType,
    },
)
ModuleLoggingConfigurationTypeDef = TypedDict(
    "ModuleLoggingConfigurationTypeDef",
    {
        "CloudWatchLogGroupArn": NotRequired[str],
        "Enabled": NotRequired[bool],
        "LogLevel": NotRequired[LoggingLevelType],
    },
)
StatisticSetTypeDef = TypedDict(
    "StatisticSetTypeDef",
    {
        "Maximum": NotRequired[float],
        "Minimum": NotRequired[float],
        "SampleCount": NotRequired[int],
        "Sum": NotRequired[float],
    },
)
TimestampTypeDef = Union[datetime, str]
TagResourceInputRequestTypeDef = TypedDict(
    "TagResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Mapping[str, str],
    },
)
UntagResourceInputRequestTypeDef = TypedDict(
    "UntagResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
        "tagKeys": Sequence[str],
    },
)
UpdateNetworkConfigurationInputTypeDef = TypedDict(
    "UpdateNetworkConfigurationInputTypeDef",
    {
        "SecurityGroupIds": Sequence[str],
    },
)
CreateCliTokenResponseTypeDef = TypedDict(
    "CreateCliTokenResponseTypeDef",
    {
        "CliToken": str,
        "WebServerHostname": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateEnvironmentOutputTypeDef = TypedDict(
    "CreateEnvironmentOutputTypeDef",
    {
        "Arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateWebLoginTokenResponseTypeDef = TypedDict(
    "CreateWebLoginTokenResponseTypeDef",
    {
        "AirflowIdentity": str,
        "IamIdentity": str,
        "WebServerHostname": str,
        "WebToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListEnvironmentsOutputTypeDef = TypedDict(
    "ListEnvironmentsOutputTypeDef",
    {
        "Environments": List[str],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateEnvironmentOutputTypeDef = TypedDict(
    "UpdateEnvironmentOutputTypeDef",
    {
        "Arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
LastUpdateTypeDef = TypedDict(
    "LastUpdateTypeDef",
    {
        "CreatedAt": NotRequired[datetime],
        "Error": NotRequired[UpdateErrorTypeDef],
        "Source": NotRequired[str],
        "Status": NotRequired[UpdateStatusType],
    },
)
ListEnvironmentsInputListEnvironmentsPaginateTypeDef = TypedDict(
    "ListEnvironmentsInputListEnvironmentsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
LoggingConfigurationInputTypeDef = TypedDict(
    "LoggingConfigurationInputTypeDef",
    {
        "DagProcessingLogs": NotRequired[ModuleLoggingConfigurationInputTypeDef],
        "SchedulerLogs": NotRequired[ModuleLoggingConfigurationInputTypeDef],
        "TaskLogs": NotRequired[ModuleLoggingConfigurationInputTypeDef],
        "WebserverLogs": NotRequired[ModuleLoggingConfigurationInputTypeDef],
        "WorkerLogs": NotRequired[ModuleLoggingConfigurationInputTypeDef],
    },
)
LoggingConfigurationTypeDef = TypedDict(
    "LoggingConfigurationTypeDef",
    {
        "DagProcessingLogs": NotRequired[ModuleLoggingConfigurationTypeDef],
        "SchedulerLogs": NotRequired[ModuleLoggingConfigurationTypeDef],
        "TaskLogs": NotRequired[ModuleLoggingConfigurationTypeDef],
        "WebserverLogs": NotRequired[ModuleLoggingConfigurationTypeDef],
        "WorkerLogs": NotRequired[ModuleLoggingConfigurationTypeDef],
    },
)
MetricDatumTypeDef = TypedDict(
    "MetricDatumTypeDef",
    {
        "MetricName": str,
        "Timestamp": TimestampTypeDef,
        "Dimensions": NotRequired[Sequence[DimensionTypeDef]],
        "StatisticValues": NotRequired[StatisticSetTypeDef],
        "Unit": NotRequired[UnitType],
        "Value": NotRequired[float],
    },
)
CreateEnvironmentInputRequestTypeDef = TypedDict(
    "CreateEnvironmentInputRequestTypeDef",
    {
        "DagS3Path": str,
        "ExecutionRoleArn": str,
        "Name": str,
        "NetworkConfiguration": NetworkConfigurationTypeDef,
        "SourceBucketArn": str,
        "AirflowConfigurationOptions": NotRequired[Mapping[str, str]],
        "AirflowVersion": NotRequired[str],
        "EndpointManagement": NotRequired[EndpointManagementType],
        "EnvironmentClass": NotRequired[str],
        "KmsKey": NotRequired[str],
        "LoggingConfiguration": NotRequired[LoggingConfigurationInputTypeDef],
        "MaxWorkers": NotRequired[int],
        "MinWorkers": NotRequired[int],
        "PluginsS3ObjectVersion": NotRequired[str],
        "PluginsS3Path": NotRequired[str],
        "RequirementsS3ObjectVersion": NotRequired[str],
        "RequirementsS3Path": NotRequired[str],
        "Schedulers": NotRequired[int],
        "StartupScriptS3ObjectVersion": NotRequired[str],
        "StartupScriptS3Path": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
        "WebserverAccessMode": NotRequired[WebserverAccessModeType],
        "WeeklyMaintenanceWindowStart": NotRequired[str],
    },
)
UpdateEnvironmentInputRequestTypeDef = TypedDict(
    "UpdateEnvironmentInputRequestTypeDef",
    {
        "Name": str,
        "AirflowConfigurationOptions": NotRequired[Mapping[str, str]],
        "AirflowVersion": NotRequired[str],
        "DagS3Path": NotRequired[str],
        "EnvironmentClass": NotRequired[str],
        "ExecutionRoleArn": NotRequired[str],
        "LoggingConfiguration": NotRequired[LoggingConfigurationInputTypeDef],
        "MaxWorkers": NotRequired[int],
        "MinWorkers": NotRequired[int],
        "NetworkConfiguration": NotRequired[UpdateNetworkConfigurationInputTypeDef],
        "PluginsS3ObjectVersion": NotRequired[str],
        "PluginsS3Path": NotRequired[str],
        "RequirementsS3ObjectVersion": NotRequired[str],
        "RequirementsS3Path": NotRequired[str],
        "Schedulers": NotRequired[int],
        "SourceBucketArn": NotRequired[str],
        "StartupScriptS3ObjectVersion": NotRequired[str],
        "StartupScriptS3Path": NotRequired[str],
        "WebserverAccessMode": NotRequired[WebserverAccessModeType],
        "WeeklyMaintenanceWindowStart": NotRequired[str],
    },
)
EnvironmentTypeDef = TypedDict(
    "EnvironmentTypeDef",
    {
        "AirflowConfigurationOptions": NotRequired[Dict[str, str]],
        "AirflowVersion": NotRequired[str],
        "Arn": NotRequired[str],
        "CeleryExecutorQueue": NotRequired[str],
        "CreatedAt": NotRequired[datetime],
        "DagS3Path": NotRequired[str],
        "DatabaseVpcEndpointService": NotRequired[str],
        "EndpointManagement": NotRequired[EndpointManagementType],
        "EnvironmentClass": NotRequired[str],
        "ExecutionRoleArn": NotRequired[str],
        "KmsKey": NotRequired[str],
        "LastUpdate": NotRequired[LastUpdateTypeDef],
        "LoggingConfiguration": NotRequired[LoggingConfigurationTypeDef],
        "MaxWorkers": NotRequired[int],
        "MinWorkers": NotRequired[int],
        "Name": NotRequired[str],
        "NetworkConfiguration": NotRequired[NetworkConfigurationTypeDef],
        "PluginsS3ObjectVersion": NotRequired[str],
        "PluginsS3Path": NotRequired[str],
        "RequirementsS3ObjectVersion": NotRequired[str],
        "RequirementsS3Path": NotRequired[str],
        "Schedulers": NotRequired[int],
        "ServiceRoleArn": NotRequired[str],
        "SourceBucketArn": NotRequired[str],
        "StartupScriptS3ObjectVersion": NotRequired[str],
        "StartupScriptS3Path": NotRequired[str],
        "Status": NotRequired[EnvironmentStatusType],
        "Tags": NotRequired[Dict[str, str]],
        "WebserverAccessMode": NotRequired[WebserverAccessModeType],
        "WebserverUrl": NotRequired[str],
        "WebserverVpcEndpointService": NotRequired[str],
        "WeeklyMaintenanceWindowStart": NotRequired[str],
    },
)
PublishMetricsInputRequestTypeDef = TypedDict(
    "PublishMetricsInputRequestTypeDef",
    {
        "EnvironmentName": str,
        "MetricData": Sequence[MetricDatumTypeDef],
    },
)
GetEnvironmentOutputTypeDef = TypedDict(
    "GetEnvironmentOutputTypeDef",
    {
        "Environment": EnvironmentTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
