"""
Type annotations for iot-roborunner service type definitions.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iot_roborunner/type_defs/)

Usage::

    ```python
    from types_aiobotocore_iot_roborunner.type_defs import CartesianCoordinatesTypeDef

    data: CartesianCoordinatesTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List

from .literals import DestinationStateType

if sys.version_info >= (3, 12):
    from typing import NotRequired
else:
    from typing_extensions import NotRequired
if sys.version_info >= (3, 12):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "CartesianCoordinatesTypeDef",
    "CreateDestinationRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "CreateSiteRequestRequestTypeDef",
    "CreateWorkerFleetRequestRequestTypeDef",
    "OrientationTypeDef",
    "VendorPropertiesTypeDef",
    "DeleteDestinationRequestRequestTypeDef",
    "DeleteSiteRequestRequestTypeDef",
    "DeleteWorkerFleetRequestRequestTypeDef",
    "DeleteWorkerRequestRequestTypeDef",
    "DestinationTypeDef",
    "GetDestinationRequestRequestTypeDef",
    "GetSiteRequestRequestTypeDef",
    "GetWorkerFleetRequestRequestTypeDef",
    "GetWorkerRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "ListDestinationsRequestRequestTypeDef",
    "ListSitesRequestRequestTypeDef",
    "SiteTypeDef",
    "ListWorkerFleetsRequestRequestTypeDef",
    "WorkerFleetTypeDef",
    "ListWorkersRequestRequestTypeDef",
    "UpdateDestinationRequestRequestTypeDef",
    "UpdateSiteRequestRequestTypeDef",
    "UpdateWorkerFleetRequestRequestTypeDef",
    "PositionCoordinatesTypeDef",
    "CreateDestinationResponseTypeDef",
    "CreateSiteResponseTypeDef",
    "CreateWorkerFleetResponseTypeDef",
    "CreateWorkerResponseTypeDef",
    "GetDestinationResponseTypeDef",
    "GetSiteResponseTypeDef",
    "GetWorkerFleetResponseTypeDef",
    "UpdateDestinationResponseTypeDef",
    "UpdateSiteResponseTypeDef",
    "UpdateWorkerFleetResponseTypeDef",
    "ListDestinationsResponseTypeDef",
    "ListDestinationsRequestListDestinationsPaginateTypeDef",
    "ListSitesRequestListSitesPaginateTypeDef",
    "ListWorkerFleetsRequestListWorkerFleetsPaginateTypeDef",
    "ListWorkersRequestListWorkersPaginateTypeDef",
    "ListSitesResponseTypeDef",
    "ListWorkerFleetsResponseTypeDef",
    "CreateWorkerRequestRequestTypeDef",
    "GetWorkerResponseTypeDef",
    "UpdateWorkerRequestRequestTypeDef",
    "UpdateWorkerResponseTypeDef",
    "WorkerTypeDef",
    "ListWorkersResponseTypeDef",
)

CartesianCoordinatesTypeDef = TypedDict(
    "CartesianCoordinatesTypeDef",
    {
        "x": float,
        "y": float,
        "z": NotRequired[float],
    },
)
CreateDestinationRequestRequestTypeDef = TypedDict(
    "CreateDestinationRequestRequestTypeDef",
    {
        "name": str,
        "site": str,
        "clientToken": NotRequired[str],
        "state": NotRequired[DestinationStateType],
        "additionalFixedProperties": NotRequired[str],
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
CreateSiteRequestRequestTypeDef = TypedDict(
    "CreateSiteRequestRequestTypeDef",
    {
        "name": str,
        "countryCode": str,
        "clientToken": NotRequired[str],
        "description": NotRequired[str],
    },
)
CreateWorkerFleetRequestRequestTypeDef = TypedDict(
    "CreateWorkerFleetRequestRequestTypeDef",
    {
        "name": str,
        "site": str,
        "clientToken": NotRequired[str],
        "additionalFixedProperties": NotRequired[str],
    },
)
OrientationTypeDef = TypedDict(
    "OrientationTypeDef",
    {
        "degrees": NotRequired[float],
    },
)
VendorPropertiesTypeDef = TypedDict(
    "VendorPropertiesTypeDef",
    {
        "vendorWorkerId": str,
        "vendorWorkerIpAddress": NotRequired[str],
        "vendorAdditionalTransientProperties": NotRequired[str],
        "vendorAdditionalFixedProperties": NotRequired[str],
    },
)
DeleteDestinationRequestRequestTypeDef = TypedDict(
    "DeleteDestinationRequestRequestTypeDef",
    {
        "id": str,
    },
)
DeleteSiteRequestRequestTypeDef = TypedDict(
    "DeleteSiteRequestRequestTypeDef",
    {
        "id": str,
    },
)
DeleteWorkerFleetRequestRequestTypeDef = TypedDict(
    "DeleteWorkerFleetRequestRequestTypeDef",
    {
        "id": str,
    },
)
DeleteWorkerRequestRequestTypeDef = TypedDict(
    "DeleteWorkerRequestRequestTypeDef",
    {
        "id": str,
    },
)
DestinationTypeDef = TypedDict(
    "DestinationTypeDef",
    {
        "arn": str,
        "id": str,
        "name": str,
        "site": str,
        "createdAt": datetime,
        "updatedAt": datetime,
        "state": DestinationStateType,
        "additionalFixedProperties": NotRequired[str],
    },
)
GetDestinationRequestRequestTypeDef = TypedDict(
    "GetDestinationRequestRequestTypeDef",
    {
        "id": str,
    },
)
GetSiteRequestRequestTypeDef = TypedDict(
    "GetSiteRequestRequestTypeDef",
    {
        "id": str,
    },
)
GetWorkerFleetRequestRequestTypeDef = TypedDict(
    "GetWorkerFleetRequestRequestTypeDef",
    {
        "id": str,
    },
)
GetWorkerRequestRequestTypeDef = TypedDict(
    "GetWorkerRequestRequestTypeDef",
    {
        "id": str,
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
ListDestinationsRequestRequestTypeDef = TypedDict(
    "ListDestinationsRequestRequestTypeDef",
    {
        "site": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "state": NotRequired[DestinationStateType],
    },
)
ListSitesRequestRequestTypeDef = TypedDict(
    "ListSitesRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
SiteTypeDef = TypedDict(
    "SiteTypeDef",
    {
        "arn": str,
        "name": str,
        "countryCode": str,
        "createdAt": datetime,
    },
)
ListWorkerFleetsRequestRequestTypeDef = TypedDict(
    "ListWorkerFleetsRequestRequestTypeDef",
    {
        "site": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
WorkerFleetTypeDef = TypedDict(
    "WorkerFleetTypeDef",
    {
        "arn": str,
        "id": str,
        "name": str,
        "site": str,
        "createdAt": datetime,
        "updatedAt": datetime,
        "additionalFixedProperties": NotRequired[str],
    },
)
ListWorkersRequestRequestTypeDef = TypedDict(
    "ListWorkersRequestRequestTypeDef",
    {
        "site": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "fleet": NotRequired[str],
    },
)
UpdateDestinationRequestRequestTypeDef = TypedDict(
    "UpdateDestinationRequestRequestTypeDef",
    {
        "id": str,
        "name": NotRequired[str],
        "state": NotRequired[DestinationStateType],
        "additionalFixedProperties": NotRequired[str],
    },
)
UpdateSiteRequestRequestTypeDef = TypedDict(
    "UpdateSiteRequestRequestTypeDef",
    {
        "id": str,
        "name": NotRequired[str],
        "countryCode": NotRequired[str],
        "description": NotRequired[str],
    },
)
UpdateWorkerFleetRequestRequestTypeDef = TypedDict(
    "UpdateWorkerFleetRequestRequestTypeDef",
    {
        "id": str,
        "name": NotRequired[str],
        "additionalFixedProperties": NotRequired[str],
    },
)
PositionCoordinatesTypeDef = TypedDict(
    "PositionCoordinatesTypeDef",
    {
        "cartesianCoordinates": NotRequired[CartesianCoordinatesTypeDef],
    },
)
CreateDestinationResponseTypeDef = TypedDict(
    "CreateDestinationResponseTypeDef",
    {
        "arn": str,
        "id": str,
        "createdAt": datetime,
        "updatedAt": datetime,
        "state": DestinationStateType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateSiteResponseTypeDef = TypedDict(
    "CreateSiteResponseTypeDef",
    {
        "arn": str,
        "id": str,
        "createdAt": datetime,
        "updatedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateWorkerFleetResponseTypeDef = TypedDict(
    "CreateWorkerFleetResponseTypeDef",
    {
        "arn": str,
        "id": str,
        "createdAt": datetime,
        "updatedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateWorkerResponseTypeDef = TypedDict(
    "CreateWorkerResponseTypeDef",
    {
        "arn": str,
        "id": str,
        "createdAt": datetime,
        "updatedAt": datetime,
        "site": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetDestinationResponseTypeDef = TypedDict(
    "GetDestinationResponseTypeDef",
    {
        "arn": str,
        "id": str,
        "name": str,
        "site": str,
        "createdAt": datetime,
        "updatedAt": datetime,
        "state": DestinationStateType,
        "additionalFixedProperties": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSiteResponseTypeDef = TypedDict(
    "GetSiteResponseTypeDef",
    {
        "arn": str,
        "id": str,
        "name": str,
        "countryCode": str,
        "description": str,
        "createdAt": datetime,
        "updatedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetWorkerFleetResponseTypeDef = TypedDict(
    "GetWorkerFleetResponseTypeDef",
    {
        "id": str,
        "arn": str,
        "name": str,
        "site": str,
        "createdAt": datetime,
        "updatedAt": datetime,
        "additionalFixedProperties": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateDestinationResponseTypeDef = TypedDict(
    "UpdateDestinationResponseTypeDef",
    {
        "arn": str,
        "id": str,
        "name": str,
        "updatedAt": datetime,
        "state": DestinationStateType,
        "additionalFixedProperties": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateSiteResponseTypeDef = TypedDict(
    "UpdateSiteResponseTypeDef",
    {
        "arn": str,
        "id": str,
        "name": str,
        "countryCode": str,
        "description": str,
        "updatedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateWorkerFleetResponseTypeDef = TypedDict(
    "UpdateWorkerFleetResponseTypeDef",
    {
        "arn": str,
        "id": str,
        "name": str,
        "updatedAt": datetime,
        "additionalFixedProperties": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListDestinationsResponseTypeDef = TypedDict(
    "ListDestinationsResponseTypeDef",
    {
        "nextToken": str,
        "destinations": List[DestinationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListDestinationsRequestListDestinationsPaginateTypeDef = TypedDict(
    "ListDestinationsRequestListDestinationsPaginateTypeDef",
    {
        "site": str,
        "state": NotRequired[DestinationStateType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListSitesRequestListSitesPaginateTypeDef = TypedDict(
    "ListSitesRequestListSitesPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListWorkerFleetsRequestListWorkerFleetsPaginateTypeDef = TypedDict(
    "ListWorkerFleetsRequestListWorkerFleetsPaginateTypeDef",
    {
        "site": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListWorkersRequestListWorkersPaginateTypeDef = TypedDict(
    "ListWorkersRequestListWorkersPaginateTypeDef",
    {
        "site": str,
        "fleet": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListSitesResponseTypeDef = TypedDict(
    "ListSitesResponseTypeDef",
    {
        "nextToken": str,
        "sites": List[SiteTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListWorkerFleetsResponseTypeDef = TypedDict(
    "ListWorkerFleetsResponseTypeDef",
    {
        "nextToken": str,
        "workerFleets": List[WorkerFleetTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateWorkerRequestRequestTypeDef = TypedDict(
    "CreateWorkerRequestRequestTypeDef",
    {
        "name": str,
        "fleet": str,
        "clientToken": NotRequired[str],
        "additionalTransientProperties": NotRequired[str],
        "additionalFixedProperties": NotRequired[str],
        "vendorProperties": NotRequired[VendorPropertiesTypeDef],
        "position": NotRequired[PositionCoordinatesTypeDef],
        "orientation": NotRequired[OrientationTypeDef],
    },
)
GetWorkerResponseTypeDef = TypedDict(
    "GetWorkerResponseTypeDef",
    {
        "arn": str,
        "id": str,
        "fleet": str,
        "site": str,
        "createdAt": datetime,
        "updatedAt": datetime,
        "name": str,
        "additionalTransientProperties": str,
        "additionalFixedProperties": str,
        "vendorProperties": VendorPropertiesTypeDef,
        "position": PositionCoordinatesTypeDef,
        "orientation": OrientationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateWorkerRequestRequestTypeDef = TypedDict(
    "UpdateWorkerRequestRequestTypeDef",
    {
        "id": str,
        "name": NotRequired[str],
        "additionalTransientProperties": NotRequired[str],
        "additionalFixedProperties": NotRequired[str],
        "vendorProperties": NotRequired[VendorPropertiesTypeDef],
        "position": NotRequired[PositionCoordinatesTypeDef],
        "orientation": NotRequired[OrientationTypeDef],
    },
)
UpdateWorkerResponseTypeDef = TypedDict(
    "UpdateWorkerResponseTypeDef",
    {
        "arn": str,
        "id": str,
        "fleet": str,
        "updatedAt": datetime,
        "name": str,
        "additionalTransientProperties": str,
        "additionalFixedProperties": str,
        "orientation": OrientationTypeDef,
        "vendorProperties": VendorPropertiesTypeDef,
        "position": PositionCoordinatesTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
WorkerTypeDef = TypedDict(
    "WorkerTypeDef",
    {
        "arn": str,
        "id": str,
        "fleet": str,
        "createdAt": datetime,
        "updatedAt": datetime,
        "name": str,
        "site": str,
        "additionalTransientProperties": NotRequired[str],
        "additionalFixedProperties": NotRequired[str],
        "vendorProperties": NotRequired[VendorPropertiesTypeDef],
        "position": NotRequired[PositionCoordinatesTypeDef],
        "orientation": NotRequired[OrientationTypeDef],
    },
)
ListWorkersResponseTypeDef = TypedDict(
    "ListWorkersResponseTypeDef",
    {
        "nextToken": str,
        "workers": List[WorkerTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
