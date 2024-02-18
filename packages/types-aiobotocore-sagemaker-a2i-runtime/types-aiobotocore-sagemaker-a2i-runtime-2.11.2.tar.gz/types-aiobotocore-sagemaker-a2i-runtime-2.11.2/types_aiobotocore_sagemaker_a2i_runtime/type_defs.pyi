"""
Type annotations for sagemaker-a2i-runtime service type definitions.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker_a2i_runtime/type_defs/)

Usage::

    ```python
    from types_aiobotocore_sagemaker_a2i_runtime.type_defs import DeleteHumanLoopRequestRequestTypeDef

    data: DeleteHumanLoopRequestRequestTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Sequence, Union

from .literals import ContentClassifierType, HumanLoopStatusType, SortOrderType

if sys.version_info >= (3, 12):
    from typing import NotRequired
else:
    from typing_extensions import NotRequired
if sys.version_info >= (3, 12):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "DeleteHumanLoopRequestRequestTypeDef",
    "DescribeHumanLoopRequestRequestTypeDef",
    "HumanLoopOutputTypeDef",
    "ResponseMetadataTypeDef",
    "HumanLoopDataAttributesTypeDef",
    "HumanLoopInputTypeDef",
    "HumanLoopSummaryTypeDef",
    "PaginatorConfigTypeDef",
    "TimestampTypeDef",
    "StopHumanLoopRequestRequestTypeDef",
    "DescribeHumanLoopResponseTypeDef",
    "StartHumanLoopResponseTypeDef",
    "StartHumanLoopRequestRequestTypeDef",
    "ListHumanLoopsResponseTypeDef",
    "ListHumanLoopsRequestListHumanLoopsPaginateTypeDef",
    "ListHumanLoopsRequestRequestTypeDef",
)

DeleteHumanLoopRequestRequestTypeDef = TypedDict(
    "DeleteHumanLoopRequestRequestTypeDef",
    {
        "HumanLoopName": str,
    },
)
DescribeHumanLoopRequestRequestTypeDef = TypedDict(
    "DescribeHumanLoopRequestRequestTypeDef",
    {
        "HumanLoopName": str,
    },
)
HumanLoopOutputTypeDef = TypedDict(
    "HumanLoopOutputTypeDef",
    {
        "OutputS3Uri": str,
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
HumanLoopDataAttributesTypeDef = TypedDict(
    "HumanLoopDataAttributesTypeDef",
    {
        "ContentClassifiers": Sequence[ContentClassifierType],
    },
)
HumanLoopInputTypeDef = TypedDict(
    "HumanLoopInputTypeDef",
    {
        "InputContent": str,
    },
)
HumanLoopSummaryTypeDef = TypedDict(
    "HumanLoopSummaryTypeDef",
    {
        "HumanLoopName": NotRequired[str],
        "HumanLoopStatus": NotRequired[HumanLoopStatusType],
        "CreationTime": NotRequired[datetime],
        "FailureReason": NotRequired[str],
        "FlowDefinitionArn": NotRequired[str],
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
TimestampTypeDef = Union[datetime, str]
StopHumanLoopRequestRequestTypeDef = TypedDict(
    "StopHumanLoopRequestRequestTypeDef",
    {
        "HumanLoopName": str,
    },
)
DescribeHumanLoopResponseTypeDef = TypedDict(
    "DescribeHumanLoopResponseTypeDef",
    {
        "CreationTime": datetime,
        "FailureReason": str,
        "FailureCode": str,
        "HumanLoopStatus": HumanLoopStatusType,
        "HumanLoopName": str,
        "HumanLoopArn": str,
        "FlowDefinitionArn": str,
        "HumanLoopOutput": HumanLoopOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartHumanLoopResponseTypeDef = TypedDict(
    "StartHumanLoopResponseTypeDef",
    {
        "HumanLoopArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartHumanLoopRequestRequestTypeDef = TypedDict(
    "StartHumanLoopRequestRequestTypeDef",
    {
        "HumanLoopName": str,
        "FlowDefinitionArn": str,
        "HumanLoopInput": HumanLoopInputTypeDef,
        "DataAttributes": NotRequired[HumanLoopDataAttributesTypeDef],
    },
)
ListHumanLoopsResponseTypeDef = TypedDict(
    "ListHumanLoopsResponseTypeDef",
    {
        "HumanLoopSummaries": List[HumanLoopSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListHumanLoopsRequestListHumanLoopsPaginateTypeDef = TypedDict(
    "ListHumanLoopsRequestListHumanLoopsPaginateTypeDef",
    {
        "FlowDefinitionArn": str,
        "CreationTimeAfter": NotRequired[TimestampTypeDef],
        "CreationTimeBefore": NotRequired[TimestampTypeDef],
        "SortOrder": NotRequired[SortOrderType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListHumanLoopsRequestRequestTypeDef = TypedDict(
    "ListHumanLoopsRequestRequestTypeDef",
    {
        "FlowDefinitionArn": str,
        "CreationTimeAfter": NotRequired[TimestampTypeDef],
        "CreationTimeBefore": NotRequired[TimestampTypeDef],
        "SortOrder": NotRequired[SortOrderType],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
