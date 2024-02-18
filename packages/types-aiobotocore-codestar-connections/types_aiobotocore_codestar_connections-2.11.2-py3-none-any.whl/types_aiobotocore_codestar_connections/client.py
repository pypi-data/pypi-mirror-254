"""
Type annotations for codestar-connections service client.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codestar_connections/client/)

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_codestar_connections.client import CodeStarconnectionsClient

    session = get_session()
    async with session.create_client("codestar-connections") as client:
        client: CodeStarconnectionsClient
    ```
"""

import sys
from typing import Any, Dict, Mapping, Sequence, Type

from aiobotocore.client import AioBaseClient
from botocore.client import ClientMeta

from .literals import ProviderTypeType
from .type_defs import (
    CreateConnectionOutputTypeDef,
    CreateHostOutputTypeDef,
    CreateRepositoryLinkOutputTypeDef,
    CreateSyncConfigurationOutputTypeDef,
    GetConnectionOutputTypeDef,
    GetHostOutputTypeDef,
    GetRepositoryLinkOutputTypeDef,
    GetRepositorySyncStatusOutputTypeDef,
    GetResourceSyncStatusOutputTypeDef,
    GetSyncBlockerSummaryOutputTypeDef,
    GetSyncConfigurationOutputTypeDef,
    ListConnectionsOutputTypeDef,
    ListHostsOutputTypeDef,
    ListRepositoryLinksOutputTypeDef,
    ListRepositorySyncDefinitionsOutputTypeDef,
    ListSyncConfigurationsOutputTypeDef,
    ListTagsForResourceOutputTypeDef,
    TagTypeDef,
    UpdateRepositoryLinkOutputTypeDef,
    UpdateSyncBlockerOutputTypeDef,
    UpdateSyncConfigurationOutputTypeDef,
    VpcConfigurationTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("CodeStarconnectionsClient",)


class BotocoreClientError(Exception):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConcurrentModificationException: Type[BotocoreClientError]
    ConditionalCheckFailedException: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    InvalidInputException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ResourceAlreadyExistsException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ResourceUnavailableException: Type[BotocoreClientError]
    RetryLatestCommitFailedException: Type[BotocoreClientError]
    SyncBlockerDoesNotExistException: Type[BotocoreClientError]
    SyncConfigurationStillExistsException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    UnsupportedOperationException: Type[BotocoreClientError]
    UnsupportedProviderTypeException: Type[BotocoreClientError]
    UpdateOutOfSyncException: Type[BotocoreClientError]


class CodeStarconnectionsClient(AioBaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-connections.html#CodeStarconnections.Client)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codestar_connections/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        CodeStarconnectionsClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-connections.html#CodeStarconnections.Client.exceptions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codestar_connections/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-connections.html#CodeStarconnections.Client.can_paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codestar_connections/client/#can_paginate)
        """

    async def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-connections.html#CodeStarconnections.Client.close)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codestar_connections/client/#close)
        """

    async def create_connection(
        self,
        *,
        ConnectionName: str,
        ProviderType: ProviderTypeType = ...,
        Tags: Sequence[TagTypeDef] = ...,
        HostArn: str = ...,
    ) -> CreateConnectionOutputTypeDef:
        """
        Creates a connection that can then be given to other Amazon Web Services
        services like CodePipeline so that it can access third-party code
        repositories.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-connections.html#CodeStarconnections.Client.create_connection)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codestar_connections/client/#create_connection)
        """

    async def create_host(
        self,
        *,
        Name: str,
        ProviderType: ProviderTypeType,
        ProviderEndpoint: str,
        VpcConfiguration: VpcConfigurationTypeDef = ...,
        Tags: Sequence[TagTypeDef] = ...,
    ) -> CreateHostOutputTypeDef:
        """
        Creates a resource that represents the infrastructure where a third-party
        provider is
        installed.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-connections.html#CodeStarconnections.Client.create_host)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codestar_connections/client/#create_host)
        """

    async def create_repository_link(
        self,
        *,
        ConnectionArn: str,
        OwnerId: str,
        RepositoryName: str,
        EncryptionKeyArn: str = ...,
        Tags: Sequence[TagTypeDef] = ...,
    ) -> CreateRepositoryLinkOutputTypeDef:
        """
        Creates a link to a specified external Git repository.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-connections.html#CodeStarconnections.Client.create_repository_link)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codestar_connections/client/#create_repository_link)
        """

    async def create_sync_configuration(
        self,
        *,
        Branch: str,
        ConfigFile: str,
        RepositoryLinkId: str,
        ResourceName: str,
        RoleArn: str,
        SyncType: Literal["CFN_STACK_SYNC"],
    ) -> CreateSyncConfigurationOutputTypeDef:
        """
        Creates a sync configuration which allows Amazon Web Services to sync content
        from a Git repository to update a specified Amazon Web Services
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-connections.html#CodeStarconnections.Client.create_sync_configuration)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codestar_connections/client/#create_sync_configuration)
        """

    async def delete_connection(self, *, ConnectionArn: str) -> Dict[str, Any]:
        """
        The connection to be deleted.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-connections.html#CodeStarconnections.Client.delete_connection)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codestar_connections/client/#delete_connection)
        """

    async def delete_host(self, *, HostArn: str) -> Dict[str, Any]:
        """
        The host to be deleted.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-connections.html#CodeStarconnections.Client.delete_host)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codestar_connections/client/#delete_host)
        """

    async def delete_repository_link(self, *, RepositoryLinkId: str) -> Dict[str, Any]:
        """
        Deletes the association between your connection and a specified external Git
        repository.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-connections.html#CodeStarconnections.Client.delete_repository_link)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codestar_connections/client/#delete_repository_link)
        """

    async def delete_sync_configuration(
        self, *, SyncType: Literal["CFN_STACK_SYNC"], ResourceName: str
    ) -> Dict[str, Any]:
        """
        Deletes the sync configuration for a specified repository and connection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-connections.html#CodeStarconnections.Client.delete_sync_configuration)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codestar_connections/client/#delete_sync_configuration)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-connections.html#CodeStarconnections.Client.generate_presigned_url)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codestar_connections/client/#generate_presigned_url)
        """

    async def get_connection(self, *, ConnectionArn: str) -> GetConnectionOutputTypeDef:
        """
        Returns the connection ARN and details such as status, owner, and provider type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-connections.html#CodeStarconnections.Client.get_connection)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codestar_connections/client/#get_connection)
        """

    async def get_host(self, *, HostArn: str) -> GetHostOutputTypeDef:
        """
        Returns the host ARN and details such as status, provider type, endpoint, and,
        if applicable, the VPC
        configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-connections.html#CodeStarconnections.Client.get_host)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codestar_connections/client/#get_host)
        """

    async def get_repository_link(self, *, RepositoryLinkId: str) -> GetRepositoryLinkOutputTypeDef:
        """
        Returns details about a repository link.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-connections.html#CodeStarconnections.Client.get_repository_link)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codestar_connections/client/#get_repository_link)
        """

    async def get_repository_sync_status(
        self, *, Branch: str, RepositoryLinkId: str, SyncType: Literal["CFN_STACK_SYNC"]
    ) -> GetRepositorySyncStatusOutputTypeDef:
        """
        Returns details about the sync status for a repository.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-connections.html#CodeStarconnections.Client.get_repository_sync_status)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codestar_connections/client/#get_repository_sync_status)
        """

    async def get_resource_sync_status(
        self, *, ResourceName: str, SyncType: Literal["CFN_STACK_SYNC"]
    ) -> GetResourceSyncStatusOutputTypeDef:
        """
        Returns the status of the sync with the Git repository for a specific Amazon
        Web Services
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-connections.html#CodeStarconnections.Client.get_resource_sync_status)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codestar_connections/client/#get_resource_sync_status)
        """

    async def get_sync_blocker_summary(
        self, *, SyncType: Literal["CFN_STACK_SYNC"], ResourceName: str
    ) -> GetSyncBlockerSummaryOutputTypeDef:
        """
        Returns a list of the most recent sync blockers.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-connections.html#CodeStarconnections.Client.get_sync_blocker_summary)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codestar_connections/client/#get_sync_blocker_summary)
        """

    async def get_sync_configuration(
        self, *, SyncType: Literal["CFN_STACK_SYNC"], ResourceName: str
    ) -> GetSyncConfigurationOutputTypeDef:
        """
        Returns details about a sync configuration, including the sync type and
        resource
        name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-connections.html#CodeStarconnections.Client.get_sync_configuration)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codestar_connections/client/#get_sync_configuration)
        """

    async def list_connections(
        self,
        *,
        ProviderTypeFilter: ProviderTypeType = ...,
        HostArnFilter: str = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
    ) -> ListConnectionsOutputTypeDef:
        """
        Lists the connections associated with your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-connections.html#CodeStarconnections.Client.list_connections)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codestar_connections/client/#list_connections)
        """

    async def list_hosts(
        self, *, MaxResults: int = ..., NextToken: str = ...
    ) -> ListHostsOutputTypeDef:
        """
        Lists the hosts associated with your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-connections.html#CodeStarconnections.Client.list_hosts)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codestar_connections/client/#list_hosts)
        """

    async def list_repository_links(
        self, *, MaxResults: int = ..., NextToken: str = ...
    ) -> ListRepositoryLinksOutputTypeDef:
        """
        Lists the repository links created for connections in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-connections.html#CodeStarconnections.Client.list_repository_links)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codestar_connections/client/#list_repository_links)
        """

    async def list_repository_sync_definitions(
        self, *, RepositoryLinkId: str, SyncType: Literal["CFN_STACK_SYNC"]
    ) -> ListRepositorySyncDefinitionsOutputTypeDef:
        """
        Lists the repository sync definitions for repository links in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-connections.html#CodeStarconnections.Client.list_repository_sync_definitions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codestar_connections/client/#list_repository_sync_definitions)
        """

    async def list_sync_configurations(
        self,
        *,
        RepositoryLinkId: str,
        SyncType: Literal["CFN_STACK_SYNC"],
        MaxResults: int = ...,
        NextToken: str = ...,
    ) -> ListSyncConfigurationsOutputTypeDef:
        """
        Returns a list of sync configurations for a specified repository.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-connections.html#CodeStarconnections.Client.list_sync_configurations)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codestar_connections/client/#list_sync_configurations)
        """

    async def list_tags_for_resource(self, *, ResourceArn: str) -> ListTagsForResourceOutputTypeDef:
        """
        Gets the set of key-value pairs (metadata) that are used to manage the resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-connections.html#CodeStarconnections.Client.list_tags_for_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codestar_connections/client/#list_tags_for_resource)
        """

    async def tag_resource(self, *, ResourceArn: str, Tags: Sequence[TagTypeDef]) -> Dict[str, Any]:
        """
        Adds to or modifies the tags of the given resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-connections.html#CodeStarconnections.Client.tag_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codestar_connections/client/#tag_resource)
        """

    async def untag_resource(self, *, ResourceArn: str, TagKeys: Sequence[str]) -> Dict[str, Any]:
        """
        Removes tags from an Amazon Web Services resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-connections.html#CodeStarconnections.Client.untag_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codestar_connections/client/#untag_resource)
        """

    async def update_host(
        self,
        *,
        HostArn: str,
        ProviderEndpoint: str = ...,
        VpcConfiguration: VpcConfigurationTypeDef = ...,
    ) -> Dict[str, Any]:
        """
        Updates a specified host with the provided configurations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-connections.html#CodeStarconnections.Client.update_host)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codestar_connections/client/#update_host)
        """

    async def update_repository_link(
        self, *, RepositoryLinkId: str, ConnectionArn: str = ..., EncryptionKeyArn: str = ...
    ) -> UpdateRepositoryLinkOutputTypeDef:
        """
        Updates the association between your connection and a specified external Git
        repository.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-connections.html#CodeStarconnections.Client.update_repository_link)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codestar_connections/client/#update_repository_link)
        """

    async def update_sync_blocker(
        self,
        *,
        Id: str,
        SyncType: Literal["CFN_STACK_SYNC"],
        ResourceName: str,
        ResolvedReason: str,
    ) -> UpdateSyncBlockerOutputTypeDef:
        """
        Allows you to update the status of a sync blocker, resolving the blocker and
        allowing syncing to
        continue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-connections.html#CodeStarconnections.Client.update_sync_blocker)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codestar_connections/client/#update_sync_blocker)
        """

    async def update_sync_configuration(
        self,
        *,
        ResourceName: str,
        SyncType: Literal["CFN_STACK_SYNC"],
        Branch: str = ...,
        ConfigFile: str = ...,
        RepositoryLinkId: str = ...,
        RoleArn: str = ...,
    ) -> UpdateSyncConfigurationOutputTypeDef:
        """
        Updates the sync configuration for your connection and a specified external Git
        repository.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-connections.html#CodeStarconnections.Client.update_sync_configuration)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codestar_connections/client/#update_sync_configuration)
        """

    async def __aenter__(self) -> "CodeStarconnectionsClient":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-connections.html#CodeStarconnections.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codestar_connections/client/)
        """

    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> Any:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-connections.html#CodeStarconnections.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codestar_connections/client/)
        """
