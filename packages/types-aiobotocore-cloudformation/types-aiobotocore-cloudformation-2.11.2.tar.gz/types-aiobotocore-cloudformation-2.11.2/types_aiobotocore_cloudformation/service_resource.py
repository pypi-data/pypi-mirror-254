"""
Type annotations for cloudformation service ServiceResource

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudformation/service_resource/)

Usage::

    ```python
    from aiobotocore.session import get_session

    from types_aiobotocore_cloudformation.service_resource import CloudFormationServiceResource
    import types_aiobotocore_cloudformation.service_resource as cloudformation_resources

    session = get_session()
    async with session.resource("cloudformation") as resource:
        resource: CloudFormationServiceResource

        my_event: cloudformation_resources.Event = resource.Event(...)
        my_stack: cloudformation_resources.Stack = resource.Stack(...)
        my_stack_resource: cloudformation_resources.StackResource = resource.StackResource(...)
        my_stack_resource_summary: cloudformation_resources.StackResourceSummary = resource.StackResourceSummary(...)
```
"""

import sys
from datetime import datetime
from typing import AsyncIterator, Awaitable, List, NoReturn, Sequence

from .client import CloudFormationClient
from .literals import (
    CapabilityType,
    HookFailureModeType,
    HookStatusType,
    OnFailureType,
    ResourceStatusType,
    StackStatusType,
)
from .type_defs import (
    ModuleInfoResponseTypeDef,
    ModuleInfoTypeDef,
    OutputTypeDef,
    ParameterTypeDef,
    RollbackConfigurationResponseTypeDef,
    RollbackConfigurationTypeDef,
    StackDriftInformationResponseTypeDef,
    StackResourceDriftInformationResponseTypeDef,
    StackResourceDriftInformationSummaryResponseTypeDef,
    TagTypeDef,
    UpdateStackOutputTypeDef,
)

try:
    from aioboto3.resources.base import AIOBoto3ServiceResource
except ImportError:
    from builtins import object as AIOBoto3ServiceResource
try:
    from aioboto3.resources.collection import AIOResourceCollection
except ImportError:
    from builtins import object as AIOResourceCollection
if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal
try:
    from boto3.resources.base import ResourceMeta
except ImportError:
    from builtins import object as ResourceMeta

__all__ = (
    "CloudFormationServiceResource",
    "Event",
    "Stack",
    "StackResource",
    "StackResourceSummary",
    "ServiceResourceStacksCollection",
    "StackEventsCollection",
    "StackResourceSummariesCollection",
)


class ServiceResourceStacksCollection(AIOResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.ServiceResource.stacks)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudformation/service_resource/#serviceresourcestackscollection)
    """

    def all(self) -> "ServiceResourceStacksCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.ServiceResource.stacks)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudformation/service_resource/#serviceresourcestackscollection)
        """

    def filter(  # type: ignore
        self, *, StackName: str = ..., NextToken: str = ...
    ) -> "ServiceResourceStacksCollection":
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.ServiceResource.stacks)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudformation/service_resource/#serviceresourcestackscollection)
        """

    def limit(self, count: int) -> "ServiceResourceStacksCollection":
        """
        Return at most this many Stacks.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.ServiceResource.stacks)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudformation/service_resource/#serviceresourcestackscollection)
        """

    def page_size(self, count: int) -> "ServiceResourceStacksCollection":
        """
        Fetch at most this many Stacks per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.ServiceResource.stacks)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudformation/service_resource/#serviceresourcestackscollection)
        """

    def pages(self) -> AsyncIterator[List["Stack"]]:
        """
        A generator which yields pages of Stacks.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.ServiceResource.stacks)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudformation/service_resource/#serviceresourcestackscollection)
        """

    def __iter__(self) -> NoReturn:
        """
        A generator which yields Stacks.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.ServiceResource.stacks)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudformation/service_resource/#serviceresourcestackscollection)
        """

    def __aiter__(self) -> AsyncIterator["Stack"]:
        """
        A generator which yields Stacks.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.ServiceResource.stacks)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudformation/service_resource/#serviceresourcestackscollection)
        """


class StackEventsCollection(AIOResourceCollection):
    def all(self) -> "StackEventsCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.
        """

    def filter(  # type: ignore
        self, *, StackName: str = ..., NextToken: str = ...
    ) -> "StackEventsCollection":
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.
        """

    def limit(self, count: int) -> "StackEventsCollection":
        """
        Return at most this many Events.
        """

    def page_size(self, count: int) -> "StackEventsCollection":
        """
        Fetch at most this many Events per service request.
        """

    def pages(self) -> AsyncIterator[List["Event"]]:
        """
        A generator which yields pages of Events.
        """

    def __iter__(self) -> NoReturn:
        """
        A generator which yields Events.
        """

    def __aiter__(self) -> AsyncIterator["Event"]:
        """
        A generator which yields Events.
        """


class StackResourceSummariesCollection(AIOResourceCollection):
    def all(self) -> "StackResourceSummariesCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.
        """

    def filter(self, *, NextToken: str = ...) -> "StackResourceSummariesCollection":  # type: ignore
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.
        """

    def limit(self, count: int) -> "StackResourceSummariesCollection":
        """
        Return at most this many StackResourceSummarys.
        """

    def page_size(self, count: int) -> "StackResourceSummariesCollection":
        """
        Fetch at most this many StackResourceSummarys per service request.
        """

    def pages(self) -> AsyncIterator[List["StackResourceSummary"]]:
        """
        A generator which yields pages of StackResourceSummarys.
        """

    def __iter__(self) -> NoReturn:
        """
        A generator which yields StackResourceSummarys.
        """

    def __aiter__(self) -> AsyncIterator["StackResourceSummary"]:
        """
        A generator which yields StackResourceSummarys.
        """


class Event(AIOBoto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.ServiceResource.Event)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudformation/service_resource/#event)
    """

    stack_id: Awaitable[str]
    event_id: Awaitable[str]
    stack_name: Awaitable[str]
    logical_resource_id: Awaitable[str]
    physical_resource_id: Awaitable[str]
    resource_type: Awaitable[str]
    timestamp: Awaitable[datetime]
    resource_status: Awaitable[ResourceStatusType]
    resource_status_reason: Awaitable[str]
    resource_properties: Awaitable[str]
    client_request_token: Awaitable[str]
    hook_type: Awaitable[str]
    hook_status: Awaitable[HookStatusType]
    hook_status_reason: Awaitable[str]
    hook_invocation_point: Awaitable[Literal["PRE_PROVISION"]]
    hook_failure_mode: Awaitable[HookFailureModeType]
    id: str
    meta: Awaitable["CloudFormationResourceMeta"]

    async def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Event.get_available_subresources)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudformation/service_resource/#eventget_available_subresources-method)
        """


_Event = Event


class Stack(AIOBoto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.ServiceResource.Stack)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudformation/service_resource/#stack)
    """

    stack_id: Awaitable[str]
    stack_name: Awaitable[str]
    change_set_id: Awaitable[str]
    description: Awaitable[str]
    parameters: Awaitable[List[ParameterTypeDef]]
    creation_time: Awaitable[datetime]
    deletion_time: Awaitable[datetime]
    last_updated_time: Awaitable[datetime]
    rollback_configuration: Awaitable[RollbackConfigurationResponseTypeDef]
    stack_status: Awaitable[StackStatusType]
    stack_status_reason: Awaitable[str]
    disable_rollback: Awaitable[bool]
    notification_arns: Awaitable[List[str]]
    timeout_in_minutes: Awaitable[int]
    capabilities: Awaitable[List[CapabilityType]]
    outputs: Awaitable[List[OutputTypeDef]]
    role_arn: Awaitable[str]
    tags: Awaitable[List[TagTypeDef]]
    enable_termination_protection: Awaitable[bool]
    parent_id: Awaitable[str]
    root_id: Awaitable[str]
    drift_information: Awaitable[StackDriftInformationResponseTypeDef]
    retain_except_on_create: Awaitable[bool]
    name: str
    events: StackEventsCollection
    resource_summaries: StackResourceSummariesCollection
    meta: Awaitable["CloudFormationResourceMeta"]

    async def Resource(self, logical_id: str) -> "_StackResource":
        """
        Creates a StackResource resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Stack.Resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudformation/service_resource/#stackresource-method)
        """

    async def cancel_update(self, *, ClientRequestToken: str = ...) -> None:
        """
        Cancels an update on the specified stack.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Stack.cancel_update)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudformation/service_resource/#stackcancel_update-method)
        """

    async def delete(
        self,
        *,
        RetainResources: Sequence[str] = ...,
        RoleARN: str = ...,
        ClientRequestToken: str = ...,
    ) -> None:
        """
        Deletes a specified stack.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Stack.delete)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudformation/service_resource/#stackdelete-method)
        """

    async def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Stack.get_available_subresources)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudformation/service_resource/#stackget_available_subresources-method)
        """

    async def load(self) -> None:
        """
        Calls :py:meth:`CloudFormation.Client.describe_stacks` to update the attributes
        of the Stack
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Stack.load)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudformation/service_resource/#stackload-method)
        """

    async def reload(self) -> None:
        """
        Calls :py:meth:`CloudFormation.Client.describe_stacks` to update the attributes
        of the Stack
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Stack.reload)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudformation/service_resource/#stackreload-method)
        """

    async def update(
        self,
        *,
        TemplateBody: str = ...,
        TemplateURL: str = ...,
        UsePreviousTemplate: bool = ...,
        StackPolicyDuringUpdateBody: str = ...,
        StackPolicyDuringUpdateURL: str = ...,
        Parameters: Sequence[ParameterTypeDef] = ...,
        Capabilities: Sequence[CapabilityType] = ...,
        ResourceTypes: Sequence[str] = ...,
        RoleARN: str = ...,
        RollbackConfiguration: RollbackConfigurationTypeDef = ...,
        StackPolicyBody: str = ...,
        StackPolicyURL: str = ...,
        NotificationARNs: Sequence[str] = ...,
        Tags: Sequence[TagTypeDef] = ...,
        DisableRollback: bool = ...,
        ClientRequestToken: str = ...,
        RetainExceptOnCreate: bool = ...,
    ) -> UpdateStackOutputTypeDef:
        """
        Updates a stack as specified in the template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Stack.update)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudformation/service_resource/#stackupdate-method)
        """


_Stack = Stack


class StackResource(AIOBoto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.ServiceResource.StackResource)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudformation/service_resource/#stackresource)
    """

    stack_id: Awaitable[str]
    logical_resource_id: Awaitable[str]
    physical_resource_id: Awaitable[str]
    resource_type: Awaitable[str]
    last_updated_timestamp: Awaitable[datetime]
    resource_status: Awaitable[ResourceStatusType]
    resource_status_reason: Awaitable[str]
    description: Awaitable[str]
    metadata: Awaitable[str]
    drift_information: Awaitable[StackResourceDriftInformationResponseTypeDef]
    module_info: Awaitable[ModuleInfoTypeDef]
    stack_name: str
    logical_id: str
    meta: Awaitable["CloudFormationResourceMeta"]

    async def Stack(self) -> "_Stack":
        """
        Creates a Stack resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.StackResource.Stack)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudformation/service_resource/#stackresourcestack-method)
        """

    async def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.StackResource.get_available_subresources)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudformation/service_resource/#stackresourceget_available_subresources-method)
        """

    async def load(self) -> None:
        """
        Calls :py:meth:`CloudFormation.Client.describe_stack_resource` to update the
        attributes of the StackResource
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.StackResource.load)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudformation/service_resource/#stackresourceload-method)
        """

    async def reload(self) -> None:
        """
        Calls :py:meth:`CloudFormation.Client.describe_stack_resource` to update the
        attributes of the StackResource
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.StackResource.reload)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudformation/service_resource/#stackresourcereload-method)
        """


_StackResource = StackResource


class StackResourceSummary(AIOBoto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.ServiceResource.StackResourceSummary)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudformation/service_resource/#stackresourcesummary)
    """

    logical_resource_id: Awaitable[str]
    physical_resource_id: Awaitable[str]
    resource_type: Awaitable[str]
    last_updated_timestamp: Awaitable[datetime]
    resource_status: Awaitable[ResourceStatusType]
    resource_status_reason: Awaitable[str]
    drift_information: Awaitable[StackResourceDriftInformationSummaryResponseTypeDef]
    module_info: Awaitable[ModuleInfoResponseTypeDef]
    stack_name: str
    logical_id: str
    meta: Awaitable["CloudFormationResourceMeta"]

    async def Resource(self) -> "_StackResource":
        """
        Creates a StackResource resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.StackResourceSummary.Resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudformation/service_resource/#stackresourcesummaryresource-method)
        """

    async def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.StackResourceSummary.get_available_subresources)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudformation/service_resource/#stackresourcesummaryget_available_subresources-method)
        """


_StackResourceSummary = StackResourceSummary


class CloudFormationResourceMeta(ResourceMeta):
    client: CloudFormationClient


class CloudFormationServiceResource(AIOBoto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.ServiceResource)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudformation/service_resource/)
    """

    meta: "CloudFormationResourceMeta"
    stacks: ServiceResourceStacksCollection

    async def Event(self, id: str) -> "_Event":
        """
        Creates a Event resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.ServiceResource.Event)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudformation/service_resource/#cloudformationserviceresourceevent-method)
        """

    async def Stack(self, name: str) -> "_Stack":
        """
        Creates a Stack resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.ServiceResource.Stack)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudformation/service_resource/#cloudformationserviceresourcestack-method)
        """

    async def StackResource(self, stack_name: str, logical_id: str) -> "_StackResource":
        """
        Creates a StackResource resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.ServiceResource.StackResource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudformation/service_resource/#cloudformationserviceresourcestackresource-method)
        """

    async def StackResourceSummary(
        self, stack_name: str, logical_id: str
    ) -> "_StackResourceSummary":
        """
        Creates a StackResourceSummary resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.ServiceResource.StackResourceSummary)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudformation/service_resource/#cloudformationserviceresourcestackresourcesummary-method)
        """

    async def create_stack(
        self,
        *,
        StackName: str,
        TemplateBody: str = ...,
        TemplateURL: str = ...,
        Parameters: Sequence[ParameterTypeDef] = ...,
        DisableRollback: bool = ...,
        RollbackConfiguration: RollbackConfigurationTypeDef = ...,
        TimeoutInMinutes: int = ...,
        NotificationARNs: Sequence[str] = ...,
        Capabilities: Sequence[CapabilityType] = ...,
        ResourceTypes: Sequence[str] = ...,
        RoleARN: str = ...,
        OnFailure: OnFailureType = ...,
        StackPolicyBody: str = ...,
        StackPolicyURL: str = ...,
        Tags: Sequence[TagTypeDef] = ...,
        ClientRequestToken: str = ...,
        EnableTerminationProtection: bool = ...,
        RetainExceptOnCreate: bool = ...,
    ) -> "_Stack":
        """
        Creates a stack as specified in the template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.ServiceResource.create_stack)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudformation/service_resource/#cloudformationserviceresourcecreate_stack-method)
        """

    async def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.ServiceResource.get_available_subresources)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudformation/service_resource/#cloudformationserviceresourceget_available_subresources-method)
        """
