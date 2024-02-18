"""
Type annotations for freetier service type definitions.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_freetier/type_defs/)

Usage::

    ```python
    from types_aiobotocore_freetier.type_defs import DimensionValuesTypeDef

    data: DimensionValuesTypeDef = ...
    ```
"""

import sys
from typing import Any, Dict, List, Sequence

from .literals import DimensionType, MatchOptionType

if sys.version_info >= (3, 12):
    from typing import NotRequired
else:
    from typing_extensions import NotRequired
if sys.version_info >= (3, 12):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "DimensionValuesTypeDef",
    "FreeTierUsageTypeDef",
    "PaginatorConfigTypeDef",
    "GetFreeTierUsageRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "ExpressionTypeDef",
    "GetFreeTierUsageResponseTypeDef",
    "GetFreeTierUsageRequestGetFreeTierUsagePaginateTypeDef",
)

DimensionValuesTypeDef = TypedDict(
    "DimensionValuesTypeDef",
    {
        "Key": DimensionType,
        "MatchOptions": Sequence[MatchOptionType],
        "Values": Sequence[str],
    },
)
FreeTierUsageTypeDef = TypedDict(
    "FreeTierUsageTypeDef",
    {
        "actualUsageAmount": NotRequired[float],
        "description": NotRequired[str],
        "forecastedUsageAmount": NotRequired[float],
        "freeTierType": NotRequired[str],
        "limit": NotRequired[float],
        "operation": NotRequired[str],
        "region": NotRequired[str],
        "service": NotRequired[str],
        "unit": NotRequired[str],
        "usageType": NotRequired[str],
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
GetFreeTierUsageRequestRequestTypeDef = TypedDict(
    "GetFreeTierUsageRequestRequestTypeDef",
    {
        "filter": NotRequired["ExpressionTypeDef"],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
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
ExpressionTypeDef = TypedDict(
    "ExpressionTypeDef",
    {
        "And": NotRequired[Sequence[Dict[str, Any]]],
        "Dimensions": NotRequired[DimensionValuesTypeDef],
        "Not": NotRequired[Dict[str, Any]],
        "Or": NotRequired[Sequence[Dict[str, Any]]],
    },
)
GetFreeTierUsageResponseTypeDef = TypedDict(
    "GetFreeTierUsageResponseTypeDef",
    {
        "freeTierUsages": List[FreeTierUsageTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetFreeTierUsageRequestGetFreeTierUsagePaginateTypeDef = TypedDict(
    "GetFreeTierUsageRequestGetFreeTierUsagePaginateTypeDef",
    {
        "filter": NotRequired[ExpressionTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
