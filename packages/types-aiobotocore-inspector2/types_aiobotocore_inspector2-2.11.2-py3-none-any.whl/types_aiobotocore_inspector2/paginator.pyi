"""
Type annotations for inspector2 service client paginators.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/paginators/)

Usage::

    ```python
    from aiobotocore.session import get_session

    from types_aiobotocore_inspector2.client import Inspector2Client
    from types_aiobotocore_inspector2.paginator import (
        GetCisScanResultDetailsPaginator,
        ListAccountPermissionsPaginator,
        ListCisScanConfigurationsPaginator,
        ListCisScanResultsAggregatedByChecksPaginator,
        ListCisScanResultsAggregatedByTargetResourcePaginator,
        ListCisScansPaginator,
        ListCoveragePaginator,
        ListCoverageStatisticsPaginator,
        ListDelegatedAdminAccountsPaginator,
        ListFiltersPaginator,
        ListFindingAggregationsPaginator,
        ListFindingsPaginator,
        ListMembersPaginator,
        ListUsageTotalsPaginator,
        SearchVulnerabilitiesPaginator,
    )

    session = get_session()
    with session.create_client("inspector2") as client:
        client: Inspector2Client

        get_cis_scan_result_details_paginator: GetCisScanResultDetailsPaginator = client.get_paginator("get_cis_scan_result_details")
        list_account_permissions_paginator: ListAccountPermissionsPaginator = client.get_paginator("list_account_permissions")
        list_cis_scan_configurations_paginator: ListCisScanConfigurationsPaginator = client.get_paginator("list_cis_scan_configurations")
        list_cis_scan_results_aggregated_by_checks_paginator: ListCisScanResultsAggregatedByChecksPaginator = client.get_paginator("list_cis_scan_results_aggregated_by_checks")
        list_cis_scan_results_aggregated_by_target_resource_paginator: ListCisScanResultsAggregatedByTargetResourcePaginator = client.get_paginator("list_cis_scan_results_aggregated_by_target_resource")
        list_cis_scans_paginator: ListCisScansPaginator = client.get_paginator("list_cis_scans")
        list_coverage_paginator: ListCoveragePaginator = client.get_paginator("list_coverage")
        list_coverage_statistics_paginator: ListCoverageStatisticsPaginator = client.get_paginator("list_coverage_statistics")
        list_delegated_admin_accounts_paginator: ListDelegatedAdminAccountsPaginator = client.get_paginator("list_delegated_admin_accounts")
        list_filters_paginator: ListFiltersPaginator = client.get_paginator("list_filters")
        list_finding_aggregations_paginator: ListFindingAggregationsPaginator = client.get_paginator("list_finding_aggregations")
        list_findings_paginator: ListFindingsPaginator = client.get_paginator("list_findings")
        list_members_paginator: ListMembersPaginator = client.get_paginator("list_members")
        list_usage_totals_paginator: ListUsageTotalsPaginator = client.get_paginator("list_usage_totals")
        search_vulnerabilities_paginator: SearchVulnerabilitiesPaginator = client.get_paginator("search_vulnerabilities")
    ```
"""

from typing import AsyncIterator, Generic, Iterator, Sequence, TypeVar

from aiobotocore.paginate import AioPaginator
from botocore.paginate import PageIterator

from .literals import (
    AggregationTypeType,
    CisScanConfigurationsSortByType,
    CisScanResultDetailsSortByType,
    CisScanResultsAggregatedByChecksSortByType,
    CisScanResultsAggregatedByTargetResourceSortByType,
    CisSortOrderType,
    FilterActionType,
    GroupKeyType,
    ListCisScansDetailLevelType,
    ListCisScansSortByType,
    ServiceType,
)
from .type_defs import (
    AggregationRequestTypeDef,
    CisScanResultDetailsFilterCriteriaTypeDef,
    CisScanResultsAggregatedByChecksFilterCriteriaTypeDef,
    CisScanResultsAggregatedByTargetResourceFilterCriteriaTypeDef,
    CoverageFilterCriteriaTypeDef,
    FilterCriteriaPaginatorTypeDef,
    GetCisScanResultDetailsResponseTypeDef,
    ListAccountPermissionsResponseTypeDef,
    ListCisScanConfigurationsFilterCriteriaTypeDef,
    ListCisScanConfigurationsResponsePaginatorTypeDef,
    ListCisScanResultsAggregatedByChecksResponseTypeDef,
    ListCisScanResultsAggregatedByTargetResourceResponseTypeDef,
    ListCisScansFilterCriteriaTypeDef,
    ListCisScansResponseTypeDef,
    ListCoverageResponseTypeDef,
    ListCoverageStatisticsResponseTypeDef,
    ListDelegatedAdminAccountsResponseTypeDef,
    ListFiltersResponsePaginatorTypeDef,
    ListFindingAggregationsResponseTypeDef,
    ListFindingsResponseTypeDef,
    ListMembersResponseTypeDef,
    ListUsageTotalsResponseTypeDef,
    PaginatorConfigTypeDef,
    SearchVulnerabilitiesFilterCriteriaTypeDef,
    SearchVulnerabilitiesResponseTypeDef,
    SortCriteriaTypeDef,
    StringFilterTypeDef,
)

__all__ = (
    "GetCisScanResultDetailsPaginator",
    "ListAccountPermissionsPaginator",
    "ListCisScanConfigurationsPaginator",
    "ListCisScanResultsAggregatedByChecksPaginator",
    "ListCisScanResultsAggregatedByTargetResourcePaginator",
    "ListCisScansPaginator",
    "ListCoveragePaginator",
    "ListCoverageStatisticsPaginator",
    "ListDelegatedAdminAccountsPaginator",
    "ListFiltersPaginator",
    "ListFindingAggregationsPaginator",
    "ListFindingsPaginator",
    "ListMembersPaginator",
    "ListUsageTotalsPaginator",
    "SearchVulnerabilitiesPaginator",
)

_ItemTypeDef = TypeVar("_ItemTypeDef")

class _PageIterator(Generic[_ItemTypeDef], PageIterator):
    def __iter__(self) -> Iterator[_ItemTypeDef]:
        """
        Proxy method to specify iterator item type.
        """

class GetCisScanResultDetailsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Paginator.GetCisScanResultDetails)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/paginators/#getcisscanresultdetailspaginator)
    """

    def paginate(
        self,
        *,
        accountId: str,
        scanArn: str,
        targetResourceId: str,
        filterCriteria: CisScanResultDetailsFilterCriteriaTypeDef = ...,
        sortBy: CisScanResultDetailsSortByType = ...,
        sortOrder: CisSortOrderType = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[GetCisScanResultDetailsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Paginator.GetCisScanResultDetails.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/paginators/#getcisscanresultdetailspaginator)
        """

class ListAccountPermissionsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Paginator.ListAccountPermissions)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/paginators/#listaccountpermissionspaginator)
    """

    def paginate(
        self, *, service: ServiceType = ..., PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListAccountPermissionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Paginator.ListAccountPermissions.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/paginators/#listaccountpermissionspaginator)
        """

class ListCisScanConfigurationsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Paginator.ListCisScanConfigurations)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/paginators/#listcisscanconfigurationspaginator)
    """

    def paginate(
        self,
        *,
        filterCriteria: ListCisScanConfigurationsFilterCriteriaTypeDef = ...,
        sortBy: CisScanConfigurationsSortByType = ...,
        sortOrder: CisSortOrderType = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListCisScanConfigurationsResponsePaginatorTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Paginator.ListCisScanConfigurations.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/paginators/#listcisscanconfigurationspaginator)
        """

class ListCisScanResultsAggregatedByChecksPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Paginator.ListCisScanResultsAggregatedByChecks)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/paginators/#listcisscanresultsaggregatedbycheckspaginator)
    """

    def paginate(
        self,
        *,
        scanArn: str,
        filterCriteria: CisScanResultsAggregatedByChecksFilterCriteriaTypeDef = ...,
        sortBy: CisScanResultsAggregatedByChecksSortByType = ...,
        sortOrder: CisSortOrderType = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListCisScanResultsAggregatedByChecksResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Paginator.ListCisScanResultsAggregatedByChecks.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/paginators/#listcisscanresultsaggregatedbycheckspaginator)
        """

class ListCisScanResultsAggregatedByTargetResourcePaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Paginator.ListCisScanResultsAggregatedByTargetResource)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/paginators/#listcisscanresultsaggregatedbytargetresourcepaginator)
    """

    def paginate(
        self,
        *,
        scanArn: str,
        filterCriteria: CisScanResultsAggregatedByTargetResourceFilterCriteriaTypeDef = ...,
        sortBy: CisScanResultsAggregatedByTargetResourceSortByType = ...,
        sortOrder: CisSortOrderType = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListCisScanResultsAggregatedByTargetResourceResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Paginator.ListCisScanResultsAggregatedByTargetResource.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/paginators/#listcisscanresultsaggregatedbytargetresourcepaginator)
        """

class ListCisScansPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Paginator.ListCisScans)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/paginators/#listcisscanspaginator)
    """

    def paginate(
        self,
        *,
        detailLevel: ListCisScansDetailLevelType = ...,
        filterCriteria: ListCisScansFilterCriteriaTypeDef = ...,
        sortBy: ListCisScansSortByType = ...,
        sortOrder: CisSortOrderType = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListCisScansResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Paginator.ListCisScans.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/paginators/#listcisscanspaginator)
        """

class ListCoveragePaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Paginator.ListCoverage)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/paginators/#listcoveragepaginator)
    """

    def paginate(
        self,
        *,
        filterCriteria: CoverageFilterCriteriaTypeDef = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListCoverageResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Paginator.ListCoverage.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/paginators/#listcoveragepaginator)
        """

class ListCoverageStatisticsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Paginator.ListCoverageStatistics)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/paginators/#listcoveragestatisticspaginator)
    """

    def paginate(
        self,
        *,
        filterCriteria: CoverageFilterCriteriaTypeDef = ...,
        groupBy: GroupKeyType = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListCoverageStatisticsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Paginator.ListCoverageStatistics.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/paginators/#listcoveragestatisticspaginator)
        """

class ListDelegatedAdminAccountsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Paginator.ListDelegatedAdminAccounts)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/paginators/#listdelegatedadminaccountspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListDelegatedAdminAccountsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Paginator.ListDelegatedAdminAccounts.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/paginators/#listdelegatedadminaccountspaginator)
        """

class ListFiltersPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Paginator.ListFilters)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/paginators/#listfilterspaginator)
    """

    def paginate(
        self,
        *,
        action: FilterActionType = ...,
        arns: Sequence[str] = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListFiltersResponsePaginatorTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Paginator.ListFilters.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/paginators/#listfilterspaginator)
        """

class ListFindingAggregationsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Paginator.ListFindingAggregations)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/paginators/#listfindingaggregationspaginator)
    """

    def paginate(
        self,
        *,
        aggregationType: AggregationTypeType,
        accountIds: Sequence[StringFilterTypeDef] = ...,
        aggregationRequest: AggregationRequestTypeDef = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListFindingAggregationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Paginator.ListFindingAggregations.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/paginators/#listfindingaggregationspaginator)
        """

class ListFindingsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Paginator.ListFindings)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/paginators/#listfindingspaginator)
    """

    def paginate(
        self,
        *,
        filterCriteria: FilterCriteriaPaginatorTypeDef = ...,
        sortCriteria: SortCriteriaTypeDef = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListFindingsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Paginator.ListFindings.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/paginators/#listfindingspaginator)
        """

class ListMembersPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Paginator.ListMembers)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/paginators/#listmemberspaginator)
    """

    def paginate(
        self, *, onlyAssociated: bool = ..., PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListMembersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Paginator.ListMembers.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/paginators/#listmemberspaginator)
        """

class ListUsageTotalsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Paginator.ListUsageTotals)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/paginators/#listusagetotalspaginator)
    """

    def paginate(
        self, *, accountIds: Sequence[str] = ..., PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListUsageTotalsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Paginator.ListUsageTotals.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/paginators/#listusagetotalspaginator)
        """

class SearchVulnerabilitiesPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Paginator.SearchVulnerabilities)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/paginators/#searchvulnerabilitiespaginator)
    """

    def paginate(
        self,
        *,
        filterCriteria: SearchVulnerabilitiesFilterCriteriaTypeDef,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[SearchVulnerabilitiesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Paginator.SearchVulnerabilities.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/paginators/#searchvulnerabilitiespaginator)
        """
