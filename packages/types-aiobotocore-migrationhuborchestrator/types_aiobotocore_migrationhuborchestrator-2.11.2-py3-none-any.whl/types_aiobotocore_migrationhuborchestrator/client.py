"""
Type annotations for migrationhuborchestrator service client.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_migrationhuborchestrator/client/)

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_migrationhuborchestrator.client import MigrationHubOrchestratorClient

    session = get_session()
    async with session.create_client("migrationhuborchestrator") as client:
        client: MigrationHubOrchestratorClient
    ```
"""

import sys
from typing import Any, Dict, Mapping, Sequence, Type, overload

from aiobotocore.client import AioBaseClient
from botocore.client import ClientMeta

from .literals import MigrationWorkflowStatusEnumType, StepActionTypeType, StepStatusType
from .paginator import (
    ListPluginsPaginator,
    ListTemplatesPaginator,
    ListTemplateStepGroupsPaginator,
    ListTemplateStepsPaginator,
    ListWorkflowsPaginator,
    ListWorkflowStepGroupsPaginator,
    ListWorkflowStepsPaginator,
)
from .type_defs import (
    CreateMigrationWorkflowResponseTypeDef,
    CreateWorkflowStepGroupResponseTypeDef,
    CreateWorkflowStepResponseTypeDef,
    DeleteMigrationWorkflowResponseTypeDef,
    GetMigrationWorkflowResponseTypeDef,
    GetMigrationWorkflowTemplateResponseTypeDef,
    GetTemplateStepGroupResponseTypeDef,
    GetTemplateStepResponseTypeDef,
    GetWorkflowStepGroupResponseTypeDef,
    GetWorkflowStepResponseTypeDef,
    ListMigrationWorkflowsResponseTypeDef,
    ListMigrationWorkflowTemplatesResponseTypeDef,
    ListPluginsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTemplateStepGroupsResponseTypeDef,
    ListTemplateStepsResponseTypeDef,
    ListWorkflowStepGroupsResponseTypeDef,
    ListWorkflowStepsResponseTypeDef,
    RetryWorkflowStepResponseTypeDef,
    StartMigrationWorkflowResponseTypeDef,
    StepInputTypeDef,
    StopMigrationWorkflowResponseTypeDef,
    UpdateMigrationWorkflowResponseTypeDef,
    UpdateWorkflowStepGroupResponseTypeDef,
    UpdateWorkflowStepResponseTypeDef,
    WorkflowStepAutomationConfigurationTypeDef,
    WorkflowStepOutputTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("MigrationHubOrchestratorClient",)


class BotocoreClientError(Exception):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class MigrationHubOrchestratorClient(AioBaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_migrationhuborchestrator/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        MigrationHubOrchestratorClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.exceptions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_migrationhuborchestrator/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.can_paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_migrationhuborchestrator/client/#can_paginate)
        """

    async def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.close)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_migrationhuborchestrator/client/#close)
        """

    async def create_workflow(
        self,
        *,
        name: str,
        templateId: str,
        applicationConfigurationId: str,
        inputParameters: Mapping[str, StepInputTypeDef],
        description: str = ...,
        stepTargets: Sequence[str] = ...,
        tags: Mapping[str, str] = ...,
    ) -> CreateMigrationWorkflowResponseTypeDef:
        """
        Create a workflow to orchestrate your migrations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.create_workflow)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_migrationhuborchestrator/client/#create_workflow)
        """

    async def create_workflow_step(
        self,
        *,
        name: str,
        stepGroupId: str,
        workflowId: str,
        stepActionType: StepActionTypeType,
        description: str = ...,
        workflowStepAutomationConfiguration: WorkflowStepAutomationConfigurationTypeDef = ...,
        stepTarget: Sequence[str] = ...,
        outputs: Sequence[WorkflowStepOutputTypeDef] = ...,
        previous: Sequence[str] = ...,
        next: Sequence[str] = ...,
    ) -> CreateWorkflowStepResponseTypeDef:
        """
        Create a step in the migration workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.create_workflow_step)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_migrationhuborchestrator/client/#create_workflow_step)
        """

    async def create_workflow_step_group(
        self,
        *,
        workflowId: str,
        name: str,
        description: str = ...,
        next: Sequence[str] = ...,
        previous: Sequence[str] = ...,
    ) -> CreateWorkflowStepGroupResponseTypeDef:
        """
        Create a step group in a migration workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.create_workflow_step_group)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_migrationhuborchestrator/client/#create_workflow_step_group)
        """

    async def delete_workflow(self, *, id: str) -> DeleteMigrationWorkflowResponseTypeDef:
        """
        Delete a migration workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.delete_workflow)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_migrationhuborchestrator/client/#delete_workflow)
        """

    async def delete_workflow_step(
        self, *, id: str, stepGroupId: str, workflowId: str
    ) -> Dict[str, Any]:
        """
        Delete a step in a migration workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.delete_workflow_step)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_migrationhuborchestrator/client/#delete_workflow_step)
        """

    async def delete_workflow_step_group(self, *, workflowId: str, id: str) -> Dict[str, Any]:
        """
        Delete a step group in a migration workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.delete_workflow_step_group)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_migrationhuborchestrator/client/#delete_workflow_step_group)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.generate_presigned_url)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_migrationhuborchestrator/client/#generate_presigned_url)
        """

    async def get_template(self, *, id: str) -> GetMigrationWorkflowTemplateResponseTypeDef:
        """
        Get the template you want to use for creating a migration workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.get_template)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_migrationhuborchestrator/client/#get_template)
        """

    async def get_template_step(
        self, *, id: str, templateId: str, stepGroupId: str
    ) -> GetTemplateStepResponseTypeDef:
        """
        Get a specific step in a template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.get_template_step)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_migrationhuborchestrator/client/#get_template_step)
        """

    async def get_template_step_group(
        self, *, templateId: str, id: str
    ) -> GetTemplateStepGroupResponseTypeDef:
        """
        Get a step group in a template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.get_template_step_group)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_migrationhuborchestrator/client/#get_template_step_group)
        """

    async def get_workflow(self, *, id: str) -> GetMigrationWorkflowResponseTypeDef:
        """
        Get migration workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.get_workflow)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_migrationhuborchestrator/client/#get_workflow)
        """

    async def get_workflow_step(
        self, *, workflowId: str, stepGroupId: str, id: str
    ) -> GetWorkflowStepResponseTypeDef:
        """
        Get a step in the migration workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.get_workflow_step)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_migrationhuborchestrator/client/#get_workflow_step)
        """

    async def get_workflow_step_group(
        self, *, id: str, workflowId: str
    ) -> GetWorkflowStepGroupResponseTypeDef:
        """
        Get the step group of a migration workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.get_workflow_step_group)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_migrationhuborchestrator/client/#get_workflow_step_group)
        """

    async def list_plugins(
        self, *, maxResults: int = ..., nextToken: str = ...
    ) -> ListPluginsResponseTypeDef:
        """
        List AWS Migration Hub Orchestrator plugins.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.list_plugins)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_migrationhuborchestrator/client/#list_plugins)
        """

    async def list_tags_for_resource(
        self, *, resourceArn: str
    ) -> ListTagsForResourceResponseTypeDef:
        """
        List the tags added to a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.list_tags_for_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_migrationhuborchestrator/client/#list_tags_for_resource)
        """

    async def list_template_step_groups(
        self, *, templateId: str, maxResults: int = ..., nextToken: str = ...
    ) -> ListTemplateStepGroupsResponseTypeDef:
        """
        List the step groups in a template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.list_template_step_groups)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_migrationhuborchestrator/client/#list_template_step_groups)
        """

    async def list_template_steps(
        self, *, templateId: str, stepGroupId: str, maxResults: int = ..., nextToken: str = ...
    ) -> ListTemplateStepsResponseTypeDef:
        """
        List the steps in a template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.list_template_steps)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_migrationhuborchestrator/client/#list_template_steps)
        """

    async def list_templates(
        self, *, maxResults: int = ..., nextToken: str = ..., name: str = ...
    ) -> ListMigrationWorkflowTemplatesResponseTypeDef:
        """
        List the templates available in Migration Hub Orchestrator to create a
        migration
        workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.list_templates)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_migrationhuborchestrator/client/#list_templates)
        """

    async def list_workflow_step_groups(
        self, *, workflowId: str, nextToken: str = ..., maxResults: int = ...
    ) -> ListWorkflowStepGroupsResponseTypeDef:
        """
        List the step groups in a migration workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.list_workflow_step_groups)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_migrationhuborchestrator/client/#list_workflow_step_groups)
        """

    async def list_workflow_steps(
        self, *, workflowId: str, stepGroupId: str, nextToken: str = ..., maxResults: int = ...
    ) -> ListWorkflowStepsResponseTypeDef:
        """
        List the steps in a workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.list_workflow_steps)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_migrationhuborchestrator/client/#list_workflow_steps)
        """

    async def list_workflows(
        self,
        *,
        maxResults: int = ...,
        nextToken: str = ...,
        templateId: str = ...,
        adsApplicationConfigurationName: str = ...,
        status: MigrationWorkflowStatusEnumType = ...,
        name: str = ...,
    ) -> ListMigrationWorkflowsResponseTypeDef:
        """
        List the migration workflows.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.list_workflows)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_migrationhuborchestrator/client/#list_workflows)
        """

    async def retry_workflow_step(
        self, *, workflowId: str, stepGroupId: str, id: str
    ) -> RetryWorkflowStepResponseTypeDef:
        """
        Retry a failed step in a migration workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.retry_workflow_step)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_migrationhuborchestrator/client/#retry_workflow_step)
        """

    async def start_workflow(self, *, id: str) -> StartMigrationWorkflowResponseTypeDef:
        """
        Start a migration workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.start_workflow)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_migrationhuborchestrator/client/#start_workflow)
        """

    async def stop_workflow(self, *, id: str) -> StopMigrationWorkflowResponseTypeDef:
        """
        Stop an ongoing migration workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.stop_workflow)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_migrationhuborchestrator/client/#stop_workflow)
        """

    async def tag_resource(self, *, resourceArn: str, tags: Mapping[str, str]) -> Dict[str, Any]:
        """
        Tag a resource by specifying its Amazon Resource Name (ARN).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.tag_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_migrationhuborchestrator/client/#tag_resource)
        """

    async def untag_resource(self, *, resourceArn: str, tagKeys: Sequence[str]) -> Dict[str, Any]:
        """
        Deletes the tags for a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.untag_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_migrationhuborchestrator/client/#untag_resource)
        """

    async def update_workflow(
        self,
        *,
        id: str,
        name: str = ...,
        description: str = ...,
        inputParameters: Mapping[str, StepInputTypeDef] = ...,
        stepTargets: Sequence[str] = ...,
    ) -> UpdateMigrationWorkflowResponseTypeDef:
        """
        Update a migration workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.update_workflow)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_migrationhuborchestrator/client/#update_workflow)
        """

    async def update_workflow_step(
        self,
        *,
        id: str,
        stepGroupId: str,
        workflowId: str,
        name: str = ...,
        description: str = ...,
        stepActionType: StepActionTypeType = ...,
        workflowStepAutomationConfiguration: WorkflowStepAutomationConfigurationTypeDef = ...,
        stepTarget: Sequence[str] = ...,
        outputs: Sequence[WorkflowStepOutputTypeDef] = ...,
        previous: Sequence[str] = ...,
        next: Sequence[str] = ...,
        status: StepStatusType = ...,
    ) -> UpdateWorkflowStepResponseTypeDef:
        """
        Update a step in a migration workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.update_workflow_step)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_migrationhuborchestrator/client/#update_workflow_step)
        """

    async def update_workflow_step_group(
        self,
        *,
        workflowId: str,
        id: str,
        name: str = ...,
        description: str = ...,
        next: Sequence[str] = ...,
        previous: Sequence[str] = ...,
    ) -> UpdateWorkflowStepGroupResponseTypeDef:
        """
        Update the step group in a migration workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.update_workflow_step_group)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_migrationhuborchestrator/client/#update_workflow_step_group)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_plugins"]) -> ListPluginsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_migrationhuborchestrator/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_template_step_groups"]
    ) -> ListTemplateStepGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_migrationhuborchestrator/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_template_steps"]
    ) -> ListTemplateStepsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_migrationhuborchestrator/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_templates"]) -> ListTemplatesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_migrationhuborchestrator/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_workflow_step_groups"]
    ) -> ListWorkflowStepGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_migrationhuborchestrator/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_workflow_steps"]
    ) -> ListWorkflowStepsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_migrationhuborchestrator/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_workflows"]) -> ListWorkflowsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_migrationhuborchestrator/client/#get_paginator)
        """

    async def __aenter__(self) -> "MigrationHubOrchestratorClient":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_migrationhuborchestrator/client/)
        """

    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> Any:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_migrationhuborchestrator/client/)
        """
