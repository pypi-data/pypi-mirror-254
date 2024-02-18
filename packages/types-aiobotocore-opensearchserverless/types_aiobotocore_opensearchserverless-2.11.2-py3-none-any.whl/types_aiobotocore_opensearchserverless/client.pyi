"""
Type annotations for opensearchserverless service client.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearchserverless/client/)

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_opensearchserverless.client import OpenSearchServiceServerlessClient

    session = get_session()
    async with session.create_client("opensearchserverless") as client:
        client: OpenSearchServiceServerlessClient
    ```
"""

import sys
from typing import Any, Dict, Mapping, Sequence, Type

from aiobotocore.client import AioBaseClient
from botocore.client import ClientMeta

from .literals import CollectionTypeType, SecurityPolicyTypeType, StandbyReplicasType
from .type_defs import (
    BatchGetCollectionResponseTypeDef,
    BatchGetEffectiveLifecyclePolicyResponseTypeDef,
    BatchGetLifecyclePolicyResponseTypeDef,
    BatchGetVpcEndpointResponseTypeDef,
    CapacityLimitsTypeDef,
    CollectionFiltersTypeDef,
    CreateAccessPolicyResponseTypeDef,
    CreateCollectionResponseTypeDef,
    CreateLifecyclePolicyResponseTypeDef,
    CreateSecurityConfigResponseTypeDef,
    CreateSecurityPolicyResponseTypeDef,
    CreateVpcEndpointResponseTypeDef,
    DeleteCollectionResponseTypeDef,
    DeleteVpcEndpointResponseTypeDef,
    GetAccessPolicyResponseTypeDef,
    GetAccountSettingsResponseTypeDef,
    GetPoliciesStatsResponseTypeDef,
    GetSecurityConfigResponseTypeDef,
    GetSecurityPolicyResponseTypeDef,
    LifecyclePolicyIdentifierTypeDef,
    LifecyclePolicyResourceIdentifierTypeDef,
    ListAccessPoliciesResponseTypeDef,
    ListCollectionsResponseTypeDef,
    ListLifecyclePoliciesResponseTypeDef,
    ListSecurityConfigsResponseTypeDef,
    ListSecurityPoliciesResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListVpcEndpointsResponseTypeDef,
    SamlConfigOptionsTypeDef,
    TagTypeDef,
    UpdateAccessPolicyResponseTypeDef,
    UpdateAccountSettingsResponseTypeDef,
    UpdateCollectionResponseTypeDef,
    UpdateLifecyclePolicyResponseTypeDef,
    UpdateSecurityConfigResponseTypeDef,
    UpdateSecurityPolicyResponseTypeDef,
    UpdateVpcEndpointResponseTypeDef,
    VpcEndpointFiltersTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("OpenSearchServiceServerlessClient",)

class BotocoreClientError(Exception):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    OcuLimitExceededException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class OpenSearchServiceServerlessClient(AioBaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearchserverless.html#OpenSearchServiceServerless.Client)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearchserverless/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        OpenSearchServiceServerlessClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearchserverless.html#OpenSearchServiceServerless.Client.exceptions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearchserverless/client/#exceptions)
        """

    async def batch_get_collection(
        self, *, ids: Sequence[str] = ..., names: Sequence[str] = ...
    ) -> BatchGetCollectionResponseTypeDef:
        """
        Returns attributes for one or more collections, including the collection
        endpoint and the OpenSearch Dashboards
        endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearchserverless.html#OpenSearchServiceServerless.Client.batch_get_collection)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearchserverless/client/#batch_get_collection)
        """

    async def batch_get_effective_lifecycle_policy(
        self, *, resourceIdentifiers: Sequence[LifecyclePolicyResourceIdentifierTypeDef]
    ) -> BatchGetEffectiveLifecyclePolicyResponseTypeDef:
        """
        Returns a list of successful and failed retrievals for the OpenSearch
        Serverless
        indexes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearchserverless.html#OpenSearchServiceServerless.Client.batch_get_effective_lifecycle_policy)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearchserverless/client/#batch_get_effective_lifecycle_policy)
        """

    async def batch_get_lifecycle_policy(
        self, *, identifiers: Sequence[LifecyclePolicyIdentifierTypeDef]
    ) -> BatchGetLifecyclePolicyResponseTypeDef:
        """
        Returns one or more configured OpenSearch Serverless lifecycle policies.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearchserverless.html#OpenSearchServiceServerless.Client.batch_get_lifecycle_policy)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearchserverless/client/#batch_get_lifecycle_policy)
        """

    async def batch_get_vpc_endpoint(
        self, *, ids: Sequence[str]
    ) -> BatchGetVpcEndpointResponseTypeDef:
        """
        Returns attributes for one or more VPC endpoints associated with the current
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearchserverless.html#OpenSearchServiceServerless.Client.batch_get_vpc_endpoint)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearchserverless/client/#batch_get_vpc_endpoint)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearchserverless.html#OpenSearchServiceServerless.Client.can_paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearchserverless/client/#can_paginate)
        """

    async def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearchserverless.html#OpenSearchServiceServerless.Client.close)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearchserverless/client/#close)
        """

    async def create_access_policy(
        self,
        *,
        name: str,
        policy: str,
        type: Literal["data"],
        clientToken: str = ...,
        description: str = ...,
    ) -> CreateAccessPolicyResponseTypeDef:
        """
        Creates a data access policy for OpenSearch Serverless.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearchserverless.html#OpenSearchServiceServerless.Client.create_access_policy)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearchserverless/client/#create_access_policy)
        """

    async def create_collection(
        self,
        *,
        name: str,
        clientToken: str = ...,
        description: str = ...,
        standbyReplicas: StandbyReplicasType = ...,
        tags: Sequence[TagTypeDef] = ...,
        type: CollectionTypeType = ...,
    ) -> CreateCollectionResponseTypeDef:
        """
        Creates a new OpenSearch Serverless collection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearchserverless.html#OpenSearchServiceServerless.Client.create_collection)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearchserverless/client/#create_collection)
        """

    async def create_lifecycle_policy(
        self,
        *,
        name: str,
        policy: str,
        type: Literal["retention"],
        clientToken: str = ...,
        description: str = ...,
    ) -> CreateLifecyclePolicyResponseTypeDef:
        """
        Creates a lifecyle policy to be applied to OpenSearch Serverless indexes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearchserverless.html#OpenSearchServiceServerless.Client.create_lifecycle_policy)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearchserverless/client/#create_lifecycle_policy)
        """

    async def create_security_config(
        self,
        *,
        name: str,
        type: Literal["saml"],
        clientToken: str = ...,
        description: str = ...,
        samlOptions: SamlConfigOptionsTypeDef = ...,
    ) -> CreateSecurityConfigResponseTypeDef:
        """
        Specifies a security configuration for OpenSearch Serverless.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearchserverless.html#OpenSearchServiceServerless.Client.create_security_config)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearchserverless/client/#create_security_config)
        """

    async def create_security_policy(
        self,
        *,
        name: str,
        policy: str,
        type: SecurityPolicyTypeType,
        clientToken: str = ...,
        description: str = ...,
    ) -> CreateSecurityPolicyResponseTypeDef:
        """
        Creates a security policy to be used by one or more OpenSearch Serverless
        collections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearchserverless.html#OpenSearchServiceServerless.Client.create_security_policy)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearchserverless/client/#create_security_policy)
        """

    async def create_vpc_endpoint(
        self,
        *,
        name: str,
        subnetIds: Sequence[str],
        vpcId: str,
        clientToken: str = ...,
        securityGroupIds: Sequence[str] = ...,
    ) -> CreateVpcEndpointResponseTypeDef:
        """
        Creates an OpenSearch Serverless-managed interface VPC endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearchserverless.html#OpenSearchServiceServerless.Client.create_vpc_endpoint)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearchserverless/client/#create_vpc_endpoint)
        """

    async def delete_access_policy(
        self, *, name: str, type: Literal["data"], clientToken: str = ...
    ) -> Dict[str, Any]:
        """
        Deletes an OpenSearch Serverless access policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearchserverless.html#OpenSearchServiceServerless.Client.delete_access_policy)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearchserverless/client/#delete_access_policy)
        """

    async def delete_collection(
        self, *, id: str, clientToken: str = ...
    ) -> DeleteCollectionResponseTypeDef:
        """
        Deletes an OpenSearch Serverless collection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearchserverless.html#OpenSearchServiceServerless.Client.delete_collection)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearchserverless/client/#delete_collection)
        """

    async def delete_lifecycle_policy(
        self, *, name: str, type: Literal["retention"], clientToken: str = ...
    ) -> Dict[str, Any]:
        """
        Deletes an OpenSearch Serverless lifecycle policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearchserverless.html#OpenSearchServiceServerless.Client.delete_lifecycle_policy)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearchserverless/client/#delete_lifecycle_policy)
        """

    async def delete_security_config(self, *, id: str, clientToken: str = ...) -> Dict[str, Any]:
        """
        Deletes a security configuration for OpenSearch Serverless.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearchserverless.html#OpenSearchServiceServerless.Client.delete_security_config)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearchserverless/client/#delete_security_config)
        """

    async def delete_security_policy(
        self, *, name: str, type: SecurityPolicyTypeType, clientToken: str = ...
    ) -> Dict[str, Any]:
        """
        Deletes an OpenSearch Serverless security policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearchserverless.html#OpenSearchServiceServerless.Client.delete_security_policy)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearchserverless/client/#delete_security_policy)
        """

    async def delete_vpc_endpoint(
        self, *, id: str, clientToken: str = ...
    ) -> DeleteVpcEndpointResponseTypeDef:
        """
        Deletes an OpenSearch Serverless-managed interface endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearchserverless.html#OpenSearchServiceServerless.Client.delete_vpc_endpoint)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearchserverless/client/#delete_vpc_endpoint)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearchserverless.html#OpenSearchServiceServerless.Client.generate_presigned_url)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearchserverless/client/#generate_presigned_url)
        """

    async def get_access_policy(
        self, *, name: str, type: Literal["data"]
    ) -> GetAccessPolicyResponseTypeDef:
        """
        Returns an OpenSearch Serverless access policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearchserverless.html#OpenSearchServiceServerless.Client.get_access_policy)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearchserverless/client/#get_access_policy)
        """

    async def get_account_settings(self) -> GetAccountSettingsResponseTypeDef:
        """
        Returns account-level settings related to OpenSearch Serverless.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearchserverless.html#OpenSearchServiceServerless.Client.get_account_settings)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearchserverless/client/#get_account_settings)
        """

    async def get_policies_stats(self) -> GetPoliciesStatsResponseTypeDef:
        """
        Returns statistical information about your OpenSearch Serverless access
        policies, security configurations, and security
        policies.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearchserverless.html#OpenSearchServiceServerless.Client.get_policies_stats)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearchserverless/client/#get_policies_stats)
        """

    async def get_security_config(self, *, id: str) -> GetSecurityConfigResponseTypeDef:
        """
        Returns information about an OpenSearch Serverless security configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearchserverless.html#OpenSearchServiceServerless.Client.get_security_config)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearchserverless/client/#get_security_config)
        """

    async def get_security_policy(
        self, *, name: str, type: SecurityPolicyTypeType
    ) -> GetSecurityPolicyResponseTypeDef:
        """
        Returns information about a configured OpenSearch Serverless security policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearchserverless.html#OpenSearchServiceServerless.Client.get_security_policy)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearchserverless/client/#get_security_policy)
        """

    async def list_access_policies(
        self,
        *,
        type: Literal["data"],
        maxResults: int = ...,
        nextToken: str = ...,
        resource: Sequence[str] = ...,
    ) -> ListAccessPoliciesResponseTypeDef:
        """
        Returns information about a list of OpenSearch Serverless access policies.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearchserverless.html#OpenSearchServiceServerless.Client.list_access_policies)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearchserverless/client/#list_access_policies)
        """

    async def list_collections(
        self,
        *,
        collectionFilters: CollectionFiltersTypeDef = ...,
        maxResults: int = ...,
        nextToken: str = ...,
    ) -> ListCollectionsResponseTypeDef:
        """
        Lists all OpenSearch Serverless collections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearchserverless.html#OpenSearchServiceServerless.Client.list_collections)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearchserverless/client/#list_collections)
        """

    async def list_lifecycle_policies(
        self,
        *,
        type: Literal["retention"],
        maxResults: int = ...,
        nextToken: str = ...,
        resources: Sequence[str] = ...,
    ) -> ListLifecyclePoliciesResponseTypeDef:
        """
        Returns a list of OpenSearch Serverless lifecycle policies.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearchserverless.html#OpenSearchServiceServerless.Client.list_lifecycle_policies)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearchserverless/client/#list_lifecycle_policies)
        """

    async def list_security_configs(
        self, *, type: Literal["saml"], maxResults: int = ..., nextToken: str = ...
    ) -> ListSecurityConfigsResponseTypeDef:
        """
        Returns information about configured OpenSearch Serverless security
        configurations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearchserverless.html#OpenSearchServiceServerless.Client.list_security_configs)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearchserverless/client/#list_security_configs)
        """

    async def list_security_policies(
        self,
        *,
        type: SecurityPolicyTypeType,
        maxResults: int = ...,
        nextToken: str = ...,
        resource: Sequence[str] = ...,
    ) -> ListSecurityPoliciesResponseTypeDef:
        """
        Returns information about configured OpenSearch Serverless security policies.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearchserverless.html#OpenSearchServiceServerless.Client.list_security_policies)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearchserverless/client/#list_security_policies)
        """

    async def list_tags_for_resource(
        self, *, resourceArn: str
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Returns the tags for an OpenSearch Serverless resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearchserverless.html#OpenSearchServiceServerless.Client.list_tags_for_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearchserverless/client/#list_tags_for_resource)
        """

    async def list_vpc_endpoints(
        self,
        *,
        maxResults: int = ...,
        nextToken: str = ...,
        vpcEndpointFilters: VpcEndpointFiltersTypeDef = ...,
    ) -> ListVpcEndpointsResponseTypeDef:
        """
        Returns the OpenSearch Serverless-managed interface VPC endpoints associated
        with the current
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearchserverless.html#OpenSearchServiceServerless.Client.list_vpc_endpoints)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearchserverless/client/#list_vpc_endpoints)
        """

    async def tag_resource(self, *, resourceArn: str, tags: Sequence[TagTypeDef]) -> Dict[str, Any]:
        """
        Associates tags with an OpenSearch Serverless resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearchserverless.html#OpenSearchServiceServerless.Client.tag_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearchserverless/client/#tag_resource)
        """

    async def untag_resource(self, *, resourceArn: str, tagKeys: Sequence[str]) -> Dict[str, Any]:
        """
        Removes a tag or set of tags from an OpenSearch Serverless resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearchserverless.html#OpenSearchServiceServerless.Client.untag_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearchserverless/client/#untag_resource)
        """

    async def update_access_policy(
        self,
        *,
        name: str,
        policyVersion: str,
        type: Literal["data"],
        clientToken: str = ...,
        description: str = ...,
        policy: str = ...,
    ) -> UpdateAccessPolicyResponseTypeDef:
        """
        Updates an OpenSearch Serverless access policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearchserverless.html#OpenSearchServiceServerless.Client.update_access_policy)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearchserverless/client/#update_access_policy)
        """

    async def update_account_settings(
        self, *, capacityLimits: CapacityLimitsTypeDef = ...
    ) -> UpdateAccountSettingsResponseTypeDef:
        """
        Update the OpenSearch Serverless settings for the current Amazon Web Services
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearchserverless.html#OpenSearchServiceServerless.Client.update_account_settings)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearchserverless/client/#update_account_settings)
        """

    async def update_collection(
        self, *, id: str, clientToken: str = ..., description: str = ...
    ) -> UpdateCollectionResponseTypeDef:
        """
        Updates an OpenSearch Serverless collection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearchserverless.html#OpenSearchServiceServerless.Client.update_collection)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearchserverless/client/#update_collection)
        """

    async def update_lifecycle_policy(
        self,
        *,
        name: str,
        policyVersion: str,
        type: Literal["retention"],
        clientToken: str = ...,
        description: str = ...,
        policy: str = ...,
    ) -> UpdateLifecyclePolicyResponseTypeDef:
        """
        Updates an OpenSearch Serverless access policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearchserverless.html#OpenSearchServiceServerless.Client.update_lifecycle_policy)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearchserverless/client/#update_lifecycle_policy)
        """

    async def update_security_config(
        self,
        *,
        configVersion: str,
        id: str,
        clientToken: str = ...,
        description: str = ...,
        samlOptions: SamlConfigOptionsTypeDef = ...,
    ) -> UpdateSecurityConfigResponseTypeDef:
        """
        Updates a security configuration for OpenSearch Serverless.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearchserverless.html#OpenSearchServiceServerless.Client.update_security_config)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearchserverless/client/#update_security_config)
        """

    async def update_security_policy(
        self,
        *,
        name: str,
        policyVersion: str,
        type: SecurityPolicyTypeType,
        clientToken: str = ...,
        description: str = ...,
        policy: str = ...,
    ) -> UpdateSecurityPolicyResponseTypeDef:
        """
        Updates an OpenSearch Serverless security policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearchserverless.html#OpenSearchServiceServerless.Client.update_security_policy)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearchserverless/client/#update_security_policy)
        """

    async def update_vpc_endpoint(
        self,
        *,
        id: str,
        addSecurityGroupIds: Sequence[str] = ...,
        addSubnetIds: Sequence[str] = ...,
        clientToken: str = ...,
        removeSecurityGroupIds: Sequence[str] = ...,
        removeSubnetIds: Sequence[str] = ...,
    ) -> UpdateVpcEndpointResponseTypeDef:
        """
        Updates an OpenSearch Serverless-managed interface endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearchserverless.html#OpenSearchServiceServerless.Client.update_vpc_endpoint)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearchserverless/client/#update_vpc_endpoint)
        """

    async def __aenter__(self) -> "OpenSearchServiceServerlessClient":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearchserverless.html#OpenSearchServiceServerless.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearchserverless/client/)
        """

    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> Any:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearchserverless.html#OpenSearchServiceServerless.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearchserverless/client/)
        """
