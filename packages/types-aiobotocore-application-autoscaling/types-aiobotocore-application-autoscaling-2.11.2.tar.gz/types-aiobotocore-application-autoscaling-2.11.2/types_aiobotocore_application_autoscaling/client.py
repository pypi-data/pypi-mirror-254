"""
Type annotations for application-autoscaling service client.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_application_autoscaling/client/)

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_application_autoscaling.client import ApplicationAutoScalingClient

    session = get_session()
    async with session.create_client("application-autoscaling") as client:
        client: ApplicationAutoScalingClient
    ```
"""

import sys
from typing import Any, Dict, Mapping, Sequence, Type, overload

from aiobotocore.client import AioBaseClient
from botocore.client import ClientMeta

from .literals import PolicyTypeType, ScalableDimensionType, ServiceNamespaceType
from .paginator import (
    DescribeScalableTargetsPaginator,
    DescribeScalingActivitiesPaginator,
    DescribeScalingPoliciesPaginator,
    DescribeScheduledActionsPaginator,
)
from .type_defs import (
    DescribeScalableTargetsResponseTypeDef,
    DescribeScalingActivitiesResponseTypeDef,
    DescribeScalingPoliciesResponseTypeDef,
    DescribeScheduledActionsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    PutScalingPolicyResponseTypeDef,
    RegisterScalableTargetResponseTypeDef,
    ScalableTargetActionTypeDef,
    StepScalingPolicyConfigurationTypeDef,
    SuspendedStateTypeDef,
    TargetTrackingScalingPolicyConfigurationTypeDef,
    TimestampTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("ApplicationAutoScalingClient",)


class BotocoreClientError(Exception):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    ConcurrentUpdateException: Type[BotocoreClientError]
    FailedResourceAccessException: Type[BotocoreClientError]
    InternalServiceException: Type[BotocoreClientError]
    InvalidNextTokenException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ObjectNotFoundException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    TooManyTagsException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class ApplicationAutoScalingClient(AioBaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_application_autoscaling/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        ApplicationAutoScalingClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client.exceptions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_application_autoscaling/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client.can_paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_application_autoscaling/client/#can_paginate)
        """

    async def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client.close)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_application_autoscaling/client/#close)
        """

    async def delete_scaling_policy(
        self,
        *,
        PolicyName: str,
        ServiceNamespace: ServiceNamespaceType,
        ResourceId: str,
        ScalableDimension: ScalableDimensionType,
    ) -> Dict[str, Any]:
        """
        Deletes the specified scaling policy for an Application Auto Scaling scalable
        target.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client.delete_scaling_policy)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_application_autoscaling/client/#delete_scaling_policy)
        """

    async def delete_scheduled_action(
        self,
        *,
        ServiceNamespace: ServiceNamespaceType,
        ScheduledActionName: str,
        ResourceId: str,
        ScalableDimension: ScalableDimensionType,
    ) -> Dict[str, Any]:
        """
        Deletes the specified scheduled action for an Application Auto Scaling scalable
        target.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client.delete_scheduled_action)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_application_autoscaling/client/#delete_scheduled_action)
        """

    async def deregister_scalable_target(
        self,
        *,
        ServiceNamespace: ServiceNamespaceType,
        ResourceId: str,
        ScalableDimension: ScalableDimensionType,
    ) -> Dict[str, Any]:
        """
        Deregisters an Application Auto Scaling scalable target when you have finished
        using
        it.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client.deregister_scalable_target)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_application_autoscaling/client/#deregister_scalable_target)
        """

    async def describe_scalable_targets(
        self,
        *,
        ServiceNamespace: ServiceNamespaceType,
        ResourceIds: Sequence[str] = ...,
        ScalableDimension: ScalableDimensionType = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
    ) -> DescribeScalableTargetsResponseTypeDef:
        """
        Gets information about the scalable targets in the specified namespace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client.describe_scalable_targets)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_application_autoscaling/client/#describe_scalable_targets)
        """

    async def describe_scaling_activities(
        self,
        *,
        ServiceNamespace: ServiceNamespaceType,
        ResourceId: str = ...,
        ScalableDimension: ScalableDimensionType = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
        IncludeNotScaledActivities: bool = ...,
    ) -> DescribeScalingActivitiesResponseTypeDef:
        """
        Provides descriptive information about the scaling activities in the specified
        namespace from the previous six
        weeks.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client.describe_scaling_activities)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_application_autoscaling/client/#describe_scaling_activities)
        """

    async def describe_scaling_policies(
        self,
        *,
        ServiceNamespace: ServiceNamespaceType,
        PolicyNames: Sequence[str] = ...,
        ResourceId: str = ...,
        ScalableDimension: ScalableDimensionType = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
    ) -> DescribeScalingPoliciesResponseTypeDef:
        """
        Describes the Application Auto Scaling scaling policies for the specified
        service
        namespace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client.describe_scaling_policies)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_application_autoscaling/client/#describe_scaling_policies)
        """

    async def describe_scheduled_actions(
        self,
        *,
        ServiceNamespace: ServiceNamespaceType,
        ScheduledActionNames: Sequence[str] = ...,
        ResourceId: str = ...,
        ScalableDimension: ScalableDimensionType = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
    ) -> DescribeScheduledActionsResponseTypeDef:
        """
        Describes the Application Auto Scaling scheduled actions for the specified
        service
        namespace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client.describe_scheduled_actions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_application_autoscaling/client/#describe_scheduled_actions)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client.generate_presigned_url)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_application_autoscaling/client/#generate_presigned_url)
        """

    async def list_tags_for_resource(
        self, *, ResourceARN: str
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Returns all the tags on the specified Application Auto Scaling scalable target.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client.list_tags_for_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_application_autoscaling/client/#list_tags_for_resource)
        """

    async def put_scaling_policy(
        self,
        *,
        PolicyName: str,
        ServiceNamespace: ServiceNamespaceType,
        ResourceId: str,
        ScalableDimension: ScalableDimensionType,
        PolicyType: PolicyTypeType = ...,
        StepScalingPolicyConfiguration: StepScalingPolicyConfigurationTypeDef = ...,
        TargetTrackingScalingPolicyConfiguration: TargetTrackingScalingPolicyConfigurationTypeDef = ...,
    ) -> PutScalingPolicyResponseTypeDef:
        """
        Creates or updates a scaling policy for an Application Auto Scaling scalable
        target.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client.put_scaling_policy)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_application_autoscaling/client/#put_scaling_policy)
        """

    async def put_scheduled_action(
        self,
        *,
        ServiceNamespace: ServiceNamespaceType,
        ScheduledActionName: str,
        ResourceId: str,
        ScalableDimension: ScalableDimensionType,
        Schedule: str = ...,
        Timezone: str = ...,
        StartTime: TimestampTypeDef = ...,
        EndTime: TimestampTypeDef = ...,
        ScalableTargetAction: ScalableTargetActionTypeDef = ...,
    ) -> Dict[str, Any]:
        """
        Creates or updates a scheduled action for an Application Auto Scaling scalable
        target.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client.put_scheduled_action)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_application_autoscaling/client/#put_scheduled_action)
        """

    async def register_scalable_target(
        self,
        *,
        ServiceNamespace: ServiceNamespaceType,
        ResourceId: str,
        ScalableDimension: ScalableDimensionType,
        MinCapacity: int = ...,
        MaxCapacity: int = ...,
        RoleARN: str = ...,
        SuspendedState: SuspendedStateTypeDef = ...,
        Tags: Mapping[str, str] = ...,
    ) -> RegisterScalableTargetResponseTypeDef:
        """
        Registers or updates a scalable target, which is the resource that you want to
        scale.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client.register_scalable_target)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_application_autoscaling/client/#register_scalable_target)
        """

    async def tag_resource(self, *, ResourceARN: str, Tags: Mapping[str, str]) -> Dict[str, Any]:
        """
        Adds or edits tags on an Application Auto Scaling scalable target.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client.tag_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_application_autoscaling/client/#tag_resource)
        """

    async def untag_resource(self, *, ResourceARN: str, TagKeys: Sequence[str]) -> Dict[str, Any]:
        """
        Deletes tags from an Application Auto Scaling scalable target.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client.untag_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_application_autoscaling/client/#untag_resource)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_scalable_targets"]
    ) -> DescribeScalableTargetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_application_autoscaling/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_scaling_activities"]
    ) -> DescribeScalingActivitiesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_application_autoscaling/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_scaling_policies"]
    ) -> DescribeScalingPoliciesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_application_autoscaling/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_scheduled_actions"]
    ) -> DescribeScheduledActionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_application_autoscaling/client/#get_paginator)
        """

    async def __aenter__(self) -> "ApplicationAutoScalingClient":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_application_autoscaling/client/)
        """

    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> Any:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_application_autoscaling/client/)
        """
