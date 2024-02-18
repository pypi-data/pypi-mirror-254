"""
Type annotations for fms service type definitions.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_fms/type_defs/)

Usage::

    ```python
    from types_aiobotocore_fms.type_defs import AccountScopeTypeDef

    data: AccountScopeTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Sequence, Union

from .literals import (
    AccountRoleStatusType,
    CustomerPolicyScopeIdTypeType,
    CustomerPolicyStatusType,
    DependentServiceNameType,
    DestinationTypeType,
    FailedItemReasonType,
    FirewallDeploymentModelType,
    MarketplaceSubscriptionOnboardingStatusType,
    OrganizationStatusType,
    PolicyComplianceStatusTypeType,
    RemediationActionTypeType,
    ResourceSetStatusType,
    RuleOrderType,
    SecurityServiceTypeType,
    TargetTypeType,
    ThirdPartyFirewallAssociationStatusType,
    ThirdPartyFirewallType,
    ViolationReasonType,
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
    "AccountScopeTypeDef",
    "ActionTargetTypeDef",
    "AdminAccountSummaryTypeDef",
    "OrganizationalUnitScopeTypeDef",
    "PolicyTypeScopeTypeDef",
    "RegionScopeTypeDef",
    "AppTypeDef",
    "AssociateAdminAccountRequestRequestTypeDef",
    "AssociateThirdPartyFirewallRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "AwsEc2NetworkInterfaceViolationTypeDef",
    "PartialMatchTypeDef",
    "BatchAssociateResourceRequestRequestTypeDef",
    "FailedItemTypeDef",
    "BatchDisassociateResourceRequestRequestTypeDef",
    "ComplianceViolatorTypeDef",
    "DeleteAppsListRequestRequestTypeDef",
    "DeletePolicyRequestRequestTypeDef",
    "DeleteProtocolsListRequestRequestTypeDef",
    "DeleteResourceSetRequestRequestTypeDef",
    "DisassociateThirdPartyFirewallRequestRequestTypeDef",
    "DiscoveredResourceTypeDef",
    "DnsDuplicateRuleGroupViolationTypeDef",
    "DnsRuleGroupLimitExceededViolationTypeDef",
    "DnsRuleGroupPriorityConflictViolationTypeDef",
    "EvaluationResultTypeDef",
    "ExpectedRouteTypeDef",
    "FMSPolicyUpdateFirewallCreationConfigActionTypeDef",
    "FirewallSubnetIsOutOfScopeViolationTypeDef",
    "FirewallSubnetMissingVPCEndpointViolationTypeDef",
    "GetAdminScopeRequestRequestTypeDef",
    "GetAppsListRequestRequestTypeDef",
    "GetComplianceDetailRequestRequestTypeDef",
    "GetPolicyRequestRequestTypeDef",
    "TimestampTypeDef",
    "GetProtocolsListRequestRequestTypeDef",
    "ProtocolsListDataTypeDef",
    "GetResourceSetRequestRequestTypeDef",
    "ResourceSetTypeDef",
    "GetThirdPartyFirewallAssociationStatusRequestRequestTypeDef",
    "GetViolationDetailsRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "ListAdminAccountsForOrganizationRequestRequestTypeDef",
    "ListAdminsManagingAccountRequestRequestTypeDef",
    "ListAppsListsRequestRequestTypeDef",
    "ListComplianceStatusRequestRequestTypeDef",
    "ListDiscoveredResourcesRequestRequestTypeDef",
    "ListMemberAccountsRequestRequestTypeDef",
    "ListPoliciesRequestRequestTypeDef",
    "PolicySummaryTypeDef",
    "ListProtocolsListsRequestRequestTypeDef",
    "ProtocolsListDataSummaryTypeDef",
    "ListResourceSetResourcesRequestRequestTypeDef",
    "ResourceTypeDef",
    "ListResourceSetsRequestRequestTypeDef",
    "ResourceSetSummaryTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "TagTypeDef",
    "ListThirdPartyFirewallFirewallPoliciesRequestRequestTypeDef",
    "ThirdPartyFirewallFirewallPolicyTypeDef",
    "RouteTypeDef",
    "NetworkFirewallMissingExpectedRTViolationTypeDef",
    "NetworkFirewallMissingFirewallViolationTypeDef",
    "NetworkFirewallMissingSubnetViolationTypeDef",
    "StatefulEngineOptionsTypeDef",
    "StatelessRuleGroupTypeDef",
    "NetworkFirewallPolicyTypeDef",
    "NetworkFirewallStatefulRuleGroupOverrideTypeDef",
    "ThirdPartyFirewallPolicyTypeDef",
    "ResourceTagTypeDef",
    "PutNotificationChannelRequestRequestTypeDef",
    "ThirdPartyFirewallMissingExpectedRouteTableViolationTypeDef",
    "ThirdPartyFirewallMissingFirewallViolationTypeDef",
    "ThirdPartyFirewallMissingSubnetViolationTypeDef",
    "SecurityGroupRuleDescriptionTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "EC2AssociateRouteTableActionTypeDef",
    "EC2CopyRouteTableActionTypeDef",
    "EC2CreateRouteActionTypeDef",
    "EC2CreateRouteTableActionTypeDef",
    "EC2DeleteRouteActionTypeDef",
    "EC2ReplaceRouteActionTypeDef",
    "EC2ReplaceRouteTableAssociationActionTypeDef",
    "AdminScopeTypeDef",
    "AppsListDataSummaryTypeDef",
    "AppsListDataTypeDef",
    "AssociateThirdPartyFirewallResponseTypeDef",
    "DisassociateThirdPartyFirewallResponseTypeDef",
    "EmptyResponseMetadataTypeDef",
    "GetAdminAccountResponseTypeDef",
    "GetNotificationChannelResponseTypeDef",
    "GetProtectionStatusResponseTypeDef",
    "GetThirdPartyFirewallAssociationStatusResponseTypeDef",
    "ListAdminAccountsForOrganizationResponseTypeDef",
    "ListAdminsManagingAccountResponseTypeDef",
    "ListMemberAccountsResponseTypeDef",
    "AwsEc2InstanceViolationTypeDef",
    "BatchAssociateResourceResponseTypeDef",
    "BatchDisassociateResourceResponseTypeDef",
    "PolicyComplianceDetailTypeDef",
    "ListDiscoveredResourcesResponseTypeDef",
    "PolicyComplianceStatusTypeDef",
    "NetworkFirewallMissingExpectedRoutesViolationTypeDef",
    "GetProtectionStatusRequestRequestTypeDef",
    "GetProtocolsListResponseTypeDef",
    "PutProtocolsListResponseTypeDef",
    "GetResourceSetResponseTypeDef",
    "PutResourceSetResponseTypeDef",
    "ListAdminAccountsForOrganizationRequestListAdminAccountsForOrganizationPaginateTypeDef",
    "ListAdminsManagingAccountRequestListAdminsManagingAccountPaginateTypeDef",
    "ListAppsListsRequestListAppsListsPaginateTypeDef",
    "ListComplianceStatusRequestListComplianceStatusPaginateTypeDef",
    "ListMemberAccountsRequestListMemberAccountsPaginateTypeDef",
    "ListPoliciesRequestListPoliciesPaginateTypeDef",
    "ListProtocolsListsRequestListProtocolsListsPaginateTypeDef",
    "ListThirdPartyFirewallFirewallPoliciesRequestListThirdPartyFirewallFirewallPoliciesPaginateTypeDef",
    "ListPoliciesResponseTypeDef",
    "ListProtocolsListsResponseTypeDef",
    "ListResourceSetResourcesResponseTypeDef",
    "ListResourceSetsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PutProtocolsListRequestRequestTypeDef",
    "PutResourceSetRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "ListThirdPartyFirewallFirewallPoliciesResponseTypeDef",
    "NetworkFirewallBlackHoleRouteDetectedViolationTypeDef",
    "NetworkFirewallInternetTrafficNotInspectedViolationTypeDef",
    "NetworkFirewallInvalidRouteConfigurationViolationTypeDef",
    "NetworkFirewallUnexpectedFirewallRoutesViolationTypeDef",
    "NetworkFirewallUnexpectedGatewayRoutesViolationTypeDef",
    "RouteHasOutOfScopeEndpointViolationTypeDef",
    "StatefulRuleGroupTypeDef",
    "PolicyOptionTypeDef",
    "SecurityGroupRemediationActionTypeDef",
    "RemediationActionTypeDef",
    "GetAdminScopeResponseTypeDef",
    "PutAdminAccountRequestRequestTypeDef",
    "ListAppsListsResponseTypeDef",
    "GetAppsListResponseTypeDef",
    "PutAppsListRequestRequestTypeDef",
    "PutAppsListResponseTypeDef",
    "GetComplianceDetailResponseTypeDef",
    "ListComplianceStatusResponseTypeDef",
    "NetworkFirewallPolicyDescriptionTypeDef",
    "SecurityServicePolicyDataTypeDef",
    "AwsVPCSecurityGroupViolationTypeDef",
    "RemediationActionWithOrderTypeDef",
    "NetworkFirewallPolicyModifiedViolationTypeDef",
    "PolicyTypeDef",
    "PossibleRemediationActionTypeDef",
    "GetPolicyResponseTypeDef",
    "PutPolicyRequestRequestTypeDef",
    "PutPolicyResponseTypeDef",
    "PossibleRemediationActionsTypeDef",
    "ResourceViolationTypeDef",
    "ViolationDetailTypeDef",
    "GetViolationDetailsResponseTypeDef",
)

AccountScopeTypeDef = TypedDict(
    "AccountScopeTypeDef",
    {
        "Accounts": NotRequired[List[str]],
        "AllAccountsEnabled": NotRequired[bool],
        "ExcludeSpecifiedAccounts": NotRequired[bool],
    },
)
ActionTargetTypeDef = TypedDict(
    "ActionTargetTypeDef",
    {
        "ResourceId": NotRequired[str],
        "Description": NotRequired[str],
    },
)
AdminAccountSummaryTypeDef = TypedDict(
    "AdminAccountSummaryTypeDef",
    {
        "AdminAccount": NotRequired[str],
        "DefaultAdmin": NotRequired[bool],
        "Status": NotRequired[OrganizationStatusType],
    },
)
OrganizationalUnitScopeTypeDef = TypedDict(
    "OrganizationalUnitScopeTypeDef",
    {
        "OrganizationalUnits": NotRequired[List[str]],
        "AllOrganizationalUnitsEnabled": NotRequired[bool],
        "ExcludeSpecifiedOrganizationalUnits": NotRequired[bool],
    },
)
PolicyTypeScopeTypeDef = TypedDict(
    "PolicyTypeScopeTypeDef",
    {
        "PolicyTypes": NotRequired[List[SecurityServiceTypeType]],
        "AllPolicyTypesEnabled": NotRequired[bool],
    },
)
RegionScopeTypeDef = TypedDict(
    "RegionScopeTypeDef",
    {
        "Regions": NotRequired[List[str]],
        "AllRegionsEnabled": NotRequired[bool],
    },
)
AppTypeDef = TypedDict(
    "AppTypeDef",
    {
        "AppName": str,
        "Protocol": str,
        "Port": int,
    },
)
AssociateAdminAccountRequestRequestTypeDef = TypedDict(
    "AssociateAdminAccountRequestRequestTypeDef",
    {
        "AdminAccount": str,
    },
)
AssociateThirdPartyFirewallRequestRequestTypeDef = TypedDict(
    "AssociateThirdPartyFirewallRequestRequestTypeDef",
    {
        "ThirdPartyFirewall": ThirdPartyFirewallType,
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
AwsEc2NetworkInterfaceViolationTypeDef = TypedDict(
    "AwsEc2NetworkInterfaceViolationTypeDef",
    {
        "ViolationTarget": NotRequired[str],
        "ViolatingSecurityGroups": NotRequired[List[str]],
    },
)
PartialMatchTypeDef = TypedDict(
    "PartialMatchTypeDef",
    {
        "Reference": NotRequired[str],
        "TargetViolationReasons": NotRequired[List[str]],
    },
)
BatchAssociateResourceRequestRequestTypeDef = TypedDict(
    "BatchAssociateResourceRequestRequestTypeDef",
    {
        "ResourceSetIdentifier": str,
        "Items": Sequence[str],
    },
)
FailedItemTypeDef = TypedDict(
    "FailedItemTypeDef",
    {
        "URI": NotRequired[str],
        "Reason": NotRequired[FailedItemReasonType],
    },
)
BatchDisassociateResourceRequestRequestTypeDef = TypedDict(
    "BatchDisassociateResourceRequestRequestTypeDef",
    {
        "ResourceSetIdentifier": str,
        "Items": Sequence[str],
    },
)
ComplianceViolatorTypeDef = TypedDict(
    "ComplianceViolatorTypeDef",
    {
        "ResourceId": NotRequired[str],
        "ViolationReason": NotRequired[ViolationReasonType],
        "ResourceType": NotRequired[str],
        "Metadata": NotRequired[Dict[str, str]],
    },
)
DeleteAppsListRequestRequestTypeDef = TypedDict(
    "DeleteAppsListRequestRequestTypeDef",
    {
        "ListId": str,
    },
)
DeletePolicyRequestRequestTypeDef = TypedDict(
    "DeletePolicyRequestRequestTypeDef",
    {
        "PolicyId": str,
        "DeleteAllPolicyResources": NotRequired[bool],
    },
)
DeleteProtocolsListRequestRequestTypeDef = TypedDict(
    "DeleteProtocolsListRequestRequestTypeDef",
    {
        "ListId": str,
    },
)
DeleteResourceSetRequestRequestTypeDef = TypedDict(
    "DeleteResourceSetRequestRequestTypeDef",
    {
        "Identifier": str,
    },
)
DisassociateThirdPartyFirewallRequestRequestTypeDef = TypedDict(
    "DisassociateThirdPartyFirewallRequestRequestTypeDef",
    {
        "ThirdPartyFirewall": ThirdPartyFirewallType,
    },
)
DiscoveredResourceTypeDef = TypedDict(
    "DiscoveredResourceTypeDef",
    {
        "URI": NotRequired[str],
        "AccountId": NotRequired[str],
        "Type": NotRequired[str],
        "Name": NotRequired[str],
    },
)
DnsDuplicateRuleGroupViolationTypeDef = TypedDict(
    "DnsDuplicateRuleGroupViolationTypeDef",
    {
        "ViolationTarget": NotRequired[str],
        "ViolationTargetDescription": NotRequired[str],
    },
)
DnsRuleGroupLimitExceededViolationTypeDef = TypedDict(
    "DnsRuleGroupLimitExceededViolationTypeDef",
    {
        "ViolationTarget": NotRequired[str],
        "ViolationTargetDescription": NotRequired[str],
        "NumberOfRuleGroupsAlreadyAssociated": NotRequired[int],
    },
)
DnsRuleGroupPriorityConflictViolationTypeDef = TypedDict(
    "DnsRuleGroupPriorityConflictViolationTypeDef",
    {
        "ViolationTarget": NotRequired[str],
        "ViolationTargetDescription": NotRequired[str],
        "ConflictingPriority": NotRequired[int],
        "ConflictingPolicyId": NotRequired[str],
        "UnavailablePriorities": NotRequired[List[int]],
    },
)
EvaluationResultTypeDef = TypedDict(
    "EvaluationResultTypeDef",
    {
        "ComplianceStatus": NotRequired[PolicyComplianceStatusTypeType],
        "ViolatorCount": NotRequired[int],
        "EvaluationLimitExceeded": NotRequired[bool],
    },
)
ExpectedRouteTypeDef = TypedDict(
    "ExpectedRouteTypeDef",
    {
        "IpV4Cidr": NotRequired[str],
        "PrefixListId": NotRequired[str],
        "IpV6Cidr": NotRequired[str],
        "ContributingSubnets": NotRequired[List[str]],
        "AllowedTargets": NotRequired[List[str]],
        "RouteTableId": NotRequired[str],
    },
)
FMSPolicyUpdateFirewallCreationConfigActionTypeDef = TypedDict(
    "FMSPolicyUpdateFirewallCreationConfigActionTypeDef",
    {
        "Description": NotRequired[str],
        "FirewallCreationConfig": NotRequired[str],
    },
)
FirewallSubnetIsOutOfScopeViolationTypeDef = TypedDict(
    "FirewallSubnetIsOutOfScopeViolationTypeDef",
    {
        "FirewallSubnetId": NotRequired[str],
        "VpcId": NotRequired[str],
        "SubnetAvailabilityZone": NotRequired[str],
        "SubnetAvailabilityZoneId": NotRequired[str],
        "VpcEndpointId": NotRequired[str],
    },
)
FirewallSubnetMissingVPCEndpointViolationTypeDef = TypedDict(
    "FirewallSubnetMissingVPCEndpointViolationTypeDef",
    {
        "FirewallSubnetId": NotRequired[str],
        "VpcId": NotRequired[str],
        "SubnetAvailabilityZone": NotRequired[str],
        "SubnetAvailabilityZoneId": NotRequired[str],
    },
)
GetAdminScopeRequestRequestTypeDef = TypedDict(
    "GetAdminScopeRequestRequestTypeDef",
    {
        "AdminAccount": str,
    },
)
GetAppsListRequestRequestTypeDef = TypedDict(
    "GetAppsListRequestRequestTypeDef",
    {
        "ListId": str,
        "DefaultList": NotRequired[bool],
    },
)
GetComplianceDetailRequestRequestTypeDef = TypedDict(
    "GetComplianceDetailRequestRequestTypeDef",
    {
        "PolicyId": str,
        "MemberAccount": str,
    },
)
GetPolicyRequestRequestTypeDef = TypedDict(
    "GetPolicyRequestRequestTypeDef",
    {
        "PolicyId": str,
    },
)
TimestampTypeDef = Union[datetime, str]
GetProtocolsListRequestRequestTypeDef = TypedDict(
    "GetProtocolsListRequestRequestTypeDef",
    {
        "ListId": str,
        "DefaultList": NotRequired[bool],
    },
)
ProtocolsListDataTypeDef = TypedDict(
    "ProtocolsListDataTypeDef",
    {
        "ListName": str,
        "ProtocolsList": List[str],
        "ListId": NotRequired[str],
        "ListUpdateToken": NotRequired[str],
        "CreateTime": NotRequired[datetime],
        "LastUpdateTime": NotRequired[datetime],
        "PreviousProtocolsList": NotRequired[Dict[str, List[str]]],
    },
)
GetResourceSetRequestRequestTypeDef = TypedDict(
    "GetResourceSetRequestRequestTypeDef",
    {
        "Identifier": str,
    },
)
ResourceSetTypeDef = TypedDict(
    "ResourceSetTypeDef",
    {
        "Name": str,
        "ResourceTypeList": List[str],
        "Id": NotRequired[str],
        "Description": NotRequired[str],
        "UpdateToken": NotRequired[str],
        "LastUpdateTime": NotRequired[datetime],
        "ResourceSetStatus": NotRequired[ResourceSetStatusType],
    },
)
GetThirdPartyFirewallAssociationStatusRequestRequestTypeDef = TypedDict(
    "GetThirdPartyFirewallAssociationStatusRequestRequestTypeDef",
    {
        "ThirdPartyFirewall": ThirdPartyFirewallType,
    },
)
GetViolationDetailsRequestRequestTypeDef = TypedDict(
    "GetViolationDetailsRequestRequestTypeDef",
    {
        "PolicyId": str,
        "MemberAccount": str,
        "ResourceId": str,
        "ResourceType": str,
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
ListAdminAccountsForOrganizationRequestRequestTypeDef = TypedDict(
    "ListAdminAccountsForOrganizationRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListAdminsManagingAccountRequestRequestTypeDef = TypedDict(
    "ListAdminsManagingAccountRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListAppsListsRequestRequestTypeDef = TypedDict(
    "ListAppsListsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "DefaultLists": NotRequired[bool],
        "NextToken": NotRequired[str],
    },
)
ListComplianceStatusRequestRequestTypeDef = TypedDict(
    "ListComplianceStatusRequestRequestTypeDef",
    {
        "PolicyId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListDiscoveredResourcesRequestRequestTypeDef = TypedDict(
    "ListDiscoveredResourcesRequestRequestTypeDef",
    {
        "MemberAccountIds": Sequence[str],
        "ResourceType": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListMemberAccountsRequestRequestTypeDef = TypedDict(
    "ListMemberAccountsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListPoliciesRequestRequestTypeDef = TypedDict(
    "ListPoliciesRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
PolicySummaryTypeDef = TypedDict(
    "PolicySummaryTypeDef",
    {
        "PolicyArn": NotRequired[str],
        "PolicyId": NotRequired[str],
        "PolicyName": NotRequired[str],
        "ResourceType": NotRequired[str],
        "SecurityServiceType": NotRequired[SecurityServiceTypeType],
        "RemediationEnabled": NotRequired[bool],
        "DeleteUnusedFMManagedResources": NotRequired[bool],
        "PolicyStatus": NotRequired[CustomerPolicyStatusType],
    },
)
ListProtocolsListsRequestRequestTypeDef = TypedDict(
    "ListProtocolsListsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "DefaultLists": NotRequired[bool],
        "NextToken": NotRequired[str],
    },
)
ProtocolsListDataSummaryTypeDef = TypedDict(
    "ProtocolsListDataSummaryTypeDef",
    {
        "ListArn": NotRequired[str],
        "ListId": NotRequired[str],
        "ListName": NotRequired[str],
        "ProtocolsList": NotRequired[List[str]],
    },
)
ListResourceSetResourcesRequestRequestTypeDef = TypedDict(
    "ListResourceSetResourcesRequestRequestTypeDef",
    {
        "Identifier": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ResourceTypeDef = TypedDict(
    "ResourceTypeDef",
    {
        "URI": str,
        "AccountId": NotRequired[str],
    },
)
ListResourceSetsRequestRequestTypeDef = TypedDict(
    "ListResourceSetsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ResourceSetSummaryTypeDef = TypedDict(
    "ResourceSetSummaryTypeDef",
    {
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "LastUpdateTime": NotRequired[datetime],
        "ResourceSetStatus": NotRequired[ResourceSetStatusType],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)
ListThirdPartyFirewallFirewallPoliciesRequestRequestTypeDef = TypedDict(
    "ListThirdPartyFirewallFirewallPoliciesRequestRequestTypeDef",
    {
        "ThirdPartyFirewall": ThirdPartyFirewallType,
        "MaxResults": int,
        "NextToken": NotRequired[str],
    },
)
ThirdPartyFirewallFirewallPolicyTypeDef = TypedDict(
    "ThirdPartyFirewallFirewallPolicyTypeDef",
    {
        "FirewallPolicyId": NotRequired[str],
        "FirewallPolicyName": NotRequired[str],
    },
)
RouteTypeDef = TypedDict(
    "RouteTypeDef",
    {
        "DestinationType": NotRequired[DestinationTypeType],
        "TargetType": NotRequired[TargetTypeType],
        "Destination": NotRequired[str],
        "Target": NotRequired[str],
    },
)
NetworkFirewallMissingExpectedRTViolationTypeDef = TypedDict(
    "NetworkFirewallMissingExpectedRTViolationTypeDef",
    {
        "ViolationTarget": NotRequired[str],
        "VPC": NotRequired[str],
        "AvailabilityZone": NotRequired[str],
        "CurrentRouteTable": NotRequired[str],
        "ExpectedRouteTable": NotRequired[str],
    },
)
NetworkFirewallMissingFirewallViolationTypeDef = TypedDict(
    "NetworkFirewallMissingFirewallViolationTypeDef",
    {
        "ViolationTarget": NotRequired[str],
        "VPC": NotRequired[str],
        "AvailabilityZone": NotRequired[str],
        "TargetViolationReason": NotRequired[str],
    },
)
NetworkFirewallMissingSubnetViolationTypeDef = TypedDict(
    "NetworkFirewallMissingSubnetViolationTypeDef",
    {
        "ViolationTarget": NotRequired[str],
        "VPC": NotRequired[str],
        "AvailabilityZone": NotRequired[str],
        "TargetViolationReason": NotRequired[str],
    },
)
StatefulEngineOptionsTypeDef = TypedDict(
    "StatefulEngineOptionsTypeDef",
    {
        "RuleOrder": NotRequired[RuleOrderType],
    },
)
StatelessRuleGroupTypeDef = TypedDict(
    "StatelessRuleGroupTypeDef",
    {
        "RuleGroupName": NotRequired[str],
        "ResourceId": NotRequired[str],
        "Priority": NotRequired[int],
    },
)
NetworkFirewallPolicyTypeDef = TypedDict(
    "NetworkFirewallPolicyTypeDef",
    {
        "FirewallDeploymentModel": NotRequired[FirewallDeploymentModelType],
    },
)
NetworkFirewallStatefulRuleGroupOverrideTypeDef = TypedDict(
    "NetworkFirewallStatefulRuleGroupOverrideTypeDef",
    {
        "Action": NotRequired[Literal["DROP_TO_ALERT"]],
    },
)
ThirdPartyFirewallPolicyTypeDef = TypedDict(
    "ThirdPartyFirewallPolicyTypeDef",
    {
        "FirewallDeploymentModel": NotRequired[FirewallDeploymentModelType],
    },
)
ResourceTagTypeDef = TypedDict(
    "ResourceTagTypeDef",
    {
        "Key": str,
        "Value": NotRequired[str],
    },
)
PutNotificationChannelRequestRequestTypeDef = TypedDict(
    "PutNotificationChannelRequestRequestTypeDef",
    {
        "SnsTopicArn": str,
        "SnsRoleName": str,
    },
)
ThirdPartyFirewallMissingExpectedRouteTableViolationTypeDef = TypedDict(
    "ThirdPartyFirewallMissingExpectedRouteTableViolationTypeDef",
    {
        "ViolationTarget": NotRequired[str],
        "VPC": NotRequired[str],
        "AvailabilityZone": NotRequired[str],
        "CurrentRouteTable": NotRequired[str],
        "ExpectedRouteTable": NotRequired[str],
    },
)
ThirdPartyFirewallMissingFirewallViolationTypeDef = TypedDict(
    "ThirdPartyFirewallMissingFirewallViolationTypeDef",
    {
        "ViolationTarget": NotRequired[str],
        "VPC": NotRequired[str],
        "AvailabilityZone": NotRequired[str],
        "TargetViolationReason": NotRequired[str],
    },
)
ThirdPartyFirewallMissingSubnetViolationTypeDef = TypedDict(
    "ThirdPartyFirewallMissingSubnetViolationTypeDef",
    {
        "ViolationTarget": NotRequired[str],
        "VPC": NotRequired[str],
        "AvailabilityZone": NotRequired[str],
        "TargetViolationReason": NotRequired[str],
    },
)
SecurityGroupRuleDescriptionTypeDef = TypedDict(
    "SecurityGroupRuleDescriptionTypeDef",
    {
        "IPV4Range": NotRequired[str],
        "IPV6Range": NotRequired[str],
        "PrefixListId": NotRequired[str],
        "Protocol": NotRequired[str],
        "FromPort": NotRequired[int],
        "ToPort": NotRequired[int],
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)
EC2AssociateRouteTableActionTypeDef = TypedDict(
    "EC2AssociateRouteTableActionTypeDef",
    {
        "RouteTableId": ActionTargetTypeDef,
        "Description": NotRequired[str],
        "SubnetId": NotRequired[ActionTargetTypeDef],
        "GatewayId": NotRequired[ActionTargetTypeDef],
    },
)
EC2CopyRouteTableActionTypeDef = TypedDict(
    "EC2CopyRouteTableActionTypeDef",
    {
        "VpcId": ActionTargetTypeDef,
        "RouteTableId": ActionTargetTypeDef,
        "Description": NotRequired[str],
    },
)
EC2CreateRouteActionTypeDef = TypedDict(
    "EC2CreateRouteActionTypeDef",
    {
        "RouteTableId": ActionTargetTypeDef,
        "Description": NotRequired[str],
        "DestinationCidrBlock": NotRequired[str],
        "DestinationPrefixListId": NotRequired[str],
        "DestinationIpv6CidrBlock": NotRequired[str],
        "VpcEndpointId": NotRequired[ActionTargetTypeDef],
        "GatewayId": NotRequired[ActionTargetTypeDef],
    },
)
EC2CreateRouteTableActionTypeDef = TypedDict(
    "EC2CreateRouteTableActionTypeDef",
    {
        "VpcId": ActionTargetTypeDef,
        "Description": NotRequired[str],
    },
)
EC2DeleteRouteActionTypeDef = TypedDict(
    "EC2DeleteRouteActionTypeDef",
    {
        "RouteTableId": ActionTargetTypeDef,
        "Description": NotRequired[str],
        "DestinationCidrBlock": NotRequired[str],
        "DestinationPrefixListId": NotRequired[str],
        "DestinationIpv6CidrBlock": NotRequired[str],
    },
)
EC2ReplaceRouteActionTypeDef = TypedDict(
    "EC2ReplaceRouteActionTypeDef",
    {
        "RouteTableId": ActionTargetTypeDef,
        "Description": NotRequired[str],
        "DestinationCidrBlock": NotRequired[str],
        "DestinationPrefixListId": NotRequired[str],
        "DestinationIpv6CidrBlock": NotRequired[str],
        "GatewayId": NotRequired[ActionTargetTypeDef],
    },
)
EC2ReplaceRouteTableAssociationActionTypeDef = TypedDict(
    "EC2ReplaceRouteTableAssociationActionTypeDef",
    {
        "AssociationId": ActionTargetTypeDef,
        "RouteTableId": ActionTargetTypeDef,
        "Description": NotRequired[str],
    },
)
AdminScopeTypeDef = TypedDict(
    "AdminScopeTypeDef",
    {
        "AccountScope": NotRequired[AccountScopeTypeDef],
        "OrganizationalUnitScope": NotRequired[OrganizationalUnitScopeTypeDef],
        "RegionScope": NotRequired[RegionScopeTypeDef],
        "PolicyTypeScope": NotRequired[PolicyTypeScopeTypeDef],
    },
)
AppsListDataSummaryTypeDef = TypedDict(
    "AppsListDataSummaryTypeDef",
    {
        "ListArn": NotRequired[str],
        "ListId": NotRequired[str],
        "ListName": NotRequired[str],
        "AppsList": NotRequired[List[AppTypeDef]],
    },
)
AppsListDataTypeDef = TypedDict(
    "AppsListDataTypeDef",
    {
        "ListName": str,
        "AppsList": List[AppTypeDef],
        "ListId": NotRequired[str],
        "ListUpdateToken": NotRequired[str],
        "CreateTime": NotRequired[datetime],
        "LastUpdateTime": NotRequired[datetime],
        "PreviousAppsList": NotRequired[Dict[str, List[AppTypeDef]]],
    },
)
AssociateThirdPartyFirewallResponseTypeDef = TypedDict(
    "AssociateThirdPartyFirewallResponseTypeDef",
    {
        "ThirdPartyFirewallStatus": ThirdPartyFirewallAssociationStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DisassociateThirdPartyFirewallResponseTypeDef = TypedDict(
    "DisassociateThirdPartyFirewallResponseTypeDef",
    {
        "ThirdPartyFirewallStatus": ThirdPartyFirewallAssociationStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAdminAccountResponseTypeDef = TypedDict(
    "GetAdminAccountResponseTypeDef",
    {
        "AdminAccount": str,
        "RoleStatus": AccountRoleStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetNotificationChannelResponseTypeDef = TypedDict(
    "GetNotificationChannelResponseTypeDef",
    {
        "SnsTopicArn": str,
        "SnsRoleName": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetProtectionStatusResponseTypeDef = TypedDict(
    "GetProtectionStatusResponseTypeDef",
    {
        "AdminAccountId": str,
        "ServiceType": SecurityServiceTypeType,
        "Data": str,
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetThirdPartyFirewallAssociationStatusResponseTypeDef = TypedDict(
    "GetThirdPartyFirewallAssociationStatusResponseTypeDef",
    {
        "ThirdPartyFirewallStatus": ThirdPartyFirewallAssociationStatusType,
        "MarketplaceOnboardingStatus": MarketplaceSubscriptionOnboardingStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAdminAccountsForOrganizationResponseTypeDef = TypedDict(
    "ListAdminAccountsForOrganizationResponseTypeDef",
    {
        "AdminAccounts": List[AdminAccountSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAdminsManagingAccountResponseTypeDef = TypedDict(
    "ListAdminsManagingAccountResponseTypeDef",
    {
        "AdminAccounts": List[str],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListMemberAccountsResponseTypeDef = TypedDict(
    "ListMemberAccountsResponseTypeDef",
    {
        "MemberAccounts": List[str],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AwsEc2InstanceViolationTypeDef = TypedDict(
    "AwsEc2InstanceViolationTypeDef",
    {
        "ViolationTarget": NotRequired[str],
        "AwsEc2NetworkInterfaceViolations": NotRequired[
            List[AwsEc2NetworkInterfaceViolationTypeDef]
        ],
    },
)
BatchAssociateResourceResponseTypeDef = TypedDict(
    "BatchAssociateResourceResponseTypeDef",
    {
        "ResourceSetIdentifier": str,
        "FailedItems": List[FailedItemTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchDisassociateResourceResponseTypeDef = TypedDict(
    "BatchDisassociateResourceResponseTypeDef",
    {
        "ResourceSetIdentifier": str,
        "FailedItems": List[FailedItemTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PolicyComplianceDetailTypeDef = TypedDict(
    "PolicyComplianceDetailTypeDef",
    {
        "PolicyOwner": NotRequired[str],
        "PolicyId": NotRequired[str],
        "MemberAccount": NotRequired[str],
        "Violators": NotRequired[List[ComplianceViolatorTypeDef]],
        "EvaluationLimitExceeded": NotRequired[bool],
        "ExpiredAt": NotRequired[datetime],
        "IssueInfoMap": NotRequired[Dict[DependentServiceNameType, str]],
    },
)
ListDiscoveredResourcesResponseTypeDef = TypedDict(
    "ListDiscoveredResourcesResponseTypeDef",
    {
        "Items": List[DiscoveredResourceTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PolicyComplianceStatusTypeDef = TypedDict(
    "PolicyComplianceStatusTypeDef",
    {
        "PolicyOwner": NotRequired[str],
        "PolicyId": NotRequired[str],
        "PolicyName": NotRequired[str],
        "MemberAccount": NotRequired[str],
        "EvaluationResults": NotRequired[List[EvaluationResultTypeDef]],
        "LastUpdated": NotRequired[datetime],
        "IssueInfoMap": NotRequired[Dict[DependentServiceNameType, str]],
    },
)
NetworkFirewallMissingExpectedRoutesViolationTypeDef = TypedDict(
    "NetworkFirewallMissingExpectedRoutesViolationTypeDef",
    {
        "ViolationTarget": NotRequired[str],
        "ExpectedRoutes": NotRequired[List[ExpectedRouteTypeDef]],
        "VpcId": NotRequired[str],
    },
)
GetProtectionStatusRequestRequestTypeDef = TypedDict(
    "GetProtectionStatusRequestRequestTypeDef",
    {
        "PolicyId": str,
        "MemberAccountId": NotRequired[str],
        "StartTime": NotRequired[TimestampTypeDef],
        "EndTime": NotRequired[TimestampTypeDef],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
GetProtocolsListResponseTypeDef = TypedDict(
    "GetProtocolsListResponseTypeDef",
    {
        "ProtocolsList": ProtocolsListDataTypeDef,
        "ProtocolsListArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutProtocolsListResponseTypeDef = TypedDict(
    "PutProtocolsListResponseTypeDef",
    {
        "ProtocolsList": ProtocolsListDataTypeDef,
        "ProtocolsListArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetResourceSetResponseTypeDef = TypedDict(
    "GetResourceSetResponseTypeDef",
    {
        "ResourceSet": ResourceSetTypeDef,
        "ResourceSetArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutResourceSetResponseTypeDef = TypedDict(
    "PutResourceSetResponseTypeDef",
    {
        "ResourceSet": ResourceSetTypeDef,
        "ResourceSetArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAdminAccountsForOrganizationRequestListAdminAccountsForOrganizationPaginateTypeDef = TypedDict(
    "ListAdminAccountsForOrganizationRequestListAdminAccountsForOrganizationPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListAdminsManagingAccountRequestListAdminsManagingAccountPaginateTypeDef = TypedDict(
    "ListAdminsManagingAccountRequestListAdminsManagingAccountPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListAppsListsRequestListAppsListsPaginateTypeDef = TypedDict(
    "ListAppsListsRequestListAppsListsPaginateTypeDef",
    {
        "DefaultLists": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListComplianceStatusRequestListComplianceStatusPaginateTypeDef = TypedDict(
    "ListComplianceStatusRequestListComplianceStatusPaginateTypeDef",
    {
        "PolicyId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListMemberAccountsRequestListMemberAccountsPaginateTypeDef = TypedDict(
    "ListMemberAccountsRequestListMemberAccountsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListPoliciesRequestListPoliciesPaginateTypeDef = TypedDict(
    "ListPoliciesRequestListPoliciesPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListProtocolsListsRequestListProtocolsListsPaginateTypeDef = TypedDict(
    "ListProtocolsListsRequestListProtocolsListsPaginateTypeDef",
    {
        "DefaultLists": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListThirdPartyFirewallFirewallPoliciesRequestListThirdPartyFirewallFirewallPoliciesPaginateTypeDef = TypedDict(
    "ListThirdPartyFirewallFirewallPoliciesRequestListThirdPartyFirewallFirewallPoliciesPaginateTypeDef",
    {
        "ThirdPartyFirewall": ThirdPartyFirewallType,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListPoliciesResponseTypeDef = TypedDict(
    "ListPoliciesResponseTypeDef",
    {
        "PolicyList": List[PolicySummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListProtocolsListsResponseTypeDef = TypedDict(
    "ListProtocolsListsResponseTypeDef",
    {
        "ProtocolsLists": List[ProtocolsListDataSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListResourceSetResourcesResponseTypeDef = TypedDict(
    "ListResourceSetResourcesResponseTypeDef",
    {
        "Items": List[ResourceTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListResourceSetsResponseTypeDef = TypedDict(
    "ListResourceSetsResponseTypeDef",
    {
        "ResourceSets": List[ResourceSetSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "TagList": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutProtocolsListRequestRequestTypeDef = TypedDict(
    "PutProtocolsListRequestRequestTypeDef",
    {
        "ProtocolsList": ProtocolsListDataTypeDef,
        "TagList": NotRequired[Sequence[TagTypeDef]],
    },
)
PutResourceSetRequestRequestTypeDef = TypedDict(
    "PutResourceSetRequestRequestTypeDef",
    {
        "ResourceSet": ResourceSetTypeDef,
        "TagList": NotRequired[Sequence[TagTypeDef]],
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagList": Sequence[TagTypeDef],
    },
)
ListThirdPartyFirewallFirewallPoliciesResponseTypeDef = TypedDict(
    "ListThirdPartyFirewallFirewallPoliciesResponseTypeDef",
    {
        "ThirdPartyFirewallFirewallPolicies": List[ThirdPartyFirewallFirewallPolicyTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
NetworkFirewallBlackHoleRouteDetectedViolationTypeDef = TypedDict(
    "NetworkFirewallBlackHoleRouteDetectedViolationTypeDef",
    {
        "ViolationTarget": NotRequired[str],
        "RouteTableId": NotRequired[str],
        "VpcId": NotRequired[str],
        "ViolatingRoutes": NotRequired[List[RouteTypeDef]],
    },
)
NetworkFirewallInternetTrafficNotInspectedViolationTypeDef = TypedDict(
    "NetworkFirewallInternetTrafficNotInspectedViolationTypeDef",
    {
        "SubnetId": NotRequired[str],
        "SubnetAvailabilityZone": NotRequired[str],
        "RouteTableId": NotRequired[str],
        "ViolatingRoutes": NotRequired[List[RouteTypeDef]],
        "IsRouteTableUsedInDifferentAZ": NotRequired[bool],
        "CurrentFirewallSubnetRouteTable": NotRequired[str],
        "ExpectedFirewallEndpoint": NotRequired[str],
        "FirewallSubnetId": NotRequired[str],
        "ExpectedFirewallSubnetRoutes": NotRequired[List[ExpectedRouteTypeDef]],
        "ActualFirewallSubnetRoutes": NotRequired[List[RouteTypeDef]],
        "InternetGatewayId": NotRequired[str],
        "CurrentInternetGatewayRouteTable": NotRequired[str],
        "ExpectedInternetGatewayRoutes": NotRequired[List[ExpectedRouteTypeDef]],
        "ActualInternetGatewayRoutes": NotRequired[List[RouteTypeDef]],
        "VpcId": NotRequired[str],
    },
)
NetworkFirewallInvalidRouteConfigurationViolationTypeDef = TypedDict(
    "NetworkFirewallInvalidRouteConfigurationViolationTypeDef",
    {
        "AffectedSubnets": NotRequired[List[str]],
        "RouteTableId": NotRequired[str],
        "IsRouteTableUsedInDifferentAZ": NotRequired[bool],
        "ViolatingRoute": NotRequired[RouteTypeDef],
        "CurrentFirewallSubnetRouteTable": NotRequired[str],
        "ExpectedFirewallEndpoint": NotRequired[str],
        "ActualFirewallEndpoint": NotRequired[str],
        "ExpectedFirewallSubnetId": NotRequired[str],
        "ActualFirewallSubnetId": NotRequired[str],
        "ExpectedFirewallSubnetRoutes": NotRequired[List[ExpectedRouteTypeDef]],
        "ActualFirewallSubnetRoutes": NotRequired[List[RouteTypeDef]],
        "InternetGatewayId": NotRequired[str],
        "CurrentInternetGatewayRouteTable": NotRequired[str],
        "ExpectedInternetGatewayRoutes": NotRequired[List[ExpectedRouteTypeDef]],
        "ActualInternetGatewayRoutes": NotRequired[List[RouteTypeDef]],
        "VpcId": NotRequired[str],
    },
)
NetworkFirewallUnexpectedFirewallRoutesViolationTypeDef = TypedDict(
    "NetworkFirewallUnexpectedFirewallRoutesViolationTypeDef",
    {
        "FirewallSubnetId": NotRequired[str],
        "ViolatingRoutes": NotRequired[List[RouteTypeDef]],
        "RouteTableId": NotRequired[str],
        "FirewallEndpoint": NotRequired[str],
        "VpcId": NotRequired[str],
    },
)
NetworkFirewallUnexpectedGatewayRoutesViolationTypeDef = TypedDict(
    "NetworkFirewallUnexpectedGatewayRoutesViolationTypeDef",
    {
        "GatewayId": NotRequired[str],
        "ViolatingRoutes": NotRequired[List[RouteTypeDef]],
        "RouteTableId": NotRequired[str],
        "VpcId": NotRequired[str],
    },
)
RouteHasOutOfScopeEndpointViolationTypeDef = TypedDict(
    "RouteHasOutOfScopeEndpointViolationTypeDef",
    {
        "SubnetId": NotRequired[str],
        "VpcId": NotRequired[str],
        "RouteTableId": NotRequired[str],
        "ViolatingRoutes": NotRequired[List[RouteTypeDef]],
        "SubnetAvailabilityZone": NotRequired[str],
        "SubnetAvailabilityZoneId": NotRequired[str],
        "CurrentFirewallSubnetRouteTable": NotRequired[str],
        "FirewallSubnetId": NotRequired[str],
        "FirewallSubnetRoutes": NotRequired[List[RouteTypeDef]],
        "InternetGatewayId": NotRequired[str],
        "CurrentInternetGatewayRouteTable": NotRequired[str],
        "InternetGatewayRoutes": NotRequired[List[RouteTypeDef]],
    },
)
StatefulRuleGroupTypeDef = TypedDict(
    "StatefulRuleGroupTypeDef",
    {
        "RuleGroupName": NotRequired[str],
        "ResourceId": NotRequired[str],
        "Priority": NotRequired[int],
        "Override": NotRequired[NetworkFirewallStatefulRuleGroupOverrideTypeDef],
    },
)
PolicyOptionTypeDef = TypedDict(
    "PolicyOptionTypeDef",
    {
        "NetworkFirewallPolicy": NotRequired[NetworkFirewallPolicyTypeDef],
        "ThirdPartyFirewallPolicy": NotRequired[ThirdPartyFirewallPolicyTypeDef],
    },
)
SecurityGroupRemediationActionTypeDef = TypedDict(
    "SecurityGroupRemediationActionTypeDef",
    {
        "RemediationActionType": NotRequired[RemediationActionTypeType],
        "Description": NotRequired[str],
        "RemediationResult": NotRequired[SecurityGroupRuleDescriptionTypeDef],
        "IsDefaultAction": NotRequired[bool],
    },
)
RemediationActionTypeDef = TypedDict(
    "RemediationActionTypeDef",
    {
        "Description": NotRequired[str],
        "EC2CreateRouteAction": NotRequired[EC2CreateRouteActionTypeDef],
        "EC2ReplaceRouteAction": NotRequired[EC2ReplaceRouteActionTypeDef],
        "EC2DeleteRouteAction": NotRequired[EC2DeleteRouteActionTypeDef],
        "EC2CopyRouteTableAction": NotRequired[EC2CopyRouteTableActionTypeDef],
        "EC2ReplaceRouteTableAssociationAction": NotRequired[
            EC2ReplaceRouteTableAssociationActionTypeDef
        ],
        "EC2AssociateRouteTableAction": NotRequired[EC2AssociateRouteTableActionTypeDef],
        "EC2CreateRouteTableAction": NotRequired[EC2CreateRouteTableActionTypeDef],
        "FMSPolicyUpdateFirewallCreationConfigAction": NotRequired[
            FMSPolicyUpdateFirewallCreationConfigActionTypeDef
        ],
    },
)
GetAdminScopeResponseTypeDef = TypedDict(
    "GetAdminScopeResponseTypeDef",
    {
        "AdminScope": AdminScopeTypeDef,
        "Status": OrganizationStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutAdminAccountRequestRequestTypeDef = TypedDict(
    "PutAdminAccountRequestRequestTypeDef",
    {
        "AdminAccount": str,
        "AdminScope": NotRequired[AdminScopeTypeDef],
    },
)
ListAppsListsResponseTypeDef = TypedDict(
    "ListAppsListsResponseTypeDef",
    {
        "AppsLists": List[AppsListDataSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAppsListResponseTypeDef = TypedDict(
    "GetAppsListResponseTypeDef",
    {
        "AppsList": AppsListDataTypeDef,
        "AppsListArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutAppsListRequestRequestTypeDef = TypedDict(
    "PutAppsListRequestRequestTypeDef",
    {
        "AppsList": AppsListDataTypeDef,
        "TagList": NotRequired[Sequence[TagTypeDef]],
    },
)
PutAppsListResponseTypeDef = TypedDict(
    "PutAppsListResponseTypeDef",
    {
        "AppsList": AppsListDataTypeDef,
        "AppsListArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetComplianceDetailResponseTypeDef = TypedDict(
    "GetComplianceDetailResponseTypeDef",
    {
        "PolicyComplianceDetail": PolicyComplianceDetailTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListComplianceStatusResponseTypeDef = TypedDict(
    "ListComplianceStatusResponseTypeDef",
    {
        "PolicyComplianceStatusList": List[PolicyComplianceStatusTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
NetworkFirewallPolicyDescriptionTypeDef = TypedDict(
    "NetworkFirewallPolicyDescriptionTypeDef",
    {
        "StatelessRuleGroups": NotRequired[List[StatelessRuleGroupTypeDef]],
        "StatelessDefaultActions": NotRequired[List[str]],
        "StatelessFragmentDefaultActions": NotRequired[List[str]],
        "StatelessCustomActions": NotRequired[List[str]],
        "StatefulRuleGroups": NotRequired[List[StatefulRuleGroupTypeDef]],
        "StatefulDefaultActions": NotRequired[List[str]],
        "StatefulEngineOptions": NotRequired[StatefulEngineOptionsTypeDef],
    },
)
SecurityServicePolicyDataTypeDef = TypedDict(
    "SecurityServicePolicyDataTypeDef",
    {
        "Type": SecurityServiceTypeType,
        "ManagedServiceData": NotRequired[str],
        "PolicyOption": NotRequired[PolicyOptionTypeDef],
    },
)
AwsVPCSecurityGroupViolationTypeDef = TypedDict(
    "AwsVPCSecurityGroupViolationTypeDef",
    {
        "ViolationTarget": NotRequired[str],
        "ViolationTargetDescription": NotRequired[str],
        "PartialMatches": NotRequired[List[PartialMatchTypeDef]],
        "PossibleSecurityGroupRemediationActions": NotRequired[
            List[SecurityGroupRemediationActionTypeDef]
        ],
    },
)
RemediationActionWithOrderTypeDef = TypedDict(
    "RemediationActionWithOrderTypeDef",
    {
        "RemediationAction": NotRequired[RemediationActionTypeDef],
        "Order": NotRequired[int],
    },
)
NetworkFirewallPolicyModifiedViolationTypeDef = TypedDict(
    "NetworkFirewallPolicyModifiedViolationTypeDef",
    {
        "ViolationTarget": NotRequired[str],
        "CurrentPolicyDescription": NotRequired[NetworkFirewallPolicyDescriptionTypeDef],
        "ExpectedPolicyDescription": NotRequired[NetworkFirewallPolicyDescriptionTypeDef],
    },
)
PolicyTypeDef = TypedDict(
    "PolicyTypeDef",
    {
        "PolicyName": str,
        "SecurityServicePolicyData": SecurityServicePolicyDataTypeDef,
        "ResourceType": str,
        "ExcludeResourceTags": bool,
        "RemediationEnabled": bool,
        "PolicyId": NotRequired[str],
        "PolicyUpdateToken": NotRequired[str],
        "ResourceTypeList": NotRequired[List[str]],
        "ResourceTags": NotRequired[List[ResourceTagTypeDef]],
        "DeleteUnusedFMManagedResources": NotRequired[bool],
        "IncludeMap": NotRequired[Dict[CustomerPolicyScopeIdTypeType, List[str]]],
        "ExcludeMap": NotRequired[Dict[CustomerPolicyScopeIdTypeType, List[str]]],
        "ResourceSetIds": NotRequired[List[str]],
        "PolicyDescription": NotRequired[str],
        "PolicyStatus": NotRequired[CustomerPolicyStatusType],
    },
)
PossibleRemediationActionTypeDef = TypedDict(
    "PossibleRemediationActionTypeDef",
    {
        "OrderedRemediationActions": List[RemediationActionWithOrderTypeDef],
        "Description": NotRequired[str],
        "IsDefaultAction": NotRequired[bool],
    },
)
GetPolicyResponseTypeDef = TypedDict(
    "GetPolicyResponseTypeDef",
    {
        "Policy": PolicyTypeDef,
        "PolicyArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutPolicyRequestRequestTypeDef = TypedDict(
    "PutPolicyRequestRequestTypeDef",
    {
        "Policy": PolicyTypeDef,
        "TagList": NotRequired[Sequence[TagTypeDef]],
    },
)
PutPolicyResponseTypeDef = TypedDict(
    "PutPolicyResponseTypeDef",
    {
        "Policy": PolicyTypeDef,
        "PolicyArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PossibleRemediationActionsTypeDef = TypedDict(
    "PossibleRemediationActionsTypeDef",
    {
        "Description": NotRequired[str],
        "Actions": NotRequired[List[PossibleRemediationActionTypeDef]],
    },
)
ResourceViolationTypeDef = TypedDict(
    "ResourceViolationTypeDef",
    {
        "AwsVPCSecurityGroupViolation": NotRequired[AwsVPCSecurityGroupViolationTypeDef],
        "AwsEc2NetworkInterfaceViolation": NotRequired[AwsEc2NetworkInterfaceViolationTypeDef],
        "AwsEc2InstanceViolation": NotRequired[AwsEc2InstanceViolationTypeDef],
        "NetworkFirewallMissingFirewallViolation": NotRequired[
            NetworkFirewallMissingFirewallViolationTypeDef
        ],
        "NetworkFirewallMissingSubnetViolation": NotRequired[
            NetworkFirewallMissingSubnetViolationTypeDef
        ],
        "NetworkFirewallMissingExpectedRTViolation": NotRequired[
            NetworkFirewallMissingExpectedRTViolationTypeDef
        ],
        "NetworkFirewallPolicyModifiedViolation": NotRequired[
            NetworkFirewallPolicyModifiedViolationTypeDef
        ],
        "NetworkFirewallInternetTrafficNotInspectedViolation": NotRequired[
            NetworkFirewallInternetTrafficNotInspectedViolationTypeDef
        ],
        "NetworkFirewallInvalidRouteConfigurationViolation": NotRequired[
            NetworkFirewallInvalidRouteConfigurationViolationTypeDef
        ],
        "NetworkFirewallBlackHoleRouteDetectedViolation": NotRequired[
            NetworkFirewallBlackHoleRouteDetectedViolationTypeDef
        ],
        "NetworkFirewallUnexpectedFirewallRoutesViolation": NotRequired[
            NetworkFirewallUnexpectedFirewallRoutesViolationTypeDef
        ],
        "NetworkFirewallUnexpectedGatewayRoutesViolation": NotRequired[
            NetworkFirewallUnexpectedGatewayRoutesViolationTypeDef
        ],
        "NetworkFirewallMissingExpectedRoutesViolation": NotRequired[
            NetworkFirewallMissingExpectedRoutesViolationTypeDef
        ],
        "DnsRuleGroupPriorityConflictViolation": NotRequired[
            DnsRuleGroupPriorityConflictViolationTypeDef
        ],
        "DnsDuplicateRuleGroupViolation": NotRequired[DnsDuplicateRuleGroupViolationTypeDef],
        "DnsRuleGroupLimitExceededViolation": NotRequired[
            DnsRuleGroupLimitExceededViolationTypeDef
        ],
        "PossibleRemediationActions": NotRequired[PossibleRemediationActionsTypeDef],
        "FirewallSubnetIsOutOfScopeViolation": NotRequired[
            FirewallSubnetIsOutOfScopeViolationTypeDef
        ],
        "RouteHasOutOfScopeEndpointViolation": NotRequired[
            RouteHasOutOfScopeEndpointViolationTypeDef
        ],
        "ThirdPartyFirewallMissingFirewallViolation": NotRequired[
            ThirdPartyFirewallMissingFirewallViolationTypeDef
        ],
        "ThirdPartyFirewallMissingSubnetViolation": NotRequired[
            ThirdPartyFirewallMissingSubnetViolationTypeDef
        ],
        "ThirdPartyFirewallMissingExpectedRouteTableViolation": NotRequired[
            ThirdPartyFirewallMissingExpectedRouteTableViolationTypeDef
        ],
        "FirewallSubnetMissingVPCEndpointViolation": NotRequired[
            FirewallSubnetMissingVPCEndpointViolationTypeDef
        ],
    },
)
ViolationDetailTypeDef = TypedDict(
    "ViolationDetailTypeDef",
    {
        "PolicyId": str,
        "MemberAccount": str,
        "ResourceId": str,
        "ResourceType": str,
        "ResourceViolations": List[ResourceViolationTypeDef],
        "ResourceTags": NotRequired[List[TagTypeDef]],
        "ResourceDescription": NotRequired[str],
    },
)
GetViolationDetailsResponseTypeDef = TypedDict(
    "GetViolationDetailsResponseTypeDef",
    {
        "ViolationDetail": ViolationDetailTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
