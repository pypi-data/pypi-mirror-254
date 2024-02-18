"""
Type annotations for kinesisvideo service client.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kinesisvideo/client/)

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_kinesisvideo.client import KinesisVideoClient

    session = get_session()
    async with session.create_client("kinesisvideo") as client:
        client: KinesisVideoClient
    ```
"""

import sys
from typing import Any, Dict, Mapping, Sequence, Type, overload

from aiobotocore.client import AioBaseClient
from botocore.client import ClientMeta

from .literals import APINameType, ChannelTypeType, UpdateDataRetentionOperationType
from .paginator import (
    DescribeMappedResourceConfigurationPaginator,
    ListEdgeAgentConfigurationsPaginator,
    ListSignalingChannelsPaginator,
    ListStreamsPaginator,
)
from .type_defs import (
    ChannelNameConditionTypeDef,
    CreateSignalingChannelOutputTypeDef,
    CreateStreamOutputTypeDef,
    DescribeEdgeConfigurationOutputTypeDef,
    DescribeImageGenerationConfigurationOutputTypeDef,
    DescribeMappedResourceConfigurationOutputTypeDef,
    DescribeMediaStorageConfigurationOutputTypeDef,
    DescribeNotificationConfigurationOutputTypeDef,
    DescribeSignalingChannelOutputTypeDef,
    DescribeStreamOutputTypeDef,
    EdgeConfigTypeDef,
    GetDataEndpointOutputTypeDef,
    GetSignalingChannelEndpointOutputTypeDef,
    ImageGenerationConfigurationTypeDef,
    ListEdgeAgentConfigurationsOutputTypeDef,
    ListSignalingChannelsOutputTypeDef,
    ListStreamsOutputTypeDef,
    ListTagsForResourceOutputTypeDef,
    ListTagsForStreamOutputTypeDef,
    MediaStorageConfigurationTypeDef,
    NotificationConfigurationTypeDef,
    SingleMasterChannelEndpointConfigurationTypeDef,
    SingleMasterConfigurationTypeDef,
    StartEdgeConfigurationUpdateOutputTypeDef,
    StreamNameConditionTypeDef,
    TagTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("KinesisVideoClient",)


class BotocoreClientError(Exception):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    AccountChannelLimitExceededException: Type[BotocoreClientError]
    AccountStreamLimitExceededException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ClientLimitExceededException: Type[BotocoreClientError]
    DeviceStreamLimitExceededException: Type[BotocoreClientError]
    InvalidArgumentException: Type[BotocoreClientError]
    InvalidDeviceException: Type[BotocoreClientError]
    InvalidResourceFormatException: Type[BotocoreClientError]
    NoDataRetentionException: Type[BotocoreClientError]
    NotAuthorizedException: Type[BotocoreClientError]
    ResourceInUseException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    StreamEdgeConfigurationNotFoundException: Type[BotocoreClientError]
    TagsPerResourceExceededLimitException: Type[BotocoreClientError]
    VersionMismatchException: Type[BotocoreClientError]


class KinesisVideoClient(AioBaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo.html#KinesisVideo.Client)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kinesisvideo/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        KinesisVideoClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo.html#KinesisVideo.Client.exceptions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kinesisvideo/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo.html#KinesisVideo.Client.can_paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kinesisvideo/client/#can_paginate)
        """

    async def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo.html#KinesisVideo.Client.close)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kinesisvideo/client/#close)
        """

    async def create_signaling_channel(
        self,
        *,
        ChannelName: str,
        ChannelType: ChannelTypeType = ...,
        SingleMasterConfiguration: SingleMasterConfigurationTypeDef = ...,
        Tags: Sequence[TagTypeDef] = ...,
    ) -> CreateSignalingChannelOutputTypeDef:
        """
        Creates a signaling channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo.html#KinesisVideo.Client.create_signaling_channel)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kinesisvideo/client/#create_signaling_channel)
        """

    async def create_stream(
        self,
        *,
        StreamName: str,
        DeviceName: str = ...,
        MediaType: str = ...,
        KmsKeyId: str = ...,
        DataRetentionInHours: int = ...,
        Tags: Mapping[str, str] = ...,
    ) -> CreateStreamOutputTypeDef:
        """
        Creates a new Kinesis video stream.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo.html#KinesisVideo.Client.create_stream)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kinesisvideo/client/#create_stream)
        """

    async def delete_edge_configuration(
        self, *, StreamName: str = ..., StreamARN: str = ...
    ) -> Dict[str, Any]:
        """
        An asynchronous API that deletes a stream’s existing edge configuration, as
        well as the corresponding media from the Edge
        Agent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo.html#KinesisVideo.Client.delete_edge_configuration)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kinesisvideo/client/#delete_edge_configuration)
        """

    async def delete_signaling_channel(
        self, *, ChannelARN: str, CurrentVersion: str = ...
    ) -> Dict[str, Any]:
        """
        Deletes a specified signaling channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo.html#KinesisVideo.Client.delete_signaling_channel)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kinesisvideo/client/#delete_signaling_channel)
        """

    async def delete_stream(self, *, StreamARN: str, CurrentVersion: str = ...) -> Dict[str, Any]:
        """
        Deletes a Kinesis video stream and the data contained in the stream.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo.html#KinesisVideo.Client.delete_stream)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kinesisvideo/client/#delete_stream)
        """

    async def describe_edge_configuration(
        self, *, StreamName: str = ..., StreamARN: str = ...
    ) -> DescribeEdgeConfigurationOutputTypeDef:
        """
        Describes a stream’s edge configuration that was set using the
        `StartEdgeConfigurationUpdate` API and the latest status of the edge agent's
        recorder and uploader
        jobs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo.html#KinesisVideo.Client.describe_edge_configuration)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kinesisvideo/client/#describe_edge_configuration)
        """

    async def describe_image_generation_configuration(
        self, *, StreamName: str = ..., StreamARN: str = ...
    ) -> DescribeImageGenerationConfigurationOutputTypeDef:
        """
        Gets the `ImageGenerationConfiguration` for a given Kinesis video stream.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo.html#KinesisVideo.Client.describe_image_generation_configuration)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kinesisvideo/client/#describe_image_generation_configuration)
        """

    async def describe_mapped_resource_configuration(
        self,
        *,
        StreamName: str = ...,
        StreamARN: str = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
    ) -> DescribeMappedResourceConfigurationOutputTypeDef:
        """
        Returns the most current information about the stream.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo.html#KinesisVideo.Client.describe_mapped_resource_configuration)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kinesisvideo/client/#describe_mapped_resource_configuration)
        """

    async def describe_media_storage_configuration(
        self, *, ChannelName: str = ..., ChannelARN: str = ...
    ) -> DescribeMediaStorageConfigurationOutputTypeDef:
        """
        Returns the most current information about the channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo.html#KinesisVideo.Client.describe_media_storage_configuration)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kinesisvideo/client/#describe_media_storage_configuration)
        """

    async def describe_notification_configuration(
        self, *, StreamName: str = ..., StreamARN: str = ...
    ) -> DescribeNotificationConfigurationOutputTypeDef:
        """
        Gets the `NotificationConfiguration` for a given Kinesis video stream.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo.html#KinesisVideo.Client.describe_notification_configuration)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kinesisvideo/client/#describe_notification_configuration)
        """

    async def describe_signaling_channel(
        self, *, ChannelName: str = ..., ChannelARN: str = ...
    ) -> DescribeSignalingChannelOutputTypeDef:
        """
        Returns the most current information about the signaling channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo.html#KinesisVideo.Client.describe_signaling_channel)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kinesisvideo/client/#describe_signaling_channel)
        """

    async def describe_stream(
        self, *, StreamName: str = ..., StreamARN: str = ...
    ) -> DescribeStreamOutputTypeDef:
        """
        Returns the most current information about the specified stream.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo.html#KinesisVideo.Client.describe_stream)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kinesisvideo/client/#describe_stream)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo.html#KinesisVideo.Client.generate_presigned_url)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kinesisvideo/client/#generate_presigned_url)
        """

    async def get_data_endpoint(
        self, *, APIName: APINameType, StreamName: str = ..., StreamARN: str = ...
    ) -> GetDataEndpointOutputTypeDef:
        """
        Gets an endpoint for a specified stream for either reading or writing.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo.html#KinesisVideo.Client.get_data_endpoint)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kinesisvideo/client/#get_data_endpoint)
        """

    async def get_signaling_channel_endpoint(
        self,
        *,
        ChannelARN: str,
        SingleMasterChannelEndpointConfiguration: SingleMasterChannelEndpointConfigurationTypeDef = ...,
    ) -> GetSignalingChannelEndpointOutputTypeDef:
        """
        Provides an endpoint for the specified signaling channel to send and receive
        messages.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo.html#KinesisVideo.Client.get_signaling_channel_endpoint)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kinesisvideo/client/#get_signaling_channel_endpoint)
        """

    async def list_edge_agent_configurations(
        self, *, HubDeviceArn: str, MaxResults: int = ..., NextToken: str = ...
    ) -> ListEdgeAgentConfigurationsOutputTypeDef:
        """
        Returns an array of edge configurations associated with the specified Edge
        Agent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo.html#KinesisVideo.Client.list_edge_agent_configurations)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kinesisvideo/client/#list_edge_agent_configurations)
        """

    async def list_signaling_channels(
        self,
        *,
        MaxResults: int = ...,
        NextToken: str = ...,
        ChannelNameCondition: ChannelNameConditionTypeDef = ...,
    ) -> ListSignalingChannelsOutputTypeDef:
        """
        Returns an array of `ChannelInfo` objects.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo.html#KinesisVideo.Client.list_signaling_channels)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kinesisvideo/client/#list_signaling_channels)
        """

    async def list_streams(
        self,
        *,
        MaxResults: int = ...,
        NextToken: str = ...,
        StreamNameCondition: StreamNameConditionTypeDef = ...,
    ) -> ListStreamsOutputTypeDef:
        """
        Returns an array of `StreamInfo` objects.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo.html#KinesisVideo.Client.list_streams)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kinesisvideo/client/#list_streams)
        """

    async def list_tags_for_resource(
        self, *, ResourceARN: str, NextToken: str = ...
    ) -> ListTagsForResourceOutputTypeDef:
        """
        Returns a list of tags associated with the specified signaling channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo.html#KinesisVideo.Client.list_tags_for_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kinesisvideo/client/#list_tags_for_resource)
        """

    async def list_tags_for_stream(
        self, *, NextToken: str = ..., StreamARN: str = ..., StreamName: str = ...
    ) -> ListTagsForStreamOutputTypeDef:
        """
        Returns a list of tags associated with the specified stream.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo.html#KinesisVideo.Client.list_tags_for_stream)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kinesisvideo/client/#list_tags_for_stream)
        """

    async def start_edge_configuration_update(
        self, *, EdgeConfig: EdgeConfigTypeDef, StreamName: str = ..., StreamARN: str = ...
    ) -> StartEdgeConfigurationUpdateOutputTypeDef:
        """
        An asynchronous API that updates a stream’s existing edge configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo.html#KinesisVideo.Client.start_edge_configuration_update)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kinesisvideo/client/#start_edge_configuration_update)
        """

    async def tag_resource(self, *, ResourceARN: str, Tags: Sequence[TagTypeDef]) -> Dict[str, Any]:
        """
        Adds one or more tags to a signaling channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo.html#KinesisVideo.Client.tag_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kinesisvideo/client/#tag_resource)
        """

    async def tag_stream(
        self, *, Tags: Mapping[str, str], StreamARN: str = ..., StreamName: str = ...
    ) -> Dict[str, Any]:
        """
        Adds one or more tags to a stream.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo.html#KinesisVideo.Client.tag_stream)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kinesisvideo/client/#tag_stream)
        """

    async def untag_resource(
        self, *, ResourceARN: str, TagKeyList: Sequence[str]
    ) -> Dict[str, Any]:
        """
        Removes one or more tags from a signaling channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo.html#KinesisVideo.Client.untag_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kinesisvideo/client/#untag_resource)
        """

    async def untag_stream(
        self, *, TagKeyList: Sequence[str], StreamARN: str = ..., StreamName: str = ...
    ) -> Dict[str, Any]:
        """
        Removes one or more tags from a stream.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo.html#KinesisVideo.Client.untag_stream)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kinesisvideo/client/#untag_stream)
        """

    async def update_data_retention(
        self,
        *,
        CurrentVersion: str,
        Operation: UpdateDataRetentionOperationType,
        DataRetentionChangeInHours: int,
        StreamName: str = ...,
        StreamARN: str = ...,
    ) -> Dict[str, Any]:
        """
        Increases or decreases the stream's data retention period by the value that you
        specify.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo.html#KinesisVideo.Client.update_data_retention)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kinesisvideo/client/#update_data_retention)
        """

    async def update_image_generation_configuration(
        self,
        *,
        StreamName: str = ...,
        StreamARN: str = ...,
        ImageGenerationConfiguration: ImageGenerationConfigurationTypeDef = ...,
    ) -> Dict[str, Any]:
        """
        Updates the `StreamInfo` and `ImageProcessingConfiguration` fields.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo.html#KinesisVideo.Client.update_image_generation_configuration)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kinesisvideo/client/#update_image_generation_configuration)
        """

    async def update_media_storage_configuration(
        self, *, ChannelARN: str, MediaStorageConfiguration: MediaStorageConfigurationTypeDef
    ) -> Dict[str, Any]:
        """
        Associates a `SignalingChannel` to a stream to store the media.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo.html#KinesisVideo.Client.update_media_storage_configuration)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kinesisvideo/client/#update_media_storage_configuration)
        """

    async def update_notification_configuration(
        self,
        *,
        StreamName: str = ...,
        StreamARN: str = ...,
        NotificationConfiguration: NotificationConfigurationTypeDef = ...,
    ) -> Dict[str, Any]:
        """
        Updates the notification information for a stream.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo.html#KinesisVideo.Client.update_notification_configuration)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kinesisvideo/client/#update_notification_configuration)
        """

    async def update_signaling_channel(
        self,
        *,
        ChannelARN: str,
        CurrentVersion: str,
        SingleMasterConfiguration: SingleMasterConfigurationTypeDef = ...,
    ) -> Dict[str, Any]:
        """
        Updates the existing signaling channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo.html#KinesisVideo.Client.update_signaling_channel)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kinesisvideo/client/#update_signaling_channel)
        """

    async def update_stream(
        self,
        *,
        CurrentVersion: str,
        StreamName: str = ...,
        StreamARN: str = ...,
        DeviceName: str = ...,
        MediaType: str = ...,
    ) -> Dict[str, Any]:
        """
        Updates stream metadata, such as the device name and media type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo.html#KinesisVideo.Client.update_stream)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kinesisvideo/client/#update_stream)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_mapped_resource_configuration"]
    ) -> DescribeMappedResourceConfigurationPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo.html#KinesisVideo.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kinesisvideo/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_edge_agent_configurations"]
    ) -> ListEdgeAgentConfigurationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo.html#KinesisVideo.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kinesisvideo/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_signaling_channels"]
    ) -> ListSignalingChannelsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo.html#KinesisVideo.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kinesisvideo/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_streams"]) -> ListStreamsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo.html#KinesisVideo.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kinesisvideo/client/#get_paginator)
        """

    async def __aenter__(self) -> "KinesisVideoClient":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo.html#KinesisVideo.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kinesisvideo/client/)
        """

    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> Any:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo.html#KinesisVideo.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kinesisvideo/client/)
        """
