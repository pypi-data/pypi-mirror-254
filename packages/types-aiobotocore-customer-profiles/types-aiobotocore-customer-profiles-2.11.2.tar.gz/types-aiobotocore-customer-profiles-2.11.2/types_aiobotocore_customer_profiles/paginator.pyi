"""
Type annotations for customer-profiles service client paginators.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_customer_profiles/paginators/)

Usage::

    ```python
    from aiobotocore.session import get_session

    from types_aiobotocore_customer_profiles.client import CustomerProfilesClient
    from types_aiobotocore_customer_profiles.paginator import (
        ListEventStreamsPaginator,
    )

    session = get_session()
    with session.create_client("customer-profiles") as client:
        client: CustomerProfilesClient

        list_event_streams_paginator: ListEventStreamsPaginator = client.get_paginator("list_event_streams")
    ```
"""

from typing import AsyncIterator, Generic, Iterator, TypeVar

from aiobotocore.paginate import AioPaginator
from botocore.paginate import PageIterator

from .type_defs import ListEventStreamsResponseTypeDef, PaginatorConfigTypeDef

__all__ = ("ListEventStreamsPaginator",)

_ItemTypeDef = TypeVar("_ItemTypeDef")

class _PageIterator(Generic[_ItemTypeDef], PageIterator):
    def __iter__(self) -> Iterator[_ItemTypeDef]:
        """
        Proxy method to specify iterator item type.
        """

class ListEventStreamsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html#CustomerProfiles.Paginator.ListEventStreams)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_customer_profiles/paginators/#listeventstreamspaginator)
    """

    def paginate(
        self, *, DomainName: str, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListEventStreamsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html#CustomerProfiles.Paginator.ListEventStreams.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_customer_profiles/paginators/#listeventstreamspaginator)
        """
