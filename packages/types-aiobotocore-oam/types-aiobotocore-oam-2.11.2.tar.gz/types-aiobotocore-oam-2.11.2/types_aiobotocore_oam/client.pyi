"""
Type annotations for oam service client.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_oam/client/)

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_oam.client import CloudWatchObservabilityAccessManagerClient

    session = get_session()
    async with session.create_client("oam") as client:
        client: CloudWatchObservabilityAccessManagerClient
    ```
"""

import sys
from typing import Any, Dict, Mapping, Sequence, Type, overload

from aiobotocore.client import AioBaseClient
from botocore.client import ClientMeta

from .literals import ResourceTypeType
from .paginator import ListAttachedLinksPaginator, ListLinksPaginator, ListSinksPaginator
from .type_defs import (
    CreateLinkOutputTypeDef,
    CreateSinkOutputTypeDef,
    GetLinkOutputTypeDef,
    GetSinkOutputTypeDef,
    GetSinkPolicyOutputTypeDef,
    ListAttachedLinksOutputTypeDef,
    ListLinksOutputTypeDef,
    ListSinksOutputTypeDef,
    ListTagsForResourceOutputTypeDef,
    PutSinkPolicyOutputTypeDef,
    UpdateLinkOutputTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("CloudWatchObservabilityAccessManagerClient",)

class BotocoreClientError(Exception):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServiceFault: Type[BotocoreClientError]
    InvalidParameterException: Type[BotocoreClientError]
    MissingRequiredParameterException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    TooManyTagsException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class CloudWatchObservabilityAccessManagerClient(AioBaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/oam.html#CloudWatchObservabilityAccessManager.Client)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_oam/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        CloudWatchObservabilityAccessManagerClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/oam.html#CloudWatchObservabilityAccessManager.Client.exceptions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_oam/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/oam.html#CloudWatchObservabilityAccessManager.Client.can_paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_oam/client/#can_paginate)
        """

    async def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/oam.html#CloudWatchObservabilityAccessManager.Client.close)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_oam/client/#close)
        """

    async def create_link(
        self,
        *,
        LabelTemplate: str,
        ResourceTypes: Sequence[ResourceTypeType],
        SinkIdentifier: str,
        Tags: Mapping[str, str] = ...,
    ) -> CreateLinkOutputTypeDef:
        """
        Creates a link between a source account and a sink that you have created in a
        monitoring
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/oam.html#CloudWatchObservabilityAccessManager.Client.create_link)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_oam/client/#create_link)
        """

    async def create_sink(
        self, *, Name: str, Tags: Mapping[str, str] = ...
    ) -> CreateSinkOutputTypeDef:
        """
        Use this to create a *sink* in the current account, so that it can be used as a
        monitoring account in CloudWatch cross-account
        observability.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/oam.html#CloudWatchObservabilityAccessManager.Client.create_sink)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_oam/client/#create_sink)
        """

    async def delete_link(self, *, Identifier: str) -> Dict[str, Any]:
        """
        Deletes a link between a monitoring account sink and a source account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/oam.html#CloudWatchObservabilityAccessManager.Client.delete_link)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_oam/client/#delete_link)
        """

    async def delete_sink(self, *, Identifier: str) -> Dict[str, Any]:
        """
        Deletes a sink.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/oam.html#CloudWatchObservabilityAccessManager.Client.delete_sink)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_oam/client/#delete_sink)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/oam.html#CloudWatchObservabilityAccessManager.Client.generate_presigned_url)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_oam/client/#generate_presigned_url)
        """

    async def get_link(self, *, Identifier: str) -> GetLinkOutputTypeDef:
        """
        Returns complete information about one link.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/oam.html#CloudWatchObservabilityAccessManager.Client.get_link)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_oam/client/#get_link)
        """

    async def get_sink(self, *, Identifier: str) -> GetSinkOutputTypeDef:
        """
        Returns complete information about one monitoring account sink.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/oam.html#CloudWatchObservabilityAccessManager.Client.get_sink)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_oam/client/#get_sink)
        """

    async def get_sink_policy(self, *, SinkIdentifier: str) -> GetSinkPolicyOutputTypeDef:
        """
        Returns the current sink policy attached to this sink.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/oam.html#CloudWatchObservabilityAccessManager.Client.get_sink_policy)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_oam/client/#get_sink_policy)
        """

    async def list_attached_links(
        self, *, SinkIdentifier: str, MaxResults: int = ..., NextToken: str = ...
    ) -> ListAttachedLinksOutputTypeDef:
        """
        Returns a list of source account links that are linked to this monitoring
        account
        sink.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/oam.html#CloudWatchObservabilityAccessManager.Client.list_attached_links)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_oam/client/#list_attached_links)
        """

    async def list_links(
        self, *, MaxResults: int = ..., NextToken: str = ...
    ) -> ListLinksOutputTypeDef:
        """
        Use this operation in a source account to return a list of links to monitoring
        account sinks that this source account
        has.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/oam.html#CloudWatchObservabilityAccessManager.Client.list_links)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_oam/client/#list_links)
        """

    async def list_sinks(
        self, *, MaxResults: int = ..., NextToken: str = ...
    ) -> ListSinksOutputTypeDef:
        """
        Use this operation in a monitoring account to return the list of sinks created
        in that
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/oam.html#CloudWatchObservabilityAccessManager.Client.list_sinks)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_oam/client/#list_sinks)
        """

    async def list_tags_for_resource(self, *, ResourceArn: str) -> ListTagsForResourceOutputTypeDef:
        """
        Displays the tags associated with a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/oam.html#CloudWatchObservabilityAccessManager.Client.list_tags_for_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_oam/client/#list_tags_for_resource)
        """

    async def put_sink_policy(
        self, *, SinkIdentifier: str, Policy: str
    ) -> PutSinkPolicyOutputTypeDef:
        """
        Creates or updates the resource policy that grants permissions to source
        accounts to link to the monitoring account
        sink.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/oam.html#CloudWatchObservabilityAccessManager.Client.put_sink_policy)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_oam/client/#put_sink_policy)
        """

    async def tag_resource(self, *, ResourceArn: str, Tags: Mapping[str, str]) -> Dict[str, Any]:
        """
        Assigns one or more tags (key-value pairs) to the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/oam.html#CloudWatchObservabilityAccessManager.Client.tag_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_oam/client/#tag_resource)
        """

    async def untag_resource(self, *, ResourceArn: str, TagKeys: Sequence[str]) -> Dict[str, Any]:
        """
        Removes one or more tags from the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/oam.html#CloudWatchObservabilityAccessManager.Client.untag_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_oam/client/#untag_resource)
        """

    async def update_link(
        self, *, Identifier: str, ResourceTypes: Sequence[ResourceTypeType]
    ) -> UpdateLinkOutputTypeDef:
        """
        Use this operation to change what types of data are shared from a source
        account to its linked monitoring account
        sink.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/oam.html#CloudWatchObservabilityAccessManager.Client.update_link)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_oam/client/#update_link)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_attached_links"]
    ) -> ListAttachedLinksPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/oam.html#CloudWatchObservabilityAccessManager.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_oam/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_links"]) -> ListLinksPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/oam.html#CloudWatchObservabilityAccessManager.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_oam/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_sinks"]) -> ListSinksPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/oam.html#CloudWatchObservabilityAccessManager.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_oam/client/#get_paginator)
        """

    async def __aenter__(self) -> "CloudWatchObservabilityAccessManagerClient":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/oam.html#CloudWatchObservabilityAccessManager.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_oam/client/)
        """

    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> Any:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/oam.html#CloudWatchObservabilityAccessManager.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_oam/client/)
        """
