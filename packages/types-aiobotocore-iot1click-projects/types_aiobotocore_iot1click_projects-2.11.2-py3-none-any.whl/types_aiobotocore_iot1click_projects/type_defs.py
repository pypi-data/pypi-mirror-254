"""
Type annotations for iot1click-projects service type definitions.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iot1click_projects/type_defs/)

Usage::

    ```python
    from types_aiobotocore_iot1click_projects.type_defs import AssociateDeviceWithPlacementRequestRequestTypeDef

    data: AssociateDeviceWithPlacementRequestRequestTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

if sys.version_info >= (3, 12):
    from typing import NotRequired
else:
    from typing_extensions import NotRequired
if sys.version_info >= (3, 12):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AssociateDeviceWithPlacementRequestRequestTypeDef",
    "CreatePlacementRequestRequestTypeDef",
    "DeletePlacementRequestRequestTypeDef",
    "DeleteProjectRequestRequestTypeDef",
    "DescribePlacementRequestRequestTypeDef",
    "PlacementDescriptionTypeDef",
    "ResponseMetadataTypeDef",
    "DescribeProjectRequestRequestTypeDef",
    "DeviceTemplateTypeDef",
    "DisassociateDeviceFromPlacementRequestRequestTypeDef",
    "GetDevicesInPlacementRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "ListPlacementsRequestRequestTypeDef",
    "PlacementSummaryTypeDef",
    "ListProjectsRequestRequestTypeDef",
    "ProjectSummaryTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdatePlacementRequestRequestTypeDef",
    "DescribePlacementResponseTypeDef",
    "GetDevicesInPlacementResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PlacementTemplateTypeDef",
    "ListPlacementsRequestListPlacementsPaginateTypeDef",
    "ListProjectsRequestListProjectsPaginateTypeDef",
    "ListPlacementsResponseTypeDef",
    "ListProjectsResponseTypeDef",
    "CreateProjectRequestRequestTypeDef",
    "ProjectDescriptionTypeDef",
    "UpdateProjectRequestRequestTypeDef",
    "DescribeProjectResponseTypeDef",
)

AssociateDeviceWithPlacementRequestRequestTypeDef = TypedDict(
    "AssociateDeviceWithPlacementRequestRequestTypeDef",
    {
        "projectName": str,
        "placementName": str,
        "deviceId": str,
        "deviceTemplateName": str,
    },
)
CreatePlacementRequestRequestTypeDef = TypedDict(
    "CreatePlacementRequestRequestTypeDef",
    {
        "placementName": str,
        "projectName": str,
        "attributes": NotRequired[Mapping[str, str]],
    },
)
DeletePlacementRequestRequestTypeDef = TypedDict(
    "DeletePlacementRequestRequestTypeDef",
    {
        "placementName": str,
        "projectName": str,
    },
)
DeleteProjectRequestRequestTypeDef = TypedDict(
    "DeleteProjectRequestRequestTypeDef",
    {
        "projectName": str,
    },
)
DescribePlacementRequestRequestTypeDef = TypedDict(
    "DescribePlacementRequestRequestTypeDef",
    {
        "placementName": str,
        "projectName": str,
    },
)
PlacementDescriptionTypeDef = TypedDict(
    "PlacementDescriptionTypeDef",
    {
        "projectName": str,
        "placementName": str,
        "attributes": Dict[str, str],
        "createdDate": datetime,
        "updatedDate": datetime,
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
DescribeProjectRequestRequestTypeDef = TypedDict(
    "DescribeProjectRequestRequestTypeDef",
    {
        "projectName": str,
    },
)
DeviceTemplateTypeDef = TypedDict(
    "DeviceTemplateTypeDef",
    {
        "deviceType": NotRequired[str],
        "callbackOverrides": NotRequired[Mapping[str, str]],
    },
)
DisassociateDeviceFromPlacementRequestRequestTypeDef = TypedDict(
    "DisassociateDeviceFromPlacementRequestRequestTypeDef",
    {
        "projectName": str,
        "placementName": str,
        "deviceTemplateName": str,
    },
)
GetDevicesInPlacementRequestRequestTypeDef = TypedDict(
    "GetDevicesInPlacementRequestRequestTypeDef",
    {
        "projectName": str,
        "placementName": str,
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
ListPlacementsRequestRequestTypeDef = TypedDict(
    "ListPlacementsRequestRequestTypeDef",
    {
        "projectName": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
PlacementSummaryTypeDef = TypedDict(
    "PlacementSummaryTypeDef",
    {
        "projectName": str,
        "placementName": str,
        "createdDate": datetime,
        "updatedDate": datetime,
    },
)
ListProjectsRequestRequestTypeDef = TypedDict(
    "ListProjectsRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ProjectSummaryTypeDef = TypedDict(
    "ProjectSummaryTypeDef",
    {
        "projectName": str,
        "createdDate": datetime,
        "updatedDate": datetime,
        "arn": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
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
UpdatePlacementRequestRequestTypeDef = TypedDict(
    "UpdatePlacementRequestRequestTypeDef",
    {
        "placementName": str,
        "projectName": str,
        "attributes": NotRequired[Mapping[str, str]],
    },
)
DescribePlacementResponseTypeDef = TypedDict(
    "DescribePlacementResponseTypeDef",
    {
        "placement": PlacementDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetDevicesInPlacementResponseTypeDef = TypedDict(
    "GetDevicesInPlacementResponseTypeDef",
    {
        "devices": Dict[str, str],
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
PlacementTemplateTypeDef = TypedDict(
    "PlacementTemplateTypeDef",
    {
        "defaultAttributes": NotRequired[Mapping[str, str]],
        "deviceTemplates": NotRequired[Mapping[str, DeviceTemplateTypeDef]],
    },
)
ListPlacementsRequestListPlacementsPaginateTypeDef = TypedDict(
    "ListPlacementsRequestListPlacementsPaginateTypeDef",
    {
        "projectName": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListProjectsRequestListProjectsPaginateTypeDef = TypedDict(
    "ListProjectsRequestListProjectsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListPlacementsResponseTypeDef = TypedDict(
    "ListPlacementsResponseTypeDef",
    {
        "placements": List[PlacementSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListProjectsResponseTypeDef = TypedDict(
    "ListProjectsResponseTypeDef",
    {
        "projects": List[ProjectSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateProjectRequestRequestTypeDef = TypedDict(
    "CreateProjectRequestRequestTypeDef",
    {
        "projectName": str,
        "description": NotRequired[str],
        "placementTemplate": NotRequired[PlacementTemplateTypeDef],
        "tags": NotRequired[Mapping[str, str]],
    },
)
ProjectDescriptionTypeDef = TypedDict(
    "ProjectDescriptionTypeDef",
    {
        "projectName": str,
        "createdDate": datetime,
        "updatedDate": datetime,
        "arn": NotRequired[str],
        "description": NotRequired[str],
        "placementTemplate": NotRequired[PlacementTemplateTypeDef],
        "tags": NotRequired[Dict[str, str]],
    },
)
UpdateProjectRequestRequestTypeDef = TypedDict(
    "UpdateProjectRequestRequestTypeDef",
    {
        "projectName": str,
        "description": NotRequired[str],
        "placementTemplate": NotRequired[PlacementTemplateTypeDef],
    },
)
DescribeProjectResponseTypeDef = TypedDict(
    "DescribeProjectResponseTypeDef",
    {
        "project": ProjectDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
