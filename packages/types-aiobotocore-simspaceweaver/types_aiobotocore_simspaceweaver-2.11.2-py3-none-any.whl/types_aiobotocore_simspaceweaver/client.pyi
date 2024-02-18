"""
Type annotations for simspaceweaver service client.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_simspaceweaver/client/)

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_simspaceweaver.client import SimSpaceWeaverClient

    session = get_session()
    async with session.create_client("simspaceweaver") as client:
        client: SimSpaceWeaverClient
    ```
"""

from typing import Any, Dict, Mapping, Sequence, Type

from aiobotocore.client import AioBaseClient
from botocore.client import ClientMeta

from .type_defs import (
    DescribeAppOutputTypeDef,
    DescribeSimulationOutputTypeDef,
    LaunchOverridesTypeDef,
    ListAppsOutputTypeDef,
    ListSimulationsOutputTypeDef,
    ListTagsForResourceOutputTypeDef,
    S3DestinationTypeDef,
    S3LocationTypeDef,
    StartAppOutputTypeDef,
    StartSimulationOutputTypeDef,
)

__all__ = ("SimSpaceWeaverClient",)

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
    TooManyTagsException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class SimSpaceWeaverClient(AioBaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/simspaceweaver.html#SimSpaceWeaver.Client)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_simspaceweaver/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        SimSpaceWeaverClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/simspaceweaver.html#SimSpaceWeaver.Client.exceptions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_simspaceweaver/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/simspaceweaver.html#SimSpaceWeaver.Client.can_paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_simspaceweaver/client/#can_paginate)
        """

    async def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/simspaceweaver.html#SimSpaceWeaver.Client.close)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_simspaceweaver/client/#close)
        """

    async def create_snapshot(
        self, *, Destination: S3DestinationTypeDef, Simulation: str
    ) -> Dict[str, Any]:
        """
        Creates a snapshot of the specified simulation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/simspaceweaver.html#SimSpaceWeaver.Client.create_snapshot)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_simspaceweaver/client/#create_snapshot)
        """

    async def delete_app(self, *, App: str, Domain: str, Simulation: str) -> Dict[str, Any]:
        """
        Deletes the instance of the given custom app.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/simspaceweaver.html#SimSpaceWeaver.Client.delete_app)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_simspaceweaver/client/#delete_app)
        """

    async def delete_simulation(self, *, Simulation: str) -> Dict[str, Any]:
        """
        Deletes all SimSpace Weaver resources assigned to the given simulation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/simspaceweaver.html#SimSpaceWeaver.Client.delete_simulation)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_simspaceweaver/client/#delete_simulation)
        """

    async def describe_app(
        self, *, App: str, Domain: str, Simulation: str
    ) -> DescribeAppOutputTypeDef:
        """
        Returns the state of the given custom app.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/simspaceweaver.html#SimSpaceWeaver.Client.describe_app)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_simspaceweaver/client/#describe_app)
        """

    async def describe_simulation(self, *, Simulation: str) -> DescribeSimulationOutputTypeDef:
        """
        Returns the current state of the given simulation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/simspaceweaver.html#SimSpaceWeaver.Client.describe_simulation)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_simspaceweaver/client/#describe_simulation)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/simspaceweaver.html#SimSpaceWeaver.Client.generate_presigned_url)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_simspaceweaver/client/#generate_presigned_url)
        """

    async def list_apps(
        self, *, Simulation: str, Domain: str = ..., MaxResults: int = ..., NextToken: str = ...
    ) -> ListAppsOutputTypeDef:
        """
        Lists all custom apps or service apps for the given simulation and domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/simspaceweaver.html#SimSpaceWeaver.Client.list_apps)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_simspaceweaver/client/#list_apps)
        """

    async def list_simulations(
        self, *, MaxResults: int = ..., NextToken: str = ...
    ) -> ListSimulationsOutputTypeDef:
        """
        Lists the SimSpace Weaver simulations in the Amazon Web Services account used
        to make the API
        call.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/simspaceweaver.html#SimSpaceWeaver.Client.list_simulations)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_simspaceweaver/client/#list_simulations)
        """

    async def list_tags_for_resource(self, *, ResourceArn: str) -> ListTagsForResourceOutputTypeDef:
        """
        Lists all tags on a SimSpace Weaver resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/simspaceweaver.html#SimSpaceWeaver.Client.list_tags_for_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_simspaceweaver/client/#list_tags_for_resource)
        """

    async def start_app(
        self,
        *,
        Domain: str,
        Name: str,
        Simulation: str,
        ClientToken: str = ...,
        Description: str = ...,
        LaunchOverrides: LaunchOverridesTypeDef = ...,
    ) -> StartAppOutputTypeDef:
        """
        Starts a custom app with the configuration specified in the simulation schema.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/simspaceweaver.html#SimSpaceWeaver.Client.start_app)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_simspaceweaver/client/#start_app)
        """

    async def start_clock(self, *, Simulation: str) -> Dict[str, Any]:
        """
        Starts the simulation clock.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/simspaceweaver.html#SimSpaceWeaver.Client.start_clock)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_simspaceweaver/client/#start_clock)
        """

    async def start_simulation(
        self,
        *,
        Name: str,
        RoleArn: str,
        ClientToken: str = ...,
        Description: str = ...,
        MaximumDuration: str = ...,
        SchemaS3Location: S3LocationTypeDef = ...,
        SnapshotS3Location: S3LocationTypeDef = ...,
        Tags: Mapping[str, str] = ...,
    ) -> StartSimulationOutputTypeDef:
        """
        Starts a simulation with the given name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/simspaceweaver.html#SimSpaceWeaver.Client.start_simulation)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_simspaceweaver/client/#start_simulation)
        """

    async def stop_app(self, *, App: str, Domain: str, Simulation: str) -> Dict[str, Any]:
        """
        Stops the given custom app and shuts down all of its allocated compute
        resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/simspaceweaver.html#SimSpaceWeaver.Client.stop_app)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_simspaceweaver/client/#stop_app)
        """

    async def stop_clock(self, *, Simulation: str) -> Dict[str, Any]:
        """
        Stops the simulation clock.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/simspaceweaver.html#SimSpaceWeaver.Client.stop_clock)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_simspaceweaver/client/#stop_clock)
        """

    async def stop_simulation(self, *, Simulation: str) -> Dict[str, Any]:
        """
        Stops the given simulation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/simspaceweaver.html#SimSpaceWeaver.Client.stop_simulation)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_simspaceweaver/client/#stop_simulation)
        """

    async def tag_resource(self, *, ResourceArn: str, Tags: Mapping[str, str]) -> Dict[str, Any]:
        """
        Adds tags to a SimSpace Weaver resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/simspaceweaver.html#SimSpaceWeaver.Client.tag_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_simspaceweaver/client/#tag_resource)
        """

    async def untag_resource(self, *, ResourceArn: str, TagKeys: Sequence[str]) -> Dict[str, Any]:
        """
        Removes tags from a SimSpace Weaver resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/simspaceweaver.html#SimSpaceWeaver.Client.untag_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_simspaceweaver/client/#untag_resource)
        """

    async def __aenter__(self) -> "SimSpaceWeaverClient":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/simspaceweaver.html#SimSpaceWeaver.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_simspaceweaver/client/)
        """

    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> Any:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/simspaceweaver.html#SimSpaceWeaver.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_simspaceweaver/client/)
        """
