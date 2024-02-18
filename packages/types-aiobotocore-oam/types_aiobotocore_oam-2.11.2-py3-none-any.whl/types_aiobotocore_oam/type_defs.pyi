"""
Type annotations for oam service type definitions.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_oam/type_defs/)

Usage::

    ```python
    from types_aiobotocore_oam.type_defs import CreateLinkInputRequestTypeDef

    data: CreateLinkInputRequestTypeDef = ...
    ```
"""

import sys
from typing import Dict, List, Mapping, Sequence

from .literals import ResourceTypeType

if sys.version_info >= (3, 12):
    from typing import NotRequired
else:
    from typing_extensions import NotRequired
if sys.version_info >= (3, 12):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "CreateLinkInputRequestTypeDef",
    "ResponseMetadataTypeDef",
    "CreateSinkInputRequestTypeDef",
    "DeleteLinkInputRequestTypeDef",
    "DeleteSinkInputRequestTypeDef",
    "GetLinkInputRequestTypeDef",
    "GetSinkInputRequestTypeDef",
    "GetSinkPolicyInputRequestTypeDef",
    "PaginatorConfigTypeDef",
    "ListAttachedLinksInputRequestTypeDef",
    "ListAttachedLinksItemTypeDef",
    "ListLinksInputRequestTypeDef",
    "ListLinksItemTypeDef",
    "ListSinksInputRequestTypeDef",
    "ListSinksItemTypeDef",
    "ListTagsForResourceInputRequestTypeDef",
    "PutSinkPolicyInputRequestTypeDef",
    "TagResourceInputRequestTypeDef",
    "UntagResourceInputRequestTypeDef",
    "UpdateLinkInputRequestTypeDef",
    "CreateLinkOutputTypeDef",
    "CreateSinkOutputTypeDef",
    "GetLinkOutputTypeDef",
    "GetSinkOutputTypeDef",
    "GetSinkPolicyOutputTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "PutSinkPolicyOutputTypeDef",
    "UpdateLinkOutputTypeDef",
    "ListAttachedLinksInputListAttachedLinksPaginateTypeDef",
    "ListLinksInputListLinksPaginateTypeDef",
    "ListSinksInputListSinksPaginateTypeDef",
    "ListAttachedLinksOutputTypeDef",
    "ListLinksOutputTypeDef",
    "ListSinksOutputTypeDef",
)

CreateLinkInputRequestTypeDef = TypedDict(
    "CreateLinkInputRequestTypeDef",
    {
        "LabelTemplate": str,
        "ResourceTypes": Sequence[ResourceTypeType],
        "SinkIdentifier": str,
        "Tags": NotRequired[Mapping[str, str]],
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
CreateSinkInputRequestTypeDef = TypedDict(
    "CreateSinkInputRequestTypeDef",
    {
        "Name": str,
        "Tags": NotRequired[Mapping[str, str]],
    },
)
DeleteLinkInputRequestTypeDef = TypedDict(
    "DeleteLinkInputRequestTypeDef",
    {
        "Identifier": str,
    },
)
DeleteSinkInputRequestTypeDef = TypedDict(
    "DeleteSinkInputRequestTypeDef",
    {
        "Identifier": str,
    },
)
GetLinkInputRequestTypeDef = TypedDict(
    "GetLinkInputRequestTypeDef",
    {
        "Identifier": str,
    },
)
GetSinkInputRequestTypeDef = TypedDict(
    "GetSinkInputRequestTypeDef",
    {
        "Identifier": str,
    },
)
GetSinkPolicyInputRequestTypeDef = TypedDict(
    "GetSinkPolicyInputRequestTypeDef",
    {
        "SinkIdentifier": str,
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
ListAttachedLinksInputRequestTypeDef = TypedDict(
    "ListAttachedLinksInputRequestTypeDef",
    {
        "SinkIdentifier": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListAttachedLinksItemTypeDef = TypedDict(
    "ListAttachedLinksItemTypeDef",
    {
        "Label": NotRequired[str],
        "LinkArn": NotRequired[str],
        "ResourceTypes": NotRequired[List[str]],
    },
)
ListLinksInputRequestTypeDef = TypedDict(
    "ListLinksInputRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListLinksItemTypeDef = TypedDict(
    "ListLinksItemTypeDef",
    {
        "Arn": NotRequired[str],
        "Id": NotRequired[str],
        "Label": NotRequired[str],
        "ResourceTypes": NotRequired[List[str]],
        "SinkArn": NotRequired[str],
    },
)
ListSinksInputRequestTypeDef = TypedDict(
    "ListSinksInputRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListSinksItemTypeDef = TypedDict(
    "ListSinksItemTypeDef",
    {
        "Arn": NotRequired[str],
        "Id": NotRequired[str],
        "Name": NotRequired[str],
    },
)
ListTagsForResourceInputRequestTypeDef = TypedDict(
    "ListTagsForResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
PutSinkPolicyInputRequestTypeDef = TypedDict(
    "PutSinkPolicyInputRequestTypeDef",
    {
        "SinkIdentifier": str,
        "Policy": str,
    },
)
TagResourceInputRequestTypeDef = TypedDict(
    "TagResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Mapping[str, str],
    },
)
UntagResourceInputRequestTypeDef = TypedDict(
    "UntagResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)
UpdateLinkInputRequestTypeDef = TypedDict(
    "UpdateLinkInputRequestTypeDef",
    {
        "Identifier": str,
        "ResourceTypes": Sequence[ResourceTypeType],
    },
)
CreateLinkOutputTypeDef = TypedDict(
    "CreateLinkOutputTypeDef",
    {
        "Arn": str,
        "Id": str,
        "Label": str,
        "LabelTemplate": str,
        "ResourceTypes": List[str],
        "SinkArn": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateSinkOutputTypeDef = TypedDict(
    "CreateSinkOutputTypeDef",
    {
        "Arn": str,
        "Id": str,
        "Name": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetLinkOutputTypeDef = TypedDict(
    "GetLinkOutputTypeDef",
    {
        "Arn": str,
        "Id": str,
        "Label": str,
        "LabelTemplate": str,
        "ResourceTypes": List[str],
        "SinkArn": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSinkOutputTypeDef = TypedDict(
    "GetSinkOutputTypeDef",
    {
        "Arn": str,
        "Id": str,
        "Name": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSinkPolicyOutputTypeDef = TypedDict(
    "GetSinkPolicyOutputTypeDef",
    {
        "SinkArn": str,
        "SinkId": str,
        "Policy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutSinkPolicyOutputTypeDef = TypedDict(
    "PutSinkPolicyOutputTypeDef",
    {
        "SinkArn": str,
        "SinkId": str,
        "Policy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateLinkOutputTypeDef = TypedDict(
    "UpdateLinkOutputTypeDef",
    {
        "Arn": str,
        "Id": str,
        "Label": str,
        "LabelTemplate": str,
        "ResourceTypes": List[str],
        "SinkArn": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAttachedLinksInputListAttachedLinksPaginateTypeDef = TypedDict(
    "ListAttachedLinksInputListAttachedLinksPaginateTypeDef",
    {
        "SinkIdentifier": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListLinksInputListLinksPaginateTypeDef = TypedDict(
    "ListLinksInputListLinksPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListSinksInputListSinksPaginateTypeDef = TypedDict(
    "ListSinksInputListSinksPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListAttachedLinksOutputTypeDef = TypedDict(
    "ListAttachedLinksOutputTypeDef",
    {
        "Items": List[ListAttachedLinksItemTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListLinksOutputTypeDef = TypedDict(
    "ListLinksOutputTypeDef",
    {
        "Items": List[ListLinksItemTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListSinksOutputTypeDef = TypedDict(
    "ListSinksOutputTypeDef",
    {
        "Items": List[ListSinksItemTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
