"""
Type annotations for autoscaling-plans service type definitions.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_autoscaling_plans/type_defs/)

Usage::

    ```python
    from types_aiobotocore_autoscaling_plans.type_defs import TagFilterTypeDef

    data: TagFilterTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Sequence, Union

from .literals import (
    ForecastDataTypeType,
    LoadMetricTypeType,
    MetricStatisticType,
    PredictiveScalingMaxCapacityBehaviorType,
    PredictiveScalingModeType,
    ScalableDimensionType,
    ScalingMetricTypeType,
    ScalingPlanStatusCodeType,
    ScalingPolicyUpdateBehaviorType,
    ScalingStatusCodeType,
    ServiceNamespaceType,
)

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 12):
    from typing import NotRequired
else:
    from typing_extensions import NotRequired
if sys.version_info >= (3, 12):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "TagFilterTypeDef",
    "ResponseMetadataTypeDef",
    "MetricDimensionTypeDef",
    "DatapointTypeDef",
    "DeleteScalingPlanRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "DescribeScalingPlanResourcesRequestRequestTypeDef",
    "TimestampTypeDef",
    "PredefinedLoadMetricSpecificationTypeDef",
    "PredefinedScalingMetricSpecificationTypeDef",
    "ApplicationSourceTypeDef",
    "CreateScalingPlanResponseTypeDef",
    "CustomizedLoadMetricSpecificationPaginatorTypeDef",
    "CustomizedLoadMetricSpecificationTypeDef",
    "CustomizedScalingMetricSpecificationPaginatorTypeDef",
    "CustomizedScalingMetricSpecificationTypeDef",
    "GetScalingPlanResourceForecastDataResponseTypeDef",
    "DescribeScalingPlanResourcesRequestDescribeScalingPlanResourcesPaginateTypeDef",
    "GetScalingPlanResourceForecastDataRequestRequestTypeDef",
    "DescribeScalingPlansRequestDescribeScalingPlansPaginateTypeDef",
    "DescribeScalingPlansRequestRequestTypeDef",
    "TargetTrackingConfigurationPaginatorTypeDef",
    "TargetTrackingConfigurationTypeDef",
    "ScalingInstructionPaginatorTypeDef",
    "ScalingPolicyPaginatorTypeDef",
    "ScalingInstructionTypeDef",
    "ScalingPolicyTypeDef",
    "ScalingPlanPaginatorTypeDef",
    "ScalingPlanResourcePaginatorTypeDef",
    "CreateScalingPlanRequestRequestTypeDef",
    "ScalingPlanTypeDef",
    "UpdateScalingPlanRequestRequestTypeDef",
    "ScalingPlanResourceTypeDef",
    "DescribeScalingPlansResponsePaginatorTypeDef",
    "DescribeScalingPlanResourcesResponsePaginatorTypeDef",
    "DescribeScalingPlansResponseTypeDef",
    "DescribeScalingPlanResourcesResponseTypeDef",
)

TagFilterTypeDef = TypedDict(
    "TagFilterTypeDef",
    {
        "Key": NotRequired[str],
        "Values": NotRequired[Sequence[str]],
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
MetricDimensionTypeDef = TypedDict(
    "MetricDimensionTypeDef",
    {
        "Name": str,
        "Value": str,
    },
)
DatapointTypeDef = TypedDict(
    "DatapointTypeDef",
    {
        "Timestamp": NotRequired[datetime],
        "Value": NotRequired[float],
    },
)
DeleteScalingPlanRequestRequestTypeDef = TypedDict(
    "DeleteScalingPlanRequestRequestTypeDef",
    {
        "ScalingPlanName": str,
        "ScalingPlanVersion": int,
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
DescribeScalingPlanResourcesRequestRequestTypeDef = TypedDict(
    "DescribeScalingPlanResourcesRequestRequestTypeDef",
    {
        "ScalingPlanName": str,
        "ScalingPlanVersion": int,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
TimestampTypeDef = Union[datetime, str]
PredefinedLoadMetricSpecificationTypeDef = TypedDict(
    "PredefinedLoadMetricSpecificationTypeDef",
    {
        "PredefinedLoadMetricType": LoadMetricTypeType,
        "ResourceLabel": NotRequired[str],
    },
)
PredefinedScalingMetricSpecificationTypeDef = TypedDict(
    "PredefinedScalingMetricSpecificationTypeDef",
    {
        "PredefinedScalingMetricType": ScalingMetricTypeType,
        "ResourceLabel": NotRequired[str],
    },
)
ApplicationSourceTypeDef = TypedDict(
    "ApplicationSourceTypeDef",
    {
        "CloudFormationStackARN": NotRequired[str],
        "TagFilters": NotRequired[Sequence[TagFilterTypeDef]],
    },
)
CreateScalingPlanResponseTypeDef = TypedDict(
    "CreateScalingPlanResponseTypeDef",
    {
        "ScalingPlanVersion": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CustomizedLoadMetricSpecificationPaginatorTypeDef = TypedDict(
    "CustomizedLoadMetricSpecificationPaginatorTypeDef",
    {
        "MetricName": str,
        "Namespace": str,
        "Statistic": MetricStatisticType,
        "Dimensions": NotRequired[List[MetricDimensionTypeDef]],
        "Unit": NotRequired[str],
    },
)
CustomizedLoadMetricSpecificationTypeDef = TypedDict(
    "CustomizedLoadMetricSpecificationTypeDef",
    {
        "MetricName": str,
        "Namespace": str,
        "Statistic": MetricStatisticType,
        "Dimensions": NotRequired[Sequence[MetricDimensionTypeDef]],
        "Unit": NotRequired[str],
    },
)
CustomizedScalingMetricSpecificationPaginatorTypeDef = TypedDict(
    "CustomizedScalingMetricSpecificationPaginatorTypeDef",
    {
        "MetricName": str,
        "Namespace": str,
        "Statistic": MetricStatisticType,
        "Dimensions": NotRequired[List[MetricDimensionTypeDef]],
        "Unit": NotRequired[str],
    },
)
CustomizedScalingMetricSpecificationTypeDef = TypedDict(
    "CustomizedScalingMetricSpecificationTypeDef",
    {
        "MetricName": str,
        "Namespace": str,
        "Statistic": MetricStatisticType,
        "Dimensions": NotRequired[Sequence[MetricDimensionTypeDef]],
        "Unit": NotRequired[str],
    },
)
GetScalingPlanResourceForecastDataResponseTypeDef = TypedDict(
    "GetScalingPlanResourceForecastDataResponseTypeDef",
    {
        "Datapoints": List[DatapointTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeScalingPlanResourcesRequestDescribeScalingPlanResourcesPaginateTypeDef = TypedDict(
    "DescribeScalingPlanResourcesRequestDescribeScalingPlanResourcesPaginateTypeDef",
    {
        "ScalingPlanName": str,
        "ScalingPlanVersion": int,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetScalingPlanResourceForecastDataRequestRequestTypeDef = TypedDict(
    "GetScalingPlanResourceForecastDataRequestRequestTypeDef",
    {
        "ScalingPlanName": str,
        "ScalingPlanVersion": int,
        "ServiceNamespace": ServiceNamespaceType,
        "ResourceId": str,
        "ScalableDimension": ScalableDimensionType,
        "ForecastDataType": ForecastDataTypeType,
        "StartTime": TimestampTypeDef,
        "EndTime": TimestampTypeDef,
    },
)
DescribeScalingPlansRequestDescribeScalingPlansPaginateTypeDef = TypedDict(
    "DescribeScalingPlansRequestDescribeScalingPlansPaginateTypeDef",
    {
        "ScalingPlanNames": NotRequired[Sequence[str]],
        "ScalingPlanVersion": NotRequired[int],
        "ApplicationSources": NotRequired[Sequence[ApplicationSourceTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeScalingPlansRequestRequestTypeDef = TypedDict(
    "DescribeScalingPlansRequestRequestTypeDef",
    {
        "ScalingPlanNames": NotRequired[Sequence[str]],
        "ScalingPlanVersion": NotRequired[int],
        "ApplicationSources": NotRequired[Sequence[ApplicationSourceTypeDef]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
TargetTrackingConfigurationPaginatorTypeDef = TypedDict(
    "TargetTrackingConfigurationPaginatorTypeDef",
    {
        "TargetValue": float,
        "PredefinedScalingMetricSpecification": NotRequired[
            PredefinedScalingMetricSpecificationTypeDef
        ],
        "CustomizedScalingMetricSpecification": NotRequired[
            CustomizedScalingMetricSpecificationPaginatorTypeDef
        ],
        "DisableScaleIn": NotRequired[bool],
        "ScaleOutCooldown": NotRequired[int],
        "ScaleInCooldown": NotRequired[int],
        "EstimatedInstanceWarmup": NotRequired[int],
    },
)
TargetTrackingConfigurationTypeDef = TypedDict(
    "TargetTrackingConfigurationTypeDef",
    {
        "TargetValue": float,
        "PredefinedScalingMetricSpecification": NotRequired[
            PredefinedScalingMetricSpecificationTypeDef
        ],
        "CustomizedScalingMetricSpecification": NotRequired[
            CustomizedScalingMetricSpecificationTypeDef
        ],
        "DisableScaleIn": NotRequired[bool],
        "ScaleOutCooldown": NotRequired[int],
        "ScaleInCooldown": NotRequired[int],
        "EstimatedInstanceWarmup": NotRequired[int],
    },
)
ScalingInstructionPaginatorTypeDef = TypedDict(
    "ScalingInstructionPaginatorTypeDef",
    {
        "ServiceNamespace": ServiceNamespaceType,
        "ResourceId": str,
        "ScalableDimension": ScalableDimensionType,
        "MinCapacity": int,
        "MaxCapacity": int,
        "TargetTrackingConfigurations": List[TargetTrackingConfigurationPaginatorTypeDef],
        "PredefinedLoadMetricSpecification": NotRequired[PredefinedLoadMetricSpecificationTypeDef],
        "CustomizedLoadMetricSpecification": NotRequired[
            CustomizedLoadMetricSpecificationPaginatorTypeDef
        ],
        "ScheduledActionBufferTime": NotRequired[int],
        "PredictiveScalingMaxCapacityBehavior": NotRequired[
            PredictiveScalingMaxCapacityBehaviorType
        ],
        "PredictiveScalingMaxCapacityBuffer": NotRequired[int],
        "PredictiveScalingMode": NotRequired[PredictiveScalingModeType],
        "ScalingPolicyUpdateBehavior": NotRequired[ScalingPolicyUpdateBehaviorType],
        "DisableDynamicScaling": NotRequired[bool],
    },
)
ScalingPolicyPaginatorTypeDef = TypedDict(
    "ScalingPolicyPaginatorTypeDef",
    {
        "PolicyName": str,
        "PolicyType": Literal["TargetTrackingScaling"],
        "TargetTrackingConfiguration": NotRequired[TargetTrackingConfigurationPaginatorTypeDef],
    },
)
ScalingInstructionTypeDef = TypedDict(
    "ScalingInstructionTypeDef",
    {
        "ServiceNamespace": ServiceNamespaceType,
        "ResourceId": str,
        "ScalableDimension": ScalableDimensionType,
        "MinCapacity": int,
        "MaxCapacity": int,
        "TargetTrackingConfigurations": Sequence[TargetTrackingConfigurationTypeDef],
        "PredefinedLoadMetricSpecification": NotRequired[PredefinedLoadMetricSpecificationTypeDef],
        "CustomizedLoadMetricSpecification": NotRequired[CustomizedLoadMetricSpecificationTypeDef],
        "ScheduledActionBufferTime": NotRequired[int],
        "PredictiveScalingMaxCapacityBehavior": NotRequired[
            PredictiveScalingMaxCapacityBehaviorType
        ],
        "PredictiveScalingMaxCapacityBuffer": NotRequired[int],
        "PredictiveScalingMode": NotRequired[PredictiveScalingModeType],
        "ScalingPolicyUpdateBehavior": NotRequired[ScalingPolicyUpdateBehaviorType],
        "DisableDynamicScaling": NotRequired[bool],
    },
)
ScalingPolicyTypeDef = TypedDict(
    "ScalingPolicyTypeDef",
    {
        "PolicyName": str,
        "PolicyType": Literal["TargetTrackingScaling"],
        "TargetTrackingConfiguration": NotRequired[TargetTrackingConfigurationTypeDef],
    },
)
ScalingPlanPaginatorTypeDef = TypedDict(
    "ScalingPlanPaginatorTypeDef",
    {
        "ScalingPlanName": str,
        "ScalingPlanVersion": int,
        "ApplicationSource": ApplicationSourceTypeDef,
        "ScalingInstructions": List[ScalingInstructionPaginatorTypeDef],
        "StatusCode": ScalingPlanStatusCodeType,
        "StatusMessage": NotRequired[str],
        "StatusStartTime": NotRequired[datetime],
        "CreationTime": NotRequired[datetime],
    },
)
ScalingPlanResourcePaginatorTypeDef = TypedDict(
    "ScalingPlanResourcePaginatorTypeDef",
    {
        "ScalingPlanName": str,
        "ScalingPlanVersion": int,
        "ServiceNamespace": ServiceNamespaceType,
        "ResourceId": str,
        "ScalableDimension": ScalableDimensionType,
        "ScalingStatusCode": ScalingStatusCodeType,
        "ScalingPolicies": NotRequired[List[ScalingPolicyPaginatorTypeDef]],
        "ScalingStatusMessage": NotRequired[str],
    },
)
CreateScalingPlanRequestRequestTypeDef = TypedDict(
    "CreateScalingPlanRequestRequestTypeDef",
    {
        "ScalingPlanName": str,
        "ApplicationSource": ApplicationSourceTypeDef,
        "ScalingInstructions": Sequence[ScalingInstructionTypeDef],
    },
)
ScalingPlanTypeDef = TypedDict(
    "ScalingPlanTypeDef",
    {
        "ScalingPlanName": str,
        "ScalingPlanVersion": int,
        "ApplicationSource": ApplicationSourceTypeDef,
        "ScalingInstructions": List[ScalingInstructionTypeDef],
        "StatusCode": ScalingPlanStatusCodeType,
        "StatusMessage": NotRequired[str],
        "StatusStartTime": NotRequired[datetime],
        "CreationTime": NotRequired[datetime],
    },
)
UpdateScalingPlanRequestRequestTypeDef = TypedDict(
    "UpdateScalingPlanRequestRequestTypeDef",
    {
        "ScalingPlanName": str,
        "ScalingPlanVersion": int,
        "ApplicationSource": NotRequired[ApplicationSourceTypeDef],
        "ScalingInstructions": NotRequired[Sequence[ScalingInstructionTypeDef]],
    },
)
ScalingPlanResourceTypeDef = TypedDict(
    "ScalingPlanResourceTypeDef",
    {
        "ScalingPlanName": str,
        "ScalingPlanVersion": int,
        "ServiceNamespace": ServiceNamespaceType,
        "ResourceId": str,
        "ScalableDimension": ScalableDimensionType,
        "ScalingStatusCode": ScalingStatusCodeType,
        "ScalingPolicies": NotRequired[List[ScalingPolicyTypeDef]],
        "ScalingStatusMessage": NotRequired[str],
    },
)
DescribeScalingPlansResponsePaginatorTypeDef = TypedDict(
    "DescribeScalingPlansResponsePaginatorTypeDef",
    {
        "ScalingPlans": List[ScalingPlanPaginatorTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeScalingPlanResourcesResponsePaginatorTypeDef = TypedDict(
    "DescribeScalingPlanResourcesResponsePaginatorTypeDef",
    {
        "ScalingPlanResources": List[ScalingPlanResourcePaginatorTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeScalingPlansResponseTypeDef = TypedDict(
    "DescribeScalingPlansResponseTypeDef",
    {
        "ScalingPlans": List[ScalingPlanTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeScalingPlanResourcesResponseTypeDef = TypedDict(
    "DescribeScalingPlanResourcesResponseTypeDef",
    {
        "ScalingPlanResources": List[ScalingPlanResourceTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
