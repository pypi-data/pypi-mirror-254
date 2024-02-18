"""
Main interface for managedblockchain-query service.

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_managedblockchain_query import (
        Client,
        ListAssetContractsPaginator,
        ListTokenBalancesPaginator,
        ListTransactionEventsPaginator,
        ListTransactionsPaginator,
        ManagedBlockchainQueryClient,
    )

    session = get_session()
    async with session.create_client("managedblockchain-query") as client:
        client: ManagedBlockchainQueryClient
        ...


    list_asset_contracts_paginator: ListAssetContractsPaginator = client.get_paginator("list_asset_contracts")
    list_token_balances_paginator: ListTokenBalancesPaginator = client.get_paginator("list_token_balances")
    list_transaction_events_paginator: ListTransactionEventsPaginator = client.get_paginator("list_transaction_events")
    list_transactions_paginator: ListTransactionsPaginator = client.get_paginator("list_transactions")
    ```
"""

from .client import ManagedBlockchainQueryClient
from .paginator import (
    ListAssetContractsPaginator,
    ListTokenBalancesPaginator,
    ListTransactionEventsPaginator,
    ListTransactionsPaginator,
)

Client = ManagedBlockchainQueryClient

__all__ = (
    "Client",
    "ListAssetContractsPaginator",
    "ListTokenBalancesPaginator",
    "ListTransactionEventsPaginator",
    "ListTransactionsPaginator",
    "ManagedBlockchainQueryClient",
)
