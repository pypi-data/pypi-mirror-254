"""
Type annotations for compute-optimizer service client paginators.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_compute_optimizer/paginators/)

Usage::

    ```python
    from aiobotocore.session import get_session

    from types_aiobotocore_compute_optimizer.client import ComputeOptimizerClient
    from types_aiobotocore_compute_optimizer.paginator import (
        DescribeRecommendationExportJobsPaginator,
        GetEnrollmentStatusesForOrganizationPaginator,
        GetLambdaFunctionRecommendationsPaginator,
        GetRecommendationPreferencesPaginator,
        GetRecommendationSummariesPaginator,
    )

    session = get_session()
    with session.create_client("compute-optimizer") as client:
        client: ComputeOptimizerClient

        describe_recommendation_export_jobs_paginator: DescribeRecommendationExportJobsPaginator = client.get_paginator("describe_recommendation_export_jobs")
        get_enrollment_statuses_for_organization_paginator: GetEnrollmentStatusesForOrganizationPaginator = client.get_paginator("get_enrollment_statuses_for_organization")
        get_lambda_function_recommendations_paginator: GetLambdaFunctionRecommendationsPaginator = client.get_paginator("get_lambda_function_recommendations")
        get_recommendation_preferences_paginator: GetRecommendationPreferencesPaginator = client.get_paginator("get_recommendation_preferences")
        get_recommendation_summaries_paginator: GetRecommendationSummariesPaginator = client.get_paginator("get_recommendation_summaries")
    ```
"""

from typing import AsyncIterator, Generic, Iterator, Sequence, TypeVar

from aiobotocore.paginate import AioPaginator
from botocore.paginate import PageIterator

from .literals import ResourceTypeType
from .type_defs import (
    DescribeRecommendationExportJobsResponseTypeDef,
    EnrollmentFilterTypeDef,
    GetEnrollmentStatusesForOrganizationResponseTypeDef,
    GetLambdaFunctionRecommendationsResponseTypeDef,
    GetRecommendationPreferencesResponseTypeDef,
    GetRecommendationSummariesResponseTypeDef,
    JobFilterTypeDef,
    LambdaFunctionRecommendationFilterTypeDef,
    PaginatorConfigTypeDef,
    ScopeTypeDef,
)

__all__ = (
    "DescribeRecommendationExportJobsPaginator",
    "GetEnrollmentStatusesForOrganizationPaginator",
    "GetLambdaFunctionRecommendationsPaginator",
    "GetRecommendationPreferencesPaginator",
    "GetRecommendationSummariesPaginator",
)

_ItemTypeDef = TypeVar("_ItemTypeDef")

class _PageIterator(Generic[_ItemTypeDef], PageIterator):
    def __iter__(self) -> Iterator[_ItemTypeDef]:
        """
        Proxy method to specify iterator item type.
        """

class DescribeRecommendationExportJobsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer.html#ComputeOptimizer.Paginator.DescribeRecommendationExportJobs)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_compute_optimizer/paginators/#describerecommendationexportjobspaginator)
    """

    def paginate(
        self,
        *,
        jobIds: Sequence[str] = ...,
        filters: Sequence[JobFilterTypeDef] = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[DescribeRecommendationExportJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer.html#ComputeOptimizer.Paginator.DescribeRecommendationExportJobs.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_compute_optimizer/paginators/#describerecommendationexportjobspaginator)
        """

class GetEnrollmentStatusesForOrganizationPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer.html#ComputeOptimizer.Paginator.GetEnrollmentStatusesForOrganization)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_compute_optimizer/paginators/#getenrollmentstatusesfororganizationpaginator)
    """

    def paginate(
        self,
        *,
        filters: Sequence[EnrollmentFilterTypeDef] = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[GetEnrollmentStatusesForOrganizationResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer.html#ComputeOptimizer.Paginator.GetEnrollmentStatusesForOrganization.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_compute_optimizer/paginators/#getenrollmentstatusesfororganizationpaginator)
        """

class GetLambdaFunctionRecommendationsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer.html#ComputeOptimizer.Paginator.GetLambdaFunctionRecommendations)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_compute_optimizer/paginators/#getlambdafunctionrecommendationspaginator)
    """

    def paginate(
        self,
        *,
        functionArns: Sequence[str] = ...,
        accountIds: Sequence[str] = ...,
        filters: Sequence[LambdaFunctionRecommendationFilterTypeDef] = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[GetLambdaFunctionRecommendationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer.html#ComputeOptimizer.Paginator.GetLambdaFunctionRecommendations.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_compute_optimizer/paginators/#getlambdafunctionrecommendationspaginator)
        """

class GetRecommendationPreferencesPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer.html#ComputeOptimizer.Paginator.GetRecommendationPreferences)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_compute_optimizer/paginators/#getrecommendationpreferencespaginator)
    """

    def paginate(
        self,
        *,
        resourceType: ResourceTypeType,
        scope: ScopeTypeDef = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[GetRecommendationPreferencesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer.html#ComputeOptimizer.Paginator.GetRecommendationPreferences.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_compute_optimizer/paginators/#getrecommendationpreferencespaginator)
        """

class GetRecommendationSummariesPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer.html#ComputeOptimizer.Paginator.GetRecommendationSummaries)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_compute_optimizer/paginators/#getrecommendationsummariespaginator)
    """

    def paginate(
        self, *, accountIds: Sequence[str] = ..., PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[GetRecommendationSummariesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer.html#ComputeOptimizer.Paginator.GetRecommendationSummaries.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_compute_optimizer/paginators/#getrecommendationsummariespaginator)
        """
