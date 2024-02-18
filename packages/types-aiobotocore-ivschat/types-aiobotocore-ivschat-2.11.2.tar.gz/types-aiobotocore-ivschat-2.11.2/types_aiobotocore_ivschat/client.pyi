"""
Type annotations for ivschat service client.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ivschat/client/)

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_ivschat.client import ivschatClient

    session = get_session()
    async with session.create_client("ivschat") as client:
        client: ivschatClient
    ```
"""

from typing import Any, Dict, Mapping, Sequence, Type

from aiobotocore.client import AioBaseClient
from botocore.client import ClientMeta

from .literals import ChatTokenCapabilityType
from .type_defs import (
    CreateChatTokenResponseTypeDef,
    CreateLoggingConfigurationResponseTypeDef,
    CreateRoomResponseTypeDef,
    DeleteMessageResponseTypeDef,
    DestinationConfigurationTypeDef,
    EmptyResponseMetadataTypeDef,
    GetLoggingConfigurationResponseTypeDef,
    GetRoomResponseTypeDef,
    ListLoggingConfigurationsResponseTypeDef,
    ListRoomsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    MessageReviewHandlerTypeDef,
    SendEventResponseTypeDef,
    UpdateLoggingConfigurationResponseTypeDef,
    UpdateRoomResponseTypeDef,
)

__all__ = ("ivschatClient",)

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
    PendingVerification: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class ivschatClient(AioBaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivschat.html#ivschat.Client)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ivschat/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        ivschatClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivschat.html#ivschat.Client.exceptions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ivschat/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivschat.html#ivschat.Client.can_paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ivschat/client/#can_paginate)
        """

    async def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivschat.html#ivschat.Client.close)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ivschat/client/#close)
        """

    async def create_chat_token(
        self,
        *,
        roomIdentifier: str,
        userId: str,
        attributes: Mapping[str, str] = ...,
        capabilities: Sequence[ChatTokenCapabilityType] = ...,
        sessionDurationInMinutes: int = ...,
    ) -> CreateChatTokenResponseTypeDef:
        """
        Creates an encrypted token that is used by a chat participant to establish an
        individual WebSocket chat connection to a
        room.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivschat.html#ivschat.Client.create_chat_token)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ivschat/client/#create_chat_token)
        """

    async def create_logging_configuration(
        self,
        *,
        destinationConfiguration: DestinationConfigurationTypeDef,
        name: str = ...,
        tags: Mapping[str, str] = ...,
    ) -> CreateLoggingConfigurationResponseTypeDef:
        """
        Creates a logging configuration that allows clients to store and record sent
        messages.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivschat.html#ivschat.Client.create_logging_configuration)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ivschat/client/#create_logging_configuration)
        """

    async def create_room(
        self,
        *,
        loggingConfigurationIdentifiers: Sequence[str] = ...,
        maximumMessageLength: int = ...,
        maximumMessageRatePerSecond: int = ...,
        messageReviewHandler: MessageReviewHandlerTypeDef = ...,
        name: str = ...,
        tags: Mapping[str, str] = ...,
    ) -> CreateRoomResponseTypeDef:
        """
        Creates a room that allows clients to connect and pass messages.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivschat.html#ivschat.Client.create_room)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ivschat/client/#create_room)
        """

    async def delete_logging_configuration(
        self, *, identifier: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified logging configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivschat.html#ivschat.Client.delete_logging_configuration)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ivschat/client/#delete_logging_configuration)
        """

    async def delete_message(
        self, *, id: str, roomIdentifier: str, reason: str = ...
    ) -> DeleteMessageResponseTypeDef:
        """
        Sends an event to a specific room which directs clients to delete a specific
        message; that is, unrender it from view and delete it from the client’s chat
        history.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivschat.html#ivschat.Client.delete_message)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ivschat/client/#delete_message)
        """

    async def delete_room(self, *, identifier: str) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified room.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivschat.html#ivschat.Client.delete_room)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ivschat/client/#delete_room)
        """

    async def disconnect_user(
        self, *, roomIdentifier: str, userId: str, reason: str = ...
    ) -> Dict[str, Any]:
        """
        Disconnects all connections using a specified user ID from a room.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivschat.html#ivschat.Client.disconnect_user)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ivschat/client/#disconnect_user)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivschat.html#ivschat.Client.generate_presigned_url)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ivschat/client/#generate_presigned_url)
        """

    async def get_logging_configuration(
        self, *, identifier: str
    ) -> GetLoggingConfigurationResponseTypeDef:
        """
        Gets the specified logging configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivschat.html#ivschat.Client.get_logging_configuration)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ivschat/client/#get_logging_configuration)
        """

    async def get_room(self, *, identifier: str) -> GetRoomResponseTypeDef:
        """
        Gets the specified room.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivschat.html#ivschat.Client.get_room)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ivschat/client/#get_room)
        """

    async def list_logging_configurations(
        self, *, maxResults: int = ..., nextToken: str = ...
    ) -> ListLoggingConfigurationsResponseTypeDef:
        """
        Gets summary information about all your logging configurations in the AWS
        region where the API request is
        processed.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivschat.html#ivschat.Client.list_logging_configurations)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ivschat/client/#list_logging_configurations)
        """

    async def list_rooms(
        self,
        *,
        loggingConfigurationIdentifier: str = ...,
        maxResults: int = ...,
        messageReviewHandlerUri: str = ...,
        name: str = ...,
        nextToken: str = ...,
    ) -> ListRoomsResponseTypeDef:
        """
        Gets summary information about all your rooms in the AWS region where the API
        request is
        processed.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivschat.html#ivschat.Client.list_rooms)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ivschat/client/#list_rooms)
        """

    async def list_tags_for_resource(
        self, *, resourceArn: str
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Gets information about AWS tags for the specified ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivschat.html#ivschat.Client.list_tags_for_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ivschat/client/#list_tags_for_resource)
        """

    async def send_event(
        self, *, eventName: str, roomIdentifier: str, attributes: Mapping[str, str] = ...
    ) -> SendEventResponseTypeDef:
        """
        Sends an event to a room.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivschat.html#ivschat.Client.send_event)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ivschat/client/#send_event)
        """

    async def tag_resource(self, *, resourceArn: str, tags: Mapping[str, str]) -> Dict[str, Any]:
        """
        Adds or updates tags for the AWS resource with the specified ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivschat.html#ivschat.Client.tag_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ivschat/client/#tag_resource)
        """

    async def untag_resource(self, *, resourceArn: str, tagKeys: Sequence[str]) -> Dict[str, Any]:
        """
        Removes tags from the resource with the specified ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivschat.html#ivschat.Client.untag_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ivschat/client/#untag_resource)
        """

    async def update_logging_configuration(
        self,
        *,
        identifier: str,
        destinationConfiguration: DestinationConfigurationTypeDef = ...,
        name: str = ...,
    ) -> UpdateLoggingConfigurationResponseTypeDef:
        """
        Updates a specified logging configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivschat.html#ivschat.Client.update_logging_configuration)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ivschat/client/#update_logging_configuration)
        """

    async def update_room(
        self,
        *,
        identifier: str,
        loggingConfigurationIdentifiers: Sequence[str] = ...,
        maximumMessageLength: int = ...,
        maximumMessageRatePerSecond: int = ...,
        messageReviewHandler: MessageReviewHandlerTypeDef = ...,
        name: str = ...,
    ) -> UpdateRoomResponseTypeDef:
        """
        Updates a room’s configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivschat.html#ivschat.Client.update_room)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ivschat/client/#update_room)
        """

    async def __aenter__(self) -> "ivschatClient":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivschat.html#ivschat.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ivschat/client/)
        """

    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> Any:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivschat.html#ivschat.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ivschat/client/)
        """
