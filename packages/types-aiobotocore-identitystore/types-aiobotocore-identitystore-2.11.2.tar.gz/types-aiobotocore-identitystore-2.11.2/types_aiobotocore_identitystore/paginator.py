"""
Type annotations for identitystore service client paginators.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_identitystore/paginators/)

Usage::

    ```python
    from aiobotocore.session import get_session

    from types_aiobotocore_identitystore.client import IdentityStoreClient
    from types_aiobotocore_identitystore.paginator import (
        ListGroupMembershipsPaginator,
        ListGroupMembershipsForMemberPaginator,
        ListGroupsPaginator,
        ListUsersPaginator,
    )

    session = get_session()
    with session.create_client("identitystore") as client:
        client: IdentityStoreClient

        list_group_memberships_paginator: ListGroupMembershipsPaginator = client.get_paginator("list_group_memberships")
        list_group_memberships_for_member_paginator: ListGroupMembershipsForMemberPaginator = client.get_paginator("list_group_memberships_for_member")
        list_groups_paginator: ListGroupsPaginator = client.get_paginator("list_groups")
        list_users_paginator: ListUsersPaginator = client.get_paginator("list_users")
    ```
"""

from typing import AsyncIterator, Generic, Iterator, Sequence, TypeVar

from aiobotocore.paginate import AioPaginator
from botocore.paginate import PageIterator

from .type_defs import (
    FilterTypeDef,
    ListGroupMembershipsForMemberResponseTypeDef,
    ListGroupMembershipsResponseTypeDef,
    ListGroupsResponseTypeDef,
    ListUsersResponseTypeDef,
    MemberIdTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "ListGroupMembershipsPaginator",
    "ListGroupMembershipsForMemberPaginator",
    "ListGroupsPaginator",
    "ListUsersPaginator",
)

_ItemTypeDef = TypeVar("_ItemTypeDef")


class _PageIterator(Generic[_ItemTypeDef], PageIterator):
    def __iter__(self) -> Iterator[_ItemTypeDef]:
        """
        Proxy method to specify iterator item type.
        """


class ListGroupMembershipsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/identitystore.html#IdentityStore.Paginator.ListGroupMemberships)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_identitystore/paginators/#listgroupmembershipspaginator)
    """

    def paginate(
        self, *, IdentityStoreId: str, GroupId: str, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListGroupMembershipsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/identitystore.html#IdentityStore.Paginator.ListGroupMemberships.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_identitystore/paginators/#listgroupmembershipspaginator)
        """


class ListGroupMembershipsForMemberPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/identitystore.html#IdentityStore.Paginator.ListGroupMembershipsForMember)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_identitystore/paginators/#listgroupmembershipsformemberpaginator)
    """

    def paginate(
        self,
        *,
        IdentityStoreId: str,
        MemberId: MemberIdTypeDef,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListGroupMembershipsForMemberResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/identitystore.html#IdentityStore.Paginator.ListGroupMembershipsForMember.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_identitystore/paginators/#listgroupmembershipsformemberpaginator)
        """


class ListGroupsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/identitystore.html#IdentityStore.Paginator.ListGroups)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_identitystore/paginators/#listgroupspaginator)
    """

    def paginate(
        self,
        *,
        IdentityStoreId: str,
        Filters: Sequence[FilterTypeDef] = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListGroupsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/identitystore.html#IdentityStore.Paginator.ListGroups.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_identitystore/paginators/#listgroupspaginator)
        """


class ListUsersPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/identitystore.html#IdentityStore.Paginator.ListUsers)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_identitystore/paginators/#listuserspaginator)
    """

    def paginate(
        self,
        *,
        IdentityStoreId: str,
        Filters: Sequence[FilterTypeDef] = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListUsersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/identitystore.html#IdentityStore.Paginator.ListUsers.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_identitystore/paginators/#listuserspaginator)
        """
