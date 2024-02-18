"""
Type annotations for cloudsearchdomain service type definitions.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudsearchdomain/type_defs/)

Usage::

    ```python
    from types_aiobotocore_cloudsearchdomain.type_defs import BlobTypeDef

    data: BlobTypeDef = ...
    ```
"""

import sys
from typing import IO, Any, Dict, List, Union

from aiobotocore.response import StreamingBody

from .literals import ContentTypeType, QueryParserType

if sys.version_info >= (3, 12):
    from typing import NotRequired
else:
    from typing_extensions import NotRequired
if sys.version_info >= (3, 12):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "BlobTypeDef",
    "BucketTypeDef",
    "DocumentServiceWarningTypeDef",
    "FieldStatsTypeDef",
    "HitTypeDef",
    "ResponseMetadataTypeDef",
    "SearchRequestRequestTypeDef",
    "SearchStatusTypeDef",
    "SuggestionMatchTypeDef",
    "SuggestRequestRequestTypeDef",
    "SuggestStatusTypeDef",
    "UploadDocumentsRequestRequestTypeDef",
    "BucketInfoTypeDef",
    "HitsTypeDef",
    "UploadDocumentsResponseTypeDef",
    "SuggestModelTypeDef",
    "SearchResponseTypeDef",
    "SuggestResponseTypeDef",
)

BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]
BucketTypeDef = TypedDict(
    "BucketTypeDef",
    {
        "value": NotRequired[str],
        "count": NotRequired[int],
    },
)
DocumentServiceWarningTypeDef = TypedDict(
    "DocumentServiceWarningTypeDef",
    {
        "message": NotRequired[str],
    },
)
FieldStatsTypeDef = TypedDict(
    "FieldStatsTypeDef",
    {
        "min": NotRequired[str],
        "max": NotRequired[str],
        "count": NotRequired[int],
        "missing": NotRequired[int],
        "sum": NotRequired[float],
        "sumOfSquares": NotRequired[float],
        "mean": NotRequired[str],
        "stddev": NotRequired[float],
    },
)
HitTypeDef = TypedDict(
    "HitTypeDef",
    {
        "id": NotRequired[str],
        "fields": NotRequired[Dict[str, List[str]]],
        "exprs": NotRequired[Dict[str, str]],
        "highlights": NotRequired[Dict[str, str]],
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
SearchRequestRequestTypeDef = TypedDict(
    "SearchRequestRequestTypeDef",
    {
        "query": str,
        "cursor": NotRequired[str],
        "expr": NotRequired[str],
        "facet": NotRequired[str],
        "filterQuery": NotRequired[str],
        "highlight": NotRequired[str],
        "partial": NotRequired[bool],
        "queryOptions": NotRequired[str],
        "queryParser": NotRequired[QueryParserType],
        "returnFields": NotRequired[str],
        "size": NotRequired[int],
        "sort": NotRequired[str],
        "start": NotRequired[int],
        "stats": NotRequired[str],
    },
)
SearchStatusTypeDef = TypedDict(
    "SearchStatusTypeDef",
    {
        "timems": NotRequired[int],
        "rid": NotRequired[str],
    },
)
SuggestionMatchTypeDef = TypedDict(
    "SuggestionMatchTypeDef",
    {
        "suggestion": NotRequired[str],
        "score": NotRequired[int],
        "id": NotRequired[str],
    },
)
SuggestRequestRequestTypeDef = TypedDict(
    "SuggestRequestRequestTypeDef",
    {
        "query": str,
        "suggester": str,
        "size": NotRequired[int],
    },
)
SuggestStatusTypeDef = TypedDict(
    "SuggestStatusTypeDef",
    {
        "timems": NotRequired[int],
        "rid": NotRequired[str],
    },
)
UploadDocumentsRequestRequestTypeDef = TypedDict(
    "UploadDocumentsRequestRequestTypeDef",
    {
        "documents": BlobTypeDef,
        "contentType": ContentTypeType,
    },
)
BucketInfoTypeDef = TypedDict(
    "BucketInfoTypeDef",
    {
        "buckets": NotRequired[List[BucketTypeDef]],
    },
)
HitsTypeDef = TypedDict(
    "HitsTypeDef",
    {
        "found": NotRequired[int],
        "start": NotRequired[int],
        "cursor": NotRequired[str],
        "hit": NotRequired[List[HitTypeDef]],
    },
)
UploadDocumentsResponseTypeDef = TypedDict(
    "UploadDocumentsResponseTypeDef",
    {
        "status": str,
        "adds": int,
        "deletes": int,
        "warnings": List[DocumentServiceWarningTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SuggestModelTypeDef = TypedDict(
    "SuggestModelTypeDef",
    {
        "query": NotRequired[str],
        "found": NotRequired[int],
        "suggestions": NotRequired[List[SuggestionMatchTypeDef]],
    },
)
SearchResponseTypeDef = TypedDict(
    "SearchResponseTypeDef",
    {
        "status": SearchStatusTypeDef,
        "hits": HitsTypeDef,
        "facets": Dict[str, BucketInfoTypeDef],
        "stats": Dict[str, FieldStatsTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SuggestResponseTypeDef = TypedDict(
    "SuggestResponseTypeDef",
    {
        "status": SuggestStatusTypeDef,
        "suggest": SuggestModelTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
