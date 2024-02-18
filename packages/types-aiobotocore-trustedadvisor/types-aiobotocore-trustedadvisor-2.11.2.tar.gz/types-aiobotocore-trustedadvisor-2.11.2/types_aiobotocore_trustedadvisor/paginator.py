"""
Type annotations for trustedadvisor service client paginators.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_trustedadvisor/paginators/)

Usage::

    ```python
    from aiobotocore.session import get_session

    from types_aiobotocore_trustedadvisor.client import TrustedAdvisorPublicAPIClient
    from types_aiobotocore_trustedadvisor.paginator import (
        ListChecksPaginator,
        ListOrganizationRecommendationAccountsPaginator,
        ListOrganizationRecommendationResourcesPaginator,
        ListOrganizationRecommendationsPaginator,
        ListRecommendationResourcesPaginator,
        ListRecommendationsPaginator,
    )

    session = get_session()
    with session.create_client("trustedadvisor") as client:
        client: TrustedAdvisorPublicAPIClient

        list_checks_paginator: ListChecksPaginator = client.get_paginator("list_checks")
        list_organization_recommendation_accounts_paginator: ListOrganizationRecommendationAccountsPaginator = client.get_paginator("list_organization_recommendation_accounts")
        list_organization_recommendation_resources_paginator: ListOrganizationRecommendationResourcesPaginator = client.get_paginator("list_organization_recommendation_resources")
        list_organization_recommendations_paginator: ListOrganizationRecommendationsPaginator = client.get_paginator("list_organization_recommendations")
        list_recommendation_resources_paginator: ListRecommendationResourcesPaginator = client.get_paginator("list_recommendation_resources")
        list_recommendations_paginator: ListRecommendationsPaginator = client.get_paginator("list_recommendations")
    ```
"""

from typing import AsyncIterator, Generic, Iterator, TypeVar

from aiobotocore.paginate import AioPaginator
from botocore.paginate import PageIterator

from .literals import (
    RecommendationLanguageType,
    RecommendationPillarType,
    RecommendationSourceType,
    RecommendationStatusType,
    RecommendationTypeType,
    ResourceStatusType,
)
from .type_defs import (
    ListChecksResponseTypeDef,
    ListOrganizationRecommendationAccountsResponseTypeDef,
    ListOrganizationRecommendationResourcesResponseTypeDef,
    ListOrganizationRecommendationsResponseTypeDef,
    ListRecommendationResourcesResponseTypeDef,
    ListRecommendationsResponseTypeDef,
    PaginatorConfigTypeDef,
    TimestampTypeDef,
)

__all__ = (
    "ListChecksPaginator",
    "ListOrganizationRecommendationAccountsPaginator",
    "ListOrganizationRecommendationResourcesPaginator",
    "ListOrganizationRecommendationsPaginator",
    "ListRecommendationResourcesPaginator",
    "ListRecommendationsPaginator",
)

_ItemTypeDef = TypeVar("_ItemTypeDef")


class _PageIterator(Generic[_ItemTypeDef], PageIterator):
    def __iter__(self) -> Iterator[_ItemTypeDef]:
        """
        Proxy method to specify iterator item type.
        """


class ListChecksPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/trustedadvisor.html#TrustedAdvisorPublicAPI.Paginator.ListChecks)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_trustedadvisor/paginators/#listcheckspaginator)
    """

    def paginate(
        self,
        *,
        awsService: str = ...,
        language: RecommendationLanguageType = ...,
        pillar: RecommendationPillarType = ...,
        source: RecommendationSourceType = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListChecksResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/trustedadvisor.html#TrustedAdvisorPublicAPI.Paginator.ListChecks.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_trustedadvisor/paginators/#listcheckspaginator)
        """


class ListOrganizationRecommendationAccountsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/trustedadvisor.html#TrustedAdvisorPublicAPI.Paginator.ListOrganizationRecommendationAccounts)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_trustedadvisor/paginators/#listorganizationrecommendationaccountspaginator)
    """

    def paginate(
        self,
        *,
        organizationRecommendationIdentifier: str,
        affectedAccountId: str = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListOrganizationRecommendationAccountsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/trustedadvisor.html#TrustedAdvisorPublicAPI.Paginator.ListOrganizationRecommendationAccounts.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_trustedadvisor/paginators/#listorganizationrecommendationaccountspaginator)
        """


class ListOrganizationRecommendationResourcesPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/trustedadvisor.html#TrustedAdvisorPublicAPI.Paginator.ListOrganizationRecommendationResources)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_trustedadvisor/paginators/#listorganizationrecommendationresourcespaginator)
    """

    def paginate(
        self,
        *,
        organizationRecommendationIdentifier: str,
        affectedAccountId: str = ...,
        regionCode: str = ...,
        status: ResourceStatusType = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListOrganizationRecommendationResourcesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/trustedadvisor.html#TrustedAdvisorPublicAPI.Paginator.ListOrganizationRecommendationResources.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_trustedadvisor/paginators/#listorganizationrecommendationresourcespaginator)
        """


class ListOrganizationRecommendationsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/trustedadvisor.html#TrustedAdvisorPublicAPI.Paginator.ListOrganizationRecommendations)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_trustedadvisor/paginators/#listorganizationrecommendationspaginator)
    """

    def paginate(
        self,
        *,
        afterLastUpdatedAt: TimestampTypeDef = ...,
        awsService: str = ...,
        beforeLastUpdatedAt: TimestampTypeDef = ...,
        checkIdentifier: str = ...,
        pillar: RecommendationPillarType = ...,
        source: RecommendationSourceType = ...,
        status: RecommendationStatusType = ...,
        type: RecommendationTypeType = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListOrganizationRecommendationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/trustedadvisor.html#TrustedAdvisorPublicAPI.Paginator.ListOrganizationRecommendations.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_trustedadvisor/paginators/#listorganizationrecommendationspaginator)
        """


class ListRecommendationResourcesPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/trustedadvisor.html#TrustedAdvisorPublicAPI.Paginator.ListRecommendationResources)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_trustedadvisor/paginators/#listrecommendationresourcespaginator)
    """

    def paginate(
        self,
        *,
        recommendationIdentifier: str,
        regionCode: str = ...,
        status: ResourceStatusType = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListRecommendationResourcesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/trustedadvisor.html#TrustedAdvisorPublicAPI.Paginator.ListRecommendationResources.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_trustedadvisor/paginators/#listrecommendationresourcespaginator)
        """


class ListRecommendationsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/trustedadvisor.html#TrustedAdvisorPublicAPI.Paginator.ListRecommendations)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_trustedadvisor/paginators/#listrecommendationspaginator)
    """

    def paginate(
        self,
        *,
        afterLastUpdatedAt: TimestampTypeDef = ...,
        awsService: str = ...,
        beforeLastUpdatedAt: TimestampTypeDef = ...,
        checkIdentifier: str = ...,
        pillar: RecommendationPillarType = ...,
        source: RecommendationSourceType = ...,
        status: RecommendationStatusType = ...,
        type: RecommendationTypeType = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListRecommendationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/trustedadvisor.html#TrustedAdvisorPublicAPI.Paginator.ListRecommendations.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_trustedadvisor/paginators/#listrecommendationspaginator)
        """
