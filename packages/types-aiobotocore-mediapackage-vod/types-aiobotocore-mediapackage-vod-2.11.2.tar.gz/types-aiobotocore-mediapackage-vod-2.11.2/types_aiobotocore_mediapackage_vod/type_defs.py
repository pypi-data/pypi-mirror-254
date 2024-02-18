"""
Type annotations for mediapackage-vod service type definitions.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediapackage_vod/type_defs/)

Usage::

    ```python
    from types_aiobotocore_mediapackage_vod.type_defs import AssetShallowTypeDef

    data: AssetShallowTypeDef = ...
    ```
"""

import sys
from typing import Dict, List, Mapping, Sequence

from .literals import (
    AdMarkersType,
    EncryptionMethodType,
    ManifestLayoutType,
    PresetSpeke20AudioType,
    PresetSpeke20VideoType,
    ProfileType,
    ScteMarkersSourceType,
    SegmentTemplateFormatType,
    StreamOrderType,
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
    "AssetShallowTypeDef",
    "AuthorizationTypeDef",
    "EgressAccessLogsTypeDef",
    "ResponseMetadataTypeDef",
    "CreateAssetRequestRequestTypeDef",
    "EgressEndpointTypeDef",
    "StreamSelectionTypeDef",
    "DeleteAssetRequestRequestTypeDef",
    "DeletePackagingConfigurationRequestRequestTypeDef",
    "DeletePackagingGroupRequestRequestTypeDef",
    "DescribeAssetRequestRequestTypeDef",
    "DescribePackagingConfigurationRequestRequestTypeDef",
    "DescribePackagingGroupRequestRequestTypeDef",
    "EncryptionContractConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "ListAssetsRequestRequestTypeDef",
    "ListPackagingConfigurationsRequestRequestTypeDef",
    "ListPackagingGroupsRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdatePackagingGroupRequestRequestTypeDef",
    "ConfigureLogsRequestRequestTypeDef",
    "CreatePackagingGroupRequestRequestTypeDef",
    "PackagingGroupTypeDef",
    "ConfigureLogsResponseTypeDef",
    "CreatePackagingGroupResponseTypeDef",
    "DescribePackagingGroupResponseTypeDef",
    "EmptyResponseMetadataTypeDef",
    "ListAssetsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "UpdatePackagingGroupResponseTypeDef",
    "CreateAssetResponseTypeDef",
    "DescribeAssetResponseTypeDef",
    "DashManifestTypeDef",
    "HlsManifestTypeDef",
    "MssManifestTypeDef",
    "SpekeKeyProviderPaginatorTypeDef",
    "SpekeKeyProviderTypeDef",
    "ListAssetsRequestListAssetsPaginateTypeDef",
    "ListPackagingConfigurationsRequestListPackagingConfigurationsPaginateTypeDef",
    "ListPackagingGroupsRequestListPackagingGroupsPaginateTypeDef",
    "ListPackagingGroupsResponseTypeDef",
    "CmafEncryptionPaginatorTypeDef",
    "DashEncryptionPaginatorTypeDef",
    "HlsEncryptionPaginatorTypeDef",
    "MssEncryptionPaginatorTypeDef",
    "CmafEncryptionTypeDef",
    "DashEncryptionTypeDef",
    "HlsEncryptionTypeDef",
    "MssEncryptionTypeDef",
    "CmafPackagePaginatorTypeDef",
    "DashPackagePaginatorTypeDef",
    "HlsPackagePaginatorTypeDef",
    "MssPackagePaginatorTypeDef",
    "CmafPackageTypeDef",
    "DashPackageTypeDef",
    "HlsPackageTypeDef",
    "MssPackageTypeDef",
    "PackagingConfigurationPaginatorTypeDef",
    "CreatePackagingConfigurationRequestRequestTypeDef",
    "CreatePackagingConfigurationResponseTypeDef",
    "DescribePackagingConfigurationResponseTypeDef",
    "PackagingConfigurationTypeDef",
    "ListPackagingConfigurationsResponsePaginatorTypeDef",
    "ListPackagingConfigurationsResponseTypeDef",
)

AssetShallowTypeDef = TypedDict(
    "AssetShallowTypeDef",
    {
        "Arn": NotRequired[str],
        "CreatedAt": NotRequired[str],
        "Id": NotRequired[str],
        "PackagingGroupId": NotRequired[str],
        "ResourceId": NotRequired[str],
        "SourceArn": NotRequired[str],
        "SourceRoleArn": NotRequired[str],
        "Tags": NotRequired[Dict[str, str]],
    },
)
AuthorizationTypeDef = TypedDict(
    "AuthorizationTypeDef",
    {
        "CdnIdentifierSecret": str,
        "SecretsRoleArn": str,
    },
)
EgressAccessLogsTypeDef = TypedDict(
    "EgressAccessLogsTypeDef",
    {
        "LogGroupName": NotRequired[str],
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
CreateAssetRequestRequestTypeDef = TypedDict(
    "CreateAssetRequestRequestTypeDef",
    {
        "Id": str,
        "PackagingGroupId": str,
        "SourceArn": str,
        "SourceRoleArn": str,
        "ResourceId": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
EgressEndpointTypeDef = TypedDict(
    "EgressEndpointTypeDef",
    {
        "PackagingConfigurationId": NotRequired[str],
        "Status": NotRequired[str],
        "Url": NotRequired[str],
    },
)
StreamSelectionTypeDef = TypedDict(
    "StreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": NotRequired[int],
        "MinVideoBitsPerSecond": NotRequired[int],
        "StreamOrder": NotRequired[StreamOrderType],
    },
)
DeleteAssetRequestRequestTypeDef = TypedDict(
    "DeleteAssetRequestRequestTypeDef",
    {
        "Id": str,
    },
)
DeletePackagingConfigurationRequestRequestTypeDef = TypedDict(
    "DeletePackagingConfigurationRequestRequestTypeDef",
    {
        "Id": str,
    },
)
DeletePackagingGroupRequestRequestTypeDef = TypedDict(
    "DeletePackagingGroupRequestRequestTypeDef",
    {
        "Id": str,
    },
)
DescribeAssetRequestRequestTypeDef = TypedDict(
    "DescribeAssetRequestRequestTypeDef",
    {
        "Id": str,
    },
)
DescribePackagingConfigurationRequestRequestTypeDef = TypedDict(
    "DescribePackagingConfigurationRequestRequestTypeDef",
    {
        "Id": str,
    },
)
DescribePackagingGroupRequestRequestTypeDef = TypedDict(
    "DescribePackagingGroupRequestRequestTypeDef",
    {
        "Id": str,
    },
)
EncryptionContractConfigurationTypeDef = TypedDict(
    "EncryptionContractConfigurationTypeDef",
    {
        "PresetSpeke20Audio": PresetSpeke20AudioType,
        "PresetSpeke20Video": PresetSpeke20VideoType,
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
ListAssetsRequestRequestTypeDef = TypedDict(
    "ListAssetsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "PackagingGroupId": NotRequired[str],
    },
)
ListPackagingConfigurationsRequestRequestTypeDef = TypedDict(
    "ListPackagingConfigurationsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "PackagingGroupId": NotRequired[str],
    },
)
ListPackagingGroupsRequestRequestTypeDef = TypedDict(
    "ListPackagingGroupsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Mapping[str, str],
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)
UpdatePackagingGroupRequestRequestTypeDef = TypedDict(
    "UpdatePackagingGroupRequestRequestTypeDef",
    {
        "Id": str,
        "Authorization": NotRequired[AuthorizationTypeDef],
    },
)
ConfigureLogsRequestRequestTypeDef = TypedDict(
    "ConfigureLogsRequestRequestTypeDef",
    {
        "Id": str,
        "EgressAccessLogs": NotRequired[EgressAccessLogsTypeDef],
    },
)
CreatePackagingGroupRequestRequestTypeDef = TypedDict(
    "CreatePackagingGroupRequestRequestTypeDef",
    {
        "Id": str,
        "Authorization": NotRequired[AuthorizationTypeDef],
        "EgressAccessLogs": NotRequired[EgressAccessLogsTypeDef],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
PackagingGroupTypeDef = TypedDict(
    "PackagingGroupTypeDef",
    {
        "ApproximateAssetCount": NotRequired[int],
        "Arn": NotRequired[str],
        "Authorization": NotRequired[AuthorizationTypeDef],
        "CreatedAt": NotRequired[str],
        "DomainName": NotRequired[str],
        "EgressAccessLogs": NotRequired[EgressAccessLogsTypeDef],
        "Id": NotRequired[str],
        "Tags": NotRequired[Dict[str, str]],
    },
)
ConfigureLogsResponseTypeDef = TypedDict(
    "ConfigureLogsResponseTypeDef",
    {
        "Arn": str,
        "Authorization": AuthorizationTypeDef,
        "CreatedAt": str,
        "DomainName": str,
        "EgressAccessLogs": EgressAccessLogsTypeDef,
        "Id": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreatePackagingGroupResponseTypeDef = TypedDict(
    "CreatePackagingGroupResponseTypeDef",
    {
        "Arn": str,
        "Authorization": AuthorizationTypeDef,
        "CreatedAt": str,
        "DomainName": str,
        "EgressAccessLogs": EgressAccessLogsTypeDef,
        "Id": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribePackagingGroupResponseTypeDef = TypedDict(
    "DescribePackagingGroupResponseTypeDef",
    {
        "ApproximateAssetCount": int,
        "Arn": str,
        "Authorization": AuthorizationTypeDef,
        "CreatedAt": str,
        "DomainName": str,
        "EgressAccessLogs": EgressAccessLogsTypeDef,
        "Id": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAssetsResponseTypeDef = TypedDict(
    "ListAssetsResponseTypeDef",
    {
        "Assets": List[AssetShallowTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdatePackagingGroupResponseTypeDef = TypedDict(
    "UpdatePackagingGroupResponseTypeDef",
    {
        "ApproximateAssetCount": int,
        "Arn": str,
        "Authorization": AuthorizationTypeDef,
        "CreatedAt": str,
        "DomainName": str,
        "EgressAccessLogs": EgressAccessLogsTypeDef,
        "Id": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateAssetResponseTypeDef = TypedDict(
    "CreateAssetResponseTypeDef",
    {
        "Arn": str,
        "CreatedAt": str,
        "EgressEndpoints": List[EgressEndpointTypeDef],
        "Id": str,
        "PackagingGroupId": str,
        "ResourceId": str,
        "SourceArn": str,
        "SourceRoleArn": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeAssetResponseTypeDef = TypedDict(
    "DescribeAssetResponseTypeDef",
    {
        "Arn": str,
        "CreatedAt": str,
        "EgressEndpoints": List[EgressEndpointTypeDef],
        "Id": str,
        "PackagingGroupId": str,
        "ResourceId": str,
        "SourceArn": str,
        "SourceRoleArn": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DashManifestTypeDef = TypedDict(
    "DashManifestTypeDef",
    {
        "ManifestLayout": NotRequired[ManifestLayoutType],
        "ManifestName": NotRequired[str],
        "MinBufferTimeSeconds": NotRequired[int],
        "Profile": NotRequired[ProfileType],
        "ScteMarkersSource": NotRequired[ScteMarkersSourceType],
        "StreamSelection": NotRequired[StreamSelectionTypeDef],
    },
)
HlsManifestTypeDef = TypedDict(
    "HlsManifestTypeDef",
    {
        "AdMarkers": NotRequired[AdMarkersType],
        "IncludeIframeOnlyStream": NotRequired[bool],
        "ManifestName": NotRequired[str],
        "ProgramDateTimeIntervalSeconds": NotRequired[int],
        "RepeatExtXKey": NotRequired[bool],
        "StreamSelection": NotRequired[StreamSelectionTypeDef],
    },
)
MssManifestTypeDef = TypedDict(
    "MssManifestTypeDef",
    {
        "ManifestName": NotRequired[str],
        "StreamSelection": NotRequired[StreamSelectionTypeDef],
    },
)
SpekeKeyProviderPaginatorTypeDef = TypedDict(
    "SpekeKeyProviderPaginatorTypeDef",
    {
        "RoleArn": str,
        "SystemIds": List[str],
        "Url": str,
        "EncryptionContractConfiguration": NotRequired[EncryptionContractConfigurationTypeDef],
    },
)
SpekeKeyProviderTypeDef = TypedDict(
    "SpekeKeyProviderTypeDef",
    {
        "RoleArn": str,
        "SystemIds": Sequence[str],
        "Url": str,
        "EncryptionContractConfiguration": NotRequired[EncryptionContractConfigurationTypeDef],
    },
)
ListAssetsRequestListAssetsPaginateTypeDef = TypedDict(
    "ListAssetsRequestListAssetsPaginateTypeDef",
    {
        "PackagingGroupId": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListPackagingConfigurationsRequestListPackagingConfigurationsPaginateTypeDef = TypedDict(
    "ListPackagingConfigurationsRequestListPackagingConfigurationsPaginateTypeDef",
    {
        "PackagingGroupId": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListPackagingGroupsRequestListPackagingGroupsPaginateTypeDef = TypedDict(
    "ListPackagingGroupsRequestListPackagingGroupsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListPackagingGroupsResponseTypeDef = TypedDict(
    "ListPackagingGroupsResponseTypeDef",
    {
        "NextToken": str,
        "PackagingGroups": List[PackagingGroupTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CmafEncryptionPaginatorTypeDef = TypedDict(
    "CmafEncryptionPaginatorTypeDef",
    {
        "SpekeKeyProvider": SpekeKeyProviderPaginatorTypeDef,
        "ConstantInitializationVector": NotRequired[str],
    },
)
DashEncryptionPaginatorTypeDef = TypedDict(
    "DashEncryptionPaginatorTypeDef",
    {
        "SpekeKeyProvider": SpekeKeyProviderPaginatorTypeDef,
    },
)
HlsEncryptionPaginatorTypeDef = TypedDict(
    "HlsEncryptionPaginatorTypeDef",
    {
        "SpekeKeyProvider": SpekeKeyProviderPaginatorTypeDef,
        "ConstantInitializationVector": NotRequired[str],
        "EncryptionMethod": NotRequired[EncryptionMethodType],
    },
)
MssEncryptionPaginatorTypeDef = TypedDict(
    "MssEncryptionPaginatorTypeDef",
    {
        "SpekeKeyProvider": SpekeKeyProviderPaginatorTypeDef,
    },
)
CmafEncryptionTypeDef = TypedDict(
    "CmafEncryptionTypeDef",
    {
        "SpekeKeyProvider": SpekeKeyProviderTypeDef,
        "ConstantInitializationVector": NotRequired[str],
    },
)
DashEncryptionTypeDef = TypedDict(
    "DashEncryptionTypeDef",
    {
        "SpekeKeyProvider": SpekeKeyProviderTypeDef,
    },
)
HlsEncryptionTypeDef = TypedDict(
    "HlsEncryptionTypeDef",
    {
        "SpekeKeyProvider": SpekeKeyProviderTypeDef,
        "ConstantInitializationVector": NotRequired[str],
        "EncryptionMethod": NotRequired[EncryptionMethodType],
    },
)
MssEncryptionTypeDef = TypedDict(
    "MssEncryptionTypeDef",
    {
        "SpekeKeyProvider": SpekeKeyProviderTypeDef,
    },
)
CmafPackagePaginatorTypeDef = TypedDict(
    "CmafPackagePaginatorTypeDef",
    {
        "HlsManifests": List[HlsManifestTypeDef],
        "Encryption": NotRequired[CmafEncryptionPaginatorTypeDef],
        "IncludeEncoderConfigurationInSegments": NotRequired[bool],
        "SegmentDurationSeconds": NotRequired[int],
    },
)
DashPackagePaginatorTypeDef = TypedDict(
    "DashPackagePaginatorTypeDef",
    {
        "DashManifests": List[DashManifestTypeDef],
        "Encryption": NotRequired[DashEncryptionPaginatorTypeDef],
        "IncludeEncoderConfigurationInSegments": NotRequired[bool],
        "IncludeIframeOnlyStream": NotRequired[bool],
        "PeriodTriggers": NotRequired[List[Literal["ADS"]]],
        "SegmentDurationSeconds": NotRequired[int],
        "SegmentTemplateFormat": NotRequired[SegmentTemplateFormatType],
    },
)
HlsPackagePaginatorTypeDef = TypedDict(
    "HlsPackagePaginatorTypeDef",
    {
        "HlsManifests": List[HlsManifestTypeDef],
        "Encryption": NotRequired[HlsEncryptionPaginatorTypeDef],
        "IncludeDvbSubtitles": NotRequired[bool],
        "SegmentDurationSeconds": NotRequired[int],
        "UseAudioRenditionGroup": NotRequired[bool],
    },
)
MssPackagePaginatorTypeDef = TypedDict(
    "MssPackagePaginatorTypeDef",
    {
        "MssManifests": List[MssManifestTypeDef],
        "Encryption": NotRequired[MssEncryptionPaginatorTypeDef],
        "SegmentDurationSeconds": NotRequired[int],
    },
)
CmafPackageTypeDef = TypedDict(
    "CmafPackageTypeDef",
    {
        "HlsManifests": Sequence[HlsManifestTypeDef],
        "Encryption": NotRequired[CmafEncryptionTypeDef],
        "IncludeEncoderConfigurationInSegments": NotRequired[bool],
        "SegmentDurationSeconds": NotRequired[int],
    },
)
DashPackageTypeDef = TypedDict(
    "DashPackageTypeDef",
    {
        "DashManifests": Sequence[DashManifestTypeDef],
        "Encryption": NotRequired[DashEncryptionTypeDef],
        "IncludeEncoderConfigurationInSegments": NotRequired[bool],
        "IncludeIframeOnlyStream": NotRequired[bool],
        "PeriodTriggers": NotRequired[Sequence[Literal["ADS"]]],
        "SegmentDurationSeconds": NotRequired[int],
        "SegmentTemplateFormat": NotRequired[SegmentTemplateFormatType],
    },
)
HlsPackageTypeDef = TypedDict(
    "HlsPackageTypeDef",
    {
        "HlsManifests": Sequence[HlsManifestTypeDef],
        "Encryption": NotRequired[HlsEncryptionTypeDef],
        "IncludeDvbSubtitles": NotRequired[bool],
        "SegmentDurationSeconds": NotRequired[int],
        "UseAudioRenditionGroup": NotRequired[bool],
    },
)
MssPackageTypeDef = TypedDict(
    "MssPackageTypeDef",
    {
        "MssManifests": Sequence[MssManifestTypeDef],
        "Encryption": NotRequired[MssEncryptionTypeDef],
        "SegmentDurationSeconds": NotRequired[int],
    },
)
PackagingConfigurationPaginatorTypeDef = TypedDict(
    "PackagingConfigurationPaginatorTypeDef",
    {
        "Arn": NotRequired[str],
        "CmafPackage": NotRequired[CmafPackagePaginatorTypeDef],
        "CreatedAt": NotRequired[str],
        "DashPackage": NotRequired[DashPackagePaginatorTypeDef],
        "HlsPackage": NotRequired[HlsPackagePaginatorTypeDef],
        "Id": NotRequired[str],
        "MssPackage": NotRequired[MssPackagePaginatorTypeDef],
        "PackagingGroupId": NotRequired[str],
        "Tags": NotRequired[Dict[str, str]],
    },
)
CreatePackagingConfigurationRequestRequestTypeDef = TypedDict(
    "CreatePackagingConfigurationRequestRequestTypeDef",
    {
        "Id": str,
        "PackagingGroupId": str,
        "CmafPackage": NotRequired[CmafPackageTypeDef],
        "DashPackage": NotRequired[DashPackageTypeDef],
        "HlsPackage": NotRequired[HlsPackageTypeDef],
        "MssPackage": NotRequired[MssPackageTypeDef],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
CreatePackagingConfigurationResponseTypeDef = TypedDict(
    "CreatePackagingConfigurationResponseTypeDef",
    {
        "Arn": str,
        "CmafPackage": CmafPackageTypeDef,
        "CreatedAt": str,
        "DashPackage": DashPackageTypeDef,
        "HlsPackage": HlsPackageTypeDef,
        "Id": str,
        "MssPackage": MssPackageTypeDef,
        "PackagingGroupId": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribePackagingConfigurationResponseTypeDef = TypedDict(
    "DescribePackagingConfigurationResponseTypeDef",
    {
        "Arn": str,
        "CmafPackage": CmafPackageTypeDef,
        "CreatedAt": str,
        "DashPackage": DashPackageTypeDef,
        "HlsPackage": HlsPackageTypeDef,
        "Id": str,
        "MssPackage": MssPackageTypeDef,
        "PackagingGroupId": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PackagingConfigurationTypeDef = TypedDict(
    "PackagingConfigurationTypeDef",
    {
        "Arn": NotRequired[str],
        "CmafPackage": NotRequired[CmafPackageTypeDef],
        "CreatedAt": NotRequired[str],
        "DashPackage": NotRequired[DashPackageTypeDef],
        "HlsPackage": NotRequired[HlsPackageTypeDef],
        "Id": NotRequired[str],
        "MssPackage": NotRequired[MssPackageTypeDef],
        "PackagingGroupId": NotRequired[str],
        "Tags": NotRequired[Dict[str, str]],
    },
)
ListPackagingConfigurationsResponsePaginatorTypeDef = TypedDict(
    "ListPackagingConfigurationsResponsePaginatorTypeDef",
    {
        "NextToken": str,
        "PackagingConfigurations": List[PackagingConfigurationPaginatorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListPackagingConfigurationsResponseTypeDef = TypedDict(
    "ListPackagingConfigurationsResponseTypeDef",
    {
        "NextToken": str,
        "PackagingConfigurations": List[PackagingConfigurationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
