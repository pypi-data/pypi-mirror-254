"""
Type annotations for kinesisvideo service client paginators.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kinesisvideo/paginators/)

Usage::

    ```python
    from aiobotocore.session import get_session

    from types_aiobotocore_kinesisvideo.client import KinesisVideoClient
    from types_aiobotocore_kinesisvideo.paginator import (
        DescribeMappedResourceConfigurationPaginator,
        ListEdgeAgentConfigurationsPaginator,
        ListSignalingChannelsPaginator,
        ListStreamsPaginator,
    )

    session = get_session()
    with session.create_client("kinesisvideo") as client:
        client: KinesisVideoClient

        describe_mapped_resource_configuration_paginator: DescribeMappedResourceConfigurationPaginator = client.get_paginator("describe_mapped_resource_configuration")
        list_edge_agent_configurations_paginator: ListEdgeAgentConfigurationsPaginator = client.get_paginator("list_edge_agent_configurations")
        list_signaling_channels_paginator: ListSignalingChannelsPaginator = client.get_paginator("list_signaling_channels")
        list_streams_paginator: ListStreamsPaginator = client.get_paginator("list_streams")
    ```
"""

from typing import AsyncIterator, Generic, Iterator, TypeVar

from aiobotocore.paginate import AioPaginator
from botocore.paginate import PageIterator

from .type_defs import (
    ChannelNameConditionTypeDef,
    DescribeMappedResourceConfigurationOutputTypeDef,
    ListEdgeAgentConfigurationsOutputTypeDef,
    ListSignalingChannelsOutputTypeDef,
    ListStreamsOutputTypeDef,
    PaginatorConfigTypeDef,
    StreamNameConditionTypeDef,
)

__all__ = (
    "DescribeMappedResourceConfigurationPaginator",
    "ListEdgeAgentConfigurationsPaginator",
    "ListSignalingChannelsPaginator",
    "ListStreamsPaginator",
)

_ItemTypeDef = TypeVar("_ItemTypeDef")


class _PageIterator(Generic[_ItemTypeDef], PageIterator):
    def __iter__(self) -> Iterator[_ItemTypeDef]:
        """
        Proxy method to specify iterator item type.
        """


class DescribeMappedResourceConfigurationPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo.html#KinesisVideo.Paginator.DescribeMappedResourceConfiguration)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kinesisvideo/paginators/#describemappedresourceconfigurationpaginator)
    """

    def paginate(
        self,
        *,
        StreamName: str = ...,
        StreamARN: str = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[DescribeMappedResourceConfigurationOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo.html#KinesisVideo.Paginator.DescribeMappedResourceConfiguration.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kinesisvideo/paginators/#describemappedresourceconfigurationpaginator)
        """


class ListEdgeAgentConfigurationsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo.html#KinesisVideo.Paginator.ListEdgeAgentConfigurations)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kinesisvideo/paginators/#listedgeagentconfigurationspaginator)
    """

    def paginate(
        self, *, HubDeviceArn: str, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListEdgeAgentConfigurationsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo.html#KinesisVideo.Paginator.ListEdgeAgentConfigurations.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kinesisvideo/paginators/#listedgeagentconfigurationspaginator)
        """


class ListSignalingChannelsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo.html#KinesisVideo.Paginator.ListSignalingChannels)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kinesisvideo/paginators/#listsignalingchannelspaginator)
    """

    def paginate(
        self,
        *,
        ChannelNameCondition: ChannelNameConditionTypeDef = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListSignalingChannelsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo.html#KinesisVideo.Paginator.ListSignalingChannels.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kinesisvideo/paginators/#listsignalingchannelspaginator)
        """


class ListStreamsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo.html#KinesisVideo.Paginator.ListStreams)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kinesisvideo/paginators/#liststreamspaginator)
    """

    def paginate(
        self,
        *,
        StreamNameCondition: StreamNameConditionTypeDef = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListStreamsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo.html#KinesisVideo.Paginator.ListStreams.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kinesisvideo/paginators/#liststreamspaginator)
        """
