"""
Type annotations for backup service client.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/)

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_backup.client import BackupClient

    session = get_session()
    async with session.create_client("backup") as client:
        client: BackupClient
    ```
"""

import sys
from typing import Any, Dict, Mapping, Sequence, Type, overload

from aiobotocore.client import AioBaseClient
from botocore.client import ClientMeta

from .literals import (
    AggregationPeriodType,
    BackupJobStateType,
    BackupJobStatusType,
    BackupVaultEventType,
    CopyJobStateType,
    CopyJobStatusType,
    RestoreJobStateType,
    RestoreJobStatusType,
    RestoreValidationStatusType,
    VaultTypeType,
)
from .paginator import (
    ListBackupJobsPaginator,
    ListBackupPlansPaginator,
    ListBackupPlanTemplatesPaginator,
    ListBackupPlanVersionsPaginator,
    ListBackupSelectionsPaginator,
    ListBackupVaultsPaginator,
    ListCopyJobsPaginator,
    ListLegalHoldsPaginator,
    ListProtectedResourcesByBackupVaultPaginator,
    ListProtectedResourcesPaginator,
    ListRecoveryPointsByBackupVaultPaginator,
    ListRecoveryPointsByLegalHoldPaginator,
    ListRecoveryPointsByResourcePaginator,
    ListRestoreJobsByProtectedResourcePaginator,
    ListRestoreJobsPaginator,
    ListRestoreTestingPlansPaginator,
    ListRestoreTestingSelectionsPaginator,
)
from .type_defs import (
    BackupPlanInputTypeDef,
    BackupSelectionTypeDef,
    CreateBackupPlanOutputTypeDef,
    CreateBackupSelectionOutputTypeDef,
    CreateBackupVaultOutputTypeDef,
    CreateFrameworkOutputTypeDef,
    CreateLegalHoldOutputTypeDef,
    CreateLogicallyAirGappedBackupVaultOutputTypeDef,
    CreateReportPlanOutputTypeDef,
    CreateRestoreTestingPlanOutputTypeDef,
    CreateRestoreTestingSelectionOutputTypeDef,
    DeleteBackupPlanOutputTypeDef,
    DescribeBackupJobOutputTypeDef,
    DescribeBackupVaultOutputTypeDef,
    DescribeCopyJobOutputTypeDef,
    DescribeFrameworkOutputTypeDef,
    DescribeGlobalSettingsOutputTypeDef,
    DescribeProtectedResourceOutputTypeDef,
    DescribeRecoveryPointOutputTypeDef,
    DescribeRegionSettingsOutputTypeDef,
    DescribeReportJobOutputTypeDef,
    DescribeReportPlanOutputTypeDef,
    DescribeRestoreJobOutputTypeDef,
    EmptyResponseMetadataTypeDef,
    ExportBackupPlanTemplateOutputTypeDef,
    FrameworkControlTypeDef,
    GetBackupPlanFromJSONOutputTypeDef,
    GetBackupPlanFromTemplateOutputTypeDef,
    GetBackupPlanOutputTypeDef,
    GetBackupSelectionOutputTypeDef,
    GetBackupVaultAccessPolicyOutputTypeDef,
    GetBackupVaultNotificationsOutputTypeDef,
    GetLegalHoldOutputTypeDef,
    GetRecoveryPointRestoreMetadataOutputTypeDef,
    GetRestoreJobMetadataOutputTypeDef,
    GetRestoreTestingInferredMetadataOutputTypeDef,
    GetRestoreTestingPlanOutputTypeDef,
    GetRestoreTestingSelectionOutputTypeDef,
    GetSupportedResourceTypesOutputTypeDef,
    LifecycleTypeDef,
    ListBackupJobsOutputTypeDef,
    ListBackupJobSummariesOutputTypeDef,
    ListBackupPlansOutputTypeDef,
    ListBackupPlanTemplatesOutputTypeDef,
    ListBackupPlanVersionsOutputTypeDef,
    ListBackupSelectionsOutputTypeDef,
    ListBackupVaultsOutputTypeDef,
    ListCopyJobsOutputTypeDef,
    ListCopyJobSummariesOutputTypeDef,
    ListFrameworksOutputTypeDef,
    ListLegalHoldsOutputTypeDef,
    ListProtectedResourcesByBackupVaultOutputTypeDef,
    ListProtectedResourcesOutputTypeDef,
    ListRecoveryPointsByBackupVaultOutputTypeDef,
    ListRecoveryPointsByLegalHoldOutputTypeDef,
    ListRecoveryPointsByResourceOutputTypeDef,
    ListReportJobsOutputTypeDef,
    ListReportPlansOutputTypeDef,
    ListRestoreJobsByProtectedResourceOutputTypeDef,
    ListRestoreJobsOutputTypeDef,
    ListRestoreJobSummariesOutputTypeDef,
    ListRestoreTestingPlansOutputTypeDef,
    ListRestoreTestingSelectionsOutputTypeDef,
    ListTagsOutputTypeDef,
    RecoveryPointSelectionTypeDef,
    ReportDeliveryChannelTypeDef,
    ReportSettingTypeDef,
    RestoreTestingPlanForCreateTypeDef,
    RestoreTestingPlanForUpdateTypeDef,
    RestoreTestingSelectionForCreateTypeDef,
    RestoreTestingSelectionForUpdateTypeDef,
    StartBackupJobOutputTypeDef,
    StartCopyJobOutputTypeDef,
    StartReportJobOutputTypeDef,
    StartRestoreJobOutputTypeDef,
    TimestampTypeDef,
    UpdateBackupPlanOutputTypeDef,
    UpdateFrameworkOutputTypeDef,
    UpdateRecoveryPointLifecycleOutputTypeDef,
    UpdateReportPlanOutputTypeDef,
    UpdateRestoreTestingPlanOutputTypeDef,
    UpdateRestoreTestingSelectionOutputTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("BackupClient",)


class BotocoreClientError(Exception):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AlreadyExistsException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    DependencyFailureException: Type[BotocoreClientError]
    InvalidParameterValueException: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]
    InvalidResourceStateException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    MissingParameterValueException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceUnavailableException: Type[BotocoreClientError]


class BackupClient(AioBaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        BackupClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.exceptions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.can_paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#can_paginate)
        """

    async def cancel_legal_hold(
        self, *, LegalHoldId: str, CancelDescription: str, RetainRecordInDays: int = ...
    ) -> Dict[str, Any]:
        """
        This action removes the specified legal hold on a recovery point.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.cancel_legal_hold)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#cancel_legal_hold)
        """

    async def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.close)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#close)
        """

    async def create_backup_plan(
        self,
        *,
        BackupPlan: BackupPlanInputTypeDef,
        BackupPlanTags: Mapping[str, str] = ...,
        CreatorRequestId: str = ...,
    ) -> CreateBackupPlanOutputTypeDef:
        """
        Creates a backup plan using a backup plan name and backup rules.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.create_backup_plan)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#create_backup_plan)
        """

    async def create_backup_selection(
        self,
        *,
        BackupPlanId: str,
        BackupSelection: BackupSelectionTypeDef,
        CreatorRequestId: str = ...,
    ) -> CreateBackupSelectionOutputTypeDef:
        """
        Creates a JSON document that specifies a set of resources to assign to a backup
        plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.create_backup_selection)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#create_backup_selection)
        """

    async def create_backup_vault(
        self,
        *,
        BackupVaultName: str,
        BackupVaultTags: Mapping[str, str] = ...,
        EncryptionKeyArn: str = ...,
        CreatorRequestId: str = ...,
    ) -> CreateBackupVaultOutputTypeDef:
        """
        Creates a logical container where backups are stored.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.create_backup_vault)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#create_backup_vault)
        """

    async def create_framework(
        self,
        *,
        FrameworkName: str,
        FrameworkControls: Sequence[FrameworkControlTypeDef],
        FrameworkDescription: str = ...,
        IdempotencyToken: str = ...,
        FrameworkTags: Mapping[str, str] = ...,
    ) -> CreateFrameworkOutputTypeDef:
        """
        Creates a framework with one or more controls.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.create_framework)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#create_framework)
        """

    async def create_legal_hold(
        self,
        *,
        Title: str,
        Description: str,
        IdempotencyToken: str = ...,
        RecoveryPointSelection: RecoveryPointSelectionTypeDef = ...,
        Tags: Mapping[str, str] = ...,
    ) -> CreateLegalHoldOutputTypeDef:
        """
        This action creates a legal hold on a recovery point (backup).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.create_legal_hold)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#create_legal_hold)
        """

    async def create_logically_air_gapped_backup_vault(
        self,
        *,
        BackupVaultName: str,
        MinRetentionDays: int,
        MaxRetentionDays: int,
        BackupVaultTags: Mapping[str, str] = ...,
        CreatorRequestId: str = ...,
    ) -> CreateLogicallyAirGappedBackupVaultOutputTypeDef:
        """
        This request creates a logical container to where backups may be copied.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.create_logically_air_gapped_backup_vault)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#create_logically_air_gapped_backup_vault)
        """

    async def create_report_plan(
        self,
        *,
        ReportPlanName: str,
        ReportDeliveryChannel: ReportDeliveryChannelTypeDef,
        ReportSetting: ReportSettingTypeDef,
        ReportPlanDescription: str = ...,
        ReportPlanTags: Mapping[str, str] = ...,
        IdempotencyToken: str = ...,
    ) -> CreateReportPlanOutputTypeDef:
        """
        Creates a report plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.create_report_plan)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#create_report_plan)
        """

    async def create_restore_testing_plan(
        self,
        *,
        RestoreTestingPlan: RestoreTestingPlanForCreateTypeDef,
        CreatorRequestId: str = ...,
        Tags: Mapping[str, str] = ...,
    ) -> CreateRestoreTestingPlanOutputTypeDef:
        """
        This is the first of two steps to create a restore testing plan; once this
        request is successful, finish the procedure with request
        CreateRestoreTestingSelection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.create_restore_testing_plan)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#create_restore_testing_plan)
        """

    async def create_restore_testing_selection(
        self,
        *,
        RestoreTestingPlanName: str,
        RestoreTestingSelection: RestoreTestingSelectionForCreateTypeDef,
        CreatorRequestId: str = ...,
    ) -> CreateRestoreTestingSelectionOutputTypeDef:
        """
        This request can be sent after CreateRestoreTestingPlan request returns
        successfully.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.create_restore_testing_selection)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#create_restore_testing_selection)
        """

    async def delete_backup_plan(self, *, BackupPlanId: str) -> DeleteBackupPlanOutputTypeDef:
        """
        Deletes a backup plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.delete_backup_plan)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#delete_backup_plan)
        """

    async def delete_backup_selection(
        self, *, BackupPlanId: str, SelectionId: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the resource selection associated with a backup plan that is specified
        by the
        `SelectionId`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.delete_backup_selection)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#delete_backup_selection)
        """

    async def delete_backup_vault(self, *, BackupVaultName: str) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the backup vault identified by its name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.delete_backup_vault)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#delete_backup_vault)
        """

    async def delete_backup_vault_access_policy(
        self, *, BackupVaultName: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the policy document that manages permissions on a backup vault.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.delete_backup_vault_access_policy)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#delete_backup_vault_access_policy)
        """

    async def delete_backup_vault_lock_configuration(
        self, *, BackupVaultName: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes Backup Vault Lock from a backup vault specified by a backup vault name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.delete_backup_vault_lock_configuration)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#delete_backup_vault_lock_configuration)
        """

    async def delete_backup_vault_notifications(
        self, *, BackupVaultName: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes event notifications for the specified backup vault.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.delete_backup_vault_notifications)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#delete_backup_vault_notifications)
        """

    async def delete_framework(self, *, FrameworkName: str) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the framework specified by a framework name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.delete_framework)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#delete_framework)
        """

    async def delete_recovery_point(
        self, *, BackupVaultName: str, RecoveryPointArn: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the recovery point specified by a recovery point ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.delete_recovery_point)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#delete_recovery_point)
        """

    async def delete_report_plan(self, *, ReportPlanName: str) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the report plan specified by a report plan name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.delete_report_plan)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#delete_report_plan)
        """

    async def delete_restore_testing_plan(
        self, *, RestoreTestingPlanName: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        This request deletes the specified restore testing plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.delete_restore_testing_plan)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#delete_restore_testing_plan)
        """

    async def delete_restore_testing_selection(
        self, *, RestoreTestingPlanName: str, RestoreTestingSelectionName: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Input the Restore Testing Plan name and Restore Testing Selection name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.delete_restore_testing_selection)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#delete_restore_testing_selection)
        """

    async def describe_backup_job(self, *, BackupJobId: str) -> DescribeBackupJobOutputTypeDef:
        """
        Returns backup job details for the specified `BackupJobId`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.describe_backup_job)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#describe_backup_job)
        """

    async def describe_backup_vault(
        self, *, BackupVaultName: str, BackupVaultAccountId: str = ...
    ) -> DescribeBackupVaultOutputTypeDef:
        """
        Returns metadata about a backup vault specified by its name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.describe_backup_vault)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#describe_backup_vault)
        """

    async def describe_copy_job(self, *, CopyJobId: str) -> DescribeCopyJobOutputTypeDef:
        """
        Returns metadata associated with creating a copy of a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.describe_copy_job)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#describe_copy_job)
        """

    async def describe_framework(self, *, FrameworkName: str) -> DescribeFrameworkOutputTypeDef:
        """
        Returns the framework details for the specified `FrameworkName`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.describe_framework)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#describe_framework)
        """

    async def describe_global_settings(self) -> DescribeGlobalSettingsOutputTypeDef:
        """
        Describes whether the Amazon Web Services account is opted in to cross-account
        backup.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.describe_global_settings)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#describe_global_settings)
        """

    async def describe_protected_resource(
        self, *, ResourceArn: str
    ) -> DescribeProtectedResourceOutputTypeDef:
        """
        Returns information about a saved resource, including the last time it was
        backed up, its Amazon Resource Name (ARN), and the Amazon Web Services service
        type of the saved
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.describe_protected_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#describe_protected_resource)
        """

    async def describe_recovery_point(
        self, *, BackupVaultName: str, RecoveryPointArn: str, BackupVaultAccountId: str = ...
    ) -> DescribeRecoveryPointOutputTypeDef:
        """
        Returns metadata associated with a recovery point, including ID, status,
        encryption, and
        lifecycle.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.describe_recovery_point)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#describe_recovery_point)
        """

    async def describe_region_settings(self) -> DescribeRegionSettingsOutputTypeDef:
        """
        Returns the current service opt-in settings for the Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.describe_region_settings)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#describe_region_settings)
        """

    async def describe_report_job(self, *, ReportJobId: str) -> DescribeReportJobOutputTypeDef:
        """
        Returns the details associated with creating a report as specified by its
        `ReportJobId`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.describe_report_job)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#describe_report_job)
        """

    async def describe_report_plan(self, *, ReportPlanName: str) -> DescribeReportPlanOutputTypeDef:
        """
        Returns a list of all report plans for an Amazon Web Services account and
        Amazon Web Services
        Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.describe_report_plan)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#describe_report_plan)
        """

    async def describe_restore_job(self, *, RestoreJobId: str) -> DescribeRestoreJobOutputTypeDef:
        """
        Returns metadata associated with a restore job that is specified by a job ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.describe_restore_job)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#describe_restore_job)
        """

    async def disassociate_recovery_point(
        self, *, BackupVaultName: str, RecoveryPointArn: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified continuous backup recovery point from Backup and releases
        control of that continuous backup to the source service, such as Amazon
        RDS.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.disassociate_recovery_point)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#disassociate_recovery_point)
        """

    async def disassociate_recovery_point_from_parent(
        self, *, BackupVaultName: str, RecoveryPointArn: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        This action to a specific child (nested) recovery point removes the
        relationship between the specified recovery point and its parent (composite)
        recovery
        point.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.disassociate_recovery_point_from_parent)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#disassociate_recovery_point_from_parent)
        """

    async def export_backup_plan_template(
        self, *, BackupPlanId: str
    ) -> ExportBackupPlanTemplateOutputTypeDef:
        """
        Returns the backup plan that is specified by the plan ID as a backup template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.export_backup_plan_template)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#export_backup_plan_template)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.generate_presigned_url)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#generate_presigned_url)
        """

    async def get_backup_plan(
        self, *, BackupPlanId: str, VersionId: str = ...
    ) -> GetBackupPlanOutputTypeDef:
        """
        Returns `BackupPlan` details for the specified `BackupPlanId`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.get_backup_plan)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#get_backup_plan)
        """

    async def get_backup_plan_from_json(
        self, *, BackupPlanTemplateJson: str
    ) -> GetBackupPlanFromJSONOutputTypeDef:
        """
        Returns a valid JSON document specifying a backup plan or an error.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.get_backup_plan_from_json)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#get_backup_plan_from_json)
        """

    async def get_backup_plan_from_template(
        self, *, BackupPlanTemplateId: str
    ) -> GetBackupPlanFromTemplateOutputTypeDef:
        """
        Returns the template specified by its `templateId` as a backup plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.get_backup_plan_from_template)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#get_backup_plan_from_template)
        """

    async def get_backup_selection(
        self, *, BackupPlanId: str, SelectionId: str
    ) -> GetBackupSelectionOutputTypeDef:
        """
        Returns selection metadata and a document in JSON format that specifies a list
        of resources that are associated with a backup
        plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.get_backup_selection)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#get_backup_selection)
        """

    async def get_backup_vault_access_policy(
        self, *, BackupVaultName: str
    ) -> GetBackupVaultAccessPolicyOutputTypeDef:
        """
        Returns the access policy document that is associated with the named backup
        vault.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.get_backup_vault_access_policy)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#get_backup_vault_access_policy)
        """

    async def get_backup_vault_notifications(
        self, *, BackupVaultName: str
    ) -> GetBackupVaultNotificationsOutputTypeDef:
        """
        Returns event notifications for the specified backup vault.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.get_backup_vault_notifications)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#get_backup_vault_notifications)
        """

    async def get_legal_hold(self, *, LegalHoldId: str) -> GetLegalHoldOutputTypeDef:
        """
        This action returns details for a specified legal hold.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.get_legal_hold)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#get_legal_hold)
        """

    async def get_recovery_point_restore_metadata(
        self, *, BackupVaultName: str, RecoveryPointArn: str, BackupVaultAccountId: str = ...
    ) -> GetRecoveryPointRestoreMetadataOutputTypeDef:
        """
        Returns a set of metadata key-value pairs that were used to create the backup.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.get_recovery_point_restore_metadata)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#get_recovery_point_restore_metadata)
        """

    async def get_restore_job_metadata(
        self, *, RestoreJobId: str
    ) -> GetRestoreJobMetadataOutputTypeDef:
        """
        This request returns the metadata for the specified restore job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.get_restore_job_metadata)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#get_restore_job_metadata)
        """

    async def get_restore_testing_inferred_metadata(
        self, *, BackupVaultName: str, RecoveryPointArn: str, BackupVaultAccountId: str = ...
    ) -> GetRestoreTestingInferredMetadataOutputTypeDef:
        """
        This request returns the minimal required set of metadata needed to start a
        restore job with secure default
        settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.get_restore_testing_inferred_metadata)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#get_restore_testing_inferred_metadata)
        """

    async def get_restore_testing_plan(
        self, *, RestoreTestingPlanName: str
    ) -> GetRestoreTestingPlanOutputTypeDef:
        """
        Returns `RestoreTestingPlan` details for the specified `RestoreTestingPlanName`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.get_restore_testing_plan)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#get_restore_testing_plan)
        """

    async def get_restore_testing_selection(
        self, *, RestoreTestingPlanName: str, RestoreTestingSelectionName: str
    ) -> GetRestoreTestingSelectionOutputTypeDef:
        """
        Returns RestoreTestingSelection, which displays resources and elements of the
        restore testing
        plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.get_restore_testing_selection)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#get_restore_testing_selection)
        """

    async def get_supported_resource_types(self) -> GetSupportedResourceTypesOutputTypeDef:
        """
        Returns the Amazon Web Services resource types supported by Backup.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.get_supported_resource_types)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#get_supported_resource_types)
        """

    async def list_backup_job_summaries(
        self,
        *,
        AccountId: str = ...,
        State: BackupJobStatusType = ...,
        ResourceType: str = ...,
        MessageCategory: str = ...,
        AggregationPeriod: AggregationPeriodType = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
    ) -> ListBackupJobSummariesOutputTypeDef:
        """
        This is a request for a summary of backup jobs created or running within the
        most recent 30
        days.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.list_backup_job_summaries)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#list_backup_job_summaries)
        """

    async def list_backup_jobs(
        self,
        *,
        NextToken: str = ...,
        MaxResults: int = ...,
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
    ) -> ListBackupJobsOutputTypeDef:
        """
        Returns a list of existing backup jobs for an authenticated account for the
        last 30
        days.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.list_backup_jobs)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#list_backup_jobs)
        """

    async def list_backup_plan_templates(
        self, *, NextToken: str = ..., MaxResults: int = ...
    ) -> ListBackupPlanTemplatesOutputTypeDef:
        """
        Returns metadata of your saved backup plan templates, including the template
        ID, name, and the creation and deletion
        dates.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.list_backup_plan_templates)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#list_backup_plan_templates)
        """

    async def list_backup_plan_versions(
        self, *, BackupPlanId: str, NextToken: str = ..., MaxResults: int = ...
    ) -> ListBackupPlanVersionsOutputTypeDef:
        """
        Returns version metadata of your backup plans, including Amazon Resource Names
        (ARNs), backup plan IDs, creation and deletion dates, plan names, and version
        IDs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.list_backup_plan_versions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#list_backup_plan_versions)
        """

    async def list_backup_plans(
        self, *, NextToken: str = ..., MaxResults: int = ..., IncludeDeleted: bool = ...
    ) -> ListBackupPlansOutputTypeDef:
        """
        Returns a list of all active backup plans for an authenticated account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.list_backup_plans)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#list_backup_plans)
        """

    async def list_backup_selections(
        self, *, BackupPlanId: str, NextToken: str = ..., MaxResults: int = ...
    ) -> ListBackupSelectionsOutputTypeDef:
        """
        Returns an array containing metadata of the resources associated with the
        target backup
        plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.list_backup_selections)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#list_backup_selections)
        """

    async def list_backup_vaults(
        self,
        *,
        ByVaultType: VaultTypeType = ...,
        ByShared: bool = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
    ) -> ListBackupVaultsOutputTypeDef:
        """
        Returns a list of recovery point storage containers along with information
        about
        them.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.list_backup_vaults)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#list_backup_vaults)
        """

    async def list_copy_job_summaries(
        self,
        *,
        AccountId: str = ...,
        State: CopyJobStatusType = ...,
        ResourceType: str = ...,
        MessageCategory: str = ...,
        AggregationPeriod: AggregationPeriodType = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
    ) -> ListCopyJobSummariesOutputTypeDef:
        """
        This request obtains a list of copy jobs created or running within the the most
        recent 30
        days.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.list_copy_job_summaries)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#list_copy_job_summaries)
        """

    async def list_copy_jobs(
        self,
        *,
        NextToken: str = ...,
        MaxResults: int = ...,
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
    ) -> ListCopyJobsOutputTypeDef:
        """
        Returns metadata about your copy jobs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.list_copy_jobs)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#list_copy_jobs)
        """

    async def list_frameworks(
        self, *, MaxResults: int = ..., NextToken: str = ...
    ) -> ListFrameworksOutputTypeDef:
        """
        Returns a list of all frameworks for an Amazon Web Services account and Amazon
        Web Services
        Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.list_frameworks)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#list_frameworks)
        """

    async def list_legal_holds(
        self, *, NextToken: str = ..., MaxResults: int = ...
    ) -> ListLegalHoldsOutputTypeDef:
        """
        This action returns metadata about active and previous legal holds.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.list_legal_holds)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#list_legal_holds)
        """

    async def list_protected_resources(
        self, *, NextToken: str = ..., MaxResults: int = ...
    ) -> ListProtectedResourcesOutputTypeDef:
        """
        Returns an array of resources successfully backed up by Backup, including the
        time the resource was saved, an Amazon Resource Name (ARN) of the resource, and
        a resource
        type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.list_protected_resources)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#list_protected_resources)
        """

    async def list_protected_resources_by_backup_vault(
        self,
        *,
        BackupVaultName: str,
        BackupVaultAccountId: str = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
    ) -> ListProtectedResourcesByBackupVaultOutputTypeDef:
        """
        This request lists the protected resources corresponding to each backup vault.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.list_protected_resources_by_backup_vault)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#list_protected_resources_by_backup_vault)
        """

    async def list_recovery_points_by_backup_vault(
        self,
        *,
        BackupVaultName: str,
        BackupVaultAccountId: str = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
        ByResourceArn: str = ...,
        ByResourceType: str = ...,
        ByBackupPlanId: str = ...,
        ByCreatedBefore: TimestampTypeDef = ...,
        ByCreatedAfter: TimestampTypeDef = ...,
        ByParentRecoveryPointArn: str = ...,
    ) -> ListRecoveryPointsByBackupVaultOutputTypeDef:
        """
        Returns detailed information about the recovery points stored in a backup vault.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.list_recovery_points_by_backup_vault)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#list_recovery_points_by_backup_vault)
        """

    async def list_recovery_points_by_legal_hold(
        self, *, LegalHoldId: str, NextToken: str = ..., MaxResults: int = ...
    ) -> ListRecoveryPointsByLegalHoldOutputTypeDef:
        """
        This action returns recovery point ARNs (Amazon Resource Names) of the
        specified legal
        hold.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.list_recovery_points_by_legal_hold)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#list_recovery_points_by_legal_hold)
        """

    async def list_recovery_points_by_resource(
        self, *, ResourceArn: str, NextToken: str = ..., MaxResults: int = ...
    ) -> ListRecoveryPointsByResourceOutputTypeDef:
        """
        Returns detailed information about all the recovery points of the type
        specified by a resource Amazon Resource Name
        (ARN).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.list_recovery_points_by_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#list_recovery_points_by_resource)
        """

    async def list_report_jobs(
        self,
        *,
        ByReportPlanName: str = ...,
        ByCreationBefore: TimestampTypeDef = ...,
        ByCreationAfter: TimestampTypeDef = ...,
        ByStatus: str = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
    ) -> ListReportJobsOutputTypeDef:
        """
        Returns details about your report jobs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.list_report_jobs)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#list_report_jobs)
        """

    async def list_report_plans(
        self, *, MaxResults: int = ..., NextToken: str = ...
    ) -> ListReportPlansOutputTypeDef:
        """
        Returns a list of your report plans.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.list_report_plans)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#list_report_plans)
        """

    async def list_restore_job_summaries(
        self,
        *,
        AccountId: str = ...,
        State: RestoreJobStateType = ...,
        ResourceType: str = ...,
        AggregationPeriod: AggregationPeriodType = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
    ) -> ListRestoreJobSummariesOutputTypeDef:
        """
        This request obtains a summary of restore jobs created or running within the
        the most recent 30
        days.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.list_restore_job_summaries)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#list_restore_job_summaries)
        """

    async def list_restore_jobs(
        self,
        *,
        NextToken: str = ...,
        MaxResults: int = ...,
        ByAccountId: str = ...,
        ByResourceType: str = ...,
        ByCreatedBefore: TimestampTypeDef = ...,
        ByCreatedAfter: TimestampTypeDef = ...,
        ByStatus: RestoreJobStatusType = ...,
        ByCompleteBefore: TimestampTypeDef = ...,
        ByCompleteAfter: TimestampTypeDef = ...,
        ByRestoreTestingPlanArn: str = ...,
    ) -> ListRestoreJobsOutputTypeDef:
        """
        Returns a list of jobs that Backup initiated to restore a saved resource,
        including details about the recovery
        process.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.list_restore_jobs)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#list_restore_jobs)
        """

    async def list_restore_jobs_by_protected_resource(
        self,
        *,
        ResourceArn: str,
        ByStatus: RestoreJobStatusType = ...,
        ByRecoveryPointCreationDateAfter: TimestampTypeDef = ...,
        ByRecoveryPointCreationDateBefore: TimestampTypeDef = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
    ) -> ListRestoreJobsByProtectedResourceOutputTypeDef:
        """
        This returns restore jobs that contain the specified protected resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.list_restore_jobs_by_protected_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#list_restore_jobs_by_protected_resource)
        """

    async def list_restore_testing_plans(
        self, *, MaxResults: int = ..., NextToken: str = ...
    ) -> ListRestoreTestingPlansOutputTypeDef:
        """
        Returns a list of restore testing plans.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.list_restore_testing_plans)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#list_restore_testing_plans)
        """

    async def list_restore_testing_selections(
        self, *, RestoreTestingPlanName: str, MaxResults: int = ..., NextToken: str = ...
    ) -> ListRestoreTestingSelectionsOutputTypeDef:
        """
        Returns a list of restore testing selections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.list_restore_testing_selections)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#list_restore_testing_selections)
        """

    async def list_tags(
        self, *, ResourceArn: str, NextToken: str = ..., MaxResults: int = ...
    ) -> ListTagsOutputTypeDef:
        """
        Returns a list of key-value pairs assigned to a target recovery point, backup
        plan, or backup
        vault.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.list_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#list_tags)
        """

    async def put_backup_vault_access_policy(
        self, *, BackupVaultName: str, Policy: str = ...
    ) -> EmptyResponseMetadataTypeDef:
        """
        Sets a resource-based policy that is used to manage access permissions on the
        target backup
        vault.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.put_backup_vault_access_policy)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#put_backup_vault_access_policy)
        """

    async def put_backup_vault_lock_configuration(
        self,
        *,
        BackupVaultName: str,
        MinRetentionDays: int = ...,
        MaxRetentionDays: int = ...,
        ChangeableForDays: int = ...,
    ) -> EmptyResponseMetadataTypeDef:
        """
        Applies Backup Vault Lock to a backup vault, preventing attempts to delete any
        recovery point stored in or created in a backup
        vault.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.put_backup_vault_lock_configuration)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#put_backup_vault_lock_configuration)
        """

    async def put_backup_vault_notifications(
        self,
        *,
        BackupVaultName: str,
        SNSTopicArn: str,
        BackupVaultEvents: Sequence[BackupVaultEventType],
    ) -> EmptyResponseMetadataTypeDef:
        """
        Turns on notifications on a backup vault for the specified topic and events.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.put_backup_vault_notifications)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#put_backup_vault_notifications)
        """

    async def put_restore_validation_result(
        self,
        *,
        RestoreJobId: str,
        ValidationStatus: RestoreValidationStatusType,
        ValidationStatusMessage: str = ...,
    ) -> EmptyResponseMetadataTypeDef:
        """
        This request allows you to send your independent self-run restore test
        validation
        results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.put_restore_validation_result)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#put_restore_validation_result)
        """

    async def start_backup_job(
        self,
        *,
        BackupVaultName: str,
        ResourceArn: str,
        IamRoleArn: str,
        IdempotencyToken: str = ...,
        StartWindowMinutes: int = ...,
        CompleteWindowMinutes: int = ...,
        Lifecycle: LifecycleTypeDef = ...,
        RecoveryPointTags: Mapping[str, str] = ...,
        BackupOptions: Mapping[str, str] = ...,
    ) -> StartBackupJobOutputTypeDef:
        """
        Starts an on-demand backup job for the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.start_backup_job)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#start_backup_job)
        """

    async def start_copy_job(
        self,
        *,
        RecoveryPointArn: str,
        SourceBackupVaultName: str,
        DestinationBackupVaultArn: str,
        IamRoleArn: str,
        IdempotencyToken: str = ...,
        Lifecycle: LifecycleTypeDef = ...,
    ) -> StartCopyJobOutputTypeDef:
        """
        Starts a job to create a one-time copy of the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.start_copy_job)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#start_copy_job)
        """

    async def start_report_job(
        self, *, ReportPlanName: str, IdempotencyToken: str = ...
    ) -> StartReportJobOutputTypeDef:
        """
        Starts an on-demand report job for the specified report plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.start_report_job)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#start_report_job)
        """

    async def start_restore_job(
        self,
        *,
        RecoveryPointArn: str,
        Metadata: Mapping[str, str],
        IamRoleArn: str = ...,
        IdempotencyToken: str = ...,
        ResourceType: str = ...,
        CopySourceTagsToRestoredResource: bool = ...,
    ) -> StartRestoreJobOutputTypeDef:
        """
        Recovers the saved resource identified by an Amazon Resource Name (ARN).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.start_restore_job)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#start_restore_job)
        """

    async def stop_backup_job(self, *, BackupJobId: str) -> EmptyResponseMetadataTypeDef:
        """
        Attempts to cancel a job to create a one-time backup of a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.stop_backup_job)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#stop_backup_job)
        """

    async def tag_resource(
        self, *, ResourceArn: str, Tags: Mapping[str, str]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Assigns a set of key-value pairs to a recovery point, backup plan, or backup
        vault identified by an Amazon Resource Name
        (ARN).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.tag_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#tag_resource)
        """

    async def untag_resource(
        self, *, ResourceArn: str, TagKeyList: Sequence[str]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Removes a set of key-value pairs from a recovery point, backup plan, or backup
        vault identified by an Amazon Resource Name (ARN) See also: [AWS API
        Documentation](https://docs.aws.amazon.com/goto/WebAPI/backup-2018-11-15/UntagResource).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.untag_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#untag_resource)
        """

    async def update_backup_plan(
        self, *, BackupPlanId: str, BackupPlan: BackupPlanInputTypeDef
    ) -> UpdateBackupPlanOutputTypeDef:
        """
        Updates an existing backup plan identified by its `backupPlanId` with the input
        document in JSON
        format.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.update_backup_plan)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#update_backup_plan)
        """

    async def update_framework(
        self,
        *,
        FrameworkName: str,
        FrameworkDescription: str = ...,
        FrameworkControls: Sequence[FrameworkControlTypeDef] = ...,
        IdempotencyToken: str = ...,
    ) -> UpdateFrameworkOutputTypeDef:
        """
        Updates an existing framework identified by its `FrameworkName` with the input
        document in JSON
        format.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.update_framework)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#update_framework)
        """

    async def update_global_settings(
        self, *, GlobalSettings: Mapping[str, str] = ...
    ) -> EmptyResponseMetadataTypeDef:
        """
        Updates whether the Amazon Web Services account is opted in to cross-account
        backup.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.update_global_settings)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#update_global_settings)
        """

    async def update_recovery_point_lifecycle(
        self, *, BackupVaultName: str, RecoveryPointArn: str, Lifecycle: LifecycleTypeDef = ...
    ) -> UpdateRecoveryPointLifecycleOutputTypeDef:
        """
        Sets the transition lifecycle of a recovery point.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.update_recovery_point_lifecycle)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#update_recovery_point_lifecycle)
        """

    async def update_region_settings(
        self,
        *,
        ResourceTypeOptInPreference: Mapping[str, bool] = ...,
        ResourceTypeManagementPreference: Mapping[str, bool] = ...,
    ) -> EmptyResponseMetadataTypeDef:
        """
        Updates the current service opt-in settings for the Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.update_region_settings)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#update_region_settings)
        """

    async def update_report_plan(
        self,
        *,
        ReportPlanName: str,
        ReportPlanDescription: str = ...,
        ReportDeliveryChannel: ReportDeliveryChannelTypeDef = ...,
        ReportSetting: ReportSettingTypeDef = ...,
        IdempotencyToken: str = ...,
    ) -> UpdateReportPlanOutputTypeDef:
        """
        Updates an existing report plan identified by its `ReportPlanName` with the
        input document in JSON
        format.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.update_report_plan)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#update_report_plan)
        """

    async def update_restore_testing_plan(
        self, *, RestoreTestingPlan: RestoreTestingPlanForUpdateTypeDef, RestoreTestingPlanName: str
    ) -> UpdateRestoreTestingPlanOutputTypeDef:
        """
        This request will send changes to your specified restore testing plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.update_restore_testing_plan)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#update_restore_testing_plan)
        """

    async def update_restore_testing_selection(
        self,
        *,
        RestoreTestingPlanName: str,
        RestoreTestingSelection: RestoreTestingSelectionForUpdateTypeDef,
        RestoreTestingSelectionName: str,
    ) -> UpdateRestoreTestingSelectionOutputTypeDef:
        """
        Most elements except the `RestoreTestingSelectionName` can be updated with this
        request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.update_restore_testing_selection)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#update_restore_testing_selection)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_backup_jobs"]) -> ListBackupJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_backup_plan_templates"]
    ) -> ListBackupPlanTemplatesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_backup_plan_versions"]
    ) -> ListBackupPlanVersionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_backup_plans"]
    ) -> ListBackupPlansPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_backup_selections"]
    ) -> ListBackupSelectionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_backup_vaults"]
    ) -> ListBackupVaultsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_copy_jobs"]) -> ListCopyJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_legal_holds"]) -> ListLegalHoldsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_protected_resources"]
    ) -> ListProtectedResourcesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_protected_resources_by_backup_vault"]
    ) -> ListProtectedResourcesByBackupVaultPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_recovery_points_by_backup_vault"]
    ) -> ListRecoveryPointsByBackupVaultPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_recovery_points_by_legal_hold"]
    ) -> ListRecoveryPointsByLegalHoldPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_recovery_points_by_resource"]
    ) -> ListRecoveryPointsByResourcePaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_restore_jobs"]
    ) -> ListRestoreJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_restore_jobs_by_protected_resource"]
    ) -> ListRestoreJobsByProtectedResourcePaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_restore_testing_plans"]
    ) -> ListRestoreTestingPlansPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_restore_testing_selections"]
    ) -> ListRestoreTestingSelectionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/#get_paginator)
        """

    async def __aenter__(self) -> "BackupClient":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/)
        """

    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> Any:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_backup/client/)
        """
