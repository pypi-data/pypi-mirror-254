"""
Main interface for finspace service.

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_finspace import (
        Client,
        ListKxEnvironmentsPaginator,
        finspaceClient,
    )

    session = get_session()
    async with session.create_client("finspace") as client:
        client: finspaceClient
        ...


    list_kx_environments_paginator: ListKxEnvironmentsPaginator = client.get_paginator("list_kx_environments")
    ```
"""

from .client import finspaceClient
from .paginator import ListKxEnvironmentsPaginator

Client = finspaceClient

__all__ = ("Client", "ListKxEnvironmentsPaginator", "finspaceClient")
