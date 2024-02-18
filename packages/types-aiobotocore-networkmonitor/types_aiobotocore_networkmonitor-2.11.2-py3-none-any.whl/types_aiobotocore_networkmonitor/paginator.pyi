"""
Type annotations for networkmonitor service client paginators.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_networkmonitor/paginators/)

Usage::

    ```python
    from aiobotocore.session import get_session

    from types_aiobotocore_networkmonitor.client import CloudWatchNetworkMonitorClient
    from types_aiobotocore_networkmonitor.paginator import (
        ListMonitorsPaginator,
    )

    session = get_session()
    with session.create_client("networkmonitor") as client:
        client: CloudWatchNetworkMonitorClient

        list_monitors_paginator: ListMonitorsPaginator = client.get_paginator("list_monitors")
    ```
"""

from typing import AsyncIterator, Generic, Iterator, TypeVar

from aiobotocore.paginate import AioPaginator
from botocore.paginate import PageIterator

from .type_defs import ListMonitorsOutputTypeDef, PaginatorConfigTypeDef

__all__ = ("ListMonitorsPaginator",)

_ItemTypeDef = TypeVar("_ItemTypeDef")

class _PageIterator(Generic[_ItemTypeDef], PageIterator):
    def __iter__(self) -> Iterator[_ItemTypeDef]:
        """
        Proxy method to specify iterator item type.
        """

class ListMonitorsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmonitor.html#CloudWatchNetworkMonitor.Paginator.ListMonitors)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_networkmonitor/paginators/#listmonitorspaginator)
    """

    def paginate(
        self, *, state: str = ..., PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListMonitorsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmonitor.html#CloudWatchNetworkMonitor.Paginator.ListMonitors.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_networkmonitor/paginators/#listmonitorspaginator)
        """
