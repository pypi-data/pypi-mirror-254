"""
Type annotations for ssm-sap service type definitions.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ssm_sap/type_defs/)

Usage::

    ```python
    from types_aiobotocore_ssm_sap.type_defs import ApplicationCredentialTypeDef

    data: ApplicationCredentialTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from .literals import (
    AllocationTypeType,
    ApplicationDiscoveryStatusType,
    ApplicationStatusType,
    ApplicationTypeType,
    ClusterStatusType,
    ComponentStatusType,
    ComponentTypeType,
    DatabaseConnectionMethodType,
    DatabaseStatusType,
    DatabaseTypeType,
    FilterOperatorType,
    HostRoleType,
    OperationModeType,
    OperationStatusType,
    ReplicationModeType,
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
    "ApplicationCredentialTypeDef",
    "ApplicationSummaryTypeDef",
    "ApplicationTypeDef",
    "IpAddressMemberTypeDef",
    "BackintConfigTypeDef",
    "ComponentSummaryTypeDef",
    "DatabaseConnectionTypeDef",
    "HostTypeDef",
    "ResilienceTypeDef",
    "DatabaseSummaryTypeDef",
    "DeleteResourcePermissionInputRequestTypeDef",
    "ResponseMetadataTypeDef",
    "DeregisterApplicationInputRequestTypeDef",
    "FilterTypeDef",
    "GetApplicationInputRequestTypeDef",
    "GetComponentInputRequestTypeDef",
    "GetDatabaseInputRequestTypeDef",
    "GetOperationInputRequestTypeDef",
    "OperationTypeDef",
    "GetResourcePermissionInputRequestTypeDef",
    "PaginatorConfigTypeDef",
    "ListComponentsInputRequestTypeDef",
    "ListDatabasesInputRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "PutResourcePermissionInputRequestTypeDef",
    "StartApplicationRefreshInputRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "DatabaseTypeDef",
    "RegisterApplicationInputRequestTypeDef",
    "AssociatedHostTypeDef",
    "UpdateApplicationSettingsInputRequestTypeDef",
    "DeleteResourcePermissionOutputTypeDef",
    "GetApplicationOutputTypeDef",
    "GetResourcePermissionOutputTypeDef",
    "ListApplicationsOutputTypeDef",
    "ListComponentsOutputTypeDef",
    "ListDatabasesOutputTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PutResourcePermissionOutputTypeDef",
    "RegisterApplicationOutputTypeDef",
    "StartApplicationRefreshOutputTypeDef",
    "UpdateApplicationSettingsOutputTypeDef",
    "ListApplicationsInputRequestTypeDef",
    "ListOperationsInputRequestTypeDef",
    "GetOperationOutputTypeDef",
    "ListOperationsOutputTypeDef",
    "ListApplicationsInputListApplicationsPaginateTypeDef",
    "ListComponentsInputListComponentsPaginateTypeDef",
    "ListDatabasesInputListDatabasesPaginateTypeDef",
    "ListOperationsInputListOperationsPaginateTypeDef",
    "GetDatabaseOutputTypeDef",
    "ComponentTypeDef",
    "GetComponentOutputTypeDef",
)

ApplicationCredentialTypeDef = TypedDict(
    "ApplicationCredentialTypeDef",
    {
        "DatabaseName": str,
        "CredentialType": Literal["ADMIN"],
        "SecretId": str,
    },
)
ApplicationSummaryTypeDef = TypedDict(
    "ApplicationSummaryTypeDef",
    {
        "Id": NotRequired[str],
        "DiscoveryStatus": NotRequired[ApplicationDiscoveryStatusType],
        "Type": NotRequired[ApplicationTypeType],
        "Arn": NotRequired[str],
        "Tags": NotRequired[Dict[str, str]],
    },
)
ApplicationTypeDef = TypedDict(
    "ApplicationTypeDef",
    {
        "Id": NotRequired[str],
        "Type": NotRequired[ApplicationTypeType],
        "Arn": NotRequired[str],
        "AppRegistryArn": NotRequired[str],
        "Status": NotRequired[ApplicationStatusType],
        "DiscoveryStatus": NotRequired[ApplicationDiscoveryStatusType],
        "Components": NotRequired[List[str]],
        "LastUpdated": NotRequired[datetime],
        "StatusMessage": NotRequired[str],
    },
)
IpAddressMemberTypeDef = TypedDict(
    "IpAddressMemberTypeDef",
    {
        "IpAddress": NotRequired[str],
        "Primary": NotRequired[bool],
        "AllocationType": NotRequired[AllocationTypeType],
    },
)
BackintConfigTypeDef = TypedDict(
    "BackintConfigTypeDef",
    {
        "BackintMode": Literal["AWSBackup"],
        "EnsureNoBackupInProcess": bool,
    },
)
ComponentSummaryTypeDef = TypedDict(
    "ComponentSummaryTypeDef",
    {
        "ApplicationId": NotRequired[str],
        "ComponentId": NotRequired[str],
        "ComponentType": NotRequired[ComponentTypeType],
        "Tags": NotRequired[Dict[str, str]],
        "Arn": NotRequired[str],
    },
)
DatabaseConnectionTypeDef = TypedDict(
    "DatabaseConnectionTypeDef",
    {
        "DatabaseConnectionMethod": NotRequired[DatabaseConnectionMethodType],
        "DatabaseArn": NotRequired[str],
        "ConnectionIp": NotRequired[str],
    },
)
HostTypeDef = TypedDict(
    "HostTypeDef",
    {
        "HostName": NotRequired[str],
        "HostIp": NotRequired[str],
        "EC2InstanceId": NotRequired[str],
        "InstanceId": NotRequired[str],
        "HostRole": NotRequired[HostRoleType],
        "OsVersion": NotRequired[str],
    },
)
ResilienceTypeDef = TypedDict(
    "ResilienceTypeDef",
    {
        "HsrTier": NotRequired[str],
        "HsrReplicationMode": NotRequired[ReplicationModeType],
        "HsrOperationMode": NotRequired[OperationModeType],
        "ClusterStatus": NotRequired[ClusterStatusType],
        "EnqueueReplication": NotRequired[bool],
    },
)
DatabaseSummaryTypeDef = TypedDict(
    "DatabaseSummaryTypeDef",
    {
        "ApplicationId": NotRequired[str],
        "ComponentId": NotRequired[str],
        "DatabaseId": NotRequired[str],
        "DatabaseType": NotRequired[DatabaseTypeType],
        "Arn": NotRequired[str],
        "Tags": NotRequired[Dict[str, str]],
    },
)
DeleteResourcePermissionInputRequestTypeDef = TypedDict(
    "DeleteResourcePermissionInputRequestTypeDef",
    {
        "ResourceArn": str,
        "ActionType": NotRequired[Literal["RESTORE"]],
        "SourceResourceArn": NotRequired[str],
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
DeregisterApplicationInputRequestTypeDef = TypedDict(
    "DeregisterApplicationInputRequestTypeDef",
    {
        "ApplicationId": str,
    },
)
FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "Name": str,
        "Value": str,
        "Operator": FilterOperatorType,
    },
)
GetApplicationInputRequestTypeDef = TypedDict(
    "GetApplicationInputRequestTypeDef",
    {
        "ApplicationId": NotRequired[str],
        "ApplicationArn": NotRequired[str],
        "AppRegistryArn": NotRequired[str],
    },
)
GetComponentInputRequestTypeDef = TypedDict(
    "GetComponentInputRequestTypeDef",
    {
        "ApplicationId": str,
        "ComponentId": str,
    },
)
GetDatabaseInputRequestTypeDef = TypedDict(
    "GetDatabaseInputRequestTypeDef",
    {
        "ApplicationId": NotRequired[str],
        "ComponentId": NotRequired[str],
        "DatabaseId": NotRequired[str],
        "DatabaseArn": NotRequired[str],
    },
)
GetOperationInputRequestTypeDef = TypedDict(
    "GetOperationInputRequestTypeDef",
    {
        "OperationId": str,
    },
)
OperationTypeDef = TypedDict(
    "OperationTypeDef",
    {
        "Id": NotRequired[str],
        "Type": NotRequired[str],
        "Status": NotRequired[OperationStatusType],
        "StatusMessage": NotRequired[str],
        "Properties": NotRequired[Dict[str, str]],
        "ResourceType": NotRequired[str],
        "ResourceId": NotRequired[str],
        "ResourceArn": NotRequired[str],
        "StartTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
        "LastUpdatedTime": NotRequired[datetime],
    },
)
GetResourcePermissionInputRequestTypeDef = TypedDict(
    "GetResourcePermissionInputRequestTypeDef",
    {
        "ResourceArn": str,
        "ActionType": NotRequired[Literal["RESTORE"]],
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
ListComponentsInputRequestTypeDef = TypedDict(
    "ListComponentsInputRequestTypeDef",
    {
        "ApplicationId": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListDatabasesInputRequestTypeDef = TypedDict(
    "ListDatabasesInputRequestTypeDef",
    {
        "ApplicationId": NotRequired[str],
        "ComponentId": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)
PutResourcePermissionInputRequestTypeDef = TypedDict(
    "PutResourcePermissionInputRequestTypeDef",
    {
        "ActionType": Literal["RESTORE"],
        "SourceResourceArn": str,
        "ResourceArn": str,
    },
)
StartApplicationRefreshInputRequestTypeDef = TypedDict(
    "StartApplicationRefreshInputRequestTypeDef",
    {
        "ApplicationId": str,
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
DatabaseTypeDef = TypedDict(
    "DatabaseTypeDef",
    {
        "ApplicationId": NotRequired[str],
        "ComponentId": NotRequired[str],
        "Credentials": NotRequired[List[ApplicationCredentialTypeDef]],
        "DatabaseId": NotRequired[str],
        "DatabaseName": NotRequired[str],
        "DatabaseType": NotRequired[DatabaseTypeType],
        "Arn": NotRequired[str],
        "Status": NotRequired[DatabaseStatusType],
        "PrimaryHost": NotRequired[str],
        "SQLPort": NotRequired[int],
        "LastUpdated": NotRequired[datetime],
    },
)
RegisterApplicationInputRequestTypeDef = TypedDict(
    "RegisterApplicationInputRequestTypeDef",
    {
        "ApplicationId": str,
        "ApplicationType": ApplicationTypeType,
        "Instances": Sequence[str],
        "SapInstanceNumber": NotRequired[str],
        "Sid": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
        "Credentials": NotRequired[Sequence[ApplicationCredentialTypeDef]],
        "DatabaseArn": NotRequired[str],
    },
)
AssociatedHostTypeDef = TypedDict(
    "AssociatedHostTypeDef",
    {
        "Hostname": NotRequired[str],
        "Ec2InstanceId": NotRequired[str],
        "IpAddresses": NotRequired[List[IpAddressMemberTypeDef]],
        "OsVersion": NotRequired[str],
    },
)
UpdateApplicationSettingsInputRequestTypeDef = TypedDict(
    "UpdateApplicationSettingsInputRequestTypeDef",
    {
        "ApplicationId": str,
        "CredentialsToAddOrUpdate": NotRequired[Sequence[ApplicationCredentialTypeDef]],
        "CredentialsToRemove": NotRequired[Sequence[ApplicationCredentialTypeDef]],
        "Backint": NotRequired[BackintConfigTypeDef],
        "DatabaseArn": NotRequired[str],
    },
)
DeleteResourcePermissionOutputTypeDef = TypedDict(
    "DeleteResourcePermissionOutputTypeDef",
    {
        "Policy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetApplicationOutputTypeDef = TypedDict(
    "GetApplicationOutputTypeDef",
    {
        "Application": ApplicationTypeDef,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetResourcePermissionOutputTypeDef = TypedDict(
    "GetResourcePermissionOutputTypeDef",
    {
        "Policy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListApplicationsOutputTypeDef = TypedDict(
    "ListApplicationsOutputTypeDef",
    {
        "Applications": List[ApplicationSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListComponentsOutputTypeDef = TypedDict(
    "ListComponentsOutputTypeDef",
    {
        "Components": List[ComponentSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListDatabasesOutputTypeDef = TypedDict(
    "ListDatabasesOutputTypeDef",
    {
        "Databases": List[DatabaseSummaryTypeDef],
        "NextToken": str,
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
PutResourcePermissionOutputTypeDef = TypedDict(
    "PutResourcePermissionOutputTypeDef",
    {
        "Policy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RegisterApplicationOutputTypeDef = TypedDict(
    "RegisterApplicationOutputTypeDef",
    {
        "Application": ApplicationTypeDef,
        "OperationId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartApplicationRefreshOutputTypeDef = TypedDict(
    "StartApplicationRefreshOutputTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateApplicationSettingsOutputTypeDef = TypedDict(
    "UpdateApplicationSettingsOutputTypeDef",
    {
        "Message": str,
        "OperationIds": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListApplicationsInputRequestTypeDef = TypedDict(
    "ListApplicationsInputRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
    },
)
ListOperationsInputRequestTypeDef = TypedDict(
    "ListOperationsInputRequestTypeDef",
    {
        "ApplicationId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
    },
)
GetOperationOutputTypeDef = TypedDict(
    "GetOperationOutputTypeDef",
    {
        "Operation": OperationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListOperationsOutputTypeDef = TypedDict(
    "ListOperationsOutputTypeDef",
    {
        "Operations": List[OperationTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListApplicationsInputListApplicationsPaginateTypeDef = TypedDict(
    "ListApplicationsInputListApplicationsPaginateTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListComponentsInputListComponentsPaginateTypeDef = TypedDict(
    "ListComponentsInputListComponentsPaginateTypeDef",
    {
        "ApplicationId": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDatabasesInputListDatabasesPaginateTypeDef = TypedDict(
    "ListDatabasesInputListDatabasesPaginateTypeDef",
    {
        "ApplicationId": NotRequired[str],
        "ComponentId": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListOperationsInputListOperationsPaginateTypeDef = TypedDict(
    "ListOperationsInputListOperationsPaginateTypeDef",
    {
        "ApplicationId": str,
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetDatabaseOutputTypeDef = TypedDict(
    "GetDatabaseOutputTypeDef",
    {
        "Database": DatabaseTypeDef,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ComponentTypeDef = TypedDict(
    "ComponentTypeDef",
    {
        "ComponentId": NotRequired[str],
        "Sid": NotRequired[str],
        "SystemNumber": NotRequired[str],
        "ParentComponent": NotRequired[str],
        "ChildComponents": NotRequired[List[str]],
        "ApplicationId": NotRequired[str],
        "ComponentType": NotRequired[ComponentTypeType],
        "Status": NotRequired[ComponentStatusType],
        "SapHostname": NotRequired[str],
        "SapFeature": NotRequired[str],
        "SapKernelVersion": NotRequired[str],
        "HdbVersion": NotRequired[str],
        "Resilience": NotRequired[ResilienceTypeDef],
        "AssociatedHost": NotRequired[AssociatedHostTypeDef],
        "Databases": NotRequired[List[str]],
        "Hosts": NotRequired[List[HostTypeDef]],
        "PrimaryHost": NotRequired[str],
        "DatabaseConnection": NotRequired[DatabaseConnectionTypeDef],
        "LastUpdated": NotRequired[datetime],
        "Arn": NotRequired[str],
    },
)
GetComponentOutputTypeDef = TypedDict(
    "GetComponentOutputTypeDef",
    {
        "Component": ComponentTypeDef,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
