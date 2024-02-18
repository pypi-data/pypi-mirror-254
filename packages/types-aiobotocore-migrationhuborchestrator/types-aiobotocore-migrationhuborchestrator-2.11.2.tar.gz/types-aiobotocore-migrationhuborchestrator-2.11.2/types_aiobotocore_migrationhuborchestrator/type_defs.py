"""
Type annotations for migrationhuborchestrator service type definitions.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_migrationhuborchestrator/type_defs/)

Usage::

    ```python
    from types_aiobotocore_migrationhuborchestrator.type_defs import StepInputTypeDef

    data: StepInputTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from .literals import (
    DataTypeType,
    MigrationWorkflowStatusEnumType,
    OwnerType,
    PluginHealthType,
    RunEnvironmentType,
    StepActionTypeType,
    StepGroupStatusType,
    StepStatusType,
    TargetTypeType,
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
    "StepInputTypeDef",
    "ResponseMetadataTypeDef",
    "CreateWorkflowStepGroupRequestRequestTypeDef",
    "ToolTypeDef",
    "DeleteMigrationWorkflowRequestRequestTypeDef",
    "DeleteWorkflowStepGroupRequestRequestTypeDef",
    "DeleteWorkflowStepRequestRequestTypeDef",
    "GetMigrationWorkflowRequestRequestTypeDef",
    "GetMigrationWorkflowTemplateRequestRequestTypeDef",
    "TemplateInputTypeDef",
    "GetTemplateStepGroupRequestRequestTypeDef",
    "GetTemplateStepRequestRequestTypeDef",
    "StepOutputTypeDef",
    "GetWorkflowStepGroupRequestRequestTypeDef",
    "GetWorkflowStepRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "ListMigrationWorkflowTemplatesRequestRequestTypeDef",
    "TemplateSummaryTypeDef",
    "ListMigrationWorkflowsRequestRequestTypeDef",
    "MigrationWorkflowSummaryTypeDef",
    "ListPluginsRequestRequestTypeDef",
    "PluginSummaryTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTemplateStepGroupsRequestRequestTypeDef",
    "TemplateStepGroupSummaryTypeDef",
    "ListTemplateStepsRequestRequestTypeDef",
    "TemplateStepSummaryTypeDef",
    "ListWorkflowStepGroupsRequestRequestTypeDef",
    "WorkflowStepGroupSummaryTypeDef",
    "ListWorkflowStepsRequestRequestTypeDef",
    "WorkflowStepSummaryTypeDef",
    "PlatformCommandTypeDef",
    "PlatformScriptKeyTypeDef",
    "RetryWorkflowStepRequestRequestTypeDef",
    "StartMigrationWorkflowRequestRequestTypeDef",
    "StopMigrationWorkflowRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateWorkflowStepGroupRequestRequestTypeDef",
    "WorkflowStepOutputUnionTypeDef",
    "CreateMigrationWorkflowRequestRequestTypeDef",
    "UpdateMigrationWorkflowRequestRequestTypeDef",
    "CreateMigrationWorkflowResponseTypeDef",
    "CreateWorkflowStepResponseTypeDef",
    "DeleteMigrationWorkflowResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "RetryWorkflowStepResponseTypeDef",
    "StartMigrationWorkflowResponseTypeDef",
    "StopMigrationWorkflowResponseTypeDef",
    "UpdateMigrationWorkflowResponseTypeDef",
    "UpdateWorkflowStepResponseTypeDef",
    "CreateWorkflowStepGroupResponseTypeDef",
    "GetMigrationWorkflowResponseTypeDef",
    "GetTemplateStepGroupResponseTypeDef",
    "GetWorkflowStepGroupResponseTypeDef",
    "UpdateWorkflowStepGroupResponseTypeDef",
    "GetMigrationWorkflowTemplateResponseTypeDef",
    "ListMigrationWorkflowTemplatesRequestListTemplatesPaginateTypeDef",
    "ListMigrationWorkflowsRequestListWorkflowsPaginateTypeDef",
    "ListPluginsRequestListPluginsPaginateTypeDef",
    "ListTemplateStepGroupsRequestListTemplateStepGroupsPaginateTypeDef",
    "ListTemplateStepsRequestListTemplateStepsPaginateTypeDef",
    "ListWorkflowStepGroupsRequestListWorkflowStepGroupsPaginateTypeDef",
    "ListWorkflowStepsRequestListWorkflowStepsPaginateTypeDef",
    "ListMigrationWorkflowTemplatesResponseTypeDef",
    "ListMigrationWorkflowsResponseTypeDef",
    "ListPluginsResponseTypeDef",
    "ListTemplateStepGroupsResponseTypeDef",
    "ListTemplateStepsResponseTypeDef",
    "ListWorkflowStepGroupsResponseTypeDef",
    "ListWorkflowStepsResponseTypeDef",
    "StepAutomationConfigurationTypeDef",
    "WorkflowStepAutomationConfigurationTypeDef",
    "WorkflowStepOutputTypeDef",
    "GetTemplateStepResponseTypeDef",
    "CreateWorkflowStepRequestRequestTypeDef",
    "GetWorkflowStepResponseTypeDef",
    "UpdateWorkflowStepRequestRequestTypeDef",
)

StepInputTypeDef = TypedDict(
    "StepInputTypeDef",
    {
        "integerValue": NotRequired[int],
        "stringValue": NotRequired[str],
        "listOfStringsValue": NotRequired[Sequence[str]],
        "mapOfStringValue": NotRequired[Mapping[str, str]],
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
CreateWorkflowStepGroupRequestRequestTypeDef = TypedDict(
    "CreateWorkflowStepGroupRequestRequestTypeDef",
    {
        "workflowId": str,
        "name": str,
        "description": NotRequired[str],
        "next": NotRequired[Sequence[str]],
        "previous": NotRequired[Sequence[str]],
    },
)
ToolTypeDef = TypedDict(
    "ToolTypeDef",
    {
        "name": NotRequired[str],
        "url": NotRequired[str],
    },
)
DeleteMigrationWorkflowRequestRequestTypeDef = TypedDict(
    "DeleteMigrationWorkflowRequestRequestTypeDef",
    {
        "id": str,
    },
)
DeleteWorkflowStepGroupRequestRequestTypeDef = TypedDict(
    "DeleteWorkflowStepGroupRequestRequestTypeDef",
    {
        "workflowId": str,
        "id": str,
    },
)
DeleteWorkflowStepRequestRequestTypeDef = TypedDict(
    "DeleteWorkflowStepRequestRequestTypeDef",
    {
        "id": str,
        "stepGroupId": str,
        "workflowId": str,
    },
)
GetMigrationWorkflowRequestRequestTypeDef = TypedDict(
    "GetMigrationWorkflowRequestRequestTypeDef",
    {
        "id": str,
    },
)
GetMigrationWorkflowTemplateRequestRequestTypeDef = TypedDict(
    "GetMigrationWorkflowTemplateRequestRequestTypeDef",
    {
        "id": str,
    },
)
TemplateInputTypeDef = TypedDict(
    "TemplateInputTypeDef",
    {
        "inputName": NotRequired[str],
        "dataType": NotRequired[DataTypeType],
        "required": NotRequired[bool],
    },
)
GetTemplateStepGroupRequestRequestTypeDef = TypedDict(
    "GetTemplateStepGroupRequestRequestTypeDef",
    {
        "templateId": str,
        "id": str,
    },
)
GetTemplateStepRequestRequestTypeDef = TypedDict(
    "GetTemplateStepRequestRequestTypeDef",
    {
        "id": str,
        "templateId": str,
        "stepGroupId": str,
    },
)
StepOutputTypeDef = TypedDict(
    "StepOutputTypeDef",
    {
        "name": NotRequired[str],
        "dataType": NotRequired[DataTypeType],
        "required": NotRequired[bool],
    },
)
GetWorkflowStepGroupRequestRequestTypeDef = TypedDict(
    "GetWorkflowStepGroupRequestRequestTypeDef",
    {
        "id": str,
        "workflowId": str,
    },
)
GetWorkflowStepRequestRequestTypeDef = TypedDict(
    "GetWorkflowStepRequestRequestTypeDef",
    {
        "workflowId": str,
        "stepGroupId": str,
        "id": str,
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
ListMigrationWorkflowTemplatesRequestRequestTypeDef = TypedDict(
    "ListMigrationWorkflowTemplatesRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "name": NotRequired[str],
    },
)
TemplateSummaryTypeDef = TypedDict(
    "TemplateSummaryTypeDef",
    {
        "id": NotRequired[str],
        "name": NotRequired[str],
        "arn": NotRequired[str],
        "description": NotRequired[str],
    },
)
ListMigrationWorkflowsRequestRequestTypeDef = TypedDict(
    "ListMigrationWorkflowsRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "templateId": NotRequired[str],
        "adsApplicationConfigurationName": NotRequired[str],
        "status": NotRequired[MigrationWorkflowStatusEnumType],
        "name": NotRequired[str],
    },
)
MigrationWorkflowSummaryTypeDef = TypedDict(
    "MigrationWorkflowSummaryTypeDef",
    {
        "id": NotRequired[str],
        "name": NotRequired[str],
        "templateId": NotRequired[str],
        "adsApplicationConfigurationName": NotRequired[str],
        "status": NotRequired[MigrationWorkflowStatusEnumType],
        "creationTime": NotRequired[datetime],
        "endTime": NotRequired[datetime],
        "statusMessage": NotRequired[str],
        "completedSteps": NotRequired[int],
        "totalSteps": NotRequired[int],
    },
)
ListPluginsRequestRequestTypeDef = TypedDict(
    "ListPluginsRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
PluginSummaryTypeDef = TypedDict(
    "PluginSummaryTypeDef",
    {
        "pluginId": NotRequired[str],
        "hostname": NotRequired[str],
        "status": NotRequired[PluginHealthType],
        "ipAddress": NotRequired[str],
        "version": NotRequired[str],
        "registeredTime": NotRequired[str],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)
ListTemplateStepGroupsRequestRequestTypeDef = TypedDict(
    "ListTemplateStepGroupsRequestRequestTypeDef",
    {
        "templateId": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
TemplateStepGroupSummaryTypeDef = TypedDict(
    "TemplateStepGroupSummaryTypeDef",
    {
        "id": NotRequired[str],
        "name": NotRequired[str],
        "previous": NotRequired[List[str]],
        "next": NotRequired[List[str]],
    },
)
ListTemplateStepsRequestRequestTypeDef = TypedDict(
    "ListTemplateStepsRequestRequestTypeDef",
    {
        "templateId": str,
        "stepGroupId": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
TemplateStepSummaryTypeDef = TypedDict(
    "TemplateStepSummaryTypeDef",
    {
        "id": NotRequired[str],
        "stepGroupId": NotRequired[str],
        "templateId": NotRequired[str],
        "name": NotRequired[str],
        "stepActionType": NotRequired[StepActionTypeType],
        "targetType": NotRequired[TargetTypeType],
        "owner": NotRequired[OwnerType],
        "previous": NotRequired[List[str]],
        "next": NotRequired[List[str]],
    },
)
ListWorkflowStepGroupsRequestRequestTypeDef = TypedDict(
    "ListWorkflowStepGroupsRequestRequestTypeDef",
    {
        "workflowId": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
WorkflowStepGroupSummaryTypeDef = TypedDict(
    "WorkflowStepGroupSummaryTypeDef",
    {
        "id": NotRequired[str],
        "name": NotRequired[str],
        "owner": NotRequired[OwnerType],
        "status": NotRequired[StepGroupStatusType],
        "previous": NotRequired[List[str]],
        "next": NotRequired[List[str]],
    },
)
ListWorkflowStepsRequestRequestTypeDef = TypedDict(
    "ListWorkflowStepsRequestRequestTypeDef",
    {
        "workflowId": str,
        "stepGroupId": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
WorkflowStepSummaryTypeDef = TypedDict(
    "WorkflowStepSummaryTypeDef",
    {
        "stepId": NotRequired[str],
        "name": NotRequired[str],
        "stepActionType": NotRequired[StepActionTypeType],
        "owner": NotRequired[OwnerType],
        "previous": NotRequired[List[str]],
        "next": NotRequired[List[str]],
        "status": NotRequired[StepStatusType],
        "statusMessage": NotRequired[str],
        "noOfSrvCompleted": NotRequired[int],
        "noOfSrvFailed": NotRequired[int],
        "totalNoOfSrv": NotRequired[int],
        "description": NotRequired[str],
        "scriptLocation": NotRequired[str],
    },
)
PlatformCommandTypeDef = TypedDict(
    "PlatformCommandTypeDef",
    {
        "linux": NotRequired[str],
        "windows": NotRequired[str],
    },
)
PlatformScriptKeyTypeDef = TypedDict(
    "PlatformScriptKeyTypeDef",
    {
        "linux": NotRequired[str],
        "windows": NotRequired[str],
    },
)
RetryWorkflowStepRequestRequestTypeDef = TypedDict(
    "RetryWorkflowStepRequestRequestTypeDef",
    {
        "workflowId": str,
        "stepGroupId": str,
        "id": str,
    },
)
StartMigrationWorkflowRequestRequestTypeDef = TypedDict(
    "StartMigrationWorkflowRequestRequestTypeDef",
    {
        "id": str,
    },
)
StopMigrationWorkflowRequestRequestTypeDef = TypedDict(
    "StopMigrationWorkflowRequestRequestTypeDef",
    {
        "id": str,
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
UpdateWorkflowStepGroupRequestRequestTypeDef = TypedDict(
    "UpdateWorkflowStepGroupRequestRequestTypeDef",
    {
        "workflowId": str,
        "id": str,
        "name": NotRequired[str],
        "description": NotRequired[str],
        "next": NotRequired[Sequence[str]],
        "previous": NotRequired[Sequence[str]],
    },
)
WorkflowStepOutputUnionTypeDef = TypedDict(
    "WorkflowStepOutputUnionTypeDef",
    {
        "integerValue": NotRequired[int],
        "stringValue": NotRequired[str],
        "listOfStringValue": NotRequired[Sequence[str]],
    },
)
CreateMigrationWorkflowRequestRequestTypeDef = TypedDict(
    "CreateMigrationWorkflowRequestRequestTypeDef",
    {
        "name": str,
        "templateId": str,
        "applicationConfigurationId": str,
        "inputParameters": Mapping[str, StepInputTypeDef],
        "description": NotRequired[str],
        "stepTargets": NotRequired[Sequence[str]],
        "tags": NotRequired[Mapping[str, str]],
    },
)
UpdateMigrationWorkflowRequestRequestTypeDef = TypedDict(
    "UpdateMigrationWorkflowRequestRequestTypeDef",
    {
        "id": str,
        "name": NotRequired[str],
        "description": NotRequired[str],
        "inputParameters": NotRequired[Mapping[str, StepInputTypeDef]],
        "stepTargets": NotRequired[Sequence[str]],
    },
)
CreateMigrationWorkflowResponseTypeDef = TypedDict(
    "CreateMigrationWorkflowResponseTypeDef",
    {
        "id": str,
        "arn": str,
        "name": str,
        "description": str,
        "templateId": str,
        "adsApplicationConfigurationId": str,
        "workflowInputs": Dict[str, StepInputTypeDef],
        "stepTargets": List[str],
        "status": MigrationWorkflowStatusEnumType,
        "creationTime": datetime,
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateWorkflowStepResponseTypeDef = TypedDict(
    "CreateWorkflowStepResponseTypeDef",
    {
        "id": str,
        "stepGroupId": str,
        "workflowId": str,
        "name": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteMigrationWorkflowResponseTypeDef = TypedDict(
    "DeleteMigrationWorkflowResponseTypeDef",
    {
        "id": str,
        "arn": str,
        "status": MigrationWorkflowStatusEnumType,
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
RetryWorkflowStepResponseTypeDef = TypedDict(
    "RetryWorkflowStepResponseTypeDef",
    {
        "stepGroupId": str,
        "workflowId": str,
        "id": str,
        "status": StepStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartMigrationWorkflowResponseTypeDef = TypedDict(
    "StartMigrationWorkflowResponseTypeDef",
    {
        "id": str,
        "arn": str,
        "status": MigrationWorkflowStatusEnumType,
        "statusMessage": str,
        "lastStartTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StopMigrationWorkflowResponseTypeDef = TypedDict(
    "StopMigrationWorkflowResponseTypeDef",
    {
        "id": str,
        "arn": str,
        "status": MigrationWorkflowStatusEnumType,
        "statusMessage": str,
        "lastStopTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateMigrationWorkflowResponseTypeDef = TypedDict(
    "UpdateMigrationWorkflowResponseTypeDef",
    {
        "id": str,
        "arn": str,
        "name": str,
        "description": str,
        "templateId": str,
        "adsApplicationConfigurationId": str,
        "workflowInputs": Dict[str, StepInputTypeDef],
        "stepTargets": List[str],
        "status": MigrationWorkflowStatusEnumType,
        "creationTime": datetime,
        "lastModifiedTime": datetime,
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateWorkflowStepResponseTypeDef = TypedDict(
    "UpdateWorkflowStepResponseTypeDef",
    {
        "id": str,
        "stepGroupId": str,
        "workflowId": str,
        "name": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateWorkflowStepGroupResponseTypeDef = TypedDict(
    "CreateWorkflowStepGroupResponseTypeDef",
    {
        "workflowId": str,
        "name": str,
        "id": str,
        "description": str,
        "tools": List[ToolTypeDef],
        "next": List[str],
        "previous": List[str],
        "creationTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetMigrationWorkflowResponseTypeDef = TypedDict(
    "GetMigrationWorkflowResponseTypeDef",
    {
        "id": str,
        "arn": str,
        "name": str,
        "description": str,
        "templateId": str,
        "adsApplicationConfigurationId": str,
        "adsApplicationName": str,
        "status": MigrationWorkflowStatusEnumType,
        "statusMessage": str,
        "creationTime": datetime,
        "lastStartTime": datetime,
        "lastStopTime": datetime,
        "lastModifiedTime": datetime,
        "endTime": datetime,
        "tools": List[ToolTypeDef],
        "totalSteps": int,
        "completedSteps": int,
        "workflowInputs": Dict[str, StepInputTypeDef],
        "tags": Dict[str, str],
        "workflowBucket": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetTemplateStepGroupResponseTypeDef = TypedDict(
    "GetTemplateStepGroupResponseTypeDef",
    {
        "templateId": str,
        "id": str,
        "name": str,
        "description": str,
        "status": StepGroupStatusType,
        "creationTime": datetime,
        "lastModifiedTime": datetime,
        "tools": List[ToolTypeDef],
        "previous": List[str],
        "next": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetWorkflowStepGroupResponseTypeDef = TypedDict(
    "GetWorkflowStepGroupResponseTypeDef",
    {
        "id": str,
        "workflowId": str,
        "name": str,
        "description": str,
        "status": StepGroupStatusType,
        "owner": OwnerType,
        "creationTime": datetime,
        "lastModifiedTime": datetime,
        "endTime": datetime,
        "tools": List[ToolTypeDef],
        "previous": List[str],
        "next": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateWorkflowStepGroupResponseTypeDef = TypedDict(
    "UpdateWorkflowStepGroupResponseTypeDef",
    {
        "workflowId": str,
        "name": str,
        "id": str,
        "description": str,
        "tools": List[ToolTypeDef],
        "next": List[str],
        "previous": List[str],
        "lastModifiedTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetMigrationWorkflowTemplateResponseTypeDef = TypedDict(
    "GetMigrationWorkflowTemplateResponseTypeDef",
    {
        "id": str,
        "name": str,
        "description": str,
        "inputs": List[TemplateInputTypeDef],
        "tools": List[ToolTypeDef],
        "status": Literal["CREATED"],
        "creationTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListMigrationWorkflowTemplatesRequestListTemplatesPaginateTypeDef = TypedDict(
    "ListMigrationWorkflowTemplatesRequestListTemplatesPaginateTypeDef",
    {
        "name": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListMigrationWorkflowsRequestListWorkflowsPaginateTypeDef = TypedDict(
    "ListMigrationWorkflowsRequestListWorkflowsPaginateTypeDef",
    {
        "templateId": NotRequired[str],
        "adsApplicationConfigurationName": NotRequired[str],
        "status": NotRequired[MigrationWorkflowStatusEnumType],
        "name": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListPluginsRequestListPluginsPaginateTypeDef = TypedDict(
    "ListPluginsRequestListPluginsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListTemplateStepGroupsRequestListTemplateStepGroupsPaginateTypeDef = TypedDict(
    "ListTemplateStepGroupsRequestListTemplateStepGroupsPaginateTypeDef",
    {
        "templateId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListTemplateStepsRequestListTemplateStepsPaginateTypeDef = TypedDict(
    "ListTemplateStepsRequestListTemplateStepsPaginateTypeDef",
    {
        "templateId": str,
        "stepGroupId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListWorkflowStepGroupsRequestListWorkflowStepGroupsPaginateTypeDef = TypedDict(
    "ListWorkflowStepGroupsRequestListWorkflowStepGroupsPaginateTypeDef",
    {
        "workflowId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListWorkflowStepsRequestListWorkflowStepsPaginateTypeDef = TypedDict(
    "ListWorkflowStepsRequestListWorkflowStepsPaginateTypeDef",
    {
        "workflowId": str,
        "stepGroupId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListMigrationWorkflowTemplatesResponseTypeDef = TypedDict(
    "ListMigrationWorkflowTemplatesResponseTypeDef",
    {
        "nextToken": str,
        "templateSummary": List[TemplateSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListMigrationWorkflowsResponseTypeDef = TypedDict(
    "ListMigrationWorkflowsResponseTypeDef",
    {
        "nextToken": str,
        "migrationWorkflowSummary": List[MigrationWorkflowSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListPluginsResponseTypeDef = TypedDict(
    "ListPluginsResponseTypeDef",
    {
        "nextToken": str,
        "plugins": List[PluginSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTemplateStepGroupsResponseTypeDef = TypedDict(
    "ListTemplateStepGroupsResponseTypeDef",
    {
        "nextToken": str,
        "templateStepGroupSummary": List[TemplateStepGroupSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTemplateStepsResponseTypeDef = TypedDict(
    "ListTemplateStepsResponseTypeDef",
    {
        "nextToken": str,
        "templateStepSummaryList": List[TemplateStepSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListWorkflowStepGroupsResponseTypeDef = TypedDict(
    "ListWorkflowStepGroupsResponseTypeDef",
    {
        "nextToken": str,
        "workflowStepGroupsSummary": List[WorkflowStepGroupSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListWorkflowStepsResponseTypeDef = TypedDict(
    "ListWorkflowStepsResponseTypeDef",
    {
        "nextToken": str,
        "workflowStepsSummary": List[WorkflowStepSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StepAutomationConfigurationTypeDef = TypedDict(
    "StepAutomationConfigurationTypeDef",
    {
        "scriptLocationS3Bucket": NotRequired[str],
        "scriptLocationS3Key": NotRequired[PlatformScriptKeyTypeDef],
        "command": NotRequired[PlatformCommandTypeDef],
        "runEnvironment": NotRequired[RunEnvironmentType],
        "targetType": NotRequired[TargetTypeType],
    },
)
WorkflowStepAutomationConfigurationTypeDef = TypedDict(
    "WorkflowStepAutomationConfigurationTypeDef",
    {
        "scriptLocationS3Bucket": NotRequired[str],
        "scriptLocationS3Key": NotRequired[PlatformScriptKeyTypeDef],
        "command": NotRequired[PlatformCommandTypeDef],
        "runEnvironment": NotRequired[RunEnvironmentType],
        "targetType": NotRequired[TargetTypeType],
    },
)
WorkflowStepOutputTypeDef = TypedDict(
    "WorkflowStepOutputTypeDef",
    {
        "name": NotRequired[str],
        "dataType": NotRequired[DataTypeType],
        "required": NotRequired[bool],
        "value": NotRequired[WorkflowStepOutputUnionTypeDef],
    },
)
GetTemplateStepResponseTypeDef = TypedDict(
    "GetTemplateStepResponseTypeDef",
    {
        "id": str,
        "stepGroupId": str,
        "templateId": str,
        "name": str,
        "description": str,
        "stepActionType": StepActionTypeType,
        "creationTime": str,
        "previous": List[str],
        "next": List[str],
        "outputs": List[StepOutputTypeDef],
        "stepAutomationConfiguration": StepAutomationConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateWorkflowStepRequestRequestTypeDef = TypedDict(
    "CreateWorkflowStepRequestRequestTypeDef",
    {
        "name": str,
        "stepGroupId": str,
        "workflowId": str,
        "stepActionType": StepActionTypeType,
        "description": NotRequired[str],
        "workflowStepAutomationConfiguration": NotRequired[
            WorkflowStepAutomationConfigurationTypeDef
        ],
        "stepTarget": NotRequired[Sequence[str]],
        "outputs": NotRequired[Sequence[WorkflowStepOutputTypeDef]],
        "previous": NotRequired[Sequence[str]],
        "next": NotRequired[Sequence[str]],
    },
)
GetWorkflowStepResponseTypeDef = TypedDict(
    "GetWorkflowStepResponseTypeDef",
    {
        "name": str,
        "stepGroupId": str,
        "workflowId": str,
        "stepId": str,
        "description": str,
        "stepActionType": StepActionTypeType,
        "owner": OwnerType,
        "workflowStepAutomationConfiguration": WorkflowStepAutomationConfigurationTypeDef,
        "stepTarget": List[str],
        "outputs": List[WorkflowStepOutputTypeDef],
        "previous": List[str],
        "next": List[str],
        "status": StepStatusType,
        "statusMessage": str,
        "scriptOutputLocation": str,
        "creationTime": datetime,
        "lastStartTime": datetime,
        "endTime": datetime,
        "noOfSrvCompleted": int,
        "noOfSrvFailed": int,
        "totalNoOfSrv": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateWorkflowStepRequestRequestTypeDef = TypedDict(
    "UpdateWorkflowStepRequestRequestTypeDef",
    {
        "id": str,
        "stepGroupId": str,
        "workflowId": str,
        "name": NotRequired[str],
        "description": NotRequired[str],
        "stepActionType": NotRequired[StepActionTypeType],
        "workflowStepAutomationConfiguration": NotRequired[
            WorkflowStepAutomationConfigurationTypeDef
        ],
        "stepTarget": NotRequired[Sequence[str]],
        "outputs": NotRequired[Sequence[WorkflowStepOutputTypeDef]],
        "previous": NotRequired[Sequence[str]],
        "next": NotRequired[Sequence[str]],
        "status": NotRequired[StepStatusType],
    },
)
