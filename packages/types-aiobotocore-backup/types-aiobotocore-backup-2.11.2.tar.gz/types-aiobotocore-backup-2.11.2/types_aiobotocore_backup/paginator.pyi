"""
Type annotations for backup service client paginators.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/paginators/)

Usage::

    ```python
    from aiobotocore.session import get_session

    from types_aiobotocore_backup.client import BackupClient
    from types_aiobotocore_backup.paginator import (
        ListBackupJobsPaginator,
        ListBackupPlanTemplatesPaginator,
        ListBackupPlanVersionsPaginator,
        ListBackupPlansPaginator,
        ListBackupSelectionsPaginator,
        ListBackupVaultsPaginator,
        ListCopyJobsPaginator,
        ListLegalHoldsPaginator,
        ListProtectedResourcesPaginator,
        ListProtectedResourcesByBackupVaultPaginator,
        ListRecoveryPointsByBackupVaultPaginator,
        ListRecoveryPointsByLegalHoldPaginator,
        ListRecoveryPointsByResourcePaginator,
        ListRestoreJobsPaginator,
        ListRestoreJobsByProtectedResourcePaginator,
        ListRestoreTestingPlansPaginator,
        ListRestoreTestingSelectionsPaginator,
    )

    session = get_session()
    with session.create_client("backup") as client:
        client: BackupClient

        list_backup_jobs_paginator: ListBackupJobsPaginator = client.get_paginator("list_backup_jobs")
        list_backup_plan_templates_paginator: ListBackupPlanTemplatesPaginator = client.get_paginator("list_backup_plan_templates")
        list_backup_plan_versions_paginator: ListBackupPlanVersionsPaginator = client.get_paginator("list_backup_plan_versions")
        list_backup_plans_paginator: ListBackupPlansPaginator = client.get_paginator("list_backup_plans")
        list_backup_selections_paginator: ListBackupSelectionsPaginator = client.get_paginator("list_backup_selections")
        list_backup_vaults_paginator: ListBackupVaultsPaginator = client.get_paginator("list_backup_vaults")
        list_copy_jobs_paginator: ListCopyJobsPaginator = client.get_paginator("list_copy_jobs")
        list_legal_holds_paginator: ListLegalHoldsPaginator = client.get_paginator("list_legal_holds")
        list_protected_resources_paginator: ListProtectedResourcesPaginator = client.get_paginator("list_protected_resources")
        list_protected_resources_by_backup_vault_paginator: ListProtectedResourcesByBackupVaultPaginator = client.get_paginator("list_protected_resources_by_backup_vault")
        list_recovery_points_by_backup_vault_paginator: ListRecoveryPointsByBackupVaultPaginator = client.get_paginator("list_recovery_points_by_backup_vault")
        list_recovery_points_by_legal_hold_paginator: ListRecoveryPointsByLegalHoldPaginator = client.get_paginator("list_recovery_points_by_legal_hold")
        list_recovery_points_by_resource_paginator: ListRecoveryPointsByResourcePaginator = client.get_paginator("list_recovery_points_by_resource")
        list_restore_jobs_paginator: ListRestoreJobsPaginator = client.get_paginator("list_restore_jobs")
        list_restore_jobs_by_protected_resource_paginator: ListRestoreJobsByProtectedResourcePaginator = client.get_paginator("list_restore_jobs_by_protected_resource")
        list_restore_testing_plans_paginator: ListRestoreTestingPlansPaginator = client.get_paginator("list_restore_testing_plans")
        list_restore_testing_selections_paginator: ListRestoreTestingSelectionsPaginator = client.get_paginator("list_restore_testing_selections")
    ```
"""

from typing import AsyncIterator, Generic, Iterator, TypeVar

from aiobotocore.paginate import AioPaginator
from botocore.paginate import PageIterator

from .literals import BackupJobStateType, CopyJobStateType, RestoreJobStatusType, VaultTypeType
from .type_defs import (
    ListBackupJobsOutputTypeDef,
    ListBackupPlansOutputPaginatorTypeDef,
    ListBackupPlanTemplatesOutputTypeDef,
    ListBackupPlanVersionsOutputPaginatorTypeDef,
    ListBackupSelectionsOutputTypeDef,
    ListBackupVaultsOutputTypeDef,
    ListCopyJobsOutputTypeDef,
    ListLegalHoldsOutputTypeDef,
    ListProtectedResourcesByBackupVaultOutputTypeDef,
    ListProtectedResourcesOutputTypeDef,
    ListRecoveryPointsByBackupVaultOutputTypeDef,
    ListRecoveryPointsByLegalHoldOutputTypeDef,
    ListRecoveryPointsByResourceOutputTypeDef,
    ListRestoreJobsByProtectedResourceOutputTypeDef,
    ListRestoreJobsOutputTypeDef,
    ListRestoreTestingPlansOutputTypeDef,
    ListRestoreTestingSelectionsOutputTypeDef,
    PaginatorConfigTypeDef,
    TimestampTypeDef,
)

__all__ = (
    "ListBackupJobsPaginator",
    "ListBackupPlanTemplatesPaginator",
    "ListBackupPlanVersionsPaginator",
    "ListBackupPlansPaginator",
    "ListBackupSelectionsPaginator",
    "ListBackupVaultsPaginator",
    "ListCopyJobsPaginator",
    "ListLegalHoldsPaginator",
    "ListProtectedResourcesPaginator",
    "ListProtectedResourcesByBackupVaultPaginator",
    "ListRecoveryPointsByBackupVaultPaginator",
    "ListRecoveryPointsByLegalHoldPaginator",
    "ListRecoveryPointsByResourcePaginator",
    "ListRestoreJobsPaginator",
    "ListRestoreJobsByProtectedResourcePaginator",
    "ListRestoreTestingPlansPaginator",
    "ListRestoreTestingSelectionsPaginator",
)

_ItemTypeDef = TypeVar("_ItemTypeDef")

class _PageIterator(Generic[_ItemTypeDef], PageIterator):
    def __iter__(self) -> Iterator[_ItemTypeDef]:
        """
        Proxy method to specify iterator item type.
        """

class ListBackupJobsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Paginator.ListBackupJobs)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/paginators/#listbackupjobspaginator)
    """

    def paginate(
        self,
        *,
        ByResourceArn: str = ...,
        ByState: BackupJobStateType = ...,
        ByBackupVaultName: str = ...,
        ByCreatedBefore: TimestampTypeDef = ...,
        ByCreatedAfter: TimestampTypeDef = ...,
        ByResourceType: str = ...,
        ByAccountId: str = ...,
        ByCompleteAfter: TimestampTypeDef = ...,
        ByCompleteBefore: TimestampTypeDef = ...,
        ByParentJobId: str = ...,
        ByMessageCategory: str = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListBackupJobsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Paginator.ListBackupJobs.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/paginators/#listbackupjobspaginator)
        """

class ListBackupPlanTemplatesPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Paginator.ListBackupPlanTemplates)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/paginators/#listbackupplantemplatespaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListBackupPlanTemplatesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Paginator.ListBackupPlanTemplates.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/paginators/#listbackupplantemplatespaginator)
        """

class ListBackupPlanVersionsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Paginator.ListBackupPlanVersions)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/paginators/#listbackupplanversionspaginator)
    """

    def paginate(
        self, *, BackupPlanId: str, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListBackupPlanVersionsOutputPaginatorTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Paginator.ListBackupPlanVersions.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/paginators/#listbackupplanversionspaginator)
        """

class ListBackupPlansPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Paginator.ListBackupPlans)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/paginators/#listbackupplanspaginator)
    """

    def paginate(
        self, *, IncludeDeleted: bool = ..., PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListBackupPlansOutputPaginatorTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Paginator.ListBackupPlans.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/paginators/#listbackupplanspaginator)
        """

class ListBackupSelectionsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Paginator.ListBackupSelections)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/paginators/#listbackupselectionspaginator)
    """

    def paginate(
        self, *, BackupPlanId: str, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListBackupSelectionsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Paginator.ListBackupSelections.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/paginators/#listbackupselectionspaginator)
        """

class ListBackupVaultsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Paginator.ListBackupVaults)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/paginators/#listbackupvaultspaginator)
    """

    def paginate(
        self,
        *,
        ByVaultType: VaultTypeType = ...,
        ByShared: bool = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListBackupVaultsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Paginator.ListBackupVaults.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/paginators/#listbackupvaultspaginator)
        """

class ListCopyJobsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Paginator.ListCopyJobs)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/paginators/#listcopyjobspaginator)
    """

    def paginate(
        self,
        *,
        ByResourceArn: str = ...,
        ByState: CopyJobStateType = ...,
        ByCreatedBefore: TimestampTypeDef = ...,
        ByCreatedAfter: TimestampTypeDef = ...,
        ByResourceType: str = ...,
        ByDestinationVaultArn: str = ...,
        ByAccountId: str = ...,
        ByCompleteBefore: TimestampTypeDef = ...,
        ByCompleteAfter: TimestampTypeDef = ...,
        ByParentJobId: str = ...,
        ByMessageCategory: str = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListCopyJobsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Paginator.ListCopyJobs.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/paginators/#listcopyjobspaginator)
        """

class ListLegalHoldsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Paginator.ListLegalHolds)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/paginators/#listlegalholdspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListLegalHoldsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Paginator.ListLegalHolds.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/paginators/#listlegalholdspaginator)
        """

class ListProtectedResourcesPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Paginator.ListProtectedResources)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/paginators/#listprotectedresourcespaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListProtectedResourcesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Paginator.ListProtectedResources.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/paginators/#listprotectedresourcespaginator)
        """

class ListProtectedResourcesByBackupVaultPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Paginator.ListProtectedResourcesByBackupVault)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/paginators/#listprotectedresourcesbybackupvaultpaginator)
    """

    def paginate(
        self,
        *,
        BackupVaultName: str,
        BackupVaultAccountId: str = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListProtectedResourcesByBackupVaultOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Paginator.ListProtectedResourcesByBackupVault.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/paginators/#listprotectedresourcesbybackupvaultpaginator)
        """

class ListRecoveryPointsByBackupVaultPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Paginator.ListRecoveryPointsByBackupVault)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/paginators/#listrecoverypointsbybackupvaultpaginator)
    """

    def paginate(
        self,
        *,
        BackupVaultName: str,
        BackupVaultAccountId: str = ...,
        ByResourceArn: str = ...,
        ByResourceType: str = ...,
        ByBackupPlanId: str = ...,
        ByCreatedBefore: TimestampTypeDef = ...,
        ByCreatedAfter: TimestampTypeDef = ...,
        ByParentRecoveryPointArn: str = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListRecoveryPointsByBackupVaultOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Paginator.ListRecoveryPointsByBackupVault.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/paginators/#listrecoverypointsbybackupvaultpaginator)
        """

class ListRecoveryPointsByLegalHoldPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Paginator.ListRecoveryPointsByLegalHold)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/paginators/#listrecoverypointsbylegalholdpaginator)
    """

    def paginate(
        self, *, LegalHoldId: str, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListRecoveryPointsByLegalHoldOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Paginator.ListRecoveryPointsByLegalHold.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/paginators/#listrecoverypointsbylegalholdpaginator)
        """

class ListRecoveryPointsByResourcePaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Paginator.ListRecoveryPointsByResource)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/paginators/#listrecoverypointsbyresourcepaginator)
    """

    def paginate(
        self, *, ResourceArn: str, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListRecoveryPointsByResourceOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Paginator.ListRecoveryPointsByResource.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/paginators/#listrecoverypointsbyresourcepaginator)
        """

class ListRestoreJobsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Paginator.ListRestoreJobs)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/paginators/#listrestorejobspaginator)
    """

    def paginate(
        self,
        *,
        ByAccountId: str = ...,
        ByResourceType: str = ...,
        ByCreatedBefore: TimestampTypeDef = ...,
        ByCreatedAfter: TimestampTypeDef = ...,
        ByStatus: RestoreJobStatusType = ...,
        ByCompleteBefore: TimestampTypeDef = ...,
        ByCompleteAfter: TimestampTypeDef = ...,
        ByRestoreTestingPlanArn: str = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListRestoreJobsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Paginator.ListRestoreJobs.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/paginators/#listrestorejobspaginator)
        """

class ListRestoreJobsByProtectedResourcePaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Paginator.ListRestoreJobsByProtectedResource)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/paginators/#listrestorejobsbyprotectedresourcepaginator)
    """

    def paginate(
        self,
        *,
        ResourceArn: str,
        ByStatus: RestoreJobStatusType = ...,
        ByRecoveryPointCreationDateAfter: TimestampTypeDef = ...,
        ByRecoveryPointCreationDateBefore: TimestampTypeDef = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListRestoreJobsByProtectedResourceOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Paginator.ListRestoreJobsByProtectedResource.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/paginators/#listrestorejobsbyprotectedresourcepaginator)
        """

class ListRestoreTestingPlansPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Paginator.ListRestoreTestingPlans)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/paginators/#listrestoretestingplanspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListRestoreTestingPlansOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Paginator.ListRestoreTestingPlans.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/paginators/#listrestoretestingplanspaginator)
        """

class ListRestoreTestingSelectionsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Paginator.ListRestoreTestingSelections)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/paginators/#listrestoretestingselectionspaginator)
    """

    def paginate(
        self, *, RestoreTestingPlanName: str, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListRestoreTestingSelectionsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Paginator.ListRestoreTestingSelections.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/paginators/#listrestoretestingselectionspaginator)
        """
