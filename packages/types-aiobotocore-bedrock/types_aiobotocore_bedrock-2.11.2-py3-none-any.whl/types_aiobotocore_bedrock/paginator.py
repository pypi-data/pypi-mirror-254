"""
Type annotations for bedrock service client paginators.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_bedrock/paginators/)

Usage::

    ```python
    from aiobotocore.session import get_session

    from types_aiobotocore_bedrock.client import BedrockClient
    from types_aiobotocore_bedrock.paginator import (
        ListCustomModelsPaginator,
        ListModelCustomizationJobsPaginator,
        ListProvisionedModelThroughputsPaginator,
    )

    session = get_session()
    with session.create_client("bedrock") as client:
        client: BedrockClient

        list_custom_models_paginator: ListCustomModelsPaginator = client.get_paginator("list_custom_models")
        list_model_customization_jobs_paginator: ListModelCustomizationJobsPaginator = client.get_paginator("list_model_customization_jobs")
        list_provisioned_model_throughputs_paginator: ListProvisionedModelThroughputsPaginator = client.get_paginator("list_provisioned_model_throughputs")
    ```
"""

import sys
from typing import AsyncIterator, Generic, Iterator, TypeVar

from aiobotocore.paginate import AioPaginator
from botocore.paginate import PageIterator

from .literals import FineTuningJobStatusType, ProvisionedModelStatusType, SortOrderType
from .type_defs import (
    ListCustomModelsResponseTypeDef,
    ListModelCustomizationJobsResponseTypeDef,
    ListProvisionedModelThroughputsResponseTypeDef,
    PaginatorConfigTypeDef,
    TimestampTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ListCustomModelsPaginator",
    "ListModelCustomizationJobsPaginator",
    "ListProvisionedModelThroughputsPaginator",
)

_ItemTypeDef = TypeVar("_ItemTypeDef")


class _PageIterator(Generic[_ItemTypeDef], PageIterator):
    def __iter__(self) -> Iterator[_ItemTypeDef]:
        """
        Proxy method to specify iterator item type.
        """


class ListCustomModelsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock.html#Bedrock.Paginator.ListCustomModels)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_bedrock/paginators/#listcustommodelspaginator)
    """

    def paginate(
        self,
        *,
        creationTimeBefore: TimestampTypeDef = ...,
        creationTimeAfter: TimestampTypeDef = ...,
        nameContains: str = ...,
        baseModelArnEquals: str = ...,
        foundationModelArnEquals: str = ...,
        sortBy: Literal["CreationTime"] = ...,
        sortOrder: SortOrderType = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListCustomModelsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock.html#Bedrock.Paginator.ListCustomModels.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_bedrock/paginators/#listcustommodelspaginator)
        """


class ListModelCustomizationJobsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock.html#Bedrock.Paginator.ListModelCustomizationJobs)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_bedrock/paginators/#listmodelcustomizationjobspaginator)
    """

    def paginate(
        self,
        *,
        creationTimeAfter: TimestampTypeDef = ...,
        creationTimeBefore: TimestampTypeDef = ...,
        statusEquals: FineTuningJobStatusType = ...,
        nameContains: str = ...,
        sortBy: Literal["CreationTime"] = ...,
        sortOrder: SortOrderType = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListModelCustomizationJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock.html#Bedrock.Paginator.ListModelCustomizationJobs.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_bedrock/paginators/#listmodelcustomizationjobspaginator)
        """


class ListProvisionedModelThroughputsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock.html#Bedrock.Paginator.ListProvisionedModelThroughputs)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_bedrock/paginators/#listprovisionedmodelthroughputspaginator)
    """

    def paginate(
        self,
        *,
        creationTimeAfter: TimestampTypeDef = ...,
        creationTimeBefore: TimestampTypeDef = ...,
        statusEquals: ProvisionedModelStatusType = ...,
        modelArnEquals: str = ...,
        nameContains: str = ...,
        sortBy: Literal["CreationTime"] = ...,
        sortOrder: SortOrderType = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListProvisionedModelThroughputsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock.html#Bedrock.Paginator.ListProvisionedModelThroughputs.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_bedrock/paginators/#listprovisionedmodelthroughputspaginator)
        """
