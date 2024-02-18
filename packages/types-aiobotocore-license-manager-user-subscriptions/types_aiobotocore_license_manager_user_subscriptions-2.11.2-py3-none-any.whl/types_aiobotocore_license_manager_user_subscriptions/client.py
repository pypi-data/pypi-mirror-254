"""
Type annotations for license-manager-user-subscriptions service client.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_license_manager_user_subscriptions/client/)

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_license_manager_user_subscriptions.client import LicenseManagerUserSubscriptionsClient

    session = get_session()
    async with session.create_client("license-manager-user-subscriptions") as client:
        client: LicenseManagerUserSubscriptionsClient
    ```
"""

import sys
from typing import Any, Dict, Mapping, Sequence, Type, overload

from aiobotocore.client import AioBaseClient
from botocore.client import ClientMeta

from .paginator import (
    ListIdentityProvidersPaginator,
    ListInstancesPaginator,
    ListProductSubscriptionsPaginator,
    ListUserAssociationsPaginator,
)
from .type_defs import (
    AssociateUserResponseTypeDef,
    DeregisterIdentityProviderResponseTypeDef,
    DisassociateUserResponseTypeDef,
    FilterTypeDef,
    IdentityProviderTypeDef,
    ListIdentityProvidersResponseTypeDef,
    ListInstancesResponseTypeDef,
    ListProductSubscriptionsResponseTypeDef,
    ListUserAssociationsResponseTypeDef,
    RegisterIdentityProviderResponseTypeDef,
    SettingsTypeDef,
    StartProductSubscriptionResponseTypeDef,
    StopProductSubscriptionResponseTypeDef,
    UpdateIdentityProviderSettingsResponseTypeDef,
    UpdateSettingsTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("LicenseManagerUserSubscriptionsClient",)


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
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class LicenseManagerUserSubscriptionsClient(AioBaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager-user-subscriptions.html#LicenseManagerUserSubscriptions.Client)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_license_manager_user_subscriptions/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        LicenseManagerUserSubscriptionsClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager-user-subscriptions.html#LicenseManagerUserSubscriptions.Client.exceptions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_license_manager_user_subscriptions/client/#exceptions)
        """

    async def associate_user(
        self,
        *,
        IdentityProvider: IdentityProviderTypeDef,
        InstanceId: str,
        Username: str,
        Domain: str = ...,
    ) -> AssociateUserResponseTypeDef:
        """
        Associates the user to an EC2 instance to utilize user-based subscriptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager-user-subscriptions.html#LicenseManagerUserSubscriptions.Client.associate_user)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_license_manager_user_subscriptions/client/#associate_user)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager-user-subscriptions.html#LicenseManagerUserSubscriptions.Client.can_paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_license_manager_user_subscriptions/client/#can_paginate)
        """

    async def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager-user-subscriptions.html#LicenseManagerUserSubscriptions.Client.close)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_license_manager_user_subscriptions/client/#close)
        """

    async def deregister_identity_provider(
        self, *, IdentityProvider: IdentityProviderTypeDef, Product: str
    ) -> DeregisterIdentityProviderResponseTypeDef:
        """
        Deregisters the identity provider from providing user-based subscriptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager-user-subscriptions.html#LicenseManagerUserSubscriptions.Client.deregister_identity_provider)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_license_manager_user_subscriptions/client/#deregister_identity_provider)
        """

    async def disassociate_user(
        self,
        *,
        IdentityProvider: IdentityProviderTypeDef,
        InstanceId: str,
        Username: str,
        Domain: str = ...,
    ) -> DisassociateUserResponseTypeDef:
        """
        Disassociates the user from an EC2 instance providing user-based subscriptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager-user-subscriptions.html#LicenseManagerUserSubscriptions.Client.disassociate_user)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_license_manager_user_subscriptions/client/#disassociate_user)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager-user-subscriptions.html#LicenseManagerUserSubscriptions.Client.generate_presigned_url)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_license_manager_user_subscriptions/client/#generate_presigned_url)
        """

    async def list_identity_providers(
        self, *, MaxResults: int = ..., NextToken: str = ...
    ) -> ListIdentityProvidersResponseTypeDef:
        """
        Lists the identity providers for user-based subscriptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager-user-subscriptions.html#LicenseManagerUserSubscriptions.Client.list_identity_providers)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_license_manager_user_subscriptions/client/#list_identity_providers)
        """

    async def list_instances(
        self, *, Filters: Sequence[FilterTypeDef] = ..., MaxResults: int = ..., NextToken: str = ...
    ) -> ListInstancesResponseTypeDef:
        """
        Lists the EC2 instances providing user-based subscriptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager-user-subscriptions.html#LicenseManagerUserSubscriptions.Client.list_instances)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_license_manager_user_subscriptions/client/#list_instances)
        """

    async def list_product_subscriptions(
        self,
        *,
        IdentityProvider: IdentityProviderTypeDef,
        Product: str,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
    ) -> ListProductSubscriptionsResponseTypeDef:
        """
        Lists the user-based subscription products available from an identity provider.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager-user-subscriptions.html#LicenseManagerUserSubscriptions.Client.list_product_subscriptions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_license_manager_user_subscriptions/client/#list_product_subscriptions)
        """

    async def list_user_associations(
        self,
        *,
        IdentityProvider: IdentityProviderTypeDef,
        InstanceId: str,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
    ) -> ListUserAssociationsResponseTypeDef:
        """
        Lists user associations for an identity provider.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager-user-subscriptions.html#LicenseManagerUserSubscriptions.Client.list_user_associations)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_license_manager_user_subscriptions/client/#list_user_associations)
        """

    async def register_identity_provider(
        self,
        *,
        IdentityProvider: IdentityProviderTypeDef,
        Product: str,
        Settings: SettingsTypeDef = ...,
    ) -> RegisterIdentityProviderResponseTypeDef:
        """
        Registers an identity provider for user-based subscriptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager-user-subscriptions.html#LicenseManagerUserSubscriptions.Client.register_identity_provider)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_license_manager_user_subscriptions/client/#register_identity_provider)
        """

    async def start_product_subscription(
        self,
        *,
        IdentityProvider: IdentityProviderTypeDef,
        Product: str,
        Username: str,
        Domain: str = ...,
    ) -> StartProductSubscriptionResponseTypeDef:
        """
        Starts a product subscription for a user with the specified identity provider.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager-user-subscriptions.html#LicenseManagerUserSubscriptions.Client.start_product_subscription)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_license_manager_user_subscriptions/client/#start_product_subscription)
        """

    async def stop_product_subscription(
        self,
        *,
        IdentityProvider: IdentityProviderTypeDef,
        Product: str,
        Username: str,
        Domain: str = ...,
    ) -> StopProductSubscriptionResponseTypeDef:
        """
        Stops a product subscription for a user with the specified identity provider.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager-user-subscriptions.html#LicenseManagerUserSubscriptions.Client.stop_product_subscription)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_license_manager_user_subscriptions/client/#stop_product_subscription)
        """

    async def update_identity_provider_settings(
        self,
        *,
        IdentityProvider: IdentityProviderTypeDef,
        Product: str,
        UpdateSettings: UpdateSettingsTypeDef,
    ) -> UpdateIdentityProviderSettingsResponseTypeDef:
        """
        Updates additional product configuration settings for the registered identity
        provider.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager-user-subscriptions.html#LicenseManagerUserSubscriptions.Client.update_identity_provider_settings)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_license_manager_user_subscriptions/client/#update_identity_provider_settings)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_identity_providers"]
    ) -> ListIdentityProvidersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager-user-subscriptions.html#LicenseManagerUserSubscriptions.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_license_manager_user_subscriptions/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_instances"]) -> ListInstancesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager-user-subscriptions.html#LicenseManagerUserSubscriptions.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_license_manager_user_subscriptions/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_product_subscriptions"]
    ) -> ListProductSubscriptionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager-user-subscriptions.html#LicenseManagerUserSubscriptions.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_license_manager_user_subscriptions/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_user_associations"]
    ) -> ListUserAssociationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager-user-subscriptions.html#LicenseManagerUserSubscriptions.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_license_manager_user_subscriptions/client/#get_paginator)
        """

    async def __aenter__(self) -> "LicenseManagerUserSubscriptionsClient":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager-user-subscriptions.html#LicenseManagerUserSubscriptions.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_license_manager_user_subscriptions/client/)
        """

    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> Any:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager-user-subscriptions.html#LicenseManagerUserSubscriptions.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_license_manager_user_subscriptions/client/)
        """
