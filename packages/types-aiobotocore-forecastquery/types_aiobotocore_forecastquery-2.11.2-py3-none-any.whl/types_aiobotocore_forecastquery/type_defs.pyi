"""
Type annotations for forecastquery service type definitions.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecastquery/type_defs/)

Usage::

    ```python
    from types_aiobotocore_forecastquery.type_defs import DataPointTypeDef

    data: DataPointTypeDef = ...
    ```
"""

import sys
from typing import Dict, List, Mapping

if sys.version_info >= (3, 12):
    from typing import NotRequired
else:
    from typing_extensions import NotRequired
if sys.version_info >= (3, 12):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "DataPointTypeDef",
    "QueryForecastRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "QueryWhatIfForecastRequestRequestTypeDef",
    "ForecastTypeDef",
    "QueryForecastResponseTypeDef",
    "QueryWhatIfForecastResponseTypeDef",
)

DataPointTypeDef = TypedDict(
    "DataPointTypeDef",
    {
        "Timestamp": NotRequired[str],
        "Value": NotRequired[float],
    },
)
QueryForecastRequestRequestTypeDef = TypedDict(
    "QueryForecastRequestRequestTypeDef",
    {
        "ForecastArn": str,
        "Filters": Mapping[str, str],
        "StartDate": NotRequired[str],
        "EndDate": NotRequired[str],
        "NextToken": NotRequired[str],
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
QueryWhatIfForecastRequestRequestTypeDef = TypedDict(
    "QueryWhatIfForecastRequestRequestTypeDef",
    {
        "WhatIfForecastArn": str,
        "Filters": Mapping[str, str],
        "StartDate": NotRequired[str],
        "EndDate": NotRequired[str],
        "NextToken": NotRequired[str],
    },
)
ForecastTypeDef = TypedDict(
    "ForecastTypeDef",
    {
        "Predictions": NotRequired[Dict[str, List[DataPointTypeDef]]],
    },
)
QueryForecastResponseTypeDef = TypedDict(
    "QueryForecastResponseTypeDef",
    {
        "Forecast": ForecastTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
QueryWhatIfForecastResponseTypeDef = TypedDict(
    "QueryWhatIfForecastResponseTypeDef",
    {
        "Forecast": ForecastTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
