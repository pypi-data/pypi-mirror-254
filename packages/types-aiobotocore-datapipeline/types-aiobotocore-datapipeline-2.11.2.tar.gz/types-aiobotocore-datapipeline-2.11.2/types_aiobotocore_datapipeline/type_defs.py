"""
Type annotations for datapipeline service type definitions.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datapipeline/type_defs/)

Usage::

    ```python
    from types_aiobotocore_datapipeline.type_defs import ParameterValueTypeDef

    data: ParameterValueTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Sequence, Union

from .literals import OperatorTypeType, TaskStatusType

if sys.version_info >= (3, 12):
    from typing import NotRequired
else:
    from typing_extensions import NotRequired
if sys.version_info >= (3, 12):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "ParameterValueTypeDef",
    "TimestampTypeDef",
    "TagTypeDef",
    "ResponseMetadataTypeDef",
    "DeactivatePipelineInputRequestTypeDef",
    "DeletePipelineInputRequestTypeDef",
    "PaginatorConfigTypeDef",
    "DescribeObjectsInputRequestTypeDef",
    "DescribePipelinesInputRequestTypeDef",
    "EvaluateExpressionInputRequestTypeDef",
    "FieldTypeDef",
    "GetPipelineDefinitionInputRequestTypeDef",
    "InstanceIdentityTypeDef",
    "ListPipelinesInputRequestTypeDef",
    "PipelineIdNameTypeDef",
    "OperatorTypeDef",
    "ParameterAttributeTypeDef",
    "ValidationErrorTypeDef",
    "ValidationWarningTypeDef",
    "RemoveTagsInputRequestTypeDef",
    "ReportTaskRunnerHeartbeatInputRequestTypeDef",
    "SetStatusInputRequestTypeDef",
    "SetTaskStatusInputRequestTypeDef",
    "ActivatePipelineInputRequestTypeDef",
    "AddTagsInputRequestTypeDef",
    "CreatePipelineInputRequestTypeDef",
    "CreatePipelineOutputTypeDef",
    "EmptyResponseMetadataTypeDef",
    "EvaluateExpressionOutputTypeDef",
    "QueryObjectsOutputTypeDef",
    "ReportTaskProgressOutputTypeDef",
    "ReportTaskRunnerHeartbeatOutputTypeDef",
    "DescribeObjectsInputDescribeObjectsPaginateTypeDef",
    "ListPipelinesInputListPipelinesPaginateTypeDef",
    "PipelineDescriptionTypeDef",
    "PipelineObjectTypeDef",
    "ReportTaskProgressInputRequestTypeDef",
    "PollForTaskInputRequestTypeDef",
    "ListPipelinesOutputTypeDef",
    "SelectorTypeDef",
    "ParameterObjectTypeDef",
    "PutPipelineDefinitionOutputTypeDef",
    "ValidatePipelineDefinitionOutputTypeDef",
    "DescribePipelinesOutputTypeDef",
    "DescribeObjectsOutputTypeDef",
    "TaskObjectTypeDef",
    "QueryTypeDef",
    "GetPipelineDefinitionOutputTypeDef",
    "PutPipelineDefinitionInputRequestTypeDef",
    "ValidatePipelineDefinitionInputRequestTypeDef",
    "PollForTaskOutputTypeDef",
    "QueryObjectsInputQueryObjectsPaginateTypeDef",
    "QueryObjectsInputRequestTypeDef",
)

ParameterValueTypeDef = TypedDict(
    "ParameterValueTypeDef",
    {
        "id": str,
        "stringValue": str,
    },
)
TimestampTypeDef = Union[datetime, str]
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "key": str,
        "value": str,
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
DeactivatePipelineInputRequestTypeDef = TypedDict(
    "DeactivatePipelineInputRequestTypeDef",
    {
        "pipelineId": str,
        "cancelActive": NotRequired[bool],
    },
)
DeletePipelineInputRequestTypeDef = TypedDict(
    "DeletePipelineInputRequestTypeDef",
    {
        "pipelineId": str,
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
DescribeObjectsInputRequestTypeDef = TypedDict(
    "DescribeObjectsInputRequestTypeDef",
    {
        "pipelineId": str,
        "objectIds": Sequence[str],
        "evaluateExpressions": NotRequired[bool],
        "marker": NotRequired[str],
    },
)
DescribePipelinesInputRequestTypeDef = TypedDict(
    "DescribePipelinesInputRequestTypeDef",
    {
        "pipelineIds": Sequence[str],
    },
)
EvaluateExpressionInputRequestTypeDef = TypedDict(
    "EvaluateExpressionInputRequestTypeDef",
    {
        "pipelineId": str,
        "objectId": str,
        "expression": str,
    },
)
FieldTypeDef = TypedDict(
    "FieldTypeDef",
    {
        "key": str,
        "stringValue": NotRequired[str],
        "refValue": NotRequired[str],
    },
)
GetPipelineDefinitionInputRequestTypeDef = TypedDict(
    "GetPipelineDefinitionInputRequestTypeDef",
    {
        "pipelineId": str,
        "version": NotRequired[str],
    },
)
InstanceIdentityTypeDef = TypedDict(
    "InstanceIdentityTypeDef",
    {
        "document": NotRequired[str],
        "signature": NotRequired[str],
    },
)
ListPipelinesInputRequestTypeDef = TypedDict(
    "ListPipelinesInputRequestTypeDef",
    {
        "marker": NotRequired[str],
    },
)
PipelineIdNameTypeDef = TypedDict(
    "PipelineIdNameTypeDef",
    {
        "id": NotRequired[str],
        "name": NotRequired[str],
    },
)
OperatorTypeDef = TypedDict(
    "OperatorTypeDef",
    {
        "type": NotRequired[OperatorTypeType],
        "values": NotRequired[Sequence[str]],
    },
)
ParameterAttributeTypeDef = TypedDict(
    "ParameterAttributeTypeDef",
    {
        "key": str,
        "stringValue": str,
    },
)
ValidationErrorTypeDef = TypedDict(
    "ValidationErrorTypeDef",
    {
        "id": NotRequired[str],
        "errors": NotRequired[List[str]],
    },
)
ValidationWarningTypeDef = TypedDict(
    "ValidationWarningTypeDef",
    {
        "id": NotRequired[str],
        "warnings": NotRequired[List[str]],
    },
)
RemoveTagsInputRequestTypeDef = TypedDict(
    "RemoveTagsInputRequestTypeDef",
    {
        "pipelineId": str,
        "tagKeys": Sequence[str],
    },
)
ReportTaskRunnerHeartbeatInputRequestTypeDef = TypedDict(
    "ReportTaskRunnerHeartbeatInputRequestTypeDef",
    {
        "taskrunnerId": str,
        "workerGroup": NotRequired[str],
        "hostname": NotRequired[str],
    },
)
SetStatusInputRequestTypeDef = TypedDict(
    "SetStatusInputRequestTypeDef",
    {
        "pipelineId": str,
        "objectIds": Sequence[str],
        "status": str,
    },
)
SetTaskStatusInputRequestTypeDef = TypedDict(
    "SetTaskStatusInputRequestTypeDef",
    {
        "taskId": str,
        "taskStatus": TaskStatusType,
        "errorId": NotRequired[str],
        "errorMessage": NotRequired[str],
        "errorStackTrace": NotRequired[str],
    },
)
ActivatePipelineInputRequestTypeDef = TypedDict(
    "ActivatePipelineInputRequestTypeDef",
    {
        "pipelineId": str,
        "parameterValues": NotRequired[Sequence[ParameterValueTypeDef]],
        "startTimestamp": NotRequired[TimestampTypeDef],
    },
)
AddTagsInputRequestTypeDef = TypedDict(
    "AddTagsInputRequestTypeDef",
    {
        "pipelineId": str,
        "tags": Sequence[TagTypeDef],
    },
)
CreatePipelineInputRequestTypeDef = TypedDict(
    "CreatePipelineInputRequestTypeDef",
    {
        "name": str,
        "uniqueId": str,
        "description": NotRequired[str],
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreatePipelineOutputTypeDef = TypedDict(
    "CreatePipelineOutputTypeDef",
    {
        "pipelineId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EvaluateExpressionOutputTypeDef = TypedDict(
    "EvaluateExpressionOutputTypeDef",
    {
        "evaluatedExpression": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
QueryObjectsOutputTypeDef = TypedDict(
    "QueryObjectsOutputTypeDef",
    {
        "ids": List[str],
        "marker": str,
        "hasMoreResults": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ReportTaskProgressOutputTypeDef = TypedDict(
    "ReportTaskProgressOutputTypeDef",
    {
        "canceled": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ReportTaskRunnerHeartbeatOutputTypeDef = TypedDict(
    "ReportTaskRunnerHeartbeatOutputTypeDef",
    {
        "terminate": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeObjectsInputDescribeObjectsPaginateTypeDef = TypedDict(
    "DescribeObjectsInputDescribeObjectsPaginateTypeDef",
    {
        "pipelineId": str,
        "objectIds": Sequence[str],
        "evaluateExpressions": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListPipelinesInputListPipelinesPaginateTypeDef = TypedDict(
    "ListPipelinesInputListPipelinesPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
PipelineDescriptionTypeDef = TypedDict(
    "PipelineDescriptionTypeDef",
    {
        "pipelineId": str,
        "name": str,
        "fields": List[FieldTypeDef],
        "description": NotRequired[str],
        "tags": NotRequired[List[TagTypeDef]],
    },
)
PipelineObjectTypeDef = TypedDict(
    "PipelineObjectTypeDef",
    {
        "id": str,
        "name": str,
        "fields": List[FieldTypeDef],
    },
)
ReportTaskProgressInputRequestTypeDef = TypedDict(
    "ReportTaskProgressInputRequestTypeDef",
    {
        "taskId": str,
        "fields": NotRequired[Sequence[FieldTypeDef]],
    },
)
PollForTaskInputRequestTypeDef = TypedDict(
    "PollForTaskInputRequestTypeDef",
    {
        "workerGroup": str,
        "hostname": NotRequired[str],
        "instanceIdentity": NotRequired[InstanceIdentityTypeDef],
    },
)
ListPipelinesOutputTypeDef = TypedDict(
    "ListPipelinesOutputTypeDef",
    {
        "pipelineIdList": List[PipelineIdNameTypeDef],
        "marker": str,
        "hasMoreResults": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SelectorTypeDef = TypedDict(
    "SelectorTypeDef",
    {
        "fieldName": NotRequired[str],
        "operator": NotRequired[OperatorTypeDef],
    },
)
ParameterObjectTypeDef = TypedDict(
    "ParameterObjectTypeDef",
    {
        "id": str,
        "attributes": List[ParameterAttributeTypeDef],
    },
)
PutPipelineDefinitionOutputTypeDef = TypedDict(
    "PutPipelineDefinitionOutputTypeDef",
    {
        "validationErrors": List[ValidationErrorTypeDef],
        "validationWarnings": List[ValidationWarningTypeDef],
        "errored": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ValidatePipelineDefinitionOutputTypeDef = TypedDict(
    "ValidatePipelineDefinitionOutputTypeDef",
    {
        "validationErrors": List[ValidationErrorTypeDef],
        "validationWarnings": List[ValidationWarningTypeDef],
        "errored": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribePipelinesOutputTypeDef = TypedDict(
    "DescribePipelinesOutputTypeDef",
    {
        "pipelineDescriptionList": List[PipelineDescriptionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeObjectsOutputTypeDef = TypedDict(
    "DescribeObjectsOutputTypeDef",
    {
        "pipelineObjects": List[PipelineObjectTypeDef],
        "marker": str,
        "hasMoreResults": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TaskObjectTypeDef = TypedDict(
    "TaskObjectTypeDef",
    {
        "taskId": NotRequired[str],
        "pipelineId": NotRequired[str],
        "attemptId": NotRequired[str],
        "objects": NotRequired[Dict[str, PipelineObjectTypeDef]],
    },
)
QueryTypeDef = TypedDict(
    "QueryTypeDef",
    {
        "selectors": NotRequired[Sequence[SelectorTypeDef]],
    },
)
GetPipelineDefinitionOutputTypeDef = TypedDict(
    "GetPipelineDefinitionOutputTypeDef",
    {
        "pipelineObjects": List[PipelineObjectTypeDef],
        "parameterObjects": List[ParameterObjectTypeDef],
        "parameterValues": List[ParameterValueTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutPipelineDefinitionInputRequestTypeDef = TypedDict(
    "PutPipelineDefinitionInputRequestTypeDef",
    {
        "pipelineId": str,
        "pipelineObjects": Sequence[PipelineObjectTypeDef],
        "parameterObjects": NotRequired[Sequence[ParameterObjectTypeDef]],
        "parameterValues": NotRequired[Sequence[ParameterValueTypeDef]],
    },
)
ValidatePipelineDefinitionInputRequestTypeDef = TypedDict(
    "ValidatePipelineDefinitionInputRequestTypeDef",
    {
        "pipelineId": str,
        "pipelineObjects": Sequence[PipelineObjectTypeDef],
        "parameterObjects": NotRequired[Sequence[ParameterObjectTypeDef]],
        "parameterValues": NotRequired[Sequence[ParameterValueTypeDef]],
    },
)
PollForTaskOutputTypeDef = TypedDict(
    "PollForTaskOutputTypeDef",
    {
        "taskObject": TaskObjectTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
QueryObjectsInputQueryObjectsPaginateTypeDef = TypedDict(
    "QueryObjectsInputQueryObjectsPaginateTypeDef",
    {
        "pipelineId": str,
        "sphere": str,
        "query": NotRequired[QueryTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
QueryObjectsInputRequestTypeDef = TypedDict(
    "QueryObjectsInputRequestTypeDef",
    {
        "pipelineId": str,
        "sphere": str,
        "query": NotRequired[QueryTypeDef],
        "marker": NotRequired[str],
        "limit": NotRequired[int],
    },
)
