"""
Type annotations for account service type definitions.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_account/type_defs/)

Usage::

    ```python
    from types_aiobotocore_account.type_defs import AlternateContactTypeDef

    data: AlternateContactTypeDef = ...
    ```
"""

import sys
from typing import Dict, List, Sequence

from .literals import AlternateContactTypeType, RegionOptStatusType

if sys.version_info >= (3, 12):
    from typing import NotRequired
else:
    from typing_extensions import NotRequired
if sys.version_info >= (3, 12):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AlternateContactTypeDef",
    "ContactInformationTypeDef",
    "DeleteAlternateContactRequestRequestTypeDef",
    "DisableRegionRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "EnableRegionRequestRequestTypeDef",
    "GetAlternateContactRequestRequestTypeDef",
    "GetContactInformationRequestRequestTypeDef",
    "GetRegionOptStatusRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "ListRegionsRequestRequestTypeDef",
    "RegionTypeDef",
    "PutAlternateContactRequestRequestTypeDef",
    "PutContactInformationRequestRequestTypeDef",
    "EmptyResponseMetadataTypeDef",
    "GetAlternateContactResponseTypeDef",
    "GetContactInformationResponseTypeDef",
    "GetRegionOptStatusResponseTypeDef",
    "ListRegionsRequestListRegionsPaginateTypeDef",
    "ListRegionsResponseTypeDef",
)

AlternateContactTypeDef = TypedDict(
    "AlternateContactTypeDef",
    {
        "AlternateContactType": NotRequired[AlternateContactTypeType],
        "EmailAddress": NotRequired[str],
        "Name": NotRequired[str],
        "PhoneNumber": NotRequired[str],
        "Title": NotRequired[str],
    },
)
ContactInformationTypeDef = TypedDict(
    "ContactInformationTypeDef",
    {
        "AddressLine1": str,
        "City": str,
        "CountryCode": str,
        "FullName": str,
        "PhoneNumber": str,
        "PostalCode": str,
        "AddressLine2": NotRequired[str],
        "AddressLine3": NotRequired[str],
        "CompanyName": NotRequired[str],
        "DistrictOrCounty": NotRequired[str],
        "StateOrRegion": NotRequired[str],
        "WebsiteUrl": NotRequired[str],
    },
)
DeleteAlternateContactRequestRequestTypeDef = TypedDict(
    "DeleteAlternateContactRequestRequestTypeDef",
    {
        "AlternateContactType": AlternateContactTypeType,
        "AccountId": NotRequired[str],
    },
)
DisableRegionRequestRequestTypeDef = TypedDict(
    "DisableRegionRequestRequestTypeDef",
    {
        "RegionName": str,
        "AccountId": NotRequired[str],
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
EnableRegionRequestRequestTypeDef = TypedDict(
    "EnableRegionRequestRequestTypeDef",
    {
        "RegionName": str,
        "AccountId": NotRequired[str],
    },
)
GetAlternateContactRequestRequestTypeDef = TypedDict(
    "GetAlternateContactRequestRequestTypeDef",
    {
        "AlternateContactType": AlternateContactTypeType,
        "AccountId": NotRequired[str],
    },
)
GetContactInformationRequestRequestTypeDef = TypedDict(
    "GetContactInformationRequestRequestTypeDef",
    {
        "AccountId": NotRequired[str],
    },
)
GetRegionOptStatusRequestRequestTypeDef = TypedDict(
    "GetRegionOptStatusRequestRequestTypeDef",
    {
        "RegionName": str,
        "AccountId": NotRequired[str],
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
ListRegionsRequestRequestTypeDef = TypedDict(
    "ListRegionsRequestRequestTypeDef",
    {
        "AccountId": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "RegionOptStatusContains": NotRequired[Sequence[RegionOptStatusType]],
    },
)
RegionTypeDef = TypedDict(
    "RegionTypeDef",
    {
        "RegionName": NotRequired[str],
        "RegionOptStatus": NotRequired[RegionOptStatusType],
    },
)
PutAlternateContactRequestRequestTypeDef = TypedDict(
    "PutAlternateContactRequestRequestTypeDef",
    {
        "AlternateContactType": AlternateContactTypeType,
        "EmailAddress": str,
        "Name": str,
        "PhoneNumber": str,
        "Title": str,
        "AccountId": NotRequired[str],
    },
)
PutContactInformationRequestRequestTypeDef = TypedDict(
    "PutContactInformationRequestRequestTypeDef",
    {
        "ContactInformation": ContactInformationTypeDef,
        "AccountId": NotRequired[str],
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAlternateContactResponseTypeDef = TypedDict(
    "GetAlternateContactResponseTypeDef",
    {
        "AlternateContact": AlternateContactTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetContactInformationResponseTypeDef = TypedDict(
    "GetContactInformationResponseTypeDef",
    {
        "ContactInformation": ContactInformationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetRegionOptStatusResponseTypeDef = TypedDict(
    "GetRegionOptStatusResponseTypeDef",
    {
        "RegionName": str,
        "RegionOptStatus": RegionOptStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListRegionsRequestListRegionsPaginateTypeDef = TypedDict(
    "ListRegionsRequestListRegionsPaginateTypeDef",
    {
        "AccountId": NotRequired[str],
        "RegionOptStatusContains": NotRequired[Sequence[RegionOptStatusType]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListRegionsResponseTypeDef = TypedDict(
    "ListRegionsResponseTypeDef",
    {
        "NextToken": str,
        "Regions": List[RegionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
