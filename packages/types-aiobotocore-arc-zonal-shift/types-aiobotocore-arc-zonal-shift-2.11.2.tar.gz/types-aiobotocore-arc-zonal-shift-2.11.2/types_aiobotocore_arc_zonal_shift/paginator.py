"""
Type annotations for arc-zonal-shift service client paginators.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_arc_zonal_shift/paginators/)

Usage::

    ```python
    from aiobotocore.session import get_session

    from types_aiobotocore_arc_zonal_shift.client import ARCZonalShiftClient
    from types_aiobotocore_arc_zonal_shift.paginator import (
        ListAutoshiftsPaginator,
        ListManagedResourcesPaginator,
        ListZonalShiftsPaginator,
    )

    session = get_session()
    with session.create_client("arc-zonal-shift") as client:
        client: ARCZonalShiftClient

        list_autoshifts_paginator: ListAutoshiftsPaginator = client.get_paginator("list_autoshifts")
        list_managed_resources_paginator: ListManagedResourcesPaginator = client.get_paginator("list_managed_resources")
        list_zonal_shifts_paginator: ListZonalShiftsPaginator = client.get_paginator("list_zonal_shifts")
    ```
"""

from typing import AsyncIterator, Generic, Iterator, TypeVar

from aiobotocore.paginate import AioPaginator
from botocore.paginate import PageIterator

from .literals import AutoshiftExecutionStatusType, ZonalShiftStatusType
from .type_defs import (
    ListAutoshiftsResponseTypeDef,
    ListManagedResourcesResponseTypeDef,
    ListZonalShiftsResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = ("ListAutoshiftsPaginator", "ListManagedResourcesPaginator", "ListZonalShiftsPaginator")

_ItemTypeDef = TypeVar("_ItemTypeDef")


class _PageIterator(Generic[_ItemTypeDef], PageIterator):
    def __iter__(self) -> Iterator[_ItemTypeDef]:
        """
        Proxy method to specify iterator item type.
        """


class ListAutoshiftsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/arc-zonal-shift.html#ARCZonalShift.Paginator.ListAutoshifts)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_arc_zonal_shift/paginators/#listautoshiftspaginator)
    """

    def paginate(
        self,
        *,
        status: AutoshiftExecutionStatusType = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListAutoshiftsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/arc-zonal-shift.html#ARCZonalShift.Paginator.ListAutoshifts.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_arc_zonal_shift/paginators/#listautoshiftspaginator)
        """


class ListManagedResourcesPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/arc-zonal-shift.html#ARCZonalShift.Paginator.ListManagedResources)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_arc_zonal_shift/paginators/#listmanagedresourcespaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListManagedResourcesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/arc-zonal-shift.html#ARCZonalShift.Paginator.ListManagedResources.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_arc_zonal_shift/paginators/#listmanagedresourcespaginator)
        """


class ListZonalShiftsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/arc-zonal-shift.html#ARCZonalShift.Paginator.ListZonalShifts)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_arc_zonal_shift/paginators/#listzonalshiftspaginator)
    """

    def paginate(
        self,
        *,
        resourceIdentifier: str = ...,
        status: ZonalShiftStatusType = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListZonalShiftsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/arc-zonal-shift.html#ARCZonalShift.Paginator.ListZonalShifts.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_arc_zonal_shift/paginators/#listzonalshiftspaginator)
        """
