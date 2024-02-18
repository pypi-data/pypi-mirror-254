"""
Type annotations for mediatailor service type definitions.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediatailor/type_defs/)

Usage::

    ```python
    from types_aiobotocore_mediatailor.type_defs import SecretsManagerAccessTokenConfigurationTypeDef

    data: SecretsManagerAccessTokenConfigurationTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from .literals import (
    AccessTypeType,
    AdMarkupTypeType,
    AlertCategoryType,
    ChannelStateType,
    FillPolicyType,
    MessageTypeType,
    ModeType,
    OriginManifestTypeType,
    PlaybackModeType,
    RelativePositionType,
    ScheduleEntryTypeType,
    TierType,
    TypeType,
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
    "SecretsManagerAccessTokenConfigurationTypeDef",
    "AdBreakOpportunityTypeDef",
    "KeyValuePairTypeDef",
    "SlateSourceTypeDef",
    "SpliceInsertMessageTypeDef",
    "AdMarkerPassthroughTypeDef",
    "AlertTypeDef",
    "AvailMatchingCriteriaTypeDef",
    "AvailSuppressionTypeDef",
    "BumperTypeDef",
    "CdnConfigurationTypeDef",
    "LogConfigurationForChannelTypeDef",
    "ClipRangeTypeDef",
    "ConfigureLogsForChannelRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "ConfigureLogsForPlaybackConfigurationRequestRequestTypeDef",
    "TimeShiftConfigurationTypeDef",
    "HttpPackageConfigurationTypeDef",
    "DefaultSegmentDeliveryConfigurationTypeDef",
    "HttpConfigurationTypeDef",
    "SegmentDeliveryConfigurationTypeDef",
    "DashConfigurationForPutTypeDef",
    "DashConfigurationTypeDef",
    "DashPlaylistSettingsTypeDef",
    "DeleteChannelPolicyRequestRequestTypeDef",
    "DeleteChannelRequestRequestTypeDef",
    "DeleteLiveSourceRequestRequestTypeDef",
    "DeletePlaybackConfigurationRequestRequestTypeDef",
    "DeletePrefetchScheduleRequestRequestTypeDef",
    "DeleteProgramRequestRequestTypeDef",
    "DeleteSourceLocationRequestRequestTypeDef",
    "DeleteVodSourceRequestRequestTypeDef",
    "DescribeChannelRequestRequestTypeDef",
    "DescribeLiveSourceRequestRequestTypeDef",
    "DescribeProgramRequestRequestTypeDef",
    "DescribeSourceLocationRequestRequestTypeDef",
    "DescribeVodSourceRequestRequestTypeDef",
    "GetChannelPolicyRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "GetChannelScheduleRequestRequestTypeDef",
    "GetPlaybackConfigurationRequestRequestTypeDef",
    "HlsConfigurationTypeDef",
    "LivePreRollConfigurationTypeDef",
    "LogConfigurationTypeDef",
    "GetPrefetchScheduleRequestRequestTypeDef",
    "HlsPlaylistSettingsPaginatorTypeDef",
    "HlsPlaylistSettingsTypeDef",
    "ListAlertsRequestRequestTypeDef",
    "ListChannelsRequestRequestTypeDef",
    "ListLiveSourcesRequestRequestTypeDef",
    "ListPlaybackConfigurationsRequestRequestTypeDef",
    "ListPrefetchSchedulesRequestRequestTypeDef",
    "ListSourceLocationsRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListVodSourcesRequestRequestTypeDef",
    "TimestampTypeDef",
    "PrefetchRetrievalPaginatorTypeDef",
    "PutChannelPolicyRequestRequestTypeDef",
    "ScheduleAdBreakTypeDef",
    "TransitionTypeDef",
    "SegmentationDescriptorTypeDef",
    "StartChannelRequestRequestTypeDef",
    "StopChannelRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateProgramTransitionTypeDef",
    "AccessConfigurationTypeDef",
    "ManifestProcessingRulesTypeDef",
    "PrefetchConsumptionPaginatorTypeDef",
    "ConfigureLogsForChannelResponseTypeDef",
    "ConfigureLogsForPlaybackConfigurationResponseTypeDef",
    "EmptyResponseMetadataTypeDef",
    "GetChannelPolicyResponseTypeDef",
    "ListAlertsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "CreateLiveSourceRequestRequestTypeDef",
    "CreateLiveSourceResponseTypeDef",
    "CreateVodSourceRequestRequestTypeDef",
    "CreateVodSourceResponseTypeDef",
    "DescribeLiveSourceResponseTypeDef",
    "DescribeVodSourceResponseTypeDef",
    "LiveSourceTypeDef",
    "UpdateLiveSourceRequestRequestTypeDef",
    "UpdateLiveSourceResponseTypeDef",
    "UpdateVodSourceRequestRequestTypeDef",
    "UpdateVodSourceResponseTypeDef",
    "VodSourceTypeDef",
    "GetChannelScheduleRequestGetChannelSchedulePaginateTypeDef",
    "ListAlertsRequestListAlertsPaginateTypeDef",
    "ListChannelsRequestListChannelsPaginateTypeDef",
    "ListLiveSourcesRequestListLiveSourcesPaginateTypeDef",
    "ListPlaybackConfigurationsRequestListPlaybackConfigurationsPaginateTypeDef",
    "ListPrefetchSchedulesRequestListPrefetchSchedulesPaginateTypeDef",
    "ListSourceLocationsRequestListSourceLocationsPaginateTypeDef",
    "ListVodSourcesRequestListVodSourcesPaginateTypeDef",
    "ResponseOutputItemPaginatorTypeDef",
    "RequestOutputItemTypeDef",
    "ResponseOutputItemTypeDef",
    "PrefetchConsumptionTypeDef",
    "PrefetchRetrievalTypeDef",
    "ScheduleEntryTypeDef",
    "ScheduleConfigurationTypeDef",
    "TimeSignalMessageTypeDef",
    "UpdateProgramScheduleConfigurationTypeDef",
    "CreateSourceLocationRequestRequestTypeDef",
    "CreateSourceLocationResponseTypeDef",
    "DescribeSourceLocationResponseTypeDef",
    "SourceLocationTypeDef",
    "UpdateSourceLocationRequestRequestTypeDef",
    "UpdateSourceLocationResponseTypeDef",
    "GetPlaybackConfigurationResponseTypeDef",
    "PlaybackConfigurationTypeDef",
    "PutPlaybackConfigurationRequestRequestTypeDef",
    "PutPlaybackConfigurationResponseTypeDef",
    "PrefetchSchedulePaginatorTypeDef",
    "ListLiveSourcesResponseTypeDef",
    "ListVodSourcesResponseTypeDef",
    "ChannelPaginatorTypeDef",
    "CreateChannelRequestRequestTypeDef",
    "UpdateChannelRequestRequestTypeDef",
    "ChannelTypeDef",
    "CreateChannelResponseTypeDef",
    "DescribeChannelResponseTypeDef",
    "UpdateChannelResponseTypeDef",
    "CreatePrefetchScheduleRequestRequestTypeDef",
    "CreatePrefetchScheduleResponseTypeDef",
    "GetPrefetchScheduleResponseTypeDef",
    "PrefetchScheduleTypeDef",
    "GetChannelScheduleResponseTypeDef",
    "AdBreakTypeDef",
    "ListSourceLocationsResponseTypeDef",
    "ListPlaybackConfigurationsResponseTypeDef",
    "ListPrefetchSchedulesResponsePaginatorTypeDef",
    "ListChannelsResponsePaginatorTypeDef",
    "ListChannelsResponseTypeDef",
    "ListPrefetchSchedulesResponseTypeDef",
    "CreateProgramRequestRequestTypeDef",
    "CreateProgramResponseTypeDef",
    "DescribeProgramResponseTypeDef",
    "UpdateProgramRequestRequestTypeDef",
    "UpdateProgramResponseTypeDef",
)

SecretsManagerAccessTokenConfigurationTypeDef = TypedDict(
    "SecretsManagerAccessTokenConfigurationTypeDef",
    {
        "HeaderName": NotRequired[str],
        "SecretArn": NotRequired[str],
        "SecretStringKey": NotRequired[str],
    },
)
AdBreakOpportunityTypeDef = TypedDict(
    "AdBreakOpportunityTypeDef",
    {
        "OffsetMillis": int,
    },
)
KeyValuePairTypeDef = TypedDict(
    "KeyValuePairTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)
SlateSourceTypeDef = TypedDict(
    "SlateSourceTypeDef",
    {
        "SourceLocationName": NotRequired[str],
        "VodSourceName": NotRequired[str],
    },
)
SpliceInsertMessageTypeDef = TypedDict(
    "SpliceInsertMessageTypeDef",
    {
        "AvailNum": NotRequired[int],
        "AvailsExpected": NotRequired[int],
        "SpliceEventId": NotRequired[int],
        "UniqueProgramId": NotRequired[int],
    },
)
AdMarkerPassthroughTypeDef = TypedDict(
    "AdMarkerPassthroughTypeDef",
    {
        "Enabled": NotRequired[bool],
    },
)
AlertTypeDef = TypedDict(
    "AlertTypeDef",
    {
        "AlertCode": str,
        "AlertMessage": str,
        "LastModifiedTime": datetime,
        "RelatedResourceArns": List[str],
        "ResourceArn": str,
        "Category": NotRequired[AlertCategoryType],
    },
)
AvailMatchingCriteriaTypeDef = TypedDict(
    "AvailMatchingCriteriaTypeDef",
    {
        "DynamicVariable": str,
        "Operator": Literal["EQUALS"],
    },
)
AvailSuppressionTypeDef = TypedDict(
    "AvailSuppressionTypeDef",
    {
        "FillPolicy": NotRequired[FillPolicyType],
        "Mode": NotRequired[ModeType],
        "Value": NotRequired[str],
    },
)
BumperTypeDef = TypedDict(
    "BumperTypeDef",
    {
        "EndUrl": NotRequired[str],
        "StartUrl": NotRequired[str],
    },
)
CdnConfigurationTypeDef = TypedDict(
    "CdnConfigurationTypeDef",
    {
        "AdSegmentUrlPrefix": NotRequired[str],
        "ContentSegmentUrlPrefix": NotRequired[str],
    },
)
LogConfigurationForChannelTypeDef = TypedDict(
    "LogConfigurationForChannelTypeDef",
    {
        "LogTypes": NotRequired[List[Literal["AS_RUN"]]],
    },
)
ClipRangeTypeDef = TypedDict(
    "ClipRangeTypeDef",
    {
        "EndOffsetMillis": int,
    },
)
ConfigureLogsForChannelRequestRequestTypeDef = TypedDict(
    "ConfigureLogsForChannelRequestRequestTypeDef",
    {
        "ChannelName": str,
        "LogTypes": Sequence[Literal["AS_RUN"]],
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
ConfigureLogsForPlaybackConfigurationRequestRequestTypeDef = TypedDict(
    "ConfigureLogsForPlaybackConfigurationRequestRequestTypeDef",
    {
        "PercentEnabled": int,
        "PlaybackConfigurationName": str,
    },
)
TimeShiftConfigurationTypeDef = TypedDict(
    "TimeShiftConfigurationTypeDef",
    {
        "MaxTimeDelaySeconds": int,
    },
)
HttpPackageConfigurationTypeDef = TypedDict(
    "HttpPackageConfigurationTypeDef",
    {
        "Path": str,
        "SourceGroup": str,
        "Type": TypeType,
    },
)
DefaultSegmentDeliveryConfigurationTypeDef = TypedDict(
    "DefaultSegmentDeliveryConfigurationTypeDef",
    {
        "BaseUrl": NotRequired[str],
    },
)
HttpConfigurationTypeDef = TypedDict(
    "HttpConfigurationTypeDef",
    {
        "BaseUrl": str,
    },
)
SegmentDeliveryConfigurationTypeDef = TypedDict(
    "SegmentDeliveryConfigurationTypeDef",
    {
        "BaseUrl": NotRequired[str],
        "Name": NotRequired[str],
    },
)
DashConfigurationForPutTypeDef = TypedDict(
    "DashConfigurationForPutTypeDef",
    {
        "MpdLocation": NotRequired[str],
        "OriginManifestType": NotRequired[OriginManifestTypeType],
    },
)
DashConfigurationTypeDef = TypedDict(
    "DashConfigurationTypeDef",
    {
        "ManifestEndpointPrefix": NotRequired[str],
        "MpdLocation": NotRequired[str],
        "OriginManifestType": NotRequired[OriginManifestTypeType],
    },
)
DashPlaylistSettingsTypeDef = TypedDict(
    "DashPlaylistSettingsTypeDef",
    {
        "ManifestWindowSeconds": NotRequired[int],
        "MinBufferTimeSeconds": NotRequired[int],
        "MinUpdatePeriodSeconds": NotRequired[int],
        "SuggestedPresentationDelaySeconds": NotRequired[int],
    },
)
DeleteChannelPolicyRequestRequestTypeDef = TypedDict(
    "DeleteChannelPolicyRequestRequestTypeDef",
    {
        "ChannelName": str,
    },
)
DeleteChannelRequestRequestTypeDef = TypedDict(
    "DeleteChannelRequestRequestTypeDef",
    {
        "ChannelName": str,
    },
)
DeleteLiveSourceRequestRequestTypeDef = TypedDict(
    "DeleteLiveSourceRequestRequestTypeDef",
    {
        "LiveSourceName": str,
        "SourceLocationName": str,
    },
)
DeletePlaybackConfigurationRequestRequestTypeDef = TypedDict(
    "DeletePlaybackConfigurationRequestRequestTypeDef",
    {
        "Name": str,
    },
)
DeletePrefetchScheduleRequestRequestTypeDef = TypedDict(
    "DeletePrefetchScheduleRequestRequestTypeDef",
    {
        "Name": str,
        "PlaybackConfigurationName": str,
    },
)
DeleteProgramRequestRequestTypeDef = TypedDict(
    "DeleteProgramRequestRequestTypeDef",
    {
        "ChannelName": str,
        "ProgramName": str,
    },
)
DeleteSourceLocationRequestRequestTypeDef = TypedDict(
    "DeleteSourceLocationRequestRequestTypeDef",
    {
        "SourceLocationName": str,
    },
)
DeleteVodSourceRequestRequestTypeDef = TypedDict(
    "DeleteVodSourceRequestRequestTypeDef",
    {
        "SourceLocationName": str,
        "VodSourceName": str,
    },
)
DescribeChannelRequestRequestTypeDef = TypedDict(
    "DescribeChannelRequestRequestTypeDef",
    {
        "ChannelName": str,
    },
)
DescribeLiveSourceRequestRequestTypeDef = TypedDict(
    "DescribeLiveSourceRequestRequestTypeDef",
    {
        "LiveSourceName": str,
        "SourceLocationName": str,
    },
)
DescribeProgramRequestRequestTypeDef = TypedDict(
    "DescribeProgramRequestRequestTypeDef",
    {
        "ChannelName": str,
        "ProgramName": str,
    },
)
DescribeSourceLocationRequestRequestTypeDef = TypedDict(
    "DescribeSourceLocationRequestRequestTypeDef",
    {
        "SourceLocationName": str,
    },
)
DescribeVodSourceRequestRequestTypeDef = TypedDict(
    "DescribeVodSourceRequestRequestTypeDef",
    {
        "SourceLocationName": str,
        "VodSourceName": str,
    },
)
GetChannelPolicyRequestRequestTypeDef = TypedDict(
    "GetChannelPolicyRequestRequestTypeDef",
    {
        "ChannelName": str,
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
GetChannelScheduleRequestRequestTypeDef = TypedDict(
    "GetChannelScheduleRequestRequestTypeDef",
    {
        "ChannelName": str,
        "DurationMinutes": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
GetPlaybackConfigurationRequestRequestTypeDef = TypedDict(
    "GetPlaybackConfigurationRequestRequestTypeDef",
    {
        "Name": str,
    },
)
HlsConfigurationTypeDef = TypedDict(
    "HlsConfigurationTypeDef",
    {
        "ManifestEndpointPrefix": NotRequired[str],
    },
)
LivePreRollConfigurationTypeDef = TypedDict(
    "LivePreRollConfigurationTypeDef",
    {
        "AdDecisionServerUrl": NotRequired[str],
        "MaxDurationSeconds": NotRequired[int],
    },
)
LogConfigurationTypeDef = TypedDict(
    "LogConfigurationTypeDef",
    {
        "PercentEnabled": int,
    },
)
GetPrefetchScheduleRequestRequestTypeDef = TypedDict(
    "GetPrefetchScheduleRequestRequestTypeDef",
    {
        "Name": str,
        "PlaybackConfigurationName": str,
    },
)
HlsPlaylistSettingsPaginatorTypeDef = TypedDict(
    "HlsPlaylistSettingsPaginatorTypeDef",
    {
        "AdMarkupType": NotRequired[List[AdMarkupTypeType]],
        "ManifestWindowSeconds": NotRequired[int],
    },
)
HlsPlaylistSettingsTypeDef = TypedDict(
    "HlsPlaylistSettingsTypeDef",
    {
        "AdMarkupType": NotRequired[Sequence[AdMarkupTypeType]],
        "ManifestWindowSeconds": NotRequired[int],
    },
)
ListAlertsRequestRequestTypeDef = TypedDict(
    "ListAlertsRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListChannelsRequestRequestTypeDef = TypedDict(
    "ListChannelsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListLiveSourcesRequestRequestTypeDef = TypedDict(
    "ListLiveSourcesRequestRequestTypeDef",
    {
        "SourceLocationName": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListPlaybackConfigurationsRequestRequestTypeDef = TypedDict(
    "ListPlaybackConfigurationsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListPrefetchSchedulesRequestRequestTypeDef = TypedDict(
    "ListPrefetchSchedulesRequestRequestTypeDef",
    {
        "PlaybackConfigurationName": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "StreamId": NotRequired[str],
    },
)
ListSourceLocationsRequestRequestTypeDef = TypedDict(
    "ListSourceLocationsRequestRequestTypeDef",
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
ListVodSourcesRequestRequestTypeDef = TypedDict(
    "ListVodSourcesRequestRequestTypeDef",
    {
        "SourceLocationName": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
TimestampTypeDef = Union[datetime, str]
PrefetchRetrievalPaginatorTypeDef = TypedDict(
    "PrefetchRetrievalPaginatorTypeDef",
    {
        "EndTime": datetime,
        "DynamicVariables": NotRequired[Dict[str, str]],
        "StartTime": NotRequired[datetime],
    },
)
PutChannelPolicyRequestRequestTypeDef = TypedDict(
    "PutChannelPolicyRequestRequestTypeDef",
    {
        "ChannelName": str,
        "Policy": str,
    },
)
ScheduleAdBreakTypeDef = TypedDict(
    "ScheduleAdBreakTypeDef",
    {
        "ApproximateDurationSeconds": NotRequired[int],
        "ApproximateStartTime": NotRequired[datetime],
        "SourceLocationName": NotRequired[str],
        "VodSourceName": NotRequired[str],
    },
)
TransitionTypeDef = TypedDict(
    "TransitionTypeDef",
    {
        "RelativePosition": RelativePositionType,
        "Type": str,
        "DurationMillis": NotRequired[int],
        "RelativeProgram": NotRequired[str],
        "ScheduledStartTimeMillis": NotRequired[int],
    },
)
SegmentationDescriptorTypeDef = TypedDict(
    "SegmentationDescriptorTypeDef",
    {
        "SegmentNum": NotRequired[int],
        "SegmentationEventId": NotRequired[int],
        "SegmentationTypeId": NotRequired[int],
        "SegmentationUpid": NotRequired[str],
        "SegmentationUpidType": NotRequired[int],
        "SegmentsExpected": NotRequired[int],
        "SubSegmentNum": NotRequired[int],
        "SubSegmentsExpected": NotRequired[int],
    },
)
StartChannelRequestRequestTypeDef = TypedDict(
    "StartChannelRequestRequestTypeDef",
    {
        "ChannelName": str,
    },
)
StopChannelRequestRequestTypeDef = TypedDict(
    "StopChannelRequestRequestTypeDef",
    {
        "ChannelName": str,
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
UpdateProgramTransitionTypeDef = TypedDict(
    "UpdateProgramTransitionTypeDef",
    {
        "DurationMillis": NotRequired[int],
        "ScheduledStartTimeMillis": NotRequired[int],
    },
)
AccessConfigurationTypeDef = TypedDict(
    "AccessConfigurationTypeDef",
    {
        "AccessType": NotRequired[AccessTypeType],
        "SecretsManagerAccessTokenConfiguration": NotRequired[
            SecretsManagerAccessTokenConfigurationTypeDef
        ],
    },
)
ManifestProcessingRulesTypeDef = TypedDict(
    "ManifestProcessingRulesTypeDef",
    {
        "AdMarkerPassthrough": NotRequired[AdMarkerPassthroughTypeDef],
    },
)
PrefetchConsumptionPaginatorTypeDef = TypedDict(
    "PrefetchConsumptionPaginatorTypeDef",
    {
        "EndTime": datetime,
        "AvailMatchingCriteria": NotRequired[List[AvailMatchingCriteriaTypeDef]],
        "StartTime": NotRequired[datetime],
    },
)
ConfigureLogsForChannelResponseTypeDef = TypedDict(
    "ConfigureLogsForChannelResponseTypeDef",
    {
        "ChannelName": str,
        "LogTypes": List[Literal["AS_RUN"]],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ConfigureLogsForPlaybackConfigurationResponseTypeDef = TypedDict(
    "ConfigureLogsForPlaybackConfigurationResponseTypeDef",
    {
        "PercentEnabled": int,
        "PlaybackConfigurationName": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetChannelPolicyResponseTypeDef = TypedDict(
    "GetChannelPolicyResponseTypeDef",
    {
        "Policy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAlertsResponseTypeDef = TypedDict(
    "ListAlertsResponseTypeDef",
    {
        "Items": List[AlertTypeDef],
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
CreateLiveSourceRequestRequestTypeDef = TypedDict(
    "CreateLiveSourceRequestRequestTypeDef",
    {
        "HttpPackageConfigurations": Sequence[HttpPackageConfigurationTypeDef],
        "LiveSourceName": str,
        "SourceLocationName": str,
        "Tags": NotRequired[Mapping[str, str]],
    },
)
CreateLiveSourceResponseTypeDef = TypedDict(
    "CreateLiveSourceResponseTypeDef",
    {
        "Arn": str,
        "CreationTime": datetime,
        "HttpPackageConfigurations": List[HttpPackageConfigurationTypeDef],
        "LastModifiedTime": datetime,
        "LiveSourceName": str,
        "SourceLocationName": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateVodSourceRequestRequestTypeDef = TypedDict(
    "CreateVodSourceRequestRequestTypeDef",
    {
        "HttpPackageConfigurations": Sequence[HttpPackageConfigurationTypeDef],
        "SourceLocationName": str,
        "VodSourceName": str,
        "Tags": NotRequired[Mapping[str, str]],
    },
)
CreateVodSourceResponseTypeDef = TypedDict(
    "CreateVodSourceResponseTypeDef",
    {
        "Arn": str,
        "CreationTime": datetime,
        "HttpPackageConfigurations": List[HttpPackageConfigurationTypeDef],
        "LastModifiedTime": datetime,
        "SourceLocationName": str,
        "Tags": Dict[str, str],
        "VodSourceName": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeLiveSourceResponseTypeDef = TypedDict(
    "DescribeLiveSourceResponseTypeDef",
    {
        "Arn": str,
        "CreationTime": datetime,
        "HttpPackageConfigurations": List[HttpPackageConfigurationTypeDef],
        "LastModifiedTime": datetime,
        "LiveSourceName": str,
        "SourceLocationName": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeVodSourceResponseTypeDef = TypedDict(
    "DescribeVodSourceResponseTypeDef",
    {
        "AdBreakOpportunities": List[AdBreakOpportunityTypeDef],
        "Arn": str,
        "CreationTime": datetime,
        "HttpPackageConfigurations": List[HttpPackageConfigurationTypeDef],
        "LastModifiedTime": datetime,
        "SourceLocationName": str,
        "Tags": Dict[str, str],
        "VodSourceName": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
LiveSourceTypeDef = TypedDict(
    "LiveSourceTypeDef",
    {
        "Arn": str,
        "HttpPackageConfigurations": List[HttpPackageConfigurationTypeDef],
        "LiveSourceName": str,
        "SourceLocationName": str,
        "CreationTime": NotRequired[datetime],
        "LastModifiedTime": NotRequired[datetime],
        "Tags": NotRequired[Dict[str, str]],
    },
)
UpdateLiveSourceRequestRequestTypeDef = TypedDict(
    "UpdateLiveSourceRequestRequestTypeDef",
    {
        "HttpPackageConfigurations": Sequence[HttpPackageConfigurationTypeDef],
        "LiveSourceName": str,
        "SourceLocationName": str,
    },
)
UpdateLiveSourceResponseTypeDef = TypedDict(
    "UpdateLiveSourceResponseTypeDef",
    {
        "Arn": str,
        "CreationTime": datetime,
        "HttpPackageConfigurations": List[HttpPackageConfigurationTypeDef],
        "LastModifiedTime": datetime,
        "LiveSourceName": str,
        "SourceLocationName": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateVodSourceRequestRequestTypeDef = TypedDict(
    "UpdateVodSourceRequestRequestTypeDef",
    {
        "HttpPackageConfigurations": Sequence[HttpPackageConfigurationTypeDef],
        "SourceLocationName": str,
        "VodSourceName": str,
    },
)
UpdateVodSourceResponseTypeDef = TypedDict(
    "UpdateVodSourceResponseTypeDef",
    {
        "Arn": str,
        "CreationTime": datetime,
        "HttpPackageConfigurations": List[HttpPackageConfigurationTypeDef],
        "LastModifiedTime": datetime,
        "SourceLocationName": str,
        "Tags": Dict[str, str],
        "VodSourceName": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
VodSourceTypeDef = TypedDict(
    "VodSourceTypeDef",
    {
        "Arn": str,
        "HttpPackageConfigurations": List[HttpPackageConfigurationTypeDef],
        "SourceLocationName": str,
        "VodSourceName": str,
        "CreationTime": NotRequired[datetime],
        "LastModifiedTime": NotRequired[datetime],
        "Tags": NotRequired[Dict[str, str]],
    },
)
GetChannelScheduleRequestGetChannelSchedulePaginateTypeDef = TypedDict(
    "GetChannelScheduleRequestGetChannelSchedulePaginateTypeDef",
    {
        "ChannelName": str,
        "DurationMinutes": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListAlertsRequestListAlertsPaginateTypeDef = TypedDict(
    "ListAlertsRequestListAlertsPaginateTypeDef",
    {
        "ResourceArn": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListChannelsRequestListChannelsPaginateTypeDef = TypedDict(
    "ListChannelsRequestListChannelsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListLiveSourcesRequestListLiveSourcesPaginateTypeDef = TypedDict(
    "ListLiveSourcesRequestListLiveSourcesPaginateTypeDef",
    {
        "SourceLocationName": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListPlaybackConfigurationsRequestListPlaybackConfigurationsPaginateTypeDef = TypedDict(
    "ListPlaybackConfigurationsRequestListPlaybackConfigurationsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListPrefetchSchedulesRequestListPrefetchSchedulesPaginateTypeDef = TypedDict(
    "ListPrefetchSchedulesRequestListPrefetchSchedulesPaginateTypeDef",
    {
        "PlaybackConfigurationName": str,
        "StreamId": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListSourceLocationsRequestListSourceLocationsPaginateTypeDef = TypedDict(
    "ListSourceLocationsRequestListSourceLocationsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListVodSourcesRequestListVodSourcesPaginateTypeDef = TypedDict(
    "ListVodSourcesRequestListVodSourcesPaginateTypeDef",
    {
        "SourceLocationName": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ResponseOutputItemPaginatorTypeDef = TypedDict(
    "ResponseOutputItemPaginatorTypeDef",
    {
        "ManifestName": str,
        "PlaybackUrl": str,
        "SourceGroup": str,
        "DashPlaylistSettings": NotRequired[DashPlaylistSettingsTypeDef],
        "HlsPlaylistSettings": NotRequired[HlsPlaylistSettingsPaginatorTypeDef],
    },
)
RequestOutputItemTypeDef = TypedDict(
    "RequestOutputItemTypeDef",
    {
        "ManifestName": str,
        "SourceGroup": str,
        "DashPlaylistSettings": NotRequired[DashPlaylistSettingsTypeDef],
        "HlsPlaylistSettings": NotRequired[HlsPlaylistSettingsTypeDef],
    },
)
ResponseOutputItemTypeDef = TypedDict(
    "ResponseOutputItemTypeDef",
    {
        "ManifestName": str,
        "PlaybackUrl": str,
        "SourceGroup": str,
        "DashPlaylistSettings": NotRequired[DashPlaylistSettingsTypeDef],
        "HlsPlaylistSettings": NotRequired[HlsPlaylistSettingsTypeDef],
    },
)
PrefetchConsumptionTypeDef = TypedDict(
    "PrefetchConsumptionTypeDef",
    {
        "EndTime": TimestampTypeDef,
        "AvailMatchingCriteria": NotRequired[Sequence[AvailMatchingCriteriaTypeDef]],
        "StartTime": NotRequired[TimestampTypeDef],
    },
)
PrefetchRetrievalTypeDef = TypedDict(
    "PrefetchRetrievalTypeDef",
    {
        "EndTime": TimestampTypeDef,
        "DynamicVariables": NotRequired[Mapping[str, str]],
        "StartTime": NotRequired[TimestampTypeDef],
    },
)
ScheduleEntryTypeDef = TypedDict(
    "ScheduleEntryTypeDef",
    {
        "Arn": str,
        "ChannelName": str,
        "ProgramName": str,
        "SourceLocationName": str,
        "ApproximateDurationSeconds": NotRequired[int],
        "ApproximateStartTime": NotRequired[datetime],
        "LiveSourceName": NotRequired[str],
        "ScheduleAdBreaks": NotRequired[List[ScheduleAdBreakTypeDef]],
        "ScheduleEntryType": NotRequired[ScheduleEntryTypeType],
        "VodSourceName": NotRequired[str],
    },
)
ScheduleConfigurationTypeDef = TypedDict(
    "ScheduleConfigurationTypeDef",
    {
        "Transition": TransitionTypeDef,
        "ClipRange": NotRequired[ClipRangeTypeDef],
    },
)
TimeSignalMessageTypeDef = TypedDict(
    "TimeSignalMessageTypeDef",
    {
        "SegmentationDescriptors": NotRequired[Sequence[SegmentationDescriptorTypeDef]],
    },
)
UpdateProgramScheduleConfigurationTypeDef = TypedDict(
    "UpdateProgramScheduleConfigurationTypeDef",
    {
        "ClipRange": NotRequired[ClipRangeTypeDef],
        "Transition": NotRequired[UpdateProgramTransitionTypeDef],
    },
)
CreateSourceLocationRequestRequestTypeDef = TypedDict(
    "CreateSourceLocationRequestRequestTypeDef",
    {
        "HttpConfiguration": HttpConfigurationTypeDef,
        "SourceLocationName": str,
        "AccessConfiguration": NotRequired[AccessConfigurationTypeDef],
        "DefaultSegmentDeliveryConfiguration": NotRequired[
            DefaultSegmentDeliveryConfigurationTypeDef
        ],
        "SegmentDeliveryConfigurations": NotRequired[Sequence[SegmentDeliveryConfigurationTypeDef]],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
CreateSourceLocationResponseTypeDef = TypedDict(
    "CreateSourceLocationResponseTypeDef",
    {
        "AccessConfiguration": AccessConfigurationTypeDef,
        "Arn": str,
        "CreationTime": datetime,
        "DefaultSegmentDeliveryConfiguration": DefaultSegmentDeliveryConfigurationTypeDef,
        "HttpConfiguration": HttpConfigurationTypeDef,
        "LastModifiedTime": datetime,
        "SegmentDeliveryConfigurations": List[SegmentDeliveryConfigurationTypeDef],
        "SourceLocationName": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeSourceLocationResponseTypeDef = TypedDict(
    "DescribeSourceLocationResponseTypeDef",
    {
        "AccessConfiguration": AccessConfigurationTypeDef,
        "Arn": str,
        "CreationTime": datetime,
        "DefaultSegmentDeliveryConfiguration": DefaultSegmentDeliveryConfigurationTypeDef,
        "HttpConfiguration": HttpConfigurationTypeDef,
        "LastModifiedTime": datetime,
        "SegmentDeliveryConfigurations": List[SegmentDeliveryConfigurationTypeDef],
        "SourceLocationName": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SourceLocationTypeDef = TypedDict(
    "SourceLocationTypeDef",
    {
        "Arn": str,
        "HttpConfiguration": HttpConfigurationTypeDef,
        "SourceLocationName": str,
        "AccessConfiguration": NotRequired[AccessConfigurationTypeDef],
        "CreationTime": NotRequired[datetime],
        "DefaultSegmentDeliveryConfiguration": NotRequired[
            DefaultSegmentDeliveryConfigurationTypeDef
        ],
        "LastModifiedTime": NotRequired[datetime],
        "SegmentDeliveryConfigurations": NotRequired[List[SegmentDeliveryConfigurationTypeDef]],
        "Tags": NotRequired[Dict[str, str]],
    },
)
UpdateSourceLocationRequestRequestTypeDef = TypedDict(
    "UpdateSourceLocationRequestRequestTypeDef",
    {
        "HttpConfiguration": HttpConfigurationTypeDef,
        "SourceLocationName": str,
        "AccessConfiguration": NotRequired[AccessConfigurationTypeDef],
        "DefaultSegmentDeliveryConfiguration": NotRequired[
            DefaultSegmentDeliveryConfigurationTypeDef
        ],
        "SegmentDeliveryConfigurations": NotRequired[Sequence[SegmentDeliveryConfigurationTypeDef]],
    },
)
UpdateSourceLocationResponseTypeDef = TypedDict(
    "UpdateSourceLocationResponseTypeDef",
    {
        "AccessConfiguration": AccessConfigurationTypeDef,
        "Arn": str,
        "CreationTime": datetime,
        "DefaultSegmentDeliveryConfiguration": DefaultSegmentDeliveryConfigurationTypeDef,
        "HttpConfiguration": HttpConfigurationTypeDef,
        "LastModifiedTime": datetime,
        "SegmentDeliveryConfigurations": List[SegmentDeliveryConfigurationTypeDef],
        "SourceLocationName": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetPlaybackConfigurationResponseTypeDef = TypedDict(
    "GetPlaybackConfigurationResponseTypeDef",
    {
        "AdDecisionServerUrl": str,
        "AvailSuppression": AvailSuppressionTypeDef,
        "Bumper": BumperTypeDef,
        "CdnConfiguration": CdnConfigurationTypeDef,
        "ConfigurationAliases": Dict[str, Dict[str, str]],
        "DashConfiguration": DashConfigurationTypeDef,
        "HlsConfiguration": HlsConfigurationTypeDef,
        "LivePreRollConfiguration": LivePreRollConfigurationTypeDef,
        "LogConfiguration": LogConfigurationTypeDef,
        "ManifestProcessingRules": ManifestProcessingRulesTypeDef,
        "Name": str,
        "PersonalizationThresholdSeconds": int,
        "PlaybackConfigurationArn": str,
        "PlaybackEndpointPrefix": str,
        "SessionInitializationEndpointPrefix": str,
        "SlateAdUrl": str,
        "Tags": Dict[str, str],
        "TranscodeProfileName": str,
        "VideoContentSourceUrl": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PlaybackConfigurationTypeDef = TypedDict(
    "PlaybackConfigurationTypeDef",
    {
        "AdDecisionServerUrl": NotRequired[str],
        "AvailSuppression": NotRequired[AvailSuppressionTypeDef],
        "Bumper": NotRequired[BumperTypeDef],
        "CdnConfiguration": NotRequired[CdnConfigurationTypeDef],
        "ConfigurationAliases": NotRequired[Dict[str, Dict[str, str]]],
        "DashConfiguration": NotRequired[DashConfigurationTypeDef],
        "HlsConfiguration": NotRequired[HlsConfigurationTypeDef],
        "LivePreRollConfiguration": NotRequired[LivePreRollConfigurationTypeDef],
        "LogConfiguration": NotRequired[LogConfigurationTypeDef],
        "ManifestProcessingRules": NotRequired[ManifestProcessingRulesTypeDef],
        "Name": NotRequired[str],
        "PersonalizationThresholdSeconds": NotRequired[int],
        "PlaybackConfigurationArn": NotRequired[str],
        "PlaybackEndpointPrefix": NotRequired[str],
        "SessionInitializationEndpointPrefix": NotRequired[str],
        "SlateAdUrl": NotRequired[str],
        "Tags": NotRequired[Dict[str, str]],
        "TranscodeProfileName": NotRequired[str],
        "VideoContentSourceUrl": NotRequired[str],
    },
)
PutPlaybackConfigurationRequestRequestTypeDef = TypedDict(
    "PutPlaybackConfigurationRequestRequestTypeDef",
    {
        "Name": str,
        "AdDecisionServerUrl": NotRequired[str],
        "AvailSuppression": NotRequired[AvailSuppressionTypeDef],
        "Bumper": NotRequired[BumperTypeDef],
        "CdnConfiguration": NotRequired[CdnConfigurationTypeDef],
        "ConfigurationAliases": NotRequired[Mapping[str, Mapping[str, str]]],
        "DashConfiguration": NotRequired[DashConfigurationForPutTypeDef],
        "LivePreRollConfiguration": NotRequired[LivePreRollConfigurationTypeDef],
        "ManifestProcessingRules": NotRequired[ManifestProcessingRulesTypeDef],
        "PersonalizationThresholdSeconds": NotRequired[int],
        "SlateAdUrl": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
        "TranscodeProfileName": NotRequired[str],
        "VideoContentSourceUrl": NotRequired[str],
    },
)
PutPlaybackConfigurationResponseTypeDef = TypedDict(
    "PutPlaybackConfigurationResponseTypeDef",
    {
        "AdDecisionServerUrl": str,
        "AvailSuppression": AvailSuppressionTypeDef,
        "Bumper": BumperTypeDef,
        "CdnConfiguration": CdnConfigurationTypeDef,
        "ConfigurationAliases": Dict[str, Dict[str, str]],
        "DashConfiguration": DashConfigurationTypeDef,
        "HlsConfiguration": HlsConfigurationTypeDef,
        "LivePreRollConfiguration": LivePreRollConfigurationTypeDef,
        "LogConfiguration": LogConfigurationTypeDef,
        "ManifestProcessingRules": ManifestProcessingRulesTypeDef,
        "Name": str,
        "PersonalizationThresholdSeconds": int,
        "PlaybackConfigurationArn": str,
        "PlaybackEndpointPrefix": str,
        "SessionInitializationEndpointPrefix": str,
        "SlateAdUrl": str,
        "Tags": Dict[str, str],
        "TranscodeProfileName": str,
        "VideoContentSourceUrl": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PrefetchSchedulePaginatorTypeDef = TypedDict(
    "PrefetchSchedulePaginatorTypeDef",
    {
        "Arn": str,
        "Consumption": PrefetchConsumptionPaginatorTypeDef,
        "Name": str,
        "PlaybackConfigurationName": str,
        "Retrieval": PrefetchRetrievalPaginatorTypeDef,
        "StreamId": NotRequired[str],
    },
)
ListLiveSourcesResponseTypeDef = TypedDict(
    "ListLiveSourcesResponseTypeDef",
    {
        "Items": List[LiveSourceTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListVodSourcesResponseTypeDef = TypedDict(
    "ListVodSourcesResponseTypeDef",
    {
        "Items": List[VodSourceTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ChannelPaginatorTypeDef = TypedDict(
    "ChannelPaginatorTypeDef",
    {
        "Arn": str,
        "ChannelName": str,
        "ChannelState": str,
        "LogConfiguration": LogConfigurationForChannelTypeDef,
        "Outputs": List[ResponseOutputItemPaginatorTypeDef],
        "PlaybackMode": str,
        "Tier": str,
        "CreationTime": NotRequired[datetime],
        "FillerSlate": NotRequired[SlateSourceTypeDef],
        "LastModifiedTime": NotRequired[datetime],
        "Tags": NotRequired[Dict[str, str]],
    },
)
CreateChannelRequestRequestTypeDef = TypedDict(
    "CreateChannelRequestRequestTypeDef",
    {
        "ChannelName": str,
        "Outputs": Sequence[RequestOutputItemTypeDef],
        "PlaybackMode": PlaybackModeType,
        "FillerSlate": NotRequired[SlateSourceTypeDef],
        "Tags": NotRequired[Mapping[str, str]],
        "Tier": NotRequired[TierType],
        "TimeShiftConfiguration": NotRequired[TimeShiftConfigurationTypeDef],
    },
)
UpdateChannelRequestRequestTypeDef = TypedDict(
    "UpdateChannelRequestRequestTypeDef",
    {
        "ChannelName": str,
        "Outputs": Sequence[RequestOutputItemTypeDef],
        "FillerSlate": NotRequired[SlateSourceTypeDef],
        "TimeShiftConfiguration": NotRequired[TimeShiftConfigurationTypeDef],
    },
)
ChannelTypeDef = TypedDict(
    "ChannelTypeDef",
    {
        "Arn": str,
        "ChannelName": str,
        "ChannelState": str,
        "LogConfiguration": LogConfigurationForChannelTypeDef,
        "Outputs": List[ResponseOutputItemTypeDef],
        "PlaybackMode": str,
        "Tier": str,
        "CreationTime": NotRequired[datetime],
        "FillerSlate": NotRequired[SlateSourceTypeDef],
        "LastModifiedTime": NotRequired[datetime],
        "Tags": NotRequired[Dict[str, str]],
    },
)
CreateChannelResponseTypeDef = TypedDict(
    "CreateChannelResponseTypeDef",
    {
        "Arn": str,
        "ChannelName": str,
        "ChannelState": ChannelStateType,
        "CreationTime": datetime,
        "FillerSlate": SlateSourceTypeDef,
        "LastModifiedTime": datetime,
        "Outputs": List[ResponseOutputItemTypeDef],
        "PlaybackMode": str,
        "Tags": Dict[str, str],
        "Tier": str,
        "TimeShiftConfiguration": TimeShiftConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeChannelResponseTypeDef = TypedDict(
    "DescribeChannelResponseTypeDef",
    {
        "Arn": str,
        "ChannelName": str,
        "ChannelState": ChannelStateType,
        "CreationTime": datetime,
        "FillerSlate": SlateSourceTypeDef,
        "LastModifiedTime": datetime,
        "LogConfiguration": LogConfigurationForChannelTypeDef,
        "Outputs": List[ResponseOutputItemTypeDef],
        "PlaybackMode": str,
        "Tags": Dict[str, str],
        "Tier": str,
        "TimeShiftConfiguration": TimeShiftConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateChannelResponseTypeDef = TypedDict(
    "UpdateChannelResponseTypeDef",
    {
        "Arn": str,
        "ChannelName": str,
        "ChannelState": ChannelStateType,
        "CreationTime": datetime,
        "FillerSlate": SlateSourceTypeDef,
        "LastModifiedTime": datetime,
        "Outputs": List[ResponseOutputItemTypeDef],
        "PlaybackMode": str,
        "Tags": Dict[str, str],
        "Tier": str,
        "TimeShiftConfiguration": TimeShiftConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreatePrefetchScheduleRequestRequestTypeDef = TypedDict(
    "CreatePrefetchScheduleRequestRequestTypeDef",
    {
        "Consumption": PrefetchConsumptionTypeDef,
        "Name": str,
        "PlaybackConfigurationName": str,
        "Retrieval": PrefetchRetrievalTypeDef,
        "StreamId": NotRequired[str],
    },
)
CreatePrefetchScheduleResponseTypeDef = TypedDict(
    "CreatePrefetchScheduleResponseTypeDef",
    {
        "Arn": str,
        "Consumption": PrefetchConsumptionTypeDef,
        "Name": str,
        "PlaybackConfigurationName": str,
        "Retrieval": PrefetchRetrievalTypeDef,
        "StreamId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetPrefetchScheduleResponseTypeDef = TypedDict(
    "GetPrefetchScheduleResponseTypeDef",
    {
        "Arn": str,
        "Consumption": PrefetchConsumptionTypeDef,
        "Name": str,
        "PlaybackConfigurationName": str,
        "Retrieval": PrefetchRetrievalTypeDef,
        "StreamId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PrefetchScheduleTypeDef = TypedDict(
    "PrefetchScheduleTypeDef",
    {
        "Arn": str,
        "Consumption": PrefetchConsumptionTypeDef,
        "Name": str,
        "PlaybackConfigurationName": str,
        "Retrieval": PrefetchRetrievalTypeDef,
        "StreamId": NotRequired[str],
    },
)
GetChannelScheduleResponseTypeDef = TypedDict(
    "GetChannelScheduleResponseTypeDef",
    {
        "Items": List[ScheduleEntryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AdBreakTypeDef = TypedDict(
    "AdBreakTypeDef",
    {
        "AdBreakMetadata": NotRequired[Sequence[KeyValuePairTypeDef]],
        "MessageType": NotRequired[MessageTypeType],
        "OffsetMillis": NotRequired[int],
        "Slate": NotRequired[SlateSourceTypeDef],
        "SpliceInsertMessage": NotRequired[SpliceInsertMessageTypeDef],
        "TimeSignalMessage": NotRequired[TimeSignalMessageTypeDef],
    },
)
ListSourceLocationsResponseTypeDef = TypedDict(
    "ListSourceLocationsResponseTypeDef",
    {
        "Items": List[SourceLocationTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListPlaybackConfigurationsResponseTypeDef = TypedDict(
    "ListPlaybackConfigurationsResponseTypeDef",
    {
        "Items": List[PlaybackConfigurationTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListPrefetchSchedulesResponsePaginatorTypeDef = TypedDict(
    "ListPrefetchSchedulesResponsePaginatorTypeDef",
    {
        "Items": List[PrefetchSchedulePaginatorTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListChannelsResponsePaginatorTypeDef = TypedDict(
    "ListChannelsResponsePaginatorTypeDef",
    {
        "Items": List[ChannelPaginatorTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListChannelsResponseTypeDef = TypedDict(
    "ListChannelsResponseTypeDef",
    {
        "Items": List[ChannelTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListPrefetchSchedulesResponseTypeDef = TypedDict(
    "ListPrefetchSchedulesResponseTypeDef",
    {
        "Items": List[PrefetchScheduleTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateProgramRequestRequestTypeDef = TypedDict(
    "CreateProgramRequestRequestTypeDef",
    {
        "ChannelName": str,
        "ProgramName": str,
        "ScheduleConfiguration": ScheduleConfigurationTypeDef,
        "SourceLocationName": str,
        "AdBreaks": NotRequired[Sequence[AdBreakTypeDef]],
        "LiveSourceName": NotRequired[str],
        "VodSourceName": NotRequired[str],
    },
)
CreateProgramResponseTypeDef = TypedDict(
    "CreateProgramResponseTypeDef",
    {
        "AdBreaks": List[AdBreakTypeDef],
        "Arn": str,
        "ChannelName": str,
        "ClipRange": ClipRangeTypeDef,
        "CreationTime": datetime,
        "DurationMillis": int,
        "LiveSourceName": str,
        "ProgramName": str,
        "ScheduledStartTime": datetime,
        "SourceLocationName": str,
        "VodSourceName": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeProgramResponseTypeDef = TypedDict(
    "DescribeProgramResponseTypeDef",
    {
        "AdBreaks": List[AdBreakTypeDef],
        "Arn": str,
        "ChannelName": str,
        "ClipRange": ClipRangeTypeDef,
        "CreationTime": datetime,
        "DurationMillis": int,
        "LiveSourceName": str,
        "ProgramName": str,
        "ScheduledStartTime": datetime,
        "SourceLocationName": str,
        "VodSourceName": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateProgramRequestRequestTypeDef = TypedDict(
    "UpdateProgramRequestRequestTypeDef",
    {
        "ChannelName": str,
        "ProgramName": str,
        "ScheduleConfiguration": UpdateProgramScheduleConfigurationTypeDef,
        "AdBreaks": NotRequired[Sequence[AdBreakTypeDef]],
    },
)
UpdateProgramResponseTypeDef = TypedDict(
    "UpdateProgramResponseTypeDef",
    {
        "AdBreaks": List[AdBreakTypeDef],
        "Arn": str,
        "ChannelName": str,
        "ClipRange": ClipRangeTypeDef,
        "CreationTime": datetime,
        "DurationMillis": int,
        "LiveSourceName": str,
        "ProgramName": str,
        "ScheduledStartTime": datetime,
        "SourceLocationName": str,
        "VodSourceName": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
