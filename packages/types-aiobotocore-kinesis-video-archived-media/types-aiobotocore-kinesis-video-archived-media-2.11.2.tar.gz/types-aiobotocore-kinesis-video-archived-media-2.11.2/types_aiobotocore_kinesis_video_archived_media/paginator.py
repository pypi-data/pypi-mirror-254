"""
Type annotations for kinesis-video-archived-media service client paginators.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kinesis_video_archived_media/paginators/)

Usage::

    ```python
    from aiobotocore.session import get_session

    from types_aiobotocore_kinesis_video_archived_media.client import KinesisVideoArchivedMediaClient
    from types_aiobotocore_kinesis_video_archived_media.paginator import (
        GetImagesPaginator,
        ListFragmentsPaginator,
    )

    session = get_session()
    with session.create_client("kinesis-video-archived-media") as client:
        client: KinesisVideoArchivedMediaClient

        get_images_paginator: GetImagesPaginator = client.get_paginator("get_images")
        list_fragments_paginator: ListFragmentsPaginator = client.get_paginator("list_fragments")
    ```
"""

import sys
from typing import AsyncIterator, Generic, Iterator, Mapping, TypeVar

from aiobotocore.paginate import AioPaginator
from botocore.paginate import PageIterator

from .literals import FormatType, ImageSelectorTypeType
from .type_defs import (
    FragmentSelectorTypeDef,
    GetImagesOutputTypeDef,
    ListFragmentsOutputTypeDef,
    PaginatorConfigTypeDef,
    TimestampTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("GetImagesPaginator", "ListFragmentsPaginator")

_ItemTypeDef = TypeVar("_ItemTypeDef")


class _PageIterator(Generic[_ItemTypeDef], PageIterator):
    def __iter__(self) -> Iterator[_ItemTypeDef]:
        """
        Proxy method to specify iterator item type.
        """


class GetImagesPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis-video-archived-media.html#KinesisVideoArchivedMedia.Paginator.GetImages)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kinesis_video_archived_media/paginators/#getimagespaginator)
    """

    def paginate(
        self,
        *,
        ImageSelectorType: ImageSelectorTypeType,
        StartTimestamp: TimestampTypeDef,
        EndTimestamp: TimestampTypeDef,
        Format: FormatType,
        StreamName: str = ...,
        StreamARN: str = ...,
        SamplingInterval: int = ...,
        FormatConfig: Mapping[Literal["JPEGQuality"], str] = ...,
        WidthPixels: int = ...,
        HeightPixels: int = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[GetImagesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis-video-archived-media.html#KinesisVideoArchivedMedia.Paginator.GetImages.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kinesis_video_archived_media/paginators/#getimagespaginator)
        """


class ListFragmentsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis-video-archived-media.html#KinesisVideoArchivedMedia.Paginator.ListFragments)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kinesis_video_archived_media/paginators/#listfragmentspaginator)
    """

    def paginate(
        self,
        *,
        StreamName: str = ...,
        StreamARN: str = ...,
        FragmentSelector: FragmentSelectorTypeDef = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListFragmentsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis-video-archived-media.html#KinesisVideoArchivedMedia.Paginator.ListFragments.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kinesis_video_archived_media/paginators/#listfragmentspaginator)
        """
