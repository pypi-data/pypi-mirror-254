"""
Type annotations for codeguruprofiler service type definitions.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeguruprofiler/type_defs/)

Usage::

    ```python
    from types_aiobotocore_codeguruprofiler.type_defs import ChannelTypeDef

    data: ChannelTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Mapping, Sequence, Union

from aiobotocore.response import StreamingBody

from .literals import (
    AgentParameterFieldType,
    AggregationPeriodType,
    ComputePlatformType,
    FeedbackTypeType,
    MetadataFieldType,
    OrderByType,
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
    "ChannelTypeDef",
    "ResponseMetadataTypeDef",
    "AgentConfigurationTypeDef",
    "AgentOrchestrationConfigTypeDef",
    "AggregatedProfileTimeTypeDef",
    "UserFeedbackTypeDef",
    "MetricTypeDef",
    "FrameMetricTypeDef",
    "TimestampTypeDef",
    "TimestampStructureTypeDef",
    "BlobTypeDef",
    "ConfigureAgentRequestRequestTypeDef",
    "DeleteProfilingGroupRequestRequestTypeDef",
    "DescribeProfilingGroupRequestRequestTypeDef",
    "FindingsReportSummaryTypeDef",
    "GetFindingsReportAccountSummaryRequestRequestTypeDef",
    "GetNotificationConfigurationRequestRequestTypeDef",
    "GetPolicyRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "ProfileTimeTypeDef",
    "ListProfilingGroupsRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "MatchTypeDef",
    "PatternTypeDef",
    "PutPermissionRequestRequestTypeDef",
    "RemoveNotificationChannelRequestRequestTypeDef",
    "RemovePermissionRequestRequestTypeDef",
    "SubmitFeedbackRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "AddNotificationChannelsRequestRequestTypeDef",
    "NotificationConfigurationTypeDef",
    "GetPolicyResponseTypeDef",
    "GetProfileResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PutPermissionResponseTypeDef",
    "RemovePermissionResponseTypeDef",
    "ConfigureAgentResponseTypeDef",
    "CreateProfilingGroupRequestRequestTypeDef",
    "UpdateProfilingGroupRequestRequestTypeDef",
    "ProfilingStatusTypeDef",
    "AnomalyInstanceTypeDef",
    "FrameMetricDatumTypeDef",
    "BatchGetFrameMetricDataRequestRequestTypeDef",
    "GetProfileRequestRequestTypeDef",
    "GetRecommendationsRequestRequestTypeDef",
    "ListFindingsReportsRequestRequestTypeDef",
    "ListProfileTimesRequestRequestTypeDef",
    "PostAgentProfileRequestRequestTypeDef",
    "GetFindingsReportAccountSummaryResponseTypeDef",
    "ListFindingsReportsResponseTypeDef",
    "ListProfileTimesRequestListProfileTimesPaginateTypeDef",
    "ListProfileTimesResponseTypeDef",
    "RecommendationTypeDef",
    "AddNotificationChannelsResponseTypeDef",
    "GetNotificationConfigurationResponseTypeDef",
    "RemoveNotificationChannelResponseTypeDef",
    "ProfilingGroupDescriptionTypeDef",
    "AnomalyTypeDef",
    "BatchGetFrameMetricDataResponseTypeDef",
    "CreateProfilingGroupResponseTypeDef",
    "DescribeProfilingGroupResponseTypeDef",
    "ListProfilingGroupsResponseTypeDef",
    "UpdateProfilingGroupResponseTypeDef",
    "GetRecommendationsResponseTypeDef",
)

ChannelTypeDef = TypedDict(
    "ChannelTypeDef",
    {
        "eventPublishers": Sequence[Literal["AnomalyDetection"]],
        "uri": str,
        "id": NotRequired[str],
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
AgentConfigurationTypeDef = TypedDict(
    "AgentConfigurationTypeDef",
    {
        "periodInSeconds": int,
        "shouldProfile": bool,
        "agentParameters": NotRequired[Dict[AgentParameterFieldType, str]],
    },
)
AgentOrchestrationConfigTypeDef = TypedDict(
    "AgentOrchestrationConfigTypeDef",
    {
        "profilingEnabled": bool,
    },
)
AggregatedProfileTimeTypeDef = TypedDict(
    "AggregatedProfileTimeTypeDef",
    {
        "period": NotRequired[AggregationPeriodType],
        "start": NotRequired[datetime],
    },
)
UserFeedbackTypeDef = TypedDict(
    "UserFeedbackTypeDef",
    {
        "type": FeedbackTypeType,
    },
)
MetricTypeDef = TypedDict(
    "MetricTypeDef",
    {
        "frameName": str,
        "threadStates": List[str],
        "type": Literal["AggregatedRelativeTotalTime"],
    },
)
FrameMetricTypeDef = TypedDict(
    "FrameMetricTypeDef",
    {
        "frameName": str,
        "threadStates": Sequence[str],
        "type": Literal["AggregatedRelativeTotalTime"],
    },
)
TimestampTypeDef = Union[datetime, str]
TimestampStructureTypeDef = TypedDict(
    "TimestampStructureTypeDef",
    {
        "value": datetime,
    },
)
BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]
ConfigureAgentRequestRequestTypeDef = TypedDict(
    "ConfigureAgentRequestRequestTypeDef",
    {
        "profilingGroupName": str,
        "fleetInstanceId": NotRequired[str],
        "metadata": NotRequired[Mapping[MetadataFieldType, str]],
    },
)
DeleteProfilingGroupRequestRequestTypeDef = TypedDict(
    "DeleteProfilingGroupRequestRequestTypeDef",
    {
        "profilingGroupName": str,
    },
)
DescribeProfilingGroupRequestRequestTypeDef = TypedDict(
    "DescribeProfilingGroupRequestRequestTypeDef",
    {
        "profilingGroupName": str,
    },
)
FindingsReportSummaryTypeDef = TypedDict(
    "FindingsReportSummaryTypeDef",
    {
        "id": NotRequired[str],
        "profileEndTime": NotRequired[datetime],
        "profileStartTime": NotRequired[datetime],
        "profilingGroupName": NotRequired[str],
        "totalNumberOfFindings": NotRequired[int],
    },
)
GetFindingsReportAccountSummaryRequestRequestTypeDef = TypedDict(
    "GetFindingsReportAccountSummaryRequestRequestTypeDef",
    {
        "dailyReportsOnly": NotRequired[bool],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
GetNotificationConfigurationRequestRequestTypeDef = TypedDict(
    "GetNotificationConfigurationRequestRequestTypeDef",
    {
        "profilingGroupName": str,
    },
)
GetPolicyRequestRequestTypeDef = TypedDict(
    "GetPolicyRequestRequestTypeDef",
    {
        "profilingGroupName": str,
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
ProfileTimeTypeDef = TypedDict(
    "ProfileTimeTypeDef",
    {
        "start": NotRequired[datetime],
    },
)
ListProfilingGroupsRequestRequestTypeDef = TypedDict(
    "ListProfilingGroupsRequestRequestTypeDef",
    {
        "includeDescription": NotRequired[bool],
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
MatchTypeDef = TypedDict(
    "MatchTypeDef",
    {
        "frameAddress": NotRequired[str],
        "targetFramesIndex": NotRequired[int],
        "thresholdBreachValue": NotRequired[float],
    },
)
PatternTypeDef = TypedDict(
    "PatternTypeDef",
    {
        "countersToAggregate": NotRequired[List[str]],
        "description": NotRequired[str],
        "id": NotRequired[str],
        "name": NotRequired[str],
        "resolutionSteps": NotRequired[str],
        "targetFrames": NotRequired[List[List[str]]],
        "thresholdPercent": NotRequired[float],
    },
)
PutPermissionRequestRequestTypeDef = TypedDict(
    "PutPermissionRequestRequestTypeDef",
    {
        "actionGroup": Literal["agentPermissions"],
        "principals": Sequence[str],
        "profilingGroupName": str,
        "revisionId": NotRequired[str],
    },
)
RemoveNotificationChannelRequestRequestTypeDef = TypedDict(
    "RemoveNotificationChannelRequestRequestTypeDef",
    {
        "channelId": str,
        "profilingGroupName": str,
    },
)
RemovePermissionRequestRequestTypeDef = TypedDict(
    "RemovePermissionRequestRequestTypeDef",
    {
        "actionGroup": Literal["agentPermissions"],
        "profilingGroupName": str,
        "revisionId": str,
    },
)
SubmitFeedbackRequestRequestTypeDef = TypedDict(
    "SubmitFeedbackRequestRequestTypeDef",
    {
        "anomalyInstanceId": str,
        "profilingGroupName": str,
        "type": FeedbackTypeType,
        "comment": NotRequired[str],
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
AddNotificationChannelsRequestRequestTypeDef = TypedDict(
    "AddNotificationChannelsRequestRequestTypeDef",
    {
        "channels": Sequence[ChannelTypeDef],
        "profilingGroupName": str,
    },
)
NotificationConfigurationTypeDef = TypedDict(
    "NotificationConfigurationTypeDef",
    {
        "channels": NotRequired[List[ChannelTypeDef]],
    },
)
GetPolicyResponseTypeDef = TypedDict(
    "GetPolicyResponseTypeDef",
    {
        "policy": str,
        "revisionId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetProfileResponseTypeDef = TypedDict(
    "GetProfileResponseTypeDef",
    {
        "contentEncoding": str,
        "contentType": str,
        "profile": StreamingBody,
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
PutPermissionResponseTypeDef = TypedDict(
    "PutPermissionResponseTypeDef",
    {
        "policy": str,
        "revisionId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RemovePermissionResponseTypeDef = TypedDict(
    "RemovePermissionResponseTypeDef",
    {
        "policy": str,
        "revisionId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ConfigureAgentResponseTypeDef = TypedDict(
    "ConfigureAgentResponseTypeDef",
    {
        "configuration": AgentConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateProfilingGroupRequestRequestTypeDef = TypedDict(
    "CreateProfilingGroupRequestRequestTypeDef",
    {
        "clientToken": str,
        "profilingGroupName": str,
        "agentOrchestrationConfig": NotRequired[AgentOrchestrationConfigTypeDef],
        "computePlatform": NotRequired[ComputePlatformType],
        "tags": NotRequired[Mapping[str, str]],
    },
)
UpdateProfilingGroupRequestRequestTypeDef = TypedDict(
    "UpdateProfilingGroupRequestRequestTypeDef",
    {
        "agentOrchestrationConfig": AgentOrchestrationConfigTypeDef,
        "profilingGroupName": str,
    },
)
ProfilingStatusTypeDef = TypedDict(
    "ProfilingStatusTypeDef",
    {
        "latestAgentOrchestratedAt": NotRequired[datetime],
        "latestAgentProfileReportedAt": NotRequired[datetime],
        "latestAggregatedProfile": NotRequired[AggregatedProfileTimeTypeDef],
    },
)
AnomalyInstanceTypeDef = TypedDict(
    "AnomalyInstanceTypeDef",
    {
        "id": str,
        "startTime": datetime,
        "endTime": NotRequired[datetime],
        "userFeedback": NotRequired[UserFeedbackTypeDef],
    },
)
FrameMetricDatumTypeDef = TypedDict(
    "FrameMetricDatumTypeDef",
    {
        "frameMetric": FrameMetricTypeDef,
        "values": List[float],
    },
)
BatchGetFrameMetricDataRequestRequestTypeDef = TypedDict(
    "BatchGetFrameMetricDataRequestRequestTypeDef",
    {
        "profilingGroupName": str,
        "endTime": NotRequired[TimestampTypeDef],
        "frameMetrics": NotRequired[Sequence[FrameMetricTypeDef]],
        "period": NotRequired[str],
        "startTime": NotRequired[TimestampTypeDef],
        "targetResolution": NotRequired[AggregationPeriodType],
    },
)
GetProfileRequestRequestTypeDef = TypedDict(
    "GetProfileRequestRequestTypeDef",
    {
        "profilingGroupName": str,
        "accept": NotRequired[str],
        "endTime": NotRequired[TimestampTypeDef],
        "maxDepth": NotRequired[int],
        "period": NotRequired[str],
        "startTime": NotRequired[TimestampTypeDef],
    },
)
GetRecommendationsRequestRequestTypeDef = TypedDict(
    "GetRecommendationsRequestRequestTypeDef",
    {
        "endTime": TimestampTypeDef,
        "profilingGroupName": str,
        "startTime": TimestampTypeDef,
        "locale": NotRequired[str],
    },
)
ListFindingsReportsRequestRequestTypeDef = TypedDict(
    "ListFindingsReportsRequestRequestTypeDef",
    {
        "endTime": TimestampTypeDef,
        "profilingGroupName": str,
        "startTime": TimestampTypeDef,
        "dailyReportsOnly": NotRequired[bool],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListProfileTimesRequestRequestTypeDef = TypedDict(
    "ListProfileTimesRequestRequestTypeDef",
    {
        "endTime": TimestampTypeDef,
        "period": AggregationPeriodType,
        "profilingGroupName": str,
        "startTime": TimestampTypeDef,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "orderBy": NotRequired[OrderByType],
    },
)
PostAgentProfileRequestRequestTypeDef = TypedDict(
    "PostAgentProfileRequestRequestTypeDef",
    {
        "agentProfile": BlobTypeDef,
        "contentType": str,
        "profilingGroupName": str,
        "profileToken": NotRequired[str],
    },
)
GetFindingsReportAccountSummaryResponseTypeDef = TypedDict(
    "GetFindingsReportAccountSummaryResponseTypeDef",
    {
        "nextToken": str,
        "reportSummaries": List[FindingsReportSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListFindingsReportsResponseTypeDef = TypedDict(
    "ListFindingsReportsResponseTypeDef",
    {
        "findingsReportSummaries": List[FindingsReportSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListProfileTimesRequestListProfileTimesPaginateTypeDef = TypedDict(
    "ListProfileTimesRequestListProfileTimesPaginateTypeDef",
    {
        "endTime": TimestampTypeDef,
        "period": AggregationPeriodType,
        "profilingGroupName": str,
        "startTime": TimestampTypeDef,
        "orderBy": NotRequired[OrderByType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListProfileTimesResponseTypeDef = TypedDict(
    "ListProfileTimesResponseTypeDef",
    {
        "nextToken": str,
        "profileTimes": List[ProfileTimeTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RecommendationTypeDef = TypedDict(
    "RecommendationTypeDef",
    {
        "allMatchesCount": int,
        "allMatchesSum": float,
        "endTime": datetime,
        "pattern": PatternTypeDef,
        "startTime": datetime,
        "topMatches": List[MatchTypeDef],
    },
)
AddNotificationChannelsResponseTypeDef = TypedDict(
    "AddNotificationChannelsResponseTypeDef",
    {
        "notificationConfiguration": NotificationConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetNotificationConfigurationResponseTypeDef = TypedDict(
    "GetNotificationConfigurationResponseTypeDef",
    {
        "notificationConfiguration": NotificationConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RemoveNotificationChannelResponseTypeDef = TypedDict(
    "RemoveNotificationChannelResponseTypeDef",
    {
        "notificationConfiguration": NotificationConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ProfilingGroupDescriptionTypeDef = TypedDict(
    "ProfilingGroupDescriptionTypeDef",
    {
        "agentOrchestrationConfig": NotRequired[AgentOrchestrationConfigTypeDef],
        "arn": NotRequired[str],
        "computePlatform": NotRequired[ComputePlatformType],
        "createdAt": NotRequired[datetime],
        "name": NotRequired[str],
        "profilingStatus": NotRequired[ProfilingStatusTypeDef],
        "tags": NotRequired[Dict[str, str]],
        "updatedAt": NotRequired[datetime],
    },
)
AnomalyTypeDef = TypedDict(
    "AnomalyTypeDef",
    {
        "instances": List[AnomalyInstanceTypeDef],
        "metric": MetricTypeDef,
        "reason": str,
    },
)
BatchGetFrameMetricDataResponseTypeDef = TypedDict(
    "BatchGetFrameMetricDataResponseTypeDef",
    {
        "endTime": datetime,
        "endTimes": List[TimestampStructureTypeDef],
        "frameMetricData": List[FrameMetricDatumTypeDef],
        "resolution": AggregationPeriodType,
        "startTime": datetime,
        "unprocessedEndTimes": Dict[str, List[TimestampStructureTypeDef]],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateProfilingGroupResponseTypeDef = TypedDict(
    "CreateProfilingGroupResponseTypeDef",
    {
        "profilingGroup": ProfilingGroupDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeProfilingGroupResponseTypeDef = TypedDict(
    "DescribeProfilingGroupResponseTypeDef",
    {
        "profilingGroup": ProfilingGroupDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListProfilingGroupsResponseTypeDef = TypedDict(
    "ListProfilingGroupsResponseTypeDef",
    {
        "nextToken": str,
        "profilingGroupNames": List[str],
        "profilingGroups": List[ProfilingGroupDescriptionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateProfilingGroupResponseTypeDef = TypedDict(
    "UpdateProfilingGroupResponseTypeDef",
    {
        "profilingGroup": ProfilingGroupDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetRecommendationsResponseTypeDef = TypedDict(
    "GetRecommendationsResponseTypeDef",
    {
        "anomalies": List[AnomalyTypeDef],
        "profileEndTime": datetime,
        "profileStartTime": datetime,
        "profilingGroupName": str,
        "recommendations": List[RecommendationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
