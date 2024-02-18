"""
Type annotations for vpc-lattice service client.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_vpc_lattice/client/)

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_vpc_lattice.client import VPCLatticeClient

    session = get_session()
    async with session.create_client("vpc-lattice") as client:
        client: VPCLatticeClient
    ```
"""

import sys
from typing import Any, Dict, Mapping, Sequence, Type, overload

from aiobotocore.client import AioBaseClient
from botocore.client import ClientMeta

from .literals import AuthTypeType, ListenerProtocolType, TargetGroupTypeType
from .paginator import (
    ListAccessLogSubscriptionsPaginator,
    ListListenersPaginator,
    ListRulesPaginator,
    ListServiceNetworkServiceAssociationsPaginator,
    ListServiceNetworksPaginator,
    ListServiceNetworkVpcAssociationsPaginator,
    ListServicesPaginator,
    ListTargetGroupsPaginator,
    ListTargetsPaginator,
)
from .type_defs import (
    BatchUpdateRuleResponseTypeDef,
    CreateAccessLogSubscriptionResponseTypeDef,
    CreateListenerResponseTypeDef,
    CreateRuleResponseTypeDef,
    CreateServiceNetworkResponseTypeDef,
    CreateServiceNetworkServiceAssociationResponseTypeDef,
    CreateServiceNetworkVpcAssociationResponseTypeDef,
    CreateServiceResponseTypeDef,
    CreateTargetGroupResponseTypeDef,
    DeleteServiceNetworkServiceAssociationResponseTypeDef,
    DeleteServiceNetworkVpcAssociationResponseTypeDef,
    DeleteServiceResponseTypeDef,
    DeleteTargetGroupResponseTypeDef,
    DeregisterTargetsResponseTypeDef,
    GetAccessLogSubscriptionResponseTypeDef,
    GetAuthPolicyResponseTypeDef,
    GetListenerResponseTypeDef,
    GetResourcePolicyResponseTypeDef,
    GetRuleResponseTypeDef,
    GetServiceNetworkResponseTypeDef,
    GetServiceNetworkServiceAssociationResponseTypeDef,
    GetServiceNetworkVpcAssociationResponseTypeDef,
    GetServiceResponseTypeDef,
    GetTargetGroupResponseTypeDef,
    HealthCheckConfigTypeDef,
    ListAccessLogSubscriptionsResponseTypeDef,
    ListListenersResponseTypeDef,
    ListRulesResponseTypeDef,
    ListServiceNetworkServiceAssociationsResponseTypeDef,
    ListServiceNetworksResponseTypeDef,
    ListServiceNetworkVpcAssociationsResponseTypeDef,
    ListServicesResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTargetGroupsResponseTypeDef,
    ListTargetsResponseTypeDef,
    PutAuthPolicyResponseTypeDef,
    RegisterTargetsResponseTypeDef,
    RuleActionTypeDef,
    RuleMatchTypeDef,
    RuleUpdateTypeDef,
    TargetGroupConfigTypeDef,
    TargetTypeDef,
    UpdateAccessLogSubscriptionResponseTypeDef,
    UpdateListenerResponseTypeDef,
    UpdateRuleResponseTypeDef,
    UpdateServiceNetworkResponseTypeDef,
    UpdateServiceNetworkVpcAssociationResponseTypeDef,
    UpdateServiceResponseTypeDef,
    UpdateTargetGroupResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("VPCLatticeClient",)


class BotocoreClientError(Exception):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class VPCLatticeClient(AioBaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice.html#VPCLattice.Client)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_vpc_lattice/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        VPCLatticeClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice.html#VPCLattice.Client.exceptions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_vpc_lattice/client/#exceptions)
        """

    async def batch_update_rule(
        self, *, listenerIdentifier: str, rules: Sequence[RuleUpdateTypeDef], serviceIdentifier: str
    ) -> BatchUpdateRuleResponseTypeDef:
        """
        Updates the listener rules in a batch.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice.html#VPCLattice.Client.batch_update_rule)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_vpc_lattice/client/#batch_update_rule)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice.html#VPCLattice.Client.can_paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_vpc_lattice/client/#can_paginate)
        """

    async def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice.html#VPCLattice.Client.close)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_vpc_lattice/client/#close)
        """

    async def create_access_log_subscription(
        self,
        *,
        destinationArn: str,
        resourceIdentifier: str,
        clientToken: str = ...,
        tags: Mapping[str, str] = ...,
    ) -> CreateAccessLogSubscriptionResponseTypeDef:
        """
        Enables access logs to be sent to Amazon CloudWatch, Amazon S3, and Amazon
        Kinesis Data
        Firehose.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice.html#VPCLattice.Client.create_access_log_subscription)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_vpc_lattice/client/#create_access_log_subscription)
        """

    async def create_listener(
        self,
        *,
        defaultAction: RuleActionTypeDef,
        name: str,
        protocol: ListenerProtocolType,
        serviceIdentifier: str,
        clientToken: str = ...,
        port: int = ...,
        tags: Mapping[str, str] = ...,
    ) -> CreateListenerResponseTypeDef:
        """
        Creates a listener for a service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice.html#VPCLattice.Client.create_listener)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_vpc_lattice/client/#create_listener)
        """

    async def create_rule(
        self,
        *,
        action: RuleActionTypeDef,
        listenerIdentifier: str,
        match: RuleMatchTypeDef,
        name: str,
        priority: int,
        serviceIdentifier: str,
        clientToken: str = ...,
        tags: Mapping[str, str] = ...,
    ) -> CreateRuleResponseTypeDef:
        """
        Creates a listener rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice.html#VPCLattice.Client.create_rule)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_vpc_lattice/client/#create_rule)
        """

    async def create_service(
        self,
        *,
        name: str,
        authType: AuthTypeType = ...,
        certificateArn: str = ...,
        clientToken: str = ...,
        customDomainName: str = ...,
        tags: Mapping[str, str] = ...,
    ) -> CreateServiceResponseTypeDef:
        """
        Creates a service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice.html#VPCLattice.Client.create_service)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_vpc_lattice/client/#create_service)
        """

    async def create_service_network(
        self,
        *,
        name: str,
        authType: AuthTypeType = ...,
        clientToken: str = ...,
        tags: Mapping[str, str] = ...,
    ) -> CreateServiceNetworkResponseTypeDef:
        """
        Creates a service network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice.html#VPCLattice.Client.create_service_network)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_vpc_lattice/client/#create_service_network)
        """

    async def create_service_network_service_association(
        self,
        *,
        serviceIdentifier: str,
        serviceNetworkIdentifier: str,
        clientToken: str = ...,
        tags: Mapping[str, str] = ...,
    ) -> CreateServiceNetworkServiceAssociationResponseTypeDef:
        """
        Associates a service with a service network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice.html#VPCLattice.Client.create_service_network_service_association)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_vpc_lattice/client/#create_service_network_service_association)
        """

    async def create_service_network_vpc_association(
        self,
        *,
        serviceNetworkIdentifier: str,
        vpcIdentifier: str,
        clientToken: str = ...,
        securityGroupIds: Sequence[str] = ...,
        tags: Mapping[str, str] = ...,
    ) -> CreateServiceNetworkVpcAssociationResponseTypeDef:
        """
        Associates a VPC with a service network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice.html#VPCLattice.Client.create_service_network_vpc_association)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_vpc_lattice/client/#create_service_network_vpc_association)
        """

    async def create_target_group(
        self,
        *,
        name: str,
        type: TargetGroupTypeType,
        clientToken: str = ...,
        config: TargetGroupConfigTypeDef = ...,
        tags: Mapping[str, str] = ...,
    ) -> CreateTargetGroupResponseTypeDef:
        """
        Creates a target group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice.html#VPCLattice.Client.create_target_group)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_vpc_lattice/client/#create_target_group)
        """

    async def delete_access_log_subscription(
        self, *, accessLogSubscriptionIdentifier: str
    ) -> Dict[str, Any]:
        """
        Deletes the specified access log subscription.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice.html#VPCLattice.Client.delete_access_log_subscription)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_vpc_lattice/client/#delete_access_log_subscription)
        """

    async def delete_auth_policy(self, *, resourceIdentifier: str) -> Dict[str, Any]:
        """
        Deletes the specified auth policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice.html#VPCLattice.Client.delete_auth_policy)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_vpc_lattice/client/#delete_auth_policy)
        """

    async def delete_listener(
        self, *, listenerIdentifier: str, serviceIdentifier: str
    ) -> Dict[str, Any]:
        """
        Deletes the specified listener.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice.html#VPCLattice.Client.delete_listener)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_vpc_lattice/client/#delete_listener)
        """

    async def delete_resource_policy(self, *, resourceArn: str) -> Dict[str, Any]:
        """
        Deletes the specified resource policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice.html#VPCLattice.Client.delete_resource_policy)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_vpc_lattice/client/#delete_resource_policy)
        """

    async def delete_rule(
        self, *, listenerIdentifier: str, ruleIdentifier: str, serviceIdentifier: str
    ) -> Dict[str, Any]:
        """
        Deletes a listener rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice.html#VPCLattice.Client.delete_rule)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_vpc_lattice/client/#delete_rule)
        """

    async def delete_service(self, *, serviceIdentifier: str) -> DeleteServiceResponseTypeDef:
        """
        Deletes a service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice.html#VPCLattice.Client.delete_service)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_vpc_lattice/client/#delete_service)
        """

    async def delete_service_network(self, *, serviceNetworkIdentifier: str) -> Dict[str, Any]:
        """
        Deletes a service network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice.html#VPCLattice.Client.delete_service_network)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_vpc_lattice/client/#delete_service_network)
        """

    async def delete_service_network_service_association(
        self, *, serviceNetworkServiceAssociationIdentifier: str
    ) -> DeleteServiceNetworkServiceAssociationResponseTypeDef:
        """
        Deletes the association between a specified service and the specific service
        network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice.html#VPCLattice.Client.delete_service_network_service_association)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_vpc_lattice/client/#delete_service_network_service_association)
        """

    async def delete_service_network_vpc_association(
        self, *, serviceNetworkVpcAssociationIdentifier: str
    ) -> DeleteServiceNetworkVpcAssociationResponseTypeDef:
        """
        Disassociates the VPC from the service network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice.html#VPCLattice.Client.delete_service_network_vpc_association)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_vpc_lattice/client/#delete_service_network_vpc_association)
        """

    async def delete_target_group(
        self, *, targetGroupIdentifier: str
    ) -> DeleteTargetGroupResponseTypeDef:
        """
        Deletes a target group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice.html#VPCLattice.Client.delete_target_group)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_vpc_lattice/client/#delete_target_group)
        """

    async def deregister_targets(
        self, *, targetGroupIdentifier: str, targets: Sequence[TargetTypeDef]
    ) -> DeregisterTargetsResponseTypeDef:
        """
        Deregisters the specified targets from the specified target group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice.html#VPCLattice.Client.deregister_targets)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_vpc_lattice/client/#deregister_targets)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice.html#VPCLattice.Client.generate_presigned_url)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_vpc_lattice/client/#generate_presigned_url)
        """

    async def get_access_log_subscription(
        self, *, accessLogSubscriptionIdentifier: str
    ) -> GetAccessLogSubscriptionResponseTypeDef:
        """
        Retrieves information about the specified access log subscription.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice.html#VPCLattice.Client.get_access_log_subscription)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_vpc_lattice/client/#get_access_log_subscription)
        """

    async def get_auth_policy(self, *, resourceIdentifier: str) -> GetAuthPolicyResponseTypeDef:
        """
        Retrieves information about the auth policy for the specified service or
        service
        network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice.html#VPCLattice.Client.get_auth_policy)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_vpc_lattice/client/#get_auth_policy)
        """

    async def get_listener(
        self, *, listenerIdentifier: str, serviceIdentifier: str
    ) -> GetListenerResponseTypeDef:
        """
        Retrieves information about the specified listener for the specified service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice.html#VPCLattice.Client.get_listener)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_vpc_lattice/client/#get_listener)
        """

    async def get_resource_policy(self, *, resourceArn: str) -> GetResourcePolicyResponseTypeDef:
        """
        Retrieves information about the resource policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice.html#VPCLattice.Client.get_resource_policy)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_vpc_lattice/client/#get_resource_policy)
        """

    async def get_rule(
        self, *, listenerIdentifier: str, ruleIdentifier: str, serviceIdentifier: str
    ) -> GetRuleResponseTypeDef:
        """
        Retrieves information about listener rules.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice.html#VPCLattice.Client.get_rule)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_vpc_lattice/client/#get_rule)
        """

    async def get_service(self, *, serviceIdentifier: str) -> GetServiceResponseTypeDef:
        """
        Retrieves information about the specified service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice.html#VPCLattice.Client.get_service)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_vpc_lattice/client/#get_service)
        """

    async def get_service_network(
        self, *, serviceNetworkIdentifier: str
    ) -> GetServiceNetworkResponseTypeDef:
        """
        Retrieves information about the specified service network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice.html#VPCLattice.Client.get_service_network)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_vpc_lattice/client/#get_service_network)
        """

    async def get_service_network_service_association(
        self, *, serviceNetworkServiceAssociationIdentifier: str
    ) -> GetServiceNetworkServiceAssociationResponseTypeDef:
        """
        Retrieves information about the specified association between a service network
        and a
        service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice.html#VPCLattice.Client.get_service_network_service_association)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_vpc_lattice/client/#get_service_network_service_association)
        """

    async def get_service_network_vpc_association(
        self, *, serviceNetworkVpcAssociationIdentifier: str
    ) -> GetServiceNetworkVpcAssociationResponseTypeDef:
        """
        Retrieves information about the association between a service network and a VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice.html#VPCLattice.Client.get_service_network_vpc_association)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_vpc_lattice/client/#get_service_network_vpc_association)
        """

    async def get_target_group(
        self, *, targetGroupIdentifier: str
    ) -> GetTargetGroupResponseTypeDef:
        """
        Retrieves information about the specified target group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice.html#VPCLattice.Client.get_target_group)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_vpc_lattice/client/#get_target_group)
        """

    async def list_access_log_subscriptions(
        self, *, resourceIdentifier: str, maxResults: int = ..., nextToken: str = ...
    ) -> ListAccessLogSubscriptionsResponseTypeDef:
        """
        Lists all access log subscriptions for the specified service network or service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice.html#VPCLattice.Client.list_access_log_subscriptions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_vpc_lattice/client/#list_access_log_subscriptions)
        """

    async def list_listeners(
        self, *, serviceIdentifier: str, maxResults: int = ..., nextToken: str = ...
    ) -> ListListenersResponseTypeDef:
        """
        Lists the listeners for the specified service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice.html#VPCLattice.Client.list_listeners)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_vpc_lattice/client/#list_listeners)
        """

    async def list_rules(
        self,
        *,
        listenerIdentifier: str,
        serviceIdentifier: str,
        maxResults: int = ...,
        nextToken: str = ...,
    ) -> ListRulesResponseTypeDef:
        """
        Lists the rules for the listener.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice.html#VPCLattice.Client.list_rules)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_vpc_lattice/client/#list_rules)
        """

    async def list_service_network_service_associations(
        self,
        *,
        maxResults: int = ...,
        nextToken: str = ...,
        serviceIdentifier: str = ...,
        serviceNetworkIdentifier: str = ...,
    ) -> ListServiceNetworkServiceAssociationsResponseTypeDef:
        """
        Lists the associations between the service network and the service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice.html#VPCLattice.Client.list_service_network_service_associations)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_vpc_lattice/client/#list_service_network_service_associations)
        """

    async def list_service_network_vpc_associations(
        self,
        *,
        maxResults: int = ...,
        nextToken: str = ...,
        serviceNetworkIdentifier: str = ...,
        vpcIdentifier: str = ...,
    ) -> ListServiceNetworkVpcAssociationsResponseTypeDef:
        """
        Lists the service network and VPC associations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice.html#VPCLattice.Client.list_service_network_vpc_associations)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_vpc_lattice/client/#list_service_network_vpc_associations)
        """

    async def list_service_networks(
        self, *, maxResults: int = ..., nextToken: str = ...
    ) -> ListServiceNetworksResponseTypeDef:
        """
        Lists the service networks owned by the caller account or shared with the
        caller
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice.html#VPCLattice.Client.list_service_networks)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_vpc_lattice/client/#list_service_networks)
        """

    async def list_services(
        self, *, maxResults: int = ..., nextToken: str = ...
    ) -> ListServicesResponseTypeDef:
        """
        Lists the services owned by the caller account or shared with the caller
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice.html#VPCLattice.Client.list_services)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_vpc_lattice/client/#list_services)
        """

    async def list_tags_for_resource(
        self, *, resourceArn: str
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists the tags for the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice.html#VPCLattice.Client.list_tags_for_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_vpc_lattice/client/#list_tags_for_resource)
        """

    async def list_target_groups(
        self,
        *,
        maxResults: int = ...,
        nextToken: str = ...,
        targetGroupType: TargetGroupTypeType = ...,
        vpcIdentifier: str = ...,
    ) -> ListTargetGroupsResponseTypeDef:
        """
        Lists your target groups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice.html#VPCLattice.Client.list_target_groups)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_vpc_lattice/client/#list_target_groups)
        """

    async def list_targets(
        self,
        *,
        targetGroupIdentifier: str,
        maxResults: int = ...,
        nextToken: str = ...,
        targets: Sequence[TargetTypeDef] = ...,
    ) -> ListTargetsResponseTypeDef:
        """
        Lists the targets for the target group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice.html#VPCLattice.Client.list_targets)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_vpc_lattice/client/#list_targets)
        """

    async def put_auth_policy(
        self, *, policy: str, resourceIdentifier: str
    ) -> PutAuthPolicyResponseTypeDef:
        """
        Creates or updates the auth policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice.html#VPCLattice.Client.put_auth_policy)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_vpc_lattice/client/#put_auth_policy)
        """

    async def put_resource_policy(self, *, policy: str, resourceArn: str) -> Dict[str, Any]:
        """
        Attaches a resource-based permission policy to a service or service network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice.html#VPCLattice.Client.put_resource_policy)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_vpc_lattice/client/#put_resource_policy)
        """

    async def register_targets(
        self, *, targetGroupIdentifier: str, targets: Sequence[TargetTypeDef]
    ) -> RegisterTargetsResponseTypeDef:
        """
        Registers the targets with the target group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice.html#VPCLattice.Client.register_targets)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_vpc_lattice/client/#register_targets)
        """

    async def tag_resource(self, *, resourceArn: str, tags: Mapping[str, str]) -> Dict[str, Any]:
        """
        Adds the specified tags to the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice.html#VPCLattice.Client.tag_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_vpc_lattice/client/#tag_resource)
        """

    async def untag_resource(self, *, resourceArn: str, tagKeys: Sequence[str]) -> Dict[str, Any]:
        """
        Removes the specified tags from the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice.html#VPCLattice.Client.untag_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_vpc_lattice/client/#untag_resource)
        """

    async def update_access_log_subscription(
        self, *, accessLogSubscriptionIdentifier: str, destinationArn: str
    ) -> UpdateAccessLogSubscriptionResponseTypeDef:
        """
        Updates the specified access log subscription.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice.html#VPCLattice.Client.update_access_log_subscription)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_vpc_lattice/client/#update_access_log_subscription)
        """

    async def update_listener(
        self, *, defaultAction: RuleActionTypeDef, listenerIdentifier: str, serviceIdentifier: str
    ) -> UpdateListenerResponseTypeDef:
        """
        Updates the specified listener for the specified service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice.html#VPCLattice.Client.update_listener)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_vpc_lattice/client/#update_listener)
        """

    async def update_rule(
        self,
        *,
        listenerIdentifier: str,
        ruleIdentifier: str,
        serviceIdentifier: str,
        action: RuleActionTypeDef = ...,
        match: RuleMatchTypeDef = ...,
        priority: int = ...,
    ) -> UpdateRuleResponseTypeDef:
        """
        Updates a rule for the listener.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice.html#VPCLattice.Client.update_rule)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_vpc_lattice/client/#update_rule)
        """

    async def update_service(
        self, *, serviceIdentifier: str, authType: AuthTypeType = ..., certificateArn: str = ...
    ) -> UpdateServiceResponseTypeDef:
        """
        Updates the specified service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice.html#VPCLattice.Client.update_service)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_vpc_lattice/client/#update_service)
        """

    async def update_service_network(
        self, *, authType: AuthTypeType, serviceNetworkIdentifier: str
    ) -> UpdateServiceNetworkResponseTypeDef:
        """
        Updates the specified service network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice.html#VPCLattice.Client.update_service_network)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_vpc_lattice/client/#update_service_network)
        """

    async def update_service_network_vpc_association(
        self, *, securityGroupIds: Sequence[str], serviceNetworkVpcAssociationIdentifier: str
    ) -> UpdateServiceNetworkVpcAssociationResponseTypeDef:
        """
        Updates the service network and VPC association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice.html#VPCLattice.Client.update_service_network_vpc_association)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_vpc_lattice/client/#update_service_network_vpc_association)
        """

    async def update_target_group(
        self, *, healthCheck: HealthCheckConfigTypeDef, targetGroupIdentifier: str
    ) -> UpdateTargetGroupResponseTypeDef:
        """
        Updates the specified target group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice.html#VPCLattice.Client.update_target_group)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_vpc_lattice/client/#update_target_group)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_access_log_subscriptions"]
    ) -> ListAccessLogSubscriptionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice.html#VPCLattice.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_vpc_lattice/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_listeners"]) -> ListListenersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice.html#VPCLattice.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_vpc_lattice/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_rules"]) -> ListRulesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice.html#VPCLattice.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_vpc_lattice/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_service_network_service_associations"]
    ) -> ListServiceNetworkServiceAssociationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice.html#VPCLattice.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_vpc_lattice/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_service_network_vpc_associations"]
    ) -> ListServiceNetworkVpcAssociationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice.html#VPCLattice.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_vpc_lattice/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_service_networks"]
    ) -> ListServiceNetworksPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice.html#VPCLattice.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_vpc_lattice/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_services"]) -> ListServicesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice.html#VPCLattice.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_vpc_lattice/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_target_groups"]
    ) -> ListTargetGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice.html#VPCLattice.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_vpc_lattice/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_targets"]) -> ListTargetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice.html#VPCLattice.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_vpc_lattice/client/#get_paginator)
        """

    async def __aenter__(self) -> "VPCLatticeClient":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice.html#VPCLattice.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_vpc_lattice/client/)
        """

    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> Any:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/vpc-lattice.html#VPCLattice.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_vpc_lattice/client/)
        """
