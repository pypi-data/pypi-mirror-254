"""
Type annotations for trustedadvisor service type definitions.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_trustedadvisor/type_defs/)

Usage::

    ```python
    from types_aiobotocore_trustedadvisor.type_defs import AccountRecommendationLifecycleSummaryTypeDef

    data: AccountRecommendationLifecycleSummaryTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Union

from .literals import (
    RecommendationLanguageType,
    RecommendationLifecycleStageType,
    RecommendationPillarType,
    RecommendationSourceType,
    RecommendationStatusType,
    RecommendationTypeType,
    ResourceStatusType,
    UpdateRecommendationLifecycleStageReasonCodeType,
    UpdateRecommendationLifecycleStageType,
)

if sys.version_info >= (3, 12):
    from typing import NotRequired
else:
    from typing_extensions import NotRequired
if sys.version_info >= (3, 12):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AccountRecommendationLifecycleSummaryTypeDef",
    "CheckSummaryTypeDef",
    "ResponseMetadataTypeDef",
    "GetOrganizationRecommendationRequestRequestTypeDef",
    "GetRecommendationRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "ListChecksRequestRequestTypeDef",
    "ListOrganizationRecommendationAccountsRequestRequestTypeDef",
    "ListOrganizationRecommendationResourcesRequestRequestTypeDef",
    "OrganizationRecommendationResourceSummaryTypeDef",
    "TimestampTypeDef",
    "ListRecommendationResourcesRequestRequestTypeDef",
    "RecommendationResourceSummaryTypeDef",
    "RecommendationResourcesAggregatesTypeDef",
    "RecommendationCostOptimizingAggregatesTypeDef",
    "UpdateOrganizationRecommendationLifecycleRequestRequestTypeDef",
    "UpdateRecommendationLifecycleRequestRequestTypeDef",
    "EmptyResponseMetadataTypeDef",
    "ListChecksResponseTypeDef",
    "ListOrganizationRecommendationAccountsResponseTypeDef",
    "ListChecksRequestListChecksPaginateTypeDef",
    "ListOrganizationRecommendationAccountsRequestListOrganizationRecommendationAccountsPaginateTypeDef",
    "ListOrganizationRecommendationResourcesRequestListOrganizationRecommendationResourcesPaginateTypeDef",
    "ListRecommendationResourcesRequestListRecommendationResourcesPaginateTypeDef",
    "ListOrganizationRecommendationResourcesResponseTypeDef",
    "ListOrganizationRecommendationsRequestListOrganizationRecommendationsPaginateTypeDef",
    "ListOrganizationRecommendationsRequestRequestTypeDef",
    "ListRecommendationsRequestListRecommendationsPaginateTypeDef",
    "ListRecommendationsRequestRequestTypeDef",
    "ListRecommendationResourcesResponseTypeDef",
    "RecommendationPillarSpecificAggregatesTypeDef",
    "OrganizationRecommendationSummaryTypeDef",
    "OrganizationRecommendationTypeDef",
    "RecommendationSummaryTypeDef",
    "RecommendationTypeDef",
    "ListOrganizationRecommendationsResponseTypeDef",
    "GetOrganizationRecommendationResponseTypeDef",
    "ListRecommendationsResponseTypeDef",
    "GetRecommendationResponseTypeDef",
)

AccountRecommendationLifecycleSummaryTypeDef = TypedDict(
    "AccountRecommendationLifecycleSummaryTypeDef",
    {
        "accountId": NotRequired[str],
        "accountRecommendationArn": NotRequired[str],
        "lastUpdatedAt": NotRequired[datetime],
        "lifecycleStage": NotRequired[RecommendationLifecycleStageType],
        "updateReason": NotRequired[str],
        "updateReasonCode": NotRequired[UpdateRecommendationLifecycleStageReasonCodeType],
        "updatedOnBehalfOf": NotRequired[str],
        "updatedOnBehalfOfJobTitle": NotRequired[str],
    },
)
CheckSummaryTypeDef = TypedDict(
    "CheckSummaryTypeDef",
    {
        "arn": str,
        "awsServices": List[str],
        "description": str,
        "id": str,
        "metadata": Dict[str, str],
        "name": str,
        "pillars": List[RecommendationPillarType],
        "source": RecommendationSourceType,
    },
)
ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, str],
        "RetryAttempts": int,
    },
)
GetOrganizationRecommendationRequestRequestTypeDef = TypedDict(
    "GetOrganizationRecommendationRequestRequestTypeDef",
    {
        "organizationRecommendationIdentifier": str,
    },
)
GetRecommendationRequestRequestTypeDef = TypedDict(
    "GetRecommendationRequestRequestTypeDef",
    {
        "recommendationIdentifier": str,
    },
)
PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": NotRequired[int],
        "PageSize": NotRequired[int],
        "StartingToken": NotRequired[str],
    },
)
ListChecksRequestRequestTypeDef = TypedDict(
    "ListChecksRequestRequestTypeDef",
    {
        "awsService": NotRequired[str],
        "language": NotRequired[RecommendationLanguageType],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "pillar": NotRequired[RecommendationPillarType],
        "source": NotRequired[RecommendationSourceType],
    },
)
ListOrganizationRecommendationAccountsRequestRequestTypeDef = TypedDict(
    "ListOrganizationRecommendationAccountsRequestRequestTypeDef",
    {
        "organizationRecommendationIdentifier": str,
        "affectedAccountId": NotRequired[str],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListOrganizationRecommendationResourcesRequestRequestTypeDef = TypedDict(
    "ListOrganizationRecommendationResourcesRequestRequestTypeDef",
    {
        "organizationRecommendationIdentifier": str,
        "affectedAccountId": NotRequired[str],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "regionCode": NotRequired[str],
        "status": NotRequired[ResourceStatusType],
    },
)
OrganizationRecommendationResourceSummaryTypeDef = TypedDict(
    "OrganizationRecommendationResourceSummaryTypeDef",
    {
        "arn": str,
        "awsResourceId": str,
        "id": str,
        "lastUpdatedAt": datetime,
        "metadata": Dict[str, str],
        "recommendationArn": str,
        "regionCode": str,
        "status": ResourceStatusType,
        "accountId": NotRequired[str],
    },
)
TimestampTypeDef = Union[datetime, str]
ListRecommendationResourcesRequestRequestTypeDef = TypedDict(
    "ListRecommendationResourcesRequestRequestTypeDef",
    {
        "recommendationIdentifier": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "regionCode": NotRequired[str],
        "status": NotRequired[ResourceStatusType],
    },
)
RecommendationResourceSummaryTypeDef = TypedDict(
    "RecommendationResourceSummaryTypeDef",
    {
        "arn": str,
        "awsResourceId": str,
        "id": str,
        "lastUpdatedAt": datetime,
        "metadata": Dict[str, str],
        "recommendationArn": str,
        "regionCode": str,
        "status": ResourceStatusType,
    },
)
RecommendationResourcesAggregatesTypeDef = TypedDict(
    "RecommendationResourcesAggregatesTypeDef",
    {
        "errorCount": int,
        "okCount": int,
        "warningCount": int,
    },
)
RecommendationCostOptimizingAggregatesTypeDef = TypedDict(
    "RecommendationCostOptimizingAggregatesTypeDef",
    {
        "estimatedMonthlySavings": float,
        "estimatedPercentMonthlySavings": float,
    },
)
UpdateOrganizationRecommendationLifecycleRequestRequestTypeDef = TypedDict(
    "UpdateOrganizationRecommendationLifecycleRequestRequestTypeDef",
    {
        "lifecycleStage": UpdateRecommendationLifecycleStageType,
        "organizationRecommendationIdentifier": str,
        "updateReason": NotRequired[str],
        "updateReasonCode": NotRequired[UpdateRecommendationLifecycleStageReasonCodeType],
    },
)
UpdateRecommendationLifecycleRequestRequestTypeDef = TypedDict(
    "UpdateRecommendationLifecycleRequestRequestTypeDef",
    {
        "lifecycleStage": UpdateRecommendationLifecycleStageType,
        "recommendationIdentifier": str,
        "updateReason": NotRequired[str],
        "updateReasonCode": NotRequired[UpdateRecommendationLifecycleStageReasonCodeType],
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListChecksResponseTypeDef = TypedDict(
    "ListChecksResponseTypeDef",
    {
        "checkSummaries": List[CheckSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListOrganizationRecommendationAccountsResponseTypeDef = TypedDict(
    "ListOrganizationRecommendationAccountsResponseTypeDef",
    {
        "accountRecommendationLifecycleSummaries": List[
            AccountRecommendationLifecycleSummaryTypeDef
        ],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListChecksRequestListChecksPaginateTypeDef = TypedDict(
    "ListChecksRequestListChecksPaginateTypeDef",
    {
        "awsService": NotRequired[str],
        "language": NotRequired[RecommendationLanguageType],
        "pillar": NotRequired[RecommendationPillarType],
        "source": NotRequired[RecommendationSourceType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListOrganizationRecommendationAccountsRequestListOrganizationRecommendationAccountsPaginateTypeDef = TypedDict(
    "ListOrganizationRecommendationAccountsRequestListOrganizationRecommendationAccountsPaginateTypeDef",
    {
        "organizationRecommendationIdentifier": str,
        "affectedAccountId": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListOrganizationRecommendationResourcesRequestListOrganizationRecommendationResourcesPaginateTypeDef = TypedDict(
    "ListOrganizationRecommendationResourcesRequestListOrganizationRecommendationResourcesPaginateTypeDef",
    {
        "organizationRecommendationIdentifier": str,
        "affectedAccountId": NotRequired[str],
        "regionCode": NotRequired[str],
        "status": NotRequired[ResourceStatusType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListRecommendationResourcesRequestListRecommendationResourcesPaginateTypeDef = TypedDict(
    "ListRecommendationResourcesRequestListRecommendationResourcesPaginateTypeDef",
    {
        "recommendationIdentifier": str,
        "regionCode": NotRequired[str],
        "status": NotRequired[ResourceStatusType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListOrganizationRecommendationResourcesResponseTypeDef = TypedDict(
    "ListOrganizationRecommendationResourcesResponseTypeDef",
    {
        "nextToken": str,
        "organizationRecommendationResourceSummaries": List[
            OrganizationRecommendationResourceSummaryTypeDef
        ],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListOrganizationRecommendationsRequestListOrganizationRecommendationsPaginateTypeDef = TypedDict(
    "ListOrganizationRecommendationsRequestListOrganizationRecommendationsPaginateTypeDef",
    {
        "afterLastUpdatedAt": NotRequired[TimestampTypeDef],
        "awsService": NotRequired[str],
        "beforeLastUpdatedAt": NotRequired[TimestampTypeDef],
        "checkIdentifier": NotRequired[str],
        "pillar": NotRequired[RecommendationPillarType],
        "source": NotRequired[RecommendationSourceType],
        "status": NotRequired[RecommendationStatusType],
        "type": NotRequired[RecommendationTypeType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListOrganizationRecommendationsRequestRequestTypeDef = TypedDict(
    "ListOrganizationRecommendationsRequestRequestTypeDef",
    {
        "afterLastUpdatedAt": NotRequired[TimestampTypeDef],
        "awsService": NotRequired[str],
        "beforeLastUpdatedAt": NotRequired[TimestampTypeDef],
        "checkIdentifier": NotRequired[str],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "pillar": NotRequired[RecommendationPillarType],
        "source": NotRequired[RecommendationSourceType],
        "status": NotRequired[RecommendationStatusType],
        "type": NotRequired[RecommendationTypeType],
    },
)
ListRecommendationsRequestListRecommendationsPaginateTypeDef = TypedDict(
    "ListRecommendationsRequestListRecommendationsPaginateTypeDef",
    {
        "afterLastUpdatedAt": NotRequired[TimestampTypeDef],
        "awsService": NotRequired[str],
        "beforeLastUpdatedAt": NotRequired[TimestampTypeDef],
        "checkIdentifier": NotRequired[str],
        "pillar": NotRequired[RecommendationPillarType],
        "source": NotRequired[RecommendationSourceType],
        "status": NotRequired[RecommendationStatusType],
        "type": NotRequired[RecommendationTypeType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListRecommendationsRequestRequestTypeDef = TypedDict(
    "ListRecommendationsRequestRequestTypeDef",
    {
        "afterLastUpdatedAt": NotRequired[TimestampTypeDef],
        "awsService": NotRequired[str],
        "beforeLastUpdatedAt": NotRequired[TimestampTypeDef],
        "checkIdentifier": NotRequired[str],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "pillar": NotRequired[RecommendationPillarType],
        "source": NotRequired[RecommendationSourceType],
        "status": NotRequired[RecommendationStatusType],
        "type": NotRequired[RecommendationTypeType],
    },
)
ListRecommendationResourcesResponseTypeDef = TypedDict(
    "ListRecommendationResourcesResponseTypeDef",
    {
        "nextToken": str,
        "recommendationResourceSummaries": List[RecommendationResourceSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RecommendationPillarSpecificAggregatesTypeDef = TypedDict(
    "RecommendationPillarSpecificAggregatesTypeDef",
    {
        "costOptimizing": NotRequired[RecommendationCostOptimizingAggregatesTypeDef],
    },
)
OrganizationRecommendationSummaryTypeDef = TypedDict(
    "OrganizationRecommendationSummaryTypeDef",
    {
        "arn": str,
        "id": str,
        "name": str,
        "pillars": List[RecommendationPillarType],
        "resourcesAggregates": RecommendationResourcesAggregatesTypeDef,
        "source": RecommendationSourceType,
        "status": RecommendationStatusType,
        "type": RecommendationTypeType,
        "awsServices": NotRequired[List[str]],
        "checkArn": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "lastUpdatedAt": NotRequired[datetime],
        "lifecycleStage": NotRequired[RecommendationLifecycleStageType],
        "pillarSpecificAggregates": NotRequired[RecommendationPillarSpecificAggregatesTypeDef],
    },
)
OrganizationRecommendationTypeDef = TypedDict(
    "OrganizationRecommendationTypeDef",
    {
        "arn": str,
        "description": str,
        "id": str,
        "name": str,
        "pillars": List[RecommendationPillarType],
        "resourcesAggregates": RecommendationResourcesAggregatesTypeDef,
        "source": RecommendationSourceType,
        "status": RecommendationStatusType,
        "type": RecommendationTypeType,
        "awsServices": NotRequired[List[str]],
        "checkArn": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "createdBy": NotRequired[str],
        "lastUpdatedAt": NotRequired[datetime],
        "lifecycleStage": NotRequired[RecommendationLifecycleStageType],
        "pillarSpecificAggregates": NotRequired[RecommendationPillarSpecificAggregatesTypeDef],
        "resolvedAt": NotRequired[datetime],
        "updateReason": NotRequired[str],
        "updateReasonCode": NotRequired[UpdateRecommendationLifecycleStageReasonCodeType],
        "updatedOnBehalfOf": NotRequired[str],
        "updatedOnBehalfOfJobTitle": NotRequired[str],
    },
)
RecommendationSummaryTypeDef = TypedDict(
    "RecommendationSummaryTypeDef",
    {
        "arn": str,
        "id": str,
        "name": str,
        "pillars": List[RecommendationPillarType],
        "resourcesAggregates": RecommendationResourcesAggregatesTypeDef,
        "source": RecommendationSourceType,
        "status": RecommendationStatusType,
        "type": RecommendationTypeType,
        "awsServices": NotRequired[List[str]],
        "checkArn": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "lastUpdatedAt": NotRequired[datetime],
        "lifecycleStage": NotRequired[RecommendationLifecycleStageType],
        "pillarSpecificAggregates": NotRequired[RecommendationPillarSpecificAggregatesTypeDef],
    },
)
RecommendationTypeDef = TypedDict(
    "RecommendationTypeDef",
    {
        "arn": str,
        "description": str,
        "id": str,
        "name": str,
        "pillars": List[RecommendationPillarType],
        "resourcesAggregates": RecommendationResourcesAggregatesTypeDef,
        "source": RecommendationSourceType,
        "status": RecommendationStatusType,
        "type": RecommendationTypeType,
        "awsServices": NotRequired[List[str]],
        "checkArn": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "createdBy": NotRequired[str],
        "lastUpdatedAt": NotRequired[datetime],
        "lifecycleStage": NotRequired[RecommendationLifecycleStageType],
        "pillarSpecificAggregates": NotRequired[RecommendationPillarSpecificAggregatesTypeDef],
        "resolvedAt": NotRequired[datetime],
        "updateReason": NotRequired[str],
        "updateReasonCode": NotRequired[UpdateRecommendationLifecycleStageReasonCodeType],
        "updatedOnBehalfOf": NotRequired[str],
        "updatedOnBehalfOfJobTitle": NotRequired[str],
    },
)
ListOrganizationRecommendationsResponseTypeDef = TypedDict(
    "ListOrganizationRecommendationsResponseTypeDef",
    {
        "nextToken": str,
        "organizationRecommendationSummaries": List[OrganizationRecommendationSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetOrganizationRecommendationResponseTypeDef = TypedDict(
    "GetOrganizationRecommendationResponseTypeDef",
    {
        "organizationRecommendation": OrganizationRecommendationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListRecommendationsResponseTypeDef = TypedDict(
    "ListRecommendationsResponseTypeDef",
    {
        "nextToken": str,
        "recommendationSummaries": List[RecommendationSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetRecommendationResponseTypeDef = TypedDict(
    "GetRecommendationResponseTypeDef",
    {
        "recommendation": RecommendationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
