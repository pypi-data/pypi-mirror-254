"""
Type annotations for iot-roborunner service client paginators.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iot_roborunner/paginators/)

Usage::

    ```python
    from aiobotocore.session import get_session

    from types_aiobotocore_iot_roborunner.client import IoTRoboRunnerClient
    from types_aiobotocore_iot_roborunner.paginator import (
        ListDestinationsPaginator,
        ListSitesPaginator,
        ListWorkerFleetsPaginator,
        ListWorkersPaginator,
    )

    session = get_session()
    with session.create_client("iot-roborunner") as client:
        client: IoTRoboRunnerClient

        list_destinations_paginator: ListDestinationsPaginator = client.get_paginator("list_destinations")
        list_sites_paginator: ListSitesPaginator = client.get_paginator("list_sites")
        list_worker_fleets_paginator: ListWorkerFleetsPaginator = client.get_paginator("list_worker_fleets")
        list_workers_paginator: ListWorkersPaginator = client.get_paginator("list_workers")
    ```
"""

from typing import AsyncIterator, Generic, Iterator, TypeVar

from aiobotocore.paginate import AioPaginator
from botocore.paginate import PageIterator

from .literals import DestinationStateType
from .type_defs import (
    ListDestinationsResponseTypeDef,
    ListSitesResponseTypeDef,
    ListWorkerFleetsResponseTypeDef,
    ListWorkersResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "ListDestinationsPaginator",
    "ListSitesPaginator",
    "ListWorkerFleetsPaginator",
    "ListWorkersPaginator",
)

_ItemTypeDef = TypeVar("_ItemTypeDef")


class _PageIterator(Generic[_ItemTypeDef], PageIterator):
    def __iter__(self) -> Iterator[_ItemTypeDef]:
        """
        Proxy method to specify iterator item type.
        """


class ListDestinationsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-roborunner.html#IoTRoboRunner.Paginator.ListDestinations)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iot_roborunner/paginators/#listdestinationspaginator)
    """

    def paginate(
        self,
        *,
        site: str,
        state: DestinationStateType = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListDestinationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-roborunner.html#IoTRoboRunner.Paginator.ListDestinations.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iot_roborunner/paginators/#listdestinationspaginator)
        """


class ListSitesPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-roborunner.html#IoTRoboRunner.Paginator.ListSites)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iot_roborunner/paginators/#listsitespaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListSitesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-roborunner.html#IoTRoboRunner.Paginator.ListSites.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iot_roborunner/paginators/#listsitespaginator)
        """


class ListWorkerFleetsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-roborunner.html#IoTRoboRunner.Paginator.ListWorkerFleets)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iot_roborunner/paginators/#listworkerfleetspaginator)
    """

    def paginate(
        self, *, site: str, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListWorkerFleetsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-roborunner.html#IoTRoboRunner.Paginator.ListWorkerFleets.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iot_roborunner/paginators/#listworkerfleetspaginator)
        """


class ListWorkersPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-roborunner.html#IoTRoboRunner.Paginator.ListWorkers)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iot_roborunner/paginators/#listworkerspaginator)
    """

    def paginate(
        self, *, site: str, fleet: str = ..., PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListWorkersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-roborunner.html#IoTRoboRunner.Paginator.ListWorkers.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iot_roborunner/paginators/#listworkerspaginator)
        """
