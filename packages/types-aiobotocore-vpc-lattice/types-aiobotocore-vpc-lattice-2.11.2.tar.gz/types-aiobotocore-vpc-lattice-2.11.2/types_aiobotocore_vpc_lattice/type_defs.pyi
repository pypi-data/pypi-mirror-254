"""
Type annotations for vpc-lattice service type definitions.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_vpc_lattice/type_defs/)

Usage::

    ```python
    from types_aiobotocore_vpc_lattice.type_defs import AccessLogSubscriptionSummaryTypeDef

    data: AccessLogSubscriptionSummaryTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from .literals import (
    AuthPolicyStateType,
    AuthTypeType,
    HealthCheckProtocolVersionType,
    IpAddressTypeType,
    LambdaEventStructureVersionType,
    ListenerProtocolType,
    ServiceNetworkServiceAssociationStatusType,
    ServiceNetworkVpcAssociationStatusType,
    ServiceStatusType,
    TargetGroupProtocolType,
    TargetGroupProtocolVersionType,
    TargetGroupStatusType,
    TargetGroupTypeType,
    TargetStatusType,
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
    "AccessLogSubscriptionSummaryTypeDef",
    "ResponseMetadataTypeDef",
    "RuleUpdateFailureTypeDef",
    "CreateAccessLogSubscriptionRequestRequestTypeDef",
    "CreateServiceNetworkRequestRequestTypeDef",
    "CreateServiceNetworkServiceAssociationRequestRequestTypeDef",
    "DnsEntryTypeDef",
    "CreateServiceNetworkVpcAssociationRequestRequestTypeDef",
    "CreateServiceRequestRequestTypeDef",
    "DeleteAccessLogSubscriptionRequestRequestTypeDef",
    "DeleteAuthPolicyRequestRequestTypeDef",
    "DeleteListenerRequestRequestTypeDef",
    "DeleteResourcePolicyRequestRequestTypeDef",
    "DeleteRuleRequestRequestTypeDef",
    "DeleteServiceNetworkRequestRequestTypeDef",
    "DeleteServiceNetworkServiceAssociationRequestRequestTypeDef",
    "DeleteServiceNetworkVpcAssociationRequestRequestTypeDef",
    "DeleteServiceRequestRequestTypeDef",
    "DeleteTargetGroupRequestRequestTypeDef",
    "TargetTypeDef",
    "TargetFailureTypeDef",
    "FixedResponseActionTypeDef",
    "WeightedTargetGroupTypeDef",
    "GetAccessLogSubscriptionRequestRequestTypeDef",
    "GetAuthPolicyRequestRequestTypeDef",
    "GetListenerRequestRequestTypeDef",
    "GetResourcePolicyRequestRequestTypeDef",
    "GetRuleRequestRequestTypeDef",
    "GetServiceNetworkRequestRequestTypeDef",
    "GetServiceNetworkServiceAssociationRequestRequestTypeDef",
    "GetServiceNetworkVpcAssociationRequestRequestTypeDef",
    "GetServiceRequestRequestTypeDef",
    "GetTargetGroupRequestRequestTypeDef",
    "HeaderMatchTypeTypeDef",
    "MatcherTypeDef",
    "PaginatorConfigTypeDef",
    "ListAccessLogSubscriptionsRequestRequestTypeDef",
    "ListListenersRequestRequestTypeDef",
    "ListenerSummaryTypeDef",
    "ListRulesRequestRequestTypeDef",
    "RuleSummaryTypeDef",
    "ListServiceNetworkServiceAssociationsRequestRequestTypeDef",
    "ListServiceNetworkVpcAssociationsRequestRequestTypeDef",
    "ServiceNetworkVpcAssociationSummaryTypeDef",
    "ListServiceNetworksRequestRequestTypeDef",
    "ServiceNetworkSummaryTypeDef",
    "ListServicesRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTargetGroupsRequestRequestTypeDef",
    "TargetGroupSummaryTypeDef",
    "TargetSummaryTypeDef",
    "PathMatchTypeTypeDef",
    "PutAuthPolicyRequestRequestTypeDef",
    "PutResourcePolicyRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateAccessLogSubscriptionRequestRequestTypeDef",
    "UpdateServiceNetworkRequestRequestTypeDef",
    "UpdateServiceNetworkVpcAssociationRequestRequestTypeDef",
    "UpdateServiceRequestRequestTypeDef",
    "CreateAccessLogSubscriptionResponseTypeDef",
    "CreateServiceNetworkResponseTypeDef",
    "CreateServiceNetworkVpcAssociationResponseTypeDef",
    "DeleteServiceNetworkServiceAssociationResponseTypeDef",
    "DeleteServiceNetworkVpcAssociationResponseTypeDef",
    "DeleteServiceResponseTypeDef",
    "DeleteTargetGroupResponseTypeDef",
    "GetAccessLogSubscriptionResponseTypeDef",
    "GetAuthPolicyResponseTypeDef",
    "GetResourcePolicyResponseTypeDef",
    "GetServiceNetworkResponseTypeDef",
    "GetServiceNetworkVpcAssociationResponseTypeDef",
    "ListAccessLogSubscriptionsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PutAuthPolicyResponseTypeDef",
    "UpdateAccessLogSubscriptionResponseTypeDef",
    "UpdateServiceNetworkResponseTypeDef",
    "UpdateServiceNetworkVpcAssociationResponseTypeDef",
    "UpdateServiceResponseTypeDef",
    "CreateServiceNetworkServiceAssociationResponseTypeDef",
    "CreateServiceResponseTypeDef",
    "GetServiceNetworkServiceAssociationResponseTypeDef",
    "GetServiceResponseTypeDef",
    "ServiceNetworkServiceAssociationSummaryTypeDef",
    "ServiceSummaryTypeDef",
    "DeregisterTargetsRequestRequestTypeDef",
    "ListTargetsRequestRequestTypeDef",
    "RegisterTargetsRequestRequestTypeDef",
    "DeregisterTargetsResponseTypeDef",
    "RegisterTargetsResponseTypeDef",
    "ForwardActionTypeDef",
    "HeaderMatchTypeDef",
    "HealthCheckConfigTypeDef",
    "ListAccessLogSubscriptionsRequestListAccessLogSubscriptionsPaginateTypeDef",
    "ListListenersRequestListListenersPaginateTypeDef",
    "ListRulesRequestListRulesPaginateTypeDef",
    "ListServiceNetworkServiceAssociationsRequestListServiceNetworkServiceAssociationsPaginateTypeDef",
    "ListServiceNetworkVpcAssociationsRequestListServiceNetworkVpcAssociationsPaginateTypeDef",
    "ListServiceNetworksRequestListServiceNetworksPaginateTypeDef",
    "ListServicesRequestListServicesPaginateTypeDef",
    "ListTargetGroupsRequestListTargetGroupsPaginateTypeDef",
    "ListTargetsRequestListTargetsPaginateTypeDef",
    "ListListenersResponseTypeDef",
    "ListRulesResponseTypeDef",
    "ListServiceNetworkVpcAssociationsResponseTypeDef",
    "ListServiceNetworksResponseTypeDef",
    "ListTargetGroupsResponseTypeDef",
    "ListTargetsResponseTypeDef",
    "PathMatchTypeDef",
    "ListServiceNetworkServiceAssociationsResponseTypeDef",
    "ListServicesResponseTypeDef",
    "RuleActionTypeDef",
    "TargetGroupConfigTypeDef",
    "UpdateTargetGroupRequestRequestTypeDef",
    "HttpMatchTypeDef",
    "CreateListenerRequestRequestTypeDef",
    "CreateListenerResponseTypeDef",
    "GetListenerResponseTypeDef",
    "UpdateListenerRequestRequestTypeDef",
    "UpdateListenerResponseTypeDef",
    "CreateTargetGroupRequestRequestTypeDef",
    "CreateTargetGroupResponseTypeDef",
    "GetTargetGroupResponseTypeDef",
    "UpdateTargetGroupResponseTypeDef",
    "RuleMatchTypeDef",
    "CreateRuleRequestRequestTypeDef",
    "CreateRuleResponseTypeDef",
    "GetRuleResponseTypeDef",
    "RuleUpdateSuccessTypeDef",
    "RuleUpdateTypeDef",
    "UpdateRuleRequestRequestTypeDef",
    "UpdateRuleResponseTypeDef",
    "BatchUpdateRuleResponseTypeDef",
    "BatchUpdateRuleRequestRequestTypeDef",
)

AccessLogSubscriptionSummaryTypeDef = TypedDict(
    "AccessLogSubscriptionSummaryTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "destinationArn": str,
        "id": str,
        "lastUpdatedAt": datetime,
        "resourceArn": str,
        "resourceId": str,
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
RuleUpdateFailureTypeDef = TypedDict(
    "RuleUpdateFailureTypeDef",
    {
        "failureCode": NotRequired[str],
        "failureMessage": NotRequired[str],
        "ruleIdentifier": NotRequired[str],
    },
)
CreateAccessLogSubscriptionRequestRequestTypeDef = TypedDict(
    "CreateAccessLogSubscriptionRequestRequestTypeDef",
    {
        "destinationArn": str,
        "resourceIdentifier": str,
        "clientToken": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)
CreateServiceNetworkRequestRequestTypeDef = TypedDict(
    "CreateServiceNetworkRequestRequestTypeDef",
    {
        "name": str,
        "authType": NotRequired[AuthTypeType],
        "clientToken": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)
CreateServiceNetworkServiceAssociationRequestRequestTypeDef = TypedDict(
    "CreateServiceNetworkServiceAssociationRequestRequestTypeDef",
    {
        "serviceIdentifier": str,
        "serviceNetworkIdentifier": str,
        "clientToken": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)
DnsEntryTypeDef = TypedDict(
    "DnsEntryTypeDef",
    {
        "domainName": NotRequired[str],
        "hostedZoneId": NotRequired[str],
    },
)
CreateServiceNetworkVpcAssociationRequestRequestTypeDef = TypedDict(
    "CreateServiceNetworkVpcAssociationRequestRequestTypeDef",
    {
        "serviceNetworkIdentifier": str,
        "vpcIdentifier": str,
        "clientToken": NotRequired[str],
        "securityGroupIds": NotRequired[Sequence[str]],
        "tags": NotRequired[Mapping[str, str]],
    },
)
CreateServiceRequestRequestTypeDef = TypedDict(
    "CreateServiceRequestRequestTypeDef",
    {
        "name": str,
        "authType": NotRequired[AuthTypeType],
        "certificateArn": NotRequired[str],
        "clientToken": NotRequired[str],
        "customDomainName": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)
DeleteAccessLogSubscriptionRequestRequestTypeDef = TypedDict(
    "DeleteAccessLogSubscriptionRequestRequestTypeDef",
    {
        "accessLogSubscriptionIdentifier": str,
    },
)
DeleteAuthPolicyRequestRequestTypeDef = TypedDict(
    "DeleteAuthPolicyRequestRequestTypeDef",
    {
        "resourceIdentifier": str,
    },
)
DeleteListenerRequestRequestTypeDef = TypedDict(
    "DeleteListenerRequestRequestTypeDef",
    {
        "listenerIdentifier": str,
        "serviceIdentifier": str,
    },
)
DeleteResourcePolicyRequestRequestTypeDef = TypedDict(
    "DeleteResourcePolicyRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)
DeleteRuleRequestRequestTypeDef = TypedDict(
    "DeleteRuleRequestRequestTypeDef",
    {
        "listenerIdentifier": str,
        "ruleIdentifier": str,
        "serviceIdentifier": str,
    },
)
DeleteServiceNetworkRequestRequestTypeDef = TypedDict(
    "DeleteServiceNetworkRequestRequestTypeDef",
    {
        "serviceNetworkIdentifier": str,
    },
)
DeleteServiceNetworkServiceAssociationRequestRequestTypeDef = TypedDict(
    "DeleteServiceNetworkServiceAssociationRequestRequestTypeDef",
    {
        "serviceNetworkServiceAssociationIdentifier": str,
    },
)
DeleteServiceNetworkVpcAssociationRequestRequestTypeDef = TypedDict(
    "DeleteServiceNetworkVpcAssociationRequestRequestTypeDef",
    {
        "serviceNetworkVpcAssociationIdentifier": str,
    },
)
DeleteServiceRequestRequestTypeDef = TypedDict(
    "DeleteServiceRequestRequestTypeDef",
    {
        "serviceIdentifier": str,
    },
)
DeleteTargetGroupRequestRequestTypeDef = TypedDict(
    "DeleteTargetGroupRequestRequestTypeDef",
    {
        "targetGroupIdentifier": str,
    },
)
TargetTypeDef = TypedDict(
    "TargetTypeDef",
    {
        "id": str,
        "port": NotRequired[int],
    },
)
TargetFailureTypeDef = TypedDict(
    "TargetFailureTypeDef",
    {
        "failureCode": NotRequired[str],
        "failureMessage": NotRequired[str],
        "id": NotRequired[str],
        "port": NotRequired[int],
    },
)
FixedResponseActionTypeDef = TypedDict(
    "FixedResponseActionTypeDef",
    {
        "statusCode": int,
    },
)
WeightedTargetGroupTypeDef = TypedDict(
    "WeightedTargetGroupTypeDef",
    {
        "targetGroupIdentifier": str,
        "weight": NotRequired[int],
    },
)
GetAccessLogSubscriptionRequestRequestTypeDef = TypedDict(
    "GetAccessLogSubscriptionRequestRequestTypeDef",
    {
        "accessLogSubscriptionIdentifier": str,
    },
)
GetAuthPolicyRequestRequestTypeDef = TypedDict(
    "GetAuthPolicyRequestRequestTypeDef",
    {
        "resourceIdentifier": str,
    },
)
GetListenerRequestRequestTypeDef = TypedDict(
    "GetListenerRequestRequestTypeDef",
    {
        "listenerIdentifier": str,
        "serviceIdentifier": str,
    },
)
GetResourcePolicyRequestRequestTypeDef = TypedDict(
    "GetResourcePolicyRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)
GetRuleRequestRequestTypeDef = TypedDict(
    "GetRuleRequestRequestTypeDef",
    {
        "listenerIdentifier": str,
        "ruleIdentifier": str,
        "serviceIdentifier": str,
    },
)
GetServiceNetworkRequestRequestTypeDef = TypedDict(
    "GetServiceNetworkRequestRequestTypeDef",
    {
        "serviceNetworkIdentifier": str,
    },
)
GetServiceNetworkServiceAssociationRequestRequestTypeDef = TypedDict(
    "GetServiceNetworkServiceAssociationRequestRequestTypeDef",
    {
        "serviceNetworkServiceAssociationIdentifier": str,
    },
)
GetServiceNetworkVpcAssociationRequestRequestTypeDef = TypedDict(
    "GetServiceNetworkVpcAssociationRequestRequestTypeDef",
    {
        "serviceNetworkVpcAssociationIdentifier": str,
    },
)
GetServiceRequestRequestTypeDef = TypedDict(
    "GetServiceRequestRequestTypeDef",
    {
        "serviceIdentifier": str,
    },
)
GetTargetGroupRequestRequestTypeDef = TypedDict(
    "GetTargetGroupRequestRequestTypeDef",
    {
        "targetGroupIdentifier": str,
    },
)
HeaderMatchTypeTypeDef = TypedDict(
    "HeaderMatchTypeTypeDef",
    {
        "contains": NotRequired[str],
        "exact": NotRequired[str],
        "prefix": NotRequired[str],
    },
)
MatcherTypeDef = TypedDict(
    "MatcherTypeDef",
    {
        "httpCode": NotRequired[str],
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
ListAccessLogSubscriptionsRequestRequestTypeDef = TypedDict(
    "ListAccessLogSubscriptionsRequestRequestTypeDef",
    {
        "resourceIdentifier": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListListenersRequestRequestTypeDef = TypedDict(
    "ListListenersRequestRequestTypeDef",
    {
        "serviceIdentifier": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListenerSummaryTypeDef = TypedDict(
    "ListenerSummaryTypeDef",
    {
        "arn": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "id": NotRequired[str],
        "lastUpdatedAt": NotRequired[datetime],
        "name": NotRequired[str],
        "port": NotRequired[int],
        "protocol": NotRequired[ListenerProtocolType],
    },
)
ListRulesRequestRequestTypeDef = TypedDict(
    "ListRulesRequestRequestTypeDef",
    {
        "listenerIdentifier": str,
        "serviceIdentifier": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
RuleSummaryTypeDef = TypedDict(
    "RuleSummaryTypeDef",
    {
        "arn": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "id": NotRequired[str],
        "isDefault": NotRequired[bool],
        "lastUpdatedAt": NotRequired[datetime],
        "name": NotRequired[str],
        "priority": NotRequired[int],
    },
)
ListServiceNetworkServiceAssociationsRequestRequestTypeDef = TypedDict(
    "ListServiceNetworkServiceAssociationsRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "serviceIdentifier": NotRequired[str],
        "serviceNetworkIdentifier": NotRequired[str],
    },
)
ListServiceNetworkVpcAssociationsRequestRequestTypeDef = TypedDict(
    "ListServiceNetworkVpcAssociationsRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "serviceNetworkIdentifier": NotRequired[str],
        "vpcIdentifier": NotRequired[str],
    },
)
ServiceNetworkVpcAssociationSummaryTypeDef = TypedDict(
    "ServiceNetworkVpcAssociationSummaryTypeDef",
    {
        "arn": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "createdBy": NotRequired[str],
        "id": NotRequired[str],
        "lastUpdatedAt": NotRequired[datetime],
        "serviceNetworkArn": NotRequired[str],
        "serviceNetworkId": NotRequired[str],
        "serviceNetworkName": NotRequired[str],
        "status": NotRequired[ServiceNetworkVpcAssociationStatusType],
        "vpcId": NotRequired[str],
    },
)
ListServiceNetworksRequestRequestTypeDef = TypedDict(
    "ListServiceNetworksRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ServiceNetworkSummaryTypeDef = TypedDict(
    "ServiceNetworkSummaryTypeDef",
    {
        "arn": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "id": NotRequired[str],
        "lastUpdatedAt": NotRequired[datetime],
        "name": NotRequired[str],
        "numberOfAssociatedServices": NotRequired[int],
        "numberOfAssociatedVPCs": NotRequired[int],
    },
)
ListServicesRequestRequestTypeDef = TypedDict(
    "ListServicesRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)
ListTargetGroupsRequestRequestTypeDef = TypedDict(
    "ListTargetGroupsRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "targetGroupType": NotRequired[TargetGroupTypeType],
        "vpcIdentifier": NotRequired[str],
    },
)
TargetGroupSummaryTypeDef = TypedDict(
    "TargetGroupSummaryTypeDef",
    {
        "arn": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "id": NotRequired[str],
        "ipAddressType": NotRequired[IpAddressTypeType],
        "lambdaEventStructureVersion": NotRequired[LambdaEventStructureVersionType],
        "lastUpdatedAt": NotRequired[datetime],
        "name": NotRequired[str],
        "port": NotRequired[int],
        "protocol": NotRequired[TargetGroupProtocolType],
        "serviceArns": NotRequired[List[str]],
        "status": NotRequired[TargetGroupStatusType],
        "type": NotRequired[TargetGroupTypeType],
        "vpcIdentifier": NotRequired[str],
    },
)
TargetSummaryTypeDef = TypedDict(
    "TargetSummaryTypeDef",
    {
        "id": NotRequired[str],
        "port": NotRequired[int],
        "reasonCode": NotRequired[str],
        "status": NotRequired[TargetStatusType],
    },
)
PathMatchTypeTypeDef = TypedDict(
    "PathMatchTypeTypeDef",
    {
        "exact": NotRequired[str],
        "prefix": NotRequired[str],
    },
)
PutAuthPolicyRequestRequestTypeDef = TypedDict(
    "PutAuthPolicyRequestRequestTypeDef",
    {
        "policy": str,
        "resourceIdentifier": str,
    },
)
PutResourcePolicyRequestRequestTypeDef = TypedDict(
    "PutResourcePolicyRequestRequestTypeDef",
    {
        "policy": str,
        "resourceArn": str,
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Mapping[str, str],
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)
UpdateAccessLogSubscriptionRequestRequestTypeDef = TypedDict(
    "UpdateAccessLogSubscriptionRequestRequestTypeDef",
    {
        "accessLogSubscriptionIdentifier": str,
        "destinationArn": str,
    },
)
UpdateServiceNetworkRequestRequestTypeDef = TypedDict(
    "UpdateServiceNetworkRequestRequestTypeDef",
    {
        "authType": AuthTypeType,
        "serviceNetworkIdentifier": str,
    },
)
UpdateServiceNetworkVpcAssociationRequestRequestTypeDef = TypedDict(
    "UpdateServiceNetworkVpcAssociationRequestRequestTypeDef",
    {
        "securityGroupIds": Sequence[str],
        "serviceNetworkVpcAssociationIdentifier": str,
    },
)
UpdateServiceRequestRequestTypeDef = TypedDict(
    "UpdateServiceRequestRequestTypeDef",
    {
        "serviceIdentifier": str,
        "authType": NotRequired[AuthTypeType],
        "certificateArn": NotRequired[str],
    },
)
CreateAccessLogSubscriptionResponseTypeDef = TypedDict(
    "CreateAccessLogSubscriptionResponseTypeDef",
    {
        "arn": str,
        "destinationArn": str,
        "id": str,
        "resourceArn": str,
        "resourceId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateServiceNetworkResponseTypeDef = TypedDict(
    "CreateServiceNetworkResponseTypeDef",
    {
        "arn": str,
        "authType": AuthTypeType,
        "id": str,
        "name": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateServiceNetworkVpcAssociationResponseTypeDef = TypedDict(
    "CreateServiceNetworkVpcAssociationResponseTypeDef",
    {
        "arn": str,
        "createdBy": str,
        "id": str,
        "securityGroupIds": List[str],
        "status": ServiceNetworkVpcAssociationStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteServiceNetworkServiceAssociationResponseTypeDef = TypedDict(
    "DeleteServiceNetworkServiceAssociationResponseTypeDef",
    {
        "arn": str,
        "id": str,
        "status": ServiceNetworkServiceAssociationStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteServiceNetworkVpcAssociationResponseTypeDef = TypedDict(
    "DeleteServiceNetworkVpcAssociationResponseTypeDef",
    {
        "arn": str,
        "id": str,
        "status": ServiceNetworkVpcAssociationStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteServiceResponseTypeDef = TypedDict(
    "DeleteServiceResponseTypeDef",
    {
        "arn": str,
        "id": str,
        "name": str,
        "status": ServiceStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteTargetGroupResponseTypeDef = TypedDict(
    "DeleteTargetGroupResponseTypeDef",
    {
        "arn": str,
        "id": str,
        "status": TargetGroupStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAccessLogSubscriptionResponseTypeDef = TypedDict(
    "GetAccessLogSubscriptionResponseTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "destinationArn": str,
        "id": str,
        "lastUpdatedAt": datetime,
        "resourceArn": str,
        "resourceId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAuthPolicyResponseTypeDef = TypedDict(
    "GetAuthPolicyResponseTypeDef",
    {
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "policy": str,
        "state": AuthPolicyStateType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetResourcePolicyResponseTypeDef = TypedDict(
    "GetResourcePolicyResponseTypeDef",
    {
        "policy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetServiceNetworkResponseTypeDef = TypedDict(
    "GetServiceNetworkResponseTypeDef",
    {
        "arn": str,
        "authType": AuthTypeType,
        "createdAt": datetime,
        "id": str,
        "lastUpdatedAt": datetime,
        "name": str,
        "numberOfAssociatedServices": int,
        "numberOfAssociatedVPCs": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetServiceNetworkVpcAssociationResponseTypeDef = TypedDict(
    "GetServiceNetworkVpcAssociationResponseTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "createdBy": str,
        "failureCode": str,
        "failureMessage": str,
        "id": str,
        "lastUpdatedAt": datetime,
        "securityGroupIds": List[str],
        "serviceNetworkArn": str,
        "serviceNetworkId": str,
        "serviceNetworkName": str,
        "status": ServiceNetworkVpcAssociationStatusType,
        "vpcId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAccessLogSubscriptionsResponseTypeDef = TypedDict(
    "ListAccessLogSubscriptionsResponseTypeDef",
    {
        "items": List[AccessLogSubscriptionSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutAuthPolicyResponseTypeDef = TypedDict(
    "PutAuthPolicyResponseTypeDef",
    {
        "policy": str,
        "state": AuthPolicyStateType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateAccessLogSubscriptionResponseTypeDef = TypedDict(
    "UpdateAccessLogSubscriptionResponseTypeDef",
    {
        "arn": str,
        "destinationArn": str,
        "id": str,
        "resourceArn": str,
        "resourceId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateServiceNetworkResponseTypeDef = TypedDict(
    "UpdateServiceNetworkResponseTypeDef",
    {
        "arn": str,
        "authType": AuthTypeType,
        "id": str,
        "name": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateServiceNetworkVpcAssociationResponseTypeDef = TypedDict(
    "UpdateServiceNetworkVpcAssociationResponseTypeDef",
    {
        "arn": str,
        "createdBy": str,
        "id": str,
        "securityGroupIds": List[str],
        "status": ServiceNetworkVpcAssociationStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateServiceResponseTypeDef = TypedDict(
    "UpdateServiceResponseTypeDef",
    {
        "arn": str,
        "authType": AuthTypeType,
        "certificateArn": str,
        "customDomainName": str,
        "id": str,
        "name": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateServiceNetworkServiceAssociationResponseTypeDef = TypedDict(
    "CreateServiceNetworkServiceAssociationResponseTypeDef",
    {
        "arn": str,
        "createdBy": str,
        "customDomainName": str,
        "dnsEntry": DnsEntryTypeDef,
        "id": str,
        "status": ServiceNetworkServiceAssociationStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateServiceResponseTypeDef = TypedDict(
    "CreateServiceResponseTypeDef",
    {
        "arn": str,
        "authType": AuthTypeType,
        "certificateArn": str,
        "customDomainName": str,
        "dnsEntry": DnsEntryTypeDef,
        "id": str,
        "name": str,
        "status": ServiceStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetServiceNetworkServiceAssociationResponseTypeDef = TypedDict(
    "GetServiceNetworkServiceAssociationResponseTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "createdBy": str,
        "customDomainName": str,
        "dnsEntry": DnsEntryTypeDef,
        "failureCode": str,
        "failureMessage": str,
        "id": str,
        "serviceArn": str,
        "serviceId": str,
        "serviceName": str,
        "serviceNetworkArn": str,
        "serviceNetworkId": str,
        "serviceNetworkName": str,
        "status": ServiceNetworkServiceAssociationStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetServiceResponseTypeDef = TypedDict(
    "GetServiceResponseTypeDef",
    {
        "arn": str,
        "authType": AuthTypeType,
        "certificateArn": str,
        "createdAt": datetime,
        "customDomainName": str,
        "dnsEntry": DnsEntryTypeDef,
        "failureCode": str,
        "failureMessage": str,
        "id": str,
        "lastUpdatedAt": datetime,
        "name": str,
        "status": ServiceStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ServiceNetworkServiceAssociationSummaryTypeDef = TypedDict(
    "ServiceNetworkServiceAssociationSummaryTypeDef",
    {
        "arn": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "createdBy": NotRequired[str],
        "customDomainName": NotRequired[str],
        "dnsEntry": NotRequired[DnsEntryTypeDef],
        "id": NotRequired[str],
        "serviceArn": NotRequired[str],
        "serviceId": NotRequired[str],
        "serviceName": NotRequired[str],
        "serviceNetworkArn": NotRequired[str],
        "serviceNetworkId": NotRequired[str],
        "serviceNetworkName": NotRequired[str],
        "status": NotRequired[ServiceNetworkServiceAssociationStatusType],
    },
)
ServiceSummaryTypeDef = TypedDict(
    "ServiceSummaryTypeDef",
    {
        "arn": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "customDomainName": NotRequired[str],
        "dnsEntry": NotRequired[DnsEntryTypeDef],
        "id": NotRequired[str],
        "lastUpdatedAt": NotRequired[datetime],
        "name": NotRequired[str],
        "status": NotRequired[ServiceStatusType],
    },
)
DeregisterTargetsRequestRequestTypeDef = TypedDict(
    "DeregisterTargetsRequestRequestTypeDef",
    {
        "targetGroupIdentifier": str,
        "targets": Sequence[TargetTypeDef],
    },
)
ListTargetsRequestRequestTypeDef = TypedDict(
    "ListTargetsRequestRequestTypeDef",
    {
        "targetGroupIdentifier": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "targets": NotRequired[Sequence[TargetTypeDef]],
    },
)
RegisterTargetsRequestRequestTypeDef = TypedDict(
    "RegisterTargetsRequestRequestTypeDef",
    {
        "targetGroupIdentifier": str,
        "targets": Sequence[TargetTypeDef],
    },
)
DeregisterTargetsResponseTypeDef = TypedDict(
    "DeregisterTargetsResponseTypeDef",
    {
        "successful": List[TargetTypeDef],
        "unsuccessful": List[TargetFailureTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RegisterTargetsResponseTypeDef = TypedDict(
    "RegisterTargetsResponseTypeDef",
    {
        "successful": List[TargetTypeDef],
        "unsuccessful": List[TargetFailureTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ForwardActionTypeDef = TypedDict(
    "ForwardActionTypeDef",
    {
        "targetGroups": Sequence[WeightedTargetGroupTypeDef],
    },
)
HeaderMatchTypeDef = TypedDict(
    "HeaderMatchTypeDef",
    {
        "match": HeaderMatchTypeTypeDef,
        "name": str,
        "caseSensitive": NotRequired[bool],
    },
)
HealthCheckConfigTypeDef = TypedDict(
    "HealthCheckConfigTypeDef",
    {
        "enabled": NotRequired[bool],
        "healthCheckIntervalSeconds": NotRequired[int],
        "healthCheckTimeoutSeconds": NotRequired[int],
        "healthyThresholdCount": NotRequired[int],
        "matcher": NotRequired[MatcherTypeDef],
        "path": NotRequired[str],
        "port": NotRequired[int],
        "protocol": NotRequired[TargetGroupProtocolType],
        "protocolVersion": NotRequired[HealthCheckProtocolVersionType],
        "unhealthyThresholdCount": NotRequired[int],
    },
)
ListAccessLogSubscriptionsRequestListAccessLogSubscriptionsPaginateTypeDef = TypedDict(
    "ListAccessLogSubscriptionsRequestListAccessLogSubscriptionsPaginateTypeDef",
    {
        "resourceIdentifier": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListListenersRequestListListenersPaginateTypeDef = TypedDict(
    "ListListenersRequestListListenersPaginateTypeDef",
    {
        "serviceIdentifier": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListRulesRequestListRulesPaginateTypeDef = TypedDict(
    "ListRulesRequestListRulesPaginateTypeDef",
    {
        "listenerIdentifier": str,
        "serviceIdentifier": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListServiceNetworkServiceAssociationsRequestListServiceNetworkServiceAssociationsPaginateTypeDef = TypedDict(
    "ListServiceNetworkServiceAssociationsRequestListServiceNetworkServiceAssociationsPaginateTypeDef",
    {
        "serviceIdentifier": NotRequired[str],
        "serviceNetworkIdentifier": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListServiceNetworkVpcAssociationsRequestListServiceNetworkVpcAssociationsPaginateTypeDef = (
    TypedDict(
        "ListServiceNetworkVpcAssociationsRequestListServiceNetworkVpcAssociationsPaginateTypeDef",
        {
            "serviceNetworkIdentifier": NotRequired[str],
            "vpcIdentifier": NotRequired[str],
            "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
        },
    )
)
ListServiceNetworksRequestListServiceNetworksPaginateTypeDef = TypedDict(
    "ListServiceNetworksRequestListServiceNetworksPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListServicesRequestListServicesPaginateTypeDef = TypedDict(
    "ListServicesRequestListServicesPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListTargetGroupsRequestListTargetGroupsPaginateTypeDef = TypedDict(
    "ListTargetGroupsRequestListTargetGroupsPaginateTypeDef",
    {
        "targetGroupType": NotRequired[TargetGroupTypeType],
        "vpcIdentifier": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListTargetsRequestListTargetsPaginateTypeDef = TypedDict(
    "ListTargetsRequestListTargetsPaginateTypeDef",
    {
        "targetGroupIdentifier": str,
        "targets": NotRequired[Sequence[TargetTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListListenersResponseTypeDef = TypedDict(
    "ListListenersResponseTypeDef",
    {
        "items": List[ListenerSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListRulesResponseTypeDef = TypedDict(
    "ListRulesResponseTypeDef",
    {
        "items": List[RuleSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListServiceNetworkVpcAssociationsResponseTypeDef = TypedDict(
    "ListServiceNetworkVpcAssociationsResponseTypeDef",
    {
        "items": List[ServiceNetworkVpcAssociationSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListServiceNetworksResponseTypeDef = TypedDict(
    "ListServiceNetworksResponseTypeDef",
    {
        "items": List[ServiceNetworkSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTargetGroupsResponseTypeDef = TypedDict(
    "ListTargetGroupsResponseTypeDef",
    {
        "items": List[TargetGroupSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTargetsResponseTypeDef = TypedDict(
    "ListTargetsResponseTypeDef",
    {
        "items": List[TargetSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PathMatchTypeDef = TypedDict(
    "PathMatchTypeDef",
    {
        "match": PathMatchTypeTypeDef,
        "caseSensitive": NotRequired[bool],
    },
)
ListServiceNetworkServiceAssociationsResponseTypeDef = TypedDict(
    "ListServiceNetworkServiceAssociationsResponseTypeDef",
    {
        "items": List[ServiceNetworkServiceAssociationSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListServicesResponseTypeDef = TypedDict(
    "ListServicesResponseTypeDef",
    {
        "items": List[ServiceSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RuleActionTypeDef = TypedDict(
    "RuleActionTypeDef",
    {
        "fixedResponse": NotRequired[FixedResponseActionTypeDef],
        "forward": NotRequired[ForwardActionTypeDef],
    },
)
TargetGroupConfigTypeDef = TypedDict(
    "TargetGroupConfigTypeDef",
    {
        "healthCheck": NotRequired[HealthCheckConfigTypeDef],
        "ipAddressType": NotRequired[IpAddressTypeType],
        "lambdaEventStructureVersion": NotRequired[LambdaEventStructureVersionType],
        "port": NotRequired[int],
        "protocol": NotRequired[TargetGroupProtocolType],
        "protocolVersion": NotRequired[TargetGroupProtocolVersionType],
        "vpcIdentifier": NotRequired[str],
    },
)
UpdateTargetGroupRequestRequestTypeDef = TypedDict(
    "UpdateTargetGroupRequestRequestTypeDef",
    {
        "healthCheck": HealthCheckConfigTypeDef,
        "targetGroupIdentifier": str,
    },
)
HttpMatchTypeDef = TypedDict(
    "HttpMatchTypeDef",
    {
        "headerMatches": NotRequired[Sequence[HeaderMatchTypeDef]],
        "method": NotRequired[str],
        "pathMatch": NotRequired[PathMatchTypeDef],
    },
)
CreateListenerRequestRequestTypeDef = TypedDict(
    "CreateListenerRequestRequestTypeDef",
    {
        "defaultAction": RuleActionTypeDef,
        "name": str,
        "protocol": ListenerProtocolType,
        "serviceIdentifier": str,
        "clientToken": NotRequired[str],
        "port": NotRequired[int],
        "tags": NotRequired[Mapping[str, str]],
    },
)
CreateListenerResponseTypeDef = TypedDict(
    "CreateListenerResponseTypeDef",
    {
        "arn": str,
        "defaultAction": RuleActionTypeDef,
        "id": str,
        "name": str,
        "port": int,
        "protocol": ListenerProtocolType,
        "serviceArn": str,
        "serviceId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetListenerResponseTypeDef = TypedDict(
    "GetListenerResponseTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "defaultAction": RuleActionTypeDef,
        "id": str,
        "lastUpdatedAt": datetime,
        "name": str,
        "port": int,
        "protocol": ListenerProtocolType,
        "serviceArn": str,
        "serviceId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateListenerRequestRequestTypeDef = TypedDict(
    "UpdateListenerRequestRequestTypeDef",
    {
        "defaultAction": RuleActionTypeDef,
        "listenerIdentifier": str,
        "serviceIdentifier": str,
    },
)
UpdateListenerResponseTypeDef = TypedDict(
    "UpdateListenerResponseTypeDef",
    {
        "arn": str,
        "defaultAction": RuleActionTypeDef,
        "id": str,
        "name": str,
        "port": int,
        "protocol": ListenerProtocolType,
        "serviceArn": str,
        "serviceId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateTargetGroupRequestRequestTypeDef = TypedDict(
    "CreateTargetGroupRequestRequestTypeDef",
    {
        "name": str,
        "type": TargetGroupTypeType,
        "clientToken": NotRequired[str],
        "config": NotRequired[TargetGroupConfigTypeDef],
        "tags": NotRequired[Mapping[str, str]],
    },
)
CreateTargetGroupResponseTypeDef = TypedDict(
    "CreateTargetGroupResponseTypeDef",
    {
        "arn": str,
        "config": TargetGroupConfigTypeDef,
        "id": str,
        "name": str,
        "status": TargetGroupStatusType,
        "type": TargetGroupTypeType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetTargetGroupResponseTypeDef = TypedDict(
    "GetTargetGroupResponseTypeDef",
    {
        "arn": str,
        "config": TargetGroupConfigTypeDef,
        "createdAt": datetime,
        "failureCode": str,
        "failureMessage": str,
        "id": str,
        "lastUpdatedAt": datetime,
        "name": str,
        "serviceArns": List[str],
        "status": TargetGroupStatusType,
        "type": TargetGroupTypeType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateTargetGroupResponseTypeDef = TypedDict(
    "UpdateTargetGroupResponseTypeDef",
    {
        "arn": str,
        "config": TargetGroupConfigTypeDef,
        "id": str,
        "name": str,
        "status": TargetGroupStatusType,
        "type": TargetGroupTypeType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RuleMatchTypeDef = TypedDict(
    "RuleMatchTypeDef",
    {
        "httpMatch": NotRequired[HttpMatchTypeDef],
    },
)
CreateRuleRequestRequestTypeDef = TypedDict(
    "CreateRuleRequestRequestTypeDef",
    {
        "action": RuleActionTypeDef,
        "listenerIdentifier": str,
        "match": RuleMatchTypeDef,
        "name": str,
        "priority": int,
        "serviceIdentifier": str,
        "clientToken": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)
CreateRuleResponseTypeDef = TypedDict(
    "CreateRuleResponseTypeDef",
    {
        "action": RuleActionTypeDef,
        "arn": str,
        "id": str,
        "match": RuleMatchTypeDef,
        "name": str,
        "priority": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetRuleResponseTypeDef = TypedDict(
    "GetRuleResponseTypeDef",
    {
        "action": RuleActionTypeDef,
        "arn": str,
        "createdAt": datetime,
        "id": str,
        "isDefault": bool,
        "lastUpdatedAt": datetime,
        "match": RuleMatchTypeDef,
        "name": str,
        "priority": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RuleUpdateSuccessTypeDef = TypedDict(
    "RuleUpdateSuccessTypeDef",
    {
        "action": NotRequired[RuleActionTypeDef],
        "arn": NotRequired[str],
        "id": NotRequired[str],
        "isDefault": NotRequired[bool],
        "match": NotRequired[RuleMatchTypeDef],
        "name": NotRequired[str],
        "priority": NotRequired[int],
    },
)
RuleUpdateTypeDef = TypedDict(
    "RuleUpdateTypeDef",
    {
        "ruleIdentifier": str,
        "action": NotRequired[RuleActionTypeDef],
        "match": NotRequired[RuleMatchTypeDef],
        "priority": NotRequired[int],
    },
)
UpdateRuleRequestRequestTypeDef = TypedDict(
    "UpdateRuleRequestRequestTypeDef",
    {
        "listenerIdentifier": str,
        "ruleIdentifier": str,
        "serviceIdentifier": str,
        "action": NotRequired[RuleActionTypeDef],
        "match": NotRequired[RuleMatchTypeDef],
        "priority": NotRequired[int],
    },
)
UpdateRuleResponseTypeDef = TypedDict(
    "UpdateRuleResponseTypeDef",
    {
        "action": RuleActionTypeDef,
        "arn": str,
        "id": str,
        "isDefault": bool,
        "match": RuleMatchTypeDef,
        "name": str,
        "priority": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchUpdateRuleResponseTypeDef = TypedDict(
    "BatchUpdateRuleResponseTypeDef",
    {
        "successful": List[RuleUpdateSuccessTypeDef],
        "unsuccessful": List[RuleUpdateFailureTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchUpdateRuleRequestRequestTypeDef = TypedDict(
    "BatchUpdateRuleRequestRequestTypeDef",
    {
        "listenerIdentifier": str,
        "rules": Sequence[RuleUpdateTypeDef],
        "serviceIdentifier": str,
    },
)
