"""
Type annotations for codeguruprofiler service client paginators.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeguruprofiler/paginators/)

Usage::

    ```python
    from aiobotocore.session import get_session

    from types_aiobotocore_codeguruprofiler.client import CodeGuruProfilerClient
    from types_aiobotocore_codeguruprofiler.paginator import (
        ListProfileTimesPaginator,
    )

    session = get_session()
    with session.create_client("codeguruprofiler") as client:
        client: CodeGuruProfilerClient

        list_profile_times_paginator: ListProfileTimesPaginator = client.get_paginator("list_profile_times")
    ```
"""

from typing import AsyncIterator, Generic, Iterator, TypeVar

from aiobotocore.paginate import AioPaginator
from botocore.paginate import PageIterator

from .literals import AggregationPeriodType, OrderByType
from .type_defs import ListProfileTimesResponseTypeDef, PaginatorConfigTypeDef, TimestampTypeDef

__all__ = ("ListProfileTimesPaginator",)

_ItemTypeDef = TypeVar("_ItemTypeDef")


class _PageIterator(Generic[_ItemTypeDef], PageIterator):
    def __iter__(self) -> Iterator[_ItemTypeDef]:
        """
        Proxy method to specify iterator item type.
        """


class ListProfileTimesPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguruprofiler.html#CodeGuruProfiler.Paginator.ListProfileTimes)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeguruprofiler/paginators/#listprofiletimespaginator)
    """

    def paginate(
        self,
        *,
        endTime: TimestampTypeDef,
        period: AggregationPeriodType,
        profilingGroupName: str,
        startTime: TimestampTypeDef,
        orderBy: OrderByType = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListProfileTimesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguruprofiler.html#CodeGuruProfiler.Paginator.ListProfileTimes.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeguruprofiler/paginators/#listprofiletimespaginator)
        """
