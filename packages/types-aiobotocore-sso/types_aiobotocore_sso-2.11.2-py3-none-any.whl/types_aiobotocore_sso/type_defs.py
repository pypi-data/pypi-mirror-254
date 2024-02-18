"""
Type annotations for sso service type definitions.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso/type_defs/)

Usage::

    ```python
    from types_aiobotocore_sso.type_defs import AccountInfoTypeDef

    data: AccountInfoTypeDef = ...
    ```
"""

import sys
from typing import Dict, List

if sys.version_info >= (3, 12):
    from typing import NotRequired
else:
    from typing_extensions import NotRequired
if sys.version_info >= (3, 12):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AccountInfoTypeDef",
    "ResponseMetadataTypeDef",
    "GetRoleCredentialsRequestRequestTypeDef",
    "RoleCredentialsTypeDef",
    "PaginatorConfigTypeDef",
    "ListAccountRolesRequestRequestTypeDef",
    "RoleInfoTypeDef",
    "ListAccountsRequestRequestTypeDef",
    "LogoutRequestRequestTypeDef",
    "EmptyResponseMetadataTypeDef",
    "ListAccountsResponseTypeDef",
    "GetRoleCredentialsResponseTypeDef",
    "ListAccountRolesRequestListAccountRolesPaginateTypeDef",
    "ListAccountsRequestListAccountsPaginateTypeDef",
    "ListAccountRolesResponseTypeDef",
)

AccountInfoTypeDef = TypedDict(
    "AccountInfoTypeDef",
    {
        "accountId": NotRequired[str],
        "accountName": NotRequired[str],
        "emailAddress": NotRequired[str],
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
GetRoleCredentialsRequestRequestTypeDef = TypedDict(
    "GetRoleCredentialsRequestRequestTypeDef",
    {
        "roleName": str,
        "accountId": str,
        "accessToken": str,
    },
)
RoleCredentialsTypeDef = TypedDict(
    "RoleCredentialsTypeDef",
    {
        "accessKeyId": NotRequired[str],
        "secretAccessKey": NotRequired[str],
        "sessionToken": NotRequired[str],
        "expiration": NotRequired[int],
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
ListAccountRolesRequestRequestTypeDef = TypedDict(
    "ListAccountRolesRequestRequestTypeDef",
    {
        "accessToken": str,
        "accountId": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
RoleInfoTypeDef = TypedDict(
    "RoleInfoTypeDef",
    {
        "roleName": NotRequired[str],
        "accountId": NotRequired[str],
    },
)
ListAccountsRequestRequestTypeDef = TypedDict(
    "ListAccountsRequestRequestTypeDef",
    {
        "accessToken": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
LogoutRequestRequestTypeDef = TypedDict(
    "LogoutRequestRequestTypeDef",
    {
        "accessToken": str,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAccountsResponseTypeDef = TypedDict(
    "ListAccountsResponseTypeDef",
    {
        "nextToken": str,
        "accountList": List[AccountInfoTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetRoleCredentialsResponseTypeDef = TypedDict(
    "GetRoleCredentialsResponseTypeDef",
    {
        "roleCredentials": RoleCredentialsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAccountRolesRequestListAccountRolesPaginateTypeDef = TypedDict(
    "ListAccountRolesRequestListAccountRolesPaginateTypeDef",
    {
        "accessToken": str,
        "accountId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListAccountsRequestListAccountsPaginateTypeDef = TypedDict(
    "ListAccountsRequestListAccountsPaginateTypeDef",
    {
        "accessToken": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListAccountRolesResponseTypeDef = TypedDict(
    "ListAccountRolesResponseTypeDef",
    {
        "nextToken": str,
        "roleList": List[RoleInfoTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
