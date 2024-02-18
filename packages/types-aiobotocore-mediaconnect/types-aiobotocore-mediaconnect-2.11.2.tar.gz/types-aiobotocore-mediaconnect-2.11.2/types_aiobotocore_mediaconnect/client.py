"""
Type annotations for mediaconnect service client.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediaconnect/client/)

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_mediaconnect.client import MediaConnectClient

    session = get_session()
    async with session.create_client("mediaconnect") as client:
        client: MediaConnectClient
    ```
"""

import sys
from typing import Any, Dict, Mapping, Sequence, Type, overload

from aiobotocore.client import AioBaseClient
from botocore.client import ClientMeta

from .literals import (
    BridgePlacementType,
    DesiredStateType,
    EntitlementStatusType,
    MediaStreamTypeType,
    ProtocolType,
)
from .paginator import (
    ListBridgesPaginator,
    ListEntitlementsPaginator,
    ListFlowsPaginator,
    ListGatewayInstancesPaginator,
    ListGatewaysPaginator,
    ListOfferingsPaginator,
    ListReservationsPaginator,
)
from .type_defs import (
    AddBridgeOutputRequestTypeDef,
    AddBridgeOutputsResponseTypeDef,
    AddBridgeSourceRequestTypeDef,
    AddBridgeSourcesResponseTypeDef,
    AddEgressGatewayBridgeRequestTypeDef,
    AddFlowMediaStreamsResponseTypeDef,
    AddFlowOutputsResponseTypeDef,
    AddFlowSourcesResponseTypeDef,
    AddFlowVpcInterfacesResponseTypeDef,
    AddIngressGatewayBridgeRequestTypeDef,
    AddMaintenanceTypeDef,
    AddMediaStreamRequestTypeDef,
    AddOutputRequestTypeDef,
    CreateBridgeResponseTypeDef,
    CreateFlowResponseTypeDef,
    CreateGatewayResponseTypeDef,
    DeleteBridgeResponseTypeDef,
    DeleteFlowResponseTypeDef,
    DeleteGatewayResponseTypeDef,
    DeregisterGatewayInstanceResponseTypeDef,
    DescribeBridgeResponseTypeDef,
    DescribeFlowResponseTypeDef,
    DescribeFlowSourceMetadataResponseTypeDef,
    DescribeGatewayInstanceResponseTypeDef,
    DescribeGatewayResponseTypeDef,
    DescribeOfferingResponseTypeDef,
    DescribeReservationResponseTypeDef,
    EmptyResponseMetadataTypeDef,
    FailoverConfigTypeDef,
    GatewayNetworkTypeDef,
    GrantEntitlementRequestTypeDef,
    GrantFlowEntitlementsResponseTypeDef,
    ListBridgesResponseTypeDef,
    ListEntitlementsResponseTypeDef,
    ListFlowsResponseTypeDef,
    ListGatewayInstancesResponseTypeDef,
    ListGatewaysResponseTypeDef,
    ListOfferingsResponseTypeDef,
    ListReservationsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    MediaStreamAttributesRequestTypeDef,
    MediaStreamOutputConfigurationRequestTypeDef,
    MediaStreamSourceConfigurationRequestTypeDef,
    PurchaseOfferingResponseTypeDef,
    RemoveBridgeOutputResponseTypeDef,
    RemoveBridgeSourceResponseTypeDef,
    RemoveFlowMediaStreamResponseTypeDef,
    RemoveFlowOutputResponseTypeDef,
    RemoveFlowSourceResponseTypeDef,
    RemoveFlowVpcInterfaceResponseTypeDef,
    RevokeFlowEntitlementResponseTypeDef,
    SetSourceRequestTypeDef,
    StartFlowResponseTypeDef,
    StopFlowResponseTypeDef,
    UpdateBridgeFlowSourceRequestTypeDef,
    UpdateBridgeNetworkOutputRequestTypeDef,
    UpdateBridgeNetworkSourceRequestTypeDef,
    UpdateBridgeOutputResponseTypeDef,
    UpdateBridgeResponseTypeDef,
    UpdateBridgeSourceResponseTypeDef,
    UpdateBridgeStateResponseTypeDef,
    UpdateEgressGatewayBridgeRequestTypeDef,
    UpdateEncryptionTypeDef,
    UpdateFailoverConfigTypeDef,
    UpdateFlowEntitlementResponseTypeDef,
    UpdateFlowMediaStreamResponseTypeDef,
    UpdateFlowOutputResponseTypeDef,
    UpdateFlowResponseTypeDef,
    UpdateFlowSourceResponseTypeDef,
    UpdateGatewayBridgeSourceRequestTypeDef,
    UpdateGatewayInstanceResponseTypeDef,
    UpdateIngressGatewayBridgeRequestTypeDef,
    UpdateMaintenanceTypeDef,
    VpcInterfaceAttachmentTypeDef,
    VpcInterfaceRequestTypeDef,
)
from .waiter import FlowActiveWaiter, FlowDeletedWaiter, FlowStandbyWaiter

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("MediaConnectClient",)


class BotocoreClientError(Exception):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AddFlowOutputs420Exception: Type[BotocoreClientError]
    BadRequestException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    CreateBridge420Exception: Type[BotocoreClientError]
    CreateFlow420Exception: Type[BotocoreClientError]
    CreateGateway420Exception: Type[BotocoreClientError]
    ForbiddenException: Type[BotocoreClientError]
    GrantFlowEntitlements420Exception: Type[BotocoreClientError]
    InternalServerErrorException: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]
    ServiceUnavailableException: Type[BotocoreClientError]
    TooManyRequestsException: Type[BotocoreClientError]


class MediaConnectClient(AioBaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Client)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediaconnect/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        MediaConnectClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Client.exceptions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediaconnect/client/#exceptions)
        """

    async def add_bridge_outputs(
        self, *, BridgeArn: str, Outputs: Sequence[AddBridgeOutputRequestTypeDef]
    ) -> AddBridgeOutputsResponseTypeDef:
        """
        Adds outputs to an existing bridge.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Client.add_bridge_outputs)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediaconnect/client/#add_bridge_outputs)
        """

    async def add_bridge_sources(
        self, *, BridgeArn: str, Sources: Sequence[AddBridgeSourceRequestTypeDef]
    ) -> AddBridgeSourcesResponseTypeDef:
        """
        Adds sources to an existing bridge.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Client.add_bridge_sources)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediaconnect/client/#add_bridge_sources)
        """

    async def add_flow_media_streams(
        self, *, FlowArn: str, MediaStreams: Sequence[AddMediaStreamRequestTypeDef]
    ) -> AddFlowMediaStreamsResponseTypeDef:
        """
        Adds media streams to an existing flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Client.add_flow_media_streams)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediaconnect/client/#add_flow_media_streams)
        """

    async def add_flow_outputs(
        self, *, FlowArn: str, Outputs: Sequence[AddOutputRequestTypeDef]
    ) -> AddFlowOutputsResponseTypeDef:
        """
        Adds outputs to an existing flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Client.add_flow_outputs)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediaconnect/client/#add_flow_outputs)
        """

    async def add_flow_sources(
        self, *, FlowArn: str, Sources: Sequence[SetSourceRequestTypeDef]
    ) -> AddFlowSourcesResponseTypeDef:
        """
        Adds Sources to flow See also: [AWS API
        Documentation](https://docs.aws.amazon.com/goto/WebAPI/mediaconnect-2018-11-14/AddFlowSources).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Client.add_flow_sources)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediaconnect/client/#add_flow_sources)
        """

    async def add_flow_vpc_interfaces(
        self, *, FlowArn: str, VpcInterfaces: Sequence[VpcInterfaceRequestTypeDef]
    ) -> AddFlowVpcInterfacesResponseTypeDef:
        """
        Adds VPC interfaces to flow See also: [AWS API
        Documentation](https://docs.aws.amazon.com/goto/WebAPI/mediaconnect-2018-11-14/AddFlowVpcInterfaces).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Client.add_flow_vpc_interfaces)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediaconnect/client/#add_flow_vpc_interfaces)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Client.can_paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediaconnect/client/#can_paginate)
        """

    async def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Client.close)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediaconnect/client/#close)
        """

    async def create_bridge(
        self,
        *,
        Name: str,
        PlacementArn: str,
        Sources: Sequence[AddBridgeSourceRequestTypeDef],
        EgressGatewayBridge: AddEgressGatewayBridgeRequestTypeDef = ...,
        IngressGatewayBridge: AddIngressGatewayBridgeRequestTypeDef = ...,
        Outputs: Sequence[AddBridgeOutputRequestTypeDef] = ...,
        SourceFailoverConfig: FailoverConfigTypeDef = ...,
    ) -> CreateBridgeResponseTypeDef:
        """
        Creates a new bridge.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Client.create_bridge)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediaconnect/client/#create_bridge)
        """

    async def create_flow(
        self,
        *,
        Name: str,
        AvailabilityZone: str = ...,
        Entitlements: Sequence[GrantEntitlementRequestTypeDef] = ...,
        MediaStreams: Sequence[AddMediaStreamRequestTypeDef] = ...,
        Outputs: Sequence[AddOutputRequestTypeDef] = ...,
        Source: SetSourceRequestTypeDef = ...,
        SourceFailoverConfig: FailoverConfigTypeDef = ...,
        Sources: Sequence[SetSourceRequestTypeDef] = ...,
        VpcInterfaces: Sequence[VpcInterfaceRequestTypeDef] = ...,
        Maintenance: AddMaintenanceTypeDef = ...,
    ) -> CreateFlowResponseTypeDef:
        """
        Creates a new flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Client.create_flow)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediaconnect/client/#create_flow)
        """

    async def create_gateway(
        self,
        *,
        EgressCidrBlocks: Sequence[str],
        Name: str,
        Networks: Sequence[GatewayNetworkTypeDef],
    ) -> CreateGatewayResponseTypeDef:
        """
        Creates a new gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Client.create_gateway)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediaconnect/client/#create_gateway)
        """

    async def delete_bridge(self, *, BridgeArn: str) -> DeleteBridgeResponseTypeDef:
        """
        Deletes a bridge.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Client.delete_bridge)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediaconnect/client/#delete_bridge)
        """

    async def delete_flow(self, *, FlowArn: str) -> DeleteFlowResponseTypeDef:
        """
        Deletes a flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Client.delete_flow)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediaconnect/client/#delete_flow)
        """

    async def delete_gateway(self, *, GatewayArn: str) -> DeleteGatewayResponseTypeDef:
        """
        Deletes a gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Client.delete_gateway)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediaconnect/client/#delete_gateway)
        """

    async def deregister_gateway_instance(
        self, *, GatewayInstanceArn: str, Force: bool = ...
    ) -> DeregisterGatewayInstanceResponseTypeDef:
        """
        Deregisters an instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Client.deregister_gateway_instance)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediaconnect/client/#deregister_gateway_instance)
        """

    async def describe_bridge(self, *, BridgeArn: str) -> DescribeBridgeResponseTypeDef:
        """
        Displays the details of a bridge.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Client.describe_bridge)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediaconnect/client/#describe_bridge)
        """

    async def describe_flow(self, *, FlowArn: str) -> DescribeFlowResponseTypeDef:
        """
        Displays the details of a flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Client.describe_flow)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediaconnect/client/#describe_flow)
        """

    async def describe_flow_source_metadata(
        self, *, FlowArn: str
    ) -> DescribeFlowSourceMetadataResponseTypeDef:
        """
        Displays details of the flow's source stream.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Client.describe_flow_source_metadata)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediaconnect/client/#describe_flow_source_metadata)
        """

    async def describe_gateway(self, *, GatewayArn: str) -> DescribeGatewayResponseTypeDef:
        """
        Displays the details of a gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Client.describe_gateway)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediaconnect/client/#describe_gateway)
        """

    async def describe_gateway_instance(
        self, *, GatewayInstanceArn: str
    ) -> DescribeGatewayInstanceResponseTypeDef:
        """
        Displays the details of an instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Client.describe_gateway_instance)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediaconnect/client/#describe_gateway_instance)
        """

    async def describe_offering(self, *, OfferingArn: str) -> DescribeOfferingResponseTypeDef:
        """
        Displays the details of an offering.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Client.describe_offering)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediaconnect/client/#describe_offering)
        """

    async def describe_reservation(
        self, *, ReservationArn: str
    ) -> DescribeReservationResponseTypeDef:
        """
        Displays the details of a reservation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Client.describe_reservation)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediaconnect/client/#describe_reservation)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Client.generate_presigned_url)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediaconnect/client/#generate_presigned_url)
        """

    async def grant_flow_entitlements(
        self, *, Entitlements: Sequence[GrantEntitlementRequestTypeDef], FlowArn: str
    ) -> GrantFlowEntitlementsResponseTypeDef:
        """
        Grants entitlements to an existing flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Client.grant_flow_entitlements)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediaconnect/client/#grant_flow_entitlements)
        """

    async def list_bridges(
        self, *, FilterArn: str = ..., MaxResults: int = ..., NextToken: str = ...
    ) -> ListBridgesResponseTypeDef:
        """
        Displays a list of bridges that are associated with this account and an
        optionally specified
        Arn.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Client.list_bridges)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediaconnect/client/#list_bridges)
        """

    async def list_entitlements(
        self, *, MaxResults: int = ..., NextToken: str = ...
    ) -> ListEntitlementsResponseTypeDef:
        """
        Displays a list of all entitlements that have been granted to this account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Client.list_entitlements)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediaconnect/client/#list_entitlements)
        """

    async def list_flows(
        self, *, MaxResults: int = ..., NextToken: str = ...
    ) -> ListFlowsResponseTypeDef:
        """
        Displays a list of flows that are associated with this account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Client.list_flows)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediaconnect/client/#list_flows)
        """

    async def list_gateway_instances(
        self, *, FilterArn: str = ..., MaxResults: int = ..., NextToken: str = ...
    ) -> ListGatewayInstancesResponseTypeDef:
        """
        Displays a list of instances associated with the AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Client.list_gateway_instances)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediaconnect/client/#list_gateway_instances)
        """

    async def list_gateways(
        self, *, MaxResults: int = ..., NextToken: str = ...
    ) -> ListGatewaysResponseTypeDef:
        """
        Displays a list of gateways that are associated with this account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Client.list_gateways)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediaconnect/client/#list_gateways)
        """

    async def list_offerings(
        self, *, MaxResults: int = ..., NextToken: str = ...
    ) -> ListOfferingsResponseTypeDef:
        """
        Displays a list of all offerings that are available to this account in the
        current AWS
        Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Client.list_offerings)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediaconnect/client/#list_offerings)
        """

    async def list_reservations(
        self, *, MaxResults: int = ..., NextToken: str = ...
    ) -> ListReservationsResponseTypeDef:
        """
        Displays a list of all reservations that have been purchased by this account in
        the current AWS
        Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Client.list_reservations)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediaconnect/client/#list_reservations)
        """

    async def list_tags_for_resource(
        self, *, ResourceArn: str
    ) -> ListTagsForResourceResponseTypeDef:
        """
        List all tags on an AWS Elemental MediaConnect resource See also: [AWS API
        Documentation](https://docs.aws.amazon.com/goto/WebAPI/mediaconnect-2018-11-14/ListTagsForResource).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Client.list_tags_for_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediaconnect/client/#list_tags_for_resource)
        """

    async def purchase_offering(
        self, *, OfferingArn: str, ReservationName: str, Start: str
    ) -> PurchaseOfferingResponseTypeDef:
        """
        Submits a request to purchase an offering.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Client.purchase_offering)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediaconnect/client/#purchase_offering)
        """

    async def remove_bridge_output(
        self, *, BridgeArn: str, OutputName: str
    ) -> RemoveBridgeOutputResponseTypeDef:
        """
        Removes an output from a bridge.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Client.remove_bridge_output)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediaconnect/client/#remove_bridge_output)
        """

    async def remove_bridge_source(
        self, *, BridgeArn: str, SourceName: str
    ) -> RemoveBridgeSourceResponseTypeDef:
        """
        Removes a source from a bridge.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Client.remove_bridge_source)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediaconnect/client/#remove_bridge_source)
        """

    async def remove_flow_media_stream(
        self, *, FlowArn: str, MediaStreamName: str
    ) -> RemoveFlowMediaStreamResponseTypeDef:
        """
        Removes a media stream from a flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Client.remove_flow_media_stream)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediaconnect/client/#remove_flow_media_stream)
        """

    async def remove_flow_output(
        self, *, FlowArn: str, OutputArn: str
    ) -> RemoveFlowOutputResponseTypeDef:
        """
        Removes an output from an existing flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Client.remove_flow_output)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediaconnect/client/#remove_flow_output)
        """

    async def remove_flow_source(
        self, *, FlowArn: str, SourceArn: str
    ) -> RemoveFlowSourceResponseTypeDef:
        """
        Removes a source from an existing flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Client.remove_flow_source)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediaconnect/client/#remove_flow_source)
        """

    async def remove_flow_vpc_interface(
        self, *, FlowArn: str, VpcInterfaceName: str
    ) -> RemoveFlowVpcInterfaceResponseTypeDef:
        """
        Removes a VPC Interface from an existing flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Client.remove_flow_vpc_interface)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediaconnect/client/#remove_flow_vpc_interface)
        """

    async def revoke_flow_entitlement(
        self, *, EntitlementArn: str, FlowArn: str
    ) -> RevokeFlowEntitlementResponseTypeDef:
        """
        Revokes an entitlement from a flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Client.revoke_flow_entitlement)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediaconnect/client/#revoke_flow_entitlement)
        """

    async def start_flow(self, *, FlowArn: str) -> StartFlowResponseTypeDef:
        """
        Starts a flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Client.start_flow)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediaconnect/client/#start_flow)
        """

    async def stop_flow(self, *, FlowArn: str) -> StopFlowResponseTypeDef:
        """
        Stops a flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Client.stop_flow)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediaconnect/client/#stop_flow)
        """

    async def tag_resource(
        self, *, ResourceArn: str, Tags: Mapping[str, str]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Associates the specified tags to a resource with the specified resourceArn.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Client.tag_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediaconnect/client/#tag_resource)
        """

    async def untag_resource(
        self, *, ResourceArn: str, TagKeys: Sequence[str]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes specified tags from a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Client.untag_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediaconnect/client/#untag_resource)
        """

    async def update_bridge(
        self,
        *,
        BridgeArn: str,
        EgressGatewayBridge: UpdateEgressGatewayBridgeRequestTypeDef = ...,
        IngressGatewayBridge: UpdateIngressGatewayBridgeRequestTypeDef = ...,
        SourceFailoverConfig: UpdateFailoverConfigTypeDef = ...,
    ) -> UpdateBridgeResponseTypeDef:
        """
        Updates the bridge See also: [AWS API
        Documentation](https://docs.aws.amazon.com/goto/WebAPI/mediaconnect-2018-11-14/UpdateBridge).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Client.update_bridge)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediaconnect/client/#update_bridge)
        """

    async def update_bridge_output(
        self,
        *,
        BridgeArn: str,
        OutputName: str,
        NetworkOutput: UpdateBridgeNetworkOutputRequestTypeDef = ...,
    ) -> UpdateBridgeOutputResponseTypeDef:
        """
        Updates an existing bridge output.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Client.update_bridge_output)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediaconnect/client/#update_bridge_output)
        """

    async def update_bridge_source(
        self,
        *,
        BridgeArn: str,
        SourceName: str,
        FlowSource: UpdateBridgeFlowSourceRequestTypeDef = ...,
        NetworkSource: UpdateBridgeNetworkSourceRequestTypeDef = ...,
    ) -> UpdateBridgeSourceResponseTypeDef:
        """
        Updates an existing bridge source.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Client.update_bridge_source)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediaconnect/client/#update_bridge_source)
        """

    async def update_bridge_state(
        self, *, BridgeArn: str, DesiredState: DesiredStateType
    ) -> UpdateBridgeStateResponseTypeDef:
        """
        Updates the bridge state See also: [AWS API
        Documentation](https://docs.aws.amazon.com/goto/WebAPI/mediaconnect-2018-11-14/UpdateBridgeState).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Client.update_bridge_state)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediaconnect/client/#update_bridge_state)
        """

    async def update_flow(
        self,
        *,
        FlowArn: str,
        SourceFailoverConfig: UpdateFailoverConfigTypeDef = ...,
        Maintenance: UpdateMaintenanceTypeDef = ...,
    ) -> UpdateFlowResponseTypeDef:
        """
        Updates flow See also: [AWS API
        Documentation](https://docs.aws.amazon.com/goto/WebAPI/mediaconnect-2018-11-14/UpdateFlow).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Client.update_flow)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediaconnect/client/#update_flow)
        """

    async def update_flow_entitlement(
        self,
        *,
        EntitlementArn: str,
        FlowArn: str,
        Description: str = ...,
        Encryption: UpdateEncryptionTypeDef = ...,
        EntitlementStatus: EntitlementStatusType = ...,
        Subscribers: Sequence[str] = ...,
    ) -> UpdateFlowEntitlementResponseTypeDef:
        """
        You can change an entitlement's description, subscribers, and encryption.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Client.update_flow_entitlement)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediaconnect/client/#update_flow_entitlement)
        """

    async def update_flow_media_stream(
        self,
        *,
        FlowArn: str,
        MediaStreamName: str,
        Attributes: MediaStreamAttributesRequestTypeDef = ...,
        ClockRate: int = ...,
        Description: str = ...,
        MediaStreamType: MediaStreamTypeType = ...,
        VideoFormat: str = ...,
    ) -> UpdateFlowMediaStreamResponseTypeDef:
        """
        Updates an existing media stream.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Client.update_flow_media_stream)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediaconnect/client/#update_flow_media_stream)
        """

    async def update_flow_output(
        self,
        *,
        FlowArn: str,
        OutputArn: str,
        CidrAllowList: Sequence[str] = ...,
        Description: str = ...,
        Destination: str = ...,
        Encryption: UpdateEncryptionTypeDef = ...,
        MaxLatency: int = ...,
        MediaStreamOutputConfigurations: Sequence[
            MediaStreamOutputConfigurationRequestTypeDef
        ] = ...,
        MinLatency: int = ...,
        Port: int = ...,
        Protocol: ProtocolType = ...,
        RemoteId: str = ...,
        SenderControlPort: int = ...,
        SenderIpAddress: str = ...,
        SmoothingLatency: int = ...,
        StreamId: str = ...,
        VpcInterfaceAttachment: VpcInterfaceAttachmentTypeDef = ...,
    ) -> UpdateFlowOutputResponseTypeDef:
        """
        Updates an existing flow output.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Client.update_flow_output)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediaconnect/client/#update_flow_output)
        """

    async def update_flow_source(
        self,
        *,
        FlowArn: str,
        SourceArn: str,
        Decryption: UpdateEncryptionTypeDef = ...,
        Description: str = ...,
        EntitlementArn: str = ...,
        IngestPort: int = ...,
        MaxBitrate: int = ...,
        MaxLatency: int = ...,
        MaxSyncBuffer: int = ...,
        MediaStreamSourceConfigurations: Sequence[
            MediaStreamSourceConfigurationRequestTypeDef
        ] = ...,
        MinLatency: int = ...,
        Protocol: ProtocolType = ...,
        SenderControlPort: int = ...,
        SenderIpAddress: str = ...,
        SourceListenerAddress: str = ...,
        SourceListenerPort: int = ...,
        StreamId: str = ...,
        VpcInterfaceName: str = ...,
        WhitelistCidr: str = ...,
        GatewayBridgeSource: UpdateGatewayBridgeSourceRequestTypeDef = ...,
    ) -> UpdateFlowSourceResponseTypeDef:
        """
        Updates the source of a flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Client.update_flow_source)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediaconnect/client/#update_flow_source)
        """

    async def update_gateway_instance(
        self, *, GatewayInstanceArn: str, BridgePlacement: BridgePlacementType = ...
    ) -> UpdateGatewayInstanceResponseTypeDef:
        """
        Updates the configuration of an existing Gateway Instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Client.update_gateway_instance)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediaconnect/client/#update_gateway_instance)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_bridges"]) -> ListBridgesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediaconnect/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_entitlements"]
    ) -> ListEntitlementsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediaconnect/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_flows"]) -> ListFlowsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediaconnect/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_gateway_instances"]
    ) -> ListGatewayInstancesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediaconnect/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_gateways"]) -> ListGatewaysPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediaconnect/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_offerings"]) -> ListOfferingsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediaconnect/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_reservations"]
    ) -> ListReservationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediaconnect/client/#get_paginator)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["flow_active"]) -> FlowActiveWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Client.get_waiter)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediaconnect/client/#get_waiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["flow_deleted"]) -> FlowDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Client.get_waiter)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediaconnect/client/#get_waiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["flow_standby"]) -> FlowStandbyWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Client.get_waiter)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediaconnect/client/#get_waiter)
        """

    async def __aenter__(self) -> "MediaConnectClient":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediaconnect/client/)
        """

    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> Any:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mediaconnect/client/)
        """
