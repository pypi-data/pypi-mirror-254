"""
Type annotations for bcm-data-exports service type definitions.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_bcm_data_exports/type_defs/)

Usage::

    ```python
    from types_aiobotocore_bcm_data_exports.type_defs import ColumnTypeDef

    data: ColumnTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from .literals import (
    CompressionOptionType,
    ExecutionStatusCodeType,
    ExecutionStatusReasonType,
    ExportStatusCodeType,
    FormatOptionType,
    OverwriteOptionType,
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
    "ColumnTypeDef",
    "ResourceTagTypeDef",
    "ResponseMetadataTypeDef",
    "DataQueryTypeDef",
    "DeleteExportRequestRequestTypeDef",
    "ExecutionStatusTypeDef",
    "ExportStatusTypeDef",
    "RefreshCadenceTypeDef",
    "GetExecutionRequestRequestTypeDef",
    "GetExportRequestRequestTypeDef",
    "GetTableRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "ListExecutionsRequestRequestTypeDef",
    "ListExportsRequestRequestTypeDef",
    "ListTablesRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "S3OutputConfigurationsTypeDef",
    "TablePropertyDescriptionTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "CreateExportResponseTypeDef",
    "DeleteExportResponseTypeDef",
    "GetTableResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "UpdateExportResponseTypeDef",
    "ExecutionReferenceTypeDef",
    "ExportReferenceTypeDef",
    "ListExecutionsRequestListExecutionsPaginateTypeDef",
    "ListExportsRequestListExportsPaginateTypeDef",
    "ListTablesRequestListTablesPaginateTypeDef",
    "S3DestinationTypeDef",
    "TableTypeDef",
    "ListExecutionsResponseTypeDef",
    "ListExportsResponseTypeDef",
    "DestinationConfigurationsTypeDef",
    "ListTablesResponseTypeDef",
    "ExportTypeDef",
    "CreateExportRequestRequestTypeDef",
    "GetExecutionResponseTypeDef",
    "GetExportResponseTypeDef",
    "UpdateExportRequestRequestTypeDef",
)

ColumnTypeDef = TypedDict(
    "ColumnTypeDef",
    {
        "Description": NotRequired[str],
        "Name": NotRequired[str],
        "Type": NotRequired[str],
    },
)
ResourceTagTypeDef = TypedDict(
    "ResourceTagTypeDef",
    {
        "Key": str,
        "Value": str,
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
DataQueryTypeDef = TypedDict(
    "DataQueryTypeDef",
    {
        "QueryStatement": str,
        "TableConfigurations": NotRequired[Mapping[str, Mapping[str, str]]],
    },
)
DeleteExportRequestRequestTypeDef = TypedDict(
    "DeleteExportRequestRequestTypeDef",
    {
        "ExportArn": str,
    },
)
ExecutionStatusTypeDef = TypedDict(
    "ExecutionStatusTypeDef",
    {
        "CompletedAt": NotRequired[datetime],
        "CreatedAt": NotRequired[datetime],
        "LastUpdatedAt": NotRequired[datetime],
        "StatusCode": NotRequired[ExecutionStatusCodeType],
        "StatusReason": NotRequired[ExecutionStatusReasonType],
    },
)
ExportStatusTypeDef = TypedDict(
    "ExportStatusTypeDef",
    {
        "CreatedAt": NotRequired[datetime],
        "LastRefreshedAt": NotRequired[datetime],
        "LastUpdatedAt": NotRequired[datetime],
        "StatusCode": NotRequired[ExportStatusCodeType],
        "StatusReason": NotRequired[ExecutionStatusReasonType],
    },
)
RefreshCadenceTypeDef = TypedDict(
    "RefreshCadenceTypeDef",
    {
        "Frequency": Literal["SYNCHRONOUS"],
    },
)
GetExecutionRequestRequestTypeDef = TypedDict(
    "GetExecutionRequestRequestTypeDef",
    {
        "ExecutionId": str,
        "ExportArn": str,
    },
)
GetExportRequestRequestTypeDef = TypedDict(
    "GetExportRequestRequestTypeDef",
    {
        "ExportArn": str,
    },
)
GetTableRequestRequestTypeDef = TypedDict(
    "GetTableRequestRequestTypeDef",
    {
        "TableName": str,
        "TableProperties": NotRequired[Mapping[str, str]],
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
ListExecutionsRequestRequestTypeDef = TypedDict(
    "ListExecutionsRequestRequestTypeDef",
    {
        "ExportArn": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListExportsRequestRequestTypeDef = TypedDict(
    "ListExportsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListTablesRequestRequestTypeDef = TypedDict(
    "ListTablesRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
S3OutputConfigurationsTypeDef = TypedDict(
    "S3OutputConfigurationsTypeDef",
    {
        "Compression": CompressionOptionType,
        "Format": FormatOptionType,
        "OutputType": Literal["CUSTOM"],
        "Overwrite": OverwriteOptionType,
    },
)
TablePropertyDescriptionTypeDef = TypedDict(
    "TablePropertyDescriptionTypeDef",
    {
        "DefaultValue": NotRequired[str],
        "Description": NotRequired[str],
        "Name": NotRequired[str],
        "ValidValues": NotRequired[List[str]],
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "ResourceTagKeys": Sequence[str],
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "ResourceTags": Sequence[ResourceTagTypeDef],
    },
)
CreateExportResponseTypeDef = TypedDict(
    "CreateExportResponseTypeDef",
    {
        "ExportArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteExportResponseTypeDef = TypedDict(
    "DeleteExportResponseTypeDef",
    {
        "ExportArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetTableResponseTypeDef = TypedDict(
    "GetTableResponseTypeDef",
    {
        "Description": str,
        "Schema": List[ColumnTypeDef],
        "TableName": str,
        "TableProperties": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "NextToken": str,
        "ResourceTags": List[ResourceTagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateExportResponseTypeDef = TypedDict(
    "UpdateExportResponseTypeDef",
    {
        "ExportArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ExecutionReferenceTypeDef = TypedDict(
    "ExecutionReferenceTypeDef",
    {
        "ExecutionId": str,
        "ExecutionStatus": ExecutionStatusTypeDef,
    },
)
ExportReferenceTypeDef = TypedDict(
    "ExportReferenceTypeDef",
    {
        "ExportArn": str,
        "ExportName": str,
        "ExportStatus": ExportStatusTypeDef,
    },
)
ListExecutionsRequestListExecutionsPaginateTypeDef = TypedDict(
    "ListExecutionsRequestListExecutionsPaginateTypeDef",
    {
        "ExportArn": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListExportsRequestListExportsPaginateTypeDef = TypedDict(
    "ListExportsRequestListExportsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListTablesRequestListTablesPaginateTypeDef = TypedDict(
    "ListTablesRequestListTablesPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
S3DestinationTypeDef = TypedDict(
    "S3DestinationTypeDef",
    {
        "S3Bucket": str,
        "S3OutputConfigurations": S3OutputConfigurationsTypeDef,
        "S3Prefix": str,
        "S3Region": str,
    },
)
TableTypeDef = TypedDict(
    "TableTypeDef",
    {
        "Description": NotRequired[str],
        "TableName": NotRequired[str],
        "TableProperties": NotRequired[List[TablePropertyDescriptionTypeDef]],
    },
)
ListExecutionsResponseTypeDef = TypedDict(
    "ListExecutionsResponseTypeDef",
    {
        "Executions": List[ExecutionReferenceTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListExportsResponseTypeDef = TypedDict(
    "ListExportsResponseTypeDef",
    {
        "Exports": List[ExportReferenceTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DestinationConfigurationsTypeDef = TypedDict(
    "DestinationConfigurationsTypeDef",
    {
        "S3Destination": S3DestinationTypeDef,
    },
)
ListTablesResponseTypeDef = TypedDict(
    "ListTablesResponseTypeDef",
    {
        "NextToken": str,
        "Tables": List[TableTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ExportTypeDef = TypedDict(
    "ExportTypeDef",
    {
        "DataQuery": DataQueryTypeDef,
        "DestinationConfigurations": DestinationConfigurationsTypeDef,
        "Name": str,
        "RefreshCadence": RefreshCadenceTypeDef,
        "Description": NotRequired[str],
        "ExportArn": NotRequired[str],
    },
)
CreateExportRequestRequestTypeDef = TypedDict(
    "CreateExportRequestRequestTypeDef",
    {
        "Export": ExportTypeDef,
        "ResourceTags": NotRequired[Sequence[ResourceTagTypeDef]],
    },
)
GetExecutionResponseTypeDef = TypedDict(
    "GetExecutionResponseTypeDef",
    {
        "ExecutionId": str,
        "ExecutionStatus": ExecutionStatusTypeDef,
        "Export": ExportTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetExportResponseTypeDef = TypedDict(
    "GetExportResponseTypeDef",
    {
        "Export": ExportTypeDef,
        "ExportStatus": ExportStatusTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateExportRequestRequestTypeDef = TypedDict(
    "UpdateExportRequestRequestTypeDef",
    {
        "Export": ExportTypeDef,
        "ExportArn": str,
    },
)
