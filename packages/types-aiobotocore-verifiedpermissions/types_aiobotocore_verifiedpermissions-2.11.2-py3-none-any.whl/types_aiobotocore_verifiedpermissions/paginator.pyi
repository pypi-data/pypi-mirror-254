"""
Type annotations for verifiedpermissions service client paginators.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_verifiedpermissions/paginators/)

Usage::

    ```python
    from aiobotocore.session import get_session

    from types_aiobotocore_verifiedpermissions.client import VerifiedPermissionsClient
    from types_aiobotocore_verifiedpermissions.paginator import (
        ListIdentitySourcesPaginator,
        ListPoliciesPaginator,
        ListPolicyStoresPaginator,
        ListPolicyTemplatesPaginator,
    )

    session = get_session()
    with session.create_client("verifiedpermissions") as client:
        client: VerifiedPermissionsClient

        list_identity_sources_paginator: ListIdentitySourcesPaginator = client.get_paginator("list_identity_sources")
        list_policies_paginator: ListPoliciesPaginator = client.get_paginator("list_policies")
        list_policy_stores_paginator: ListPolicyStoresPaginator = client.get_paginator("list_policy_stores")
        list_policy_templates_paginator: ListPolicyTemplatesPaginator = client.get_paginator("list_policy_templates")
    ```
"""

from typing import AsyncIterator, Generic, Iterator, Sequence, TypeVar

from aiobotocore.paginate import AioPaginator
from botocore.paginate import PageIterator

from .type_defs import (
    IdentitySourceFilterTypeDef,
    ListIdentitySourcesOutputTypeDef,
    ListPoliciesOutputTypeDef,
    ListPolicyStoresOutputTypeDef,
    ListPolicyTemplatesOutputTypeDef,
    PaginatorConfigTypeDef,
    PolicyFilterTypeDef,
)

__all__ = (
    "ListIdentitySourcesPaginator",
    "ListPoliciesPaginator",
    "ListPolicyStoresPaginator",
    "ListPolicyTemplatesPaginator",
)

_ItemTypeDef = TypeVar("_ItemTypeDef")

class _PageIterator(Generic[_ItemTypeDef], PageIterator):
    def __iter__(self) -> Iterator[_ItemTypeDef]:
        """
        Proxy method to specify iterator item type.
        """

class ListIdentitySourcesPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/verifiedpermissions.html#VerifiedPermissions.Paginator.ListIdentitySources)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_verifiedpermissions/paginators/#listidentitysourcespaginator)
    """

    def paginate(
        self,
        *,
        policyStoreId: str,
        filters: Sequence[IdentitySourceFilterTypeDef] = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListIdentitySourcesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/verifiedpermissions.html#VerifiedPermissions.Paginator.ListIdentitySources.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_verifiedpermissions/paginators/#listidentitysourcespaginator)
        """

class ListPoliciesPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/verifiedpermissions.html#VerifiedPermissions.Paginator.ListPolicies)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_verifiedpermissions/paginators/#listpoliciespaginator)
    """

    def paginate(
        self,
        *,
        policyStoreId: str,
        filter: PolicyFilterTypeDef = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListPoliciesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/verifiedpermissions.html#VerifiedPermissions.Paginator.ListPolicies.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_verifiedpermissions/paginators/#listpoliciespaginator)
        """

class ListPolicyStoresPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/verifiedpermissions.html#VerifiedPermissions.Paginator.ListPolicyStores)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_verifiedpermissions/paginators/#listpolicystorespaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListPolicyStoresOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/verifiedpermissions.html#VerifiedPermissions.Paginator.ListPolicyStores.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_verifiedpermissions/paginators/#listpolicystorespaginator)
        """

class ListPolicyTemplatesPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/verifiedpermissions.html#VerifiedPermissions.Paginator.ListPolicyTemplates)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_verifiedpermissions/paginators/#listpolicytemplatespaginator)
    """

    def paginate(
        self, *, policyStoreId: str, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListPolicyTemplatesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/verifiedpermissions.html#VerifiedPermissions.Paginator.ListPolicyTemplates.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_verifiedpermissions/paginators/#listpolicytemplatespaginator)
        """
