"""
Type annotations for textract service client paginators.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_textract/paginators/)

Usage::

    ```python
    from aiobotocore.session import get_session

    from types_aiobotocore_textract.client import TextractClient
    from types_aiobotocore_textract.paginator import (
        ListAdapterVersionsPaginator,
        ListAdaptersPaginator,
    )

    session = get_session()
    with session.create_client("textract") as client:
        client: TextractClient

        list_adapter_versions_paginator: ListAdapterVersionsPaginator = client.get_paginator("list_adapter_versions")
        list_adapters_paginator: ListAdaptersPaginator = client.get_paginator("list_adapters")
    ```
"""

from typing import AsyncIterator, Generic, Iterator, TypeVar

from aiobotocore.paginate import AioPaginator
from botocore.paginate import PageIterator

from .type_defs import (
    ListAdaptersResponseTypeDef,
    ListAdapterVersionsResponseTypeDef,
    PaginatorConfigTypeDef,
    TimestampTypeDef,
)

__all__ = ("ListAdapterVersionsPaginator", "ListAdaptersPaginator")

_ItemTypeDef = TypeVar("_ItemTypeDef")


class _PageIterator(Generic[_ItemTypeDef], PageIterator):
    def __iter__(self) -> Iterator[_ItemTypeDef]:
        """
        Proxy method to specify iterator item type.
        """


class ListAdapterVersionsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/textract.html#Textract.Paginator.ListAdapterVersions)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_textract/paginators/#listadapterversionspaginator)
    """

    def paginate(
        self,
        *,
        AdapterId: str = ...,
        AfterCreationTime: TimestampTypeDef = ...,
        BeforeCreationTime: TimestampTypeDef = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListAdapterVersionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/textract.html#Textract.Paginator.ListAdapterVersions.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_textract/paginators/#listadapterversionspaginator)
        """


class ListAdaptersPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/textract.html#Textract.Paginator.ListAdapters)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_textract/paginators/#listadapterspaginator)
    """

    def paginate(
        self,
        *,
        AfterCreationTime: TimestampTypeDef = ...,
        BeforeCreationTime: TimestampTypeDef = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListAdaptersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/textract.html#Textract.Paginator.ListAdapters.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_textract/paginators/#listadapterspaginator)
        """
