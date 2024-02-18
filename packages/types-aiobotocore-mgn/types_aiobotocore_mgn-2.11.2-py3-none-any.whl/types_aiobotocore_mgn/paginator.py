"""
Type annotations for mgn service client paginators.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mgn/paginators/)

Usage::

    ```python
    from aiobotocore.session import get_session

    from types_aiobotocore_mgn.client import mgnClient
    from types_aiobotocore_mgn.paginator import (
        DescribeJobLogItemsPaginator,
        DescribeJobsPaginator,
        DescribeLaunchConfigurationTemplatesPaginator,
        DescribeReplicationConfigurationTemplatesPaginator,
        DescribeSourceServersPaginator,
        DescribeVcenterClientsPaginator,
        ListApplicationsPaginator,
        ListConnectorsPaginator,
        ListExportErrorsPaginator,
        ListExportsPaginator,
        ListImportErrorsPaginator,
        ListImportsPaginator,
        ListManagedAccountsPaginator,
        ListSourceServerActionsPaginator,
        ListTemplateActionsPaginator,
        ListWavesPaginator,
    )

    session = get_session()
    with session.create_client("mgn") as client:
        client: mgnClient

        describe_job_log_items_paginator: DescribeJobLogItemsPaginator = client.get_paginator("describe_job_log_items")
        describe_jobs_paginator: DescribeJobsPaginator = client.get_paginator("describe_jobs")
        describe_launch_configuration_templates_paginator: DescribeLaunchConfigurationTemplatesPaginator = client.get_paginator("describe_launch_configuration_templates")
        describe_replication_configuration_templates_paginator: DescribeReplicationConfigurationTemplatesPaginator = client.get_paginator("describe_replication_configuration_templates")
        describe_source_servers_paginator: DescribeSourceServersPaginator = client.get_paginator("describe_source_servers")
        describe_vcenter_clients_paginator: DescribeVcenterClientsPaginator = client.get_paginator("describe_vcenter_clients")
        list_applications_paginator: ListApplicationsPaginator = client.get_paginator("list_applications")
        list_connectors_paginator: ListConnectorsPaginator = client.get_paginator("list_connectors")
        list_export_errors_paginator: ListExportErrorsPaginator = client.get_paginator("list_export_errors")
        list_exports_paginator: ListExportsPaginator = client.get_paginator("list_exports")
        list_import_errors_paginator: ListImportErrorsPaginator = client.get_paginator("list_import_errors")
        list_imports_paginator: ListImportsPaginator = client.get_paginator("list_imports")
        list_managed_accounts_paginator: ListManagedAccountsPaginator = client.get_paginator("list_managed_accounts")
        list_source_server_actions_paginator: ListSourceServerActionsPaginator = client.get_paginator("list_source_server_actions")
        list_template_actions_paginator: ListTemplateActionsPaginator = client.get_paginator("list_template_actions")
        list_waves_paginator: ListWavesPaginator = client.get_paginator("list_waves")
    ```
"""

from typing import AsyncIterator, Generic, Iterator, Sequence, TypeVar

from aiobotocore.paginate import AioPaginator
from botocore.paginate import PageIterator

from .type_defs import (
    DescribeJobLogItemsResponseTypeDef,
    DescribeJobsRequestFiltersTypeDef,
    DescribeJobsResponsePaginatorTypeDef,
    DescribeLaunchConfigurationTemplatesResponsePaginatorTypeDef,
    DescribeReplicationConfigurationTemplatesResponseTypeDef,
    DescribeSourceServersRequestFiltersTypeDef,
    DescribeSourceServersResponseTypeDef,
    DescribeVcenterClientsResponseTypeDef,
    ListApplicationsRequestFiltersTypeDef,
    ListApplicationsResponseTypeDef,
    ListConnectorsRequestFiltersTypeDef,
    ListConnectorsResponseTypeDef,
    ListExportErrorsResponseTypeDef,
    ListExportsRequestFiltersTypeDef,
    ListExportsResponseTypeDef,
    ListImportErrorsResponseTypeDef,
    ListImportsRequestFiltersTypeDef,
    ListImportsResponseTypeDef,
    ListManagedAccountsResponseTypeDef,
    ListSourceServerActionsResponseTypeDef,
    ListTemplateActionsResponseTypeDef,
    ListWavesRequestFiltersTypeDef,
    ListWavesResponseTypeDef,
    PaginatorConfigTypeDef,
    SourceServerActionsRequestFiltersTypeDef,
    TemplateActionsRequestFiltersTypeDef,
)

__all__ = (
    "DescribeJobLogItemsPaginator",
    "DescribeJobsPaginator",
    "DescribeLaunchConfigurationTemplatesPaginator",
    "DescribeReplicationConfigurationTemplatesPaginator",
    "DescribeSourceServersPaginator",
    "DescribeVcenterClientsPaginator",
    "ListApplicationsPaginator",
    "ListConnectorsPaginator",
    "ListExportErrorsPaginator",
    "ListExportsPaginator",
    "ListImportErrorsPaginator",
    "ListImportsPaginator",
    "ListManagedAccountsPaginator",
    "ListSourceServerActionsPaginator",
    "ListTemplateActionsPaginator",
    "ListWavesPaginator",
)

_ItemTypeDef = TypeVar("_ItemTypeDef")


class _PageIterator(Generic[_ItemTypeDef], PageIterator):
    def __iter__(self) -> Iterator[_ItemTypeDef]:
        """
        Proxy method to specify iterator item type.
        """


class DescribeJobLogItemsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgn.html#mgn.Paginator.DescribeJobLogItems)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mgn/paginators/#describejoblogitemspaginator)
    """

    def paginate(
        self, *, jobID: str, accountID: str = ..., PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[DescribeJobLogItemsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgn.html#mgn.Paginator.DescribeJobLogItems.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mgn/paginators/#describejoblogitemspaginator)
        """


class DescribeJobsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgn.html#mgn.Paginator.DescribeJobs)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mgn/paginators/#describejobspaginator)
    """

    def paginate(
        self,
        *,
        accountID: str = ...,
        filters: DescribeJobsRequestFiltersTypeDef = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[DescribeJobsResponsePaginatorTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgn.html#mgn.Paginator.DescribeJobs.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mgn/paginators/#describejobspaginator)
        """


class DescribeLaunchConfigurationTemplatesPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgn.html#mgn.Paginator.DescribeLaunchConfigurationTemplates)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mgn/paginators/#describelaunchconfigurationtemplatespaginator)
    """

    def paginate(
        self,
        *,
        launchConfigurationTemplateIDs: Sequence[str] = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[DescribeLaunchConfigurationTemplatesResponsePaginatorTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgn.html#mgn.Paginator.DescribeLaunchConfigurationTemplates.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mgn/paginators/#describelaunchconfigurationtemplatespaginator)
        """


class DescribeReplicationConfigurationTemplatesPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgn.html#mgn.Paginator.DescribeReplicationConfigurationTemplates)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mgn/paginators/#describereplicationconfigurationtemplatespaginator)
    """

    def paginate(
        self,
        *,
        replicationConfigurationTemplateIDs: Sequence[str] = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[DescribeReplicationConfigurationTemplatesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgn.html#mgn.Paginator.DescribeReplicationConfigurationTemplates.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mgn/paginators/#describereplicationconfigurationtemplatespaginator)
        """


class DescribeSourceServersPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgn.html#mgn.Paginator.DescribeSourceServers)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mgn/paginators/#describesourceserverspaginator)
    """

    def paginate(
        self,
        *,
        accountID: str = ...,
        filters: DescribeSourceServersRequestFiltersTypeDef = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[DescribeSourceServersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgn.html#mgn.Paginator.DescribeSourceServers.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mgn/paginators/#describesourceserverspaginator)
        """


class DescribeVcenterClientsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgn.html#mgn.Paginator.DescribeVcenterClients)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mgn/paginators/#describevcenterclientspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[DescribeVcenterClientsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgn.html#mgn.Paginator.DescribeVcenterClients.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mgn/paginators/#describevcenterclientspaginator)
        """


class ListApplicationsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgn.html#mgn.Paginator.ListApplications)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mgn/paginators/#listapplicationspaginator)
    """

    def paginate(
        self,
        *,
        accountID: str = ...,
        filters: ListApplicationsRequestFiltersTypeDef = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListApplicationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgn.html#mgn.Paginator.ListApplications.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mgn/paginators/#listapplicationspaginator)
        """


class ListConnectorsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgn.html#mgn.Paginator.ListConnectors)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mgn/paginators/#listconnectorspaginator)
    """

    def paginate(
        self,
        *,
        filters: ListConnectorsRequestFiltersTypeDef = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListConnectorsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgn.html#mgn.Paginator.ListConnectors.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mgn/paginators/#listconnectorspaginator)
        """


class ListExportErrorsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgn.html#mgn.Paginator.ListExportErrors)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mgn/paginators/#listexporterrorspaginator)
    """

    def paginate(
        self, *, exportID: str, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListExportErrorsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgn.html#mgn.Paginator.ListExportErrors.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mgn/paginators/#listexporterrorspaginator)
        """


class ListExportsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgn.html#mgn.Paginator.ListExports)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mgn/paginators/#listexportspaginator)
    """

    def paginate(
        self,
        *,
        filters: ListExportsRequestFiltersTypeDef = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListExportsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgn.html#mgn.Paginator.ListExports.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mgn/paginators/#listexportspaginator)
        """


class ListImportErrorsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgn.html#mgn.Paginator.ListImportErrors)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mgn/paginators/#listimporterrorspaginator)
    """

    def paginate(
        self, *, importID: str, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListImportErrorsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgn.html#mgn.Paginator.ListImportErrors.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mgn/paginators/#listimporterrorspaginator)
        """


class ListImportsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgn.html#mgn.Paginator.ListImports)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mgn/paginators/#listimportspaginator)
    """

    def paginate(
        self,
        *,
        filters: ListImportsRequestFiltersTypeDef = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListImportsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgn.html#mgn.Paginator.ListImports.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mgn/paginators/#listimportspaginator)
        """


class ListManagedAccountsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgn.html#mgn.Paginator.ListManagedAccounts)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mgn/paginators/#listmanagedaccountspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListManagedAccountsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgn.html#mgn.Paginator.ListManagedAccounts.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mgn/paginators/#listmanagedaccountspaginator)
        """


class ListSourceServerActionsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgn.html#mgn.Paginator.ListSourceServerActions)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mgn/paginators/#listsourceserveractionspaginator)
    """

    def paginate(
        self,
        *,
        sourceServerID: str,
        accountID: str = ...,
        filters: SourceServerActionsRequestFiltersTypeDef = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListSourceServerActionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgn.html#mgn.Paginator.ListSourceServerActions.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mgn/paginators/#listsourceserveractionspaginator)
        """


class ListTemplateActionsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgn.html#mgn.Paginator.ListTemplateActions)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mgn/paginators/#listtemplateactionspaginator)
    """

    def paginate(
        self,
        *,
        launchConfigurationTemplateID: str,
        filters: TemplateActionsRequestFiltersTypeDef = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListTemplateActionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgn.html#mgn.Paginator.ListTemplateActions.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mgn/paginators/#listtemplateactionspaginator)
        """


class ListWavesPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgn.html#mgn.Paginator.ListWaves)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mgn/paginators/#listwavespaginator)
    """

    def paginate(
        self,
        *,
        accountID: str = ...,
        filters: ListWavesRequestFiltersTypeDef = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListWavesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgn.html#mgn.Paginator.ListWaves.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mgn/paginators/#listwavespaginator)
        """
