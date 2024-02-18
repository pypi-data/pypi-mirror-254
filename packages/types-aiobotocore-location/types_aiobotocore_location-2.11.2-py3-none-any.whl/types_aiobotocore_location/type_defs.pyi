"""
Type annotations for location service type definitions.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_location/type_defs/)

Usage::

    ```python
    from types_aiobotocore_location.type_defs import ApiKeyFilterTypeDef

    data: ApiKeyFilterTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from aiobotocore.response import StreamingBody

from .literals import (
    BatchItemErrorCodeType,
    DimensionUnitType,
    DistanceUnitType,
    IntendedUseType,
    OptimizationModeType,
    PositionFilteringType,
    PricingPlanType,
    RouteMatrixErrorCodeType,
    StatusType,
    TravelModeType,
    VehicleWeightUnitType,
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
    "ApiKeyFilterTypeDef",
    "ApiKeyRestrictionsPaginatorTypeDef",
    "ApiKeyRestrictionsTypeDef",
    "AssociateTrackerConsumerRequestRequestTypeDef",
    "BatchItemErrorTypeDef",
    "BatchDeleteDevicePositionHistoryRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "BatchDeleteGeofenceRequestRequestTypeDef",
    "BatchGetDevicePositionRequestRequestTypeDef",
    "BatchPutGeofenceSuccessTypeDef",
    "CalculateRouteCarModeOptionsTypeDef",
    "TimestampTypeDef",
    "CalculateRouteMatrixSummaryTypeDef",
    "CalculateRouteSummaryTypeDef",
    "TruckDimensionsTypeDef",
    "TruckWeightTypeDef",
    "CirclePaginatorTypeDef",
    "CircleTypeDef",
    "CreateGeofenceCollectionRequestRequestTypeDef",
    "MapConfigurationTypeDef",
    "DataSourceConfigurationTypeDef",
    "CreateRouteCalculatorRequestRequestTypeDef",
    "CreateTrackerRequestRequestTypeDef",
    "DeleteGeofenceCollectionRequestRequestTypeDef",
    "DeleteKeyRequestRequestTypeDef",
    "DeleteMapRequestRequestTypeDef",
    "DeletePlaceIndexRequestRequestTypeDef",
    "DeleteRouteCalculatorRequestRequestTypeDef",
    "DeleteTrackerRequestRequestTypeDef",
    "DescribeGeofenceCollectionRequestRequestTypeDef",
    "DescribeKeyRequestRequestTypeDef",
    "DescribeMapRequestRequestTypeDef",
    "DescribePlaceIndexRequestRequestTypeDef",
    "DescribeRouteCalculatorRequestRequestTypeDef",
    "DescribeTrackerRequestRequestTypeDef",
    "PositionalAccuracyTypeDef",
    "DisassociateTrackerConsumerRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "GetDevicePositionRequestRequestTypeDef",
    "GetGeofenceRequestRequestTypeDef",
    "GetMapGlyphsRequestRequestTypeDef",
    "GetMapSpritesRequestRequestTypeDef",
    "GetMapStyleDescriptorRequestRequestTypeDef",
    "GetMapTileRequestRequestTypeDef",
    "GetPlaceRequestRequestTypeDef",
    "LegGeometryTypeDef",
    "StepTypeDef",
    "TrackingFilterGeometryTypeDef",
    "ListGeofenceCollectionsRequestRequestTypeDef",
    "ListGeofenceCollectionsResponseEntryTypeDef",
    "ListGeofencesRequestRequestTypeDef",
    "ListMapsRequestRequestTypeDef",
    "ListMapsResponseEntryTypeDef",
    "ListPlaceIndexesRequestRequestTypeDef",
    "ListPlaceIndexesResponseEntryTypeDef",
    "ListRouteCalculatorsRequestRequestTypeDef",
    "ListRouteCalculatorsResponseEntryTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTrackerConsumersRequestRequestTypeDef",
    "ListTrackersRequestRequestTypeDef",
    "ListTrackersResponseEntryTypeDef",
    "MapConfigurationUpdateTypeDef",
    "PlaceGeometryTypeDef",
    "TimeZoneTypeDef",
    "RouteMatrixEntryErrorTypeDef",
    "SearchForSuggestionsResultTypeDef",
    "SearchPlaceIndexForPositionRequestRequestTypeDef",
    "SearchPlaceIndexForPositionSummaryTypeDef",
    "SearchPlaceIndexForSuggestionsRequestRequestTypeDef",
    "SearchPlaceIndexForSuggestionsSummaryTypeDef",
    "SearchPlaceIndexForTextRequestRequestTypeDef",
    "SearchPlaceIndexForTextSummaryTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateGeofenceCollectionRequestRequestTypeDef",
    "UpdateRouteCalculatorRequestRequestTypeDef",
    "UpdateTrackerRequestRequestTypeDef",
    "ListKeysRequestRequestTypeDef",
    "ListKeysResponseEntryPaginatorTypeDef",
    "ListKeysResponseEntryTypeDef",
    "BatchDeleteDevicePositionHistoryErrorTypeDef",
    "BatchDeleteGeofenceErrorTypeDef",
    "BatchEvaluateGeofencesErrorTypeDef",
    "BatchGetDevicePositionErrorTypeDef",
    "BatchPutGeofenceErrorTypeDef",
    "BatchUpdateDevicePositionErrorTypeDef",
    "CreateGeofenceCollectionResponseTypeDef",
    "CreateKeyResponseTypeDef",
    "CreateMapResponseTypeDef",
    "CreatePlaceIndexResponseTypeDef",
    "CreateRouteCalculatorResponseTypeDef",
    "CreateTrackerResponseTypeDef",
    "DescribeGeofenceCollectionResponseTypeDef",
    "DescribeKeyResponseTypeDef",
    "DescribeRouteCalculatorResponseTypeDef",
    "DescribeTrackerResponseTypeDef",
    "GetMapGlyphsResponseTypeDef",
    "GetMapSpritesResponseTypeDef",
    "GetMapStyleDescriptorResponseTypeDef",
    "GetMapTileResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTrackerConsumersResponseTypeDef",
    "PutGeofenceResponseTypeDef",
    "UpdateGeofenceCollectionResponseTypeDef",
    "UpdateKeyResponseTypeDef",
    "UpdateMapResponseTypeDef",
    "UpdatePlaceIndexResponseTypeDef",
    "UpdateRouteCalculatorResponseTypeDef",
    "UpdateTrackerResponseTypeDef",
    "CreateKeyRequestRequestTypeDef",
    "GetDevicePositionHistoryRequestRequestTypeDef",
    "UpdateKeyRequestRequestTypeDef",
    "CalculateRouteTruckModeOptionsTypeDef",
    "GeofenceGeometryPaginatorTypeDef",
    "GeofenceGeometryTypeDef",
    "CreateMapRequestRequestTypeDef",
    "DescribeMapResponseTypeDef",
    "CreatePlaceIndexRequestRequestTypeDef",
    "DescribePlaceIndexResponseTypeDef",
    "UpdatePlaceIndexRequestRequestTypeDef",
    "DevicePositionTypeDef",
    "DevicePositionUpdateTypeDef",
    "GetDevicePositionResponseTypeDef",
    "ListDevicePositionsResponseEntryTypeDef",
    "GetDevicePositionHistoryRequestGetDevicePositionHistoryPaginateTypeDef",
    "ListGeofenceCollectionsRequestListGeofenceCollectionsPaginateTypeDef",
    "ListGeofencesRequestListGeofencesPaginateTypeDef",
    "ListKeysRequestListKeysPaginateTypeDef",
    "ListMapsRequestListMapsPaginateTypeDef",
    "ListPlaceIndexesRequestListPlaceIndexesPaginateTypeDef",
    "ListRouteCalculatorsRequestListRouteCalculatorsPaginateTypeDef",
    "ListTrackerConsumersRequestListTrackerConsumersPaginateTypeDef",
    "ListTrackersRequestListTrackersPaginateTypeDef",
    "LegTypeDef",
    "ListDevicePositionsRequestListDevicePositionsPaginateTypeDef",
    "ListDevicePositionsRequestRequestTypeDef",
    "ListGeofenceCollectionsResponseTypeDef",
    "ListMapsResponseTypeDef",
    "ListPlaceIndexesResponseTypeDef",
    "ListRouteCalculatorsResponseTypeDef",
    "ListTrackersResponseTypeDef",
    "UpdateMapRequestRequestTypeDef",
    "PlaceTypeDef",
    "RouteMatrixEntryTypeDef",
    "SearchPlaceIndexForSuggestionsResponseTypeDef",
    "ListKeysResponsePaginatorTypeDef",
    "ListKeysResponseTypeDef",
    "BatchDeleteDevicePositionHistoryResponseTypeDef",
    "BatchDeleteGeofenceResponseTypeDef",
    "BatchEvaluateGeofencesResponseTypeDef",
    "BatchPutGeofenceResponseTypeDef",
    "BatchUpdateDevicePositionResponseTypeDef",
    "CalculateRouteMatrixRequestRequestTypeDef",
    "CalculateRouteRequestRequestTypeDef",
    "ListGeofenceResponseEntryPaginatorTypeDef",
    "BatchPutGeofenceRequestEntryTypeDef",
    "GetGeofenceResponseTypeDef",
    "ListGeofenceResponseEntryTypeDef",
    "PutGeofenceRequestRequestTypeDef",
    "BatchGetDevicePositionResponseTypeDef",
    "GetDevicePositionHistoryResponseTypeDef",
    "BatchEvaluateGeofencesRequestRequestTypeDef",
    "BatchUpdateDevicePositionRequestRequestTypeDef",
    "ListDevicePositionsResponseTypeDef",
    "CalculateRouteResponseTypeDef",
    "GetPlaceResponseTypeDef",
    "SearchForPositionResultTypeDef",
    "SearchForTextResultTypeDef",
    "CalculateRouteMatrixResponseTypeDef",
    "ListGeofencesResponsePaginatorTypeDef",
    "BatchPutGeofenceRequestRequestTypeDef",
    "ListGeofencesResponseTypeDef",
    "SearchPlaceIndexForPositionResponseTypeDef",
    "SearchPlaceIndexForTextResponseTypeDef",
)

ApiKeyFilterTypeDef = TypedDict(
    "ApiKeyFilterTypeDef",
    {
        "KeyStatus": NotRequired[StatusType],
    },
)
ApiKeyRestrictionsPaginatorTypeDef = TypedDict(
    "ApiKeyRestrictionsPaginatorTypeDef",
    {
        "AllowActions": List[str],
        "AllowResources": List[str],
        "AllowReferers": NotRequired[List[str]],
    },
)
ApiKeyRestrictionsTypeDef = TypedDict(
    "ApiKeyRestrictionsTypeDef",
    {
        "AllowActions": Sequence[str],
        "AllowResources": Sequence[str],
        "AllowReferers": NotRequired[Sequence[str]],
    },
)
AssociateTrackerConsumerRequestRequestTypeDef = TypedDict(
    "AssociateTrackerConsumerRequestRequestTypeDef",
    {
        "ConsumerArn": str,
        "TrackerName": str,
    },
)
BatchItemErrorTypeDef = TypedDict(
    "BatchItemErrorTypeDef",
    {
        "Code": NotRequired[BatchItemErrorCodeType],
        "Message": NotRequired[str],
    },
)
BatchDeleteDevicePositionHistoryRequestRequestTypeDef = TypedDict(
    "BatchDeleteDevicePositionHistoryRequestRequestTypeDef",
    {
        "DeviceIds": Sequence[str],
        "TrackerName": str,
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
BatchDeleteGeofenceRequestRequestTypeDef = TypedDict(
    "BatchDeleteGeofenceRequestRequestTypeDef",
    {
        "CollectionName": str,
        "GeofenceIds": Sequence[str],
    },
)
BatchGetDevicePositionRequestRequestTypeDef = TypedDict(
    "BatchGetDevicePositionRequestRequestTypeDef",
    {
        "DeviceIds": Sequence[str],
        "TrackerName": str,
    },
)
BatchPutGeofenceSuccessTypeDef = TypedDict(
    "BatchPutGeofenceSuccessTypeDef",
    {
        "CreateTime": datetime,
        "GeofenceId": str,
        "UpdateTime": datetime,
    },
)
CalculateRouteCarModeOptionsTypeDef = TypedDict(
    "CalculateRouteCarModeOptionsTypeDef",
    {
        "AvoidFerries": NotRequired[bool],
        "AvoidTolls": NotRequired[bool],
    },
)
TimestampTypeDef = Union[datetime, str]
CalculateRouteMatrixSummaryTypeDef = TypedDict(
    "CalculateRouteMatrixSummaryTypeDef",
    {
        "DataSource": str,
        "DistanceUnit": DistanceUnitType,
        "ErrorCount": int,
        "RouteCount": int,
    },
)
CalculateRouteSummaryTypeDef = TypedDict(
    "CalculateRouteSummaryTypeDef",
    {
        "DataSource": str,
        "Distance": float,
        "DistanceUnit": DistanceUnitType,
        "DurationSeconds": float,
        "RouteBBox": List[float],
    },
)
TruckDimensionsTypeDef = TypedDict(
    "TruckDimensionsTypeDef",
    {
        "Height": NotRequired[float],
        "Length": NotRequired[float],
        "Unit": NotRequired[DimensionUnitType],
        "Width": NotRequired[float],
    },
)
TruckWeightTypeDef = TypedDict(
    "TruckWeightTypeDef",
    {
        "Total": NotRequired[float],
        "Unit": NotRequired[VehicleWeightUnitType],
    },
)
CirclePaginatorTypeDef = TypedDict(
    "CirclePaginatorTypeDef",
    {
        "Center": List[float],
        "Radius": float,
    },
)
CircleTypeDef = TypedDict(
    "CircleTypeDef",
    {
        "Center": Sequence[float],
        "Radius": float,
    },
)
CreateGeofenceCollectionRequestRequestTypeDef = TypedDict(
    "CreateGeofenceCollectionRequestRequestTypeDef",
    {
        "CollectionName": str,
        "Description": NotRequired[str],
        "KmsKeyId": NotRequired[str],
        "PricingPlan": NotRequired[PricingPlanType],
        "PricingPlanDataSource": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
MapConfigurationTypeDef = TypedDict(
    "MapConfigurationTypeDef",
    {
        "Style": str,
        "CustomLayers": NotRequired[Sequence[str]],
        "PoliticalView": NotRequired[str],
    },
)
DataSourceConfigurationTypeDef = TypedDict(
    "DataSourceConfigurationTypeDef",
    {
        "IntendedUse": NotRequired[IntendedUseType],
    },
)
CreateRouteCalculatorRequestRequestTypeDef = TypedDict(
    "CreateRouteCalculatorRequestRequestTypeDef",
    {
        "CalculatorName": str,
        "DataSource": str,
        "Description": NotRequired[str],
        "PricingPlan": NotRequired[PricingPlanType],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
CreateTrackerRequestRequestTypeDef = TypedDict(
    "CreateTrackerRequestRequestTypeDef",
    {
        "TrackerName": str,
        "Description": NotRequired[str],
        "EventBridgeEnabled": NotRequired[bool],
        "KmsKeyEnableGeospatialQueries": NotRequired[bool],
        "KmsKeyId": NotRequired[str],
        "PositionFiltering": NotRequired[PositionFilteringType],
        "PricingPlan": NotRequired[PricingPlanType],
        "PricingPlanDataSource": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
DeleteGeofenceCollectionRequestRequestTypeDef = TypedDict(
    "DeleteGeofenceCollectionRequestRequestTypeDef",
    {
        "CollectionName": str,
    },
)
DeleteKeyRequestRequestTypeDef = TypedDict(
    "DeleteKeyRequestRequestTypeDef",
    {
        "KeyName": str,
        "ForceDelete": NotRequired[bool],
    },
)
DeleteMapRequestRequestTypeDef = TypedDict(
    "DeleteMapRequestRequestTypeDef",
    {
        "MapName": str,
    },
)
DeletePlaceIndexRequestRequestTypeDef = TypedDict(
    "DeletePlaceIndexRequestRequestTypeDef",
    {
        "IndexName": str,
    },
)
DeleteRouteCalculatorRequestRequestTypeDef = TypedDict(
    "DeleteRouteCalculatorRequestRequestTypeDef",
    {
        "CalculatorName": str,
    },
)
DeleteTrackerRequestRequestTypeDef = TypedDict(
    "DeleteTrackerRequestRequestTypeDef",
    {
        "TrackerName": str,
    },
)
DescribeGeofenceCollectionRequestRequestTypeDef = TypedDict(
    "DescribeGeofenceCollectionRequestRequestTypeDef",
    {
        "CollectionName": str,
    },
)
DescribeKeyRequestRequestTypeDef = TypedDict(
    "DescribeKeyRequestRequestTypeDef",
    {
        "KeyName": str,
    },
)
DescribeMapRequestRequestTypeDef = TypedDict(
    "DescribeMapRequestRequestTypeDef",
    {
        "MapName": str,
    },
)
DescribePlaceIndexRequestRequestTypeDef = TypedDict(
    "DescribePlaceIndexRequestRequestTypeDef",
    {
        "IndexName": str,
    },
)
DescribeRouteCalculatorRequestRequestTypeDef = TypedDict(
    "DescribeRouteCalculatorRequestRequestTypeDef",
    {
        "CalculatorName": str,
    },
)
DescribeTrackerRequestRequestTypeDef = TypedDict(
    "DescribeTrackerRequestRequestTypeDef",
    {
        "TrackerName": str,
    },
)
PositionalAccuracyTypeDef = TypedDict(
    "PositionalAccuracyTypeDef",
    {
        "Horizontal": float,
    },
)
DisassociateTrackerConsumerRequestRequestTypeDef = TypedDict(
    "DisassociateTrackerConsumerRequestRequestTypeDef",
    {
        "ConsumerArn": str,
        "TrackerName": str,
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
GetDevicePositionRequestRequestTypeDef = TypedDict(
    "GetDevicePositionRequestRequestTypeDef",
    {
        "DeviceId": str,
        "TrackerName": str,
    },
)
GetGeofenceRequestRequestTypeDef = TypedDict(
    "GetGeofenceRequestRequestTypeDef",
    {
        "CollectionName": str,
        "GeofenceId": str,
    },
)
GetMapGlyphsRequestRequestTypeDef = TypedDict(
    "GetMapGlyphsRequestRequestTypeDef",
    {
        "FontStack": str,
        "FontUnicodeRange": str,
        "MapName": str,
        "Key": NotRequired[str],
    },
)
GetMapSpritesRequestRequestTypeDef = TypedDict(
    "GetMapSpritesRequestRequestTypeDef",
    {
        "FileName": str,
        "MapName": str,
        "Key": NotRequired[str],
    },
)
GetMapStyleDescriptorRequestRequestTypeDef = TypedDict(
    "GetMapStyleDescriptorRequestRequestTypeDef",
    {
        "MapName": str,
        "Key": NotRequired[str],
    },
)
GetMapTileRequestRequestTypeDef = TypedDict(
    "GetMapTileRequestRequestTypeDef",
    {
        "MapName": str,
        "X": str,
        "Y": str,
        "Z": str,
        "Key": NotRequired[str],
    },
)
GetPlaceRequestRequestTypeDef = TypedDict(
    "GetPlaceRequestRequestTypeDef",
    {
        "IndexName": str,
        "PlaceId": str,
        "Key": NotRequired[str],
        "Language": NotRequired[str],
    },
)
LegGeometryTypeDef = TypedDict(
    "LegGeometryTypeDef",
    {
        "LineString": NotRequired[List[List[float]]],
    },
)
StepTypeDef = TypedDict(
    "StepTypeDef",
    {
        "Distance": float,
        "DurationSeconds": float,
        "EndPosition": List[float],
        "StartPosition": List[float],
        "GeometryOffset": NotRequired[int],
    },
)
TrackingFilterGeometryTypeDef = TypedDict(
    "TrackingFilterGeometryTypeDef",
    {
        "Polygon": NotRequired[Sequence[Sequence[Sequence[float]]]],
    },
)
ListGeofenceCollectionsRequestRequestTypeDef = TypedDict(
    "ListGeofenceCollectionsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListGeofenceCollectionsResponseEntryTypeDef = TypedDict(
    "ListGeofenceCollectionsResponseEntryTypeDef",
    {
        "CollectionName": str,
        "CreateTime": datetime,
        "Description": str,
        "UpdateTime": datetime,
        "PricingPlan": NotRequired[PricingPlanType],
        "PricingPlanDataSource": NotRequired[str],
    },
)
ListGeofencesRequestRequestTypeDef = TypedDict(
    "ListGeofencesRequestRequestTypeDef",
    {
        "CollectionName": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListMapsRequestRequestTypeDef = TypedDict(
    "ListMapsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListMapsResponseEntryTypeDef = TypedDict(
    "ListMapsResponseEntryTypeDef",
    {
        "CreateTime": datetime,
        "DataSource": str,
        "Description": str,
        "MapName": str,
        "UpdateTime": datetime,
        "PricingPlan": NotRequired[PricingPlanType],
    },
)
ListPlaceIndexesRequestRequestTypeDef = TypedDict(
    "ListPlaceIndexesRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListPlaceIndexesResponseEntryTypeDef = TypedDict(
    "ListPlaceIndexesResponseEntryTypeDef",
    {
        "CreateTime": datetime,
        "DataSource": str,
        "Description": str,
        "IndexName": str,
        "UpdateTime": datetime,
        "PricingPlan": NotRequired[PricingPlanType],
    },
)
ListRouteCalculatorsRequestRequestTypeDef = TypedDict(
    "ListRouteCalculatorsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListRouteCalculatorsResponseEntryTypeDef = TypedDict(
    "ListRouteCalculatorsResponseEntryTypeDef",
    {
        "CalculatorName": str,
        "CreateTime": datetime,
        "DataSource": str,
        "Description": str,
        "UpdateTime": datetime,
        "PricingPlan": NotRequired[PricingPlanType],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
ListTrackerConsumersRequestRequestTypeDef = TypedDict(
    "ListTrackerConsumersRequestRequestTypeDef",
    {
        "TrackerName": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListTrackersRequestRequestTypeDef = TypedDict(
    "ListTrackersRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListTrackersResponseEntryTypeDef = TypedDict(
    "ListTrackersResponseEntryTypeDef",
    {
        "CreateTime": datetime,
        "Description": str,
        "TrackerName": str,
        "UpdateTime": datetime,
        "PricingPlan": NotRequired[PricingPlanType],
        "PricingPlanDataSource": NotRequired[str],
    },
)
MapConfigurationUpdateTypeDef = TypedDict(
    "MapConfigurationUpdateTypeDef",
    {
        "CustomLayers": NotRequired[Sequence[str]],
        "PoliticalView": NotRequired[str],
    },
)
PlaceGeometryTypeDef = TypedDict(
    "PlaceGeometryTypeDef",
    {
        "Point": NotRequired[List[float]],
    },
)
TimeZoneTypeDef = TypedDict(
    "TimeZoneTypeDef",
    {
        "Name": str,
        "Offset": NotRequired[int],
    },
)
RouteMatrixEntryErrorTypeDef = TypedDict(
    "RouteMatrixEntryErrorTypeDef",
    {
        "Code": RouteMatrixErrorCodeType,
        "Message": NotRequired[str],
    },
)
SearchForSuggestionsResultTypeDef = TypedDict(
    "SearchForSuggestionsResultTypeDef",
    {
        "Text": str,
        "Categories": NotRequired[List[str]],
        "PlaceId": NotRequired[str],
        "SupplementalCategories": NotRequired[List[str]],
    },
)
SearchPlaceIndexForPositionRequestRequestTypeDef = TypedDict(
    "SearchPlaceIndexForPositionRequestRequestTypeDef",
    {
        "IndexName": str,
        "Position": Sequence[float],
        "Key": NotRequired[str],
        "Language": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
SearchPlaceIndexForPositionSummaryTypeDef = TypedDict(
    "SearchPlaceIndexForPositionSummaryTypeDef",
    {
        "DataSource": str,
        "Position": List[float],
        "Language": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
SearchPlaceIndexForSuggestionsRequestRequestTypeDef = TypedDict(
    "SearchPlaceIndexForSuggestionsRequestRequestTypeDef",
    {
        "IndexName": str,
        "Text": str,
        "BiasPosition": NotRequired[Sequence[float]],
        "FilterBBox": NotRequired[Sequence[float]],
        "FilterCategories": NotRequired[Sequence[str]],
        "FilterCountries": NotRequired[Sequence[str]],
        "Key": NotRequired[str],
        "Language": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
SearchPlaceIndexForSuggestionsSummaryTypeDef = TypedDict(
    "SearchPlaceIndexForSuggestionsSummaryTypeDef",
    {
        "DataSource": str,
        "Text": str,
        "BiasPosition": NotRequired[List[float]],
        "FilterBBox": NotRequired[List[float]],
        "FilterCategories": NotRequired[List[str]],
        "FilterCountries": NotRequired[List[str]],
        "Language": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
SearchPlaceIndexForTextRequestRequestTypeDef = TypedDict(
    "SearchPlaceIndexForTextRequestRequestTypeDef",
    {
        "IndexName": str,
        "Text": str,
        "BiasPosition": NotRequired[Sequence[float]],
        "FilterBBox": NotRequired[Sequence[float]],
        "FilterCategories": NotRequired[Sequence[str]],
        "FilterCountries": NotRequired[Sequence[str]],
        "Key": NotRequired[str],
        "Language": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
SearchPlaceIndexForTextSummaryTypeDef = TypedDict(
    "SearchPlaceIndexForTextSummaryTypeDef",
    {
        "DataSource": str,
        "Text": str,
        "BiasPosition": NotRequired[List[float]],
        "FilterBBox": NotRequired[List[float]],
        "FilterCategories": NotRequired[List[str]],
        "FilterCountries": NotRequired[List[str]],
        "Language": NotRequired[str],
        "MaxResults": NotRequired[int],
        "ResultBBox": NotRequired[List[float]],
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
UpdateGeofenceCollectionRequestRequestTypeDef = TypedDict(
    "UpdateGeofenceCollectionRequestRequestTypeDef",
    {
        "CollectionName": str,
        "Description": NotRequired[str],
        "PricingPlan": NotRequired[PricingPlanType],
        "PricingPlanDataSource": NotRequired[str],
    },
)
UpdateRouteCalculatorRequestRequestTypeDef = TypedDict(
    "UpdateRouteCalculatorRequestRequestTypeDef",
    {
        "CalculatorName": str,
        "Description": NotRequired[str],
        "PricingPlan": NotRequired[PricingPlanType],
    },
)
UpdateTrackerRequestRequestTypeDef = TypedDict(
    "UpdateTrackerRequestRequestTypeDef",
    {
        "TrackerName": str,
        "Description": NotRequired[str],
        "EventBridgeEnabled": NotRequired[bool],
        "KmsKeyEnableGeospatialQueries": NotRequired[bool],
        "PositionFiltering": NotRequired[PositionFilteringType],
        "PricingPlan": NotRequired[PricingPlanType],
        "PricingPlanDataSource": NotRequired[str],
    },
)
ListKeysRequestRequestTypeDef = TypedDict(
    "ListKeysRequestRequestTypeDef",
    {
        "Filter": NotRequired[ApiKeyFilterTypeDef],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListKeysResponseEntryPaginatorTypeDef = TypedDict(
    "ListKeysResponseEntryPaginatorTypeDef",
    {
        "CreateTime": datetime,
        "ExpireTime": datetime,
        "KeyName": str,
        "Restrictions": ApiKeyRestrictionsPaginatorTypeDef,
        "UpdateTime": datetime,
        "Description": NotRequired[str],
    },
)
ListKeysResponseEntryTypeDef = TypedDict(
    "ListKeysResponseEntryTypeDef",
    {
        "CreateTime": datetime,
        "ExpireTime": datetime,
        "KeyName": str,
        "Restrictions": ApiKeyRestrictionsTypeDef,
        "UpdateTime": datetime,
        "Description": NotRequired[str],
    },
)
BatchDeleteDevicePositionHistoryErrorTypeDef = TypedDict(
    "BatchDeleteDevicePositionHistoryErrorTypeDef",
    {
        "DeviceId": str,
        "Error": BatchItemErrorTypeDef,
    },
)
BatchDeleteGeofenceErrorTypeDef = TypedDict(
    "BatchDeleteGeofenceErrorTypeDef",
    {
        "Error": BatchItemErrorTypeDef,
        "GeofenceId": str,
    },
)
BatchEvaluateGeofencesErrorTypeDef = TypedDict(
    "BatchEvaluateGeofencesErrorTypeDef",
    {
        "DeviceId": str,
        "Error": BatchItemErrorTypeDef,
        "SampleTime": datetime,
    },
)
BatchGetDevicePositionErrorTypeDef = TypedDict(
    "BatchGetDevicePositionErrorTypeDef",
    {
        "DeviceId": str,
        "Error": BatchItemErrorTypeDef,
    },
)
BatchPutGeofenceErrorTypeDef = TypedDict(
    "BatchPutGeofenceErrorTypeDef",
    {
        "Error": BatchItemErrorTypeDef,
        "GeofenceId": str,
    },
)
BatchUpdateDevicePositionErrorTypeDef = TypedDict(
    "BatchUpdateDevicePositionErrorTypeDef",
    {
        "DeviceId": str,
        "Error": BatchItemErrorTypeDef,
        "SampleTime": datetime,
    },
)
CreateGeofenceCollectionResponseTypeDef = TypedDict(
    "CreateGeofenceCollectionResponseTypeDef",
    {
        "CollectionArn": str,
        "CollectionName": str,
        "CreateTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateKeyResponseTypeDef = TypedDict(
    "CreateKeyResponseTypeDef",
    {
        "CreateTime": datetime,
        "Key": str,
        "KeyArn": str,
        "KeyName": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateMapResponseTypeDef = TypedDict(
    "CreateMapResponseTypeDef",
    {
        "CreateTime": datetime,
        "MapArn": str,
        "MapName": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreatePlaceIndexResponseTypeDef = TypedDict(
    "CreatePlaceIndexResponseTypeDef",
    {
        "CreateTime": datetime,
        "IndexArn": str,
        "IndexName": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateRouteCalculatorResponseTypeDef = TypedDict(
    "CreateRouteCalculatorResponseTypeDef",
    {
        "CalculatorArn": str,
        "CalculatorName": str,
        "CreateTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateTrackerResponseTypeDef = TypedDict(
    "CreateTrackerResponseTypeDef",
    {
        "CreateTime": datetime,
        "TrackerArn": str,
        "TrackerName": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeGeofenceCollectionResponseTypeDef = TypedDict(
    "DescribeGeofenceCollectionResponseTypeDef",
    {
        "CollectionArn": str,
        "CollectionName": str,
        "CreateTime": datetime,
        "Description": str,
        "GeofenceCount": int,
        "KmsKeyId": str,
        "PricingPlan": PricingPlanType,
        "PricingPlanDataSource": str,
        "Tags": Dict[str, str],
        "UpdateTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeKeyResponseTypeDef = TypedDict(
    "DescribeKeyResponseTypeDef",
    {
        "CreateTime": datetime,
        "Description": str,
        "ExpireTime": datetime,
        "Key": str,
        "KeyArn": str,
        "KeyName": str,
        "Restrictions": ApiKeyRestrictionsTypeDef,
        "Tags": Dict[str, str],
        "UpdateTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeRouteCalculatorResponseTypeDef = TypedDict(
    "DescribeRouteCalculatorResponseTypeDef",
    {
        "CalculatorArn": str,
        "CalculatorName": str,
        "CreateTime": datetime,
        "DataSource": str,
        "Description": str,
        "PricingPlan": PricingPlanType,
        "Tags": Dict[str, str],
        "UpdateTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeTrackerResponseTypeDef = TypedDict(
    "DescribeTrackerResponseTypeDef",
    {
        "CreateTime": datetime,
        "Description": str,
        "EventBridgeEnabled": bool,
        "KmsKeyEnableGeospatialQueries": bool,
        "KmsKeyId": str,
        "PositionFiltering": PositionFilteringType,
        "PricingPlan": PricingPlanType,
        "PricingPlanDataSource": str,
        "Tags": Dict[str, str],
        "TrackerArn": str,
        "TrackerName": str,
        "UpdateTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetMapGlyphsResponseTypeDef = TypedDict(
    "GetMapGlyphsResponseTypeDef",
    {
        "Blob": StreamingBody,
        "CacheControl": str,
        "ContentType": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetMapSpritesResponseTypeDef = TypedDict(
    "GetMapSpritesResponseTypeDef",
    {
        "Blob": StreamingBody,
        "CacheControl": str,
        "ContentType": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetMapStyleDescriptorResponseTypeDef = TypedDict(
    "GetMapStyleDescriptorResponseTypeDef",
    {
        "Blob": StreamingBody,
        "CacheControl": str,
        "ContentType": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetMapTileResponseTypeDef = TypedDict(
    "GetMapTileResponseTypeDef",
    {
        "Blob": StreamingBody,
        "CacheControl": str,
        "ContentType": str,
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
ListTrackerConsumersResponseTypeDef = TypedDict(
    "ListTrackerConsumersResponseTypeDef",
    {
        "ConsumerArns": List[str],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutGeofenceResponseTypeDef = TypedDict(
    "PutGeofenceResponseTypeDef",
    {
        "CreateTime": datetime,
        "GeofenceId": str,
        "UpdateTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateGeofenceCollectionResponseTypeDef = TypedDict(
    "UpdateGeofenceCollectionResponseTypeDef",
    {
        "CollectionArn": str,
        "CollectionName": str,
        "UpdateTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateKeyResponseTypeDef = TypedDict(
    "UpdateKeyResponseTypeDef",
    {
        "KeyArn": str,
        "KeyName": str,
        "UpdateTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateMapResponseTypeDef = TypedDict(
    "UpdateMapResponseTypeDef",
    {
        "MapArn": str,
        "MapName": str,
        "UpdateTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdatePlaceIndexResponseTypeDef = TypedDict(
    "UpdatePlaceIndexResponseTypeDef",
    {
        "IndexArn": str,
        "IndexName": str,
        "UpdateTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateRouteCalculatorResponseTypeDef = TypedDict(
    "UpdateRouteCalculatorResponseTypeDef",
    {
        "CalculatorArn": str,
        "CalculatorName": str,
        "UpdateTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateTrackerResponseTypeDef = TypedDict(
    "UpdateTrackerResponseTypeDef",
    {
        "TrackerArn": str,
        "TrackerName": str,
        "UpdateTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateKeyRequestRequestTypeDef = TypedDict(
    "CreateKeyRequestRequestTypeDef",
    {
        "KeyName": str,
        "Restrictions": ApiKeyRestrictionsTypeDef,
        "Description": NotRequired[str],
        "ExpireTime": NotRequired[TimestampTypeDef],
        "NoExpiry": NotRequired[bool],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
GetDevicePositionHistoryRequestRequestTypeDef = TypedDict(
    "GetDevicePositionHistoryRequestRequestTypeDef",
    {
        "DeviceId": str,
        "TrackerName": str,
        "EndTimeExclusive": NotRequired[TimestampTypeDef],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "StartTimeInclusive": NotRequired[TimestampTypeDef],
    },
)
UpdateKeyRequestRequestTypeDef = TypedDict(
    "UpdateKeyRequestRequestTypeDef",
    {
        "KeyName": str,
        "Description": NotRequired[str],
        "ExpireTime": NotRequired[TimestampTypeDef],
        "ForceUpdate": NotRequired[bool],
        "NoExpiry": NotRequired[bool],
        "Restrictions": NotRequired[ApiKeyRestrictionsTypeDef],
    },
)
CalculateRouteTruckModeOptionsTypeDef = TypedDict(
    "CalculateRouteTruckModeOptionsTypeDef",
    {
        "AvoidFerries": NotRequired[bool],
        "AvoidTolls": NotRequired[bool],
        "Dimensions": NotRequired[TruckDimensionsTypeDef],
        "Weight": NotRequired[TruckWeightTypeDef],
    },
)
GeofenceGeometryPaginatorTypeDef = TypedDict(
    "GeofenceGeometryPaginatorTypeDef",
    {
        "Circle": NotRequired[CirclePaginatorTypeDef],
        "Polygon": NotRequired[List[List[List[float]]]],
    },
)
GeofenceGeometryTypeDef = TypedDict(
    "GeofenceGeometryTypeDef",
    {
        "Circle": NotRequired[CircleTypeDef],
        "Polygon": NotRequired[Sequence[Sequence[Sequence[float]]]],
    },
)
CreateMapRequestRequestTypeDef = TypedDict(
    "CreateMapRequestRequestTypeDef",
    {
        "Configuration": MapConfigurationTypeDef,
        "MapName": str,
        "Description": NotRequired[str],
        "PricingPlan": NotRequired[PricingPlanType],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
DescribeMapResponseTypeDef = TypedDict(
    "DescribeMapResponseTypeDef",
    {
        "Configuration": MapConfigurationTypeDef,
        "CreateTime": datetime,
        "DataSource": str,
        "Description": str,
        "MapArn": str,
        "MapName": str,
        "PricingPlan": PricingPlanType,
        "Tags": Dict[str, str],
        "UpdateTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreatePlaceIndexRequestRequestTypeDef = TypedDict(
    "CreatePlaceIndexRequestRequestTypeDef",
    {
        "DataSource": str,
        "IndexName": str,
        "DataSourceConfiguration": NotRequired[DataSourceConfigurationTypeDef],
        "Description": NotRequired[str],
        "PricingPlan": NotRequired[PricingPlanType],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
DescribePlaceIndexResponseTypeDef = TypedDict(
    "DescribePlaceIndexResponseTypeDef",
    {
        "CreateTime": datetime,
        "DataSource": str,
        "DataSourceConfiguration": DataSourceConfigurationTypeDef,
        "Description": str,
        "IndexArn": str,
        "IndexName": str,
        "PricingPlan": PricingPlanType,
        "Tags": Dict[str, str],
        "UpdateTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdatePlaceIndexRequestRequestTypeDef = TypedDict(
    "UpdatePlaceIndexRequestRequestTypeDef",
    {
        "IndexName": str,
        "DataSourceConfiguration": NotRequired[DataSourceConfigurationTypeDef],
        "Description": NotRequired[str],
        "PricingPlan": NotRequired[PricingPlanType],
    },
)
DevicePositionTypeDef = TypedDict(
    "DevicePositionTypeDef",
    {
        "Position": List[float],
        "ReceivedTime": datetime,
        "SampleTime": datetime,
        "Accuracy": NotRequired[PositionalAccuracyTypeDef],
        "DeviceId": NotRequired[str],
        "PositionProperties": NotRequired[Dict[str, str]],
    },
)
DevicePositionUpdateTypeDef = TypedDict(
    "DevicePositionUpdateTypeDef",
    {
        "DeviceId": str,
        "Position": Sequence[float],
        "SampleTime": TimestampTypeDef,
        "Accuracy": NotRequired[PositionalAccuracyTypeDef],
        "PositionProperties": NotRequired[Mapping[str, str]],
    },
)
GetDevicePositionResponseTypeDef = TypedDict(
    "GetDevicePositionResponseTypeDef",
    {
        "Accuracy": PositionalAccuracyTypeDef,
        "DeviceId": str,
        "Position": List[float],
        "PositionProperties": Dict[str, str],
        "ReceivedTime": datetime,
        "SampleTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListDevicePositionsResponseEntryTypeDef = TypedDict(
    "ListDevicePositionsResponseEntryTypeDef",
    {
        "DeviceId": str,
        "Position": List[float],
        "SampleTime": datetime,
        "Accuracy": NotRequired[PositionalAccuracyTypeDef],
        "PositionProperties": NotRequired[Dict[str, str]],
    },
)
GetDevicePositionHistoryRequestGetDevicePositionHistoryPaginateTypeDef = TypedDict(
    "GetDevicePositionHistoryRequestGetDevicePositionHistoryPaginateTypeDef",
    {
        "DeviceId": str,
        "TrackerName": str,
        "EndTimeExclusive": NotRequired[TimestampTypeDef],
        "StartTimeInclusive": NotRequired[TimestampTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListGeofenceCollectionsRequestListGeofenceCollectionsPaginateTypeDef = TypedDict(
    "ListGeofenceCollectionsRequestListGeofenceCollectionsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListGeofencesRequestListGeofencesPaginateTypeDef = TypedDict(
    "ListGeofencesRequestListGeofencesPaginateTypeDef",
    {
        "CollectionName": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListKeysRequestListKeysPaginateTypeDef = TypedDict(
    "ListKeysRequestListKeysPaginateTypeDef",
    {
        "Filter": NotRequired[ApiKeyFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListMapsRequestListMapsPaginateTypeDef = TypedDict(
    "ListMapsRequestListMapsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListPlaceIndexesRequestListPlaceIndexesPaginateTypeDef = TypedDict(
    "ListPlaceIndexesRequestListPlaceIndexesPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListRouteCalculatorsRequestListRouteCalculatorsPaginateTypeDef = TypedDict(
    "ListRouteCalculatorsRequestListRouteCalculatorsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListTrackerConsumersRequestListTrackerConsumersPaginateTypeDef = TypedDict(
    "ListTrackerConsumersRequestListTrackerConsumersPaginateTypeDef",
    {
        "TrackerName": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListTrackersRequestListTrackersPaginateTypeDef = TypedDict(
    "ListTrackersRequestListTrackersPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
LegTypeDef = TypedDict(
    "LegTypeDef",
    {
        "Distance": float,
        "DurationSeconds": float,
        "EndPosition": List[float],
        "StartPosition": List[float],
        "Steps": List[StepTypeDef],
        "Geometry": NotRequired[LegGeometryTypeDef],
    },
)
ListDevicePositionsRequestListDevicePositionsPaginateTypeDef = TypedDict(
    "ListDevicePositionsRequestListDevicePositionsPaginateTypeDef",
    {
        "TrackerName": str,
        "FilterGeometry": NotRequired[TrackingFilterGeometryTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDevicePositionsRequestRequestTypeDef = TypedDict(
    "ListDevicePositionsRequestRequestTypeDef",
    {
        "TrackerName": str,
        "FilterGeometry": NotRequired[TrackingFilterGeometryTypeDef],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListGeofenceCollectionsResponseTypeDef = TypedDict(
    "ListGeofenceCollectionsResponseTypeDef",
    {
        "Entries": List[ListGeofenceCollectionsResponseEntryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListMapsResponseTypeDef = TypedDict(
    "ListMapsResponseTypeDef",
    {
        "Entries": List[ListMapsResponseEntryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListPlaceIndexesResponseTypeDef = TypedDict(
    "ListPlaceIndexesResponseTypeDef",
    {
        "Entries": List[ListPlaceIndexesResponseEntryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListRouteCalculatorsResponseTypeDef = TypedDict(
    "ListRouteCalculatorsResponseTypeDef",
    {
        "Entries": List[ListRouteCalculatorsResponseEntryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTrackersResponseTypeDef = TypedDict(
    "ListTrackersResponseTypeDef",
    {
        "Entries": List[ListTrackersResponseEntryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateMapRequestRequestTypeDef = TypedDict(
    "UpdateMapRequestRequestTypeDef",
    {
        "MapName": str,
        "ConfigurationUpdate": NotRequired[MapConfigurationUpdateTypeDef],
        "Description": NotRequired[str],
        "PricingPlan": NotRequired[PricingPlanType],
    },
)
PlaceTypeDef = TypedDict(
    "PlaceTypeDef",
    {
        "Geometry": PlaceGeometryTypeDef,
        "AddressNumber": NotRequired[str],
        "Categories": NotRequired[List[str]],
        "Country": NotRequired[str],
        "Interpolated": NotRequired[bool],
        "Label": NotRequired[str],
        "Municipality": NotRequired[str],
        "Neighborhood": NotRequired[str],
        "PostalCode": NotRequired[str],
        "Region": NotRequired[str],
        "Street": NotRequired[str],
        "SubMunicipality": NotRequired[str],
        "SubRegion": NotRequired[str],
        "SupplementalCategories": NotRequired[List[str]],
        "TimeZone": NotRequired[TimeZoneTypeDef],
        "UnitNumber": NotRequired[str],
        "UnitType": NotRequired[str],
    },
)
RouteMatrixEntryTypeDef = TypedDict(
    "RouteMatrixEntryTypeDef",
    {
        "Distance": NotRequired[float],
        "DurationSeconds": NotRequired[float],
        "Error": NotRequired[RouteMatrixEntryErrorTypeDef],
    },
)
SearchPlaceIndexForSuggestionsResponseTypeDef = TypedDict(
    "SearchPlaceIndexForSuggestionsResponseTypeDef",
    {
        "Results": List[SearchForSuggestionsResultTypeDef],
        "Summary": SearchPlaceIndexForSuggestionsSummaryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListKeysResponsePaginatorTypeDef = TypedDict(
    "ListKeysResponsePaginatorTypeDef",
    {
        "Entries": List[ListKeysResponseEntryPaginatorTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListKeysResponseTypeDef = TypedDict(
    "ListKeysResponseTypeDef",
    {
        "Entries": List[ListKeysResponseEntryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchDeleteDevicePositionHistoryResponseTypeDef = TypedDict(
    "BatchDeleteDevicePositionHistoryResponseTypeDef",
    {
        "Errors": List[BatchDeleteDevicePositionHistoryErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchDeleteGeofenceResponseTypeDef = TypedDict(
    "BatchDeleteGeofenceResponseTypeDef",
    {
        "Errors": List[BatchDeleteGeofenceErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchEvaluateGeofencesResponseTypeDef = TypedDict(
    "BatchEvaluateGeofencesResponseTypeDef",
    {
        "Errors": List[BatchEvaluateGeofencesErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchPutGeofenceResponseTypeDef = TypedDict(
    "BatchPutGeofenceResponseTypeDef",
    {
        "Errors": List[BatchPutGeofenceErrorTypeDef],
        "Successes": List[BatchPutGeofenceSuccessTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchUpdateDevicePositionResponseTypeDef = TypedDict(
    "BatchUpdateDevicePositionResponseTypeDef",
    {
        "Errors": List[BatchUpdateDevicePositionErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CalculateRouteMatrixRequestRequestTypeDef = TypedDict(
    "CalculateRouteMatrixRequestRequestTypeDef",
    {
        "CalculatorName": str,
        "DeparturePositions": Sequence[Sequence[float]],
        "DestinationPositions": Sequence[Sequence[float]],
        "CarModeOptions": NotRequired[CalculateRouteCarModeOptionsTypeDef],
        "DepartNow": NotRequired[bool],
        "DepartureTime": NotRequired[TimestampTypeDef],
        "DistanceUnit": NotRequired[DistanceUnitType],
        "Key": NotRequired[str],
        "TravelMode": NotRequired[TravelModeType],
        "TruckModeOptions": NotRequired[CalculateRouteTruckModeOptionsTypeDef],
    },
)
CalculateRouteRequestRequestTypeDef = TypedDict(
    "CalculateRouteRequestRequestTypeDef",
    {
        "CalculatorName": str,
        "DeparturePosition": Sequence[float],
        "DestinationPosition": Sequence[float],
        "ArrivalTime": NotRequired[TimestampTypeDef],
        "CarModeOptions": NotRequired[CalculateRouteCarModeOptionsTypeDef],
        "DepartNow": NotRequired[bool],
        "DepartureTime": NotRequired[TimestampTypeDef],
        "DistanceUnit": NotRequired[DistanceUnitType],
        "IncludeLegGeometry": NotRequired[bool],
        "Key": NotRequired[str],
        "OptimizeFor": NotRequired[OptimizationModeType],
        "TravelMode": NotRequired[TravelModeType],
        "TruckModeOptions": NotRequired[CalculateRouteTruckModeOptionsTypeDef],
        "WaypointPositions": NotRequired[Sequence[Sequence[float]]],
    },
)
ListGeofenceResponseEntryPaginatorTypeDef = TypedDict(
    "ListGeofenceResponseEntryPaginatorTypeDef",
    {
        "CreateTime": datetime,
        "GeofenceId": str,
        "Geometry": GeofenceGeometryPaginatorTypeDef,
        "Status": str,
        "UpdateTime": datetime,
        "GeofenceProperties": NotRequired[Dict[str, str]],
    },
)
BatchPutGeofenceRequestEntryTypeDef = TypedDict(
    "BatchPutGeofenceRequestEntryTypeDef",
    {
        "GeofenceId": str,
        "Geometry": GeofenceGeometryTypeDef,
        "GeofenceProperties": NotRequired[Mapping[str, str]],
    },
)
GetGeofenceResponseTypeDef = TypedDict(
    "GetGeofenceResponseTypeDef",
    {
        "CreateTime": datetime,
        "GeofenceId": str,
        "GeofenceProperties": Dict[str, str],
        "Geometry": GeofenceGeometryTypeDef,
        "Status": str,
        "UpdateTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListGeofenceResponseEntryTypeDef = TypedDict(
    "ListGeofenceResponseEntryTypeDef",
    {
        "CreateTime": datetime,
        "GeofenceId": str,
        "Geometry": GeofenceGeometryTypeDef,
        "Status": str,
        "UpdateTime": datetime,
        "GeofenceProperties": NotRequired[Dict[str, str]],
    },
)
PutGeofenceRequestRequestTypeDef = TypedDict(
    "PutGeofenceRequestRequestTypeDef",
    {
        "CollectionName": str,
        "GeofenceId": str,
        "Geometry": GeofenceGeometryTypeDef,
        "GeofenceProperties": NotRequired[Mapping[str, str]],
    },
)
BatchGetDevicePositionResponseTypeDef = TypedDict(
    "BatchGetDevicePositionResponseTypeDef",
    {
        "DevicePositions": List[DevicePositionTypeDef],
        "Errors": List[BatchGetDevicePositionErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetDevicePositionHistoryResponseTypeDef = TypedDict(
    "GetDevicePositionHistoryResponseTypeDef",
    {
        "DevicePositions": List[DevicePositionTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchEvaluateGeofencesRequestRequestTypeDef = TypedDict(
    "BatchEvaluateGeofencesRequestRequestTypeDef",
    {
        "CollectionName": str,
        "DevicePositionUpdates": Sequence[DevicePositionUpdateTypeDef],
    },
)
BatchUpdateDevicePositionRequestRequestTypeDef = TypedDict(
    "BatchUpdateDevicePositionRequestRequestTypeDef",
    {
        "TrackerName": str,
        "Updates": Sequence[DevicePositionUpdateTypeDef],
    },
)
ListDevicePositionsResponseTypeDef = TypedDict(
    "ListDevicePositionsResponseTypeDef",
    {
        "Entries": List[ListDevicePositionsResponseEntryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CalculateRouteResponseTypeDef = TypedDict(
    "CalculateRouteResponseTypeDef",
    {
        "Legs": List[LegTypeDef],
        "Summary": CalculateRouteSummaryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetPlaceResponseTypeDef = TypedDict(
    "GetPlaceResponseTypeDef",
    {
        "Place": PlaceTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SearchForPositionResultTypeDef = TypedDict(
    "SearchForPositionResultTypeDef",
    {
        "Distance": float,
        "Place": PlaceTypeDef,
        "PlaceId": NotRequired[str],
    },
)
SearchForTextResultTypeDef = TypedDict(
    "SearchForTextResultTypeDef",
    {
        "Place": PlaceTypeDef,
        "Distance": NotRequired[float],
        "PlaceId": NotRequired[str],
        "Relevance": NotRequired[float],
    },
)
CalculateRouteMatrixResponseTypeDef = TypedDict(
    "CalculateRouteMatrixResponseTypeDef",
    {
        "RouteMatrix": List[List[RouteMatrixEntryTypeDef]],
        "SnappedDeparturePositions": List[List[float]],
        "SnappedDestinationPositions": List[List[float]],
        "Summary": CalculateRouteMatrixSummaryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListGeofencesResponsePaginatorTypeDef = TypedDict(
    "ListGeofencesResponsePaginatorTypeDef",
    {
        "Entries": List[ListGeofenceResponseEntryPaginatorTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchPutGeofenceRequestRequestTypeDef = TypedDict(
    "BatchPutGeofenceRequestRequestTypeDef",
    {
        "CollectionName": str,
        "Entries": Sequence[BatchPutGeofenceRequestEntryTypeDef],
    },
)
ListGeofencesResponseTypeDef = TypedDict(
    "ListGeofencesResponseTypeDef",
    {
        "Entries": List[ListGeofenceResponseEntryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SearchPlaceIndexForPositionResponseTypeDef = TypedDict(
    "SearchPlaceIndexForPositionResponseTypeDef",
    {
        "Results": List[SearchForPositionResultTypeDef],
        "Summary": SearchPlaceIndexForPositionSummaryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SearchPlaceIndexForTextResponseTypeDef = TypedDict(
    "SearchPlaceIndexForTextResponseTypeDef",
    {
        "Results": List[SearchForTextResultTypeDef],
        "Summary": SearchPlaceIndexForTextSummaryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
