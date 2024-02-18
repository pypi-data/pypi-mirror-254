"""
Type annotations for appintegrations service client.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appintegrations/client/)

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_appintegrations.client import AppIntegrationsServiceClient

    session = get_session()
    async with session.create_client("appintegrations") as client:
        client: AppIntegrationsServiceClient
    ```
"""

import sys
from typing import Any, Dict, Mapping, Sequence, Type, overload

from aiobotocore.client import AioBaseClient
from botocore.client import ClientMeta

from .paginator import (
    ListApplicationAssociationsPaginator,
    ListApplicationsPaginator,
    ListDataIntegrationAssociationsPaginator,
    ListDataIntegrationsPaginator,
    ListEventIntegrationAssociationsPaginator,
    ListEventIntegrationsPaginator,
)
from .type_defs import (
    ApplicationSourceConfigTypeDef,
    CreateApplicationResponseTypeDef,
    CreateDataIntegrationResponseTypeDef,
    CreateEventIntegrationResponseTypeDef,
    EventFilterTypeDef,
    FileConfigurationTypeDef,
    GetApplicationResponseTypeDef,
    GetDataIntegrationResponseTypeDef,
    GetEventIntegrationResponseTypeDef,
    ListApplicationAssociationsResponseTypeDef,
    ListApplicationsResponseTypeDef,
    ListDataIntegrationAssociationsResponseTypeDef,
    ListDataIntegrationsResponseTypeDef,
    ListEventIntegrationAssociationsResponseTypeDef,
    ListEventIntegrationsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    PublicationTypeDef,
    ScheduleConfigurationTypeDef,
    SubscriptionTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("AppIntegrationsServiceClient",)


class BotocoreClientError(Exception):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    DuplicateResourceException: Type[BotocoreClientError]
    InternalServiceError: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ResourceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    UnsupportedOperationException: Type[BotocoreClientError]


class AppIntegrationsServiceClient(AioBaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appintegrations.html#AppIntegrationsService.Client)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appintegrations/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        AppIntegrationsServiceClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appintegrations.html#AppIntegrationsService.Client.exceptions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appintegrations/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appintegrations.html#AppIntegrationsService.Client.can_paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appintegrations/client/#can_paginate)
        """

    async def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appintegrations.html#AppIntegrationsService.Client.close)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appintegrations/client/#close)
        """

    async def create_application(
        self,
        *,
        Name: str,
        Namespace: str,
        ApplicationSourceConfig: ApplicationSourceConfigTypeDef,
        Description: str = ...,
        Subscriptions: Sequence[SubscriptionTypeDef] = ...,
        Publications: Sequence[PublicationTypeDef] = ...,
        ClientToken: str = ...,
        Tags: Mapping[str, str] = ...,
        Permissions: Sequence[str] = ...,
    ) -> CreateApplicationResponseTypeDef:
        """
        This API is in preview release and subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appintegrations.html#AppIntegrationsService.Client.create_application)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appintegrations/client/#create_application)
        """

    async def create_data_integration(
        self,
        *,
        Name: str,
        KmsKey: str,
        SourceURI: str,
        Description: str = ...,
        ScheduleConfig: ScheduleConfigurationTypeDef = ...,
        Tags: Mapping[str, str] = ...,
        ClientToken: str = ...,
        FileConfiguration: FileConfigurationTypeDef = ...,
        ObjectConfiguration: Mapping[str, Mapping[str, Sequence[str]]] = ...,
    ) -> CreateDataIntegrationResponseTypeDef:
        """
        Creates and persists a DataIntegration resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appintegrations.html#AppIntegrationsService.Client.create_data_integration)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appintegrations/client/#create_data_integration)
        """

    async def create_event_integration(
        self,
        *,
        Name: str,
        EventFilter: EventFilterTypeDef,
        EventBridgeBus: str,
        Description: str = ...,
        ClientToken: str = ...,
        Tags: Mapping[str, str] = ...,
    ) -> CreateEventIntegrationResponseTypeDef:
        """
        Creates an EventIntegration, given a specified name, description, and a
        reference to an Amazon EventBridge bus in your account and a partner event
        source that pushes events to that
        bus.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appintegrations.html#AppIntegrationsService.Client.create_event_integration)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appintegrations/client/#create_event_integration)
        """

    async def delete_application(self, *, Arn: str) -> Dict[str, Any]:
        """
        Deletes the Application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appintegrations.html#AppIntegrationsService.Client.delete_application)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appintegrations/client/#delete_application)
        """

    async def delete_data_integration(self, *, DataIntegrationIdentifier: str) -> Dict[str, Any]:
        """
        Deletes the DataIntegration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appintegrations.html#AppIntegrationsService.Client.delete_data_integration)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appintegrations/client/#delete_data_integration)
        """

    async def delete_event_integration(self, *, Name: str) -> Dict[str, Any]:
        """
        Deletes the specified existing event integration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appintegrations.html#AppIntegrationsService.Client.delete_event_integration)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appintegrations/client/#delete_event_integration)
        """

    async def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appintegrations.html#AppIntegrationsService.Client.generate_presigned_url)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appintegrations/client/#generate_presigned_url)
        """

    async def get_application(self, *, Arn: str) -> GetApplicationResponseTypeDef:
        """
        This API is in preview release and subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appintegrations.html#AppIntegrationsService.Client.get_application)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appintegrations/client/#get_application)
        """

    async def get_data_integration(self, *, Identifier: str) -> GetDataIntegrationResponseTypeDef:
        """
        Returns information about the DataIntegration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appintegrations.html#AppIntegrationsService.Client.get_data_integration)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appintegrations/client/#get_data_integration)
        """

    async def get_event_integration(self, *, Name: str) -> GetEventIntegrationResponseTypeDef:
        """
        Returns information about the event integration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appintegrations.html#AppIntegrationsService.Client.get_event_integration)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appintegrations/client/#get_event_integration)
        """

    async def list_application_associations(
        self, *, ApplicationId: str, NextToken: str = ..., MaxResults: int = ...
    ) -> ListApplicationAssociationsResponseTypeDef:
        """
        Returns a paginated list of application associations for an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appintegrations.html#AppIntegrationsService.Client.list_application_associations)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appintegrations/client/#list_application_associations)
        """

    async def list_applications(
        self, *, NextToken: str = ..., MaxResults: int = ...
    ) -> ListApplicationsResponseTypeDef:
        """
        This API is in preview release and subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appintegrations.html#AppIntegrationsService.Client.list_applications)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appintegrations/client/#list_applications)
        """

    async def list_data_integration_associations(
        self, *, DataIntegrationIdentifier: str, NextToken: str = ..., MaxResults: int = ...
    ) -> ListDataIntegrationAssociationsResponseTypeDef:
        """
        Returns a paginated list of DataIntegration associations in the account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appintegrations.html#AppIntegrationsService.Client.list_data_integration_associations)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appintegrations/client/#list_data_integration_associations)
        """

    async def list_data_integrations(
        self, *, NextToken: str = ..., MaxResults: int = ...
    ) -> ListDataIntegrationsResponseTypeDef:
        """
        Returns a paginated list of DataIntegrations in the account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appintegrations.html#AppIntegrationsService.Client.list_data_integrations)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appintegrations/client/#list_data_integrations)
        """

    async def list_event_integration_associations(
        self, *, EventIntegrationName: str, NextToken: str = ..., MaxResults: int = ...
    ) -> ListEventIntegrationAssociationsResponseTypeDef:
        """
        Returns a paginated list of event integration associations in the account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appintegrations.html#AppIntegrationsService.Client.list_event_integration_associations)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appintegrations/client/#list_event_integration_associations)
        """

    async def list_event_integrations(
        self, *, NextToken: str = ..., MaxResults: int = ...
    ) -> ListEventIntegrationsResponseTypeDef:
        """
        Returns a paginated list of event integrations in the account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appintegrations.html#AppIntegrationsService.Client.list_event_integrations)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appintegrations/client/#list_event_integrations)
        """

    async def list_tags_for_resource(
        self, *, resourceArn: str
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists the tags for the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appintegrations.html#AppIntegrationsService.Client.list_tags_for_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appintegrations/client/#list_tags_for_resource)
        """

    async def tag_resource(self, *, resourceArn: str, tags: Mapping[str, str]) -> Dict[str, Any]:
        """
        Adds the specified tags to the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appintegrations.html#AppIntegrationsService.Client.tag_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appintegrations/client/#tag_resource)
        """

    async def untag_resource(self, *, resourceArn: str, tagKeys: Sequence[str]) -> Dict[str, Any]:
        """
        Removes the specified tags from the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appintegrations.html#AppIntegrationsService.Client.untag_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appintegrations/client/#untag_resource)
        """

    async def update_application(
        self,
        *,
        Arn: str,
        Name: str = ...,
        Description: str = ...,
        ApplicationSourceConfig: ApplicationSourceConfigTypeDef = ...,
        Subscriptions: Sequence[SubscriptionTypeDef] = ...,
        Publications: Sequence[PublicationTypeDef] = ...,
        Permissions: Sequence[str] = ...,
    ) -> Dict[str, Any]:
        """
        This API is in preview release and subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appintegrations.html#AppIntegrationsService.Client.update_application)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appintegrations/client/#update_application)
        """

    async def update_data_integration(
        self, *, Identifier: str, Name: str = ..., Description: str = ...
    ) -> Dict[str, Any]:
        """
        Updates the description of a DataIntegration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appintegrations.html#AppIntegrationsService.Client.update_data_integration)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appintegrations/client/#update_data_integration)
        """

    async def update_event_integration(
        self, *, Name: str, Description: str = ...
    ) -> Dict[str, Any]:
        """
        Updates the description of an event integration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appintegrations.html#AppIntegrationsService.Client.update_event_integration)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appintegrations/client/#update_event_integration)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_application_associations"]
    ) -> ListApplicationAssociationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appintegrations.html#AppIntegrationsService.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appintegrations/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_applications"]
    ) -> ListApplicationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appintegrations.html#AppIntegrationsService.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appintegrations/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_data_integration_associations"]
    ) -> ListDataIntegrationAssociationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appintegrations.html#AppIntegrationsService.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appintegrations/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_data_integrations"]
    ) -> ListDataIntegrationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appintegrations.html#AppIntegrationsService.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appintegrations/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_event_integration_associations"]
    ) -> ListEventIntegrationAssociationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appintegrations.html#AppIntegrationsService.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appintegrations/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_event_integrations"]
    ) -> ListEventIntegrationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appintegrations.html#AppIntegrationsService.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appintegrations/client/#get_paginator)
        """

    async def __aenter__(self) -> "AppIntegrationsServiceClient":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appintegrations.html#AppIntegrationsService.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appintegrations/client/)
        """

    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> Any:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appintegrations.html#AppIntegrationsService.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appintegrations/client/)
        """
