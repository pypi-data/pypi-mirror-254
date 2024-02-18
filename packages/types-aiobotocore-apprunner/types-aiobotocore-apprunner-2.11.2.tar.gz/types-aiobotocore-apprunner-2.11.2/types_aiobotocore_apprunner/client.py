"""
Type annotations for apprunner service client.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_apprunner/client/)

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_apprunner.client import AppRunnerClient

    session = get_session()
    async with session.create_client("apprunner") as client:
        client: AppRunnerClient
    ```
"""

from typing import Any, Dict, Mapping, Sequence, Type

from aiobotocore.client import AioBaseClient
from botocore.client import ClientMeta

from .literals import ProviderTypeType
from .type_defs import (
    AssociateCustomDomainResponseTypeDef,
    CreateAutoScalingConfigurationResponseTypeDef,
    CreateConnectionResponseTypeDef,
    CreateObservabilityConfigurationResponseTypeDef,
    CreateServiceResponseTypeDef,
    CreateVpcConnectorResponseTypeDef,
    CreateVpcIngressConnectionResponseTypeDef,
    DeleteAutoScalingConfigurationResponseTypeDef,
    DeleteConnectionResponseTypeDef,
    DeleteObservabilityConfigurationResponseTypeDef,
    DeleteServiceResponseTypeDef,
    DeleteVpcConnectorResponseTypeDef,
    DeleteVpcIngressConnectionResponseTypeDef,
    DescribeAutoScalingConfigurationResponseTypeDef,
    DescribeCustomDomainsResponseTypeDef,
    DescribeObservabilityConfigurationResponseTypeDef,
    DescribeServiceResponseTypeDef,
    DescribeVpcConnectorResponseTypeDef,
    DescribeVpcIngressConnectionResponseTypeDef,
    DisassociateCustomDomainResponseTypeDef,
    EncryptionConfigurationTypeDef,
    HealthCheckConfigurationTypeDef,
    IngressVpcConfigurationTypeDef,
    InstanceConfigurationTypeDef,
    ListAutoScalingConfigurationsResponseTypeDef,
    ListConnectionsResponseTypeDef,
    ListObservabilityConfigurationsResponseTypeDef,
    ListOperationsResponseTypeDef,
    ListServicesForAutoScalingConfigurationResponseTypeDef,
    ListServicesResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListVpcConnectorsResponseTypeDef,
    ListVpcIngressConnectionsFilterTypeDef,
    ListVpcIngressConnectionsResponseTypeDef,
    NetworkConfigurationTypeDef,
    PauseServiceResponseTypeDef,
    ResumeServiceResponseTypeDef,
    ServiceObservabilityConfigurationTypeDef,
    SourceConfigurationTypeDef,
    StartDeploymentResponseTypeDef,
    TagTypeDef,
    TraceConfigurationTypeDef,
    UpdateDefaultAutoScalingConfigurationResponseTypeDef,
    UpdateServiceResponseTypeDef,
    UpdateVpcIngressConnectionResponseTypeDef,
)

__all__ = ("AppRunnerClient",)


class BotocoreClientError(Exception):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    InternalServiceErrorException: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]
    InvalidStateException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]


class AppRunnerClient(AioBaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apprunner.html#AppRunner.Client)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_apprunner/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        AppRunnerClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apprunner.html#AppRunner.Client.exceptions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_apprunner/client/#exceptions)
        """

    async def associate_custom_domain(
        self, *, ServiceArn: str, DomainName: str, EnableWWWSubdomain: bool = ...
    ) -> AssociateCustomDomainResponseTypeDef:
        """
        Associate your own domain name with the App Runner subdomain URL of your App
        Runner
        service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apprunner.html#AppRunner.Client.associate_custom_domain)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_apprunner/client/#associate_custom_domain)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apprunner.html#AppRunner.Client.can_paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_apprunner/client/#can_paginate)
        """

    async def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apprunner.html#AppRunner.Client.close)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_apprunner/client/#close)
        """

    async def create_auto_scaling_configuration(
        self,
        *,
        AutoScalingConfigurationName: str,
        MaxConcurrency: int = ...,
        MinSize: int = ...,
        MaxSize: int = ...,
        Tags: Sequence[TagTypeDef] = ...,
    ) -> CreateAutoScalingConfigurationResponseTypeDef:
        """
        Create an App Runner automatic scaling configuration resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apprunner.html#AppRunner.Client.create_auto_scaling_configuration)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_apprunner/client/#create_auto_scaling_configuration)
        """

    async def create_connection(
        self,
        *,
        ConnectionName: str,
        ProviderType: ProviderTypeType,
        Tags: Sequence[TagTypeDef] = ...,
    ) -> CreateConnectionResponseTypeDef:
        """
        Create an App Runner connection resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apprunner.html#AppRunner.Client.create_connection)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_apprunner/client/#create_connection)
        """

    async def create_observability_configuration(
        self,
        *,
        ObservabilityConfigurationName: str,
        TraceConfiguration: TraceConfigurationTypeDef = ...,
        Tags: Sequence[TagTypeDef] = ...,
    ) -> CreateObservabilityConfigurationResponseTypeDef:
        """
        Create an App Runner observability configuration resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apprunner.html#AppRunner.Client.create_observability_configuration)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_apprunner/client/#create_observability_configuration)
        """

    async def create_service(
        self,
        *,
        ServiceName: str,
        SourceConfiguration: SourceConfigurationTypeDef,
        InstanceConfiguration: InstanceConfigurationTypeDef = ...,
        Tags: Sequence[TagTypeDef] = ...,
        EncryptionConfiguration: EncryptionConfigurationTypeDef = ...,
        HealthCheckConfiguration: HealthCheckConfigurationTypeDef = ...,
        AutoScalingConfigurationArn: str = ...,
        NetworkConfiguration: NetworkConfigurationTypeDef = ...,
        ObservabilityConfiguration: ServiceObservabilityConfigurationTypeDef = ...,
    ) -> CreateServiceResponseTypeDef:
        """
        Create an App Runner service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apprunner.html#AppRunner.Client.create_service)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_apprunner/client/#create_service)
        """

    async def create_vpc_connector(
        self,
        *,
        VpcConnectorName: str,
        Subnets: Sequence[str],
        SecurityGroups: Sequence[str] = ...,
        Tags: Sequence[TagTypeDef] = ...,
    ) -> CreateVpcConnectorResponseTypeDef:
        """
        Create an App Runner VPC connector resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apprunner.html#AppRunner.Client.create_vpc_connector)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_apprunner/client/#create_vpc_connector)
        """

    async def create_vpc_ingress_connection(
        self,
        *,
        ServiceArn: str,
        VpcIngressConnectionName: str,
        IngressVpcConfiguration: IngressVpcConfigurationTypeDef,
        Tags: Sequence[TagTypeDef] = ...,
    ) -> CreateVpcIngressConnectionResponseTypeDef:
        """
        Create an App Runner VPC Ingress Connection resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apprunner.html#AppRunner.Client.create_vpc_ingress_connection)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_apprunner/client/#create_vpc_ingress_connection)
        """

    async def delete_auto_scaling_configuration(
        self, *, AutoScalingConfigurationArn: str, DeleteAllRevisions: bool = ...
    ) -> DeleteAutoScalingConfigurationResponseTypeDef:
        """
        Delete an App Runner automatic scaling configuration resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apprunner.html#AppRunner.Client.delete_auto_scaling_configuration)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_apprunner/client/#delete_auto_scaling_configuration)
        """

    async def delete_connection(self, *, ConnectionArn: str) -> DeleteConnectionResponseTypeDef:
        """
        Delete an App Runner connection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apprunner.html#AppRunner.Client.delete_connection)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_apprunner/client/#delete_connection)
        """

    async def delete_observability_configuration(
        self, *, ObservabilityConfigurationArn: str
    ) -> DeleteObservabilityConfigurationResponseTypeDef:
        """
        Delete an App Runner observability configuration resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apprunner.html#AppRunner.Client.delete_observability_configuration)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_apprunner/client/#delete_observability_configuration)
        """

    async def delete_service(self, *, ServiceArn: str) -> DeleteServiceResponseTypeDef:
        """
        Delete an App Runner service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apprunner.html#AppRunner.Client.delete_service)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_apprunner/client/#delete_service)
        """

    async def delete_vpc_connector(
        self, *, VpcConnectorArn: str
    ) -> DeleteVpcConnectorResponseTypeDef:
        """
        Delete an App Runner VPC connector resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apprunner.html#AppRunner.Client.delete_vpc_connector)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_apprunner/client/#delete_vpc_connector)
        """

    async def delete_vpc_ingress_connection(
        self, *, VpcIngressConnectionArn: str
    ) -> DeleteVpcIngressConnectionResponseTypeDef:
        """
        Delete an App Runner VPC Ingress Connection resource that's associated with an
        App Runner
        service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apprunner.html#AppRunner.Client.delete_vpc_ingress_connection)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_apprunner/client/#delete_vpc_ingress_connection)
        """

    async def describe_auto_scaling_configuration(
        self, *, AutoScalingConfigurationArn: str
    ) -> DescribeAutoScalingConfigurationResponseTypeDef:
        """
        Return a full description of an App Runner automatic scaling configuration
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apprunner.html#AppRunner.Client.describe_auto_scaling_configuration)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_apprunner/client/#describe_auto_scaling_configuration)
        """

    async def describe_custom_domains(
        self, *, ServiceArn: str, NextToken: str = ..., MaxResults: int = ...
    ) -> DescribeCustomDomainsResponseTypeDef:
        """
        Return a description of custom domain names that are associated with an App
        Runner
        service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apprunner.html#AppRunner.Client.describe_custom_domains)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_apprunner/client/#describe_custom_domains)
        """

    async def describe_observability_configuration(
        self, *, ObservabilityConfigurationArn: str
    ) -> DescribeObservabilityConfigurationResponseTypeDef:
        """
        Return a full description of an App Runner observability configuration resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apprunner.html#AppRunner.Client.describe_observability_configuration)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_apprunner/client/#describe_observability_configuration)
        """

    async def describe_service(self, *, ServiceArn: str) -> DescribeServiceResponseTypeDef:
        """
        Return a full description of an App Runner service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apprunner.html#AppRunner.Client.describe_service)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_apprunner/client/#describe_service)
        """

    async def describe_vpc_connector(
        self, *, VpcConnectorArn: str
    ) -> DescribeVpcConnectorResponseTypeDef:
        """
        Return a description of an App Runner VPC connector resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apprunner.html#AppRunner.Client.describe_vpc_connector)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_apprunner/client/#describe_vpc_connector)
        """

    async def describe_vpc_ingress_connection(
        self, *, VpcIngressConnectionArn: str
    ) -> DescribeVpcIngressConnectionResponseTypeDef:
        """
        Return a full description of an App Runner VPC Ingress Connection resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apprunner.html#AppRunner.Client.describe_vpc_ingress_connection)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_apprunner/client/#describe_vpc_ingress_connection)
        """

    async def disassociate_custom_domain(
        self, *, ServiceArn: str, DomainName: str
    ) -> DisassociateCustomDomainResponseTypeDef:
        """
        Disassociate a custom domain name from an App Runner service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apprunner.html#AppRunner.Client.disassociate_custom_domain)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_apprunner/client/#disassociate_custom_domain)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apprunner.html#AppRunner.Client.generate_presigned_url)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_apprunner/client/#generate_presigned_url)
        """

    async def list_auto_scaling_configurations(
        self,
        *,
        AutoScalingConfigurationName: str = ...,
        LatestOnly: bool = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
    ) -> ListAutoScalingConfigurationsResponseTypeDef:
        """
        Returns a list of active App Runner automatic scaling configurations in your
        Amazon Web Services
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apprunner.html#AppRunner.Client.list_auto_scaling_configurations)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_apprunner/client/#list_auto_scaling_configurations)
        """

    async def list_connections(
        self, *, ConnectionName: str = ..., MaxResults: int = ..., NextToken: str = ...
    ) -> ListConnectionsResponseTypeDef:
        """
        Returns a list of App Runner connections that are associated with your Amazon
        Web Services
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apprunner.html#AppRunner.Client.list_connections)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_apprunner/client/#list_connections)
        """

    async def list_observability_configurations(
        self,
        *,
        ObservabilityConfigurationName: str = ...,
        LatestOnly: bool = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
    ) -> ListObservabilityConfigurationsResponseTypeDef:
        """
        Returns a list of active App Runner observability configurations in your Amazon
        Web Services
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apprunner.html#AppRunner.Client.list_observability_configurations)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_apprunner/client/#list_observability_configurations)
        """

    async def list_operations(
        self, *, ServiceArn: str, NextToken: str = ..., MaxResults: int = ...
    ) -> ListOperationsResponseTypeDef:
        """
        Return a list of operations that occurred on an App Runner service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apprunner.html#AppRunner.Client.list_operations)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_apprunner/client/#list_operations)
        """

    async def list_services(
        self, *, NextToken: str = ..., MaxResults: int = ...
    ) -> ListServicesResponseTypeDef:
        """
        Returns a list of running App Runner services in your Amazon Web Services
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apprunner.html#AppRunner.Client.list_services)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_apprunner/client/#list_services)
        """

    async def list_services_for_auto_scaling_configuration(
        self, *, AutoScalingConfigurationArn: str, MaxResults: int = ..., NextToken: str = ...
    ) -> ListServicesForAutoScalingConfigurationResponseTypeDef:
        """
        Returns a list of the associated App Runner services using an auto scaling
        configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apprunner.html#AppRunner.Client.list_services_for_auto_scaling_configuration)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_apprunner/client/#list_services_for_auto_scaling_configuration)
        """

    async def list_tags_for_resource(
        self, *, ResourceArn: str
    ) -> ListTagsForResourceResponseTypeDef:
        """
        List tags that are associated with for an App Runner resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apprunner.html#AppRunner.Client.list_tags_for_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_apprunner/client/#list_tags_for_resource)
        """

    async def list_vpc_connectors(
        self, *, MaxResults: int = ..., NextToken: str = ...
    ) -> ListVpcConnectorsResponseTypeDef:
        """
        Returns a list of App Runner VPC connectors in your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apprunner.html#AppRunner.Client.list_vpc_connectors)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_apprunner/client/#list_vpc_connectors)
        """

    async def list_vpc_ingress_connections(
        self,
        *,
        Filter: ListVpcIngressConnectionsFilterTypeDef = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
    ) -> ListVpcIngressConnectionsResponseTypeDef:
        """
        Return a list of App Runner VPC Ingress Connections in your Amazon Web Services
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apprunner.html#AppRunner.Client.list_vpc_ingress_connections)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_apprunner/client/#list_vpc_ingress_connections)
        """

    async def pause_service(self, *, ServiceArn: str) -> PauseServiceResponseTypeDef:
        """
        Pause an active App Runner service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apprunner.html#AppRunner.Client.pause_service)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_apprunner/client/#pause_service)
        """

    async def resume_service(self, *, ServiceArn: str) -> ResumeServiceResponseTypeDef:
        """
        Resume an active App Runner service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apprunner.html#AppRunner.Client.resume_service)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_apprunner/client/#resume_service)
        """

    async def start_deployment(self, *, ServiceArn: str) -> StartDeploymentResponseTypeDef:
        """
        Initiate a manual deployment of the latest commit in a source code repository
        or the latest image in a source image repository to an App Runner
        service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apprunner.html#AppRunner.Client.start_deployment)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_apprunner/client/#start_deployment)
        """

    async def tag_resource(self, *, ResourceArn: str, Tags: Sequence[TagTypeDef]) -> Dict[str, Any]:
        """
        Add tags to, or update the tag values of, an App Runner resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apprunner.html#AppRunner.Client.tag_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_apprunner/client/#tag_resource)
        """

    async def untag_resource(self, *, ResourceArn: str, TagKeys: Sequence[str]) -> Dict[str, Any]:
        """
        Remove tags from an App Runner resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apprunner.html#AppRunner.Client.untag_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_apprunner/client/#untag_resource)
        """

    async def update_default_auto_scaling_configuration(
        self, *, AutoScalingConfigurationArn: str
    ) -> UpdateDefaultAutoScalingConfigurationResponseTypeDef:
        """
        Update an auto scaling configuration to be the default.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apprunner.html#AppRunner.Client.update_default_auto_scaling_configuration)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_apprunner/client/#update_default_auto_scaling_configuration)
        """

    async def update_service(
        self,
        *,
        ServiceArn: str,
        SourceConfiguration: SourceConfigurationTypeDef = ...,
        InstanceConfiguration: InstanceConfigurationTypeDef = ...,
        AutoScalingConfigurationArn: str = ...,
        HealthCheckConfiguration: HealthCheckConfigurationTypeDef = ...,
        NetworkConfiguration: NetworkConfigurationTypeDef = ...,
        ObservabilityConfiguration: ServiceObservabilityConfigurationTypeDef = ...,
    ) -> UpdateServiceResponseTypeDef:
        """
        Update an App Runner service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apprunner.html#AppRunner.Client.update_service)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_apprunner/client/#update_service)
        """

    async def update_vpc_ingress_connection(
        self,
        *,
        VpcIngressConnectionArn: str,
        IngressVpcConfiguration: IngressVpcConfigurationTypeDef,
    ) -> UpdateVpcIngressConnectionResponseTypeDef:
        """
        Update an existing App Runner VPC Ingress Connection resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apprunner.html#AppRunner.Client.update_vpc_ingress_connection)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_apprunner/client/#update_vpc_ingress_connection)
        """

    async def __aenter__(self) -> "AppRunnerClient":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apprunner.html#AppRunner.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_apprunner/client/)
        """

    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> Any:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apprunner.html#AppRunner.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_apprunner/client/)
        """
