"""
Type annotations for appintegrations service type definitions.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appintegrations/type_defs/)

Usage::

    ```python
    from types_aiobotocore_appintegrations.type_defs import ApplicationAssociationSummaryTypeDef

    data: ApplicationAssociationSummaryTypeDef = ...
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
    "ApplicationAssociationSummaryTypeDef",
    "ExternalUrlConfigTypeDef",
    "ApplicationSummaryTypeDef",
    "PublicationTypeDef",
    "SubscriptionTypeDef",
    "ResponseMetadataTypeDef",
    "FileConfigurationTypeDef",
    "ScheduleConfigurationTypeDef",
    "EventFilterTypeDef",
    "DataIntegrationAssociationSummaryTypeDef",
    "DataIntegrationSummaryTypeDef",
    "DeleteApplicationRequestRequestTypeDef",
    "DeleteDataIntegrationRequestRequestTypeDef",
    "DeleteEventIntegrationRequestRequestTypeDef",
    "EventIntegrationAssociationTypeDef",
    "GetApplicationRequestRequestTypeDef",
    "GetDataIntegrationRequestRequestTypeDef",
    "GetEventIntegrationRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "ListApplicationAssociationsRequestRequestTypeDef",
    "ListApplicationsRequestRequestTypeDef",
    "ListDataIntegrationAssociationsRequestRequestTypeDef",
    "ListDataIntegrationsRequestRequestTypeDef",
    "ListEventIntegrationAssociationsRequestRequestTypeDef",
    "ListEventIntegrationsRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateDataIntegrationRequestRequestTypeDef",
    "UpdateEventIntegrationRequestRequestTypeDef",
    "ApplicationSourceConfigTypeDef",
    "CreateApplicationResponseTypeDef",
    "CreateEventIntegrationResponseTypeDef",
    "ListApplicationAssociationsResponseTypeDef",
    "ListApplicationsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "CreateDataIntegrationRequestRequestTypeDef",
    "CreateDataIntegrationResponseTypeDef",
    "GetDataIntegrationResponseTypeDef",
    "CreateEventIntegrationRequestRequestTypeDef",
    "EventIntegrationTypeDef",
    "GetEventIntegrationResponseTypeDef",
    "ListDataIntegrationAssociationsResponseTypeDef",
    "ListDataIntegrationsResponseTypeDef",
    "ListEventIntegrationAssociationsResponseTypeDef",
    "ListApplicationAssociationsRequestListApplicationAssociationsPaginateTypeDef",
    "ListApplicationsRequestListApplicationsPaginateTypeDef",
    "ListDataIntegrationAssociationsRequestListDataIntegrationAssociationsPaginateTypeDef",
    "ListDataIntegrationsRequestListDataIntegrationsPaginateTypeDef",
    "ListEventIntegrationAssociationsRequestListEventIntegrationAssociationsPaginateTypeDef",
    "ListEventIntegrationsRequestListEventIntegrationsPaginateTypeDef",
    "CreateApplicationRequestRequestTypeDef",
    "GetApplicationResponseTypeDef",
    "UpdateApplicationRequestRequestTypeDef",
    "ListEventIntegrationsResponseTypeDef",
)

ApplicationAssociationSummaryTypeDef = TypedDict(
    "ApplicationAssociationSummaryTypeDef",
    {
        "ApplicationAssociationArn": NotRequired[str],
        "ApplicationArn": NotRequired[str],
        "ClientId": NotRequired[str],
    },
)
ExternalUrlConfigTypeDef = TypedDict(
    "ExternalUrlConfigTypeDef",
    {
        "AccessUrl": str,
        "ApprovedOrigins": NotRequired[Sequence[str]],
    },
)
ApplicationSummaryTypeDef = TypedDict(
    "ApplicationSummaryTypeDef",
    {
        "Arn": NotRequired[str],
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "Namespace": NotRequired[str],
        "CreatedTime": NotRequired[datetime],
        "LastModifiedTime": NotRequired[datetime],
    },
)
PublicationTypeDef = TypedDict(
    "PublicationTypeDef",
    {
        "Event": str,
        "Schema": str,
        "Description": NotRequired[str],
    },
)
SubscriptionTypeDef = TypedDict(
    "SubscriptionTypeDef",
    {
        "Event": str,
        "Description": NotRequired[str],
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
FileConfigurationTypeDef = TypedDict(
    "FileConfigurationTypeDef",
    {
        "Folders": Sequence[str],
        "Filters": NotRequired[Mapping[str, Sequence[str]]],
    },
)
ScheduleConfigurationTypeDef = TypedDict(
    "ScheduleConfigurationTypeDef",
    {
        "ScheduleExpression": str,
        "FirstExecutionFrom": NotRequired[str],
        "Object": NotRequired[str],
    },
)
EventFilterTypeDef = TypedDict(
    "EventFilterTypeDef",
    {
        "Source": str,
    },
)
DataIntegrationAssociationSummaryTypeDef = TypedDict(
    "DataIntegrationAssociationSummaryTypeDef",
    {
        "DataIntegrationAssociationArn": NotRequired[str],
        "DataIntegrationArn": NotRequired[str],
        "ClientId": NotRequired[str],
    },
)
DataIntegrationSummaryTypeDef = TypedDict(
    "DataIntegrationSummaryTypeDef",
    {
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
        "SourceURI": NotRequired[str],
    },
)
DeleteApplicationRequestRequestTypeDef = TypedDict(
    "DeleteApplicationRequestRequestTypeDef",
    {
        "Arn": str,
    },
)
DeleteDataIntegrationRequestRequestTypeDef = TypedDict(
    "DeleteDataIntegrationRequestRequestTypeDef",
    {
        "DataIntegrationIdentifier": str,
    },
)
DeleteEventIntegrationRequestRequestTypeDef = TypedDict(
    "DeleteEventIntegrationRequestRequestTypeDef",
    {
        "Name": str,
    },
)
EventIntegrationAssociationTypeDef = TypedDict(
    "EventIntegrationAssociationTypeDef",
    {
        "EventIntegrationAssociationArn": NotRequired[str],
        "EventIntegrationAssociationId": NotRequired[str],
        "EventIntegrationName": NotRequired[str],
        "ClientId": NotRequired[str],
        "EventBridgeRuleName": NotRequired[str],
        "ClientAssociationMetadata": NotRequired[Dict[str, str]],
    },
)
GetApplicationRequestRequestTypeDef = TypedDict(
    "GetApplicationRequestRequestTypeDef",
    {
        "Arn": str,
    },
)
GetDataIntegrationRequestRequestTypeDef = TypedDict(
    "GetDataIntegrationRequestRequestTypeDef",
    {
        "Identifier": str,
    },
)
GetEventIntegrationRequestRequestTypeDef = TypedDict(
    "GetEventIntegrationRequestRequestTypeDef",
    {
        "Name": str,
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
ListApplicationAssociationsRequestRequestTypeDef = TypedDict(
    "ListApplicationAssociationsRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListApplicationsRequestRequestTypeDef = TypedDict(
    "ListApplicationsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListDataIntegrationAssociationsRequestRequestTypeDef = TypedDict(
    "ListDataIntegrationAssociationsRequestRequestTypeDef",
    {
        "DataIntegrationIdentifier": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListDataIntegrationsRequestRequestTypeDef = TypedDict(
    "ListDataIntegrationsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListEventIntegrationAssociationsRequestRequestTypeDef = TypedDict(
    "ListEventIntegrationAssociationsRequestRequestTypeDef",
    {
        "EventIntegrationName": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListEventIntegrationsRequestRequestTypeDef = TypedDict(
    "ListEventIntegrationsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
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
UpdateDataIntegrationRequestRequestTypeDef = TypedDict(
    "UpdateDataIntegrationRequestRequestTypeDef",
    {
        "Identifier": str,
        "Name": NotRequired[str],
        "Description": NotRequired[str],
    },
)
UpdateEventIntegrationRequestRequestTypeDef = TypedDict(
    "UpdateEventIntegrationRequestRequestTypeDef",
    {
        "Name": str,
        "Description": NotRequired[str],
    },
)
ApplicationSourceConfigTypeDef = TypedDict(
    "ApplicationSourceConfigTypeDef",
    {
        "ExternalUrlConfig": NotRequired[ExternalUrlConfigTypeDef],
    },
)
CreateApplicationResponseTypeDef = TypedDict(
    "CreateApplicationResponseTypeDef",
    {
        "Arn": str,
        "Id": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateEventIntegrationResponseTypeDef = TypedDict(
    "CreateEventIntegrationResponseTypeDef",
    {
        "EventIntegrationArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListApplicationAssociationsResponseTypeDef = TypedDict(
    "ListApplicationAssociationsResponseTypeDef",
    {
        "ApplicationAssociations": List[ApplicationAssociationSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListApplicationsResponseTypeDef = TypedDict(
    "ListApplicationsResponseTypeDef",
    {
        "Applications": List[ApplicationSummaryTypeDef],
        "NextToken": str,
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
CreateDataIntegrationRequestRequestTypeDef = TypedDict(
    "CreateDataIntegrationRequestRequestTypeDef",
    {
        "Name": str,
        "KmsKey": str,
        "SourceURI": str,
        "Description": NotRequired[str],
        "ScheduleConfig": NotRequired[ScheduleConfigurationTypeDef],
        "Tags": NotRequired[Mapping[str, str]],
        "ClientToken": NotRequired[str],
        "FileConfiguration": NotRequired[FileConfigurationTypeDef],
        "ObjectConfiguration": NotRequired[Mapping[str, Mapping[str, Sequence[str]]]],
    },
)
CreateDataIntegrationResponseTypeDef = TypedDict(
    "CreateDataIntegrationResponseTypeDef",
    {
        "Arn": str,
        "Id": str,
        "Name": str,
        "Description": str,
        "KmsKey": str,
        "SourceURI": str,
        "ScheduleConfiguration": ScheduleConfigurationTypeDef,
        "Tags": Dict[str, str],
        "ClientToken": str,
        "FileConfiguration": FileConfigurationTypeDef,
        "ObjectConfiguration": Dict[str, Dict[str, List[str]]],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetDataIntegrationResponseTypeDef = TypedDict(
    "GetDataIntegrationResponseTypeDef",
    {
        "Arn": str,
        "Id": str,
        "Name": str,
        "Description": str,
        "KmsKey": str,
        "SourceURI": str,
        "ScheduleConfiguration": ScheduleConfigurationTypeDef,
        "Tags": Dict[str, str],
        "FileConfiguration": FileConfigurationTypeDef,
        "ObjectConfiguration": Dict[str, Dict[str, List[str]]],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateEventIntegrationRequestRequestTypeDef = TypedDict(
    "CreateEventIntegrationRequestRequestTypeDef",
    {
        "Name": str,
        "EventFilter": EventFilterTypeDef,
        "EventBridgeBus": str,
        "Description": NotRequired[str],
        "ClientToken": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
EventIntegrationTypeDef = TypedDict(
    "EventIntegrationTypeDef",
    {
        "EventIntegrationArn": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "EventFilter": NotRequired[EventFilterTypeDef],
        "EventBridgeBus": NotRequired[str],
        "Tags": NotRequired[Dict[str, str]],
    },
)
GetEventIntegrationResponseTypeDef = TypedDict(
    "GetEventIntegrationResponseTypeDef",
    {
        "Name": str,
        "Description": str,
        "EventIntegrationArn": str,
        "EventBridgeBus": str,
        "EventFilter": EventFilterTypeDef,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListDataIntegrationAssociationsResponseTypeDef = TypedDict(
    "ListDataIntegrationAssociationsResponseTypeDef",
    {
        "DataIntegrationAssociations": List[DataIntegrationAssociationSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListDataIntegrationsResponseTypeDef = TypedDict(
    "ListDataIntegrationsResponseTypeDef",
    {
        "DataIntegrations": List[DataIntegrationSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListEventIntegrationAssociationsResponseTypeDef = TypedDict(
    "ListEventIntegrationAssociationsResponseTypeDef",
    {
        "EventIntegrationAssociations": List[EventIntegrationAssociationTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListApplicationAssociationsRequestListApplicationAssociationsPaginateTypeDef = TypedDict(
    "ListApplicationAssociationsRequestListApplicationAssociationsPaginateTypeDef",
    {
        "ApplicationId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListApplicationsRequestListApplicationsPaginateTypeDef = TypedDict(
    "ListApplicationsRequestListApplicationsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDataIntegrationAssociationsRequestListDataIntegrationAssociationsPaginateTypeDef = TypedDict(
    "ListDataIntegrationAssociationsRequestListDataIntegrationAssociationsPaginateTypeDef",
    {
        "DataIntegrationIdentifier": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDataIntegrationsRequestListDataIntegrationsPaginateTypeDef = TypedDict(
    "ListDataIntegrationsRequestListDataIntegrationsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListEventIntegrationAssociationsRequestListEventIntegrationAssociationsPaginateTypeDef = TypedDict(
    "ListEventIntegrationAssociationsRequestListEventIntegrationAssociationsPaginateTypeDef",
    {
        "EventIntegrationName": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListEventIntegrationsRequestListEventIntegrationsPaginateTypeDef = TypedDict(
    "ListEventIntegrationsRequestListEventIntegrationsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
CreateApplicationRequestRequestTypeDef = TypedDict(
    "CreateApplicationRequestRequestTypeDef",
    {
        "Name": str,
        "Namespace": str,
        "ApplicationSourceConfig": ApplicationSourceConfigTypeDef,
        "Description": NotRequired[str],
        "Subscriptions": NotRequired[Sequence[SubscriptionTypeDef]],
        "Publications": NotRequired[Sequence[PublicationTypeDef]],
        "ClientToken": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
        "Permissions": NotRequired[Sequence[str]],
    },
)
GetApplicationResponseTypeDef = TypedDict(
    "GetApplicationResponseTypeDef",
    {
        "Arn": str,
        "Id": str,
        "Name": str,
        "Namespace": str,
        "Description": str,
        "ApplicationSourceConfig": ApplicationSourceConfigTypeDef,
        "Subscriptions": List[SubscriptionTypeDef],
        "Publications": List[PublicationTypeDef],
        "CreatedTime": datetime,
        "LastModifiedTime": datetime,
        "Tags": Dict[str, str],
        "Permissions": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateApplicationRequestRequestTypeDef = TypedDict(
    "UpdateApplicationRequestRequestTypeDef",
    {
        "Arn": str,
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "ApplicationSourceConfig": NotRequired[ApplicationSourceConfigTypeDef],
        "Subscriptions": NotRequired[Sequence[SubscriptionTypeDef]],
        "Publications": NotRequired[Sequence[PublicationTypeDef]],
        "Permissions": NotRequired[Sequence[str]],
    },
)
ListEventIntegrationsResponseTypeDef = TypedDict(
    "ListEventIntegrationsResponseTypeDef",
    {
        "EventIntegrations": List[EventIntegrationTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
