"""
Main interface for inspector-scan service.

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_inspector_scan import (
        Client,
        inspectorscanClient,
    )

    session = get_session()
    async with session.create_client("inspector-scan") as client:
        client: inspectorscanClient
        ...

    ```
"""

from .client import inspectorscanClient

Client = inspectorscanClient

__all__ = ("Client", "inspectorscanClient")
