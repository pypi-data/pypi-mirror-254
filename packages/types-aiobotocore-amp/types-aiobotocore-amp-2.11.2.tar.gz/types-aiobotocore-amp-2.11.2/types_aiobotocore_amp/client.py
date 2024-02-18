"""
Type annotations for amp service client.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amp/client/)

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_amp.client import PrometheusServiceClient

    session = get_session()
    async with session.create_client("amp") as client:
        client: PrometheusServiceClient
    ```
"""

import sys
from typing import Any, Dict, Mapping, Sequence, Type, overload

from aiobotocore.client import AioBaseClient
from botocore.client import ClientMeta

from .paginator import (
    ListRuleGroupsNamespacesPaginator,
    ListScrapersPaginator,
    ListWorkspacesPaginator,
)
from .type_defs import (
    BlobTypeDef,
    CreateAlertManagerDefinitionResponseTypeDef,
    CreateLoggingConfigurationResponseTypeDef,
    CreateRuleGroupsNamespaceResponseTypeDef,
    CreateScraperResponseTypeDef,
    CreateWorkspaceResponseTypeDef,
    DeleteScraperResponseTypeDef,
    DescribeAlertManagerDefinitionResponseTypeDef,
    DescribeLoggingConfigurationResponseTypeDef,
    DescribeRuleGroupsNamespaceResponseTypeDef,
    DescribeScraperResponseTypeDef,
    DescribeWorkspaceResponseTypeDef,
    DestinationTypeDef,
    EmptyResponseMetadataTypeDef,
    GetDefaultScraperConfigurationResponseTypeDef,
    ListRuleGroupsNamespacesResponseTypeDef,
    ListScrapersResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListWorkspacesResponseTypeDef,
    PutAlertManagerDefinitionResponseTypeDef,
    PutRuleGroupsNamespaceResponseTypeDef,
    ScrapeConfigurationTypeDef,
    SourceTypeDef,
    UpdateLoggingConfigurationResponseTypeDef,
)
from .waiter import (
    ScraperActiveWaiter,
    ScraperDeletedWaiter,
    WorkspaceActiveWaiter,
    WorkspaceDeletedWaiter,
)

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("PrometheusServiceClient",)


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


class PrometheusServiceClient(AioBaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp.html#PrometheusService.Client)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amp/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        PrometheusServiceClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp.html#PrometheusService.Client.exceptions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amp/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp.html#PrometheusService.Client.can_paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amp/client/#can_paginate)
        """

    async def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp.html#PrometheusService.Client.close)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amp/client/#close)
        """

    async def create_alert_manager_definition(
        self, *, workspaceId: str, data: BlobTypeDef, clientToken: str = ...
    ) -> CreateAlertManagerDefinitionResponseTypeDef:
        """
        Create an alert manager definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp.html#PrometheusService.Client.create_alert_manager_definition)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amp/client/#create_alert_manager_definition)
        """

    async def create_logging_configuration(
        self, *, workspaceId: str, logGroupArn: str, clientToken: str = ...
    ) -> CreateLoggingConfigurationResponseTypeDef:
        """
        Create logging configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp.html#PrometheusService.Client.create_logging_configuration)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amp/client/#create_logging_configuration)
        """

    async def create_rule_groups_namespace(
        self,
        *,
        workspaceId: str,
        name: str,
        data: BlobTypeDef,
        clientToken: str = ...,
        tags: Mapping[str, str] = ...,
    ) -> CreateRuleGroupsNamespaceResponseTypeDef:
        """
        Create a rule group namespace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp.html#PrometheusService.Client.create_rule_groups_namespace)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amp/client/#create_rule_groups_namespace)
        """

    async def create_scraper(
        self,
        *,
        scrapeConfiguration: ScrapeConfigurationTypeDef,
        source: SourceTypeDef,
        destination: DestinationTypeDef,
        alias: str = ...,
        clientToken: str = ...,
        tags: Mapping[str, str] = ...,
    ) -> CreateScraperResponseTypeDef:
        """
        Create a scraper.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp.html#PrometheusService.Client.create_scraper)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amp/client/#create_scraper)
        """

    async def create_workspace(
        self,
        *,
        alias: str = ...,
        clientToken: str = ...,
        tags: Mapping[str, str] = ...,
        kmsKeyArn: str = ...,
    ) -> CreateWorkspaceResponseTypeDef:
        """
        Creates a new AMP workspace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp.html#PrometheusService.Client.create_workspace)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amp/client/#create_workspace)
        """

    async def delete_alert_manager_definition(
        self, *, workspaceId: str, clientToken: str = ...
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes an alert manager definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp.html#PrometheusService.Client.delete_alert_manager_definition)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amp/client/#delete_alert_manager_definition)
        """

    async def delete_logging_configuration(
        self, *, workspaceId: str, clientToken: str = ...
    ) -> EmptyResponseMetadataTypeDef:
        """
        Delete logging configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp.html#PrometheusService.Client.delete_logging_configuration)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amp/client/#delete_logging_configuration)
        """

    async def delete_rule_groups_namespace(
        self, *, workspaceId: str, name: str, clientToken: str = ...
    ) -> EmptyResponseMetadataTypeDef:
        """
        Delete a rule groups namespace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp.html#PrometheusService.Client.delete_rule_groups_namespace)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amp/client/#delete_rule_groups_namespace)
        """

    async def delete_scraper(
        self, *, scraperId: str, clientToken: str = ...
    ) -> DeleteScraperResponseTypeDef:
        """
        Deletes a scraper.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp.html#PrometheusService.Client.delete_scraper)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amp/client/#delete_scraper)
        """

    async def delete_workspace(
        self, *, workspaceId: str, clientToken: str = ...
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes an AMP workspace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp.html#PrometheusService.Client.delete_workspace)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amp/client/#delete_workspace)
        """

    async def describe_alert_manager_definition(
        self, *, workspaceId: str
    ) -> DescribeAlertManagerDefinitionResponseTypeDef:
        """
        Describes an alert manager definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp.html#PrometheusService.Client.describe_alert_manager_definition)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amp/client/#describe_alert_manager_definition)
        """

    async def describe_logging_configuration(
        self, *, workspaceId: str
    ) -> DescribeLoggingConfigurationResponseTypeDef:
        """
        Describes logging configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp.html#PrometheusService.Client.describe_logging_configuration)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amp/client/#describe_logging_configuration)
        """

    async def describe_rule_groups_namespace(
        self, *, workspaceId: str, name: str
    ) -> DescribeRuleGroupsNamespaceResponseTypeDef:
        """
        Describe a rule groups namespace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp.html#PrometheusService.Client.describe_rule_groups_namespace)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amp/client/#describe_rule_groups_namespace)
        """

    async def describe_scraper(self, *, scraperId: str) -> DescribeScraperResponseTypeDef:
        """
        Describe an existing scraper.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp.html#PrometheusService.Client.describe_scraper)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amp/client/#describe_scraper)
        """

    async def describe_workspace(self, *, workspaceId: str) -> DescribeWorkspaceResponseTypeDef:
        """
        Describes an existing AMP workspace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp.html#PrometheusService.Client.describe_workspace)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amp/client/#describe_workspace)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp.html#PrometheusService.Client.generate_presigned_url)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amp/client/#generate_presigned_url)
        """

    async def get_default_scraper_configuration(
        self,
    ) -> GetDefaultScraperConfigurationResponseTypeDef:
        """
        Gets a default configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp.html#PrometheusService.Client.get_default_scraper_configuration)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amp/client/#get_default_scraper_configuration)
        """

    async def list_rule_groups_namespaces(
        self, *, workspaceId: str, name: str = ..., nextToken: str = ..., maxResults: int = ...
    ) -> ListRuleGroupsNamespacesResponseTypeDef:
        """
        Lists rule groups namespaces.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp.html#PrometheusService.Client.list_rule_groups_namespaces)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amp/client/#list_rule_groups_namespaces)
        """

    async def list_scrapers(
        self,
        *,
        filters: Mapping[str, Sequence[str]] = ...,
        nextToken: str = ...,
        maxResults: int = ...,
    ) -> ListScrapersResponseTypeDef:
        """
        Lists all scrapers in a customer account, including scrapers being created or
        deleted.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp.html#PrometheusService.Client.list_scrapers)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amp/client/#list_scrapers)
        """

    async def list_tags_for_resource(
        self, *, resourceArn: str
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists the tags you have assigned to the resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp.html#PrometheusService.Client.list_tags_for_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amp/client/#list_tags_for_resource)
        """

    async def list_workspaces(
        self, *, nextToken: str = ..., alias: str = ..., maxResults: int = ...
    ) -> ListWorkspacesResponseTypeDef:
        """
        Lists all AMP workspaces, including workspaces being created or deleted.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp.html#PrometheusService.Client.list_workspaces)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amp/client/#list_workspaces)
        """

    async def put_alert_manager_definition(
        self, *, workspaceId: str, data: BlobTypeDef, clientToken: str = ...
    ) -> PutAlertManagerDefinitionResponseTypeDef:
        """
        Update an alert manager definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp.html#PrometheusService.Client.put_alert_manager_definition)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amp/client/#put_alert_manager_definition)
        """

    async def put_rule_groups_namespace(
        self, *, workspaceId: str, name: str, data: BlobTypeDef, clientToken: str = ...
    ) -> PutRuleGroupsNamespaceResponseTypeDef:
        """
        Update a rule groups namespace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp.html#PrometheusService.Client.put_rule_groups_namespace)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amp/client/#put_rule_groups_namespace)
        """

    async def tag_resource(self, *, resourceArn: str, tags: Mapping[str, str]) -> Dict[str, Any]:
        """
        Creates tags for the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp.html#PrometheusService.Client.tag_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amp/client/#tag_resource)
        """

    async def untag_resource(self, *, resourceArn: str, tagKeys: Sequence[str]) -> Dict[str, Any]:
        """
        Deletes tags from the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp.html#PrometheusService.Client.untag_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amp/client/#untag_resource)
        """

    async def update_logging_configuration(
        self, *, workspaceId: str, logGroupArn: str, clientToken: str = ...
    ) -> UpdateLoggingConfigurationResponseTypeDef:
        """
        Update logging configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp.html#PrometheusService.Client.update_logging_configuration)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amp/client/#update_logging_configuration)
        """

    async def update_workspace_alias(
        self, *, workspaceId: str, alias: str = ..., clientToken: str = ...
    ) -> EmptyResponseMetadataTypeDef:
        """
        Updates an AMP workspace alias.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp.html#PrometheusService.Client.update_workspace_alias)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amp/client/#update_workspace_alias)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_rule_groups_namespaces"]
    ) -> ListRuleGroupsNamespacesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp.html#PrometheusService.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amp/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_scrapers"]) -> ListScrapersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp.html#PrometheusService.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amp/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_workspaces"]) -> ListWorkspacesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp.html#PrometheusService.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amp/client/#get_paginator)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["scraper_active"]) -> ScraperActiveWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp.html#PrometheusService.Client.get_waiter)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amp/client/#get_waiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["scraper_deleted"]) -> ScraperDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp.html#PrometheusService.Client.get_waiter)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amp/client/#get_waiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["workspace_active"]) -> WorkspaceActiveWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp.html#PrometheusService.Client.get_waiter)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amp/client/#get_waiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["workspace_deleted"]) -> WorkspaceDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp.html#PrometheusService.Client.get_waiter)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amp/client/#get_waiter)
        """

    async def __aenter__(self) -> "PrometheusServiceClient":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp.html#PrometheusService.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amp/client/)
        """

    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> Any:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp.html#PrometheusService.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amp/client/)
        """
