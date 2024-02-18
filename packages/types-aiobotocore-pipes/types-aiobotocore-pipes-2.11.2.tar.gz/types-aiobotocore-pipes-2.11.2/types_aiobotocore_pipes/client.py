"""
Type annotations for pipes service client.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pipes/client/)

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_pipes.client import EventBridgePipesClient

    session = get_session()
    async with session.create_client("pipes") as client:
        client: EventBridgePipesClient
    ```
"""

import sys
from typing import Any, Dict, Mapping, Sequence, Type

from aiobotocore.client import AioBaseClient
from botocore.client import ClientMeta

from .literals import PipeStateType, RequestedPipeStateType
from .paginator import ListPipesPaginator
from .type_defs import (
    CreatePipeResponseTypeDef,
    DeletePipeResponseTypeDef,
    DescribePipeResponseTypeDef,
    ListPipesResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    PipeEnrichmentParametersTypeDef,
    PipeLogConfigurationParametersTypeDef,
    PipeSourceParametersTypeDef,
    PipeTargetParametersTypeDef,
    StartPipeResponseTypeDef,
    StopPipeResponseTypeDef,
    UpdatePipeResponseTypeDef,
    UpdatePipeSourceParametersTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("EventBridgePipesClient",)


class BotocoreClientError(Exception):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalException: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class EventBridgePipesClient(AioBaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pipes.html#EventBridgePipes.Client)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pipes/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        EventBridgePipesClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pipes.html#EventBridgePipes.Client.exceptions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pipes/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pipes.html#EventBridgePipes.Client.can_paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pipes/client/#can_paginate)
        """

    async def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pipes.html#EventBridgePipes.Client.close)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pipes/client/#close)
        """

    async def create_pipe(
        self,
        *,
        Name: str,
        RoleArn: str,
        Source: str,
        Target: str,
        Description: str = ...,
        DesiredState: RequestedPipeStateType = ...,
        Enrichment: str = ...,
        EnrichmentParameters: PipeEnrichmentParametersTypeDef = ...,
        LogConfiguration: PipeLogConfigurationParametersTypeDef = ...,
        SourceParameters: PipeSourceParametersTypeDef = ...,
        Tags: Mapping[str, str] = ...,
        TargetParameters: PipeTargetParametersTypeDef = ...,
    ) -> CreatePipeResponseTypeDef:
        """
        Create a pipe.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pipes.html#EventBridgePipes.Client.create_pipe)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pipes/client/#create_pipe)
        """

    async def delete_pipe(self, *, Name: str) -> DeletePipeResponseTypeDef:
        """
        Delete an existing pipe.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pipes.html#EventBridgePipes.Client.delete_pipe)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pipes/client/#delete_pipe)
        """

    async def describe_pipe(self, *, Name: str) -> DescribePipeResponseTypeDef:
        """
        Get the information about an existing pipe.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pipes.html#EventBridgePipes.Client.describe_pipe)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pipes/client/#describe_pipe)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pipes.html#EventBridgePipes.Client.generate_presigned_url)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pipes/client/#generate_presigned_url)
        """

    async def list_pipes(
        self,
        *,
        CurrentState: PipeStateType = ...,
        DesiredState: RequestedPipeStateType = ...,
        Limit: int = ...,
        NamePrefix: str = ...,
        NextToken: str = ...,
        SourcePrefix: str = ...,
        TargetPrefix: str = ...,
    ) -> ListPipesResponseTypeDef:
        """
        Get the pipes associated with this account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pipes.html#EventBridgePipes.Client.list_pipes)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pipes/client/#list_pipes)
        """

    async def list_tags_for_resource(
        self, *, resourceArn: str
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Displays the tags associated with a pipe.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pipes.html#EventBridgePipes.Client.list_tags_for_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pipes/client/#list_tags_for_resource)
        """

    async def start_pipe(self, *, Name: str) -> StartPipeResponseTypeDef:
        """
        Start an existing pipe.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pipes.html#EventBridgePipes.Client.start_pipe)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pipes/client/#start_pipe)
        """

    async def stop_pipe(self, *, Name: str) -> StopPipeResponseTypeDef:
        """
        Stop an existing pipe.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pipes.html#EventBridgePipes.Client.stop_pipe)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pipes/client/#stop_pipe)
        """

    async def tag_resource(self, *, resourceArn: str, tags: Mapping[str, str]) -> Dict[str, Any]:
        """
        Assigns one or more tags (key-value pairs) to the specified pipe.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pipes.html#EventBridgePipes.Client.tag_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pipes/client/#tag_resource)
        """

    async def untag_resource(self, *, resourceArn: str, tagKeys: Sequence[str]) -> Dict[str, Any]:
        """
        Removes one or more tags from the specified pipes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pipes.html#EventBridgePipes.Client.untag_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pipes/client/#untag_resource)
        """

    async def update_pipe(
        self,
        *,
        Name: str,
        RoleArn: str,
        Description: str = ...,
        DesiredState: RequestedPipeStateType = ...,
        Enrichment: str = ...,
        EnrichmentParameters: PipeEnrichmentParametersTypeDef = ...,
        LogConfiguration: PipeLogConfigurationParametersTypeDef = ...,
        SourceParameters: UpdatePipeSourceParametersTypeDef = ...,
        Target: str = ...,
        TargetParameters: PipeTargetParametersTypeDef = ...,
    ) -> UpdatePipeResponseTypeDef:
        """
        Update an existing pipe.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pipes.html#EventBridgePipes.Client.update_pipe)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pipes/client/#update_pipe)
        """

    def get_paginator(self, operation_name: Literal["list_pipes"]) -> ListPipesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pipes.html#EventBridgePipes.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pipes/client/#get_paginator)
        """

    async def __aenter__(self) -> "EventBridgePipesClient":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pipes.html#EventBridgePipes.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pipes/client/)
        """

    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> Any:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pipes.html#EventBridgePipes.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pipes/client/)
        """
