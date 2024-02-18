"""
Type annotations for cloudfront-keyvaluestore service client paginators.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront_keyvaluestore/paginators/)

Usage::

    ```python
    from aiobotocore.session import get_session

    from types_aiobotocore_cloudfront_keyvaluestore.client import CloudFrontKeyValueStoreClient
    from types_aiobotocore_cloudfront_keyvaluestore.paginator import (
        ListKeysPaginator,
    )

    session = get_session()
    with session.create_client("cloudfront-keyvaluestore") as client:
        client: CloudFrontKeyValueStoreClient

        list_keys_paginator: ListKeysPaginator = client.get_paginator("list_keys")
    ```
"""

from typing import AsyncIterator, Generic, Iterator, TypeVar

from aiobotocore.paginate import AioPaginator
from botocore.paginate import PageIterator

from .type_defs import ListKeysResponseTypeDef, PaginatorConfigTypeDef

__all__ = ("ListKeysPaginator",)

_ItemTypeDef = TypeVar("_ItemTypeDef")

class _PageIterator(Generic[_ItemTypeDef], PageIterator):
    def __iter__(self) -> Iterator[_ItemTypeDef]:
        """
        Proxy method to specify iterator item type.
        """

class ListKeysPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront-keyvaluestore.html#CloudFrontKeyValueStore.Paginator.ListKeys)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront_keyvaluestore/paginators/#listkeyspaginator)
    """

    def paginate(
        self, *, KvsARN: str, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListKeysResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront-keyvaluestore.html#CloudFrontKeyValueStore.Paginator.ListKeys.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront_keyvaluestore/paginators/#listkeyspaginator)
        """
