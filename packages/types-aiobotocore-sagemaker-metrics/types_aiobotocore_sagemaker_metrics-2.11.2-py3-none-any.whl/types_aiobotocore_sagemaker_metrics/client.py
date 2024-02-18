"""
Type annotations for sagemaker-metrics service client.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker_metrics/client/)

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_sagemaker_metrics.client import SageMakerMetricsClient

    session = get_session()
    async with session.create_client("sagemaker-metrics") as client:
        client: SageMakerMetricsClient
    ```
"""

from typing import Any, Dict, Mapping, Sequence, Type

from aiobotocore.client import AioBaseClient
from botocore.client import ClientMeta

from .type_defs import BatchPutMetricsResponseTypeDef, RawMetricDataTypeDef

__all__ = ("SageMakerMetricsClient",)


class BotocoreClientError(Exception):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]


class SageMakerMetricsClient(AioBaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-metrics.html#SageMakerMetrics.Client)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker_metrics/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        SageMakerMetricsClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-metrics.html#SageMakerMetrics.Client.exceptions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker_metrics/client/#exceptions)
        """

    async def batch_put_metrics(
        self, *, TrialComponentName: str, MetricData: Sequence[RawMetricDataTypeDef]
    ) -> BatchPutMetricsResponseTypeDef:
        """
        Used to ingest training metrics into SageMaker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-metrics.html#SageMakerMetrics.Client.batch_put_metrics)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker_metrics/client/#batch_put_metrics)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-metrics.html#SageMakerMetrics.Client.can_paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker_metrics/client/#can_paginate)
        """

    async def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-metrics.html#SageMakerMetrics.Client.close)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker_metrics/client/#close)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-metrics.html#SageMakerMetrics.Client.generate_presigned_url)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker_metrics/client/#generate_presigned_url)
        """

    async def __aenter__(self) -> "SageMakerMetricsClient":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-metrics.html#SageMakerMetrics.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker_metrics/client/)
        """

    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> Any:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-metrics.html#SageMakerMetrics.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker_metrics/client/)
        """
