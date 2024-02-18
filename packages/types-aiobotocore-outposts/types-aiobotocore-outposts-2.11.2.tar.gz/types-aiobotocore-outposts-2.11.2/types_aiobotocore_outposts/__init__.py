"""
Main interface for outposts service.

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_outposts import (
        Client,
        GetOutpostInstanceTypesPaginator,
        ListAssetsPaginator,
        ListCatalogItemsPaginator,
        ListOrdersPaginator,
        ListOutpostsPaginator,
        ListSitesPaginator,
        OutpostsClient,
    )

    session = get_session()
    async with session.create_client("outposts") as client:
        client: OutpostsClient
        ...


    get_outpost_instance_types_paginator: GetOutpostInstanceTypesPaginator = client.get_paginator("get_outpost_instance_types")
    list_assets_paginator: ListAssetsPaginator = client.get_paginator("list_assets")
    list_catalog_items_paginator: ListCatalogItemsPaginator = client.get_paginator("list_catalog_items")
    list_orders_paginator: ListOrdersPaginator = client.get_paginator("list_orders")
    list_outposts_paginator: ListOutpostsPaginator = client.get_paginator("list_outposts")
    list_sites_paginator: ListSitesPaginator = client.get_paginator("list_sites")
    ```
"""

from .client import OutpostsClient
from .paginator import (
    GetOutpostInstanceTypesPaginator,
    ListAssetsPaginator,
    ListCatalogItemsPaginator,
    ListOrdersPaginator,
    ListOutpostsPaginator,
    ListSitesPaginator,
)

Client = OutpostsClient

__all__ = (
    "Client",
    "GetOutpostInstanceTypesPaginator",
    "ListAssetsPaginator",
    "ListCatalogItemsPaginator",
    "ListOrdersPaginator",
    "ListOutpostsPaginator",
    "ListSitesPaginator",
    "OutpostsClient",
)
