"""
Type annotations for devops-guru service type definitions.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_devops_guru/type_defs/)

Usage::

    ```python
    from types_aiobotocore_devops_guru.type_defs import AccountInsightHealthTypeDef

    data: AccountInsightHealthTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Sequence, Union

from .literals import (
    AnomalySeverityType,
    AnomalyStatusType,
    AnomalyTypeType,
    CloudWatchMetricDataStatusCodeType,
    CloudWatchMetricsStatType,
    CostEstimationServiceResourceStateType,
    CostEstimationStatusType,
    EventClassType,
    EventDataSourceType,
    EventSourceOptInStatusType,
    InsightFeedbackOptionType,
    InsightSeverityType,
    InsightStatusType,
    InsightTypeType,
    LocaleType,
    LogAnomalyTypeType,
    NotificationMessageTypeType,
    OptInStatusType,
    OrganizationResourceCollectionTypeType,
    ResourceCollectionTypeType,
    ResourcePermissionType,
    ResourceTypeFilterType,
    ServerSideEncryptionTypeType,
    ServiceNameType,
    UpdateResourceCollectionActionType,
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
    "AccountInsightHealthTypeDef",
    "ResponseMetadataTypeDef",
    "AmazonCodeGuruProfilerIntegrationTypeDef",
    "AnomalyReportedTimeRangeTypeDef",
    "AnomalyResourceTypeDef",
    "AnomalySourceMetadataTypeDef",
    "AnomalyTimeRangeTypeDef",
    "CloudFormationCollectionFilterTypeDef",
    "CloudFormationCollectionTypeDef",
    "CloudFormationCostEstimationResourceCollectionFilterTypeDef",
    "InsightHealthTypeDef",
    "TimestampMetricValuePairTypeDef",
    "CloudWatchMetricsDimensionTypeDef",
    "TagCostEstimationResourceCollectionFilterTypeDef",
    "CostEstimationTimeRangeTypeDef",
    "DeleteInsightRequestRequestTypeDef",
    "TimestampTypeDef",
    "DescribeAnomalyRequestRequestTypeDef",
    "DescribeFeedbackRequestRequestTypeDef",
    "InsightFeedbackTypeDef",
    "DescribeInsightRequestRequestTypeDef",
    "DescribeOrganizationHealthRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "DescribeOrganizationResourceCollectionHealthRequestRequestTypeDef",
    "DescribeResourceCollectionHealthRequestRequestTypeDef",
    "EventResourceTypeDef",
    "GetCostEstimationRequestRequestTypeDef",
    "ServiceResourceCostTypeDef",
    "GetResourceCollectionRequestRequestTypeDef",
    "InsightTimeRangeTypeDef",
    "KMSServerSideEncryptionIntegrationConfigTypeDef",
    "KMSServerSideEncryptionIntegrationTypeDef",
    "ServiceCollectionTypeDef",
    "ListAnomalousLogGroupsRequestRequestTypeDef",
    "ListInsightsOngoingStatusFilterTypeDef",
    "ListMonitoredResourcesFiltersTypeDef",
    "ListNotificationChannelsRequestRequestTypeDef",
    "ListRecommendationsRequestRequestTypeDef",
    "LogAnomalyClassTypeDef",
    "LogsAnomalyDetectionIntegrationConfigTypeDef",
    "LogsAnomalyDetectionIntegrationTypeDef",
    "NotificationFilterConfigPaginatorTypeDef",
    "SnsChannelConfigTypeDef",
    "NotificationFilterConfigTypeDef",
    "OpsCenterIntegrationConfigTypeDef",
    "OpsCenterIntegrationTypeDef",
    "PerformanceInsightsMetricDimensionGroupTypeDef",
    "PerformanceInsightsStatTypeDef",
    "PerformanceInsightsReferenceScalarTypeDef",
    "PredictionTimeRangeTypeDef",
    "RecommendationRelatedAnomalyResourceTypeDef",
    "RecommendationRelatedCloudWatchMetricsSourceDetailTypeDef",
    "RecommendationRelatedEventResourceTypeDef",
    "RemoveNotificationChannelRequestRequestTypeDef",
    "TagCollectionFilterTypeDef",
    "TagCollectionTypeDef",
    "ServiceInsightHealthTypeDef",
    "UpdateCloudFormationCollectionFilterTypeDef",
    "UpdateTagCollectionFilterTypeDef",
    "AccountHealthTypeDef",
    "AddNotificationChannelResponseTypeDef",
    "DescribeAccountHealthResponseTypeDef",
    "DescribeAccountOverviewResponseTypeDef",
    "DescribeOrganizationHealthResponseTypeDef",
    "DescribeOrganizationOverviewResponseTypeDef",
    "EventSourcesConfigTypeDef",
    "CloudFormationHealthTypeDef",
    "TagHealthTypeDef",
    "CloudWatchMetricsDataSummaryTypeDef",
    "CostEstimationResourceCollectionFilterTypeDef",
    "DescribeAccountOverviewRequestRequestTypeDef",
    "DescribeOrganizationOverviewRequestRequestTypeDef",
    "EndTimeRangeTypeDef",
    "EventTimeRangeTypeDef",
    "StartTimeRangeTypeDef",
    "DescribeFeedbackResponseTypeDef",
    "PutFeedbackRequestRequestTypeDef",
    "DescribeOrganizationResourceCollectionHealthRequestDescribeOrganizationResourceCollectionHealthPaginateTypeDef",
    "DescribeResourceCollectionHealthRequestDescribeResourceCollectionHealthPaginateTypeDef",
    "GetCostEstimationRequestGetCostEstimationPaginateTypeDef",
    "GetResourceCollectionRequestGetResourceCollectionPaginateTypeDef",
    "ListAnomalousLogGroupsRequestListAnomalousLogGroupsPaginateTypeDef",
    "ListNotificationChannelsRequestListNotificationChannelsPaginateTypeDef",
    "ListRecommendationsRequestListRecommendationsPaginateTypeDef",
    "ListAnomaliesForInsightFiltersTypeDef",
    "ListMonitoredResourcesRequestListMonitoredResourcesPaginateTypeDef",
    "ListMonitoredResourcesRequestRequestTypeDef",
    "LogAnomalyShowcaseTypeDef",
    "NotificationChannelConfigPaginatorTypeDef",
    "NotificationChannelConfigTypeDef",
    "UpdateServiceIntegrationConfigTypeDef",
    "ServiceIntegrationConfigTypeDef",
    "PerformanceInsightsMetricQueryTypeDef",
    "RecommendationRelatedAnomalySourceDetailTypeDef",
    "RecommendationRelatedEventTypeDef",
    "ResourceCollectionFilterTypeDef",
    "ResourceCollectionTypeDef",
    "ServiceHealthTypeDef",
    "UpdateResourceCollectionFilterTypeDef",
    "DescribeEventSourcesConfigResponseTypeDef",
    "UpdateEventSourcesConfigRequestRequestTypeDef",
    "CloudWatchMetricsDetailTypeDef",
    "GetCostEstimationResponseTypeDef",
    "StartCostEstimationRequestRequestTypeDef",
    "ListInsightsClosedStatusFilterTypeDef",
    "ListInsightsAnyStatusFilterTypeDef",
    "ListAnomaliesForInsightRequestListAnomaliesForInsightPaginateTypeDef",
    "ListAnomaliesForInsightRequestRequestTypeDef",
    "AnomalousLogGroupTypeDef",
    "NotificationChannelPaginatorTypeDef",
    "AddNotificationChannelRequestRequestTypeDef",
    "NotificationChannelTypeDef",
    "UpdateServiceIntegrationRequestRequestTypeDef",
    "DescribeServiceIntegrationResponseTypeDef",
    "PerformanceInsightsReferenceMetricTypeDef",
    "RecommendationRelatedAnomalyTypeDef",
    "GetResourceCollectionResponseTypeDef",
    "EventTypeDef",
    "ListEventsFiltersTypeDef",
    "MonitoredResourceIdentifierTypeDef",
    "ProactiveInsightSummaryTypeDef",
    "ProactiveInsightTypeDef",
    "ProactiveOrganizationInsightSummaryTypeDef",
    "ReactiveInsightSummaryTypeDef",
    "ReactiveInsightTypeDef",
    "ReactiveOrganizationInsightSummaryTypeDef",
    "SearchInsightsFiltersTypeDef",
    "SearchOrganizationInsightsFiltersTypeDef",
    "DescribeOrganizationResourceCollectionHealthResponseTypeDef",
    "DescribeResourceCollectionHealthResponseTypeDef",
    "UpdateResourceCollectionRequestRequestTypeDef",
    "ListInsightsStatusFilterTypeDef",
    "ListAnomalousLogGroupsResponseTypeDef",
    "ListNotificationChannelsResponsePaginatorTypeDef",
    "ListNotificationChannelsResponseTypeDef",
    "PerformanceInsightsReferenceComparisonValuesTypeDef",
    "RecommendationTypeDef",
    "ListEventsResponseTypeDef",
    "ListEventsRequestListEventsPaginateTypeDef",
    "ListEventsRequestRequestTypeDef",
    "ListMonitoredResourcesResponseTypeDef",
    "ListInsightsResponseTypeDef",
    "SearchInsightsResponseTypeDef",
    "SearchOrganizationInsightsResponseTypeDef",
    "DescribeInsightResponseTypeDef",
    "ListOrganizationInsightsResponseTypeDef",
    "SearchInsightsRequestRequestTypeDef",
    "SearchInsightsRequestSearchInsightsPaginateTypeDef",
    "SearchOrganizationInsightsRequestRequestTypeDef",
    "SearchOrganizationInsightsRequestSearchOrganizationInsightsPaginateTypeDef",
    "ListInsightsRequestListInsightsPaginateTypeDef",
    "ListInsightsRequestRequestTypeDef",
    "ListOrganizationInsightsRequestListOrganizationInsightsPaginateTypeDef",
    "ListOrganizationInsightsRequestRequestTypeDef",
    "PerformanceInsightsReferenceDataTypeDef",
    "ListRecommendationsResponseTypeDef",
    "PerformanceInsightsMetricsDetailTypeDef",
    "AnomalySourceDetailsTypeDef",
    "ProactiveAnomalySummaryTypeDef",
    "ProactiveAnomalyTypeDef",
    "ReactiveAnomalySummaryTypeDef",
    "ReactiveAnomalyTypeDef",
    "ListAnomaliesForInsightResponseTypeDef",
    "DescribeAnomalyResponseTypeDef",
)

AccountInsightHealthTypeDef = TypedDict(
    "AccountInsightHealthTypeDef",
    {
        "OpenProactiveInsights": NotRequired[int],
        "OpenReactiveInsights": NotRequired[int],
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
AmazonCodeGuruProfilerIntegrationTypeDef = TypedDict(
    "AmazonCodeGuruProfilerIntegrationTypeDef",
    {
        "Status": NotRequired[EventSourceOptInStatusType],
    },
)
AnomalyReportedTimeRangeTypeDef = TypedDict(
    "AnomalyReportedTimeRangeTypeDef",
    {
        "OpenTime": datetime,
        "CloseTime": NotRequired[datetime],
    },
)
AnomalyResourceTypeDef = TypedDict(
    "AnomalyResourceTypeDef",
    {
        "Name": NotRequired[str],
        "Type": NotRequired[str],
    },
)
AnomalySourceMetadataTypeDef = TypedDict(
    "AnomalySourceMetadataTypeDef",
    {
        "Source": NotRequired[str],
        "SourceResourceName": NotRequired[str],
        "SourceResourceType": NotRequired[str],
    },
)
AnomalyTimeRangeTypeDef = TypedDict(
    "AnomalyTimeRangeTypeDef",
    {
        "StartTime": datetime,
        "EndTime": NotRequired[datetime],
    },
)
CloudFormationCollectionFilterTypeDef = TypedDict(
    "CloudFormationCollectionFilterTypeDef",
    {
        "StackNames": NotRequired[List[str]],
    },
)
CloudFormationCollectionTypeDef = TypedDict(
    "CloudFormationCollectionTypeDef",
    {
        "StackNames": NotRequired[List[str]],
    },
)
CloudFormationCostEstimationResourceCollectionFilterTypeDef = TypedDict(
    "CloudFormationCostEstimationResourceCollectionFilterTypeDef",
    {
        "StackNames": NotRequired[List[str]],
    },
)
InsightHealthTypeDef = TypedDict(
    "InsightHealthTypeDef",
    {
        "OpenProactiveInsights": NotRequired[int],
        "OpenReactiveInsights": NotRequired[int],
        "MeanTimeToRecoverInMilliseconds": NotRequired[int],
    },
)
TimestampMetricValuePairTypeDef = TypedDict(
    "TimestampMetricValuePairTypeDef",
    {
        "Timestamp": NotRequired[datetime],
        "MetricValue": NotRequired[float],
    },
)
CloudWatchMetricsDimensionTypeDef = TypedDict(
    "CloudWatchMetricsDimensionTypeDef",
    {
        "Name": NotRequired[str],
        "Value": NotRequired[str],
    },
)
TagCostEstimationResourceCollectionFilterTypeDef = TypedDict(
    "TagCostEstimationResourceCollectionFilterTypeDef",
    {
        "AppBoundaryKey": str,
        "TagValues": List[str],
    },
)
CostEstimationTimeRangeTypeDef = TypedDict(
    "CostEstimationTimeRangeTypeDef",
    {
        "StartTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
    },
)
DeleteInsightRequestRequestTypeDef = TypedDict(
    "DeleteInsightRequestRequestTypeDef",
    {
        "Id": str,
    },
)
TimestampTypeDef = Union[datetime, str]
DescribeAnomalyRequestRequestTypeDef = TypedDict(
    "DescribeAnomalyRequestRequestTypeDef",
    {
        "Id": str,
        "AccountId": NotRequired[str],
    },
)
DescribeFeedbackRequestRequestTypeDef = TypedDict(
    "DescribeFeedbackRequestRequestTypeDef",
    {
        "InsightId": NotRequired[str],
    },
)
InsightFeedbackTypeDef = TypedDict(
    "InsightFeedbackTypeDef",
    {
        "Id": NotRequired[str],
        "Feedback": NotRequired[InsightFeedbackOptionType],
    },
)
DescribeInsightRequestRequestTypeDef = TypedDict(
    "DescribeInsightRequestRequestTypeDef",
    {
        "Id": str,
        "AccountId": NotRequired[str],
    },
)
DescribeOrganizationHealthRequestRequestTypeDef = TypedDict(
    "DescribeOrganizationHealthRequestRequestTypeDef",
    {
        "AccountIds": NotRequired[Sequence[str]],
        "OrganizationalUnitIds": NotRequired[Sequence[str]],
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
DescribeOrganizationResourceCollectionHealthRequestRequestTypeDef = TypedDict(
    "DescribeOrganizationResourceCollectionHealthRequestRequestTypeDef",
    {
        "OrganizationResourceCollectionType": OrganizationResourceCollectionTypeType,
        "AccountIds": NotRequired[Sequence[str]],
        "OrganizationalUnitIds": NotRequired[Sequence[str]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
DescribeResourceCollectionHealthRequestRequestTypeDef = TypedDict(
    "DescribeResourceCollectionHealthRequestRequestTypeDef",
    {
        "ResourceCollectionType": ResourceCollectionTypeType,
        "NextToken": NotRequired[str],
    },
)
EventResourceTypeDef = TypedDict(
    "EventResourceTypeDef",
    {
        "Type": NotRequired[str],
        "Name": NotRequired[str],
        "Arn": NotRequired[str],
    },
)
GetCostEstimationRequestRequestTypeDef = TypedDict(
    "GetCostEstimationRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
    },
)
ServiceResourceCostTypeDef = TypedDict(
    "ServiceResourceCostTypeDef",
    {
        "Type": NotRequired[str],
        "State": NotRequired[CostEstimationServiceResourceStateType],
        "Count": NotRequired[int],
        "UnitCost": NotRequired[float],
        "Cost": NotRequired[float],
    },
)
GetResourceCollectionRequestRequestTypeDef = TypedDict(
    "GetResourceCollectionRequestRequestTypeDef",
    {
        "ResourceCollectionType": ResourceCollectionTypeType,
        "NextToken": NotRequired[str],
    },
)
InsightTimeRangeTypeDef = TypedDict(
    "InsightTimeRangeTypeDef",
    {
        "StartTime": datetime,
        "EndTime": NotRequired[datetime],
    },
)
KMSServerSideEncryptionIntegrationConfigTypeDef = TypedDict(
    "KMSServerSideEncryptionIntegrationConfigTypeDef",
    {
        "KMSKeyId": NotRequired[str],
        "OptInStatus": NotRequired[OptInStatusType],
        "Type": NotRequired[ServerSideEncryptionTypeType],
    },
)
KMSServerSideEncryptionIntegrationTypeDef = TypedDict(
    "KMSServerSideEncryptionIntegrationTypeDef",
    {
        "KMSKeyId": NotRequired[str],
        "OptInStatus": NotRequired[OptInStatusType],
        "Type": NotRequired[ServerSideEncryptionTypeType],
    },
)
ServiceCollectionTypeDef = TypedDict(
    "ServiceCollectionTypeDef",
    {
        "ServiceNames": NotRequired[Sequence[ServiceNameType]],
    },
)
ListAnomalousLogGroupsRequestRequestTypeDef = TypedDict(
    "ListAnomalousLogGroupsRequestRequestTypeDef",
    {
        "InsightId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListInsightsOngoingStatusFilterTypeDef = TypedDict(
    "ListInsightsOngoingStatusFilterTypeDef",
    {
        "Type": InsightTypeType,
    },
)
ListMonitoredResourcesFiltersTypeDef = TypedDict(
    "ListMonitoredResourcesFiltersTypeDef",
    {
        "ResourcePermission": ResourcePermissionType,
        "ResourceTypeFilters": Sequence[ResourceTypeFilterType],
    },
)
ListNotificationChannelsRequestRequestTypeDef = TypedDict(
    "ListNotificationChannelsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
    },
)
ListRecommendationsRequestRequestTypeDef = TypedDict(
    "ListRecommendationsRequestRequestTypeDef",
    {
        "InsightId": str,
        "NextToken": NotRequired[str],
        "Locale": NotRequired[LocaleType],
        "AccountId": NotRequired[str],
    },
)
LogAnomalyClassTypeDef = TypedDict(
    "LogAnomalyClassTypeDef",
    {
        "LogStreamName": NotRequired[str],
        "LogAnomalyType": NotRequired[LogAnomalyTypeType],
        "LogAnomalyToken": NotRequired[str],
        "LogEventId": NotRequired[str],
        "Explanation": NotRequired[str],
        "NumberOfLogLinesOccurrences": NotRequired[int],
        "LogEventTimestamp": NotRequired[datetime],
    },
)
LogsAnomalyDetectionIntegrationConfigTypeDef = TypedDict(
    "LogsAnomalyDetectionIntegrationConfigTypeDef",
    {
        "OptInStatus": NotRequired[OptInStatusType],
    },
)
LogsAnomalyDetectionIntegrationTypeDef = TypedDict(
    "LogsAnomalyDetectionIntegrationTypeDef",
    {
        "OptInStatus": NotRequired[OptInStatusType],
    },
)
NotificationFilterConfigPaginatorTypeDef = TypedDict(
    "NotificationFilterConfigPaginatorTypeDef",
    {
        "Severities": NotRequired[List[InsightSeverityType]],
        "MessageTypes": NotRequired[List[NotificationMessageTypeType]],
    },
)
SnsChannelConfigTypeDef = TypedDict(
    "SnsChannelConfigTypeDef",
    {
        "TopicArn": NotRequired[str],
    },
)
NotificationFilterConfigTypeDef = TypedDict(
    "NotificationFilterConfigTypeDef",
    {
        "Severities": NotRequired[Sequence[InsightSeverityType]],
        "MessageTypes": NotRequired[Sequence[NotificationMessageTypeType]],
    },
)
OpsCenterIntegrationConfigTypeDef = TypedDict(
    "OpsCenterIntegrationConfigTypeDef",
    {
        "OptInStatus": NotRequired[OptInStatusType],
    },
)
OpsCenterIntegrationTypeDef = TypedDict(
    "OpsCenterIntegrationTypeDef",
    {
        "OptInStatus": NotRequired[OptInStatusType],
    },
)
PerformanceInsightsMetricDimensionGroupTypeDef = TypedDict(
    "PerformanceInsightsMetricDimensionGroupTypeDef",
    {
        "Group": NotRequired[str],
        "Dimensions": NotRequired[List[str]],
        "Limit": NotRequired[int],
    },
)
PerformanceInsightsStatTypeDef = TypedDict(
    "PerformanceInsightsStatTypeDef",
    {
        "Type": NotRequired[str],
        "Value": NotRequired[float],
    },
)
PerformanceInsightsReferenceScalarTypeDef = TypedDict(
    "PerformanceInsightsReferenceScalarTypeDef",
    {
        "Value": NotRequired[float],
    },
)
PredictionTimeRangeTypeDef = TypedDict(
    "PredictionTimeRangeTypeDef",
    {
        "StartTime": datetime,
        "EndTime": NotRequired[datetime],
    },
)
RecommendationRelatedAnomalyResourceTypeDef = TypedDict(
    "RecommendationRelatedAnomalyResourceTypeDef",
    {
        "Name": NotRequired[str],
        "Type": NotRequired[str],
    },
)
RecommendationRelatedCloudWatchMetricsSourceDetailTypeDef = TypedDict(
    "RecommendationRelatedCloudWatchMetricsSourceDetailTypeDef",
    {
        "MetricName": NotRequired[str],
        "Namespace": NotRequired[str],
    },
)
RecommendationRelatedEventResourceTypeDef = TypedDict(
    "RecommendationRelatedEventResourceTypeDef",
    {
        "Name": NotRequired[str],
        "Type": NotRequired[str],
    },
)
RemoveNotificationChannelRequestRequestTypeDef = TypedDict(
    "RemoveNotificationChannelRequestRequestTypeDef",
    {
        "Id": str,
    },
)
TagCollectionFilterTypeDef = TypedDict(
    "TagCollectionFilterTypeDef",
    {
        "AppBoundaryKey": str,
        "TagValues": List[str],
    },
)
TagCollectionTypeDef = TypedDict(
    "TagCollectionTypeDef",
    {
        "AppBoundaryKey": str,
        "TagValues": List[str],
    },
)
ServiceInsightHealthTypeDef = TypedDict(
    "ServiceInsightHealthTypeDef",
    {
        "OpenProactiveInsights": NotRequired[int],
        "OpenReactiveInsights": NotRequired[int],
    },
)
UpdateCloudFormationCollectionFilterTypeDef = TypedDict(
    "UpdateCloudFormationCollectionFilterTypeDef",
    {
        "StackNames": NotRequired[Sequence[str]],
    },
)
UpdateTagCollectionFilterTypeDef = TypedDict(
    "UpdateTagCollectionFilterTypeDef",
    {
        "AppBoundaryKey": str,
        "TagValues": Sequence[str],
    },
)
AccountHealthTypeDef = TypedDict(
    "AccountHealthTypeDef",
    {
        "AccountId": NotRequired[str],
        "Insight": NotRequired[AccountInsightHealthTypeDef],
    },
)
AddNotificationChannelResponseTypeDef = TypedDict(
    "AddNotificationChannelResponseTypeDef",
    {
        "Id": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeAccountHealthResponseTypeDef = TypedDict(
    "DescribeAccountHealthResponseTypeDef",
    {
        "OpenReactiveInsights": int,
        "OpenProactiveInsights": int,
        "MetricsAnalyzed": int,
        "ResourceHours": int,
        "AnalyzedResourceCount": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeAccountOverviewResponseTypeDef = TypedDict(
    "DescribeAccountOverviewResponseTypeDef",
    {
        "ReactiveInsights": int,
        "ProactiveInsights": int,
        "MeanTimeToRecoverInMilliseconds": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeOrganizationHealthResponseTypeDef = TypedDict(
    "DescribeOrganizationHealthResponseTypeDef",
    {
        "OpenReactiveInsights": int,
        "OpenProactiveInsights": int,
        "MetricsAnalyzed": int,
        "ResourceHours": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeOrganizationOverviewResponseTypeDef = TypedDict(
    "DescribeOrganizationOverviewResponseTypeDef",
    {
        "ReactiveInsights": int,
        "ProactiveInsights": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EventSourcesConfigTypeDef = TypedDict(
    "EventSourcesConfigTypeDef",
    {
        "AmazonCodeGuruProfiler": NotRequired[AmazonCodeGuruProfilerIntegrationTypeDef],
    },
)
CloudFormationHealthTypeDef = TypedDict(
    "CloudFormationHealthTypeDef",
    {
        "StackName": NotRequired[str],
        "Insight": NotRequired[InsightHealthTypeDef],
        "AnalyzedResourceCount": NotRequired[int],
    },
)
TagHealthTypeDef = TypedDict(
    "TagHealthTypeDef",
    {
        "AppBoundaryKey": NotRequired[str],
        "TagValue": NotRequired[str],
        "Insight": NotRequired[InsightHealthTypeDef],
        "AnalyzedResourceCount": NotRequired[int],
    },
)
CloudWatchMetricsDataSummaryTypeDef = TypedDict(
    "CloudWatchMetricsDataSummaryTypeDef",
    {
        "TimestampMetricValuePairList": NotRequired[List[TimestampMetricValuePairTypeDef]],
        "StatusCode": NotRequired[CloudWatchMetricDataStatusCodeType],
    },
)
CostEstimationResourceCollectionFilterTypeDef = TypedDict(
    "CostEstimationResourceCollectionFilterTypeDef",
    {
        "CloudFormation": NotRequired[CloudFormationCostEstimationResourceCollectionFilterTypeDef],
        "Tags": NotRequired[List[TagCostEstimationResourceCollectionFilterTypeDef]],
    },
)
DescribeAccountOverviewRequestRequestTypeDef = TypedDict(
    "DescribeAccountOverviewRequestRequestTypeDef",
    {
        "FromTime": TimestampTypeDef,
        "ToTime": NotRequired[TimestampTypeDef],
    },
)
DescribeOrganizationOverviewRequestRequestTypeDef = TypedDict(
    "DescribeOrganizationOverviewRequestRequestTypeDef",
    {
        "FromTime": TimestampTypeDef,
        "ToTime": NotRequired[TimestampTypeDef],
        "AccountIds": NotRequired[Sequence[str]],
        "OrganizationalUnitIds": NotRequired[Sequence[str]],
    },
)
EndTimeRangeTypeDef = TypedDict(
    "EndTimeRangeTypeDef",
    {
        "FromTime": NotRequired[TimestampTypeDef],
        "ToTime": NotRequired[TimestampTypeDef],
    },
)
EventTimeRangeTypeDef = TypedDict(
    "EventTimeRangeTypeDef",
    {
        "FromTime": TimestampTypeDef,
        "ToTime": TimestampTypeDef,
    },
)
StartTimeRangeTypeDef = TypedDict(
    "StartTimeRangeTypeDef",
    {
        "FromTime": NotRequired[TimestampTypeDef],
        "ToTime": NotRequired[TimestampTypeDef],
    },
)
DescribeFeedbackResponseTypeDef = TypedDict(
    "DescribeFeedbackResponseTypeDef",
    {
        "InsightFeedback": InsightFeedbackTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutFeedbackRequestRequestTypeDef = TypedDict(
    "PutFeedbackRequestRequestTypeDef",
    {
        "InsightFeedback": NotRequired[InsightFeedbackTypeDef],
    },
)
DescribeOrganizationResourceCollectionHealthRequestDescribeOrganizationResourceCollectionHealthPaginateTypeDef = TypedDict(
    "DescribeOrganizationResourceCollectionHealthRequestDescribeOrganizationResourceCollectionHealthPaginateTypeDef",
    {
        "OrganizationResourceCollectionType": OrganizationResourceCollectionTypeType,
        "AccountIds": NotRequired[Sequence[str]],
        "OrganizationalUnitIds": NotRequired[Sequence[str]],
        "MaxResults": NotRequired[int],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeResourceCollectionHealthRequestDescribeResourceCollectionHealthPaginateTypeDef = TypedDict(
    "DescribeResourceCollectionHealthRequestDescribeResourceCollectionHealthPaginateTypeDef",
    {
        "ResourceCollectionType": ResourceCollectionTypeType,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetCostEstimationRequestGetCostEstimationPaginateTypeDef = TypedDict(
    "GetCostEstimationRequestGetCostEstimationPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetResourceCollectionRequestGetResourceCollectionPaginateTypeDef = TypedDict(
    "GetResourceCollectionRequestGetResourceCollectionPaginateTypeDef",
    {
        "ResourceCollectionType": ResourceCollectionTypeType,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListAnomalousLogGroupsRequestListAnomalousLogGroupsPaginateTypeDef = TypedDict(
    "ListAnomalousLogGroupsRequestListAnomalousLogGroupsPaginateTypeDef",
    {
        "InsightId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListNotificationChannelsRequestListNotificationChannelsPaginateTypeDef = TypedDict(
    "ListNotificationChannelsRequestListNotificationChannelsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListRecommendationsRequestListRecommendationsPaginateTypeDef = TypedDict(
    "ListRecommendationsRequestListRecommendationsPaginateTypeDef",
    {
        "InsightId": str,
        "Locale": NotRequired[LocaleType],
        "AccountId": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListAnomaliesForInsightFiltersTypeDef = TypedDict(
    "ListAnomaliesForInsightFiltersTypeDef",
    {
        "ServiceCollection": NotRequired[ServiceCollectionTypeDef],
    },
)
ListMonitoredResourcesRequestListMonitoredResourcesPaginateTypeDef = TypedDict(
    "ListMonitoredResourcesRequestListMonitoredResourcesPaginateTypeDef",
    {
        "Filters": NotRequired[ListMonitoredResourcesFiltersTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListMonitoredResourcesRequestRequestTypeDef = TypedDict(
    "ListMonitoredResourcesRequestRequestTypeDef",
    {
        "Filters": NotRequired[ListMonitoredResourcesFiltersTypeDef],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
LogAnomalyShowcaseTypeDef = TypedDict(
    "LogAnomalyShowcaseTypeDef",
    {
        "LogAnomalyClasses": NotRequired[List[LogAnomalyClassTypeDef]],
    },
)
NotificationChannelConfigPaginatorTypeDef = TypedDict(
    "NotificationChannelConfigPaginatorTypeDef",
    {
        "Sns": SnsChannelConfigTypeDef,
        "Filters": NotRequired[NotificationFilterConfigPaginatorTypeDef],
    },
)
NotificationChannelConfigTypeDef = TypedDict(
    "NotificationChannelConfigTypeDef",
    {
        "Sns": SnsChannelConfigTypeDef,
        "Filters": NotRequired[NotificationFilterConfigTypeDef],
    },
)
UpdateServiceIntegrationConfigTypeDef = TypedDict(
    "UpdateServiceIntegrationConfigTypeDef",
    {
        "OpsCenter": NotRequired[OpsCenterIntegrationConfigTypeDef],
        "LogsAnomalyDetection": NotRequired[LogsAnomalyDetectionIntegrationConfigTypeDef],
        "KMSServerSideEncryption": NotRequired[KMSServerSideEncryptionIntegrationConfigTypeDef],
    },
)
ServiceIntegrationConfigTypeDef = TypedDict(
    "ServiceIntegrationConfigTypeDef",
    {
        "OpsCenter": NotRequired[OpsCenterIntegrationTypeDef],
        "LogsAnomalyDetection": NotRequired[LogsAnomalyDetectionIntegrationTypeDef],
        "KMSServerSideEncryption": NotRequired[KMSServerSideEncryptionIntegrationTypeDef],
    },
)
PerformanceInsightsMetricQueryTypeDef = TypedDict(
    "PerformanceInsightsMetricQueryTypeDef",
    {
        "Metric": NotRequired[str],
        "GroupBy": NotRequired[PerformanceInsightsMetricDimensionGroupTypeDef],
        "Filter": NotRequired[Dict[str, str]],
    },
)
RecommendationRelatedAnomalySourceDetailTypeDef = TypedDict(
    "RecommendationRelatedAnomalySourceDetailTypeDef",
    {
        "CloudWatchMetrics": NotRequired[
            List[RecommendationRelatedCloudWatchMetricsSourceDetailTypeDef]
        ],
    },
)
RecommendationRelatedEventTypeDef = TypedDict(
    "RecommendationRelatedEventTypeDef",
    {
        "Name": NotRequired[str],
        "Resources": NotRequired[List[RecommendationRelatedEventResourceTypeDef]],
    },
)
ResourceCollectionFilterTypeDef = TypedDict(
    "ResourceCollectionFilterTypeDef",
    {
        "CloudFormation": NotRequired[CloudFormationCollectionFilterTypeDef],
        "Tags": NotRequired[List[TagCollectionFilterTypeDef]],
    },
)
ResourceCollectionTypeDef = TypedDict(
    "ResourceCollectionTypeDef",
    {
        "CloudFormation": NotRequired[CloudFormationCollectionTypeDef],
        "Tags": NotRequired[List[TagCollectionTypeDef]],
    },
)
ServiceHealthTypeDef = TypedDict(
    "ServiceHealthTypeDef",
    {
        "ServiceName": NotRequired[ServiceNameType],
        "Insight": NotRequired[ServiceInsightHealthTypeDef],
        "AnalyzedResourceCount": NotRequired[int],
    },
)
UpdateResourceCollectionFilterTypeDef = TypedDict(
    "UpdateResourceCollectionFilterTypeDef",
    {
        "CloudFormation": NotRequired[UpdateCloudFormationCollectionFilterTypeDef],
        "Tags": NotRequired[Sequence[UpdateTagCollectionFilterTypeDef]],
    },
)
DescribeEventSourcesConfigResponseTypeDef = TypedDict(
    "DescribeEventSourcesConfigResponseTypeDef",
    {
        "EventSources": EventSourcesConfigTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateEventSourcesConfigRequestRequestTypeDef = TypedDict(
    "UpdateEventSourcesConfigRequestRequestTypeDef",
    {
        "EventSources": NotRequired[EventSourcesConfigTypeDef],
    },
)
CloudWatchMetricsDetailTypeDef = TypedDict(
    "CloudWatchMetricsDetailTypeDef",
    {
        "MetricName": NotRequired[str],
        "Namespace": NotRequired[str],
        "Dimensions": NotRequired[List[CloudWatchMetricsDimensionTypeDef]],
        "Stat": NotRequired[CloudWatchMetricsStatType],
        "Unit": NotRequired[str],
        "Period": NotRequired[int],
        "MetricDataSummary": NotRequired[CloudWatchMetricsDataSummaryTypeDef],
    },
)
GetCostEstimationResponseTypeDef = TypedDict(
    "GetCostEstimationResponseTypeDef",
    {
        "ResourceCollection": CostEstimationResourceCollectionFilterTypeDef,
        "Status": CostEstimationStatusType,
        "Costs": List[ServiceResourceCostTypeDef],
        "TimeRange": CostEstimationTimeRangeTypeDef,
        "TotalCost": float,
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartCostEstimationRequestRequestTypeDef = TypedDict(
    "StartCostEstimationRequestRequestTypeDef",
    {
        "ResourceCollection": CostEstimationResourceCollectionFilterTypeDef,
        "ClientToken": NotRequired[str],
    },
)
ListInsightsClosedStatusFilterTypeDef = TypedDict(
    "ListInsightsClosedStatusFilterTypeDef",
    {
        "Type": InsightTypeType,
        "EndTimeRange": EndTimeRangeTypeDef,
    },
)
ListInsightsAnyStatusFilterTypeDef = TypedDict(
    "ListInsightsAnyStatusFilterTypeDef",
    {
        "Type": InsightTypeType,
        "StartTimeRange": StartTimeRangeTypeDef,
    },
)
ListAnomaliesForInsightRequestListAnomaliesForInsightPaginateTypeDef = TypedDict(
    "ListAnomaliesForInsightRequestListAnomaliesForInsightPaginateTypeDef",
    {
        "InsightId": str,
        "StartTimeRange": NotRequired[StartTimeRangeTypeDef],
        "AccountId": NotRequired[str],
        "Filters": NotRequired[ListAnomaliesForInsightFiltersTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListAnomaliesForInsightRequestRequestTypeDef = TypedDict(
    "ListAnomaliesForInsightRequestRequestTypeDef",
    {
        "InsightId": str,
        "StartTimeRange": NotRequired[StartTimeRangeTypeDef],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "AccountId": NotRequired[str],
        "Filters": NotRequired[ListAnomaliesForInsightFiltersTypeDef],
    },
)
AnomalousLogGroupTypeDef = TypedDict(
    "AnomalousLogGroupTypeDef",
    {
        "LogGroupName": NotRequired[str],
        "ImpactStartTime": NotRequired[datetime],
        "ImpactEndTime": NotRequired[datetime],
        "NumberOfLogLinesScanned": NotRequired[int],
        "LogAnomalyShowcases": NotRequired[List[LogAnomalyShowcaseTypeDef]],
    },
)
NotificationChannelPaginatorTypeDef = TypedDict(
    "NotificationChannelPaginatorTypeDef",
    {
        "Id": NotRequired[str],
        "Config": NotRequired[NotificationChannelConfigPaginatorTypeDef],
    },
)
AddNotificationChannelRequestRequestTypeDef = TypedDict(
    "AddNotificationChannelRequestRequestTypeDef",
    {
        "Config": NotificationChannelConfigTypeDef,
    },
)
NotificationChannelTypeDef = TypedDict(
    "NotificationChannelTypeDef",
    {
        "Id": NotRequired[str],
        "Config": NotRequired[NotificationChannelConfigTypeDef],
    },
)
UpdateServiceIntegrationRequestRequestTypeDef = TypedDict(
    "UpdateServiceIntegrationRequestRequestTypeDef",
    {
        "ServiceIntegration": UpdateServiceIntegrationConfigTypeDef,
    },
)
DescribeServiceIntegrationResponseTypeDef = TypedDict(
    "DescribeServiceIntegrationResponseTypeDef",
    {
        "ServiceIntegration": ServiceIntegrationConfigTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PerformanceInsightsReferenceMetricTypeDef = TypedDict(
    "PerformanceInsightsReferenceMetricTypeDef",
    {
        "MetricQuery": NotRequired[PerformanceInsightsMetricQueryTypeDef],
    },
)
RecommendationRelatedAnomalyTypeDef = TypedDict(
    "RecommendationRelatedAnomalyTypeDef",
    {
        "Resources": NotRequired[List[RecommendationRelatedAnomalyResourceTypeDef]],
        "SourceDetails": NotRequired[List[RecommendationRelatedAnomalySourceDetailTypeDef]],
        "AnomalyId": NotRequired[str],
    },
)
GetResourceCollectionResponseTypeDef = TypedDict(
    "GetResourceCollectionResponseTypeDef",
    {
        "ResourceCollection": ResourceCollectionFilterTypeDef,
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EventTypeDef = TypedDict(
    "EventTypeDef",
    {
        "ResourceCollection": NotRequired[ResourceCollectionTypeDef],
        "Id": NotRequired[str],
        "Time": NotRequired[datetime],
        "EventSource": NotRequired[str],
        "Name": NotRequired[str],
        "DataSource": NotRequired[EventDataSourceType],
        "EventClass": NotRequired[EventClassType],
        "Resources": NotRequired[List[EventResourceTypeDef]],
    },
)
ListEventsFiltersTypeDef = TypedDict(
    "ListEventsFiltersTypeDef",
    {
        "InsightId": NotRequired[str],
        "EventTimeRange": NotRequired[EventTimeRangeTypeDef],
        "EventClass": NotRequired[EventClassType],
        "EventSource": NotRequired[str],
        "DataSource": NotRequired[EventDataSourceType],
        "ResourceCollection": NotRequired[ResourceCollectionTypeDef],
    },
)
MonitoredResourceIdentifierTypeDef = TypedDict(
    "MonitoredResourceIdentifierTypeDef",
    {
        "MonitoredResourceName": NotRequired[str],
        "Type": NotRequired[str],
        "ResourcePermission": NotRequired[ResourcePermissionType],
        "LastUpdated": NotRequired[datetime],
        "ResourceCollection": NotRequired[ResourceCollectionTypeDef],
    },
)
ProactiveInsightSummaryTypeDef = TypedDict(
    "ProactiveInsightSummaryTypeDef",
    {
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "Severity": NotRequired[InsightSeverityType],
        "Status": NotRequired[InsightStatusType],
        "InsightTimeRange": NotRequired[InsightTimeRangeTypeDef],
        "PredictionTimeRange": NotRequired[PredictionTimeRangeTypeDef],
        "ResourceCollection": NotRequired[ResourceCollectionTypeDef],
        "ServiceCollection": NotRequired[ServiceCollectionTypeDef],
        "AssociatedResourceArns": NotRequired[List[str]],
    },
)
ProactiveInsightTypeDef = TypedDict(
    "ProactiveInsightTypeDef",
    {
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "Severity": NotRequired[InsightSeverityType],
        "Status": NotRequired[InsightStatusType],
        "InsightTimeRange": NotRequired[InsightTimeRangeTypeDef],
        "PredictionTimeRange": NotRequired[PredictionTimeRangeTypeDef],
        "ResourceCollection": NotRequired[ResourceCollectionTypeDef],
        "SsmOpsItemId": NotRequired[str],
        "Description": NotRequired[str],
    },
)
ProactiveOrganizationInsightSummaryTypeDef = TypedDict(
    "ProactiveOrganizationInsightSummaryTypeDef",
    {
        "Id": NotRequired[str],
        "AccountId": NotRequired[str],
        "OrganizationalUnitId": NotRequired[str],
        "Name": NotRequired[str],
        "Severity": NotRequired[InsightSeverityType],
        "Status": NotRequired[InsightStatusType],
        "InsightTimeRange": NotRequired[InsightTimeRangeTypeDef],
        "PredictionTimeRange": NotRequired[PredictionTimeRangeTypeDef],
        "ResourceCollection": NotRequired[ResourceCollectionTypeDef],
        "ServiceCollection": NotRequired[ServiceCollectionTypeDef],
    },
)
ReactiveInsightSummaryTypeDef = TypedDict(
    "ReactiveInsightSummaryTypeDef",
    {
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "Severity": NotRequired[InsightSeverityType],
        "Status": NotRequired[InsightStatusType],
        "InsightTimeRange": NotRequired[InsightTimeRangeTypeDef],
        "ResourceCollection": NotRequired[ResourceCollectionTypeDef],
        "ServiceCollection": NotRequired[ServiceCollectionTypeDef],
        "AssociatedResourceArns": NotRequired[List[str]],
    },
)
ReactiveInsightTypeDef = TypedDict(
    "ReactiveInsightTypeDef",
    {
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "Severity": NotRequired[InsightSeverityType],
        "Status": NotRequired[InsightStatusType],
        "InsightTimeRange": NotRequired[InsightTimeRangeTypeDef],
        "ResourceCollection": NotRequired[ResourceCollectionTypeDef],
        "SsmOpsItemId": NotRequired[str],
        "Description": NotRequired[str],
    },
)
ReactiveOrganizationInsightSummaryTypeDef = TypedDict(
    "ReactiveOrganizationInsightSummaryTypeDef",
    {
        "Id": NotRequired[str],
        "AccountId": NotRequired[str],
        "OrganizationalUnitId": NotRequired[str],
        "Name": NotRequired[str],
        "Severity": NotRequired[InsightSeverityType],
        "Status": NotRequired[InsightStatusType],
        "InsightTimeRange": NotRequired[InsightTimeRangeTypeDef],
        "ResourceCollection": NotRequired[ResourceCollectionTypeDef],
        "ServiceCollection": NotRequired[ServiceCollectionTypeDef],
    },
)
SearchInsightsFiltersTypeDef = TypedDict(
    "SearchInsightsFiltersTypeDef",
    {
        "Severities": NotRequired[Sequence[InsightSeverityType]],
        "Statuses": NotRequired[Sequence[InsightStatusType]],
        "ResourceCollection": NotRequired[ResourceCollectionTypeDef],
        "ServiceCollection": NotRequired[ServiceCollectionTypeDef],
    },
)
SearchOrganizationInsightsFiltersTypeDef = TypedDict(
    "SearchOrganizationInsightsFiltersTypeDef",
    {
        "Severities": NotRequired[Sequence[InsightSeverityType]],
        "Statuses": NotRequired[Sequence[InsightStatusType]],
        "ResourceCollection": NotRequired[ResourceCollectionTypeDef],
        "ServiceCollection": NotRequired[ServiceCollectionTypeDef],
    },
)
DescribeOrganizationResourceCollectionHealthResponseTypeDef = TypedDict(
    "DescribeOrganizationResourceCollectionHealthResponseTypeDef",
    {
        "CloudFormation": List[CloudFormationHealthTypeDef],
        "Service": List[ServiceHealthTypeDef],
        "Account": List[AccountHealthTypeDef],
        "NextToken": str,
        "Tags": List[TagHealthTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeResourceCollectionHealthResponseTypeDef = TypedDict(
    "DescribeResourceCollectionHealthResponseTypeDef",
    {
        "CloudFormation": List[CloudFormationHealthTypeDef],
        "Service": List[ServiceHealthTypeDef],
        "NextToken": str,
        "Tags": List[TagHealthTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateResourceCollectionRequestRequestTypeDef = TypedDict(
    "UpdateResourceCollectionRequestRequestTypeDef",
    {
        "Action": UpdateResourceCollectionActionType,
        "ResourceCollection": UpdateResourceCollectionFilterTypeDef,
    },
)
ListInsightsStatusFilterTypeDef = TypedDict(
    "ListInsightsStatusFilterTypeDef",
    {
        "Ongoing": NotRequired[ListInsightsOngoingStatusFilterTypeDef],
        "Closed": NotRequired[ListInsightsClosedStatusFilterTypeDef],
        "Any": NotRequired[ListInsightsAnyStatusFilterTypeDef],
    },
)
ListAnomalousLogGroupsResponseTypeDef = TypedDict(
    "ListAnomalousLogGroupsResponseTypeDef",
    {
        "InsightId": str,
        "AnomalousLogGroups": List[AnomalousLogGroupTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListNotificationChannelsResponsePaginatorTypeDef = TypedDict(
    "ListNotificationChannelsResponsePaginatorTypeDef",
    {
        "Channels": List[NotificationChannelPaginatorTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListNotificationChannelsResponseTypeDef = TypedDict(
    "ListNotificationChannelsResponseTypeDef",
    {
        "Channels": List[NotificationChannelTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PerformanceInsightsReferenceComparisonValuesTypeDef = TypedDict(
    "PerformanceInsightsReferenceComparisonValuesTypeDef",
    {
        "ReferenceScalar": NotRequired[PerformanceInsightsReferenceScalarTypeDef],
        "ReferenceMetric": NotRequired[PerformanceInsightsReferenceMetricTypeDef],
    },
)
RecommendationTypeDef = TypedDict(
    "RecommendationTypeDef",
    {
        "Description": NotRequired[str],
        "Link": NotRequired[str],
        "Name": NotRequired[str],
        "Reason": NotRequired[str],
        "RelatedEvents": NotRequired[List[RecommendationRelatedEventTypeDef]],
        "RelatedAnomalies": NotRequired[List[RecommendationRelatedAnomalyTypeDef]],
        "Category": NotRequired[str],
    },
)
ListEventsResponseTypeDef = TypedDict(
    "ListEventsResponseTypeDef",
    {
        "Events": List[EventTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListEventsRequestListEventsPaginateTypeDef = TypedDict(
    "ListEventsRequestListEventsPaginateTypeDef",
    {
        "Filters": ListEventsFiltersTypeDef,
        "AccountId": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListEventsRequestRequestTypeDef = TypedDict(
    "ListEventsRequestRequestTypeDef",
    {
        "Filters": ListEventsFiltersTypeDef,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "AccountId": NotRequired[str],
    },
)
ListMonitoredResourcesResponseTypeDef = TypedDict(
    "ListMonitoredResourcesResponseTypeDef",
    {
        "MonitoredResourceIdentifiers": List[MonitoredResourceIdentifierTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListInsightsResponseTypeDef = TypedDict(
    "ListInsightsResponseTypeDef",
    {
        "ProactiveInsights": List[ProactiveInsightSummaryTypeDef],
        "ReactiveInsights": List[ReactiveInsightSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SearchInsightsResponseTypeDef = TypedDict(
    "SearchInsightsResponseTypeDef",
    {
        "ProactiveInsights": List[ProactiveInsightSummaryTypeDef],
        "ReactiveInsights": List[ReactiveInsightSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SearchOrganizationInsightsResponseTypeDef = TypedDict(
    "SearchOrganizationInsightsResponseTypeDef",
    {
        "ProactiveInsights": List[ProactiveInsightSummaryTypeDef],
        "ReactiveInsights": List[ReactiveInsightSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeInsightResponseTypeDef = TypedDict(
    "DescribeInsightResponseTypeDef",
    {
        "ProactiveInsight": ProactiveInsightTypeDef,
        "ReactiveInsight": ReactiveInsightTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListOrganizationInsightsResponseTypeDef = TypedDict(
    "ListOrganizationInsightsResponseTypeDef",
    {
        "ProactiveInsights": List[ProactiveOrganizationInsightSummaryTypeDef],
        "ReactiveInsights": List[ReactiveOrganizationInsightSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SearchInsightsRequestRequestTypeDef = TypedDict(
    "SearchInsightsRequestRequestTypeDef",
    {
        "StartTimeRange": StartTimeRangeTypeDef,
        "Type": InsightTypeType,
        "Filters": NotRequired[SearchInsightsFiltersTypeDef],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
SearchInsightsRequestSearchInsightsPaginateTypeDef = TypedDict(
    "SearchInsightsRequestSearchInsightsPaginateTypeDef",
    {
        "StartTimeRange": StartTimeRangeTypeDef,
        "Type": InsightTypeType,
        "Filters": NotRequired[SearchInsightsFiltersTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
SearchOrganizationInsightsRequestRequestTypeDef = TypedDict(
    "SearchOrganizationInsightsRequestRequestTypeDef",
    {
        "AccountIds": Sequence[str],
        "StartTimeRange": StartTimeRangeTypeDef,
        "Type": InsightTypeType,
        "Filters": NotRequired[SearchOrganizationInsightsFiltersTypeDef],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
SearchOrganizationInsightsRequestSearchOrganizationInsightsPaginateTypeDef = TypedDict(
    "SearchOrganizationInsightsRequestSearchOrganizationInsightsPaginateTypeDef",
    {
        "AccountIds": Sequence[str],
        "StartTimeRange": StartTimeRangeTypeDef,
        "Type": InsightTypeType,
        "Filters": NotRequired[SearchOrganizationInsightsFiltersTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListInsightsRequestListInsightsPaginateTypeDef = TypedDict(
    "ListInsightsRequestListInsightsPaginateTypeDef",
    {
        "StatusFilter": ListInsightsStatusFilterTypeDef,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListInsightsRequestRequestTypeDef = TypedDict(
    "ListInsightsRequestRequestTypeDef",
    {
        "StatusFilter": ListInsightsStatusFilterTypeDef,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListOrganizationInsightsRequestListOrganizationInsightsPaginateTypeDef = TypedDict(
    "ListOrganizationInsightsRequestListOrganizationInsightsPaginateTypeDef",
    {
        "StatusFilter": ListInsightsStatusFilterTypeDef,
        "AccountIds": NotRequired[Sequence[str]],
        "OrganizationalUnitIds": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListOrganizationInsightsRequestRequestTypeDef = TypedDict(
    "ListOrganizationInsightsRequestRequestTypeDef",
    {
        "StatusFilter": ListInsightsStatusFilterTypeDef,
        "MaxResults": NotRequired[int],
        "AccountIds": NotRequired[Sequence[str]],
        "OrganizationalUnitIds": NotRequired[Sequence[str]],
        "NextToken": NotRequired[str],
    },
)
PerformanceInsightsReferenceDataTypeDef = TypedDict(
    "PerformanceInsightsReferenceDataTypeDef",
    {
        "Name": NotRequired[str],
        "ComparisonValues": NotRequired[PerformanceInsightsReferenceComparisonValuesTypeDef],
    },
)
ListRecommendationsResponseTypeDef = TypedDict(
    "ListRecommendationsResponseTypeDef",
    {
        "Recommendations": List[RecommendationTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PerformanceInsightsMetricsDetailTypeDef = TypedDict(
    "PerformanceInsightsMetricsDetailTypeDef",
    {
        "MetricDisplayName": NotRequired[str],
        "Unit": NotRequired[str],
        "MetricQuery": NotRequired[PerformanceInsightsMetricQueryTypeDef],
        "ReferenceData": NotRequired[List[PerformanceInsightsReferenceDataTypeDef]],
        "StatsAtAnomaly": NotRequired[List[PerformanceInsightsStatTypeDef]],
        "StatsAtBaseline": NotRequired[List[PerformanceInsightsStatTypeDef]],
    },
)
AnomalySourceDetailsTypeDef = TypedDict(
    "AnomalySourceDetailsTypeDef",
    {
        "CloudWatchMetrics": NotRequired[List[CloudWatchMetricsDetailTypeDef]],
        "PerformanceInsightsMetrics": NotRequired[List[PerformanceInsightsMetricsDetailTypeDef]],
    },
)
ProactiveAnomalySummaryTypeDef = TypedDict(
    "ProactiveAnomalySummaryTypeDef",
    {
        "Id": NotRequired[str],
        "Severity": NotRequired[AnomalySeverityType],
        "Status": NotRequired[AnomalyStatusType],
        "UpdateTime": NotRequired[datetime],
        "AnomalyTimeRange": NotRequired[AnomalyTimeRangeTypeDef],
        "AnomalyReportedTimeRange": NotRequired[AnomalyReportedTimeRangeTypeDef],
        "PredictionTimeRange": NotRequired[PredictionTimeRangeTypeDef],
        "SourceDetails": NotRequired[AnomalySourceDetailsTypeDef],
        "AssociatedInsightId": NotRequired[str],
        "ResourceCollection": NotRequired[ResourceCollectionTypeDef],
        "Limit": NotRequired[float],
        "SourceMetadata": NotRequired[AnomalySourceMetadataTypeDef],
        "AnomalyResources": NotRequired[List[AnomalyResourceTypeDef]],
        "Description": NotRequired[str],
    },
)
ProactiveAnomalyTypeDef = TypedDict(
    "ProactiveAnomalyTypeDef",
    {
        "Id": NotRequired[str],
        "Severity": NotRequired[AnomalySeverityType],
        "Status": NotRequired[AnomalyStatusType],
        "UpdateTime": NotRequired[datetime],
        "AnomalyTimeRange": NotRequired[AnomalyTimeRangeTypeDef],
        "AnomalyReportedTimeRange": NotRequired[AnomalyReportedTimeRangeTypeDef],
        "PredictionTimeRange": NotRequired[PredictionTimeRangeTypeDef],
        "SourceDetails": NotRequired[AnomalySourceDetailsTypeDef],
        "AssociatedInsightId": NotRequired[str],
        "ResourceCollection": NotRequired[ResourceCollectionTypeDef],
        "Limit": NotRequired[float],
        "SourceMetadata": NotRequired[AnomalySourceMetadataTypeDef],
        "AnomalyResources": NotRequired[List[AnomalyResourceTypeDef]],
        "Description": NotRequired[str],
    },
)
ReactiveAnomalySummaryTypeDef = TypedDict(
    "ReactiveAnomalySummaryTypeDef",
    {
        "Id": NotRequired[str],
        "Severity": NotRequired[AnomalySeverityType],
        "Status": NotRequired[AnomalyStatusType],
        "AnomalyTimeRange": NotRequired[AnomalyTimeRangeTypeDef],
        "AnomalyReportedTimeRange": NotRequired[AnomalyReportedTimeRangeTypeDef],
        "SourceDetails": NotRequired[AnomalySourceDetailsTypeDef],
        "AssociatedInsightId": NotRequired[str],
        "ResourceCollection": NotRequired[ResourceCollectionTypeDef],
        "Type": NotRequired[AnomalyTypeType],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "CausalAnomalyId": NotRequired[str],
        "AnomalyResources": NotRequired[List[AnomalyResourceTypeDef]],
    },
)
ReactiveAnomalyTypeDef = TypedDict(
    "ReactiveAnomalyTypeDef",
    {
        "Id": NotRequired[str],
        "Severity": NotRequired[AnomalySeverityType],
        "Status": NotRequired[AnomalyStatusType],
        "AnomalyTimeRange": NotRequired[AnomalyTimeRangeTypeDef],
        "AnomalyReportedTimeRange": NotRequired[AnomalyReportedTimeRangeTypeDef],
        "SourceDetails": NotRequired[AnomalySourceDetailsTypeDef],
        "AssociatedInsightId": NotRequired[str],
        "ResourceCollection": NotRequired[ResourceCollectionTypeDef],
        "Type": NotRequired[AnomalyTypeType],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "CausalAnomalyId": NotRequired[str],
        "AnomalyResources": NotRequired[List[AnomalyResourceTypeDef]],
    },
)
ListAnomaliesForInsightResponseTypeDef = TypedDict(
    "ListAnomaliesForInsightResponseTypeDef",
    {
        "ProactiveAnomalies": List[ProactiveAnomalySummaryTypeDef],
        "ReactiveAnomalies": List[ReactiveAnomalySummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeAnomalyResponseTypeDef = TypedDict(
    "DescribeAnomalyResponseTypeDef",
    {
        "ProactiveAnomaly": ProactiveAnomalyTypeDef,
        "ReactiveAnomaly": ReactiveAnomalyTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
