"""
Type annotations for opsworks service ServiceResource

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opsworks/service_resource/)

Usage::

    ```python
    from aiobotocore.session import get_session

    from types_aiobotocore_opsworks.service_resource import OpsWorksServiceResource
    import types_aiobotocore_opsworks.service_resource as opsworks_resources

    session = get_session()
    async with session.resource("opsworks") as resource:
        resource: OpsWorksServiceResource

        my_layer: opsworks_resources.Layer = resource.Layer(...)
        my_stack: opsworks_resources.Stack = resource.Stack(...)
        my_stack_summary: opsworks_resources.StackSummary = resource.StackSummary(...)
```
"""

import sys
from typing import AsyncIterator, Awaitable, Dict, List, Mapping, NoReturn, Sequence

from .client import OpsWorksClient
from .literals import LayerAttributesKeysType, LayerTypeType, RootDeviceTypeType
from .type_defs import (
    ChefConfigurationResponseTypeDef,
    ChefConfigurationTypeDef,
    CloudWatchLogsConfigurationResponseTypeDef,
    CloudWatchLogsConfigurationTypeDef,
    InstancesCountResponseTypeDef,
    LifecycleEventConfigurationResponseTypeDef,
    LifecycleEventConfigurationTypeDef,
    RecipesResponseTypeDef,
    RecipesTypeDef,
    SourceResponseTypeDef,
    SourceTypeDef,
    StackConfigurationManagerResponseTypeDef,
    StackConfigurationManagerTypeDef,
    VolumeConfigurationTypeDef,
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
    "OpsWorksServiceResource",
    "Layer",
    "Stack",
    "StackSummary",
    "ServiceResourceStacksCollection",
    "StackLayersCollection",
)

class ServiceResourceStacksCollection(AIOResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.ServiceResource.stacks)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opsworks/service_resource/#serviceresourcestackscollection)
    """

    def all(self) -> "ServiceResourceStacksCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.ServiceResource.stacks)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opsworks/service_resource/#serviceresourcestackscollection)
        """

    def filter(  # type: ignore
        self, *, StackIds: Sequence[str] = ...
    ) -> "ServiceResourceStacksCollection":
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.ServiceResource.stacks)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opsworks/service_resource/#serviceresourcestackscollection)
        """

    def limit(self, count: int) -> "ServiceResourceStacksCollection":
        """
        Return at most this many Stacks.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.ServiceResource.stacks)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opsworks/service_resource/#serviceresourcestackscollection)
        """

    def page_size(self, count: int) -> "ServiceResourceStacksCollection":
        """
        Fetch at most this many Stacks per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.ServiceResource.stacks)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opsworks/service_resource/#serviceresourcestackscollection)
        """

    def pages(self) -> AsyncIterator[List["Stack"]]:
        """
        A generator which yields pages of Stacks.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.ServiceResource.stacks)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opsworks/service_resource/#serviceresourcestackscollection)
        """

    def __iter__(self) -> NoReturn:
        """
        A generator which yields Stacks.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.ServiceResource.stacks)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opsworks/service_resource/#serviceresourcestackscollection)
        """

    def __aiter__(self) -> AsyncIterator["Stack"]:
        """
        A generator which yields Stacks.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.ServiceResource.stacks)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opsworks/service_resource/#serviceresourcestackscollection)
        """

class StackLayersCollection(AIOResourceCollection):
    def all(self) -> "StackLayersCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.
        """

    def filter(  # type: ignore
        self, *, StackId: str = ..., LayerIds: Sequence[str] = ...
    ) -> "StackLayersCollection":
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.
        """

    def limit(self, count: int) -> "StackLayersCollection":
        """
        Return at most this many Layers.
        """

    def page_size(self, count: int) -> "StackLayersCollection":
        """
        Fetch at most this many Layers per service request.
        """

    def pages(self) -> AsyncIterator[List["Layer"]]:
        """
        A generator which yields pages of Layers.
        """

    def __iter__(self) -> NoReturn:
        """
        A generator which yields Layers.
        """

    def __aiter__(self) -> AsyncIterator["Layer"]:
        """
        A generator which yields Layers.
        """

class Layer(AIOBoto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.ServiceResource.Layer)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opsworks/service_resource/#layer)
    """

    arn: Awaitable[str]
    stack_id: Awaitable[str]
    layer_id: Awaitable[str]
    type: Awaitable[LayerTypeType]
    name: Awaitable[str]
    shortname: Awaitable[str]
    attributes: Awaitable[Dict[LayerAttributesKeysType, str]]
    cloud_watch_logs_configuration: Awaitable[CloudWatchLogsConfigurationResponseTypeDef]
    custom_instance_profile_arn: Awaitable[str]
    custom_json: Awaitable[str]
    custom_security_group_ids: Awaitable[List[str]]
    default_security_group_names: Awaitable[List[str]]
    packages: Awaitable[List[str]]
    volume_configurations: Awaitable[List[VolumeConfigurationTypeDef]]
    enable_auto_healing: Awaitable[bool]
    auto_assign_elastic_ips: Awaitable[bool]
    auto_assign_public_ips: Awaitable[bool]
    default_recipes: Awaitable[RecipesResponseTypeDef]
    custom_recipes: Awaitable[RecipesResponseTypeDef]
    created_at: Awaitable[str]
    install_updates_on_boot: Awaitable[bool]
    use_ebs_optimized_instances: Awaitable[bool]
    lifecycle_event_configuration: Awaitable[LifecycleEventConfigurationResponseTypeDef]
    id: str
    stack: "Stack"
    meta: Awaitable["OpsWorksResourceMeta"]

    async def delete(self) -> None:
        """
        Deletes a specified layer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Layer.delete)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opsworks/service_resource/#layerdelete-method)
        """

    async def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Layer.get_available_subresources)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opsworks/service_resource/#layerget_available_subresources-method)
        """

    async def load(self) -> None:
        """
        Calls :py:meth:`OpsWorks.Client.describe_layers` to update the attributes of
        the Layer
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Layer.load)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opsworks/service_resource/#layerload-method)
        """

    async def reload(self) -> None:
        """
        Calls :py:meth:`OpsWorks.Client.describe_layers` to update the attributes of
        the Layer
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Layer.reload)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opsworks/service_resource/#layerreload-method)
        """

_Layer = Layer

class StackSummary(AIOBoto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.ServiceResource.StackSummary)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opsworks/service_resource/#stacksummary)
    """

    name: Awaitable[str]
    arn: Awaitable[str]
    layers_count: Awaitable[int]
    apps_count: Awaitable[int]
    instances_count: Awaitable[InstancesCountResponseTypeDef]
    stack_id: str
    meta: Awaitable["OpsWorksResourceMeta"]

    async def Stack(self) -> "_Stack":
        """
        Creates a Stack resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.StackSummary.Stack)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opsworks/service_resource/#stacksummarystack-method)
        """

    async def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.StackSummary.get_available_subresources)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opsworks/service_resource/#stacksummaryget_available_subresources-method)
        """

    async def load(self) -> None:
        """
        Calls :py:meth:`OpsWorks.Client.describe_stack_summary` to update the
        attributes of the StackSummary
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.StackSummary.load)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opsworks/service_resource/#stacksummaryload-method)
        """

    async def reload(self) -> None:
        """
        Calls :py:meth:`OpsWorks.Client.describe_stack_summary` to update the
        attributes of the StackSummary
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.StackSummary.reload)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opsworks/service_resource/#stacksummaryreload-method)
        """

_StackSummary = StackSummary

class Stack(AIOBoto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.ServiceResource.Stack)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opsworks/service_resource/#stack)
    """

    stack_id: Awaitable[str]
    name: Awaitable[str]
    arn: Awaitable[str]
    region: Awaitable[str]
    vpc_id: Awaitable[str]
    attributes: Awaitable[Dict[Literal["Color"], str]]
    service_role_arn: Awaitable[str]
    default_instance_profile_arn: Awaitable[str]
    default_os: Awaitable[str]
    hostname_theme: Awaitable[str]
    default_availability_zone: Awaitable[str]
    default_subnet_id: Awaitable[str]
    custom_json: Awaitable[str]
    configuration_manager: Awaitable[StackConfigurationManagerResponseTypeDef]
    chef_configuration: Awaitable[ChefConfigurationResponseTypeDef]
    use_custom_cookbooks: Awaitable[bool]
    use_opsworks_security_groups: Awaitable[bool]
    custom_cookbooks_source: Awaitable[SourceResponseTypeDef]
    default_ssh_key_name: Awaitable[str]
    created_at: Awaitable[str]
    default_root_device_type: Awaitable[RootDeviceTypeType]
    agent_version: Awaitable[str]
    id: str
    layers: StackLayersCollection
    meta: Awaitable["OpsWorksResourceMeta"]

    async def Summary(self) -> "_StackSummary":
        """
        Creates a StackSummary resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Stack.Summary)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opsworks/service_resource/#stacksummary-method)
        """

    async def create_layer(
        self,
        *,
        Type: LayerTypeType,
        Name: str,
        Shortname: str,
        Attributes: Mapping[LayerAttributesKeysType, str] = ...,
        CloudWatchLogsConfiguration: CloudWatchLogsConfigurationTypeDef = ...,
        CustomInstanceProfileArn: str = ...,
        CustomJson: str = ...,
        CustomSecurityGroupIds: Sequence[str] = ...,
        Packages: Sequence[str] = ...,
        VolumeConfigurations: Sequence[VolumeConfigurationTypeDef] = ...,
        EnableAutoHealing: bool = ...,
        AutoAssignElasticIps: bool = ...,
        AutoAssignPublicIps: bool = ...,
        CustomRecipes: RecipesTypeDef = ...,
        InstallUpdatesOnBoot: bool = ...,
        UseEbsOptimizedInstances: bool = ...,
        LifecycleEventConfiguration: LifecycleEventConfigurationTypeDef = ...,
    ) -> "_Layer":
        """
        Creates a layer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Stack.create_layer)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opsworks/service_resource/#stackcreate_layer-method)
        """

    async def delete(self) -> None:
        """
        Deletes a specified stack.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Stack.delete)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opsworks/service_resource/#stackdelete-method)
        """

    async def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Stack.get_available_subresources)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opsworks/service_resource/#stackget_available_subresources-method)
        """

    async def load(self) -> None:
        """
        Calls :py:meth:`OpsWorks.Client.describe_stacks` to update the attributes of
        the Stack
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Stack.load)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opsworks/service_resource/#stackload-method)
        """

    async def reload(self) -> None:
        """
        Calls :py:meth:`OpsWorks.Client.describe_stacks` to update the attributes of
        the Stack
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Stack.reload)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opsworks/service_resource/#stackreload-method)
        """

_Stack = Stack

class OpsWorksResourceMeta(ResourceMeta):
    client: OpsWorksClient

class OpsWorksServiceResource(AIOBoto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.ServiceResource)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opsworks/service_resource/)
    """

    meta: "OpsWorksResourceMeta"
    stacks: ServiceResourceStacksCollection

    async def Layer(self, id: str) -> "_Layer":
        """
        Creates a Layer resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.ServiceResource.Layer)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opsworks/service_resource/#opsworksserviceresourcelayer-method)
        """

    async def Stack(self, id: str) -> "_Stack":
        """
        Creates a Stack resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.ServiceResource.Stack)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opsworks/service_resource/#opsworksserviceresourcestack-method)
        """

    async def StackSummary(self, stack_id: str) -> "_StackSummary":
        """
        Creates a StackSummary resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.ServiceResource.StackSummary)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opsworks/service_resource/#opsworksserviceresourcestacksummary-method)
        """

    async def create_stack(
        self,
        *,
        Name: str,
        Region: str,
        ServiceRoleArn: str,
        DefaultInstanceProfileArn: str,
        VpcId: str = ...,
        Attributes: Mapping[Literal["Color"], str] = ...,
        DefaultOs: str = ...,
        HostnameTheme: str = ...,
        DefaultAvailabilityZone: str = ...,
        DefaultSubnetId: str = ...,
        CustomJson: str = ...,
        ConfigurationManager: StackConfigurationManagerTypeDef = ...,
        ChefConfiguration: ChefConfigurationTypeDef = ...,
        UseCustomCookbooks: bool = ...,
        UseOpsworksSecurityGroups: bool = ...,
        CustomCookbooksSource: SourceTypeDef = ...,
        DefaultSshKeyName: str = ...,
        DefaultRootDeviceType: RootDeviceTypeType = ...,
        AgentVersion: str = ...,
    ) -> "_Stack":
        """
        Creates a new stack.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.ServiceResource.create_stack)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opsworks/service_resource/#opsworksserviceresourcecreate_stack-method)
        """

    async def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.ServiceResource.get_available_subresources)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opsworks/service_resource/#opsworksserviceresourceget_available_subresources-method)
        """
