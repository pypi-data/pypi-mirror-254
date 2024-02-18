"""
Type annotations for eks service client.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_eks/client/)

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_eks.client import EKSClient

    session = get_session()
    async with session.create_client("eks") as client:
        client: EKSClient
    ```
"""

import sys
from typing import Any, Dict, Mapping, Sequence, Type, overload

from aiobotocore.client import AioBaseClient
from botocore.client import ClientMeta

from .literals import (
    AMITypesType,
    CapacityTypesType,
    EksAnywhereSubscriptionStatusType,
    ResolveConflictsType,
)
from .paginator import (
    DescribeAddonVersionsPaginator,
    ListAccessEntriesPaginator,
    ListAccessPoliciesPaginator,
    ListAddonsPaginator,
    ListAssociatedAccessPoliciesPaginator,
    ListClustersPaginator,
    ListEksAnywhereSubscriptionsPaginator,
    ListFargateProfilesPaginator,
    ListIdentityProviderConfigsPaginator,
    ListInsightsPaginator,
    ListNodegroupsPaginator,
    ListPodIdentityAssociationsPaginator,
    ListUpdatesPaginator,
)
from .type_defs import (
    AccessScopeTypeDef,
    AssociateAccessPolicyResponseTypeDef,
    AssociateEncryptionConfigResponseTypeDef,
    AssociateIdentityProviderConfigResponseTypeDef,
    ConnectorConfigRequestTypeDef,
    CreateAccessConfigRequestTypeDef,
    CreateAccessEntryResponseTypeDef,
    CreateAddonResponseTypeDef,
    CreateClusterResponseTypeDef,
    CreateEksAnywhereSubscriptionResponseTypeDef,
    CreateFargateProfileResponseTypeDef,
    CreateNodegroupResponseTypeDef,
    CreatePodIdentityAssociationResponseTypeDef,
    DeleteAddonResponseTypeDef,
    DeleteClusterResponseTypeDef,
    DeleteEksAnywhereSubscriptionResponseTypeDef,
    DeleteFargateProfileResponseTypeDef,
    DeleteNodegroupResponseTypeDef,
    DeletePodIdentityAssociationResponseTypeDef,
    DeregisterClusterResponseTypeDef,
    DescribeAccessEntryResponseTypeDef,
    DescribeAddonConfigurationResponseTypeDef,
    DescribeAddonResponseTypeDef,
    DescribeAddonVersionsResponseTypeDef,
    DescribeClusterResponseTypeDef,
    DescribeEksAnywhereSubscriptionResponseTypeDef,
    DescribeFargateProfileResponseTypeDef,
    DescribeIdentityProviderConfigResponseTypeDef,
    DescribeInsightResponseTypeDef,
    DescribeNodegroupResponseTypeDef,
    DescribePodIdentityAssociationResponseTypeDef,
    DescribeUpdateResponseTypeDef,
    DisassociateIdentityProviderConfigResponseTypeDef,
    EksAnywhereSubscriptionTermTypeDef,
    EncryptionConfigTypeDef,
    FargateProfileSelectorTypeDef,
    IdentityProviderConfigTypeDef,
    InsightsFilterTypeDef,
    KubernetesNetworkConfigRequestTypeDef,
    LaunchTemplateSpecificationTypeDef,
    ListAccessEntriesResponseTypeDef,
    ListAccessPoliciesResponseTypeDef,
    ListAddonsResponseTypeDef,
    ListAssociatedAccessPoliciesResponseTypeDef,
    ListClustersResponseTypeDef,
    ListEksAnywhereSubscriptionsResponseTypeDef,
    ListFargateProfilesResponseTypeDef,
    ListIdentityProviderConfigsResponseTypeDef,
    ListInsightsResponseTypeDef,
    ListNodegroupsResponseTypeDef,
    ListPodIdentityAssociationsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListUpdatesResponseTypeDef,
    LoggingTypeDef,
    NodegroupScalingConfigTypeDef,
    NodegroupUpdateConfigTypeDef,
    OidcIdentityProviderConfigRequestTypeDef,
    OutpostConfigRequestTypeDef,
    RegisterClusterResponseTypeDef,
    RemoteAccessConfigTypeDef,
    TaintTypeDef,
    UpdateAccessConfigRequestTypeDef,
    UpdateAccessEntryResponseTypeDef,
    UpdateAddonResponseTypeDef,
    UpdateClusterConfigResponseTypeDef,
    UpdateClusterVersionResponseTypeDef,
    UpdateEksAnywhereSubscriptionResponseTypeDef,
    UpdateLabelsPayloadTypeDef,
    UpdateNodegroupConfigResponseTypeDef,
    UpdateNodegroupVersionResponseTypeDef,
    UpdatePodIdentityAssociationResponseTypeDef,
    UpdateTaintsPayloadTypeDef,
    VpcConfigRequestTypeDef,
)
from .waiter import (
    AddonActiveWaiter,
    AddonDeletedWaiter,
    ClusterActiveWaiter,
    ClusterDeletedWaiter,
    FargateProfileActiveWaiter,
    FargateProfileDeletedWaiter,
    NodegroupActiveWaiter,
    NodegroupDeletedWaiter,
)

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("EKSClient",)


class BotocoreClientError(Exception):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    BadRequestException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ClientException: Type[BotocoreClientError]
    InvalidParameterException: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]
    ResourceInUseException: Type[BotocoreClientError]
    ResourceLimitExceededException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ResourcePropagationDelayException: Type[BotocoreClientError]
    ServerException: Type[BotocoreClientError]
    ServiceUnavailableException: Type[BotocoreClientError]
    UnsupportedAvailabilityZoneException: Type[BotocoreClientError]


class EKSClient(AioBaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_eks/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        EKSClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.exceptions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_eks/client/#exceptions)
        """

    async def associate_access_policy(
        self,
        *,
        clusterName: str,
        principalArn: str,
        policyArn: str,
        accessScope: AccessScopeTypeDef,
    ) -> AssociateAccessPolicyResponseTypeDef:
        """
        Associates an access policy and its scope to an access entry.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.associate_access_policy)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_eks/client/#associate_access_policy)
        """

    async def associate_encryption_config(
        self,
        *,
        clusterName: str,
        encryptionConfig: Sequence[EncryptionConfigTypeDef],
        clientRequestToken: str = ...,
    ) -> AssociateEncryptionConfigResponseTypeDef:
        """
        Associates an encryption configuration to an existing cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.associate_encryption_config)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_eks/client/#associate_encryption_config)
        """

    async def associate_identity_provider_config(
        self,
        *,
        clusterName: str,
        oidc: OidcIdentityProviderConfigRequestTypeDef,
        tags: Mapping[str, str] = ...,
        clientRequestToken: str = ...,
    ) -> AssociateIdentityProviderConfigResponseTypeDef:
        """
        Associates an identity provider configuration to a cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.associate_identity_provider_config)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_eks/client/#associate_identity_provider_config)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.can_paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_eks/client/#can_paginate)
        """

    async def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.close)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_eks/client/#close)
        """

    async def create_access_entry(
        self,
        *,
        clusterName: str,
        principalArn: str,
        kubernetesGroups: Sequence[str] = ...,
        tags: Mapping[str, str] = ...,
        clientRequestToken: str = ...,
        username: str = ...,
        type: str = ...,
    ) -> CreateAccessEntryResponseTypeDef:
        """
        Creates an access entry.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.create_access_entry)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_eks/client/#create_access_entry)
        """

    async def create_addon(
        self,
        *,
        clusterName: str,
        addonName: str,
        addonVersion: str = ...,
        serviceAccountRoleArn: str = ...,
        resolveConflicts: ResolveConflictsType = ...,
        clientRequestToken: str = ...,
        tags: Mapping[str, str] = ...,
        configurationValues: str = ...,
    ) -> CreateAddonResponseTypeDef:
        """
        Creates an Amazon EKS add-on.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.create_addon)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_eks/client/#create_addon)
        """

    async def create_cluster(
        self,
        *,
        name: str,
        roleArn: str,
        resourcesVpcConfig: VpcConfigRequestTypeDef,
        version: str = ...,
        kubernetesNetworkConfig: KubernetesNetworkConfigRequestTypeDef = ...,
        logging: LoggingTypeDef = ...,
        clientRequestToken: str = ...,
        tags: Mapping[str, str] = ...,
        encryptionConfig: Sequence[EncryptionConfigTypeDef] = ...,
        outpostConfig: OutpostConfigRequestTypeDef = ...,
        accessConfig: CreateAccessConfigRequestTypeDef = ...,
    ) -> CreateClusterResponseTypeDef:
        """
        Creates an Amazon EKS control plane.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.create_cluster)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_eks/client/#create_cluster)
        """

    async def create_eks_anywhere_subscription(
        self,
        *,
        name: str,
        term: EksAnywhereSubscriptionTermTypeDef,
        licenseQuantity: int = ...,
        licenseType: Literal["Cluster"] = ...,
        autoRenew: bool = ...,
        clientRequestToken: str = ...,
        tags: Mapping[str, str] = ...,
    ) -> CreateEksAnywhereSubscriptionResponseTypeDef:
        """
        Creates an EKS Anywhere subscription.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.create_eks_anywhere_subscription)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_eks/client/#create_eks_anywhere_subscription)
        """

    async def create_fargate_profile(
        self,
        *,
        fargateProfileName: str,
        clusterName: str,
        podExecutionRoleArn: str,
        subnets: Sequence[str] = ...,
        selectors: Sequence[FargateProfileSelectorTypeDef] = ...,
        clientRequestToken: str = ...,
        tags: Mapping[str, str] = ...,
    ) -> CreateFargateProfileResponseTypeDef:
        """
        Creates an Fargate profile for your Amazon EKS cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.create_fargate_profile)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_eks/client/#create_fargate_profile)
        """

    async def create_nodegroup(
        self,
        *,
        clusterName: str,
        nodegroupName: str,
        subnets: Sequence[str],
        nodeRole: str,
        scalingConfig: NodegroupScalingConfigTypeDef = ...,
        diskSize: int = ...,
        instanceTypes: Sequence[str] = ...,
        amiType: AMITypesType = ...,
        remoteAccess: RemoteAccessConfigTypeDef = ...,
        labels: Mapping[str, str] = ...,
        taints: Sequence[TaintTypeDef] = ...,
        tags: Mapping[str, str] = ...,
        clientRequestToken: str = ...,
        launchTemplate: LaunchTemplateSpecificationTypeDef = ...,
        updateConfig: NodegroupUpdateConfigTypeDef = ...,
        capacityType: CapacityTypesType = ...,
        version: str = ...,
        releaseVersion: str = ...,
    ) -> CreateNodegroupResponseTypeDef:
        """
        Creates a managed node group for an Amazon EKS cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.create_nodegroup)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_eks/client/#create_nodegroup)
        """

    async def create_pod_identity_association(
        self,
        *,
        clusterName: str,
        namespace: str,
        serviceAccount: str,
        roleArn: str,
        clientRequestToken: str = ...,
        tags: Mapping[str, str] = ...,
    ) -> CreatePodIdentityAssociationResponseTypeDef:
        """
        Creates an EKS Pod Identity association between a service account in an Amazon
        EKS cluster and an IAM role with *EKS Pod
        Identity*.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.create_pod_identity_association)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_eks/client/#create_pod_identity_association)
        """

    async def delete_access_entry(self, *, clusterName: str, principalArn: str) -> Dict[str, Any]:
        """
        Deletes an access entry.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.delete_access_entry)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_eks/client/#delete_access_entry)
        """

    async def delete_addon(
        self, *, clusterName: str, addonName: str, preserve: bool = ...
    ) -> DeleteAddonResponseTypeDef:
        """
        Deletes an Amazon EKS add-on.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.delete_addon)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_eks/client/#delete_addon)
        """

    async def delete_cluster(self, *, name: str) -> DeleteClusterResponseTypeDef:
        """
        Deletes an Amazon EKS cluster control plane.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.delete_cluster)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_eks/client/#delete_cluster)
        """

    async def delete_eks_anywhere_subscription(
        self, *, id: str
    ) -> DeleteEksAnywhereSubscriptionResponseTypeDef:
        """
        Deletes an expired or inactive subscription.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.delete_eks_anywhere_subscription)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_eks/client/#delete_eks_anywhere_subscription)
        """

    async def delete_fargate_profile(
        self, *, clusterName: str, fargateProfileName: str
    ) -> DeleteFargateProfileResponseTypeDef:
        """
        Deletes an Fargate profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.delete_fargate_profile)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_eks/client/#delete_fargate_profile)
        """

    async def delete_nodegroup(
        self, *, clusterName: str, nodegroupName: str
    ) -> DeleteNodegroupResponseTypeDef:
        """
        Deletes a managed node group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.delete_nodegroup)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_eks/client/#delete_nodegroup)
        """

    async def delete_pod_identity_association(
        self, *, clusterName: str, associationId: str
    ) -> DeletePodIdentityAssociationResponseTypeDef:
        """
        Deletes a EKS Pod Identity association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.delete_pod_identity_association)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_eks/client/#delete_pod_identity_association)
        """

    async def deregister_cluster(self, *, name: str) -> DeregisterClusterResponseTypeDef:
        """
        Deregisters a connected cluster to remove it from the Amazon EKS control plane.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.deregister_cluster)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_eks/client/#deregister_cluster)
        """

    async def describe_access_entry(
        self, *, clusterName: str, principalArn: str
    ) -> DescribeAccessEntryResponseTypeDef:
        """
        Describes an access entry.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.describe_access_entry)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_eks/client/#describe_access_entry)
        """

    async def describe_addon(
        self, *, clusterName: str, addonName: str
    ) -> DescribeAddonResponseTypeDef:
        """
        Describes an Amazon EKS add-on.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.describe_addon)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_eks/client/#describe_addon)
        """

    async def describe_addon_configuration(
        self, *, addonName: str, addonVersion: str
    ) -> DescribeAddonConfigurationResponseTypeDef:
        """
        Returns configuration options.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.describe_addon_configuration)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_eks/client/#describe_addon_configuration)
        """

    async def describe_addon_versions(
        self,
        *,
        kubernetesVersion: str = ...,
        maxResults: int = ...,
        nextToken: str = ...,
        addonName: str = ...,
        types: Sequence[str] = ...,
        publishers: Sequence[str] = ...,
        owners: Sequence[str] = ...,
    ) -> DescribeAddonVersionsResponseTypeDef:
        """
        Describes the versions for an add-on.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.describe_addon_versions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_eks/client/#describe_addon_versions)
        """

    async def describe_cluster(self, *, name: str) -> DescribeClusterResponseTypeDef:
        """
        Describes an Amazon EKS cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.describe_cluster)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_eks/client/#describe_cluster)
        """

    async def describe_eks_anywhere_subscription(
        self, *, id: str
    ) -> DescribeEksAnywhereSubscriptionResponseTypeDef:
        """
        Returns descriptive information about a subscription.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.describe_eks_anywhere_subscription)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_eks/client/#describe_eks_anywhere_subscription)
        """

    async def describe_fargate_profile(
        self, *, clusterName: str, fargateProfileName: str
    ) -> DescribeFargateProfileResponseTypeDef:
        """
        Describes an Fargate profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.describe_fargate_profile)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_eks/client/#describe_fargate_profile)
        """

    async def describe_identity_provider_config(
        self, *, clusterName: str, identityProviderConfig: IdentityProviderConfigTypeDef
    ) -> DescribeIdentityProviderConfigResponseTypeDef:
        """
        Describes an identity provider configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.describe_identity_provider_config)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_eks/client/#describe_identity_provider_config)
        """

    async def describe_insight(
        self, *, clusterName: str, id: str
    ) -> DescribeInsightResponseTypeDef:
        """
        Returns details about an insight that you specify using its ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.describe_insight)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_eks/client/#describe_insight)
        """

    async def describe_nodegroup(
        self, *, clusterName: str, nodegroupName: str
    ) -> DescribeNodegroupResponseTypeDef:
        """
        Describes a managed node group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.describe_nodegroup)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_eks/client/#describe_nodegroup)
        """

    async def describe_pod_identity_association(
        self, *, clusterName: str, associationId: str
    ) -> DescribePodIdentityAssociationResponseTypeDef:
        """
        Returns descriptive information about an EKS Pod Identity association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.describe_pod_identity_association)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_eks/client/#describe_pod_identity_association)
        """

    async def describe_update(
        self, *, name: str, updateId: str, nodegroupName: str = ..., addonName: str = ...
    ) -> DescribeUpdateResponseTypeDef:
        """
        Describes an update to an Amazon EKS resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.describe_update)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_eks/client/#describe_update)
        """

    async def disassociate_access_policy(
        self, *, clusterName: str, principalArn: str, policyArn: str
    ) -> Dict[str, Any]:
        """
        Disassociates an access policy from an access entry.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.disassociate_access_policy)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_eks/client/#disassociate_access_policy)
        """

    async def disassociate_identity_provider_config(
        self,
        *,
        clusterName: str,
        identityProviderConfig: IdentityProviderConfigTypeDef,
        clientRequestToken: str = ...,
    ) -> DisassociateIdentityProviderConfigResponseTypeDef:
        """
        Disassociates an identity provider configuration from a cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.disassociate_identity_provider_config)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_eks/client/#disassociate_identity_provider_config)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.generate_presigned_url)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_eks/client/#generate_presigned_url)
        """

    async def list_access_entries(
        self,
        *,
        clusterName: str,
        associatedPolicyArn: str = ...,
        maxResults: int = ...,
        nextToken: str = ...,
    ) -> ListAccessEntriesResponseTypeDef:
        """
        Lists the access entries for your cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.list_access_entries)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_eks/client/#list_access_entries)
        """

    async def list_access_policies(
        self, *, maxResults: int = ..., nextToken: str = ...
    ) -> ListAccessPoliciesResponseTypeDef:
        """
        Lists the available access policies.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.list_access_policies)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_eks/client/#list_access_policies)
        """

    async def list_addons(
        self, *, clusterName: str, maxResults: int = ..., nextToken: str = ...
    ) -> ListAddonsResponseTypeDef:
        """
        Lists the installed add-ons.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.list_addons)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_eks/client/#list_addons)
        """

    async def list_associated_access_policies(
        self, *, clusterName: str, principalArn: str, maxResults: int = ..., nextToken: str = ...
    ) -> ListAssociatedAccessPoliciesResponseTypeDef:
        """
        Lists the access policies associated with an access entry.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.list_associated_access_policies)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_eks/client/#list_associated_access_policies)
        """

    async def list_clusters(
        self, *, maxResults: int = ..., nextToken: str = ..., include: Sequence[str] = ...
    ) -> ListClustersResponseTypeDef:
        """
        Lists the Amazon EKS clusters in your Amazon Web Services account in the
        specified Amazon Web Services
        Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.list_clusters)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_eks/client/#list_clusters)
        """

    async def list_eks_anywhere_subscriptions(
        self,
        *,
        maxResults: int = ...,
        nextToken: str = ...,
        includeStatus: Sequence[EksAnywhereSubscriptionStatusType] = ...,
    ) -> ListEksAnywhereSubscriptionsResponseTypeDef:
        """
        Displays the full description of the subscription.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.list_eks_anywhere_subscriptions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_eks/client/#list_eks_anywhere_subscriptions)
        """

    async def list_fargate_profiles(
        self, *, clusterName: str, maxResults: int = ..., nextToken: str = ...
    ) -> ListFargateProfilesResponseTypeDef:
        """
        Lists the Fargate profiles associated with the specified cluster in your Amazon
        Web Services account in the specified Amazon Web Services
        Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.list_fargate_profiles)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_eks/client/#list_fargate_profiles)
        """

    async def list_identity_provider_configs(
        self, *, clusterName: str, maxResults: int = ..., nextToken: str = ...
    ) -> ListIdentityProviderConfigsResponseTypeDef:
        """
        Lists the identity provider configurations for your cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.list_identity_provider_configs)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_eks/client/#list_identity_provider_configs)
        """

    async def list_insights(
        self,
        *,
        clusterName: str,
        filter: InsightsFilterTypeDef = ...,
        maxResults: int = ...,
        nextToken: str = ...,
    ) -> ListInsightsResponseTypeDef:
        """
        Returns a list of all insights checked for against the specified cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.list_insights)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_eks/client/#list_insights)
        """

    async def list_nodegroups(
        self, *, clusterName: str, maxResults: int = ..., nextToken: str = ...
    ) -> ListNodegroupsResponseTypeDef:
        """
        Lists the managed node groups associated with the specified cluster in your
        Amazon Web Services account in the specified Amazon Web Services
        Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.list_nodegroups)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_eks/client/#list_nodegroups)
        """

    async def list_pod_identity_associations(
        self,
        *,
        clusterName: str,
        namespace: str = ...,
        serviceAccount: str = ...,
        maxResults: int = ...,
        nextToken: str = ...,
    ) -> ListPodIdentityAssociationsResponseTypeDef:
        """
        List the EKS Pod Identity associations in a cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.list_pod_identity_associations)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_eks/client/#list_pod_identity_associations)
        """

    async def list_tags_for_resource(
        self, *, resourceArn: str
    ) -> ListTagsForResourceResponseTypeDef:
        """
        List the tags for an Amazon EKS resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.list_tags_for_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_eks/client/#list_tags_for_resource)
        """

    async def list_updates(
        self,
        *,
        name: str,
        nodegroupName: str = ...,
        addonName: str = ...,
        nextToken: str = ...,
        maxResults: int = ...,
    ) -> ListUpdatesResponseTypeDef:
        """
        Lists the updates associated with an Amazon EKS resource in your Amazon Web
        Services account, in the specified Amazon Web Services
        Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.list_updates)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_eks/client/#list_updates)
        """

    async def register_cluster(
        self,
        *,
        name: str,
        connectorConfig: ConnectorConfigRequestTypeDef,
        clientRequestToken: str = ...,
        tags: Mapping[str, str] = ...,
    ) -> RegisterClusterResponseTypeDef:
        """
        Connects a Kubernetes cluster to the Amazon EKS control plane.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.register_cluster)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_eks/client/#register_cluster)
        """

    async def tag_resource(self, *, resourceArn: str, tags: Mapping[str, str]) -> Dict[str, Any]:
        """
        Associates the specified tags to an Amazon EKS resource with the specified
        `resourceArn`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.tag_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_eks/client/#tag_resource)
        """

    async def untag_resource(self, *, resourceArn: str, tagKeys: Sequence[str]) -> Dict[str, Any]:
        """
        Deletes specified tags from an Amazon EKS resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.untag_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_eks/client/#untag_resource)
        """

    async def update_access_entry(
        self,
        *,
        clusterName: str,
        principalArn: str,
        kubernetesGroups: Sequence[str] = ...,
        clientRequestToken: str = ...,
        username: str = ...,
    ) -> UpdateAccessEntryResponseTypeDef:
        """
        Updates an access entry.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.update_access_entry)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_eks/client/#update_access_entry)
        """

    async def update_addon(
        self,
        *,
        clusterName: str,
        addonName: str,
        addonVersion: str = ...,
        serviceAccountRoleArn: str = ...,
        resolveConflicts: ResolveConflictsType = ...,
        clientRequestToken: str = ...,
        configurationValues: str = ...,
    ) -> UpdateAddonResponseTypeDef:
        """
        Updates an Amazon EKS add-on.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.update_addon)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_eks/client/#update_addon)
        """

    async def update_cluster_config(
        self,
        *,
        name: str,
        resourcesVpcConfig: VpcConfigRequestTypeDef = ...,
        logging: LoggingTypeDef = ...,
        clientRequestToken: str = ...,
        accessConfig: UpdateAccessConfigRequestTypeDef = ...,
    ) -> UpdateClusterConfigResponseTypeDef:
        """
        Updates an Amazon EKS cluster configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.update_cluster_config)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_eks/client/#update_cluster_config)
        """

    async def update_cluster_version(
        self, *, name: str, version: str, clientRequestToken: str = ...
    ) -> UpdateClusterVersionResponseTypeDef:
        """
        Updates an Amazon EKS cluster to the specified Kubernetes version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.update_cluster_version)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_eks/client/#update_cluster_version)
        """

    async def update_eks_anywhere_subscription(
        self, *, id: str, autoRenew: bool, clientRequestToken: str = ...
    ) -> UpdateEksAnywhereSubscriptionResponseTypeDef:
        """
        Update an EKS Anywhere Subscription.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.update_eks_anywhere_subscription)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_eks/client/#update_eks_anywhere_subscription)
        """

    async def update_nodegroup_config(
        self,
        *,
        clusterName: str,
        nodegroupName: str,
        labels: UpdateLabelsPayloadTypeDef = ...,
        taints: UpdateTaintsPayloadTypeDef = ...,
        scalingConfig: NodegroupScalingConfigTypeDef = ...,
        updateConfig: NodegroupUpdateConfigTypeDef = ...,
        clientRequestToken: str = ...,
    ) -> UpdateNodegroupConfigResponseTypeDef:
        """
        Updates an Amazon EKS managed node group configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.update_nodegroup_config)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_eks/client/#update_nodegroup_config)
        """

    async def update_nodegroup_version(
        self,
        *,
        clusterName: str,
        nodegroupName: str,
        version: str = ...,
        releaseVersion: str = ...,
        launchTemplate: LaunchTemplateSpecificationTypeDef = ...,
        force: bool = ...,
        clientRequestToken: str = ...,
    ) -> UpdateNodegroupVersionResponseTypeDef:
        """
        Updates the Kubernetes version or AMI version of an Amazon EKS managed node
        group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.update_nodegroup_version)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_eks/client/#update_nodegroup_version)
        """

    async def update_pod_identity_association(
        self,
        *,
        clusterName: str,
        associationId: str,
        roleArn: str = ...,
        clientRequestToken: str = ...,
    ) -> UpdatePodIdentityAssociationResponseTypeDef:
        """
        Updates a EKS Pod Identity association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.update_pod_identity_association)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_eks/client/#update_pod_identity_association)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_addon_versions"]
    ) -> DescribeAddonVersionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_eks/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_access_entries"]
    ) -> ListAccessEntriesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_eks/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_access_policies"]
    ) -> ListAccessPoliciesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_eks/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_addons"]) -> ListAddonsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_eks/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_associated_access_policies"]
    ) -> ListAssociatedAccessPoliciesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_eks/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_clusters"]) -> ListClustersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_eks/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_eks_anywhere_subscriptions"]
    ) -> ListEksAnywhereSubscriptionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_eks/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_fargate_profiles"]
    ) -> ListFargateProfilesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_eks/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_identity_provider_configs"]
    ) -> ListIdentityProviderConfigsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_eks/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_insights"]) -> ListInsightsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_eks/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_nodegroups"]) -> ListNodegroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_eks/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_pod_identity_associations"]
    ) -> ListPodIdentityAssociationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_eks/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_updates"]) -> ListUpdatesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_eks/client/#get_paginator)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["addon_active"]) -> AddonActiveWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.get_waiter)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_eks/client/#get_waiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["addon_deleted"]) -> AddonDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.get_waiter)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_eks/client/#get_waiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["cluster_active"]) -> ClusterActiveWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.get_waiter)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_eks/client/#get_waiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["cluster_deleted"]) -> ClusterDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.get_waiter)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_eks/client/#get_waiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["fargate_profile_active"]
    ) -> FargateProfileActiveWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.get_waiter)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_eks/client/#get_waiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["fargate_profile_deleted"]
    ) -> FargateProfileDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.get_waiter)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_eks/client/#get_waiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["nodegroup_active"]) -> NodegroupActiveWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.get_waiter)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_eks/client/#get_waiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["nodegroup_deleted"]) -> NodegroupDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.get_waiter)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_eks/client/#get_waiter)
        """

    async def __aenter__(self) -> "EKSClient":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_eks/client/)
        """

    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> Any:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_eks/client/)
        """
