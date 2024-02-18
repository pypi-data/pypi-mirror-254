"""
Type annotations for managedblockchain-query service client paginators.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_managedblockchain_query/paginators/)

Usage::

    ```python
    from aiobotocore.session import get_session

    from types_aiobotocore_managedblockchain_query.client import ManagedBlockchainQueryClient
    from types_aiobotocore_managedblockchain_query.paginator import (
        ListAssetContractsPaginator,
        ListTokenBalancesPaginator,
        ListTransactionEventsPaginator,
        ListTransactionsPaginator,
    )

    session = get_session()
    with session.create_client("managedblockchain-query") as client:
        client: ManagedBlockchainQueryClient

        list_asset_contracts_paginator: ListAssetContractsPaginator = client.get_paginator("list_asset_contracts")
        list_token_balances_paginator: ListTokenBalancesPaginator = client.get_paginator("list_token_balances")
        list_transaction_events_paginator: ListTransactionEventsPaginator = client.get_paginator("list_transaction_events")
        list_transactions_paginator: ListTransactionsPaginator = client.get_paginator("list_transactions")
    ```
"""

from typing import AsyncIterator, Generic, Iterator, TypeVar

from aiobotocore.paginate import AioPaginator
from botocore.paginate import PageIterator

from .literals import QueryNetworkType
from .type_defs import (
    BlockchainInstantPaginatorTypeDef,
    ConfirmationStatusFilterTypeDef,
    ContractFilterTypeDef,
    ListAssetContractsOutputTypeDef,
    ListTokenBalancesOutputPaginatorTypeDef,
    ListTransactionEventsOutputTypeDef,
    ListTransactionsOutputTypeDef,
    ListTransactionsSortTypeDef,
    OwnerFilterTypeDef,
    PaginatorConfigTypeDef,
    TokenFilterTypeDef,
)

__all__ = (
    "ListAssetContractsPaginator",
    "ListTokenBalancesPaginator",
    "ListTransactionEventsPaginator",
    "ListTransactionsPaginator",
)

_ItemTypeDef = TypeVar("_ItemTypeDef")


class _PageIterator(Generic[_ItemTypeDef], PageIterator):
    def __iter__(self) -> Iterator[_ItemTypeDef]:
        """
        Proxy method to specify iterator item type.
        """


class ListAssetContractsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/managedblockchain-query.html#ManagedBlockchainQuery.Paginator.ListAssetContracts)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_managedblockchain_query/paginators/#listassetcontractspaginator)
    """

    def paginate(
        self,
        *,
        contractFilter: ContractFilterTypeDef,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListAssetContractsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/managedblockchain-query.html#ManagedBlockchainQuery.Paginator.ListAssetContracts.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_managedblockchain_query/paginators/#listassetcontractspaginator)
        """


class ListTokenBalancesPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/managedblockchain-query.html#ManagedBlockchainQuery.Paginator.ListTokenBalances)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_managedblockchain_query/paginators/#listtokenbalancespaginator)
    """

    def paginate(
        self,
        *,
        tokenFilter: TokenFilterTypeDef,
        ownerFilter: OwnerFilterTypeDef = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListTokenBalancesOutputPaginatorTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/managedblockchain-query.html#ManagedBlockchainQuery.Paginator.ListTokenBalances.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_managedblockchain_query/paginators/#listtokenbalancespaginator)
        """


class ListTransactionEventsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/managedblockchain-query.html#ManagedBlockchainQuery.Paginator.ListTransactionEvents)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_managedblockchain_query/paginators/#listtransactioneventspaginator)
    """

    def paginate(
        self,
        *,
        transactionHash: str,
        network: QueryNetworkType,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListTransactionEventsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/managedblockchain-query.html#ManagedBlockchainQuery.Paginator.ListTransactionEvents.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_managedblockchain_query/paginators/#listtransactioneventspaginator)
        """


class ListTransactionsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/managedblockchain-query.html#ManagedBlockchainQuery.Paginator.ListTransactions)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_managedblockchain_query/paginators/#listtransactionspaginator)
    """

    def paginate(
        self,
        *,
        address: str,
        network: QueryNetworkType,
        fromBlockchainInstant: BlockchainInstantPaginatorTypeDef = ...,
        toBlockchainInstant: BlockchainInstantPaginatorTypeDef = ...,
        sort: ListTransactionsSortTypeDef = ...,
        confirmationStatusFilter: ConfirmationStatusFilterTypeDef = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListTransactionsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/managedblockchain-query.html#ManagedBlockchainQuery.Paginator.ListTransactions.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_managedblockchain_query/paginators/#listtransactionspaginator)
        """
