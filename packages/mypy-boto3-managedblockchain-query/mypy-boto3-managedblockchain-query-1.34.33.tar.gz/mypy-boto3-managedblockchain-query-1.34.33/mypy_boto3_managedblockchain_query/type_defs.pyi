"""
Type annotations for managedblockchain-query service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain_query/type_defs/)

Usage::

    ```python
    from mypy_boto3_managedblockchain_query.type_defs import ContractIdentifierTypeDef

    data: ContractIdentifierTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Sequence, Union

from .literals import (
    ConfirmationStatusType,
    ErrorTypeType,
    ExecutionStatusType,
    QueryNetworkType,
    QueryTokenStandardType,
    QueryTransactionEventTypeType,
    SortOrderType,
)

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 12):
    from typing import NotRequired
else:
    from typing_extensions import NotRequired
if sys.version_info >= (3, 12):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "ContractIdentifierTypeDef",
    "OwnerIdentifierTypeDef",
    "TokenIdentifierTypeDef",
    "ResponseMetadataTypeDef",
    "BlockchainInstantPaginatorTypeDef",
    "TimestampTypeDef",
    "ConfirmationStatusFilterTypeDef",
    "ContractFilterTypeDef",
    "ContractMetadataTypeDef",
    "GetTransactionInputRequestTypeDef",
    "TransactionTypeDef",
    "PaginatorConfigTypeDef",
    "OwnerFilterTypeDef",
    "TokenFilterTypeDef",
    "ListTransactionEventsInputRequestTypeDef",
    "TransactionEventTypeDef",
    "ListTransactionsSortTypeDef",
    "TransactionOutputItemTypeDef",
    "AssetContractTypeDef",
    "GetAssetContractInputRequestTypeDef",
    "TokenBalancePaginatorTypeDef",
    "BlockchainInstantTypeDef",
    "ListAssetContractsInputRequestTypeDef",
    "GetAssetContractOutputTypeDef",
    "GetTransactionOutputTypeDef",
    "ListAssetContractsInputListAssetContractsPaginateTypeDef",
    "ListTransactionEventsInputListTransactionEventsPaginateTypeDef",
    "ListTokenBalancesInputListTokenBalancesPaginateTypeDef",
    "ListTokenBalancesInputRequestTypeDef",
    "ListTransactionEventsOutputTypeDef",
    "ListTransactionsInputListTransactionsPaginateTypeDef",
    "ListTransactionsOutputTypeDef",
    "ListAssetContractsOutputTypeDef",
    "ListTokenBalancesOutputPaginatorTypeDef",
    "BatchGetTokenBalanceErrorItemTypeDef",
    "BatchGetTokenBalanceInputItemTypeDef",
    "BatchGetTokenBalanceOutputItemTypeDef",
    "GetTokenBalanceInputRequestTypeDef",
    "GetTokenBalanceOutputTypeDef",
    "ListTransactionsInputRequestTypeDef",
    "TokenBalanceTypeDef",
    "BatchGetTokenBalanceInputRequestTypeDef",
    "BatchGetTokenBalanceOutputTypeDef",
    "ListTokenBalancesOutputTypeDef",
)

ContractIdentifierTypeDef = TypedDict(
    "ContractIdentifierTypeDef",
    {
        "network": QueryNetworkType,
        "contractAddress": str,
    },
)
OwnerIdentifierTypeDef = TypedDict(
    "OwnerIdentifierTypeDef",
    {
        "address": str,
    },
)
TokenIdentifierTypeDef = TypedDict(
    "TokenIdentifierTypeDef",
    {
        "network": QueryNetworkType,
        "contractAddress": NotRequired[str],
        "tokenId": NotRequired[str],
    },
)
ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, str],
        "RetryAttempts": int,
    },
)
BlockchainInstantPaginatorTypeDef = TypedDict(
    "BlockchainInstantPaginatorTypeDef",
    {
        "time": NotRequired[datetime],
    },
)
TimestampTypeDef = Union[datetime, str]
ConfirmationStatusFilterTypeDef = TypedDict(
    "ConfirmationStatusFilterTypeDef",
    {
        "include": Sequence[ConfirmationStatusType],
    },
)
ContractFilterTypeDef = TypedDict(
    "ContractFilterTypeDef",
    {
        "network": QueryNetworkType,
        "tokenStandard": QueryTokenStandardType,
        "deployerAddress": str,
    },
)
ContractMetadataTypeDef = TypedDict(
    "ContractMetadataTypeDef",
    {
        "name": NotRequired[str],
        "symbol": NotRequired[str],
        "decimals": NotRequired[int],
    },
)
GetTransactionInputRequestTypeDef = TypedDict(
    "GetTransactionInputRequestTypeDef",
    {
        "transactionHash": str,
        "network": QueryNetworkType,
    },
)
TransactionTypeDef = TypedDict(
    "TransactionTypeDef",
    {
        "network": QueryNetworkType,
        "transactionHash": str,
        "transactionTimestamp": datetime,
        "transactionIndex": int,
        "numberOfTransactions": int,
        "to": str,
        "blockHash": NotRequired[str],
        "blockNumber": NotRequired[str],
        "from": NotRequired[str],
        "contractAddress": NotRequired[str],
        "gasUsed": NotRequired[str],
        "cumulativeGasUsed": NotRequired[str],
        "effectiveGasPrice": NotRequired[str],
        "signatureV": NotRequired[int],
        "signatureR": NotRequired[str],
        "signatureS": NotRequired[str],
        "transactionFee": NotRequired[str],
        "transactionId": NotRequired[str],
        "confirmationStatus": NotRequired[ConfirmationStatusType],
        "executionStatus": NotRequired[ExecutionStatusType],
    },
)
PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": NotRequired[int],
        "PageSize": NotRequired[int],
        "StartingToken": NotRequired[str],
    },
)
OwnerFilterTypeDef = TypedDict(
    "OwnerFilterTypeDef",
    {
        "address": str,
    },
)
TokenFilterTypeDef = TypedDict(
    "TokenFilterTypeDef",
    {
        "network": QueryNetworkType,
        "contractAddress": NotRequired[str],
        "tokenId": NotRequired[str],
    },
)
ListTransactionEventsInputRequestTypeDef = TypedDict(
    "ListTransactionEventsInputRequestTypeDef",
    {
        "transactionHash": str,
        "network": QueryNetworkType,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
TransactionEventTypeDef = TypedDict(
    "TransactionEventTypeDef",
    {
        "network": QueryNetworkType,
        "transactionHash": str,
        "eventType": QueryTransactionEventTypeType,
        "from": NotRequired[str],
        "to": NotRequired[str],
        "value": NotRequired[str],
        "contractAddress": NotRequired[str],
        "tokenId": NotRequired[str],
        "transactionId": NotRequired[str],
        "voutIndex": NotRequired[int],
    },
)
ListTransactionsSortTypeDef = TypedDict(
    "ListTransactionsSortTypeDef",
    {
        "sortBy": NotRequired[Literal["TRANSACTION_TIMESTAMP"]],
        "sortOrder": NotRequired[SortOrderType],
    },
)
TransactionOutputItemTypeDef = TypedDict(
    "TransactionOutputItemTypeDef",
    {
        "transactionHash": str,
        "network": QueryNetworkType,
        "transactionTimestamp": datetime,
        "confirmationStatus": NotRequired[ConfirmationStatusType],
    },
)
AssetContractTypeDef = TypedDict(
    "AssetContractTypeDef",
    {
        "contractIdentifier": ContractIdentifierTypeDef,
        "tokenStandard": QueryTokenStandardType,
        "deployerAddress": str,
    },
)
GetAssetContractInputRequestTypeDef = TypedDict(
    "GetAssetContractInputRequestTypeDef",
    {
        "contractIdentifier": ContractIdentifierTypeDef,
    },
)
TokenBalancePaginatorTypeDef = TypedDict(
    "TokenBalancePaginatorTypeDef",
    {
        "balance": str,
        "atBlockchainInstant": BlockchainInstantPaginatorTypeDef,
        "ownerIdentifier": NotRequired[OwnerIdentifierTypeDef],
        "tokenIdentifier": NotRequired[TokenIdentifierTypeDef],
        "lastUpdatedTime": NotRequired[BlockchainInstantPaginatorTypeDef],
    },
)
BlockchainInstantTypeDef = TypedDict(
    "BlockchainInstantTypeDef",
    {
        "time": NotRequired[TimestampTypeDef],
    },
)
ListAssetContractsInputRequestTypeDef = TypedDict(
    "ListAssetContractsInputRequestTypeDef",
    {
        "contractFilter": ContractFilterTypeDef,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
GetAssetContractOutputTypeDef = TypedDict(
    "GetAssetContractOutputTypeDef",
    {
        "contractIdentifier": ContractIdentifierTypeDef,
        "tokenStandard": QueryTokenStandardType,
        "deployerAddress": str,
        "metadata": ContractMetadataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetTransactionOutputTypeDef = TypedDict(
    "GetTransactionOutputTypeDef",
    {
        "transaction": TransactionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAssetContractsInputListAssetContractsPaginateTypeDef = TypedDict(
    "ListAssetContractsInputListAssetContractsPaginateTypeDef",
    {
        "contractFilter": ContractFilterTypeDef,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListTransactionEventsInputListTransactionEventsPaginateTypeDef = TypedDict(
    "ListTransactionEventsInputListTransactionEventsPaginateTypeDef",
    {
        "transactionHash": str,
        "network": QueryNetworkType,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListTokenBalancesInputListTokenBalancesPaginateTypeDef = TypedDict(
    "ListTokenBalancesInputListTokenBalancesPaginateTypeDef",
    {
        "tokenFilter": TokenFilterTypeDef,
        "ownerFilter": NotRequired[OwnerFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListTokenBalancesInputRequestTypeDef = TypedDict(
    "ListTokenBalancesInputRequestTypeDef",
    {
        "tokenFilter": TokenFilterTypeDef,
        "ownerFilter": NotRequired[OwnerFilterTypeDef],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListTransactionEventsOutputTypeDef = TypedDict(
    "ListTransactionEventsOutputTypeDef",
    {
        "events": List[TransactionEventTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTransactionsInputListTransactionsPaginateTypeDef = TypedDict(
    "ListTransactionsInputListTransactionsPaginateTypeDef",
    {
        "address": str,
        "network": QueryNetworkType,
        "fromBlockchainInstant": NotRequired[BlockchainInstantPaginatorTypeDef],
        "toBlockchainInstant": NotRequired[BlockchainInstantPaginatorTypeDef],
        "sort": NotRequired[ListTransactionsSortTypeDef],
        "confirmationStatusFilter": NotRequired[ConfirmationStatusFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListTransactionsOutputTypeDef = TypedDict(
    "ListTransactionsOutputTypeDef",
    {
        "transactions": List[TransactionOutputItemTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAssetContractsOutputTypeDef = TypedDict(
    "ListAssetContractsOutputTypeDef",
    {
        "contracts": List[AssetContractTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTokenBalancesOutputPaginatorTypeDef = TypedDict(
    "ListTokenBalancesOutputPaginatorTypeDef",
    {
        "tokenBalances": List[TokenBalancePaginatorTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchGetTokenBalanceErrorItemTypeDef = TypedDict(
    "BatchGetTokenBalanceErrorItemTypeDef",
    {
        "errorCode": str,
        "errorMessage": str,
        "errorType": ErrorTypeType,
        "tokenIdentifier": NotRequired[TokenIdentifierTypeDef],
        "ownerIdentifier": NotRequired[OwnerIdentifierTypeDef],
        "atBlockchainInstant": NotRequired[BlockchainInstantTypeDef],
    },
)
BatchGetTokenBalanceInputItemTypeDef = TypedDict(
    "BatchGetTokenBalanceInputItemTypeDef",
    {
        "tokenIdentifier": TokenIdentifierTypeDef,
        "ownerIdentifier": OwnerIdentifierTypeDef,
        "atBlockchainInstant": NotRequired[BlockchainInstantTypeDef],
    },
)
BatchGetTokenBalanceOutputItemTypeDef = TypedDict(
    "BatchGetTokenBalanceOutputItemTypeDef",
    {
        "balance": str,
        "atBlockchainInstant": BlockchainInstantTypeDef,
        "ownerIdentifier": NotRequired[OwnerIdentifierTypeDef],
        "tokenIdentifier": NotRequired[TokenIdentifierTypeDef],
        "lastUpdatedTime": NotRequired[BlockchainInstantTypeDef],
    },
)
GetTokenBalanceInputRequestTypeDef = TypedDict(
    "GetTokenBalanceInputRequestTypeDef",
    {
        "tokenIdentifier": TokenIdentifierTypeDef,
        "ownerIdentifier": OwnerIdentifierTypeDef,
        "atBlockchainInstant": NotRequired[BlockchainInstantTypeDef],
    },
)
GetTokenBalanceOutputTypeDef = TypedDict(
    "GetTokenBalanceOutputTypeDef",
    {
        "ownerIdentifier": OwnerIdentifierTypeDef,
        "tokenIdentifier": TokenIdentifierTypeDef,
        "balance": str,
        "atBlockchainInstant": BlockchainInstantTypeDef,
        "lastUpdatedTime": BlockchainInstantTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTransactionsInputRequestTypeDef = TypedDict(
    "ListTransactionsInputRequestTypeDef",
    {
        "address": str,
        "network": QueryNetworkType,
        "fromBlockchainInstant": NotRequired[BlockchainInstantTypeDef],
        "toBlockchainInstant": NotRequired[BlockchainInstantTypeDef],
        "sort": NotRequired[ListTransactionsSortTypeDef],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "confirmationStatusFilter": NotRequired[ConfirmationStatusFilterTypeDef],
    },
)
TokenBalanceTypeDef = TypedDict(
    "TokenBalanceTypeDef",
    {
        "balance": str,
        "atBlockchainInstant": BlockchainInstantTypeDef,
        "ownerIdentifier": NotRequired[OwnerIdentifierTypeDef],
        "tokenIdentifier": NotRequired[TokenIdentifierTypeDef],
        "lastUpdatedTime": NotRequired[BlockchainInstantTypeDef],
    },
)
BatchGetTokenBalanceInputRequestTypeDef = TypedDict(
    "BatchGetTokenBalanceInputRequestTypeDef",
    {
        "getTokenBalanceInputs": NotRequired[Sequence[BatchGetTokenBalanceInputItemTypeDef]],
    },
)
BatchGetTokenBalanceOutputTypeDef = TypedDict(
    "BatchGetTokenBalanceOutputTypeDef",
    {
        "tokenBalances": List[BatchGetTokenBalanceOutputItemTypeDef],
        "errors": List[BatchGetTokenBalanceErrorItemTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTokenBalancesOutputTypeDef = TypedDict(
    "ListTokenBalancesOutputTypeDef",
    {
        "tokenBalances": List[TokenBalanceTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
