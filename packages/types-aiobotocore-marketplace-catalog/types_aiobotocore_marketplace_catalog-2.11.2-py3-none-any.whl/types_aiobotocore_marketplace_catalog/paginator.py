"""
Type annotations for marketplace-catalog service client paginators.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_marketplace_catalog/paginators/)

Usage::

    ```python
    from aiobotocore.session import get_session

    from types_aiobotocore_marketplace_catalog.client import MarketplaceCatalogClient
    from types_aiobotocore_marketplace_catalog.paginator import (
        ListChangeSetsPaginator,
        ListEntitiesPaginator,
    )

    session = get_session()
    with session.create_client("marketplace-catalog") as client:
        client: MarketplaceCatalogClient

        list_change_sets_paginator: ListChangeSetsPaginator = client.get_paginator("list_change_sets")
        list_entities_paginator: ListEntitiesPaginator = client.get_paginator("list_entities")
    ```
"""

from typing import AsyncIterator, Generic, Iterator, Sequence, TypeVar

from aiobotocore.paginate import AioPaginator
from botocore.paginate import PageIterator

from .literals import OwnershipTypeType
from .type_defs import (
    EntityTypeFiltersTypeDef,
    EntityTypeSortTypeDef,
    FilterTypeDef,
    ListChangeSetsResponseTypeDef,
    ListEntitiesResponseTypeDef,
    PaginatorConfigTypeDef,
    SortTypeDef,
)

__all__ = ("ListChangeSetsPaginator", "ListEntitiesPaginator")

_ItemTypeDef = TypeVar("_ItemTypeDef")


class _PageIterator(Generic[_ItemTypeDef], PageIterator):
    def __iter__(self) -> Iterator[_ItemTypeDef]:
        """
        Proxy method to specify iterator item type.
        """


class ListChangeSetsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/marketplace-catalog.html#MarketplaceCatalog.Paginator.ListChangeSets)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_marketplace_catalog/paginators/#listchangesetspaginator)
    """

    def paginate(
        self,
        *,
        Catalog: str,
        FilterList: Sequence[FilterTypeDef] = ...,
        Sort: SortTypeDef = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListChangeSetsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/marketplace-catalog.html#MarketplaceCatalog.Paginator.ListChangeSets.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_marketplace_catalog/paginators/#listchangesetspaginator)
        """


class ListEntitiesPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/marketplace-catalog.html#MarketplaceCatalog.Paginator.ListEntities)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_marketplace_catalog/paginators/#listentitiespaginator)
    """

    def paginate(
        self,
        *,
        Catalog: str,
        EntityType: str,
        FilterList: Sequence[FilterTypeDef] = ...,
        Sort: SortTypeDef = ...,
        OwnershipType: OwnershipTypeType = ...,
        EntityTypeFilters: EntityTypeFiltersTypeDef = ...,
        EntityTypeSort: EntityTypeSortTypeDef = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListEntitiesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/marketplace-catalog.html#MarketplaceCatalog.Paginator.ListEntities.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_marketplace_catalog/paginators/#listentitiespaginator)
        """
