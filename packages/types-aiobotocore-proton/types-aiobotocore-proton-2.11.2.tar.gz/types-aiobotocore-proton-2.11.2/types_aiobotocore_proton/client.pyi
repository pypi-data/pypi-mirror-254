"""
Type annotations for proton service client.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/)

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_proton.client import ProtonClient

    session = get_session()
    async with session.create_client("proton") as client:
        client: ProtonClient
    ```
"""

import sys
from typing import Any, Dict, Mapping, Sequence, Type, overload

from aiobotocore.client import AioBaseClient
from botocore.client import ClientMeta

from .literals import (
    ComponentDeploymentUpdateTypeType,
    DeploymentUpdateTypeType,
    EnvironmentAccountConnectionRequesterAccountTypeType,
    EnvironmentAccountConnectionStatusType,
    ListServiceInstancesSortByType,
    RepositoryProviderType,
    ResourceDeploymentStatusType,
    SortOrderType,
    SyncTypeType,
    TemplateTypeType,
    TemplateVersionStatusType,
)
from .paginator import (
    ListComponentOutputsPaginator,
    ListComponentProvisionedResourcesPaginator,
    ListComponentsPaginator,
    ListDeploymentsPaginator,
    ListEnvironmentAccountConnectionsPaginator,
    ListEnvironmentOutputsPaginator,
    ListEnvironmentProvisionedResourcesPaginator,
    ListEnvironmentsPaginator,
    ListEnvironmentTemplatesPaginator,
    ListEnvironmentTemplateVersionsPaginator,
    ListRepositoriesPaginator,
    ListRepositorySyncDefinitionsPaginator,
    ListServiceInstanceOutputsPaginator,
    ListServiceInstanceProvisionedResourcesPaginator,
    ListServiceInstancesPaginator,
    ListServicePipelineOutputsPaginator,
    ListServicePipelineProvisionedResourcesPaginator,
    ListServicesPaginator,
    ListServiceTemplatesPaginator,
    ListServiceTemplateVersionsPaginator,
    ListTagsForResourcePaginator,
)
from .type_defs import (
    AcceptEnvironmentAccountConnectionOutputTypeDef,
    CancelComponentDeploymentOutputTypeDef,
    CancelEnvironmentDeploymentOutputTypeDef,
    CancelServiceInstanceDeploymentOutputTypeDef,
    CancelServicePipelineDeploymentOutputTypeDef,
    CompatibleEnvironmentTemplateInputTypeDef,
    CreateComponentOutputTypeDef,
    CreateEnvironmentAccountConnectionOutputTypeDef,
    CreateEnvironmentOutputTypeDef,
    CreateEnvironmentTemplateOutputTypeDef,
    CreateEnvironmentTemplateVersionOutputTypeDef,
    CreateRepositoryOutputTypeDef,
    CreateServiceInstanceOutputTypeDef,
    CreateServiceOutputTypeDef,
    CreateServiceSyncConfigOutputTypeDef,
    CreateServiceTemplateOutputTypeDef,
    CreateServiceTemplateVersionOutputTypeDef,
    CreateTemplateSyncConfigOutputTypeDef,
    DeleteComponentOutputTypeDef,
    DeleteDeploymentOutputTypeDef,
    DeleteEnvironmentAccountConnectionOutputTypeDef,
    DeleteEnvironmentOutputTypeDef,
    DeleteEnvironmentTemplateOutputTypeDef,
    DeleteEnvironmentTemplateVersionOutputTypeDef,
    DeleteRepositoryOutputTypeDef,
    DeleteServiceOutputTypeDef,
    DeleteServiceSyncConfigOutputTypeDef,
    DeleteServiceTemplateOutputTypeDef,
    DeleteServiceTemplateVersionOutputTypeDef,
    DeleteTemplateSyncConfigOutputTypeDef,
    EnvironmentTemplateFilterTypeDef,
    GetAccountSettingsOutputTypeDef,
    GetComponentOutputTypeDef,
    GetDeploymentOutputTypeDef,
    GetEnvironmentAccountConnectionOutputTypeDef,
    GetEnvironmentOutputTypeDef,
    GetEnvironmentTemplateOutputTypeDef,
    GetEnvironmentTemplateVersionOutputTypeDef,
    GetRepositoryOutputTypeDef,
    GetRepositorySyncStatusOutputTypeDef,
    GetResourcesSummaryOutputTypeDef,
    GetServiceInstanceOutputTypeDef,
    GetServiceInstanceSyncStatusOutputTypeDef,
    GetServiceOutputTypeDef,
    GetServiceSyncBlockerSummaryOutputTypeDef,
    GetServiceSyncConfigOutputTypeDef,
    GetServiceTemplateOutputTypeDef,
    GetServiceTemplateVersionOutputTypeDef,
    GetTemplateSyncConfigOutputTypeDef,
    GetTemplateSyncStatusOutputTypeDef,
    ListComponentOutputsOutputTypeDef,
    ListComponentProvisionedResourcesOutputTypeDef,
    ListComponentsOutputTypeDef,
    ListDeploymentsOutputTypeDef,
    ListEnvironmentAccountConnectionsOutputTypeDef,
    ListEnvironmentOutputsOutputTypeDef,
    ListEnvironmentProvisionedResourcesOutputTypeDef,
    ListEnvironmentsOutputTypeDef,
    ListEnvironmentTemplatesOutputTypeDef,
    ListEnvironmentTemplateVersionsOutputTypeDef,
    ListRepositoriesOutputTypeDef,
    ListRepositorySyncDefinitionsOutputTypeDef,
    ListServiceInstanceOutputsOutputTypeDef,
    ListServiceInstanceProvisionedResourcesOutputTypeDef,
    ListServiceInstancesFilterTypeDef,
    ListServiceInstancesOutputTypeDef,
    ListServicePipelineOutputsOutputTypeDef,
    ListServicePipelineProvisionedResourcesOutputTypeDef,
    ListServicesOutputTypeDef,
    ListServiceTemplatesOutputTypeDef,
    ListServiceTemplateVersionsOutputTypeDef,
    ListTagsForResourceOutputTypeDef,
    OutputTypeDef,
    RejectEnvironmentAccountConnectionOutputTypeDef,
    RepositoryBranchInputTypeDef,
    TagTypeDef,
    TemplateVersionSourceInputTypeDef,
    UpdateAccountSettingsOutputTypeDef,
    UpdateComponentOutputTypeDef,
    UpdateEnvironmentAccountConnectionOutputTypeDef,
    UpdateEnvironmentOutputTypeDef,
    UpdateEnvironmentTemplateOutputTypeDef,
    UpdateEnvironmentTemplateVersionOutputTypeDef,
    UpdateServiceInstanceOutputTypeDef,
    UpdateServiceOutputTypeDef,
    UpdateServicePipelineOutputTypeDef,
    UpdateServiceSyncBlockerOutputTypeDef,
    UpdateServiceSyncConfigOutputTypeDef,
    UpdateServiceTemplateOutputTypeDef,
    UpdateServiceTemplateVersionOutputTypeDef,
    UpdateTemplateSyncConfigOutputTypeDef,
)
from .waiter import (
    ComponentDeletedWaiter,
    ComponentDeployedWaiter,
    EnvironmentDeployedWaiter,
    EnvironmentTemplateVersionRegisteredWaiter,
    ServiceCreatedWaiter,
    ServiceDeletedWaiter,
    ServiceInstanceDeployedWaiter,
    ServicePipelineDeployedWaiter,
    ServiceTemplateVersionRegisteredWaiter,
    ServiceUpdatedWaiter,
)

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("ProtonClient",)

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

class ProtonClient(AioBaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        ProtonClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.exceptions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#exceptions)
        """

    async def accept_environment_account_connection(
        self, *, id: str
    ) -> AcceptEnvironmentAccountConnectionOutputTypeDef:
        """
        In a management account, an environment account connection request is accepted.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.accept_environment_account_connection)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#accept_environment_account_connection)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.can_paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#can_paginate)
        """

    async def cancel_component_deployment(
        self, *, componentName: str
    ) -> CancelComponentDeploymentOutputTypeDef:
        """
        Attempts to cancel a component deployment (for a component that is in the
        `IN_PROGRESS` deployment
        status).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.cancel_component_deployment)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#cancel_component_deployment)
        """

    async def cancel_environment_deployment(
        self, *, environmentName: str
    ) -> CancelEnvironmentDeploymentOutputTypeDef:
        """
        Attempts to cancel an environment deployment on an  UpdateEnvironment action,
        if the deployment is
        `IN_PROGRESS`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.cancel_environment_deployment)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#cancel_environment_deployment)
        """

    async def cancel_service_instance_deployment(
        self, *, serviceInstanceName: str, serviceName: str
    ) -> CancelServiceInstanceDeploymentOutputTypeDef:
        """
        Attempts to cancel a service instance deployment on an  UpdateServiceInstance
        action, if the deployment is
        `IN_PROGRESS`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.cancel_service_instance_deployment)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#cancel_service_instance_deployment)
        """

    async def cancel_service_pipeline_deployment(
        self, *, serviceName: str
    ) -> CancelServicePipelineDeploymentOutputTypeDef:
        """
        Attempts to cancel a service pipeline deployment on an  UpdateServicePipeline
        action, if the deployment is
        `IN_PROGRESS`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.cancel_service_pipeline_deployment)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#cancel_service_pipeline_deployment)
        """

    async def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.close)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#close)
        """

    async def create_component(
        self,
        *,
        manifest: str,
        name: str,
        templateFile: str,
        clientToken: str = ...,
        description: str = ...,
        environmentName: str = ...,
        serviceInstanceName: str = ...,
        serviceName: str = ...,
        serviceSpec: str = ...,
        tags: Sequence[TagTypeDef] = ...,
    ) -> CreateComponentOutputTypeDef:
        """
        Create an Proton component.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.create_component)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#create_component)
        """

    async def create_environment(
        self,
        *,
        name: str,
        spec: str,
        templateMajorVersion: str,
        templateName: str,
        codebuildRoleArn: str = ...,
        componentRoleArn: str = ...,
        description: str = ...,
        environmentAccountConnectionId: str = ...,
        protonServiceRoleArn: str = ...,
        provisioningRepository: RepositoryBranchInputTypeDef = ...,
        tags: Sequence[TagTypeDef] = ...,
        templateMinorVersion: str = ...,
    ) -> CreateEnvironmentOutputTypeDef:
        """
        Deploy a new environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.create_environment)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#create_environment)
        """

    async def create_environment_account_connection(
        self,
        *,
        environmentName: str,
        managementAccountId: str,
        clientToken: str = ...,
        codebuildRoleArn: str = ...,
        componentRoleArn: str = ...,
        roleArn: str = ...,
        tags: Sequence[TagTypeDef] = ...,
    ) -> CreateEnvironmentAccountConnectionOutputTypeDef:
        """
        Create an environment account connection in an environment account so that
        environment infrastructure resources can be provisioned in the environment
        account from a management
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.create_environment_account_connection)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#create_environment_account_connection)
        """

    async def create_environment_template(
        self,
        *,
        name: str,
        description: str = ...,
        displayName: str = ...,
        encryptionKey: str = ...,
        provisioning: Literal["CUSTOMER_MANAGED"] = ...,
        tags: Sequence[TagTypeDef] = ...,
    ) -> CreateEnvironmentTemplateOutputTypeDef:
        """
        Create an environment template for Proton.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.create_environment_template)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#create_environment_template)
        """

    async def create_environment_template_version(
        self,
        *,
        source: TemplateVersionSourceInputTypeDef,
        templateName: str,
        clientToken: str = ...,
        description: str = ...,
        majorVersion: str = ...,
        tags: Sequence[TagTypeDef] = ...,
    ) -> CreateEnvironmentTemplateVersionOutputTypeDef:
        """
        Create a new major or minor version of an environment template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.create_environment_template_version)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#create_environment_template_version)
        """

    async def create_repository(
        self,
        *,
        connectionArn: str,
        name: str,
        provider: RepositoryProviderType,
        encryptionKey: str = ...,
        tags: Sequence[TagTypeDef] = ...,
    ) -> CreateRepositoryOutputTypeDef:
        """
        Create and register a link to a repository.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.create_repository)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#create_repository)
        """

    async def create_service(
        self,
        *,
        name: str,
        spec: str,
        templateMajorVersion: str,
        templateName: str,
        branchName: str = ...,
        description: str = ...,
        repositoryConnectionArn: str = ...,
        repositoryId: str = ...,
        tags: Sequence[TagTypeDef] = ...,
        templateMinorVersion: str = ...,
    ) -> CreateServiceOutputTypeDef:
        """
        Create an Proton service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.create_service)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#create_service)
        """

    async def create_service_instance(
        self,
        *,
        name: str,
        serviceName: str,
        spec: str,
        clientToken: str = ...,
        tags: Sequence[TagTypeDef] = ...,
        templateMajorVersion: str = ...,
        templateMinorVersion: str = ...,
    ) -> CreateServiceInstanceOutputTypeDef:
        """
        Create a service instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.create_service_instance)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#create_service_instance)
        """

    async def create_service_sync_config(
        self,
        *,
        branch: str,
        filePath: str,
        repositoryName: str,
        repositoryProvider: RepositoryProviderType,
        serviceName: str,
    ) -> CreateServiceSyncConfigOutputTypeDef:
        """
        Create the Proton Ops configuration file.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.create_service_sync_config)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#create_service_sync_config)
        """

    async def create_service_template(
        self,
        *,
        name: str,
        description: str = ...,
        displayName: str = ...,
        encryptionKey: str = ...,
        pipelineProvisioning: Literal["CUSTOMER_MANAGED"] = ...,
        tags: Sequence[TagTypeDef] = ...,
    ) -> CreateServiceTemplateOutputTypeDef:
        """
        Create a service template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.create_service_template)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#create_service_template)
        """

    async def create_service_template_version(
        self,
        *,
        compatibleEnvironmentTemplates: Sequence[CompatibleEnvironmentTemplateInputTypeDef],
        source: TemplateVersionSourceInputTypeDef,
        templateName: str,
        clientToken: str = ...,
        description: str = ...,
        majorVersion: str = ...,
        supportedComponentSources: Sequence[Literal["DIRECTLY_DEFINED"]] = ...,
        tags: Sequence[TagTypeDef] = ...,
    ) -> CreateServiceTemplateVersionOutputTypeDef:
        """
        Create a new major or minor version of a service template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.create_service_template_version)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#create_service_template_version)
        """

    async def create_template_sync_config(
        self,
        *,
        branch: str,
        repositoryName: str,
        repositoryProvider: RepositoryProviderType,
        templateName: str,
        templateType: TemplateTypeType,
        subdirectory: str = ...,
    ) -> CreateTemplateSyncConfigOutputTypeDef:
        """
        Set up a template to create new template versions automatically by tracking a
        linked
        repository.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.create_template_sync_config)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#create_template_sync_config)
        """

    async def delete_component(self, *, name: str) -> DeleteComponentOutputTypeDef:
        """
        Delete an Proton component resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.delete_component)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#delete_component)
        """

    async def delete_deployment(self, *, id: str) -> DeleteDeploymentOutputTypeDef:
        """
        Delete the deployment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.delete_deployment)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#delete_deployment)
        """

    async def delete_environment(self, *, name: str) -> DeleteEnvironmentOutputTypeDef:
        """
        Delete an environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.delete_environment)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#delete_environment)
        """

    async def delete_environment_account_connection(
        self, *, id: str
    ) -> DeleteEnvironmentAccountConnectionOutputTypeDef:
        """
        In an environment account, delete an environment account connection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.delete_environment_account_connection)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#delete_environment_account_connection)
        """

    async def delete_environment_template(
        self, *, name: str
    ) -> DeleteEnvironmentTemplateOutputTypeDef:
        """
        If no other major or minor versions of an environment template exist, delete
        the environment
        template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.delete_environment_template)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#delete_environment_template)
        """

    async def delete_environment_template_version(
        self, *, majorVersion: str, minorVersion: str, templateName: str
    ) -> DeleteEnvironmentTemplateVersionOutputTypeDef:
        """
        If no other minor versions of an environment template exist, delete a major
        version of the environment template if it's not the `Recommended`
        version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.delete_environment_template_version)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#delete_environment_template_version)
        """

    async def delete_repository(
        self, *, name: str, provider: RepositoryProviderType
    ) -> DeleteRepositoryOutputTypeDef:
        """
        De-register and unlink your repository.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.delete_repository)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#delete_repository)
        """

    async def delete_service(self, *, name: str) -> DeleteServiceOutputTypeDef:
        """
        Delete a service, with its instances and pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.delete_service)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#delete_service)
        """

    async def delete_service_sync_config(
        self, *, serviceName: str
    ) -> DeleteServiceSyncConfigOutputTypeDef:
        """
        Delete the Proton Ops file.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.delete_service_sync_config)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#delete_service_sync_config)
        """

    async def delete_service_template(self, *, name: str) -> DeleteServiceTemplateOutputTypeDef:
        """
        If no other major or minor versions of the service template exist, delete the
        service
        template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.delete_service_template)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#delete_service_template)
        """

    async def delete_service_template_version(
        self, *, majorVersion: str, minorVersion: str, templateName: str
    ) -> DeleteServiceTemplateVersionOutputTypeDef:
        """
        If no other minor versions of a service template exist, delete a major version
        of the service template if it's not the `Recommended`
        version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.delete_service_template_version)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#delete_service_template_version)
        """

    async def delete_template_sync_config(
        self, *, templateName: str, templateType: TemplateTypeType
    ) -> DeleteTemplateSyncConfigOutputTypeDef:
        """
        Delete a template sync configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.delete_template_sync_config)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#delete_template_sync_config)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.generate_presigned_url)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#generate_presigned_url)
        """

    async def get_account_settings(self) -> GetAccountSettingsOutputTypeDef:
        """
        Get detail data for Proton account-wide settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.get_account_settings)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#get_account_settings)
        """

    async def get_component(self, *, name: str) -> GetComponentOutputTypeDef:
        """
        Get detailed data for a component.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.get_component)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#get_component)
        """

    async def get_deployment(
        self,
        *,
        id: str,
        componentName: str = ...,
        environmentName: str = ...,
        serviceInstanceName: str = ...,
        serviceName: str = ...,
    ) -> GetDeploymentOutputTypeDef:
        """
        Get detailed data for a deployment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.get_deployment)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#get_deployment)
        """

    async def get_environment(self, *, name: str) -> GetEnvironmentOutputTypeDef:
        """
        Get detailed data for an environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.get_environment)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#get_environment)
        """

    async def get_environment_account_connection(
        self, *, id: str
    ) -> GetEnvironmentAccountConnectionOutputTypeDef:
        """
        In an environment account, get the detailed data for an environment account
        connection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.get_environment_account_connection)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#get_environment_account_connection)
        """

    async def get_environment_template(self, *, name: str) -> GetEnvironmentTemplateOutputTypeDef:
        """
        Get detailed data for an environment template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.get_environment_template)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#get_environment_template)
        """

    async def get_environment_template_version(
        self, *, majorVersion: str, minorVersion: str, templateName: str
    ) -> GetEnvironmentTemplateVersionOutputTypeDef:
        """
        Get detailed data for a major or minor version of an environment template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.get_environment_template_version)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#get_environment_template_version)
        """

    async def get_repository(
        self, *, name: str, provider: RepositoryProviderType
    ) -> GetRepositoryOutputTypeDef:
        """
        Get detail data for a linked repository.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.get_repository)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#get_repository)
        """

    async def get_repository_sync_status(
        self,
        *,
        branch: str,
        repositoryName: str,
        repositoryProvider: RepositoryProviderType,
        syncType: SyncTypeType,
    ) -> GetRepositorySyncStatusOutputTypeDef:
        """
        Get the sync status of a repository used for Proton template sync.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.get_repository_sync_status)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#get_repository_sync_status)
        """

    async def get_resources_summary(self) -> GetResourcesSummaryOutputTypeDef:
        """
        Get counts of Proton resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.get_resources_summary)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#get_resources_summary)
        """

    async def get_service(self, *, name: str) -> GetServiceOutputTypeDef:
        """
        Get detailed data for a service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.get_service)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#get_service)
        """

    async def get_service_instance(
        self, *, name: str, serviceName: str
    ) -> GetServiceInstanceOutputTypeDef:
        """
        Get detailed data for a service instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.get_service_instance)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#get_service_instance)
        """

    async def get_service_instance_sync_status(
        self, *, serviceInstanceName: str, serviceName: str
    ) -> GetServiceInstanceSyncStatusOutputTypeDef:
        """
        Get the status of the synced service instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.get_service_instance_sync_status)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#get_service_instance_sync_status)
        """

    async def get_service_sync_blocker_summary(
        self, *, serviceName: str, serviceInstanceName: str = ...
    ) -> GetServiceSyncBlockerSummaryOutputTypeDef:
        """
        Get detailed data for the service sync blocker summary.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.get_service_sync_blocker_summary)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#get_service_sync_blocker_summary)
        """

    async def get_service_sync_config(
        self, *, serviceName: str
    ) -> GetServiceSyncConfigOutputTypeDef:
        """
        Get detailed information for the service sync configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.get_service_sync_config)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#get_service_sync_config)
        """

    async def get_service_template(self, *, name: str) -> GetServiceTemplateOutputTypeDef:
        """
        Get detailed data for a service template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.get_service_template)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#get_service_template)
        """

    async def get_service_template_version(
        self, *, majorVersion: str, minorVersion: str, templateName: str
    ) -> GetServiceTemplateVersionOutputTypeDef:
        """
        Get detailed data for a major or minor version of a service template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.get_service_template_version)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#get_service_template_version)
        """

    async def get_template_sync_config(
        self, *, templateName: str, templateType: TemplateTypeType
    ) -> GetTemplateSyncConfigOutputTypeDef:
        """
        Get detail data for a template sync configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.get_template_sync_config)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#get_template_sync_config)
        """

    async def get_template_sync_status(
        self, *, templateName: str, templateType: TemplateTypeType, templateVersion: str
    ) -> GetTemplateSyncStatusOutputTypeDef:
        """
        Get the status of a template sync.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.get_template_sync_status)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#get_template_sync_status)
        """

    async def list_component_outputs(
        self, *, componentName: str, deploymentId: str = ..., nextToken: str = ...
    ) -> ListComponentOutputsOutputTypeDef:
        """
        Get a list of component Infrastructure as Code (IaC) outputs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.list_component_outputs)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#list_component_outputs)
        """

    async def list_component_provisioned_resources(
        self, *, componentName: str, nextToken: str = ...
    ) -> ListComponentProvisionedResourcesOutputTypeDef:
        """
        List provisioned resources for a component with details.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.list_component_provisioned_resources)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#list_component_provisioned_resources)
        """

    async def list_components(
        self,
        *,
        environmentName: str = ...,
        maxResults: int = ...,
        nextToken: str = ...,
        serviceInstanceName: str = ...,
        serviceName: str = ...,
    ) -> ListComponentsOutputTypeDef:
        """
        List components with summary data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.list_components)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#list_components)
        """

    async def list_deployments(
        self,
        *,
        componentName: str = ...,
        environmentName: str = ...,
        maxResults: int = ...,
        nextToken: str = ...,
        serviceInstanceName: str = ...,
        serviceName: str = ...,
    ) -> ListDeploymentsOutputTypeDef:
        """
        List deployments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.list_deployments)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#list_deployments)
        """

    async def list_environment_account_connections(
        self,
        *,
        requestedBy: EnvironmentAccountConnectionRequesterAccountTypeType,
        environmentName: str = ...,
        maxResults: int = ...,
        nextToken: str = ...,
        statuses: Sequence[EnvironmentAccountConnectionStatusType] = ...,
    ) -> ListEnvironmentAccountConnectionsOutputTypeDef:
        """
        View a list of environment account connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.list_environment_account_connections)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#list_environment_account_connections)
        """

    async def list_environment_outputs(
        self, *, environmentName: str, deploymentId: str = ..., nextToken: str = ...
    ) -> ListEnvironmentOutputsOutputTypeDef:
        """
        List the infrastructure as code outputs for your environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.list_environment_outputs)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#list_environment_outputs)
        """

    async def list_environment_provisioned_resources(
        self, *, environmentName: str, nextToken: str = ...
    ) -> ListEnvironmentProvisionedResourcesOutputTypeDef:
        """
        List the provisioned resources for your environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.list_environment_provisioned_resources)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#list_environment_provisioned_resources)
        """

    async def list_environment_template_versions(
        self,
        *,
        templateName: str,
        majorVersion: str = ...,
        maxResults: int = ...,
        nextToken: str = ...,
    ) -> ListEnvironmentTemplateVersionsOutputTypeDef:
        """
        List major or minor versions of an environment template with detail data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.list_environment_template_versions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#list_environment_template_versions)
        """

    async def list_environment_templates(
        self, *, maxResults: int = ..., nextToken: str = ...
    ) -> ListEnvironmentTemplatesOutputTypeDef:
        """
        List environment templates.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.list_environment_templates)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#list_environment_templates)
        """

    async def list_environments(
        self,
        *,
        environmentTemplates: Sequence[EnvironmentTemplateFilterTypeDef] = ...,
        maxResults: int = ...,
        nextToken: str = ...,
    ) -> ListEnvironmentsOutputTypeDef:
        """
        List environments with detail data summaries.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.list_environments)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#list_environments)
        """

    async def list_repositories(
        self, *, maxResults: int = ..., nextToken: str = ...
    ) -> ListRepositoriesOutputTypeDef:
        """
        List linked repositories with detail data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.list_repositories)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#list_repositories)
        """

    async def list_repository_sync_definitions(
        self,
        *,
        repositoryName: str,
        repositoryProvider: RepositoryProviderType,
        syncType: SyncTypeType,
        nextToken: str = ...,
    ) -> ListRepositorySyncDefinitionsOutputTypeDef:
        """
        List repository sync definitions with detail data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.list_repository_sync_definitions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#list_repository_sync_definitions)
        """

    async def list_service_instance_outputs(
        self,
        *,
        serviceInstanceName: str,
        serviceName: str,
        deploymentId: str = ...,
        nextToken: str = ...,
    ) -> ListServiceInstanceOutputsOutputTypeDef:
        """
        Get a list service of instance Infrastructure as Code (IaC) outputs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.list_service_instance_outputs)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#list_service_instance_outputs)
        """

    async def list_service_instance_provisioned_resources(
        self, *, serviceInstanceName: str, serviceName: str, nextToken: str = ...
    ) -> ListServiceInstanceProvisionedResourcesOutputTypeDef:
        """
        List provisioned resources for a service instance with details.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.list_service_instance_provisioned_resources)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#list_service_instance_provisioned_resources)
        """

    async def list_service_instances(
        self,
        *,
        filters: Sequence[ListServiceInstancesFilterTypeDef] = ...,
        maxResults: int = ...,
        nextToken: str = ...,
        serviceName: str = ...,
        sortBy: ListServiceInstancesSortByType = ...,
        sortOrder: SortOrderType = ...,
    ) -> ListServiceInstancesOutputTypeDef:
        """
        List service instances with summary data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.list_service_instances)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#list_service_instances)
        """

    async def list_service_pipeline_outputs(
        self, *, serviceName: str, deploymentId: str = ..., nextToken: str = ...
    ) -> ListServicePipelineOutputsOutputTypeDef:
        """
        Get a list of service pipeline Infrastructure as Code (IaC) outputs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.list_service_pipeline_outputs)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#list_service_pipeline_outputs)
        """

    async def list_service_pipeline_provisioned_resources(
        self, *, serviceName: str, nextToken: str = ...
    ) -> ListServicePipelineProvisionedResourcesOutputTypeDef:
        """
        List provisioned resources for a service and pipeline with details.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.list_service_pipeline_provisioned_resources)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#list_service_pipeline_provisioned_resources)
        """

    async def list_service_template_versions(
        self,
        *,
        templateName: str,
        majorVersion: str = ...,
        maxResults: int = ...,
        nextToken: str = ...,
    ) -> ListServiceTemplateVersionsOutputTypeDef:
        """
        List major or minor versions of a service template with detail data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.list_service_template_versions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#list_service_template_versions)
        """

    async def list_service_templates(
        self, *, maxResults: int = ..., nextToken: str = ...
    ) -> ListServiceTemplatesOutputTypeDef:
        """
        List service templates with detail data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.list_service_templates)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#list_service_templates)
        """

    async def list_services(
        self, *, maxResults: int = ..., nextToken: str = ...
    ) -> ListServicesOutputTypeDef:
        """
        List services with summaries of detail data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.list_services)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#list_services)
        """

    async def list_tags_for_resource(
        self, *, resourceArn: str, maxResults: int = ..., nextToken: str = ...
    ) -> ListTagsForResourceOutputTypeDef:
        """
        List tags for a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.list_tags_for_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#list_tags_for_resource)
        """

    async def notify_resource_deployment_status_change(
        self,
        *,
        resourceArn: str,
        deploymentId: str = ...,
        outputs: Sequence[OutputTypeDef] = ...,
        status: ResourceDeploymentStatusType = ...,
        statusMessage: str = ...,
    ) -> Dict[str, Any]:
        """
        Notify Proton of status changes to a provisioned resource when you use
        self-managed
        provisioning.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.notify_resource_deployment_status_change)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#notify_resource_deployment_status_change)
        """

    async def reject_environment_account_connection(
        self, *, id: str
    ) -> RejectEnvironmentAccountConnectionOutputTypeDef:
        """
        In a management account, reject an environment account connection from another
        environment
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.reject_environment_account_connection)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#reject_environment_account_connection)
        """

    async def tag_resource(self, *, resourceArn: str, tags: Sequence[TagTypeDef]) -> Dict[str, Any]:
        """
        Tag a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.tag_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#tag_resource)
        """

    async def untag_resource(self, *, resourceArn: str, tagKeys: Sequence[str]) -> Dict[str, Any]:
        """
        Remove a customer tag from a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.untag_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#untag_resource)
        """

    async def update_account_settings(
        self,
        *,
        deletePipelineProvisioningRepository: bool = ...,
        pipelineCodebuildRoleArn: str = ...,
        pipelineProvisioningRepository: RepositoryBranchInputTypeDef = ...,
        pipelineServiceRoleArn: str = ...,
    ) -> UpdateAccountSettingsOutputTypeDef:
        """
        Update Proton settings that are used for multiple services in the Amazon Web
        Services
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.update_account_settings)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#update_account_settings)
        """

    async def update_component(
        self,
        *,
        deploymentType: ComponentDeploymentUpdateTypeType,
        name: str,
        clientToken: str = ...,
        description: str = ...,
        serviceInstanceName: str = ...,
        serviceName: str = ...,
        serviceSpec: str = ...,
        templateFile: str = ...,
    ) -> UpdateComponentOutputTypeDef:
        """
        Update a component.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.update_component)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#update_component)
        """

    async def update_environment(
        self,
        *,
        deploymentType: DeploymentUpdateTypeType,
        name: str,
        codebuildRoleArn: str = ...,
        componentRoleArn: str = ...,
        description: str = ...,
        environmentAccountConnectionId: str = ...,
        protonServiceRoleArn: str = ...,
        provisioningRepository: RepositoryBranchInputTypeDef = ...,
        spec: str = ...,
        templateMajorVersion: str = ...,
        templateMinorVersion: str = ...,
    ) -> UpdateEnvironmentOutputTypeDef:
        """
        Update an environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.update_environment)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#update_environment)
        """

    async def update_environment_account_connection(
        self,
        *,
        id: str,
        codebuildRoleArn: str = ...,
        componentRoleArn: str = ...,
        roleArn: str = ...,
    ) -> UpdateEnvironmentAccountConnectionOutputTypeDef:
        """
        In an environment account, update an environment account connection to use a
        new IAM
        role.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.update_environment_account_connection)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#update_environment_account_connection)
        """

    async def update_environment_template(
        self, *, name: str, description: str = ..., displayName: str = ...
    ) -> UpdateEnvironmentTemplateOutputTypeDef:
        """
        Update an environment template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.update_environment_template)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#update_environment_template)
        """

    async def update_environment_template_version(
        self,
        *,
        majorVersion: str,
        minorVersion: str,
        templateName: str,
        description: str = ...,
        status: TemplateVersionStatusType = ...,
    ) -> UpdateEnvironmentTemplateVersionOutputTypeDef:
        """
        Update a major or minor version of an environment template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.update_environment_template_version)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#update_environment_template_version)
        """

    async def update_service(
        self, *, name: str, description: str = ..., spec: str = ...
    ) -> UpdateServiceOutputTypeDef:
        """
        Edit a service description or use a spec to add and delete service instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.update_service)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#update_service)
        """

    async def update_service_instance(
        self,
        *,
        deploymentType: DeploymentUpdateTypeType,
        name: str,
        serviceName: str,
        clientToken: str = ...,
        spec: str = ...,
        templateMajorVersion: str = ...,
        templateMinorVersion: str = ...,
    ) -> UpdateServiceInstanceOutputTypeDef:
        """
        Update a service instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.update_service_instance)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#update_service_instance)
        """

    async def update_service_pipeline(
        self,
        *,
        deploymentType: DeploymentUpdateTypeType,
        serviceName: str,
        spec: str,
        templateMajorVersion: str = ...,
        templateMinorVersion: str = ...,
    ) -> UpdateServicePipelineOutputTypeDef:
        """
        Update the service pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.update_service_pipeline)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#update_service_pipeline)
        """

    async def update_service_sync_blocker(
        self, *, id: str, resolvedReason: str
    ) -> UpdateServiceSyncBlockerOutputTypeDef:
        """
        Update the service sync blocker by resolving it.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.update_service_sync_blocker)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#update_service_sync_blocker)
        """

    async def update_service_sync_config(
        self,
        *,
        branch: str,
        filePath: str,
        repositoryName: str,
        repositoryProvider: RepositoryProviderType,
        serviceName: str,
    ) -> UpdateServiceSyncConfigOutputTypeDef:
        """
        Update the Proton Ops config file.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.update_service_sync_config)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#update_service_sync_config)
        """

    async def update_service_template(
        self, *, name: str, description: str = ..., displayName: str = ...
    ) -> UpdateServiceTemplateOutputTypeDef:
        """
        Update a service template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.update_service_template)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#update_service_template)
        """

    async def update_service_template_version(
        self,
        *,
        majorVersion: str,
        minorVersion: str,
        templateName: str,
        compatibleEnvironmentTemplates: Sequence[CompatibleEnvironmentTemplateInputTypeDef] = ...,
        description: str = ...,
        status: TemplateVersionStatusType = ...,
        supportedComponentSources: Sequence[Literal["DIRECTLY_DEFINED"]] = ...,
    ) -> UpdateServiceTemplateVersionOutputTypeDef:
        """
        Update a major or minor version of a service template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.update_service_template_version)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#update_service_template_version)
        """

    async def update_template_sync_config(
        self,
        *,
        branch: str,
        repositoryName: str,
        repositoryProvider: RepositoryProviderType,
        templateName: str,
        templateType: TemplateTypeType,
        subdirectory: str = ...,
    ) -> UpdateTemplateSyncConfigOutputTypeDef:
        """
        Update template sync configuration parameters, except for the `templateName`
        and
        `templateType`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.update_template_sync_config)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#update_template_sync_config)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_component_outputs"]
    ) -> ListComponentOutputsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_component_provisioned_resources"]
    ) -> ListComponentProvisionedResourcesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_components"]) -> ListComponentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_deployments"]
    ) -> ListDeploymentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_environment_account_connections"]
    ) -> ListEnvironmentAccountConnectionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_environment_outputs"]
    ) -> ListEnvironmentOutputsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_environment_provisioned_resources"]
    ) -> ListEnvironmentProvisionedResourcesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_environment_template_versions"]
    ) -> ListEnvironmentTemplateVersionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_environment_templates"]
    ) -> ListEnvironmentTemplatesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_environments"]
    ) -> ListEnvironmentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_repositories"]
    ) -> ListRepositoriesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_repository_sync_definitions"]
    ) -> ListRepositorySyncDefinitionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_service_instance_outputs"]
    ) -> ListServiceInstanceOutputsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_service_instance_provisioned_resources"]
    ) -> ListServiceInstanceProvisionedResourcesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_service_instances"]
    ) -> ListServiceInstancesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_service_pipeline_outputs"]
    ) -> ListServicePipelineOutputsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_service_pipeline_provisioned_resources"]
    ) -> ListServicePipelineProvisionedResourcesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_service_template_versions"]
    ) -> ListServiceTemplateVersionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_service_templates"]
    ) -> ListServiceTemplatesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_services"]) -> ListServicesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_tags_for_resource"]
    ) -> ListTagsForResourcePaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#get_paginator)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["component_deleted"]) -> ComponentDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.get_waiter)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#get_waiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["component_deployed"]) -> ComponentDeployedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.get_waiter)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#get_waiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["environment_deployed"]) -> EnvironmentDeployedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.get_waiter)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#get_waiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["environment_template_version_registered"]
    ) -> EnvironmentTemplateVersionRegisteredWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.get_waiter)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#get_waiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["service_created"]) -> ServiceCreatedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.get_waiter)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#get_waiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["service_deleted"]) -> ServiceDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.get_waiter)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#get_waiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["service_instance_deployed"]
    ) -> ServiceInstanceDeployedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.get_waiter)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#get_waiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["service_pipeline_deployed"]
    ) -> ServicePipelineDeployedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.get_waiter)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#get_waiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["service_template_version_registered"]
    ) -> ServiceTemplateVersionRegisteredWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.get_waiter)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#get_waiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["service_updated"]) -> ServiceUpdatedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client.get_waiter)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/#get_waiter)
        """

    async def __aenter__(self) -> "ProtonClient":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/)
        """

    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> Any:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html#Proton.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/client/)
        """
