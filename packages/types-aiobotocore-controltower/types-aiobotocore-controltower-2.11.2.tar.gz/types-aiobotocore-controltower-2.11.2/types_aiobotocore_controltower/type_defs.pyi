"""
Type annotations for controltower service type definitions.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_controltower/type_defs/)

Usage::

    ```python
    from types_aiobotocore_controltower.type_defs import ControlOperationTypeDef

    data: ControlOperationTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List, Mapping, Sequence

from .literals import (
    ControlOperationStatusType,
    ControlOperationTypeType,
    DriftStatusType,
    EnablementStatusType,
    LandingZoneDriftStatusType,
    LandingZoneOperationStatusType,
    LandingZoneOperationTypeType,
    LandingZoneStatusType,
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
    "ControlOperationTypeDef",
    "CreateLandingZoneInputRequestTypeDef",
    "ResponseMetadataTypeDef",
    "DeleteLandingZoneInputRequestTypeDef",
    "DisableControlInputRequestTypeDef",
    "DriftStatusSummaryTypeDef",
    "EnabledControlParameterTypeDef",
    "EnabledControlParameterSummaryTypeDef",
    "EnablementStatusSummaryTypeDef",
    "RegionTypeDef",
    "GetControlOperationInputRequestTypeDef",
    "GetEnabledControlInputRequestTypeDef",
    "GetLandingZoneInputRequestTypeDef",
    "GetLandingZoneOperationInputRequestTypeDef",
    "LandingZoneOperationDetailTypeDef",
    "LandingZoneDriftStatusSummaryTypeDef",
    "LandingZoneSummaryTypeDef",
    "PaginatorConfigTypeDef",
    "ListEnabledControlsInputRequestTypeDef",
    "ListLandingZonesInputRequestTypeDef",
    "ListTagsForResourceInputRequestTypeDef",
    "ResetLandingZoneInputRequestTypeDef",
    "TagResourceInputRequestTypeDef",
    "UntagResourceInputRequestTypeDef",
    "UpdateLandingZoneInputRequestTypeDef",
    "CreateLandingZoneOutputTypeDef",
    "DeleteLandingZoneOutputTypeDef",
    "DisableControlOutputTypeDef",
    "EnableControlOutputTypeDef",
    "GetControlOperationOutputTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "ResetLandingZoneOutputTypeDef",
    "UpdateEnabledControlOutputTypeDef",
    "UpdateLandingZoneOutputTypeDef",
    "EnableControlInputRequestTypeDef",
    "UpdateEnabledControlInputRequestTypeDef",
    "EnabledControlSummaryTypeDef",
    "EnabledControlDetailsTypeDef",
    "GetLandingZoneOperationOutputTypeDef",
    "LandingZoneDetailTypeDef",
    "ListLandingZonesOutputTypeDef",
    "ListEnabledControlsInputListEnabledControlsPaginateTypeDef",
    "ListLandingZonesInputListLandingZonesPaginateTypeDef",
    "ListEnabledControlsOutputTypeDef",
    "GetEnabledControlOutputTypeDef",
    "GetLandingZoneOutputTypeDef",
)

ControlOperationTypeDef = TypedDict(
    "ControlOperationTypeDef",
    {
        "endTime": NotRequired[datetime],
        "operationType": NotRequired[ControlOperationTypeType],
        "startTime": NotRequired[datetime],
        "status": NotRequired[ControlOperationStatusType],
        "statusMessage": NotRequired[str],
    },
)
CreateLandingZoneInputRequestTypeDef = TypedDict(
    "CreateLandingZoneInputRequestTypeDef",
    {
        "manifest": Mapping[str, Any],
        "version": str,
        "tags": NotRequired[Mapping[str, str]],
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
DeleteLandingZoneInputRequestTypeDef = TypedDict(
    "DeleteLandingZoneInputRequestTypeDef",
    {
        "landingZoneIdentifier": str,
    },
)
DisableControlInputRequestTypeDef = TypedDict(
    "DisableControlInputRequestTypeDef",
    {
        "controlIdentifier": str,
        "targetIdentifier": str,
    },
)
DriftStatusSummaryTypeDef = TypedDict(
    "DriftStatusSummaryTypeDef",
    {
        "driftStatus": NotRequired[DriftStatusType],
    },
)
EnabledControlParameterTypeDef = TypedDict(
    "EnabledControlParameterTypeDef",
    {
        "key": str,
        "value": Mapping[str, Any],
    },
)
EnabledControlParameterSummaryTypeDef = TypedDict(
    "EnabledControlParameterSummaryTypeDef",
    {
        "key": str,
        "value": Dict[str, Any],
    },
)
EnablementStatusSummaryTypeDef = TypedDict(
    "EnablementStatusSummaryTypeDef",
    {
        "lastOperationIdentifier": NotRequired[str],
        "status": NotRequired[EnablementStatusType],
    },
)
RegionTypeDef = TypedDict(
    "RegionTypeDef",
    {
        "name": NotRequired[str],
    },
)
GetControlOperationInputRequestTypeDef = TypedDict(
    "GetControlOperationInputRequestTypeDef",
    {
        "operationIdentifier": str,
    },
)
GetEnabledControlInputRequestTypeDef = TypedDict(
    "GetEnabledControlInputRequestTypeDef",
    {
        "enabledControlIdentifier": str,
    },
)
GetLandingZoneInputRequestTypeDef = TypedDict(
    "GetLandingZoneInputRequestTypeDef",
    {
        "landingZoneIdentifier": str,
    },
)
GetLandingZoneOperationInputRequestTypeDef = TypedDict(
    "GetLandingZoneOperationInputRequestTypeDef",
    {
        "operationIdentifier": str,
    },
)
LandingZoneOperationDetailTypeDef = TypedDict(
    "LandingZoneOperationDetailTypeDef",
    {
        "endTime": NotRequired[datetime],
        "operationType": NotRequired[LandingZoneOperationTypeType],
        "startTime": NotRequired[datetime],
        "status": NotRequired[LandingZoneOperationStatusType],
        "statusMessage": NotRequired[str],
    },
)
LandingZoneDriftStatusSummaryTypeDef = TypedDict(
    "LandingZoneDriftStatusSummaryTypeDef",
    {
        "status": NotRequired[LandingZoneDriftStatusType],
    },
)
LandingZoneSummaryTypeDef = TypedDict(
    "LandingZoneSummaryTypeDef",
    {
        "arn": NotRequired[str],
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
ListEnabledControlsInputRequestTypeDef = TypedDict(
    "ListEnabledControlsInputRequestTypeDef",
    {
        "targetIdentifier": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListLandingZonesInputRequestTypeDef = TypedDict(
    "ListLandingZonesInputRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListTagsForResourceInputRequestTypeDef = TypedDict(
    "ListTagsForResourceInputRequestTypeDef",
    {
        "resourceArn": str,
    },
)
ResetLandingZoneInputRequestTypeDef = TypedDict(
    "ResetLandingZoneInputRequestTypeDef",
    {
        "landingZoneIdentifier": str,
    },
)
TagResourceInputRequestTypeDef = TypedDict(
    "TagResourceInputRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Mapping[str, str],
    },
)
UntagResourceInputRequestTypeDef = TypedDict(
    "UntagResourceInputRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)
UpdateLandingZoneInputRequestTypeDef = TypedDict(
    "UpdateLandingZoneInputRequestTypeDef",
    {
        "landingZoneIdentifier": str,
        "manifest": Mapping[str, Any],
        "version": str,
    },
)
CreateLandingZoneOutputTypeDef = TypedDict(
    "CreateLandingZoneOutputTypeDef",
    {
        "arn": str,
        "operationIdentifier": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteLandingZoneOutputTypeDef = TypedDict(
    "DeleteLandingZoneOutputTypeDef",
    {
        "operationIdentifier": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DisableControlOutputTypeDef = TypedDict(
    "DisableControlOutputTypeDef",
    {
        "operationIdentifier": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EnableControlOutputTypeDef = TypedDict(
    "EnableControlOutputTypeDef",
    {
        "arn": str,
        "operationIdentifier": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetControlOperationOutputTypeDef = TypedDict(
    "GetControlOperationOutputTypeDef",
    {
        "controlOperation": ControlOperationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ResetLandingZoneOutputTypeDef = TypedDict(
    "ResetLandingZoneOutputTypeDef",
    {
        "operationIdentifier": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateEnabledControlOutputTypeDef = TypedDict(
    "UpdateEnabledControlOutputTypeDef",
    {
        "operationIdentifier": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateLandingZoneOutputTypeDef = TypedDict(
    "UpdateLandingZoneOutputTypeDef",
    {
        "operationIdentifier": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EnableControlInputRequestTypeDef = TypedDict(
    "EnableControlInputRequestTypeDef",
    {
        "controlIdentifier": str,
        "targetIdentifier": str,
        "parameters": NotRequired[Sequence[EnabledControlParameterTypeDef]],
        "tags": NotRequired[Mapping[str, str]],
    },
)
UpdateEnabledControlInputRequestTypeDef = TypedDict(
    "UpdateEnabledControlInputRequestTypeDef",
    {
        "enabledControlIdentifier": str,
        "parameters": Sequence[EnabledControlParameterTypeDef],
    },
)
EnabledControlSummaryTypeDef = TypedDict(
    "EnabledControlSummaryTypeDef",
    {
        "arn": NotRequired[str],
        "controlIdentifier": NotRequired[str],
        "driftStatusSummary": NotRequired[DriftStatusSummaryTypeDef],
        "statusSummary": NotRequired[EnablementStatusSummaryTypeDef],
        "targetIdentifier": NotRequired[str],
    },
)
EnabledControlDetailsTypeDef = TypedDict(
    "EnabledControlDetailsTypeDef",
    {
        "arn": NotRequired[str],
        "controlIdentifier": NotRequired[str],
        "driftStatusSummary": NotRequired[DriftStatusSummaryTypeDef],
        "parameters": NotRequired[List[EnabledControlParameterSummaryTypeDef]],
        "statusSummary": NotRequired[EnablementStatusSummaryTypeDef],
        "targetIdentifier": NotRequired[str],
        "targetRegions": NotRequired[List[RegionTypeDef]],
    },
)
GetLandingZoneOperationOutputTypeDef = TypedDict(
    "GetLandingZoneOperationOutputTypeDef",
    {
        "operationDetails": LandingZoneOperationDetailTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
LandingZoneDetailTypeDef = TypedDict(
    "LandingZoneDetailTypeDef",
    {
        "manifest": Dict[str, Any],
        "version": str,
        "arn": NotRequired[str],
        "driftStatus": NotRequired[LandingZoneDriftStatusSummaryTypeDef],
        "latestAvailableVersion": NotRequired[str],
        "status": NotRequired[LandingZoneStatusType],
    },
)
ListLandingZonesOutputTypeDef = TypedDict(
    "ListLandingZonesOutputTypeDef",
    {
        "landingZones": List[LandingZoneSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListEnabledControlsInputListEnabledControlsPaginateTypeDef = TypedDict(
    "ListEnabledControlsInputListEnabledControlsPaginateTypeDef",
    {
        "targetIdentifier": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListLandingZonesInputListLandingZonesPaginateTypeDef = TypedDict(
    "ListLandingZonesInputListLandingZonesPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListEnabledControlsOutputTypeDef = TypedDict(
    "ListEnabledControlsOutputTypeDef",
    {
        "enabledControls": List[EnabledControlSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetEnabledControlOutputTypeDef = TypedDict(
    "GetEnabledControlOutputTypeDef",
    {
        "enabledControlDetails": EnabledControlDetailsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetLandingZoneOutputTypeDef = TypedDict(
    "GetLandingZoneOutputTypeDef",
    {
        "landingZone": LandingZoneDetailTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
