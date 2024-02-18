"""
Type annotations for network-firewall service client paginators.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_network_firewall/paginators/)

Usage::

    ```python
    from aiobotocore.session import get_session

    from types_aiobotocore_network_firewall.client import NetworkFirewallClient
    from types_aiobotocore_network_firewall.paginator import (
        ListFirewallPoliciesPaginator,
        ListFirewallsPaginator,
        ListRuleGroupsPaginator,
        ListTLSInspectionConfigurationsPaginator,
        ListTagsForResourcePaginator,
    )

    session = get_session()
    with session.create_client("network-firewall") as client:
        client: NetworkFirewallClient

        list_firewall_policies_paginator: ListFirewallPoliciesPaginator = client.get_paginator("list_firewall_policies")
        list_firewalls_paginator: ListFirewallsPaginator = client.get_paginator("list_firewalls")
        list_rule_groups_paginator: ListRuleGroupsPaginator = client.get_paginator("list_rule_groups")
        list_tls_inspection_configurations_paginator: ListTLSInspectionConfigurationsPaginator = client.get_paginator("list_tls_inspection_configurations")
        list_tags_for_resource_paginator: ListTagsForResourcePaginator = client.get_paginator("list_tags_for_resource")
    ```
"""

from typing import AsyncIterator, Generic, Iterator, Sequence, TypeVar

from aiobotocore.paginate import AioPaginator
from botocore.paginate import PageIterator

from .literals import ResourceManagedStatusType, ResourceManagedTypeType, RuleGroupTypeType
from .type_defs import (
    ListFirewallPoliciesResponseTypeDef,
    ListFirewallsResponseTypeDef,
    ListRuleGroupsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTLSInspectionConfigurationsResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "ListFirewallPoliciesPaginator",
    "ListFirewallsPaginator",
    "ListRuleGroupsPaginator",
    "ListTLSInspectionConfigurationsPaginator",
    "ListTagsForResourcePaginator",
)

_ItemTypeDef = TypeVar("_ItemTypeDef")


class _PageIterator(Generic[_ItemTypeDef], PageIterator):
    def __iter__(self) -> Iterator[_ItemTypeDef]:
        """
        Proxy method to specify iterator item type.
        """


class ListFirewallPoliciesPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall.html#NetworkFirewall.Paginator.ListFirewallPolicies)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_network_firewall/paginators/#listfirewallpoliciespaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListFirewallPoliciesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall.html#NetworkFirewall.Paginator.ListFirewallPolicies.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_network_firewall/paginators/#listfirewallpoliciespaginator)
        """


class ListFirewallsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall.html#NetworkFirewall.Paginator.ListFirewalls)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_network_firewall/paginators/#listfirewallspaginator)
    """

    def paginate(
        self, *, VpcIds: Sequence[str] = ..., PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListFirewallsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall.html#NetworkFirewall.Paginator.ListFirewalls.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_network_firewall/paginators/#listfirewallspaginator)
        """


class ListRuleGroupsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall.html#NetworkFirewall.Paginator.ListRuleGroups)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_network_firewall/paginators/#listrulegroupspaginator)
    """

    def paginate(
        self,
        *,
        Scope: ResourceManagedStatusType = ...,
        ManagedType: ResourceManagedTypeType = ...,
        Type: RuleGroupTypeType = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListRuleGroupsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall.html#NetworkFirewall.Paginator.ListRuleGroups.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_network_firewall/paginators/#listrulegroupspaginator)
        """


class ListTLSInspectionConfigurationsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall.html#NetworkFirewall.Paginator.ListTLSInspectionConfigurations)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_network_firewall/paginators/#listtlsinspectionconfigurationspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListTLSInspectionConfigurationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall.html#NetworkFirewall.Paginator.ListTLSInspectionConfigurations.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_network_firewall/paginators/#listtlsinspectionconfigurationspaginator)
        """


class ListTagsForResourcePaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall.html#NetworkFirewall.Paginator.ListTagsForResource)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_network_firewall/paginators/#listtagsforresourcepaginator)
    """

    def paginate(
        self, *, ResourceArn: str, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListTagsForResourceResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall.html#NetworkFirewall.Paginator.ListTagsForResource.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_network_firewall/paginators/#listtagsforresourcepaginator)
        """
