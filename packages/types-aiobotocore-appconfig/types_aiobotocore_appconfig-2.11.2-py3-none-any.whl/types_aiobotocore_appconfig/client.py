"""
Type annotations for appconfig service client.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appconfig/client/)

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_appconfig.client import AppConfigClient

    session = get_session()
    async with session.create_client("appconfig") as client:
        client: AppConfigClient
    ```
"""

import sys
from typing import Any, Dict, Mapping, Sequence, Type, overload

from aiobotocore.client import AioBaseClient
from botocore.client import ClientMeta

from .literals import ActionPointType, GrowthTypeType, ReplicateToType
from .paginator import (
    ListApplicationsPaginator,
    ListConfigurationProfilesPaginator,
    ListDeploymentsPaginator,
    ListDeploymentStrategiesPaginator,
    ListEnvironmentsPaginator,
    ListExtensionAssociationsPaginator,
    ListExtensionsPaginator,
    ListHostedConfigurationVersionsPaginator,
)
from .type_defs import (
    ActionTypeDef,
    ApplicationResponseTypeDef,
    ApplicationsTypeDef,
    BlobTypeDef,
    ConfigurationProfilesTypeDef,
    ConfigurationProfileTypeDef,
    ConfigurationTypeDef,
    DeploymentStrategiesTypeDef,
    DeploymentStrategyResponseTypeDef,
    DeploymentsTypeDef,
    DeploymentTypeDef,
    EmptyResponseMetadataTypeDef,
    EnvironmentResponseTypeDef,
    EnvironmentsTypeDef,
    ExtensionAssociationsTypeDef,
    ExtensionAssociationTypeDef,
    ExtensionsTypeDef,
    ExtensionTypeDef,
    HostedConfigurationVersionsTypeDef,
    HostedConfigurationVersionTypeDef,
    MonitorTypeDef,
    ParameterTypeDef,
    ResourceTagsTypeDef,
    ValidatorTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("AppConfigClient",)


class BotocoreClientError(Exception):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    BadRequestException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    PayloadTooLargeException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]


class AppConfigClient(AioBaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig.html#AppConfig.Client)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appconfig/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        AppConfigClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig.html#AppConfig.Client.exceptions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appconfig/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig.html#AppConfig.Client.can_paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appconfig/client/#can_paginate)
        """

    async def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig.html#AppConfig.Client.close)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appconfig/client/#close)
        """

    async def create_application(
        self, *, Name: str, Description: str = ..., Tags: Mapping[str, str] = ...
    ) -> ApplicationResponseTypeDef:
        """
        Creates an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig.html#AppConfig.Client.create_application)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appconfig/client/#create_application)
        """

    async def create_configuration_profile(
        self,
        *,
        ApplicationId: str,
        Name: str,
        LocationUri: str,
        Description: str = ...,
        RetrievalRoleArn: str = ...,
        Validators: Sequence[ValidatorTypeDef] = ...,
        Tags: Mapping[str, str] = ...,
        Type: str = ...,
        KmsKeyIdentifier: str = ...,
    ) -> ConfigurationProfileTypeDef:
        """
        Creates a configuration profile, which is information that enables AppConfig to
        access the configuration
        source.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig.html#AppConfig.Client.create_configuration_profile)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appconfig/client/#create_configuration_profile)
        """

    async def create_deployment_strategy(
        self,
        *,
        Name: str,
        DeploymentDurationInMinutes: int,
        GrowthFactor: float,
        Description: str = ...,
        FinalBakeTimeInMinutes: int = ...,
        GrowthType: GrowthTypeType = ...,
        ReplicateTo: ReplicateToType = ...,
        Tags: Mapping[str, str] = ...,
    ) -> DeploymentStrategyResponseTypeDef:
        """
        Creates a deployment strategy that defines important criteria for rolling out
        your configuration to the designated
        targets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig.html#AppConfig.Client.create_deployment_strategy)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appconfig/client/#create_deployment_strategy)
        """

    async def create_environment(
        self,
        *,
        ApplicationId: str,
        Name: str,
        Description: str = ...,
        Monitors: Sequence[MonitorTypeDef] = ...,
        Tags: Mapping[str, str] = ...,
    ) -> EnvironmentResponseTypeDef:
        """
        Creates an environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig.html#AppConfig.Client.create_environment)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appconfig/client/#create_environment)
        """

    async def create_extension(
        self,
        *,
        Name: str,
        Actions: Mapping[ActionPointType, Sequence[ActionTypeDef]],
        Description: str = ...,
        Parameters: Mapping[str, ParameterTypeDef] = ...,
        Tags: Mapping[str, str] = ...,
        LatestVersionNumber: int = ...,
    ) -> ExtensionTypeDef:
        """
        Creates an AppConfig extension.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig.html#AppConfig.Client.create_extension)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appconfig/client/#create_extension)
        """

    async def create_extension_association(
        self,
        *,
        ExtensionIdentifier: str,
        ResourceIdentifier: str,
        ExtensionVersionNumber: int = ...,
        Parameters: Mapping[str, str] = ...,
        Tags: Mapping[str, str] = ...,
    ) -> ExtensionAssociationTypeDef:
        """
        When you create an extension or configure an Amazon Web Services authored
        extension, you associate the extension with an AppConfig application,
        environment, or configuration
        profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig.html#AppConfig.Client.create_extension_association)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appconfig/client/#create_extension_association)
        """

    async def create_hosted_configuration_version(
        self,
        *,
        ApplicationId: str,
        ConfigurationProfileId: str,
        Content: BlobTypeDef,
        ContentType: str,
        Description: str = ...,
        LatestVersionNumber: int = ...,
        VersionLabel: str = ...,
    ) -> HostedConfigurationVersionTypeDef:
        """
        Creates a new configuration in the AppConfig hosted configuration store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig.html#AppConfig.Client.create_hosted_configuration_version)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appconfig/client/#create_hosted_configuration_version)
        """

    async def delete_application(self, *, ApplicationId: str) -> EmptyResponseMetadataTypeDef:
        """
        Deletes an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig.html#AppConfig.Client.delete_application)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appconfig/client/#delete_application)
        """

    async def delete_configuration_profile(
        self, *, ApplicationId: str, ConfigurationProfileId: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a configuration profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig.html#AppConfig.Client.delete_configuration_profile)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appconfig/client/#delete_configuration_profile)
        """

    async def delete_deployment_strategy(
        self, *, DeploymentStrategyId: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a deployment strategy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig.html#AppConfig.Client.delete_deployment_strategy)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appconfig/client/#delete_deployment_strategy)
        """

    async def delete_environment(
        self, *, ApplicationId: str, EnvironmentId: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes an environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig.html#AppConfig.Client.delete_environment)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appconfig/client/#delete_environment)
        """

    async def delete_extension(
        self, *, ExtensionIdentifier: str, VersionNumber: int = ...
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes an AppConfig extension.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig.html#AppConfig.Client.delete_extension)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appconfig/client/#delete_extension)
        """

    async def delete_extension_association(
        self, *, ExtensionAssociationId: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes an extension association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig.html#AppConfig.Client.delete_extension_association)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appconfig/client/#delete_extension_association)
        """

    async def delete_hosted_configuration_version(
        self, *, ApplicationId: str, ConfigurationProfileId: str, VersionNumber: int
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a version of a configuration from the AppConfig hosted configuration
        store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig.html#AppConfig.Client.delete_hosted_configuration_version)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appconfig/client/#delete_hosted_configuration_version)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig.html#AppConfig.Client.generate_presigned_url)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appconfig/client/#generate_presigned_url)
        """

    async def get_application(self, *, ApplicationId: str) -> ApplicationResponseTypeDef:
        """
        Retrieves information about an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig.html#AppConfig.Client.get_application)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appconfig/client/#get_application)
        """

    async def get_configuration(
        self,
        *,
        Application: str,
        Environment: str,
        Configuration: str,
        ClientId: str,
        ClientConfigurationVersion: str = ...,
    ) -> ConfigurationTypeDef:
        """
        (Deprecated) Retrieves the latest deployed configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig.html#AppConfig.Client.get_configuration)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appconfig/client/#get_configuration)
        """

    async def get_configuration_profile(
        self, *, ApplicationId: str, ConfigurationProfileId: str
    ) -> ConfigurationProfileTypeDef:
        """
        Retrieves information about a configuration profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig.html#AppConfig.Client.get_configuration_profile)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appconfig/client/#get_configuration_profile)
        """

    async def get_deployment(
        self, *, ApplicationId: str, EnvironmentId: str, DeploymentNumber: int
    ) -> DeploymentTypeDef:
        """
        Retrieves information about a configuration deployment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig.html#AppConfig.Client.get_deployment)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appconfig/client/#get_deployment)
        """

    async def get_deployment_strategy(
        self, *, DeploymentStrategyId: str
    ) -> DeploymentStrategyResponseTypeDef:
        """
        Retrieves information about a deployment strategy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig.html#AppConfig.Client.get_deployment_strategy)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appconfig/client/#get_deployment_strategy)
        """

    async def get_environment(
        self, *, ApplicationId: str, EnvironmentId: str
    ) -> EnvironmentResponseTypeDef:
        """
        Retrieves information about an environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig.html#AppConfig.Client.get_environment)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appconfig/client/#get_environment)
        """

    async def get_extension(
        self, *, ExtensionIdentifier: str, VersionNumber: int = ...
    ) -> ExtensionTypeDef:
        """
        Returns information about an AppConfig extension.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig.html#AppConfig.Client.get_extension)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appconfig/client/#get_extension)
        """

    async def get_extension_association(
        self, *, ExtensionAssociationId: str
    ) -> ExtensionAssociationTypeDef:
        """
        Returns information about an AppConfig extension association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig.html#AppConfig.Client.get_extension_association)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appconfig/client/#get_extension_association)
        """

    async def get_hosted_configuration_version(
        self, *, ApplicationId: str, ConfigurationProfileId: str, VersionNumber: int
    ) -> HostedConfigurationVersionTypeDef:
        """
        Retrieves information about a specific configuration version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig.html#AppConfig.Client.get_hosted_configuration_version)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appconfig/client/#get_hosted_configuration_version)
        """

    async def list_applications(
        self, *, MaxResults: int = ..., NextToken: str = ...
    ) -> ApplicationsTypeDef:
        """
        Lists all applications in your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig.html#AppConfig.Client.list_applications)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appconfig/client/#list_applications)
        """

    async def list_configuration_profiles(
        self, *, ApplicationId: str, MaxResults: int = ..., NextToken: str = ..., Type: str = ...
    ) -> ConfigurationProfilesTypeDef:
        """
        Lists the configuration profiles for an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig.html#AppConfig.Client.list_configuration_profiles)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appconfig/client/#list_configuration_profiles)
        """

    async def list_deployment_strategies(
        self, *, MaxResults: int = ..., NextToken: str = ...
    ) -> DeploymentStrategiesTypeDef:
        """
        Lists deployment strategies.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig.html#AppConfig.Client.list_deployment_strategies)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appconfig/client/#list_deployment_strategies)
        """

    async def list_deployments(
        self, *, ApplicationId: str, EnvironmentId: str, MaxResults: int = ..., NextToken: str = ...
    ) -> DeploymentsTypeDef:
        """
        Lists the deployments for an environment in descending deployment number order.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig.html#AppConfig.Client.list_deployments)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appconfig/client/#list_deployments)
        """

    async def list_environments(
        self, *, ApplicationId: str, MaxResults: int = ..., NextToken: str = ...
    ) -> EnvironmentsTypeDef:
        """
        Lists the environments for an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig.html#AppConfig.Client.list_environments)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appconfig/client/#list_environments)
        """

    async def list_extension_associations(
        self,
        *,
        ResourceIdentifier: str = ...,
        ExtensionIdentifier: str = ...,
        ExtensionVersionNumber: int = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
    ) -> ExtensionAssociationsTypeDef:
        """
        Lists all AppConfig extension associations in the account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig.html#AppConfig.Client.list_extension_associations)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appconfig/client/#list_extension_associations)
        """

    async def list_extensions(
        self, *, MaxResults: int = ..., NextToken: str = ..., Name: str = ...
    ) -> ExtensionsTypeDef:
        """
        Lists all custom and Amazon Web Services authored AppConfig extensions in the
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig.html#AppConfig.Client.list_extensions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appconfig/client/#list_extensions)
        """

    async def list_hosted_configuration_versions(
        self,
        *,
        ApplicationId: str,
        ConfigurationProfileId: str,
        MaxResults: int = ...,
        NextToken: str = ...,
        VersionLabel: str = ...,
    ) -> HostedConfigurationVersionsTypeDef:
        """
        Lists configurations stored in the AppConfig hosted configuration store by
        version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig.html#AppConfig.Client.list_hosted_configuration_versions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appconfig/client/#list_hosted_configuration_versions)
        """

    async def list_tags_for_resource(self, *, ResourceArn: str) -> ResourceTagsTypeDef:
        """
        Retrieves the list of key-value tags assigned to the resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig.html#AppConfig.Client.list_tags_for_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appconfig/client/#list_tags_for_resource)
        """

    async def start_deployment(
        self,
        *,
        ApplicationId: str,
        EnvironmentId: str,
        DeploymentStrategyId: str,
        ConfigurationProfileId: str,
        ConfigurationVersion: str,
        Description: str = ...,
        Tags: Mapping[str, str] = ...,
        KmsKeyIdentifier: str = ...,
    ) -> DeploymentTypeDef:
        """
        Starts a deployment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig.html#AppConfig.Client.start_deployment)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appconfig/client/#start_deployment)
        """

    async def stop_deployment(
        self, *, ApplicationId: str, EnvironmentId: str, DeploymentNumber: int
    ) -> DeploymentTypeDef:
        """
        Stops a deployment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig.html#AppConfig.Client.stop_deployment)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appconfig/client/#stop_deployment)
        """

    async def tag_resource(
        self, *, ResourceArn: str, Tags: Mapping[str, str]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Assigns metadata to an AppConfig resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig.html#AppConfig.Client.tag_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appconfig/client/#tag_resource)
        """

    async def untag_resource(
        self, *, ResourceArn: str, TagKeys: Sequence[str]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a tag key and value from an AppConfig resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig.html#AppConfig.Client.untag_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appconfig/client/#untag_resource)
        """

    async def update_application(
        self, *, ApplicationId: str, Name: str = ..., Description: str = ...
    ) -> ApplicationResponseTypeDef:
        """
        Updates an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig.html#AppConfig.Client.update_application)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appconfig/client/#update_application)
        """

    async def update_configuration_profile(
        self,
        *,
        ApplicationId: str,
        ConfigurationProfileId: str,
        Name: str = ...,
        Description: str = ...,
        RetrievalRoleArn: str = ...,
        Validators: Sequence[ValidatorTypeDef] = ...,
        KmsKeyIdentifier: str = ...,
    ) -> ConfigurationProfileTypeDef:
        """
        Updates a configuration profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig.html#AppConfig.Client.update_configuration_profile)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appconfig/client/#update_configuration_profile)
        """

    async def update_deployment_strategy(
        self,
        *,
        DeploymentStrategyId: str,
        Description: str = ...,
        DeploymentDurationInMinutes: int = ...,
        FinalBakeTimeInMinutes: int = ...,
        GrowthFactor: float = ...,
        GrowthType: GrowthTypeType = ...,
    ) -> DeploymentStrategyResponseTypeDef:
        """
        Updates a deployment strategy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig.html#AppConfig.Client.update_deployment_strategy)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appconfig/client/#update_deployment_strategy)
        """

    async def update_environment(
        self,
        *,
        ApplicationId: str,
        EnvironmentId: str,
        Name: str = ...,
        Description: str = ...,
        Monitors: Sequence[MonitorTypeDef] = ...,
    ) -> EnvironmentResponseTypeDef:
        """
        Updates an environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig.html#AppConfig.Client.update_environment)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appconfig/client/#update_environment)
        """

    async def update_extension(
        self,
        *,
        ExtensionIdentifier: str,
        Description: str = ...,
        Actions: Mapping[ActionPointType, Sequence[ActionTypeDef]] = ...,
        Parameters: Mapping[str, ParameterTypeDef] = ...,
        VersionNumber: int = ...,
    ) -> ExtensionTypeDef:
        """
        Updates an AppConfig extension.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig.html#AppConfig.Client.update_extension)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appconfig/client/#update_extension)
        """

    async def update_extension_association(
        self, *, ExtensionAssociationId: str, Parameters: Mapping[str, str] = ...
    ) -> ExtensionAssociationTypeDef:
        """
        Updates an association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig.html#AppConfig.Client.update_extension_association)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appconfig/client/#update_extension_association)
        """

    async def validate_configuration(
        self, *, ApplicationId: str, ConfigurationProfileId: str, ConfigurationVersion: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Uses the validators in a configuration profile to validate a configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig.html#AppConfig.Client.validate_configuration)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appconfig/client/#validate_configuration)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_applications"]
    ) -> ListApplicationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig.html#AppConfig.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appconfig/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_configuration_profiles"]
    ) -> ListConfigurationProfilesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig.html#AppConfig.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appconfig/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_deployment_strategies"]
    ) -> ListDeploymentStrategiesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig.html#AppConfig.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appconfig/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_deployments"]
    ) -> ListDeploymentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig.html#AppConfig.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appconfig/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_environments"]
    ) -> ListEnvironmentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig.html#AppConfig.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appconfig/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_extension_associations"]
    ) -> ListExtensionAssociationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig.html#AppConfig.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appconfig/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_extensions"]) -> ListExtensionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig.html#AppConfig.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appconfig/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_hosted_configuration_versions"]
    ) -> ListHostedConfigurationVersionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig.html#AppConfig.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appconfig/client/#get_paginator)
        """

    async def __aenter__(self) -> "AppConfigClient":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig.html#AppConfig.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appconfig/client/)
        """

    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> Any:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig.html#AppConfig.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appconfig/client/)
        """
