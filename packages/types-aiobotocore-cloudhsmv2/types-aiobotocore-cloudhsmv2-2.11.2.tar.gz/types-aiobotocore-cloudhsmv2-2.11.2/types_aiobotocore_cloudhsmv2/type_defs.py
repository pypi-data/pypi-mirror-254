"""
Type annotations for cloudhsmv2 service type definitions.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudhsmv2/type_defs/)

Usage::

    ```python
    from types_aiobotocore_cloudhsmv2.type_defs import BackupRetentionPolicyTypeDef

    data: BackupRetentionPolicyTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from .literals import BackupStateType, ClusterStateType, HsmStateType

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
    "BackupRetentionPolicyTypeDef",
    "TagTypeDef",
    "CertificatesTypeDef",
    "HsmTypeDef",
    "DestinationBackupTypeDef",
    "ResponseMetadataTypeDef",
    "CreateHsmRequestRequestTypeDef",
    "DeleteBackupRequestRequestTypeDef",
    "DeleteClusterRequestRequestTypeDef",
    "DeleteHsmRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "DescribeBackupsRequestRequestTypeDef",
    "DescribeClustersRequestRequestTypeDef",
    "InitializeClusterRequestRequestTypeDef",
    "ListTagsRequestRequestTypeDef",
    "ModifyBackupAttributesRequestRequestTypeDef",
    "RestoreBackupRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "ModifyClusterRequestRequestTypeDef",
    "BackupTypeDef",
    "CopyBackupToRegionRequestRequestTypeDef",
    "CreateClusterRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "ClusterTypeDef",
    "CopyBackupToRegionResponseTypeDef",
    "CreateHsmResponseTypeDef",
    "DeleteHsmResponseTypeDef",
    "InitializeClusterResponseTypeDef",
    "ListTagsResponseTypeDef",
    "DescribeBackupsRequestDescribeBackupsPaginateTypeDef",
    "DescribeClustersRequestDescribeClustersPaginateTypeDef",
    "ListTagsRequestListTagsPaginateTypeDef",
    "DeleteBackupResponseTypeDef",
    "DescribeBackupsResponseTypeDef",
    "ModifyBackupAttributesResponseTypeDef",
    "RestoreBackupResponseTypeDef",
    "CreateClusterResponseTypeDef",
    "DeleteClusterResponseTypeDef",
    "DescribeClustersResponseTypeDef",
    "ModifyClusterResponseTypeDef",
)

BackupRetentionPolicyTypeDef = TypedDict(
    "BackupRetentionPolicyTypeDef",
    {
        "Type": NotRequired[Literal["DAYS"]],
        "Value": NotRequired[str],
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)
CertificatesTypeDef = TypedDict(
    "CertificatesTypeDef",
    {
        "ClusterCsr": NotRequired[str],
        "HsmCertificate": NotRequired[str],
        "AwsHardwareCertificate": NotRequired[str],
        "ManufacturerHardwareCertificate": NotRequired[str],
        "ClusterCertificate": NotRequired[str],
    },
)
HsmTypeDef = TypedDict(
    "HsmTypeDef",
    {
        "HsmId": str,
        "AvailabilityZone": NotRequired[str],
        "ClusterId": NotRequired[str],
        "SubnetId": NotRequired[str],
        "EniId": NotRequired[str],
        "EniIp": NotRequired[str],
        "State": NotRequired[HsmStateType],
        "StateMessage": NotRequired[str],
    },
)
DestinationBackupTypeDef = TypedDict(
    "DestinationBackupTypeDef",
    {
        "CreateTimestamp": NotRequired[datetime],
        "SourceRegion": NotRequired[str],
        "SourceBackup": NotRequired[str],
        "SourceCluster": NotRequired[str],
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
CreateHsmRequestRequestTypeDef = TypedDict(
    "CreateHsmRequestRequestTypeDef",
    {
        "ClusterId": str,
        "AvailabilityZone": str,
        "IpAddress": NotRequired[str],
    },
)
DeleteBackupRequestRequestTypeDef = TypedDict(
    "DeleteBackupRequestRequestTypeDef",
    {
        "BackupId": str,
    },
)
DeleteClusterRequestRequestTypeDef = TypedDict(
    "DeleteClusterRequestRequestTypeDef",
    {
        "ClusterId": str,
    },
)
DeleteHsmRequestRequestTypeDef = TypedDict(
    "DeleteHsmRequestRequestTypeDef",
    {
        "ClusterId": str,
        "HsmId": NotRequired[str],
        "EniId": NotRequired[str],
        "EniIp": NotRequired[str],
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
DescribeBackupsRequestRequestTypeDef = TypedDict(
    "DescribeBackupsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "Filters": NotRequired[Mapping[str, Sequence[str]]],
        "SortAscending": NotRequired[bool],
    },
)
DescribeClustersRequestRequestTypeDef = TypedDict(
    "DescribeClustersRequestRequestTypeDef",
    {
        "Filters": NotRequired[Mapping[str, Sequence[str]]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
InitializeClusterRequestRequestTypeDef = TypedDict(
    "InitializeClusterRequestRequestTypeDef",
    {
        "ClusterId": str,
        "SignedCert": str,
        "TrustAnchor": str,
    },
)
ListTagsRequestRequestTypeDef = TypedDict(
    "ListTagsRequestRequestTypeDef",
    {
        "ResourceId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ModifyBackupAttributesRequestRequestTypeDef = TypedDict(
    "ModifyBackupAttributesRequestRequestTypeDef",
    {
        "BackupId": str,
        "NeverExpires": bool,
    },
)
RestoreBackupRequestRequestTypeDef = TypedDict(
    "RestoreBackupRequestRequestTypeDef",
    {
        "BackupId": str,
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceId": str,
        "TagKeyList": Sequence[str],
    },
)
ModifyClusterRequestRequestTypeDef = TypedDict(
    "ModifyClusterRequestRequestTypeDef",
    {
        "BackupRetentionPolicy": BackupRetentionPolicyTypeDef,
        "ClusterId": str,
    },
)
BackupTypeDef = TypedDict(
    "BackupTypeDef",
    {
        "BackupId": str,
        "BackupState": NotRequired[BackupStateType],
        "ClusterId": NotRequired[str],
        "CreateTimestamp": NotRequired[datetime],
        "CopyTimestamp": NotRequired[datetime],
        "NeverExpires": NotRequired[bool],
        "SourceRegion": NotRequired[str],
        "SourceBackup": NotRequired[str],
        "SourceCluster": NotRequired[str],
        "DeleteTimestamp": NotRequired[datetime],
        "TagList": NotRequired[List[TagTypeDef]],
    },
)
CopyBackupToRegionRequestRequestTypeDef = TypedDict(
    "CopyBackupToRegionRequestRequestTypeDef",
    {
        "DestinationRegion": str,
        "BackupId": str,
        "TagList": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateClusterRequestRequestTypeDef = TypedDict(
    "CreateClusterRequestRequestTypeDef",
    {
        "HsmType": str,
        "SubnetIds": Sequence[str],
        "BackupRetentionPolicy": NotRequired[BackupRetentionPolicyTypeDef],
        "SourceBackupId": NotRequired[str],
        "TagList": NotRequired[Sequence[TagTypeDef]],
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceId": str,
        "TagList": Sequence[TagTypeDef],
    },
)
ClusterTypeDef = TypedDict(
    "ClusterTypeDef",
    {
        "BackupPolicy": NotRequired[Literal["DEFAULT"]],
        "BackupRetentionPolicy": NotRequired[BackupRetentionPolicyTypeDef],
        "ClusterId": NotRequired[str],
        "CreateTimestamp": NotRequired[datetime],
        "Hsms": NotRequired[List[HsmTypeDef]],
        "HsmType": NotRequired[str],
        "PreCoPassword": NotRequired[str],
        "SecurityGroup": NotRequired[str],
        "SourceBackupId": NotRequired[str],
        "State": NotRequired[ClusterStateType],
        "StateMessage": NotRequired[str],
        "SubnetMapping": NotRequired[Dict[str, str]],
        "VpcId": NotRequired[str],
        "Certificates": NotRequired[CertificatesTypeDef],
        "TagList": NotRequired[List[TagTypeDef]],
    },
)
CopyBackupToRegionResponseTypeDef = TypedDict(
    "CopyBackupToRegionResponseTypeDef",
    {
        "DestinationBackup": DestinationBackupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateHsmResponseTypeDef = TypedDict(
    "CreateHsmResponseTypeDef",
    {
        "Hsm": HsmTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteHsmResponseTypeDef = TypedDict(
    "DeleteHsmResponseTypeDef",
    {
        "HsmId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
InitializeClusterResponseTypeDef = TypedDict(
    "InitializeClusterResponseTypeDef",
    {
        "State": ClusterStateType,
        "StateMessage": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTagsResponseTypeDef = TypedDict(
    "ListTagsResponseTypeDef",
    {
        "TagList": List[TagTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeBackupsRequestDescribeBackupsPaginateTypeDef = TypedDict(
    "DescribeBackupsRequestDescribeBackupsPaginateTypeDef",
    {
        "Filters": NotRequired[Mapping[str, Sequence[str]]],
        "SortAscending": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeClustersRequestDescribeClustersPaginateTypeDef = TypedDict(
    "DescribeClustersRequestDescribeClustersPaginateTypeDef",
    {
        "Filters": NotRequired[Mapping[str, Sequence[str]]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListTagsRequestListTagsPaginateTypeDef = TypedDict(
    "ListTagsRequestListTagsPaginateTypeDef",
    {
        "ResourceId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DeleteBackupResponseTypeDef = TypedDict(
    "DeleteBackupResponseTypeDef",
    {
        "Backup": BackupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeBackupsResponseTypeDef = TypedDict(
    "DescribeBackupsResponseTypeDef",
    {
        "Backups": List[BackupTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyBackupAttributesResponseTypeDef = TypedDict(
    "ModifyBackupAttributesResponseTypeDef",
    {
        "Backup": BackupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RestoreBackupResponseTypeDef = TypedDict(
    "RestoreBackupResponseTypeDef",
    {
        "Backup": BackupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateClusterResponseTypeDef = TypedDict(
    "CreateClusterResponseTypeDef",
    {
        "Cluster": ClusterTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteClusterResponseTypeDef = TypedDict(
    "DeleteClusterResponseTypeDef",
    {
        "Cluster": ClusterTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeClustersResponseTypeDef = TypedDict(
    "DescribeClustersResponseTypeDef",
    {
        "Clusters": List[ClusterTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyClusterResponseTypeDef = TypedDict(
    "ModifyClusterResponseTypeDef",
    {
        "Cluster": ClusterTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
