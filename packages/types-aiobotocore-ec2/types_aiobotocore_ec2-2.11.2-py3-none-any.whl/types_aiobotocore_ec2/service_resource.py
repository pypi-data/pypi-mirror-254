"""
Type annotations for ec2 service ServiceResource

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/)

Usage::

    ```python
    from aiobotocore.session import get_session

    from types_aiobotocore_ec2.service_resource import EC2ServiceResource
    import types_aiobotocore_ec2.service_resource as ec2_resources

    session = get_session()
    async with session.resource("ec2") as resource:
        resource: EC2ServiceResource

        my_classic_address: ec2_resources.ClassicAddress = resource.ClassicAddress(...)
        my_dhcp_options: ec2_resources.DhcpOptions = resource.DhcpOptions(...)
        my_image: ec2_resources.Image = resource.Image(...)
        my_instance: ec2_resources.Instance = resource.Instance(...)
        my_internet_gateway: ec2_resources.InternetGateway = resource.InternetGateway(...)
        my_key_pair: ec2_resources.KeyPair = resource.KeyPair(...)
        my_key_pair_info: ec2_resources.KeyPairInfo = resource.KeyPairInfo(...)
        my_network_acl: ec2_resources.NetworkAcl = resource.NetworkAcl(...)
        my_network_interface: ec2_resources.NetworkInterface = resource.NetworkInterface(...)
        my_network_interface_association: ec2_resources.NetworkInterfaceAssociation = resource.NetworkInterfaceAssociation(...)
        my_placement_group: ec2_resources.PlacementGroup = resource.PlacementGroup(...)
        my_route: ec2_resources.Route = resource.Route(...)
        my_route_table: ec2_resources.RouteTable = resource.RouteTable(...)
        my_route_table_association: ec2_resources.RouteTableAssociation = resource.RouteTableAssociation(...)
        my_security_group: ec2_resources.SecurityGroup = resource.SecurityGroup(...)
        my_snapshot: ec2_resources.Snapshot = resource.Snapshot(...)
        my_subnet: ec2_resources.Subnet = resource.Subnet(...)
        my_tag: ec2_resources.Tag = resource.Tag(...)
        my_volume: ec2_resources.Volume = resource.Volume(...)
        my_vpc: ec2_resources.Vpc = resource.Vpc(...)
        my_vpc_peering_connection: ec2_resources.VpcPeeringConnection = resource.VpcPeeringConnection(...)
        my_vpc_address: ec2_resources.VpcAddress = resource.VpcAddress(...)
```
"""

import sys
from datetime import datetime
from typing import AsyncIterator, Awaitable, List, NoReturn, Sequence

from .client import EC2Client
from .literals import (
    ArchitectureValuesType,
    BootModeValuesType,
    DeviceTypeType,
    DomainTypeType,
    HypervisorTypeType,
    ImageAttributeNameType,
    ImageStateType,
    ImageTypeValuesType,
    InstanceAttributeNameType,
    InstanceBootModeValuesType,
    InstanceLifecycleTypeType,
    InstanceTypeType,
    KeyFormatType,
    KeyTypeType,
    NetworkInterfaceAttributeType,
    NetworkInterfaceCreationTypeType,
    NetworkInterfaceStatusType,
    NetworkInterfaceTypeType,
    OperationTypeType,
    PlacementGroupStateType,
    PlacementStrategyType,
    ReportInstanceReasonCodesType,
    ReportStatusTypeType,
    ResourceTypeType,
    RouteOriginType,
    RouteStateType,
    RuleActionType,
    ShutdownBehaviorType,
    SnapshotAttributeNameType,
    SnapshotStateType,
    SpreadLevelType,
    SSETypeType,
    StorageTierType,
    SubnetStateType,
    TenancyType,
    VirtualizationTypeType,
    VolumeAttributeNameType,
    VolumeStateType,
    VolumeTypeType,
    VpcAttributeNameType,
    VpcStateType,
)
from .type_defs import (
    AcceptVpcPeeringConnectionResultTypeDef,
    AssignPrivateIpAddressesResultTypeDef,
    AssociateAddressResultTypeDef,
    AttachClassicLinkVpcResultTypeDef,
    AttachNetworkInterfaceResultTypeDef,
    AttributeBooleanValueTypeDef,
    AttributeValueTypeDef,
    AuthorizeSecurityGroupEgressResultTypeDef,
    AuthorizeSecurityGroupIngressResultTypeDef,
    BlobAttributeValueTypeDef,
    BlobTypeDef,
    BlockDeviceMappingTypeDef,
    CapacityReservationSpecificationResponseResponseTypeDef,
    CapacityReservationSpecificationTypeDef,
    ConnectionTrackingConfigurationResponseTypeDef,
    ConnectionTrackingSpecificationRequestTypeDef,
    CopySnapshotResultTypeDef,
    CpuOptionsRequestTypeDef,
    CpuOptionsResponseTypeDef,
    CreateVolumePermissionModificationsTypeDef,
    CreditSpecificationRequestTypeDef,
    DeleteKeyPairResultTypeDef,
    DeleteVpcPeeringConnectionResultTypeDef,
    DescribeNetworkInterfaceAttributeResultTypeDef,
    DescribeSnapshotAttributeResultTypeDef,
    DescribeVolumeAttributeResultTypeDef,
    DescribeVolumeStatusResultTypeDef,
    DescribeVpcAttributeResultTypeDef,
    DetachClassicLinkVpcResultTypeDef,
    DhcpConfigurationTypeDef,
    DisableVpcClassicLinkResultTypeDef,
    ElasticGpuAssociationTypeDef,
    ElasticGpuSpecificationTypeDef,
    ElasticInferenceAcceleratorAssociationTypeDef,
    ElasticInferenceAcceleratorTypeDef,
    EnableVpcClassicLinkResultTypeDef,
    EnaSrdSpecificationTypeDef,
    EnclaveOptionsRequestTypeDef,
    EnclaveOptionsResponseTypeDef,
    FilterTypeDef,
    GetConsoleOutputResultTypeDef,
    GetPasswordDataResultTypeDef,
    GroupIdentifierTypeDef,
    HibernationOptionsRequestTypeDef,
    HibernationOptionsResponseTypeDef,
    IamInstanceProfileResponseTypeDef,
    IamInstanceProfileSpecificationTypeDef,
    IcmpTypeCodeTypeDef,
    ImageAttributeTypeDef,
    InstanceAttributeTypeDef,
    InstanceBlockDeviceMappingSpecificationTypeDef,
    InstanceBlockDeviceMappingTypeDef,
    InstanceIpv6AddressTypeDef,
    InstanceMaintenanceOptionsRequestTypeDef,
    InstanceMaintenanceOptionsResponseTypeDef,
    InstanceMarketOptionsRequestTypeDef,
    InstanceMetadataOptionsRequestTypeDef,
    InstanceMetadataOptionsResponseResponseTypeDef,
    InstanceNetworkInterfaceSpecificationServiceResourceTypeDef,
    InstanceNetworkInterfaceSpecificationSubnetTypeDef,
    InstanceNetworkInterfaceTypeDef,
    InstanceStateResponseTypeDef,
    InternetGatewayAttachmentTypeDef,
    IpPermissionTypeDef,
    Ipv4PrefixSpecificationRequestTypeDef,
    Ipv4PrefixSpecificationTypeDef,
    Ipv6PrefixSpecificationRequestTypeDef,
    Ipv6PrefixSpecificationTypeDef,
    LaunchPermissionModificationsTypeDef,
    LaunchTemplateSpecificationTypeDef,
    LicenseConfigurationRequestTypeDef,
    LicenseConfigurationTypeDef,
    MonitoringResponseTypeDef,
    MonitorInstancesResultTypeDef,
    NetworkAclAssociationTypeDef,
    NetworkAclEntryTypeDef,
    NetworkInterfaceAssociationResponseTypeDef,
    NetworkInterfaceAttachmentChangesTypeDef,
    NetworkInterfaceAttachmentResponseTypeDef,
    NetworkInterfaceIpv6AddressTypeDef,
    NetworkInterfacePrivateIpAddressTypeDef,
    NewDhcpConfigurationTypeDef,
    PlacementExtraResponseTypeDef,
    PlacementTypeDef,
    PortRangeTypeDef,
    PrivateDnsNameOptionsOnLaunchResponseTypeDef,
    PrivateDnsNameOptionsRequestTypeDef,
    PrivateDnsNameOptionsResponseResponseTypeDef,
    PrivateIpAddressSpecificationTypeDef,
    ProductCodeTypeDef,
    PropagatingVgwTypeDef,
    RejectVpcPeeringConnectionResultTypeDef,
    ReplaceNetworkAclAssociationResultTypeDef,
    RevokeSecurityGroupEgressResultTypeDef,
    RevokeSecurityGroupIngressResultTypeDef,
    RouteTableAssociationStateResponseTypeDef,
    RouteTableAssociationTypeDef,
    RouteTypeDef,
    RunInstancesMonitoringEnabledTypeDef,
    StartInstancesResultTypeDef,
    StateReasonResponseTypeDef,
    StateReasonTypeDef,
    StopInstancesResultTypeDef,
    SubnetIpv6CidrBlockAssociationTypeDef,
    TagSpecificationTypeDef,
    TagTypeDef,
    TerminateInstancesResultTypeDef,
    TimestampTypeDef,
    UnmonitorInstancesResultTypeDef,
    VolumeAttachmentResponseTypeDef,
    VolumeAttachmentTypeDef,
    VpcCidrBlockAssociationTypeDef,
    VpcIpv6CidrBlockAssociationTypeDef,
    VpcPeeringConnectionStateReasonResponseTypeDef,
    VpcPeeringConnectionVpcInfoResponseTypeDef,
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
    "EC2ServiceResource",
    "ClassicAddress",
    "DhcpOptions",
    "Image",
    "Instance",
    "InternetGateway",
    "KeyPair",
    "KeyPairInfo",
    "NetworkAcl",
    "NetworkInterface",
    "NetworkInterfaceAssociation",
    "PlacementGroup",
    "Route",
    "RouteTable",
    "RouteTableAssociation",
    "SecurityGroup",
    "Snapshot",
    "Subnet",
    "Tag",
    "Volume",
    "Vpc",
    "VpcPeeringConnection",
    "VpcAddress",
    "ServiceResourceClassicAddressesCollection",
    "ServiceResourceDhcpOptionsSetsCollection",
    "ServiceResourceImagesCollection",
    "ServiceResourceInstancesCollection",
    "ServiceResourceInternetGatewaysCollection",
    "ServiceResourceKeyPairsCollection",
    "ServiceResourceNetworkAclsCollection",
    "ServiceResourceNetworkInterfacesCollection",
    "ServiceResourcePlacementGroupsCollection",
    "ServiceResourceRouteTablesCollection",
    "ServiceResourceSecurityGroupsCollection",
    "ServiceResourceSnapshotsCollection",
    "ServiceResourceSubnetsCollection",
    "ServiceResourceVolumesCollection",
    "ServiceResourceVpcAddressesCollection",
    "ServiceResourceVpcPeeringConnectionsCollection",
    "ServiceResourceVpcsCollection",
    "InstanceVolumesCollection",
    "InstanceVpcAddressesCollection",
    "PlacementGroupInstancesCollection",
    "SubnetInstancesCollection",
    "SubnetNetworkInterfacesCollection",
    "VolumeSnapshotsCollection",
    "VpcAcceptedVpcPeeringConnectionsCollection",
    "VpcInstancesCollection",
    "VpcInternetGatewaysCollection",
    "VpcNetworkAclsCollection",
    "VpcNetworkInterfacesCollection",
    "VpcRequestedVpcPeeringConnectionsCollection",
    "VpcRouteTablesCollection",
    "VpcSecurityGroupsCollection",
    "VpcSubnetsCollection",
)


class ServiceResourceClassicAddressesCollection(AIOResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.classic_addresses)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourceclassicaddressescollection)
    """

    def all(self) -> "ServiceResourceClassicAddressesCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.classic_addresses)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourceclassicaddressescollection)
        """

    def filter(  # type: ignore
        self,
        *,
        Filters: Sequence[FilterTypeDef] = ...,
        PublicIps: Sequence[str] = ...,
        AllocationIds: Sequence[str] = ...,
        DryRun: bool = ...,
    ) -> "ServiceResourceClassicAddressesCollection":
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.classic_addresses)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourceclassicaddressescollection)
        """

    def limit(self, count: int) -> "ServiceResourceClassicAddressesCollection":
        """
        Return at most this many ClassicAddresss.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.classic_addresses)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourceclassicaddressescollection)
        """

    def page_size(self, count: int) -> "ServiceResourceClassicAddressesCollection":
        """
        Fetch at most this many ClassicAddresss per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.classic_addresses)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourceclassicaddressescollection)
        """

    def pages(self) -> AsyncIterator[List["ClassicAddress"]]:
        """
        A generator which yields pages of ClassicAddresss.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.classic_addresses)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourceclassicaddressescollection)
        """

    def __iter__(self) -> NoReturn:
        """
        A generator which yields ClassicAddresss.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.classic_addresses)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourceclassicaddressescollection)
        """

    def __aiter__(self) -> AsyncIterator["ClassicAddress"]:
        """
        A generator which yields ClassicAddresss.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.classic_addresses)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourceclassicaddressescollection)
        """


class ServiceResourceDhcpOptionsSetsCollection(AIOResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.dhcp_options_sets)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourcedhcpoptionssetscollection)
    """

    def all(self) -> "ServiceResourceDhcpOptionsSetsCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.dhcp_options_sets)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourcedhcpoptionssetscollection)
        """

    def filter(  # type: ignore
        self,
        *,
        DhcpOptionsIds: Sequence[str] = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        DryRun: bool = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
    ) -> "ServiceResourceDhcpOptionsSetsCollection":
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.dhcp_options_sets)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourcedhcpoptionssetscollection)
        """

    def limit(self, count: int) -> "ServiceResourceDhcpOptionsSetsCollection":
        """
        Return at most this many DhcpOptionss.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.dhcp_options_sets)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourcedhcpoptionssetscollection)
        """

    def page_size(self, count: int) -> "ServiceResourceDhcpOptionsSetsCollection":
        """
        Fetch at most this many DhcpOptionss per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.dhcp_options_sets)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourcedhcpoptionssetscollection)
        """

    def pages(self) -> AsyncIterator[List["DhcpOptions"]]:
        """
        A generator which yields pages of DhcpOptionss.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.dhcp_options_sets)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourcedhcpoptionssetscollection)
        """

    def __iter__(self) -> NoReturn:
        """
        A generator which yields DhcpOptionss.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.dhcp_options_sets)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourcedhcpoptionssetscollection)
        """

    def __aiter__(self) -> AsyncIterator["DhcpOptions"]:
        """
        A generator which yields DhcpOptionss.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.dhcp_options_sets)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourcedhcpoptionssetscollection)
        """


class ServiceResourceImagesCollection(AIOResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.images)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourceimagescollection)
    """

    def all(self) -> "ServiceResourceImagesCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.images)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourceimagescollection)
        """

    def filter(  # type: ignore
        self,
        *,
        ExecutableUsers: Sequence[str] = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        ImageIds: Sequence[str] = ...,
        Owners: Sequence[str] = ...,
        IncludeDeprecated: bool = ...,
        IncludeDisabled: bool = ...,
        DryRun: bool = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
    ) -> "ServiceResourceImagesCollection":
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.images)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourceimagescollection)
        """

    def limit(self, count: int) -> "ServiceResourceImagesCollection":
        """
        Return at most this many Images.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.images)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourceimagescollection)
        """

    def page_size(self, count: int) -> "ServiceResourceImagesCollection":
        """
        Fetch at most this many Images per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.images)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourceimagescollection)
        """

    def pages(self) -> AsyncIterator[List["Image"]]:
        """
        A generator which yields pages of Images.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.images)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourceimagescollection)
        """

    def __iter__(self) -> NoReturn:
        """
        A generator which yields Images.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.images)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourceimagescollection)
        """

    def __aiter__(self) -> AsyncIterator["Image"]:
        """
        A generator which yields Images.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.images)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourceimagescollection)
        """


class ServiceResourceInstancesCollection(AIOResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.instances)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourceinstancescollection)
    """

    def all(self) -> "ServiceResourceInstancesCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.instances)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourceinstancescollection)
        """

    def filter(  # type: ignore
        self,
        *,
        Filters: Sequence[FilterTypeDef] = ...,
        InstanceIds: Sequence[str] = ...,
        DryRun: bool = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
    ) -> "ServiceResourceInstancesCollection":
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.instances)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourceinstancescollection)
        """

    async def create_tags(self, *, DryRun: bool = ...) -> None:
        """
        Batch method.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.instances)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourceinstancescollection)
        """

    async def monitor(self, *, DryRun: bool = ...) -> List[MonitorInstancesResultTypeDef]:
        """
        Batch method.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.instances)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourceinstancescollection)
        """

    async def reboot(self, *, DryRun: bool = ...) -> None:
        """
        Batch method.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.instances)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourceinstancescollection)
        """

    async def start(
        self, *, AdditionalInfo: str = ..., DryRun: bool = ...
    ) -> List[StartInstancesResultTypeDef]:
        """
        Batch method.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.instances)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourceinstancescollection)
        """

    async def stop(
        self, *, Hibernate: bool = ..., DryRun: bool = ..., Force: bool = ...
    ) -> List[StopInstancesResultTypeDef]:
        """
        Batch method.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.instances)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourceinstancescollection)
        """

    async def terminate(self, *, DryRun: bool = ...) -> List[TerminateInstancesResultTypeDef]:
        """
        Batch method.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.instances)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourceinstancescollection)
        """

    async def unmonitor(self, *, DryRun: bool = ...) -> List[UnmonitorInstancesResultTypeDef]:
        """
        Batch method.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.instances)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourceinstancescollection)
        """

    def limit(self, count: int) -> "ServiceResourceInstancesCollection":
        """
        Return at most this many Instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.instances)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourceinstancescollection)
        """

    def page_size(self, count: int) -> "ServiceResourceInstancesCollection":
        """
        Fetch at most this many Instances per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.instances)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourceinstancescollection)
        """

    def pages(self) -> AsyncIterator[List["Instance"]]:
        """
        A generator which yields pages of Instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.instances)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourceinstancescollection)
        """

    def __iter__(self) -> NoReturn:
        """
        A generator which yields Instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.instances)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourceinstancescollection)
        """

    def __aiter__(self) -> AsyncIterator["Instance"]:
        """
        A generator which yields Instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.instances)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourceinstancescollection)
        """


class ServiceResourceInternetGatewaysCollection(AIOResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.internet_gateways)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourceinternetgatewayscollection)
    """

    def all(self) -> "ServiceResourceInternetGatewaysCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.internet_gateways)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourceinternetgatewayscollection)
        """

    def filter(  # type: ignore
        self,
        *,
        Filters: Sequence[FilterTypeDef] = ...,
        DryRun: bool = ...,
        InternetGatewayIds: Sequence[str] = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
    ) -> "ServiceResourceInternetGatewaysCollection":
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.internet_gateways)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourceinternetgatewayscollection)
        """

    def limit(self, count: int) -> "ServiceResourceInternetGatewaysCollection":
        """
        Return at most this many InternetGateways.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.internet_gateways)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourceinternetgatewayscollection)
        """

    def page_size(self, count: int) -> "ServiceResourceInternetGatewaysCollection":
        """
        Fetch at most this many InternetGateways per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.internet_gateways)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourceinternetgatewayscollection)
        """

    def pages(self) -> AsyncIterator[List["InternetGateway"]]:
        """
        A generator which yields pages of InternetGateways.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.internet_gateways)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourceinternetgatewayscollection)
        """

    def __iter__(self) -> NoReturn:
        """
        A generator which yields InternetGateways.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.internet_gateways)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourceinternetgatewayscollection)
        """

    def __aiter__(self) -> AsyncIterator["InternetGateway"]:
        """
        A generator which yields InternetGateways.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.internet_gateways)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourceinternetgatewayscollection)
        """


class ServiceResourceKeyPairsCollection(AIOResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.key_pairs)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourcekeypairscollection)
    """

    def all(self) -> "ServiceResourceKeyPairsCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.key_pairs)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourcekeypairscollection)
        """

    def filter(  # type: ignore
        self,
        *,
        Filters: Sequence[FilterTypeDef] = ...,
        KeyNames: Sequence[str] = ...,
        KeyPairIds: Sequence[str] = ...,
        DryRun: bool = ...,
        IncludePublicKey: bool = ...,
    ) -> "ServiceResourceKeyPairsCollection":
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.key_pairs)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourcekeypairscollection)
        """

    def limit(self, count: int) -> "ServiceResourceKeyPairsCollection":
        """
        Return at most this many KeyPairInfos.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.key_pairs)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourcekeypairscollection)
        """

    def page_size(self, count: int) -> "ServiceResourceKeyPairsCollection":
        """
        Fetch at most this many KeyPairInfos per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.key_pairs)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourcekeypairscollection)
        """

    def pages(self) -> AsyncIterator[List["KeyPairInfo"]]:
        """
        A generator which yields pages of KeyPairInfos.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.key_pairs)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourcekeypairscollection)
        """

    def __iter__(self) -> NoReturn:
        """
        A generator which yields KeyPairInfos.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.key_pairs)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourcekeypairscollection)
        """

    def __aiter__(self) -> AsyncIterator["KeyPairInfo"]:
        """
        A generator which yields KeyPairInfos.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.key_pairs)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourcekeypairscollection)
        """


class ServiceResourceNetworkAclsCollection(AIOResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.network_acls)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourcenetworkaclscollection)
    """

    def all(self) -> "ServiceResourceNetworkAclsCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.network_acls)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourcenetworkaclscollection)
        """

    def filter(  # type: ignore
        self,
        *,
        Filters: Sequence[FilterTypeDef] = ...,
        DryRun: bool = ...,
        NetworkAclIds: Sequence[str] = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
    ) -> "ServiceResourceNetworkAclsCollection":
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.network_acls)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourcenetworkaclscollection)
        """

    def limit(self, count: int) -> "ServiceResourceNetworkAclsCollection":
        """
        Return at most this many NetworkAcls.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.network_acls)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourcenetworkaclscollection)
        """

    def page_size(self, count: int) -> "ServiceResourceNetworkAclsCollection":
        """
        Fetch at most this many NetworkAcls per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.network_acls)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourcenetworkaclscollection)
        """

    def pages(self) -> AsyncIterator[List["NetworkAcl"]]:
        """
        A generator which yields pages of NetworkAcls.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.network_acls)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourcenetworkaclscollection)
        """

    def __iter__(self) -> NoReturn:
        """
        A generator which yields NetworkAcls.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.network_acls)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourcenetworkaclscollection)
        """

    def __aiter__(self) -> AsyncIterator["NetworkAcl"]:
        """
        A generator which yields NetworkAcls.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.network_acls)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourcenetworkaclscollection)
        """


class ServiceResourceNetworkInterfacesCollection(AIOResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.network_interfaces)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourcenetworkinterfacescollection)
    """

    def all(self) -> "ServiceResourceNetworkInterfacesCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.network_interfaces)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourcenetworkinterfacescollection)
        """

    def filter(  # type: ignore
        self,
        *,
        Filters: Sequence[FilterTypeDef] = ...,
        DryRun: bool = ...,
        NetworkInterfaceIds: Sequence[str] = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
    ) -> "ServiceResourceNetworkInterfacesCollection":
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.network_interfaces)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourcenetworkinterfacescollection)
        """

    def limit(self, count: int) -> "ServiceResourceNetworkInterfacesCollection":
        """
        Return at most this many NetworkInterfaces.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.network_interfaces)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourcenetworkinterfacescollection)
        """

    def page_size(self, count: int) -> "ServiceResourceNetworkInterfacesCollection":
        """
        Fetch at most this many NetworkInterfaces per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.network_interfaces)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourcenetworkinterfacescollection)
        """

    def pages(self) -> AsyncIterator[List["NetworkInterface"]]:
        """
        A generator which yields pages of NetworkInterfaces.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.network_interfaces)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourcenetworkinterfacescollection)
        """

    def __iter__(self) -> NoReturn:
        """
        A generator which yields NetworkInterfaces.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.network_interfaces)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourcenetworkinterfacescollection)
        """

    def __aiter__(self) -> AsyncIterator["NetworkInterface"]:
        """
        A generator which yields NetworkInterfaces.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.network_interfaces)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourcenetworkinterfacescollection)
        """


class ServiceResourcePlacementGroupsCollection(AIOResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.placement_groups)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourceplacementgroupscollection)
    """

    def all(self) -> "ServiceResourcePlacementGroupsCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.placement_groups)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourceplacementgroupscollection)
        """

    def filter(  # type: ignore
        self,
        *,
        Filters: Sequence[FilterTypeDef] = ...,
        DryRun: bool = ...,
        GroupNames: Sequence[str] = ...,
        GroupIds: Sequence[str] = ...,
    ) -> "ServiceResourcePlacementGroupsCollection":
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.placement_groups)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourceplacementgroupscollection)
        """

    def limit(self, count: int) -> "ServiceResourcePlacementGroupsCollection":
        """
        Return at most this many PlacementGroups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.placement_groups)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourceplacementgroupscollection)
        """

    def page_size(self, count: int) -> "ServiceResourcePlacementGroupsCollection":
        """
        Fetch at most this many PlacementGroups per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.placement_groups)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourceplacementgroupscollection)
        """

    def pages(self) -> AsyncIterator[List["PlacementGroup"]]:
        """
        A generator which yields pages of PlacementGroups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.placement_groups)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourceplacementgroupscollection)
        """

    def __iter__(self) -> NoReturn:
        """
        A generator which yields PlacementGroups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.placement_groups)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourceplacementgroupscollection)
        """

    def __aiter__(self) -> AsyncIterator["PlacementGroup"]:
        """
        A generator which yields PlacementGroups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.placement_groups)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourceplacementgroupscollection)
        """


class ServiceResourceRouteTablesCollection(AIOResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.route_tables)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourceroutetablescollection)
    """

    def all(self) -> "ServiceResourceRouteTablesCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.route_tables)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourceroutetablescollection)
        """

    def filter(  # type: ignore
        self,
        *,
        Filters: Sequence[FilterTypeDef] = ...,
        DryRun: bool = ...,
        RouteTableIds: Sequence[str] = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
    ) -> "ServiceResourceRouteTablesCollection":
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.route_tables)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourceroutetablescollection)
        """

    def limit(self, count: int) -> "ServiceResourceRouteTablesCollection":
        """
        Return at most this many RouteTables.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.route_tables)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourceroutetablescollection)
        """

    def page_size(self, count: int) -> "ServiceResourceRouteTablesCollection":
        """
        Fetch at most this many RouteTables per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.route_tables)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourceroutetablescollection)
        """

    def pages(self) -> AsyncIterator[List["RouteTable"]]:
        """
        A generator which yields pages of RouteTables.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.route_tables)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourceroutetablescollection)
        """

    def __iter__(self) -> NoReturn:
        """
        A generator which yields RouteTables.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.route_tables)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourceroutetablescollection)
        """

    def __aiter__(self) -> AsyncIterator["RouteTable"]:
        """
        A generator which yields RouteTables.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.route_tables)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourceroutetablescollection)
        """


class ServiceResourceSecurityGroupsCollection(AIOResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.security_groups)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourcesecuritygroupscollection)
    """

    def all(self) -> "ServiceResourceSecurityGroupsCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.security_groups)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourcesecuritygroupscollection)
        """

    def filter(  # type: ignore
        self,
        *,
        Filters: Sequence[FilterTypeDef] = ...,
        GroupIds: Sequence[str] = ...,
        GroupNames: Sequence[str] = ...,
        DryRun: bool = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
    ) -> "ServiceResourceSecurityGroupsCollection":
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.security_groups)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourcesecuritygroupscollection)
        """

    def limit(self, count: int) -> "ServiceResourceSecurityGroupsCollection":
        """
        Return at most this many SecurityGroups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.security_groups)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourcesecuritygroupscollection)
        """

    def page_size(self, count: int) -> "ServiceResourceSecurityGroupsCollection":
        """
        Fetch at most this many SecurityGroups per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.security_groups)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourcesecuritygroupscollection)
        """

    def pages(self) -> AsyncIterator[List["SecurityGroup"]]:
        """
        A generator which yields pages of SecurityGroups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.security_groups)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourcesecuritygroupscollection)
        """

    def __iter__(self) -> NoReturn:
        """
        A generator which yields SecurityGroups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.security_groups)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourcesecuritygroupscollection)
        """

    def __aiter__(self) -> AsyncIterator["SecurityGroup"]:
        """
        A generator which yields SecurityGroups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.security_groups)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourcesecuritygroupscollection)
        """


class ServiceResourceSnapshotsCollection(AIOResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.snapshots)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourcesnapshotscollection)
    """

    def all(self) -> "ServiceResourceSnapshotsCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.snapshots)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourcesnapshotscollection)
        """

    def filter(  # type: ignore
        self,
        *,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
        OwnerIds: Sequence[str] = ...,
        RestorableByUserIds: Sequence[str] = ...,
        SnapshotIds: Sequence[str] = ...,
        DryRun: bool = ...,
    ) -> "ServiceResourceSnapshotsCollection":
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.snapshots)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourcesnapshotscollection)
        """

    def limit(self, count: int) -> "ServiceResourceSnapshotsCollection":
        """
        Return at most this many Snapshots.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.snapshots)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourcesnapshotscollection)
        """

    def page_size(self, count: int) -> "ServiceResourceSnapshotsCollection":
        """
        Fetch at most this many Snapshots per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.snapshots)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourcesnapshotscollection)
        """

    def pages(self) -> AsyncIterator[List["Snapshot"]]:
        """
        A generator which yields pages of Snapshots.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.snapshots)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourcesnapshotscollection)
        """

    def __iter__(self) -> NoReturn:
        """
        A generator which yields Snapshots.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.snapshots)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourcesnapshotscollection)
        """

    def __aiter__(self) -> AsyncIterator["Snapshot"]:
        """
        A generator which yields Snapshots.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.snapshots)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourcesnapshotscollection)
        """


class ServiceResourceSubnetsCollection(AIOResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.subnets)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourcesubnetscollection)
    """

    def all(self) -> "ServiceResourceSubnetsCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.subnets)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourcesubnetscollection)
        """

    def filter(  # type: ignore
        self,
        *,
        Filters: Sequence[FilterTypeDef] = ...,
        SubnetIds: Sequence[str] = ...,
        DryRun: bool = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
    ) -> "ServiceResourceSubnetsCollection":
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.subnets)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourcesubnetscollection)
        """

    def limit(self, count: int) -> "ServiceResourceSubnetsCollection":
        """
        Return at most this many Subnets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.subnets)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourcesubnetscollection)
        """

    def page_size(self, count: int) -> "ServiceResourceSubnetsCollection":
        """
        Fetch at most this many Subnets per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.subnets)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourcesubnetscollection)
        """

    def pages(self) -> AsyncIterator[List["Subnet"]]:
        """
        A generator which yields pages of Subnets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.subnets)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourcesubnetscollection)
        """

    def __iter__(self) -> NoReturn:
        """
        A generator which yields Subnets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.subnets)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourcesubnetscollection)
        """

    def __aiter__(self) -> AsyncIterator["Subnet"]:
        """
        A generator which yields Subnets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.subnets)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourcesubnetscollection)
        """


class ServiceResourceVolumesCollection(AIOResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.volumes)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourcevolumescollection)
    """

    def all(self) -> "ServiceResourceVolumesCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.volumes)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourcevolumescollection)
        """

    def filter(  # type: ignore
        self,
        *,
        Filters: Sequence[FilterTypeDef] = ...,
        VolumeIds: Sequence[str] = ...,
        DryRun: bool = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
    ) -> "ServiceResourceVolumesCollection":
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.volumes)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourcevolumescollection)
        """

    def limit(self, count: int) -> "ServiceResourceVolumesCollection":
        """
        Return at most this many Volumes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.volumes)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourcevolumescollection)
        """

    def page_size(self, count: int) -> "ServiceResourceVolumesCollection":
        """
        Fetch at most this many Volumes per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.volumes)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourcevolumescollection)
        """

    def pages(self) -> AsyncIterator[List["Volume"]]:
        """
        A generator which yields pages of Volumes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.volumes)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourcevolumescollection)
        """

    def __iter__(self) -> NoReturn:
        """
        A generator which yields Volumes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.volumes)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourcevolumescollection)
        """

    def __aiter__(self) -> AsyncIterator["Volume"]:
        """
        A generator which yields Volumes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.volumes)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourcevolumescollection)
        """


class ServiceResourceVpcAddressesCollection(AIOResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.vpc_addresses)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourcevpcaddressescollection)
    """

    def all(self) -> "ServiceResourceVpcAddressesCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.vpc_addresses)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourcevpcaddressescollection)
        """

    def filter(  # type: ignore
        self,
        *,
        Filters: Sequence[FilterTypeDef] = ...,
        PublicIps: Sequence[str] = ...,
        AllocationIds: Sequence[str] = ...,
        DryRun: bool = ...,
    ) -> "ServiceResourceVpcAddressesCollection":
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.vpc_addresses)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourcevpcaddressescollection)
        """

    def limit(self, count: int) -> "ServiceResourceVpcAddressesCollection":
        """
        Return at most this many VpcAddresss.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.vpc_addresses)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourcevpcaddressescollection)
        """

    def page_size(self, count: int) -> "ServiceResourceVpcAddressesCollection":
        """
        Fetch at most this many VpcAddresss per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.vpc_addresses)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourcevpcaddressescollection)
        """

    def pages(self) -> AsyncIterator[List["VpcAddress"]]:
        """
        A generator which yields pages of VpcAddresss.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.vpc_addresses)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourcevpcaddressescollection)
        """

    def __iter__(self) -> NoReturn:
        """
        A generator which yields VpcAddresss.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.vpc_addresses)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourcevpcaddressescollection)
        """

    def __aiter__(self) -> AsyncIterator["VpcAddress"]:
        """
        A generator which yields VpcAddresss.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.vpc_addresses)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourcevpcaddressescollection)
        """


class ServiceResourceVpcPeeringConnectionsCollection(AIOResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.vpc_peering_connections)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourcevpcpeeringconnectionscollection)
    """

    def all(self) -> "ServiceResourceVpcPeeringConnectionsCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.vpc_peering_connections)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourcevpcpeeringconnectionscollection)
        """

    def filter(  # type: ignore
        self,
        *,
        Filters: Sequence[FilterTypeDef] = ...,
        DryRun: bool = ...,
        VpcPeeringConnectionIds: Sequence[str] = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
    ) -> "ServiceResourceVpcPeeringConnectionsCollection":
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.vpc_peering_connections)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourcevpcpeeringconnectionscollection)
        """

    def limit(self, count: int) -> "ServiceResourceVpcPeeringConnectionsCollection":
        """
        Return at most this many VpcPeeringConnections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.vpc_peering_connections)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourcevpcpeeringconnectionscollection)
        """

    def page_size(self, count: int) -> "ServiceResourceVpcPeeringConnectionsCollection":
        """
        Fetch at most this many VpcPeeringConnections per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.vpc_peering_connections)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourcevpcpeeringconnectionscollection)
        """

    def pages(self) -> AsyncIterator[List["VpcPeeringConnection"]]:
        """
        A generator which yields pages of VpcPeeringConnections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.vpc_peering_connections)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourcevpcpeeringconnectionscollection)
        """

    def __iter__(self) -> NoReturn:
        """
        A generator which yields VpcPeeringConnections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.vpc_peering_connections)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourcevpcpeeringconnectionscollection)
        """

    def __aiter__(self) -> AsyncIterator["VpcPeeringConnection"]:
        """
        A generator which yields VpcPeeringConnections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.vpc_peering_connections)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourcevpcpeeringconnectionscollection)
        """


class ServiceResourceVpcsCollection(AIOResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.vpcs)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourcevpcscollection)
    """

    def all(self) -> "ServiceResourceVpcsCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.vpcs)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourcevpcscollection)
        """

    def filter(  # type: ignore
        self,
        *,
        Filters: Sequence[FilterTypeDef] = ...,
        VpcIds: Sequence[str] = ...,
        DryRun: bool = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
    ) -> "ServiceResourceVpcsCollection":
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.vpcs)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourcevpcscollection)
        """

    def limit(self, count: int) -> "ServiceResourceVpcsCollection":
        """
        Return at most this many Vpcs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.vpcs)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourcevpcscollection)
        """

    def page_size(self, count: int) -> "ServiceResourceVpcsCollection":
        """
        Fetch at most this many Vpcs per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.vpcs)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourcevpcscollection)
        """

    def pages(self) -> AsyncIterator[List["Vpc"]]:
        """
        A generator which yields pages of Vpcs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.vpcs)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourcevpcscollection)
        """

    def __iter__(self) -> NoReturn:
        """
        A generator which yields Vpcs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.vpcs)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourcevpcscollection)
        """

    def __aiter__(self) -> AsyncIterator["Vpc"]:
        """
        A generator which yields Vpcs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.vpcs)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#serviceresourcevpcscollection)
        """


class InstanceVolumesCollection(AIOResourceCollection):
    def all(self) -> "InstanceVolumesCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.
        """

    def filter(  # type: ignore
        self,
        *,
        Filters: Sequence[FilterTypeDef] = ...,
        VolumeIds: Sequence[str] = ...,
        DryRun: bool = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
    ) -> "InstanceVolumesCollection":
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.
        """

    def limit(self, count: int) -> "InstanceVolumesCollection":
        """
        Return at most this many Volumes.
        """

    def page_size(self, count: int) -> "InstanceVolumesCollection":
        """
        Fetch at most this many Volumes per service request.
        """

    def pages(self) -> AsyncIterator[List["Volume"]]:
        """
        A generator which yields pages of Volumes.
        """

    def __iter__(self) -> NoReturn:
        """
        A generator which yields Volumes.
        """

    def __aiter__(self) -> AsyncIterator["Volume"]:
        """
        A generator which yields Volumes.
        """


class InstanceVpcAddressesCollection(AIOResourceCollection):
    def all(self) -> "InstanceVpcAddressesCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.
        """

    def filter(  # type: ignore
        self,
        *,
        Filters: Sequence[FilterTypeDef] = ...,
        PublicIps: Sequence[str] = ...,
        AllocationIds: Sequence[str] = ...,
        DryRun: bool = ...,
    ) -> "InstanceVpcAddressesCollection":
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.
        """

    def limit(self, count: int) -> "InstanceVpcAddressesCollection":
        """
        Return at most this many VpcAddresss.
        """

    def page_size(self, count: int) -> "InstanceVpcAddressesCollection":
        """
        Fetch at most this many VpcAddresss per service request.
        """

    def pages(self) -> AsyncIterator[List["VpcAddress"]]:
        """
        A generator which yields pages of VpcAddresss.
        """

    def __iter__(self) -> NoReturn:
        """
        A generator which yields VpcAddresss.
        """

    def __aiter__(self) -> AsyncIterator["VpcAddress"]:
        """
        A generator which yields VpcAddresss.
        """


class PlacementGroupInstancesCollection(AIOResourceCollection):
    def all(self) -> "PlacementGroupInstancesCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.
        """

    def filter(  # type: ignore
        self,
        *,
        Filters: Sequence[FilterTypeDef] = ...,
        InstanceIds: Sequence[str] = ...,
        DryRun: bool = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
    ) -> "PlacementGroupInstancesCollection":
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.
        """

    async def create_tags(self, *, DryRun: bool = ...) -> None:
        """
        Batch method.
        """

    async def monitor(self, *, DryRun: bool = ...) -> List[MonitorInstancesResultTypeDef]:
        """
        Batch method.
        """

    async def reboot(self, *, DryRun: bool = ...) -> None:
        """
        Batch method.
        """

    async def start(
        self, *, AdditionalInfo: str = ..., DryRun: bool = ...
    ) -> List[StartInstancesResultTypeDef]:
        """
        Batch method.
        """

    async def stop(
        self, *, Hibernate: bool = ..., DryRun: bool = ..., Force: bool = ...
    ) -> List[StopInstancesResultTypeDef]:
        """
        Batch method.
        """

    async def terminate(self, *, DryRun: bool = ...) -> List[TerminateInstancesResultTypeDef]:
        """
        Batch method.
        """

    async def unmonitor(self, *, DryRun: bool = ...) -> List[UnmonitorInstancesResultTypeDef]:
        """
        Batch method.
        """

    def limit(self, count: int) -> "PlacementGroupInstancesCollection":
        """
        Return at most this many Instances.
        """

    def page_size(self, count: int) -> "PlacementGroupInstancesCollection":
        """
        Fetch at most this many Instances per service request.
        """

    def pages(self) -> AsyncIterator[List["Instance"]]:
        """
        A generator which yields pages of Instances.
        """

    def __iter__(self) -> NoReturn:
        """
        A generator which yields Instances.
        """

    def __aiter__(self) -> AsyncIterator["Instance"]:
        """
        A generator which yields Instances.
        """


class SubnetInstancesCollection(AIOResourceCollection):
    def all(self) -> "SubnetInstancesCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.
        """

    def filter(  # type: ignore
        self,
        *,
        Filters: Sequence[FilterTypeDef] = ...,
        InstanceIds: Sequence[str] = ...,
        DryRun: bool = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
    ) -> "SubnetInstancesCollection":
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.
        """

    async def create_tags(self, *, DryRun: bool = ...) -> None:
        """
        Batch method.
        """

    async def monitor(self, *, DryRun: bool = ...) -> List[MonitorInstancesResultTypeDef]:
        """
        Batch method.
        """

    async def reboot(self, *, DryRun: bool = ...) -> None:
        """
        Batch method.
        """

    async def start(
        self, *, AdditionalInfo: str = ..., DryRun: bool = ...
    ) -> List[StartInstancesResultTypeDef]:
        """
        Batch method.
        """

    async def stop(
        self, *, Hibernate: bool = ..., DryRun: bool = ..., Force: bool = ...
    ) -> List[StopInstancesResultTypeDef]:
        """
        Batch method.
        """

    async def terminate(self, *, DryRun: bool = ...) -> List[TerminateInstancesResultTypeDef]:
        """
        Batch method.
        """

    async def unmonitor(self, *, DryRun: bool = ...) -> List[UnmonitorInstancesResultTypeDef]:
        """
        Batch method.
        """

    def limit(self, count: int) -> "SubnetInstancesCollection":
        """
        Return at most this many Instances.
        """

    def page_size(self, count: int) -> "SubnetInstancesCollection":
        """
        Fetch at most this many Instances per service request.
        """

    def pages(self) -> AsyncIterator[List["Instance"]]:
        """
        A generator which yields pages of Instances.
        """

    def __iter__(self) -> NoReturn:
        """
        A generator which yields Instances.
        """

    def __aiter__(self) -> AsyncIterator["Instance"]:
        """
        A generator which yields Instances.
        """


class SubnetNetworkInterfacesCollection(AIOResourceCollection):
    def all(self) -> "SubnetNetworkInterfacesCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.
        """

    def filter(  # type: ignore
        self,
        *,
        Filters: Sequence[FilterTypeDef] = ...,
        DryRun: bool = ...,
        NetworkInterfaceIds: Sequence[str] = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
    ) -> "SubnetNetworkInterfacesCollection":
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.
        """

    def limit(self, count: int) -> "SubnetNetworkInterfacesCollection":
        """
        Return at most this many NetworkInterfaces.
        """

    def page_size(self, count: int) -> "SubnetNetworkInterfacesCollection":
        """
        Fetch at most this many NetworkInterfaces per service request.
        """

    def pages(self) -> AsyncIterator[List["NetworkInterface"]]:
        """
        A generator which yields pages of NetworkInterfaces.
        """

    def __iter__(self) -> NoReturn:
        """
        A generator which yields NetworkInterfaces.
        """

    def __aiter__(self) -> AsyncIterator["NetworkInterface"]:
        """
        A generator which yields NetworkInterfaces.
        """


class VolumeSnapshotsCollection(AIOResourceCollection):
    def all(self) -> "VolumeSnapshotsCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.
        """

    def filter(  # type: ignore
        self,
        *,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
        OwnerIds: Sequence[str] = ...,
        RestorableByUserIds: Sequence[str] = ...,
        SnapshotIds: Sequence[str] = ...,
        DryRun: bool = ...,
    ) -> "VolumeSnapshotsCollection":
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.
        """

    def limit(self, count: int) -> "VolumeSnapshotsCollection":
        """
        Return at most this many Snapshots.
        """

    def page_size(self, count: int) -> "VolumeSnapshotsCollection":
        """
        Fetch at most this many Snapshots per service request.
        """

    def pages(self) -> AsyncIterator[List["Snapshot"]]:
        """
        A generator which yields pages of Snapshots.
        """

    def __iter__(self) -> NoReturn:
        """
        A generator which yields Snapshots.
        """

    def __aiter__(self) -> AsyncIterator["Snapshot"]:
        """
        A generator which yields Snapshots.
        """


class VpcAcceptedVpcPeeringConnectionsCollection(AIOResourceCollection):
    def all(self) -> "VpcAcceptedVpcPeeringConnectionsCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.
        """

    def filter(  # type: ignore
        self,
        *,
        Filters: Sequence[FilterTypeDef] = ...,
        DryRun: bool = ...,
        VpcPeeringConnectionIds: Sequence[str] = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
    ) -> "VpcAcceptedVpcPeeringConnectionsCollection":
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.
        """

    def limit(self, count: int) -> "VpcAcceptedVpcPeeringConnectionsCollection":
        """
        Return at most this many VpcPeeringConnections.
        """

    def page_size(self, count: int) -> "VpcAcceptedVpcPeeringConnectionsCollection":
        """
        Fetch at most this many VpcPeeringConnections per service request.
        """

    def pages(self) -> AsyncIterator[List["VpcPeeringConnection"]]:
        """
        A generator which yields pages of VpcPeeringConnections.
        """

    def __iter__(self) -> NoReturn:
        """
        A generator which yields VpcPeeringConnections.
        """

    def __aiter__(self) -> AsyncIterator["VpcPeeringConnection"]:
        """
        A generator which yields VpcPeeringConnections.
        """


class VpcInstancesCollection(AIOResourceCollection):
    def all(self) -> "VpcInstancesCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.
        """

    def filter(  # type: ignore
        self,
        *,
        Filters: Sequence[FilterTypeDef] = ...,
        InstanceIds: Sequence[str] = ...,
        DryRun: bool = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
    ) -> "VpcInstancesCollection":
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.
        """

    async def create_tags(self, *, DryRun: bool = ...) -> None:
        """
        Batch method.
        """

    async def monitor(self, *, DryRun: bool = ...) -> List[MonitorInstancesResultTypeDef]:
        """
        Batch method.
        """

    async def reboot(self, *, DryRun: bool = ...) -> None:
        """
        Batch method.
        """

    async def start(
        self, *, AdditionalInfo: str = ..., DryRun: bool = ...
    ) -> List[StartInstancesResultTypeDef]:
        """
        Batch method.
        """

    async def stop(
        self, *, Hibernate: bool = ..., DryRun: bool = ..., Force: bool = ...
    ) -> List[StopInstancesResultTypeDef]:
        """
        Batch method.
        """

    async def terminate(self, *, DryRun: bool = ...) -> List[TerminateInstancesResultTypeDef]:
        """
        Batch method.
        """

    async def unmonitor(self, *, DryRun: bool = ...) -> List[UnmonitorInstancesResultTypeDef]:
        """
        Batch method.
        """

    def limit(self, count: int) -> "VpcInstancesCollection":
        """
        Return at most this many Instances.
        """

    def page_size(self, count: int) -> "VpcInstancesCollection":
        """
        Fetch at most this many Instances per service request.
        """

    def pages(self) -> AsyncIterator[List["Instance"]]:
        """
        A generator which yields pages of Instances.
        """

    def __iter__(self) -> NoReturn:
        """
        A generator which yields Instances.
        """

    def __aiter__(self) -> AsyncIterator["Instance"]:
        """
        A generator which yields Instances.
        """


class VpcInternetGatewaysCollection(AIOResourceCollection):
    def all(self) -> "VpcInternetGatewaysCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.
        """

    def filter(  # type: ignore
        self,
        *,
        Filters: Sequence[FilterTypeDef] = ...,
        DryRun: bool = ...,
        InternetGatewayIds: Sequence[str] = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
    ) -> "VpcInternetGatewaysCollection":
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.
        """

    def limit(self, count: int) -> "VpcInternetGatewaysCollection":
        """
        Return at most this many InternetGateways.
        """

    def page_size(self, count: int) -> "VpcInternetGatewaysCollection":
        """
        Fetch at most this many InternetGateways per service request.
        """

    def pages(self) -> AsyncIterator[List["InternetGateway"]]:
        """
        A generator which yields pages of InternetGateways.
        """

    def __iter__(self) -> NoReturn:
        """
        A generator which yields InternetGateways.
        """

    def __aiter__(self) -> AsyncIterator["InternetGateway"]:
        """
        A generator which yields InternetGateways.
        """


class VpcNetworkAclsCollection(AIOResourceCollection):
    def all(self) -> "VpcNetworkAclsCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.
        """

    def filter(  # type: ignore
        self,
        *,
        Filters: Sequence[FilterTypeDef] = ...,
        DryRun: bool = ...,
        NetworkAclIds: Sequence[str] = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
    ) -> "VpcNetworkAclsCollection":
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.
        """

    def limit(self, count: int) -> "VpcNetworkAclsCollection":
        """
        Return at most this many NetworkAcls.
        """

    def page_size(self, count: int) -> "VpcNetworkAclsCollection":
        """
        Fetch at most this many NetworkAcls per service request.
        """

    def pages(self) -> AsyncIterator[List["NetworkAcl"]]:
        """
        A generator which yields pages of NetworkAcls.
        """

    def __iter__(self) -> NoReturn:
        """
        A generator which yields NetworkAcls.
        """

    def __aiter__(self) -> AsyncIterator["NetworkAcl"]:
        """
        A generator which yields NetworkAcls.
        """


class VpcNetworkInterfacesCollection(AIOResourceCollection):
    def all(self) -> "VpcNetworkInterfacesCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.
        """

    def filter(  # type: ignore
        self,
        *,
        Filters: Sequence[FilterTypeDef] = ...,
        DryRun: bool = ...,
        NetworkInterfaceIds: Sequence[str] = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
    ) -> "VpcNetworkInterfacesCollection":
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.
        """

    def limit(self, count: int) -> "VpcNetworkInterfacesCollection":
        """
        Return at most this many NetworkInterfaces.
        """

    def page_size(self, count: int) -> "VpcNetworkInterfacesCollection":
        """
        Fetch at most this many NetworkInterfaces per service request.
        """

    def pages(self) -> AsyncIterator[List["NetworkInterface"]]:
        """
        A generator which yields pages of NetworkInterfaces.
        """

    def __iter__(self) -> NoReturn:
        """
        A generator which yields NetworkInterfaces.
        """

    def __aiter__(self) -> AsyncIterator["NetworkInterface"]:
        """
        A generator which yields NetworkInterfaces.
        """


class VpcRequestedVpcPeeringConnectionsCollection(AIOResourceCollection):
    def all(self) -> "VpcRequestedVpcPeeringConnectionsCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.
        """

    def filter(  # type: ignore
        self,
        *,
        Filters: Sequence[FilterTypeDef] = ...,
        DryRun: bool = ...,
        VpcPeeringConnectionIds: Sequence[str] = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
    ) -> "VpcRequestedVpcPeeringConnectionsCollection":
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.
        """

    def limit(self, count: int) -> "VpcRequestedVpcPeeringConnectionsCollection":
        """
        Return at most this many VpcPeeringConnections.
        """

    def page_size(self, count: int) -> "VpcRequestedVpcPeeringConnectionsCollection":
        """
        Fetch at most this many VpcPeeringConnections per service request.
        """

    def pages(self) -> AsyncIterator[List["VpcPeeringConnection"]]:
        """
        A generator which yields pages of VpcPeeringConnections.
        """

    def __iter__(self) -> NoReturn:
        """
        A generator which yields VpcPeeringConnections.
        """

    def __aiter__(self) -> AsyncIterator["VpcPeeringConnection"]:
        """
        A generator which yields VpcPeeringConnections.
        """


class VpcRouteTablesCollection(AIOResourceCollection):
    def all(self) -> "VpcRouteTablesCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.
        """

    def filter(  # type: ignore
        self,
        *,
        Filters: Sequence[FilterTypeDef] = ...,
        DryRun: bool = ...,
        RouteTableIds: Sequence[str] = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
    ) -> "VpcRouteTablesCollection":
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.
        """

    def limit(self, count: int) -> "VpcRouteTablesCollection":
        """
        Return at most this many RouteTables.
        """

    def page_size(self, count: int) -> "VpcRouteTablesCollection":
        """
        Fetch at most this many RouteTables per service request.
        """

    def pages(self) -> AsyncIterator[List["RouteTable"]]:
        """
        A generator which yields pages of RouteTables.
        """

    def __iter__(self) -> NoReturn:
        """
        A generator which yields RouteTables.
        """

    def __aiter__(self) -> AsyncIterator["RouteTable"]:
        """
        A generator which yields RouteTables.
        """


class VpcSecurityGroupsCollection(AIOResourceCollection):
    def all(self) -> "VpcSecurityGroupsCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.
        """

    def filter(  # type: ignore
        self,
        *,
        Filters: Sequence[FilterTypeDef] = ...,
        GroupIds: Sequence[str] = ...,
        GroupNames: Sequence[str] = ...,
        DryRun: bool = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
    ) -> "VpcSecurityGroupsCollection":
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.
        """

    def limit(self, count: int) -> "VpcSecurityGroupsCollection":
        """
        Return at most this many SecurityGroups.
        """

    def page_size(self, count: int) -> "VpcSecurityGroupsCollection":
        """
        Fetch at most this many SecurityGroups per service request.
        """

    def pages(self) -> AsyncIterator[List["SecurityGroup"]]:
        """
        A generator which yields pages of SecurityGroups.
        """

    def __iter__(self) -> NoReturn:
        """
        A generator which yields SecurityGroups.
        """

    def __aiter__(self) -> AsyncIterator["SecurityGroup"]:
        """
        A generator which yields SecurityGroups.
        """


class VpcSubnetsCollection(AIOResourceCollection):
    def all(self) -> "VpcSubnetsCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.
        """

    def filter(  # type: ignore
        self,
        *,
        Filters: Sequence[FilterTypeDef] = ...,
        SubnetIds: Sequence[str] = ...,
        DryRun: bool = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
    ) -> "VpcSubnetsCollection":
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.
        """

    def limit(self, count: int) -> "VpcSubnetsCollection":
        """
        Return at most this many Subnets.
        """

    def page_size(self, count: int) -> "VpcSubnetsCollection":
        """
        Fetch at most this many Subnets per service request.
        """

    def pages(self) -> AsyncIterator[List["Subnet"]]:
        """
        A generator which yields pages of Subnets.
        """

    def __iter__(self) -> NoReturn:
        """
        A generator which yields Subnets.
        """

    def __aiter__(self) -> AsyncIterator["Subnet"]:
        """
        A generator which yields Subnets.
        """


class ClassicAddress(AIOBoto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.ClassicAddress)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#classicaddress)
    """

    instance_id: Awaitable[str]
    allocation_id: Awaitable[str]
    association_id: Awaitable[str]
    domain: Awaitable[DomainTypeType]
    network_interface_id: Awaitable[str]
    network_interface_owner_id: Awaitable[str]
    private_ip_address: Awaitable[str]
    tags: Awaitable[List[TagTypeDef]]
    public_ipv4_pool: Awaitable[str]
    network_border_group: Awaitable[str]
    customer_owned_ip: Awaitable[str]
    customer_owned_ipv4_pool: Awaitable[str]
    carrier_ip: Awaitable[str]
    public_ip: str
    meta: Awaitable["EC2ResourceMeta"]

    async def associate(
        self,
        *,
        AllocationId: str = ...,
        InstanceId: str = ...,
        AllowReassociation: bool = ...,
        DryRun: bool = ...,
        NetworkInterfaceId: str = ...,
        PrivateIpAddress: str = ...,
    ) -> AssociateAddressResultTypeDef:
        """
        Associates an Elastic IP address, or carrier IP address (for instances that are
        in subnets in Wavelength Zones) with an instance or a network
        interface.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ClassicAddress.associate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#classicaddressassociate-method)
        """

    async def disassociate(
        self, *, AssociationId: str = ..., PublicIp: str = ..., DryRun: bool = ...
    ) -> None:
        """
        Disassociates an Elastic IP address from the instance or network interface it's
        associated
        with.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ClassicAddress.disassociate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#classicaddressdisassociate-method)
        """

    async def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ClassicAddress.get_available_subresources)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#classicaddressget_available_subresources-method)
        """

    async def load(self) -> None:
        """
        Calls :py:meth:`EC2.Client.describe_addresses` to update the attributes of the
        ClassicAddress
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ClassicAddress.load)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#classicaddressload-method)
        """

    async def release(
        self,
        *,
        AllocationId: str = ...,
        PublicIp: str = ...,
        NetworkBorderGroup: str = ...,
        DryRun: bool = ...,
    ) -> None:
        """
        Releases the specified Elastic IP address.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ClassicAddress.release)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#classicaddressrelease-method)
        """

    async def reload(self) -> None:
        """
        Calls :py:meth:`EC2.Client.describe_addresses` to update the attributes of the
        ClassicAddress
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ClassicAddress.reload)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#classicaddressreload-method)
        """


_ClassicAddress = ClassicAddress


class DhcpOptions(AIOBoto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.DhcpOptions)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#dhcpoptions)
    """

    dhcp_configurations: Awaitable[List[DhcpConfigurationTypeDef]]
    dhcp_options_id: Awaitable[str]
    owner_id: Awaitable[str]
    tags: Awaitable[List[TagTypeDef]]
    id: str
    meta: Awaitable["EC2ResourceMeta"]

    async def associate_with_vpc(self, *, VpcId: str, DryRun: bool = ...) -> None:
        """
        Associates a set of DHCP options (that you've previously created) with the
        specified VPC, or associates no DHCP options with the
        VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.DhcpOptions.associate_with_vpc)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#dhcpoptionsassociate_with_vpc-method)
        """

    async def create_tags(self, *, Tags: Sequence[TagTypeDef], DryRun: bool = ...) -> None:
        """
        Adds or overwrites only the specified tags for the specified Amazon EC2
        resource or
        resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.DhcpOptions.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#dhcpoptionscreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Image.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#imagecreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.InternetGateway.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#internetgatewaycreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.NetworkAcl.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#networkaclcreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.NetworkInterface.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#networkinterfacecreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.RouteTable.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#routetablecreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.SecurityGroup.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#securitygroupcreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Snapshot.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#snapshotcreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Subnet.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#subnetcreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Volume.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#volumecreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Vpc.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#vpccreate_tags-method)
        """

    async def delete(self, *, DryRun: bool = ...) -> None:
        """
        Deletes the specified set of DHCP options.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.DhcpOptions.delete)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#dhcpoptionsdelete-method)
        """

    async def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.DhcpOptions.get_available_subresources)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#dhcpoptionsget_available_subresources-method)
        """

    async def load(self) -> None:
        """
        Calls :py:meth:`EC2.Client.describe_dhcp_options` to update the attributes of
        the DhcpOptions
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.DhcpOptions.load)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#dhcpoptionsload-method)
        """

    async def reload(self) -> None:
        """
        Calls :py:meth:`EC2.Client.describe_dhcp_options` to update the attributes of
        the DhcpOptions
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.DhcpOptions.reload)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#dhcpoptionsreload-method)
        """


_DhcpOptions = DhcpOptions


class Image(AIOBoto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.Image)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#image)
    """

    architecture: Awaitable[ArchitectureValuesType]
    creation_date: Awaitable[str]
    image_id: Awaitable[str]
    image_location: Awaitable[str]
    image_type: Awaitable[ImageTypeValuesType]
    public: Awaitable[bool]
    kernel_id: Awaitable[str]
    owner_id: Awaitable[str]
    platform: Awaitable[Literal["Windows"]]
    platform_details: Awaitable[str]
    usage_operation: Awaitable[str]
    product_codes: Awaitable[List[ProductCodeTypeDef]]
    ramdisk_id: Awaitable[str]
    state: Awaitable[ImageStateType]
    block_device_mappings: Awaitable[List[BlockDeviceMappingTypeDef]]
    description: Awaitable[str]
    ena_support: Awaitable[bool]
    hypervisor: Awaitable[HypervisorTypeType]
    image_owner_alias: Awaitable[str]
    name: Awaitable[str]
    root_device_name: Awaitable[str]
    root_device_type: Awaitable[DeviceTypeType]
    sriov_net_support: Awaitable[str]
    state_reason: Awaitable[StateReasonTypeDef]
    tags: Awaitable[List[TagTypeDef]]
    virtualization_type: Awaitable[VirtualizationTypeType]
    boot_mode: Awaitable[BootModeValuesType]
    tpm_support: Awaitable[Literal["v2.0"]]
    deprecation_time: Awaitable[str]
    imds_support: Awaitable[Literal["v2.0"]]
    source_instance_id: Awaitable[str]
    id: str
    meta: Awaitable["EC2ResourceMeta"]

    async def create_tags(self, *, Tags: Sequence[TagTypeDef], DryRun: bool = ...) -> None:
        """
        Adds or overwrites only the specified tags for the specified Amazon EC2
        resource or
        resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.DhcpOptions.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#dhcpoptionscreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Image.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#imagecreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.InternetGateway.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#internetgatewaycreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.NetworkAcl.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#networkaclcreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.NetworkInterface.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#networkinterfacecreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.RouteTable.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#routetablecreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.SecurityGroup.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#securitygroupcreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Snapshot.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#snapshotcreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Subnet.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#subnetcreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Volume.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#volumecreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Vpc.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#vpccreate_tags-method)
        """

    async def deregister(self, *, DryRun: bool = ...) -> None:
        """
        Deregisters the specified AMI.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Image.deregister)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#imagederegister-method)
        """

    async def describe_attribute(
        self, *, Attribute: ImageAttributeNameType, DryRun: bool = ...
    ) -> ImageAttributeTypeDef:
        """
        Describes the specified attribute of the specified AMI.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Image.describe_attribute)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#imagedescribe_attribute-method)
        """

    async def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Image.get_available_subresources)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#imageget_available_subresources-method)
        """

    async def load(self) -> None:
        """
        Calls :py:meth:`EC2.Client.describe_images` to update the attributes of the
        Image
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Image.load)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#imageload-method)
        """

    async def modify_attribute(
        self,
        *,
        Attribute: str = ...,
        Description: AttributeValueTypeDef = ...,
        LaunchPermission: LaunchPermissionModificationsTypeDef = ...,
        OperationType: OperationTypeType = ...,
        ProductCodes: Sequence[str] = ...,
        UserGroups: Sequence[str] = ...,
        UserIds: Sequence[str] = ...,
        Value: str = ...,
        DryRun: bool = ...,
        OrganizationArns: Sequence[str] = ...,
        OrganizationalUnitArns: Sequence[str] = ...,
        ImdsSupport: AttributeValueTypeDef = ...,
    ) -> None:
        """
        Modifies the specified attribute of the specified AMI.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Image.modify_attribute)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#imagemodify_attribute-method)
        """

    async def reload(self) -> None:
        """
        Calls :py:meth:`EC2.Client.describe_images` to update the attributes of the
        Image
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Image.reload)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#imagereload-method)
        """

    async def reset_attribute(
        self, *, Attribute: Literal["launchPermission"], DryRun: bool = ...
    ) -> None:
        """
        Resets an attribute of an AMI to its default value.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Image.reset_attribute)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#imagereset_attribute-method)
        """

    async def wait_until_exists(self) -> None:
        """
        Waits until this Image is exists.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Image.wait_until_exists)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#imagewait_until_exists-method)
        """


_Image = Image


class InternetGateway(AIOBoto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.InternetGateway)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#internetgateway)
    """

    attachments: Awaitable[List[InternetGatewayAttachmentTypeDef]]
    internet_gateway_id: Awaitable[str]
    owner_id: Awaitable[str]
    tags: Awaitable[List[TagTypeDef]]
    id: str
    meta: Awaitable["EC2ResourceMeta"]

    async def attach_to_vpc(self, *, VpcId: str, DryRun: bool = ...) -> None:
        """
        Attaches an internet gateway or a virtual private gateway to a VPC, enabling
        connectivity between the internet and the
        VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.InternetGateway.attach_to_vpc)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#internetgatewayattach_to_vpc-method)
        """

    async def create_tags(self, *, Tags: Sequence[TagTypeDef], DryRun: bool = ...) -> None:
        """
        Adds or overwrites only the specified tags for the specified Amazon EC2
        resource or
        resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.DhcpOptions.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#dhcpoptionscreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Image.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#imagecreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.InternetGateway.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#internetgatewaycreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.NetworkAcl.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#networkaclcreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.NetworkInterface.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#networkinterfacecreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.RouteTable.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#routetablecreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.SecurityGroup.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#securitygroupcreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Snapshot.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#snapshotcreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Subnet.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#subnetcreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Volume.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#volumecreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Vpc.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#vpccreate_tags-method)
        """

    async def delete(self, *, DryRun: bool = ...) -> None:
        """
        Deletes the specified internet gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.InternetGateway.delete)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#internetgatewaydelete-method)
        """

    async def detach_from_vpc(self, *, VpcId: str, DryRun: bool = ...) -> None:
        """
        Detaches an internet gateway from a VPC, disabling connectivity between the
        internet and the
        VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.InternetGateway.detach_from_vpc)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#internetgatewaydetach_from_vpc-method)
        """

    async def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.InternetGateway.get_available_subresources)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#internetgatewayget_available_subresources-method)
        """

    async def load(self) -> None:
        """
        Calls :py:meth:`EC2.Client.describe_internet_gateways` to update the attributes
        of the InternetGateway
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.InternetGateway.load)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#internetgatewayload-method)
        """

    async def reload(self) -> None:
        """
        Calls :py:meth:`EC2.Client.describe_internet_gateways` to update the attributes
        of the InternetGateway
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.InternetGateway.reload)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#internetgatewayreload-method)
        """


_InternetGateway = InternetGateway


class KeyPair(AIOBoto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.KeyPair)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#keypair)
    """

    key_fingerprint: Awaitable[str]
    key_material: Awaitable[str]
    key_name: Awaitable[str]
    key_pair_id: Awaitable[str]
    tags: Awaitable[List[TagTypeDef]]
    name: str
    meta: Awaitable["EC2ResourceMeta"]

    async def delete(
        self, *, KeyPairId: str = ..., DryRun: bool = ...
    ) -> DeleteKeyPairResultTypeDef:
        """
        Deletes the specified key pair, by removing the public key from Amazon EC2.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.KeyPair.delete)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#keypairdelete-method)
        """

    async def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.KeyPair.get_available_subresources)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#keypairget_available_subresources-method)
        """


_KeyPair = KeyPair


class KeyPairInfo(AIOBoto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.KeyPairInfo)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#keypairinfo)
    """

    key_pair_id: Awaitable[str]
    key_fingerprint: Awaitable[str]
    key_name: Awaitable[str]
    key_type: Awaitable[KeyTypeType]
    tags: Awaitable[List[TagTypeDef]]
    public_key: Awaitable[str]
    create_time: Awaitable[datetime]
    name: str
    meta: Awaitable["EC2ResourceMeta"]

    async def delete(
        self, *, KeyPairId: str = ..., DryRun: bool = ...
    ) -> DeleteKeyPairResultTypeDef:
        """
        Deletes the specified key pair, by removing the public key from Amazon EC2.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.KeyPairInfo.delete)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#keypairinfodelete-method)
        """

    async def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.KeyPairInfo.get_available_subresources)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#keypairinfoget_available_subresources-method)
        """

    async def load(self) -> None:
        """
        Calls :py:meth:`EC2.Client.describe_key_pairs` to update the attributes of the
        KeyPairInfo
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.KeyPairInfo.load)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#keypairinfoload-method)
        """

    async def reload(self) -> None:
        """
        Calls :py:meth:`EC2.Client.describe_key_pairs` to update the attributes of the
        KeyPairInfo
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.KeyPairInfo.reload)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#keypairinforeload-method)
        """


_KeyPairInfo = KeyPairInfo


class NetworkAcl(AIOBoto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.NetworkAcl)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#networkacl)
    """

    associations: Awaitable[List[NetworkAclAssociationTypeDef]]
    entries: Awaitable[List[NetworkAclEntryTypeDef]]
    is_default: Awaitable[bool]
    network_acl_id: Awaitable[str]
    tags: Awaitable[List[TagTypeDef]]
    vpc_id: Awaitable[str]
    owner_id: Awaitable[str]
    id: str
    vpc: "Vpc"
    meta: Awaitable["EC2ResourceMeta"]

    async def create_entry(
        self,
        *,
        Egress: bool,
        Protocol: str,
        RuleAction: RuleActionType,
        RuleNumber: int,
        CidrBlock: str = ...,
        DryRun: bool = ...,
        IcmpTypeCode: IcmpTypeCodeTypeDef = ...,
        Ipv6CidrBlock: str = ...,
        PortRange: PortRangeTypeDef = ...,
    ) -> None:
        """
        Creates an entry (a rule) in a network ACL with the specified rule number.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.NetworkAcl.create_entry)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#networkaclcreate_entry-method)
        """

    async def create_tags(self, *, Tags: Sequence[TagTypeDef], DryRun: bool = ...) -> None:
        """
        Adds or overwrites only the specified tags for the specified Amazon EC2
        resource or
        resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.DhcpOptions.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#dhcpoptionscreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Image.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#imagecreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.InternetGateway.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#internetgatewaycreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.NetworkAcl.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#networkaclcreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.NetworkInterface.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#networkinterfacecreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.RouteTable.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#routetablecreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.SecurityGroup.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#securitygroupcreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Snapshot.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#snapshotcreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Subnet.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#subnetcreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Volume.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#volumecreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Vpc.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#vpccreate_tags-method)
        """

    async def delete(self, *, DryRun: bool = ...) -> None:
        """
        Deletes the specified network ACL.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.NetworkAcl.delete)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#networkacldelete-method)
        """

    async def delete_entry(self, *, Egress: bool, RuleNumber: int, DryRun: bool = ...) -> None:
        """
        Deletes the specified ingress or egress entry (rule) from the specified network
        ACL.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.NetworkAcl.delete_entry)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#networkacldelete_entry-method)
        """

    async def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.NetworkAcl.get_available_subresources)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#networkaclget_available_subresources-method)
        """

    async def load(self) -> None:
        """
        Calls :py:meth:`EC2.Client.describe_network_acls` to update the attributes of
        the NetworkAcl
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.NetworkAcl.load)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#networkaclload-method)
        """

    async def reload(self) -> None:
        """
        Calls :py:meth:`EC2.Client.describe_network_acls` to update the attributes of
        the NetworkAcl
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.NetworkAcl.reload)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#networkaclreload-method)
        """

    async def replace_association(
        self, *, AssociationId: str, DryRun: bool = ...
    ) -> ReplaceNetworkAclAssociationResultTypeDef:
        """
        Changes which network ACL a subnet is associated with.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.NetworkAcl.replace_association)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#networkaclreplace_association-method)
        """

    async def replace_entry(
        self,
        *,
        Egress: bool,
        Protocol: str,
        RuleAction: RuleActionType,
        RuleNumber: int,
        CidrBlock: str = ...,
        DryRun: bool = ...,
        IcmpTypeCode: IcmpTypeCodeTypeDef = ...,
        Ipv6CidrBlock: str = ...,
        PortRange: PortRangeTypeDef = ...,
    ) -> None:
        """
        Replaces an entry (rule) in a network ACL.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.NetworkAcl.replace_entry)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#networkaclreplace_entry-method)
        """


_NetworkAcl = NetworkAcl


class NetworkInterface(AIOBoto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.NetworkInterface)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#networkinterface)
    """

    association_attribute: Awaitable[NetworkInterfaceAssociationResponseTypeDef]
    attachment: Awaitable[NetworkInterfaceAttachmentResponseTypeDef]
    availability_zone: Awaitable[str]
    connection_tracking_configuration: Awaitable[ConnectionTrackingConfigurationResponseTypeDef]
    description: Awaitable[str]
    groups: Awaitable[List[GroupIdentifierTypeDef]]
    interface_type: Awaitable[NetworkInterfaceTypeType]
    ipv6_addresses: Awaitable[List[NetworkInterfaceIpv6AddressTypeDef]]
    mac_address: Awaitable[str]
    network_interface_id: Awaitable[str]
    outpost_arn: Awaitable[str]
    owner_id: Awaitable[str]
    private_dns_name: Awaitable[str]
    private_ip_address: Awaitable[str]
    private_ip_addresses: Awaitable[List[NetworkInterfacePrivateIpAddressTypeDef]]
    ipv4_prefixes: Awaitable[List[Ipv4PrefixSpecificationTypeDef]]
    ipv6_prefixes: Awaitable[List[Ipv6PrefixSpecificationTypeDef]]
    requester_id: Awaitable[str]
    requester_managed: Awaitable[bool]
    source_dest_check: Awaitable[bool]
    status: Awaitable[NetworkInterfaceStatusType]
    subnet_id: Awaitable[str]
    tag_set: Awaitable[List[TagTypeDef]]
    vpc_id: Awaitable[str]
    deny_all_igw_traffic: Awaitable[bool]
    ipv6_native: Awaitable[bool]
    ipv6_address: Awaitable[str]
    id: str
    association: "NetworkInterfaceAssociation"
    subnet: "Subnet"
    vpc: "Vpc"
    meta: Awaitable["EC2ResourceMeta"]

    async def assign_private_ip_addresses(
        self,
        *,
        AllowReassignment: bool = ...,
        PrivateIpAddresses: Sequence[str] = ...,
        SecondaryPrivateIpAddressCount: int = ...,
        Ipv4Prefixes: Sequence[str] = ...,
        Ipv4PrefixCount: int = ...,
    ) -> AssignPrivateIpAddressesResultTypeDef:
        """
        Assigns one or more secondary private IP addresses to the specified network
        interface.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.NetworkInterface.assign_private_ip_addresses)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#networkinterfaceassign_private_ip_addresses-method)
        """

    async def attach(
        self,
        *,
        DeviceIndex: int,
        InstanceId: str,
        DryRun: bool = ...,
        NetworkCardIndex: int = ...,
        EnaSrdSpecification: EnaSrdSpecificationTypeDef = ...,
    ) -> AttachNetworkInterfaceResultTypeDef:
        """
        Attaches a network interface to an instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.NetworkInterface.attach)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#networkinterfaceattach-method)
        """

    async def create_tags(self, *, Tags: Sequence[TagTypeDef], DryRun: bool = ...) -> None:
        """
        Adds or overwrites only the specified tags for the specified Amazon EC2
        resource or
        resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.DhcpOptions.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#dhcpoptionscreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Image.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#imagecreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.InternetGateway.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#internetgatewaycreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.NetworkAcl.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#networkaclcreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.NetworkInterface.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#networkinterfacecreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.RouteTable.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#routetablecreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.SecurityGroup.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#securitygroupcreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Snapshot.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#snapshotcreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Subnet.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#subnetcreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Volume.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#volumecreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Vpc.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#vpccreate_tags-method)
        """

    async def delete(self, *, DryRun: bool = ...) -> None:
        """
        Deletes the specified network interface.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.NetworkInterface.delete)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#networkinterfacedelete-method)
        """

    async def describe_attribute(
        self, *, Attribute: NetworkInterfaceAttributeType = ..., DryRun: bool = ...
    ) -> DescribeNetworkInterfaceAttributeResultTypeDef:
        """
        Describes a network interface attribute.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.NetworkInterface.describe_attribute)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#networkinterfacedescribe_attribute-method)
        """

    async def detach(self, *, AttachmentId: str, DryRun: bool = ..., Force: bool = ...) -> None:
        """
        Detaches a network interface from an instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.NetworkInterface.detach)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#networkinterfacedetach-method)
        """

    async def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.NetworkInterface.get_available_subresources)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#networkinterfaceget_available_subresources-method)
        """

    async def load(self) -> None:
        """
        Calls :py:meth:`EC2.Client.describe_network_interfaces` to update the
        attributes of the NetworkInterface
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.NetworkInterface.load)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#networkinterfaceload-method)
        """

    async def modify_attribute(
        self,
        *,
        Attachment: NetworkInterfaceAttachmentChangesTypeDef = ...,
        Description: AttributeValueTypeDef = ...,
        DryRun: bool = ...,
        Groups: Sequence[str] = ...,
        SourceDestCheck: AttributeBooleanValueTypeDef = ...,
        EnaSrdSpecification: EnaSrdSpecificationTypeDef = ...,
        EnablePrimaryIpv6: bool = ...,
        ConnectionTrackingSpecification: ConnectionTrackingSpecificationRequestTypeDef = ...,
    ) -> None:
        """
        Modifies the specified network interface attribute.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.NetworkInterface.modify_attribute)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#networkinterfacemodify_attribute-method)
        """

    async def reload(self) -> None:
        """
        Calls :py:meth:`EC2.Client.describe_network_interfaces` to update the
        attributes of the NetworkInterface
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.NetworkInterface.reload)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#networkinterfacereload-method)
        """

    async def reset_attribute(self, *, DryRun: bool = ..., SourceDestCheck: str = ...) -> None:
        """
        Resets a network interface attribute.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.NetworkInterface.reset_attribute)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#networkinterfacereset_attribute-method)
        """

    async def unassign_private_ip_addresses(
        self, *, PrivateIpAddresses: Sequence[str] = ..., Ipv4Prefixes: Sequence[str] = ...
    ) -> None:
        """
        Unassigns one or more secondary private IP addresses, or IPv4 Prefix Delegation
        prefixes from a network
        interface.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.NetworkInterface.unassign_private_ip_addresses)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#networkinterfaceunassign_private_ip_addresses-method)
        """


_NetworkInterface = NetworkInterface


class NetworkInterfaceAssociation(AIOBoto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.NetworkInterfaceAssociation)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#networkinterfaceassociation)
    """

    carrier_ip: Awaitable[str]
    customer_owned_ip: Awaitable[str]
    ip_owner_id: Awaitable[str]
    public_dns_name: Awaitable[str]
    public_ip: Awaitable[str]
    id: str
    address: "VpcAddress"
    meta: Awaitable["EC2ResourceMeta"]

    async def delete(self, *, PublicIp: str = ..., DryRun: bool = ...) -> None:
        """
        Disassociates an Elastic IP address from the instance or network interface it's
        associated
        with.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.NetworkInterfaceAssociation.delete)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#networkinterfaceassociationdelete-method)
        """

    async def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.NetworkInterfaceAssociation.get_available_subresources)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#networkinterfaceassociationget_available_subresources-method)
        """

    async def load(self) -> None:
        """
        Calls :py:meth:`EC2.Client.describe_network_interfaces` to update the
        attributes of the NetworkInterfaceAssociation
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.NetworkInterfaceAssociation.load)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#networkinterfaceassociationload-method)
        """

    async def reload(self) -> None:
        """
        Calls :py:meth:`EC2.Client.describe_network_interfaces` to update the
        attributes of the NetworkInterfaceAssociation
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.NetworkInterfaceAssociation.reload)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#networkinterfaceassociationreload-method)
        """


_NetworkInterfaceAssociation = NetworkInterfaceAssociation


class PlacementGroup(AIOBoto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.PlacementGroup)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#placementgroup)
    """

    group_name: Awaitable[str]
    state: Awaitable[PlacementGroupStateType]
    strategy: Awaitable[PlacementStrategyType]
    partition_count: Awaitable[int]
    group_id: Awaitable[str]
    tags: Awaitable[List[TagTypeDef]]
    group_arn: Awaitable[str]
    spread_level: Awaitable[SpreadLevelType]
    name: str
    instances: PlacementGroupInstancesCollection
    meta: Awaitable["EC2ResourceMeta"]

    async def delete(self, *, DryRun: bool = ...) -> None:
        """
        Deletes the specified placement group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.PlacementGroup.delete)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#placementgroupdelete-method)
        """

    async def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.PlacementGroup.get_available_subresources)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#placementgroupget_available_subresources-method)
        """

    async def load(self) -> None:
        """
        Calls :py:meth:`EC2.Client.describe_placement_groups` to update the attributes
        of the PlacementGroup
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.PlacementGroup.load)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#placementgroupload-method)
        """

    async def reload(self) -> None:
        """
        Calls :py:meth:`EC2.Client.describe_placement_groups` to update the attributes
        of the PlacementGroup
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.PlacementGroup.reload)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#placementgroupreload-method)
        """


_PlacementGroup = PlacementGroup


class SecurityGroup(AIOBoto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.SecurityGroup)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#securitygroup)
    """

    description: Awaitable[str]
    group_name: Awaitable[str]
    ip_permissions: Awaitable[List[IpPermissionTypeDef]]
    owner_id: Awaitable[str]
    group_id: Awaitable[str]
    ip_permissions_egress: Awaitable[List[IpPermissionTypeDef]]
    tags: Awaitable[List[TagTypeDef]]
    vpc_id: Awaitable[str]
    id: str
    meta: Awaitable["EC2ResourceMeta"]

    async def authorize_egress(
        self,
        *,
        DryRun: bool = ...,
        IpPermissions: Sequence[IpPermissionTypeDef] = ...,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...,
        CidrIp: str = ...,
        FromPort: int = ...,
        IpProtocol: str = ...,
        ToPort: int = ...,
        SourceSecurityGroupName: str = ...,
        SourceSecurityGroupOwnerId: str = ...,
    ) -> AuthorizeSecurityGroupEgressResultTypeDef:
        """
        Adds the specified outbound (egress) rules to a security group for use with a
        VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.SecurityGroup.authorize_egress)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#securitygroupauthorize_egress-method)
        """

    async def authorize_ingress(
        self,
        *,
        CidrIp: str = ...,
        FromPort: int = ...,
        GroupName: str = ...,
        IpPermissions: Sequence[IpPermissionTypeDef] = ...,
        IpProtocol: str = ...,
        SourceSecurityGroupName: str = ...,
        SourceSecurityGroupOwnerId: str = ...,
        ToPort: int = ...,
        DryRun: bool = ...,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...,
    ) -> AuthorizeSecurityGroupIngressResultTypeDef:
        """
        Adds the specified inbound (ingress) rules to a security group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.SecurityGroup.authorize_ingress)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#securitygroupauthorize_ingress-method)
        """

    async def create_tags(self, *, Tags: Sequence[TagTypeDef], DryRun: bool = ...) -> None:
        """
        Adds or overwrites only the specified tags for the specified Amazon EC2
        resource or
        resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.DhcpOptions.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#dhcpoptionscreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Image.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#imagecreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.InternetGateway.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#internetgatewaycreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.NetworkAcl.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#networkaclcreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.NetworkInterface.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#networkinterfacecreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.RouteTable.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#routetablecreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.SecurityGroup.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#securitygroupcreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Snapshot.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#snapshotcreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Subnet.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#subnetcreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Volume.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#volumecreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Vpc.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#vpccreate_tags-method)
        """

    async def delete(self, *, GroupName: str = ..., DryRun: bool = ...) -> None:
        """
        Deletes a security group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.SecurityGroup.delete)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#securitygroupdelete-method)
        """

    async def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.SecurityGroup.get_available_subresources)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#securitygroupget_available_subresources-method)
        """

    async def load(self) -> None:
        """
        Calls :py:meth:`EC2.Client.describe_security_groups` to update the attributes
        of the SecurityGroup
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.SecurityGroup.load)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#securitygroupload-method)
        """

    async def reload(self) -> None:
        """
        Calls :py:meth:`EC2.Client.describe_security_groups` to update the attributes
        of the SecurityGroup
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.SecurityGroup.reload)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#securitygroupreload-method)
        """

    async def revoke_egress(
        self,
        *,
        DryRun: bool = ...,
        IpPermissions: Sequence[IpPermissionTypeDef] = ...,
        SecurityGroupRuleIds: Sequence[str] = ...,
        CidrIp: str = ...,
        FromPort: int = ...,
        IpProtocol: str = ...,
        ToPort: int = ...,
        SourceSecurityGroupName: str = ...,
        SourceSecurityGroupOwnerId: str = ...,
    ) -> RevokeSecurityGroupEgressResultTypeDef:
        """
        Removes the specified outbound (egress) rules from the specified security group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.SecurityGroup.revoke_egress)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#securitygrouprevoke_egress-method)
        """

    async def revoke_ingress(
        self,
        *,
        CidrIp: str = ...,
        FromPort: int = ...,
        GroupName: str = ...,
        IpPermissions: Sequence[IpPermissionTypeDef] = ...,
        IpProtocol: str = ...,
        SourceSecurityGroupName: str = ...,
        SourceSecurityGroupOwnerId: str = ...,
        ToPort: int = ...,
        DryRun: bool = ...,
        SecurityGroupRuleIds: Sequence[str] = ...,
    ) -> RevokeSecurityGroupIngressResultTypeDef:
        """
        Removes the specified inbound (ingress) rules from a security group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.SecurityGroup.revoke_ingress)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#securitygrouprevoke_ingress-method)
        """


_SecurityGroup = SecurityGroup


class Snapshot(AIOBoto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.Snapshot)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#snapshot)
    """

    data_encryption_key_id: Awaitable[str]
    description: Awaitable[str]
    encrypted: Awaitable[bool]
    kms_key_id: Awaitable[str]
    owner_id: Awaitable[str]
    progress: Awaitable[str]
    snapshot_id: Awaitable[str]
    start_time: Awaitable[datetime]
    state: Awaitable[SnapshotStateType]
    state_message: Awaitable[str]
    volume_id: Awaitable[str]
    volume_size: Awaitable[int]
    owner_alias: Awaitable[str]
    outpost_arn: Awaitable[str]
    tags: Awaitable[List[TagTypeDef]]
    storage_tier: Awaitable[StorageTierType]
    restore_expiry_time: Awaitable[datetime]
    sse_type: Awaitable[SSETypeType]
    id: str
    volume: "Volume"
    meta: Awaitable["EC2ResourceMeta"]

    async def copy(
        self,
        *,
        SourceRegion: str,
        Description: str = ...,
        DestinationOutpostArn: str = ...,
        DestinationRegion: str = ...,
        Encrypted: bool = ...,
        KmsKeyId: str = ...,
        PresignedUrl: str = ...,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...,
        DryRun: bool = ...,
    ) -> CopySnapshotResultTypeDef:
        """
        Copies a point-in-time snapshot of an EBS volume and stores it in Amazon S3.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Snapshot.copy)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#snapshotcopy-method)
        """

    async def create_tags(self, *, Tags: Sequence[TagTypeDef], DryRun: bool = ...) -> None:
        """
        Adds or overwrites only the specified tags for the specified Amazon EC2
        resource or
        resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.DhcpOptions.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#dhcpoptionscreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Image.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#imagecreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.InternetGateway.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#internetgatewaycreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.NetworkAcl.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#networkaclcreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.NetworkInterface.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#networkinterfacecreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.RouteTable.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#routetablecreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.SecurityGroup.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#securitygroupcreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Snapshot.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#snapshotcreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Subnet.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#subnetcreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Volume.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#volumecreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Vpc.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#vpccreate_tags-method)
        """

    async def delete(self, *, DryRun: bool = ...) -> None:
        """
        Deletes the specified snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Snapshot.delete)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#snapshotdelete-method)
        """

    async def describe_attribute(
        self, *, Attribute: SnapshotAttributeNameType, DryRun: bool = ...
    ) -> DescribeSnapshotAttributeResultTypeDef:
        """
        Describes the specified attribute of the specified snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Snapshot.describe_attribute)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#snapshotdescribe_attribute-method)
        """

    async def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Snapshot.get_available_subresources)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#snapshotget_available_subresources-method)
        """

    async def load(self) -> None:
        """
        Calls :py:meth:`EC2.Client.describe_snapshots` to update the attributes of the
        Snapshot
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Snapshot.load)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#snapshotload-method)
        """

    async def modify_attribute(
        self,
        *,
        Attribute: SnapshotAttributeNameType = ...,
        CreateVolumePermission: CreateVolumePermissionModificationsTypeDef = ...,
        GroupNames: Sequence[str] = ...,
        OperationType: OperationTypeType = ...,
        UserIds: Sequence[str] = ...,
        DryRun: bool = ...,
    ) -> None:
        """
        Adds or removes permission settings for the specified snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Snapshot.modify_attribute)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#snapshotmodify_attribute-method)
        """

    async def reload(self) -> None:
        """
        Calls :py:meth:`EC2.Client.describe_snapshots` to update the attributes of the
        Snapshot
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Snapshot.reload)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#snapshotreload-method)
        """

    async def reset_attribute(
        self, *, Attribute: SnapshotAttributeNameType, DryRun: bool = ...
    ) -> None:
        """
        Resets permission settings for the specified snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Snapshot.reset_attribute)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#snapshotreset_attribute-method)
        """

    async def wait_until_completed(self) -> None:
        """
        Waits until this Snapshot is completed.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Snapshot.wait_until_completed)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#snapshotwait_until_completed-method)
        """


_Snapshot = Snapshot


class Tag(AIOBoto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.Tag)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#tag)
    """

    resource_type: Awaitable[ResourceTypeType]
    resource_id: str
    key: str
    value: str
    meta: Awaitable["EC2ResourceMeta"]

    async def delete(self, *, DryRun: bool = ...) -> None:
        """
        Deletes the specified set of tags from the specified set of resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Tag.delete)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#tagdelete-method)
        """

    async def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Tag.get_available_subresources)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#tagget_available_subresources-method)
        """

    async def load(self) -> None:
        """
        Calls :py:meth:`EC2.Client.describe_tags` to update the attributes of the Tag
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Tag.load)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#tagload-method)
        """

    async def reload(self) -> None:
        """
        Calls :py:meth:`EC2.Client.describe_tags` to update the attributes of the Tag
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Tag.reload)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#tagreload-method)
        """


_Tag = Tag


class VpcPeeringConnection(AIOBoto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.VpcPeeringConnection)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#vpcpeeringconnection)
    """

    accepter_vpc_info: Awaitable[VpcPeeringConnectionVpcInfoResponseTypeDef]
    expiration_time: Awaitable[datetime]
    requester_vpc_info: Awaitable[VpcPeeringConnectionVpcInfoResponseTypeDef]
    status: Awaitable[VpcPeeringConnectionStateReasonResponseTypeDef]
    tags: Awaitable[List[TagTypeDef]]
    vpc_peering_connection_id: Awaitable[str]
    id: str
    accepter_vpc: "Vpc"
    requester_vpc: "Vpc"
    meta: Awaitable["EC2ResourceMeta"]

    async def accept(self, *, DryRun: bool = ...) -> AcceptVpcPeeringConnectionResultTypeDef:
        """
        Accept a VPC peering connection request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.VpcPeeringConnection.accept)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#vpcpeeringconnectionaccept-method)
        """

    async def delete(self, *, DryRun: bool = ...) -> DeleteVpcPeeringConnectionResultTypeDef:
        """
        Deletes a VPC peering connection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.VpcPeeringConnection.delete)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#vpcpeeringconnectiondelete-method)
        """

    async def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.VpcPeeringConnection.get_available_subresources)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#vpcpeeringconnectionget_available_subresources-method)
        """

    async def load(self) -> None:
        """
        Calls :py:meth:`EC2.Client.describe_vpc_peering_connections` to update the
        attributes of the VpcPeeringConnection
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.VpcPeeringConnection.load)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#vpcpeeringconnectionload-method)
        """

    async def reject(self, *, DryRun: bool = ...) -> RejectVpcPeeringConnectionResultTypeDef:
        """
        Rejects a VPC peering connection request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.VpcPeeringConnection.reject)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#vpcpeeringconnectionreject-method)
        """

    async def reload(self) -> None:
        """
        Calls :py:meth:`EC2.Client.describe_vpc_peering_connections` to update the
        attributes of the VpcPeeringConnection
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.VpcPeeringConnection.reload)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#vpcpeeringconnectionreload-method)
        """

    async def wait_until_exists(self) -> None:
        """
        Waits until this VpcPeeringConnection is exists.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.VpcPeeringConnection.wait_until_exists)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#vpcpeeringconnectionwait_until_exists-method)
        """


_VpcPeeringConnection = VpcPeeringConnection


class VpcAddress(AIOBoto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.VpcAddress)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#vpcaddress)
    """

    instance_id: Awaitable[str]
    public_ip: Awaitable[str]
    association_id: Awaitable[str]
    domain: Awaitable[DomainTypeType]
    network_interface_id: Awaitable[str]
    network_interface_owner_id: Awaitable[str]
    private_ip_address: Awaitable[str]
    tags: Awaitable[List[TagTypeDef]]
    public_ipv4_pool: Awaitable[str]
    network_border_group: Awaitable[str]
    customer_owned_ip: Awaitable[str]
    customer_owned_ipv4_pool: Awaitable[str]
    carrier_ip: Awaitable[str]
    allocation_id: str
    association: "NetworkInterfaceAssociation"
    meta: Awaitable["EC2ResourceMeta"]

    async def associate(
        self,
        *,
        InstanceId: str = ...,
        PublicIp: str = ...,
        AllowReassociation: bool = ...,
        DryRun: bool = ...,
        NetworkInterfaceId: str = ...,
        PrivateIpAddress: str = ...,
    ) -> AssociateAddressResultTypeDef:
        """
        Associates an Elastic IP address, or carrier IP address (for instances that are
        in subnets in Wavelength Zones) with an instance or a network
        interface.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.VpcAddress.associate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#vpcaddressassociate-method)
        """

    async def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.VpcAddress.get_available_subresources)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#vpcaddressget_available_subresources-method)
        """

    async def load(self) -> None:
        """
        Calls :py:meth:`EC2.Client.describe_addresses` to update the attributes of the
        VpcAddress
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.VpcAddress.load)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#vpcaddressload-method)
        """

    async def release(
        self,
        *,
        AllocationId: str = ...,
        PublicIp: str = ...,
        NetworkBorderGroup: str = ...,
        DryRun: bool = ...,
    ) -> None:
        """
        Releases the specified Elastic IP address.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.VpcAddress.release)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#vpcaddressrelease-method)
        """

    async def reload(self) -> None:
        """
        Calls :py:meth:`EC2.Client.describe_addresses` to update the attributes of the
        VpcAddress
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.VpcAddress.reload)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#vpcaddressreload-method)
        """


_VpcAddress = VpcAddress


class Instance(AIOBoto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.Instance)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#instance)
    """

    ami_launch_index: Awaitable[int]
    image_id: Awaitable[str]
    instance_id: Awaitable[str]
    instance_type: Awaitable[InstanceTypeType]
    kernel_id: Awaitable[str]
    key_name: Awaitable[str]
    launch_time: Awaitable[datetime]
    monitoring: Awaitable[MonitoringResponseTypeDef]
    placement: Awaitable[PlacementExtraResponseTypeDef]
    platform: Awaitable[Literal["Windows"]]
    private_dns_name: Awaitable[str]
    private_ip_address: Awaitable[str]
    product_codes: Awaitable[List[ProductCodeTypeDef]]
    public_dns_name: Awaitable[str]
    public_ip_address: Awaitable[str]
    ramdisk_id: Awaitable[str]
    state: Awaitable[InstanceStateResponseTypeDef]
    state_transition_reason: Awaitable[str]
    subnet_id: Awaitable[str]
    vpc_id: Awaitable[str]
    architecture: Awaitable[ArchitectureValuesType]
    block_device_mappings: Awaitable[List[InstanceBlockDeviceMappingTypeDef]]
    client_token: Awaitable[str]
    ebs_optimized: Awaitable[bool]
    ena_support: Awaitable[bool]
    hypervisor: Awaitable[HypervisorTypeType]
    iam_instance_profile: Awaitable[IamInstanceProfileResponseTypeDef]
    instance_lifecycle: Awaitable[InstanceLifecycleTypeType]
    elastic_gpu_associations: Awaitable[List[ElasticGpuAssociationTypeDef]]
    elastic_inference_accelerator_associations: Awaitable[
        List[ElasticInferenceAcceleratorAssociationTypeDef]
    ]
    network_interfaces_attribute: Awaitable[List[InstanceNetworkInterfaceTypeDef]]
    outpost_arn: Awaitable[str]
    root_device_name: Awaitable[str]
    root_device_type: Awaitable[DeviceTypeType]
    security_groups: Awaitable[List[GroupIdentifierTypeDef]]
    source_dest_check: Awaitable[bool]
    spot_instance_request_id: Awaitable[str]
    sriov_net_support: Awaitable[str]
    state_reason: Awaitable[StateReasonResponseTypeDef]
    tags: Awaitable[List[TagTypeDef]]
    virtualization_type: Awaitable[VirtualizationTypeType]
    cpu_options: Awaitable[CpuOptionsResponseTypeDef]
    capacity_reservation_id: Awaitable[str]
    capacity_reservation_specification: Awaitable[
        CapacityReservationSpecificationResponseResponseTypeDef
    ]
    hibernation_options: Awaitable[HibernationOptionsResponseTypeDef]
    licenses: Awaitable[List[LicenseConfigurationTypeDef]]
    metadata_options: Awaitable[InstanceMetadataOptionsResponseResponseTypeDef]
    enclave_options: Awaitable[EnclaveOptionsResponseTypeDef]
    boot_mode: Awaitable[BootModeValuesType]
    platform_details: Awaitable[str]
    usage_operation: Awaitable[str]
    usage_operation_update_time: Awaitable[datetime]
    private_dns_name_options: Awaitable[PrivateDnsNameOptionsResponseResponseTypeDef]
    ipv6_address: Awaitable[str]
    tpm_support: Awaitable[str]
    maintenance_options: Awaitable[InstanceMaintenanceOptionsResponseTypeDef]
    current_instance_boot_mode: Awaitable[InstanceBootModeValuesType]
    id: str
    classic_address: "ClassicAddress"
    image: "Image"
    key_pair: "KeyPairInfo"
    network_interfaces: List["NetworkInterface"]
    placement_group: "PlacementGroup"
    subnet: "Subnet"
    vpc: "Vpc"
    volumes: InstanceVolumesCollection
    vpc_addresses: InstanceVpcAddressesCollection
    meta: Awaitable["EC2ResourceMeta"]

    async def attach_classic_link_vpc(
        self, *, Groups: Sequence[str], VpcId: str, DryRun: bool = ...
    ) -> AttachClassicLinkVpcResultTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Instance.attach_classic_link_vpc)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#instanceattach_classic_link_vpc-method)
        """

    async def attach_volume(
        self, *, Device: str, VolumeId: str, DryRun: bool = ...
    ) -> VolumeAttachmentTypeDef:
        """
        Attaches an EBS volume to a running or stopped instance and exposes it to the
        instance with the specified device
        name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Instance.attach_volume)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#instanceattach_volume-method)
        """

    async def console_output(
        self, *, DryRun: bool = ..., Latest: bool = ...
    ) -> GetConsoleOutputResultTypeDef:
        """
        Gets the console output for the specified instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Instance.console_output)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#instanceconsole_output-method)
        """

    async def create_image(
        self,
        *,
        Name: str,
        BlockDeviceMappings: Sequence[BlockDeviceMappingTypeDef] = ...,
        Description: str = ...,
        DryRun: bool = ...,
        NoReboot: bool = ...,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...,
    ) -> "_Image":
        """
        Creates an Amazon EBS-backed AMI from an Amazon EBS-backed instance that is
        either running or
        stopped.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Instance.create_image)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#instancecreate_image-method)
        """

    async def create_tags(self, *, Tags: Sequence[TagTypeDef], DryRun: bool = ...) -> None:
        """
        Adds or overwrites only the specified tags for the specified Amazon EC2
        resource or
        resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Instance.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#instancecreate_tags-method)
        """

    async def delete_tags(self, *, Tags: Sequence[TagTypeDef] = ..., DryRun: bool = ...) -> None:
        """
        Deletes the specified set of tags from the specified set of resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Instance.delete_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#instancedelete_tags-method)
        """

    async def describe_attribute(
        self, *, Attribute: InstanceAttributeNameType, DryRun: bool = ...
    ) -> InstanceAttributeTypeDef:
        """
        Describes the specified attribute of the specified instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Instance.describe_attribute)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#instancedescribe_attribute-method)
        """

    async def detach_classic_link_vpc(
        self, *, VpcId: str, DryRun: bool = ...
    ) -> DetachClassicLinkVpcResultTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Instance.detach_classic_link_vpc)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#instancedetach_classic_link_vpc-method)
        """

    async def detach_volume(
        self, *, VolumeId: str, Device: str = ..., Force: bool = ..., DryRun: bool = ...
    ) -> VolumeAttachmentTypeDef:
        """
        Detaches an EBS volume from an instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Instance.detach_volume)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#instancedetach_volume-method)
        """

    async def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Instance.get_available_subresources)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#instanceget_available_subresources-method)
        """

    async def load(self) -> None:
        """
        Calls :py:meth:`EC2.Client.describe_instances` to update the attributes of the
        Instance
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Instance.load)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#instanceload-method)
        """

    async def modify_attribute(
        self,
        *,
        SourceDestCheck: AttributeBooleanValueTypeDef = ...,
        Attribute: InstanceAttributeNameType = ...,
        BlockDeviceMappings: Sequence[InstanceBlockDeviceMappingSpecificationTypeDef] = ...,
        DisableApiTermination: AttributeBooleanValueTypeDef = ...,
        DryRun: bool = ...,
        EbsOptimized: AttributeBooleanValueTypeDef = ...,
        EnaSupport: AttributeBooleanValueTypeDef = ...,
        Groups: Sequence[str] = ...,
        InstanceInitiatedShutdownBehavior: AttributeValueTypeDef = ...,
        InstanceType: AttributeValueTypeDef = ...,
        Kernel: AttributeValueTypeDef = ...,
        Ramdisk: AttributeValueTypeDef = ...,
        SriovNetSupport: AttributeValueTypeDef = ...,
        UserData: BlobAttributeValueTypeDef = ...,
        Value: str = ...,
        DisableApiStop: AttributeBooleanValueTypeDef = ...,
    ) -> None:
        """
        Modifies the specified attribute of the specified instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Instance.modify_attribute)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#instancemodify_attribute-method)
        """

    async def monitor(self, *, DryRun: bool = ...) -> MonitorInstancesResultTypeDef:
        """
        Enables detailed monitoring for a running instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Instance.monitor)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#instancemonitor-method)
        """

    async def password_data(self, *, DryRun: bool = ...) -> GetPasswordDataResultTypeDef:
        """
        Retrieves the encrypted administrator password for a running Windows instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Instance.password_data)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#instancepassword_data-method)
        """

    async def reboot(self, *, DryRun: bool = ...) -> None:
        """
        Requests a reboot of the specified instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Instance.reboot)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#instancereboot-method)
        """

    async def reload(self) -> None:
        """
        Calls :py:meth:`EC2.Client.describe_instances` to update the attributes of the
        Instance
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Instance.reload)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#instancereload-method)
        """

    async def report_status(
        self,
        *,
        ReasonCodes: Sequence[ReportInstanceReasonCodesType],
        Status: ReportStatusTypeType,
        Description: str = ...,
        DryRun: bool = ...,
        EndTime: TimestampTypeDef = ...,
        StartTime: TimestampTypeDef = ...,
    ) -> None:
        """
        Submits feedback about the status of an instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Instance.report_status)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#instancereport_status-method)
        """

    async def reset_attribute(
        self, *, Attribute: InstanceAttributeNameType, DryRun: bool = ...
    ) -> None:
        """
        Resets an attribute of an instance to its default value.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Instance.reset_attribute)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#instancereset_attribute-method)
        """

    async def reset_kernel(
        self, *, Attribute: InstanceAttributeNameType = "kernel", DryRun: bool = ...
    ) -> None:
        """
        Resets an attribute of an instance to its default value.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Instance.reset_kernel)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#instancereset_kernel-method)
        """

    async def reset_ramdisk(
        self, *, Attribute: InstanceAttributeNameType = "ramdisk", DryRun: bool = ...
    ) -> None:
        """
        Resets an attribute of an instance to its default value.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Instance.reset_ramdisk)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#instancereset_ramdisk-method)
        """

    async def reset_source_dest_check(
        self, *, Attribute: InstanceAttributeNameType = "sourceDestCheck", DryRun: bool = ...
    ) -> None:
        """
        Resets an attribute of an instance to its default value.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Instance.reset_source_dest_check)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#instancereset_source_dest_check-method)
        """

    async def start(
        self, *, AdditionalInfo: str = ..., DryRun: bool = ...
    ) -> StartInstancesResultTypeDef:
        """
        Starts an Amazon EBS-backed instance that you've previously stopped.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Instance.start)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#instancestart-method)
        """

    async def stop(
        self, *, Hibernate: bool = ..., DryRun: bool = ..., Force: bool = ...
    ) -> StopInstancesResultTypeDef:
        """
        Stops an Amazon EBS-backed instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Instance.stop)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#instancestop-method)
        """

    async def terminate(self, *, DryRun: bool = ...) -> TerminateInstancesResultTypeDef:
        """
        Shuts down the specified instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Instance.terminate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#instanceterminate-method)
        """

    async def unmonitor(self, *, DryRun: bool = ...) -> UnmonitorInstancesResultTypeDef:
        """
        Disables detailed monitoring for a running instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Instance.unmonitor)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#instanceunmonitor-method)
        """

    async def wait_until_exists(self) -> None:
        """
        Waits until this Instance is exists.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Instance.wait_until_exists)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#instancewait_until_exists-method)
        """

    async def wait_until_running(self) -> None:
        """
        Waits until this Instance is running.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Instance.wait_until_running)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#instancewait_until_running-method)
        """

    async def wait_until_stopped(self) -> None:
        """
        Waits until this Instance is stopped.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Instance.wait_until_stopped)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#instancewait_until_stopped-method)
        """

    async def wait_until_terminated(self) -> None:
        """
        Waits until this Instance is terminated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Instance.wait_until_terminated)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#instancewait_until_terminated-method)
        """


_Instance = Instance


class Route(AIOBoto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.Route)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#route)
    """

    destination_ipv6_cidr_block: Awaitable[str]
    destination_prefix_list_id: Awaitable[str]
    egress_only_internet_gateway_id: Awaitable[str]
    gateway_id: Awaitable[str]
    instance_id: Awaitable[str]
    instance_owner_id: Awaitable[str]
    nat_gateway_id: Awaitable[str]
    transit_gateway_id: Awaitable[str]
    local_gateway_id: Awaitable[str]
    carrier_gateway_id: Awaitable[str]
    network_interface_id: Awaitable[str]
    origin: Awaitable[RouteOriginType]
    state: Awaitable[RouteStateType]
    vpc_peering_connection_id: Awaitable[str]
    core_network_arn: Awaitable[str]
    route_table_id: str
    destination_cidr_block: str
    meta: Awaitable["EC2ResourceMeta"]

    async def RouteTable(self) -> "_RouteTable":
        """
        Creates a RouteTable resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Route.RouteTable)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#routeroutetable-method)
        """

    async def delete(
        self,
        *,
        DestinationIpv6CidrBlock: str = ...,
        DestinationPrefixListId: str = ...,
        DryRun: bool = ...,
    ) -> None:
        """
        Deletes the specified route from the specified route table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Route.delete)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#routedelete-method)
        """

    async def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Route.get_available_subresources)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#routeget_available_subresources-method)
        """

    async def replace(
        self,
        *,
        DestinationIpv6CidrBlock: str = ...,
        DestinationPrefixListId: str = ...,
        DryRun: bool = ...,
        VpcEndpointId: str = ...,
        EgressOnlyInternetGatewayId: str = ...,
        GatewayId: str = ...,
        InstanceId: str = ...,
        LocalTarget: bool = ...,
        NatGatewayId: str = ...,
        TransitGatewayId: str = ...,
        LocalGatewayId: str = ...,
        CarrierGatewayId: str = ...,
        NetworkInterfaceId: str = ...,
        VpcPeeringConnectionId: str = ...,
        CoreNetworkArn: str = ...,
    ) -> None:
        """
        Replaces an existing route within a route table in a VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Route.replace)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#routereplace-method)
        """


_Route = Route


class RouteTableAssociation(AIOBoto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.RouteTableAssociation)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#routetableassociation)
    """

    main: Awaitable[bool]
    route_table_association_id: Awaitable[str]
    route_table_id: Awaitable[str]
    subnet_id: Awaitable[str]
    gateway_id: Awaitable[str]
    association_state: Awaitable[RouteTableAssociationStateResponseTypeDef]
    id: str
    route_table: "RouteTable"
    subnet: "Subnet"
    meta: Awaitable["EC2ResourceMeta"]

    async def delete(self, *, DryRun: bool = ...) -> None:
        """
        Disassociates a subnet or gateway from a route table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.RouteTableAssociation.delete)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#routetableassociationdelete-method)
        """

    async def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.RouteTableAssociation.get_available_subresources)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#routetableassociationget_available_subresources-method)
        """

    async def replace_subnet(
        self, *, RouteTableId: str, DryRun: bool = ...
    ) -> "_RouteTableAssociation":
        """
        Changes the route table associated with a given subnet, internet gateway, or
        virtual private gateway in a
        VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.RouteTableAssociation.replace_subnet)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#routetableassociationreplace_subnet-method)
        """


_RouteTableAssociation = RouteTableAssociation


class Volume(AIOBoto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.Volume)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#volume)
    """

    attachments: Awaitable[List[VolumeAttachmentTypeDef]]
    availability_zone: Awaitable[str]
    create_time: Awaitable[datetime]
    encrypted: Awaitable[bool]
    kms_key_id: Awaitable[str]
    outpost_arn: Awaitable[str]
    size: Awaitable[int]
    snapshot_id: Awaitable[str]
    state: Awaitable[VolumeStateType]
    volume_id: Awaitable[str]
    iops: Awaitable[int]
    tags: Awaitable[List[TagTypeDef]]
    volume_type: Awaitable[VolumeTypeType]
    fast_restored: Awaitable[bool]
    multi_attach_enabled: Awaitable[bool]
    throughput: Awaitable[int]
    sse_type: Awaitable[SSETypeType]
    id: str
    snapshots: VolumeSnapshotsCollection
    meta: Awaitable["EC2ResourceMeta"]

    async def attach_to_instance(
        self, *, Device: str, InstanceId: str, DryRun: bool = ...
    ) -> VolumeAttachmentResponseTypeDef:
        """
        Attaches an EBS volume to a running or stopped instance and exposes it to the
        instance with the specified device
        name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Volume.attach_to_instance)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#volumeattach_to_instance-method)
        """

    async def create_snapshot(
        self,
        *,
        Description: str = ...,
        OutpostArn: str = ...,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...,
        DryRun: bool = ...,
    ) -> "_Snapshot":
        """
        Creates a snapshot of an EBS volume and stores it in Amazon S3.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Volume.create_snapshot)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#volumecreate_snapshot-method)
        """

    async def create_tags(self, *, Tags: Sequence[TagTypeDef], DryRun: bool = ...) -> None:
        """
        Adds or overwrites only the specified tags for the specified Amazon EC2
        resource or
        resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.DhcpOptions.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#dhcpoptionscreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Image.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#imagecreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.InternetGateway.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#internetgatewaycreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.NetworkAcl.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#networkaclcreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.NetworkInterface.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#networkinterfacecreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.RouteTable.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#routetablecreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.SecurityGroup.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#securitygroupcreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Snapshot.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#snapshotcreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Subnet.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#subnetcreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Volume.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#volumecreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Vpc.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#vpccreate_tags-method)
        """

    async def delete(self, *, DryRun: bool = ...) -> None:
        """
        Deletes the specified EBS volume.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Volume.delete)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#volumedelete-method)
        """

    async def describe_attribute(
        self, *, Attribute: VolumeAttributeNameType, DryRun: bool = ...
    ) -> DescribeVolumeAttributeResultTypeDef:
        """
        Describes the specified attribute of the specified volume.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Volume.describe_attribute)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#volumedescribe_attribute-method)
        """

    async def describe_status(
        self,
        *,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
        DryRun: bool = ...,
    ) -> DescribeVolumeStatusResultTypeDef:
        """
        Describes the status of the specified volumes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Volume.describe_status)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#volumedescribe_status-method)
        """

    async def detach_from_instance(
        self, *, Device: str = ..., Force: bool = ..., InstanceId: str = ..., DryRun: bool = ...
    ) -> VolumeAttachmentResponseTypeDef:
        """
        Detaches an EBS volume from an instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Volume.detach_from_instance)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#volumedetach_from_instance-method)
        """

    async def enable_io(self, *, DryRun: bool = ...) -> None:
        """
        Enables I/O operations for a volume that had I/O operations disabled because
        the data on the volume was potentially
        inconsistent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Volume.enable_io)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#volumeenable_io-method)
        """

    async def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Volume.get_available_subresources)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#volumeget_available_subresources-method)
        """

    async def load(self) -> None:
        """
        Calls :py:meth:`EC2.Client.describe_volumes` to update the attributes of the
        Volume
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Volume.load)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#volumeload-method)
        """

    async def modify_attribute(
        self, *, AutoEnableIO: AttributeBooleanValueTypeDef = ..., DryRun: bool = ...
    ) -> None:
        """
        Modifies a volume attribute.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Volume.modify_attribute)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#volumemodify_attribute-method)
        """

    async def reload(self) -> None:
        """
        Calls :py:meth:`EC2.Client.describe_volumes` to update the attributes of the
        Volume
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Volume.reload)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#volumereload-method)
        """


_Volume = Volume


class RouteTable(AIOBoto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.RouteTable)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#routetable)
    """

    associations_attribute: Awaitable[List[RouteTableAssociationTypeDef]]
    propagating_vgws: Awaitable[List[PropagatingVgwTypeDef]]
    route_table_id: Awaitable[str]
    routes_attribute: Awaitable[List[RouteTypeDef]]
    tags: Awaitable[List[TagTypeDef]]
    vpc_id: Awaitable[str]
    owner_id: Awaitable[str]
    id: str
    associations: List["RouteTableAssociation"]
    routes: List["Route"]
    vpc: "Vpc"
    meta: Awaitable["EC2ResourceMeta"]

    async def associate_with_subnet(
        self, *, DryRun: bool = ..., SubnetId: str = ..., GatewayId: str = ...
    ) -> "_RouteTableAssociation":
        """
        Associates a subnet in your VPC or an internet gateway or virtual private
        gateway attached to your VPC with a route table in your
        VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.RouteTable.associate_with_subnet)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#routetableassociate_with_subnet-method)
        """

    async def create_route(
        self,
        *,
        DestinationCidrBlock: str = ...,
        DestinationIpv6CidrBlock: str = ...,
        DestinationPrefixListId: str = ...,
        DryRun: bool = ...,
        VpcEndpointId: str = ...,
        EgressOnlyInternetGatewayId: str = ...,
        GatewayId: str = ...,
        InstanceId: str = ...,
        NatGatewayId: str = ...,
        TransitGatewayId: str = ...,
        LocalGatewayId: str = ...,
        CarrierGatewayId: str = ...,
        NetworkInterfaceId: str = ...,
        VpcPeeringConnectionId: str = ...,
        CoreNetworkArn: str = ...,
    ) -> "_Route":
        """
        Creates a route in a route table within a VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.RouteTable.create_route)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#routetablecreate_route-method)
        """

    async def create_tags(self, *, Tags: Sequence[TagTypeDef], DryRun: bool = ...) -> None:
        """
        Adds or overwrites only the specified tags for the specified Amazon EC2
        resource or
        resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.DhcpOptions.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#dhcpoptionscreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Image.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#imagecreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.InternetGateway.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#internetgatewaycreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.NetworkAcl.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#networkaclcreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.NetworkInterface.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#networkinterfacecreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.RouteTable.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#routetablecreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.SecurityGroup.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#securitygroupcreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Snapshot.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#snapshotcreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Subnet.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#subnetcreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Volume.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#volumecreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Vpc.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#vpccreate_tags-method)
        """

    async def delete(self, *, DryRun: bool = ...) -> None:
        """
        Deletes the specified route table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.RouteTable.delete)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#routetabledelete-method)
        """

    async def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.RouteTable.get_available_subresources)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#routetableget_available_subresources-method)
        """

    async def load(self) -> None:
        """
        Calls :py:meth:`EC2.Client.describe_route_tables` to update the attributes of
        the RouteTable
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.RouteTable.load)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#routetableload-method)
        """

    async def reload(self) -> None:
        """
        Calls :py:meth:`EC2.Client.describe_route_tables` to update the attributes of
        the RouteTable
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.RouteTable.reload)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#routetablereload-method)
        """


_RouteTable = RouteTable


class Subnet(AIOBoto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.Subnet)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#subnet)
    """

    availability_zone: Awaitable[str]
    availability_zone_id: Awaitable[str]
    available_ip_address_count: Awaitable[int]
    cidr_block: Awaitable[str]
    default_for_az: Awaitable[bool]
    enable_lni_at_device_index: Awaitable[int]
    map_public_ip_on_launch: Awaitable[bool]
    map_customer_owned_ip_on_launch: Awaitable[bool]
    customer_owned_ipv4_pool: Awaitable[str]
    state: Awaitable[SubnetStateType]
    subnet_id: Awaitable[str]
    vpc_id: Awaitable[str]
    owner_id: Awaitable[str]
    assign_ipv6_address_on_creation: Awaitable[bool]
    ipv6_cidr_block_association_set: Awaitable[List[SubnetIpv6CidrBlockAssociationTypeDef]]
    tags: Awaitable[List[TagTypeDef]]
    subnet_arn: Awaitable[str]
    outpost_arn: Awaitable[str]
    enable_dns64: Awaitable[bool]
    ipv6_native: Awaitable[bool]
    private_dns_name_options_on_launch: Awaitable[PrivateDnsNameOptionsOnLaunchResponseTypeDef]
    id: str
    vpc: "Vpc"
    instances: SubnetInstancesCollection
    network_interfaces: SubnetNetworkInterfacesCollection
    meta: Awaitable["EC2ResourceMeta"]

    async def create_instances(
        self,
        *,
        MaxCount: int,
        MinCount: int,
        BlockDeviceMappings: Sequence[BlockDeviceMappingTypeDef] = ...,
        ImageId: str = ...,
        InstanceType: InstanceTypeType = ...,
        Ipv6AddressCount: int = ...,
        Ipv6Addresses: Sequence[InstanceIpv6AddressTypeDef] = ...,
        KernelId: str = ...,
        KeyName: str = ...,
        Monitoring: RunInstancesMonitoringEnabledTypeDef = ...,
        Placement: PlacementTypeDef = ...,
        RamdiskId: str = ...,
        SecurityGroupIds: Sequence[str] = ...,
        SecurityGroups: Sequence[str] = ...,
        UserData: str = ...,
        AdditionalInfo: str = ...,
        ClientToken: str = ...,
        DisableApiTermination: bool = ...,
        DryRun: bool = ...,
        EbsOptimized: bool = ...,
        IamInstanceProfile: IamInstanceProfileSpecificationTypeDef = ...,
        InstanceInitiatedShutdownBehavior: ShutdownBehaviorType = ...,
        NetworkInterfaces: Sequence[InstanceNetworkInterfaceSpecificationSubnetTypeDef] = ...,
        PrivateIpAddress: str = ...,
        ElasticGpuSpecification: Sequence[ElasticGpuSpecificationTypeDef] = ...,
        ElasticInferenceAccelerators: Sequence[ElasticInferenceAcceleratorTypeDef] = ...,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...,
        LaunchTemplate: LaunchTemplateSpecificationTypeDef = ...,
        InstanceMarketOptions: InstanceMarketOptionsRequestTypeDef = ...,
        CreditSpecification: CreditSpecificationRequestTypeDef = ...,
        CpuOptions: CpuOptionsRequestTypeDef = ...,
        CapacityReservationSpecification: CapacityReservationSpecificationTypeDef = ...,
        HibernationOptions: HibernationOptionsRequestTypeDef = ...,
        LicenseSpecifications: Sequence[LicenseConfigurationRequestTypeDef] = ...,
        MetadataOptions: InstanceMetadataOptionsRequestTypeDef = ...,
        EnclaveOptions: EnclaveOptionsRequestTypeDef = ...,
        PrivateDnsNameOptions: PrivateDnsNameOptionsRequestTypeDef = ...,
        MaintenanceOptions: InstanceMaintenanceOptionsRequestTypeDef = ...,
        DisableApiStop: bool = ...,
        EnablePrimaryIpv6: bool = ...,
    ) -> List["_Instance"]:
        """
        Launches the specified number of instances using an AMI for which you have
        permissions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Subnet.create_instances)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#subnetcreate_instances-method)
        """

    async def create_network_interface(
        self,
        *,
        Description: str = ...,
        DryRun: bool = ...,
        Groups: Sequence[str] = ...,
        Ipv6AddressCount: int = ...,
        Ipv6Addresses: Sequence[InstanceIpv6AddressTypeDef] = ...,
        PrivateIpAddress: str = ...,
        PrivateIpAddresses: Sequence[PrivateIpAddressSpecificationTypeDef] = ...,
        SecondaryPrivateIpAddressCount: int = ...,
        Ipv4Prefixes: Sequence[Ipv4PrefixSpecificationRequestTypeDef] = ...,
        Ipv4PrefixCount: int = ...,
        Ipv6Prefixes: Sequence[Ipv6PrefixSpecificationRequestTypeDef] = ...,
        Ipv6PrefixCount: int = ...,
        InterfaceType: NetworkInterfaceCreationTypeType = ...,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...,
        ClientToken: str = ...,
        EnablePrimaryIpv6: bool = ...,
        ConnectionTrackingSpecification: ConnectionTrackingSpecificationRequestTypeDef = ...,
    ) -> "_NetworkInterface":
        """
        Creates a network interface in the specified subnet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Subnet.create_network_interface)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#subnetcreate_network_interface-method)
        """

    async def create_tags(self, *, Tags: Sequence[TagTypeDef], DryRun: bool = ...) -> None:
        """
        Adds or overwrites only the specified tags for the specified Amazon EC2
        resource or
        resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.DhcpOptions.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#dhcpoptionscreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Image.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#imagecreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.InternetGateway.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#internetgatewaycreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.NetworkAcl.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#networkaclcreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.NetworkInterface.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#networkinterfacecreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.RouteTable.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#routetablecreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.SecurityGroup.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#securitygroupcreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Snapshot.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#snapshotcreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Subnet.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#subnetcreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Volume.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#volumecreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Vpc.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#vpccreate_tags-method)
        """

    async def delete(self, *, DryRun: bool = ...) -> None:
        """
        Deletes the specified subnet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Subnet.delete)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#subnetdelete-method)
        """

    async def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Subnet.get_available_subresources)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#subnetget_available_subresources-method)
        """

    async def load(self) -> None:
        """
        Calls :py:meth:`EC2.Client.describe_subnets` to update the attributes of the
        Subnet
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Subnet.load)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#subnetload-method)
        """

    async def reload(self) -> None:
        """
        Calls :py:meth:`EC2.Client.describe_subnets` to update the attributes of the
        Subnet
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Subnet.reload)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#subnetreload-method)
        """


_Subnet = Subnet


class Vpc(AIOBoto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.Vpc)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#vpc)
    """

    cidr_block: Awaitable[str]
    dhcp_options_id: Awaitable[str]
    state: Awaitable[VpcStateType]
    vpc_id: Awaitable[str]
    owner_id: Awaitable[str]
    instance_tenancy: Awaitable[TenancyType]
    ipv6_cidr_block_association_set: Awaitable[List[VpcIpv6CidrBlockAssociationTypeDef]]
    cidr_block_association_set: Awaitable[List[VpcCidrBlockAssociationTypeDef]]
    is_default: Awaitable[bool]
    tags: Awaitable[List[TagTypeDef]]
    id: str
    dhcp_options: "DhcpOptions"
    accepted_vpc_peering_connections: VpcAcceptedVpcPeeringConnectionsCollection
    instances: VpcInstancesCollection
    internet_gateways: VpcInternetGatewaysCollection
    network_acls: VpcNetworkAclsCollection
    network_interfaces: VpcNetworkInterfacesCollection
    requested_vpc_peering_connections: VpcRequestedVpcPeeringConnectionsCollection
    route_tables: VpcRouteTablesCollection
    security_groups: VpcSecurityGroupsCollection
    subnets: VpcSubnetsCollection
    meta: Awaitable["EC2ResourceMeta"]

    async def associate_dhcp_options(self, *, DhcpOptionsId: str, DryRun: bool = ...) -> None:
        """
        Associates a set of DHCP options (that you've previously created) with the
        specified VPC, or associates no DHCP options with the
        VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Vpc.associate_dhcp_options)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#vpcassociate_dhcp_options-method)
        """

    async def attach_classic_link_instance(
        self, *, Groups: Sequence[str], InstanceId: str, DryRun: bool = ...
    ) -> AttachClassicLinkVpcResultTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Vpc.attach_classic_link_instance)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#vpcattach_classic_link_instance-method)
        """

    async def attach_internet_gateway(self, *, InternetGatewayId: str, DryRun: bool = ...) -> None:
        """
        Attaches an internet gateway or a virtual private gateway to a VPC, enabling
        connectivity between the internet and the
        VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Vpc.attach_internet_gateway)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#vpcattach_internet_gateway-method)
        """

    async def create_network_acl(
        self,
        *,
        DryRun: bool = ...,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...,
        ClientToken: str = ...,
    ) -> "_NetworkAcl":
        """
        Creates a network ACL in a VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Vpc.create_network_acl)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#vpccreate_network_acl-method)
        """

    async def create_route_table(
        self,
        *,
        DryRun: bool = ...,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...,
        ClientToken: str = ...,
    ) -> "_RouteTable":
        """
        Creates a route table for the specified VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Vpc.create_route_table)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#vpccreate_route_table-method)
        """

    async def create_security_group(
        self,
        *,
        Description: str,
        GroupName: str,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...,
        DryRun: bool = ...,
    ) -> "_SecurityGroup":
        """
        Creates a security group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Vpc.create_security_group)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#vpccreate_security_group-method)
        """

    async def create_subnet(
        self,
        *,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...,
        AvailabilityZone: str = ...,
        AvailabilityZoneId: str = ...,
        CidrBlock: str = ...,
        Ipv6CidrBlock: str = ...,
        OutpostArn: str = ...,
        DryRun: bool = ...,
        Ipv6Native: bool = ...,
        Ipv4IpamPoolId: str = ...,
        Ipv4NetmaskLength: int = ...,
        Ipv6IpamPoolId: str = ...,
        Ipv6NetmaskLength: int = ...,
    ) -> "_Subnet":
        """
        Creates a subnet in the specified VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Vpc.create_subnet)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#vpccreate_subnet-method)
        """

    async def create_tags(self, *, Tags: Sequence[TagTypeDef], DryRun: bool = ...) -> None:
        """
        Adds or overwrites only the specified tags for the specified Amazon EC2
        resource or
        resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.DhcpOptions.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#dhcpoptionscreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Image.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#imagecreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.InternetGateway.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#internetgatewaycreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.NetworkAcl.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#networkaclcreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.NetworkInterface.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#networkinterfacecreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.RouteTable.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#routetablecreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.SecurityGroup.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#securitygroupcreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Snapshot.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#snapshotcreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Subnet.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#subnetcreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Volume.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#volumecreate_tags-method)

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Vpc.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#vpccreate_tags-method)
        """

    async def delete(self, *, DryRun: bool = ...) -> None:
        """
        Deletes the specified VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Vpc.delete)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#vpcdelete-method)
        """

    async def describe_attribute(
        self, *, Attribute: VpcAttributeNameType, DryRun: bool = ...
    ) -> DescribeVpcAttributeResultTypeDef:
        """
        Describes the specified attribute of the specified VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Vpc.describe_attribute)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#vpcdescribe_attribute-method)
        """

    async def detach_classic_link_instance(
        self, *, InstanceId: str, DryRun: bool = ...
    ) -> DetachClassicLinkVpcResultTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Vpc.detach_classic_link_instance)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#vpcdetach_classic_link_instance-method)
        """

    async def detach_internet_gateway(self, *, InternetGatewayId: str, DryRun: bool = ...) -> None:
        """
        Detaches an internet gateway from a VPC, disabling connectivity between the
        internet and the
        VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Vpc.detach_internet_gateway)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#vpcdetach_internet_gateway-method)
        """

    async def disable_classic_link(
        self, *, DryRun: bool = ...
    ) -> DisableVpcClassicLinkResultTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Vpc.disable_classic_link)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#vpcdisable_classic_link-method)
        """

    async def enable_classic_link(self, *, DryRun: bool = ...) -> EnableVpcClassicLinkResultTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Vpc.enable_classic_link)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#vpcenable_classic_link-method)
        """

    async def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Vpc.get_available_subresources)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#vpcget_available_subresources-method)
        """

    async def load(self) -> None:
        """
        Calls :py:meth:`EC2.Client.describe_vpcs` to update the attributes of the Vpc
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Vpc.load)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#vpcload-method)
        """

    async def modify_attribute(
        self,
        *,
        EnableDnsHostnames: AttributeBooleanValueTypeDef = ...,
        EnableDnsSupport: AttributeBooleanValueTypeDef = ...,
        EnableNetworkAddressUsageMetrics: AttributeBooleanValueTypeDef = ...,
    ) -> None:
        """
        Modifies the specified attribute of the specified VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Vpc.modify_attribute)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#vpcmodify_attribute-method)
        """

    async def reload(self) -> None:
        """
        Calls :py:meth:`EC2.Client.describe_vpcs` to update the attributes of the Vpc
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Vpc.reload)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#vpcreload-method)
        """

    async def request_vpc_peering_connection(
        self,
        *,
        DryRun: bool = ...,
        PeerOwnerId: str = ...,
        PeerVpcId: str = ...,
        PeerRegion: str = ...,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...,
    ) -> "_VpcPeeringConnection":
        """
        Requests a VPC peering connection between two VPCs: a requester VPC that you
        own and an accepter VPC with which to create the
        connection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Vpc.request_vpc_peering_connection)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#vpcrequest_vpc_peering_connection-method)
        """

    async def wait_until_available(self) -> None:
        """
        Waits until this Vpc is available.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Vpc.wait_until_available)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#vpcwait_until_available-method)
        """

    async def wait_until_exists(self) -> None:
        """
        Waits until this Vpc is exists.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Vpc.wait_until_exists)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#vpcwait_until_exists-method)
        """


_Vpc = Vpc


class EC2ResourceMeta(ResourceMeta):
    client: EC2Client


class EC2ServiceResource(AIOBoto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/)
    """

    meta: "EC2ResourceMeta"
    classic_addresses: ServiceResourceClassicAddressesCollection
    dhcp_options_sets: ServiceResourceDhcpOptionsSetsCollection
    images: ServiceResourceImagesCollection
    instances: ServiceResourceInstancesCollection
    internet_gateways: ServiceResourceInternetGatewaysCollection
    key_pairs: ServiceResourceKeyPairsCollection
    network_acls: ServiceResourceNetworkAclsCollection
    network_interfaces: ServiceResourceNetworkInterfacesCollection
    placement_groups: ServiceResourcePlacementGroupsCollection
    route_tables: ServiceResourceRouteTablesCollection
    security_groups: ServiceResourceSecurityGroupsCollection
    snapshots: ServiceResourceSnapshotsCollection
    subnets: ServiceResourceSubnetsCollection
    volumes: ServiceResourceVolumesCollection
    vpc_addresses: ServiceResourceVpcAddressesCollection
    vpc_peering_connections: ServiceResourceVpcPeeringConnectionsCollection
    vpcs: ServiceResourceVpcsCollection

    async def ClassicAddress(self, public_ip: str) -> "_ClassicAddress":
        """
        Creates a ClassicAddress resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.ClassicAddress)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#ec2serviceresourceclassicaddress-method)
        """

    async def DhcpOptions(self, id: str) -> "_DhcpOptions":
        """
        Creates a DhcpOptions resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.DhcpOptions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#ec2serviceresourcedhcpoptions-method)
        """

    async def Image(self, id: str) -> "_Image":
        """
        Creates a Image resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.Image)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#ec2serviceresourceimage-method)
        """

    async def Instance(self, id: str) -> "_Instance":
        """
        Creates a Instance resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.Instance)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#ec2serviceresourceinstance-method)
        """

    async def InternetGateway(self, id: str) -> "_InternetGateway":
        """
        Creates a InternetGateway resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.InternetGateway)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#ec2serviceresourceinternetgateway-method)
        """

    async def KeyPair(self, name: str) -> "_KeyPair":
        """
        Creates a KeyPairInfo resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.KeyPair)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#ec2serviceresourcekeypair-method)
        """

    async def NetworkAcl(self, id: str) -> "_NetworkAcl":
        """
        Creates a NetworkAcl resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.NetworkAcl)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#ec2serviceresourcenetworkacl-method)
        """

    async def NetworkInterface(self, id: str) -> "_NetworkInterface":
        """
        Creates a NetworkInterface resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.NetworkInterface)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#ec2serviceresourcenetworkinterface-method)
        """

    async def NetworkInterfaceAssociation(self, id: str) -> "_NetworkInterfaceAssociation":
        """
        Creates a NetworkInterfaceAssociation resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.NetworkInterfaceAssociation)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#ec2serviceresourcenetworkinterfaceassociation-method)
        """

    async def PlacementGroup(self, name: str) -> "_PlacementGroup":
        """
        Creates a PlacementGroup resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.PlacementGroup)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#ec2serviceresourceplacementgroup-method)
        """

    async def Route(self, route_table_id: str, destination_cidr_block: str) -> "_Route":
        """
        Creates a Route resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.Route)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#ec2serviceresourceroute-method)
        """

    async def RouteTable(self, id: str) -> "_RouteTable":
        """
        Creates a RouteTable resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.RouteTable)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#ec2serviceresourceroutetable-method)
        """

    async def RouteTableAssociation(self, id: str) -> "_RouteTableAssociation":
        """
        Creates a RouteTableAssociation resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.RouteTableAssociation)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#ec2serviceresourceroutetableassociation-method)
        """

    async def SecurityGroup(self, id: str) -> "_SecurityGroup":
        """
        Creates a SecurityGroup resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.SecurityGroup)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#ec2serviceresourcesecuritygroup-method)
        """

    async def Snapshot(self, id: str) -> "_Snapshot":
        """
        Creates a Snapshot resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.Snapshot)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#ec2serviceresourcesnapshot-method)
        """

    async def Subnet(self, id: str) -> "_Subnet":
        """
        Creates a Subnet resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.Subnet)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#ec2serviceresourcesubnet-method)
        """

    async def Tag(self, resource_id: str, key: str, value: str) -> "_Tag":
        """
        Creates a Tag resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.Tag)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#ec2serviceresourcetag-method)
        """

    async def Volume(self, id: str) -> "_Volume":
        """
        Creates a Volume resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.Volume)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#ec2serviceresourcevolume-method)
        """

    async def Vpc(self, id: str) -> "_Vpc":
        """
        Creates a Vpc resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.Vpc)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#ec2serviceresourcevpc-method)
        """

    async def VpcAddress(self, allocation_id: str) -> "_VpcAddress":
        """
        Creates a VpcAddress resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.VpcAddress)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#ec2serviceresourcevpcaddress-method)
        """

    async def VpcPeeringConnection(self, id: str) -> "_VpcPeeringConnection":
        """
        Creates a VpcPeeringConnection resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.VpcPeeringConnection)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#ec2serviceresourcevpcpeeringconnection-method)
        """

    async def create_dhcp_options(
        self,
        *,
        DhcpConfigurations: Sequence[NewDhcpConfigurationTypeDef],
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...,
        DryRun: bool = ...,
    ) -> "_DhcpOptions":
        """
        Creates a set of DHCP options for your VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.create_dhcp_options)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#ec2serviceresourcecreate_dhcp_options-method)
        """

    async def create_instances(
        self,
        *,
        MaxCount: int,
        MinCount: int,
        BlockDeviceMappings: Sequence[BlockDeviceMappingTypeDef] = ...,
        ImageId: str = ...,
        InstanceType: InstanceTypeType = ...,
        Ipv6AddressCount: int = ...,
        Ipv6Addresses: Sequence[InstanceIpv6AddressTypeDef] = ...,
        KernelId: str = ...,
        KeyName: str = ...,
        Monitoring: RunInstancesMonitoringEnabledTypeDef = ...,
        Placement: PlacementTypeDef = ...,
        RamdiskId: str = ...,
        SecurityGroupIds: Sequence[str] = ...,
        SecurityGroups: Sequence[str] = ...,
        SubnetId: str = ...,
        UserData: str = ...,
        AdditionalInfo: str = ...,
        ClientToken: str = ...,
        DisableApiTermination: bool = ...,
        DryRun: bool = ...,
        EbsOptimized: bool = ...,
        IamInstanceProfile: IamInstanceProfileSpecificationTypeDef = ...,
        InstanceInitiatedShutdownBehavior: ShutdownBehaviorType = ...,
        NetworkInterfaces: Sequence[
            InstanceNetworkInterfaceSpecificationServiceResourceTypeDef
        ] = ...,
        PrivateIpAddress: str = ...,
        ElasticGpuSpecification: Sequence[ElasticGpuSpecificationTypeDef] = ...,
        ElasticInferenceAccelerators: Sequence[ElasticInferenceAcceleratorTypeDef] = ...,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...,
        LaunchTemplate: LaunchTemplateSpecificationTypeDef = ...,
        InstanceMarketOptions: InstanceMarketOptionsRequestTypeDef = ...,
        CreditSpecification: CreditSpecificationRequestTypeDef = ...,
        CpuOptions: CpuOptionsRequestTypeDef = ...,
        CapacityReservationSpecification: CapacityReservationSpecificationTypeDef = ...,
        HibernationOptions: HibernationOptionsRequestTypeDef = ...,
        LicenseSpecifications: Sequence[LicenseConfigurationRequestTypeDef] = ...,
        MetadataOptions: InstanceMetadataOptionsRequestTypeDef = ...,
        EnclaveOptions: EnclaveOptionsRequestTypeDef = ...,
        PrivateDnsNameOptions: PrivateDnsNameOptionsRequestTypeDef = ...,
        MaintenanceOptions: InstanceMaintenanceOptionsRequestTypeDef = ...,
        DisableApiStop: bool = ...,
        EnablePrimaryIpv6: bool = ...,
    ) -> List["_Instance"]:
        """
        Launches the specified number of instances using an AMI for which you have
        permissions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.create_instances)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#ec2serviceresourcecreate_instances-method)
        """

    async def create_internet_gateway(
        self, *, TagSpecifications: Sequence[TagSpecificationTypeDef] = ..., DryRun: bool = ...
    ) -> "_InternetGateway":
        """
        Creates an internet gateway for use with a VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.create_internet_gateway)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#ec2serviceresourcecreate_internet_gateway-method)
        """

    async def create_key_pair(
        self,
        *,
        KeyName: str,
        DryRun: bool = ...,
        KeyType: KeyTypeType = ...,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...,
        KeyFormat: KeyFormatType = ...,
    ) -> "_KeyPair":
        """
        Creates an ED25519 or 2048-bit RSA key pair with the specified name and in the
        specified PEM or PPK
        format.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.create_key_pair)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#ec2serviceresourcecreate_key_pair-method)
        """

    async def create_network_acl(
        self,
        *,
        VpcId: str,
        DryRun: bool = ...,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...,
        ClientToken: str = ...,
    ) -> "_NetworkAcl":
        """
        Creates a network ACL in a VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.create_network_acl)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#ec2serviceresourcecreate_network_acl-method)
        """

    async def create_network_interface(
        self,
        *,
        SubnetId: str,
        Description: str = ...,
        DryRun: bool = ...,
        Groups: Sequence[str] = ...,
        Ipv6AddressCount: int = ...,
        Ipv6Addresses: Sequence[InstanceIpv6AddressTypeDef] = ...,
        PrivateIpAddress: str = ...,
        PrivateIpAddresses: Sequence[PrivateIpAddressSpecificationTypeDef] = ...,
        SecondaryPrivateIpAddressCount: int = ...,
        Ipv4Prefixes: Sequence[Ipv4PrefixSpecificationRequestTypeDef] = ...,
        Ipv4PrefixCount: int = ...,
        Ipv6Prefixes: Sequence[Ipv6PrefixSpecificationRequestTypeDef] = ...,
        Ipv6PrefixCount: int = ...,
        InterfaceType: NetworkInterfaceCreationTypeType = ...,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...,
        ClientToken: str = ...,
        EnablePrimaryIpv6: bool = ...,
        ConnectionTrackingSpecification: ConnectionTrackingSpecificationRequestTypeDef = ...,
    ) -> "_NetworkInterface":
        """
        Creates a network interface in the specified subnet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.create_network_interface)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#ec2serviceresourcecreate_network_interface-method)
        """

    async def create_placement_group(
        self,
        *,
        DryRun: bool = ...,
        GroupName: str = ...,
        Strategy: PlacementStrategyType = ...,
        PartitionCount: int = ...,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...,
        SpreadLevel: SpreadLevelType = ...,
    ) -> "_PlacementGroup":
        """
        Creates a placement group in which to launch instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.create_placement_group)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#ec2serviceresourcecreate_placement_group-method)
        """

    async def create_route_table(
        self,
        *,
        VpcId: str,
        DryRun: bool = ...,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...,
        ClientToken: str = ...,
    ) -> "_RouteTable":
        """
        Creates a route table for the specified VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.create_route_table)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#ec2serviceresourcecreate_route_table-method)
        """

    async def create_security_group(
        self,
        *,
        Description: str,
        GroupName: str,
        VpcId: str = ...,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...,
        DryRun: bool = ...,
    ) -> "_SecurityGroup":
        """
        Creates a security group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.create_security_group)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#ec2serviceresourcecreate_security_group-method)
        """

    async def create_snapshot(
        self,
        *,
        VolumeId: str,
        Description: str = ...,
        OutpostArn: str = ...,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...,
        DryRun: bool = ...,
    ) -> "_Snapshot":
        """
        Creates a snapshot of an EBS volume and stores it in Amazon S3.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.create_snapshot)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#ec2serviceresourcecreate_snapshot-method)
        """

    async def create_subnet(
        self,
        *,
        VpcId: str,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...,
        AvailabilityZone: str = ...,
        AvailabilityZoneId: str = ...,
        CidrBlock: str = ...,
        Ipv6CidrBlock: str = ...,
        OutpostArn: str = ...,
        DryRun: bool = ...,
        Ipv6Native: bool = ...,
        Ipv4IpamPoolId: str = ...,
        Ipv4NetmaskLength: int = ...,
        Ipv6IpamPoolId: str = ...,
        Ipv6NetmaskLength: int = ...,
    ) -> "_Subnet":
        """
        Creates a subnet in the specified VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.create_subnet)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#ec2serviceresourcecreate_subnet-method)
        """

    async def create_tags(
        self, *, Resources: Sequence[str], Tags: Sequence[TagTypeDef], DryRun: bool = ...
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.create_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#ec2serviceresourcecreate_tags-method)
        """

    async def create_volume(
        self,
        *,
        AvailabilityZone: str,
        Encrypted: bool = ...,
        Iops: int = ...,
        KmsKeyId: str = ...,
        OutpostArn: str = ...,
        Size: int = ...,
        SnapshotId: str = ...,
        VolumeType: VolumeTypeType = ...,
        DryRun: bool = ...,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...,
        MultiAttachEnabled: bool = ...,
        Throughput: int = ...,
        ClientToken: str = ...,
    ) -> "_Volume":
        """
        Creates an EBS volume that can be attached to an instance in the same
        Availability
        Zone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.create_volume)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#ec2serviceresourcecreate_volume-method)
        """

    async def create_vpc(
        self,
        *,
        CidrBlock: str = ...,
        AmazonProvidedIpv6CidrBlock: bool = ...,
        Ipv6Pool: str = ...,
        Ipv6CidrBlock: str = ...,
        Ipv4IpamPoolId: str = ...,
        Ipv4NetmaskLength: int = ...,
        Ipv6IpamPoolId: str = ...,
        Ipv6NetmaskLength: int = ...,
        DryRun: bool = ...,
        InstanceTenancy: TenancyType = ...,
        Ipv6CidrBlockNetworkBorderGroup: str = ...,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...,
    ) -> "_Vpc":
        """
        Creates a VPC with the specified CIDR blocks.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.create_vpc)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#ec2serviceresourcecreate_vpc-method)
        """

    async def create_vpc_peering_connection(
        self,
        *,
        VpcId: str,
        DryRun: bool = ...,
        PeerOwnerId: str = ...,
        PeerVpcId: str = ...,
        PeerRegion: str = ...,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...,
    ) -> "_VpcPeeringConnection":
        """
        Requests a VPC peering connection between two VPCs: a requester VPC that you
        own and an accepter VPC with which to create the
        connection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.create_vpc_peering_connection)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#ec2serviceresourcecreate_vpc_peering_connection-method)
        """

    async def disassociate_route_table(self, *, AssociationId: str, DryRun: bool = ...) -> None:
        """
        Disassociates a subnet or gateway from a route table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.disassociate_route_table)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#ec2serviceresourcedisassociate_route_table-method)
        """

    async def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.get_available_subresources)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#ec2serviceresourceget_available_subresources-method)
        """

    async def import_key_pair(
        self,
        *,
        KeyName: str,
        PublicKeyMaterial: BlobTypeDef,
        DryRun: bool = ...,
        TagSpecifications: Sequence[TagSpecificationTypeDef] = ...,
    ) -> "_KeyPairInfo":
        """
        Imports the public key from an RSA or ED25519 key pair that you created with a
        third-party
        tool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.import_key_pair)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#ec2serviceresourceimport_key_pair-method)
        """

    async def register_image(
        self,
        *,
        Name: str,
        ImageLocation: str = ...,
        Architecture: ArchitectureValuesType = ...,
        BlockDeviceMappings: Sequence[BlockDeviceMappingTypeDef] = ...,
        Description: str = ...,
        DryRun: bool = ...,
        EnaSupport: bool = ...,
        KernelId: str = ...,
        BillingProducts: Sequence[str] = ...,
        RamdiskId: str = ...,
        RootDeviceName: str = ...,
        SriovNetSupport: str = ...,
        VirtualizationType: str = ...,
        BootMode: BootModeValuesType = ...,
        TpmSupport: Literal["v2.0"] = ...,
        UefiData: str = ...,
        ImdsSupport: Literal["v2.0"] = ...,
    ) -> "_Image":
        """
        Registers an AMI.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.register_image)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ec2/service_resource/#ec2serviceresourceregister_image-method)
        """
