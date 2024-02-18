"""
Type annotations for workmail service client paginators.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_workmail/paginators/)

Usage::

    ```python
    from aiobotocore.session import get_session

    from types_aiobotocore_workmail.client import WorkMailClient
    from types_aiobotocore_workmail.paginator import (
        ListAliasesPaginator,
        ListAvailabilityConfigurationsPaginator,
        ListGroupMembersPaginator,
        ListGroupsPaginator,
        ListMailboxPermissionsPaginator,
        ListOrganizationsPaginator,
        ListResourceDelegatesPaginator,
        ListResourcesPaginator,
        ListUsersPaginator,
    )

    session = get_session()
    with session.create_client("workmail") as client:
        client: WorkMailClient

        list_aliases_paginator: ListAliasesPaginator = client.get_paginator("list_aliases")
        list_availability_configurations_paginator: ListAvailabilityConfigurationsPaginator = client.get_paginator("list_availability_configurations")
        list_group_members_paginator: ListGroupMembersPaginator = client.get_paginator("list_group_members")
        list_groups_paginator: ListGroupsPaginator = client.get_paginator("list_groups")
        list_mailbox_permissions_paginator: ListMailboxPermissionsPaginator = client.get_paginator("list_mailbox_permissions")
        list_organizations_paginator: ListOrganizationsPaginator = client.get_paginator("list_organizations")
        list_resource_delegates_paginator: ListResourceDelegatesPaginator = client.get_paginator("list_resource_delegates")
        list_resources_paginator: ListResourcesPaginator = client.get_paginator("list_resources")
        list_users_paginator: ListUsersPaginator = client.get_paginator("list_users")
    ```
"""

from typing import AsyncIterator, Generic, Iterator, TypeVar

from aiobotocore.paginate import AioPaginator
from botocore.paginate import PageIterator

from .type_defs import (
    ListAliasesResponseTypeDef,
    ListAvailabilityConfigurationsResponseTypeDef,
    ListGroupMembersResponseTypeDef,
    ListGroupsFiltersTypeDef,
    ListGroupsResponseTypeDef,
    ListMailboxPermissionsResponseTypeDef,
    ListOrganizationsResponseTypeDef,
    ListResourceDelegatesResponseTypeDef,
    ListResourcesFiltersTypeDef,
    ListResourcesResponseTypeDef,
    ListUsersFiltersTypeDef,
    ListUsersResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "ListAliasesPaginator",
    "ListAvailabilityConfigurationsPaginator",
    "ListGroupMembersPaginator",
    "ListGroupsPaginator",
    "ListMailboxPermissionsPaginator",
    "ListOrganizationsPaginator",
    "ListResourceDelegatesPaginator",
    "ListResourcesPaginator",
    "ListUsersPaginator",
)

_ItemTypeDef = TypeVar("_ItemTypeDef")

class _PageIterator(Generic[_ItemTypeDef], PageIterator):
    def __iter__(self) -> Iterator[_ItemTypeDef]:
        """
        Proxy method to specify iterator item type.
        """

class ListAliasesPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail.Paginator.ListAliases)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_workmail/paginators/#listaliasespaginator)
    """

    def paginate(
        self, *, OrganizationId: str, EntityId: str, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListAliasesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail.Paginator.ListAliases.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_workmail/paginators/#listaliasespaginator)
        """

class ListAvailabilityConfigurationsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail.Paginator.ListAvailabilityConfigurations)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_workmail/paginators/#listavailabilityconfigurationspaginator)
    """

    def paginate(
        self, *, OrganizationId: str, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListAvailabilityConfigurationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail.Paginator.ListAvailabilityConfigurations.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_workmail/paginators/#listavailabilityconfigurationspaginator)
        """

class ListGroupMembersPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail.Paginator.ListGroupMembers)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_workmail/paginators/#listgroupmemberspaginator)
    """

    def paginate(
        self, *, OrganizationId: str, GroupId: str, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListGroupMembersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail.Paginator.ListGroupMembers.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_workmail/paginators/#listgroupmemberspaginator)
        """

class ListGroupsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail.Paginator.ListGroups)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_workmail/paginators/#listgroupspaginator)
    """

    def paginate(
        self,
        *,
        OrganizationId: str,
        Filters: ListGroupsFiltersTypeDef = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListGroupsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail.Paginator.ListGroups.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_workmail/paginators/#listgroupspaginator)
        """

class ListMailboxPermissionsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail.Paginator.ListMailboxPermissions)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_workmail/paginators/#listmailboxpermissionspaginator)
    """

    def paginate(
        self, *, OrganizationId: str, EntityId: str, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListMailboxPermissionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail.Paginator.ListMailboxPermissions.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_workmail/paginators/#listmailboxpermissionspaginator)
        """

class ListOrganizationsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail.Paginator.ListOrganizations)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_workmail/paginators/#listorganizationspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListOrganizationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail.Paginator.ListOrganizations.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_workmail/paginators/#listorganizationspaginator)
        """

class ListResourceDelegatesPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail.Paginator.ListResourceDelegates)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_workmail/paginators/#listresourcedelegatespaginator)
    """

    def paginate(
        self,
        *,
        OrganizationId: str,
        ResourceId: str,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListResourceDelegatesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail.Paginator.ListResourceDelegates.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_workmail/paginators/#listresourcedelegatespaginator)
        """

class ListResourcesPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail.Paginator.ListResources)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_workmail/paginators/#listresourcespaginator)
    """

    def paginate(
        self,
        *,
        OrganizationId: str,
        Filters: ListResourcesFiltersTypeDef = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListResourcesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail.Paginator.ListResources.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_workmail/paginators/#listresourcespaginator)
        """

class ListUsersPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail.Paginator.ListUsers)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_workmail/paginators/#listuserspaginator)
    """

    def paginate(
        self,
        *,
        OrganizationId: str,
        Filters: ListUsersFiltersTypeDef = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListUsersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail.Paginator.ListUsers.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_workmail/paginators/#listuserspaginator)
        """
