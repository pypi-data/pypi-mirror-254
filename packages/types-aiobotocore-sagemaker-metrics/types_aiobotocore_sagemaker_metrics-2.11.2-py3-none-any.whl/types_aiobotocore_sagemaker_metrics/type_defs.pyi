"""
Type annotations for sagemaker-metrics service type definitions.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker_metrics/type_defs/)

Usage::

    ```python
    from types_aiobotocore_sagemaker_metrics.type_defs import BatchPutMetricsErrorTypeDef

    data: BatchPutMetricsErrorTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Sequence, Union

from .literals import PutMetricsErrorCodeType

if sys.version_info >= (3, 12):
    from typing import NotRequired
else:
    from typing_extensions import NotRequired
if sys.version_info >= (3, 12):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "BatchPutMetricsErrorTypeDef",
    "ResponseMetadataTypeDef",
    "TimestampTypeDef",
    "BatchPutMetricsResponseTypeDef",
    "RawMetricDataTypeDef",
    "BatchPutMetricsRequestRequestTypeDef",
)

BatchPutMetricsErrorTypeDef = TypedDict(
    "BatchPutMetricsErrorTypeDef",
    {
        "Code": NotRequired[PutMetricsErrorCodeType],
        "MetricIndex": NotRequired[int],
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
TimestampTypeDef = Union[datetime, str]
BatchPutMetricsResponseTypeDef = TypedDict(
    "BatchPutMetricsResponseTypeDef",
    {
        "Errors": List[BatchPutMetricsErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RawMetricDataTypeDef = TypedDict(
    "RawMetricDataTypeDef",
    {
        "MetricName": str,
        "Timestamp": TimestampTypeDef,
        "Value": float,
        "Step": NotRequired[int],
    },
)
BatchPutMetricsRequestRequestTypeDef = TypedDict(
    "BatchPutMetricsRequestRequestTypeDef",
    {
        "TrialComponentName": str,
        "MetricData": Sequence[RawMetricDataTypeDef],
    },
)
