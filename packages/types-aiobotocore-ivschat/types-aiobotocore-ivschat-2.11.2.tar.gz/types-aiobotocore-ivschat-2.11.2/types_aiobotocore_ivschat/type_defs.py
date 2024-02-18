"""
Type annotations for ivschat service type definitions.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ivschat/type_defs/)

Usage::

    ```python
    from types_aiobotocore_ivschat.type_defs import CloudWatchLogsDestinationConfigurationTypeDef

    data: CloudWatchLogsDestinationConfigurationTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from .literals import ChatTokenCapabilityType, FallbackResultType, LoggingConfigurationStateType

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 12):
    from typing import NotRequired
else:
    from typing_extensions import NotRequired
if sys.version_info >= (3, 12):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "CloudWatchLogsDestinationConfigurationTypeDef",
    "CreateChatTokenRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "MessageReviewHandlerTypeDef",
    "DeleteLoggingConfigurationRequestRequestTypeDef",
    "DeleteMessageRequestRequestTypeDef",
    "DeleteRoomRequestRequestTypeDef",
    "FirehoseDestinationConfigurationTypeDef",
    "S3DestinationConfigurationTypeDef",
    "DisconnectUserRequestRequestTypeDef",
    "GetLoggingConfigurationRequestRequestTypeDef",
    "GetRoomRequestRequestTypeDef",
    "ListLoggingConfigurationsRequestRequestTypeDef",
    "ListRoomsRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "SendEventRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "CreateChatTokenResponseTypeDef",
    "DeleteMessageResponseTypeDef",
    "EmptyResponseMetadataTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "SendEventResponseTypeDef",
    "CreateRoomRequestRequestTypeDef",
    "CreateRoomResponseTypeDef",
    "GetRoomResponseTypeDef",
    "RoomSummaryTypeDef",
    "UpdateRoomRequestRequestTypeDef",
    "UpdateRoomResponseTypeDef",
    "DestinationConfigurationTypeDef",
    "ListRoomsResponseTypeDef",
    "CreateLoggingConfigurationRequestRequestTypeDef",
    "CreateLoggingConfigurationResponseTypeDef",
    "GetLoggingConfigurationResponseTypeDef",
    "LoggingConfigurationSummaryTypeDef",
    "UpdateLoggingConfigurationRequestRequestTypeDef",
    "UpdateLoggingConfigurationResponseTypeDef",
    "ListLoggingConfigurationsResponseTypeDef",
)

CloudWatchLogsDestinationConfigurationTypeDef = TypedDict(
    "CloudWatchLogsDestinationConfigurationTypeDef",
    {
        "logGroupName": str,
    },
)
CreateChatTokenRequestRequestTypeDef = TypedDict(
    "CreateChatTokenRequestRequestTypeDef",
    {
        "roomIdentifier": str,
        "userId": str,
        "attributes": NotRequired[Mapping[str, str]],
        "capabilities": NotRequired[Sequence[ChatTokenCapabilityType]],
        "sessionDurationInMinutes": NotRequired[int],
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
MessageReviewHandlerTypeDef = TypedDict(
    "MessageReviewHandlerTypeDef",
    {
        "fallbackResult": NotRequired[FallbackResultType],
        "uri": NotRequired[str],
    },
)
DeleteLoggingConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteLoggingConfigurationRequestRequestTypeDef",
    {
        "identifier": str,
    },
)
DeleteMessageRequestRequestTypeDef = TypedDict(
    "DeleteMessageRequestRequestTypeDef",
    {
        "id": str,
        "roomIdentifier": str,
        "reason": NotRequired[str],
    },
)
DeleteRoomRequestRequestTypeDef = TypedDict(
    "DeleteRoomRequestRequestTypeDef",
    {
        "identifier": str,
    },
)
FirehoseDestinationConfigurationTypeDef = TypedDict(
    "FirehoseDestinationConfigurationTypeDef",
    {
        "deliveryStreamName": str,
    },
)
S3DestinationConfigurationTypeDef = TypedDict(
    "S3DestinationConfigurationTypeDef",
    {
        "bucketName": str,
    },
)
DisconnectUserRequestRequestTypeDef = TypedDict(
    "DisconnectUserRequestRequestTypeDef",
    {
        "roomIdentifier": str,
        "userId": str,
        "reason": NotRequired[str],
    },
)
GetLoggingConfigurationRequestRequestTypeDef = TypedDict(
    "GetLoggingConfigurationRequestRequestTypeDef",
    {
        "identifier": str,
    },
)
GetRoomRequestRequestTypeDef = TypedDict(
    "GetRoomRequestRequestTypeDef",
    {
        "identifier": str,
    },
)
ListLoggingConfigurationsRequestRequestTypeDef = TypedDict(
    "ListLoggingConfigurationsRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListRoomsRequestRequestTypeDef = TypedDict(
    "ListRoomsRequestRequestTypeDef",
    {
        "loggingConfigurationIdentifier": NotRequired[str],
        "maxResults": NotRequired[int],
        "messageReviewHandlerUri": NotRequired[str],
        "name": NotRequired[str],
        "nextToken": NotRequired[str],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)
SendEventRequestRequestTypeDef = TypedDict(
    "SendEventRequestRequestTypeDef",
    {
        "eventName": str,
        "roomIdentifier": str,
        "attributes": NotRequired[Mapping[str, str]],
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
CreateChatTokenResponseTypeDef = TypedDict(
    "CreateChatTokenResponseTypeDef",
    {
        "sessionExpirationTime": datetime,
        "token": str,
        "tokenExpirationTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteMessageResponseTypeDef = TypedDict(
    "DeleteMessageResponseTypeDef",
    {
        "id": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
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
SendEventResponseTypeDef = TypedDict(
    "SendEventResponseTypeDef",
    {
        "id": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateRoomRequestRequestTypeDef = TypedDict(
    "CreateRoomRequestRequestTypeDef",
    {
        "loggingConfigurationIdentifiers": NotRequired[Sequence[str]],
        "maximumMessageLength": NotRequired[int],
        "maximumMessageRatePerSecond": NotRequired[int],
        "messageReviewHandler": NotRequired[MessageReviewHandlerTypeDef],
        "name": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)
CreateRoomResponseTypeDef = TypedDict(
    "CreateRoomResponseTypeDef",
    {
        "arn": str,
        "createTime": datetime,
        "id": str,
        "loggingConfigurationIdentifiers": List[str],
        "maximumMessageLength": int,
        "maximumMessageRatePerSecond": int,
        "messageReviewHandler": MessageReviewHandlerTypeDef,
        "name": str,
        "tags": Dict[str, str],
        "updateTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetRoomResponseTypeDef = TypedDict(
    "GetRoomResponseTypeDef",
    {
        "arn": str,
        "createTime": datetime,
        "id": str,
        "loggingConfigurationIdentifiers": List[str],
        "maximumMessageLength": int,
        "maximumMessageRatePerSecond": int,
        "messageReviewHandler": MessageReviewHandlerTypeDef,
        "name": str,
        "tags": Dict[str, str],
        "updateTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RoomSummaryTypeDef = TypedDict(
    "RoomSummaryTypeDef",
    {
        "arn": NotRequired[str],
        "createTime": NotRequired[datetime],
        "id": NotRequired[str],
        "loggingConfigurationIdentifiers": NotRequired[List[str]],
        "messageReviewHandler": NotRequired[MessageReviewHandlerTypeDef],
        "name": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
        "updateTime": NotRequired[datetime],
    },
)
UpdateRoomRequestRequestTypeDef = TypedDict(
    "UpdateRoomRequestRequestTypeDef",
    {
        "identifier": str,
        "loggingConfigurationIdentifiers": NotRequired[Sequence[str]],
        "maximumMessageLength": NotRequired[int],
        "maximumMessageRatePerSecond": NotRequired[int],
        "messageReviewHandler": NotRequired[MessageReviewHandlerTypeDef],
        "name": NotRequired[str],
    },
)
UpdateRoomResponseTypeDef = TypedDict(
    "UpdateRoomResponseTypeDef",
    {
        "arn": str,
        "createTime": datetime,
        "id": str,
        "loggingConfigurationIdentifiers": List[str],
        "maximumMessageLength": int,
        "maximumMessageRatePerSecond": int,
        "messageReviewHandler": MessageReviewHandlerTypeDef,
        "name": str,
        "tags": Dict[str, str],
        "updateTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DestinationConfigurationTypeDef = TypedDict(
    "DestinationConfigurationTypeDef",
    {
        "cloudWatchLogs": NotRequired[CloudWatchLogsDestinationConfigurationTypeDef],
        "firehose": NotRequired[FirehoseDestinationConfigurationTypeDef],
        "s3": NotRequired[S3DestinationConfigurationTypeDef],
    },
)
ListRoomsResponseTypeDef = TypedDict(
    "ListRoomsResponseTypeDef",
    {
        "nextToken": str,
        "rooms": List[RoomSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateLoggingConfigurationRequestRequestTypeDef = TypedDict(
    "CreateLoggingConfigurationRequestRequestTypeDef",
    {
        "destinationConfiguration": DestinationConfigurationTypeDef,
        "name": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)
CreateLoggingConfigurationResponseTypeDef = TypedDict(
    "CreateLoggingConfigurationResponseTypeDef",
    {
        "arn": str,
        "createTime": datetime,
        "destinationConfiguration": DestinationConfigurationTypeDef,
        "id": str,
        "name": str,
        "state": Literal["ACTIVE"],
        "tags": Dict[str, str],
        "updateTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetLoggingConfigurationResponseTypeDef = TypedDict(
    "GetLoggingConfigurationResponseTypeDef",
    {
        "arn": str,
        "createTime": datetime,
        "destinationConfiguration": DestinationConfigurationTypeDef,
        "id": str,
        "name": str,
        "state": LoggingConfigurationStateType,
        "tags": Dict[str, str],
        "updateTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
LoggingConfigurationSummaryTypeDef = TypedDict(
    "LoggingConfigurationSummaryTypeDef",
    {
        "arn": NotRequired[str],
        "createTime": NotRequired[datetime],
        "destinationConfiguration": NotRequired[DestinationConfigurationTypeDef],
        "id": NotRequired[str],
        "name": NotRequired[str],
        "state": NotRequired[LoggingConfigurationStateType],
        "tags": NotRequired[Dict[str, str]],
        "updateTime": NotRequired[datetime],
    },
)
UpdateLoggingConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateLoggingConfigurationRequestRequestTypeDef",
    {
        "identifier": str,
        "destinationConfiguration": NotRequired[DestinationConfigurationTypeDef],
        "name": NotRequired[str],
    },
)
UpdateLoggingConfigurationResponseTypeDef = TypedDict(
    "UpdateLoggingConfigurationResponseTypeDef",
    {
        "arn": str,
        "createTime": datetime,
        "destinationConfiguration": DestinationConfigurationTypeDef,
        "id": str,
        "name": str,
        "state": Literal["ACTIVE"],
        "tags": Dict[str, str],
        "updateTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListLoggingConfigurationsResponseTypeDef = TypedDict(
    "ListLoggingConfigurationsResponseTypeDef",
    {
        "loggingConfigurations": List[LoggingConfigurationSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
