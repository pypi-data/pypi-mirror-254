"""
Type annotations for sagemaker-featurestore-runtime service type definitions.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker_featurestore_runtime/type_defs/)

Usage::

    ```python
    from types_aiobotocore_sagemaker_featurestore_runtime.type_defs import BatchGetRecordErrorTypeDef

    data: BatchGetRecordErrorTypeDef = ...
    ```
"""

import sys
from typing import Dict, List, Sequence

from .literals import (
    DeletionModeType,
    ExpirationTimeResponseType,
    TargetStoreType,
    TtlDurationUnitType,
)

if sys.version_info >= (3, 12):
    from typing import NotRequired
else:
    from typing_extensions import NotRequired
if sys.version_info >= (3, 12):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "BatchGetRecordErrorTypeDef",
    "BatchGetRecordIdentifierTypeDef",
    "ResponseMetadataTypeDef",
    "FeatureValueTypeDef",
    "DeleteRecordRequestRequestTypeDef",
    "GetRecordRequestRequestTypeDef",
    "TtlDurationTypeDef",
    "BatchGetRecordRequestRequestTypeDef",
    "EmptyResponseMetadataTypeDef",
    "BatchGetRecordResultDetailTypeDef",
    "GetRecordResponseTypeDef",
    "PutRecordRequestRequestTypeDef",
    "BatchGetRecordResponseTypeDef",
)

BatchGetRecordErrorTypeDef = TypedDict(
    "BatchGetRecordErrorTypeDef",
    {
        "FeatureGroupName": str,
        "RecordIdentifierValueAsString": str,
        "ErrorCode": str,
        "ErrorMessage": str,
    },
)
BatchGetRecordIdentifierTypeDef = TypedDict(
    "BatchGetRecordIdentifierTypeDef",
    {
        "FeatureGroupName": str,
        "RecordIdentifiersValueAsString": Sequence[str],
        "FeatureNames": NotRequired[Sequence[str]],
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
FeatureValueTypeDef = TypedDict(
    "FeatureValueTypeDef",
    {
        "FeatureName": str,
        "ValueAsString": NotRequired[str],
        "ValueAsStringList": NotRequired[List[str]],
    },
)
DeleteRecordRequestRequestTypeDef = TypedDict(
    "DeleteRecordRequestRequestTypeDef",
    {
        "FeatureGroupName": str,
        "RecordIdentifierValueAsString": str,
        "EventTime": str,
        "TargetStores": NotRequired[Sequence[TargetStoreType]],
        "DeletionMode": NotRequired[DeletionModeType],
    },
)
GetRecordRequestRequestTypeDef = TypedDict(
    "GetRecordRequestRequestTypeDef",
    {
        "FeatureGroupName": str,
        "RecordIdentifierValueAsString": str,
        "FeatureNames": NotRequired[Sequence[str]],
        "ExpirationTimeResponse": NotRequired[ExpirationTimeResponseType],
    },
)
TtlDurationTypeDef = TypedDict(
    "TtlDurationTypeDef",
    {
        "Unit": TtlDurationUnitType,
        "Value": int,
    },
)
BatchGetRecordRequestRequestTypeDef = TypedDict(
    "BatchGetRecordRequestRequestTypeDef",
    {
        "Identifiers": Sequence[BatchGetRecordIdentifierTypeDef],
        "ExpirationTimeResponse": NotRequired[ExpirationTimeResponseType],
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchGetRecordResultDetailTypeDef = TypedDict(
    "BatchGetRecordResultDetailTypeDef",
    {
        "FeatureGroupName": str,
        "RecordIdentifierValueAsString": str,
        "Record": List[FeatureValueTypeDef],
        "ExpiresAt": NotRequired[str],
    },
)
GetRecordResponseTypeDef = TypedDict(
    "GetRecordResponseTypeDef",
    {
        "Record": List[FeatureValueTypeDef],
        "ExpiresAt": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutRecordRequestRequestTypeDef = TypedDict(
    "PutRecordRequestRequestTypeDef",
    {
        "FeatureGroupName": str,
        "Record": Sequence[FeatureValueTypeDef],
        "TargetStores": NotRequired[Sequence[TargetStoreType]],
        "TtlDuration": NotRequired[TtlDurationTypeDef],
    },
)
BatchGetRecordResponseTypeDef = TypedDict(
    "BatchGetRecordResponseTypeDef",
    {
        "Records": List[BatchGetRecordResultDetailTypeDef],
        "Errors": List[BatchGetRecordErrorTypeDef],
        "UnprocessedIdentifiers": List[BatchGetRecordIdentifierTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
