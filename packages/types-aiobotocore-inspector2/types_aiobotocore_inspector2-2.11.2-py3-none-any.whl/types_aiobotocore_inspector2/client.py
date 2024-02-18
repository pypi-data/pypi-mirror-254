"""
Type annotations for inspector2 service client.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/)

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_inspector2.client import Inspector2Client

    session = get_session()
    async with session.create_client("inspector2") as client:
        client: Inspector2Client
    ```
"""

import sys
from typing import Any, Dict, Mapping, Sequence, Type, overload

from aiobotocore.client import AioBaseClient
from botocore.client import ClientMeta

from .literals import (
    AggregationTypeType,
    CisScanConfigurationsSortByType,
    CisScanResultDetailsSortByType,
    CisScanResultsAggregatedByChecksSortByType,
    CisScanResultsAggregatedByTargetResourceSortByType,
    CisSecurityLevelType,
    CisSortOrderType,
    FilterActionType,
    GroupKeyType,
    ListCisScansDetailLevelType,
    ListCisScansSortByType,
    ReportFormatType,
    ResourceScanTypeType,
    ResourceTypeType,
    SbomReportFormatType,
    ScanTypeType,
    ServiceType,
)
from .paginator import (
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
from .type_defs import (
    AggregationRequestTypeDef,
    AssociateMemberResponseTypeDef,
    AutoEnableTypeDef,
    BatchGetAccountStatusResponseTypeDef,
    BatchGetCodeSnippetResponseTypeDef,
    BatchGetFindingDetailsResponseTypeDef,
    BatchGetFreeTrialInfoResponseTypeDef,
    BatchGetMemberEc2DeepInspectionStatusResponseTypeDef,
    BatchUpdateMemberEc2DeepInspectionStatusResponseTypeDef,
    CancelFindingsReportResponseTypeDef,
    CancelSbomExportResponseTypeDef,
    CisScanResultDetailsFilterCriteriaTypeDef,
    CisScanResultsAggregatedByChecksFilterCriteriaTypeDef,
    CisScanResultsAggregatedByTargetResourceFilterCriteriaTypeDef,
    CisSessionMessageTypeDef,
    CoverageFilterCriteriaTypeDef,
    CreateCisScanConfigurationResponseTypeDef,
    CreateCisTargetsTypeDef,
    CreateFilterResponseTypeDef,
    CreateFindingsReportResponseTypeDef,
    CreateSbomExportResponseTypeDef,
    DeleteCisScanConfigurationResponseTypeDef,
    DeleteFilterResponseTypeDef,
    DescribeOrganizationConfigurationResponseTypeDef,
    DestinationTypeDef,
    DisableDelegatedAdminAccountResponseTypeDef,
    DisableResponseTypeDef,
    DisassociateMemberResponseTypeDef,
    EcrConfigurationTypeDef,
    EnableDelegatedAdminAccountResponseTypeDef,
    EnableResponseTypeDef,
    FilterCriteriaTypeDef,
    GetCisScanReportResponseTypeDef,
    GetCisScanResultDetailsResponseTypeDef,
    GetConfigurationResponseTypeDef,
    GetDelegatedAdminAccountResponseTypeDef,
    GetEc2DeepInspectionConfigurationResponseTypeDef,
    GetEncryptionKeyResponseTypeDef,
    GetFindingsReportStatusResponseTypeDef,
    GetMemberResponseTypeDef,
    GetSbomExportResponseTypeDef,
    ListAccountPermissionsResponseTypeDef,
    ListCisScanConfigurationsFilterCriteriaTypeDef,
    ListCisScanConfigurationsResponseTypeDef,
    ListCisScanResultsAggregatedByChecksResponseTypeDef,
    ListCisScanResultsAggregatedByTargetResourceResponseTypeDef,
    ListCisScansFilterCriteriaTypeDef,
    ListCisScansResponseTypeDef,
    ListCoverageResponseTypeDef,
    ListCoverageStatisticsResponseTypeDef,
    ListDelegatedAdminAccountsResponseTypeDef,
    ListFiltersResponseTypeDef,
    ListFindingAggregationsResponseTypeDef,
    ListFindingsResponseTypeDef,
    ListMembersResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListUsageTotalsResponseTypeDef,
    MemberAccountEc2DeepInspectionStatusTypeDef,
    ResourceFilterCriteriaTypeDef,
    ScheduleTypeDef,
    SearchVulnerabilitiesFilterCriteriaTypeDef,
    SearchVulnerabilitiesResponseTypeDef,
    SortCriteriaTypeDef,
    StartCisSessionMessageTypeDef,
    StopCisSessionMessageTypeDef,
    StringFilterTypeDef,
    UpdateCisScanConfigurationResponseTypeDef,
    UpdateCisTargetsTypeDef,
    UpdateEc2DeepInspectionConfigurationResponseTypeDef,
    UpdateFilterResponseTypeDef,
    UpdateOrganizationConfigurationResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("Inspector2Client",)


class BotocoreClientError(Exception):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    BadRequestException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class Inspector2Client(AioBaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        Inspector2Client exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.exceptions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#exceptions)
        """

    async def associate_member(self, *, accountId: str) -> AssociateMemberResponseTypeDef:
        """
        Associates an Amazon Web Services account with an Amazon Inspector delegated
        administrator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.associate_member)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#associate_member)
        """

    async def batch_get_account_status(
        self, *, accountIds: Sequence[str] = ...
    ) -> BatchGetAccountStatusResponseTypeDef:
        """
        Retrieves the Amazon Inspector status of multiple Amazon Web Services accounts
        within your
        environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.batch_get_account_status)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#batch_get_account_status)
        """

    async def batch_get_code_snippet(
        self, *, findingArns: Sequence[str]
    ) -> BatchGetCodeSnippetResponseTypeDef:
        """
        Retrieves code snippets from findings that Amazon Inspector detected code
        vulnerabilities
        in.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.batch_get_code_snippet)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#batch_get_code_snippet)
        """

    async def batch_get_finding_details(
        self, *, findingArns: Sequence[str]
    ) -> BatchGetFindingDetailsResponseTypeDef:
        """
        Gets vulnerability details for findings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.batch_get_finding_details)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#batch_get_finding_details)
        """

    async def batch_get_free_trial_info(
        self, *, accountIds: Sequence[str]
    ) -> BatchGetFreeTrialInfoResponseTypeDef:
        """
        Gets free trial status for multiple Amazon Web Services accounts.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.batch_get_free_trial_info)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#batch_get_free_trial_info)
        """

    async def batch_get_member_ec2_deep_inspection_status(
        self, *, accountIds: Sequence[str] = ...
    ) -> BatchGetMemberEc2DeepInspectionStatusResponseTypeDef:
        """
        Retrieves Amazon Inspector deep inspection activation status of multiple member
        accounts within your
        organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.batch_get_member_ec2_deep_inspection_status)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#batch_get_member_ec2_deep_inspection_status)
        """

    async def batch_update_member_ec2_deep_inspection_status(
        self, *, accountIds: Sequence[MemberAccountEc2DeepInspectionStatusTypeDef]
    ) -> BatchUpdateMemberEc2DeepInspectionStatusResponseTypeDef:
        """
        Activates or deactivates Amazon Inspector deep inspection for the provided
        member accounts in your
        organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.batch_update_member_ec2_deep_inspection_status)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#batch_update_member_ec2_deep_inspection_status)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.can_paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#can_paginate)
        """

    async def cancel_findings_report(self, *, reportId: str) -> CancelFindingsReportResponseTypeDef:
        """
        Cancels the given findings report.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.cancel_findings_report)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#cancel_findings_report)
        """

    async def cancel_sbom_export(self, *, reportId: str) -> CancelSbomExportResponseTypeDef:
        """
        Cancels a software bill of materials (SBOM) report.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.cancel_sbom_export)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#cancel_sbom_export)
        """

    async def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.close)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#close)
        """

    async def create_cis_scan_configuration(
        self,
        *,
        scanName: str,
        schedule: ScheduleTypeDef,
        securityLevel: CisSecurityLevelType,
        targets: CreateCisTargetsTypeDef,
        tags: Mapping[str, str] = ...,
    ) -> CreateCisScanConfigurationResponseTypeDef:
        """
        Creates a CIS scan configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.create_cis_scan_configuration)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#create_cis_scan_configuration)
        """

    async def create_filter(
        self,
        *,
        action: FilterActionType,
        filterCriteria: FilterCriteriaTypeDef,
        name: str,
        description: str = ...,
        reason: str = ...,
        tags: Mapping[str, str] = ...,
    ) -> CreateFilterResponseTypeDef:
        """
        Creates a filter resource using specified filter criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.create_filter)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#create_filter)
        """

    async def create_findings_report(
        self,
        *,
        reportFormat: ReportFormatType,
        s3Destination: DestinationTypeDef,
        filterCriteria: FilterCriteriaTypeDef = ...,
    ) -> CreateFindingsReportResponseTypeDef:
        """
        Creates a finding report.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.create_findings_report)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#create_findings_report)
        """

    async def create_sbom_export(
        self,
        *,
        reportFormat: SbomReportFormatType,
        s3Destination: DestinationTypeDef,
        resourceFilterCriteria: ResourceFilterCriteriaTypeDef = ...,
    ) -> CreateSbomExportResponseTypeDef:
        """
        Creates a software bill of materials (SBOM) report.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.create_sbom_export)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#create_sbom_export)
        """

    async def delete_cis_scan_configuration(
        self, *, scanConfigurationArn: str
    ) -> DeleteCisScanConfigurationResponseTypeDef:
        """
        Deletes a CIS scan configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.delete_cis_scan_configuration)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#delete_cis_scan_configuration)
        """

    async def delete_filter(self, *, arn: str) -> DeleteFilterResponseTypeDef:
        """
        Deletes a filter resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.delete_filter)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#delete_filter)
        """

    async def describe_organization_configuration(
        self,
    ) -> DescribeOrganizationConfigurationResponseTypeDef:
        """
        Describe Amazon Inspector configuration settings for an Amazon Web Services
        organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.describe_organization_configuration)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#describe_organization_configuration)
        """

    async def disable(
        self,
        *,
        accountIds: Sequence[str] = ...,
        resourceTypes: Sequence[ResourceScanTypeType] = ...,
    ) -> DisableResponseTypeDef:
        """
        Disables Amazon Inspector scans for one or more Amazon Web Services accounts.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.disable)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#disable)
        """

    async def disable_delegated_admin_account(
        self, *, delegatedAdminAccountId: str
    ) -> DisableDelegatedAdminAccountResponseTypeDef:
        """
        Disables the Amazon Inspector delegated administrator for your organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.disable_delegated_admin_account)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#disable_delegated_admin_account)
        """

    async def disassociate_member(self, *, accountId: str) -> DisassociateMemberResponseTypeDef:
        """
        Disassociates a member account from an Amazon Inspector delegated administrator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.disassociate_member)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#disassociate_member)
        """

    async def enable(
        self,
        *,
        resourceTypes: Sequence[ResourceScanTypeType],
        accountIds: Sequence[str] = ...,
        clientToken: str = ...,
    ) -> EnableResponseTypeDef:
        """
        Enables Amazon Inspector scans for one or more Amazon Web Services accounts.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.enable)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#enable)
        """

    async def enable_delegated_admin_account(
        self, *, delegatedAdminAccountId: str, clientToken: str = ...
    ) -> EnableDelegatedAdminAccountResponseTypeDef:
        """
        Enables the Amazon Inspector delegated administrator for your Organizations
        organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.enable_delegated_admin_account)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#enable_delegated_admin_account)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.generate_presigned_url)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#generate_presigned_url)
        """

    async def get_cis_scan_report(
        self, *, scanArn: str, targetAccounts: Sequence[str] = ...
    ) -> GetCisScanReportResponseTypeDef:
        """
        Retrieves a CIS scan report.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.get_cis_scan_report)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#get_cis_scan_report)
        """

    async def get_cis_scan_result_details(
        self,
        *,
        accountId: str,
        scanArn: str,
        targetResourceId: str,
        filterCriteria: CisScanResultDetailsFilterCriteriaTypeDef = ...,
        maxResults: int = ...,
        nextToken: str = ...,
        sortBy: CisScanResultDetailsSortByType = ...,
        sortOrder: CisSortOrderType = ...,
    ) -> GetCisScanResultDetailsResponseTypeDef:
        """
        Retrieves CIS scan result details.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.get_cis_scan_result_details)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#get_cis_scan_result_details)
        """

    async def get_configuration(self) -> GetConfigurationResponseTypeDef:
        """
        Retrieves setting configurations for Inspector scans.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.get_configuration)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#get_configuration)
        """

    async def get_delegated_admin_account(self) -> GetDelegatedAdminAccountResponseTypeDef:
        """
        Retrieves information about the Amazon Inspector delegated administrator for
        your
        organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.get_delegated_admin_account)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#get_delegated_admin_account)
        """

    async def get_ec2_deep_inspection_configuration(
        self,
    ) -> GetEc2DeepInspectionConfigurationResponseTypeDef:
        """
        Retrieves the activation status of Amazon Inspector deep inspection and custom
        paths associated with your
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.get_ec2_deep_inspection_configuration)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#get_ec2_deep_inspection_configuration)
        """

    async def get_encryption_key(
        self, *, resourceType: ResourceTypeType, scanType: ScanTypeType
    ) -> GetEncryptionKeyResponseTypeDef:
        """
        Gets an encryption key.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.get_encryption_key)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#get_encryption_key)
        """

    async def get_findings_report_status(
        self, *, reportId: str = ...
    ) -> GetFindingsReportStatusResponseTypeDef:
        """
        Gets the status of a findings report.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.get_findings_report_status)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#get_findings_report_status)
        """

    async def get_member(self, *, accountId: str) -> GetMemberResponseTypeDef:
        """
        Gets member information for your organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.get_member)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#get_member)
        """

    async def get_sbom_export(self, *, reportId: str) -> GetSbomExportResponseTypeDef:
        """
        Gets details of a software bill of materials (SBOM) report.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.get_sbom_export)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#get_sbom_export)
        """

    async def list_account_permissions(
        self, *, maxResults: int = ..., nextToken: str = ..., service: ServiceType = ...
    ) -> ListAccountPermissionsResponseTypeDef:
        """
        Lists the permissions an account has to configure Amazon Inspector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.list_account_permissions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#list_account_permissions)
        """

    async def list_cis_scan_configurations(
        self,
        *,
        filterCriteria: ListCisScanConfigurationsFilterCriteriaTypeDef = ...,
        maxResults: int = ...,
        nextToken: str = ...,
        sortBy: CisScanConfigurationsSortByType = ...,
        sortOrder: CisSortOrderType = ...,
    ) -> ListCisScanConfigurationsResponseTypeDef:
        """
        Lists CIS scan configurations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.list_cis_scan_configurations)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#list_cis_scan_configurations)
        """

    async def list_cis_scan_results_aggregated_by_checks(
        self,
        *,
        scanArn: str,
        filterCriteria: CisScanResultsAggregatedByChecksFilterCriteriaTypeDef = ...,
        maxResults: int = ...,
        nextToken: str = ...,
        sortBy: CisScanResultsAggregatedByChecksSortByType = ...,
        sortOrder: CisSortOrderType = ...,
    ) -> ListCisScanResultsAggregatedByChecksResponseTypeDef:
        """
        Lists scan results aggregated by checks.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.list_cis_scan_results_aggregated_by_checks)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#list_cis_scan_results_aggregated_by_checks)
        """

    async def list_cis_scan_results_aggregated_by_target_resource(
        self,
        *,
        scanArn: str,
        filterCriteria: CisScanResultsAggregatedByTargetResourceFilterCriteriaTypeDef = ...,
        maxResults: int = ...,
        nextToken: str = ...,
        sortBy: CisScanResultsAggregatedByTargetResourceSortByType = ...,
        sortOrder: CisSortOrderType = ...,
    ) -> ListCisScanResultsAggregatedByTargetResourceResponseTypeDef:
        """
        Lists scan results aggregated by a target resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.list_cis_scan_results_aggregated_by_target_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#list_cis_scan_results_aggregated_by_target_resource)
        """

    async def list_cis_scans(
        self,
        *,
        detailLevel: ListCisScansDetailLevelType = ...,
        filterCriteria: ListCisScansFilterCriteriaTypeDef = ...,
        maxResults: int = ...,
        nextToken: str = ...,
        sortBy: ListCisScansSortByType = ...,
        sortOrder: CisSortOrderType = ...,
    ) -> ListCisScansResponseTypeDef:
        """
        Returns a CIS scan list.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.list_cis_scans)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#list_cis_scans)
        """

    async def list_coverage(
        self,
        *,
        filterCriteria: CoverageFilterCriteriaTypeDef = ...,
        maxResults: int = ...,
        nextToken: str = ...,
    ) -> ListCoverageResponseTypeDef:
        """
        Lists coverage details for you environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.list_coverage)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#list_coverage)
        """

    async def list_coverage_statistics(
        self,
        *,
        filterCriteria: CoverageFilterCriteriaTypeDef = ...,
        groupBy: GroupKeyType = ...,
        nextToken: str = ...,
    ) -> ListCoverageStatisticsResponseTypeDef:
        """
        Lists Amazon Inspector coverage statistics for your environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.list_coverage_statistics)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#list_coverage_statistics)
        """

    async def list_delegated_admin_accounts(
        self, *, maxResults: int = ..., nextToken: str = ...
    ) -> ListDelegatedAdminAccountsResponseTypeDef:
        """
        Lists information about the Amazon Inspector delegated administrator of your
        organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.list_delegated_admin_accounts)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#list_delegated_admin_accounts)
        """

    async def list_filters(
        self,
        *,
        action: FilterActionType = ...,
        arns: Sequence[str] = ...,
        maxResults: int = ...,
        nextToken: str = ...,
    ) -> ListFiltersResponseTypeDef:
        """
        Lists the filters associated with your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.list_filters)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#list_filters)
        """

    async def list_finding_aggregations(
        self,
        *,
        aggregationType: AggregationTypeType,
        accountIds: Sequence[StringFilterTypeDef] = ...,
        aggregationRequest: AggregationRequestTypeDef = ...,
        maxResults: int = ...,
        nextToken: str = ...,
    ) -> ListFindingAggregationsResponseTypeDef:
        """
        Lists aggregated finding data for your environment based on specific criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.list_finding_aggregations)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#list_finding_aggregations)
        """

    async def list_findings(
        self,
        *,
        filterCriteria: FilterCriteriaTypeDef = ...,
        maxResults: int = ...,
        nextToken: str = ...,
        sortCriteria: SortCriteriaTypeDef = ...,
    ) -> ListFindingsResponseTypeDef:
        """
        Lists findings for your environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.list_findings)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#list_findings)
        """

    async def list_members(
        self, *, maxResults: int = ..., nextToken: str = ..., onlyAssociated: bool = ...
    ) -> ListMembersResponseTypeDef:
        """
        List members associated with the Amazon Inspector delegated administrator for
        your
        organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.list_members)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#list_members)
        """

    async def list_tags_for_resource(
        self, *, resourceArn: str
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists all tags attached to a given resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.list_tags_for_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#list_tags_for_resource)
        """

    async def list_usage_totals(
        self, *, accountIds: Sequence[str] = ..., maxResults: int = ..., nextToken: str = ...
    ) -> ListUsageTotalsResponseTypeDef:
        """
        Lists the Amazon Inspector usage totals over the last 30 days.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.list_usage_totals)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#list_usage_totals)
        """

    async def reset_encryption_key(
        self, *, resourceType: ResourceTypeType, scanType: ScanTypeType
    ) -> Dict[str, Any]:
        """
        Resets an encryption key.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.reset_encryption_key)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#reset_encryption_key)
        """

    async def search_vulnerabilities(
        self, *, filterCriteria: SearchVulnerabilitiesFilterCriteriaTypeDef, nextToken: str = ...
    ) -> SearchVulnerabilitiesResponseTypeDef:
        """
        Lists Amazon Inspector coverage details for a specific vulnerability.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.search_vulnerabilities)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#search_vulnerabilities)
        """

    async def send_cis_session_health(self, *, scanJobId: str, sessionToken: str) -> Dict[str, Any]:
        """
        Sends a CIS session health.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.send_cis_session_health)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#send_cis_session_health)
        """

    async def send_cis_session_telemetry(
        self, *, messages: Sequence[CisSessionMessageTypeDef], scanJobId: str, sessionToken: str
    ) -> Dict[str, Any]:
        """
        Sends a CIS session telemetry.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.send_cis_session_telemetry)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#send_cis_session_telemetry)
        """

    async def start_cis_session(
        self, *, message: StartCisSessionMessageTypeDef, scanJobId: str
    ) -> Dict[str, Any]:
        """
        Starts a CIS session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.start_cis_session)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#start_cis_session)
        """

    async def stop_cis_session(
        self, *, message: StopCisSessionMessageTypeDef, scanJobId: str, sessionToken: str
    ) -> Dict[str, Any]:
        """
        Stops a CIS session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.stop_cis_session)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#stop_cis_session)
        """

    async def tag_resource(self, *, resourceArn: str, tags: Mapping[str, str]) -> Dict[str, Any]:
        """
        Adds tags to a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.tag_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#tag_resource)
        """

    async def untag_resource(self, *, resourceArn: str, tagKeys: Sequence[str]) -> Dict[str, Any]:
        """
        Removes tags from a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.untag_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#untag_resource)
        """

    async def update_cis_scan_configuration(
        self,
        *,
        scanConfigurationArn: str,
        scanName: str = ...,
        schedule: ScheduleTypeDef = ...,
        securityLevel: CisSecurityLevelType = ...,
        targets: UpdateCisTargetsTypeDef = ...,
    ) -> UpdateCisScanConfigurationResponseTypeDef:
        """
        Updates a CIS scan configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.update_cis_scan_configuration)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#update_cis_scan_configuration)
        """

    async def update_configuration(
        self, *, ecrConfiguration: EcrConfigurationTypeDef
    ) -> Dict[str, Any]:
        """
        Updates setting configurations for your Amazon Inspector account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.update_configuration)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#update_configuration)
        """

    async def update_ec2_deep_inspection_configuration(
        self, *, activateDeepInspection: bool = ..., packagePaths: Sequence[str] = ...
    ) -> UpdateEc2DeepInspectionConfigurationResponseTypeDef:
        """
        Activates, deactivates Amazon Inspector deep inspection, or updates custom
        paths for your
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.update_ec2_deep_inspection_configuration)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#update_ec2_deep_inspection_configuration)
        """

    async def update_encryption_key(
        self, *, kmsKeyId: str, resourceType: ResourceTypeType, scanType: ScanTypeType
    ) -> Dict[str, Any]:
        """
        Updates an encryption key.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.update_encryption_key)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#update_encryption_key)
        """

    async def update_filter(
        self,
        *,
        filterArn: str,
        action: FilterActionType = ...,
        description: str = ...,
        filterCriteria: FilterCriteriaTypeDef = ...,
        name: str = ...,
        reason: str = ...,
    ) -> UpdateFilterResponseTypeDef:
        """
        Specifies the action that is to be applied to the findings that match the
        filter.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.update_filter)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#update_filter)
        """

    async def update_org_ec2_deep_inspection_configuration(
        self, *, orgPackagePaths: Sequence[str]
    ) -> Dict[str, Any]:
        """
        Updates the Amazon Inspector deep inspection custom paths for your organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.update_org_ec2_deep_inspection_configuration)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#update_org_ec2_deep_inspection_configuration)
        """

    async def update_organization_configuration(
        self, *, autoEnable: AutoEnableTypeDef
    ) -> UpdateOrganizationConfigurationResponseTypeDef:
        """
        Updates the configurations for your Amazon Inspector organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.update_organization_configuration)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#update_organization_configuration)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_cis_scan_result_details"]
    ) -> GetCisScanResultDetailsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_account_permissions"]
    ) -> ListAccountPermissionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_cis_scan_configurations"]
    ) -> ListCisScanConfigurationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_cis_scan_results_aggregated_by_checks"]
    ) -> ListCisScanResultsAggregatedByChecksPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_cis_scan_results_aggregated_by_target_resource"]
    ) -> ListCisScanResultsAggregatedByTargetResourcePaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_cis_scans"]) -> ListCisScansPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_coverage"]) -> ListCoveragePaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_coverage_statistics"]
    ) -> ListCoverageStatisticsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_delegated_admin_accounts"]
    ) -> ListDelegatedAdminAccountsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_filters"]) -> ListFiltersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_finding_aggregations"]
    ) -> ListFindingAggregationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_findings"]) -> ListFindingsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_members"]) -> ListMembersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_usage_totals"]
    ) -> ListUsageTotalsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["search_vulnerabilities"]
    ) -> SearchVulnerabilitiesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/#get_paginator)
        """

    async def __aenter__(self) -> "Inspector2Client":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/)
        """

    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> Any:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/client/)
        """
