"""
Type annotations for budgets service type definitions.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_budgets/type_defs/)

Usage::

    ```python
    from types_aiobotocore_budgets.type_defs import ActionThresholdTypeDef

    data: ActionThresholdTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from .literals import (
    ActionStatusType,
    ActionSubTypeType,
    ActionTypeType,
    ApprovalModelType,
    AutoAdjustTypeType,
    BudgetTypeType,
    ComparisonOperatorType,
    EventTypeType,
    ExecutionTypeType,
    NotificationStateType,
    NotificationTypeType,
    SubscriptionTypeType,
    ThresholdTypeType,
    TimeUnitType,
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
    "ActionThresholdTypeDef",
    "SubscriberTypeDef",
    "HistoricalOptionsTypeDef",
    "TimestampTypeDef",
    "NotificationTypeDef",
    "CostTypesTypeDef",
    "SpendTypeDef",
    "ResponseMetadataTypeDef",
    "IamActionDefinitionPaginatorTypeDef",
    "ScpActionDefinitionPaginatorTypeDef",
    "SsmActionDefinitionPaginatorTypeDef",
    "IamActionDefinitionTypeDef",
    "ScpActionDefinitionTypeDef",
    "SsmActionDefinitionTypeDef",
    "DeleteBudgetActionRequestRequestTypeDef",
    "DeleteBudgetRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "DescribeBudgetActionRequestRequestTypeDef",
    "DescribeBudgetActionsForAccountRequestRequestTypeDef",
    "DescribeBudgetActionsForBudgetRequestRequestTypeDef",
    "DescribeBudgetNotificationsForAccountRequestRequestTypeDef",
    "DescribeBudgetRequestRequestTypeDef",
    "DescribeBudgetsRequestRequestTypeDef",
    "DescribeNotificationsForBudgetRequestRequestTypeDef",
    "ExecuteBudgetActionRequestRequestTypeDef",
    "AutoAdjustDataPaginatorTypeDef",
    "AutoAdjustDataTypeDef",
    "TimePeriodTypeDef",
    "BudgetNotificationsForAccountTypeDef",
    "CreateNotificationRequestRequestTypeDef",
    "CreateSubscriberRequestRequestTypeDef",
    "DeleteNotificationRequestRequestTypeDef",
    "DeleteSubscriberRequestRequestTypeDef",
    "DescribeSubscribersForNotificationRequestRequestTypeDef",
    "NotificationWithSubscribersTypeDef",
    "UpdateNotificationRequestRequestTypeDef",
    "UpdateSubscriberRequestRequestTypeDef",
    "CalculatedSpendTypeDef",
    "CreateBudgetActionResponseTypeDef",
    "DescribeNotificationsForBudgetResponseTypeDef",
    "DescribeSubscribersForNotificationResponseTypeDef",
    "ExecuteBudgetActionResponseTypeDef",
    "DefinitionPaginatorTypeDef",
    "DefinitionTypeDef",
    "DescribeBudgetActionsForAccountRequestDescribeBudgetActionsForAccountPaginateTypeDef",
    "DescribeBudgetActionsForBudgetRequestDescribeBudgetActionsForBudgetPaginateTypeDef",
    "DescribeBudgetNotificationsForAccountRequestDescribeBudgetNotificationsForAccountPaginateTypeDef",
    "DescribeBudgetsRequestDescribeBudgetsPaginateTypeDef",
    "DescribeNotificationsForBudgetRequestDescribeNotificationsForBudgetPaginateTypeDef",
    "DescribeSubscribersForNotificationRequestDescribeSubscribersForNotificationPaginateTypeDef",
    "BudgetedAndActualAmountsTypeDef",
    "DescribeBudgetActionHistoriesRequestDescribeBudgetActionHistoriesPaginateTypeDef",
    "DescribeBudgetActionHistoriesRequestRequestTypeDef",
    "DescribeBudgetPerformanceHistoryRequestDescribeBudgetPerformanceHistoryPaginateTypeDef",
    "DescribeBudgetPerformanceHistoryRequestRequestTypeDef",
    "DescribeBudgetNotificationsForAccountResponseTypeDef",
    "BudgetPaginatorTypeDef",
    "BudgetTypeDef",
    "ActionPaginatorTypeDef",
    "ActionTypeDef",
    "CreateBudgetActionRequestRequestTypeDef",
    "UpdateBudgetActionRequestRequestTypeDef",
    "BudgetPerformanceHistoryTypeDef",
    "DescribeBudgetsResponsePaginatorTypeDef",
    "CreateBudgetRequestRequestTypeDef",
    "DescribeBudgetResponseTypeDef",
    "DescribeBudgetsResponseTypeDef",
    "UpdateBudgetRequestRequestTypeDef",
    "ActionHistoryDetailsPaginatorTypeDef",
    "DescribeBudgetActionsForAccountResponsePaginatorTypeDef",
    "DescribeBudgetActionsForBudgetResponsePaginatorTypeDef",
    "ActionHistoryDetailsTypeDef",
    "DeleteBudgetActionResponseTypeDef",
    "DescribeBudgetActionResponseTypeDef",
    "DescribeBudgetActionsForAccountResponseTypeDef",
    "DescribeBudgetActionsForBudgetResponseTypeDef",
    "UpdateBudgetActionResponseTypeDef",
    "DescribeBudgetPerformanceHistoryResponseTypeDef",
    "ActionHistoryPaginatorTypeDef",
    "ActionHistoryTypeDef",
    "DescribeBudgetActionHistoriesResponsePaginatorTypeDef",
    "DescribeBudgetActionHistoriesResponseTypeDef",
)

ActionThresholdTypeDef = TypedDict(
    "ActionThresholdTypeDef",
    {
        "ActionThresholdValue": float,
        "ActionThresholdType": ThresholdTypeType,
    },
)
SubscriberTypeDef = TypedDict(
    "SubscriberTypeDef",
    {
        "SubscriptionType": SubscriptionTypeType,
        "Address": str,
    },
)
HistoricalOptionsTypeDef = TypedDict(
    "HistoricalOptionsTypeDef",
    {
        "BudgetAdjustmentPeriod": int,
        "LookBackAvailablePeriods": NotRequired[int],
    },
)
TimestampTypeDef = Union[datetime, str]
NotificationTypeDef = TypedDict(
    "NotificationTypeDef",
    {
        "NotificationType": NotificationTypeType,
        "ComparisonOperator": ComparisonOperatorType,
        "Threshold": float,
        "ThresholdType": NotRequired[ThresholdTypeType],
        "NotificationState": NotRequired[NotificationStateType],
    },
)
CostTypesTypeDef = TypedDict(
    "CostTypesTypeDef",
    {
        "IncludeTax": NotRequired[bool],
        "IncludeSubscription": NotRequired[bool],
        "UseBlended": NotRequired[bool],
        "IncludeRefund": NotRequired[bool],
        "IncludeCredit": NotRequired[bool],
        "IncludeUpfront": NotRequired[bool],
        "IncludeRecurring": NotRequired[bool],
        "IncludeOtherSubscription": NotRequired[bool],
        "IncludeSupport": NotRequired[bool],
        "IncludeDiscount": NotRequired[bool],
        "UseAmortized": NotRequired[bool],
    },
)
SpendTypeDef = TypedDict(
    "SpendTypeDef",
    {
        "Amount": str,
        "Unit": str,
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
IamActionDefinitionPaginatorTypeDef = TypedDict(
    "IamActionDefinitionPaginatorTypeDef",
    {
        "PolicyArn": str,
        "Roles": NotRequired[List[str]],
        "Groups": NotRequired[List[str]],
        "Users": NotRequired[List[str]],
    },
)
ScpActionDefinitionPaginatorTypeDef = TypedDict(
    "ScpActionDefinitionPaginatorTypeDef",
    {
        "PolicyId": str,
        "TargetIds": List[str],
    },
)
SsmActionDefinitionPaginatorTypeDef = TypedDict(
    "SsmActionDefinitionPaginatorTypeDef",
    {
        "ActionSubType": ActionSubTypeType,
        "Region": str,
        "InstanceIds": List[str],
    },
)
IamActionDefinitionTypeDef = TypedDict(
    "IamActionDefinitionTypeDef",
    {
        "PolicyArn": str,
        "Roles": NotRequired[Sequence[str]],
        "Groups": NotRequired[Sequence[str]],
        "Users": NotRequired[Sequence[str]],
    },
)
ScpActionDefinitionTypeDef = TypedDict(
    "ScpActionDefinitionTypeDef",
    {
        "PolicyId": str,
        "TargetIds": Sequence[str],
    },
)
SsmActionDefinitionTypeDef = TypedDict(
    "SsmActionDefinitionTypeDef",
    {
        "ActionSubType": ActionSubTypeType,
        "Region": str,
        "InstanceIds": Sequence[str],
    },
)
DeleteBudgetActionRequestRequestTypeDef = TypedDict(
    "DeleteBudgetActionRequestRequestTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "ActionId": str,
    },
)
DeleteBudgetRequestRequestTypeDef = TypedDict(
    "DeleteBudgetRequestRequestTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
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
DescribeBudgetActionRequestRequestTypeDef = TypedDict(
    "DescribeBudgetActionRequestRequestTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "ActionId": str,
    },
)
DescribeBudgetActionsForAccountRequestRequestTypeDef = TypedDict(
    "DescribeBudgetActionsForAccountRequestRequestTypeDef",
    {
        "AccountId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DescribeBudgetActionsForBudgetRequestRequestTypeDef = TypedDict(
    "DescribeBudgetActionsForBudgetRequestRequestTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DescribeBudgetNotificationsForAccountRequestRequestTypeDef = TypedDict(
    "DescribeBudgetNotificationsForAccountRequestRequestTypeDef",
    {
        "AccountId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DescribeBudgetRequestRequestTypeDef = TypedDict(
    "DescribeBudgetRequestRequestTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
    },
)
DescribeBudgetsRequestRequestTypeDef = TypedDict(
    "DescribeBudgetsRequestRequestTypeDef",
    {
        "AccountId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DescribeNotificationsForBudgetRequestRequestTypeDef = TypedDict(
    "DescribeNotificationsForBudgetRequestRequestTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ExecuteBudgetActionRequestRequestTypeDef = TypedDict(
    "ExecuteBudgetActionRequestRequestTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "ActionId": str,
        "ExecutionType": ExecutionTypeType,
    },
)
AutoAdjustDataPaginatorTypeDef = TypedDict(
    "AutoAdjustDataPaginatorTypeDef",
    {
        "AutoAdjustType": AutoAdjustTypeType,
        "HistoricalOptions": NotRequired[HistoricalOptionsTypeDef],
        "LastAutoAdjustTime": NotRequired[datetime],
    },
)
AutoAdjustDataTypeDef = TypedDict(
    "AutoAdjustDataTypeDef",
    {
        "AutoAdjustType": AutoAdjustTypeType,
        "HistoricalOptions": NotRequired[HistoricalOptionsTypeDef],
        "LastAutoAdjustTime": NotRequired[TimestampTypeDef],
    },
)
TimePeriodTypeDef = TypedDict(
    "TimePeriodTypeDef",
    {
        "Start": NotRequired[TimestampTypeDef],
        "End": NotRequired[TimestampTypeDef],
    },
)
BudgetNotificationsForAccountTypeDef = TypedDict(
    "BudgetNotificationsForAccountTypeDef",
    {
        "Notifications": NotRequired[List[NotificationTypeDef]],
        "BudgetName": NotRequired[str],
    },
)
CreateNotificationRequestRequestTypeDef = TypedDict(
    "CreateNotificationRequestRequestTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "Notification": NotificationTypeDef,
        "Subscribers": Sequence[SubscriberTypeDef],
    },
)
CreateSubscriberRequestRequestTypeDef = TypedDict(
    "CreateSubscriberRequestRequestTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "Notification": NotificationTypeDef,
        "Subscriber": SubscriberTypeDef,
    },
)
DeleteNotificationRequestRequestTypeDef = TypedDict(
    "DeleteNotificationRequestRequestTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "Notification": NotificationTypeDef,
    },
)
DeleteSubscriberRequestRequestTypeDef = TypedDict(
    "DeleteSubscriberRequestRequestTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "Notification": NotificationTypeDef,
        "Subscriber": SubscriberTypeDef,
    },
)
DescribeSubscribersForNotificationRequestRequestTypeDef = TypedDict(
    "DescribeSubscribersForNotificationRequestRequestTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "Notification": NotificationTypeDef,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
NotificationWithSubscribersTypeDef = TypedDict(
    "NotificationWithSubscribersTypeDef",
    {
        "Notification": NotificationTypeDef,
        "Subscribers": Sequence[SubscriberTypeDef],
    },
)
UpdateNotificationRequestRequestTypeDef = TypedDict(
    "UpdateNotificationRequestRequestTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "OldNotification": NotificationTypeDef,
        "NewNotification": NotificationTypeDef,
    },
)
UpdateSubscriberRequestRequestTypeDef = TypedDict(
    "UpdateSubscriberRequestRequestTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "Notification": NotificationTypeDef,
        "OldSubscriber": SubscriberTypeDef,
        "NewSubscriber": SubscriberTypeDef,
    },
)
CalculatedSpendTypeDef = TypedDict(
    "CalculatedSpendTypeDef",
    {
        "ActualSpend": SpendTypeDef,
        "ForecastedSpend": NotRequired[SpendTypeDef],
    },
)
CreateBudgetActionResponseTypeDef = TypedDict(
    "CreateBudgetActionResponseTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "ActionId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeNotificationsForBudgetResponseTypeDef = TypedDict(
    "DescribeNotificationsForBudgetResponseTypeDef",
    {
        "Notifications": List[NotificationTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeSubscribersForNotificationResponseTypeDef = TypedDict(
    "DescribeSubscribersForNotificationResponseTypeDef",
    {
        "Subscribers": List[SubscriberTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ExecuteBudgetActionResponseTypeDef = TypedDict(
    "ExecuteBudgetActionResponseTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "ActionId": str,
        "ExecutionType": ExecutionTypeType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DefinitionPaginatorTypeDef = TypedDict(
    "DefinitionPaginatorTypeDef",
    {
        "IamActionDefinition": NotRequired[IamActionDefinitionPaginatorTypeDef],
        "ScpActionDefinition": NotRequired[ScpActionDefinitionPaginatorTypeDef],
        "SsmActionDefinition": NotRequired[SsmActionDefinitionPaginatorTypeDef],
    },
)
DefinitionTypeDef = TypedDict(
    "DefinitionTypeDef",
    {
        "IamActionDefinition": NotRequired[IamActionDefinitionTypeDef],
        "ScpActionDefinition": NotRequired[ScpActionDefinitionTypeDef],
        "SsmActionDefinition": NotRequired[SsmActionDefinitionTypeDef],
    },
)
DescribeBudgetActionsForAccountRequestDescribeBudgetActionsForAccountPaginateTypeDef = TypedDict(
    "DescribeBudgetActionsForAccountRequestDescribeBudgetActionsForAccountPaginateTypeDef",
    {
        "AccountId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeBudgetActionsForBudgetRequestDescribeBudgetActionsForBudgetPaginateTypeDef = TypedDict(
    "DescribeBudgetActionsForBudgetRequestDescribeBudgetActionsForBudgetPaginateTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeBudgetNotificationsForAccountRequestDescribeBudgetNotificationsForAccountPaginateTypeDef = TypedDict(
    "DescribeBudgetNotificationsForAccountRequestDescribeBudgetNotificationsForAccountPaginateTypeDef",
    {
        "AccountId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeBudgetsRequestDescribeBudgetsPaginateTypeDef = TypedDict(
    "DescribeBudgetsRequestDescribeBudgetsPaginateTypeDef",
    {
        "AccountId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeNotificationsForBudgetRequestDescribeNotificationsForBudgetPaginateTypeDef = TypedDict(
    "DescribeNotificationsForBudgetRequestDescribeNotificationsForBudgetPaginateTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeSubscribersForNotificationRequestDescribeSubscribersForNotificationPaginateTypeDef = TypedDict(
    "DescribeSubscribersForNotificationRequestDescribeSubscribersForNotificationPaginateTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "Notification": NotificationTypeDef,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
BudgetedAndActualAmountsTypeDef = TypedDict(
    "BudgetedAndActualAmountsTypeDef",
    {
        "BudgetedAmount": NotRequired[SpendTypeDef],
        "ActualAmount": NotRequired[SpendTypeDef],
        "TimePeriod": NotRequired[TimePeriodTypeDef],
    },
)
DescribeBudgetActionHistoriesRequestDescribeBudgetActionHistoriesPaginateTypeDef = TypedDict(
    "DescribeBudgetActionHistoriesRequestDescribeBudgetActionHistoriesPaginateTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "ActionId": str,
        "TimePeriod": NotRequired[TimePeriodTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeBudgetActionHistoriesRequestRequestTypeDef = TypedDict(
    "DescribeBudgetActionHistoriesRequestRequestTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "ActionId": str,
        "TimePeriod": NotRequired[TimePeriodTypeDef],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DescribeBudgetPerformanceHistoryRequestDescribeBudgetPerformanceHistoryPaginateTypeDef = TypedDict(
    "DescribeBudgetPerformanceHistoryRequestDescribeBudgetPerformanceHistoryPaginateTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "TimePeriod": NotRequired[TimePeriodTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeBudgetPerformanceHistoryRequestRequestTypeDef = TypedDict(
    "DescribeBudgetPerformanceHistoryRequestRequestTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "TimePeriod": NotRequired[TimePeriodTypeDef],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DescribeBudgetNotificationsForAccountResponseTypeDef = TypedDict(
    "DescribeBudgetNotificationsForAccountResponseTypeDef",
    {
        "BudgetNotificationsForAccount": List[BudgetNotificationsForAccountTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BudgetPaginatorTypeDef = TypedDict(
    "BudgetPaginatorTypeDef",
    {
        "BudgetName": str,
        "TimeUnit": TimeUnitType,
        "BudgetType": BudgetTypeType,
        "BudgetLimit": NotRequired[SpendTypeDef],
        "PlannedBudgetLimits": NotRequired[Dict[str, SpendTypeDef]],
        "CostFilters": NotRequired[Dict[str, List[str]]],
        "CostTypes": NotRequired[CostTypesTypeDef],
        "TimePeriod": NotRequired[TimePeriodTypeDef],
        "CalculatedSpend": NotRequired[CalculatedSpendTypeDef],
        "LastUpdatedTime": NotRequired[datetime],
        "AutoAdjustData": NotRequired[AutoAdjustDataPaginatorTypeDef],
    },
)
BudgetTypeDef = TypedDict(
    "BudgetTypeDef",
    {
        "BudgetName": str,
        "TimeUnit": TimeUnitType,
        "BudgetType": BudgetTypeType,
        "BudgetLimit": NotRequired[SpendTypeDef],
        "PlannedBudgetLimits": NotRequired[Mapping[str, SpendTypeDef]],
        "CostFilters": NotRequired[Mapping[str, Sequence[str]]],
        "CostTypes": NotRequired[CostTypesTypeDef],
        "TimePeriod": NotRequired[TimePeriodTypeDef],
        "CalculatedSpend": NotRequired[CalculatedSpendTypeDef],
        "LastUpdatedTime": NotRequired[TimestampTypeDef],
        "AutoAdjustData": NotRequired[AutoAdjustDataTypeDef],
    },
)
ActionPaginatorTypeDef = TypedDict(
    "ActionPaginatorTypeDef",
    {
        "ActionId": str,
        "BudgetName": str,
        "NotificationType": NotificationTypeType,
        "ActionType": ActionTypeType,
        "ActionThreshold": ActionThresholdTypeDef,
        "Definition": DefinitionPaginatorTypeDef,
        "ExecutionRoleArn": str,
        "ApprovalModel": ApprovalModelType,
        "Status": ActionStatusType,
        "Subscribers": List[SubscriberTypeDef],
    },
)
ActionTypeDef = TypedDict(
    "ActionTypeDef",
    {
        "ActionId": str,
        "BudgetName": str,
        "NotificationType": NotificationTypeType,
        "ActionType": ActionTypeType,
        "ActionThreshold": ActionThresholdTypeDef,
        "Definition": DefinitionTypeDef,
        "ExecutionRoleArn": str,
        "ApprovalModel": ApprovalModelType,
        "Status": ActionStatusType,
        "Subscribers": List[SubscriberTypeDef],
    },
)
CreateBudgetActionRequestRequestTypeDef = TypedDict(
    "CreateBudgetActionRequestRequestTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "NotificationType": NotificationTypeType,
        "ActionType": ActionTypeType,
        "ActionThreshold": ActionThresholdTypeDef,
        "Definition": DefinitionTypeDef,
        "ExecutionRoleArn": str,
        "ApprovalModel": ApprovalModelType,
        "Subscribers": Sequence[SubscriberTypeDef],
    },
)
UpdateBudgetActionRequestRequestTypeDef = TypedDict(
    "UpdateBudgetActionRequestRequestTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "ActionId": str,
        "NotificationType": NotRequired[NotificationTypeType],
        "ActionThreshold": NotRequired[ActionThresholdTypeDef],
        "Definition": NotRequired[DefinitionTypeDef],
        "ExecutionRoleArn": NotRequired[str],
        "ApprovalModel": NotRequired[ApprovalModelType],
        "Subscribers": NotRequired[Sequence[SubscriberTypeDef]],
    },
)
BudgetPerformanceHistoryTypeDef = TypedDict(
    "BudgetPerformanceHistoryTypeDef",
    {
        "BudgetName": NotRequired[str],
        "BudgetType": NotRequired[BudgetTypeType],
        "CostFilters": NotRequired[Dict[str, List[str]]],
        "CostTypes": NotRequired[CostTypesTypeDef],
        "TimeUnit": NotRequired[TimeUnitType],
        "BudgetedAndActualAmountsList": NotRequired[List[BudgetedAndActualAmountsTypeDef]],
    },
)
DescribeBudgetsResponsePaginatorTypeDef = TypedDict(
    "DescribeBudgetsResponsePaginatorTypeDef",
    {
        "Budgets": List[BudgetPaginatorTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateBudgetRequestRequestTypeDef = TypedDict(
    "CreateBudgetRequestRequestTypeDef",
    {
        "AccountId": str,
        "Budget": BudgetTypeDef,
        "NotificationsWithSubscribers": NotRequired[Sequence[NotificationWithSubscribersTypeDef]],
    },
)
DescribeBudgetResponseTypeDef = TypedDict(
    "DescribeBudgetResponseTypeDef",
    {
        "Budget": BudgetTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeBudgetsResponseTypeDef = TypedDict(
    "DescribeBudgetsResponseTypeDef",
    {
        "Budgets": List[BudgetTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateBudgetRequestRequestTypeDef = TypedDict(
    "UpdateBudgetRequestRequestTypeDef",
    {
        "AccountId": str,
        "NewBudget": BudgetTypeDef,
    },
)
ActionHistoryDetailsPaginatorTypeDef = TypedDict(
    "ActionHistoryDetailsPaginatorTypeDef",
    {
        "Message": str,
        "Action": ActionPaginatorTypeDef,
    },
)
DescribeBudgetActionsForAccountResponsePaginatorTypeDef = TypedDict(
    "DescribeBudgetActionsForAccountResponsePaginatorTypeDef",
    {
        "Actions": List[ActionPaginatorTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeBudgetActionsForBudgetResponsePaginatorTypeDef = TypedDict(
    "DescribeBudgetActionsForBudgetResponsePaginatorTypeDef",
    {
        "Actions": List[ActionPaginatorTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ActionHistoryDetailsTypeDef = TypedDict(
    "ActionHistoryDetailsTypeDef",
    {
        "Message": str,
        "Action": ActionTypeDef,
    },
)
DeleteBudgetActionResponseTypeDef = TypedDict(
    "DeleteBudgetActionResponseTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "Action": ActionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeBudgetActionResponseTypeDef = TypedDict(
    "DescribeBudgetActionResponseTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "Action": ActionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeBudgetActionsForAccountResponseTypeDef = TypedDict(
    "DescribeBudgetActionsForAccountResponseTypeDef",
    {
        "Actions": List[ActionTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeBudgetActionsForBudgetResponseTypeDef = TypedDict(
    "DescribeBudgetActionsForBudgetResponseTypeDef",
    {
        "Actions": List[ActionTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateBudgetActionResponseTypeDef = TypedDict(
    "UpdateBudgetActionResponseTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "OldAction": ActionTypeDef,
        "NewAction": ActionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeBudgetPerformanceHistoryResponseTypeDef = TypedDict(
    "DescribeBudgetPerformanceHistoryResponseTypeDef",
    {
        "BudgetPerformanceHistory": BudgetPerformanceHistoryTypeDef,
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ActionHistoryPaginatorTypeDef = TypedDict(
    "ActionHistoryPaginatorTypeDef",
    {
        "Timestamp": datetime,
        "Status": ActionStatusType,
        "EventType": EventTypeType,
        "ActionHistoryDetails": ActionHistoryDetailsPaginatorTypeDef,
    },
)
ActionHistoryTypeDef = TypedDict(
    "ActionHistoryTypeDef",
    {
        "Timestamp": datetime,
        "Status": ActionStatusType,
        "EventType": EventTypeType,
        "ActionHistoryDetails": ActionHistoryDetailsTypeDef,
    },
)
DescribeBudgetActionHistoriesResponsePaginatorTypeDef = TypedDict(
    "DescribeBudgetActionHistoriesResponsePaginatorTypeDef",
    {
        "ActionHistories": List[ActionHistoryPaginatorTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeBudgetActionHistoriesResponseTypeDef = TypedDict(
    "DescribeBudgetActionHistoriesResponseTypeDef",
    {
        "ActionHistories": List[ActionHistoryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
