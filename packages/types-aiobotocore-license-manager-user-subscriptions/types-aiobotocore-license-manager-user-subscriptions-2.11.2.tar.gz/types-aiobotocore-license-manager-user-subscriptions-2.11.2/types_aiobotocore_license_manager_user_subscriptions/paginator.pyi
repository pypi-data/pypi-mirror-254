"""
Type annotations for license-manager-user-subscriptions service client paginators.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_license_manager_user_subscriptions/paginators/)

Usage::

    ```python
    from aiobotocore.session import get_session

    from types_aiobotocore_license_manager_user_subscriptions.client import LicenseManagerUserSubscriptionsClient
    from types_aiobotocore_license_manager_user_subscriptions.paginator import (
        ListIdentityProvidersPaginator,
        ListInstancesPaginator,
        ListProductSubscriptionsPaginator,
        ListUserAssociationsPaginator,
    )

    session = get_session()
    with session.create_client("license-manager-user-subscriptions") as client:
        client: LicenseManagerUserSubscriptionsClient

        list_identity_providers_paginator: ListIdentityProvidersPaginator = client.get_paginator("list_identity_providers")
        list_instances_paginator: ListInstancesPaginator = client.get_paginator("list_instances")
        list_product_subscriptions_paginator: ListProductSubscriptionsPaginator = client.get_paginator("list_product_subscriptions")
        list_user_associations_paginator: ListUserAssociationsPaginator = client.get_paginator("list_user_associations")
    ```
"""

from typing import AsyncIterator, Generic, Iterator, Sequence, TypeVar

from aiobotocore.paginate import AioPaginator
from botocore.paginate import PageIterator

from .type_defs import (
    FilterTypeDef,
    IdentityProviderTypeDef,
    ListIdentityProvidersResponseTypeDef,
    ListInstancesResponseTypeDef,
    ListProductSubscriptionsResponseTypeDef,
    ListUserAssociationsResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "ListIdentityProvidersPaginator",
    "ListInstancesPaginator",
    "ListProductSubscriptionsPaginator",
    "ListUserAssociationsPaginator",
)

_ItemTypeDef = TypeVar("_ItemTypeDef")

class _PageIterator(Generic[_ItemTypeDef], PageIterator):
    def __iter__(self) -> Iterator[_ItemTypeDef]:
        """
        Proxy method to specify iterator item type.
        """

class ListIdentityProvidersPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager-user-subscriptions.html#LicenseManagerUserSubscriptions.Paginator.ListIdentityProviders)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_license_manager_user_subscriptions/paginators/#listidentityproviderspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListIdentityProvidersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager-user-subscriptions.html#LicenseManagerUserSubscriptions.Paginator.ListIdentityProviders.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_license_manager_user_subscriptions/paginators/#listidentityproviderspaginator)
        """

class ListInstancesPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager-user-subscriptions.html#LicenseManagerUserSubscriptions.Paginator.ListInstances)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_license_manager_user_subscriptions/paginators/#listinstancespaginator)
    """

    def paginate(
        self,
        *,
        Filters: Sequence[FilterTypeDef] = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListInstancesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager-user-subscriptions.html#LicenseManagerUserSubscriptions.Paginator.ListInstances.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_license_manager_user_subscriptions/paginators/#listinstancespaginator)
        """

class ListProductSubscriptionsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager-user-subscriptions.html#LicenseManagerUserSubscriptions.Paginator.ListProductSubscriptions)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_license_manager_user_subscriptions/paginators/#listproductsubscriptionspaginator)
    """

    def paginate(
        self,
        *,
        IdentityProvider: IdentityProviderTypeDef,
        Product: str,
        Filters: Sequence[FilterTypeDef] = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListProductSubscriptionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager-user-subscriptions.html#LicenseManagerUserSubscriptions.Paginator.ListProductSubscriptions.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_license_manager_user_subscriptions/paginators/#listproductsubscriptionspaginator)
        """

class ListUserAssociationsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager-user-subscriptions.html#LicenseManagerUserSubscriptions.Paginator.ListUserAssociations)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_license_manager_user_subscriptions/paginators/#listuserassociationspaginator)
    """

    def paginate(
        self,
        *,
        IdentityProvider: IdentityProviderTypeDef,
        InstanceId: str,
        Filters: Sequence[FilterTypeDef] = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListUserAssociationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager-user-subscriptions.html#LicenseManagerUserSubscriptions.Paginator.ListUserAssociations.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_license_manager_user_subscriptions/paginators/#listuserassociationspaginator)
        """
