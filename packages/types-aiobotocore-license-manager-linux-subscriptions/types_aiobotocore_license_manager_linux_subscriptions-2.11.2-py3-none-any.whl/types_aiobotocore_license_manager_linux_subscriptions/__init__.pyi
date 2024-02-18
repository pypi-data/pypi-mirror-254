"""
Main interface for license-manager-linux-subscriptions service.

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_license_manager_linux_subscriptions import (
        Client,
        LicenseManagerLinuxSubscriptionsClient,
        ListLinuxSubscriptionInstancesPaginator,
        ListLinuxSubscriptionsPaginator,
    )

    session = get_session()
    async with session.create_client("license-manager-linux-subscriptions") as client:
        client: LicenseManagerLinuxSubscriptionsClient
        ...


    list_linux_subscription_instances_paginator: ListLinuxSubscriptionInstancesPaginator = client.get_paginator("list_linux_subscription_instances")
    list_linux_subscriptions_paginator: ListLinuxSubscriptionsPaginator = client.get_paginator("list_linux_subscriptions")
    ```
"""

from .client import LicenseManagerLinuxSubscriptionsClient
from .paginator import ListLinuxSubscriptionInstancesPaginator, ListLinuxSubscriptionsPaginator

Client = LicenseManagerLinuxSubscriptionsClient

__all__ = (
    "Client",
    "LicenseManagerLinuxSubscriptionsClient",
    "ListLinuxSubscriptionInstancesPaginator",
    "ListLinuxSubscriptionsPaginator",
)
