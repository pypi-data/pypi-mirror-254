"""
Type annotations for internetmonitor service type definitions.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_internetmonitor/type_defs/)

Usage::

    ```python
    from types_aiobotocore_internetmonitor.type_defs import AvailabilityMeasurementTypeDef

    data: AvailabilityMeasurementTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from .literals import (
    HealthEventImpactTypeType,
    HealthEventStatusType,
    LocalHealthEventsConfigStatusType,
    LogDeliveryStatusType,
    MonitorConfigStateType,
    MonitorProcessingStatusCodeType,
    OperatorType,
    QueryStatusType,
    QueryTypeType,
    TriangulationEventTypeType,
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
    "AvailabilityMeasurementTypeDef",
    "ResponseMetadataTypeDef",
    "DeleteMonitorInputRequestTypeDef",
    "FilterParameterTypeDef",
    "GetHealthEventInputRequestTypeDef",
    "GetMonitorInputRequestTypeDef",
    "GetQueryResultsInputRequestTypeDef",
    "QueryFieldTypeDef",
    "GetQueryStatusInputRequestTypeDef",
    "LocalHealthEventsConfigTypeDef",
    "S3ConfigTypeDef",
    "PaginatorConfigTypeDef",
    "TimestampTypeDef",
    "ListMonitorsInputRequestTypeDef",
    "MonitorTypeDef",
    "ListTagsForResourceInputRequestTypeDef",
    "NetworkTypeDef",
    "RoundTripTimeTypeDef",
    "StopQueryInputRequestTypeDef",
    "TagResourceInputRequestTypeDef",
    "UntagResourceInputRequestTypeDef",
    "CreateMonitorOutputTypeDef",
    "GetQueryStatusOutputTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "StartQueryOutputTypeDef",
    "UpdateMonitorOutputTypeDef",
    "GetQueryResultsOutputTypeDef",
    "HealthEventsConfigTypeDef",
    "InternetMeasurementsLogDeliveryTypeDef",
    "ListMonitorsInputListMonitorsPaginateTypeDef",
    "ListHealthEventsInputListHealthEventsPaginateTypeDef",
    "ListHealthEventsInputRequestTypeDef",
    "StartQueryInputRequestTypeDef",
    "ListMonitorsOutputTypeDef",
    "NetworkImpairmentTypeDef",
    "PerformanceMeasurementTypeDef",
    "CreateMonitorInputRequestTypeDef",
    "GetMonitorOutputTypeDef",
    "UpdateMonitorInputRequestTypeDef",
    "InternetHealthTypeDef",
    "ImpactedLocationTypeDef",
    "GetHealthEventOutputTypeDef",
    "HealthEventTypeDef",
    "ListHealthEventsOutputTypeDef",
)

AvailabilityMeasurementTypeDef = TypedDict(
    "AvailabilityMeasurementTypeDef",
    {
        "ExperienceScore": NotRequired[float],
        "PercentOfTotalTrafficImpacted": NotRequired[float],
        "PercentOfClientLocationImpacted": NotRequired[float],
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
DeleteMonitorInputRequestTypeDef = TypedDict(
    "DeleteMonitorInputRequestTypeDef",
    {
        "MonitorName": str,
    },
)
FilterParameterTypeDef = TypedDict(
    "FilterParameterTypeDef",
    {
        "Field": NotRequired[str],
        "Operator": NotRequired[OperatorType],
        "Values": NotRequired[Sequence[str]],
    },
)
GetHealthEventInputRequestTypeDef = TypedDict(
    "GetHealthEventInputRequestTypeDef",
    {
        "MonitorName": str,
        "EventId": str,
    },
)
GetMonitorInputRequestTypeDef = TypedDict(
    "GetMonitorInputRequestTypeDef",
    {
        "MonitorName": str,
    },
)
GetQueryResultsInputRequestTypeDef = TypedDict(
    "GetQueryResultsInputRequestTypeDef",
    {
        "MonitorName": str,
        "QueryId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
QueryFieldTypeDef = TypedDict(
    "QueryFieldTypeDef",
    {
        "Name": NotRequired[str],
        "Type": NotRequired[str],
    },
)
GetQueryStatusInputRequestTypeDef = TypedDict(
    "GetQueryStatusInputRequestTypeDef",
    {
        "MonitorName": str,
        "QueryId": str,
    },
)
LocalHealthEventsConfigTypeDef = TypedDict(
    "LocalHealthEventsConfigTypeDef",
    {
        "Status": NotRequired[LocalHealthEventsConfigStatusType],
        "HealthScoreThreshold": NotRequired[float],
        "MinTrafficImpact": NotRequired[float],
    },
)
S3ConfigTypeDef = TypedDict(
    "S3ConfigTypeDef",
    {
        "BucketName": NotRequired[str],
        "BucketPrefix": NotRequired[str],
        "LogDeliveryStatus": NotRequired[LogDeliveryStatusType],
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
TimestampTypeDef = Union[datetime, str]
ListMonitorsInputRequestTypeDef = TypedDict(
    "ListMonitorsInputRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "MonitorStatus": NotRequired[str],
    },
)
MonitorTypeDef = TypedDict(
    "MonitorTypeDef",
    {
        "MonitorName": str,
        "MonitorArn": str,
        "Status": MonitorConfigStateType,
        "ProcessingStatus": NotRequired[MonitorProcessingStatusCodeType],
    },
)
ListTagsForResourceInputRequestTypeDef = TypedDict(
    "ListTagsForResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
NetworkTypeDef = TypedDict(
    "NetworkTypeDef",
    {
        "ASName": str,
        "ASNumber": int,
    },
)
RoundTripTimeTypeDef = TypedDict(
    "RoundTripTimeTypeDef",
    {
        "P50": NotRequired[float],
        "P90": NotRequired[float],
        "P95": NotRequired[float],
    },
)
StopQueryInputRequestTypeDef = TypedDict(
    "StopQueryInputRequestTypeDef",
    {
        "MonitorName": str,
        "QueryId": str,
    },
)
TagResourceInputRequestTypeDef = TypedDict(
    "TagResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Mapping[str, str],
    },
)
UntagResourceInputRequestTypeDef = TypedDict(
    "UntagResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)
CreateMonitorOutputTypeDef = TypedDict(
    "CreateMonitorOutputTypeDef",
    {
        "Arn": str,
        "Status": MonitorConfigStateType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetQueryStatusOutputTypeDef = TypedDict(
    "GetQueryStatusOutputTypeDef",
    {
        "Status": QueryStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartQueryOutputTypeDef = TypedDict(
    "StartQueryOutputTypeDef",
    {
        "QueryId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateMonitorOutputTypeDef = TypedDict(
    "UpdateMonitorOutputTypeDef",
    {
        "MonitorArn": str,
        "Status": MonitorConfigStateType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetQueryResultsOutputTypeDef = TypedDict(
    "GetQueryResultsOutputTypeDef",
    {
        "Fields": List[QueryFieldTypeDef],
        "Data": List[List[str]],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
HealthEventsConfigTypeDef = TypedDict(
    "HealthEventsConfigTypeDef",
    {
        "AvailabilityScoreThreshold": NotRequired[float],
        "PerformanceScoreThreshold": NotRequired[float],
        "AvailabilityLocalHealthEventsConfig": NotRequired[LocalHealthEventsConfigTypeDef],
        "PerformanceLocalHealthEventsConfig": NotRequired[LocalHealthEventsConfigTypeDef],
    },
)
InternetMeasurementsLogDeliveryTypeDef = TypedDict(
    "InternetMeasurementsLogDeliveryTypeDef",
    {
        "S3Config": NotRequired[S3ConfigTypeDef],
    },
)
ListMonitorsInputListMonitorsPaginateTypeDef = TypedDict(
    "ListMonitorsInputListMonitorsPaginateTypeDef",
    {
        "MonitorStatus": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListHealthEventsInputListHealthEventsPaginateTypeDef = TypedDict(
    "ListHealthEventsInputListHealthEventsPaginateTypeDef",
    {
        "MonitorName": str,
        "StartTime": NotRequired[TimestampTypeDef],
        "EndTime": NotRequired[TimestampTypeDef],
        "EventStatus": NotRequired[HealthEventStatusType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListHealthEventsInputRequestTypeDef = TypedDict(
    "ListHealthEventsInputRequestTypeDef",
    {
        "MonitorName": str,
        "StartTime": NotRequired[TimestampTypeDef],
        "EndTime": NotRequired[TimestampTypeDef],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "EventStatus": NotRequired[HealthEventStatusType],
    },
)
StartQueryInputRequestTypeDef = TypedDict(
    "StartQueryInputRequestTypeDef",
    {
        "MonitorName": str,
        "StartTime": TimestampTypeDef,
        "EndTime": TimestampTypeDef,
        "QueryType": QueryTypeType,
        "FilterParameters": NotRequired[Sequence[FilterParameterTypeDef]],
    },
)
ListMonitorsOutputTypeDef = TypedDict(
    "ListMonitorsOutputTypeDef",
    {
        "Monitors": List[MonitorTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
NetworkImpairmentTypeDef = TypedDict(
    "NetworkImpairmentTypeDef",
    {
        "Networks": List[NetworkTypeDef],
        "AsPath": List[NetworkTypeDef],
        "NetworkEventType": TriangulationEventTypeType,
    },
)
PerformanceMeasurementTypeDef = TypedDict(
    "PerformanceMeasurementTypeDef",
    {
        "ExperienceScore": NotRequired[float],
        "PercentOfTotalTrafficImpacted": NotRequired[float],
        "PercentOfClientLocationImpacted": NotRequired[float],
        "RoundTripTime": NotRequired[RoundTripTimeTypeDef],
    },
)
CreateMonitorInputRequestTypeDef = TypedDict(
    "CreateMonitorInputRequestTypeDef",
    {
        "MonitorName": str,
        "Resources": NotRequired[Sequence[str]],
        "ClientToken": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
        "MaxCityNetworksToMonitor": NotRequired[int],
        "InternetMeasurementsLogDelivery": NotRequired[InternetMeasurementsLogDeliveryTypeDef],
        "TrafficPercentageToMonitor": NotRequired[int],
        "HealthEventsConfig": NotRequired[HealthEventsConfigTypeDef],
    },
)
GetMonitorOutputTypeDef = TypedDict(
    "GetMonitorOutputTypeDef",
    {
        "MonitorName": str,
        "MonitorArn": str,
        "Resources": List[str],
        "Status": MonitorConfigStateType,
        "CreatedAt": datetime,
        "ModifiedAt": datetime,
        "ProcessingStatus": MonitorProcessingStatusCodeType,
        "ProcessingStatusInfo": str,
        "Tags": Dict[str, str],
        "MaxCityNetworksToMonitor": int,
        "InternetMeasurementsLogDelivery": InternetMeasurementsLogDeliveryTypeDef,
        "TrafficPercentageToMonitor": int,
        "HealthEventsConfig": HealthEventsConfigTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateMonitorInputRequestTypeDef = TypedDict(
    "UpdateMonitorInputRequestTypeDef",
    {
        "MonitorName": str,
        "ResourcesToAdd": NotRequired[Sequence[str]],
        "ResourcesToRemove": NotRequired[Sequence[str]],
        "Status": NotRequired[MonitorConfigStateType],
        "ClientToken": NotRequired[str],
        "MaxCityNetworksToMonitor": NotRequired[int],
        "InternetMeasurementsLogDelivery": NotRequired[InternetMeasurementsLogDeliveryTypeDef],
        "TrafficPercentageToMonitor": NotRequired[int],
        "HealthEventsConfig": NotRequired[HealthEventsConfigTypeDef],
    },
)
InternetHealthTypeDef = TypedDict(
    "InternetHealthTypeDef",
    {
        "Availability": NotRequired[AvailabilityMeasurementTypeDef],
        "Performance": NotRequired[PerformanceMeasurementTypeDef],
    },
)
ImpactedLocationTypeDef = TypedDict(
    "ImpactedLocationTypeDef",
    {
        "ASName": str,
        "ASNumber": int,
        "Country": str,
        "Status": HealthEventStatusType,
        "Subdivision": NotRequired[str],
        "Metro": NotRequired[str],
        "City": NotRequired[str],
        "Latitude": NotRequired[float],
        "Longitude": NotRequired[float],
        "CountryCode": NotRequired[str],
        "SubdivisionCode": NotRequired[str],
        "ServiceLocation": NotRequired[str],
        "CausedBy": NotRequired[NetworkImpairmentTypeDef],
        "InternetHealth": NotRequired[InternetHealthTypeDef],
    },
)
GetHealthEventOutputTypeDef = TypedDict(
    "GetHealthEventOutputTypeDef",
    {
        "EventArn": str,
        "EventId": str,
        "StartedAt": datetime,
        "EndedAt": datetime,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "ImpactedLocations": List[ImpactedLocationTypeDef],
        "Status": HealthEventStatusType,
        "PercentOfTotalTrafficImpacted": float,
        "ImpactType": HealthEventImpactTypeType,
        "HealthScoreThreshold": float,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
HealthEventTypeDef = TypedDict(
    "HealthEventTypeDef",
    {
        "EventArn": str,
        "EventId": str,
        "StartedAt": datetime,
        "LastUpdatedAt": datetime,
        "ImpactedLocations": List[ImpactedLocationTypeDef],
        "Status": HealthEventStatusType,
        "ImpactType": HealthEventImpactTypeType,
        "EndedAt": NotRequired[datetime],
        "CreatedAt": NotRequired[datetime],
        "PercentOfTotalTrafficImpacted": NotRequired[float],
        "HealthScoreThreshold": NotRequired[float],
    },
)
ListHealthEventsOutputTypeDef = TypedDict(
    "ListHealthEventsOutputTypeDef",
    {
        "HealthEvents": List[HealthEventTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
