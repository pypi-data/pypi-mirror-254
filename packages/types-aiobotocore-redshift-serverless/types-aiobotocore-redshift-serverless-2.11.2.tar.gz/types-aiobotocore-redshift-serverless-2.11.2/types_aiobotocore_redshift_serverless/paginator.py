"""
Type annotations for redshift-serverless service client paginators.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_redshift_serverless/paginators/)

Usage::

    ```python
    from aiobotocore.session import get_session

    from types_aiobotocore_redshift_serverless.client import RedshiftServerlessClient
    from types_aiobotocore_redshift_serverless.paginator import (
        ListCustomDomainAssociationsPaginator,
        ListEndpointAccessPaginator,
        ListNamespacesPaginator,
        ListRecoveryPointsPaginator,
        ListScheduledActionsPaginator,
        ListSnapshotCopyConfigurationsPaginator,
        ListSnapshotsPaginator,
        ListTableRestoreStatusPaginator,
        ListUsageLimitsPaginator,
        ListWorkgroupsPaginator,
    )

    session = get_session()
    with session.create_client("redshift-serverless") as client:
        client: RedshiftServerlessClient

        list_custom_domain_associations_paginator: ListCustomDomainAssociationsPaginator = client.get_paginator("list_custom_domain_associations")
        list_endpoint_access_paginator: ListEndpointAccessPaginator = client.get_paginator("list_endpoint_access")
        list_namespaces_paginator: ListNamespacesPaginator = client.get_paginator("list_namespaces")
        list_recovery_points_paginator: ListRecoveryPointsPaginator = client.get_paginator("list_recovery_points")
        list_scheduled_actions_paginator: ListScheduledActionsPaginator = client.get_paginator("list_scheduled_actions")
        list_snapshot_copy_configurations_paginator: ListSnapshotCopyConfigurationsPaginator = client.get_paginator("list_snapshot_copy_configurations")
        list_snapshots_paginator: ListSnapshotsPaginator = client.get_paginator("list_snapshots")
        list_table_restore_status_paginator: ListTableRestoreStatusPaginator = client.get_paginator("list_table_restore_status")
        list_usage_limits_paginator: ListUsageLimitsPaginator = client.get_paginator("list_usage_limits")
        list_workgroups_paginator: ListWorkgroupsPaginator = client.get_paginator("list_workgroups")
    ```
"""

from typing import AsyncIterator, Generic, Iterator, TypeVar

from aiobotocore.paginate import AioPaginator
from botocore.paginate import PageIterator

from .literals import UsageLimitUsageTypeType
from .type_defs import (
    ListCustomDomainAssociationsResponseTypeDef,
    ListEndpointAccessResponseTypeDef,
    ListNamespacesResponseTypeDef,
    ListRecoveryPointsResponseTypeDef,
    ListScheduledActionsResponseTypeDef,
    ListSnapshotCopyConfigurationsResponseTypeDef,
    ListSnapshotsResponseTypeDef,
    ListTableRestoreStatusResponseTypeDef,
    ListUsageLimitsResponseTypeDef,
    ListWorkgroupsResponseTypeDef,
    PaginatorConfigTypeDef,
    TimestampTypeDef,
)

__all__ = (
    "ListCustomDomainAssociationsPaginator",
    "ListEndpointAccessPaginator",
    "ListNamespacesPaginator",
    "ListRecoveryPointsPaginator",
    "ListScheduledActionsPaginator",
    "ListSnapshotCopyConfigurationsPaginator",
    "ListSnapshotsPaginator",
    "ListTableRestoreStatusPaginator",
    "ListUsageLimitsPaginator",
    "ListWorkgroupsPaginator",
)

_ItemTypeDef = TypeVar("_ItemTypeDef")


class _PageIterator(Generic[_ItemTypeDef], PageIterator):
    def __iter__(self) -> Iterator[_ItemTypeDef]:
        """
        Proxy method to specify iterator item type.
        """


class ListCustomDomainAssociationsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless.html#RedshiftServerless.Paginator.ListCustomDomainAssociations)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_redshift_serverless/paginators/#listcustomdomainassociationspaginator)
    """

    def paginate(
        self,
        *,
        customDomainCertificateArn: str = ...,
        customDomainName: str = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListCustomDomainAssociationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless.html#RedshiftServerless.Paginator.ListCustomDomainAssociations.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_redshift_serverless/paginators/#listcustomdomainassociationspaginator)
        """


class ListEndpointAccessPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless.html#RedshiftServerless.Paginator.ListEndpointAccess)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_redshift_serverless/paginators/#listendpointaccesspaginator)
    """

    def paginate(
        self,
        *,
        ownerAccount: str = ...,
        vpcId: str = ...,
        workgroupName: str = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListEndpointAccessResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless.html#RedshiftServerless.Paginator.ListEndpointAccess.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_redshift_serverless/paginators/#listendpointaccesspaginator)
        """


class ListNamespacesPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless.html#RedshiftServerless.Paginator.ListNamespaces)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_redshift_serverless/paginators/#listnamespacespaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListNamespacesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless.html#RedshiftServerless.Paginator.ListNamespaces.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_redshift_serverless/paginators/#listnamespacespaginator)
        """


class ListRecoveryPointsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless.html#RedshiftServerless.Paginator.ListRecoveryPoints)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_redshift_serverless/paginators/#listrecoverypointspaginator)
    """

    def paginate(
        self,
        *,
        endTime: TimestampTypeDef = ...,
        namespaceArn: str = ...,
        namespaceName: str = ...,
        startTime: TimestampTypeDef = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListRecoveryPointsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless.html#RedshiftServerless.Paginator.ListRecoveryPoints.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_redshift_serverless/paginators/#listrecoverypointspaginator)
        """


class ListScheduledActionsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless.html#RedshiftServerless.Paginator.ListScheduledActions)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_redshift_serverless/paginators/#listscheduledactionspaginator)
    """

    def paginate(
        self, *, namespaceName: str = ..., PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListScheduledActionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless.html#RedshiftServerless.Paginator.ListScheduledActions.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_redshift_serverless/paginators/#listscheduledactionspaginator)
        """


class ListSnapshotCopyConfigurationsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless.html#RedshiftServerless.Paginator.ListSnapshotCopyConfigurations)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_redshift_serverless/paginators/#listsnapshotcopyconfigurationspaginator)
    """

    def paginate(
        self, *, namespaceName: str = ..., PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListSnapshotCopyConfigurationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless.html#RedshiftServerless.Paginator.ListSnapshotCopyConfigurations.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_redshift_serverless/paginators/#listsnapshotcopyconfigurationspaginator)
        """


class ListSnapshotsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless.html#RedshiftServerless.Paginator.ListSnapshots)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_redshift_serverless/paginators/#listsnapshotspaginator)
    """

    def paginate(
        self,
        *,
        endTime: TimestampTypeDef = ...,
        namespaceArn: str = ...,
        namespaceName: str = ...,
        ownerAccount: str = ...,
        startTime: TimestampTypeDef = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListSnapshotsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless.html#RedshiftServerless.Paginator.ListSnapshots.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_redshift_serverless/paginators/#listsnapshotspaginator)
        """


class ListTableRestoreStatusPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless.html#RedshiftServerless.Paginator.ListTableRestoreStatus)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_redshift_serverless/paginators/#listtablerestorestatuspaginator)
    """

    def paginate(
        self,
        *,
        namespaceName: str = ...,
        workgroupName: str = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListTableRestoreStatusResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless.html#RedshiftServerless.Paginator.ListTableRestoreStatus.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_redshift_serverless/paginators/#listtablerestorestatuspaginator)
        """


class ListUsageLimitsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless.html#RedshiftServerless.Paginator.ListUsageLimits)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_redshift_serverless/paginators/#listusagelimitspaginator)
    """

    def paginate(
        self,
        *,
        resourceArn: str = ...,
        usageType: UsageLimitUsageTypeType = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListUsageLimitsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless.html#RedshiftServerless.Paginator.ListUsageLimits.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_redshift_serverless/paginators/#listusagelimitspaginator)
        """


class ListWorkgroupsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless.html#RedshiftServerless.Paginator.ListWorkgroups)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_redshift_serverless/paginators/#listworkgroupspaginator)
    """

    def paginate(
        self, *, ownerAccount: str = ..., PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListWorkgroupsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless.html#RedshiftServerless.Paginator.ListWorkgroups.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_redshift_serverless/paginators/#listworkgroupspaginator)
        """
