"""
Type annotations for amp service client waiters.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amp/waiters/)

Usage::

    ```python
    from aiobotocore.session import get_session

    from types_aiobotocore_amp.client import PrometheusServiceClient
    from types_aiobotocore_amp.waiter import (
        ScraperActiveWaiter,
        ScraperDeletedWaiter,
        WorkspaceActiveWaiter,
        WorkspaceDeletedWaiter,
    )

    session = get_session()
    async with session.create_client("amp") as client:
        client: PrometheusServiceClient

        scraper_active_waiter: ScraperActiveWaiter = client.get_waiter("scraper_active")
        scraper_deleted_waiter: ScraperDeletedWaiter = client.get_waiter("scraper_deleted")
        workspace_active_waiter: WorkspaceActiveWaiter = client.get_waiter("workspace_active")
        workspace_deleted_waiter: WorkspaceDeletedWaiter = client.get_waiter("workspace_deleted")
    ```
"""

from aiobotocore.waiter import AIOWaiter

from .type_defs import WaiterConfigTypeDef

__all__ = (
    "ScraperActiveWaiter",
    "ScraperDeletedWaiter",
    "WorkspaceActiveWaiter",
    "WorkspaceDeletedWaiter",
)


class ScraperActiveWaiter(AIOWaiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp.html#PrometheusService.Waiter.ScraperActive)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amp/waiters/#scraperactivewaiter)
    """

    async def wait(self, *, scraperId: str, WaiterConfig: WaiterConfigTypeDef = ...) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp.html#PrometheusService.Waiter.ScraperActive.wait)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amp/waiters/#scraperactivewaiter)
        """


class ScraperDeletedWaiter(AIOWaiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp.html#PrometheusService.Waiter.ScraperDeleted)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amp/waiters/#scraperdeletedwaiter)
    """

    async def wait(self, *, scraperId: str, WaiterConfig: WaiterConfigTypeDef = ...) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp.html#PrometheusService.Waiter.ScraperDeleted.wait)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amp/waiters/#scraperdeletedwaiter)
        """


class WorkspaceActiveWaiter(AIOWaiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp.html#PrometheusService.Waiter.WorkspaceActive)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amp/waiters/#workspaceactivewaiter)
    """

    async def wait(self, *, workspaceId: str, WaiterConfig: WaiterConfigTypeDef = ...) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp.html#PrometheusService.Waiter.WorkspaceActive.wait)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amp/waiters/#workspaceactivewaiter)
        """


class WorkspaceDeletedWaiter(AIOWaiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp.html#PrometheusService.Waiter.WorkspaceDeleted)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amp/waiters/#workspacedeletedwaiter)
    """

    async def wait(self, *, workspaceId: str, WaiterConfig: WaiterConfigTypeDef = ...) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp.html#PrometheusService.Waiter.WorkspaceDeleted.wait)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amp/waiters/#workspacedeletedwaiter)
        """
