"""
Type annotations for mediapackage service type definitions.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediapackage/type_defs/)

Usage::

    ```python
    from types_aiobotocore_mediapackage.type_defs import AuthorizationTypeDef

    data: AuthorizationTypeDef = ...
    ```
"""

import sys
from typing import Dict, List, Mapping, Sequence

from .literals import (
    AdMarkersType,
    AdsOnDeliveryRestrictionsType,
    AdTriggersElementType,
    CmafEncryptionMethodType,
    EncryptionMethodType,
    ManifestLayoutType,
    OriginationType,
    PlaylistTypeType,
    PresetSpeke20AudioType,
    PresetSpeke20VideoType,
    ProfileType,
    SegmentTemplateFormatType,
    StatusType,
    StreamOrderType,
    UtcTimingType,
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
    "AuthorizationTypeDef",
    "EgressAccessLogsTypeDef",
    "IngressAccessLogsTypeDef",
    "HlsManifestCreateOrUpdateParametersTypeDef",
    "StreamSelectionTypeDef",
    "HlsManifestTypeDef",
    "ResponseMetadataTypeDef",
    "CreateChannelRequestRequestTypeDef",
    "S3DestinationTypeDef",
    "DeleteChannelRequestRequestTypeDef",
    "DeleteOriginEndpointRequestRequestTypeDef",
    "DescribeChannelRequestRequestTypeDef",
    "DescribeHarvestJobRequestRequestTypeDef",
    "DescribeOriginEndpointRequestRequestTypeDef",
    "EncryptionContractConfigurationTypeDef",
    "IngestEndpointTypeDef",
    "PaginatorConfigTypeDef",
    "ListChannelsRequestRequestTypeDef",
    "ListHarvestJobsRequestRequestTypeDef",
    "ListOriginEndpointsRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "RotateChannelCredentialsRequestRequestTypeDef",
    "RotateIngestEndpointCredentialsRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateChannelRequestRequestTypeDef",
    "ConfigureLogsRequestRequestTypeDef",
    "EmptyResponseMetadataTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "CreateHarvestJobRequestRequestTypeDef",
    "CreateHarvestJobResponseTypeDef",
    "DescribeHarvestJobResponseTypeDef",
    "HarvestJobTypeDef",
    "SpekeKeyProviderPaginatorTypeDef",
    "SpekeKeyProviderTypeDef",
    "HlsIngestTypeDef",
    "ListChannelsRequestListChannelsPaginateTypeDef",
    "ListHarvestJobsRequestListHarvestJobsPaginateTypeDef",
    "ListOriginEndpointsRequestListOriginEndpointsPaginateTypeDef",
    "ListHarvestJobsResponseTypeDef",
    "CmafEncryptionPaginatorTypeDef",
    "DashEncryptionPaginatorTypeDef",
    "HlsEncryptionPaginatorTypeDef",
    "MssEncryptionPaginatorTypeDef",
    "CmafEncryptionTypeDef",
    "DashEncryptionTypeDef",
    "HlsEncryptionTypeDef",
    "MssEncryptionTypeDef",
    "ChannelTypeDef",
    "ConfigureLogsResponseTypeDef",
    "CreateChannelResponseTypeDef",
    "DescribeChannelResponseTypeDef",
    "RotateChannelCredentialsResponseTypeDef",
    "RotateIngestEndpointCredentialsResponseTypeDef",
    "UpdateChannelResponseTypeDef",
    "CmafPackagePaginatorTypeDef",
    "DashPackagePaginatorTypeDef",
    "HlsPackagePaginatorTypeDef",
    "MssPackagePaginatorTypeDef",
    "CmafPackageCreateOrUpdateParametersTypeDef",
    "CmafPackageTypeDef",
    "DashPackageTypeDef",
    "HlsPackageTypeDef",
    "MssPackageTypeDef",
    "ListChannelsResponseTypeDef",
    "OriginEndpointPaginatorTypeDef",
    "CreateOriginEndpointRequestRequestTypeDef",
    "CreateOriginEndpointResponseTypeDef",
    "DescribeOriginEndpointResponseTypeDef",
    "OriginEndpointTypeDef",
    "UpdateOriginEndpointRequestRequestTypeDef",
    "UpdateOriginEndpointResponseTypeDef",
    "ListOriginEndpointsResponsePaginatorTypeDef",
    "ListOriginEndpointsResponseTypeDef",
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
IngressAccessLogsTypeDef = TypedDict(
    "IngressAccessLogsTypeDef",
    {
        "LogGroupName": NotRequired[str],
    },
)
HlsManifestCreateOrUpdateParametersTypeDef = TypedDict(
    "HlsManifestCreateOrUpdateParametersTypeDef",
    {
        "Id": str,
        "AdMarkers": NotRequired[AdMarkersType],
        "AdTriggers": NotRequired[Sequence[AdTriggersElementType]],
        "AdsOnDeliveryRestrictions": NotRequired[AdsOnDeliveryRestrictionsType],
        "IncludeIframeOnlyStream": NotRequired[bool],
        "ManifestName": NotRequired[str],
        "PlaylistType": NotRequired[PlaylistTypeType],
        "PlaylistWindowSeconds": NotRequired[int],
        "ProgramDateTimeIntervalSeconds": NotRequired[int],
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
HlsManifestTypeDef = TypedDict(
    "HlsManifestTypeDef",
    {
        "Id": str,
        "AdMarkers": NotRequired[AdMarkersType],
        "IncludeIframeOnlyStream": NotRequired[bool],
        "ManifestName": NotRequired[str],
        "PlaylistType": NotRequired[PlaylistTypeType],
        "PlaylistWindowSeconds": NotRequired[int],
        "ProgramDateTimeIntervalSeconds": NotRequired[int],
        "Url": NotRequired[str],
        "AdTriggers": NotRequired[List[AdTriggersElementType]],
        "AdsOnDeliveryRestrictions": NotRequired[AdsOnDeliveryRestrictionsType],
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
CreateChannelRequestRequestTypeDef = TypedDict(
    "CreateChannelRequestRequestTypeDef",
    {
        "Id": str,
        "Description": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
S3DestinationTypeDef = TypedDict(
    "S3DestinationTypeDef",
    {
        "BucketName": str,
        "ManifestKey": str,
        "RoleArn": str,
    },
)
DeleteChannelRequestRequestTypeDef = TypedDict(
    "DeleteChannelRequestRequestTypeDef",
    {
        "Id": str,
    },
)
DeleteOriginEndpointRequestRequestTypeDef = TypedDict(
    "DeleteOriginEndpointRequestRequestTypeDef",
    {
        "Id": str,
    },
)
DescribeChannelRequestRequestTypeDef = TypedDict(
    "DescribeChannelRequestRequestTypeDef",
    {
        "Id": str,
    },
)
DescribeHarvestJobRequestRequestTypeDef = TypedDict(
    "DescribeHarvestJobRequestRequestTypeDef",
    {
        "Id": str,
    },
)
DescribeOriginEndpointRequestRequestTypeDef = TypedDict(
    "DescribeOriginEndpointRequestRequestTypeDef",
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
IngestEndpointTypeDef = TypedDict(
    "IngestEndpointTypeDef",
    {
        "Id": NotRequired[str],
        "Password": NotRequired[str],
        "Url": NotRequired[str],
        "Username": NotRequired[str],
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
ListChannelsRequestRequestTypeDef = TypedDict(
    "ListChannelsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListHarvestJobsRequestRequestTypeDef = TypedDict(
    "ListHarvestJobsRequestRequestTypeDef",
    {
        "IncludeChannelId": NotRequired[str],
        "IncludeStatus": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListOriginEndpointsRequestRequestTypeDef = TypedDict(
    "ListOriginEndpointsRequestRequestTypeDef",
    {
        "ChannelId": NotRequired[str],
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
RotateChannelCredentialsRequestRequestTypeDef = TypedDict(
    "RotateChannelCredentialsRequestRequestTypeDef",
    {
        "Id": str,
    },
)
RotateIngestEndpointCredentialsRequestRequestTypeDef = TypedDict(
    "RotateIngestEndpointCredentialsRequestRequestTypeDef",
    {
        "Id": str,
        "IngestEndpointId": str,
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
UpdateChannelRequestRequestTypeDef = TypedDict(
    "UpdateChannelRequestRequestTypeDef",
    {
        "Id": str,
        "Description": NotRequired[str],
    },
)
ConfigureLogsRequestRequestTypeDef = TypedDict(
    "ConfigureLogsRequestRequestTypeDef",
    {
        "Id": str,
        "EgressAccessLogs": NotRequired[EgressAccessLogsTypeDef],
        "IngressAccessLogs": NotRequired[IngressAccessLogsTypeDef],
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
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
CreateHarvestJobRequestRequestTypeDef = TypedDict(
    "CreateHarvestJobRequestRequestTypeDef",
    {
        "EndTime": str,
        "Id": str,
        "OriginEndpointId": str,
        "S3Destination": S3DestinationTypeDef,
        "StartTime": str,
    },
)
CreateHarvestJobResponseTypeDef = TypedDict(
    "CreateHarvestJobResponseTypeDef",
    {
        "Arn": str,
        "ChannelId": str,
        "CreatedAt": str,
        "EndTime": str,
        "Id": str,
        "OriginEndpointId": str,
        "S3Destination": S3DestinationTypeDef,
        "StartTime": str,
        "Status": StatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeHarvestJobResponseTypeDef = TypedDict(
    "DescribeHarvestJobResponseTypeDef",
    {
        "Arn": str,
        "ChannelId": str,
        "CreatedAt": str,
        "EndTime": str,
        "Id": str,
        "OriginEndpointId": str,
        "S3Destination": S3DestinationTypeDef,
        "StartTime": str,
        "Status": StatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
HarvestJobTypeDef = TypedDict(
    "HarvestJobTypeDef",
    {
        "Arn": NotRequired[str],
        "ChannelId": NotRequired[str],
        "CreatedAt": NotRequired[str],
        "EndTime": NotRequired[str],
        "Id": NotRequired[str],
        "OriginEndpointId": NotRequired[str],
        "S3Destination": NotRequired[S3DestinationTypeDef],
        "StartTime": NotRequired[str],
        "Status": NotRequired[StatusType],
    },
)
SpekeKeyProviderPaginatorTypeDef = TypedDict(
    "SpekeKeyProviderPaginatorTypeDef",
    {
        "ResourceId": str,
        "RoleArn": str,
        "SystemIds": List[str],
        "Url": str,
        "CertificateArn": NotRequired[str],
        "EncryptionContractConfiguration": NotRequired[EncryptionContractConfigurationTypeDef],
    },
)
SpekeKeyProviderTypeDef = TypedDict(
    "SpekeKeyProviderTypeDef",
    {
        "ResourceId": str,
        "RoleArn": str,
        "SystemIds": Sequence[str],
        "Url": str,
        "CertificateArn": NotRequired[str],
        "EncryptionContractConfiguration": NotRequired[EncryptionContractConfigurationTypeDef],
    },
)
HlsIngestTypeDef = TypedDict(
    "HlsIngestTypeDef",
    {
        "IngestEndpoints": NotRequired[List[IngestEndpointTypeDef]],
    },
)
ListChannelsRequestListChannelsPaginateTypeDef = TypedDict(
    "ListChannelsRequestListChannelsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListHarvestJobsRequestListHarvestJobsPaginateTypeDef = TypedDict(
    "ListHarvestJobsRequestListHarvestJobsPaginateTypeDef",
    {
        "IncludeChannelId": NotRequired[str],
        "IncludeStatus": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListOriginEndpointsRequestListOriginEndpointsPaginateTypeDef = TypedDict(
    "ListOriginEndpointsRequestListOriginEndpointsPaginateTypeDef",
    {
        "ChannelId": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListHarvestJobsResponseTypeDef = TypedDict(
    "ListHarvestJobsResponseTypeDef",
    {
        "HarvestJobs": List[HarvestJobTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CmafEncryptionPaginatorTypeDef = TypedDict(
    "CmafEncryptionPaginatorTypeDef",
    {
        "SpekeKeyProvider": SpekeKeyProviderPaginatorTypeDef,
        "ConstantInitializationVector": NotRequired[str],
        "EncryptionMethod": NotRequired[CmafEncryptionMethodType],
        "KeyRotationIntervalSeconds": NotRequired[int],
    },
)
DashEncryptionPaginatorTypeDef = TypedDict(
    "DashEncryptionPaginatorTypeDef",
    {
        "SpekeKeyProvider": SpekeKeyProviderPaginatorTypeDef,
        "KeyRotationIntervalSeconds": NotRequired[int],
    },
)
HlsEncryptionPaginatorTypeDef = TypedDict(
    "HlsEncryptionPaginatorTypeDef",
    {
        "SpekeKeyProvider": SpekeKeyProviderPaginatorTypeDef,
        "ConstantInitializationVector": NotRequired[str],
        "EncryptionMethod": NotRequired[EncryptionMethodType],
        "KeyRotationIntervalSeconds": NotRequired[int],
        "RepeatExtXKey": NotRequired[bool],
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
        "EncryptionMethod": NotRequired[CmafEncryptionMethodType],
        "KeyRotationIntervalSeconds": NotRequired[int],
    },
)
DashEncryptionTypeDef = TypedDict(
    "DashEncryptionTypeDef",
    {
        "SpekeKeyProvider": SpekeKeyProviderTypeDef,
        "KeyRotationIntervalSeconds": NotRequired[int],
    },
)
HlsEncryptionTypeDef = TypedDict(
    "HlsEncryptionTypeDef",
    {
        "SpekeKeyProvider": SpekeKeyProviderTypeDef,
        "ConstantInitializationVector": NotRequired[str],
        "EncryptionMethod": NotRequired[EncryptionMethodType],
        "KeyRotationIntervalSeconds": NotRequired[int],
        "RepeatExtXKey": NotRequired[bool],
    },
)
MssEncryptionTypeDef = TypedDict(
    "MssEncryptionTypeDef",
    {
        "SpekeKeyProvider": SpekeKeyProviderTypeDef,
    },
)
ChannelTypeDef = TypedDict(
    "ChannelTypeDef",
    {
        "Arn": NotRequired[str],
        "CreatedAt": NotRequired[str],
        "Description": NotRequired[str],
        "EgressAccessLogs": NotRequired[EgressAccessLogsTypeDef],
        "HlsIngest": NotRequired[HlsIngestTypeDef],
        "Id": NotRequired[str],
        "IngressAccessLogs": NotRequired[IngressAccessLogsTypeDef],
        "Tags": NotRequired[Dict[str, str]],
    },
)
ConfigureLogsResponseTypeDef = TypedDict(
    "ConfigureLogsResponseTypeDef",
    {
        "Arn": str,
        "CreatedAt": str,
        "Description": str,
        "EgressAccessLogs": EgressAccessLogsTypeDef,
        "HlsIngest": HlsIngestTypeDef,
        "Id": str,
        "IngressAccessLogs": IngressAccessLogsTypeDef,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateChannelResponseTypeDef = TypedDict(
    "CreateChannelResponseTypeDef",
    {
        "Arn": str,
        "CreatedAt": str,
        "Description": str,
        "EgressAccessLogs": EgressAccessLogsTypeDef,
        "HlsIngest": HlsIngestTypeDef,
        "Id": str,
        "IngressAccessLogs": IngressAccessLogsTypeDef,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeChannelResponseTypeDef = TypedDict(
    "DescribeChannelResponseTypeDef",
    {
        "Arn": str,
        "CreatedAt": str,
        "Description": str,
        "EgressAccessLogs": EgressAccessLogsTypeDef,
        "HlsIngest": HlsIngestTypeDef,
        "Id": str,
        "IngressAccessLogs": IngressAccessLogsTypeDef,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RotateChannelCredentialsResponseTypeDef = TypedDict(
    "RotateChannelCredentialsResponseTypeDef",
    {
        "Arn": str,
        "CreatedAt": str,
        "Description": str,
        "EgressAccessLogs": EgressAccessLogsTypeDef,
        "HlsIngest": HlsIngestTypeDef,
        "Id": str,
        "IngressAccessLogs": IngressAccessLogsTypeDef,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RotateIngestEndpointCredentialsResponseTypeDef = TypedDict(
    "RotateIngestEndpointCredentialsResponseTypeDef",
    {
        "Arn": str,
        "CreatedAt": str,
        "Description": str,
        "EgressAccessLogs": EgressAccessLogsTypeDef,
        "HlsIngest": HlsIngestTypeDef,
        "Id": str,
        "IngressAccessLogs": IngressAccessLogsTypeDef,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateChannelResponseTypeDef = TypedDict(
    "UpdateChannelResponseTypeDef",
    {
        "Arn": str,
        "CreatedAt": str,
        "Description": str,
        "EgressAccessLogs": EgressAccessLogsTypeDef,
        "HlsIngest": HlsIngestTypeDef,
        "Id": str,
        "IngressAccessLogs": IngressAccessLogsTypeDef,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CmafPackagePaginatorTypeDef = TypedDict(
    "CmafPackagePaginatorTypeDef",
    {
        "Encryption": NotRequired[CmafEncryptionPaginatorTypeDef],
        "HlsManifests": NotRequired[List[HlsManifestTypeDef]],
        "SegmentDurationSeconds": NotRequired[int],
        "SegmentPrefix": NotRequired[str],
        "StreamSelection": NotRequired[StreamSelectionTypeDef],
    },
)
DashPackagePaginatorTypeDef = TypedDict(
    "DashPackagePaginatorTypeDef",
    {
        "AdTriggers": NotRequired[List[AdTriggersElementType]],
        "AdsOnDeliveryRestrictions": NotRequired[AdsOnDeliveryRestrictionsType],
        "Encryption": NotRequired[DashEncryptionPaginatorTypeDef],
        "IncludeIframeOnlyStream": NotRequired[bool],
        "ManifestLayout": NotRequired[ManifestLayoutType],
        "ManifestWindowSeconds": NotRequired[int],
        "MinBufferTimeSeconds": NotRequired[int],
        "MinUpdatePeriodSeconds": NotRequired[int],
        "PeriodTriggers": NotRequired[List[Literal["ADS"]]],
        "Profile": NotRequired[ProfileType],
        "SegmentDurationSeconds": NotRequired[int],
        "SegmentTemplateFormat": NotRequired[SegmentTemplateFormatType],
        "StreamSelection": NotRequired[StreamSelectionTypeDef],
        "SuggestedPresentationDelaySeconds": NotRequired[int],
        "UtcTiming": NotRequired[UtcTimingType],
        "UtcTimingUri": NotRequired[str],
    },
)
HlsPackagePaginatorTypeDef = TypedDict(
    "HlsPackagePaginatorTypeDef",
    {
        "AdMarkers": NotRequired[AdMarkersType],
        "AdTriggers": NotRequired[List[AdTriggersElementType]],
        "AdsOnDeliveryRestrictions": NotRequired[AdsOnDeliveryRestrictionsType],
        "Encryption": NotRequired[HlsEncryptionPaginatorTypeDef],
        "IncludeDvbSubtitles": NotRequired[bool],
        "IncludeIframeOnlyStream": NotRequired[bool],
        "PlaylistType": NotRequired[PlaylistTypeType],
        "PlaylistWindowSeconds": NotRequired[int],
        "ProgramDateTimeIntervalSeconds": NotRequired[int],
        "SegmentDurationSeconds": NotRequired[int],
        "StreamSelection": NotRequired[StreamSelectionTypeDef],
        "UseAudioRenditionGroup": NotRequired[bool],
    },
)
MssPackagePaginatorTypeDef = TypedDict(
    "MssPackagePaginatorTypeDef",
    {
        "Encryption": NotRequired[MssEncryptionPaginatorTypeDef],
        "ManifestWindowSeconds": NotRequired[int],
        "SegmentDurationSeconds": NotRequired[int],
        "StreamSelection": NotRequired[StreamSelectionTypeDef],
    },
)
CmafPackageCreateOrUpdateParametersTypeDef = TypedDict(
    "CmafPackageCreateOrUpdateParametersTypeDef",
    {
        "Encryption": NotRequired[CmafEncryptionTypeDef],
        "HlsManifests": NotRequired[Sequence[HlsManifestCreateOrUpdateParametersTypeDef]],
        "SegmentDurationSeconds": NotRequired[int],
        "SegmentPrefix": NotRequired[str],
        "StreamSelection": NotRequired[StreamSelectionTypeDef],
    },
)
CmafPackageTypeDef = TypedDict(
    "CmafPackageTypeDef",
    {
        "Encryption": NotRequired[CmafEncryptionTypeDef],
        "HlsManifests": NotRequired[List[HlsManifestTypeDef]],
        "SegmentDurationSeconds": NotRequired[int],
        "SegmentPrefix": NotRequired[str],
        "StreamSelection": NotRequired[StreamSelectionTypeDef],
    },
)
DashPackageTypeDef = TypedDict(
    "DashPackageTypeDef",
    {
        "AdTriggers": NotRequired[Sequence[AdTriggersElementType]],
        "AdsOnDeliveryRestrictions": NotRequired[AdsOnDeliveryRestrictionsType],
        "Encryption": NotRequired[DashEncryptionTypeDef],
        "IncludeIframeOnlyStream": NotRequired[bool],
        "ManifestLayout": NotRequired[ManifestLayoutType],
        "ManifestWindowSeconds": NotRequired[int],
        "MinBufferTimeSeconds": NotRequired[int],
        "MinUpdatePeriodSeconds": NotRequired[int],
        "PeriodTriggers": NotRequired[Sequence[Literal["ADS"]]],
        "Profile": NotRequired[ProfileType],
        "SegmentDurationSeconds": NotRequired[int],
        "SegmentTemplateFormat": NotRequired[SegmentTemplateFormatType],
        "StreamSelection": NotRequired[StreamSelectionTypeDef],
        "SuggestedPresentationDelaySeconds": NotRequired[int],
        "UtcTiming": NotRequired[UtcTimingType],
        "UtcTimingUri": NotRequired[str],
    },
)
HlsPackageTypeDef = TypedDict(
    "HlsPackageTypeDef",
    {
        "AdMarkers": NotRequired[AdMarkersType],
        "AdTriggers": NotRequired[Sequence[AdTriggersElementType]],
        "AdsOnDeliveryRestrictions": NotRequired[AdsOnDeliveryRestrictionsType],
        "Encryption": NotRequired[HlsEncryptionTypeDef],
        "IncludeDvbSubtitles": NotRequired[bool],
        "IncludeIframeOnlyStream": NotRequired[bool],
        "PlaylistType": NotRequired[PlaylistTypeType],
        "PlaylistWindowSeconds": NotRequired[int],
        "ProgramDateTimeIntervalSeconds": NotRequired[int],
        "SegmentDurationSeconds": NotRequired[int],
        "StreamSelection": NotRequired[StreamSelectionTypeDef],
        "UseAudioRenditionGroup": NotRequired[bool],
    },
)
MssPackageTypeDef = TypedDict(
    "MssPackageTypeDef",
    {
        "Encryption": NotRequired[MssEncryptionTypeDef],
        "ManifestWindowSeconds": NotRequired[int],
        "SegmentDurationSeconds": NotRequired[int],
        "StreamSelection": NotRequired[StreamSelectionTypeDef],
    },
)
ListChannelsResponseTypeDef = TypedDict(
    "ListChannelsResponseTypeDef",
    {
        "Channels": List[ChannelTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
OriginEndpointPaginatorTypeDef = TypedDict(
    "OriginEndpointPaginatorTypeDef",
    {
        "Arn": NotRequired[str],
        "Authorization": NotRequired[AuthorizationTypeDef],
        "ChannelId": NotRequired[str],
        "CmafPackage": NotRequired[CmafPackagePaginatorTypeDef],
        "CreatedAt": NotRequired[str],
        "DashPackage": NotRequired[DashPackagePaginatorTypeDef],
        "Description": NotRequired[str],
        "HlsPackage": NotRequired[HlsPackagePaginatorTypeDef],
        "Id": NotRequired[str],
        "ManifestName": NotRequired[str],
        "MssPackage": NotRequired[MssPackagePaginatorTypeDef],
        "Origination": NotRequired[OriginationType],
        "StartoverWindowSeconds": NotRequired[int],
        "Tags": NotRequired[Dict[str, str]],
        "TimeDelaySeconds": NotRequired[int],
        "Url": NotRequired[str],
        "Whitelist": NotRequired[List[str]],
    },
)
CreateOriginEndpointRequestRequestTypeDef = TypedDict(
    "CreateOriginEndpointRequestRequestTypeDef",
    {
        "ChannelId": str,
        "Id": str,
        "Authorization": NotRequired[AuthorizationTypeDef],
        "CmafPackage": NotRequired[CmafPackageCreateOrUpdateParametersTypeDef],
        "DashPackage": NotRequired[DashPackageTypeDef],
        "Description": NotRequired[str],
        "HlsPackage": NotRequired[HlsPackageTypeDef],
        "ManifestName": NotRequired[str],
        "MssPackage": NotRequired[MssPackageTypeDef],
        "Origination": NotRequired[OriginationType],
        "StartoverWindowSeconds": NotRequired[int],
        "Tags": NotRequired[Mapping[str, str]],
        "TimeDelaySeconds": NotRequired[int],
        "Whitelist": NotRequired[Sequence[str]],
    },
)
CreateOriginEndpointResponseTypeDef = TypedDict(
    "CreateOriginEndpointResponseTypeDef",
    {
        "Arn": str,
        "Authorization": AuthorizationTypeDef,
        "ChannelId": str,
        "CmafPackage": CmafPackageTypeDef,
        "CreatedAt": str,
        "DashPackage": DashPackageTypeDef,
        "Description": str,
        "HlsPackage": HlsPackageTypeDef,
        "Id": str,
        "ManifestName": str,
        "MssPackage": MssPackageTypeDef,
        "Origination": OriginationType,
        "StartoverWindowSeconds": int,
        "Tags": Dict[str, str],
        "TimeDelaySeconds": int,
        "Url": str,
        "Whitelist": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeOriginEndpointResponseTypeDef = TypedDict(
    "DescribeOriginEndpointResponseTypeDef",
    {
        "Arn": str,
        "Authorization": AuthorizationTypeDef,
        "ChannelId": str,
        "CmafPackage": CmafPackageTypeDef,
        "CreatedAt": str,
        "DashPackage": DashPackageTypeDef,
        "Description": str,
        "HlsPackage": HlsPackageTypeDef,
        "Id": str,
        "ManifestName": str,
        "MssPackage": MssPackageTypeDef,
        "Origination": OriginationType,
        "StartoverWindowSeconds": int,
        "Tags": Dict[str, str],
        "TimeDelaySeconds": int,
        "Url": str,
        "Whitelist": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
OriginEndpointTypeDef = TypedDict(
    "OriginEndpointTypeDef",
    {
        "Arn": NotRequired[str],
        "Authorization": NotRequired[AuthorizationTypeDef],
        "ChannelId": NotRequired[str],
        "CmafPackage": NotRequired[CmafPackageTypeDef],
        "CreatedAt": NotRequired[str],
        "DashPackage": NotRequired[DashPackageTypeDef],
        "Description": NotRequired[str],
        "HlsPackage": NotRequired[HlsPackageTypeDef],
        "Id": NotRequired[str],
        "ManifestName": NotRequired[str],
        "MssPackage": NotRequired[MssPackageTypeDef],
        "Origination": NotRequired[OriginationType],
        "StartoverWindowSeconds": NotRequired[int],
        "Tags": NotRequired[Dict[str, str]],
        "TimeDelaySeconds": NotRequired[int],
        "Url": NotRequired[str],
        "Whitelist": NotRequired[List[str]],
    },
)
UpdateOriginEndpointRequestRequestTypeDef = TypedDict(
    "UpdateOriginEndpointRequestRequestTypeDef",
    {
        "Id": str,
        "Authorization": NotRequired[AuthorizationTypeDef],
        "CmafPackage": NotRequired[CmafPackageCreateOrUpdateParametersTypeDef],
        "DashPackage": NotRequired[DashPackageTypeDef],
        "Description": NotRequired[str],
        "HlsPackage": NotRequired[HlsPackageTypeDef],
        "ManifestName": NotRequired[str],
        "MssPackage": NotRequired[MssPackageTypeDef],
        "Origination": NotRequired[OriginationType],
        "StartoverWindowSeconds": NotRequired[int],
        "TimeDelaySeconds": NotRequired[int],
        "Whitelist": NotRequired[Sequence[str]],
    },
)
UpdateOriginEndpointResponseTypeDef = TypedDict(
    "UpdateOriginEndpointResponseTypeDef",
    {
        "Arn": str,
        "Authorization": AuthorizationTypeDef,
        "ChannelId": str,
        "CmafPackage": CmafPackageTypeDef,
        "CreatedAt": str,
        "DashPackage": DashPackageTypeDef,
        "Description": str,
        "HlsPackage": HlsPackageTypeDef,
        "Id": str,
        "ManifestName": str,
        "MssPackage": MssPackageTypeDef,
        "Origination": OriginationType,
        "StartoverWindowSeconds": int,
        "Tags": Dict[str, str],
        "TimeDelaySeconds": int,
        "Url": str,
        "Whitelist": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListOriginEndpointsResponsePaginatorTypeDef = TypedDict(
    "ListOriginEndpointsResponsePaginatorTypeDef",
    {
        "NextToken": str,
        "OriginEndpoints": List[OriginEndpointPaginatorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListOriginEndpointsResponseTypeDef = TypedDict(
    "ListOriginEndpointsResponseTypeDef",
    {
        "NextToken": str,
        "OriginEndpoints": List[OriginEndpointTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
