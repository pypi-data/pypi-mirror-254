"""
Main interface for emr-serverless service.

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_emr_serverless import (
        Client,
        EMRServerlessClient,
        ListApplicationsPaginator,
        ListJobRunsPaginator,
    )

    session = get_session()
    async with session.create_client("emr-serverless") as client:
        client: EMRServerlessClient
        ...


    list_applications_paginator: ListApplicationsPaginator = client.get_paginator("list_applications")
    list_job_runs_paginator: ListJobRunsPaginator = client.get_paginator("list_job_runs")
    ```
"""

from .client import EMRServerlessClient
from .paginator import ListApplicationsPaginator, ListJobRunsPaginator

Client = EMRServerlessClient

__all__ = ("Client", "EMRServerlessClient", "ListApplicationsPaginator", "ListJobRunsPaginator")
