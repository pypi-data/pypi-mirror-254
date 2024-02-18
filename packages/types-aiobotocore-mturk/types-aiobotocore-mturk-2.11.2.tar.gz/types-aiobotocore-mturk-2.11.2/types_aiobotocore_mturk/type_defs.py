"""
Type annotations for mturk service type definitions.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mturk/type_defs/)

Usage::

    ```python
    from types_aiobotocore_mturk.type_defs import AcceptQualificationRequestRequestRequestTypeDef

    data: AcceptQualificationRequestRequestRequestTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Sequence, Union

from .literals import (
    AssignmentStatusType,
    ComparatorType,
    EventTypeType,
    HITAccessActionsType,
    HITReviewStatusType,
    HITStatusType,
    NotificationTransportType,
    NotifyWorkersFailureCodeType,
    QualificationStatusType,
    QualificationTypeStatusType,
    ReviewableHITStatusType,
    ReviewActionStatusType,
    ReviewPolicyLevelType,
)

if sys.version_info >= (3, 12):
    from typing import NotRequired
else:
    from typing_extensions import NotRequired
if sys.version_info >= (3, 12):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AcceptQualificationRequestRequestRequestTypeDef",
    "ApproveAssignmentRequestRequestTypeDef",
    "AssignmentTypeDef",
    "AssociateQualificationWithWorkerRequestRequestTypeDef",
    "BonusPaymentTypeDef",
    "CreateAdditionalAssignmentsForHITRequestRequestTypeDef",
    "HITLayoutParameterTypeDef",
    "ResponseMetadataTypeDef",
    "CreateQualificationTypeRequestRequestTypeDef",
    "QualificationTypeTypeDef",
    "CreateWorkerBlockRequestRequestTypeDef",
    "DeleteHITRequestRequestTypeDef",
    "DeleteQualificationTypeRequestRequestTypeDef",
    "DeleteWorkerBlockRequestRequestTypeDef",
    "DisassociateQualificationFromWorkerRequestRequestTypeDef",
    "GetAssignmentRequestRequestTypeDef",
    "GetFileUploadURLRequestRequestTypeDef",
    "GetHITRequestRequestTypeDef",
    "GetQualificationScoreRequestRequestTypeDef",
    "GetQualificationTypeRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "ListAssignmentsForHITRequestRequestTypeDef",
    "ListBonusPaymentsRequestRequestTypeDef",
    "ListHITsForQualificationTypeRequestRequestTypeDef",
    "ListHITsRequestRequestTypeDef",
    "ListQualificationRequestsRequestRequestTypeDef",
    "QualificationRequestTypeDef",
    "ListQualificationTypesRequestRequestTypeDef",
    "ListReviewPolicyResultsForHITRequestRequestTypeDef",
    "ListReviewableHITsRequestRequestTypeDef",
    "ListWorkerBlocksRequestRequestTypeDef",
    "WorkerBlockTypeDef",
    "ListWorkersWithQualificationTypeRequestRequestTypeDef",
    "LocaleTypeDef",
    "NotificationSpecificationTypeDef",
    "NotifyWorkersFailureStatusTypeDef",
    "NotifyWorkersRequestRequestTypeDef",
    "ParameterMapEntryTypeDef",
    "RejectAssignmentRequestRequestTypeDef",
    "RejectQualificationRequestRequestRequestTypeDef",
    "ReviewActionDetailTypeDef",
    "ReviewResultDetailTypeDef",
    "SendBonusRequestRequestTypeDef",
    "TimestampTypeDef",
    "UpdateHITReviewStatusRequestRequestTypeDef",
    "UpdateHITTypeOfHITRequestRequestTypeDef",
    "UpdateQualificationTypeRequestRequestTypeDef",
    "CreateHITTypeResponseTypeDef",
    "GetAccountBalanceResponseTypeDef",
    "GetFileUploadURLResponseTypeDef",
    "ListAssignmentsForHITResponseTypeDef",
    "ListBonusPaymentsResponseTypeDef",
    "CreateQualificationTypeResponseTypeDef",
    "GetQualificationTypeResponseTypeDef",
    "ListQualificationTypesResponseTypeDef",
    "UpdateQualificationTypeResponseTypeDef",
    "ListAssignmentsForHITRequestListAssignmentsForHITPaginateTypeDef",
    "ListBonusPaymentsRequestListBonusPaymentsPaginateTypeDef",
    "ListHITsForQualificationTypeRequestListHITsForQualificationTypePaginateTypeDef",
    "ListHITsRequestListHITsPaginateTypeDef",
    "ListQualificationRequestsRequestListQualificationRequestsPaginateTypeDef",
    "ListQualificationTypesRequestListQualificationTypesPaginateTypeDef",
    "ListReviewableHITsRequestListReviewableHITsPaginateTypeDef",
    "ListWorkerBlocksRequestListWorkerBlocksPaginateTypeDef",
    "ListWorkersWithQualificationTypeRequestListWorkersWithQualificationTypePaginateTypeDef",
    "ListQualificationRequestsResponseTypeDef",
    "ListWorkerBlocksResponseTypeDef",
    "QualificationRequirementPaginatorTypeDef",
    "QualificationRequirementTypeDef",
    "QualificationTypeDef",
    "SendTestEventNotificationRequestRequestTypeDef",
    "UpdateNotificationSettingsRequestRequestTypeDef",
    "NotifyWorkersResponseTypeDef",
    "PolicyParameterTypeDef",
    "ReviewReportTypeDef",
    "UpdateExpirationForHITRequestRequestTypeDef",
    "HITPaginatorTypeDef",
    "CreateHITTypeRequestRequestTypeDef",
    "HITTypeDef",
    "GetQualificationScoreResponseTypeDef",
    "ListWorkersWithQualificationTypeResponseTypeDef",
    "ReviewPolicyTypeDef",
    "ListHITsForQualificationTypeResponsePaginatorTypeDef",
    "ListHITsResponsePaginatorTypeDef",
    "ListReviewableHITsResponsePaginatorTypeDef",
    "CreateHITResponseTypeDef",
    "CreateHITWithHITTypeResponseTypeDef",
    "GetAssignmentResponseTypeDef",
    "GetHITResponseTypeDef",
    "ListHITsForQualificationTypeResponseTypeDef",
    "ListHITsResponseTypeDef",
    "ListReviewableHITsResponseTypeDef",
    "CreateHITRequestRequestTypeDef",
    "CreateHITWithHITTypeRequestRequestTypeDef",
    "ListReviewPolicyResultsForHITResponseTypeDef",
)

AcceptQualificationRequestRequestRequestTypeDef = TypedDict(
    "AcceptQualificationRequestRequestRequestTypeDef",
    {
        "QualificationRequestId": str,
        "IntegerValue": NotRequired[int],
    },
)
ApproveAssignmentRequestRequestTypeDef = TypedDict(
    "ApproveAssignmentRequestRequestTypeDef",
    {
        "AssignmentId": str,
        "RequesterFeedback": NotRequired[str],
        "OverrideRejection": NotRequired[bool],
    },
)
AssignmentTypeDef = TypedDict(
    "AssignmentTypeDef",
    {
        "AssignmentId": NotRequired[str],
        "WorkerId": NotRequired[str],
        "HITId": NotRequired[str],
        "AssignmentStatus": NotRequired[AssignmentStatusType],
        "AutoApprovalTime": NotRequired[datetime],
        "AcceptTime": NotRequired[datetime],
        "SubmitTime": NotRequired[datetime],
        "ApprovalTime": NotRequired[datetime],
        "RejectionTime": NotRequired[datetime],
        "Deadline": NotRequired[datetime],
        "Answer": NotRequired[str],
        "RequesterFeedback": NotRequired[str],
    },
)
AssociateQualificationWithWorkerRequestRequestTypeDef = TypedDict(
    "AssociateQualificationWithWorkerRequestRequestTypeDef",
    {
        "QualificationTypeId": str,
        "WorkerId": str,
        "IntegerValue": NotRequired[int],
        "SendNotification": NotRequired[bool],
    },
)
BonusPaymentTypeDef = TypedDict(
    "BonusPaymentTypeDef",
    {
        "WorkerId": NotRequired[str],
        "BonusAmount": NotRequired[str],
        "AssignmentId": NotRequired[str],
        "Reason": NotRequired[str],
        "GrantTime": NotRequired[datetime],
    },
)
CreateAdditionalAssignmentsForHITRequestRequestTypeDef = TypedDict(
    "CreateAdditionalAssignmentsForHITRequestRequestTypeDef",
    {
        "HITId": str,
        "NumberOfAdditionalAssignments": int,
        "UniqueRequestToken": NotRequired[str],
    },
)
HITLayoutParameterTypeDef = TypedDict(
    "HITLayoutParameterTypeDef",
    {
        "Name": str,
        "Value": str,
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
CreateQualificationTypeRequestRequestTypeDef = TypedDict(
    "CreateQualificationTypeRequestRequestTypeDef",
    {
        "Name": str,
        "Description": str,
        "QualificationTypeStatus": QualificationTypeStatusType,
        "Keywords": NotRequired[str],
        "RetryDelayInSeconds": NotRequired[int],
        "Test": NotRequired[str],
        "AnswerKey": NotRequired[str],
        "TestDurationInSeconds": NotRequired[int],
        "AutoGranted": NotRequired[bool],
        "AutoGrantedValue": NotRequired[int],
    },
)
QualificationTypeTypeDef = TypedDict(
    "QualificationTypeTypeDef",
    {
        "QualificationTypeId": NotRequired[str],
        "CreationTime": NotRequired[datetime],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "Keywords": NotRequired[str],
        "QualificationTypeStatus": NotRequired[QualificationTypeStatusType],
        "Test": NotRequired[str],
        "TestDurationInSeconds": NotRequired[int],
        "AnswerKey": NotRequired[str],
        "RetryDelayInSeconds": NotRequired[int],
        "IsRequestable": NotRequired[bool],
        "AutoGranted": NotRequired[bool],
        "AutoGrantedValue": NotRequired[int],
    },
)
CreateWorkerBlockRequestRequestTypeDef = TypedDict(
    "CreateWorkerBlockRequestRequestTypeDef",
    {
        "WorkerId": str,
        "Reason": str,
    },
)
DeleteHITRequestRequestTypeDef = TypedDict(
    "DeleteHITRequestRequestTypeDef",
    {
        "HITId": str,
    },
)
DeleteQualificationTypeRequestRequestTypeDef = TypedDict(
    "DeleteQualificationTypeRequestRequestTypeDef",
    {
        "QualificationTypeId": str,
    },
)
DeleteWorkerBlockRequestRequestTypeDef = TypedDict(
    "DeleteWorkerBlockRequestRequestTypeDef",
    {
        "WorkerId": str,
        "Reason": NotRequired[str],
    },
)
DisassociateQualificationFromWorkerRequestRequestTypeDef = TypedDict(
    "DisassociateQualificationFromWorkerRequestRequestTypeDef",
    {
        "WorkerId": str,
        "QualificationTypeId": str,
        "Reason": NotRequired[str],
    },
)
GetAssignmentRequestRequestTypeDef = TypedDict(
    "GetAssignmentRequestRequestTypeDef",
    {
        "AssignmentId": str,
    },
)
GetFileUploadURLRequestRequestTypeDef = TypedDict(
    "GetFileUploadURLRequestRequestTypeDef",
    {
        "AssignmentId": str,
        "QuestionIdentifier": str,
    },
)
GetHITRequestRequestTypeDef = TypedDict(
    "GetHITRequestRequestTypeDef",
    {
        "HITId": str,
    },
)
GetQualificationScoreRequestRequestTypeDef = TypedDict(
    "GetQualificationScoreRequestRequestTypeDef",
    {
        "QualificationTypeId": str,
        "WorkerId": str,
    },
)
GetQualificationTypeRequestRequestTypeDef = TypedDict(
    "GetQualificationTypeRequestRequestTypeDef",
    {
        "QualificationTypeId": str,
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
ListAssignmentsForHITRequestRequestTypeDef = TypedDict(
    "ListAssignmentsForHITRequestRequestTypeDef",
    {
        "HITId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "AssignmentStatuses": NotRequired[Sequence[AssignmentStatusType]],
    },
)
ListBonusPaymentsRequestRequestTypeDef = TypedDict(
    "ListBonusPaymentsRequestRequestTypeDef",
    {
        "HITId": NotRequired[str],
        "AssignmentId": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListHITsForQualificationTypeRequestRequestTypeDef = TypedDict(
    "ListHITsForQualificationTypeRequestRequestTypeDef",
    {
        "QualificationTypeId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListHITsRequestRequestTypeDef = TypedDict(
    "ListHITsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListQualificationRequestsRequestRequestTypeDef = TypedDict(
    "ListQualificationRequestsRequestRequestTypeDef",
    {
        "QualificationTypeId": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
QualificationRequestTypeDef = TypedDict(
    "QualificationRequestTypeDef",
    {
        "QualificationRequestId": NotRequired[str],
        "QualificationTypeId": NotRequired[str],
        "WorkerId": NotRequired[str],
        "Test": NotRequired[str],
        "Answer": NotRequired[str],
        "SubmitTime": NotRequired[datetime],
    },
)
ListQualificationTypesRequestRequestTypeDef = TypedDict(
    "ListQualificationTypesRequestRequestTypeDef",
    {
        "MustBeRequestable": bool,
        "Query": NotRequired[str],
        "MustBeOwnedByCaller": NotRequired[bool],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListReviewPolicyResultsForHITRequestRequestTypeDef = TypedDict(
    "ListReviewPolicyResultsForHITRequestRequestTypeDef",
    {
        "HITId": str,
        "PolicyLevels": NotRequired[Sequence[ReviewPolicyLevelType]],
        "RetrieveActions": NotRequired[bool],
        "RetrieveResults": NotRequired[bool],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListReviewableHITsRequestRequestTypeDef = TypedDict(
    "ListReviewableHITsRequestRequestTypeDef",
    {
        "HITTypeId": NotRequired[str],
        "Status": NotRequired[ReviewableHITStatusType],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListWorkerBlocksRequestRequestTypeDef = TypedDict(
    "ListWorkerBlocksRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
WorkerBlockTypeDef = TypedDict(
    "WorkerBlockTypeDef",
    {
        "WorkerId": NotRequired[str],
        "Reason": NotRequired[str],
    },
)
ListWorkersWithQualificationTypeRequestRequestTypeDef = TypedDict(
    "ListWorkersWithQualificationTypeRequestRequestTypeDef",
    {
        "QualificationTypeId": str,
        "Status": NotRequired[QualificationStatusType],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
LocaleTypeDef = TypedDict(
    "LocaleTypeDef",
    {
        "Country": str,
        "Subdivision": NotRequired[str],
    },
)
NotificationSpecificationTypeDef = TypedDict(
    "NotificationSpecificationTypeDef",
    {
        "Destination": str,
        "Transport": NotificationTransportType,
        "Version": str,
        "EventTypes": Sequence[EventTypeType],
    },
)
NotifyWorkersFailureStatusTypeDef = TypedDict(
    "NotifyWorkersFailureStatusTypeDef",
    {
        "NotifyWorkersFailureCode": NotRequired[NotifyWorkersFailureCodeType],
        "NotifyWorkersFailureMessage": NotRequired[str],
        "WorkerId": NotRequired[str],
    },
)
NotifyWorkersRequestRequestTypeDef = TypedDict(
    "NotifyWorkersRequestRequestTypeDef",
    {
        "Subject": str,
        "MessageText": str,
        "WorkerIds": Sequence[str],
    },
)
ParameterMapEntryTypeDef = TypedDict(
    "ParameterMapEntryTypeDef",
    {
        "Key": NotRequired[str],
        "Values": NotRequired[Sequence[str]],
    },
)
RejectAssignmentRequestRequestTypeDef = TypedDict(
    "RejectAssignmentRequestRequestTypeDef",
    {
        "AssignmentId": str,
        "RequesterFeedback": str,
    },
)
RejectQualificationRequestRequestRequestTypeDef = TypedDict(
    "RejectQualificationRequestRequestRequestTypeDef",
    {
        "QualificationRequestId": str,
        "Reason": NotRequired[str],
    },
)
ReviewActionDetailTypeDef = TypedDict(
    "ReviewActionDetailTypeDef",
    {
        "ActionId": NotRequired[str],
        "ActionName": NotRequired[str],
        "TargetId": NotRequired[str],
        "TargetType": NotRequired[str],
        "Status": NotRequired[ReviewActionStatusType],
        "CompleteTime": NotRequired[datetime],
        "Result": NotRequired[str],
        "ErrorCode": NotRequired[str],
    },
)
ReviewResultDetailTypeDef = TypedDict(
    "ReviewResultDetailTypeDef",
    {
        "ActionId": NotRequired[str],
        "SubjectId": NotRequired[str],
        "SubjectType": NotRequired[str],
        "QuestionId": NotRequired[str],
        "Key": NotRequired[str],
        "Value": NotRequired[str],
    },
)
SendBonusRequestRequestTypeDef = TypedDict(
    "SendBonusRequestRequestTypeDef",
    {
        "WorkerId": str,
        "BonusAmount": str,
        "AssignmentId": str,
        "Reason": str,
        "UniqueRequestToken": NotRequired[str],
    },
)
TimestampTypeDef = Union[datetime, str]
UpdateHITReviewStatusRequestRequestTypeDef = TypedDict(
    "UpdateHITReviewStatusRequestRequestTypeDef",
    {
        "HITId": str,
        "Revert": NotRequired[bool],
    },
)
UpdateHITTypeOfHITRequestRequestTypeDef = TypedDict(
    "UpdateHITTypeOfHITRequestRequestTypeDef",
    {
        "HITId": str,
        "HITTypeId": str,
    },
)
UpdateQualificationTypeRequestRequestTypeDef = TypedDict(
    "UpdateQualificationTypeRequestRequestTypeDef",
    {
        "QualificationTypeId": str,
        "Description": NotRequired[str],
        "QualificationTypeStatus": NotRequired[QualificationTypeStatusType],
        "Test": NotRequired[str],
        "AnswerKey": NotRequired[str],
        "TestDurationInSeconds": NotRequired[int],
        "RetryDelayInSeconds": NotRequired[int],
        "AutoGranted": NotRequired[bool],
        "AutoGrantedValue": NotRequired[int],
    },
)
CreateHITTypeResponseTypeDef = TypedDict(
    "CreateHITTypeResponseTypeDef",
    {
        "HITTypeId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAccountBalanceResponseTypeDef = TypedDict(
    "GetAccountBalanceResponseTypeDef",
    {
        "AvailableBalance": str,
        "OnHoldBalance": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetFileUploadURLResponseTypeDef = TypedDict(
    "GetFileUploadURLResponseTypeDef",
    {
        "FileUploadURL": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAssignmentsForHITResponseTypeDef = TypedDict(
    "ListAssignmentsForHITResponseTypeDef",
    {
        "NextToken": str,
        "NumResults": int,
        "Assignments": List[AssignmentTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListBonusPaymentsResponseTypeDef = TypedDict(
    "ListBonusPaymentsResponseTypeDef",
    {
        "NumResults": int,
        "NextToken": str,
        "BonusPayments": List[BonusPaymentTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateQualificationTypeResponseTypeDef = TypedDict(
    "CreateQualificationTypeResponseTypeDef",
    {
        "QualificationType": QualificationTypeTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetQualificationTypeResponseTypeDef = TypedDict(
    "GetQualificationTypeResponseTypeDef",
    {
        "QualificationType": QualificationTypeTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListQualificationTypesResponseTypeDef = TypedDict(
    "ListQualificationTypesResponseTypeDef",
    {
        "NumResults": int,
        "NextToken": str,
        "QualificationTypes": List[QualificationTypeTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateQualificationTypeResponseTypeDef = TypedDict(
    "UpdateQualificationTypeResponseTypeDef",
    {
        "QualificationType": QualificationTypeTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAssignmentsForHITRequestListAssignmentsForHITPaginateTypeDef = TypedDict(
    "ListAssignmentsForHITRequestListAssignmentsForHITPaginateTypeDef",
    {
        "HITId": str,
        "AssignmentStatuses": NotRequired[Sequence[AssignmentStatusType]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListBonusPaymentsRequestListBonusPaymentsPaginateTypeDef = TypedDict(
    "ListBonusPaymentsRequestListBonusPaymentsPaginateTypeDef",
    {
        "HITId": NotRequired[str],
        "AssignmentId": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListHITsForQualificationTypeRequestListHITsForQualificationTypePaginateTypeDef = TypedDict(
    "ListHITsForQualificationTypeRequestListHITsForQualificationTypePaginateTypeDef",
    {
        "QualificationTypeId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListHITsRequestListHITsPaginateTypeDef = TypedDict(
    "ListHITsRequestListHITsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListQualificationRequestsRequestListQualificationRequestsPaginateTypeDef = TypedDict(
    "ListQualificationRequestsRequestListQualificationRequestsPaginateTypeDef",
    {
        "QualificationTypeId": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListQualificationTypesRequestListQualificationTypesPaginateTypeDef = TypedDict(
    "ListQualificationTypesRequestListQualificationTypesPaginateTypeDef",
    {
        "MustBeRequestable": bool,
        "Query": NotRequired[str],
        "MustBeOwnedByCaller": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListReviewableHITsRequestListReviewableHITsPaginateTypeDef = TypedDict(
    "ListReviewableHITsRequestListReviewableHITsPaginateTypeDef",
    {
        "HITTypeId": NotRequired[str],
        "Status": NotRequired[ReviewableHITStatusType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListWorkerBlocksRequestListWorkerBlocksPaginateTypeDef = TypedDict(
    "ListWorkerBlocksRequestListWorkerBlocksPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListWorkersWithQualificationTypeRequestListWorkersWithQualificationTypePaginateTypeDef = TypedDict(
    "ListWorkersWithQualificationTypeRequestListWorkersWithQualificationTypePaginateTypeDef",
    {
        "QualificationTypeId": str,
        "Status": NotRequired[QualificationStatusType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListQualificationRequestsResponseTypeDef = TypedDict(
    "ListQualificationRequestsResponseTypeDef",
    {
        "NumResults": int,
        "NextToken": str,
        "QualificationRequests": List[QualificationRequestTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListWorkerBlocksResponseTypeDef = TypedDict(
    "ListWorkerBlocksResponseTypeDef",
    {
        "NextToken": str,
        "NumResults": int,
        "WorkerBlocks": List[WorkerBlockTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
QualificationRequirementPaginatorTypeDef = TypedDict(
    "QualificationRequirementPaginatorTypeDef",
    {
        "QualificationTypeId": str,
        "Comparator": ComparatorType,
        "IntegerValues": NotRequired[List[int]],
        "LocaleValues": NotRequired[List[LocaleTypeDef]],
        "RequiredToPreview": NotRequired[bool],
        "ActionsGuarded": NotRequired[HITAccessActionsType],
    },
)
QualificationRequirementTypeDef = TypedDict(
    "QualificationRequirementTypeDef",
    {
        "QualificationTypeId": str,
        "Comparator": ComparatorType,
        "IntegerValues": NotRequired[Sequence[int]],
        "LocaleValues": NotRequired[Sequence[LocaleTypeDef]],
        "RequiredToPreview": NotRequired[bool],
        "ActionsGuarded": NotRequired[HITAccessActionsType],
    },
)
QualificationTypeDef = TypedDict(
    "QualificationTypeDef",
    {
        "QualificationTypeId": NotRequired[str],
        "WorkerId": NotRequired[str],
        "GrantTime": NotRequired[datetime],
        "IntegerValue": NotRequired[int],
        "LocaleValue": NotRequired[LocaleTypeDef],
        "Status": NotRequired[QualificationStatusType],
    },
)
SendTestEventNotificationRequestRequestTypeDef = TypedDict(
    "SendTestEventNotificationRequestRequestTypeDef",
    {
        "Notification": NotificationSpecificationTypeDef,
        "TestEventType": EventTypeType,
    },
)
UpdateNotificationSettingsRequestRequestTypeDef = TypedDict(
    "UpdateNotificationSettingsRequestRequestTypeDef",
    {
        "HITTypeId": str,
        "Notification": NotRequired[NotificationSpecificationTypeDef],
        "Active": NotRequired[bool],
    },
)
NotifyWorkersResponseTypeDef = TypedDict(
    "NotifyWorkersResponseTypeDef",
    {
        "NotifyWorkersFailureStatuses": List[NotifyWorkersFailureStatusTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PolicyParameterTypeDef = TypedDict(
    "PolicyParameterTypeDef",
    {
        "Key": NotRequired[str],
        "Values": NotRequired[Sequence[str]],
        "MapEntries": NotRequired[Sequence[ParameterMapEntryTypeDef]],
    },
)
ReviewReportTypeDef = TypedDict(
    "ReviewReportTypeDef",
    {
        "ReviewResults": NotRequired[List[ReviewResultDetailTypeDef]],
        "ReviewActions": NotRequired[List[ReviewActionDetailTypeDef]],
    },
)
UpdateExpirationForHITRequestRequestTypeDef = TypedDict(
    "UpdateExpirationForHITRequestRequestTypeDef",
    {
        "HITId": str,
        "ExpireAt": TimestampTypeDef,
    },
)
HITPaginatorTypeDef = TypedDict(
    "HITPaginatorTypeDef",
    {
        "HITId": NotRequired[str],
        "HITTypeId": NotRequired[str],
        "HITGroupId": NotRequired[str],
        "HITLayoutId": NotRequired[str],
        "CreationTime": NotRequired[datetime],
        "Title": NotRequired[str],
        "Description": NotRequired[str],
        "Question": NotRequired[str],
        "Keywords": NotRequired[str],
        "HITStatus": NotRequired[HITStatusType],
        "MaxAssignments": NotRequired[int],
        "Reward": NotRequired[str],
        "AutoApprovalDelayInSeconds": NotRequired[int],
        "Expiration": NotRequired[datetime],
        "AssignmentDurationInSeconds": NotRequired[int],
        "RequesterAnnotation": NotRequired[str],
        "QualificationRequirements": NotRequired[List[QualificationRequirementPaginatorTypeDef]],
        "HITReviewStatus": NotRequired[HITReviewStatusType],
        "NumberOfAssignmentsPending": NotRequired[int],
        "NumberOfAssignmentsAvailable": NotRequired[int],
        "NumberOfAssignmentsCompleted": NotRequired[int],
    },
)
CreateHITTypeRequestRequestTypeDef = TypedDict(
    "CreateHITTypeRequestRequestTypeDef",
    {
        "AssignmentDurationInSeconds": int,
        "Reward": str,
        "Title": str,
        "Description": str,
        "AutoApprovalDelayInSeconds": NotRequired[int],
        "Keywords": NotRequired[str],
        "QualificationRequirements": NotRequired[Sequence[QualificationRequirementTypeDef]],
    },
)
HITTypeDef = TypedDict(
    "HITTypeDef",
    {
        "HITId": NotRequired[str],
        "HITTypeId": NotRequired[str],
        "HITGroupId": NotRequired[str],
        "HITLayoutId": NotRequired[str],
        "CreationTime": NotRequired[datetime],
        "Title": NotRequired[str],
        "Description": NotRequired[str],
        "Question": NotRequired[str],
        "Keywords": NotRequired[str],
        "HITStatus": NotRequired[HITStatusType],
        "MaxAssignments": NotRequired[int],
        "Reward": NotRequired[str],
        "AutoApprovalDelayInSeconds": NotRequired[int],
        "Expiration": NotRequired[datetime],
        "AssignmentDurationInSeconds": NotRequired[int],
        "RequesterAnnotation": NotRequired[str],
        "QualificationRequirements": NotRequired[List[QualificationRequirementTypeDef]],
        "HITReviewStatus": NotRequired[HITReviewStatusType],
        "NumberOfAssignmentsPending": NotRequired[int],
        "NumberOfAssignmentsAvailable": NotRequired[int],
        "NumberOfAssignmentsCompleted": NotRequired[int],
    },
)
GetQualificationScoreResponseTypeDef = TypedDict(
    "GetQualificationScoreResponseTypeDef",
    {
        "Qualification": QualificationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListWorkersWithQualificationTypeResponseTypeDef = TypedDict(
    "ListWorkersWithQualificationTypeResponseTypeDef",
    {
        "NextToken": str,
        "NumResults": int,
        "Qualifications": List[QualificationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ReviewPolicyTypeDef = TypedDict(
    "ReviewPolicyTypeDef",
    {
        "PolicyName": str,
        "Parameters": NotRequired[Sequence[PolicyParameterTypeDef]],
    },
)
ListHITsForQualificationTypeResponsePaginatorTypeDef = TypedDict(
    "ListHITsForQualificationTypeResponsePaginatorTypeDef",
    {
        "NextToken": str,
        "NumResults": int,
        "HITs": List[HITPaginatorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListHITsResponsePaginatorTypeDef = TypedDict(
    "ListHITsResponsePaginatorTypeDef",
    {
        "NextToken": str,
        "NumResults": int,
        "HITs": List[HITPaginatorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListReviewableHITsResponsePaginatorTypeDef = TypedDict(
    "ListReviewableHITsResponsePaginatorTypeDef",
    {
        "NextToken": str,
        "NumResults": int,
        "HITs": List[HITPaginatorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateHITResponseTypeDef = TypedDict(
    "CreateHITResponseTypeDef",
    {
        "HIT": HITTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateHITWithHITTypeResponseTypeDef = TypedDict(
    "CreateHITWithHITTypeResponseTypeDef",
    {
        "HIT": HITTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAssignmentResponseTypeDef = TypedDict(
    "GetAssignmentResponseTypeDef",
    {
        "Assignment": AssignmentTypeDef,
        "HIT": HITTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetHITResponseTypeDef = TypedDict(
    "GetHITResponseTypeDef",
    {
        "HIT": HITTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListHITsForQualificationTypeResponseTypeDef = TypedDict(
    "ListHITsForQualificationTypeResponseTypeDef",
    {
        "NextToken": str,
        "NumResults": int,
        "HITs": List[HITTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListHITsResponseTypeDef = TypedDict(
    "ListHITsResponseTypeDef",
    {
        "NextToken": str,
        "NumResults": int,
        "HITs": List[HITTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListReviewableHITsResponseTypeDef = TypedDict(
    "ListReviewableHITsResponseTypeDef",
    {
        "NextToken": str,
        "NumResults": int,
        "HITs": List[HITTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateHITRequestRequestTypeDef = TypedDict(
    "CreateHITRequestRequestTypeDef",
    {
        "LifetimeInSeconds": int,
        "AssignmentDurationInSeconds": int,
        "Reward": str,
        "Title": str,
        "Description": str,
        "MaxAssignments": NotRequired[int],
        "AutoApprovalDelayInSeconds": NotRequired[int],
        "Keywords": NotRequired[str],
        "Question": NotRequired[str],
        "RequesterAnnotation": NotRequired[str],
        "QualificationRequirements": NotRequired[Sequence[QualificationRequirementTypeDef]],
        "UniqueRequestToken": NotRequired[str],
        "AssignmentReviewPolicy": NotRequired[ReviewPolicyTypeDef],
        "HITReviewPolicy": NotRequired[ReviewPolicyTypeDef],
        "HITLayoutId": NotRequired[str],
        "HITLayoutParameters": NotRequired[Sequence[HITLayoutParameterTypeDef]],
    },
)
CreateHITWithHITTypeRequestRequestTypeDef = TypedDict(
    "CreateHITWithHITTypeRequestRequestTypeDef",
    {
        "HITTypeId": str,
        "LifetimeInSeconds": int,
        "MaxAssignments": NotRequired[int],
        "Question": NotRequired[str],
        "RequesterAnnotation": NotRequired[str],
        "UniqueRequestToken": NotRequired[str],
        "AssignmentReviewPolicy": NotRequired[ReviewPolicyTypeDef],
        "HITReviewPolicy": NotRequired[ReviewPolicyTypeDef],
        "HITLayoutId": NotRequired[str],
        "HITLayoutParameters": NotRequired[Sequence[HITLayoutParameterTypeDef]],
    },
)
ListReviewPolicyResultsForHITResponseTypeDef = TypedDict(
    "ListReviewPolicyResultsForHITResponseTypeDef",
    {
        "HITId": str,
        "AssignmentReviewPolicy": ReviewPolicyTypeDef,
        "HITReviewPolicy": ReviewPolicyTypeDef,
        "AssignmentReviewReport": ReviewReportTypeDef,
        "HITReviewReport": ReviewReportTypeDef,
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
