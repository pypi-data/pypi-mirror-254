"""
Type annotations for billingconductor service type definitions.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_billingconductor/type_defs/)

Usage::

    ```python
    from types_aiobotocore_billingconductor.type_defs import AccountAssociationsListElementTypeDef

    data: AccountAssociationsListElementTypeDef = ...
    ```
"""

import sys
from typing import Dict, List, Mapping, Sequence

from .literals import (
    AssociateResourceErrorReasonType,
    BillingGroupStatusType,
    CurrencyCodeType,
    CustomLineItemRelationshipType,
    CustomLineItemTypeType,
    GroupByAttributeNameType,
    PricingRuleScopeType,
    PricingRuleTypeType,
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
    "AccountAssociationsListElementTypeDef",
    "AccountGroupingTypeDef",
    "AssociateAccountsInputRequestTypeDef",
    "ResponseMetadataTypeDef",
    "AssociatePricingRulesInputRequestTypeDef",
    "AssociateResourceErrorTypeDef",
    "AttributeTypeDef",
    "CustomLineItemBillingPeriodRangeTypeDef",
    "BillingGroupCostReportElementTypeDef",
    "ComputationPreferenceTypeDef",
    "ListBillingGroupAccountGroupingTypeDef",
    "BillingPeriodRangeTypeDef",
    "CreateFreeTierConfigTypeDef",
    "CreatePricingPlanInputRequestTypeDef",
    "CustomLineItemFlatChargeDetailsTypeDef",
    "CustomLineItemPercentageChargeDetailsTypeDef",
    "LineItemFilterTypeDef",
    "DeleteBillingGroupInputRequestTypeDef",
    "DeletePricingPlanInputRequestTypeDef",
    "DeletePricingRuleInputRequestTypeDef",
    "DisassociateAccountsInputRequestTypeDef",
    "DisassociatePricingRulesInputRequestTypeDef",
    "FreeTierConfigTypeDef",
    "LineItemFilterPaginatorTypeDef",
    "ListAccountAssociationsFilterTypeDef",
    "PaginatorConfigTypeDef",
    "ListBillingGroupCostReportsFilterTypeDef",
    "ListBillingGroupsFilterTypeDef",
    "ListCustomLineItemFlatChargeDetailsTypeDef",
    "ListCustomLineItemPercentageChargeDetailsTypeDef",
    "ListCustomLineItemVersionsBillingPeriodRangeFilterTypeDef",
    "ListCustomLineItemsFilterTypeDef",
    "ListPricingPlansAssociatedWithPricingRuleInputRequestTypeDef",
    "ListPricingPlansFilterTypeDef",
    "PricingPlanListElementTypeDef",
    "ListPricingRulesAssociatedToPricingPlanInputRequestTypeDef",
    "ListPricingRulesFilterTypeDef",
    "ListResourcesAssociatedToCustomLineItemFilterTypeDef",
    "ListResourcesAssociatedToCustomLineItemResponseElementTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateBillingGroupAccountGroupingTypeDef",
    "UpdateCustomLineItemFlatChargeDetailsTypeDef",
    "UpdateCustomLineItemPercentageChargeDetailsTypeDef",
    "UpdateFreeTierConfigTypeDef",
    "UpdatePricingPlanInputRequestTypeDef",
    "AssociateAccountsOutputTypeDef",
    "AssociatePricingRulesOutputTypeDef",
    "CreateBillingGroupOutputTypeDef",
    "CreateCustomLineItemOutputTypeDef",
    "CreatePricingPlanOutputTypeDef",
    "CreatePricingRuleOutputTypeDef",
    "DeleteBillingGroupOutputTypeDef",
    "DeleteCustomLineItemOutputTypeDef",
    "DeletePricingPlanOutputTypeDef",
    "DeletePricingRuleOutputTypeDef",
    "DisassociateAccountsOutputTypeDef",
    "DisassociatePricingRulesOutputTypeDef",
    "ListAccountAssociationsOutputTypeDef",
    "ListPricingPlansAssociatedWithPricingRuleOutputTypeDef",
    "ListPricingRulesAssociatedToPricingPlanOutputTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "UpdatePricingPlanOutputTypeDef",
    "AssociateResourceResponseElementTypeDef",
    "DisassociateResourceResponseElementTypeDef",
    "BillingGroupCostReportResultElementTypeDef",
    "BatchAssociateResourcesToCustomLineItemInputRequestTypeDef",
    "BatchDisassociateResourcesFromCustomLineItemInputRequestTypeDef",
    "DeleteCustomLineItemInputRequestTypeDef",
    "ListBillingGroupCostReportsOutputTypeDef",
    "CreateBillingGroupInputRequestTypeDef",
    "BillingGroupListElementTypeDef",
    "GetBillingGroupCostReportInputRequestTypeDef",
    "CreateTieringInputTypeDef",
    "CustomLineItemChargeDetailsTypeDef",
    "TieringTypeDef",
    "ListAccountAssociationsInputRequestTypeDef",
    "ListAccountAssociationsInputListAccountAssociationsPaginateTypeDef",
    "ListPricingPlansAssociatedWithPricingRuleInputListPricingPlansAssociatedWithPricingRulePaginateTypeDef",
    "ListPricingRulesAssociatedToPricingPlanInputListPricingRulesAssociatedToPricingPlanPaginateTypeDef",
    "ListBillingGroupCostReportsInputListBillingGroupCostReportsPaginateTypeDef",
    "ListBillingGroupCostReportsInputRequestTypeDef",
    "ListBillingGroupsInputListBillingGroupsPaginateTypeDef",
    "ListBillingGroupsInputRequestTypeDef",
    "ListCustomLineItemChargeDetailsPaginatorTypeDef",
    "ListCustomLineItemChargeDetailsTypeDef",
    "ListCustomLineItemVersionsFilterTypeDef",
    "ListCustomLineItemsInputListCustomLineItemsPaginateTypeDef",
    "ListCustomLineItemsInputRequestTypeDef",
    "ListPricingPlansInputListPricingPlansPaginateTypeDef",
    "ListPricingPlansInputRequestTypeDef",
    "ListPricingPlansOutputTypeDef",
    "ListPricingRulesInputListPricingRulesPaginateTypeDef",
    "ListPricingRulesInputRequestTypeDef",
    "ListResourcesAssociatedToCustomLineItemInputListResourcesAssociatedToCustomLineItemPaginateTypeDef",
    "ListResourcesAssociatedToCustomLineItemInputRequestTypeDef",
    "ListResourcesAssociatedToCustomLineItemOutputTypeDef",
    "UpdateBillingGroupInputRequestTypeDef",
    "UpdateBillingGroupOutputTypeDef",
    "UpdateCustomLineItemChargeDetailsTypeDef",
    "UpdateTieringInputTypeDef",
    "BatchAssociateResourcesToCustomLineItemOutputTypeDef",
    "BatchDisassociateResourcesFromCustomLineItemOutputTypeDef",
    "GetBillingGroupCostReportOutputTypeDef",
    "ListBillingGroupsOutputTypeDef",
    "CreatePricingRuleInputRequestTypeDef",
    "CreateCustomLineItemInputRequestTypeDef",
    "PricingRuleListElementTypeDef",
    "CustomLineItemListElementPaginatorTypeDef",
    "CustomLineItemVersionListElementPaginatorTypeDef",
    "CustomLineItemListElementTypeDef",
    "CustomLineItemVersionListElementTypeDef",
    "UpdateCustomLineItemOutputTypeDef",
    "ListCustomLineItemVersionsInputListCustomLineItemVersionsPaginateTypeDef",
    "ListCustomLineItemVersionsInputRequestTypeDef",
    "UpdateCustomLineItemInputRequestTypeDef",
    "UpdatePricingRuleInputRequestTypeDef",
    "UpdatePricingRuleOutputTypeDef",
    "ListPricingRulesOutputTypeDef",
    "ListCustomLineItemsOutputPaginatorTypeDef",
    "ListCustomLineItemVersionsOutputPaginatorTypeDef",
    "ListCustomLineItemsOutputTypeDef",
    "ListCustomLineItemVersionsOutputTypeDef",
)

AccountAssociationsListElementTypeDef = TypedDict(
    "AccountAssociationsListElementTypeDef",
    {
        "AccountId": NotRequired[str],
        "BillingGroupArn": NotRequired[str],
        "AccountName": NotRequired[str],
        "AccountEmail": NotRequired[str],
    },
)
AccountGroupingTypeDef = TypedDict(
    "AccountGroupingTypeDef",
    {
        "LinkedAccountIds": Sequence[str],
        "AutoAssociate": NotRequired[bool],
    },
)
AssociateAccountsInputRequestTypeDef = TypedDict(
    "AssociateAccountsInputRequestTypeDef",
    {
        "Arn": str,
        "AccountIds": Sequence[str],
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
AssociatePricingRulesInputRequestTypeDef = TypedDict(
    "AssociatePricingRulesInputRequestTypeDef",
    {
        "Arn": str,
        "PricingRuleArns": Sequence[str],
    },
)
AssociateResourceErrorTypeDef = TypedDict(
    "AssociateResourceErrorTypeDef",
    {
        "Message": NotRequired[str],
        "Reason": NotRequired[AssociateResourceErrorReasonType],
    },
)
AttributeTypeDef = TypedDict(
    "AttributeTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
    },
)
CustomLineItemBillingPeriodRangeTypeDef = TypedDict(
    "CustomLineItemBillingPeriodRangeTypeDef",
    {
        "InclusiveStartBillingPeriod": str,
        "ExclusiveEndBillingPeriod": NotRequired[str],
    },
)
BillingGroupCostReportElementTypeDef = TypedDict(
    "BillingGroupCostReportElementTypeDef",
    {
        "Arn": NotRequired[str],
        "AWSCost": NotRequired[str],
        "ProformaCost": NotRequired[str],
        "Margin": NotRequired[str],
        "MarginPercentage": NotRequired[str],
        "Currency": NotRequired[str],
    },
)
ComputationPreferenceTypeDef = TypedDict(
    "ComputationPreferenceTypeDef",
    {
        "PricingPlanArn": str,
    },
)
ListBillingGroupAccountGroupingTypeDef = TypedDict(
    "ListBillingGroupAccountGroupingTypeDef",
    {
        "AutoAssociate": NotRequired[bool],
    },
)
BillingPeriodRangeTypeDef = TypedDict(
    "BillingPeriodRangeTypeDef",
    {
        "InclusiveStartBillingPeriod": str,
        "ExclusiveEndBillingPeriod": str,
    },
)
CreateFreeTierConfigTypeDef = TypedDict(
    "CreateFreeTierConfigTypeDef",
    {
        "Activated": bool,
    },
)
CreatePricingPlanInputRequestTypeDef = TypedDict(
    "CreatePricingPlanInputRequestTypeDef",
    {
        "Name": str,
        "ClientToken": NotRequired[str],
        "Description": NotRequired[str],
        "PricingRuleArns": NotRequired[Sequence[str]],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
CustomLineItemFlatChargeDetailsTypeDef = TypedDict(
    "CustomLineItemFlatChargeDetailsTypeDef",
    {
        "ChargeValue": float,
    },
)
CustomLineItemPercentageChargeDetailsTypeDef = TypedDict(
    "CustomLineItemPercentageChargeDetailsTypeDef",
    {
        "PercentageValue": float,
        "AssociatedValues": NotRequired[Sequence[str]],
    },
)
LineItemFilterTypeDef = TypedDict(
    "LineItemFilterTypeDef",
    {
        "Attribute": Literal["LINE_ITEM_TYPE"],
        "MatchOption": Literal["NOT_EQUAL"],
        "Values": Sequence[Literal["SAVINGS_PLAN_NEGATION"]],
    },
)
DeleteBillingGroupInputRequestTypeDef = TypedDict(
    "DeleteBillingGroupInputRequestTypeDef",
    {
        "Arn": str,
    },
)
DeletePricingPlanInputRequestTypeDef = TypedDict(
    "DeletePricingPlanInputRequestTypeDef",
    {
        "Arn": str,
    },
)
DeletePricingRuleInputRequestTypeDef = TypedDict(
    "DeletePricingRuleInputRequestTypeDef",
    {
        "Arn": str,
    },
)
DisassociateAccountsInputRequestTypeDef = TypedDict(
    "DisassociateAccountsInputRequestTypeDef",
    {
        "Arn": str,
        "AccountIds": Sequence[str],
    },
)
DisassociatePricingRulesInputRequestTypeDef = TypedDict(
    "DisassociatePricingRulesInputRequestTypeDef",
    {
        "Arn": str,
        "PricingRuleArns": Sequence[str],
    },
)
FreeTierConfigTypeDef = TypedDict(
    "FreeTierConfigTypeDef",
    {
        "Activated": bool,
    },
)
LineItemFilterPaginatorTypeDef = TypedDict(
    "LineItemFilterPaginatorTypeDef",
    {
        "Attribute": Literal["LINE_ITEM_TYPE"],
        "MatchOption": Literal["NOT_EQUAL"],
        "Values": List[Literal["SAVINGS_PLAN_NEGATION"]],
    },
)
ListAccountAssociationsFilterTypeDef = TypedDict(
    "ListAccountAssociationsFilterTypeDef",
    {
        "Association": NotRequired[str],
        "AccountId": NotRequired[str],
        "AccountIds": NotRequired[Sequence[str]],
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
ListBillingGroupCostReportsFilterTypeDef = TypedDict(
    "ListBillingGroupCostReportsFilterTypeDef",
    {
        "BillingGroupArns": NotRequired[Sequence[str]],
    },
)
ListBillingGroupsFilterTypeDef = TypedDict(
    "ListBillingGroupsFilterTypeDef",
    {
        "Arns": NotRequired[Sequence[str]],
        "PricingPlan": NotRequired[str],
        "Statuses": NotRequired[Sequence[BillingGroupStatusType]],
        "AutoAssociate": NotRequired[bool],
    },
)
ListCustomLineItemFlatChargeDetailsTypeDef = TypedDict(
    "ListCustomLineItemFlatChargeDetailsTypeDef",
    {
        "ChargeValue": float,
    },
)
ListCustomLineItemPercentageChargeDetailsTypeDef = TypedDict(
    "ListCustomLineItemPercentageChargeDetailsTypeDef",
    {
        "PercentageValue": float,
    },
)
ListCustomLineItemVersionsBillingPeriodRangeFilterTypeDef = TypedDict(
    "ListCustomLineItemVersionsBillingPeriodRangeFilterTypeDef",
    {
        "StartBillingPeriod": NotRequired[str],
        "EndBillingPeriod": NotRequired[str],
    },
)
ListCustomLineItemsFilterTypeDef = TypedDict(
    "ListCustomLineItemsFilterTypeDef",
    {
        "Names": NotRequired[Sequence[str]],
        "BillingGroups": NotRequired[Sequence[str]],
        "Arns": NotRequired[Sequence[str]],
        "AccountIds": NotRequired[Sequence[str]],
    },
)
ListPricingPlansAssociatedWithPricingRuleInputRequestTypeDef = TypedDict(
    "ListPricingPlansAssociatedWithPricingRuleInputRequestTypeDef",
    {
        "PricingRuleArn": str,
        "BillingPeriod": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListPricingPlansFilterTypeDef = TypedDict(
    "ListPricingPlansFilterTypeDef",
    {
        "Arns": NotRequired[Sequence[str]],
    },
)
PricingPlanListElementTypeDef = TypedDict(
    "PricingPlanListElementTypeDef",
    {
        "Name": NotRequired[str],
        "Arn": NotRequired[str],
        "Description": NotRequired[str],
        "Size": NotRequired[int],
        "CreationTime": NotRequired[int],
        "LastModifiedTime": NotRequired[int],
    },
)
ListPricingRulesAssociatedToPricingPlanInputRequestTypeDef = TypedDict(
    "ListPricingRulesAssociatedToPricingPlanInputRequestTypeDef",
    {
        "PricingPlanArn": str,
        "BillingPeriod": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListPricingRulesFilterTypeDef = TypedDict(
    "ListPricingRulesFilterTypeDef",
    {
        "Arns": NotRequired[Sequence[str]],
    },
)
ListResourcesAssociatedToCustomLineItemFilterTypeDef = TypedDict(
    "ListResourcesAssociatedToCustomLineItemFilterTypeDef",
    {
        "Relationship": NotRequired[CustomLineItemRelationshipType],
    },
)
ListResourcesAssociatedToCustomLineItemResponseElementTypeDef = TypedDict(
    "ListResourcesAssociatedToCustomLineItemResponseElementTypeDef",
    {
        "Arn": NotRequired[str],
        "Relationship": NotRequired[CustomLineItemRelationshipType],
        "EndBillingPeriod": NotRequired[str],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Mapping[str, str],
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)
UpdateBillingGroupAccountGroupingTypeDef = TypedDict(
    "UpdateBillingGroupAccountGroupingTypeDef",
    {
        "AutoAssociate": NotRequired[bool],
    },
)
UpdateCustomLineItemFlatChargeDetailsTypeDef = TypedDict(
    "UpdateCustomLineItemFlatChargeDetailsTypeDef",
    {
        "ChargeValue": float,
    },
)
UpdateCustomLineItemPercentageChargeDetailsTypeDef = TypedDict(
    "UpdateCustomLineItemPercentageChargeDetailsTypeDef",
    {
        "PercentageValue": float,
    },
)
UpdateFreeTierConfigTypeDef = TypedDict(
    "UpdateFreeTierConfigTypeDef",
    {
        "Activated": bool,
    },
)
UpdatePricingPlanInputRequestTypeDef = TypedDict(
    "UpdatePricingPlanInputRequestTypeDef",
    {
        "Arn": str,
        "Name": NotRequired[str],
        "Description": NotRequired[str],
    },
)
AssociateAccountsOutputTypeDef = TypedDict(
    "AssociateAccountsOutputTypeDef",
    {
        "Arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AssociatePricingRulesOutputTypeDef = TypedDict(
    "AssociatePricingRulesOutputTypeDef",
    {
        "Arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateBillingGroupOutputTypeDef = TypedDict(
    "CreateBillingGroupOutputTypeDef",
    {
        "Arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateCustomLineItemOutputTypeDef = TypedDict(
    "CreateCustomLineItemOutputTypeDef",
    {
        "Arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreatePricingPlanOutputTypeDef = TypedDict(
    "CreatePricingPlanOutputTypeDef",
    {
        "Arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreatePricingRuleOutputTypeDef = TypedDict(
    "CreatePricingRuleOutputTypeDef",
    {
        "Arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteBillingGroupOutputTypeDef = TypedDict(
    "DeleteBillingGroupOutputTypeDef",
    {
        "Arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteCustomLineItemOutputTypeDef = TypedDict(
    "DeleteCustomLineItemOutputTypeDef",
    {
        "Arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeletePricingPlanOutputTypeDef = TypedDict(
    "DeletePricingPlanOutputTypeDef",
    {
        "Arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeletePricingRuleOutputTypeDef = TypedDict(
    "DeletePricingRuleOutputTypeDef",
    {
        "Arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DisassociateAccountsOutputTypeDef = TypedDict(
    "DisassociateAccountsOutputTypeDef",
    {
        "Arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DisassociatePricingRulesOutputTypeDef = TypedDict(
    "DisassociatePricingRulesOutputTypeDef",
    {
        "Arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAccountAssociationsOutputTypeDef = TypedDict(
    "ListAccountAssociationsOutputTypeDef",
    {
        "LinkedAccounts": List[AccountAssociationsListElementTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListPricingPlansAssociatedWithPricingRuleOutputTypeDef = TypedDict(
    "ListPricingPlansAssociatedWithPricingRuleOutputTypeDef",
    {
        "BillingPeriod": str,
        "PricingRuleArn": str,
        "PricingPlanArns": List[str],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListPricingRulesAssociatedToPricingPlanOutputTypeDef = TypedDict(
    "ListPricingRulesAssociatedToPricingPlanOutputTypeDef",
    {
        "BillingPeriod": str,
        "PricingPlanArn": str,
        "PricingRuleArns": List[str],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdatePricingPlanOutputTypeDef = TypedDict(
    "UpdatePricingPlanOutputTypeDef",
    {
        "Arn": str,
        "Name": str,
        "Description": str,
        "Size": int,
        "LastModifiedTime": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AssociateResourceResponseElementTypeDef = TypedDict(
    "AssociateResourceResponseElementTypeDef",
    {
        "Arn": NotRequired[str],
        "Error": NotRequired[AssociateResourceErrorTypeDef],
    },
)
DisassociateResourceResponseElementTypeDef = TypedDict(
    "DisassociateResourceResponseElementTypeDef",
    {
        "Arn": NotRequired[str],
        "Error": NotRequired[AssociateResourceErrorTypeDef],
    },
)
BillingGroupCostReportResultElementTypeDef = TypedDict(
    "BillingGroupCostReportResultElementTypeDef",
    {
        "Arn": NotRequired[str],
        "AWSCost": NotRequired[str],
        "ProformaCost": NotRequired[str],
        "Margin": NotRequired[str],
        "MarginPercentage": NotRequired[str],
        "Currency": NotRequired[str],
        "Attributes": NotRequired[List[AttributeTypeDef]],
    },
)
BatchAssociateResourcesToCustomLineItemInputRequestTypeDef = TypedDict(
    "BatchAssociateResourcesToCustomLineItemInputRequestTypeDef",
    {
        "TargetArn": str,
        "ResourceArns": Sequence[str],
        "BillingPeriodRange": NotRequired[CustomLineItemBillingPeriodRangeTypeDef],
    },
)
BatchDisassociateResourcesFromCustomLineItemInputRequestTypeDef = TypedDict(
    "BatchDisassociateResourcesFromCustomLineItemInputRequestTypeDef",
    {
        "TargetArn": str,
        "ResourceArns": Sequence[str],
        "BillingPeriodRange": NotRequired[CustomLineItemBillingPeriodRangeTypeDef],
    },
)
DeleteCustomLineItemInputRequestTypeDef = TypedDict(
    "DeleteCustomLineItemInputRequestTypeDef",
    {
        "Arn": str,
        "BillingPeriodRange": NotRequired[CustomLineItemBillingPeriodRangeTypeDef],
    },
)
ListBillingGroupCostReportsOutputTypeDef = TypedDict(
    "ListBillingGroupCostReportsOutputTypeDef",
    {
        "BillingGroupCostReports": List[BillingGroupCostReportElementTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateBillingGroupInputRequestTypeDef = TypedDict(
    "CreateBillingGroupInputRequestTypeDef",
    {
        "Name": str,
        "AccountGrouping": AccountGroupingTypeDef,
        "ComputationPreference": ComputationPreferenceTypeDef,
        "ClientToken": NotRequired[str],
        "PrimaryAccountId": NotRequired[str],
        "Description": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
BillingGroupListElementTypeDef = TypedDict(
    "BillingGroupListElementTypeDef",
    {
        "Name": NotRequired[str],
        "Arn": NotRequired[str],
        "Description": NotRequired[str],
        "PrimaryAccountId": NotRequired[str],
        "ComputationPreference": NotRequired[ComputationPreferenceTypeDef],
        "Size": NotRequired[int],
        "CreationTime": NotRequired[int],
        "LastModifiedTime": NotRequired[int],
        "Status": NotRequired[BillingGroupStatusType],
        "StatusReason": NotRequired[str],
        "AccountGrouping": NotRequired[ListBillingGroupAccountGroupingTypeDef],
    },
)
GetBillingGroupCostReportInputRequestTypeDef = TypedDict(
    "GetBillingGroupCostReportInputRequestTypeDef",
    {
        "Arn": str,
        "BillingPeriodRange": NotRequired[BillingPeriodRangeTypeDef],
        "GroupBy": NotRequired[Sequence[GroupByAttributeNameType]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
CreateTieringInputTypeDef = TypedDict(
    "CreateTieringInputTypeDef",
    {
        "FreeTier": CreateFreeTierConfigTypeDef,
    },
)
CustomLineItemChargeDetailsTypeDef = TypedDict(
    "CustomLineItemChargeDetailsTypeDef",
    {
        "Type": CustomLineItemTypeType,
        "Flat": NotRequired[CustomLineItemFlatChargeDetailsTypeDef],
        "Percentage": NotRequired[CustomLineItemPercentageChargeDetailsTypeDef],
        "LineItemFilters": NotRequired[Sequence[LineItemFilterTypeDef]],
    },
)
TieringTypeDef = TypedDict(
    "TieringTypeDef",
    {
        "FreeTier": FreeTierConfigTypeDef,
    },
)
ListAccountAssociationsInputRequestTypeDef = TypedDict(
    "ListAccountAssociationsInputRequestTypeDef",
    {
        "BillingPeriod": NotRequired[str],
        "Filters": NotRequired[ListAccountAssociationsFilterTypeDef],
        "NextToken": NotRequired[str],
    },
)
ListAccountAssociationsInputListAccountAssociationsPaginateTypeDef = TypedDict(
    "ListAccountAssociationsInputListAccountAssociationsPaginateTypeDef",
    {
        "BillingPeriod": NotRequired[str],
        "Filters": NotRequired[ListAccountAssociationsFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListPricingPlansAssociatedWithPricingRuleInputListPricingPlansAssociatedWithPricingRulePaginateTypeDef = TypedDict(
    "ListPricingPlansAssociatedWithPricingRuleInputListPricingPlansAssociatedWithPricingRulePaginateTypeDef",
    {
        "PricingRuleArn": str,
        "BillingPeriod": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListPricingRulesAssociatedToPricingPlanInputListPricingRulesAssociatedToPricingPlanPaginateTypeDef = TypedDict(
    "ListPricingRulesAssociatedToPricingPlanInputListPricingRulesAssociatedToPricingPlanPaginateTypeDef",
    {
        "PricingPlanArn": str,
        "BillingPeriod": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListBillingGroupCostReportsInputListBillingGroupCostReportsPaginateTypeDef = TypedDict(
    "ListBillingGroupCostReportsInputListBillingGroupCostReportsPaginateTypeDef",
    {
        "BillingPeriod": NotRequired[str],
        "Filters": NotRequired[ListBillingGroupCostReportsFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListBillingGroupCostReportsInputRequestTypeDef = TypedDict(
    "ListBillingGroupCostReportsInputRequestTypeDef",
    {
        "BillingPeriod": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "Filters": NotRequired[ListBillingGroupCostReportsFilterTypeDef],
    },
)
ListBillingGroupsInputListBillingGroupsPaginateTypeDef = TypedDict(
    "ListBillingGroupsInputListBillingGroupsPaginateTypeDef",
    {
        "BillingPeriod": NotRequired[str],
        "Filters": NotRequired[ListBillingGroupsFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListBillingGroupsInputRequestTypeDef = TypedDict(
    "ListBillingGroupsInputRequestTypeDef",
    {
        "BillingPeriod": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "Filters": NotRequired[ListBillingGroupsFilterTypeDef],
    },
)
ListCustomLineItemChargeDetailsPaginatorTypeDef = TypedDict(
    "ListCustomLineItemChargeDetailsPaginatorTypeDef",
    {
        "Type": CustomLineItemTypeType,
        "Flat": NotRequired[ListCustomLineItemFlatChargeDetailsTypeDef],
        "Percentage": NotRequired[ListCustomLineItemPercentageChargeDetailsTypeDef],
        "LineItemFilters": NotRequired[List[LineItemFilterPaginatorTypeDef]],
    },
)
ListCustomLineItemChargeDetailsTypeDef = TypedDict(
    "ListCustomLineItemChargeDetailsTypeDef",
    {
        "Type": CustomLineItemTypeType,
        "Flat": NotRequired[ListCustomLineItemFlatChargeDetailsTypeDef],
        "Percentage": NotRequired[ListCustomLineItemPercentageChargeDetailsTypeDef],
        "LineItemFilters": NotRequired[List[LineItemFilterTypeDef]],
    },
)
ListCustomLineItemVersionsFilterTypeDef = TypedDict(
    "ListCustomLineItemVersionsFilterTypeDef",
    {
        "BillingPeriodRange": NotRequired[
            ListCustomLineItemVersionsBillingPeriodRangeFilterTypeDef
        ],
    },
)
ListCustomLineItemsInputListCustomLineItemsPaginateTypeDef = TypedDict(
    "ListCustomLineItemsInputListCustomLineItemsPaginateTypeDef",
    {
        "BillingPeriod": NotRequired[str],
        "Filters": NotRequired[ListCustomLineItemsFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListCustomLineItemsInputRequestTypeDef = TypedDict(
    "ListCustomLineItemsInputRequestTypeDef",
    {
        "BillingPeriod": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "Filters": NotRequired[ListCustomLineItemsFilterTypeDef],
    },
)
ListPricingPlansInputListPricingPlansPaginateTypeDef = TypedDict(
    "ListPricingPlansInputListPricingPlansPaginateTypeDef",
    {
        "BillingPeriod": NotRequired[str],
        "Filters": NotRequired[ListPricingPlansFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListPricingPlansInputRequestTypeDef = TypedDict(
    "ListPricingPlansInputRequestTypeDef",
    {
        "BillingPeriod": NotRequired[str],
        "Filters": NotRequired[ListPricingPlansFilterTypeDef],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListPricingPlansOutputTypeDef = TypedDict(
    "ListPricingPlansOutputTypeDef",
    {
        "BillingPeriod": str,
        "PricingPlans": List[PricingPlanListElementTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListPricingRulesInputListPricingRulesPaginateTypeDef = TypedDict(
    "ListPricingRulesInputListPricingRulesPaginateTypeDef",
    {
        "BillingPeriod": NotRequired[str],
        "Filters": NotRequired[ListPricingRulesFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListPricingRulesInputRequestTypeDef = TypedDict(
    "ListPricingRulesInputRequestTypeDef",
    {
        "BillingPeriod": NotRequired[str],
        "Filters": NotRequired[ListPricingRulesFilterTypeDef],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListResourcesAssociatedToCustomLineItemInputListResourcesAssociatedToCustomLineItemPaginateTypeDef = TypedDict(
    "ListResourcesAssociatedToCustomLineItemInputListResourcesAssociatedToCustomLineItemPaginateTypeDef",
    {
        "Arn": str,
        "BillingPeriod": NotRequired[str],
        "Filters": NotRequired[ListResourcesAssociatedToCustomLineItemFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListResourcesAssociatedToCustomLineItemInputRequestTypeDef = TypedDict(
    "ListResourcesAssociatedToCustomLineItemInputRequestTypeDef",
    {
        "Arn": str,
        "BillingPeriod": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "Filters": NotRequired[ListResourcesAssociatedToCustomLineItemFilterTypeDef],
    },
)
ListResourcesAssociatedToCustomLineItemOutputTypeDef = TypedDict(
    "ListResourcesAssociatedToCustomLineItemOutputTypeDef",
    {
        "Arn": str,
        "AssociatedResources": List[ListResourcesAssociatedToCustomLineItemResponseElementTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateBillingGroupInputRequestTypeDef = TypedDict(
    "UpdateBillingGroupInputRequestTypeDef",
    {
        "Arn": str,
        "Name": NotRequired[str],
        "Status": NotRequired[BillingGroupStatusType],
        "ComputationPreference": NotRequired[ComputationPreferenceTypeDef],
        "Description": NotRequired[str],
        "AccountGrouping": NotRequired[UpdateBillingGroupAccountGroupingTypeDef],
    },
)
UpdateBillingGroupOutputTypeDef = TypedDict(
    "UpdateBillingGroupOutputTypeDef",
    {
        "Arn": str,
        "Name": str,
        "Description": str,
        "PrimaryAccountId": str,
        "PricingPlanArn": str,
        "Size": int,
        "LastModifiedTime": int,
        "Status": BillingGroupStatusType,
        "StatusReason": str,
        "AccountGrouping": UpdateBillingGroupAccountGroupingTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateCustomLineItemChargeDetailsTypeDef = TypedDict(
    "UpdateCustomLineItemChargeDetailsTypeDef",
    {
        "Flat": NotRequired[UpdateCustomLineItemFlatChargeDetailsTypeDef],
        "Percentage": NotRequired[UpdateCustomLineItemPercentageChargeDetailsTypeDef],
        "LineItemFilters": NotRequired[Sequence[LineItemFilterTypeDef]],
    },
)
UpdateTieringInputTypeDef = TypedDict(
    "UpdateTieringInputTypeDef",
    {
        "FreeTier": UpdateFreeTierConfigTypeDef,
    },
)
BatchAssociateResourcesToCustomLineItemOutputTypeDef = TypedDict(
    "BatchAssociateResourcesToCustomLineItemOutputTypeDef",
    {
        "SuccessfullyAssociatedResources": List[AssociateResourceResponseElementTypeDef],
        "FailedAssociatedResources": List[AssociateResourceResponseElementTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchDisassociateResourcesFromCustomLineItemOutputTypeDef = TypedDict(
    "BatchDisassociateResourcesFromCustomLineItemOutputTypeDef",
    {
        "SuccessfullyDisassociatedResources": List[DisassociateResourceResponseElementTypeDef],
        "FailedDisassociatedResources": List[DisassociateResourceResponseElementTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetBillingGroupCostReportOutputTypeDef = TypedDict(
    "GetBillingGroupCostReportOutputTypeDef",
    {
        "BillingGroupCostReportResults": List[BillingGroupCostReportResultElementTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListBillingGroupsOutputTypeDef = TypedDict(
    "ListBillingGroupsOutputTypeDef",
    {
        "BillingGroups": List[BillingGroupListElementTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreatePricingRuleInputRequestTypeDef = TypedDict(
    "CreatePricingRuleInputRequestTypeDef",
    {
        "Name": str,
        "Scope": PricingRuleScopeType,
        "Type": PricingRuleTypeType,
        "ClientToken": NotRequired[str],
        "Description": NotRequired[str],
        "ModifierPercentage": NotRequired[float],
        "Service": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
        "BillingEntity": NotRequired[str],
        "Tiering": NotRequired[CreateTieringInputTypeDef],
        "UsageType": NotRequired[str],
        "Operation": NotRequired[str],
    },
)
CreateCustomLineItemInputRequestTypeDef = TypedDict(
    "CreateCustomLineItemInputRequestTypeDef",
    {
        "Name": str,
        "Description": str,
        "BillingGroupArn": str,
        "ChargeDetails": CustomLineItemChargeDetailsTypeDef,
        "ClientToken": NotRequired[str],
        "BillingPeriodRange": NotRequired[CustomLineItemBillingPeriodRangeTypeDef],
        "Tags": NotRequired[Mapping[str, str]],
        "AccountId": NotRequired[str],
    },
)
PricingRuleListElementTypeDef = TypedDict(
    "PricingRuleListElementTypeDef",
    {
        "Name": NotRequired[str],
        "Arn": NotRequired[str],
        "Description": NotRequired[str],
        "Scope": NotRequired[PricingRuleScopeType],
        "Type": NotRequired[PricingRuleTypeType],
        "ModifierPercentage": NotRequired[float],
        "Service": NotRequired[str],
        "AssociatedPricingPlanCount": NotRequired[int],
        "CreationTime": NotRequired[int],
        "LastModifiedTime": NotRequired[int],
        "BillingEntity": NotRequired[str],
        "Tiering": NotRequired[TieringTypeDef],
        "UsageType": NotRequired[str],
        "Operation": NotRequired[str],
    },
)
CustomLineItemListElementPaginatorTypeDef = TypedDict(
    "CustomLineItemListElementPaginatorTypeDef",
    {
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
        "ChargeDetails": NotRequired[ListCustomLineItemChargeDetailsPaginatorTypeDef],
        "CurrencyCode": NotRequired[CurrencyCodeType],
        "Description": NotRequired[str],
        "ProductCode": NotRequired[str],
        "BillingGroupArn": NotRequired[str],
        "CreationTime": NotRequired[int],
        "LastModifiedTime": NotRequired[int],
        "AssociationSize": NotRequired[int],
        "AccountId": NotRequired[str],
    },
)
CustomLineItemVersionListElementPaginatorTypeDef = TypedDict(
    "CustomLineItemVersionListElementPaginatorTypeDef",
    {
        "Name": NotRequired[str],
        "ChargeDetails": NotRequired[ListCustomLineItemChargeDetailsPaginatorTypeDef],
        "CurrencyCode": NotRequired[CurrencyCodeType],
        "Description": NotRequired[str],
        "ProductCode": NotRequired[str],
        "BillingGroupArn": NotRequired[str],
        "CreationTime": NotRequired[int],
        "LastModifiedTime": NotRequired[int],
        "AssociationSize": NotRequired[int],
        "StartBillingPeriod": NotRequired[str],
        "EndBillingPeriod": NotRequired[str],
        "Arn": NotRequired[str],
        "StartTime": NotRequired[int],
        "AccountId": NotRequired[str],
    },
)
CustomLineItemListElementTypeDef = TypedDict(
    "CustomLineItemListElementTypeDef",
    {
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
        "ChargeDetails": NotRequired[ListCustomLineItemChargeDetailsTypeDef],
        "CurrencyCode": NotRequired[CurrencyCodeType],
        "Description": NotRequired[str],
        "ProductCode": NotRequired[str],
        "BillingGroupArn": NotRequired[str],
        "CreationTime": NotRequired[int],
        "LastModifiedTime": NotRequired[int],
        "AssociationSize": NotRequired[int],
        "AccountId": NotRequired[str],
    },
)
CustomLineItemVersionListElementTypeDef = TypedDict(
    "CustomLineItemVersionListElementTypeDef",
    {
        "Name": NotRequired[str],
        "ChargeDetails": NotRequired[ListCustomLineItemChargeDetailsTypeDef],
        "CurrencyCode": NotRequired[CurrencyCodeType],
        "Description": NotRequired[str],
        "ProductCode": NotRequired[str],
        "BillingGroupArn": NotRequired[str],
        "CreationTime": NotRequired[int],
        "LastModifiedTime": NotRequired[int],
        "AssociationSize": NotRequired[int],
        "StartBillingPeriod": NotRequired[str],
        "EndBillingPeriod": NotRequired[str],
        "Arn": NotRequired[str],
        "StartTime": NotRequired[int],
        "AccountId": NotRequired[str],
    },
)
UpdateCustomLineItemOutputTypeDef = TypedDict(
    "UpdateCustomLineItemOutputTypeDef",
    {
        "Arn": str,
        "BillingGroupArn": str,
        "Name": str,
        "Description": str,
        "ChargeDetails": ListCustomLineItemChargeDetailsTypeDef,
        "LastModifiedTime": int,
        "AssociationSize": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListCustomLineItemVersionsInputListCustomLineItemVersionsPaginateTypeDef = TypedDict(
    "ListCustomLineItemVersionsInputListCustomLineItemVersionsPaginateTypeDef",
    {
        "Arn": str,
        "Filters": NotRequired[ListCustomLineItemVersionsFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListCustomLineItemVersionsInputRequestTypeDef = TypedDict(
    "ListCustomLineItemVersionsInputRequestTypeDef",
    {
        "Arn": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "Filters": NotRequired[ListCustomLineItemVersionsFilterTypeDef],
    },
)
UpdateCustomLineItemInputRequestTypeDef = TypedDict(
    "UpdateCustomLineItemInputRequestTypeDef",
    {
        "Arn": str,
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "ChargeDetails": NotRequired[UpdateCustomLineItemChargeDetailsTypeDef],
        "BillingPeriodRange": NotRequired[CustomLineItemBillingPeriodRangeTypeDef],
    },
)
UpdatePricingRuleInputRequestTypeDef = TypedDict(
    "UpdatePricingRuleInputRequestTypeDef",
    {
        "Arn": str,
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "Type": NotRequired[PricingRuleTypeType],
        "ModifierPercentage": NotRequired[float],
        "Tiering": NotRequired[UpdateTieringInputTypeDef],
    },
)
UpdatePricingRuleOutputTypeDef = TypedDict(
    "UpdatePricingRuleOutputTypeDef",
    {
        "Arn": str,
        "Name": str,
        "Description": str,
        "Scope": PricingRuleScopeType,
        "Type": PricingRuleTypeType,
        "ModifierPercentage": float,
        "Service": str,
        "AssociatedPricingPlanCount": int,
        "LastModifiedTime": int,
        "BillingEntity": str,
        "Tiering": UpdateTieringInputTypeDef,
        "UsageType": str,
        "Operation": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListPricingRulesOutputTypeDef = TypedDict(
    "ListPricingRulesOutputTypeDef",
    {
        "BillingPeriod": str,
        "PricingRules": List[PricingRuleListElementTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListCustomLineItemsOutputPaginatorTypeDef = TypedDict(
    "ListCustomLineItemsOutputPaginatorTypeDef",
    {
        "CustomLineItems": List[CustomLineItemListElementPaginatorTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListCustomLineItemVersionsOutputPaginatorTypeDef = TypedDict(
    "ListCustomLineItemVersionsOutputPaginatorTypeDef",
    {
        "CustomLineItemVersions": List[CustomLineItemVersionListElementPaginatorTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListCustomLineItemsOutputTypeDef = TypedDict(
    "ListCustomLineItemsOutputTypeDef",
    {
        "CustomLineItems": List[CustomLineItemListElementTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListCustomLineItemVersionsOutputTypeDef = TypedDict(
    "ListCustomLineItemVersionsOutputTypeDef",
    {
        "CustomLineItemVersions": List[CustomLineItemVersionListElementTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
