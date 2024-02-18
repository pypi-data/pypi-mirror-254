"""
Type annotations for emr-serverless service type definitions.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_emr_serverless/type_defs/)

Usage::

    ```python
    from types_aiobotocore_emr_serverless.type_defs import ApplicationSummaryTypeDef

    data: ApplicationSummaryTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List, Mapping, Sequence, Union

from .literals import ApplicationStateType, ArchitectureType, JobRunStateType

if sys.version_info >= (3, 12):
    from typing import NotRequired
else:
    from typing_extensions import NotRequired
if sys.version_info >= (3, 12):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "ApplicationSummaryTypeDef",
    "AutoStartConfigTypeDef",
    "AutoStopConfigTypeDef",
    "ImageConfigurationTypeDef",
    "MaximumAllowedResourcesTypeDef",
    "NetworkConfigurationTypeDef",
    "CancelJobRunRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "CloudWatchLoggingConfigurationTypeDef",
    "ConfigurationTypeDef",
    "ImageConfigurationInputTypeDef",
    "DeleteApplicationRequestRequestTypeDef",
    "GetApplicationRequestRequestTypeDef",
    "GetDashboardForJobRunRequestRequestTypeDef",
    "GetJobRunRequestRequestTypeDef",
    "HiveTypeDef",
    "WorkerResourceConfigTypeDef",
    "SparkSubmitTypeDef",
    "JobRunSummaryTypeDef",
    "ResourceUtilizationTypeDef",
    "TotalResourceUtilizationTypeDef",
    "PaginatorConfigTypeDef",
    "ListApplicationsRequestRequestTypeDef",
    "TimestampTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ManagedPersistenceMonitoringConfigurationTypeDef",
    "S3MonitoringConfigurationTypeDef",
    "StartApplicationRequestRequestTypeDef",
    "StopApplicationRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "WorkerTypeSpecificationTypeDef",
    "CancelJobRunResponseTypeDef",
    "CreateApplicationResponseTypeDef",
    "GetDashboardForJobRunResponseTypeDef",
    "ListApplicationsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "StartJobRunResponseTypeDef",
    "WorkerTypeSpecificationInputTypeDef",
    "InitialCapacityConfigTypeDef",
    "JobDriverTypeDef",
    "ListJobRunsResponseTypeDef",
    "ListApplicationsRequestListApplicationsPaginateTypeDef",
    "ListJobRunsRequestListJobRunsPaginateTypeDef",
    "ListJobRunsRequestRequestTypeDef",
    "MonitoringConfigurationTypeDef",
    "ApplicationTypeDef",
    "ConfigurationOverridesTypeDef",
    "CreateApplicationRequestRequestTypeDef",
    "UpdateApplicationRequestRequestTypeDef",
    "GetApplicationResponseTypeDef",
    "UpdateApplicationResponseTypeDef",
    "JobRunTypeDef",
    "StartJobRunRequestRequestTypeDef",
    "GetJobRunResponseTypeDef",
)

ApplicationSummaryTypeDef = TypedDict(
    "ApplicationSummaryTypeDef",
    {
        "id": str,
        "arn": str,
        "releaseLabel": str,
        "type": str,
        "state": ApplicationStateType,
        "createdAt": datetime,
        "updatedAt": datetime,
        "name": NotRequired[str],
        "stateDetails": NotRequired[str],
        "architecture": NotRequired[ArchitectureType],
    },
)
AutoStartConfigTypeDef = TypedDict(
    "AutoStartConfigTypeDef",
    {
        "enabled": NotRequired[bool],
    },
)
AutoStopConfigTypeDef = TypedDict(
    "AutoStopConfigTypeDef",
    {
        "enabled": NotRequired[bool],
        "idleTimeoutMinutes": NotRequired[int],
    },
)
ImageConfigurationTypeDef = TypedDict(
    "ImageConfigurationTypeDef",
    {
        "imageUri": str,
        "resolvedImageDigest": NotRequired[str],
    },
)
MaximumAllowedResourcesTypeDef = TypedDict(
    "MaximumAllowedResourcesTypeDef",
    {
        "cpu": str,
        "memory": str,
        "disk": NotRequired[str],
    },
)
NetworkConfigurationTypeDef = TypedDict(
    "NetworkConfigurationTypeDef",
    {
        "subnetIds": NotRequired[Sequence[str]],
        "securityGroupIds": NotRequired[Sequence[str]],
    },
)
CancelJobRunRequestRequestTypeDef = TypedDict(
    "CancelJobRunRequestRequestTypeDef",
    {
        "applicationId": str,
        "jobRunId": str,
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
CloudWatchLoggingConfigurationTypeDef = TypedDict(
    "CloudWatchLoggingConfigurationTypeDef",
    {
        "enabled": bool,
        "logGroupName": NotRequired[str],
        "logStreamNamePrefix": NotRequired[str],
        "encryptionKeyArn": NotRequired[str],
        "logTypes": NotRequired[Mapping[str, Sequence[str]]],
    },
)
ConfigurationTypeDef = TypedDict(
    "ConfigurationTypeDef",
    {
        "classification": str,
        "properties": NotRequired[Mapping[str, str]],
        "configurations": NotRequired[Sequence[Dict[str, Any]]],
    },
)
ImageConfigurationInputTypeDef = TypedDict(
    "ImageConfigurationInputTypeDef",
    {
        "imageUri": NotRequired[str],
    },
)
DeleteApplicationRequestRequestTypeDef = TypedDict(
    "DeleteApplicationRequestRequestTypeDef",
    {
        "applicationId": str,
    },
)
GetApplicationRequestRequestTypeDef = TypedDict(
    "GetApplicationRequestRequestTypeDef",
    {
        "applicationId": str,
    },
)
GetDashboardForJobRunRequestRequestTypeDef = TypedDict(
    "GetDashboardForJobRunRequestRequestTypeDef",
    {
        "applicationId": str,
        "jobRunId": str,
    },
)
GetJobRunRequestRequestTypeDef = TypedDict(
    "GetJobRunRequestRequestTypeDef",
    {
        "applicationId": str,
        "jobRunId": str,
    },
)
HiveTypeDef = TypedDict(
    "HiveTypeDef",
    {
        "query": str,
        "initQueryFile": NotRequired[str],
        "parameters": NotRequired[str],
    },
)
WorkerResourceConfigTypeDef = TypedDict(
    "WorkerResourceConfigTypeDef",
    {
        "cpu": str,
        "memory": str,
        "disk": NotRequired[str],
    },
)
SparkSubmitTypeDef = TypedDict(
    "SparkSubmitTypeDef",
    {
        "entryPoint": str,
        "entryPointArguments": NotRequired[List[str]],
        "sparkSubmitParameters": NotRequired[str],
    },
)
JobRunSummaryTypeDef = TypedDict(
    "JobRunSummaryTypeDef",
    {
        "applicationId": str,
        "id": str,
        "arn": str,
        "createdBy": str,
        "createdAt": datetime,
        "updatedAt": datetime,
        "executionRole": str,
        "state": JobRunStateType,
        "stateDetails": str,
        "releaseLabel": str,
        "name": NotRequired[str],
        "type": NotRequired[str],
    },
)
ResourceUtilizationTypeDef = TypedDict(
    "ResourceUtilizationTypeDef",
    {
        "vCPUHour": NotRequired[float],
        "memoryGBHour": NotRequired[float],
        "storageGBHour": NotRequired[float],
    },
)
TotalResourceUtilizationTypeDef = TypedDict(
    "TotalResourceUtilizationTypeDef",
    {
        "vCPUHour": NotRequired[float],
        "memoryGBHour": NotRequired[float],
        "storageGBHour": NotRequired[float],
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
ListApplicationsRequestRequestTypeDef = TypedDict(
    "ListApplicationsRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "states": NotRequired[Sequence[ApplicationStateType]],
    },
)
TimestampTypeDef = Union[datetime, str]
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)
ManagedPersistenceMonitoringConfigurationTypeDef = TypedDict(
    "ManagedPersistenceMonitoringConfigurationTypeDef",
    {
        "enabled": NotRequired[bool],
        "encryptionKeyArn": NotRequired[str],
    },
)
S3MonitoringConfigurationTypeDef = TypedDict(
    "S3MonitoringConfigurationTypeDef",
    {
        "logUri": NotRequired[str],
        "encryptionKeyArn": NotRequired[str],
    },
)
StartApplicationRequestRequestTypeDef = TypedDict(
    "StartApplicationRequestRequestTypeDef",
    {
        "applicationId": str,
    },
)
StopApplicationRequestRequestTypeDef = TypedDict(
    "StopApplicationRequestRequestTypeDef",
    {
        "applicationId": str,
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
WorkerTypeSpecificationTypeDef = TypedDict(
    "WorkerTypeSpecificationTypeDef",
    {
        "imageConfiguration": NotRequired[ImageConfigurationTypeDef],
    },
)
CancelJobRunResponseTypeDef = TypedDict(
    "CancelJobRunResponseTypeDef",
    {
        "applicationId": str,
        "jobRunId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateApplicationResponseTypeDef = TypedDict(
    "CreateApplicationResponseTypeDef",
    {
        "applicationId": str,
        "name": str,
        "arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetDashboardForJobRunResponseTypeDef = TypedDict(
    "GetDashboardForJobRunResponseTypeDef",
    {
        "url": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListApplicationsResponseTypeDef = TypedDict(
    "ListApplicationsResponseTypeDef",
    {
        "applications": List[ApplicationSummaryTypeDef],
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
StartJobRunResponseTypeDef = TypedDict(
    "StartJobRunResponseTypeDef",
    {
        "applicationId": str,
        "jobRunId": str,
        "arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
WorkerTypeSpecificationInputTypeDef = TypedDict(
    "WorkerTypeSpecificationInputTypeDef",
    {
        "imageConfiguration": NotRequired[ImageConfigurationInputTypeDef],
    },
)
InitialCapacityConfigTypeDef = TypedDict(
    "InitialCapacityConfigTypeDef",
    {
        "workerCount": int,
        "workerConfiguration": NotRequired[WorkerResourceConfigTypeDef],
    },
)
JobDriverTypeDef = TypedDict(
    "JobDriverTypeDef",
    {
        "sparkSubmit": NotRequired[SparkSubmitTypeDef],
        "hive": NotRequired[HiveTypeDef],
    },
)
ListJobRunsResponseTypeDef = TypedDict(
    "ListJobRunsResponseTypeDef",
    {
        "jobRuns": List[JobRunSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListApplicationsRequestListApplicationsPaginateTypeDef = TypedDict(
    "ListApplicationsRequestListApplicationsPaginateTypeDef",
    {
        "states": NotRequired[Sequence[ApplicationStateType]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListJobRunsRequestListJobRunsPaginateTypeDef = TypedDict(
    "ListJobRunsRequestListJobRunsPaginateTypeDef",
    {
        "applicationId": str,
        "createdAtAfter": NotRequired[TimestampTypeDef],
        "createdAtBefore": NotRequired[TimestampTypeDef],
        "states": NotRequired[Sequence[JobRunStateType]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListJobRunsRequestRequestTypeDef = TypedDict(
    "ListJobRunsRequestRequestTypeDef",
    {
        "applicationId": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "createdAtAfter": NotRequired[TimestampTypeDef],
        "createdAtBefore": NotRequired[TimestampTypeDef],
        "states": NotRequired[Sequence[JobRunStateType]],
    },
)
MonitoringConfigurationTypeDef = TypedDict(
    "MonitoringConfigurationTypeDef",
    {
        "s3MonitoringConfiguration": NotRequired[S3MonitoringConfigurationTypeDef],
        "managedPersistenceMonitoringConfiguration": NotRequired[
            ManagedPersistenceMonitoringConfigurationTypeDef
        ],
        "cloudWatchLoggingConfiguration": NotRequired[CloudWatchLoggingConfigurationTypeDef],
    },
)
ApplicationTypeDef = TypedDict(
    "ApplicationTypeDef",
    {
        "applicationId": str,
        "arn": str,
        "releaseLabel": str,
        "type": str,
        "state": ApplicationStateType,
        "createdAt": datetime,
        "updatedAt": datetime,
        "name": NotRequired[str],
        "stateDetails": NotRequired[str],
        "initialCapacity": NotRequired[Dict[str, InitialCapacityConfigTypeDef]],
        "maximumCapacity": NotRequired[MaximumAllowedResourcesTypeDef],
        "tags": NotRequired[Dict[str, str]],
        "autoStartConfiguration": NotRequired[AutoStartConfigTypeDef],
        "autoStopConfiguration": NotRequired[AutoStopConfigTypeDef],
        "networkConfiguration": NotRequired[NetworkConfigurationTypeDef],
        "architecture": NotRequired[ArchitectureType],
        "imageConfiguration": NotRequired[ImageConfigurationTypeDef],
        "workerTypeSpecifications": NotRequired[Dict[str, WorkerTypeSpecificationTypeDef]],
        "runtimeConfiguration": NotRequired[List["ConfigurationTypeDef"]],
        "monitoringConfiguration": NotRequired[MonitoringConfigurationTypeDef],
    },
)
ConfigurationOverridesTypeDef = TypedDict(
    "ConfigurationOverridesTypeDef",
    {
        "applicationConfiguration": NotRequired[List["ConfigurationTypeDef"]],
        "monitoringConfiguration": NotRequired[MonitoringConfigurationTypeDef],
    },
)
CreateApplicationRequestRequestTypeDef = TypedDict(
    "CreateApplicationRequestRequestTypeDef",
    {
        "releaseLabel": str,
        "type": str,
        "clientToken": str,
        "name": NotRequired[str],
        "initialCapacity": NotRequired[Mapping[str, InitialCapacityConfigTypeDef]],
        "maximumCapacity": NotRequired[MaximumAllowedResourcesTypeDef],
        "tags": NotRequired[Mapping[str, str]],
        "autoStartConfiguration": NotRequired[AutoStartConfigTypeDef],
        "autoStopConfiguration": NotRequired[AutoStopConfigTypeDef],
        "networkConfiguration": NotRequired[NetworkConfigurationTypeDef],
        "architecture": NotRequired[ArchitectureType],
        "imageConfiguration": NotRequired[ImageConfigurationInputTypeDef],
        "workerTypeSpecifications": NotRequired[Mapping[str, WorkerTypeSpecificationInputTypeDef]],
        "runtimeConfiguration": NotRequired[Sequence["ConfigurationTypeDef"]],
        "monitoringConfiguration": NotRequired[MonitoringConfigurationTypeDef],
    },
)
UpdateApplicationRequestRequestTypeDef = TypedDict(
    "UpdateApplicationRequestRequestTypeDef",
    {
        "applicationId": str,
        "clientToken": str,
        "initialCapacity": NotRequired[Mapping[str, InitialCapacityConfigTypeDef]],
        "maximumCapacity": NotRequired[MaximumAllowedResourcesTypeDef],
        "autoStartConfiguration": NotRequired[AutoStartConfigTypeDef],
        "autoStopConfiguration": NotRequired[AutoStopConfigTypeDef],
        "networkConfiguration": NotRequired[NetworkConfigurationTypeDef],
        "architecture": NotRequired[ArchitectureType],
        "imageConfiguration": NotRequired[ImageConfigurationInputTypeDef],
        "workerTypeSpecifications": NotRequired[Mapping[str, WorkerTypeSpecificationInputTypeDef]],
        "releaseLabel": NotRequired[str],
        "runtimeConfiguration": NotRequired[Sequence["ConfigurationTypeDef"]],
        "monitoringConfiguration": NotRequired[MonitoringConfigurationTypeDef],
    },
)
GetApplicationResponseTypeDef = TypedDict(
    "GetApplicationResponseTypeDef",
    {
        "application": ApplicationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateApplicationResponseTypeDef = TypedDict(
    "UpdateApplicationResponseTypeDef",
    {
        "application": ApplicationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
JobRunTypeDef = TypedDict(
    "JobRunTypeDef",
    {
        "applicationId": str,
        "jobRunId": str,
        "arn": str,
        "createdBy": str,
        "createdAt": datetime,
        "updatedAt": datetime,
        "executionRole": str,
        "state": JobRunStateType,
        "stateDetails": str,
        "releaseLabel": str,
        "jobDriver": JobDriverTypeDef,
        "name": NotRequired[str],
        "configurationOverrides": NotRequired[ConfigurationOverridesTypeDef],
        "tags": NotRequired[Dict[str, str]],
        "totalResourceUtilization": NotRequired[TotalResourceUtilizationTypeDef],
        "networkConfiguration": NotRequired[NetworkConfigurationTypeDef],
        "totalExecutionDurationSeconds": NotRequired[int],
        "executionTimeoutMinutes": NotRequired[int],
        "billedResourceUtilization": NotRequired[ResourceUtilizationTypeDef],
    },
)
StartJobRunRequestRequestTypeDef = TypedDict(
    "StartJobRunRequestRequestTypeDef",
    {
        "applicationId": str,
        "clientToken": str,
        "executionRoleArn": str,
        "jobDriver": NotRequired[JobDriverTypeDef],
        "configurationOverrides": NotRequired[ConfigurationOverridesTypeDef],
        "tags": NotRequired[Mapping[str, str]],
        "executionTimeoutMinutes": NotRequired[int],
        "name": NotRequired[str],
    },
)
GetJobRunResponseTypeDef = TypedDict(
    "GetJobRunResponseTypeDef",
    {
        "jobRun": JobRunTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
