"""
Type annotations for finspace service client.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_finspace/client/)

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_finspace.client import finspaceClient

    session = get_session()
    async with session.create_client("finspace") as client:
        client: finspaceClient
    ```
"""

import sys
from typing import Any, Dict, Mapping, Sequence, Type

from aiobotocore.client import AioBaseClient
from botocore.client import ClientMeta

from .literals import FederationModeType, KxAzModeType, KxClusterTypeType
from .paginator import ListKxEnvironmentsPaginator
from .type_defs import (
    AutoScalingConfigurationTypeDef,
    CapacityConfigurationTypeDef,
    ChangeRequestTypeDef,
    CodeConfigurationTypeDef,
    CreateEnvironmentResponseTypeDef,
    CreateKxChangesetResponseTypeDef,
    CreateKxClusterResponseTypeDef,
    CreateKxDatabaseResponseTypeDef,
    CreateKxDataviewResponseTypeDef,
    CreateKxEnvironmentResponseTypeDef,
    CreateKxScalingGroupResponseTypeDef,
    CreateKxUserResponseTypeDef,
    CreateKxVolumeResponseTypeDef,
    CustomDNSServerTypeDef,
    FederationParametersTypeDef,
    GetEnvironmentResponseTypeDef,
    GetKxChangesetResponseTypeDef,
    GetKxClusterResponseTypeDef,
    GetKxConnectionStringResponseTypeDef,
    GetKxDatabaseResponseTypeDef,
    GetKxDataviewResponseTypeDef,
    GetKxEnvironmentResponseTypeDef,
    GetKxScalingGroupResponseTypeDef,
    GetKxUserResponseTypeDef,
    GetKxVolumeResponseTypeDef,
    KxCacheStorageConfigurationTypeDef,
    KxClusterCodeDeploymentConfigurationTypeDef,
    KxCommandLineArgumentTypeDef,
    KxDatabaseConfigurationTypeDef,
    KxDataviewSegmentConfigurationTypeDef,
    KxDeploymentConfigurationTypeDef,
    KxNAS1ConfigurationTypeDef,
    KxSavedownStorageConfigurationTypeDef,
    KxScalingGroupConfigurationTypeDef,
    ListEnvironmentsResponseTypeDef,
    ListKxChangesetsResponseTypeDef,
    ListKxClusterNodesResponseTypeDef,
    ListKxClustersResponseTypeDef,
    ListKxDatabasesResponseTypeDef,
    ListKxDataviewsResponseTypeDef,
    ListKxEnvironmentsResponseTypeDef,
    ListKxScalingGroupsResponseTypeDef,
    ListKxUsersResponseTypeDef,
    ListKxVolumesResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    SuperuserParametersTypeDef,
    TickerplantLogConfigurationTypeDef,
    TransitGatewayConfigurationTypeDef,
    UpdateEnvironmentResponseTypeDef,
    UpdateKxDatabaseResponseTypeDef,
    UpdateKxDataviewResponseTypeDef,
    UpdateKxEnvironmentNetworkResponseTypeDef,
    UpdateKxEnvironmentResponseTypeDef,
    UpdateKxUserResponseTypeDef,
    UpdateKxVolumeResponseTypeDef,
    VpcConfigurationTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("finspaceClient",)

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
    InvalidRequestException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ResourceAlreadyExistsException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class finspaceClient(AioBaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace.html#finspace.Client)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_finspace/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        finspaceClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace.html#finspace.Client.exceptions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_finspace/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace.html#finspace.Client.can_paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_finspace/client/#can_paginate)
        """

    async def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace.html#finspace.Client.close)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_finspace/client/#close)
        """

    async def create_environment(
        self,
        *,
        name: str,
        description: str = ...,
        kmsKeyId: str = ...,
        tags: Mapping[str, str] = ...,
        federationMode: FederationModeType = ...,
        federationParameters: FederationParametersTypeDef = ...,
        superuserParameters: SuperuserParametersTypeDef = ...,
        dataBundles: Sequence[str] = ...,
    ) -> CreateEnvironmentResponseTypeDef:
        """
        Create a new FinSpace environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace.html#finspace.Client.create_environment)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_finspace/client/#create_environment)
        """

    async def create_kx_changeset(
        self,
        *,
        environmentId: str,
        databaseName: str,
        changeRequests: Sequence[ChangeRequestTypeDef],
        clientToken: str,
    ) -> CreateKxChangesetResponseTypeDef:
        """
        Creates a changeset for a kdb database.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace.html#finspace.Client.create_kx_changeset)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_finspace/client/#create_kx_changeset)
        """

    async def create_kx_cluster(
        self,
        *,
        environmentId: str,
        clusterName: str,
        clusterType: KxClusterTypeType,
        releaseLabel: str,
        vpcConfiguration: VpcConfigurationTypeDef,
        azMode: KxAzModeType,
        clientToken: str = ...,
        tickerplantLogConfiguration: TickerplantLogConfigurationTypeDef = ...,
        databases: Sequence[KxDatabaseConfigurationTypeDef] = ...,
        cacheStorageConfigurations: Sequence[KxCacheStorageConfigurationTypeDef] = ...,
        autoScalingConfiguration: AutoScalingConfigurationTypeDef = ...,
        clusterDescription: str = ...,
        capacityConfiguration: CapacityConfigurationTypeDef = ...,
        initializationScript: str = ...,
        commandLineArguments: Sequence[KxCommandLineArgumentTypeDef] = ...,
        code: CodeConfigurationTypeDef = ...,
        executionRole: str = ...,
        savedownStorageConfiguration: KxSavedownStorageConfigurationTypeDef = ...,
        availabilityZoneId: str = ...,
        tags: Mapping[str, str] = ...,
        scalingGroupConfiguration: KxScalingGroupConfigurationTypeDef = ...,
    ) -> CreateKxClusterResponseTypeDef:
        """
        Creates a new kdb cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace.html#finspace.Client.create_kx_cluster)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_finspace/client/#create_kx_cluster)
        """

    async def create_kx_database(
        self,
        *,
        environmentId: str,
        databaseName: str,
        clientToken: str,
        description: str = ...,
        tags: Mapping[str, str] = ...,
    ) -> CreateKxDatabaseResponseTypeDef:
        """
        Creates a new kdb database in the environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace.html#finspace.Client.create_kx_database)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_finspace/client/#create_kx_database)
        """

    async def create_kx_dataview(
        self,
        *,
        environmentId: str,
        databaseName: str,
        dataviewName: str,
        azMode: KxAzModeType,
        clientToken: str,
        availabilityZoneId: str = ...,
        changesetId: str = ...,
        segmentConfigurations: Sequence[KxDataviewSegmentConfigurationTypeDef] = ...,
        autoUpdate: bool = ...,
        description: str = ...,
        tags: Mapping[str, str] = ...,
    ) -> CreateKxDataviewResponseTypeDef:
        """
        Creates a snapshot of kdb database with tiered storage capabilities and a
        pre-warmed cache, ready for mounting on kdb
        clusters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace.html#finspace.Client.create_kx_dataview)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_finspace/client/#create_kx_dataview)
        """

    async def create_kx_environment(
        self,
        *,
        name: str,
        kmsKeyId: str,
        description: str = ...,
        tags: Mapping[str, str] = ...,
        clientToken: str = ...,
    ) -> CreateKxEnvironmentResponseTypeDef:
        """
        Creates a managed kdb environment for the account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace.html#finspace.Client.create_kx_environment)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_finspace/client/#create_kx_environment)
        """

    async def create_kx_scaling_group(
        self,
        *,
        clientToken: str,
        environmentId: str,
        scalingGroupName: str,
        hostType: str,
        availabilityZoneId: str,
        tags: Mapping[str, str] = ...,
    ) -> CreateKxScalingGroupResponseTypeDef:
        """
        Creates a new scaling group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace.html#finspace.Client.create_kx_scaling_group)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_finspace/client/#create_kx_scaling_group)
        """

    async def create_kx_user(
        self,
        *,
        environmentId: str,
        userName: str,
        iamRole: str,
        tags: Mapping[str, str] = ...,
        clientToken: str = ...,
    ) -> CreateKxUserResponseTypeDef:
        """
        Creates a user in FinSpace kdb environment with an associated IAM role.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace.html#finspace.Client.create_kx_user)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_finspace/client/#create_kx_user)
        """

    async def create_kx_volume(
        self,
        *,
        environmentId: str,
        volumeType: Literal["NAS_1"],
        volumeName: str,
        azMode: KxAzModeType,
        availabilityZoneIds: Sequence[str],
        clientToken: str = ...,
        description: str = ...,
        nas1Configuration: KxNAS1ConfigurationTypeDef = ...,
        tags: Mapping[str, str] = ...,
    ) -> CreateKxVolumeResponseTypeDef:
        """
        Creates a new volume with a specific amount of throughput and storage capacity.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace.html#finspace.Client.create_kx_volume)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_finspace/client/#create_kx_volume)
        """

    async def delete_environment(self, *, environmentId: str) -> Dict[str, Any]:
        """
        Delete an FinSpace environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace.html#finspace.Client.delete_environment)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_finspace/client/#delete_environment)
        """

    async def delete_kx_cluster(
        self, *, environmentId: str, clusterName: str, clientToken: str = ...
    ) -> Dict[str, Any]:
        """
        Deletes a kdb cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace.html#finspace.Client.delete_kx_cluster)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_finspace/client/#delete_kx_cluster)
        """

    async def delete_kx_database(
        self, *, environmentId: str, databaseName: str, clientToken: str
    ) -> Dict[str, Any]:
        """
        Deletes the specified database and all of its associated data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace.html#finspace.Client.delete_kx_database)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_finspace/client/#delete_kx_database)
        """

    async def delete_kx_dataview(
        self, *, environmentId: str, databaseName: str, dataviewName: str, clientToken: str
    ) -> Dict[str, Any]:
        """
        Deletes the specified dataview.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace.html#finspace.Client.delete_kx_dataview)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_finspace/client/#delete_kx_dataview)
        """

    async def delete_kx_environment(
        self, *, environmentId: str, clientToken: str = ...
    ) -> Dict[str, Any]:
        """
        Deletes the kdb environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace.html#finspace.Client.delete_kx_environment)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_finspace/client/#delete_kx_environment)
        """

    async def delete_kx_scaling_group(
        self, *, environmentId: str, scalingGroupName: str, clientToken: str = ...
    ) -> Dict[str, Any]:
        """
        Deletes the specified scaling group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace.html#finspace.Client.delete_kx_scaling_group)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_finspace/client/#delete_kx_scaling_group)
        """

    async def delete_kx_user(
        self, *, userName: str, environmentId: str, clientToken: str = ...
    ) -> Dict[str, Any]:
        """
        Deletes a user in the specified kdb environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace.html#finspace.Client.delete_kx_user)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_finspace/client/#delete_kx_user)
        """

    async def delete_kx_volume(
        self, *, environmentId: str, volumeName: str, clientToken: str = ...
    ) -> Dict[str, Any]:
        """
        Deletes a volume.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace.html#finspace.Client.delete_kx_volume)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_finspace/client/#delete_kx_volume)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace.html#finspace.Client.generate_presigned_url)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_finspace/client/#generate_presigned_url)
        """

    async def get_environment(self, *, environmentId: str) -> GetEnvironmentResponseTypeDef:
        """
        Returns the FinSpace environment object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace.html#finspace.Client.get_environment)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_finspace/client/#get_environment)
        """

    async def get_kx_changeset(
        self, *, environmentId: str, databaseName: str, changesetId: str
    ) -> GetKxChangesetResponseTypeDef:
        """
        Returns information about a kdb changeset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace.html#finspace.Client.get_kx_changeset)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_finspace/client/#get_kx_changeset)
        """

    async def get_kx_cluster(
        self, *, environmentId: str, clusterName: str
    ) -> GetKxClusterResponseTypeDef:
        """
        Retrieves information about a kdb cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace.html#finspace.Client.get_kx_cluster)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_finspace/client/#get_kx_cluster)
        """

    async def get_kx_connection_string(
        self, *, userArn: str, environmentId: str, clusterName: str
    ) -> GetKxConnectionStringResponseTypeDef:
        """
        Retrieves a connection string for a user to connect to a kdb cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace.html#finspace.Client.get_kx_connection_string)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_finspace/client/#get_kx_connection_string)
        """

    async def get_kx_database(
        self, *, environmentId: str, databaseName: str
    ) -> GetKxDatabaseResponseTypeDef:
        """
        Returns database information for the specified environment ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace.html#finspace.Client.get_kx_database)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_finspace/client/#get_kx_database)
        """

    async def get_kx_dataview(
        self, *, environmentId: str, databaseName: str, dataviewName: str
    ) -> GetKxDataviewResponseTypeDef:
        """
        Retrieves details of the dataview.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace.html#finspace.Client.get_kx_dataview)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_finspace/client/#get_kx_dataview)
        """

    async def get_kx_environment(self, *, environmentId: str) -> GetKxEnvironmentResponseTypeDef:
        """
        Retrieves all the information for the specified kdb environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace.html#finspace.Client.get_kx_environment)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_finspace/client/#get_kx_environment)
        """

    async def get_kx_scaling_group(
        self, *, environmentId: str, scalingGroupName: str
    ) -> GetKxScalingGroupResponseTypeDef:
        """
        Retrieves details of a scaling group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace.html#finspace.Client.get_kx_scaling_group)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_finspace/client/#get_kx_scaling_group)
        """

    async def get_kx_user(self, *, userName: str, environmentId: str) -> GetKxUserResponseTypeDef:
        """
        Retrieves information about the specified kdb user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace.html#finspace.Client.get_kx_user)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_finspace/client/#get_kx_user)
        """

    async def get_kx_volume(
        self, *, environmentId: str, volumeName: str
    ) -> GetKxVolumeResponseTypeDef:
        """
        Retrieves the information about the volume.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace.html#finspace.Client.get_kx_volume)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_finspace/client/#get_kx_volume)
        """

    async def list_environments(
        self, *, nextToken: str = ..., maxResults: int = ...
    ) -> ListEnvironmentsResponseTypeDef:
        """
        A list of all of your FinSpace environments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace.html#finspace.Client.list_environments)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_finspace/client/#list_environments)
        """

    async def list_kx_changesets(
        self, *, environmentId: str, databaseName: str, nextToken: str = ..., maxResults: int = ...
    ) -> ListKxChangesetsResponseTypeDef:
        """
        Returns a list of all the changesets for a database.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace.html#finspace.Client.list_kx_changesets)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_finspace/client/#list_kx_changesets)
        """

    async def list_kx_cluster_nodes(
        self, *, environmentId: str, clusterName: str, nextToken: str = ..., maxResults: int = ...
    ) -> ListKxClusterNodesResponseTypeDef:
        """
        Lists all the nodes in a kdb cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace.html#finspace.Client.list_kx_cluster_nodes)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_finspace/client/#list_kx_cluster_nodes)
        """

    async def list_kx_clusters(
        self,
        *,
        environmentId: str,
        clusterType: KxClusterTypeType = ...,
        maxResults: int = ...,
        nextToken: str = ...,
    ) -> ListKxClustersResponseTypeDef:
        """
        Returns a list of clusters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace.html#finspace.Client.list_kx_clusters)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_finspace/client/#list_kx_clusters)
        """

    async def list_kx_databases(
        self, *, environmentId: str, nextToken: str = ..., maxResults: int = ...
    ) -> ListKxDatabasesResponseTypeDef:
        """
        Returns a list of all the databases in the kdb environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace.html#finspace.Client.list_kx_databases)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_finspace/client/#list_kx_databases)
        """

    async def list_kx_dataviews(
        self, *, environmentId: str, databaseName: str, nextToken: str = ..., maxResults: int = ...
    ) -> ListKxDataviewsResponseTypeDef:
        """
        Returns a list of all the dataviews in the database.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace.html#finspace.Client.list_kx_dataviews)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_finspace/client/#list_kx_dataviews)
        """

    async def list_kx_environments(
        self, *, nextToken: str = ..., maxResults: int = ...
    ) -> ListKxEnvironmentsResponseTypeDef:
        """
        Returns a list of kdb environments created in an account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace.html#finspace.Client.list_kx_environments)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_finspace/client/#list_kx_environments)
        """

    async def list_kx_scaling_groups(
        self, *, environmentId: str, maxResults: int = ..., nextToken: str = ...
    ) -> ListKxScalingGroupsResponseTypeDef:
        """
        Returns a list of scaling groups in a kdb environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace.html#finspace.Client.list_kx_scaling_groups)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_finspace/client/#list_kx_scaling_groups)
        """

    async def list_kx_users(
        self, *, environmentId: str, nextToken: str = ..., maxResults: int = ...
    ) -> ListKxUsersResponseTypeDef:
        """
        Lists all the users in a kdb environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace.html#finspace.Client.list_kx_users)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_finspace/client/#list_kx_users)
        """

    async def list_kx_volumes(
        self,
        *,
        environmentId: str,
        maxResults: int = ...,
        nextToken: str = ...,
        volumeType: Literal["NAS_1"] = ...,
    ) -> ListKxVolumesResponseTypeDef:
        """
        Lists all the volumes in a kdb environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace.html#finspace.Client.list_kx_volumes)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_finspace/client/#list_kx_volumes)
        """

    async def list_tags_for_resource(
        self, *, resourceArn: str
    ) -> ListTagsForResourceResponseTypeDef:
        """
        A list of all tags for a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace.html#finspace.Client.list_tags_for_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_finspace/client/#list_tags_for_resource)
        """

    async def tag_resource(self, *, resourceArn: str, tags: Mapping[str, str]) -> Dict[str, Any]:
        """
        Adds metadata tags to a FinSpace resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace.html#finspace.Client.tag_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_finspace/client/#tag_resource)
        """

    async def untag_resource(self, *, resourceArn: str, tagKeys: Sequence[str]) -> Dict[str, Any]:
        """
        Removes metadata tags from a FinSpace resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace.html#finspace.Client.untag_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_finspace/client/#untag_resource)
        """

    async def update_environment(
        self,
        *,
        environmentId: str,
        name: str = ...,
        description: str = ...,
        federationMode: FederationModeType = ...,
        federationParameters: FederationParametersTypeDef = ...,
    ) -> UpdateEnvironmentResponseTypeDef:
        """
        Update your FinSpace environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace.html#finspace.Client.update_environment)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_finspace/client/#update_environment)
        """

    async def update_kx_cluster_code_configuration(
        self,
        *,
        environmentId: str,
        clusterName: str,
        code: CodeConfigurationTypeDef,
        clientToken: str = ...,
        initializationScript: str = ...,
        commandLineArguments: Sequence[KxCommandLineArgumentTypeDef] = ...,
        deploymentConfiguration: KxClusterCodeDeploymentConfigurationTypeDef = ...,
    ) -> Dict[str, Any]:
        """
        Allows you to update code configuration on a running cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace.html#finspace.Client.update_kx_cluster_code_configuration)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_finspace/client/#update_kx_cluster_code_configuration)
        """

    async def update_kx_cluster_databases(
        self,
        *,
        environmentId: str,
        clusterName: str,
        databases: Sequence[KxDatabaseConfigurationTypeDef],
        clientToken: str = ...,
        deploymentConfiguration: KxDeploymentConfigurationTypeDef = ...,
    ) -> Dict[str, Any]:
        """
        Updates the databases mounted on a kdb cluster, which includes the
        `changesetId` and all the dbPaths to be
        cached.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace.html#finspace.Client.update_kx_cluster_databases)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_finspace/client/#update_kx_cluster_databases)
        """

    async def update_kx_database(
        self, *, environmentId: str, databaseName: str, clientToken: str, description: str = ...
    ) -> UpdateKxDatabaseResponseTypeDef:
        """
        Updates information for the given kdb database.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace.html#finspace.Client.update_kx_database)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_finspace/client/#update_kx_database)
        """

    async def update_kx_dataview(
        self,
        *,
        environmentId: str,
        databaseName: str,
        dataviewName: str,
        clientToken: str,
        description: str = ...,
        changesetId: str = ...,
        segmentConfigurations: Sequence[KxDataviewSegmentConfigurationTypeDef] = ...,
    ) -> UpdateKxDataviewResponseTypeDef:
        """
        Updates the specified dataview.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace.html#finspace.Client.update_kx_dataview)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_finspace/client/#update_kx_dataview)
        """

    async def update_kx_environment(
        self, *, environmentId: str, name: str = ..., description: str = ..., clientToken: str = ...
    ) -> UpdateKxEnvironmentResponseTypeDef:
        """
        Updates information for the given kdb environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace.html#finspace.Client.update_kx_environment)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_finspace/client/#update_kx_environment)
        """

    async def update_kx_environment_network(
        self,
        *,
        environmentId: str,
        transitGatewayConfiguration: TransitGatewayConfigurationTypeDef = ...,
        customDNSConfiguration: Sequence[CustomDNSServerTypeDef] = ...,
        clientToken: str = ...,
    ) -> UpdateKxEnvironmentNetworkResponseTypeDef:
        """
        Updates environment network to connect to your internal network by using a
        transit
        gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace.html#finspace.Client.update_kx_environment_network)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_finspace/client/#update_kx_environment_network)
        """

    async def update_kx_user(
        self, *, environmentId: str, userName: str, iamRole: str, clientToken: str = ...
    ) -> UpdateKxUserResponseTypeDef:
        """
        Updates the user details.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace.html#finspace.Client.update_kx_user)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_finspace/client/#update_kx_user)
        """

    async def update_kx_volume(
        self,
        *,
        environmentId: str,
        volumeName: str,
        description: str = ...,
        clientToken: str = ...,
        nas1Configuration: KxNAS1ConfigurationTypeDef = ...,
    ) -> UpdateKxVolumeResponseTypeDef:
        """
        Updates the throughput or capacity of a volume.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace.html#finspace.Client.update_kx_volume)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_finspace/client/#update_kx_volume)
        """

    def get_paginator(
        self, operation_name: Literal["list_kx_environments"]
    ) -> ListKxEnvironmentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace.html#finspace.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_finspace/client/#get_paginator)
        """

    async def __aenter__(self) -> "finspaceClient":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace.html#finspace.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_finspace/client/)
        """

    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> Any:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace.html#finspace.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_finspace/client/)
        """
