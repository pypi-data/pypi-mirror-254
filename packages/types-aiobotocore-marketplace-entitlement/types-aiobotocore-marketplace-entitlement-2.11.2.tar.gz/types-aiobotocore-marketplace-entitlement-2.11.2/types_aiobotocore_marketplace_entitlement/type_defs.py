"""
Type annotations for marketplace-entitlement service type definitions.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_marketplace_entitlement/type_defs/)

Usage::

    ```python
    from types_aiobotocore_marketplace_entitlement.type_defs import EntitlementValueTypeDef

    data: EntitlementValueTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from .literals import GetEntitlementFilterNameType

if sys.version_info >= (3, 12):
    from typing import NotRequired
else:
    from typing_extensions import NotRequired
if sys.version_info >= (3, 12):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "EntitlementValueTypeDef",
    "PaginatorConfigTypeDef",
    "GetEntitlementsRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "EntitlementTypeDef",
    "GetEntitlementsRequestGetEntitlementsPaginateTypeDef",
    "GetEntitlementsResultTypeDef",
)

EntitlementValueTypeDef = TypedDict(
    "EntitlementValueTypeDef",
    {
        "IntegerValue": NotRequired[int],
        "DoubleValue": NotRequired[float],
        "BooleanValue": NotRequired[bool],
        "StringValue": NotRequired[str],
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
GetEntitlementsRequestRequestTypeDef = TypedDict(
    "GetEntitlementsRequestRequestTypeDef",
    {
        "ProductCode": str,
        "Filter": NotRequired[Mapping[GetEntitlementFilterNameType, Sequence[str]]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
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
EntitlementTypeDef = TypedDict(
    "EntitlementTypeDef",
    {
        "ProductCode": NotRequired[str],
        "Dimension": NotRequired[str],
        "CustomerIdentifier": NotRequired[str],
        "Value": NotRequired[EntitlementValueTypeDef],
        "ExpirationDate": NotRequired[datetime],
    },
)
GetEntitlementsRequestGetEntitlementsPaginateTypeDef = TypedDict(
    "GetEntitlementsRequestGetEntitlementsPaginateTypeDef",
    {
        "ProductCode": str,
        "Filter": NotRequired[Mapping[GetEntitlementFilterNameType, Sequence[str]]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetEntitlementsResultTypeDef = TypedDict(
    "GetEntitlementsResultTypeDef",
    {
        "Entitlements": List[EntitlementTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
