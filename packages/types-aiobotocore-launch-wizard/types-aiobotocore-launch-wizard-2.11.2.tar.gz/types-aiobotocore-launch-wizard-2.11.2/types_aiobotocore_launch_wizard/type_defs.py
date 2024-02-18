"""
Type annotations for launch-wizard service type definitions.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_launch_wizard/type_defs/)

Usage::

    ```python
    from types_aiobotocore_launch_wizard.type_defs import CreateDeploymentInputRequestTypeDef

    data: CreateDeploymentInputRequestTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from .literals import (
    DeploymentFilterKeyType,
    DeploymentStatusType,
    EventStatusType,
    WorkloadDeploymentPatternStatusType,
    WorkloadStatusType,
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
    "CreateDeploymentInputRequestTypeDef",
    "ResponseMetadataTypeDef",
    "DeleteDeploymentInputRequestTypeDef",
    "DeploymentDataSummaryTypeDef",
    "DeploymentDataTypeDef",
    "DeploymentEventDataSummaryTypeDef",
    "DeploymentFilterTypeDef",
    "GetDeploymentInputRequestTypeDef",
    "GetWorkloadInputRequestTypeDef",
    "WorkloadDataTypeDef",
    "PaginatorConfigTypeDef",
    "ListDeploymentEventsInputRequestTypeDef",
    "ListWorkloadDeploymentPatternsInputRequestTypeDef",
    "WorkloadDeploymentPatternDataSummaryTypeDef",
    "ListWorkloadsInputRequestTypeDef",
    "WorkloadDataSummaryTypeDef",
    "CreateDeploymentOutputTypeDef",
    "DeleteDeploymentOutputTypeDef",
    "ListDeploymentsOutputTypeDef",
    "GetDeploymentOutputTypeDef",
    "ListDeploymentEventsOutputTypeDef",
    "ListDeploymentsInputRequestTypeDef",
    "GetWorkloadOutputTypeDef",
    "ListDeploymentEventsInputListDeploymentEventsPaginateTypeDef",
    "ListDeploymentsInputListDeploymentsPaginateTypeDef",
    "ListWorkloadDeploymentPatternsInputListWorkloadDeploymentPatternsPaginateTypeDef",
    "ListWorkloadsInputListWorkloadsPaginateTypeDef",
    "ListWorkloadDeploymentPatternsOutputTypeDef",
    "ListWorkloadsOutputTypeDef",
)

CreateDeploymentInputRequestTypeDef = TypedDict(
    "CreateDeploymentInputRequestTypeDef",
    {
        "deploymentPatternName": str,
        "name": str,
        "specifications": Mapping[str, str],
        "workloadName": str,
        "dryRun": NotRequired[bool],
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
DeleteDeploymentInputRequestTypeDef = TypedDict(
    "DeleteDeploymentInputRequestTypeDef",
    {
        "deploymentId": str,
    },
)
DeploymentDataSummaryTypeDef = TypedDict(
    "DeploymentDataSummaryTypeDef",
    {
        "createdAt": NotRequired[datetime],
        "id": NotRequired[str],
        "name": NotRequired[str],
        "patternName": NotRequired[str],
        "status": NotRequired[DeploymentStatusType],
        "workloadName": NotRequired[str],
    },
)
DeploymentDataTypeDef = TypedDict(
    "DeploymentDataTypeDef",
    {
        "createdAt": NotRequired[datetime],
        "deletedAt": NotRequired[datetime],
        "id": NotRequired[str],
        "name": NotRequired[str],
        "patternName": NotRequired[str],
        "resourceGroup": NotRequired[str],
        "specifications": NotRequired[Dict[str, str]],
        "status": NotRequired[DeploymentStatusType],
        "workloadName": NotRequired[str],
    },
)
DeploymentEventDataSummaryTypeDef = TypedDict(
    "DeploymentEventDataSummaryTypeDef",
    {
        "description": NotRequired[str],
        "name": NotRequired[str],
        "status": NotRequired[EventStatusType],
        "statusReason": NotRequired[str],
        "timestamp": NotRequired[datetime],
    },
)
DeploymentFilterTypeDef = TypedDict(
    "DeploymentFilterTypeDef",
    {
        "name": NotRequired[DeploymentFilterKeyType],
        "values": NotRequired[Sequence[str]],
    },
)
GetDeploymentInputRequestTypeDef = TypedDict(
    "GetDeploymentInputRequestTypeDef",
    {
        "deploymentId": str,
    },
)
GetWorkloadInputRequestTypeDef = TypedDict(
    "GetWorkloadInputRequestTypeDef",
    {
        "workloadName": str,
    },
)
WorkloadDataTypeDef = TypedDict(
    "WorkloadDataTypeDef",
    {
        "description": NotRequired[str],
        "displayName": NotRequired[str],
        "documentationUrl": NotRequired[str],
        "iconUrl": NotRequired[str],
        "status": NotRequired[WorkloadStatusType],
        "statusMessage": NotRequired[str],
        "workloadName": NotRequired[str],
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
ListDeploymentEventsInputRequestTypeDef = TypedDict(
    "ListDeploymentEventsInputRequestTypeDef",
    {
        "deploymentId": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListWorkloadDeploymentPatternsInputRequestTypeDef = TypedDict(
    "ListWorkloadDeploymentPatternsInputRequestTypeDef",
    {
        "workloadName": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
WorkloadDeploymentPatternDataSummaryTypeDef = TypedDict(
    "WorkloadDeploymentPatternDataSummaryTypeDef",
    {
        "deploymentPatternName": NotRequired[str],
        "description": NotRequired[str],
        "displayName": NotRequired[str],
        "status": NotRequired[WorkloadDeploymentPatternStatusType],
        "statusMessage": NotRequired[str],
        "workloadName": NotRequired[str],
        "workloadVersionName": NotRequired[str],
    },
)
ListWorkloadsInputRequestTypeDef = TypedDict(
    "ListWorkloadsInputRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
WorkloadDataSummaryTypeDef = TypedDict(
    "WorkloadDataSummaryTypeDef",
    {
        "displayName": NotRequired[str],
        "workloadName": NotRequired[str],
    },
)
CreateDeploymentOutputTypeDef = TypedDict(
    "CreateDeploymentOutputTypeDef",
    {
        "deploymentId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteDeploymentOutputTypeDef = TypedDict(
    "DeleteDeploymentOutputTypeDef",
    {
        "status": DeploymentStatusType,
        "statusReason": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListDeploymentsOutputTypeDef = TypedDict(
    "ListDeploymentsOutputTypeDef",
    {
        "deployments": List[DeploymentDataSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetDeploymentOutputTypeDef = TypedDict(
    "GetDeploymentOutputTypeDef",
    {
        "deployment": DeploymentDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListDeploymentEventsOutputTypeDef = TypedDict(
    "ListDeploymentEventsOutputTypeDef",
    {
        "deploymentEvents": List[DeploymentEventDataSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListDeploymentsInputRequestTypeDef = TypedDict(
    "ListDeploymentsInputRequestTypeDef",
    {
        "filters": NotRequired[Sequence[DeploymentFilterTypeDef]],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
GetWorkloadOutputTypeDef = TypedDict(
    "GetWorkloadOutputTypeDef",
    {
        "workload": WorkloadDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListDeploymentEventsInputListDeploymentEventsPaginateTypeDef = TypedDict(
    "ListDeploymentEventsInputListDeploymentEventsPaginateTypeDef",
    {
        "deploymentId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDeploymentsInputListDeploymentsPaginateTypeDef = TypedDict(
    "ListDeploymentsInputListDeploymentsPaginateTypeDef",
    {
        "filters": NotRequired[Sequence[DeploymentFilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListWorkloadDeploymentPatternsInputListWorkloadDeploymentPatternsPaginateTypeDef = TypedDict(
    "ListWorkloadDeploymentPatternsInputListWorkloadDeploymentPatternsPaginateTypeDef",
    {
        "workloadName": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListWorkloadsInputListWorkloadsPaginateTypeDef = TypedDict(
    "ListWorkloadsInputListWorkloadsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListWorkloadDeploymentPatternsOutputTypeDef = TypedDict(
    "ListWorkloadDeploymentPatternsOutputTypeDef",
    {
        "nextToken": str,
        "workloadDeploymentPatterns": List[WorkloadDeploymentPatternDataSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListWorkloadsOutputTypeDef = TypedDict(
    "ListWorkloadsOutputTypeDef",
    {
        "nextToken": str,
        "workloads": List[WorkloadDataSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
