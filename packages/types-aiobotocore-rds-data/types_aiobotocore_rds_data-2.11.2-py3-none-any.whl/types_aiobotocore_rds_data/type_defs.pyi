"""
Type annotations for rds-data service type definitions.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rds_data/type_defs/)

Usage::

    ```python
    from types_aiobotocore_rds_data.type_defs import ArrayValueTypeDef

    data: ArrayValueTypeDef = ...
    ```
"""

import sys
from typing import IO, Any, Dict, List, Sequence, Union

from aiobotocore.response import StreamingBody

from .literals import DecimalReturnTypeType, LongReturnTypeType, RecordsFormatTypeType, TypeHintType

if sys.version_info >= (3, 12):
    from typing import NotRequired
else:
    from typing_extensions import NotRequired
if sys.version_info >= (3, 12):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "ArrayValueTypeDef",
    "ResponseMetadataTypeDef",
    "BeginTransactionRequestRequestTypeDef",
    "BlobTypeDef",
    "ColumnMetadataTypeDef",
    "CommitTransactionRequestRequestTypeDef",
    "ExecuteSqlRequestRequestTypeDef",
    "ResultSetOptionsTypeDef",
    "RecordTypeDef",
    "RollbackTransactionRequestRequestTypeDef",
    "StructValueTypeDef",
    "ValueTypeDef",
    "BeginTransactionResponseTypeDef",
    "CommitTransactionResponseTypeDef",
    "RollbackTransactionResponseTypeDef",
    "FieldTypeDef",
    "ResultSetMetadataTypeDef",
    "ExecuteStatementResponseTypeDef",
    "SqlParameterTypeDef",
    "UpdateResultTypeDef",
    "ResultFrameTypeDef",
    "BatchExecuteStatementRequestRequestTypeDef",
    "ExecuteStatementRequestRequestTypeDef",
    "BatchExecuteStatementResponseTypeDef",
    "SqlStatementResultTypeDef",
    "ExecuteSqlResponseTypeDef",
)

ArrayValueTypeDef = TypedDict(
    "ArrayValueTypeDef",
    {
        "booleanValues": NotRequired[Sequence[bool]],
        "longValues": NotRequired[Sequence[int]],
        "doubleValues": NotRequired[Sequence[float]],
        "stringValues": NotRequired[Sequence[str]],
        "arrayValues": NotRequired[Sequence[Dict[str, Any]]],
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
BeginTransactionRequestRequestTypeDef = TypedDict(
    "BeginTransactionRequestRequestTypeDef",
    {
        "resourceArn": str,
        "secretArn": str,
        "database": NotRequired[str],
        "schema": NotRequired[str],
    },
)
BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]
ColumnMetadataTypeDef = TypedDict(
    "ColumnMetadataTypeDef",
    {
        "name": NotRequired[str],
        "type": NotRequired[int],
        "typeName": NotRequired[str],
        "label": NotRequired[str],
        "schemaName": NotRequired[str],
        "tableName": NotRequired[str],
        "isAutoIncrement": NotRequired[bool],
        "isSigned": NotRequired[bool],
        "isCurrency": NotRequired[bool],
        "isCaseSensitive": NotRequired[bool],
        "nullable": NotRequired[int],
        "precision": NotRequired[int],
        "scale": NotRequired[int],
        "arrayBaseColumnType": NotRequired[int],
    },
)
CommitTransactionRequestRequestTypeDef = TypedDict(
    "CommitTransactionRequestRequestTypeDef",
    {
        "resourceArn": str,
        "secretArn": str,
        "transactionId": str,
    },
)
ExecuteSqlRequestRequestTypeDef = TypedDict(
    "ExecuteSqlRequestRequestTypeDef",
    {
        "dbClusterOrInstanceArn": str,
        "awsSecretStoreArn": str,
        "sqlStatements": str,
        "database": NotRequired[str],
        "schema": NotRequired[str],
    },
)
ResultSetOptionsTypeDef = TypedDict(
    "ResultSetOptionsTypeDef",
    {
        "decimalReturnType": NotRequired[DecimalReturnTypeType],
        "longReturnType": NotRequired[LongReturnTypeType],
    },
)
RecordTypeDef = TypedDict(
    "RecordTypeDef",
    {
        "values": NotRequired[List["ValueTypeDef"]],
    },
)
RollbackTransactionRequestRequestTypeDef = TypedDict(
    "RollbackTransactionRequestRequestTypeDef",
    {
        "resourceArn": str,
        "secretArn": str,
        "transactionId": str,
    },
)
StructValueTypeDef = TypedDict(
    "StructValueTypeDef",
    {
        "attributes": NotRequired[List["ValueTypeDef"]],
    },
)
ValueTypeDef = TypedDict(
    "ValueTypeDef",
    {
        "isNull": NotRequired[bool],
        "bitValue": NotRequired[bool],
        "bigIntValue": NotRequired[int],
        "intValue": NotRequired[int],
        "doubleValue": NotRequired[float],
        "realValue": NotRequired[float],
        "stringValue": NotRequired[str],
        "blobValue": NotRequired[bytes],
        "arrayValues": NotRequired[List[Dict[str, Any]]],
        "structValue": NotRequired[Dict[str, Any]],
    },
)
BeginTransactionResponseTypeDef = TypedDict(
    "BeginTransactionResponseTypeDef",
    {
        "transactionId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CommitTransactionResponseTypeDef = TypedDict(
    "CommitTransactionResponseTypeDef",
    {
        "transactionStatus": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RollbackTransactionResponseTypeDef = TypedDict(
    "RollbackTransactionResponseTypeDef",
    {
        "transactionStatus": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
FieldTypeDef = TypedDict(
    "FieldTypeDef",
    {
        "isNull": NotRequired[bool],
        "booleanValue": NotRequired[bool],
        "longValue": NotRequired[int],
        "doubleValue": NotRequired[float],
        "stringValue": NotRequired[str],
        "blobValue": NotRequired[BlobTypeDef],
        "arrayValue": NotRequired["ArrayValueTypeDef"],
    },
)
ResultSetMetadataTypeDef = TypedDict(
    "ResultSetMetadataTypeDef",
    {
        "columnCount": NotRequired[int],
        "columnMetadata": NotRequired[List[ColumnMetadataTypeDef]],
    },
)
ExecuteStatementResponseTypeDef = TypedDict(
    "ExecuteStatementResponseTypeDef",
    {
        "records": List[List[FieldTypeDef]],
        "columnMetadata": List[ColumnMetadataTypeDef],
        "numberOfRecordsUpdated": int,
        "generatedFields": List[FieldTypeDef],
        "formattedRecords": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SqlParameterTypeDef = TypedDict(
    "SqlParameterTypeDef",
    {
        "name": NotRequired[str],
        "value": NotRequired[FieldTypeDef],
        "typeHint": NotRequired[TypeHintType],
    },
)
UpdateResultTypeDef = TypedDict(
    "UpdateResultTypeDef",
    {
        "generatedFields": NotRequired[List[FieldTypeDef]],
    },
)
ResultFrameTypeDef = TypedDict(
    "ResultFrameTypeDef",
    {
        "resultSetMetadata": NotRequired[ResultSetMetadataTypeDef],
        "records": NotRequired[List[RecordTypeDef]],
    },
)
BatchExecuteStatementRequestRequestTypeDef = TypedDict(
    "BatchExecuteStatementRequestRequestTypeDef",
    {
        "resourceArn": str,
        "secretArn": str,
        "sql": str,
        "database": NotRequired[str],
        "schema": NotRequired[str],
        "parameterSets": NotRequired[Sequence[Sequence[SqlParameterTypeDef]]],
        "transactionId": NotRequired[str],
    },
)
ExecuteStatementRequestRequestTypeDef = TypedDict(
    "ExecuteStatementRequestRequestTypeDef",
    {
        "resourceArn": str,
        "secretArn": str,
        "sql": str,
        "database": NotRequired[str],
        "schema": NotRequired[str],
        "parameters": NotRequired[Sequence[SqlParameterTypeDef]],
        "transactionId": NotRequired[str],
        "includeResultMetadata": NotRequired[bool],
        "continueAfterTimeout": NotRequired[bool],
        "resultSetOptions": NotRequired[ResultSetOptionsTypeDef],
        "formatRecordsAs": NotRequired[RecordsFormatTypeType],
    },
)
BatchExecuteStatementResponseTypeDef = TypedDict(
    "BatchExecuteStatementResponseTypeDef",
    {
        "updateResults": List[UpdateResultTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SqlStatementResultTypeDef = TypedDict(
    "SqlStatementResultTypeDef",
    {
        "resultFrame": NotRequired[ResultFrameTypeDef],
        "numberOfRecordsUpdated": NotRequired[int],
    },
)
ExecuteSqlResponseTypeDef = TypedDict(
    "ExecuteSqlResponseTypeDef",
    {
        "sqlStatementResults": List[SqlStatementResultTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
