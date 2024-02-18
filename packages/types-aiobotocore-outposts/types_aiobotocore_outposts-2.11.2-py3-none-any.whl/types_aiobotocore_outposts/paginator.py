"""
Type annotations for outposts service client paginators.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_outposts/paginators/)

Usage::

    ```python
    from aiobotocore.session import get_session

    from types_aiobotocore_outposts.client import OutpostsClient
    from types_aiobotocore_outposts.paginator import (
        GetOutpostInstanceTypesPaginator,
        ListAssetsPaginator,
        ListCatalogItemsPaginator,
        ListOrdersPaginator,
        ListOutpostsPaginator,
        ListSitesPaginator,
    )

    session = get_session()
    with session.create_client("outposts") as client:
        client: OutpostsClient

        get_outpost_instance_types_paginator: GetOutpostInstanceTypesPaginator = client.get_paginator("get_outpost_instance_types")
        list_assets_paginator: ListAssetsPaginator = client.get_paginator("list_assets")
        list_catalog_items_paginator: ListCatalogItemsPaginator = client.get_paginator("list_catalog_items")
        list_orders_paginator: ListOrdersPaginator = client.get_paginator("list_orders")
        list_outposts_paginator: ListOutpostsPaginator = client.get_paginator("list_outposts")
        list_sites_paginator: ListSitesPaginator = client.get_paginator("list_sites")
    ```
"""

from typing import AsyncIterator, Generic, Iterator, Sequence, TypeVar

from aiobotocore.paginate import AioPaginator
from botocore.paginate import PageIterator

from .literals import AssetStateType, CatalogItemClassType, SupportedStorageEnumType
from .type_defs import (
    GetOutpostInstanceTypesOutputTypeDef,
    ListAssetsOutputTypeDef,
    ListCatalogItemsOutputTypeDef,
    ListOrdersOutputTypeDef,
    ListOutpostsOutputTypeDef,
    ListSitesOutputTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "GetOutpostInstanceTypesPaginator",
    "ListAssetsPaginator",
    "ListCatalogItemsPaginator",
    "ListOrdersPaginator",
    "ListOutpostsPaginator",
    "ListSitesPaginator",
)

_ItemTypeDef = TypeVar("_ItemTypeDef")


class _PageIterator(Generic[_ItemTypeDef], PageIterator):
    def __iter__(self) -> Iterator[_ItemTypeDef]:
        """
        Proxy method to specify iterator item type.
        """


class GetOutpostInstanceTypesPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts.html#Outposts.Paginator.GetOutpostInstanceTypes)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_outposts/paginators/#getoutpostinstancetypespaginator)
    """

    def paginate(
        self, *, OutpostId: str, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[GetOutpostInstanceTypesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts.html#Outposts.Paginator.GetOutpostInstanceTypes.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_outposts/paginators/#getoutpostinstancetypespaginator)
        """


class ListAssetsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts.html#Outposts.Paginator.ListAssets)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_outposts/paginators/#listassetspaginator)
    """

    def paginate(
        self,
        *,
        OutpostIdentifier: str,
        HostIdFilter: Sequence[str] = ...,
        StatusFilter: Sequence[AssetStateType] = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListAssetsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts.html#Outposts.Paginator.ListAssets.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_outposts/paginators/#listassetspaginator)
        """


class ListCatalogItemsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts.html#Outposts.Paginator.ListCatalogItems)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_outposts/paginators/#listcatalogitemspaginator)
    """

    def paginate(
        self,
        *,
        ItemClassFilter: Sequence[CatalogItemClassType] = ...,
        SupportedStorageFilter: Sequence[SupportedStorageEnumType] = ...,
        EC2FamilyFilter: Sequence[str] = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListCatalogItemsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts.html#Outposts.Paginator.ListCatalogItems.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_outposts/paginators/#listcatalogitemspaginator)
        """


class ListOrdersPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts.html#Outposts.Paginator.ListOrders)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_outposts/paginators/#listorderspaginator)
    """

    def paginate(
        self, *, OutpostIdentifierFilter: str = ..., PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListOrdersOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts.html#Outposts.Paginator.ListOrders.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_outposts/paginators/#listorderspaginator)
        """


class ListOutpostsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts.html#Outposts.Paginator.ListOutposts)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_outposts/paginators/#listoutpostspaginator)
    """

    def paginate(
        self,
        *,
        LifeCycleStatusFilter: Sequence[str] = ...,
        AvailabilityZoneFilter: Sequence[str] = ...,
        AvailabilityZoneIdFilter: Sequence[str] = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListOutpostsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts.html#Outposts.Paginator.ListOutposts.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_outposts/paginators/#listoutpostspaginator)
        """


class ListSitesPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts.html#Outposts.Paginator.ListSites)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_outposts/paginators/#listsitespaginator)
    """

    def paginate(
        self,
        *,
        OperatingAddressCountryCodeFilter: Sequence[str] = ...,
        OperatingAddressStateOrRegionFilter: Sequence[str] = ...,
        OperatingAddressCityFilter: Sequence[str] = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListSitesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts.html#Outposts.Paginator.ListSites.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_outposts/paginators/#listsitespaginator)
        """
