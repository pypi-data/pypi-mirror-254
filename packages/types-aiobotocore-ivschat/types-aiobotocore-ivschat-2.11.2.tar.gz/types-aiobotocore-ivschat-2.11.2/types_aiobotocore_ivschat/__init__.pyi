"""
Main interface for ivschat service.

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_ivschat import (
        Client,
        ivschatClient,
    )

    session = get_session()
    async with session.create_client("ivschat") as client:
        client: ivschatClient
        ...

    ```
"""

from .client import ivschatClient

Client = ivschatClient

__all__ = ("Client", "ivschatClient")
