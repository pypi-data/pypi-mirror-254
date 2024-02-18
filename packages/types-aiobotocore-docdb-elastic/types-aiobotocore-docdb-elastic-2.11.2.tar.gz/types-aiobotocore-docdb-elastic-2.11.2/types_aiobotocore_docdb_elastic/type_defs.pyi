"""
Type annotations for docdb-elastic service type definitions.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_docdb_elastic/type_defs/)

Usage::

    ```python
    from types_aiobotocore_docdb_elastic.type_defs import ClusterInListTypeDef

    data: ClusterInListTypeDef = ...
    ```
"""

import sys
from typing import Dict, List, Mapping, Sequence

from .literals import AuthType, StatusType

if sys.version_info >= (3, 12):
    from typing import NotRequired
else:
    from typing_extensions import NotRequired
if sys.version_info >= (3, 12):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "ClusterInListTypeDef",
    "ClusterSnapshotInListTypeDef",
    "ClusterSnapshotTypeDef",
    "ClusterTypeDef",
    "CreateClusterInputRequestTypeDef",
    "ResponseMetadataTypeDef",
    "CreateClusterSnapshotInputRequestTypeDef",
    "DeleteClusterInputRequestTypeDef",
    "DeleteClusterSnapshotInputRequestTypeDef",
    "GetClusterInputRequestTypeDef",
    "GetClusterSnapshotInputRequestTypeDef",
    "PaginatorConfigTypeDef",
    "ListClusterSnapshotsInputRequestTypeDef",
    "ListClustersInputRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "RestoreClusterFromSnapshotInputRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateClusterInputRequestTypeDef",
    "CreateClusterOutputTypeDef",
    "CreateClusterSnapshotOutputTypeDef",
    "DeleteClusterOutputTypeDef",
    "DeleteClusterSnapshotOutputTypeDef",
    "GetClusterOutputTypeDef",
    "GetClusterSnapshotOutputTypeDef",
    "ListClusterSnapshotsOutputTypeDef",
    "ListClustersOutputTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "RestoreClusterFromSnapshotOutputTypeDef",
    "UpdateClusterOutputTypeDef",
    "ListClusterSnapshotsInputListClusterSnapshotsPaginateTypeDef",
    "ListClustersInputListClustersPaginateTypeDef",
)

ClusterInListTypeDef = TypedDict(
    "ClusterInListTypeDef",
    {
        "clusterArn": str,
        "clusterName": str,
        "status": StatusType,
    },
)
ClusterSnapshotInListTypeDef = TypedDict(
    "ClusterSnapshotInListTypeDef",
    {
        "clusterArn": str,
        "snapshotArn": str,
        "snapshotCreationTime": str,
        "snapshotName": str,
        "status": StatusType,
    },
)
ClusterSnapshotTypeDef = TypedDict(
    "ClusterSnapshotTypeDef",
    {
        "adminUserName": str,
        "clusterArn": str,
        "clusterCreationTime": str,
        "kmsKeyId": str,
        "snapshotArn": str,
        "snapshotCreationTime": str,
        "snapshotName": str,
        "status": StatusType,
        "subnetIds": List[str],
        "vpcSecurityGroupIds": List[str],
    },
)
ClusterTypeDef = TypedDict(
    "ClusterTypeDef",
    {
        "adminUserName": str,
        "authType": AuthType,
        "clusterArn": str,
        "clusterEndpoint": str,
        "clusterName": str,
        "createTime": str,
        "kmsKeyId": str,
        "preferredMaintenanceWindow": str,
        "shardCapacity": int,
        "shardCount": int,
        "status": StatusType,
        "subnetIds": List[str],
        "vpcSecurityGroupIds": List[str],
    },
)
CreateClusterInputRequestTypeDef = TypedDict(
    "CreateClusterInputRequestTypeDef",
    {
        "adminUserName": str,
        "adminUserPassword": str,
        "authType": AuthType,
        "clusterName": str,
        "shardCapacity": int,
        "shardCount": int,
        "clientToken": NotRequired[str],
        "kmsKeyId": NotRequired[str],
        "preferredMaintenanceWindow": NotRequired[str],
        "subnetIds": NotRequired[Sequence[str]],
        "tags": NotRequired[Mapping[str, str]],
        "vpcSecurityGroupIds": NotRequired[Sequence[str]],
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
CreateClusterSnapshotInputRequestTypeDef = TypedDict(
    "CreateClusterSnapshotInputRequestTypeDef",
    {
        "clusterArn": str,
        "snapshotName": str,
        "tags": NotRequired[Mapping[str, str]],
    },
)
DeleteClusterInputRequestTypeDef = TypedDict(
    "DeleteClusterInputRequestTypeDef",
    {
        "clusterArn": str,
    },
)
DeleteClusterSnapshotInputRequestTypeDef = TypedDict(
    "DeleteClusterSnapshotInputRequestTypeDef",
    {
        "snapshotArn": str,
    },
)
GetClusterInputRequestTypeDef = TypedDict(
    "GetClusterInputRequestTypeDef",
    {
        "clusterArn": str,
    },
)
GetClusterSnapshotInputRequestTypeDef = TypedDict(
    "GetClusterSnapshotInputRequestTypeDef",
    {
        "snapshotArn": str,
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
ListClusterSnapshotsInputRequestTypeDef = TypedDict(
    "ListClusterSnapshotsInputRequestTypeDef",
    {
        "clusterArn": NotRequired[str],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListClustersInputRequestTypeDef = TypedDict(
    "ListClustersInputRequestTypeDef",
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
RestoreClusterFromSnapshotInputRequestTypeDef = TypedDict(
    "RestoreClusterFromSnapshotInputRequestTypeDef",
    {
        "clusterName": str,
        "snapshotArn": str,
        "kmsKeyId": NotRequired[str],
        "subnetIds": NotRequired[Sequence[str]],
        "tags": NotRequired[Mapping[str, str]],
        "vpcSecurityGroupIds": NotRequired[Sequence[str]],
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
UpdateClusterInputRequestTypeDef = TypedDict(
    "UpdateClusterInputRequestTypeDef",
    {
        "clusterArn": str,
        "adminUserPassword": NotRequired[str],
        "authType": NotRequired[AuthType],
        "clientToken": NotRequired[str],
        "preferredMaintenanceWindow": NotRequired[str],
        "shardCapacity": NotRequired[int],
        "shardCount": NotRequired[int],
        "subnetIds": NotRequired[Sequence[str]],
        "vpcSecurityGroupIds": NotRequired[Sequence[str]],
    },
)
CreateClusterOutputTypeDef = TypedDict(
    "CreateClusterOutputTypeDef",
    {
        "cluster": ClusterTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateClusterSnapshotOutputTypeDef = TypedDict(
    "CreateClusterSnapshotOutputTypeDef",
    {
        "snapshot": ClusterSnapshotTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteClusterOutputTypeDef = TypedDict(
    "DeleteClusterOutputTypeDef",
    {
        "cluster": ClusterTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteClusterSnapshotOutputTypeDef = TypedDict(
    "DeleteClusterSnapshotOutputTypeDef",
    {
        "snapshot": ClusterSnapshotTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetClusterOutputTypeDef = TypedDict(
    "GetClusterOutputTypeDef",
    {
        "cluster": ClusterTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetClusterSnapshotOutputTypeDef = TypedDict(
    "GetClusterSnapshotOutputTypeDef",
    {
        "snapshot": ClusterSnapshotTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListClusterSnapshotsOutputTypeDef = TypedDict(
    "ListClusterSnapshotsOutputTypeDef",
    {
        "nextToken": str,
        "snapshots": List[ClusterSnapshotInListTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListClustersOutputTypeDef = TypedDict(
    "ListClustersOutputTypeDef",
    {
        "clusters": List[ClusterInListTypeDef],
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
RestoreClusterFromSnapshotOutputTypeDef = TypedDict(
    "RestoreClusterFromSnapshotOutputTypeDef",
    {
        "cluster": ClusterTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateClusterOutputTypeDef = TypedDict(
    "UpdateClusterOutputTypeDef",
    {
        "cluster": ClusterTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListClusterSnapshotsInputListClusterSnapshotsPaginateTypeDef = TypedDict(
    "ListClusterSnapshotsInputListClusterSnapshotsPaginateTypeDef",
    {
        "clusterArn": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListClustersInputListClustersPaginateTypeDef = TypedDict(
    "ListClustersInputListClustersPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
