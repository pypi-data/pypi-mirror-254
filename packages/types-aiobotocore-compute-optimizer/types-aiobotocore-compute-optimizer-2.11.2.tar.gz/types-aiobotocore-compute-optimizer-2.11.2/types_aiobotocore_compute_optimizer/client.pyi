"""
Type annotations for compute-optimizer service client.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_compute_optimizer/client/)

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_compute_optimizer.client import ComputeOptimizerClient

    session = get_session()
    async with session.create_client("compute-optimizer") as client:
        client: ComputeOptimizerClient
    ```
"""

import sys
from typing import Any, Dict, Mapping, Sequence, Type, overload

from aiobotocore.client import AioBaseClient
from botocore.client import ClientMeta

from .literals import (
    EnhancedInfrastructureMetricsType,
    ExportableAutoScalingGroupFieldType,
    ExportableECSServiceFieldType,
    ExportableInstanceFieldType,
    ExportableLambdaFunctionFieldType,
    ExportableLicenseFieldType,
    ExportableVolumeFieldType,
    InferredWorkloadTypesPreferenceType,
    LookBackPeriodPreferenceType,
    MetricStatisticType,
    RecommendationPreferenceNameType,
    ResourceTypeType,
    SavingsEstimationModeType,
    StatusType,
)
from .paginator import (
    DescribeRecommendationExportJobsPaginator,
    GetEnrollmentStatusesForOrganizationPaginator,
    GetLambdaFunctionRecommendationsPaginator,
    GetRecommendationPreferencesPaginator,
    GetRecommendationSummariesPaginator,
)
from .type_defs import (
    DescribeRecommendationExportJobsResponseTypeDef,
    EBSFilterTypeDef,
    ECSServiceRecommendationFilterTypeDef,
    EnrollmentFilterTypeDef,
    ExportAutoScalingGroupRecommendationsResponseTypeDef,
    ExportEBSVolumeRecommendationsResponseTypeDef,
    ExportEC2InstanceRecommendationsResponseTypeDef,
    ExportECSServiceRecommendationsResponseTypeDef,
    ExportLambdaFunctionRecommendationsResponseTypeDef,
    ExportLicenseRecommendationsResponseTypeDef,
    ExternalMetricsPreferenceTypeDef,
    FilterTypeDef,
    GetAutoScalingGroupRecommendationsResponseTypeDef,
    GetEBSVolumeRecommendationsResponseTypeDef,
    GetEC2InstanceRecommendationsResponseTypeDef,
    GetEC2RecommendationProjectedMetricsResponseTypeDef,
    GetECSServiceRecommendationProjectedMetricsResponseTypeDef,
    GetECSServiceRecommendationsResponseTypeDef,
    GetEffectiveRecommendationPreferencesResponseTypeDef,
    GetEnrollmentStatusesForOrganizationResponseTypeDef,
    GetEnrollmentStatusResponseTypeDef,
    GetLambdaFunctionRecommendationsResponseTypeDef,
    GetLicenseRecommendationsResponseTypeDef,
    GetRecommendationPreferencesResponseTypeDef,
    GetRecommendationSummariesResponseTypeDef,
    JobFilterTypeDef,
    LambdaFunctionRecommendationFilterTypeDef,
    LicenseRecommendationFilterTypeDef,
    PreferredResourceTypeDef,
    RecommendationPreferencesTypeDef,
    S3DestinationConfigTypeDef,
    ScopeTypeDef,
    TimestampTypeDef,
    UpdateEnrollmentStatusResponseTypeDef,
    UtilizationPreferenceTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("ComputeOptimizerClient",)

class BotocoreClientError(Exception):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    InvalidParameterValueException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    MissingAuthenticationToken: Type[BotocoreClientError]
    OptInRequiredException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceUnavailableException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]

class ComputeOptimizerClient(AioBaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer.html#ComputeOptimizer.Client)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_compute_optimizer/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        ComputeOptimizerClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer.html#ComputeOptimizer.Client.exceptions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_compute_optimizer/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer.html#ComputeOptimizer.Client.can_paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_compute_optimizer/client/#can_paginate)
        """

    async def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer.html#ComputeOptimizer.Client.close)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_compute_optimizer/client/#close)
        """

    async def delete_recommendation_preferences(
        self,
        *,
        resourceType: ResourceTypeType,
        recommendationPreferenceNames: Sequence[RecommendationPreferenceNameType],
        scope: ScopeTypeDef = ...,
    ) -> Dict[str, Any]:
        """
        Deletes a recommendation preference, such as enhanced infrastructure metrics.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer.html#ComputeOptimizer.Client.delete_recommendation_preferences)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_compute_optimizer/client/#delete_recommendation_preferences)
        """

    async def describe_recommendation_export_jobs(
        self,
        *,
        jobIds: Sequence[str] = ...,
        filters: Sequence[JobFilterTypeDef] = ...,
        nextToken: str = ...,
        maxResults: int = ...,
    ) -> DescribeRecommendationExportJobsResponseTypeDef:
        """
        Describes recommendation export jobs created in the last seven days.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer.html#ComputeOptimizer.Client.describe_recommendation_export_jobs)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_compute_optimizer/client/#describe_recommendation_export_jobs)
        """

    async def export_auto_scaling_group_recommendations(
        self,
        *,
        s3DestinationConfig: S3DestinationConfigTypeDef,
        accountIds: Sequence[str] = ...,
        filters: Sequence[FilterTypeDef] = ...,
        fieldsToExport: Sequence[ExportableAutoScalingGroupFieldType] = ...,
        fileFormat: Literal["Csv"] = ...,
        includeMemberAccounts: bool = ...,
        recommendationPreferences: RecommendationPreferencesTypeDef = ...,
    ) -> ExportAutoScalingGroupRecommendationsResponseTypeDef:
        """
        Exports optimization recommendations for Auto Scaling groups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer.html#ComputeOptimizer.Client.export_auto_scaling_group_recommendations)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_compute_optimizer/client/#export_auto_scaling_group_recommendations)
        """

    async def export_ebs_volume_recommendations(
        self,
        *,
        s3DestinationConfig: S3DestinationConfigTypeDef,
        accountIds: Sequence[str] = ...,
        filters: Sequence[EBSFilterTypeDef] = ...,
        fieldsToExport: Sequence[ExportableVolumeFieldType] = ...,
        fileFormat: Literal["Csv"] = ...,
        includeMemberAccounts: bool = ...,
    ) -> ExportEBSVolumeRecommendationsResponseTypeDef:
        """
        Exports optimization recommendations for Amazon EBS volumes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer.html#ComputeOptimizer.Client.export_ebs_volume_recommendations)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_compute_optimizer/client/#export_ebs_volume_recommendations)
        """

    async def export_ec2_instance_recommendations(
        self,
        *,
        s3DestinationConfig: S3DestinationConfigTypeDef,
        accountIds: Sequence[str] = ...,
        filters: Sequence[FilterTypeDef] = ...,
        fieldsToExport: Sequence[ExportableInstanceFieldType] = ...,
        fileFormat: Literal["Csv"] = ...,
        includeMemberAccounts: bool = ...,
        recommendationPreferences: RecommendationPreferencesTypeDef = ...,
    ) -> ExportEC2InstanceRecommendationsResponseTypeDef:
        """
        Exports optimization recommendations for Amazon EC2 instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer.html#ComputeOptimizer.Client.export_ec2_instance_recommendations)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_compute_optimizer/client/#export_ec2_instance_recommendations)
        """

    async def export_ecs_service_recommendations(
        self,
        *,
        s3DestinationConfig: S3DestinationConfigTypeDef,
        accountIds: Sequence[str] = ...,
        filters: Sequence[ECSServiceRecommendationFilterTypeDef] = ...,
        fieldsToExport: Sequence[ExportableECSServiceFieldType] = ...,
        fileFormat: Literal["Csv"] = ...,
        includeMemberAccounts: bool = ...,
    ) -> ExportECSServiceRecommendationsResponseTypeDef:
        """
        Exports optimization recommendations for Amazon ECS services on Fargate.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer.html#ComputeOptimizer.Client.export_ecs_service_recommendations)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_compute_optimizer/client/#export_ecs_service_recommendations)
        """

    async def export_lambda_function_recommendations(
        self,
        *,
        s3DestinationConfig: S3DestinationConfigTypeDef,
        accountIds: Sequence[str] = ...,
        filters: Sequence[LambdaFunctionRecommendationFilterTypeDef] = ...,
        fieldsToExport: Sequence[ExportableLambdaFunctionFieldType] = ...,
        fileFormat: Literal["Csv"] = ...,
        includeMemberAccounts: bool = ...,
    ) -> ExportLambdaFunctionRecommendationsResponseTypeDef:
        """
        Exports optimization recommendations for Lambda functions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer.html#ComputeOptimizer.Client.export_lambda_function_recommendations)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_compute_optimizer/client/#export_lambda_function_recommendations)
        """

    async def export_license_recommendations(
        self,
        *,
        s3DestinationConfig: S3DestinationConfigTypeDef,
        accountIds: Sequence[str] = ...,
        filters: Sequence[LicenseRecommendationFilterTypeDef] = ...,
        fieldsToExport: Sequence[ExportableLicenseFieldType] = ...,
        fileFormat: Literal["Csv"] = ...,
        includeMemberAccounts: bool = ...,
    ) -> ExportLicenseRecommendationsResponseTypeDef:
        """
        Export optimization recommendations for your licenses.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer.html#ComputeOptimizer.Client.export_license_recommendations)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_compute_optimizer/client/#export_license_recommendations)
        """

    async def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer.html#ComputeOptimizer.Client.generate_presigned_url)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_compute_optimizer/client/#generate_presigned_url)
        """

    async def get_auto_scaling_group_recommendations(
        self,
        *,
        accountIds: Sequence[str] = ...,
        autoScalingGroupArns: Sequence[str] = ...,
        nextToken: str = ...,
        maxResults: int = ...,
        filters: Sequence[FilterTypeDef] = ...,
        recommendationPreferences: RecommendationPreferencesTypeDef = ...,
    ) -> GetAutoScalingGroupRecommendationsResponseTypeDef:
        """
        Returns Auto Scaling group recommendations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer.html#ComputeOptimizer.Client.get_auto_scaling_group_recommendations)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_compute_optimizer/client/#get_auto_scaling_group_recommendations)
        """

    async def get_ebs_volume_recommendations(
        self,
        *,
        volumeArns: Sequence[str] = ...,
        nextToken: str = ...,
        maxResults: int = ...,
        filters: Sequence[EBSFilterTypeDef] = ...,
        accountIds: Sequence[str] = ...,
    ) -> GetEBSVolumeRecommendationsResponseTypeDef:
        """
        Returns Amazon Elastic Block Store (Amazon EBS) volume recommendations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer.html#ComputeOptimizer.Client.get_ebs_volume_recommendations)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_compute_optimizer/client/#get_ebs_volume_recommendations)
        """

    async def get_ec2_instance_recommendations(
        self,
        *,
        instanceArns: Sequence[str] = ...,
        nextToken: str = ...,
        maxResults: int = ...,
        filters: Sequence[FilterTypeDef] = ...,
        accountIds: Sequence[str] = ...,
        recommendationPreferences: RecommendationPreferencesTypeDef = ...,
    ) -> GetEC2InstanceRecommendationsResponseTypeDef:
        """
        Returns Amazon EC2 instance recommendations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer.html#ComputeOptimizer.Client.get_ec2_instance_recommendations)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_compute_optimizer/client/#get_ec2_instance_recommendations)
        """

    async def get_ec2_recommendation_projected_metrics(
        self,
        *,
        instanceArn: str,
        stat: MetricStatisticType,
        period: int,
        startTime: TimestampTypeDef,
        endTime: TimestampTypeDef,
        recommendationPreferences: RecommendationPreferencesTypeDef = ...,
    ) -> GetEC2RecommendationProjectedMetricsResponseTypeDef:
        """
        Returns the projected utilization metrics of Amazon EC2 instance
        recommendations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer.html#ComputeOptimizer.Client.get_ec2_recommendation_projected_metrics)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_compute_optimizer/client/#get_ec2_recommendation_projected_metrics)
        """

    async def get_ecs_service_recommendation_projected_metrics(
        self,
        *,
        serviceArn: str,
        stat: MetricStatisticType,
        period: int,
        startTime: TimestampTypeDef,
        endTime: TimestampTypeDef,
    ) -> GetECSServiceRecommendationProjectedMetricsResponseTypeDef:
        """
        Returns the projected metrics of Amazon ECS service recommendations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer.html#ComputeOptimizer.Client.get_ecs_service_recommendation_projected_metrics)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_compute_optimizer/client/#get_ecs_service_recommendation_projected_metrics)
        """

    async def get_ecs_service_recommendations(
        self,
        *,
        serviceArns: Sequence[str] = ...,
        nextToken: str = ...,
        maxResults: int = ...,
        filters: Sequence[ECSServiceRecommendationFilterTypeDef] = ...,
        accountIds: Sequence[str] = ...,
    ) -> GetECSServiceRecommendationsResponseTypeDef:
        """
        Returns Amazon ECS service recommendations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer.html#ComputeOptimizer.Client.get_ecs_service_recommendations)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_compute_optimizer/client/#get_ecs_service_recommendations)
        """

    async def get_effective_recommendation_preferences(
        self, *, resourceArn: str
    ) -> GetEffectiveRecommendationPreferencesResponseTypeDef:
        """
        Returns the recommendation preferences that are in effect for a given resource,
        such as enhanced infrastructure
        metrics.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer.html#ComputeOptimizer.Client.get_effective_recommendation_preferences)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_compute_optimizer/client/#get_effective_recommendation_preferences)
        """

    async def get_enrollment_status(self) -> GetEnrollmentStatusResponseTypeDef:
        """
        Returns the enrollment (opt in) status of an account to the Compute Optimizer
        service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer.html#ComputeOptimizer.Client.get_enrollment_status)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_compute_optimizer/client/#get_enrollment_status)
        """

    async def get_enrollment_statuses_for_organization(
        self,
        *,
        filters: Sequence[EnrollmentFilterTypeDef] = ...,
        nextToken: str = ...,
        maxResults: int = ...,
    ) -> GetEnrollmentStatusesForOrganizationResponseTypeDef:
        """
        Returns the Compute Optimizer enrollment (opt-in) status of organization member
        accounts, if your account is an organization management
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer.html#ComputeOptimizer.Client.get_enrollment_statuses_for_organization)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_compute_optimizer/client/#get_enrollment_statuses_for_organization)
        """

    async def get_lambda_function_recommendations(
        self,
        *,
        functionArns: Sequence[str] = ...,
        accountIds: Sequence[str] = ...,
        filters: Sequence[LambdaFunctionRecommendationFilterTypeDef] = ...,
        nextToken: str = ...,
        maxResults: int = ...,
    ) -> GetLambdaFunctionRecommendationsResponseTypeDef:
        """
        Returns Lambda function recommendations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer.html#ComputeOptimizer.Client.get_lambda_function_recommendations)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_compute_optimizer/client/#get_lambda_function_recommendations)
        """

    async def get_license_recommendations(
        self,
        *,
        resourceArns: Sequence[str] = ...,
        nextToken: str = ...,
        maxResults: int = ...,
        filters: Sequence[LicenseRecommendationFilterTypeDef] = ...,
        accountIds: Sequence[str] = ...,
    ) -> GetLicenseRecommendationsResponseTypeDef:
        """
        Returns license recommendations for Amazon EC2 instances that run on a specific
        license.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer.html#ComputeOptimizer.Client.get_license_recommendations)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_compute_optimizer/client/#get_license_recommendations)
        """

    async def get_recommendation_preferences(
        self,
        *,
        resourceType: ResourceTypeType,
        scope: ScopeTypeDef = ...,
        nextToken: str = ...,
        maxResults: int = ...,
    ) -> GetRecommendationPreferencesResponseTypeDef:
        """
        Returns existing recommendation preferences, such as enhanced infrastructure
        metrics.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer.html#ComputeOptimizer.Client.get_recommendation_preferences)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_compute_optimizer/client/#get_recommendation_preferences)
        """

    async def get_recommendation_summaries(
        self, *, accountIds: Sequence[str] = ..., nextToken: str = ..., maxResults: int = ...
    ) -> GetRecommendationSummariesResponseTypeDef:
        """
        Returns the optimization findings for an account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer.html#ComputeOptimizer.Client.get_recommendation_summaries)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_compute_optimizer/client/#get_recommendation_summaries)
        """

    async def put_recommendation_preferences(
        self,
        *,
        resourceType: ResourceTypeType,
        scope: ScopeTypeDef = ...,
        enhancedInfrastructureMetrics: EnhancedInfrastructureMetricsType = ...,
        inferredWorkloadTypes: InferredWorkloadTypesPreferenceType = ...,
        externalMetricsPreference: ExternalMetricsPreferenceTypeDef = ...,
        lookBackPeriod: LookBackPeriodPreferenceType = ...,
        utilizationPreferences: Sequence[UtilizationPreferenceTypeDef] = ...,
        preferredResources: Sequence[PreferredResourceTypeDef] = ...,
        savingsEstimationMode: SavingsEstimationModeType = ...,
    ) -> Dict[str, Any]:
        """
        Creates a new recommendation preference or updates an existing recommendation
        preference, such as enhanced infrastructure
        metrics.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer.html#ComputeOptimizer.Client.put_recommendation_preferences)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_compute_optimizer/client/#put_recommendation_preferences)
        """

    async def update_enrollment_status(
        self, *, status: StatusType, includeMemberAccounts: bool = ...
    ) -> UpdateEnrollmentStatusResponseTypeDef:
        """
        Updates the enrollment (opt in and opt out) status of an account to the Compute
        Optimizer
        service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer.html#ComputeOptimizer.Client.update_enrollment_status)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_compute_optimizer/client/#update_enrollment_status)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_recommendation_export_jobs"]
    ) -> DescribeRecommendationExportJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer.html#ComputeOptimizer.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_compute_optimizer/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_enrollment_statuses_for_organization"]
    ) -> GetEnrollmentStatusesForOrganizationPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer.html#ComputeOptimizer.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_compute_optimizer/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_lambda_function_recommendations"]
    ) -> GetLambdaFunctionRecommendationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer.html#ComputeOptimizer.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_compute_optimizer/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_recommendation_preferences"]
    ) -> GetRecommendationPreferencesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer.html#ComputeOptimizer.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_compute_optimizer/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_recommendation_summaries"]
    ) -> GetRecommendationSummariesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer.html#ComputeOptimizer.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_compute_optimizer/client/#get_paginator)
        """

    async def __aenter__(self) -> "ComputeOptimizerClient":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer.html#ComputeOptimizer.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_compute_optimizer/client/)
        """

    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> Any:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer.html#ComputeOptimizer.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_compute_optimizer/client/)
        """
