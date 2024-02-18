"""
Main interface for supplychain service.

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_supplychain import (
        Client,
        SupplyChainClient,
    )

    session = get_session()
    async with session.create_client("supplychain") as client:
        client: SupplyChainClient
        ...

    ```
"""

from .client import SupplyChainClient

Client = SupplyChainClient

__all__ = ("Client", "SupplyChainClient")
