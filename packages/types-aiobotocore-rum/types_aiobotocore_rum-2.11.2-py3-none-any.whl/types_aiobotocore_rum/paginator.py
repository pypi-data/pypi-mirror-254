"""
Type annotations for rum service client paginators.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rum/paginators/)

Usage::

    ```python
    from aiobotocore.session import get_session

    from types_aiobotocore_rum.client import CloudWatchRUMClient
    from types_aiobotocore_rum.paginator import (
        BatchGetRumMetricDefinitionsPaginator,
        GetAppMonitorDataPaginator,
        ListAppMonitorsPaginator,
        ListRumMetricsDestinationsPaginator,
    )

    session = get_session()
    with session.create_client("rum") as client:
        client: CloudWatchRUMClient

        batch_get_rum_metric_definitions_paginator: BatchGetRumMetricDefinitionsPaginator = client.get_paginator("batch_get_rum_metric_definitions")
        get_app_monitor_data_paginator: GetAppMonitorDataPaginator = client.get_paginator("get_app_monitor_data")
        list_app_monitors_paginator: ListAppMonitorsPaginator = client.get_paginator("list_app_monitors")
        list_rum_metrics_destinations_paginator: ListRumMetricsDestinationsPaginator = client.get_paginator("list_rum_metrics_destinations")
    ```
"""

from typing import AsyncIterator, Generic, Iterator, Sequence, TypeVar

from aiobotocore.paginate import AioPaginator
from botocore.paginate import PageIterator

from .literals import MetricDestinationType
from .type_defs import (
    BatchGetRumMetricDefinitionsResponseTypeDef,
    GetAppMonitorDataResponseTypeDef,
    ListAppMonitorsResponseTypeDef,
    ListRumMetricsDestinationsResponseTypeDef,
    PaginatorConfigTypeDef,
    QueryFilterTypeDef,
    TimeRangeTypeDef,
)

__all__ = (
    "BatchGetRumMetricDefinitionsPaginator",
    "GetAppMonitorDataPaginator",
    "ListAppMonitorsPaginator",
    "ListRumMetricsDestinationsPaginator",
)

_ItemTypeDef = TypeVar("_ItemTypeDef")


class _PageIterator(Generic[_ItemTypeDef], PageIterator):
    def __iter__(self) -> Iterator[_ItemTypeDef]:
        """
        Proxy method to specify iterator item type.
        """


class BatchGetRumMetricDefinitionsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rum.html#CloudWatchRUM.Paginator.BatchGetRumMetricDefinitions)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rum/paginators/#batchgetrummetricdefinitionspaginator)
    """

    def paginate(
        self,
        *,
        AppMonitorName: str,
        Destination: MetricDestinationType,
        DestinationArn: str = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[BatchGetRumMetricDefinitionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rum.html#CloudWatchRUM.Paginator.BatchGetRumMetricDefinitions.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rum/paginators/#batchgetrummetricdefinitionspaginator)
        """


class GetAppMonitorDataPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rum.html#CloudWatchRUM.Paginator.GetAppMonitorData)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rum/paginators/#getappmonitordatapaginator)
    """

    def paginate(
        self,
        *,
        Name: str,
        TimeRange: TimeRangeTypeDef,
        Filters: Sequence[QueryFilterTypeDef] = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[GetAppMonitorDataResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rum.html#CloudWatchRUM.Paginator.GetAppMonitorData.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rum/paginators/#getappmonitordatapaginator)
        """


class ListAppMonitorsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rum.html#CloudWatchRUM.Paginator.ListAppMonitors)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rum/paginators/#listappmonitorspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListAppMonitorsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rum.html#CloudWatchRUM.Paginator.ListAppMonitors.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rum/paginators/#listappmonitorspaginator)
        """


class ListRumMetricsDestinationsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rum.html#CloudWatchRUM.Paginator.ListRumMetricsDestinations)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rum/paginators/#listrummetricsdestinationspaginator)
    """

    def paginate(
        self, *, AppMonitorName: str, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListRumMetricsDestinationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rum.html#CloudWatchRUM.Paginator.ListRumMetricsDestinations.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rum/paginators/#listrummetricsdestinationspaginator)
        """
