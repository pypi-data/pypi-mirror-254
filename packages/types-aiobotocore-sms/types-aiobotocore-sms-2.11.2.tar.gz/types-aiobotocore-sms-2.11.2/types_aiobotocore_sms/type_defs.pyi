"""
Type annotations for sms service type definitions.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sms/type_defs/)

Usage::

    ```python
    from types_aiobotocore_sms.type_defs import LaunchDetailsTypeDef

    data: LaunchDetailsTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Sequence, Union

from .literals import (
    AppLaunchConfigurationStatusType,
    AppLaunchStatusType,
    AppReplicationConfigurationStatusType,
    AppReplicationStatusType,
    AppStatusType,
    ConnectorCapabilityType,
    ConnectorStatusType,
    LicenseTypeType,
    OutputFormatType,
    ReplicationJobStateType,
    ReplicationRunStateType,
    ReplicationRunTypeType,
    ScriptTypeType,
    ServerCatalogStatusType,
    ValidationStatusType,
    VmManagerTypeType,
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
    "LaunchDetailsTypeDef",
    "ConnectorTypeDef",
    "TagTypeDef",
    "ResponseMetadataTypeDef",
    "TimestampTypeDef",
    "DeleteAppLaunchConfigurationRequestRequestTypeDef",
    "DeleteAppReplicationConfigurationRequestRequestTypeDef",
    "DeleteAppRequestRequestTypeDef",
    "DeleteAppValidationConfigurationRequestRequestTypeDef",
    "DeleteReplicationJobRequestRequestTypeDef",
    "DisassociateConnectorRequestRequestTypeDef",
    "GenerateChangeSetRequestRequestTypeDef",
    "S3LocationTypeDef",
    "GenerateTemplateRequestRequestTypeDef",
    "GetAppLaunchConfigurationRequestRequestTypeDef",
    "GetAppReplicationConfigurationRequestRequestTypeDef",
    "GetAppRequestRequestTypeDef",
    "GetAppValidationConfigurationRequestRequestTypeDef",
    "GetAppValidationOutputRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "GetConnectorsRequestRequestTypeDef",
    "GetReplicationJobsRequestRequestTypeDef",
    "GetReplicationRunsRequestRequestTypeDef",
    "VmServerAddressTypeDef",
    "ImportAppCatalogRequestRequestTypeDef",
    "LaunchAppRequestRequestTypeDef",
    "ListAppsRequestRequestTypeDef",
    "NotificationContextTypeDef",
    "ReplicationRunStageDetailsTypeDef",
    "ServerReplicationParametersTypeDef",
    "StartAppReplicationRequestRequestTypeDef",
    "StartOnDemandAppReplicationRequestRequestTypeDef",
    "StartOnDemandReplicationRunRequestRequestTypeDef",
    "StopAppReplicationRequestRequestTypeDef",
    "TerminateAppRequestRequestTypeDef",
    "AppSummaryTypeDef",
    "CreateReplicationJobResponseTypeDef",
    "GetConnectorsResponseTypeDef",
    "StartOnDemandReplicationRunResponseTypeDef",
    "CreateReplicationJobRequestRequestTypeDef",
    "UpdateReplicationJobRequestRequestTypeDef",
    "GenerateChangeSetResponseTypeDef",
    "GenerateTemplateResponseTypeDef",
    "SSMOutputTypeDef",
    "SourceTypeDef",
    "UserDataTypeDef",
    "GetConnectorsRequestGetConnectorsPaginateTypeDef",
    "GetReplicationJobsRequestGetReplicationJobsPaginateTypeDef",
    "GetReplicationRunsRequestGetReplicationRunsPaginateTypeDef",
    "ListAppsRequestListAppsPaginateTypeDef",
    "GetServersRequestGetServersPaginateTypeDef",
    "GetServersRequestRequestTypeDef",
    "VmServerTypeDef",
    "NotifyAppValidationOutputRequestRequestTypeDef",
    "ReplicationRunTypeDef",
    "ListAppsResponseTypeDef",
    "AppValidationOutputTypeDef",
    "SSMValidationParametersTypeDef",
    "UserDataValidationParametersTypeDef",
    "ServerTypeDef",
    "ReplicationJobTypeDef",
    "AppValidationConfigurationTypeDef",
    "GetServersResponseTypeDef",
    "ServerGroupTypeDef",
    "ServerLaunchConfigurationTypeDef",
    "ServerReplicationConfigurationTypeDef",
    "ServerValidationConfigurationTypeDef",
    "ServerValidationOutputTypeDef",
    "GetReplicationJobsResponseTypeDef",
    "GetReplicationRunsResponseTypeDef",
    "CreateAppRequestRequestTypeDef",
    "CreateAppResponseTypeDef",
    "GetAppResponseTypeDef",
    "UpdateAppRequestRequestTypeDef",
    "UpdateAppResponseTypeDef",
    "ServerGroupLaunchConfigurationTypeDef",
    "ServerGroupReplicationConfigurationTypeDef",
    "ServerGroupValidationConfigurationTypeDef",
    "ValidationOutputTypeDef",
    "GetAppLaunchConfigurationResponseTypeDef",
    "PutAppLaunchConfigurationRequestRequestTypeDef",
    "GetAppReplicationConfigurationResponseTypeDef",
    "PutAppReplicationConfigurationRequestRequestTypeDef",
    "GetAppValidationConfigurationResponseTypeDef",
    "PutAppValidationConfigurationRequestRequestTypeDef",
    "GetAppValidationOutputResponseTypeDef",
)

LaunchDetailsTypeDef = TypedDict(
    "LaunchDetailsTypeDef",
    {
        "latestLaunchTime": NotRequired[datetime],
        "stackName": NotRequired[str],
        "stackId": NotRequired[str],
    },
)
ConnectorTypeDef = TypedDict(
    "ConnectorTypeDef",
    {
        "connectorId": NotRequired[str],
        "version": NotRequired[str],
        "status": NotRequired[ConnectorStatusType],
        "capabilityList": NotRequired[List[ConnectorCapabilityType]],
        "vmManagerName": NotRequired[str],
        "vmManagerType": NotRequired[VmManagerTypeType],
        "vmManagerId": NotRequired[str],
        "ipAddress": NotRequired[str],
        "macAddress": NotRequired[str],
        "associatedOn": NotRequired[datetime],
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "key": NotRequired[str],
        "value": NotRequired[str],
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
TimestampTypeDef = Union[datetime, str]
DeleteAppLaunchConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteAppLaunchConfigurationRequestRequestTypeDef",
    {
        "appId": NotRequired[str],
    },
)
DeleteAppReplicationConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteAppReplicationConfigurationRequestRequestTypeDef",
    {
        "appId": NotRequired[str],
    },
)
DeleteAppRequestRequestTypeDef = TypedDict(
    "DeleteAppRequestRequestTypeDef",
    {
        "appId": NotRequired[str],
        "forceStopAppReplication": NotRequired[bool],
        "forceTerminateApp": NotRequired[bool],
    },
)
DeleteAppValidationConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteAppValidationConfigurationRequestRequestTypeDef",
    {
        "appId": str,
    },
)
DeleteReplicationJobRequestRequestTypeDef = TypedDict(
    "DeleteReplicationJobRequestRequestTypeDef",
    {
        "replicationJobId": str,
    },
)
DisassociateConnectorRequestRequestTypeDef = TypedDict(
    "DisassociateConnectorRequestRequestTypeDef",
    {
        "connectorId": str,
    },
)
GenerateChangeSetRequestRequestTypeDef = TypedDict(
    "GenerateChangeSetRequestRequestTypeDef",
    {
        "appId": NotRequired[str],
        "changesetFormat": NotRequired[OutputFormatType],
    },
)
S3LocationTypeDef = TypedDict(
    "S3LocationTypeDef",
    {
        "bucket": NotRequired[str],
        "key": NotRequired[str],
    },
)
GenerateTemplateRequestRequestTypeDef = TypedDict(
    "GenerateTemplateRequestRequestTypeDef",
    {
        "appId": NotRequired[str],
        "templateFormat": NotRequired[OutputFormatType],
    },
)
GetAppLaunchConfigurationRequestRequestTypeDef = TypedDict(
    "GetAppLaunchConfigurationRequestRequestTypeDef",
    {
        "appId": NotRequired[str],
    },
)
GetAppReplicationConfigurationRequestRequestTypeDef = TypedDict(
    "GetAppReplicationConfigurationRequestRequestTypeDef",
    {
        "appId": NotRequired[str],
    },
)
GetAppRequestRequestTypeDef = TypedDict(
    "GetAppRequestRequestTypeDef",
    {
        "appId": NotRequired[str],
    },
)
GetAppValidationConfigurationRequestRequestTypeDef = TypedDict(
    "GetAppValidationConfigurationRequestRequestTypeDef",
    {
        "appId": str,
    },
)
GetAppValidationOutputRequestRequestTypeDef = TypedDict(
    "GetAppValidationOutputRequestRequestTypeDef",
    {
        "appId": str,
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
GetConnectorsRequestRequestTypeDef = TypedDict(
    "GetConnectorsRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
GetReplicationJobsRequestRequestTypeDef = TypedDict(
    "GetReplicationJobsRequestRequestTypeDef",
    {
        "replicationJobId": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
GetReplicationRunsRequestRequestTypeDef = TypedDict(
    "GetReplicationRunsRequestRequestTypeDef",
    {
        "replicationJobId": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
VmServerAddressTypeDef = TypedDict(
    "VmServerAddressTypeDef",
    {
        "vmManagerId": NotRequired[str],
        "vmId": NotRequired[str],
    },
)
ImportAppCatalogRequestRequestTypeDef = TypedDict(
    "ImportAppCatalogRequestRequestTypeDef",
    {
        "roleName": NotRequired[str],
    },
)
LaunchAppRequestRequestTypeDef = TypedDict(
    "LaunchAppRequestRequestTypeDef",
    {
        "appId": NotRequired[str],
    },
)
ListAppsRequestRequestTypeDef = TypedDict(
    "ListAppsRequestRequestTypeDef",
    {
        "appIds": NotRequired[Sequence[str]],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
NotificationContextTypeDef = TypedDict(
    "NotificationContextTypeDef",
    {
        "validationId": NotRequired[str],
        "status": NotRequired[ValidationStatusType],
        "statusMessage": NotRequired[str],
    },
)
ReplicationRunStageDetailsTypeDef = TypedDict(
    "ReplicationRunStageDetailsTypeDef",
    {
        "stage": NotRequired[str],
        "stageProgress": NotRequired[str],
    },
)
ServerReplicationParametersTypeDef = TypedDict(
    "ServerReplicationParametersTypeDef",
    {
        "seedTime": NotRequired[datetime],
        "frequency": NotRequired[int],
        "runOnce": NotRequired[bool],
        "licenseType": NotRequired[LicenseTypeType],
        "numberOfRecentAmisToKeep": NotRequired[int],
        "encrypted": NotRequired[bool],
        "kmsKeyId": NotRequired[str],
    },
)
StartAppReplicationRequestRequestTypeDef = TypedDict(
    "StartAppReplicationRequestRequestTypeDef",
    {
        "appId": NotRequired[str],
    },
)
StartOnDemandAppReplicationRequestRequestTypeDef = TypedDict(
    "StartOnDemandAppReplicationRequestRequestTypeDef",
    {
        "appId": str,
        "description": NotRequired[str],
    },
)
StartOnDemandReplicationRunRequestRequestTypeDef = TypedDict(
    "StartOnDemandReplicationRunRequestRequestTypeDef",
    {
        "replicationJobId": str,
        "description": NotRequired[str],
    },
)
StopAppReplicationRequestRequestTypeDef = TypedDict(
    "StopAppReplicationRequestRequestTypeDef",
    {
        "appId": NotRequired[str],
    },
)
TerminateAppRequestRequestTypeDef = TypedDict(
    "TerminateAppRequestRequestTypeDef",
    {
        "appId": NotRequired[str],
    },
)
AppSummaryTypeDef = TypedDict(
    "AppSummaryTypeDef",
    {
        "appId": NotRequired[str],
        "importedAppId": NotRequired[str],
        "name": NotRequired[str],
        "description": NotRequired[str],
        "status": NotRequired[AppStatusType],
        "statusMessage": NotRequired[str],
        "replicationConfigurationStatus": NotRequired[AppReplicationConfigurationStatusType],
        "replicationStatus": NotRequired[AppReplicationStatusType],
        "replicationStatusMessage": NotRequired[str],
        "latestReplicationTime": NotRequired[datetime],
        "launchConfigurationStatus": NotRequired[AppLaunchConfigurationStatusType],
        "launchStatus": NotRequired[AppLaunchStatusType],
        "launchStatusMessage": NotRequired[str],
        "launchDetails": NotRequired[LaunchDetailsTypeDef],
        "creationTime": NotRequired[datetime],
        "lastModified": NotRequired[datetime],
        "roleName": NotRequired[str],
        "totalServerGroups": NotRequired[int],
        "totalServers": NotRequired[int],
    },
)
CreateReplicationJobResponseTypeDef = TypedDict(
    "CreateReplicationJobResponseTypeDef",
    {
        "replicationJobId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetConnectorsResponseTypeDef = TypedDict(
    "GetConnectorsResponseTypeDef",
    {
        "connectorList": List[ConnectorTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartOnDemandReplicationRunResponseTypeDef = TypedDict(
    "StartOnDemandReplicationRunResponseTypeDef",
    {
        "replicationRunId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateReplicationJobRequestRequestTypeDef = TypedDict(
    "CreateReplicationJobRequestRequestTypeDef",
    {
        "serverId": str,
        "seedReplicationTime": TimestampTypeDef,
        "frequency": NotRequired[int],
        "runOnce": NotRequired[bool],
        "licenseType": NotRequired[LicenseTypeType],
        "roleName": NotRequired[str],
        "description": NotRequired[str],
        "numberOfRecentAmisToKeep": NotRequired[int],
        "encrypted": NotRequired[bool],
        "kmsKeyId": NotRequired[str],
    },
)
UpdateReplicationJobRequestRequestTypeDef = TypedDict(
    "UpdateReplicationJobRequestRequestTypeDef",
    {
        "replicationJobId": str,
        "frequency": NotRequired[int],
        "nextReplicationRunStartTime": NotRequired[TimestampTypeDef],
        "licenseType": NotRequired[LicenseTypeType],
        "roleName": NotRequired[str],
        "description": NotRequired[str],
        "numberOfRecentAmisToKeep": NotRequired[int],
        "encrypted": NotRequired[bool],
        "kmsKeyId": NotRequired[str],
    },
)
GenerateChangeSetResponseTypeDef = TypedDict(
    "GenerateChangeSetResponseTypeDef",
    {
        "s3Location": S3LocationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GenerateTemplateResponseTypeDef = TypedDict(
    "GenerateTemplateResponseTypeDef",
    {
        "s3Location": S3LocationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SSMOutputTypeDef = TypedDict(
    "SSMOutputTypeDef",
    {
        "s3Location": NotRequired[S3LocationTypeDef],
    },
)
SourceTypeDef = TypedDict(
    "SourceTypeDef",
    {
        "s3Location": NotRequired[S3LocationTypeDef],
    },
)
UserDataTypeDef = TypedDict(
    "UserDataTypeDef",
    {
        "s3Location": NotRequired[S3LocationTypeDef],
    },
)
GetConnectorsRequestGetConnectorsPaginateTypeDef = TypedDict(
    "GetConnectorsRequestGetConnectorsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetReplicationJobsRequestGetReplicationJobsPaginateTypeDef = TypedDict(
    "GetReplicationJobsRequestGetReplicationJobsPaginateTypeDef",
    {
        "replicationJobId": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetReplicationRunsRequestGetReplicationRunsPaginateTypeDef = TypedDict(
    "GetReplicationRunsRequestGetReplicationRunsPaginateTypeDef",
    {
        "replicationJobId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListAppsRequestListAppsPaginateTypeDef = TypedDict(
    "ListAppsRequestListAppsPaginateTypeDef",
    {
        "appIds": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetServersRequestGetServersPaginateTypeDef = TypedDict(
    "GetServersRequestGetServersPaginateTypeDef",
    {
        "vmServerAddressList": NotRequired[Sequence[VmServerAddressTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetServersRequestRequestTypeDef = TypedDict(
    "GetServersRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "vmServerAddressList": NotRequired[Sequence[VmServerAddressTypeDef]],
    },
)
VmServerTypeDef = TypedDict(
    "VmServerTypeDef",
    {
        "vmServerAddress": NotRequired[VmServerAddressTypeDef],
        "vmName": NotRequired[str],
        "vmManagerName": NotRequired[str],
        "vmManagerType": NotRequired[VmManagerTypeType],
        "vmPath": NotRequired[str],
    },
)
NotifyAppValidationOutputRequestRequestTypeDef = TypedDict(
    "NotifyAppValidationOutputRequestRequestTypeDef",
    {
        "appId": str,
        "notificationContext": NotRequired[NotificationContextTypeDef],
    },
)
ReplicationRunTypeDef = TypedDict(
    "ReplicationRunTypeDef",
    {
        "replicationRunId": NotRequired[str],
        "state": NotRequired[ReplicationRunStateType],
        "type": NotRequired[ReplicationRunTypeType],
        "stageDetails": NotRequired[ReplicationRunStageDetailsTypeDef],
        "statusMessage": NotRequired[str],
        "amiId": NotRequired[str],
        "scheduledStartTime": NotRequired[datetime],
        "completedTime": NotRequired[datetime],
        "description": NotRequired[str],
        "encrypted": NotRequired[bool],
        "kmsKeyId": NotRequired[str],
    },
)
ListAppsResponseTypeDef = TypedDict(
    "ListAppsResponseTypeDef",
    {
        "apps": List[AppSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AppValidationOutputTypeDef = TypedDict(
    "AppValidationOutputTypeDef",
    {
        "ssmOutput": NotRequired[SSMOutputTypeDef],
    },
)
SSMValidationParametersTypeDef = TypedDict(
    "SSMValidationParametersTypeDef",
    {
        "source": NotRequired[SourceTypeDef],
        "instanceId": NotRequired[str],
        "scriptType": NotRequired[ScriptTypeType],
        "command": NotRequired[str],
        "executionTimeoutSeconds": NotRequired[int],
        "outputS3BucketName": NotRequired[str],
    },
)
UserDataValidationParametersTypeDef = TypedDict(
    "UserDataValidationParametersTypeDef",
    {
        "source": NotRequired[SourceTypeDef],
        "scriptType": NotRequired[ScriptTypeType],
    },
)
ServerTypeDef = TypedDict(
    "ServerTypeDef",
    {
        "serverId": NotRequired[str],
        "serverType": NotRequired[Literal["VIRTUAL_MACHINE"]],
        "vmServer": NotRequired[VmServerTypeDef],
        "replicationJobId": NotRequired[str],
        "replicationJobTerminated": NotRequired[bool],
    },
)
ReplicationJobTypeDef = TypedDict(
    "ReplicationJobTypeDef",
    {
        "replicationJobId": NotRequired[str],
        "serverId": NotRequired[str],
        "serverType": NotRequired[Literal["VIRTUAL_MACHINE"]],
        "vmServer": NotRequired[VmServerTypeDef],
        "seedReplicationTime": NotRequired[datetime],
        "frequency": NotRequired[int],
        "runOnce": NotRequired[bool],
        "nextReplicationRunStartTime": NotRequired[datetime],
        "licenseType": NotRequired[LicenseTypeType],
        "roleName": NotRequired[str],
        "latestAmiId": NotRequired[str],
        "state": NotRequired[ReplicationJobStateType],
        "statusMessage": NotRequired[str],
        "description": NotRequired[str],
        "numberOfRecentAmisToKeep": NotRequired[int],
        "encrypted": NotRequired[bool],
        "kmsKeyId": NotRequired[str],
        "replicationRunList": NotRequired[List[ReplicationRunTypeDef]],
    },
)
AppValidationConfigurationTypeDef = TypedDict(
    "AppValidationConfigurationTypeDef",
    {
        "validationId": NotRequired[str],
        "name": NotRequired[str],
        "appValidationStrategy": NotRequired[Literal["SSM"]],
        "ssmValidationParameters": NotRequired[SSMValidationParametersTypeDef],
    },
)
GetServersResponseTypeDef = TypedDict(
    "GetServersResponseTypeDef",
    {
        "lastModifiedOn": datetime,
        "serverCatalogStatus": ServerCatalogStatusType,
        "serverList": List[ServerTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ServerGroupTypeDef = TypedDict(
    "ServerGroupTypeDef",
    {
        "serverGroupId": NotRequired[str],
        "name": NotRequired[str],
        "serverList": NotRequired[Sequence[ServerTypeDef]],
    },
)
ServerLaunchConfigurationTypeDef = TypedDict(
    "ServerLaunchConfigurationTypeDef",
    {
        "server": NotRequired[ServerTypeDef],
        "logicalId": NotRequired[str],
        "vpc": NotRequired[str],
        "subnet": NotRequired[str],
        "securityGroup": NotRequired[str],
        "ec2KeyName": NotRequired[str],
        "userData": NotRequired[UserDataTypeDef],
        "instanceType": NotRequired[str],
        "associatePublicIpAddress": NotRequired[bool],
        "iamInstanceProfileName": NotRequired[str],
        "configureScript": NotRequired[S3LocationTypeDef],
        "configureScriptType": NotRequired[ScriptTypeType],
    },
)
ServerReplicationConfigurationTypeDef = TypedDict(
    "ServerReplicationConfigurationTypeDef",
    {
        "server": NotRequired[ServerTypeDef],
        "serverReplicationParameters": NotRequired[ServerReplicationParametersTypeDef],
    },
)
ServerValidationConfigurationTypeDef = TypedDict(
    "ServerValidationConfigurationTypeDef",
    {
        "server": NotRequired[ServerTypeDef],
        "validationId": NotRequired[str],
        "name": NotRequired[str],
        "serverValidationStrategy": NotRequired[Literal["USERDATA"]],
        "userDataValidationParameters": NotRequired[UserDataValidationParametersTypeDef],
    },
)
ServerValidationOutputTypeDef = TypedDict(
    "ServerValidationOutputTypeDef",
    {
        "server": NotRequired[ServerTypeDef],
    },
)
GetReplicationJobsResponseTypeDef = TypedDict(
    "GetReplicationJobsResponseTypeDef",
    {
        "replicationJobList": List[ReplicationJobTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetReplicationRunsResponseTypeDef = TypedDict(
    "GetReplicationRunsResponseTypeDef",
    {
        "replicationJob": ReplicationJobTypeDef,
        "replicationRunList": List[ReplicationRunTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateAppRequestRequestTypeDef = TypedDict(
    "CreateAppRequestRequestTypeDef",
    {
        "name": NotRequired[str],
        "description": NotRequired[str],
        "roleName": NotRequired[str],
        "clientToken": NotRequired[str],
        "serverGroups": NotRequired[Sequence[ServerGroupTypeDef]],
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateAppResponseTypeDef = TypedDict(
    "CreateAppResponseTypeDef",
    {
        "appSummary": AppSummaryTypeDef,
        "serverGroups": List[ServerGroupTypeDef],
        "tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAppResponseTypeDef = TypedDict(
    "GetAppResponseTypeDef",
    {
        "appSummary": AppSummaryTypeDef,
        "serverGroups": List[ServerGroupTypeDef],
        "tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateAppRequestRequestTypeDef = TypedDict(
    "UpdateAppRequestRequestTypeDef",
    {
        "appId": NotRequired[str],
        "name": NotRequired[str],
        "description": NotRequired[str],
        "roleName": NotRequired[str],
        "serverGroups": NotRequired[Sequence[ServerGroupTypeDef]],
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
UpdateAppResponseTypeDef = TypedDict(
    "UpdateAppResponseTypeDef",
    {
        "appSummary": AppSummaryTypeDef,
        "serverGroups": List[ServerGroupTypeDef],
        "tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ServerGroupLaunchConfigurationTypeDef = TypedDict(
    "ServerGroupLaunchConfigurationTypeDef",
    {
        "serverGroupId": NotRequired[str],
        "launchOrder": NotRequired[int],
        "serverLaunchConfigurations": NotRequired[List[ServerLaunchConfigurationTypeDef]],
    },
)
ServerGroupReplicationConfigurationTypeDef = TypedDict(
    "ServerGroupReplicationConfigurationTypeDef",
    {
        "serverGroupId": NotRequired[str],
        "serverReplicationConfigurations": NotRequired[List[ServerReplicationConfigurationTypeDef]],
    },
)
ServerGroupValidationConfigurationTypeDef = TypedDict(
    "ServerGroupValidationConfigurationTypeDef",
    {
        "serverGroupId": NotRequired[str],
        "serverValidationConfigurations": NotRequired[List[ServerValidationConfigurationTypeDef]],
    },
)
ValidationOutputTypeDef = TypedDict(
    "ValidationOutputTypeDef",
    {
        "validationId": NotRequired[str],
        "name": NotRequired[str],
        "status": NotRequired[ValidationStatusType],
        "statusMessage": NotRequired[str],
        "latestValidationTime": NotRequired[datetime],
        "appValidationOutput": NotRequired[AppValidationOutputTypeDef],
        "serverValidationOutput": NotRequired[ServerValidationOutputTypeDef],
    },
)
GetAppLaunchConfigurationResponseTypeDef = TypedDict(
    "GetAppLaunchConfigurationResponseTypeDef",
    {
        "appId": str,
        "roleName": str,
        "autoLaunch": bool,
        "serverGroupLaunchConfigurations": List[ServerGroupLaunchConfigurationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutAppLaunchConfigurationRequestRequestTypeDef = TypedDict(
    "PutAppLaunchConfigurationRequestRequestTypeDef",
    {
        "appId": NotRequired[str],
        "roleName": NotRequired[str],
        "autoLaunch": NotRequired[bool],
        "serverGroupLaunchConfigurations": NotRequired[
            Sequence[ServerGroupLaunchConfigurationTypeDef]
        ],
    },
)
GetAppReplicationConfigurationResponseTypeDef = TypedDict(
    "GetAppReplicationConfigurationResponseTypeDef",
    {
        "serverGroupReplicationConfigurations": List[ServerGroupReplicationConfigurationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutAppReplicationConfigurationRequestRequestTypeDef = TypedDict(
    "PutAppReplicationConfigurationRequestRequestTypeDef",
    {
        "appId": NotRequired[str],
        "serverGroupReplicationConfigurations": NotRequired[
            Sequence[ServerGroupReplicationConfigurationTypeDef]
        ],
    },
)
GetAppValidationConfigurationResponseTypeDef = TypedDict(
    "GetAppValidationConfigurationResponseTypeDef",
    {
        "appValidationConfigurations": List[AppValidationConfigurationTypeDef],
        "serverGroupValidationConfigurations": List[ServerGroupValidationConfigurationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutAppValidationConfigurationRequestRequestTypeDef = TypedDict(
    "PutAppValidationConfigurationRequestRequestTypeDef",
    {
        "appId": str,
        "appValidationConfigurations": NotRequired[Sequence[AppValidationConfigurationTypeDef]],
        "serverGroupValidationConfigurations": NotRequired[
            Sequence[ServerGroupValidationConfigurationTypeDef]
        ],
    },
)
GetAppValidationOutputResponseTypeDef = TypedDict(
    "GetAppValidationOutputResponseTypeDef",
    {
        "validationOutputList": List[ValidationOutputTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
