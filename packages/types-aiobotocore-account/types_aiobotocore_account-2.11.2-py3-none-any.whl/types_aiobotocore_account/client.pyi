"""
Type annotations for account service client.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_account/client/)

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_account.client import AccountClient

    session = get_session()
    async with session.create_client("account") as client:
        client: AccountClient
    ```
"""

import sys
from typing import Any, Dict, Mapping, Sequence, Type

from aiobotocore.client import AioBaseClient
from botocore.client import ClientMeta

from .literals import AlternateContactTypeType, RegionOptStatusType
from .paginator import ListRegionsPaginator
from .type_defs import (
    ContactInformationTypeDef,
    EmptyResponseMetadataTypeDef,
    GetAlternateContactResponseTypeDef,
    GetContactInformationResponseTypeDef,
    GetRegionOptStatusResponseTypeDef,
    ListRegionsResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("AccountClient",)

class BotocoreClientError(Exception):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    TooManyRequestsException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class AccountClient(AioBaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/account.html#Account.Client)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_account/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        AccountClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/account.html#Account.Client.exceptions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_account/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/account.html#Account.Client.can_paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_account/client/#can_paginate)
        """

    async def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/account.html#Account.Client.close)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_account/client/#close)
        """

    async def delete_alternate_contact(
        self, *, AlternateContactType: AlternateContactTypeType, AccountId: str = ...
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified alternate contact from an Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/account.html#Account.Client.delete_alternate_contact)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_account/client/#delete_alternate_contact)
        """

    async def disable_region(
        self, *, RegionName: str, AccountId: str = ...
    ) -> EmptyResponseMetadataTypeDef:
        """
        Disables (opts-out) a particular Region for an account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/account.html#Account.Client.disable_region)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_account/client/#disable_region)
        """

    async def enable_region(
        self, *, RegionName: str, AccountId: str = ...
    ) -> EmptyResponseMetadataTypeDef:
        """
        Enables (opts-in) a particular Region for an account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/account.html#Account.Client.enable_region)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_account/client/#enable_region)
        """

    async def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/account.html#Account.Client.generate_presigned_url)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_account/client/#generate_presigned_url)
        """

    async def get_alternate_contact(
        self, *, AlternateContactType: AlternateContactTypeType, AccountId: str = ...
    ) -> GetAlternateContactResponseTypeDef:
        """
        Retrieves the specified alternate contact attached to an Amazon Web Services
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/account.html#Account.Client.get_alternate_contact)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_account/client/#get_alternate_contact)
        """

    async def get_contact_information(
        self, *, AccountId: str = ...
    ) -> GetContactInformationResponseTypeDef:
        """
        Retrieves the primary contact information of an Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/account.html#Account.Client.get_contact_information)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_account/client/#get_contact_information)
        """

    async def get_region_opt_status(
        self, *, RegionName: str, AccountId: str = ...
    ) -> GetRegionOptStatusResponseTypeDef:
        """
        Retrieves the opt-in status of a particular Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/account.html#Account.Client.get_region_opt_status)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_account/client/#get_region_opt_status)
        """

    async def list_regions(
        self,
        *,
        AccountId: str = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
        RegionOptStatusContains: Sequence[RegionOptStatusType] = ...,
    ) -> ListRegionsResponseTypeDef:
        """
        Lists all the Regions for a given account and their respective opt-in statuses.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/account.html#Account.Client.list_regions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_account/client/#list_regions)
        """

    async def put_alternate_contact(
        self,
        *,
        AlternateContactType: AlternateContactTypeType,
        EmailAddress: str,
        Name: str,
        PhoneNumber: str,
        Title: str,
        AccountId: str = ...,
    ) -> EmptyResponseMetadataTypeDef:
        """
        Modifies the specified alternate contact attached to an Amazon Web Services
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/account.html#Account.Client.put_alternate_contact)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_account/client/#put_alternate_contact)
        """

    async def put_contact_information(
        self, *, ContactInformation: ContactInformationTypeDef, AccountId: str = ...
    ) -> EmptyResponseMetadataTypeDef:
        """
        Updates the primary contact information of an Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/account.html#Account.Client.put_contact_information)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_account/client/#put_contact_information)
        """

    def get_paginator(self, operation_name: Literal["list_regions"]) -> ListRegionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/account.html#Account.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_account/client/#get_paginator)
        """

    async def __aenter__(self) -> "AccountClient":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/account.html#Account.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_account/client/)
        """

    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> Any:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/account.html#Account.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_account/client/)
        """
