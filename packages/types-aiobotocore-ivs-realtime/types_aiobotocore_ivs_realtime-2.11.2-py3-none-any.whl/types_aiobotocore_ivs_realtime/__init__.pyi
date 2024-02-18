"""
Main interface for ivs-realtime service.

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_ivs_realtime import (
        Client,
        ivsrealtimeClient,
    )

    session = get_session()
    async with session.create_client("ivs-realtime") as client:
        client: ivsrealtimeClient
        ...

    ```
"""

from .client import ivsrealtimeClient

Client = ivsrealtimeClient

__all__ = ("Client", "ivsrealtimeClient")
