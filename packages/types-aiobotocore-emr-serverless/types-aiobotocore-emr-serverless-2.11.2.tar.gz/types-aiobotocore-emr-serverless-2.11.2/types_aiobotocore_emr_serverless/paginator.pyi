"""
Type annotations for emr-serverless service client paginators.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_emr_serverless/paginators/)

Usage::

    ```python
    from aiobotocore.session import get_session

    from types_aiobotocore_emr_serverless.client import EMRServerlessClient
    from types_aiobotocore_emr_serverless.paginator import (
        ListApplicationsPaginator,
        ListJobRunsPaginator,
    )

    session = get_session()
    with session.create_client("emr-serverless") as client:
        client: EMRServerlessClient

        list_applications_paginator: ListApplicationsPaginator = client.get_paginator("list_applications")
        list_job_runs_paginator: ListJobRunsPaginator = client.get_paginator("list_job_runs")
    ```
"""

from typing import AsyncIterator, Generic, Iterator, Sequence, TypeVar

from aiobotocore.paginate import AioPaginator
from botocore.paginate import PageIterator

from .literals import ApplicationStateType, JobRunStateType
from .type_defs import (
    ListApplicationsResponseTypeDef,
    ListJobRunsResponseTypeDef,
    PaginatorConfigTypeDef,
    TimestampTypeDef,
)

__all__ = ("ListApplicationsPaginator", "ListJobRunsPaginator")

_ItemTypeDef = TypeVar("_ItemTypeDef")

class _PageIterator(Generic[_ItemTypeDef], PageIterator):
    def __iter__(self) -> Iterator[_ItemTypeDef]:
        """
        Proxy method to specify iterator item type.
        """

class ListApplicationsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-serverless.html#EMRServerless.Paginator.ListApplications)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_emr_serverless/paginators/#listapplicationspaginator)
    """

    def paginate(
        self,
        *,
        states: Sequence[ApplicationStateType] = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListApplicationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-serverless.html#EMRServerless.Paginator.ListApplications.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_emr_serverless/paginators/#listapplicationspaginator)
        """

class ListJobRunsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-serverless.html#EMRServerless.Paginator.ListJobRuns)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_emr_serverless/paginators/#listjobrunspaginator)
    """

    def paginate(
        self,
        *,
        applicationId: str,
        createdAtAfter: TimestampTypeDef = ...,
        createdAtBefore: TimestampTypeDef = ...,
        states: Sequence[JobRunStateType] = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListJobRunsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-serverless.html#EMRServerless.Paginator.ListJobRuns.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_emr_serverless/paginators/#listjobrunspaginator)
        """
