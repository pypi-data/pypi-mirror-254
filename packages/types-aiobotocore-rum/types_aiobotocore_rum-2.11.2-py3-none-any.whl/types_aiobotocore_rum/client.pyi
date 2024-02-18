"""
Type annotations for rum service client.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rum/client/)

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_rum.client import CloudWatchRUMClient

    session = get_session()
    async with session.create_client("rum") as client:
        client: CloudWatchRUMClient
    ```
"""

import sys
from typing import Any, Dict, Mapping, Sequence, Type, overload

from aiobotocore.client import AioBaseClient
from botocore.client import ClientMeta

from .literals import MetricDestinationType
from .paginator import (
    BatchGetRumMetricDefinitionsPaginator,
    GetAppMonitorDataPaginator,
    ListAppMonitorsPaginator,
    ListRumMetricsDestinationsPaginator,
)
from .type_defs import (
    AppMonitorConfigurationTypeDef,
    AppMonitorDetailsTypeDef,
    BatchCreateRumMetricDefinitionsResponseTypeDef,
    BatchDeleteRumMetricDefinitionsResponseTypeDef,
    BatchGetRumMetricDefinitionsResponseTypeDef,
    CreateAppMonitorResponseTypeDef,
    CustomEventsTypeDef,
    GetAppMonitorDataResponseTypeDef,
    GetAppMonitorResponseTypeDef,
    ListAppMonitorsResponseTypeDef,
    ListRumMetricsDestinationsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    MetricDefinitionRequestTypeDef,
    QueryFilterTypeDef,
    RumEventTypeDef,
    TimeRangeTypeDef,
    UserDetailsTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("CloudWatchRUMClient",)

class BotocoreClientError(Exception):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class CloudWatchRUMClient(AioBaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rum.html#CloudWatchRUM.Client)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rum/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        CloudWatchRUMClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rum.html#CloudWatchRUM.Client.exceptions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rum/client/#exceptions)
        """

    async def batch_create_rum_metric_definitions(
        self,
        *,
        AppMonitorName: str,
        Destination: MetricDestinationType,
        MetricDefinitions: Sequence[MetricDefinitionRequestTypeDef],
        DestinationArn: str = ...,
    ) -> BatchCreateRumMetricDefinitionsResponseTypeDef:
        """
        Specifies the extended metrics and custom metrics that you want a CloudWatch
        RUM app monitor to send to a
        destination.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rum.html#CloudWatchRUM.Client.batch_create_rum_metric_definitions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rum/client/#batch_create_rum_metric_definitions)
        """

    async def batch_delete_rum_metric_definitions(
        self,
        *,
        AppMonitorName: str,
        Destination: MetricDestinationType,
        MetricDefinitionIds: Sequence[str],
        DestinationArn: str = ...,
    ) -> BatchDeleteRumMetricDefinitionsResponseTypeDef:
        """
        Removes the specified metrics from being sent to an extended metrics
        destination.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rum.html#CloudWatchRUM.Client.batch_delete_rum_metric_definitions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rum/client/#batch_delete_rum_metric_definitions)
        """

    async def batch_get_rum_metric_definitions(
        self,
        *,
        AppMonitorName: str,
        Destination: MetricDestinationType,
        DestinationArn: str = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
    ) -> BatchGetRumMetricDefinitionsResponseTypeDef:
        """
        Retrieves the list of metrics and dimensions that a RUM app monitor is sending
        to a single
        destination.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rum.html#CloudWatchRUM.Client.batch_get_rum_metric_definitions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rum/client/#batch_get_rum_metric_definitions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rum.html#CloudWatchRUM.Client.can_paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rum/client/#can_paginate)
        """

    async def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rum.html#CloudWatchRUM.Client.close)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rum/client/#close)
        """

    async def create_app_monitor(
        self,
        *,
        Domain: str,
        Name: str,
        AppMonitorConfiguration: AppMonitorConfigurationTypeDef = ...,
        CustomEvents: CustomEventsTypeDef = ...,
        CwLogEnabled: bool = ...,
        Tags: Mapping[str, str] = ...,
    ) -> CreateAppMonitorResponseTypeDef:
        """
        Creates a Amazon CloudWatch RUM app monitor, which collects telemetry data from
        your application and sends that data to
        RUM.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rum.html#CloudWatchRUM.Client.create_app_monitor)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rum/client/#create_app_monitor)
        """

    async def delete_app_monitor(self, *, Name: str) -> Dict[str, Any]:
        """
        Deletes an existing app monitor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rum.html#CloudWatchRUM.Client.delete_app_monitor)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rum/client/#delete_app_monitor)
        """

    async def delete_rum_metrics_destination(
        self, *, AppMonitorName: str, Destination: MetricDestinationType, DestinationArn: str = ...
    ) -> Dict[str, Any]:
        """
        Deletes a destination for CloudWatch RUM extended metrics, so that the
        specified app monitor stops sending extended metrics to that
        destination.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rum.html#CloudWatchRUM.Client.delete_rum_metrics_destination)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rum/client/#delete_rum_metrics_destination)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rum.html#CloudWatchRUM.Client.generate_presigned_url)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rum/client/#generate_presigned_url)
        """

    async def get_app_monitor(self, *, Name: str) -> GetAppMonitorResponseTypeDef:
        """
        Retrieves the complete configuration information for one app monitor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rum.html#CloudWatchRUM.Client.get_app_monitor)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rum/client/#get_app_monitor)
        """

    async def get_app_monitor_data(
        self,
        *,
        Name: str,
        TimeRange: TimeRangeTypeDef,
        Filters: Sequence[QueryFilterTypeDef] = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
    ) -> GetAppMonitorDataResponseTypeDef:
        """
        Retrieves the raw performance events that RUM has collected from your web
        application, so that you can do your own processing or analysis of this
        data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rum.html#CloudWatchRUM.Client.get_app_monitor_data)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rum/client/#get_app_monitor_data)
        """

    async def list_app_monitors(
        self, *, MaxResults: int = ..., NextToken: str = ...
    ) -> ListAppMonitorsResponseTypeDef:
        """
        Returns a list of the Amazon CloudWatch RUM app monitors in the account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rum.html#CloudWatchRUM.Client.list_app_monitors)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rum/client/#list_app_monitors)
        """

    async def list_rum_metrics_destinations(
        self, *, AppMonitorName: str, MaxResults: int = ..., NextToken: str = ...
    ) -> ListRumMetricsDestinationsResponseTypeDef:
        """
        Returns a list of destinations that you have created to receive RUM extended
        metrics, for the specified app
        monitor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rum.html#CloudWatchRUM.Client.list_rum_metrics_destinations)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rum/client/#list_rum_metrics_destinations)
        """

    async def list_tags_for_resource(
        self, *, ResourceArn: str
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Displays the tags associated with a CloudWatch RUM resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rum.html#CloudWatchRUM.Client.list_tags_for_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rum/client/#list_tags_for_resource)
        """

    async def put_rum_events(
        self,
        *,
        AppMonitorDetails: AppMonitorDetailsTypeDef,
        BatchId: str,
        Id: str,
        RumEvents: Sequence[RumEventTypeDef],
        UserDetails: UserDetailsTypeDef,
    ) -> Dict[str, Any]:
        """
        Sends telemetry events about your application performance and user behavior to
        CloudWatch
        RUM.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rum.html#CloudWatchRUM.Client.put_rum_events)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rum/client/#put_rum_events)
        """

    async def put_rum_metrics_destination(
        self,
        *,
        AppMonitorName: str,
        Destination: MetricDestinationType,
        DestinationArn: str = ...,
        IamRoleArn: str = ...,
    ) -> Dict[str, Any]:
        """
        Creates or updates a destination to receive extended metrics from CloudWatch
        RUM.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rum.html#CloudWatchRUM.Client.put_rum_metrics_destination)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rum/client/#put_rum_metrics_destination)
        """

    async def tag_resource(self, *, ResourceArn: str, Tags: Mapping[str, str]) -> Dict[str, Any]:
        """
        Assigns one or more tags (key-value pairs) to the specified CloudWatch RUM
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rum.html#CloudWatchRUM.Client.tag_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rum/client/#tag_resource)
        """

    async def untag_resource(self, *, ResourceArn: str, TagKeys: Sequence[str]) -> Dict[str, Any]:
        """
        Removes one or more tags from the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rum.html#CloudWatchRUM.Client.untag_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rum/client/#untag_resource)
        """

    async def update_app_monitor(
        self,
        *,
        Name: str,
        AppMonitorConfiguration: AppMonitorConfigurationTypeDef = ...,
        CustomEvents: CustomEventsTypeDef = ...,
        CwLogEnabled: bool = ...,
        Domain: str = ...,
    ) -> Dict[str, Any]:
        """
        Updates the configuration of an existing app monitor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rum.html#CloudWatchRUM.Client.update_app_monitor)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rum/client/#update_app_monitor)
        """

    async def update_rum_metric_definition(
        self,
        *,
        AppMonitorName: str,
        Destination: MetricDestinationType,
        MetricDefinition: MetricDefinitionRequestTypeDef,
        MetricDefinitionId: str,
        DestinationArn: str = ...,
    ) -> Dict[str, Any]:
        """
        Modifies one existing metric definition for CloudWatch RUM extended metrics.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rum.html#CloudWatchRUM.Client.update_rum_metric_definition)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rum/client/#update_rum_metric_definition)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["batch_get_rum_metric_definitions"]
    ) -> BatchGetRumMetricDefinitionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rum.html#CloudWatchRUM.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rum/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_app_monitor_data"]
    ) -> GetAppMonitorDataPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rum.html#CloudWatchRUM.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rum/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_app_monitors"]
    ) -> ListAppMonitorsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rum.html#CloudWatchRUM.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rum/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_rum_metrics_destinations"]
    ) -> ListRumMetricsDestinationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rum.html#CloudWatchRUM.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rum/client/#get_paginator)
        """

    async def __aenter__(self) -> "CloudWatchRUMClient":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rum.html#CloudWatchRUM.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rum/client/)
        """

    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> Any:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rum.html#CloudWatchRUM.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rum/client/)
        """
