"""
Type annotations for appfabric service client.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appfabric/client/)

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_appfabric.client import AppFabricClient

    session = get_session()
    async with session.create_client("appfabric") as client:
        client: AppFabricClient
    ```
"""

import sys
from typing import Any, Dict, Mapping, Sequence, Type, overload

from aiobotocore.client import AioBaseClient
from botocore.client import ClientMeta

from .literals import AuthTypeType
from .paginator import (
    ListAppAuthorizationsPaginator,
    ListAppBundlesPaginator,
    ListIngestionDestinationsPaginator,
    ListIngestionsPaginator,
)
from .type_defs import (
    AuthRequestTypeDef,
    BatchGetUserAccessTasksResponseTypeDef,
    ConnectAppAuthorizationResponseTypeDef,
    CreateAppAuthorizationResponseTypeDef,
    CreateAppBundleResponseTypeDef,
    CreateIngestionDestinationResponseTypeDef,
    CreateIngestionResponseTypeDef,
    CredentialTypeDef,
    DestinationConfigurationTypeDef,
    GetAppAuthorizationResponseTypeDef,
    GetAppBundleResponseTypeDef,
    GetIngestionDestinationResponseTypeDef,
    GetIngestionResponseTypeDef,
    ListAppAuthorizationsResponseTypeDef,
    ListAppBundlesResponseTypeDef,
    ListIngestionDestinationsResponseTypeDef,
    ListIngestionsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ProcessingConfigurationTypeDef,
    StartUserAccessTasksResponseTypeDef,
    TagTypeDef,
    TenantTypeDef,
    UpdateAppAuthorizationResponseTypeDef,
    UpdateIngestionDestinationResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("AppFabricClient",)

class BotocoreClientError(Exception):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class AppFabricClient(AioBaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appfabric.html#AppFabric.Client)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appfabric/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        AppFabricClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appfabric.html#AppFabric.Client.exceptions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appfabric/client/#exceptions)
        """

    async def batch_get_user_access_tasks(
        self, *, appBundleIdentifier: str, taskIdList: Sequence[str]
    ) -> BatchGetUserAccessTasksResponseTypeDef:
        """
        Gets user access details in a batch request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appfabric.html#AppFabric.Client.batch_get_user_access_tasks)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appfabric/client/#batch_get_user_access_tasks)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appfabric.html#AppFabric.Client.can_paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appfabric/client/#can_paginate)
        """

    async def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appfabric.html#AppFabric.Client.close)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appfabric/client/#close)
        """

    async def connect_app_authorization(
        self,
        *,
        appBundleIdentifier: str,
        appAuthorizationIdentifier: str,
        authRequest: AuthRequestTypeDef = ...,
    ) -> ConnectAppAuthorizationResponseTypeDef:
        """
        Establishes a connection between Amazon Web Services AppFabric and an
        application, which allows AppFabric to call the APIs of the
        application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appfabric.html#AppFabric.Client.connect_app_authorization)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appfabric/client/#connect_app_authorization)
        """

    async def create_app_authorization(
        self,
        *,
        appBundleIdentifier: str,
        app: str,
        credential: CredentialTypeDef,
        tenant: TenantTypeDef,
        authType: AuthTypeType,
        clientToken: str = ...,
        tags: Sequence[TagTypeDef] = ...,
    ) -> CreateAppAuthorizationResponseTypeDef:
        """
        Creates an app authorization within an app bundle, which allows AppFabric to
        connect to an
        application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appfabric.html#AppFabric.Client.create_app_authorization)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appfabric/client/#create_app_authorization)
        """

    async def create_app_bundle(
        self,
        *,
        clientToken: str = ...,
        customerManagedKeyIdentifier: str = ...,
        tags: Sequence[TagTypeDef] = ...,
    ) -> CreateAppBundleResponseTypeDef:
        """
        Creates an app bundle to collect data from an application using AppFabric.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appfabric.html#AppFabric.Client.create_app_bundle)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appfabric/client/#create_app_bundle)
        """

    async def create_ingestion(
        self,
        *,
        appBundleIdentifier: str,
        app: str,
        tenantId: str,
        ingestionType: Literal["auditLog"],
        clientToken: str = ...,
        tags: Sequence[TagTypeDef] = ...,
    ) -> CreateIngestionResponseTypeDef:
        """
        Creates a data ingestion for an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appfabric.html#AppFabric.Client.create_ingestion)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appfabric/client/#create_ingestion)
        """

    async def create_ingestion_destination(
        self,
        *,
        appBundleIdentifier: str,
        ingestionIdentifier: str,
        processingConfiguration: ProcessingConfigurationTypeDef,
        destinationConfiguration: DestinationConfigurationTypeDef,
        clientToken: str = ...,
        tags: Sequence[TagTypeDef] = ...,
    ) -> CreateIngestionDestinationResponseTypeDef:
        """
        Creates an ingestion destination, which specifies how an application's ingested
        data is processed by Amazon Web Services AppFabric and where it's
        delivered.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appfabric.html#AppFabric.Client.create_ingestion_destination)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appfabric/client/#create_ingestion_destination)
        """

    async def delete_app_authorization(
        self, *, appBundleIdentifier: str, appAuthorizationIdentifier: str
    ) -> Dict[str, Any]:
        """
        Deletes an app authorization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appfabric.html#AppFabric.Client.delete_app_authorization)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appfabric/client/#delete_app_authorization)
        """

    async def delete_app_bundle(self, *, appBundleIdentifier: str) -> Dict[str, Any]:
        """
        Deletes an app bundle.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appfabric.html#AppFabric.Client.delete_app_bundle)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appfabric/client/#delete_app_bundle)
        """

    async def delete_ingestion(
        self, *, appBundleIdentifier: str, ingestionIdentifier: str
    ) -> Dict[str, Any]:
        """
        Deletes an ingestion.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appfabric.html#AppFabric.Client.delete_ingestion)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appfabric/client/#delete_ingestion)
        """

    async def delete_ingestion_destination(
        self,
        *,
        appBundleIdentifier: str,
        ingestionIdentifier: str,
        ingestionDestinationIdentifier: str,
    ) -> Dict[str, Any]:
        """
        Deletes an ingestion destination.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appfabric.html#AppFabric.Client.delete_ingestion_destination)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appfabric/client/#delete_ingestion_destination)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appfabric.html#AppFabric.Client.generate_presigned_url)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appfabric/client/#generate_presigned_url)
        """

    async def get_app_authorization(
        self, *, appBundleIdentifier: str, appAuthorizationIdentifier: str
    ) -> GetAppAuthorizationResponseTypeDef:
        """
        Returns information about an app authorization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appfabric.html#AppFabric.Client.get_app_authorization)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appfabric/client/#get_app_authorization)
        """

    async def get_app_bundle(self, *, appBundleIdentifier: str) -> GetAppBundleResponseTypeDef:
        """
        Returns information about an app bundle.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appfabric.html#AppFabric.Client.get_app_bundle)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appfabric/client/#get_app_bundle)
        """

    async def get_ingestion(
        self, *, appBundleIdentifier: str, ingestionIdentifier: str
    ) -> GetIngestionResponseTypeDef:
        """
        Returns information about an ingestion.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appfabric.html#AppFabric.Client.get_ingestion)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appfabric/client/#get_ingestion)
        """

    async def get_ingestion_destination(
        self,
        *,
        appBundleIdentifier: str,
        ingestionIdentifier: str,
        ingestionDestinationIdentifier: str,
    ) -> GetIngestionDestinationResponseTypeDef:
        """
        Returns information about an ingestion destination.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appfabric.html#AppFabric.Client.get_ingestion_destination)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appfabric/client/#get_ingestion_destination)
        """

    async def list_app_authorizations(
        self, *, appBundleIdentifier: str, maxResults: int = ..., nextToken: str = ...
    ) -> ListAppAuthorizationsResponseTypeDef:
        """
        Returns a list of all app authorizations configured for an app bundle.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appfabric.html#AppFabric.Client.list_app_authorizations)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appfabric/client/#list_app_authorizations)
        """

    async def list_app_bundles(
        self, *, maxResults: int = ..., nextToken: str = ...
    ) -> ListAppBundlesResponseTypeDef:
        """
        Returns a list of app bundles.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appfabric.html#AppFabric.Client.list_app_bundles)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appfabric/client/#list_app_bundles)
        """

    async def list_ingestion_destinations(
        self,
        *,
        appBundleIdentifier: str,
        ingestionIdentifier: str,
        maxResults: int = ...,
        nextToken: str = ...,
    ) -> ListIngestionDestinationsResponseTypeDef:
        """
        Returns a list of all ingestion destinations configured for an ingestion.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appfabric.html#AppFabric.Client.list_ingestion_destinations)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appfabric/client/#list_ingestion_destinations)
        """

    async def list_ingestions(
        self, *, appBundleIdentifier: str, maxResults: int = ..., nextToken: str = ...
    ) -> ListIngestionsResponseTypeDef:
        """
        Returns a list of all ingestions configured for an app bundle.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appfabric.html#AppFabric.Client.list_ingestions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appfabric/client/#list_ingestions)
        """

    async def list_tags_for_resource(
        self, *, resourceArn: str
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Returns a list of tags for a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appfabric.html#AppFabric.Client.list_tags_for_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appfabric/client/#list_tags_for_resource)
        """

    async def start_ingestion(
        self, *, ingestionIdentifier: str, appBundleIdentifier: str
    ) -> Dict[str, Any]:
        """
        Starts (enables) an ingestion, which collects data from an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appfabric.html#AppFabric.Client.start_ingestion)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appfabric/client/#start_ingestion)
        """

    async def start_user_access_tasks(
        self, *, appBundleIdentifier: str, email: str
    ) -> StartUserAccessTasksResponseTypeDef:
        """
        Starts the tasks to search user access status for a specific email address.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appfabric.html#AppFabric.Client.start_user_access_tasks)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appfabric/client/#start_user_access_tasks)
        """

    async def stop_ingestion(
        self, *, ingestionIdentifier: str, appBundleIdentifier: str
    ) -> Dict[str, Any]:
        """
        Stops (disables) an ingestion.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appfabric.html#AppFabric.Client.stop_ingestion)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appfabric/client/#stop_ingestion)
        """

    async def tag_resource(self, *, resourceArn: str, tags: Sequence[TagTypeDef]) -> Dict[str, Any]:
        """
        Assigns one or more tags (key-value pairs) to the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appfabric.html#AppFabric.Client.tag_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appfabric/client/#tag_resource)
        """

    async def untag_resource(self, *, resourceArn: str, tagKeys: Sequence[str]) -> Dict[str, Any]:
        """
        Removes a tag or tags from a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appfabric.html#AppFabric.Client.untag_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appfabric/client/#untag_resource)
        """

    async def update_app_authorization(
        self,
        *,
        appBundleIdentifier: str,
        appAuthorizationIdentifier: str,
        credential: CredentialTypeDef = ...,
        tenant: TenantTypeDef = ...,
    ) -> UpdateAppAuthorizationResponseTypeDef:
        """
        Updates an app authorization within an app bundle, which allows AppFabric to
        connect to an
        application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appfabric.html#AppFabric.Client.update_app_authorization)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appfabric/client/#update_app_authorization)
        """

    async def update_ingestion_destination(
        self,
        *,
        appBundleIdentifier: str,
        ingestionIdentifier: str,
        ingestionDestinationIdentifier: str,
        destinationConfiguration: DestinationConfigurationTypeDef,
    ) -> UpdateIngestionDestinationResponseTypeDef:
        """
        Updates an ingestion destination, which specifies how an application's ingested
        data is processed by Amazon Web Services AppFabric and where it's
        delivered.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appfabric.html#AppFabric.Client.update_ingestion_destination)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appfabric/client/#update_ingestion_destination)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_app_authorizations"]
    ) -> ListAppAuthorizationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appfabric.html#AppFabric.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appfabric/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_app_bundles"]) -> ListAppBundlesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appfabric.html#AppFabric.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appfabric/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_ingestion_destinations"]
    ) -> ListIngestionDestinationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appfabric.html#AppFabric.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appfabric/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_ingestions"]) -> ListIngestionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appfabric.html#AppFabric.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appfabric/client/#get_paginator)
        """

    async def __aenter__(self) -> "AppFabricClient":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appfabric.html#AppFabric.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appfabric/client/)
        """

    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> Any:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appfabric.html#AppFabric.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appfabric/client/)
        """
