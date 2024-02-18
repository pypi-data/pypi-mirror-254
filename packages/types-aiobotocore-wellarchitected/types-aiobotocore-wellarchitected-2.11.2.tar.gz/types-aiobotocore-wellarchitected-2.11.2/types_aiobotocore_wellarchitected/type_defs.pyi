"""
Type annotations for wellarchitected service type definitions.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_wellarchitected/type_defs/)

Usage::

    ```python
    from types_aiobotocore_wellarchitected.type_defs import ChoiceContentTypeDef

    data: ChoiceContentTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from .literals import (
    AdditionalResourceTypeType,
    AnswerReasonType,
    CheckFailureReasonType,
    CheckStatusType,
    ChoiceReasonType,
    ChoiceStatusType,
    DefinitionTypeType,
    DifferenceStatusType,
    DiscoveryIntegrationStatusType,
    ImportLensStatusType,
    LensStatusType,
    LensStatusTypeType,
    LensTypeType,
    NotificationTypeType,
    OrganizationSharingStatusType,
    PermissionTypeType,
    ProfileNotificationTypeType,
    ProfileOwnerTypeType,
    QuestionPriorityType,
    QuestionType,
    QuestionTypeType,
    ReportFormatType,
    ReviewTemplateAnswerStatusType,
    ReviewTemplateUpdateStatusType,
    RiskType,
    ShareInvitationActionType,
    ShareResourceTypeType,
    ShareStatusType,
    TrustedAdvisorIntegrationStatusType,
    WorkloadEnvironmentType,
    WorkloadImprovementStatusType,
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
    "ChoiceContentTypeDef",
    "ChoiceAnswerSummaryTypeDef",
    "ChoiceAnswerTypeDef",
    "AssociateLensesInputRequestTypeDef",
    "AssociateProfilesInputRequestTypeDef",
    "BestPracticeTypeDef",
    "CheckDetailTypeDef",
    "CheckSummaryTypeDef",
    "ChoiceImprovementPlanTypeDef",
    "ChoiceUpdateTypeDef",
    "CreateLensShareInputRequestTypeDef",
    "ResponseMetadataTypeDef",
    "CreateLensVersionInputRequestTypeDef",
    "CreateMilestoneInputRequestTypeDef",
    "ProfileQuestionUpdateTypeDef",
    "CreateProfileShareInputRequestTypeDef",
    "CreateReviewTemplateInputRequestTypeDef",
    "CreateTemplateShareInputRequestTypeDef",
    "WorkloadDiscoveryConfigTypeDef",
    "CreateWorkloadShareInputRequestTypeDef",
    "DeleteLensInputRequestTypeDef",
    "DeleteLensShareInputRequestTypeDef",
    "DeleteProfileInputRequestTypeDef",
    "DeleteProfileShareInputRequestTypeDef",
    "DeleteReviewTemplateInputRequestTypeDef",
    "DeleteTemplateShareInputRequestTypeDef",
    "DeleteWorkloadInputRequestTypeDef",
    "DeleteWorkloadShareInputRequestTypeDef",
    "DisassociateLensesInputRequestTypeDef",
    "DisassociateProfilesInputRequestTypeDef",
    "ExportLensInputRequestTypeDef",
    "GetAnswerInputRequestTypeDef",
    "GetConsolidatedReportInputRequestTypeDef",
    "GetLensInputRequestTypeDef",
    "LensTypeDef",
    "GetLensReviewInputRequestTypeDef",
    "GetLensReviewReportInputRequestTypeDef",
    "LensReviewReportTypeDef",
    "GetLensVersionDifferenceInputRequestTypeDef",
    "GetMilestoneInputRequestTypeDef",
    "GetProfileInputRequestTypeDef",
    "GetReviewTemplateAnswerInputRequestTypeDef",
    "GetReviewTemplateInputRequestTypeDef",
    "GetReviewTemplateLensReviewInputRequestTypeDef",
    "ReviewTemplateTypeDef",
    "GetWorkloadInputRequestTypeDef",
    "ImportLensInputRequestTypeDef",
    "WorkloadProfileTypeDef",
    "PillarReviewSummaryTypeDef",
    "LensShareSummaryTypeDef",
    "LensSummaryTypeDef",
    "LensUpgradeSummaryTypeDef",
    "ListAnswersInputRequestTypeDef",
    "ListCheckDetailsInputRequestTypeDef",
    "ListCheckSummariesInputRequestTypeDef",
    "ListLensReviewImprovementsInputRequestTypeDef",
    "ListLensReviewsInputRequestTypeDef",
    "ListLensSharesInputRequestTypeDef",
    "ListLensesInputRequestTypeDef",
    "ListMilestonesInputRequestTypeDef",
    "ListNotificationsInputRequestTypeDef",
    "ListProfileNotificationsInputRequestTypeDef",
    "ProfileNotificationSummaryTypeDef",
    "ListProfileSharesInputRequestTypeDef",
    "ProfileShareSummaryTypeDef",
    "ListProfilesInputRequestTypeDef",
    "ProfileSummaryTypeDef",
    "ListReviewTemplateAnswersInputRequestTypeDef",
    "ListReviewTemplatesInputRequestTypeDef",
    "ReviewTemplateSummaryTypeDef",
    "ListShareInvitationsInputRequestTypeDef",
    "ShareInvitationSummaryTypeDef",
    "ListTagsForResourceInputRequestTypeDef",
    "ListTemplateSharesInputRequestTypeDef",
    "TemplateShareSummaryTypeDef",
    "ListWorkloadSharesInputRequestTypeDef",
    "WorkloadShareSummaryTypeDef",
    "ListWorkloadsInputRequestTypeDef",
    "QuestionDifferenceTypeDef",
    "ProfileChoiceTypeDef",
    "ProfileTemplateChoiceTypeDef",
    "ReviewTemplatePillarReviewSummaryTypeDef",
    "ShareInvitationTypeDef",
    "TagResourceInputRequestTypeDef",
    "UntagResourceInputRequestTypeDef",
    "UpdateGlobalSettingsInputRequestTypeDef",
    "UpdateLensReviewInputRequestTypeDef",
    "UpdateReviewTemplateInputRequestTypeDef",
    "UpdateReviewTemplateLensReviewInputRequestTypeDef",
    "UpdateShareInvitationInputRequestTypeDef",
    "UpdateWorkloadShareInputRequestTypeDef",
    "WorkloadShareTypeDef",
    "UpgradeLensReviewInputRequestTypeDef",
    "UpgradeProfileVersionInputRequestTypeDef",
    "UpgradeReviewTemplateLensReviewInputRequestTypeDef",
    "AdditionalResourcesTypeDef",
    "QuestionMetricTypeDef",
    "ImprovementSummaryTypeDef",
    "UpdateAnswerInputRequestTypeDef",
    "UpdateReviewTemplateAnswerInputRequestTypeDef",
    "CreateLensShareOutputTypeDef",
    "CreateLensVersionOutputTypeDef",
    "CreateMilestoneOutputTypeDef",
    "CreateProfileOutputTypeDef",
    "CreateProfileShareOutputTypeDef",
    "CreateReviewTemplateOutputTypeDef",
    "CreateTemplateShareOutputTypeDef",
    "CreateWorkloadOutputTypeDef",
    "CreateWorkloadShareOutputTypeDef",
    "EmptyResponseMetadataTypeDef",
    "ExportLensOutputTypeDef",
    "ImportLensOutputTypeDef",
    "ListCheckDetailsOutputTypeDef",
    "ListCheckSummariesOutputTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "CreateProfileInputRequestTypeDef",
    "UpdateProfileInputRequestTypeDef",
    "CreateWorkloadInputRequestTypeDef",
    "UpdateWorkloadInputRequestTypeDef",
    "GetLensOutputTypeDef",
    "GetLensReviewReportOutputTypeDef",
    "GetReviewTemplateOutputTypeDef",
    "UpdateReviewTemplateOutputTypeDef",
    "LensReviewSummaryTypeDef",
    "WorkloadSummaryTypeDef",
    "WorkloadTypeDef",
    "LensReviewTypeDef",
    "ListLensSharesOutputTypeDef",
    "ListLensesOutputTypeDef",
    "NotificationSummaryTypeDef",
    "ListProfileNotificationsOutputTypeDef",
    "ListProfileSharesOutputTypeDef",
    "ListProfilesOutputTypeDef",
    "ListReviewTemplatesOutputTypeDef",
    "ListShareInvitationsOutputTypeDef",
    "ListTemplateSharesOutputTypeDef",
    "ListWorkloadSharesOutputTypeDef",
    "PillarDifferenceTypeDef",
    "ProfileQuestionTypeDef",
    "ProfileTemplateQuestionTypeDef",
    "ReviewTemplateLensReviewTypeDef",
    "UpdateShareInvitationOutputTypeDef",
    "UpdateWorkloadShareOutputTypeDef",
    "ChoiceTypeDef",
    "PillarMetricTypeDef",
    "ListLensReviewImprovementsOutputTypeDef",
    "ListLensReviewsOutputTypeDef",
    "ListWorkloadsOutputTypeDef",
    "MilestoneSummaryTypeDef",
    "GetWorkloadOutputTypeDef",
    "MilestoneTypeDef",
    "UpdateWorkloadOutputTypeDef",
    "GetLensReviewOutputTypeDef",
    "UpdateLensReviewOutputTypeDef",
    "ListNotificationsOutputTypeDef",
    "VersionDifferencesTypeDef",
    "ProfileTypeDef",
    "ProfileTemplateTypeDef",
    "GetReviewTemplateLensReviewOutputTypeDef",
    "UpdateReviewTemplateLensReviewOutputTypeDef",
    "AnswerSummaryTypeDef",
    "AnswerTypeDef",
    "ReviewTemplateAnswerSummaryTypeDef",
    "ReviewTemplateAnswerTypeDef",
    "LensMetricTypeDef",
    "ListMilestonesOutputTypeDef",
    "GetMilestoneOutputTypeDef",
    "GetLensVersionDifferenceOutputTypeDef",
    "GetProfileOutputTypeDef",
    "UpdateProfileOutputTypeDef",
    "GetProfileTemplateOutputTypeDef",
    "ListAnswersOutputTypeDef",
    "GetAnswerOutputTypeDef",
    "UpdateAnswerOutputTypeDef",
    "ListReviewTemplateAnswersOutputTypeDef",
    "GetReviewTemplateAnswerOutputTypeDef",
    "UpdateReviewTemplateAnswerOutputTypeDef",
    "ConsolidatedReportMetricTypeDef",
    "GetConsolidatedReportOutputTypeDef",
)

ChoiceContentTypeDef = TypedDict(
    "ChoiceContentTypeDef",
    {
        "DisplayText": NotRequired[str],
        "Url": NotRequired[str],
    },
)
ChoiceAnswerSummaryTypeDef = TypedDict(
    "ChoiceAnswerSummaryTypeDef",
    {
        "ChoiceId": NotRequired[str],
        "Status": NotRequired[ChoiceStatusType],
        "Reason": NotRequired[ChoiceReasonType],
    },
)
ChoiceAnswerTypeDef = TypedDict(
    "ChoiceAnswerTypeDef",
    {
        "ChoiceId": NotRequired[str],
        "Status": NotRequired[ChoiceStatusType],
        "Reason": NotRequired[ChoiceReasonType],
        "Notes": NotRequired[str],
    },
)
AssociateLensesInputRequestTypeDef = TypedDict(
    "AssociateLensesInputRequestTypeDef",
    {
        "WorkloadId": str,
        "LensAliases": Sequence[str],
    },
)
AssociateProfilesInputRequestTypeDef = TypedDict(
    "AssociateProfilesInputRequestTypeDef",
    {
        "WorkloadId": str,
        "ProfileArns": Sequence[str],
    },
)
BestPracticeTypeDef = TypedDict(
    "BestPracticeTypeDef",
    {
        "ChoiceId": NotRequired[str],
        "ChoiceTitle": NotRequired[str],
    },
)
CheckDetailTypeDef = TypedDict(
    "CheckDetailTypeDef",
    {
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "Provider": NotRequired[Literal["TRUSTED_ADVISOR"]],
        "LensArn": NotRequired[str],
        "PillarId": NotRequired[str],
        "QuestionId": NotRequired[str],
        "ChoiceId": NotRequired[str],
        "Status": NotRequired[CheckStatusType],
        "AccountId": NotRequired[str],
        "FlaggedResources": NotRequired[int],
        "Reason": NotRequired[CheckFailureReasonType],
        "UpdatedAt": NotRequired[datetime],
    },
)
CheckSummaryTypeDef = TypedDict(
    "CheckSummaryTypeDef",
    {
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "Provider": NotRequired[Literal["TRUSTED_ADVISOR"]],
        "Description": NotRequired[str],
        "UpdatedAt": NotRequired[datetime],
        "LensArn": NotRequired[str],
        "PillarId": NotRequired[str],
        "QuestionId": NotRequired[str],
        "ChoiceId": NotRequired[str],
        "Status": NotRequired[CheckStatusType],
        "AccountSummary": NotRequired[Dict[CheckStatusType, int]],
    },
)
ChoiceImprovementPlanTypeDef = TypedDict(
    "ChoiceImprovementPlanTypeDef",
    {
        "ChoiceId": NotRequired[str],
        "DisplayText": NotRequired[str],
        "ImprovementPlanUrl": NotRequired[str],
    },
)
ChoiceUpdateTypeDef = TypedDict(
    "ChoiceUpdateTypeDef",
    {
        "Status": ChoiceStatusType,
        "Reason": NotRequired[ChoiceReasonType],
        "Notes": NotRequired[str],
    },
)
CreateLensShareInputRequestTypeDef = TypedDict(
    "CreateLensShareInputRequestTypeDef",
    {
        "LensAlias": str,
        "SharedWith": str,
        "ClientRequestToken": str,
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
CreateLensVersionInputRequestTypeDef = TypedDict(
    "CreateLensVersionInputRequestTypeDef",
    {
        "LensAlias": str,
        "LensVersion": str,
        "ClientRequestToken": str,
        "IsMajorVersion": NotRequired[bool],
    },
)
CreateMilestoneInputRequestTypeDef = TypedDict(
    "CreateMilestoneInputRequestTypeDef",
    {
        "WorkloadId": str,
        "MilestoneName": str,
        "ClientRequestToken": str,
    },
)
ProfileQuestionUpdateTypeDef = TypedDict(
    "ProfileQuestionUpdateTypeDef",
    {
        "QuestionId": NotRequired[str],
        "SelectedChoiceIds": NotRequired[Sequence[str]],
    },
)
CreateProfileShareInputRequestTypeDef = TypedDict(
    "CreateProfileShareInputRequestTypeDef",
    {
        "ProfileArn": str,
        "SharedWith": str,
        "ClientRequestToken": str,
    },
)
CreateReviewTemplateInputRequestTypeDef = TypedDict(
    "CreateReviewTemplateInputRequestTypeDef",
    {
        "TemplateName": str,
        "Description": str,
        "Lenses": Sequence[str],
        "ClientRequestToken": str,
        "Notes": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
CreateTemplateShareInputRequestTypeDef = TypedDict(
    "CreateTemplateShareInputRequestTypeDef",
    {
        "TemplateArn": str,
        "SharedWith": str,
        "ClientRequestToken": str,
    },
)
WorkloadDiscoveryConfigTypeDef = TypedDict(
    "WorkloadDiscoveryConfigTypeDef",
    {
        "TrustedAdvisorIntegrationStatus": NotRequired[TrustedAdvisorIntegrationStatusType],
        "WorkloadResourceDefinition": NotRequired[Sequence[DefinitionTypeType]],
    },
)
CreateWorkloadShareInputRequestTypeDef = TypedDict(
    "CreateWorkloadShareInputRequestTypeDef",
    {
        "WorkloadId": str,
        "SharedWith": str,
        "PermissionType": PermissionTypeType,
        "ClientRequestToken": str,
    },
)
DeleteLensInputRequestTypeDef = TypedDict(
    "DeleteLensInputRequestTypeDef",
    {
        "LensAlias": str,
        "ClientRequestToken": str,
        "LensStatus": LensStatusTypeType,
    },
)
DeleteLensShareInputRequestTypeDef = TypedDict(
    "DeleteLensShareInputRequestTypeDef",
    {
        "ShareId": str,
        "LensAlias": str,
        "ClientRequestToken": str,
    },
)
DeleteProfileInputRequestTypeDef = TypedDict(
    "DeleteProfileInputRequestTypeDef",
    {
        "ProfileArn": str,
        "ClientRequestToken": str,
    },
)
DeleteProfileShareInputRequestTypeDef = TypedDict(
    "DeleteProfileShareInputRequestTypeDef",
    {
        "ShareId": str,
        "ProfileArn": str,
        "ClientRequestToken": str,
    },
)
DeleteReviewTemplateInputRequestTypeDef = TypedDict(
    "DeleteReviewTemplateInputRequestTypeDef",
    {
        "TemplateArn": str,
        "ClientRequestToken": str,
    },
)
DeleteTemplateShareInputRequestTypeDef = TypedDict(
    "DeleteTemplateShareInputRequestTypeDef",
    {
        "ShareId": str,
        "TemplateArn": str,
        "ClientRequestToken": str,
    },
)
DeleteWorkloadInputRequestTypeDef = TypedDict(
    "DeleteWorkloadInputRequestTypeDef",
    {
        "WorkloadId": str,
        "ClientRequestToken": str,
    },
)
DeleteWorkloadShareInputRequestTypeDef = TypedDict(
    "DeleteWorkloadShareInputRequestTypeDef",
    {
        "ShareId": str,
        "WorkloadId": str,
        "ClientRequestToken": str,
    },
)
DisassociateLensesInputRequestTypeDef = TypedDict(
    "DisassociateLensesInputRequestTypeDef",
    {
        "WorkloadId": str,
        "LensAliases": Sequence[str],
    },
)
DisassociateProfilesInputRequestTypeDef = TypedDict(
    "DisassociateProfilesInputRequestTypeDef",
    {
        "WorkloadId": str,
        "ProfileArns": Sequence[str],
    },
)
ExportLensInputRequestTypeDef = TypedDict(
    "ExportLensInputRequestTypeDef",
    {
        "LensAlias": str,
        "LensVersion": NotRequired[str],
    },
)
GetAnswerInputRequestTypeDef = TypedDict(
    "GetAnswerInputRequestTypeDef",
    {
        "WorkloadId": str,
        "LensAlias": str,
        "QuestionId": str,
        "MilestoneNumber": NotRequired[int],
    },
)
GetConsolidatedReportInputRequestTypeDef = TypedDict(
    "GetConsolidatedReportInputRequestTypeDef",
    {
        "Format": ReportFormatType,
        "IncludeSharedResources": NotRequired[bool],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
GetLensInputRequestTypeDef = TypedDict(
    "GetLensInputRequestTypeDef",
    {
        "LensAlias": str,
        "LensVersion": NotRequired[str],
    },
)
LensTypeDef = TypedDict(
    "LensTypeDef",
    {
        "LensArn": NotRequired[str],
        "LensVersion": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "Owner": NotRequired[str],
        "ShareInvitationId": NotRequired[str],
        "Tags": NotRequired[Dict[str, str]],
    },
)
GetLensReviewInputRequestTypeDef = TypedDict(
    "GetLensReviewInputRequestTypeDef",
    {
        "WorkloadId": str,
        "LensAlias": str,
        "MilestoneNumber": NotRequired[int],
    },
)
GetLensReviewReportInputRequestTypeDef = TypedDict(
    "GetLensReviewReportInputRequestTypeDef",
    {
        "WorkloadId": str,
        "LensAlias": str,
        "MilestoneNumber": NotRequired[int],
    },
)
LensReviewReportTypeDef = TypedDict(
    "LensReviewReportTypeDef",
    {
        "LensAlias": NotRequired[str],
        "LensArn": NotRequired[str],
        "Base64String": NotRequired[str],
    },
)
GetLensVersionDifferenceInputRequestTypeDef = TypedDict(
    "GetLensVersionDifferenceInputRequestTypeDef",
    {
        "LensAlias": str,
        "BaseLensVersion": NotRequired[str],
        "TargetLensVersion": NotRequired[str],
    },
)
GetMilestoneInputRequestTypeDef = TypedDict(
    "GetMilestoneInputRequestTypeDef",
    {
        "WorkloadId": str,
        "MilestoneNumber": int,
    },
)
GetProfileInputRequestTypeDef = TypedDict(
    "GetProfileInputRequestTypeDef",
    {
        "ProfileArn": str,
        "ProfileVersion": NotRequired[str],
    },
)
GetReviewTemplateAnswerInputRequestTypeDef = TypedDict(
    "GetReviewTemplateAnswerInputRequestTypeDef",
    {
        "TemplateArn": str,
        "LensAlias": str,
        "QuestionId": str,
    },
)
GetReviewTemplateInputRequestTypeDef = TypedDict(
    "GetReviewTemplateInputRequestTypeDef",
    {
        "TemplateArn": str,
    },
)
GetReviewTemplateLensReviewInputRequestTypeDef = TypedDict(
    "GetReviewTemplateLensReviewInputRequestTypeDef",
    {
        "TemplateArn": str,
        "LensAlias": str,
    },
)
ReviewTemplateTypeDef = TypedDict(
    "ReviewTemplateTypeDef",
    {
        "Description": NotRequired[str],
        "Lenses": NotRequired[List[str]],
        "Notes": NotRequired[str],
        "QuestionCounts": NotRequired[Dict[QuestionType, int]],
        "Owner": NotRequired[str],
        "UpdatedAt": NotRequired[datetime],
        "TemplateArn": NotRequired[str],
        "TemplateName": NotRequired[str],
        "Tags": NotRequired[Dict[str, str]],
        "UpdateStatus": NotRequired[ReviewTemplateUpdateStatusType],
        "ShareInvitationId": NotRequired[str],
    },
)
GetWorkloadInputRequestTypeDef = TypedDict(
    "GetWorkloadInputRequestTypeDef",
    {
        "WorkloadId": str,
    },
)
ImportLensInputRequestTypeDef = TypedDict(
    "ImportLensInputRequestTypeDef",
    {
        "JSONString": str,
        "ClientRequestToken": str,
        "LensAlias": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
WorkloadProfileTypeDef = TypedDict(
    "WorkloadProfileTypeDef",
    {
        "ProfileArn": NotRequired[str],
        "ProfileVersion": NotRequired[str],
    },
)
PillarReviewSummaryTypeDef = TypedDict(
    "PillarReviewSummaryTypeDef",
    {
        "PillarId": NotRequired[str],
        "PillarName": NotRequired[str],
        "Notes": NotRequired[str],
        "RiskCounts": NotRequired[Dict[RiskType, int]],
        "PrioritizedRiskCounts": NotRequired[Dict[RiskType, int]],
    },
)
LensShareSummaryTypeDef = TypedDict(
    "LensShareSummaryTypeDef",
    {
        "ShareId": NotRequired[str],
        "SharedWith": NotRequired[str],
        "Status": NotRequired[ShareStatusType],
        "StatusMessage": NotRequired[str],
    },
)
LensSummaryTypeDef = TypedDict(
    "LensSummaryTypeDef",
    {
        "LensArn": NotRequired[str],
        "LensAlias": NotRequired[str],
        "LensName": NotRequired[str],
        "LensType": NotRequired[LensTypeType],
        "Description": NotRequired[str],
        "CreatedAt": NotRequired[datetime],
        "UpdatedAt": NotRequired[datetime],
        "LensVersion": NotRequired[str],
        "Owner": NotRequired[str],
        "LensStatus": NotRequired[LensStatusType],
    },
)
LensUpgradeSummaryTypeDef = TypedDict(
    "LensUpgradeSummaryTypeDef",
    {
        "WorkloadId": NotRequired[str],
        "WorkloadName": NotRequired[str],
        "LensAlias": NotRequired[str],
        "LensArn": NotRequired[str],
        "CurrentLensVersion": NotRequired[str],
        "LatestLensVersion": NotRequired[str],
        "ResourceArn": NotRequired[str],
        "ResourceName": NotRequired[str],
    },
)
ListAnswersInputRequestTypeDef = TypedDict(
    "ListAnswersInputRequestTypeDef",
    {
        "WorkloadId": str,
        "LensAlias": str,
        "PillarId": NotRequired[str],
        "MilestoneNumber": NotRequired[int],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "QuestionPriority": NotRequired[QuestionPriorityType],
    },
)
ListCheckDetailsInputRequestTypeDef = TypedDict(
    "ListCheckDetailsInputRequestTypeDef",
    {
        "WorkloadId": str,
        "LensArn": str,
        "PillarId": str,
        "QuestionId": str,
        "ChoiceId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListCheckSummariesInputRequestTypeDef = TypedDict(
    "ListCheckSummariesInputRequestTypeDef",
    {
        "WorkloadId": str,
        "LensArn": str,
        "PillarId": str,
        "QuestionId": str,
        "ChoiceId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListLensReviewImprovementsInputRequestTypeDef = TypedDict(
    "ListLensReviewImprovementsInputRequestTypeDef",
    {
        "WorkloadId": str,
        "LensAlias": str,
        "PillarId": NotRequired[str],
        "MilestoneNumber": NotRequired[int],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "QuestionPriority": NotRequired[QuestionPriorityType],
    },
)
ListLensReviewsInputRequestTypeDef = TypedDict(
    "ListLensReviewsInputRequestTypeDef",
    {
        "WorkloadId": str,
        "MilestoneNumber": NotRequired[int],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListLensSharesInputRequestTypeDef = TypedDict(
    "ListLensSharesInputRequestTypeDef",
    {
        "LensAlias": str,
        "SharedWithPrefix": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "Status": NotRequired[ShareStatusType],
    },
)
ListLensesInputRequestTypeDef = TypedDict(
    "ListLensesInputRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "LensType": NotRequired[LensTypeType],
        "LensStatus": NotRequired[LensStatusTypeType],
        "LensName": NotRequired[str],
    },
)
ListMilestonesInputRequestTypeDef = TypedDict(
    "ListMilestonesInputRequestTypeDef",
    {
        "WorkloadId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListNotificationsInputRequestTypeDef = TypedDict(
    "ListNotificationsInputRequestTypeDef",
    {
        "WorkloadId": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "ResourceArn": NotRequired[str],
    },
)
ListProfileNotificationsInputRequestTypeDef = TypedDict(
    "ListProfileNotificationsInputRequestTypeDef",
    {
        "WorkloadId": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ProfileNotificationSummaryTypeDef = TypedDict(
    "ProfileNotificationSummaryTypeDef",
    {
        "CurrentProfileVersion": NotRequired[str],
        "LatestProfileVersion": NotRequired[str],
        "Type": NotRequired[ProfileNotificationTypeType],
        "ProfileArn": NotRequired[str],
        "ProfileName": NotRequired[str],
        "WorkloadId": NotRequired[str],
        "WorkloadName": NotRequired[str],
    },
)
ListProfileSharesInputRequestTypeDef = TypedDict(
    "ListProfileSharesInputRequestTypeDef",
    {
        "ProfileArn": str,
        "SharedWithPrefix": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "Status": NotRequired[ShareStatusType],
    },
)
ProfileShareSummaryTypeDef = TypedDict(
    "ProfileShareSummaryTypeDef",
    {
        "ShareId": NotRequired[str],
        "SharedWith": NotRequired[str],
        "Status": NotRequired[ShareStatusType],
        "StatusMessage": NotRequired[str],
    },
)
ListProfilesInputRequestTypeDef = TypedDict(
    "ListProfilesInputRequestTypeDef",
    {
        "ProfileNamePrefix": NotRequired[str],
        "ProfileOwnerType": NotRequired[ProfileOwnerTypeType],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ProfileSummaryTypeDef = TypedDict(
    "ProfileSummaryTypeDef",
    {
        "ProfileArn": NotRequired[str],
        "ProfileVersion": NotRequired[str],
        "ProfileName": NotRequired[str],
        "ProfileDescription": NotRequired[str],
        "Owner": NotRequired[str],
        "CreatedAt": NotRequired[datetime],
        "UpdatedAt": NotRequired[datetime],
    },
)
ListReviewTemplateAnswersInputRequestTypeDef = TypedDict(
    "ListReviewTemplateAnswersInputRequestTypeDef",
    {
        "TemplateArn": str,
        "LensAlias": str,
        "PillarId": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListReviewTemplatesInputRequestTypeDef = TypedDict(
    "ListReviewTemplatesInputRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ReviewTemplateSummaryTypeDef = TypedDict(
    "ReviewTemplateSummaryTypeDef",
    {
        "Description": NotRequired[str],
        "Lenses": NotRequired[List[str]],
        "Owner": NotRequired[str],
        "UpdatedAt": NotRequired[datetime],
        "TemplateArn": NotRequired[str],
        "TemplateName": NotRequired[str],
        "UpdateStatus": NotRequired[ReviewTemplateUpdateStatusType],
    },
)
ListShareInvitationsInputRequestTypeDef = TypedDict(
    "ListShareInvitationsInputRequestTypeDef",
    {
        "WorkloadNamePrefix": NotRequired[str],
        "LensNamePrefix": NotRequired[str],
        "ShareResourceType": NotRequired[ShareResourceTypeType],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "ProfileNamePrefix": NotRequired[str],
        "TemplateNamePrefix": NotRequired[str],
    },
)
ShareInvitationSummaryTypeDef = TypedDict(
    "ShareInvitationSummaryTypeDef",
    {
        "ShareInvitationId": NotRequired[str],
        "SharedBy": NotRequired[str],
        "SharedWith": NotRequired[str],
        "PermissionType": NotRequired[PermissionTypeType],
        "ShareResourceType": NotRequired[ShareResourceTypeType],
        "WorkloadName": NotRequired[str],
        "WorkloadId": NotRequired[str],
        "LensName": NotRequired[str],
        "LensArn": NotRequired[str],
        "ProfileName": NotRequired[str],
        "ProfileArn": NotRequired[str],
        "TemplateName": NotRequired[str],
        "TemplateArn": NotRequired[str],
    },
)
ListTagsForResourceInputRequestTypeDef = TypedDict(
    "ListTagsForResourceInputRequestTypeDef",
    {
        "WorkloadArn": str,
    },
)
ListTemplateSharesInputRequestTypeDef = TypedDict(
    "ListTemplateSharesInputRequestTypeDef",
    {
        "TemplateArn": str,
        "SharedWithPrefix": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "Status": NotRequired[ShareStatusType],
    },
)
TemplateShareSummaryTypeDef = TypedDict(
    "TemplateShareSummaryTypeDef",
    {
        "ShareId": NotRequired[str],
        "SharedWith": NotRequired[str],
        "Status": NotRequired[ShareStatusType],
        "StatusMessage": NotRequired[str],
    },
)
ListWorkloadSharesInputRequestTypeDef = TypedDict(
    "ListWorkloadSharesInputRequestTypeDef",
    {
        "WorkloadId": str,
        "SharedWithPrefix": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "Status": NotRequired[ShareStatusType],
    },
)
WorkloadShareSummaryTypeDef = TypedDict(
    "WorkloadShareSummaryTypeDef",
    {
        "ShareId": NotRequired[str],
        "SharedWith": NotRequired[str],
        "PermissionType": NotRequired[PermissionTypeType],
        "Status": NotRequired[ShareStatusType],
        "StatusMessage": NotRequired[str],
    },
)
ListWorkloadsInputRequestTypeDef = TypedDict(
    "ListWorkloadsInputRequestTypeDef",
    {
        "WorkloadNamePrefix": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
QuestionDifferenceTypeDef = TypedDict(
    "QuestionDifferenceTypeDef",
    {
        "QuestionId": NotRequired[str],
        "QuestionTitle": NotRequired[str],
        "DifferenceStatus": NotRequired[DifferenceStatusType],
    },
)
ProfileChoiceTypeDef = TypedDict(
    "ProfileChoiceTypeDef",
    {
        "ChoiceId": NotRequired[str],
        "ChoiceTitle": NotRequired[str],
        "ChoiceDescription": NotRequired[str],
    },
)
ProfileTemplateChoiceTypeDef = TypedDict(
    "ProfileTemplateChoiceTypeDef",
    {
        "ChoiceId": NotRequired[str],
        "ChoiceTitle": NotRequired[str],
        "ChoiceDescription": NotRequired[str],
    },
)
ReviewTemplatePillarReviewSummaryTypeDef = TypedDict(
    "ReviewTemplatePillarReviewSummaryTypeDef",
    {
        "PillarId": NotRequired[str],
        "PillarName": NotRequired[str],
        "Notes": NotRequired[str],
        "QuestionCounts": NotRequired[Dict[QuestionType, int]],
    },
)
ShareInvitationTypeDef = TypedDict(
    "ShareInvitationTypeDef",
    {
        "ShareInvitationId": NotRequired[str],
        "ShareResourceType": NotRequired[ShareResourceTypeType],
        "WorkloadId": NotRequired[str],
        "LensAlias": NotRequired[str],
        "LensArn": NotRequired[str],
        "ProfileArn": NotRequired[str],
        "TemplateArn": NotRequired[str],
    },
)
TagResourceInputRequestTypeDef = TypedDict(
    "TagResourceInputRequestTypeDef",
    {
        "WorkloadArn": str,
        "Tags": Mapping[str, str],
    },
)
UntagResourceInputRequestTypeDef = TypedDict(
    "UntagResourceInputRequestTypeDef",
    {
        "WorkloadArn": str,
        "TagKeys": Sequence[str],
    },
)
UpdateGlobalSettingsInputRequestTypeDef = TypedDict(
    "UpdateGlobalSettingsInputRequestTypeDef",
    {
        "OrganizationSharingStatus": NotRequired[OrganizationSharingStatusType],
        "DiscoveryIntegrationStatus": NotRequired[DiscoveryIntegrationStatusType],
    },
)
UpdateLensReviewInputRequestTypeDef = TypedDict(
    "UpdateLensReviewInputRequestTypeDef",
    {
        "WorkloadId": str,
        "LensAlias": str,
        "LensNotes": NotRequired[str],
        "PillarNotes": NotRequired[Mapping[str, str]],
    },
)
UpdateReviewTemplateInputRequestTypeDef = TypedDict(
    "UpdateReviewTemplateInputRequestTypeDef",
    {
        "TemplateArn": str,
        "TemplateName": NotRequired[str],
        "Description": NotRequired[str],
        "Notes": NotRequired[str],
        "LensesToAssociate": NotRequired[Sequence[str]],
        "LensesToDisassociate": NotRequired[Sequence[str]],
    },
)
UpdateReviewTemplateLensReviewInputRequestTypeDef = TypedDict(
    "UpdateReviewTemplateLensReviewInputRequestTypeDef",
    {
        "TemplateArn": str,
        "LensAlias": str,
        "LensNotes": NotRequired[str],
        "PillarNotes": NotRequired[Mapping[str, str]],
    },
)
UpdateShareInvitationInputRequestTypeDef = TypedDict(
    "UpdateShareInvitationInputRequestTypeDef",
    {
        "ShareInvitationId": str,
        "ShareInvitationAction": ShareInvitationActionType,
    },
)
UpdateWorkloadShareInputRequestTypeDef = TypedDict(
    "UpdateWorkloadShareInputRequestTypeDef",
    {
        "ShareId": str,
        "WorkloadId": str,
        "PermissionType": PermissionTypeType,
    },
)
WorkloadShareTypeDef = TypedDict(
    "WorkloadShareTypeDef",
    {
        "ShareId": NotRequired[str],
        "SharedBy": NotRequired[str],
        "SharedWith": NotRequired[str],
        "PermissionType": NotRequired[PermissionTypeType],
        "Status": NotRequired[ShareStatusType],
        "WorkloadName": NotRequired[str],
        "WorkloadId": NotRequired[str],
    },
)
UpgradeLensReviewInputRequestTypeDef = TypedDict(
    "UpgradeLensReviewInputRequestTypeDef",
    {
        "WorkloadId": str,
        "LensAlias": str,
        "MilestoneName": str,
        "ClientRequestToken": NotRequired[str],
    },
)
UpgradeProfileVersionInputRequestTypeDef = TypedDict(
    "UpgradeProfileVersionInputRequestTypeDef",
    {
        "WorkloadId": str,
        "ProfileArn": str,
        "MilestoneName": NotRequired[str],
        "ClientRequestToken": NotRequired[str],
    },
)
UpgradeReviewTemplateLensReviewInputRequestTypeDef = TypedDict(
    "UpgradeReviewTemplateLensReviewInputRequestTypeDef",
    {
        "TemplateArn": str,
        "LensAlias": str,
        "ClientRequestToken": NotRequired[str],
    },
)
AdditionalResourcesTypeDef = TypedDict(
    "AdditionalResourcesTypeDef",
    {
        "Type": NotRequired[AdditionalResourceTypeType],
        "Content": NotRequired[List[ChoiceContentTypeDef]],
    },
)
QuestionMetricTypeDef = TypedDict(
    "QuestionMetricTypeDef",
    {
        "QuestionId": NotRequired[str],
        "Risk": NotRequired[RiskType],
        "BestPractices": NotRequired[List[BestPracticeTypeDef]],
    },
)
ImprovementSummaryTypeDef = TypedDict(
    "ImprovementSummaryTypeDef",
    {
        "QuestionId": NotRequired[str],
        "PillarId": NotRequired[str],
        "QuestionTitle": NotRequired[str],
        "Risk": NotRequired[RiskType],
        "ImprovementPlanUrl": NotRequired[str],
        "ImprovementPlans": NotRequired[List[ChoiceImprovementPlanTypeDef]],
    },
)
UpdateAnswerInputRequestTypeDef = TypedDict(
    "UpdateAnswerInputRequestTypeDef",
    {
        "WorkloadId": str,
        "LensAlias": str,
        "QuestionId": str,
        "SelectedChoices": NotRequired[Sequence[str]],
        "ChoiceUpdates": NotRequired[Mapping[str, ChoiceUpdateTypeDef]],
        "Notes": NotRequired[str],
        "IsApplicable": NotRequired[bool],
        "Reason": NotRequired[AnswerReasonType],
    },
)
UpdateReviewTemplateAnswerInputRequestTypeDef = TypedDict(
    "UpdateReviewTemplateAnswerInputRequestTypeDef",
    {
        "TemplateArn": str,
        "LensAlias": str,
        "QuestionId": str,
        "SelectedChoices": NotRequired[Sequence[str]],
        "ChoiceUpdates": NotRequired[Mapping[str, ChoiceUpdateTypeDef]],
        "Notes": NotRequired[str],
        "IsApplicable": NotRequired[bool],
        "Reason": NotRequired[AnswerReasonType],
    },
)
CreateLensShareOutputTypeDef = TypedDict(
    "CreateLensShareOutputTypeDef",
    {
        "ShareId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateLensVersionOutputTypeDef = TypedDict(
    "CreateLensVersionOutputTypeDef",
    {
        "LensArn": str,
        "LensVersion": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateMilestoneOutputTypeDef = TypedDict(
    "CreateMilestoneOutputTypeDef",
    {
        "WorkloadId": str,
        "MilestoneNumber": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateProfileOutputTypeDef = TypedDict(
    "CreateProfileOutputTypeDef",
    {
        "ProfileArn": str,
        "ProfileVersion": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateProfileShareOutputTypeDef = TypedDict(
    "CreateProfileShareOutputTypeDef",
    {
        "ShareId": str,
        "ProfileArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateReviewTemplateOutputTypeDef = TypedDict(
    "CreateReviewTemplateOutputTypeDef",
    {
        "TemplateArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateTemplateShareOutputTypeDef = TypedDict(
    "CreateTemplateShareOutputTypeDef",
    {
        "TemplateArn": str,
        "ShareId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateWorkloadOutputTypeDef = TypedDict(
    "CreateWorkloadOutputTypeDef",
    {
        "WorkloadId": str,
        "WorkloadArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateWorkloadShareOutputTypeDef = TypedDict(
    "CreateWorkloadShareOutputTypeDef",
    {
        "WorkloadId": str,
        "ShareId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ExportLensOutputTypeDef = TypedDict(
    "ExportLensOutputTypeDef",
    {
        "LensJSON": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ImportLensOutputTypeDef = TypedDict(
    "ImportLensOutputTypeDef",
    {
        "LensArn": str,
        "Status": ImportLensStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListCheckDetailsOutputTypeDef = TypedDict(
    "ListCheckDetailsOutputTypeDef",
    {
        "CheckDetails": List[CheckDetailTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListCheckSummariesOutputTypeDef = TypedDict(
    "ListCheckSummariesOutputTypeDef",
    {
        "CheckSummaries": List[CheckSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateProfileInputRequestTypeDef = TypedDict(
    "CreateProfileInputRequestTypeDef",
    {
        "ProfileName": str,
        "ProfileDescription": str,
        "ProfileQuestions": Sequence[ProfileQuestionUpdateTypeDef],
        "ClientRequestToken": str,
        "Tags": NotRequired[Mapping[str, str]],
    },
)
UpdateProfileInputRequestTypeDef = TypedDict(
    "UpdateProfileInputRequestTypeDef",
    {
        "ProfileArn": str,
        "ProfileDescription": NotRequired[str],
        "ProfileQuestions": NotRequired[Sequence[ProfileQuestionUpdateTypeDef]],
    },
)
CreateWorkloadInputRequestTypeDef = TypedDict(
    "CreateWorkloadInputRequestTypeDef",
    {
        "WorkloadName": str,
        "Description": str,
        "Environment": WorkloadEnvironmentType,
        "Lenses": Sequence[str],
        "ClientRequestToken": str,
        "AccountIds": NotRequired[Sequence[str]],
        "AwsRegions": NotRequired[Sequence[str]],
        "NonAwsRegions": NotRequired[Sequence[str]],
        "PillarPriorities": NotRequired[Sequence[str]],
        "ArchitecturalDesign": NotRequired[str],
        "ReviewOwner": NotRequired[str],
        "IndustryType": NotRequired[str],
        "Industry": NotRequired[str],
        "Notes": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
        "DiscoveryConfig": NotRequired[WorkloadDiscoveryConfigTypeDef],
        "Applications": NotRequired[Sequence[str]],
        "ProfileArns": NotRequired[Sequence[str]],
        "ReviewTemplateArns": NotRequired[Sequence[str]],
    },
)
UpdateWorkloadInputRequestTypeDef = TypedDict(
    "UpdateWorkloadInputRequestTypeDef",
    {
        "WorkloadId": str,
        "WorkloadName": NotRequired[str],
        "Description": NotRequired[str],
        "Environment": NotRequired[WorkloadEnvironmentType],
        "AccountIds": NotRequired[Sequence[str]],
        "AwsRegions": NotRequired[Sequence[str]],
        "NonAwsRegions": NotRequired[Sequence[str]],
        "PillarPriorities": NotRequired[Sequence[str]],
        "ArchitecturalDesign": NotRequired[str],
        "ReviewOwner": NotRequired[str],
        "IsReviewOwnerUpdateAcknowledged": NotRequired[bool],
        "IndustryType": NotRequired[str],
        "Industry": NotRequired[str],
        "Notes": NotRequired[str],
        "ImprovementStatus": NotRequired[WorkloadImprovementStatusType],
        "DiscoveryConfig": NotRequired[WorkloadDiscoveryConfigTypeDef],
        "Applications": NotRequired[Sequence[str]],
    },
)
GetLensOutputTypeDef = TypedDict(
    "GetLensOutputTypeDef",
    {
        "Lens": LensTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetLensReviewReportOutputTypeDef = TypedDict(
    "GetLensReviewReportOutputTypeDef",
    {
        "WorkloadId": str,
        "MilestoneNumber": int,
        "LensReviewReport": LensReviewReportTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetReviewTemplateOutputTypeDef = TypedDict(
    "GetReviewTemplateOutputTypeDef",
    {
        "ReviewTemplate": ReviewTemplateTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateReviewTemplateOutputTypeDef = TypedDict(
    "UpdateReviewTemplateOutputTypeDef",
    {
        "ReviewTemplate": ReviewTemplateTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
LensReviewSummaryTypeDef = TypedDict(
    "LensReviewSummaryTypeDef",
    {
        "LensAlias": NotRequired[str],
        "LensArn": NotRequired[str],
        "LensVersion": NotRequired[str],
        "LensName": NotRequired[str],
        "LensStatus": NotRequired[LensStatusType],
        "UpdatedAt": NotRequired[datetime],
        "RiskCounts": NotRequired[Dict[RiskType, int]],
        "Profiles": NotRequired[List[WorkloadProfileTypeDef]],
        "PrioritizedRiskCounts": NotRequired[Dict[RiskType, int]],
    },
)
WorkloadSummaryTypeDef = TypedDict(
    "WorkloadSummaryTypeDef",
    {
        "WorkloadId": NotRequired[str],
        "WorkloadArn": NotRequired[str],
        "WorkloadName": NotRequired[str],
        "Owner": NotRequired[str],
        "UpdatedAt": NotRequired[datetime],
        "Lenses": NotRequired[List[str]],
        "RiskCounts": NotRequired[Dict[RiskType, int]],
        "ImprovementStatus": NotRequired[WorkloadImprovementStatusType],
        "Profiles": NotRequired[List[WorkloadProfileTypeDef]],
        "PrioritizedRiskCounts": NotRequired[Dict[RiskType, int]],
    },
)
WorkloadTypeDef = TypedDict(
    "WorkloadTypeDef",
    {
        "WorkloadId": NotRequired[str],
        "WorkloadArn": NotRequired[str],
        "WorkloadName": NotRequired[str],
        "Description": NotRequired[str],
        "Environment": NotRequired[WorkloadEnvironmentType],
        "UpdatedAt": NotRequired[datetime],
        "AccountIds": NotRequired[List[str]],
        "AwsRegions": NotRequired[List[str]],
        "NonAwsRegions": NotRequired[List[str]],
        "ArchitecturalDesign": NotRequired[str],
        "ReviewOwner": NotRequired[str],
        "ReviewRestrictionDate": NotRequired[datetime],
        "IsReviewOwnerUpdateAcknowledged": NotRequired[bool],
        "IndustryType": NotRequired[str],
        "Industry": NotRequired[str],
        "Notes": NotRequired[str],
        "ImprovementStatus": NotRequired[WorkloadImprovementStatusType],
        "RiskCounts": NotRequired[Dict[RiskType, int]],
        "PillarPriorities": NotRequired[List[str]],
        "Lenses": NotRequired[List[str]],
        "Owner": NotRequired[str],
        "ShareInvitationId": NotRequired[str],
        "Tags": NotRequired[Dict[str, str]],
        "DiscoveryConfig": NotRequired[WorkloadDiscoveryConfigTypeDef],
        "Applications": NotRequired[List[str]],
        "Profiles": NotRequired[List[WorkloadProfileTypeDef]],
        "PrioritizedRiskCounts": NotRequired[Dict[RiskType, int]],
    },
)
LensReviewTypeDef = TypedDict(
    "LensReviewTypeDef",
    {
        "LensAlias": NotRequired[str],
        "LensArn": NotRequired[str],
        "LensVersion": NotRequired[str],
        "LensName": NotRequired[str],
        "LensStatus": NotRequired[LensStatusType],
        "PillarReviewSummaries": NotRequired[List[PillarReviewSummaryTypeDef]],
        "UpdatedAt": NotRequired[datetime],
        "Notes": NotRequired[str],
        "RiskCounts": NotRequired[Dict[RiskType, int]],
        "NextToken": NotRequired[str],
        "Profiles": NotRequired[List[WorkloadProfileTypeDef]],
        "PrioritizedRiskCounts": NotRequired[Dict[RiskType, int]],
    },
)
ListLensSharesOutputTypeDef = TypedDict(
    "ListLensSharesOutputTypeDef",
    {
        "LensShareSummaries": List[LensShareSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListLensesOutputTypeDef = TypedDict(
    "ListLensesOutputTypeDef",
    {
        "LensSummaries": List[LensSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
NotificationSummaryTypeDef = TypedDict(
    "NotificationSummaryTypeDef",
    {
        "Type": NotRequired[NotificationTypeType],
        "LensUpgradeSummary": NotRequired[LensUpgradeSummaryTypeDef],
    },
)
ListProfileNotificationsOutputTypeDef = TypedDict(
    "ListProfileNotificationsOutputTypeDef",
    {
        "NotificationSummaries": List[ProfileNotificationSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListProfileSharesOutputTypeDef = TypedDict(
    "ListProfileSharesOutputTypeDef",
    {
        "ProfileShareSummaries": List[ProfileShareSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListProfilesOutputTypeDef = TypedDict(
    "ListProfilesOutputTypeDef",
    {
        "ProfileSummaries": List[ProfileSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListReviewTemplatesOutputTypeDef = TypedDict(
    "ListReviewTemplatesOutputTypeDef",
    {
        "ReviewTemplates": List[ReviewTemplateSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListShareInvitationsOutputTypeDef = TypedDict(
    "ListShareInvitationsOutputTypeDef",
    {
        "ShareInvitationSummaries": List[ShareInvitationSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTemplateSharesOutputTypeDef = TypedDict(
    "ListTemplateSharesOutputTypeDef",
    {
        "TemplateArn": str,
        "TemplateShareSummaries": List[TemplateShareSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListWorkloadSharesOutputTypeDef = TypedDict(
    "ListWorkloadSharesOutputTypeDef",
    {
        "WorkloadId": str,
        "WorkloadShareSummaries": List[WorkloadShareSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PillarDifferenceTypeDef = TypedDict(
    "PillarDifferenceTypeDef",
    {
        "PillarId": NotRequired[str],
        "PillarName": NotRequired[str],
        "DifferenceStatus": NotRequired[DifferenceStatusType],
        "QuestionDifferences": NotRequired[List[QuestionDifferenceTypeDef]],
    },
)
ProfileQuestionTypeDef = TypedDict(
    "ProfileQuestionTypeDef",
    {
        "QuestionId": NotRequired[str],
        "QuestionTitle": NotRequired[str],
        "QuestionDescription": NotRequired[str],
        "QuestionChoices": NotRequired[List[ProfileChoiceTypeDef]],
        "SelectedChoiceIds": NotRequired[List[str]],
        "MinSelectedChoices": NotRequired[int],
        "MaxSelectedChoices": NotRequired[int],
    },
)
ProfileTemplateQuestionTypeDef = TypedDict(
    "ProfileTemplateQuestionTypeDef",
    {
        "QuestionId": NotRequired[str],
        "QuestionTitle": NotRequired[str],
        "QuestionDescription": NotRequired[str],
        "QuestionChoices": NotRequired[List[ProfileTemplateChoiceTypeDef]],
        "MinSelectedChoices": NotRequired[int],
        "MaxSelectedChoices": NotRequired[int],
    },
)
ReviewTemplateLensReviewTypeDef = TypedDict(
    "ReviewTemplateLensReviewTypeDef",
    {
        "LensAlias": NotRequired[str],
        "LensArn": NotRequired[str],
        "LensVersion": NotRequired[str],
        "LensName": NotRequired[str],
        "LensStatus": NotRequired[LensStatusType],
        "PillarReviewSummaries": NotRequired[List[ReviewTemplatePillarReviewSummaryTypeDef]],
        "UpdatedAt": NotRequired[datetime],
        "Notes": NotRequired[str],
        "QuestionCounts": NotRequired[Dict[QuestionType, int]],
        "NextToken": NotRequired[str],
    },
)
UpdateShareInvitationOutputTypeDef = TypedDict(
    "UpdateShareInvitationOutputTypeDef",
    {
        "ShareInvitation": ShareInvitationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateWorkloadShareOutputTypeDef = TypedDict(
    "UpdateWorkloadShareOutputTypeDef",
    {
        "WorkloadId": str,
        "WorkloadShare": WorkloadShareTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ChoiceTypeDef = TypedDict(
    "ChoiceTypeDef",
    {
        "ChoiceId": NotRequired[str],
        "Title": NotRequired[str],
        "Description": NotRequired[str],
        "HelpfulResource": NotRequired[ChoiceContentTypeDef],
        "ImprovementPlan": NotRequired[ChoiceContentTypeDef],
        "AdditionalResources": NotRequired[List[AdditionalResourcesTypeDef]],
    },
)
PillarMetricTypeDef = TypedDict(
    "PillarMetricTypeDef",
    {
        "PillarId": NotRequired[str],
        "RiskCounts": NotRequired[Dict[RiskType, int]],
        "Questions": NotRequired[List[QuestionMetricTypeDef]],
    },
)
ListLensReviewImprovementsOutputTypeDef = TypedDict(
    "ListLensReviewImprovementsOutputTypeDef",
    {
        "WorkloadId": str,
        "MilestoneNumber": int,
        "LensAlias": str,
        "LensArn": str,
        "ImprovementSummaries": List[ImprovementSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListLensReviewsOutputTypeDef = TypedDict(
    "ListLensReviewsOutputTypeDef",
    {
        "WorkloadId": str,
        "MilestoneNumber": int,
        "LensReviewSummaries": List[LensReviewSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListWorkloadsOutputTypeDef = TypedDict(
    "ListWorkloadsOutputTypeDef",
    {
        "WorkloadSummaries": List[WorkloadSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
MilestoneSummaryTypeDef = TypedDict(
    "MilestoneSummaryTypeDef",
    {
        "MilestoneNumber": NotRequired[int],
        "MilestoneName": NotRequired[str],
        "RecordedAt": NotRequired[datetime],
        "WorkloadSummary": NotRequired[WorkloadSummaryTypeDef],
    },
)
GetWorkloadOutputTypeDef = TypedDict(
    "GetWorkloadOutputTypeDef",
    {
        "Workload": WorkloadTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
MilestoneTypeDef = TypedDict(
    "MilestoneTypeDef",
    {
        "MilestoneNumber": NotRequired[int],
        "MilestoneName": NotRequired[str],
        "RecordedAt": NotRequired[datetime],
        "Workload": NotRequired[WorkloadTypeDef],
    },
)
UpdateWorkloadOutputTypeDef = TypedDict(
    "UpdateWorkloadOutputTypeDef",
    {
        "Workload": WorkloadTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetLensReviewOutputTypeDef = TypedDict(
    "GetLensReviewOutputTypeDef",
    {
        "WorkloadId": str,
        "MilestoneNumber": int,
        "LensReview": LensReviewTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateLensReviewOutputTypeDef = TypedDict(
    "UpdateLensReviewOutputTypeDef",
    {
        "WorkloadId": str,
        "LensReview": LensReviewTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListNotificationsOutputTypeDef = TypedDict(
    "ListNotificationsOutputTypeDef",
    {
        "NotificationSummaries": List[NotificationSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
VersionDifferencesTypeDef = TypedDict(
    "VersionDifferencesTypeDef",
    {
        "PillarDifferences": NotRequired[List[PillarDifferenceTypeDef]],
    },
)
ProfileTypeDef = TypedDict(
    "ProfileTypeDef",
    {
        "ProfileArn": NotRequired[str],
        "ProfileVersion": NotRequired[str],
        "ProfileName": NotRequired[str],
        "ProfileDescription": NotRequired[str],
        "ProfileQuestions": NotRequired[List[ProfileQuestionTypeDef]],
        "Owner": NotRequired[str],
        "CreatedAt": NotRequired[datetime],
        "UpdatedAt": NotRequired[datetime],
        "ShareInvitationId": NotRequired[str],
        "Tags": NotRequired[Dict[str, str]],
    },
)
ProfileTemplateTypeDef = TypedDict(
    "ProfileTemplateTypeDef",
    {
        "TemplateName": NotRequired[str],
        "TemplateQuestions": NotRequired[List[ProfileTemplateQuestionTypeDef]],
        "CreatedAt": NotRequired[datetime],
        "UpdatedAt": NotRequired[datetime],
    },
)
GetReviewTemplateLensReviewOutputTypeDef = TypedDict(
    "GetReviewTemplateLensReviewOutputTypeDef",
    {
        "TemplateArn": str,
        "LensReview": ReviewTemplateLensReviewTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateReviewTemplateLensReviewOutputTypeDef = TypedDict(
    "UpdateReviewTemplateLensReviewOutputTypeDef",
    {
        "TemplateArn": str,
        "LensReview": ReviewTemplateLensReviewTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AnswerSummaryTypeDef = TypedDict(
    "AnswerSummaryTypeDef",
    {
        "QuestionId": NotRequired[str],
        "PillarId": NotRequired[str],
        "QuestionTitle": NotRequired[str],
        "Choices": NotRequired[List[ChoiceTypeDef]],
        "SelectedChoices": NotRequired[List[str]],
        "ChoiceAnswerSummaries": NotRequired[List[ChoiceAnswerSummaryTypeDef]],
        "IsApplicable": NotRequired[bool],
        "Risk": NotRequired[RiskType],
        "Reason": NotRequired[AnswerReasonType],
        "QuestionType": NotRequired[QuestionTypeType],
    },
)
AnswerTypeDef = TypedDict(
    "AnswerTypeDef",
    {
        "QuestionId": NotRequired[str],
        "PillarId": NotRequired[str],
        "QuestionTitle": NotRequired[str],
        "QuestionDescription": NotRequired[str],
        "ImprovementPlanUrl": NotRequired[str],
        "HelpfulResourceUrl": NotRequired[str],
        "HelpfulResourceDisplayText": NotRequired[str],
        "Choices": NotRequired[List[ChoiceTypeDef]],
        "SelectedChoices": NotRequired[List[str]],
        "ChoiceAnswers": NotRequired[List[ChoiceAnswerTypeDef]],
        "IsApplicable": NotRequired[bool],
        "Risk": NotRequired[RiskType],
        "Notes": NotRequired[str],
        "Reason": NotRequired[AnswerReasonType],
    },
)
ReviewTemplateAnswerSummaryTypeDef = TypedDict(
    "ReviewTemplateAnswerSummaryTypeDef",
    {
        "QuestionId": NotRequired[str],
        "PillarId": NotRequired[str],
        "QuestionTitle": NotRequired[str],
        "Choices": NotRequired[List[ChoiceTypeDef]],
        "SelectedChoices": NotRequired[List[str]],
        "ChoiceAnswerSummaries": NotRequired[List[ChoiceAnswerSummaryTypeDef]],
        "IsApplicable": NotRequired[bool],
        "AnswerStatus": NotRequired[ReviewTemplateAnswerStatusType],
        "Reason": NotRequired[AnswerReasonType],
        "QuestionType": NotRequired[QuestionTypeType],
    },
)
ReviewTemplateAnswerTypeDef = TypedDict(
    "ReviewTemplateAnswerTypeDef",
    {
        "QuestionId": NotRequired[str],
        "PillarId": NotRequired[str],
        "QuestionTitle": NotRequired[str],
        "QuestionDescription": NotRequired[str],
        "ImprovementPlanUrl": NotRequired[str],
        "HelpfulResourceUrl": NotRequired[str],
        "HelpfulResourceDisplayText": NotRequired[str],
        "Choices": NotRequired[List[ChoiceTypeDef]],
        "SelectedChoices": NotRequired[List[str]],
        "ChoiceAnswers": NotRequired[List[ChoiceAnswerTypeDef]],
        "IsApplicable": NotRequired[bool],
        "AnswerStatus": NotRequired[ReviewTemplateAnswerStatusType],
        "Notes": NotRequired[str],
        "Reason": NotRequired[AnswerReasonType],
    },
)
LensMetricTypeDef = TypedDict(
    "LensMetricTypeDef",
    {
        "LensArn": NotRequired[str],
        "Pillars": NotRequired[List[PillarMetricTypeDef]],
        "RiskCounts": NotRequired[Dict[RiskType, int]],
    },
)
ListMilestonesOutputTypeDef = TypedDict(
    "ListMilestonesOutputTypeDef",
    {
        "WorkloadId": str,
        "MilestoneSummaries": List[MilestoneSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetMilestoneOutputTypeDef = TypedDict(
    "GetMilestoneOutputTypeDef",
    {
        "WorkloadId": str,
        "Milestone": MilestoneTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetLensVersionDifferenceOutputTypeDef = TypedDict(
    "GetLensVersionDifferenceOutputTypeDef",
    {
        "LensAlias": str,
        "LensArn": str,
        "BaseLensVersion": str,
        "TargetLensVersion": str,
        "LatestLensVersion": str,
        "VersionDifferences": VersionDifferencesTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetProfileOutputTypeDef = TypedDict(
    "GetProfileOutputTypeDef",
    {
        "Profile": ProfileTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateProfileOutputTypeDef = TypedDict(
    "UpdateProfileOutputTypeDef",
    {
        "Profile": ProfileTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetProfileTemplateOutputTypeDef = TypedDict(
    "GetProfileTemplateOutputTypeDef",
    {
        "ProfileTemplate": ProfileTemplateTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAnswersOutputTypeDef = TypedDict(
    "ListAnswersOutputTypeDef",
    {
        "WorkloadId": str,
        "MilestoneNumber": int,
        "LensAlias": str,
        "LensArn": str,
        "AnswerSummaries": List[AnswerSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAnswerOutputTypeDef = TypedDict(
    "GetAnswerOutputTypeDef",
    {
        "WorkloadId": str,
        "MilestoneNumber": int,
        "LensAlias": str,
        "LensArn": str,
        "Answer": AnswerTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateAnswerOutputTypeDef = TypedDict(
    "UpdateAnswerOutputTypeDef",
    {
        "WorkloadId": str,
        "LensAlias": str,
        "LensArn": str,
        "Answer": AnswerTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListReviewTemplateAnswersOutputTypeDef = TypedDict(
    "ListReviewTemplateAnswersOutputTypeDef",
    {
        "TemplateArn": str,
        "LensAlias": str,
        "AnswerSummaries": List[ReviewTemplateAnswerSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetReviewTemplateAnswerOutputTypeDef = TypedDict(
    "GetReviewTemplateAnswerOutputTypeDef",
    {
        "TemplateArn": str,
        "LensAlias": str,
        "Answer": ReviewTemplateAnswerTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateReviewTemplateAnswerOutputTypeDef = TypedDict(
    "UpdateReviewTemplateAnswerOutputTypeDef",
    {
        "TemplateArn": str,
        "LensAlias": str,
        "Answer": ReviewTemplateAnswerTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ConsolidatedReportMetricTypeDef = TypedDict(
    "ConsolidatedReportMetricTypeDef",
    {
        "MetricType": NotRequired[Literal["WORKLOAD"]],
        "RiskCounts": NotRequired[Dict[RiskType, int]],
        "WorkloadId": NotRequired[str],
        "WorkloadName": NotRequired[str],
        "WorkloadArn": NotRequired[str],
        "UpdatedAt": NotRequired[datetime],
        "Lenses": NotRequired[List[LensMetricTypeDef]],
        "LensesAppliedCount": NotRequired[int],
    },
)
GetConsolidatedReportOutputTypeDef = TypedDict(
    "GetConsolidatedReportOutputTypeDef",
    {
        "Metrics": List[ConsolidatedReportMetricTypeDef],
        "NextToken": str,
        "Base64String": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
