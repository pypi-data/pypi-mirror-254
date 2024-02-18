"""
Main interface for repostspace service.

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_repostspace import (
        Client,
        ListSpacesPaginator,
        rePostPrivateClient,
    )

    session = get_session()
    async with session.create_client("repostspace") as client:
        client: rePostPrivateClient
        ...


    list_spaces_paginator: ListSpacesPaginator = client.get_paginator("list_spaces")
    ```
"""

from .client import rePostPrivateClient
from .paginator import ListSpacesPaginator

Client = rePostPrivateClient

__all__ = ("Client", "ListSpacesPaginator", "rePostPrivateClient")
