"""
Type annotations for ssm service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/type_defs/)

Usage::

    ```python
    from mypy_boto3_ssm.type_defs import AccountSharingInfoTypeDef

    data: AccountSharingInfoTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List, Mapping, Sequence, Union

from .literals import (
    AssociationComplianceSeverityType,
    AssociationExecutionFilterKeyType,
    AssociationExecutionTargetsFilterKeyType,
    AssociationFilterKeyType,
    AssociationFilterOperatorTypeType,
    AssociationStatusNameType,
    AssociationSyncComplianceType,
    AttachmentsSourceKeyType,
    AutomationExecutionFilterKeyType,
    AutomationExecutionStatusType,
    AutomationTypeType,
    CalendarStateType,
    CommandFilterKeyType,
    CommandInvocationStatusType,
    CommandPluginStatusType,
    CommandStatusType,
    ComplianceQueryOperatorTypeType,
    ComplianceSeverityType,
    ComplianceStatusType,
    ComplianceUploadTypeType,
    ConnectionStatusType,
    DescribeActivationsFilterKeysType,
    DocumentFilterKeyType,
    DocumentFormatType,
    DocumentHashTypeType,
    DocumentParameterTypeType,
    DocumentReviewActionType,
    DocumentStatusType,
    DocumentTypeType,
    ExecutionModeType,
    ExternalAlarmStateType,
    FaultType,
    InstanceInformationFilterKeyType,
    InstancePatchStateOperatorTypeType,
    InventoryAttributeDataTypeType,
    InventoryDeletionStatusType,
    InventoryQueryOperatorTypeType,
    InventorySchemaDeleteOptionType,
    LastResourceDataSyncStatusType,
    MaintenanceWindowExecutionStatusType,
    MaintenanceWindowResourceTypeType,
    MaintenanceWindowTaskCutoffBehaviorType,
    MaintenanceWindowTaskTypeType,
    NotificationEventType,
    NotificationTypeType,
    OperatingSystemType,
    OpsFilterOperatorTypeType,
    OpsItemDataTypeType,
    OpsItemFilterKeyType,
    OpsItemFilterOperatorType,
    OpsItemRelatedItemsFilterKeyType,
    OpsItemStatusType,
    ParametersFilterKeyType,
    ParameterTierType,
    ParameterTypeType,
    PatchActionType,
    PatchComplianceDataStateType,
    PatchComplianceLevelType,
    PatchDeploymentStatusType,
    PatchFilterKeyType,
    PatchOperationTypeType,
    PatchPropertyType,
    PatchSetType,
    PingStatusType,
    PlatformTypeType,
    RebootOptionType,
    ResourceTypeForTaggingType,
    ResourceTypeType,
    ReviewStatusType,
    SessionFilterKeyType,
    SessionStateType,
    SessionStatusType,
    SignalTypeType,
    SourceTypeType,
    StepExecutionFilterKeyType,
    StopTypeType,
)

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 12):
    from typing import NotRequired
else:
    from typing_extensions import NotRequired
if sys.version_info >= (3, 12):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AccountSharingInfoTypeDef",
    "TagTypeDef",
    "AlarmTypeDef",
    "AlarmStateInformationTypeDef",
    "AssociateOpsItemRelatedItemRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "AssociationOverviewTypeDef",
    "AssociationStatusTypeDef",
    "TargetTypeDef",
    "AssociationExecutionFilterTypeDef",
    "OutputSourceTypeDef",
    "AssociationExecutionTargetsFilterTypeDef",
    "AssociationFilterTypeDef",
    "TargetPaginatorTypeDef",
    "AttachmentContentTypeDef",
    "AttachmentInformationTypeDef",
    "AttachmentsSourceTypeDef",
    "AutomationExecutionFilterTypeDef",
    "ResolvedTargetsTypeDef",
    "ProgressCountersTypeDef",
    "PatchSourceTypeDef",
    "CancelCommandRequestRequestTypeDef",
    "CancelMaintenanceWindowExecutionRequestRequestTypeDef",
    "CloudWatchOutputConfigTypeDef",
    "CommandFilterTypeDef",
    "CommandPluginTypeDef",
    "NotificationConfigTypeDef",
    "ComplianceExecutionSummaryTypeDef",
    "ComplianceItemEntryTypeDef",
    "ComplianceStringFilterTypeDef",
    "SeveritySummaryTypeDef",
    "RegistrationMetadataItemTypeDef",
    "TimestampTypeDef",
    "DocumentRequiresTypeDef",
    "OpsItemDataValueTypeDef",
    "OpsItemNotificationTypeDef",
    "RelatedOpsItemTypeDef",
    "MetadataValueTypeDef",
    "DeleteActivationRequestRequestTypeDef",
    "DeleteAssociationRequestRequestTypeDef",
    "DeleteDocumentRequestRequestTypeDef",
    "DeleteInventoryRequestRequestTypeDef",
    "DeleteMaintenanceWindowRequestRequestTypeDef",
    "DeleteOpsItemRequestRequestTypeDef",
    "DeleteOpsMetadataRequestRequestTypeDef",
    "DeleteParameterRequestRequestTypeDef",
    "DeleteParametersRequestRequestTypeDef",
    "DeletePatchBaselineRequestRequestTypeDef",
    "DeleteResourceDataSyncRequestRequestTypeDef",
    "DeleteResourcePolicyRequestRequestTypeDef",
    "DeregisterManagedInstanceRequestRequestTypeDef",
    "DeregisterPatchBaselineForPatchGroupRequestRequestTypeDef",
    "DeregisterTargetFromMaintenanceWindowRequestRequestTypeDef",
    "DeregisterTaskFromMaintenanceWindowRequestRequestTypeDef",
    "DescribeActivationsFilterTypeDef",
    "PaginatorConfigTypeDef",
    "DescribeAssociationRequestRequestTypeDef",
    "StepExecutionFilterTypeDef",
    "PatchOrchestratorFilterTypeDef",
    "PatchTypeDef",
    "DescribeDocumentPermissionRequestRequestTypeDef",
    "DescribeDocumentRequestRequestTypeDef",
    "DescribeEffectiveInstanceAssociationsRequestRequestTypeDef",
    "InstanceAssociationTypeDef",
    "DescribeEffectivePatchesForPatchBaselineRequestRequestTypeDef",
    "DescribeInstanceAssociationsStatusRequestRequestTypeDef",
    "InstanceInformationFilterTypeDef",
    "InstanceInformationStringFilterTypeDef",
    "InstancePatchStateFilterTypeDef",
    "InstancePatchStateTypeDef",
    "DescribeInstancePatchStatesRequestRequestTypeDef",
    "PatchComplianceDataTypeDef",
    "DescribeInventoryDeletionsRequestRequestTypeDef",
    "MaintenanceWindowFilterTypeDef",
    "MaintenanceWindowExecutionTaskInvocationIdentityTypeDef",
    "MaintenanceWindowExecutionTypeDef",
    "ScheduledWindowExecutionTypeDef",
    "MaintenanceWindowIdentityForTargetTypeDef",
    "MaintenanceWindowIdentityTypeDef",
    "OpsItemFilterTypeDef",
    "ParameterStringFilterTypeDef",
    "ParametersFilterTypeDef",
    "PatchBaselineIdentityTypeDef",
    "DescribePatchGroupStateRequestRequestTypeDef",
    "DescribePatchPropertiesRequestRequestTypeDef",
    "SessionFilterTypeDef",
    "DisassociateOpsItemRelatedItemRequestRequestTypeDef",
    "DocumentDefaultVersionDescriptionTypeDef",
    "DocumentParameterTypeDef",
    "ReviewInformationTypeDef",
    "DocumentFilterTypeDef",
    "DocumentKeyValuesFilterTypeDef",
    "DocumentReviewCommentSourceTypeDef",
    "DocumentVersionInfoTypeDef",
    "PatchStatusTypeDef",
    "FailureDetailsTypeDef",
    "GetAutomationExecutionRequestRequestTypeDef",
    "GetCalendarStateRequestRequestTypeDef",
    "WaiterConfigTypeDef",
    "GetCommandInvocationRequestRequestTypeDef",
    "GetConnectionStatusRequestRequestTypeDef",
    "GetDefaultPatchBaselineRequestRequestTypeDef",
    "GetDocumentRequestRequestTypeDef",
    "InventoryFilterTypeDef",
    "ResultAttributeTypeDef",
    "GetInventorySchemaRequestRequestTypeDef",
    "GetMaintenanceWindowExecutionRequestRequestTypeDef",
    "GetMaintenanceWindowExecutionTaskInvocationRequestRequestTypeDef",
    "GetMaintenanceWindowExecutionTaskRequestRequestTypeDef",
    "MaintenanceWindowTaskParameterValueExpressionTypeDef",
    "GetMaintenanceWindowRequestRequestTypeDef",
    "GetMaintenanceWindowTaskRequestRequestTypeDef",
    "LoggingInfoTypeDef",
    "GetOpsItemRequestRequestTypeDef",
    "GetOpsMetadataRequestRequestTypeDef",
    "OpsFilterTypeDef",
    "OpsResultAttributeTypeDef",
    "GetParameterHistoryRequestRequestTypeDef",
    "GetParameterRequestRequestTypeDef",
    "ParameterTypeDef",
    "GetParametersRequestRequestTypeDef",
    "GetPatchBaselineForPatchGroupRequestRequestTypeDef",
    "GetPatchBaselineRequestRequestTypeDef",
    "GetResourcePoliciesRequestRequestTypeDef",
    "GetResourcePoliciesResponseEntryTypeDef",
    "GetServiceSettingRequestRequestTypeDef",
    "ServiceSettingTypeDef",
    "InstanceAggregatedAssociationOverviewTypeDef",
    "S3OutputLocationTypeDef",
    "S3OutputUrlTypeDef",
    "InventoryDeletionSummaryItemTypeDef",
    "InventoryItemAttributeTypeDef",
    "InventoryItemTypeDef",
    "InventoryResultItemTypeDef",
    "LabelParameterVersionRequestRequestTypeDef",
    "ListAssociationVersionsRequestRequestTypeDef",
    "ListDocumentMetadataHistoryRequestRequestTypeDef",
    "ListDocumentVersionsRequestRequestTypeDef",
    "OpsItemEventFilterTypeDef",
    "OpsItemRelatedItemsFilterTypeDef",
    "OpsMetadataFilterTypeDef",
    "OpsMetadataTypeDef",
    "ListResourceDataSyncRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "MaintenanceWindowAutomationParametersTypeDef",
    "MaintenanceWindowLambdaParametersTypeDef",
    "MaintenanceWindowStepFunctionsParametersTypeDef",
    "ModifyDocumentPermissionRequestRequestTypeDef",
    "OpsEntityItemTypeDef",
    "OpsItemIdentityTypeDef",
    "ParameterInlinePolicyTypeDef",
    "ParentStepDetailsTypeDef",
    "PatchFilterTypeDef",
    "PutResourcePolicyRequestRequestTypeDef",
    "RegisterDefaultPatchBaselineRequestRequestTypeDef",
    "RegisterPatchBaselineForPatchGroupRequestRequestTypeDef",
    "RemoveTagsFromResourceRequestRequestTypeDef",
    "ResetServiceSettingRequestRequestTypeDef",
    "ResourceDataSyncOrganizationalUnitTypeDef",
    "ResourceDataSyncDestinationDataSharingTypeDef",
    "ResumeSessionRequestRequestTypeDef",
    "SendAutomationSignalRequestRequestTypeDef",
    "SessionManagerOutputUrlTypeDef",
    "StartAssociationsOnceRequestRequestTypeDef",
    "StartSessionRequestRequestTypeDef",
    "StopAutomationExecutionRequestRequestTypeDef",
    "TerminateSessionRequestRequestTypeDef",
    "UnlabelParameterVersionRequestRequestTypeDef",
    "UpdateDocumentDefaultVersionRequestRequestTypeDef",
    "UpdateMaintenanceWindowRequestRequestTypeDef",
    "UpdateManagedInstanceRoleRequestRequestTypeDef",
    "UpdateServiceSettingRequestRequestTypeDef",
    "ActivationTypeDef",
    "AddTagsToResourceRequestRequestTypeDef",
    "CreateMaintenanceWindowRequestRequestTypeDef",
    "PutParameterRequestRequestTypeDef",
    "AlarmConfigurationPaginatorTypeDef",
    "AlarmConfigurationTypeDef",
    "AssociateOpsItemRelatedItemResponseTypeDef",
    "CancelMaintenanceWindowExecutionResultTypeDef",
    "CreateActivationResultTypeDef",
    "CreateMaintenanceWindowResultTypeDef",
    "CreateOpsItemResponseTypeDef",
    "CreateOpsMetadataResultTypeDef",
    "CreatePatchBaselineResultTypeDef",
    "DeleteMaintenanceWindowResultTypeDef",
    "DeleteParametersResultTypeDef",
    "DeletePatchBaselineResultTypeDef",
    "DeregisterPatchBaselineForPatchGroupResultTypeDef",
    "DeregisterTargetFromMaintenanceWindowResultTypeDef",
    "DeregisterTaskFromMaintenanceWindowResultTypeDef",
    "DescribeDocumentPermissionResponseTypeDef",
    "DescribePatchGroupStateResultTypeDef",
    "DescribePatchPropertiesResultTypeDef",
    "GetCalendarStateResponseTypeDef",
    "GetConnectionStatusResponseTypeDef",
    "GetDefaultPatchBaselineResultTypeDef",
    "GetDeployablePatchSnapshotForInstanceResultTypeDef",
    "GetMaintenanceWindowExecutionResultTypeDef",
    "GetMaintenanceWindowExecutionTaskInvocationResultTypeDef",
    "GetMaintenanceWindowResultTypeDef",
    "GetPatchBaselineForPatchGroupResultTypeDef",
    "LabelParameterVersionResultTypeDef",
    "ListInventoryEntriesResultTypeDef",
    "ListTagsForResourceResultTypeDef",
    "PutInventoryResultTypeDef",
    "PutParameterResultTypeDef",
    "PutResourcePolicyResponseTypeDef",
    "RegisterDefaultPatchBaselineResultTypeDef",
    "RegisterPatchBaselineForPatchGroupResultTypeDef",
    "RegisterTargetWithMaintenanceWindowResultTypeDef",
    "RegisterTaskWithMaintenanceWindowResultTypeDef",
    "ResumeSessionResponseTypeDef",
    "StartAutomationExecutionResultTypeDef",
    "StartChangeRequestExecutionResultTypeDef",
    "StartSessionResponseTypeDef",
    "TerminateSessionResponseTypeDef",
    "UnlabelParameterVersionResultTypeDef",
    "UpdateMaintenanceWindowResultTypeDef",
    "UpdateOpsMetadataResultTypeDef",
    "UpdateAssociationStatusRequestRequestTypeDef",
    "AssociationTypeDef",
    "DescribeMaintenanceWindowsForTargetRequestRequestTypeDef",
    "MaintenanceWindowTargetTypeDef",
    "RegisterTargetWithMaintenanceWindowRequestRequestTypeDef",
    "UpdateMaintenanceWindowTargetRequestRequestTypeDef",
    "UpdateMaintenanceWindowTargetResultTypeDef",
    "DescribeAssociationExecutionsRequestRequestTypeDef",
    "AssociationExecutionTargetTypeDef",
    "DescribeAssociationExecutionTargetsRequestRequestTypeDef",
    "ListAssociationsRequestRequestTypeDef",
    "AssociationPaginatorTypeDef",
    "MaintenanceWindowTargetPaginatorTypeDef",
    "UpdateDocumentRequestRequestTypeDef",
    "DescribeAutomationExecutionsRequestRequestTypeDef",
    "GetCommandInvocationResultTypeDef",
    "ListCommandInvocationsRequestRequestTypeDef",
    "ListCommandsRequestRequestTypeDef",
    "CommandInvocationTypeDef",
    "MaintenanceWindowRunCommandParametersTypeDef",
    "ComplianceItemTypeDef",
    "PutComplianceItemsRequestRequestTypeDef",
    "ListComplianceItemsRequestRequestTypeDef",
    "ListComplianceSummariesRequestRequestTypeDef",
    "ListResourceComplianceSummariesRequestRequestTypeDef",
    "CompliantSummaryTypeDef",
    "NonCompliantSummaryTypeDef",
    "CreateActivationRequestRequestTypeDef",
    "CreateDocumentRequestRequestTypeDef",
    "DocumentIdentifierTypeDef",
    "GetDocumentResultTypeDef",
    "OpsItemSummaryTypeDef",
    "CreateOpsItemRequestRequestTypeDef",
    "OpsItemTypeDef",
    "UpdateOpsItemRequestRequestTypeDef",
    "CreateOpsMetadataRequestRequestTypeDef",
    "GetOpsMetadataResultTypeDef",
    "UpdateOpsMetadataRequestRequestTypeDef",
    "DescribeActivationsRequestRequestTypeDef",
    "DescribeActivationsRequestDescribeActivationsPaginateTypeDef",
    "DescribeAssociationExecutionTargetsRequestDescribeAssociationExecutionTargetsPaginateTypeDef",
    "DescribeAssociationExecutionsRequestDescribeAssociationExecutionsPaginateTypeDef",
    "DescribeAutomationExecutionsRequestDescribeAutomationExecutionsPaginateTypeDef",
    "DescribeEffectiveInstanceAssociationsRequestDescribeEffectiveInstanceAssociationsPaginateTypeDef",
    "DescribeEffectivePatchesForPatchBaselineRequestDescribeEffectivePatchesForPatchBaselinePaginateTypeDef",
    "DescribeInstanceAssociationsStatusRequestDescribeInstanceAssociationsStatusPaginateTypeDef",
    "DescribeInstancePatchStatesRequestDescribeInstancePatchStatesPaginateTypeDef",
    "DescribeInventoryDeletionsRequestDescribeInventoryDeletionsPaginateTypeDef",
    "DescribeMaintenanceWindowsForTargetRequestDescribeMaintenanceWindowsForTargetPaginateTypeDef",
    "DescribePatchPropertiesRequestDescribePatchPropertiesPaginateTypeDef",
    "GetInventorySchemaRequestGetInventorySchemaPaginateTypeDef",
    "GetParameterHistoryRequestGetParameterHistoryPaginateTypeDef",
    "GetResourcePoliciesRequestGetResourcePoliciesPaginateTypeDef",
    "ListAssociationVersionsRequestListAssociationVersionsPaginateTypeDef",
    "ListAssociationsRequestListAssociationsPaginateTypeDef",
    "ListCommandInvocationsRequestListCommandInvocationsPaginateTypeDef",
    "ListCommandsRequestListCommandsPaginateTypeDef",
    "ListComplianceItemsRequestListComplianceItemsPaginateTypeDef",
    "ListComplianceSummariesRequestListComplianceSummariesPaginateTypeDef",
    "ListDocumentVersionsRequestListDocumentVersionsPaginateTypeDef",
    "ListResourceComplianceSummariesRequestListResourceComplianceSummariesPaginateTypeDef",
    "ListResourceDataSyncRequestListResourceDataSyncPaginateTypeDef",
    "DescribeAutomationStepExecutionsRequestDescribeAutomationStepExecutionsPaginateTypeDef",
    "DescribeAutomationStepExecutionsRequestRequestTypeDef",
    "DescribeAvailablePatchesRequestDescribeAvailablePatchesPaginateTypeDef",
    "DescribeAvailablePatchesRequestRequestTypeDef",
    "DescribeInstancePatchesRequestDescribeInstancePatchesPaginateTypeDef",
    "DescribeInstancePatchesRequestRequestTypeDef",
    "DescribeMaintenanceWindowScheduleRequestDescribeMaintenanceWindowSchedulePaginateTypeDef",
    "DescribeMaintenanceWindowScheduleRequestRequestTypeDef",
    "DescribePatchBaselinesRequestDescribePatchBaselinesPaginateTypeDef",
    "DescribePatchBaselinesRequestRequestTypeDef",
    "DescribePatchGroupsRequestDescribePatchGroupsPaginateTypeDef",
    "DescribePatchGroupsRequestRequestTypeDef",
    "DescribeAvailablePatchesResultTypeDef",
    "DescribeEffectiveInstanceAssociationsResultTypeDef",
    "DescribeInstanceInformationRequestDescribeInstanceInformationPaginateTypeDef",
    "DescribeInstanceInformationRequestRequestTypeDef",
    "DescribeInstancePatchStatesForPatchGroupRequestDescribeInstancePatchStatesForPatchGroupPaginateTypeDef",
    "DescribeInstancePatchStatesForPatchGroupRequestRequestTypeDef",
    "DescribeInstancePatchStatesForPatchGroupResultTypeDef",
    "DescribeInstancePatchStatesResultTypeDef",
    "DescribeInstancePatchesResultTypeDef",
    "DescribeMaintenanceWindowExecutionTaskInvocationsRequestDescribeMaintenanceWindowExecutionTaskInvocationsPaginateTypeDef",
    "DescribeMaintenanceWindowExecutionTaskInvocationsRequestRequestTypeDef",
    "DescribeMaintenanceWindowExecutionTasksRequestDescribeMaintenanceWindowExecutionTasksPaginateTypeDef",
    "DescribeMaintenanceWindowExecutionTasksRequestRequestTypeDef",
    "DescribeMaintenanceWindowExecutionsRequestDescribeMaintenanceWindowExecutionsPaginateTypeDef",
    "DescribeMaintenanceWindowExecutionsRequestRequestTypeDef",
    "DescribeMaintenanceWindowTargetsRequestDescribeMaintenanceWindowTargetsPaginateTypeDef",
    "DescribeMaintenanceWindowTargetsRequestRequestTypeDef",
    "DescribeMaintenanceWindowTasksRequestDescribeMaintenanceWindowTasksPaginateTypeDef",
    "DescribeMaintenanceWindowTasksRequestRequestTypeDef",
    "DescribeMaintenanceWindowsRequestDescribeMaintenanceWindowsPaginateTypeDef",
    "DescribeMaintenanceWindowsRequestRequestTypeDef",
    "DescribeMaintenanceWindowExecutionTaskInvocationsResultTypeDef",
    "DescribeMaintenanceWindowExecutionsResultTypeDef",
    "DescribeMaintenanceWindowScheduleResultTypeDef",
    "DescribeMaintenanceWindowsForTargetResultTypeDef",
    "DescribeMaintenanceWindowsResultTypeDef",
    "DescribeOpsItemsRequestDescribeOpsItemsPaginateTypeDef",
    "DescribeOpsItemsRequestRequestTypeDef",
    "GetParametersByPathRequestGetParametersByPathPaginateTypeDef",
    "GetParametersByPathRequestRequestTypeDef",
    "DescribeParametersRequestDescribeParametersPaginateTypeDef",
    "DescribeParametersRequestRequestTypeDef",
    "DescribePatchBaselinesResultTypeDef",
    "PatchGroupPatchBaselineMappingTypeDef",
    "DescribeSessionsRequestDescribeSessionsPaginateTypeDef",
    "DescribeSessionsRequestRequestTypeDef",
    "UpdateDocumentDefaultVersionResultTypeDef",
    "DocumentDescriptionTypeDef",
    "ListDocumentsRequestListDocumentsPaginateTypeDef",
    "ListDocumentsRequestRequestTypeDef",
    "DocumentReviewerResponseSourceTypeDef",
    "DocumentReviewsTypeDef",
    "ListDocumentVersionsResultTypeDef",
    "EffectivePatchTypeDef",
    "GetCommandInvocationRequestCommandExecutedWaitTypeDef",
    "InventoryGroupTypeDef",
    "ListInventoryEntriesRequestRequestTypeDef",
    "GetInventoryRequestRequestTypeDef",
    "OpsAggregatorTypeDef",
    "GetOpsSummaryRequestRequestTypeDef",
    "GetParameterResultTypeDef",
    "GetParametersByPathResultTypeDef",
    "GetParametersResultTypeDef",
    "GetResourcePoliciesResponseTypeDef",
    "GetServiceSettingResultTypeDef",
    "ResetServiceSettingResultTypeDef",
    "InstanceInformationTypeDef",
    "InstanceAssociationOutputLocationTypeDef",
    "InstanceAssociationOutputUrlTypeDef",
    "InventoryDeletionSummaryTypeDef",
    "InventoryItemSchemaTypeDef",
    "PutInventoryRequestRequestTypeDef",
    "InventoryResultEntityTypeDef",
    "ListOpsItemEventsRequestListOpsItemEventsPaginateTypeDef",
    "ListOpsItemEventsRequestRequestTypeDef",
    "ListOpsItemRelatedItemsRequestListOpsItemRelatedItemsPaginateTypeDef",
    "ListOpsItemRelatedItemsRequestRequestTypeDef",
    "ListOpsMetadataRequestListOpsMetadataPaginateTypeDef",
    "ListOpsMetadataRequestRequestTypeDef",
    "ListOpsMetadataResultTypeDef",
    "OpsEntityTypeDef",
    "OpsItemEventSummaryTypeDef",
    "OpsItemRelatedItemSummaryTypeDef",
    "ParameterHistoryTypeDef",
    "ParameterMetadataTypeDef",
    "PatchFilterGroupTypeDef",
    "ResourceDataSyncAwsOrganizationsSourcePaginatorTypeDef",
    "ResourceDataSyncAwsOrganizationsSourceTypeDef",
    "ResourceDataSyncS3DestinationTypeDef",
    "SessionTypeDef",
    "DescribeActivationsResultTypeDef",
    "AssociationExecutionPaginatorTypeDef",
    "CommandPaginatorTypeDef",
    "MaintenanceWindowExecutionTaskIdentityPaginatorTypeDef",
    "MaintenanceWindowTaskPaginatorTypeDef",
    "TargetLocationPaginatorTypeDef",
    "AssociationExecutionTypeDef",
    "CommandTypeDef",
    "GetMaintenanceWindowExecutionTaskResultTypeDef",
    "MaintenanceWindowExecutionTaskIdentityTypeDef",
    "MaintenanceWindowTaskTypeDef",
    "SendCommandRequestRequestTypeDef",
    "TargetLocationTypeDef",
    "ListAssociationsResultTypeDef",
    "DescribeMaintenanceWindowTargetsResultTypeDef",
    "DescribeAssociationExecutionTargetsResultTypeDef",
    "ListAssociationsResultPaginatorTypeDef",
    "DescribeMaintenanceWindowTargetsResultPaginatorTypeDef",
    "ListCommandInvocationsResultTypeDef",
    "MaintenanceWindowTaskInvocationParametersTypeDef",
    "ListComplianceItemsResultTypeDef",
    "ComplianceSummaryItemTypeDef",
    "ResourceComplianceSummaryItemTypeDef",
    "ListDocumentsResultTypeDef",
    "DescribeOpsItemsResponseTypeDef",
    "GetOpsItemResponseTypeDef",
    "DescribePatchGroupsResultTypeDef",
    "CreateDocumentResultTypeDef",
    "DescribeDocumentResultTypeDef",
    "UpdateDocumentResultTypeDef",
    "DocumentMetadataResponseInfoTypeDef",
    "UpdateDocumentMetadataRequestRequestTypeDef",
    "DescribeEffectivePatchesForPatchBaselineResultTypeDef",
    "InventoryAggregatorTypeDef",
    "GetOpsSummaryRequestGetOpsSummaryPaginateTypeDef",
    "DescribeInstanceInformationResultTypeDef",
    "InstanceAssociationStatusInfoTypeDef",
    "DeleteInventoryResultTypeDef",
    "InventoryDeletionStatusItemTypeDef",
    "GetInventorySchemaResultTypeDef",
    "GetInventoryResultTypeDef",
    "GetOpsSummaryResultTypeDef",
    "ListOpsItemEventsResponseTypeDef",
    "ListOpsItemRelatedItemsResponseTypeDef",
    "GetParameterHistoryResultTypeDef",
    "DescribeParametersResultTypeDef",
    "PatchRuleTypeDef",
    "ResourceDataSyncSourceWithStatePaginatorTypeDef",
    "ResourceDataSyncSourceTypeDef",
    "ResourceDataSyncSourceWithStateTypeDef",
    "DescribeSessionsResponseTypeDef",
    "DescribeAssociationExecutionsResultPaginatorTypeDef",
    "ListCommandsResultPaginatorTypeDef",
    "DescribeMaintenanceWindowExecutionTasksResultPaginatorTypeDef",
    "DescribeMaintenanceWindowTasksResultPaginatorTypeDef",
    "AssociationVersionInfoPaginatorTypeDef",
    "RunbookPaginatorTypeDef",
    "StepExecutionPaginatorTypeDef",
    "DescribeAssociationExecutionsResultTypeDef",
    "ListCommandsResultTypeDef",
    "SendCommandResultTypeDef",
    "DescribeMaintenanceWindowExecutionTasksResultTypeDef",
    "DescribeMaintenanceWindowTasksResultTypeDef",
    "AssociationDescriptionTypeDef",
    "AssociationVersionInfoTypeDef",
    "CreateAssociationBatchRequestEntryTypeDef",
    "CreateAssociationRequestRequestTypeDef",
    "RunbookTypeDef",
    "StartAutomationExecutionRequestRequestTypeDef",
    "StepExecutionTypeDef",
    "UpdateAssociationRequestRequestTypeDef",
    "GetMaintenanceWindowTaskResultTypeDef",
    "RegisterTaskWithMaintenanceWindowRequestRequestTypeDef",
    "UpdateMaintenanceWindowTaskRequestRequestTypeDef",
    "UpdateMaintenanceWindowTaskResultTypeDef",
    "ListComplianceSummariesResultTypeDef",
    "ListResourceComplianceSummariesResultTypeDef",
    "ListDocumentMetadataHistoryResponseTypeDef",
    "GetInventoryRequestGetInventoryPaginateTypeDef",
    "DescribeInstanceAssociationsStatusResultTypeDef",
    "DescribeInventoryDeletionsResultTypeDef",
    "PatchRuleGroupTypeDef",
    "ResourceDataSyncItemPaginatorTypeDef",
    "CreateResourceDataSyncRequestRequestTypeDef",
    "UpdateResourceDataSyncRequestRequestTypeDef",
    "ResourceDataSyncItemTypeDef",
    "ListAssociationVersionsResultPaginatorTypeDef",
    "AutomationExecutionMetadataPaginatorTypeDef",
    "DescribeAutomationStepExecutionsResultPaginatorTypeDef",
    "CreateAssociationResultTypeDef",
    "DescribeAssociationResultTypeDef",
    "UpdateAssociationResultTypeDef",
    "UpdateAssociationStatusResultTypeDef",
    "ListAssociationVersionsResultTypeDef",
    "CreateAssociationBatchRequestRequestTypeDef",
    "FailedCreateAssociationTypeDef",
    "AutomationExecutionMetadataTypeDef",
    "StartChangeRequestExecutionRequestRequestTypeDef",
    "AutomationExecutionTypeDef",
    "DescribeAutomationStepExecutionsResultTypeDef",
    "BaselineOverrideTypeDef",
    "CreatePatchBaselineRequestRequestTypeDef",
    "GetPatchBaselineResultTypeDef",
    "UpdatePatchBaselineRequestRequestTypeDef",
    "UpdatePatchBaselineResultTypeDef",
    "ListResourceDataSyncResultPaginatorTypeDef",
    "ListResourceDataSyncResultTypeDef",
    "DescribeAutomationExecutionsResultPaginatorTypeDef",
    "CreateAssociationBatchResultTypeDef",
    "DescribeAutomationExecutionsResultTypeDef",
    "GetAutomationExecutionResultTypeDef",
    "GetDeployablePatchSnapshotForInstanceRequestRequestTypeDef",
)

AccountSharingInfoTypeDef = TypedDict(
    "AccountSharingInfoTypeDef",
    {
        "AccountId": NotRequired[str],
        "SharedDocumentVersion": NotRequired[str],
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)
AlarmTypeDef = TypedDict(
    "AlarmTypeDef",
    {
        "Name": str,
    },
)
AlarmStateInformationTypeDef = TypedDict(
    "AlarmStateInformationTypeDef",
    {
        "Name": str,
        "State": ExternalAlarmStateType,
    },
)
AssociateOpsItemRelatedItemRequestRequestTypeDef = TypedDict(
    "AssociateOpsItemRelatedItemRequestRequestTypeDef",
    {
        "OpsItemId": str,
        "AssociationType": str,
        "ResourceType": str,
        "ResourceUri": str,
    },
)
ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, str],
        "RetryAttempts": int,
    },
)
AssociationOverviewTypeDef = TypedDict(
    "AssociationOverviewTypeDef",
    {
        "Status": NotRequired[str],
        "DetailedStatus": NotRequired[str],
        "AssociationStatusAggregatedCount": NotRequired[Dict[str, int]],
    },
)
AssociationStatusTypeDef = TypedDict(
    "AssociationStatusTypeDef",
    {
        "Date": datetime,
        "Name": AssociationStatusNameType,
        "Message": str,
        "AdditionalInfo": NotRequired[str],
    },
)
TargetTypeDef = TypedDict(
    "TargetTypeDef",
    {
        "Key": NotRequired[str],
        "Values": NotRequired[Sequence[str]],
    },
)
AssociationExecutionFilterTypeDef = TypedDict(
    "AssociationExecutionFilterTypeDef",
    {
        "Key": AssociationExecutionFilterKeyType,
        "Value": str,
        "Type": AssociationFilterOperatorTypeType,
    },
)
OutputSourceTypeDef = TypedDict(
    "OutputSourceTypeDef",
    {
        "OutputSourceId": NotRequired[str],
        "OutputSourceType": NotRequired[str],
    },
)
AssociationExecutionTargetsFilterTypeDef = TypedDict(
    "AssociationExecutionTargetsFilterTypeDef",
    {
        "Key": AssociationExecutionTargetsFilterKeyType,
        "Value": str,
    },
)
AssociationFilterTypeDef = TypedDict(
    "AssociationFilterTypeDef",
    {
        "key": AssociationFilterKeyType,
        "value": str,
    },
)
TargetPaginatorTypeDef = TypedDict(
    "TargetPaginatorTypeDef",
    {
        "Key": NotRequired[str],
        "Values": NotRequired[List[str]],
    },
)
AttachmentContentTypeDef = TypedDict(
    "AttachmentContentTypeDef",
    {
        "Name": NotRequired[str],
        "Size": NotRequired[int],
        "Hash": NotRequired[str],
        "HashType": NotRequired[Literal["Sha256"]],
        "Url": NotRequired[str],
    },
)
AttachmentInformationTypeDef = TypedDict(
    "AttachmentInformationTypeDef",
    {
        "Name": NotRequired[str],
    },
)
AttachmentsSourceTypeDef = TypedDict(
    "AttachmentsSourceTypeDef",
    {
        "Key": NotRequired[AttachmentsSourceKeyType],
        "Values": NotRequired[Sequence[str]],
        "Name": NotRequired[str],
    },
)
AutomationExecutionFilterTypeDef = TypedDict(
    "AutomationExecutionFilterTypeDef",
    {
        "Key": AutomationExecutionFilterKeyType,
        "Values": Sequence[str],
    },
)
ResolvedTargetsTypeDef = TypedDict(
    "ResolvedTargetsTypeDef",
    {
        "ParameterValues": NotRequired[List[str]],
        "Truncated": NotRequired[bool],
    },
)
ProgressCountersTypeDef = TypedDict(
    "ProgressCountersTypeDef",
    {
        "TotalSteps": NotRequired[int],
        "SuccessSteps": NotRequired[int],
        "FailedSteps": NotRequired[int],
        "CancelledSteps": NotRequired[int],
        "TimedOutSteps": NotRequired[int],
    },
)
PatchSourceTypeDef = TypedDict(
    "PatchSourceTypeDef",
    {
        "Name": str,
        "Products": Sequence[str],
        "Configuration": str,
    },
)
CancelCommandRequestRequestTypeDef = TypedDict(
    "CancelCommandRequestRequestTypeDef",
    {
        "CommandId": str,
        "InstanceIds": NotRequired[Sequence[str]],
    },
)
CancelMaintenanceWindowExecutionRequestRequestTypeDef = TypedDict(
    "CancelMaintenanceWindowExecutionRequestRequestTypeDef",
    {
        "WindowExecutionId": str,
    },
)
CloudWatchOutputConfigTypeDef = TypedDict(
    "CloudWatchOutputConfigTypeDef",
    {
        "CloudWatchLogGroupName": NotRequired[str],
        "CloudWatchOutputEnabled": NotRequired[bool],
    },
)
CommandFilterTypeDef = TypedDict(
    "CommandFilterTypeDef",
    {
        "key": CommandFilterKeyType,
        "value": str,
    },
)
CommandPluginTypeDef = TypedDict(
    "CommandPluginTypeDef",
    {
        "Name": NotRequired[str],
        "Status": NotRequired[CommandPluginStatusType],
        "StatusDetails": NotRequired[str],
        "ResponseCode": NotRequired[int],
        "ResponseStartDateTime": NotRequired[datetime],
        "ResponseFinishDateTime": NotRequired[datetime],
        "Output": NotRequired[str],
        "StandardOutputUrl": NotRequired[str],
        "StandardErrorUrl": NotRequired[str],
        "OutputS3Region": NotRequired[str],
        "OutputS3BucketName": NotRequired[str],
        "OutputS3KeyPrefix": NotRequired[str],
    },
)
NotificationConfigTypeDef = TypedDict(
    "NotificationConfigTypeDef",
    {
        "NotificationArn": NotRequired[str],
        "NotificationEvents": NotRequired[List[NotificationEventType]],
        "NotificationType": NotRequired[NotificationTypeType],
    },
)
ComplianceExecutionSummaryTypeDef = TypedDict(
    "ComplianceExecutionSummaryTypeDef",
    {
        "ExecutionTime": datetime,
        "ExecutionId": NotRequired[str],
        "ExecutionType": NotRequired[str],
    },
)
ComplianceItemEntryTypeDef = TypedDict(
    "ComplianceItemEntryTypeDef",
    {
        "Severity": ComplianceSeverityType,
        "Status": ComplianceStatusType,
        "Id": NotRequired[str],
        "Title": NotRequired[str],
        "Details": NotRequired[Mapping[str, str]],
    },
)
ComplianceStringFilterTypeDef = TypedDict(
    "ComplianceStringFilterTypeDef",
    {
        "Key": NotRequired[str],
        "Values": NotRequired[Sequence[str]],
        "Type": NotRequired[ComplianceQueryOperatorTypeType],
    },
)
SeveritySummaryTypeDef = TypedDict(
    "SeveritySummaryTypeDef",
    {
        "CriticalCount": NotRequired[int],
        "HighCount": NotRequired[int],
        "MediumCount": NotRequired[int],
        "LowCount": NotRequired[int],
        "InformationalCount": NotRequired[int],
        "UnspecifiedCount": NotRequired[int],
    },
)
RegistrationMetadataItemTypeDef = TypedDict(
    "RegistrationMetadataItemTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)
TimestampTypeDef = Union[datetime, str]
DocumentRequiresTypeDef = TypedDict(
    "DocumentRequiresTypeDef",
    {
        "Name": str,
        "Version": NotRequired[str],
        "RequireType": NotRequired[str],
        "VersionName": NotRequired[str],
    },
)
OpsItemDataValueTypeDef = TypedDict(
    "OpsItemDataValueTypeDef",
    {
        "Value": NotRequired[str],
        "Type": NotRequired[OpsItemDataTypeType],
    },
)
OpsItemNotificationTypeDef = TypedDict(
    "OpsItemNotificationTypeDef",
    {
        "Arn": NotRequired[str],
    },
)
RelatedOpsItemTypeDef = TypedDict(
    "RelatedOpsItemTypeDef",
    {
        "OpsItemId": str,
    },
)
MetadataValueTypeDef = TypedDict(
    "MetadataValueTypeDef",
    {
        "Value": NotRequired[str],
    },
)
DeleteActivationRequestRequestTypeDef = TypedDict(
    "DeleteActivationRequestRequestTypeDef",
    {
        "ActivationId": str,
    },
)
DeleteAssociationRequestRequestTypeDef = TypedDict(
    "DeleteAssociationRequestRequestTypeDef",
    {
        "Name": NotRequired[str],
        "InstanceId": NotRequired[str],
        "AssociationId": NotRequired[str],
    },
)
DeleteDocumentRequestRequestTypeDef = TypedDict(
    "DeleteDocumentRequestRequestTypeDef",
    {
        "Name": str,
        "DocumentVersion": NotRequired[str],
        "VersionName": NotRequired[str],
        "Force": NotRequired[bool],
    },
)
DeleteInventoryRequestRequestTypeDef = TypedDict(
    "DeleteInventoryRequestRequestTypeDef",
    {
        "TypeName": str,
        "SchemaDeleteOption": NotRequired[InventorySchemaDeleteOptionType],
        "DryRun": NotRequired[bool],
        "ClientToken": NotRequired[str],
    },
)
DeleteMaintenanceWindowRequestRequestTypeDef = TypedDict(
    "DeleteMaintenanceWindowRequestRequestTypeDef",
    {
        "WindowId": str,
    },
)
DeleteOpsItemRequestRequestTypeDef = TypedDict(
    "DeleteOpsItemRequestRequestTypeDef",
    {
        "OpsItemId": str,
    },
)
DeleteOpsMetadataRequestRequestTypeDef = TypedDict(
    "DeleteOpsMetadataRequestRequestTypeDef",
    {
        "OpsMetadataArn": str,
    },
)
DeleteParameterRequestRequestTypeDef = TypedDict(
    "DeleteParameterRequestRequestTypeDef",
    {
        "Name": str,
    },
)
DeleteParametersRequestRequestTypeDef = TypedDict(
    "DeleteParametersRequestRequestTypeDef",
    {
        "Names": Sequence[str],
    },
)
DeletePatchBaselineRequestRequestTypeDef = TypedDict(
    "DeletePatchBaselineRequestRequestTypeDef",
    {
        "BaselineId": str,
    },
)
DeleteResourceDataSyncRequestRequestTypeDef = TypedDict(
    "DeleteResourceDataSyncRequestRequestTypeDef",
    {
        "SyncName": str,
        "SyncType": NotRequired[str],
    },
)
DeleteResourcePolicyRequestRequestTypeDef = TypedDict(
    "DeleteResourcePolicyRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "PolicyId": str,
        "PolicyHash": str,
    },
)
DeregisterManagedInstanceRequestRequestTypeDef = TypedDict(
    "DeregisterManagedInstanceRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)
DeregisterPatchBaselineForPatchGroupRequestRequestTypeDef = TypedDict(
    "DeregisterPatchBaselineForPatchGroupRequestRequestTypeDef",
    {
        "BaselineId": str,
        "PatchGroup": str,
    },
)
DeregisterTargetFromMaintenanceWindowRequestRequestTypeDef = TypedDict(
    "DeregisterTargetFromMaintenanceWindowRequestRequestTypeDef",
    {
        "WindowId": str,
        "WindowTargetId": str,
        "Safe": NotRequired[bool],
    },
)
DeregisterTaskFromMaintenanceWindowRequestRequestTypeDef = TypedDict(
    "DeregisterTaskFromMaintenanceWindowRequestRequestTypeDef",
    {
        "WindowId": str,
        "WindowTaskId": str,
    },
)
DescribeActivationsFilterTypeDef = TypedDict(
    "DescribeActivationsFilterTypeDef",
    {
        "FilterKey": NotRequired[DescribeActivationsFilterKeysType],
        "FilterValues": NotRequired[Sequence[str]],
    },
)
PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": NotRequired[int],
        "PageSize": NotRequired[int],
        "StartingToken": NotRequired[str],
    },
)
DescribeAssociationRequestRequestTypeDef = TypedDict(
    "DescribeAssociationRequestRequestTypeDef",
    {
        "Name": NotRequired[str],
        "InstanceId": NotRequired[str],
        "AssociationId": NotRequired[str],
        "AssociationVersion": NotRequired[str],
    },
)
StepExecutionFilterTypeDef = TypedDict(
    "StepExecutionFilterTypeDef",
    {
        "Key": StepExecutionFilterKeyType,
        "Values": Sequence[str],
    },
)
PatchOrchestratorFilterTypeDef = TypedDict(
    "PatchOrchestratorFilterTypeDef",
    {
        "Key": NotRequired[str],
        "Values": NotRequired[Sequence[str]],
    },
)
PatchTypeDef = TypedDict(
    "PatchTypeDef",
    {
        "Id": NotRequired[str],
        "ReleaseDate": NotRequired[datetime],
        "Title": NotRequired[str],
        "Description": NotRequired[str],
        "ContentUrl": NotRequired[str],
        "Vendor": NotRequired[str],
        "ProductFamily": NotRequired[str],
        "Product": NotRequired[str],
        "Classification": NotRequired[str],
        "MsrcSeverity": NotRequired[str],
        "KbNumber": NotRequired[str],
        "MsrcNumber": NotRequired[str],
        "Language": NotRequired[str],
        "AdvisoryIds": NotRequired[List[str]],
        "BugzillaIds": NotRequired[List[str]],
        "CVEIds": NotRequired[List[str]],
        "Name": NotRequired[str],
        "Epoch": NotRequired[int],
        "Version": NotRequired[str],
        "Release": NotRequired[str],
        "Arch": NotRequired[str],
        "Severity": NotRequired[str],
        "Repository": NotRequired[str],
    },
)
DescribeDocumentPermissionRequestRequestTypeDef = TypedDict(
    "DescribeDocumentPermissionRequestRequestTypeDef",
    {
        "Name": str,
        "PermissionType": Literal["Share"],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DescribeDocumentRequestRequestTypeDef = TypedDict(
    "DescribeDocumentRequestRequestTypeDef",
    {
        "Name": str,
        "DocumentVersion": NotRequired[str],
        "VersionName": NotRequired[str],
    },
)
DescribeEffectiveInstanceAssociationsRequestRequestTypeDef = TypedDict(
    "DescribeEffectiveInstanceAssociationsRequestRequestTypeDef",
    {
        "InstanceId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
InstanceAssociationTypeDef = TypedDict(
    "InstanceAssociationTypeDef",
    {
        "AssociationId": NotRequired[str],
        "InstanceId": NotRequired[str],
        "Content": NotRequired[str],
        "AssociationVersion": NotRequired[str],
    },
)
DescribeEffectivePatchesForPatchBaselineRequestRequestTypeDef = TypedDict(
    "DescribeEffectivePatchesForPatchBaselineRequestRequestTypeDef",
    {
        "BaselineId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DescribeInstanceAssociationsStatusRequestRequestTypeDef = TypedDict(
    "DescribeInstanceAssociationsStatusRequestRequestTypeDef",
    {
        "InstanceId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
InstanceInformationFilterTypeDef = TypedDict(
    "InstanceInformationFilterTypeDef",
    {
        "key": InstanceInformationFilterKeyType,
        "valueSet": Sequence[str],
    },
)
InstanceInformationStringFilterTypeDef = TypedDict(
    "InstanceInformationStringFilterTypeDef",
    {
        "Key": str,
        "Values": Sequence[str],
    },
)
InstancePatchStateFilterTypeDef = TypedDict(
    "InstancePatchStateFilterTypeDef",
    {
        "Key": str,
        "Values": Sequence[str],
        "Type": InstancePatchStateOperatorTypeType,
    },
)
InstancePatchStateTypeDef = TypedDict(
    "InstancePatchStateTypeDef",
    {
        "InstanceId": str,
        "PatchGroup": str,
        "BaselineId": str,
        "OperationStartTime": datetime,
        "OperationEndTime": datetime,
        "Operation": PatchOperationTypeType,
        "SnapshotId": NotRequired[str],
        "InstallOverrideList": NotRequired[str],
        "OwnerInformation": NotRequired[str],
        "InstalledCount": NotRequired[int],
        "InstalledOtherCount": NotRequired[int],
        "InstalledPendingRebootCount": NotRequired[int],
        "InstalledRejectedCount": NotRequired[int],
        "MissingCount": NotRequired[int],
        "FailedCount": NotRequired[int],
        "UnreportedNotApplicableCount": NotRequired[int],
        "NotApplicableCount": NotRequired[int],
        "LastNoRebootInstallOperationTime": NotRequired[datetime],
        "RebootOption": NotRequired[RebootOptionType],
        "CriticalNonCompliantCount": NotRequired[int],
        "SecurityNonCompliantCount": NotRequired[int],
        "OtherNonCompliantCount": NotRequired[int],
    },
)
DescribeInstancePatchStatesRequestRequestTypeDef = TypedDict(
    "DescribeInstancePatchStatesRequestRequestTypeDef",
    {
        "InstanceIds": Sequence[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
PatchComplianceDataTypeDef = TypedDict(
    "PatchComplianceDataTypeDef",
    {
        "Title": str,
        "KBId": str,
        "Classification": str,
        "Severity": str,
        "State": PatchComplianceDataStateType,
        "InstalledTime": datetime,
        "CVEIds": NotRequired[str],
    },
)
DescribeInventoryDeletionsRequestRequestTypeDef = TypedDict(
    "DescribeInventoryDeletionsRequestRequestTypeDef",
    {
        "DeletionId": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
MaintenanceWindowFilterTypeDef = TypedDict(
    "MaintenanceWindowFilterTypeDef",
    {
        "Key": NotRequired[str],
        "Values": NotRequired[Sequence[str]],
    },
)
MaintenanceWindowExecutionTaskInvocationIdentityTypeDef = TypedDict(
    "MaintenanceWindowExecutionTaskInvocationIdentityTypeDef",
    {
        "WindowExecutionId": NotRequired[str],
        "TaskExecutionId": NotRequired[str],
        "InvocationId": NotRequired[str],
        "ExecutionId": NotRequired[str],
        "TaskType": NotRequired[MaintenanceWindowTaskTypeType],
        "Parameters": NotRequired[str],
        "Status": NotRequired[MaintenanceWindowExecutionStatusType],
        "StatusDetails": NotRequired[str],
        "StartTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
        "OwnerInformation": NotRequired[str],
        "WindowTargetId": NotRequired[str],
    },
)
MaintenanceWindowExecutionTypeDef = TypedDict(
    "MaintenanceWindowExecutionTypeDef",
    {
        "WindowId": NotRequired[str],
        "WindowExecutionId": NotRequired[str],
        "Status": NotRequired[MaintenanceWindowExecutionStatusType],
        "StatusDetails": NotRequired[str],
        "StartTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
    },
)
ScheduledWindowExecutionTypeDef = TypedDict(
    "ScheduledWindowExecutionTypeDef",
    {
        "WindowId": NotRequired[str],
        "Name": NotRequired[str],
        "ExecutionTime": NotRequired[str],
    },
)
MaintenanceWindowIdentityForTargetTypeDef = TypedDict(
    "MaintenanceWindowIdentityForTargetTypeDef",
    {
        "WindowId": NotRequired[str],
        "Name": NotRequired[str],
    },
)
MaintenanceWindowIdentityTypeDef = TypedDict(
    "MaintenanceWindowIdentityTypeDef",
    {
        "WindowId": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "Enabled": NotRequired[bool],
        "Duration": NotRequired[int],
        "Cutoff": NotRequired[int],
        "Schedule": NotRequired[str],
        "ScheduleTimezone": NotRequired[str],
        "ScheduleOffset": NotRequired[int],
        "EndDate": NotRequired[str],
        "StartDate": NotRequired[str],
        "NextExecutionTime": NotRequired[str],
    },
)
OpsItemFilterTypeDef = TypedDict(
    "OpsItemFilterTypeDef",
    {
        "Key": OpsItemFilterKeyType,
        "Values": Sequence[str],
        "Operator": OpsItemFilterOperatorType,
    },
)
ParameterStringFilterTypeDef = TypedDict(
    "ParameterStringFilterTypeDef",
    {
        "Key": str,
        "Option": NotRequired[str],
        "Values": NotRequired[Sequence[str]],
    },
)
ParametersFilterTypeDef = TypedDict(
    "ParametersFilterTypeDef",
    {
        "Key": ParametersFilterKeyType,
        "Values": Sequence[str],
    },
)
PatchBaselineIdentityTypeDef = TypedDict(
    "PatchBaselineIdentityTypeDef",
    {
        "BaselineId": NotRequired[str],
        "BaselineName": NotRequired[str],
        "OperatingSystem": NotRequired[OperatingSystemType],
        "BaselineDescription": NotRequired[str],
        "DefaultBaseline": NotRequired[bool],
    },
)
DescribePatchGroupStateRequestRequestTypeDef = TypedDict(
    "DescribePatchGroupStateRequestRequestTypeDef",
    {
        "PatchGroup": str,
    },
)
DescribePatchPropertiesRequestRequestTypeDef = TypedDict(
    "DescribePatchPropertiesRequestRequestTypeDef",
    {
        "OperatingSystem": OperatingSystemType,
        "Property": PatchPropertyType,
        "PatchSet": NotRequired[PatchSetType],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
SessionFilterTypeDef = TypedDict(
    "SessionFilterTypeDef",
    {
        "key": SessionFilterKeyType,
        "value": str,
    },
)
DisassociateOpsItemRelatedItemRequestRequestTypeDef = TypedDict(
    "DisassociateOpsItemRelatedItemRequestRequestTypeDef",
    {
        "OpsItemId": str,
        "AssociationId": str,
    },
)
DocumentDefaultVersionDescriptionTypeDef = TypedDict(
    "DocumentDefaultVersionDescriptionTypeDef",
    {
        "Name": NotRequired[str],
        "DefaultVersion": NotRequired[str],
        "DefaultVersionName": NotRequired[str],
    },
)
DocumentParameterTypeDef = TypedDict(
    "DocumentParameterTypeDef",
    {
        "Name": NotRequired[str],
        "Type": NotRequired[DocumentParameterTypeType],
        "Description": NotRequired[str],
        "DefaultValue": NotRequired[str],
    },
)
ReviewInformationTypeDef = TypedDict(
    "ReviewInformationTypeDef",
    {
        "ReviewedTime": NotRequired[datetime],
        "Status": NotRequired[ReviewStatusType],
        "Reviewer": NotRequired[str],
    },
)
DocumentFilterTypeDef = TypedDict(
    "DocumentFilterTypeDef",
    {
        "key": DocumentFilterKeyType,
        "value": str,
    },
)
DocumentKeyValuesFilterTypeDef = TypedDict(
    "DocumentKeyValuesFilterTypeDef",
    {
        "Key": NotRequired[str],
        "Values": NotRequired[Sequence[str]],
    },
)
DocumentReviewCommentSourceTypeDef = TypedDict(
    "DocumentReviewCommentSourceTypeDef",
    {
        "Type": NotRequired[Literal["Comment"]],
        "Content": NotRequired[str],
    },
)
DocumentVersionInfoTypeDef = TypedDict(
    "DocumentVersionInfoTypeDef",
    {
        "Name": NotRequired[str],
        "DisplayName": NotRequired[str],
        "DocumentVersion": NotRequired[str],
        "VersionName": NotRequired[str],
        "CreatedDate": NotRequired[datetime],
        "IsDefaultVersion": NotRequired[bool],
        "DocumentFormat": NotRequired[DocumentFormatType],
        "Status": NotRequired[DocumentStatusType],
        "StatusInformation": NotRequired[str],
        "ReviewStatus": NotRequired[ReviewStatusType],
    },
)
PatchStatusTypeDef = TypedDict(
    "PatchStatusTypeDef",
    {
        "DeploymentStatus": NotRequired[PatchDeploymentStatusType],
        "ComplianceLevel": NotRequired[PatchComplianceLevelType],
        "ApprovalDate": NotRequired[datetime],
    },
)
FailureDetailsTypeDef = TypedDict(
    "FailureDetailsTypeDef",
    {
        "FailureStage": NotRequired[str],
        "FailureType": NotRequired[str],
        "Details": NotRequired[Dict[str, List[str]]],
    },
)
GetAutomationExecutionRequestRequestTypeDef = TypedDict(
    "GetAutomationExecutionRequestRequestTypeDef",
    {
        "AutomationExecutionId": str,
    },
)
GetCalendarStateRequestRequestTypeDef = TypedDict(
    "GetCalendarStateRequestRequestTypeDef",
    {
        "CalendarNames": Sequence[str],
        "AtTime": NotRequired[str],
    },
)
WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": NotRequired[int],
        "MaxAttempts": NotRequired[int],
    },
)
GetCommandInvocationRequestRequestTypeDef = TypedDict(
    "GetCommandInvocationRequestRequestTypeDef",
    {
        "CommandId": str,
        "InstanceId": str,
        "PluginName": NotRequired[str],
    },
)
GetConnectionStatusRequestRequestTypeDef = TypedDict(
    "GetConnectionStatusRequestRequestTypeDef",
    {
        "Target": str,
    },
)
GetDefaultPatchBaselineRequestRequestTypeDef = TypedDict(
    "GetDefaultPatchBaselineRequestRequestTypeDef",
    {
        "OperatingSystem": NotRequired[OperatingSystemType],
    },
)
GetDocumentRequestRequestTypeDef = TypedDict(
    "GetDocumentRequestRequestTypeDef",
    {
        "Name": str,
        "VersionName": NotRequired[str],
        "DocumentVersion": NotRequired[str],
        "DocumentFormat": NotRequired[DocumentFormatType],
    },
)
InventoryFilterTypeDef = TypedDict(
    "InventoryFilterTypeDef",
    {
        "Key": str,
        "Values": Sequence[str],
        "Type": NotRequired[InventoryQueryOperatorTypeType],
    },
)
ResultAttributeTypeDef = TypedDict(
    "ResultAttributeTypeDef",
    {
        "TypeName": str,
    },
)
GetInventorySchemaRequestRequestTypeDef = TypedDict(
    "GetInventorySchemaRequestRequestTypeDef",
    {
        "TypeName": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "Aggregator": NotRequired[bool],
        "SubType": NotRequired[bool],
    },
)
GetMaintenanceWindowExecutionRequestRequestTypeDef = TypedDict(
    "GetMaintenanceWindowExecutionRequestRequestTypeDef",
    {
        "WindowExecutionId": str,
    },
)
GetMaintenanceWindowExecutionTaskInvocationRequestRequestTypeDef = TypedDict(
    "GetMaintenanceWindowExecutionTaskInvocationRequestRequestTypeDef",
    {
        "WindowExecutionId": str,
        "TaskId": str,
        "InvocationId": str,
    },
)
GetMaintenanceWindowExecutionTaskRequestRequestTypeDef = TypedDict(
    "GetMaintenanceWindowExecutionTaskRequestRequestTypeDef",
    {
        "WindowExecutionId": str,
        "TaskId": str,
    },
)
MaintenanceWindowTaskParameterValueExpressionTypeDef = TypedDict(
    "MaintenanceWindowTaskParameterValueExpressionTypeDef",
    {
        "Values": NotRequired[List[str]],
    },
)
GetMaintenanceWindowRequestRequestTypeDef = TypedDict(
    "GetMaintenanceWindowRequestRequestTypeDef",
    {
        "WindowId": str,
    },
)
GetMaintenanceWindowTaskRequestRequestTypeDef = TypedDict(
    "GetMaintenanceWindowTaskRequestRequestTypeDef",
    {
        "WindowId": str,
        "WindowTaskId": str,
    },
)
LoggingInfoTypeDef = TypedDict(
    "LoggingInfoTypeDef",
    {
        "S3BucketName": str,
        "S3Region": str,
        "S3KeyPrefix": NotRequired[str],
    },
)
GetOpsItemRequestRequestTypeDef = TypedDict(
    "GetOpsItemRequestRequestTypeDef",
    {
        "OpsItemId": str,
        "OpsItemArn": NotRequired[str],
    },
)
GetOpsMetadataRequestRequestTypeDef = TypedDict(
    "GetOpsMetadataRequestRequestTypeDef",
    {
        "OpsMetadataArn": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
OpsFilterTypeDef = TypedDict(
    "OpsFilterTypeDef",
    {
        "Key": str,
        "Values": Sequence[str],
        "Type": NotRequired[OpsFilterOperatorTypeType],
    },
)
OpsResultAttributeTypeDef = TypedDict(
    "OpsResultAttributeTypeDef",
    {
        "TypeName": str,
    },
)
GetParameterHistoryRequestRequestTypeDef = TypedDict(
    "GetParameterHistoryRequestRequestTypeDef",
    {
        "Name": str,
        "WithDecryption": NotRequired[bool],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
GetParameterRequestRequestTypeDef = TypedDict(
    "GetParameterRequestRequestTypeDef",
    {
        "Name": str,
        "WithDecryption": NotRequired[bool],
    },
)
ParameterTypeDef = TypedDict(
    "ParameterTypeDef",
    {
        "Name": NotRequired[str],
        "Type": NotRequired[ParameterTypeType],
        "Value": NotRequired[str],
        "Version": NotRequired[int],
        "Selector": NotRequired[str],
        "SourceResult": NotRequired[str],
        "LastModifiedDate": NotRequired[datetime],
        "ARN": NotRequired[str],
        "DataType": NotRequired[str],
    },
)
GetParametersRequestRequestTypeDef = TypedDict(
    "GetParametersRequestRequestTypeDef",
    {
        "Names": Sequence[str],
        "WithDecryption": NotRequired[bool],
    },
)
GetPatchBaselineForPatchGroupRequestRequestTypeDef = TypedDict(
    "GetPatchBaselineForPatchGroupRequestRequestTypeDef",
    {
        "PatchGroup": str,
        "OperatingSystem": NotRequired[OperatingSystemType],
    },
)
GetPatchBaselineRequestRequestTypeDef = TypedDict(
    "GetPatchBaselineRequestRequestTypeDef",
    {
        "BaselineId": str,
    },
)
GetResourcePoliciesRequestRequestTypeDef = TypedDict(
    "GetResourcePoliciesRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
GetResourcePoliciesResponseEntryTypeDef = TypedDict(
    "GetResourcePoliciesResponseEntryTypeDef",
    {
        "PolicyId": NotRequired[str],
        "PolicyHash": NotRequired[str],
        "Policy": NotRequired[str],
    },
)
GetServiceSettingRequestRequestTypeDef = TypedDict(
    "GetServiceSettingRequestRequestTypeDef",
    {
        "SettingId": str,
    },
)
ServiceSettingTypeDef = TypedDict(
    "ServiceSettingTypeDef",
    {
        "SettingId": NotRequired[str],
        "SettingValue": NotRequired[str],
        "LastModifiedDate": NotRequired[datetime],
        "LastModifiedUser": NotRequired[str],
        "ARN": NotRequired[str],
        "Status": NotRequired[str],
    },
)
InstanceAggregatedAssociationOverviewTypeDef = TypedDict(
    "InstanceAggregatedAssociationOverviewTypeDef",
    {
        "DetailedStatus": NotRequired[str],
        "InstanceAssociationStatusAggregatedCount": NotRequired[Dict[str, int]],
    },
)
S3OutputLocationTypeDef = TypedDict(
    "S3OutputLocationTypeDef",
    {
        "OutputS3Region": NotRequired[str],
        "OutputS3BucketName": NotRequired[str],
        "OutputS3KeyPrefix": NotRequired[str],
    },
)
S3OutputUrlTypeDef = TypedDict(
    "S3OutputUrlTypeDef",
    {
        "OutputUrl": NotRequired[str],
    },
)
InventoryDeletionSummaryItemTypeDef = TypedDict(
    "InventoryDeletionSummaryItemTypeDef",
    {
        "Version": NotRequired[str],
        "Count": NotRequired[int],
        "RemainingCount": NotRequired[int],
    },
)
InventoryItemAttributeTypeDef = TypedDict(
    "InventoryItemAttributeTypeDef",
    {
        "Name": str,
        "DataType": InventoryAttributeDataTypeType,
    },
)
InventoryItemTypeDef = TypedDict(
    "InventoryItemTypeDef",
    {
        "TypeName": str,
        "SchemaVersion": str,
        "CaptureTime": str,
        "ContentHash": NotRequired[str],
        "Content": NotRequired[Sequence[Mapping[str, str]]],
        "Context": NotRequired[Mapping[str, str]],
    },
)
InventoryResultItemTypeDef = TypedDict(
    "InventoryResultItemTypeDef",
    {
        "TypeName": str,
        "SchemaVersion": str,
        "Content": List[Dict[str, str]],
        "CaptureTime": NotRequired[str],
        "ContentHash": NotRequired[str],
    },
)
LabelParameterVersionRequestRequestTypeDef = TypedDict(
    "LabelParameterVersionRequestRequestTypeDef",
    {
        "Name": str,
        "Labels": Sequence[str],
        "ParameterVersion": NotRequired[int],
    },
)
ListAssociationVersionsRequestRequestTypeDef = TypedDict(
    "ListAssociationVersionsRequestRequestTypeDef",
    {
        "AssociationId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListDocumentMetadataHistoryRequestRequestTypeDef = TypedDict(
    "ListDocumentMetadataHistoryRequestRequestTypeDef",
    {
        "Name": str,
        "Metadata": Literal["DocumentReviews"],
        "DocumentVersion": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListDocumentVersionsRequestRequestTypeDef = TypedDict(
    "ListDocumentVersionsRequestRequestTypeDef",
    {
        "Name": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
OpsItemEventFilterTypeDef = TypedDict(
    "OpsItemEventFilterTypeDef",
    {
        "Key": Literal["OpsItemId"],
        "Values": Sequence[str],
        "Operator": Literal["Equal"],
    },
)
OpsItemRelatedItemsFilterTypeDef = TypedDict(
    "OpsItemRelatedItemsFilterTypeDef",
    {
        "Key": OpsItemRelatedItemsFilterKeyType,
        "Values": Sequence[str],
        "Operator": Literal["Equal"],
    },
)
OpsMetadataFilterTypeDef = TypedDict(
    "OpsMetadataFilterTypeDef",
    {
        "Key": str,
        "Values": Sequence[str],
    },
)
OpsMetadataTypeDef = TypedDict(
    "OpsMetadataTypeDef",
    {
        "ResourceId": NotRequired[str],
        "OpsMetadataArn": NotRequired[str],
        "LastModifiedDate": NotRequired[datetime],
        "LastModifiedUser": NotRequired[str],
        "CreationDate": NotRequired[datetime],
    },
)
ListResourceDataSyncRequestRequestTypeDef = TypedDict(
    "ListResourceDataSyncRequestRequestTypeDef",
    {
        "SyncType": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceType": ResourceTypeForTaggingType,
        "ResourceId": str,
    },
)
MaintenanceWindowAutomationParametersTypeDef = TypedDict(
    "MaintenanceWindowAutomationParametersTypeDef",
    {
        "DocumentVersion": NotRequired[str],
        "Parameters": NotRequired[Dict[str, List[str]]],
    },
)
MaintenanceWindowLambdaParametersTypeDef = TypedDict(
    "MaintenanceWindowLambdaParametersTypeDef",
    {
        "ClientContext": NotRequired[str],
        "Qualifier": NotRequired[str],
        "Payload": NotRequired[bytes],
    },
)
MaintenanceWindowStepFunctionsParametersTypeDef = TypedDict(
    "MaintenanceWindowStepFunctionsParametersTypeDef",
    {
        "Input": NotRequired[str],
        "Name": NotRequired[str],
    },
)
ModifyDocumentPermissionRequestRequestTypeDef = TypedDict(
    "ModifyDocumentPermissionRequestRequestTypeDef",
    {
        "Name": str,
        "PermissionType": Literal["Share"],
        "AccountIdsToAdd": NotRequired[Sequence[str]],
        "AccountIdsToRemove": NotRequired[Sequence[str]],
        "SharedDocumentVersion": NotRequired[str],
    },
)
OpsEntityItemTypeDef = TypedDict(
    "OpsEntityItemTypeDef",
    {
        "CaptureTime": NotRequired[str],
        "Content": NotRequired[List[Dict[str, str]]],
    },
)
OpsItemIdentityTypeDef = TypedDict(
    "OpsItemIdentityTypeDef",
    {
        "Arn": NotRequired[str],
    },
)
ParameterInlinePolicyTypeDef = TypedDict(
    "ParameterInlinePolicyTypeDef",
    {
        "PolicyText": NotRequired[str],
        "PolicyType": NotRequired[str],
        "PolicyStatus": NotRequired[str],
    },
)
ParentStepDetailsTypeDef = TypedDict(
    "ParentStepDetailsTypeDef",
    {
        "StepExecutionId": NotRequired[str],
        "StepName": NotRequired[str],
        "Action": NotRequired[str],
        "Iteration": NotRequired[int],
        "IteratorValue": NotRequired[str],
    },
)
PatchFilterTypeDef = TypedDict(
    "PatchFilterTypeDef",
    {
        "Key": PatchFilterKeyType,
        "Values": Sequence[str],
    },
)
PutResourcePolicyRequestRequestTypeDef = TypedDict(
    "PutResourcePolicyRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Policy": str,
        "PolicyId": NotRequired[str],
        "PolicyHash": NotRequired[str],
    },
)
RegisterDefaultPatchBaselineRequestRequestTypeDef = TypedDict(
    "RegisterDefaultPatchBaselineRequestRequestTypeDef",
    {
        "BaselineId": str,
    },
)
RegisterPatchBaselineForPatchGroupRequestRequestTypeDef = TypedDict(
    "RegisterPatchBaselineForPatchGroupRequestRequestTypeDef",
    {
        "BaselineId": str,
        "PatchGroup": str,
    },
)
RemoveTagsFromResourceRequestRequestTypeDef = TypedDict(
    "RemoveTagsFromResourceRequestRequestTypeDef",
    {
        "ResourceType": ResourceTypeForTaggingType,
        "ResourceId": str,
        "TagKeys": Sequence[str],
    },
)
ResetServiceSettingRequestRequestTypeDef = TypedDict(
    "ResetServiceSettingRequestRequestTypeDef",
    {
        "SettingId": str,
    },
)
ResourceDataSyncOrganizationalUnitTypeDef = TypedDict(
    "ResourceDataSyncOrganizationalUnitTypeDef",
    {
        "OrganizationalUnitId": NotRequired[str],
    },
)
ResourceDataSyncDestinationDataSharingTypeDef = TypedDict(
    "ResourceDataSyncDestinationDataSharingTypeDef",
    {
        "DestinationDataSharingType": NotRequired[str],
    },
)
ResumeSessionRequestRequestTypeDef = TypedDict(
    "ResumeSessionRequestRequestTypeDef",
    {
        "SessionId": str,
    },
)
SendAutomationSignalRequestRequestTypeDef = TypedDict(
    "SendAutomationSignalRequestRequestTypeDef",
    {
        "AutomationExecutionId": str,
        "SignalType": SignalTypeType,
        "Payload": NotRequired[Mapping[str, Sequence[str]]],
    },
)
SessionManagerOutputUrlTypeDef = TypedDict(
    "SessionManagerOutputUrlTypeDef",
    {
        "S3OutputUrl": NotRequired[str],
        "CloudWatchOutputUrl": NotRequired[str],
    },
)
StartAssociationsOnceRequestRequestTypeDef = TypedDict(
    "StartAssociationsOnceRequestRequestTypeDef",
    {
        "AssociationIds": Sequence[str],
    },
)
StartSessionRequestRequestTypeDef = TypedDict(
    "StartSessionRequestRequestTypeDef",
    {
        "Target": str,
        "DocumentName": NotRequired[str],
        "Reason": NotRequired[str],
        "Parameters": NotRequired[Mapping[str, Sequence[str]]],
    },
)
StopAutomationExecutionRequestRequestTypeDef = TypedDict(
    "StopAutomationExecutionRequestRequestTypeDef",
    {
        "AutomationExecutionId": str,
        "Type": NotRequired[StopTypeType],
    },
)
TerminateSessionRequestRequestTypeDef = TypedDict(
    "TerminateSessionRequestRequestTypeDef",
    {
        "SessionId": str,
    },
)
UnlabelParameterVersionRequestRequestTypeDef = TypedDict(
    "UnlabelParameterVersionRequestRequestTypeDef",
    {
        "Name": str,
        "ParameterVersion": int,
        "Labels": Sequence[str],
    },
)
UpdateDocumentDefaultVersionRequestRequestTypeDef = TypedDict(
    "UpdateDocumentDefaultVersionRequestRequestTypeDef",
    {
        "Name": str,
        "DocumentVersion": str,
    },
)
UpdateMaintenanceWindowRequestRequestTypeDef = TypedDict(
    "UpdateMaintenanceWindowRequestRequestTypeDef",
    {
        "WindowId": str,
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "StartDate": NotRequired[str],
        "EndDate": NotRequired[str],
        "Schedule": NotRequired[str],
        "ScheduleTimezone": NotRequired[str],
        "ScheduleOffset": NotRequired[int],
        "Duration": NotRequired[int],
        "Cutoff": NotRequired[int],
        "AllowUnassociatedTargets": NotRequired[bool],
        "Enabled": NotRequired[bool],
        "Replace": NotRequired[bool],
    },
)
UpdateManagedInstanceRoleRequestRequestTypeDef = TypedDict(
    "UpdateManagedInstanceRoleRequestRequestTypeDef",
    {
        "InstanceId": str,
        "IamRole": str,
    },
)
UpdateServiceSettingRequestRequestTypeDef = TypedDict(
    "UpdateServiceSettingRequestRequestTypeDef",
    {
        "SettingId": str,
        "SettingValue": str,
    },
)
ActivationTypeDef = TypedDict(
    "ActivationTypeDef",
    {
        "ActivationId": NotRequired[str],
        "Description": NotRequired[str],
        "DefaultInstanceName": NotRequired[str],
        "IamRole": NotRequired[str],
        "RegistrationLimit": NotRequired[int],
        "RegistrationsCount": NotRequired[int],
        "ExpirationDate": NotRequired[datetime],
        "Expired": NotRequired[bool],
        "CreatedDate": NotRequired[datetime],
        "Tags": NotRequired[List[TagTypeDef]],
    },
)
AddTagsToResourceRequestRequestTypeDef = TypedDict(
    "AddTagsToResourceRequestRequestTypeDef",
    {
        "ResourceType": ResourceTypeForTaggingType,
        "ResourceId": str,
        "Tags": Sequence[TagTypeDef],
    },
)
CreateMaintenanceWindowRequestRequestTypeDef = TypedDict(
    "CreateMaintenanceWindowRequestRequestTypeDef",
    {
        "Name": str,
        "Schedule": str,
        "Duration": int,
        "Cutoff": int,
        "AllowUnassociatedTargets": bool,
        "Description": NotRequired[str],
        "StartDate": NotRequired[str],
        "EndDate": NotRequired[str],
        "ScheduleTimezone": NotRequired[str],
        "ScheduleOffset": NotRequired[int],
        "ClientToken": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
PutParameterRequestRequestTypeDef = TypedDict(
    "PutParameterRequestRequestTypeDef",
    {
        "Name": str,
        "Value": str,
        "Description": NotRequired[str],
        "Type": NotRequired[ParameterTypeType],
        "KeyId": NotRequired[str],
        "Overwrite": NotRequired[bool],
        "AllowedPattern": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "Tier": NotRequired[ParameterTierType],
        "Policies": NotRequired[str],
        "DataType": NotRequired[str],
    },
)
AlarmConfigurationPaginatorTypeDef = TypedDict(
    "AlarmConfigurationPaginatorTypeDef",
    {
        "Alarms": List[AlarmTypeDef],
        "IgnorePollAlarmFailure": NotRequired[bool],
    },
)
AlarmConfigurationTypeDef = TypedDict(
    "AlarmConfigurationTypeDef",
    {
        "Alarms": Sequence[AlarmTypeDef],
        "IgnorePollAlarmFailure": NotRequired[bool],
    },
)
AssociateOpsItemRelatedItemResponseTypeDef = TypedDict(
    "AssociateOpsItemRelatedItemResponseTypeDef",
    {
        "AssociationId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CancelMaintenanceWindowExecutionResultTypeDef = TypedDict(
    "CancelMaintenanceWindowExecutionResultTypeDef",
    {
        "WindowExecutionId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateActivationResultTypeDef = TypedDict(
    "CreateActivationResultTypeDef",
    {
        "ActivationId": str,
        "ActivationCode": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateMaintenanceWindowResultTypeDef = TypedDict(
    "CreateMaintenanceWindowResultTypeDef",
    {
        "WindowId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateOpsItemResponseTypeDef = TypedDict(
    "CreateOpsItemResponseTypeDef",
    {
        "OpsItemId": str,
        "OpsItemArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateOpsMetadataResultTypeDef = TypedDict(
    "CreateOpsMetadataResultTypeDef",
    {
        "OpsMetadataArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreatePatchBaselineResultTypeDef = TypedDict(
    "CreatePatchBaselineResultTypeDef",
    {
        "BaselineId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteMaintenanceWindowResultTypeDef = TypedDict(
    "DeleteMaintenanceWindowResultTypeDef",
    {
        "WindowId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteParametersResultTypeDef = TypedDict(
    "DeleteParametersResultTypeDef",
    {
        "DeletedParameters": List[str],
        "InvalidParameters": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeletePatchBaselineResultTypeDef = TypedDict(
    "DeletePatchBaselineResultTypeDef",
    {
        "BaselineId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeregisterPatchBaselineForPatchGroupResultTypeDef = TypedDict(
    "DeregisterPatchBaselineForPatchGroupResultTypeDef",
    {
        "BaselineId": str,
        "PatchGroup": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeregisterTargetFromMaintenanceWindowResultTypeDef = TypedDict(
    "DeregisterTargetFromMaintenanceWindowResultTypeDef",
    {
        "WindowId": str,
        "WindowTargetId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeregisterTaskFromMaintenanceWindowResultTypeDef = TypedDict(
    "DeregisterTaskFromMaintenanceWindowResultTypeDef",
    {
        "WindowId": str,
        "WindowTaskId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeDocumentPermissionResponseTypeDef = TypedDict(
    "DescribeDocumentPermissionResponseTypeDef",
    {
        "AccountIds": List[str],
        "AccountSharingInfoList": List[AccountSharingInfoTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribePatchGroupStateResultTypeDef = TypedDict(
    "DescribePatchGroupStateResultTypeDef",
    {
        "Instances": int,
        "InstancesWithInstalledPatches": int,
        "InstancesWithInstalledOtherPatches": int,
        "InstancesWithInstalledPendingRebootPatches": int,
        "InstancesWithInstalledRejectedPatches": int,
        "InstancesWithMissingPatches": int,
        "InstancesWithFailedPatches": int,
        "InstancesWithNotApplicablePatches": int,
        "InstancesWithUnreportedNotApplicablePatches": int,
        "InstancesWithCriticalNonCompliantPatches": int,
        "InstancesWithSecurityNonCompliantPatches": int,
        "InstancesWithOtherNonCompliantPatches": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribePatchPropertiesResultTypeDef = TypedDict(
    "DescribePatchPropertiesResultTypeDef",
    {
        "Properties": List[Dict[str, str]],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetCalendarStateResponseTypeDef = TypedDict(
    "GetCalendarStateResponseTypeDef",
    {
        "State": CalendarStateType,
        "AtTime": str,
        "NextTransitionTime": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetConnectionStatusResponseTypeDef = TypedDict(
    "GetConnectionStatusResponseTypeDef",
    {
        "Target": str,
        "Status": ConnectionStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetDefaultPatchBaselineResultTypeDef = TypedDict(
    "GetDefaultPatchBaselineResultTypeDef",
    {
        "BaselineId": str,
        "OperatingSystem": OperatingSystemType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetDeployablePatchSnapshotForInstanceResultTypeDef = TypedDict(
    "GetDeployablePatchSnapshotForInstanceResultTypeDef",
    {
        "InstanceId": str,
        "SnapshotId": str,
        "SnapshotDownloadUrl": str,
        "Product": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetMaintenanceWindowExecutionResultTypeDef = TypedDict(
    "GetMaintenanceWindowExecutionResultTypeDef",
    {
        "WindowExecutionId": str,
        "TaskIds": List[str],
        "Status": MaintenanceWindowExecutionStatusType,
        "StatusDetails": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetMaintenanceWindowExecutionTaskInvocationResultTypeDef = TypedDict(
    "GetMaintenanceWindowExecutionTaskInvocationResultTypeDef",
    {
        "WindowExecutionId": str,
        "TaskExecutionId": str,
        "InvocationId": str,
        "ExecutionId": str,
        "TaskType": MaintenanceWindowTaskTypeType,
        "Parameters": str,
        "Status": MaintenanceWindowExecutionStatusType,
        "StatusDetails": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "OwnerInformation": str,
        "WindowTargetId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetMaintenanceWindowResultTypeDef = TypedDict(
    "GetMaintenanceWindowResultTypeDef",
    {
        "WindowId": str,
        "Name": str,
        "Description": str,
        "StartDate": str,
        "EndDate": str,
        "Schedule": str,
        "ScheduleTimezone": str,
        "ScheduleOffset": int,
        "NextExecutionTime": str,
        "Duration": int,
        "Cutoff": int,
        "AllowUnassociatedTargets": bool,
        "Enabled": bool,
        "CreatedDate": datetime,
        "ModifiedDate": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetPatchBaselineForPatchGroupResultTypeDef = TypedDict(
    "GetPatchBaselineForPatchGroupResultTypeDef",
    {
        "BaselineId": str,
        "PatchGroup": str,
        "OperatingSystem": OperatingSystemType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
LabelParameterVersionResultTypeDef = TypedDict(
    "LabelParameterVersionResultTypeDef",
    {
        "InvalidLabels": List[str],
        "ParameterVersion": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListInventoryEntriesResultTypeDef = TypedDict(
    "ListInventoryEntriesResultTypeDef",
    {
        "TypeName": str,
        "InstanceId": str,
        "SchemaVersion": str,
        "CaptureTime": str,
        "Entries": List[Dict[str, str]],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTagsForResourceResultTypeDef = TypedDict(
    "ListTagsForResourceResultTypeDef",
    {
        "TagList": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutInventoryResultTypeDef = TypedDict(
    "PutInventoryResultTypeDef",
    {
        "Message": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutParameterResultTypeDef = TypedDict(
    "PutParameterResultTypeDef",
    {
        "Version": int,
        "Tier": ParameterTierType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutResourcePolicyResponseTypeDef = TypedDict(
    "PutResourcePolicyResponseTypeDef",
    {
        "PolicyId": str,
        "PolicyHash": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RegisterDefaultPatchBaselineResultTypeDef = TypedDict(
    "RegisterDefaultPatchBaselineResultTypeDef",
    {
        "BaselineId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RegisterPatchBaselineForPatchGroupResultTypeDef = TypedDict(
    "RegisterPatchBaselineForPatchGroupResultTypeDef",
    {
        "BaselineId": str,
        "PatchGroup": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RegisterTargetWithMaintenanceWindowResultTypeDef = TypedDict(
    "RegisterTargetWithMaintenanceWindowResultTypeDef",
    {
        "WindowTargetId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RegisterTaskWithMaintenanceWindowResultTypeDef = TypedDict(
    "RegisterTaskWithMaintenanceWindowResultTypeDef",
    {
        "WindowTaskId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ResumeSessionResponseTypeDef = TypedDict(
    "ResumeSessionResponseTypeDef",
    {
        "SessionId": str,
        "TokenValue": str,
        "StreamUrl": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartAutomationExecutionResultTypeDef = TypedDict(
    "StartAutomationExecutionResultTypeDef",
    {
        "AutomationExecutionId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartChangeRequestExecutionResultTypeDef = TypedDict(
    "StartChangeRequestExecutionResultTypeDef",
    {
        "AutomationExecutionId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartSessionResponseTypeDef = TypedDict(
    "StartSessionResponseTypeDef",
    {
        "SessionId": str,
        "TokenValue": str,
        "StreamUrl": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TerminateSessionResponseTypeDef = TypedDict(
    "TerminateSessionResponseTypeDef",
    {
        "SessionId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UnlabelParameterVersionResultTypeDef = TypedDict(
    "UnlabelParameterVersionResultTypeDef",
    {
        "RemovedLabels": List[str],
        "InvalidLabels": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateMaintenanceWindowResultTypeDef = TypedDict(
    "UpdateMaintenanceWindowResultTypeDef",
    {
        "WindowId": str,
        "Name": str,
        "Description": str,
        "StartDate": str,
        "EndDate": str,
        "Schedule": str,
        "ScheduleTimezone": str,
        "ScheduleOffset": int,
        "Duration": int,
        "Cutoff": int,
        "AllowUnassociatedTargets": bool,
        "Enabled": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateOpsMetadataResultTypeDef = TypedDict(
    "UpdateOpsMetadataResultTypeDef",
    {
        "OpsMetadataArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateAssociationStatusRequestRequestTypeDef = TypedDict(
    "UpdateAssociationStatusRequestRequestTypeDef",
    {
        "Name": str,
        "InstanceId": str,
        "AssociationStatus": AssociationStatusTypeDef,
    },
)
AssociationTypeDef = TypedDict(
    "AssociationTypeDef",
    {
        "Name": NotRequired[str],
        "InstanceId": NotRequired[str],
        "AssociationId": NotRequired[str],
        "AssociationVersion": NotRequired[str],
        "DocumentVersion": NotRequired[str],
        "Targets": NotRequired[List[TargetTypeDef]],
        "LastExecutionDate": NotRequired[datetime],
        "Overview": NotRequired[AssociationOverviewTypeDef],
        "ScheduleExpression": NotRequired[str],
        "AssociationName": NotRequired[str],
        "ScheduleOffset": NotRequired[int],
        "Duration": NotRequired[int],
        "TargetMaps": NotRequired[List[Dict[str, List[str]]]],
    },
)
DescribeMaintenanceWindowsForTargetRequestRequestTypeDef = TypedDict(
    "DescribeMaintenanceWindowsForTargetRequestRequestTypeDef",
    {
        "Targets": Sequence[TargetTypeDef],
        "ResourceType": MaintenanceWindowResourceTypeType,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
MaintenanceWindowTargetTypeDef = TypedDict(
    "MaintenanceWindowTargetTypeDef",
    {
        "WindowId": NotRequired[str],
        "WindowTargetId": NotRequired[str],
        "ResourceType": NotRequired[MaintenanceWindowResourceTypeType],
        "Targets": NotRequired[List[TargetTypeDef]],
        "OwnerInformation": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
    },
)
RegisterTargetWithMaintenanceWindowRequestRequestTypeDef = TypedDict(
    "RegisterTargetWithMaintenanceWindowRequestRequestTypeDef",
    {
        "WindowId": str,
        "ResourceType": MaintenanceWindowResourceTypeType,
        "Targets": Sequence[TargetTypeDef],
        "OwnerInformation": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "ClientToken": NotRequired[str],
    },
)
UpdateMaintenanceWindowTargetRequestRequestTypeDef = TypedDict(
    "UpdateMaintenanceWindowTargetRequestRequestTypeDef",
    {
        "WindowId": str,
        "WindowTargetId": str,
        "Targets": NotRequired[Sequence[TargetTypeDef]],
        "OwnerInformation": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "Replace": NotRequired[bool],
    },
)
UpdateMaintenanceWindowTargetResultTypeDef = TypedDict(
    "UpdateMaintenanceWindowTargetResultTypeDef",
    {
        "WindowId": str,
        "WindowTargetId": str,
        "Targets": List[TargetTypeDef],
        "OwnerInformation": str,
        "Name": str,
        "Description": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeAssociationExecutionsRequestRequestTypeDef = TypedDict(
    "DescribeAssociationExecutionsRequestRequestTypeDef",
    {
        "AssociationId": str,
        "Filters": NotRequired[Sequence[AssociationExecutionFilterTypeDef]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
AssociationExecutionTargetTypeDef = TypedDict(
    "AssociationExecutionTargetTypeDef",
    {
        "AssociationId": NotRequired[str],
        "AssociationVersion": NotRequired[str],
        "ExecutionId": NotRequired[str],
        "ResourceId": NotRequired[str],
        "ResourceType": NotRequired[str],
        "Status": NotRequired[str],
        "DetailedStatus": NotRequired[str],
        "LastExecutionDate": NotRequired[datetime],
        "OutputSource": NotRequired[OutputSourceTypeDef],
    },
)
DescribeAssociationExecutionTargetsRequestRequestTypeDef = TypedDict(
    "DescribeAssociationExecutionTargetsRequestRequestTypeDef",
    {
        "AssociationId": str,
        "ExecutionId": str,
        "Filters": NotRequired[Sequence[AssociationExecutionTargetsFilterTypeDef]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListAssociationsRequestRequestTypeDef = TypedDict(
    "ListAssociationsRequestRequestTypeDef",
    {
        "AssociationFilterList": NotRequired[Sequence[AssociationFilterTypeDef]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
AssociationPaginatorTypeDef = TypedDict(
    "AssociationPaginatorTypeDef",
    {
        "Name": NotRequired[str],
        "InstanceId": NotRequired[str],
        "AssociationId": NotRequired[str],
        "AssociationVersion": NotRequired[str],
        "DocumentVersion": NotRequired[str],
        "Targets": NotRequired[List[TargetPaginatorTypeDef]],
        "LastExecutionDate": NotRequired[datetime],
        "Overview": NotRequired[AssociationOverviewTypeDef],
        "ScheduleExpression": NotRequired[str],
        "AssociationName": NotRequired[str],
        "ScheduleOffset": NotRequired[int],
        "Duration": NotRequired[int],
        "TargetMaps": NotRequired[List[Dict[str, List[str]]]],
    },
)
MaintenanceWindowTargetPaginatorTypeDef = TypedDict(
    "MaintenanceWindowTargetPaginatorTypeDef",
    {
        "WindowId": NotRequired[str],
        "WindowTargetId": NotRequired[str],
        "ResourceType": NotRequired[MaintenanceWindowResourceTypeType],
        "Targets": NotRequired[List[TargetPaginatorTypeDef]],
        "OwnerInformation": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
    },
)
UpdateDocumentRequestRequestTypeDef = TypedDict(
    "UpdateDocumentRequestRequestTypeDef",
    {
        "Content": str,
        "Name": str,
        "Attachments": NotRequired[Sequence[AttachmentsSourceTypeDef]],
        "DisplayName": NotRequired[str],
        "VersionName": NotRequired[str],
        "DocumentVersion": NotRequired[str],
        "DocumentFormat": NotRequired[DocumentFormatType],
        "TargetType": NotRequired[str],
    },
)
DescribeAutomationExecutionsRequestRequestTypeDef = TypedDict(
    "DescribeAutomationExecutionsRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence[AutomationExecutionFilterTypeDef]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
GetCommandInvocationResultTypeDef = TypedDict(
    "GetCommandInvocationResultTypeDef",
    {
        "CommandId": str,
        "InstanceId": str,
        "Comment": str,
        "DocumentName": str,
        "DocumentVersion": str,
        "PluginName": str,
        "ResponseCode": int,
        "ExecutionStartDateTime": str,
        "ExecutionElapsedTime": str,
        "ExecutionEndDateTime": str,
        "Status": CommandInvocationStatusType,
        "StatusDetails": str,
        "StandardOutputContent": str,
        "StandardOutputUrl": str,
        "StandardErrorContent": str,
        "StandardErrorUrl": str,
        "CloudWatchOutputConfig": CloudWatchOutputConfigTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListCommandInvocationsRequestRequestTypeDef = TypedDict(
    "ListCommandInvocationsRequestRequestTypeDef",
    {
        "CommandId": NotRequired[str],
        "InstanceId": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "Filters": NotRequired[Sequence[CommandFilterTypeDef]],
        "Details": NotRequired[bool],
    },
)
ListCommandsRequestRequestTypeDef = TypedDict(
    "ListCommandsRequestRequestTypeDef",
    {
        "CommandId": NotRequired[str],
        "InstanceId": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "Filters": NotRequired[Sequence[CommandFilterTypeDef]],
    },
)
CommandInvocationTypeDef = TypedDict(
    "CommandInvocationTypeDef",
    {
        "CommandId": NotRequired[str],
        "InstanceId": NotRequired[str],
        "InstanceName": NotRequired[str],
        "Comment": NotRequired[str],
        "DocumentName": NotRequired[str],
        "DocumentVersion": NotRequired[str],
        "RequestedDateTime": NotRequired[datetime],
        "Status": NotRequired[CommandInvocationStatusType],
        "StatusDetails": NotRequired[str],
        "TraceOutput": NotRequired[str],
        "StandardOutputUrl": NotRequired[str],
        "StandardErrorUrl": NotRequired[str],
        "CommandPlugins": NotRequired[List[CommandPluginTypeDef]],
        "ServiceRole": NotRequired[str],
        "NotificationConfig": NotRequired[NotificationConfigTypeDef],
        "CloudWatchOutputConfig": NotRequired[CloudWatchOutputConfigTypeDef],
    },
)
MaintenanceWindowRunCommandParametersTypeDef = TypedDict(
    "MaintenanceWindowRunCommandParametersTypeDef",
    {
        "Comment": NotRequired[str],
        "CloudWatchOutputConfig": NotRequired[CloudWatchOutputConfigTypeDef],
        "DocumentHash": NotRequired[str],
        "DocumentHashType": NotRequired[DocumentHashTypeType],
        "DocumentVersion": NotRequired[str],
        "NotificationConfig": NotRequired[NotificationConfigTypeDef],
        "OutputS3BucketName": NotRequired[str],
        "OutputS3KeyPrefix": NotRequired[str],
        "Parameters": NotRequired[Dict[str, List[str]]],
        "ServiceRoleArn": NotRequired[str],
        "TimeoutSeconds": NotRequired[int],
    },
)
ComplianceItemTypeDef = TypedDict(
    "ComplianceItemTypeDef",
    {
        "ComplianceType": NotRequired[str],
        "ResourceType": NotRequired[str],
        "ResourceId": NotRequired[str],
        "Id": NotRequired[str],
        "Title": NotRequired[str],
        "Status": NotRequired[ComplianceStatusType],
        "Severity": NotRequired[ComplianceSeverityType],
        "ExecutionSummary": NotRequired[ComplianceExecutionSummaryTypeDef],
        "Details": NotRequired[Dict[str, str]],
    },
)
PutComplianceItemsRequestRequestTypeDef = TypedDict(
    "PutComplianceItemsRequestRequestTypeDef",
    {
        "ResourceId": str,
        "ResourceType": str,
        "ComplianceType": str,
        "ExecutionSummary": ComplianceExecutionSummaryTypeDef,
        "Items": Sequence[ComplianceItemEntryTypeDef],
        "ItemContentHash": NotRequired[str],
        "UploadType": NotRequired[ComplianceUploadTypeType],
    },
)
ListComplianceItemsRequestRequestTypeDef = TypedDict(
    "ListComplianceItemsRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence[ComplianceStringFilterTypeDef]],
        "ResourceIds": NotRequired[Sequence[str]],
        "ResourceTypes": NotRequired[Sequence[str]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListComplianceSummariesRequestRequestTypeDef = TypedDict(
    "ListComplianceSummariesRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence[ComplianceStringFilterTypeDef]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListResourceComplianceSummariesRequestRequestTypeDef = TypedDict(
    "ListResourceComplianceSummariesRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence[ComplianceStringFilterTypeDef]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
CompliantSummaryTypeDef = TypedDict(
    "CompliantSummaryTypeDef",
    {
        "CompliantCount": NotRequired[int],
        "SeveritySummary": NotRequired[SeveritySummaryTypeDef],
    },
)
NonCompliantSummaryTypeDef = TypedDict(
    "NonCompliantSummaryTypeDef",
    {
        "NonCompliantCount": NotRequired[int],
        "SeveritySummary": NotRequired[SeveritySummaryTypeDef],
    },
)
CreateActivationRequestRequestTypeDef = TypedDict(
    "CreateActivationRequestRequestTypeDef",
    {
        "IamRole": str,
        "Description": NotRequired[str],
        "DefaultInstanceName": NotRequired[str],
        "RegistrationLimit": NotRequired[int],
        "ExpirationDate": NotRequired[TimestampTypeDef],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "RegistrationMetadata": NotRequired[Sequence[RegistrationMetadataItemTypeDef]],
    },
)
CreateDocumentRequestRequestTypeDef = TypedDict(
    "CreateDocumentRequestRequestTypeDef",
    {
        "Content": str,
        "Name": str,
        "Requires": NotRequired[Sequence[DocumentRequiresTypeDef]],
        "Attachments": NotRequired[Sequence[AttachmentsSourceTypeDef]],
        "DisplayName": NotRequired[str],
        "VersionName": NotRequired[str],
        "DocumentType": NotRequired[DocumentTypeType],
        "DocumentFormat": NotRequired[DocumentFormatType],
        "TargetType": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
DocumentIdentifierTypeDef = TypedDict(
    "DocumentIdentifierTypeDef",
    {
        "Name": NotRequired[str],
        "CreatedDate": NotRequired[datetime],
        "DisplayName": NotRequired[str],
        "Owner": NotRequired[str],
        "VersionName": NotRequired[str],
        "PlatformTypes": NotRequired[List[PlatformTypeType]],
        "DocumentVersion": NotRequired[str],
        "DocumentType": NotRequired[DocumentTypeType],
        "SchemaVersion": NotRequired[str],
        "DocumentFormat": NotRequired[DocumentFormatType],
        "TargetType": NotRequired[str],
        "Tags": NotRequired[List[TagTypeDef]],
        "Requires": NotRequired[List[DocumentRequiresTypeDef]],
        "ReviewStatus": NotRequired[ReviewStatusType],
        "Author": NotRequired[str],
    },
)
GetDocumentResultTypeDef = TypedDict(
    "GetDocumentResultTypeDef",
    {
        "Name": str,
        "CreatedDate": datetime,
        "DisplayName": str,
        "VersionName": str,
        "DocumentVersion": str,
        "Status": DocumentStatusType,
        "StatusInformation": str,
        "Content": str,
        "DocumentType": DocumentTypeType,
        "DocumentFormat": DocumentFormatType,
        "Requires": List[DocumentRequiresTypeDef],
        "AttachmentsContent": List[AttachmentContentTypeDef],
        "ReviewStatus": ReviewStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
OpsItemSummaryTypeDef = TypedDict(
    "OpsItemSummaryTypeDef",
    {
        "CreatedBy": NotRequired[str],
        "CreatedTime": NotRequired[datetime],
        "LastModifiedBy": NotRequired[str],
        "LastModifiedTime": NotRequired[datetime],
        "Priority": NotRequired[int],
        "Source": NotRequired[str],
        "Status": NotRequired[OpsItemStatusType],
        "OpsItemId": NotRequired[str],
        "Title": NotRequired[str],
        "OperationalData": NotRequired[Dict[str, OpsItemDataValueTypeDef]],
        "Category": NotRequired[str],
        "Severity": NotRequired[str],
        "OpsItemType": NotRequired[str],
        "ActualStartTime": NotRequired[datetime],
        "ActualEndTime": NotRequired[datetime],
        "PlannedStartTime": NotRequired[datetime],
        "PlannedEndTime": NotRequired[datetime],
    },
)
CreateOpsItemRequestRequestTypeDef = TypedDict(
    "CreateOpsItemRequestRequestTypeDef",
    {
        "Description": str,
        "Source": str,
        "Title": str,
        "OpsItemType": NotRequired[str],
        "OperationalData": NotRequired[Mapping[str, OpsItemDataValueTypeDef]],
        "Notifications": NotRequired[Sequence[OpsItemNotificationTypeDef]],
        "Priority": NotRequired[int],
        "RelatedOpsItems": NotRequired[Sequence[RelatedOpsItemTypeDef]],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "Category": NotRequired[str],
        "Severity": NotRequired[str],
        "ActualStartTime": NotRequired[TimestampTypeDef],
        "ActualEndTime": NotRequired[TimestampTypeDef],
        "PlannedStartTime": NotRequired[TimestampTypeDef],
        "PlannedEndTime": NotRequired[TimestampTypeDef],
        "AccountId": NotRequired[str],
    },
)
OpsItemTypeDef = TypedDict(
    "OpsItemTypeDef",
    {
        "CreatedBy": NotRequired[str],
        "OpsItemType": NotRequired[str],
        "CreatedTime": NotRequired[datetime],
        "Description": NotRequired[str],
        "LastModifiedBy": NotRequired[str],
        "LastModifiedTime": NotRequired[datetime],
        "Notifications": NotRequired[List[OpsItemNotificationTypeDef]],
        "Priority": NotRequired[int],
        "RelatedOpsItems": NotRequired[List[RelatedOpsItemTypeDef]],
        "Status": NotRequired[OpsItemStatusType],
        "OpsItemId": NotRequired[str],
        "Version": NotRequired[str],
        "Title": NotRequired[str],
        "Source": NotRequired[str],
        "OperationalData": NotRequired[Dict[str, OpsItemDataValueTypeDef]],
        "Category": NotRequired[str],
        "Severity": NotRequired[str],
        "ActualStartTime": NotRequired[datetime],
        "ActualEndTime": NotRequired[datetime],
        "PlannedStartTime": NotRequired[datetime],
        "PlannedEndTime": NotRequired[datetime],
        "OpsItemArn": NotRequired[str],
    },
)
UpdateOpsItemRequestRequestTypeDef = TypedDict(
    "UpdateOpsItemRequestRequestTypeDef",
    {
        "OpsItemId": str,
        "Description": NotRequired[str],
        "OperationalData": NotRequired[Mapping[str, OpsItemDataValueTypeDef]],
        "OperationalDataToDelete": NotRequired[Sequence[str]],
        "Notifications": NotRequired[Sequence[OpsItemNotificationTypeDef]],
        "Priority": NotRequired[int],
        "RelatedOpsItems": NotRequired[Sequence[RelatedOpsItemTypeDef]],
        "Status": NotRequired[OpsItemStatusType],
        "Title": NotRequired[str],
        "Category": NotRequired[str],
        "Severity": NotRequired[str],
        "ActualStartTime": NotRequired[TimestampTypeDef],
        "ActualEndTime": NotRequired[TimestampTypeDef],
        "PlannedStartTime": NotRequired[TimestampTypeDef],
        "PlannedEndTime": NotRequired[TimestampTypeDef],
        "OpsItemArn": NotRequired[str],
    },
)
CreateOpsMetadataRequestRequestTypeDef = TypedDict(
    "CreateOpsMetadataRequestRequestTypeDef",
    {
        "ResourceId": str,
        "Metadata": NotRequired[Mapping[str, MetadataValueTypeDef]],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
GetOpsMetadataResultTypeDef = TypedDict(
    "GetOpsMetadataResultTypeDef",
    {
        "ResourceId": str,
        "Metadata": Dict[str, MetadataValueTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateOpsMetadataRequestRequestTypeDef = TypedDict(
    "UpdateOpsMetadataRequestRequestTypeDef",
    {
        "OpsMetadataArn": str,
        "MetadataToUpdate": NotRequired[Mapping[str, MetadataValueTypeDef]],
        "KeysToDelete": NotRequired[Sequence[str]],
    },
)
DescribeActivationsRequestRequestTypeDef = TypedDict(
    "DescribeActivationsRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence[DescribeActivationsFilterTypeDef]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DescribeActivationsRequestDescribeActivationsPaginateTypeDef = TypedDict(
    "DescribeActivationsRequestDescribeActivationsPaginateTypeDef",
    {
        "Filters": NotRequired[Sequence[DescribeActivationsFilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeAssociationExecutionTargetsRequestDescribeAssociationExecutionTargetsPaginateTypeDef = TypedDict(
    "DescribeAssociationExecutionTargetsRequestDescribeAssociationExecutionTargetsPaginateTypeDef",
    {
        "AssociationId": str,
        "ExecutionId": str,
        "Filters": NotRequired[Sequence[AssociationExecutionTargetsFilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeAssociationExecutionsRequestDescribeAssociationExecutionsPaginateTypeDef = TypedDict(
    "DescribeAssociationExecutionsRequestDescribeAssociationExecutionsPaginateTypeDef",
    {
        "AssociationId": str,
        "Filters": NotRequired[Sequence[AssociationExecutionFilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeAutomationExecutionsRequestDescribeAutomationExecutionsPaginateTypeDef = TypedDict(
    "DescribeAutomationExecutionsRequestDescribeAutomationExecutionsPaginateTypeDef",
    {
        "Filters": NotRequired[Sequence[AutomationExecutionFilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeEffectiveInstanceAssociationsRequestDescribeEffectiveInstanceAssociationsPaginateTypeDef = TypedDict(
    "DescribeEffectiveInstanceAssociationsRequestDescribeEffectiveInstanceAssociationsPaginateTypeDef",
    {
        "InstanceId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeEffectivePatchesForPatchBaselineRequestDescribeEffectivePatchesForPatchBaselinePaginateTypeDef = TypedDict(
    "DescribeEffectivePatchesForPatchBaselineRequestDescribeEffectivePatchesForPatchBaselinePaginateTypeDef",
    {
        "BaselineId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeInstanceAssociationsStatusRequestDescribeInstanceAssociationsStatusPaginateTypeDef = TypedDict(
    "DescribeInstanceAssociationsStatusRequestDescribeInstanceAssociationsStatusPaginateTypeDef",
    {
        "InstanceId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeInstancePatchStatesRequestDescribeInstancePatchStatesPaginateTypeDef = TypedDict(
    "DescribeInstancePatchStatesRequestDescribeInstancePatchStatesPaginateTypeDef",
    {
        "InstanceIds": Sequence[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeInventoryDeletionsRequestDescribeInventoryDeletionsPaginateTypeDef = TypedDict(
    "DescribeInventoryDeletionsRequestDescribeInventoryDeletionsPaginateTypeDef",
    {
        "DeletionId": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeMaintenanceWindowsForTargetRequestDescribeMaintenanceWindowsForTargetPaginateTypeDef = TypedDict(
    "DescribeMaintenanceWindowsForTargetRequestDescribeMaintenanceWindowsForTargetPaginateTypeDef",
    {
        "Targets": Sequence[TargetPaginatorTypeDef],
        "ResourceType": MaintenanceWindowResourceTypeType,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribePatchPropertiesRequestDescribePatchPropertiesPaginateTypeDef = TypedDict(
    "DescribePatchPropertiesRequestDescribePatchPropertiesPaginateTypeDef",
    {
        "OperatingSystem": OperatingSystemType,
        "Property": PatchPropertyType,
        "PatchSet": NotRequired[PatchSetType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetInventorySchemaRequestGetInventorySchemaPaginateTypeDef = TypedDict(
    "GetInventorySchemaRequestGetInventorySchemaPaginateTypeDef",
    {
        "TypeName": NotRequired[str],
        "Aggregator": NotRequired[bool],
        "SubType": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetParameterHistoryRequestGetParameterHistoryPaginateTypeDef = TypedDict(
    "GetParameterHistoryRequestGetParameterHistoryPaginateTypeDef",
    {
        "Name": str,
        "WithDecryption": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetResourcePoliciesRequestGetResourcePoliciesPaginateTypeDef = TypedDict(
    "GetResourcePoliciesRequestGetResourcePoliciesPaginateTypeDef",
    {
        "ResourceArn": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListAssociationVersionsRequestListAssociationVersionsPaginateTypeDef = TypedDict(
    "ListAssociationVersionsRequestListAssociationVersionsPaginateTypeDef",
    {
        "AssociationId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListAssociationsRequestListAssociationsPaginateTypeDef = TypedDict(
    "ListAssociationsRequestListAssociationsPaginateTypeDef",
    {
        "AssociationFilterList": NotRequired[Sequence[AssociationFilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListCommandInvocationsRequestListCommandInvocationsPaginateTypeDef = TypedDict(
    "ListCommandInvocationsRequestListCommandInvocationsPaginateTypeDef",
    {
        "CommandId": NotRequired[str],
        "InstanceId": NotRequired[str],
        "Filters": NotRequired[Sequence[CommandFilterTypeDef]],
        "Details": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListCommandsRequestListCommandsPaginateTypeDef = TypedDict(
    "ListCommandsRequestListCommandsPaginateTypeDef",
    {
        "CommandId": NotRequired[str],
        "InstanceId": NotRequired[str],
        "Filters": NotRequired[Sequence[CommandFilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListComplianceItemsRequestListComplianceItemsPaginateTypeDef = TypedDict(
    "ListComplianceItemsRequestListComplianceItemsPaginateTypeDef",
    {
        "Filters": NotRequired[Sequence[ComplianceStringFilterTypeDef]],
        "ResourceIds": NotRequired[Sequence[str]],
        "ResourceTypes": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListComplianceSummariesRequestListComplianceSummariesPaginateTypeDef = TypedDict(
    "ListComplianceSummariesRequestListComplianceSummariesPaginateTypeDef",
    {
        "Filters": NotRequired[Sequence[ComplianceStringFilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDocumentVersionsRequestListDocumentVersionsPaginateTypeDef = TypedDict(
    "ListDocumentVersionsRequestListDocumentVersionsPaginateTypeDef",
    {
        "Name": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListResourceComplianceSummariesRequestListResourceComplianceSummariesPaginateTypeDef = TypedDict(
    "ListResourceComplianceSummariesRequestListResourceComplianceSummariesPaginateTypeDef",
    {
        "Filters": NotRequired[Sequence[ComplianceStringFilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListResourceDataSyncRequestListResourceDataSyncPaginateTypeDef = TypedDict(
    "ListResourceDataSyncRequestListResourceDataSyncPaginateTypeDef",
    {
        "SyncType": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeAutomationStepExecutionsRequestDescribeAutomationStepExecutionsPaginateTypeDef = TypedDict(
    "DescribeAutomationStepExecutionsRequestDescribeAutomationStepExecutionsPaginateTypeDef",
    {
        "AutomationExecutionId": str,
        "Filters": NotRequired[Sequence[StepExecutionFilterTypeDef]],
        "ReverseOrder": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeAutomationStepExecutionsRequestRequestTypeDef = TypedDict(
    "DescribeAutomationStepExecutionsRequestRequestTypeDef",
    {
        "AutomationExecutionId": str,
        "Filters": NotRequired[Sequence[StepExecutionFilterTypeDef]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "ReverseOrder": NotRequired[bool],
    },
)
DescribeAvailablePatchesRequestDescribeAvailablePatchesPaginateTypeDef = TypedDict(
    "DescribeAvailablePatchesRequestDescribeAvailablePatchesPaginateTypeDef",
    {
        "Filters": NotRequired[Sequence[PatchOrchestratorFilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeAvailablePatchesRequestRequestTypeDef = TypedDict(
    "DescribeAvailablePatchesRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence[PatchOrchestratorFilterTypeDef]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DescribeInstancePatchesRequestDescribeInstancePatchesPaginateTypeDef = TypedDict(
    "DescribeInstancePatchesRequestDescribeInstancePatchesPaginateTypeDef",
    {
        "InstanceId": str,
        "Filters": NotRequired[Sequence[PatchOrchestratorFilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeInstancePatchesRequestRequestTypeDef = TypedDict(
    "DescribeInstancePatchesRequestRequestTypeDef",
    {
        "InstanceId": str,
        "Filters": NotRequired[Sequence[PatchOrchestratorFilterTypeDef]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
DescribeMaintenanceWindowScheduleRequestDescribeMaintenanceWindowSchedulePaginateTypeDef = (
    TypedDict(
        "DescribeMaintenanceWindowScheduleRequestDescribeMaintenanceWindowSchedulePaginateTypeDef",
        {
            "WindowId": NotRequired[str],
            "Targets": NotRequired[Sequence[TargetPaginatorTypeDef]],
            "ResourceType": NotRequired[MaintenanceWindowResourceTypeType],
            "Filters": NotRequired[Sequence[PatchOrchestratorFilterTypeDef]],
            "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
        },
    )
)
DescribeMaintenanceWindowScheduleRequestRequestTypeDef = TypedDict(
    "DescribeMaintenanceWindowScheduleRequestRequestTypeDef",
    {
        "WindowId": NotRequired[str],
        "Targets": NotRequired[Sequence[TargetTypeDef]],
        "ResourceType": NotRequired[MaintenanceWindowResourceTypeType],
        "Filters": NotRequired[Sequence[PatchOrchestratorFilterTypeDef]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DescribePatchBaselinesRequestDescribePatchBaselinesPaginateTypeDef = TypedDict(
    "DescribePatchBaselinesRequestDescribePatchBaselinesPaginateTypeDef",
    {
        "Filters": NotRequired[Sequence[PatchOrchestratorFilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribePatchBaselinesRequestRequestTypeDef = TypedDict(
    "DescribePatchBaselinesRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence[PatchOrchestratorFilterTypeDef]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DescribePatchGroupsRequestDescribePatchGroupsPaginateTypeDef = TypedDict(
    "DescribePatchGroupsRequestDescribePatchGroupsPaginateTypeDef",
    {
        "Filters": NotRequired[Sequence[PatchOrchestratorFilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribePatchGroupsRequestRequestTypeDef = TypedDict(
    "DescribePatchGroupsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "Filters": NotRequired[Sequence[PatchOrchestratorFilterTypeDef]],
        "NextToken": NotRequired[str],
    },
)
DescribeAvailablePatchesResultTypeDef = TypedDict(
    "DescribeAvailablePatchesResultTypeDef",
    {
        "Patches": List[PatchTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeEffectiveInstanceAssociationsResultTypeDef = TypedDict(
    "DescribeEffectiveInstanceAssociationsResultTypeDef",
    {
        "Associations": List[InstanceAssociationTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeInstanceInformationRequestDescribeInstanceInformationPaginateTypeDef = TypedDict(
    "DescribeInstanceInformationRequestDescribeInstanceInformationPaginateTypeDef",
    {
        "InstanceInformationFilterList": NotRequired[Sequence[InstanceInformationFilterTypeDef]],
        "Filters": NotRequired[Sequence[InstanceInformationStringFilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeInstanceInformationRequestRequestTypeDef = TypedDict(
    "DescribeInstanceInformationRequestRequestTypeDef",
    {
        "InstanceInformationFilterList": NotRequired[Sequence[InstanceInformationFilterTypeDef]],
        "Filters": NotRequired[Sequence[InstanceInformationStringFilterTypeDef]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DescribeInstancePatchStatesForPatchGroupRequestDescribeInstancePatchStatesForPatchGroupPaginateTypeDef = TypedDict(
    "DescribeInstancePatchStatesForPatchGroupRequestDescribeInstancePatchStatesForPatchGroupPaginateTypeDef",
    {
        "PatchGroup": str,
        "Filters": NotRequired[Sequence[InstancePatchStateFilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeInstancePatchStatesForPatchGroupRequestRequestTypeDef = TypedDict(
    "DescribeInstancePatchStatesForPatchGroupRequestRequestTypeDef",
    {
        "PatchGroup": str,
        "Filters": NotRequired[Sequence[InstancePatchStateFilterTypeDef]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
DescribeInstancePatchStatesForPatchGroupResultTypeDef = TypedDict(
    "DescribeInstancePatchStatesForPatchGroupResultTypeDef",
    {
        "InstancePatchStates": List[InstancePatchStateTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeInstancePatchStatesResultTypeDef = TypedDict(
    "DescribeInstancePatchStatesResultTypeDef",
    {
        "InstancePatchStates": List[InstancePatchStateTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeInstancePatchesResultTypeDef = TypedDict(
    "DescribeInstancePatchesResultTypeDef",
    {
        "Patches": List[PatchComplianceDataTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeMaintenanceWindowExecutionTaskInvocationsRequestDescribeMaintenanceWindowExecutionTaskInvocationsPaginateTypeDef = TypedDict(
    "DescribeMaintenanceWindowExecutionTaskInvocationsRequestDescribeMaintenanceWindowExecutionTaskInvocationsPaginateTypeDef",
    {
        "WindowExecutionId": str,
        "TaskId": str,
        "Filters": NotRequired[Sequence[MaintenanceWindowFilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeMaintenanceWindowExecutionTaskInvocationsRequestRequestTypeDef = TypedDict(
    "DescribeMaintenanceWindowExecutionTaskInvocationsRequestRequestTypeDef",
    {
        "WindowExecutionId": str,
        "TaskId": str,
        "Filters": NotRequired[Sequence[MaintenanceWindowFilterTypeDef]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DescribeMaintenanceWindowExecutionTasksRequestDescribeMaintenanceWindowExecutionTasksPaginateTypeDef = TypedDict(
    "DescribeMaintenanceWindowExecutionTasksRequestDescribeMaintenanceWindowExecutionTasksPaginateTypeDef",
    {
        "WindowExecutionId": str,
        "Filters": NotRequired[Sequence[MaintenanceWindowFilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeMaintenanceWindowExecutionTasksRequestRequestTypeDef = TypedDict(
    "DescribeMaintenanceWindowExecutionTasksRequestRequestTypeDef",
    {
        "WindowExecutionId": str,
        "Filters": NotRequired[Sequence[MaintenanceWindowFilterTypeDef]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DescribeMaintenanceWindowExecutionsRequestDescribeMaintenanceWindowExecutionsPaginateTypeDef = TypedDict(
    "DescribeMaintenanceWindowExecutionsRequestDescribeMaintenanceWindowExecutionsPaginateTypeDef",
    {
        "WindowId": str,
        "Filters": NotRequired[Sequence[MaintenanceWindowFilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeMaintenanceWindowExecutionsRequestRequestTypeDef = TypedDict(
    "DescribeMaintenanceWindowExecutionsRequestRequestTypeDef",
    {
        "WindowId": str,
        "Filters": NotRequired[Sequence[MaintenanceWindowFilterTypeDef]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DescribeMaintenanceWindowTargetsRequestDescribeMaintenanceWindowTargetsPaginateTypeDef = TypedDict(
    "DescribeMaintenanceWindowTargetsRequestDescribeMaintenanceWindowTargetsPaginateTypeDef",
    {
        "WindowId": str,
        "Filters": NotRequired[Sequence[MaintenanceWindowFilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeMaintenanceWindowTargetsRequestRequestTypeDef = TypedDict(
    "DescribeMaintenanceWindowTargetsRequestRequestTypeDef",
    {
        "WindowId": str,
        "Filters": NotRequired[Sequence[MaintenanceWindowFilterTypeDef]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DescribeMaintenanceWindowTasksRequestDescribeMaintenanceWindowTasksPaginateTypeDef = TypedDict(
    "DescribeMaintenanceWindowTasksRequestDescribeMaintenanceWindowTasksPaginateTypeDef",
    {
        "WindowId": str,
        "Filters": NotRequired[Sequence[MaintenanceWindowFilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeMaintenanceWindowTasksRequestRequestTypeDef = TypedDict(
    "DescribeMaintenanceWindowTasksRequestRequestTypeDef",
    {
        "WindowId": str,
        "Filters": NotRequired[Sequence[MaintenanceWindowFilterTypeDef]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DescribeMaintenanceWindowsRequestDescribeMaintenanceWindowsPaginateTypeDef = TypedDict(
    "DescribeMaintenanceWindowsRequestDescribeMaintenanceWindowsPaginateTypeDef",
    {
        "Filters": NotRequired[Sequence[MaintenanceWindowFilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeMaintenanceWindowsRequestRequestTypeDef = TypedDict(
    "DescribeMaintenanceWindowsRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence[MaintenanceWindowFilterTypeDef]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DescribeMaintenanceWindowExecutionTaskInvocationsResultTypeDef = TypedDict(
    "DescribeMaintenanceWindowExecutionTaskInvocationsResultTypeDef",
    {
        "WindowExecutionTaskInvocationIdentities": List[
            MaintenanceWindowExecutionTaskInvocationIdentityTypeDef
        ],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeMaintenanceWindowExecutionsResultTypeDef = TypedDict(
    "DescribeMaintenanceWindowExecutionsResultTypeDef",
    {
        "WindowExecutions": List[MaintenanceWindowExecutionTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeMaintenanceWindowScheduleResultTypeDef = TypedDict(
    "DescribeMaintenanceWindowScheduleResultTypeDef",
    {
        "ScheduledWindowExecutions": List[ScheduledWindowExecutionTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeMaintenanceWindowsForTargetResultTypeDef = TypedDict(
    "DescribeMaintenanceWindowsForTargetResultTypeDef",
    {
        "WindowIdentities": List[MaintenanceWindowIdentityForTargetTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeMaintenanceWindowsResultTypeDef = TypedDict(
    "DescribeMaintenanceWindowsResultTypeDef",
    {
        "WindowIdentities": List[MaintenanceWindowIdentityTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeOpsItemsRequestDescribeOpsItemsPaginateTypeDef = TypedDict(
    "DescribeOpsItemsRequestDescribeOpsItemsPaginateTypeDef",
    {
        "OpsItemFilters": NotRequired[Sequence[OpsItemFilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeOpsItemsRequestRequestTypeDef = TypedDict(
    "DescribeOpsItemsRequestRequestTypeDef",
    {
        "OpsItemFilters": NotRequired[Sequence[OpsItemFilterTypeDef]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
GetParametersByPathRequestGetParametersByPathPaginateTypeDef = TypedDict(
    "GetParametersByPathRequestGetParametersByPathPaginateTypeDef",
    {
        "Path": str,
        "Recursive": NotRequired[bool],
        "ParameterFilters": NotRequired[Sequence[ParameterStringFilterTypeDef]],
        "WithDecryption": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetParametersByPathRequestRequestTypeDef = TypedDict(
    "GetParametersByPathRequestRequestTypeDef",
    {
        "Path": str,
        "Recursive": NotRequired[bool],
        "ParameterFilters": NotRequired[Sequence[ParameterStringFilterTypeDef]],
        "WithDecryption": NotRequired[bool],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DescribeParametersRequestDescribeParametersPaginateTypeDef = TypedDict(
    "DescribeParametersRequestDescribeParametersPaginateTypeDef",
    {
        "Filters": NotRequired[Sequence[ParametersFilterTypeDef]],
        "ParameterFilters": NotRequired[Sequence[ParameterStringFilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeParametersRequestRequestTypeDef = TypedDict(
    "DescribeParametersRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence[ParametersFilterTypeDef]],
        "ParameterFilters": NotRequired[Sequence[ParameterStringFilterTypeDef]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DescribePatchBaselinesResultTypeDef = TypedDict(
    "DescribePatchBaselinesResultTypeDef",
    {
        "BaselineIdentities": List[PatchBaselineIdentityTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PatchGroupPatchBaselineMappingTypeDef = TypedDict(
    "PatchGroupPatchBaselineMappingTypeDef",
    {
        "PatchGroup": NotRequired[str],
        "BaselineIdentity": NotRequired[PatchBaselineIdentityTypeDef],
    },
)
DescribeSessionsRequestDescribeSessionsPaginateTypeDef = TypedDict(
    "DescribeSessionsRequestDescribeSessionsPaginateTypeDef",
    {
        "State": SessionStateType,
        "Filters": NotRequired[Sequence[SessionFilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeSessionsRequestRequestTypeDef = TypedDict(
    "DescribeSessionsRequestRequestTypeDef",
    {
        "State": SessionStateType,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "Filters": NotRequired[Sequence[SessionFilterTypeDef]],
    },
)
UpdateDocumentDefaultVersionResultTypeDef = TypedDict(
    "UpdateDocumentDefaultVersionResultTypeDef",
    {
        "Description": DocumentDefaultVersionDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DocumentDescriptionTypeDef = TypedDict(
    "DocumentDescriptionTypeDef",
    {
        "Sha1": NotRequired[str],
        "Hash": NotRequired[str],
        "HashType": NotRequired[DocumentHashTypeType],
        "Name": NotRequired[str],
        "DisplayName": NotRequired[str],
        "VersionName": NotRequired[str],
        "Owner": NotRequired[str],
        "CreatedDate": NotRequired[datetime],
        "Status": NotRequired[DocumentStatusType],
        "StatusInformation": NotRequired[str],
        "DocumentVersion": NotRequired[str],
        "Description": NotRequired[str],
        "Parameters": NotRequired[List[DocumentParameterTypeDef]],
        "PlatformTypes": NotRequired[List[PlatformTypeType]],
        "DocumentType": NotRequired[DocumentTypeType],
        "SchemaVersion": NotRequired[str],
        "LatestVersion": NotRequired[str],
        "DefaultVersion": NotRequired[str],
        "DocumentFormat": NotRequired[DocumentFormatType],
        "TargetType": NotRequired[str],
        "Tags": NotRequired[List[TagTypeDef]],
        "AttachmentsInformation": NotRequired[List[AttachmentInformationTypeDef]],
        "Requires": NotRequired[List[DocumentRequiresTypeDef]],
        "Author": NotRequired[str],
        "ReviewInformation": NotRequired[List[ReviewInformationTypeDef]],
        "ApprovedVersion": NotRequired[str],
        "PendingReviewVersion": NotRequired[str],
        "ReviewStatus": NotRequired[ReviewStatusType],
        "Category": NotRequired[List[str]],
        "CategoryEnum": NotRequired[List[str]],
    },
)
ListDocumentsRequestListDocumentsPaginateTypeDef = TypedDict(
    "ListDocumentsRequestListDocumentsPaginateTypeDef",
    {
        "DocumentFilterList": NotRequired[Sequence[DocumentFilterTypeDef]],
        "Filters": NotRequired[Sequence[DocumentKeyValuesFilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDocumentsRequestRequestTypeDef = TypedDict(
    "ListDocumentsRequestRequestTypeDef",
    {
        "DocumentFilterList": NotRequired[Sequence[DocumentFilterTypeDef]],
        "Filters": NotRequired[Sequence[DocumentKeyValuesFilterTypeDef]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DocumentReviewerResponseSourceTypeDef = TypedDict(
    "DocumentReviewerResponseSourceTypeDef",
    {
        "CreateTime": NotRequired[datetime],
        "UpdatedTime": NotRequired[datetime],
        "ReviewStatus": NotRequired[ReviewStatusType],
        "Comment": NotRequired[List[DocumentReviewCommentSourceTypeDef]],
        "Reviewer": NotRequired[str],
    },
)
DocumentReviewsTypeDef = TypedDict(
    "DocumentReviewsTypeDef",
    {
        "Action": DocumentReviewActionType,
        "Comment": NotRequired[Sequence[DocumentReviewCommentSourceTypeDef]],
    },
)
ListDocumentVersionsResultTypeDef = TypedDict(
    "ListDocumentVersionsResultTypeDef",
    {
        "DocumentVersions": List[DocumentVersionInfoTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EffectivePatchTypeDef = TypedDict(
    "EffectivePatchTypeDef",
    {
        "Patch": NotRequired[PatchTypeDef],
        "PatchStatus": NotRequired[PatchStatusTypeDef],
    },
)
GetCommandInvocationRequestCommandExecutedWaitTypeDef = TypedDict(
    "GetCommandInvocationRequestCommandExecutedWaitTypeDef",
    {
        "CommandId": str,
        "InstanceId": str,
        "PluginName": NotRequired[str],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
InventoryGroupTypeDef = TypedDict(
    "InventoryGroupTypeDef",
    {
        "Name": str,
        "Filters": Sequence[InventoryFilterTypeDef],
    },
)
ListInventoryEntriesRequestRequestTypeDef = TypedDict(
    "ListInventoryEntriesRequestRequestTypeDef",
    {
        "InstanceId": str,
        "TypeName": str,
        "Filters": NotRequired[Sequence[InventoryFilterTypeDef]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
GetInventoryRequestRequestTypeDef = TypedDict(
    "GetInventoryRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence[InventoryFilterTypeDef]],
        "Aggregators": NotRequired[Sequence["InventoryAggregatorTypeDef"]],
        "ResultAttributes": NotRequired[Sequence[ResultAttributeTypeDef]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
OpsAggregatorTypeDef = TypedDict(
    "OpsAggregatorTypeDef",
    {
        "AggregatorType": NotRequired[str],
        "TypeName": NotRequired[str],
        "AttributeName": NotRequired[str],
        "Values": NotRequired[Mapping[str, str]],
        "Filters": NotRequired[Sequence[OpsFilterTypeDef]],
        "Aggregators": NotRequired[Sequence[Dict[str, Any]]],
    },
)
GetOpsSummaryRequestRequestTypeDef = TypedDict(
    "GetOpsSummaryRequestRequestTypeDef",
    {
        "SyncName": NotRequired[str],
        "Filters": NotRequired[Sequence[OpsFilterTypeDef]],
        "Aggregators": NotRequired[Sequence["OpsAggregatorTypeDef"]],
        "ResultAttributes": NotRequired[Sequence[OpsResultAttributeTypeDef]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
GetParameterResultTypeDef = TypedDict(
    "GetParameterResultTypeDef",
    {
        "Parameter": ParameterTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetParametersByPathResultTypeDef = TypedDict(
    "GetParametersByPathResultTypeDef",
    {
        "Parameters": List[ParameterTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetParametersResultTypeDef = TypedDict(
    "GetParametersResultTypeDef",
    {
        "Parameters": List[ParameterTypeDef],
        "InvalidParameters": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetResourcePoliciesResponseTypeDef = TypedDict(
    "GetResourcePoliciesResponseTypeDef",
    {
        "NextToken": str,
        "Policies": List[GetResourcePoliciesResponseEntryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetServiceSettingResultTypeDef = TypedDict(
    "GetServiceSettingResultTypeDef",
    {
        "ServiceSetting": ServiceSettingTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ResetServiceSettingResultTypeDef = TypedDict(
    "ResetServiceSettingResultTypeDef",
    {
        "ServiceSetting": ServiceSettingTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
InstanceInformationTypeDef = TypedDict(
    "InstanceInformationTypeDef",
    {
        "InstanceId": NotRequired[str],
        "PingStatus": NotRequired[PingStatusType],
        "LastPingDateTime": NotRequired[datetime],
        "AgentVersion": NotRequired[str],
        "IsLatestVersion": NotRequired[bool],
        "PlatformType": NotRequired[PlatformTypeType],
        "PlatformName": NotRequired[str],
        "PlatformVersion": NotRequired[str],
        "ActivationId": NotRequired[str],
        "IamRole": NotRequired[str],
        "RegistrationDate": NotRequired[datetime],
        "ResourceType": NotRequired[ResourceTypeType],
        "Name": NotRequired[str],
        "IPAddress": NotRequired[str],
        "ComputerName": NotRequired[str],
        "AssociationStatus": NotRequired[str],
        "LastAssociationExecutionDate": NotRequired[datetime],
        "LastSuccessfulAssociationExecutionDate": NotRequired[datetime],
        "AssociationOverview": NotRequired[InstanceAggregatedAssociationOverviewTypeDef],
        "SourceId": NotRequired[str],
        "SourceType": NotRequired[SourceTypeType],
    },
)
InstanceAssociationOutputLocationTypeDef = TypedDict(
    "InstanceAssociationOutputLocationTypeDef",
    {
        "S3Location": NotRequired[S3OutputLocationTypeDef],
    },
)
InstanceAssociationOutputUrlTypeDef = TypedDict(
    "InstanceAssociationOutputUrlTypeDef",
    {
        "S3OutputUrl": NotRequired[S3OutputUrlTypeDef],
    },
)
InventoryDeletionSummaryTypeDef = TypedDict(
    "InventoryDeletionSummaryTypeDef",
    {
        "TotalCount": NotRequired[int],
        "RemainingCount": NotRequired[int],
        "SummaryItems": NotRequired[List[InventoryDeletionSummaryItemTypeDef]],
    },
)
InventoryItemSchemaTypeDef = TypedDict(
    "InventoryItemSchemaTypeDef",
    {
        "TypeName": str,
        "Attributes": List[InventoryItemAttributeTypeDef],
        "Version": NotRequired[str],
        "DisplayName": NotRequired[str],
    },
)
PutInventoryRequestRequestTypeDef = TypedDict(
    "PutInventoryRequestRequestTypeDef",
    {
        "InstanceId": str,
        "Items": Sequence[InventoryItemTypeDef],
    },
)
InventoryResultEntityTypeDef = TypedDict(
    "InventoryResultEntityTypeDef",
    {
        "Id": NotRequired[str],
        "Data": NotRequired[Dict[str, InventoryResultItemTypeDef]],
    },
)
ListOpsItemEventsRequestListOpsItemEventsPaginateTypeDef = TypedDict(
    "ListOpsItemEventsRequestListOpsItemEventsPaginateTypeDef",
    {
        "Filters": NotRequired[Sequence[OpsItemEventFilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListOpsItemEventsRequestRequestTypeDef = TypedDict(
    "ListOpsItemEventsRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence[OpsItemEventFilterTypeDef]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListOpsItemRelatedItemsRequestListOpsItemRelatedItemsPaginateTypeDef = TypedDict(
    "ListOpsItemRelatedItemsRequestListOpsItemRelatedItemsPaginateTypeDef",
    {
        "OpsItemId": NotRequired[str],
        "Filters": NotRequired[Sequence[OpsItemRelatedItemsFilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListOpsItemRelatedItemsRequestRequestTypeDef = TypedDict(
    "ListOpsItemRelatedItemsRequestRequestTypeDef",
    {
        "OpsItemId": NotRequired[str],
        "Filters": NotRequired[Sequence[OpsItemRelatedItemsFilterTypeDef]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListOpsMetadataRequestListOpsMetadataPaginateTypeDef = TypedDict(
    "ListOpsMetadataRequestListOpsMetadataPaginateTypeDef",
    {
        "Filters": NotRequired[Sequence[OpsMetadataFilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListOpsMetadataRequestRequestTypeDef = TypedDict(
    "ListOpsMetadataRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence[OpsMetadataFilterTypeDef]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListOpsMetadataResultTypeDef = TypedDict(
    "ListOpsMetadataResultTypeDef",
    {
        "OpsMetadataList": List[OpsMetadataTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
OpsEntityTypeDef = TypedDict(
    "OpsEntityTypeDef",
    {
        "Id": NotRequired[str],
        "Data": NotRequired[Dict[str, OpsEntityItemTypeDef]],
    },
)
OpsItemEventSummaryTypeDef = TypedDict(
    "OpsItemEventSummaryTypeDef",
    {
        "OpsItemId": NotRequired[str],
        "EventId": NotRequired[str],
        "Source": NotRequired[str],
        "DetailType": NotRequired[str],
        "Detail": NotRequired[str],
        "CreatedBy": NotRequired[OpsItemIdentityTypeDef],
        "CreatedTime": NotRequired[datetime],
    },
)
OpsItemRelatedItemSummaryTypeDef = TypedDict(
    "OpsItemRelatedItemSummaryTypeDef",
    {
        "OpsItemId": NotRequired[str],
        "AssociationId": NotRequired[str],
        "ResourceType": NotRequired[str],
        "AssociationType": NotRequired[str],
        "ResourceUri": NotRequired[str],
        "CreatedBy": NotRequired[OpsItemIdentityTypeDef],
        "CreatedTime": NotRequired[datetime],
        "LastModifiedBy": NotRequired[OpsItemIdentityTypeDef],
        "LastModifiedTime": NotRequired[datetime],
    },
)
ParameterHistoryTypeDef = TypedDict(
    "ParameterHistoryTypeDef",
    {
        "Name": NotRequired[str],
        "Type": NotRequired[ParameterTypeType],
        "KeyId": NotRequired[str],
        "LastModifiedDate": NotRequired[datetime],
        "LastModifiedUser": NotRequired[str],
        "Description": NotRequired[str],
        "Value": NotRequired[str],
        "AllowedPattern": NotRequired[str],
        "Version": NotRequired[int],
        "Labels": NotRequired[List[str]],
        "Tier": NotRequired[ParameterTierType],
        "Policies": NotRequired[List[ParameterInlinePolicyTypeDef]],
        "DataType": NotRequired[str],
    },
)
ParameterMetadataTypeDef = TypedDict(
    "ParameterMetadataTypeDef",
    {
        "Name": NotRequired[str],
        "Type": NotRequired[ParameterTypeType],
        "KeyId": NotRequired[str],
        "LastModifiedDate": NotRequired[datetime],
        "LastModifiedUser": NotRequired[str],
        "Description": NotRequired[str],
        "AllowedPattern": NotRequired[str],
        "Version": NotRequired[int],
        "Tier": NotRequired[ParameterTierType],
        "Policies": NotRequired[List[ParameterInlinePolicyTypeDef]],
        "DataType": NotRequired[str],
    },
)
PatchFilterGroupTypeDef = TypedDict(
    "PatchFilterGroupTypeDef",
    {
        "PatchFilters": Sequence[PatchFilterTypeDef],
    },
)
ResourceDataSyncAwsOrganizationsSourcePaginatorTypeDef = TypedDict(
    "ResourceDataSyncAwsOrganizationsSourcePaginatorTypeDef",
    {
        "OrganizationSourceType": str,
        "OrganizationalUnits": NotRequired[List[ResourceDataSyncOrganizationalUnitTypeDef]],
    },
)
ResourceDataSyncAwsOrganizationsSourceTypeDef = TypedDict(
    "ResourceDataSyncAwsOrganizationsSourceTypeDef",
    {
        "OrganizationSourceType": str,
        "OrganizationalUnits": NotRequired[Sequence[ResourceDataSyncOrganizationalUnitTypeDef]],
    },
)
ResourceDataSyncS3DestinationTypeDef = TypedDict(
    "ResourceDataSyncS3DestinationTypeDef",
    {
        "BucketName": str,
        "SyncFormat": Literal["JsonSerDe"],
        "Region": str,
        "Prefix": NotRequired[str],
        "AWSKMSKeyARN": NotRequired[str],
        "DestinationDataSharing": NotRequired[ResourceDataSyncDestinationDataSharingTypeDef],
    },
)
SessionTypeDef = TypedDict(
    "SessionTypeDef",
    {
        "SessionId": NotRequired[str],
        "Target": NotRequired[str],
        "Status": NotRequired[SessionStatusType],
        "StartDate": NotRequired[datetime],
        "EndDate": NotRequired[datetime],
        "DocumentName": NotRequired[str],
        "Owner": NotRequired[str],
        "Reason": NotRequired[str],
        "Details": NotRequired[str],
        "OutputUrl": NotRequired[SessionManagerOutputUrlTypeDef],
        "MaxSessionDuration": NotRequired[str],
    },
)
DescribeActivationsResultTypeDef = TypedDict(
    "DescribeActivationsResultTypeDef",
    {
        "ActivationList": List[ActivationTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AssociationExecutionPaginatorTypeDef = TypedDict(
    "AssociationExecutionPaginatorTypeDef",
    {
        "AssociationId": NotRequired[str],
        "AssociationVersion": NotRequired[str],
        "ExecutionId": NotRequired[str],
        "Status": NotRequired[str],
        "DetailedStatus": NotRequired[str],
        "CreatedTime": NotRequired[datetime],
        "LastExecutionDate": NotRequired[datetime],
        "ResourceCountByStatus": NotRequired[str],
        "AlarmConfiguration": NotRequired[AlarmConfigurationPaginatorTypeDef],
        "TriggeredAlarms": NotRequired[List[AlarmStateInformationTypeDef]],
    },
)
CommandPaginatorTypeDef = TypedDict(
    "CommandPaginatorTypeDef",
    {
        "CommandId": NotRequired[str],
        "DocumentName": NotRequired[str],
        "DocumentVersion": NotRequired[str],
        "Comment": NotRequired[str],
        "ExpiresAfter": NotRequired[datetime],
        "Parameters": NotRequired[Dict[str, List[str]]],
        "InstanceIds": NotRequired[List[str]],
        "Targets": NotRequired[List[TargetPaginatorTypeDef]],
        "RequestedDateTime": NotRequired[datetime],
        "Status": NotRequired[CommandStatusType],
        "StatusDetails": NotRequired[str],
        "OutputS3Region": NotRequired[str],
        "OutputS3BucketName": NotRequired[str],
        "OutputS3KeyPrefix": NotRequired[str],
        "MaxConcurrency": NotRequired[str],
        "MaxErrors": NotRequired[str],
        "TargetCount": NotRequired[int],
        "CompletedCount": NotRequired[int],
        "ErrorCount": NotRequired[int],
        "DeliveryTimedOutCount": NotRequired[int],
        "ServiceRole": NotRequired[str],
        "NotificationConfig": NotRequired[NotificationConfigTypeDef],
        "CloudWatchOutputConfig": NotRequired[CloudWatchOutputConfigTypeDef],
        "TimeoutSeconds": NotRequired[int],
        "AlarmConfiguration": NotRequired[AlarmConfigurationPaginatorTypeDef],
        "TriggeredAlarms": NotRequired[List[AlarmStateInformationTypeDef]],
    },
)
MaintenanceWindowExecutionTaskIdentityPaginatorTypeDef = TypedDict(
    "MaintenanceWindowExecutionTaskIdentityPaginatorTypeDef",
    {
        "WindowExecutionId": NotRequired[str],
        "TaskExecutionId": NotRequired[str],
        "Status": NotRequired[MaintenanceWindowExecutionStatusType],
        "StatusDetails": NotRequired[str],
        "StartTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
        "TaskArn": NotRequired[str],
        "TaskType": NotRequired[MaintenanceWindowTaskTypeType],
        "AlarmConfiguration": NotRequired[AlarmConfigurationPaginatorTypeDef],
        "TriggeredAlarms": NotRequired[List[AlarmStateInformationTypeDef]],
    },
)
MaintenanceWindowTaskPaginatorTypeDef = TypedDict(
    "MaintenanceWindowTaskPaginatorTypeDef",
    {
        "WindowId": NotRequired[str],
        "WindowTaskId": NotRequired[str],
        "TaskArn": NotRequired[str],
        "Type": NotRequired[MaintenanceWindowTaskTypeType],
        "Targets": NotRequired[List[TargetPaginatorTypeDef]],
        "TaskParameters": NotRequired[
            Dict[str, MaintenanceWindowTaskParameterValueExpressionTypeDef]
        ],
        "Priority": NotRequired[int],
        "LoggingInfo": NotRequired[LoggingInfoTypeDef],
        "ServiceRoleArn": NotRequired[str],
        "MaxConcurrency": NotRequired[str],
        "MaxErrors": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "CutoffBehavior": NotRequired[MaintenanceWindowTaskCutoffBehaviorType],
        "AlarmConfiguration": NotRequired[AlarmConfigurationPaginatorTypeDef],
    },
)
TargetLocationPaginatorTypeDef = TypedDict(
    "TargetLocationPaginatorTypeDef",
    {
        "Accounts": NotRequired[List[str]],
        "Regions": NotRequired[List[str]],
        "TargetLocationMaxConcurrency": NotRequired[str],
        "TargetLocationMaxErrors": NotRequired[str],
        "ExecutionRoleName": NotRequired[str],
        "TargetLocationAlarmConfiguration": NotRequired[AlarmConfigurationPaginatorTypeDef],
    },
)
AssociationExecutionTypeDef = TypedDict(
    "AssociationExecutionTypeDef",
    {
        "AssociationId": NotRequired[str],
        "AssociationVersion": NotRequired[str],
        "ExecutionId": NotRequired[str],
        "Status": NotRequired[str],
        "DetailedStatus": NotRequired[str],
        "CreatedTime": NotRequired[datetime],
        "LastExecutionDate": NotRequired[datetime],
        "ResourceCountByStatus": NotRequired[str],
        "AlarmConfiguration": NotRequired[AlarmConfigurationTypeDef],
        "TriggeredAlarms": NotRequired[List[AlarmStateInformationTypeDef]],
    },
)
CommandTypeDef = TypedDict(
    "CommandTypeDef",
    {
        "CommandId": NotRequired[str],
        "DocumentName": NotRequired[str],
        "DocumentVersion": NotRequired[str],
        "Comment": NotRequired[str],
        "ExpiresAfter": NotRequired[datetime],
        "Parameters": NotRequired[Dict[str, List[str]]],
        "InstanceIds": NotRequired[List[str]],
        "Targets": NotRequired[List[TargetTypeDef]],
        "RequestedDateTime": NotRequired[datetime],
        "Status": NotRequired[CommandStatusType],
        "StatusDetails": NotRequired[str],
        "OutputS3Region": NotRequired[str],
        "OutputS3BucketName": NotRequired[str],
        "OutputS3KeyPrefix": NotRequired[str],
        "MaxConcurrency": NotRequired[str],
        "MaxErrors": NotRequired[str],
        "TargetCount": NotRequired[int],
        "CompletedCount": NotRequired[int],
        "ErrorCount": NotRequired[int],
        "DeliveryTimedOutCount": NotRequired[int],
        "ServiceRole": NotRequired[str],
        "NotificationConfig": NotRequired[NotificationConfigTypeDef],
        "CloudWatchOutputConfig": NotRequired[CloudWatchOutputConfigTypeDef],
        "TimeoutSeconds": NotRequired[int],
        "AlarmConfiguration": NotRequired[AlarmConfigurationTypeDef],
        "TriggeredAlarms": NotRequired[List[AlarmStateInformationTypeDef]],
    },
)
GetMaintenanceWindowExecutionTaskResultTypeDef = TypedDict(
    "GetMaintenanceWindowExecutionTaskResultTypeDef",
    {
        "WindowExecutionId": str,
        "TaskExecutionId": str,
        "TaskArn": str,
        "ServiceRole": str,
        "Type": MaintenanceWindowTaskTypeType,
        "TaskParameters": List[Dict[str, MaintenanceWindowTaskParameterValueExpressionTypeDef]],
        "Priority": int,
        "MaxConcurrency": str,
        "MaxErrors": str,
        "Status": MaintenanceWindowExecutionStatusType,
        "StatusDetails": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "AlarmConfiguration": AlarmConfigurationTypeDef,
        "TriggeredAlarms": List[AlarmStateInformationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
MaintenanceWindowExecutionTaskIdentityTypeDef = TypedDict(
    "MaintenanceWindowExecutionTaskIdentityTypeDef",
    {
        "WindowExecutionId": NotRequired[str],
        "TaskExecutionId": NotRequired[str],
        "Status": NotRequired[MaintenanceWindowExecutionStatusType],
        "StatusDetails": NotRequired[str],
        "StartTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
        "TaskArn": NotRequired[str],
        "TaskType": NotRequired[MaintenanceWindowTaskTypeType],
        "AlarmConfiguration": NotRequired[AlarmConfigurationTypeDef],
        "TriggeredAlarms": NotRequired[List[AlarmStateInformationTypeDef]],
    },
)
MaintenanceWindowTaskTypeDef = TypedDict(
    "MaintenanceWindowTaskTypeDef",
    {
        "WindowId": NotRequired[str],
        "WindowTaskId": NotRequired[str],
        "TaskArn": NotRequired[str],
        "Type": NotRequired[MaintenanceWindowTaskTypeType],
        "Targets": NotRequired[List[TargetTypeDef]],
        "TaskParameters": NotRequired[
            Dict[str, MaintenanceWindowTaskParameterValueExpressionTypeDef]
        ],
        "Priority": NotRequired[int],
        "LoggingInfo": NotRequired[LoggingInfoTypeDef],
        "ServiceRoleArn": NotRequired[str],
        "MaxConcurrency": NotRequired[str],
        "MaxErrors": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "CutoffBehavior": NotRequired[MaintenanceWindowTaskCutoffBehaviorType],
        "AlarmConfiguration": NotRequired[AlarmConfigurationTypeDef],
    },
)
SendCommandRequestRequestTypeDef = TypedDict(
    "SendCommandRequestRequestTypeDef",
    {
        "DocumentName": str,
        "InstanceIds": NotRequired[Sequence[str]],
        "Targets": NotRequired[Sequence[TargetTypeDef]],
        "DocumentVersion": NotRequired[str],
        "DocumentHash": NotRequired[str],
        "DocumentHashType": NotRequired[DocumentHashTypeType],
        "TimeoutSeconds": NotRequired[int],
        "Comment": NotRequired[str],
        "Parameters": NotRequired[Mapping[str, Sequence[str]]],
        "OutputS3Region": NotRequired[str],
        "OutputS3BucketName": NotRequired[str],
        "OutputS3KeyPrefix": NotRequired[str],
        "MaxConcurrency": NotRequired[str],
        "MaxErrors": NotRequired[str],
        "ServiceRoleArn": NotRequired[str],
        "NotificationConfig": NotRequired[NotificationConfigTypeDef],
        "CloudWatchOutputConfig": NotRequired[CloudWatchOutputConfigTypeDef],
        "AlarmConfiguration": NotRequired[AlarmConfigurationTypeDef],
    },
)
TargetLocationTypeDef = TypedDict(
    "TargetLocationTypeDef",
    {
        "Accounts": NotRequired[Sequence[str]],
        "Regions": NotRequired[Sequence[str]],
        "TargetLocationMaxConcurrency": NotRequired[str],
        "TargetLocationMaxErrors": NotRequired[str],
        "ExecutionRoleName": NotRequired[str],
        "TargetLocationAlarmConfiguration": NotRequired[AlarmConfigurationTypeDef],
    },
)
ListAssociationsResultTypeDef = TypedDict(
    "ListAssociationsResultTypeDef",
    {
        "Associations": List[AssociationTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeMaintenanceWindowTargetsResultTypeDef = TypedDict(
    "DescribeMaintenanceWindowTargetsResultTypeDef",
    {
        "Targets": List[MaintenanceWindowTargetTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeAssociationExecutionTargetsResultTypeDef = TypedDict(
    "DescribeAssociationExecutionTargetsResultTypeDef",
    {
        "AssociationExecutionTargets": List[AssociationExecutionTargetTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAssociationsResultPaginatorTypeDef = TypedDict(
    "ListAssociationsResultPaginatorTypeDef",
    {
        "Associations": List[AssociationPaginatorTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeMaintenanceWindowTargetsResultPaginatorTypeDef = TypedDict(
    "DescribeMaintenanceWindowTargetsResultPaginatorTypeDef",
    {
        "Targets": List[MaintenanceWindowTargetPaginatorTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListCommandInvocationsResultTypeDef = TypedDict(
    "ListCommandInvocationsResultTypeDef",
    {
        "CommandInvocations": List[CommandInvocationTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
MaintenanceWindowTaskInvocationParametersTypeDef = TypedDict(
    "MaintenanceWindowTaskInvocationParametersTypeDef",
    {
        "RunCommand": NotRequired[MaintenanceWindowRunCommandParametersTypeDef],
        "Automation": NotRequired[MaintenanceWindowAutomationParametersTypeDef],
        "StepFunctions": NotRequired[MaintenanceWindowStepFunctionsParametersTypeDef],
        "Lambda": NotRequired[MaintenanceWindowLambdaParametersTypeDef],
    },
)
ListComplianceItemsResultTypeDef = TypedDict(
    "ListComplianceItemsResultTypeDef",
    {
        "ComplianceItems": List[ComplianceItemTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ComplianceSummaryItemTypeDef = TypedDict(
    "ComplianceSummaryItemTypeDef",
    {
        "ComplianceType": NotRequired[str],
        "CompliantSummary": NotRequired[CompliantSummaryTypeDef],
        "NonCompliantSummary": NotRequired[NonCompliantSummaryTypeDef],
    },
)
ResourceComplianceSummaryItemTypeDef = TypedDict(
    "ResourceComplianceSummaryItemTypeDef",
    {
        "ComplianceType": NotRequired[str],
        "ResourceType": NotRequired[str],
        "ResourceId": NotRequired[str],
        "Status": NotRequired[ComplianceStatusType],
        "OverallSeverity": NotRequired[ComplianceSeverityType],
        "ExecutionSummary": NotRequired[ComplianceExecutionSummaryTypeDef],
        "CompliantSummary": NotRequired[CompliantSummaryTypeDef],
        "NonCompliantSummary": NotRequired[NonCompliantSummaryTypeDef],
    },
)
ListDocumentsResultTypeDef = TypedDict(
    "ListDocumentsResultTypeDef",
    {
        "DocumentIdentifiers": List[DocumentIdentifierTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeOpsItemsResponseTypeDef = TypedDict(
    "DescribeOpsItemsResponseTypeDef",
    {
        "NextToken": str,
        "OpsItemSummaries": List[OpsItemSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetOpsItemResponseTypeDef = TypedDict(
    "GetOpsItemResponseTypeDef",
    {
        "OpsItem": OpsItemTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribePatchGroupsResultTypeDef = TypedDict(
    "DescribePatchGroupsResultTypeDef",
    {
        "Mappings": List[PatchGroupPatchBaselineMappingTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDocumentResultTypeDef = TypedDict(
    "CreateDocumentResultTypeDef",
    {
        "DocumentDescription": DocumentDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeDocumentResultTypeDef = TypedDict(
    "DescribeDocumentResultTypeDef",
    {
        "Document": DocumentDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateDocumentResultTypeDef = TypedDict(
    "UpdateDocumentResultTypeDef",
    {
        "DocumentDescription": DocumentDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DocumentMetadataResponseInfoTypeDef = TypedDict(
    "DocumentMetadataResponseInfoTypeDef",
    {
        "ReviewerResponse": NotRequired[List[DocumentReviewerResponseSourceTypeDef]],
    },
)
UpdateDocumentMetadataRequestRequestTypeDef = TypedDict(
    "UpdateDocumentMetadataRequestRequestTypeDef",
    {
        "Name": str,
        "DocumentReviews": DocumentReviewsTypeDef,
        "DocumentVersion": NotRequired[str],
    },
)
DescribeEffectivePatchesForPatchBaselineResultTypeDef = TypedDict(
    "DescribeEffectivePatchesForPatchBaselineResultTypeDef",
    {
        "EffectivePatches": List[EffectivePatchTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
InventoryAggregatorTypeDef = TypedDict(
    "InventoryAggregatorTypeDef",
    {
        "Expression": NotRequired[str],
        "Aggregators": NotRequired[Sequence[Dict[str, Any]]],
        "Groups": NotRequired[Sequence[InventoryGroupTypeDef]],
    },
)
GetOpsSummaryRequestGetOpsSummaryPaginateTypeDef = TypedDict(
    "GetOpsSummaryRequestGetOpsSummaryPaginateTypeDef",
    {
        "SyncName": NotRequired[str],
        "Filters": NotRequired[Sequence[OpsFilterTypeDef]],
        "Aggregators": NotRequired[Sequence[OpsAggregatorTypeDef]],
        "ResultAttributes": NotRequired[Sequence[OpsResultAttributeTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeInstanceInformationResultTypeDef = TypedDict(
    "DescribeInstanceInformationResultTypeDef",
    {
        "InstanceInformationList": List[InstanceInformationTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
InstanceAssociationStatusInfoTypeDef = TypedDict(
    "InstanceAssociationStatusInfoTypeDef",
    {
        "AssociationId": NotRequired[str],
        "Name": NotRequired[str],
        "DocumentVersion": NotRequired[str],
        "AssociationVersion": NotRequired[str],
        "InstanceId": NotRequired[str],
        "ExecutionDate": NotRequired[datetime],
        "Status": NotRequired[str],
        "DetailedStatus": NotRequired[str],
        "ExecutionSummary": NotRequired[str],
        "ErrorCode": NotRequired[str],
        "OutputUrl": NotRequired[InstanceAssociationOutputUrlTypeDef],
        "AssociationName": NotRequired[str],
    },
)
DeleteInventoryResultTypeDef = TypedDict(
    "DeleteInventoryResultTypeDef",
    {
        "DeletionId": str,
        "TypeName": str,
        "DeletionSummary": InventoryDeletionSummaryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
InventoryDeletionStatusItemTypeDef = TypedDict(
    "InventoryDeletionStatusItemTypeDef",
    {
        "DeletionId": NotRequired[str],
        "TypeName": NotRequired[str],
        "DeletionStartTime": NotRequired[datetime],
        "LastStatus": NotRequired[InventoryDeletionStatusType],
        "LastStatusMessage": NotRequired[str],
        "DeletionSummary": NotRequired[InventoryDeletionSummaryTypeDef],
        "LastStatusUpdateTime": NotRequired[datetime],
    },
)
GetInventorySchemaResultTypeDef = TypedDict(
    "GetInventorySchemaResultTypeDef",
    {
        "Schemas": List[InventoryItemSchemaTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetInventoryResultTypeDef = TypedDict(
    "GetInventoryResultTypeDef",
    {
        "Entities": List[InventoryResultEntityTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetOpsSummaryResultTypeDef = TypedDict(
    "GetOpsSummaryResultTypeDef",
    {
        "Entities": List[OpsEntityTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListOpsItemEventsResponseTypeDef = TypedDict(
    "ListOpsItemEventsResponseTypeDef",
    {
        "NextToken": str,
        "Summaries": List[OpsItemEventSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListOpsItemRelatedItemsResponseTypeDef = TypedDict(
    "ListOpsItemRelatedItemsResponseTypeDef",
    {
        "NextToken": str,
        "Summaries": List[OpsItemRelatedItemSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetParameterHistoryResultTypeDef = TypedDict(
    "GetParameterHistoryResultTypeDef",
    {
        "Parameters": List[ParameterHistoryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeParametersResultTypeDef = TypedDict(
    "DescribeParametersResultTypeDef",
    {
        "Parameters": List[ParameterMetadataTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PatchRuleTypeDef = TypedDict(
    "PatchRuleTypeDef",
    {
        "PatchFilterGroup": PatchFilterGroupTypeDef,
        "ComplianceLevel": NotRequired[PatchComplianceLevelType],
        "ApproveAfterDays": NotRequired[int],
        "ApproveUntilDate": NotRequired[str],
        "EnableNonSecurity": NotRequired[bool],
    },
)
ResourceDataSyncSourceWithStatePaginatorTypeDef = TypedDict(
    "ResourceDataSyncSourceWithStatePaginatorTypeDef",
    {
        "SourceType": NotRequired[str],
        "AwsOrganizationsSource": NotRequired[
            ResourceDataSyncAwsOrganizationsSourcePaginatorTypeDef
        ],
        "SourceRegions": NotRequired[List[str]],
        "IncludeFutureRegions": NotRequired[bool],
        "State": NotRequired[str],
        "EnableAllOpsDataSources": NotRequired[bool],
    },
)
ResourceDataSyncSourceTypeDef = TypedDict(
    "ResourceDataSyncSourceTypeDef",
    {
        "SourceType": str,
        "SourceRegions": Sequence[str],
        "AwsOrganizationsSource": NotRequired[ResourceDataSyncAwsOrganizationsSourceTypeDef],
        "IncludeFutureRegions": NotRequired[bool],
        "EnableAllOpsDataSources": NotRequired[bool],
    },
)
ResourceDataSyncSourceWithStateTypeDef = TypedDict(
    "ResourceDataSyncSourceWithStateTypeDef",
    {
        "SourceType": NotRequired[str],
        "AwsOrganizationsSource": NotRequired[ResourceDataSyncAwsOrganizationsSourceTypeDef],
        "SourceRegions": NotRequired[List[str]],
        "IncludeFutureRegions": NotRequired[bool],
        "State": NotRequired[str],
        "EnableAllOpsDataSources": NotRequired[bool],
    },
)
DescribeSessionsResponseTypeDef = TypedDict(
    "DescribeSessionsResponseTypeDef",
    {
        "Sessions": List[SessionTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeAssociationExecutionsResultPaginatorTypeDef = TypedDict(
    "DescribeAssociationExecutionsResultPaginatorTypeDef",
    {
        "AssociationExecutions": List[AssociationExecutionPaginatorTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListCommandsResultPaginatorTypeDef = TypedDict(
    "ListCommandsResultPaginatorTypeDef",
    {
        "Commands": List[CommandPaginatorTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeMaintenanceWindowExecutionTasksResultPaginatorTypeDef = TypedDict(
    "DescribeMaintenanceWindowExecutionTasksResultPaginatorTypeDef",
    {
        "WindowExecutionTaskIdentities": List[
            MaintenanceWindowExecutionTaskIdentityPaginatorTypeDef
        ],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeMaintenanceWindowTasksResultPaginatorTypeDef = TypedDict(
    "DescribeMaintenanceWindowTasksResultPaginatorTypeDef",
    {
        "Tasks": List[MaintenanceWindowTaskPaginatorTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AssociationVersionInfoPaginatorTypeDef = TypedDict(
    "AssociationVersionInfoPaginatorTypeDef",
    {
        "AssociationId": NotRequired[str],
        "AssociationVersion": NotRequired[str],
        "CreatedDate": NotRequired[datetime],
        "Name": NotRequired[str],
        "DocumentVersion": NotRequired[str],
        "Parameters": NotRequired[Dict[str, List[str]]],
        "Targets": NotRequired[List[TargetPaginatorTypeDef]],
        "ScheduleExpression": NotRequired[str],
        "OutputLocation": NotRequired[InstanceAssociationOutputLocationTypeDef],
        "AssociationName": NotRequired[str],
        "MaxErrors": NotRequired[str],
        "MaxConcurrency": NotRequired[str],
        "ComplianceSeverity": NotRequired[AssociationComplianceSeverityType],
        "SyncCompliance": NotRequired[AssociationSyncComplianceType],
        "ApplyOnlyAtCronInterval": NotRequired[bool],
        "CalendarNames": NotRequired[List[str]],
        "TargetLocations": NotRequired[List[TargetLocationPaginatorTypeDef]],
        "ScheduleOffset": NotRequired[int],
        "Duration": NotRequired[int],
        "TargetMaps": NotRequired[List[Dict[str, List[str]]]],
    },
)
RunbookPaginatorTypeDef = TypedDict(
    "RunbookPaginatorTypeDef",
    {
        "DocumentName": str,
        "DocumentVersion": NotRequired[str],
        "Parameters": NotRequired[Dict[str, List[str]]],
        "TargetParameterName": NotRequired[str],
        "Targets": NotRequired[List[TargetPaginatorTypeDef]],
        "TargetMaps": NotRequired[List[Dict[str, List[str]]]],
        "MaxConcurrency": NotRequired[str],
        "MaxErrors": NotRequired[str],
        "TargetLocations": NotRequired[List[TargetLocationPaginatorTypeDef]],
    },
)
StepExecutionPaginatorTypeDef = TypedDict(
    "StepExecutionPaginatorTypeDef",
    {
        "StepName": NotRequired[str],
        "Action": NotRequired[str],
        "TimeoutSeconds": NotRequired[int],
        "OnFailure": NotRequired[str],
        "MaxAttempts": NotRequired[int],
        "ExecutionStartTime": NotRequired[datetime],
        "ExecutionEndTime": NotRequired[datetime],
        "StepStatus": NotRequired[AutomationExecutionStatusType],
        "ResponseCode": NotRequired[str],
        "Inputs": NotRequired[Dict[str, str]],
        "Outputs": NotRequired[Dict[str, List[str]]],
        "Response": NotRequired[str],
        "FailureMessage": NotRequired[str],
        "FailureDetails": NotRequired[FailureDetailsTypeDef],
        "StepExecutionId": NotRequired[str],
        "OverriddenParameters": NotRequired[Dict[str, List[str]]],
        "IsEnd": NotRequired[bool],
        "NextStep": NotRequired[str],
        "IsCritical": NotRequired[bool],
        "ValidNextSteps": NotRequired[List[str]],
        "Targets": NotRequired[List[TargetPaginatorTypeDef]],
        "TargetLocation": NotRequired[TargetLocationPaginatorTypeDef],
        "TriggeredAlarms": NotRequired[List[AlarmStateInformationTypeDef]],
        "ParentStepDetails": NotRequired[ParentStepDetailsTypeDef],
    },
)
DescribeAssociationExecutionsResultTypeDef = TypedDict(
    "DescribeAssociationExecutionsResultTypeDef",
    {
        "AssociationExecutions": List[AssociationExecutionTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListCommandsResultTypeDef = TypedDict(
    "ListCommandsResultTypeDef",
    {
        "Commands": List[CommandTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SendCommandResultTypeDef = TypedDict(
    "SendCommandResultTypeDef",
    {
        "Command": CommandTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeMaintenanceWindowExecutionTasksResultTypeDef = TypedDict(
    "DescribeMaintenanceWindowExecutionTasksResultTypeDef",
    {
        "WindowExecutionTaskIdentities": List[MaintenanceWindowExecutionTaskIdentityTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeMaintenanceWindowTasksResultTypeDef = TypedDict(
    "DescribeMaintenanceWindowTasksResultTypeDef",
    {
        "Tasks": List[MaintenanceWindowTaskTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AssociationDescriptionTypeDef = TypedDict(
    "AssociationDescriptionTypeDef",
    {
        "Name": NotRequired[str],
        "InstanceId": NotRequired[str],
        "AssociationVersion": NotRequired[str],
        "Date": NotRequired[datetime],
        "LastUpdateAssociationDate": NotRequired[datetime],
        "Status": NotRequired[AssociationStatusTypeDef],
        "Overview": NotRequired[AssociationOverviewTypeDef],
        "DocumentVersion": NotRequired[str],
        "AutomationTargetParameterName": NotRequired[str],
        "Parameters": NotRequired[Dict[str, List[str]]],
        "AssociationId": NotRequired[str],
        "Targets": NotRequired[List[TargetTypeDef]],
        "ScheduleExpression": NotRequired[str],
        "OutputLocation": NotRequired[InstanceAssociationOutputLocationTypeDef],
        "LastExecutionDate": NotRequired[datetime],
        "LastSuccessfulExecutionDate": NotRequired[datetime],
        "AssociationName": NotRequired[str],
        "MaxErrors": NotRequired[str],
        "MaxConcurrency": NotRequired[str],
        "ComplianceSeverity": NotRequired[AssociationComplianceSeverityType],
        "SyncCompliance": NotRequired[AssociationSyncComplianceType],
        "ApplyOnlyAtCronInterval": NotRequired[bool],
        "CalendarNames": NotRequired[List[str]],
        "TargetLocations": NotRequired[List[TargetLocationTypeDef]],
        "ScheduleOffset": NotRequired[int],
        "Duration": NotRequired[int],
        "TargetMaps": NotRequired[List[Dict[str, List[str]]]],
        "AlarmConfiguration": NotRequired[AlarmConfigurationTypeDef],
        "TriggeredAlarms": NotRequired[List[AlarmStateInformationTypeDef]],
    },
)
AssociationVersionInfoTypeDef = TypedDict(
    "AssociationVersionInfoTypeDef",
    {
        "AssociationId": NotRequired[str],
        "AssociationVersion": NotRequired[str],
        "CreatedDate": NotRequired[datetime],
        "Name": NotRequired[str],
        "DocumentVersion": NotRequired[str],
        "Parameters": NotRequired[Dict[str, List[str]]],
        "Targets": NotRequired[List[TargetTypeDef]],
        "ScheduleExpression": NotRequired[str],
        "OutputLocation": NotRequired[InstanceAssociationOutputLocationTypeDef],
        "AssociationName": NotRequired[str],
        "MaxErrors": NotRequired[str],
        "MaxConcurrency": NotRequired[str],
        "ComplianceSeverity": NotRequired[AssociationComplianceSeverityType],
        "SyncCompliance": NotRequired[AssociationSyncComplianceType],
        "ApplyOnlyAtCronInterval": NotRequired[bool],
        "CalendarNames": NotRequired[List[str]],
        "TargetLocations": NotRequired[List[TargetLocationTypeDef]],
        "ScheduleOffset": NotRequired[int],
        "Duration": NotRequired[int],
        "TargetMaps": NotRequired[List[Dict[str, List[str]]]],
    },
)
CreateAssociationBatchRequestEntryTypeDef = TypedDict(
    "CreateAssociationBatchRequestEntryTypeDef",
    {
        "Name": str,
        "InstanceId": NotRequired[str],
        "Parameters": NotRequired[Mapping[str, Sequence[str]]],
        "AutomationTargetParameterName": NotRequired[str],
        "DocumentVersion": NotRequired[str],
        "Targets": NotRequired[Sequence[TargetTypeDef]],
        "ScheduleExpression": NotRequired[str],
        "OutputLocation": NotRequired[InstanceAssociationOutputLocationTypeDef],
        "AssociationName": NotRequired[str],
        "MaxErrors": NotRequired[str],
        "MaxConcurrency": NotRequired[str],
        "ComplianceSeverity": NotRequired[AssociationComplianceSeverityType],
        "SyncCompliance": NotRequired[AssociationSyncComplianceType],
        "ApplyOnlyAtCronInterval": NotRequired[bool],
        "CalendarNames": NotRequired[Sequence[str]],
        "TargetLocations": NotRequired[Sequence[TargetLocationTypeDef]],
        "ScheduleOffset": NotRequired[int],
        "Duration": NotRequired[int],
        "TargetMaps": NotRequired[Sequence[Mapping[str, Sequence[str]]]],
        "AlarmConfiguration": NotRequired[AlarmConfigurationTypeDef],
    },
)
CreateAssociationRequestRequestTypeDef = TypedDict(
    "CreateAssociationRequestRequestTypeDef",
    {
        "Name": str,
        "DocumentVersion": NotRequired[str],
        "InstanceId": NotRequired[str],
        "Parameters": NotRequired[Mapping[str, Sequence[str]]],
        "Targets": NotRequired[Sequence[TargetTypeDef]],
        "ScheduleExpression": NotRequired[str],
        "OutputLocation": NotRequired[InstanceAssociationOutputLocationTypeDef],
        "AssociationName": NotRequired[str],
        "AutomationTargetParameterName": NotRequired[str],
        "MaxErrors": NotRequired[str],
        "MaxConcurrency": NotRequired[str],
        "ComplianceSeverity": NotRequired[AssociationComplianceSeverityType],
        "SyncCompliance": NotRequired[AssociationSyncComplianceType],
        "ApplyOnlyAtCronInterval": NotRequired[bool],
        "CalendarNames": NotRequired[Sequence[str]],
        "TargetLocations": NotRequired[Sequence[TargetLocationTypeDef]],
        "ScheduleOffset": NotRequired[int],
        "Duration": NotRequired[int],
        "TargetMaps": NotRequired[Sequence[Mapping[str, Sequence[str]]]],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "AlarmConfiguration": NotRequired[AlarmConfigurationTypeDef],
    },
)
RunbookTypeDef = TypedDict(
    "RunbookTypeDef",
    {
        "DocumentName": str,
        "DocumentVersion": NotRequired[str],
        "Parameters": NotRequired[Dict[str, List[str]]],
        "TargetParameterName": NotRequired[str],
        "Targets": NotRequired[List[TargetTypeDef]],
        "TargetMaps": NotRequired[List[Dict[str, List[str]]]],
        "MaxConcurrency": NotRequired[str],
        "MaxErrors": NotRequired[str],
        "TargetLocations": NotRequired[List[TargetLocationTypeDef]],
    },
)
StartAutomationExecutionRequestRequestTypeDef = TypedDict(
    "StartAutomationExecutionRequestRequestTypeDef",
    {
        "DocumentName": str,
        "DocumentVersion": NotRequired[str],
        "Parameters": NotRequired[Mapping[str, Sequence[str]]],
        "ClientToken": NotRequired[str],
        "Mode": NotRequired[ExecutionModeType],
        "TargetParameterName": NotRequired[str],
        "Targets": NotRequired[Sequence[TargetTypeDef]],
        "TargetMaps": NotRequired[Sequence[Mapping[str, Sequence[str]]]],
        "MaxConcurrency": NotRequired[str],
        "MaxErrors": NotRequired[str],
        "TargetLocations": NotRequired[Sequence[TargetLocationTypeDef]],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "AlarmConfiguration": NotRequired[AlarmConfigurationTypeDef],
    },
)
StepExecutionTypeDef = TypedDict(
    "StepExecutionTypeDef",
    {
        "StepName": NotRequired[str],
        "Action": NotRequired[str],
        "TimeoutSeconds": NotRequired[int],
        "OnFailure": NotRequired[str],
        "MaxAttempts": NotRequired[int],
        "ExecutionStartTime": NotRequired[datetime],
        "ExecutionEndTime": NotRequired[datetime],
        "StepStatus": NotRequired[AutomationExecutionStatusType],
        "ResponseCode": NotRequired[str],
        "Inputs": NotRequired[Dict[str, str]],
        "Outputs": NotRequired[Dict[str, List[str]]],
        "Response": NotRequired[str],
        "FailureMessage": NotRequired[str],
        "FailureDetails": NotRequired[FailureDetailsTypeDef],
        "StepExecutionId": NotRequired[str],
        "OverriddenParameters": NotRequired[Dict[str, List[str]]],
        "IsEnd": NotRequired[bool],
        "NextStep": NotRequired[str],
        "IsCritical": NotRequired[bool],
        "ValidNextSteps": NotRequired[List[str]],
        "Targets": NotRequired[List[TargetTypeDef]],
        "TargetLocation": NotRequired[TargetLocationTypeDef],
        "TriggeredAlarms": NotRequired[List[AlarmStateInformationTypeDef]],
        "ParentStepDetails": NotRequired[ParentStepDetailsTypeDef],
    },
)
UpdateAssociationRequestRequestTypeDef = TypedDict(
    "UpdateAssociationRequestRequestTypeDef",
    {
        "AssociationId": str,
        "Parameters": NotRequired[Mapping[str, Sequence[str]]],
        "DocumentVersion": NotRequired[str],
        "ScheduleExpression": NotRequired[str],
        "OutputLocation": NotRequired[InstanceAssociationOutputLocationTypeDef],
        "Name": NotRequired[str],
        "Targets": NotRequired[Sequence[TargetTypeDef]],
        "AssociationName": NotRequired[str],
        "AssociationVersion": NotRequired[str],
        "AutomationTargetParameterName": NotRequired[str],
        "MaxErrors": NotRequired[str],
        "MaxConcurrency": NotRequired[str],
        "ComplianceSeverity": NotRequired[AssociationComplianceSeverityType],
        "SyncCompliance": NotRequired[AssociationSyncComplianceType],
        "ApplyOnlyAtCronInterval": NotRequired[bool],
        "CalendarNames": NotRequired[Sequence[str]],
        "TargetLocations": NotRequired[Sequence[TargetLocationTypeDef]],
        "ScheduleOffset": NotRequired[int],
        "Duration": NotRequired[int],
        "TargetMaps": NotRequired[Sequence[Mapping[str, Sequence[str]]]],
        "AlarmConfiguration": NotRequired[AlarmConfigurationTypeDef],
    },
)
GetMaintenanceWindowTaskResultTypeDef = TypedDict(
    "GetMaintenanceWindowTaskResultTypeDef",
    {
        "WindowId": str,
        "WindowTaskId": str,
        "Targets": List[TargetTypeDef],
        "TaskArn": str,
        "ServiceRoleArn": str,
        "TaskType": MaintenanceWindowTaskTypeType,
        "TaskParameters": Dict[str, MaintenanceWindowTaskParameterValueExpressionTypeDef],
        "TaskInvocationParameters": MaintenanceWindowTaskInvocationParametersTypeDef,
        "Priority": int,
        "MaxConcurrency": str,
        "MaxErrors": str,
        "LoggingInfo": LoggingInfoTypeDef,
        "Name": str,
        "Description": str,
        "CutoffBehavior": MaintenanceWindowTaskCutoffBehaviorType,
        "AlarmConfiguration": AlarmConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RegisterTaskWithMaintenanceWindowRequestRequestTypeDef = TypedDict(
    "RegisterTaskWithMaintenanceWindowRequestRequestTypeDef",
    {
        "WindowId": str,
        "TaskArn": str,
        "TaskType": MaintenanceWindowTaskTypeType,
        "Targets": NotRequired[Sequence[TargetTypeDef]],
        "ServiceRoleArn": NotRequired[str],
        "TaskParameters": NotRequired[
            Mapping[str, MaintenanceWindowTaskParameterValueExpressionTypeDef]
        ],
        "TaskInvocationParameters": NotRequired[MaintenanceWindowTaskInvocationParametersTypeDef],
        "Priority": NotRequired[int],
        "MaxConcurrency": NotRequired[str],
        "MaxErrors": NotRequired[str],
        "LoggingInfo": NotRequired[LoggingInfoTypeDef],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "ClientToken": NotRequired[str],
        "CutoffBehavior": NotRequired[MaintenanceWindowTaskCutoffBehaviorType],
        "AlarmConfiguration": NotRequired[AlarmConfigurationTypeDef],
    },
)
UpdateMaintenanceWindowTaskRequestRequestTypeDef = TypedDict(
    "UpdateMaintenanceWindowTaskRequestRequestTypeDef",
    {
        "WindowId": str,
        "WindowTaskId": str,
        "Targets": NotRequired[Sequence[TargetTypeDef]],
        "TaskArn": NotRequired[str],
        "ServiceRoleArn": NotRequired[str],
        "TaskParameters": NotRequired[
            Mapping[str, MaintenanceWindowTaskParameterValueExpressionTypeDef]
        ],
        "TaskInvocationParameters": NotRequired[MaintenanceWindowTaskInvocationParametersTypeDef],
        "Priority": NotRequired[int],
        "MaxConcurrency": NotRequired[str],
        "MaxErrors": NotRequired[str],
        "LoggingInfo": NotRequired[LoggingInfoTypeDef],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "Replace": NotRequired[bool],
        "CutoffBehavior": NotRequired[MaintenanceWindowTaskCutoffBehaviorType],
        "AlarmConfiguration": NotRequired[AlarmConfigurationTypeDef],
    },
)
UpdateMaintenanceWindowTaskResultTypeDef = TypedDict(
    "UpdateMaintenanceWindowTaskResultTypeDef",
    {
        "WindowId": str,
        "WindowTaskId": str,
        "Targets": List[TargetTypeDef],
        "TaskArn": str,
        "ServiceRoleArn": str,
        "TaskParameters": Dict[str, MaintenanceWindowTaskParameterValueExpressionTypeDef],
        "TaskInvocationParameters": MaintenanceWindowTaskInvocationParametersTypeDef,
        "Priority": int,
        "MaxConcurrency": str,
        "MaxErrors": str,
        "LoggingInfo": LoggingInfoTypeDef,
        "Name": str,
        "Description": str,
        "CutoffBehavior": MaintenanceWindowTaskCutoffBehaviorType,
        "AlarmConfiguration": AlarmConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListComplianceSummariesResultTypeDef = TypedDict(
    "ListComplianceSummariesResultTypeDef",
    {
        "ComplianceSummaryItems": List[ComplianceSummaryItemTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListResourceComplianceSummariesResultTypeDef = TypedDict(
    "ListResourceComplianceSummariesResultTypeDef",
    {
        "ResourceComplianceSummaryItems": List[ResourceComplianceSummaryItemTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListDocumentMetadataHistoryResponseTypeDef = TypedDict(
    "ListDocumentMetadataHistoryResponseTypeDef",
    {
        "Name": str,
        "DocumentVersion": str,
        "Author": str,
        "Metadata": DocumentMetadataResponseInfoTypeDef,
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetInventoryRequestGetInventoryPaginateTypeDef = TypedDict(
    "GetInventoryRequestGetInventoryPaginateTypeDef",
    {
        "Filters": NotRequired[Sequence[InventoryFilterTypeDef]],
        "Aggregators": NotRequired[Sequence[InventoryAggregatorTypeDef]],
        "ResultAttributes": NotRequired[Sequence[ResultAttributeTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeInstanceAssociationsStatusResultTypeDef = TypedDict(
    "DescribeInstanceAssociationsStatusResultTypeDef",
    {
        "InstanceAssociationStatusInfos": List[InstanceAssociationStatusInfoTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeInventoryDeletionsResultTypeDef = TypedDict(
    "DescribeInventoryDeletionsResultTypeDef",
    {
        "InventoryDeletions": List[InventoryDeletionStatusItemTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PatchRuleGroupTypeDef = TypedDict(
    "PatchRuleGroupTypeDef",
    {
        "PatchRules": Sequence[PatchRuleTypeDef],
    },
)
ResourceDataSyncItemPaginatorTypeDef = TypedDict(
    "ResourceDataSyncItemPaginatorTypeDef",
    {
        "SyncName": NotRequired[str],
        "SyncType": NotRequired[str],
        "SyncSource": NotRequired[ResourceDataSyncSourceWithStatePaginatorTypeDef],
        "S3Destination": NotRequired[ResourceDataSyncS3DestinationTypeDef],
        "LastSyncTime": NotRequired[datetime],
        "LastSuccessfulSyncTime": NotRequired[datetime],
        "SyncLastModifiedTime": NotRequired[datetime],
        "LastStatus": NotRequired[LastResourceDataSyncStatusType],
        "SyncCreatedTime": NotRequired[datetime],
        "LastSyncStatusMessage": NotRequired[str],
    },
)
CreateResourceDataSyncRequestRequestTypeDef = TypedDict(
    "CreateResourceDataSyncRequestRequestTypeDef",
    {
        "SyncName": str,
        "S3Destination": NotRequired[ResourceDataSyncS3DestinationTypeDef],
        "SyncType": NotRequired[str],
        "SyncSource": NotRequired[ResourceDataSyncSourceTypeDef],
    },
)
UpdateResourceDataSyncRequestRequestTypeDef = TypedDict(
    "UpdateResourceDataSyncRequestRequestTypeDef",
    {
        "SyncName": str,
        "SyncType": str,
        "SyncSource": ResourceDataSyncSourceTypeDef,
    },
)
ResourceDataSyncItemTypeDef = TypedDict(
    "ResourceDataSyncItemTypeDef",
    {
        "SyncName": NotRequired[str],
        "SyncType": NotRequired[str],
        "SyncSource": NotRequired[ResourceDataSyncSourceWithStateTypeDef],
        "S3Destination": NotRequired[ResourceDataSyncS3DestinationTypeDef],
        "LastSyncTime": NotRequired[datetime],
        "LastSuccessfulSyncTime": NotRequired[datetime],
        "SyncLastModifiedTime": NotRequired[datetime],
        "LastStatus": NotRequired[LastResourceDataSyncStatusType],
        "SyncCreatedTime": NotRequired[datetime],
        "LastSyncStatusMessage": NotRequired[str],
    },
)
ListAssociationVersionsResultPaginatorTypeDef = TypedDict(
    "ListAssociationVersionsResultPaginatorTypeDef",
    {
        "AssociationVersions": List[AssociationVersionInfoPaginatorTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AutomationExecutionMetadataPaginatorTypeDef = TypedDict(
    "AutomationExecutionMetadataPaginatorTypeDef",
    {
        "AutomationExecutionId": NotRequired[str],
        "DocumentName": NotRequired[str],
        "DocumentVersion": NotRequired[str],
        "AutomationExecutionStatus": NotRequired[AutomationExecutionStatusType],
        "ExecutionStartTime": NotRequired[datetime],
        "ExecutionEndTime": NotRequired[datetime],
        "ExecutedBy": NotRequired[str],
        "LogFile": NotRequired[str],
        "Outputs": NotRequired[Dict[str, List[str]]],
        "Mode": NotRequired[ExecutionModeType],
        "ParentAutomationExecutionId": NotRequired[str],
        "CurrentStepName": NotRequired[str],
        "CurrentAction": NotRequired[str],
        "FailureMessage": NotRequired[str],
        "TargetParameterName": NotRequired[str],
        "Targets": NotRequired[List[TargetPaginatorTypeDef]],
        "TargetMaps": NotRequired[List[Dict[str, List[str]]]],
        "ResolvedTargets": NotRequired[ResolvedTargetsTypeDef],
        "MaxConcurrency": NotRequired[str],
        "MaxErrors": NotRequired[str],
        "Target": NotRequired[str],
        "AutomationType": NotRequired[AutomationTypeType],
        "AlarmConfiguration": NotRequired[AlarmConfigurationPaginatorTypeDef],
        "TriggeredAlarms": NotRequired[List[AlarmStateInformationTypeDef]],
        "AutomationSubtype": NotRequired[Literal["ChangeRequest"]],
        "ScheduledTime": NotRequired[datetime],
        "Runbooks": NotRequired[List[RunbookPaginatorTypeDef]],
        "OpsItemId": NotRequired[str],
        "AssociationId": NotRequired[str],
        "ChangeRequestName": NotRequired[str],
    },
)
DescribeAutomationStepExecutionsResultPaginatorTypeDef = TypedDict(
    "DescribeAutomationStepExecutionsResultPaginatorTypeDef",
    {
        "StepExecutions": List[StepExecutionPaginatorTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateAssociationResultTypeDef = TypedDict(
    "CreateAssociationResultTypeDef",
    {
        "AssociationDescription": AssociationDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeAssociationResultTypeDef = TypedDict(
    "DescribeAssociationResultTypeDef",
    {
        "AssociationDescription": AssociationDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateAssociationResultTypeDef = TypedDict(
    "UpdateAssociationResultTypeDef",
    {
        "AssociationDescription": AssociationDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateAssociationStatusResultTypeDef = TypedDict(
    "UpdateAssociationStatusResultTypeDef",
    {
        "AssociationDescription": AssociationDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAssociationVersionsResultTypeDef = TypedDict(
    "ListAssociationVersionsResultTypeDef",
    {
        "AssociationVersions": List[AssociationVersionInfoTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateAssociationBatchRequestRequestTypeDef = TypedDict(
    "CreateAssociationBatchRequestRequestTypeDef",
    {
        "Entries": Sequence[CreateAssociationBatchRequestEntryTypeDef],
    },
)
FailedCreateAssociationTypeDef = TypedDict(
    "FailedCreateAssociationTypeDef",
    {
        "Entry": NotRequired[CreateAssociationBatchRequestEntryTypeDef],
        "Message": NotRequired[str],
        "Fault": NotRequired[FaultType],
    },
)
AutomationExecutionMetadataTypeDef = TypedDict(
    "AutomationExecutionMetadataTypeDef",
    {
        "AutomationExecutionId": NotRequired[str],
        "DocumentName": NotRequired[str],
        "DocumentVersion": NotRequired[str],
        "AutomationExecutionStatus": NotRequired[AutomationExecutionStatusType],
        "ExecutionStartTime": NotRequired[datetime],
        "ExecutionEndTime": NotRequired[datetime],
        "ExecutedBy": NotRequired[str],
        "LogFile": NotRequired[str],
        "Outputs": NotRequired[Dict[str, List[str]]],
        "Mode": NotRequired[ExecutionModeType],
        "ParentAutomationExecutionId": NotRequired[str],
        "CurrentStepName": NotRequired[str],
        "CurrentAction": NotRequired[str],
        "FailureMessage": NotRequired[str],
        "TargetParameterName": NotRequired[str],
        "Targets": NotRequired[List[TargetTypeDef]],
        "TargetMaps": NotRequired[List[Dict[str, List[str]]]],
        "ResolvedTargets": NotRequired[ResolvedTargetsTypeDef],
        "MaxConcurrency": NotRequired[str],
        "MaxErrors": NotRequired[str],
        "Target": NotRequired[str],
        "AutomationType": NotRequired[AutomationTypeType],
        "AlarmConfiguration": NotRequired[AlarmConfigurationTypeDef],
        "TriggeredAlarms": NotRequired[List[AlarmStateInformationTypeDef]],
        "AutomationSubtype": NotRequired[Literal["ChangeRequest"]],
        "ScheduledTime": NotRequired[datetime],
        "Runbooks": NotRequired[List[RunbookTypeDef]],
        "OpsItemId": NotRequired[str],
        "AssociationId": NotRequired[str],
        "ChangeRequestName": NotRequired[str],
    },
)
StartChangeRequestExecutionRequestRequestTypeDef = TypedDict(
    "StartChangeRequestExecutionRequestRequestTypeDef",
    {
        "DocumentName": str,
        "Runbooks": Sequence[RunbookTypeDef],
        "ScheduledTime": NotRequired[TimestampTypeDef],
        "DocumentVersion": NotRequired[str],
        "Parameters": NotRequired[Mapping[str, Sequence[str]]],
        "ChangeRequestName": NotRequired[str],
        "ClientToken": NotRequired[str],
        "AutoApprove": NotRequired[bool],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "ScheduledEndTime": NotRequired[TimestampTypeDef],
        "ChangeDetails": NotRequired[str],
    },
)
AutomationExecutionTypeDef = TypedDict(
    "AutomationExecutionTypeDef",
    {
        "AutomationExecutionId": NotRequired[str],
        "DocumentName": NotRequired[str],
        "DocumentVersion": NotRequired[str],
        "ExecutionStartTime": NotRequired[datetime],
        "ExecutionEndTime": NotRequired[datetime],
        "AutomationExecutionStatus": NotRequired[AutomationExecutionStatusType],
        "StepExecutions": NotRequired[List[StepExecutionTypeDef]],
        "StepExecutionsTruncated": NotRequired[bool],
        "Parameters": NotRequired[Dict[str, List[str]]],
        "Outputs": NotRequired[Dict[str, List[str]]],
        "FailureMessage": NotRequired[str],
        "Mode": NotRequired[ExecutionModeType],
        "ParentAutomationExecutionId": NotRequired[str],
        "ExecutedBy": NotRequired[str],
        "CurrentStepName": NotRequired[str],
        "CurrentAction": NotRequired[str],
        "TargetParameterName": NotRequired[str],
        "Targets": NotRequired[List[TargetTypeDef]],
        "TargetMaps": NotRequired[List[Dict[str, List[str]]]],
        "ResolvedTargets": NotRequired[ResolvedTargetsTypeDef],
        "MaxConcurrency": NotRequired[str],
        "MaxErrors": NotRequired[str],
        "Target": NotRequired[str],
        "TargetLocations": NotRequired[List[TargetLocationTypeDef]],
        "ProgressCounters": NotRequired[ProgressCountersTypeDef],
        "AlarmConfiguration": NotRequired[AlarmConfigurationTypeDef],
        "TriggeredAlarms": NotRequired[List[AlarmStateInformationTypeDef]],
        "AutomationSubtype": NotRequired[Literal["ChangeRequest"]],
        "ScheduledTime": NotRequired[datetime],
        "Runbooks": NotRequired[List[RunbookTypeDef]],
        "OpsItemId": NotRequired[str],
        "AssociationId": NotRequired[str],
        "ChangeRequestName": NotRequired[str],
        "Variables": NotRequired[Dict[str, List[str]]],
    },
)
DescribeAutomationStepExecutionsResultTypeDef = TypedDict(
    "DescribeAutomationStepExecutionsResultTypeDef",
    {
        "StepExecutions": List[StepExecutionTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BaselineOverrideTypeDef = TypedDict(
    "BaselineOverrideTypeDef",
    {
        "OperatingSystem": NotRequired[OperatingSystemType],
        "GlobalFilters": NotRequired[PatchFilterGroupTypeDef],
        "ApprovalRules": NotRequired[PatchRuleGroupTypeDef],
        "ApprovedPatches": NotRequired[Sequence[str]],
        "ApprovedPatchesComplianceLevel": NotRequired[PatchComplianceLevelType],
        "RejectedPatches": NotRequired[Sequence[str]],
        "RejectedPatchesAction": NotRequired[PatchActionType],
        "ApprovedPatchesEnableNonSecurity": NotRequired[bool],
        "Sources": NotRequired[Sequence[PatchSourceTypeDef]],
    },
)
CreatePatchBaselineRequestRequestTypeDef = TypedDict(
    "CreatePatchBaselineRequestRequestTypeDef",
    {
        "Name": str,
        "OperatingSystem": NotRequired[OperatingSystemType],
        "GlobalFilters": NotRequired[PatchFilterGroupTypeDef],
        "ApprovalRules": NotRequired[PatchRuleGroupTypeDef],
        "ApprovedPatches": NotRequired[Sequence[str]],
        "ApprovedPatchesComplianceLevel": NotRequired[PatchComplianceLevelType],
        "ApprovedPatchesEnableNonSecurity": NotRequired[bool],
        "RejectedPatches": NotRequired[Sequence[str]],
        "RejectedPatchesAction": NotRequired[PatchActionType],
        "Description": NotRequired[str],
        "Sources": NotRequired[Sequence[PatchSourceTypeDef]],
        "ClientToken": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
GetPatchBaselineResultTypeDef = TypedDict(
    "GetPatchBaselineResultTypeDef",
    {
        "BaselineId": str,
        "Name": str,
        "OperatingSystem": OperatingSystemType,
        "GlobalFilters": PatchFilterGroupTypeDef,
        "ApprovalRules": PatchRuleGroupTypeDef,
        "ApprovedPatches": List[str],
        "ApprovedPatchesComplianceLevel": PatchComplianceLevelType,
        "ApprovedPatchesEnableNonSecurity": bool,
        "RejectedPatches": List[str],
        "RejectedPatchesAction": PatchActionType,
        "PatchGroups": List[str],
        "CreatedDate": datetime,
        "ModifiedDate": datetime,
        "Description": str,
        "Sources": List[PatchSourceTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdatePatchBaselineRequestRequestTypeDef = TypedDict(
    "UpdatePatchBaselineRequestRequestTypeDef",
    {
        "BaselineId": str,
        "Name": NotRequired[str],
        "GlobalFilters": NotRequired[PatchFilterGroupTypeDef],
        "ApprovalRules": NotRequired[PatchRuleGroupTypeDef],
        "ApprovedPatches": NotRequired[Sequence[str]],
        "ApprovedPatchesComplianceLevel": NotRequired[PatchComplianceLevelType],
        "ApprovedPatchesEnableNonSecurity": NotRequired[bool],
        "RejectedPatches": NotRequired[Sequence[str]],
        "RejectedPatchesAction": NotRequired[PatchActionType],
        "Description": NotRequired[str],
        "Sources": NotRequired[Sequence[PatchSourceTypeDef]],
        "Replace": NotRequired[bool],
    },
)
UpdatePatchBaselineResultTypeDef = TypedDict(
    "UpdatePatchBaselineResultTypeDef",
    {
        "BaselineId": str,
        "Name": str,
        "OperatingSystem": OperatingSystemType,
        "GlobalFilters": PatchFilterGroupTypeDef,
        "ApprovalRules": PatchRuleGroupTypeDef,
        "ApprovedPatches": List[str],
        "ApprovedPatchesComplianceLevel": PatchComplianceLevelType,
        "ApprovedPatchesEnableNonSecurity": bool,
        "RejectedPatches": List[str],
        "RejectedPatchesAction": PatchActionType,
        "CreatedDate": datetime,
        "ModifiedDate": datetime,
        "Description": str,
        "Sources": List[PatchSourceTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListResourceDataSyncResultPaginatorTypeDef = TypedDict(
    "ListResourceDataSyncResultPaginatorTypeDef",
    {
        "ResourceDataSyncItems": List[ResourceDataSyncItemPaginatorTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListResourceDataSyncResultTypeDef = TypedDict(
    "ListResourceDataSyncResultTypeDef",
    {
        "ResourceDataSyncItems": List[ResourceDataSyncItemTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeAutomationExecutionsResultPaginatorTypeDef = TypedDict(
    "DescribeAutomationExecutionsResultPaginatorTypeDef",
    {
        "AutomationExecutionMetadataList": List[AutomationExecutionMetadataPaginatorTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateAssociationBatchResultTypeDef = TypedDict(
    "CreateAssociationBatchResultTypeDef",
    {
        "Successful": List[AssociationDescriptionTypeDef],
        "Failed": List[FailedCreateAssociationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeAutomationExecutionsResultTypeDef = TypedDict(
    "DescribeAutomationExecutionsResultTypeDef",
    {
        "AutomationExecutionMetadataList": List[AutomationExecutionMetadataTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAutomationExecutionResultTypeDef = TypedDict(
    "GetAutomationExecutionResultTypeDef",
    {
        "AutomationExecution": AutomationExecutionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetDeployablePatchSnapshotForInstanceRequestRequestTypeDef = TypedDict(
    "GetDeployablePatchSnapshotForInstanceRequestRequestTypeDef",
    {
        "InstanceId": str,
        "SnapshotId": str,
        "BaselineOverride": NotRequired[BaselineOverrideTypeDef],
    },
)
