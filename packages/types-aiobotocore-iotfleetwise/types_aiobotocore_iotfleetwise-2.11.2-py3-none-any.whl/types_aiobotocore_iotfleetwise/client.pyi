"""
Type annotations for iotfleetwise service client.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotfleetwise/client/)

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_iotfleetwise.client import IoTFleetWiseClient

    session = get_session()
    async with session.create_client("iotfleetwise") as client:
        client: IoTFleetWiseClient
    ```
"""

import sys
from typing import Any, Dict, Mapping, Sequence, Type, overload

from aiobotocore.client import AioBaseClient
from botocore.client import ClientMeta

from .literals import (
    CompressionType,
    DiagnosticsModeType,
    EncryptionTypeType,
    ManifestStatusType,
    SignalNodeTypeType,
    SpoolingModeType,
    UpdateCampaignActionType,
    UpdateModeType,
    VehicleAssociationBehaviorType,
)
from .paginator import (
    GetVehicleStatusPaginator,
    ListCampaignsPaginator,
    ListDecoderManifestNetworkInterfacesPaginator,
    ListDecoderManifestSignalsPaginator,
    ListDecoderManifestsPaginator,
    ListFleetsForVehiclePaginator,
    ListFleetsPaginator,
    ListModelManifestNodesPaginator,
    ListModelManifestsPaginator,
    ListSignalCatalogNodesPaginator,
    ListSignalCatalogsPaginator,
    ListVehiclesInFleetPaginator,
    ListVehiclesPaginator,
)
from .type_defs import (
    BatchCreateVehicleResponseTypeDef,
    BatchUpdateVehicleResponseTypeDef,
    CloudWatchLogDeliveryOptionsTypeDef,
    CollectionSchemeTypeDef,
    CreateCampaignResponseTypeDef,
    CreateDecoderManifestResponseTypeDef,
    CreateFleetResponseTypeDef,
    CreateModelManifestResponseTypeDef,
    CreateSignalCatalogResponseTypeDef,
    CreateVehicleRequestItemTypeDef,
    CreateVehicleResponseTypeDef,
    DataDestinationConfigTypeDef,
    DeleteCampaignResponseTypeDef,
    DeleteDecoderManifestResponseTypeDef,
    DeleteFleetResponseTypeDef,
    DeleteModelManifestResponseTypeDef,
    DeleteSignalCatalogResponseTypeDef,
    DeleteVehicleResponseTypeDef,
    FormattedVssTypeDef,
    GetCampaignResponseTypeDef,
    GetDecoderManifestResponseTypeDef,
    GetEncryptionConfigurationResponseTypeDef,
    GetFleetResponseTypeDef,
    GetLoggingOptionsResponseTypeDef,
    GetModelManifestResponseTypeDef,
    GetRegisterAccountStatusResponseTypeDef,
    GetSignalCatalogResponseTypeDef,
    GetVehicleResponseTypeDef,
    GetVehicleStatusResponseTypeDef,
    IamResourcesTypeDef,
    ImportDecoderManifestResponseTypeDef,
    ImportSignalCatalogResponseTypeDef,
    ListCampaignsResponseTypeDef,
    ListDecoderManifestNetworkInterfacesResponseTypeDef,
    ListDecoderManifestSignalsResponseTypeDef,
    ListDecoderManifestsResponseTypeDef,
    ListFleetsForVehicleResponseTypeDef,
    ListFleetsResponseTypeDef,
    ListModelManifestNodesResponseTypeDef,
    ListModelManifestsResponseTypeDef,
    ListSignalCatalogNodesResponseTypeDef,
    ListSignalCatalogsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListVehiclesInFleetResponseTypeDef,
    ListVehiclesResponseTypeDef,
    NetworkFileDefinitionTypeDef,
    NetworkInterfaceTypeDef,
    NodeTypeDef,
    PutEncryptionConfigurationResponseTypeDef,
    RegisterAccountResponseTypeDef,
    SignalDecoderTypeDef,
    SignalInformationTypeDef,
    TagTypeDef,
    TimestampTypeDef,
    TimestreamResourcesTypeDef,
    UpdateCampaignResponseTypeDef,
    UpdateDecoderManifestResponseTypeDef,
    UpdateFleetResponseTypeDef,
    UpdateModelManifestResponseTypeDef,
    UpdateSignalCatalogResponseTypeDef,
    UpdateVehicleRequestItemTypeDef,
    UpdateVehicleResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("IoTFleetWiseClient",)

class BotocoreClientError(Exception):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    DecoderManifestValidationException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    InvalidNodeException: Type[BotocoreClientError]
    InvalidSignalsException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class IoTFleetWiseClient(AioBaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise.html#IoTFleetWise.Client)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotfleetwise/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        IoTFleetWiseClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise.html#IoTFleetWise.Client.exceptions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotfleetwise/client/#exceptions)
        """

    async def associate_vehicle_fleet(self, *, vehicleName: str, fleetId: str) -> Dict[str, Any]:
        """
        Adds, or associates, a vehicle with a fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise.html#IoTFleetWise.Client.associate_vehicle_fleet)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotfleetwise/client/#associate_vehicle_fleet)
        """

    async def batch_create_vehicle(
        self, *, vehicles: Sequence[CreateVehicleRequestItemTypeDef]
    ) -> BatchCreateVehicleResponseTypeDef:
        """
        Creates a group, or batch, of vehicles.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise.html#IoTFleetWise.Client.batch_create_vehicle)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotfleetwise/client/#batch_create_vehicle)
        """

    async def batch_update_vehicle(
        self, *, vehicles: Sequence[UpdateVehicleRequestItemTypeDef]
    ) -> BatchUpdateVehicleResponseTypeDef:
        """
        Updates a group, or batch, of vehicles.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise.html#IoTFleetWise.Client.batch_update_vehicle)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotfleetwise/client/#batch_update_vehicle)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise.html#IoTFleetWise.Client.can_paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotfleetwise/client/#can_paginate)
        """

    async def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise.html#IoTFleetWise.Client.close)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotfleetwise/client/#close)
        """

    async def create_campaign(
        self,
        *,
        name: str,
        signalCatalogArn: str,
        targetArn: str,
        collectionScheme: CollectionSchemeTypeDef,
        description: str = ...,
        startTime: TimestampTypeDef = ...,
        expiryTime: TimestampTypeDef = ...,
        postTriggerCollectionDuration: int = ...,
        diagnosticsMode: DiagnosticsModeType = ...,
        spoolingMode: SpoolingModeType = ...,
        compression: CompressionType = ...,
        priority: int = ...,
        signalsToCollect: Sequence[SignalInformationTypeDef] = ...,
        dataExtraDimensions: Sequence[str] = ...,
        tags: Sequence[TagTypeDef] = ...,
        dataDestinationConfigs: Sequence[DataDestinationConfigTypeDef] = ...,
    ) -> CreateCampaignResponseTypeDef:
        """
        Creates an orchestration of data collection rules.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise.html#IoTFleetWise.Client.create_campaign)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotfleetwise/client/#create_campaign)
        """

    async def create_decoder_manifest(
        self,
        *,
        name: str,
        modelManifestArn: str,
        description: str = ...,
        signalDecoders: Sequence[SignalDecoderTypeDef] = ...,
        networkInterfaces: Sequence[NetworkInterfaceTypeDef] = ...,
        tags: Sequence[TagTypeDef] = ...,
    ) -> CreateDecoderManifestResponseTypeDef:
        """
        Creates the decoder manifest associated with a model manifest.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise.html#IoTFleetWise.Client.create_decoder_manifest)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotfleetwise/client/#create_decoder_manifest)
        """

    async def create_fleet(
        self,
        *,
        fleetId: str,
        signalCatalogArn: str,
        description: str = ...,
        tags: Sequence[TagTypeDef] = ...,
    ) -> CreateFleetResponseTypeDef:
        """
        Creates a fleet that represents a group of vehicles.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise.html#IoTFleetWise.Client.create_fleet)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotfleetwise/client/#create_fleet)
        """

    async def create_model_manifest(
        self,
        *,
        name: str,
        nodes: Sequence[str],
        signalCatalogArn: str,
        description: str = ...,
        tags: Sequence[TagTypeDef] = ...,
    ) -> CreateModelManifestResponseTypeDef:
        """
        Creates a vehicle model (model manifest) that specifies signals (attributes,
        branches, sensors, and
        actuators).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise.html#IoTFleetWise.Client.create_model_manifest)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotfleetwise/client/#create_model_manifest)
        """

    async def create_signal_catalog(
        self,
        *,
        name: str,
        description: str = ...,
        nodes: Sequence[NodeTypeDef] = ...,
        tags: Sequence[TagTypeDef] = ...,
    ) -> CreateSignalCatalogResponseTypeDef:
        """
        Creates a collection of standardized signals that can be reused to create
        vehicle
        models.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise.html#IoTFleetWise.Client.create_signal_catalog)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotfleetwise/client/#create_signal_catalog)
        """

    async def create_vehicle(
        self,
        *,
        vehicleName: str,
        modelManifestArn: str,
        decoderManifestArn: str,
        attributes: Mapping[str, str] = ...,
        associationBehavior: VehicleAssociationBehaviorType = ...,
        tags: Sequence[TagTypeDef] = ...,
    ) -> CreateVehicleResponseTypeDef:
        """
        Creates a vehicle, which is an instance of a vehicle model (model manifest).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise.html#IoTFleetWise.Client.create_vehicle)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotfleetwise/client/#create_vehicle)
        """

    async def delete_campaign(self, *, name: str) -> DeleteCampaignResponseTypeDef:
        """
        Deletes a data collection campaign.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise.html#IoTFleetWise.Client.delete_campaign)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotfleetwise/client/#delete_campaign)
        """

    async def delete_decoder_manifest(self, *, name: str) -> DeleteDecoderManifestResponseTypeDef:
        """
        Deletes a decoder manifest.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise.html#IoTFleetWise.Client.delete_decoder_manifest)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotfleetwise/client/#delete_decoder_manifest)
        """

    async def delete_fleet(self, *, fleetId: str) -> DeleteFleetResponseTypeDef:
        """
        Deletes a fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise.html#IoTFleetWise.Client.delete_fleet)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotfleetwise/client/#delete_fleet)
        """

    async def delete_model_manifest(self, *, name: str) -> DeleteModelManifestResponseTypeDef:
        """
        Deletes a vehicle model (model manifest).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise.html#IoTFleetWise.Client.delete_model_manifest)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotfleetwise/client/#delete_model_manifest)
        """

    async def delete_signal_catalog(self, *, name: str) -> DeleteSignalCatalogResponseTypeDef:
        """
        Deletes a signal catalog.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise.html#IoTFleetWise.Client.delete_signal_catalog)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotfleetwise/client/#delete_signal_catalog)
        """

    async def delete_vehicle(self, *, vehicleName: str) -> DeleteVehicleResponseTypeDef:
        """
        Deletes a vehicle and removes it from any campaigns.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise.html#IoTFleetWise.Client.delete_vehicle)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotfleetwise/client/#delete_vehicle)
        """

    async def disassociate_vehicle_fleet(self, *, vehicleName: str, fleetId: str) -> Dict[str, Any]:
        """
        Removes, or disassociates, a vehicle from a fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise.html#IoTFleetWise.Client.disassociate_vehicle_fleet)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotfleetwise/client/#disassociate_vehicle_fleet)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise.html#IoTFleetWise.Client.generate_presigned_url)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotfleetwise/client/#generate_presigned_url)
        """

    async def get_campaign(self, *, name: str) -> GetCampaignResponseTypeDef:
        """
        Retrieves information about a campaign.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise.html#IoTFleetWise.Client.get_campaign)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotfleetwise/client/#get_campaign)
        """

    async def get_decoder_manifest(self, *, name: str) -> GetDecoderManifestResponseTypeDef:
        """
        Retrieves information about a created decoder manifest.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise.html#IoTFleetWise.Client.get_decoder_manifest)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotfleetwise/client/#get_decoder_manifest)
        """

    async def get_encryption_configuration(self) -> GetEncryptionConfigurationResponseTypeDef:
        """
        Retrieves the encryption configuration for resources and data in Amazon Web
        Services IoT
        FleetWise.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise.html#IoTFleetWise.Client.get_encryption_configuration)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotfleetwise/client/#get_encryption_configuration)
        """

    async def get_fleet(self, *, fleetId: str) -> GetFleetResponseTypeDef:
        """
        Retrieves information about a fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise.html#IoTFleetWise.Client.get_fleet)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotfleetwise/client/#get_fleet)
        """

    async def get_logging_options(self) -> GetLoggingOptionsResponseTypeDef:
        """
        Retrieves the logging options.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise.html#IoTFleetWise.Client.get_logging_options)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotfleetwise/client/#get_logging_options)
        """

    async def get_model_manifest(self, *, name: str) -> GetModelManifestResponseTypeDef:
        """
        Retrieves information about a vehicle model (model manifest).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise.html#IoTFleetWise.Client.get_model_manifest)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotfleetwise/client/#get_model_manifest)
        """

    async def get_register_account_status(self) -> GetRegisterAccountStatusResponseTypeDef:
        """
        Retrieves information about the status of registering your Amazon Web Services
        account, IAM, and Amazon Timestream resources so that Amazon Web Services IoT
        FleetWise can transfer your vehicle data to the Amazon Web Services
        Cloud.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise.html#IoTFleetWise.Client.get_register_account_status)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotfleetwise/client/#get_register_account_status)
        """

    async def get_signal_catalog(self, *, name: str) -> GetSignalCatalogResponseTypeDef:
        """
        Retrieves information about a signal catalog.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise.html#IoTFleetWise.Client.get_signal_catalog)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotfleetwise/client/#get_signal_catalog)
        """

    async def get_vehicle(self, *, vehicleName: str) -> GetVehicleResponseTypeDef:
        """
        Retrieves information about a vehicle.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise.html#IoTFleetWise.Client.get_vehicle)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotfleetwise/client/#get_vehicle)
        """

    async def get_vehicle_status(
        self, *, vehicleName: str, nextToken: str = ..., maxResults: int = ...
    ) -> GetVehicleStatusResponseTypeDef:
        """
        Retrieves information about the status of a vehicle with any associated
        campaigns.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise.html#IoTFleetWise.Client.get_vehicle_status)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotfleetwise/client/#get_vehicle_status)
        """

    async def import_decoder_manifest(
        self, *, name: str, networkFileDefinitions: Sequence[NetworkFileDefinitionTypeDef]
    ) -> ImportDecoderManifestResponseTypeDef:
        """
        Creates a decoder manifest using your existing CAN DBC file from your local
        device.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise.html#IoTFleetWise.Client.import_decoder_manifest)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotfleetwise/client/#import_decoder_manifest)
        """

    async def import_signal_catalog(
        self,
        *,
        name: str,
        description: str = ...,
        vss: FormattedVssTypeDef = ...,
        tags: Sequence[TagTypeDef] = ...,
    ) -> ImportSignalCatalogResponseTypeDef:
        """
        Creates a signal catalog using your existing VSS formatted content from your
        local
        device.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise.html#IoTFleetWise.Client.import_signal_catalog)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotfleetwise/client/#import_signal_catalog)
        """

    async def list_campaigns(
        self, *, nextToken: str = ..., maxResults: int = ..., status: str = ...
    ) -> ListCampaignsResponseTypeDef:
        """
        Lists information about created campaigns.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise.html#IoTFleetWise.Client.list_campaigns)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotfleetwise/client/#list_campaigns)
        """

    async def list_decoder_manifest_network_interfaces(
        self, *, name: str, nextToken: str = ..., maxResults: int = ...
    ) -> ListDecoderManifestNetworkInterfacesResponseTypeDef:
        """
        Lists the network interfaces specified in a decoder manifest.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise.html#IoTFleetWise.Client.list_decoder_manifest_network_interfaces)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotfleetwise/client/#list_decoder_manifest_network_interfaces)
        """

    async def list_decoder_manifest_signals(
        self, *, name: str, nextToken: str = ..., maxResults: int = ...
    ) -> ListDecoderManifestSignalsResponseTypeDef:
        """
        A list of information about signal decoders specified in a decoder manifest.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise.html#IoTFleetWise.Client.list_decoder_manifest_signals)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotfleetwise/client/#list_decoder_manifest_signals)
        """

    async def list_decoder_manifests(
        self, *, modelManifestArn: str = ..., nextToken: str = ..., maxResults: int = ...
    ) -> ListDecoderManifestsResponseTypeDef:
        """
        Lists decoder manifests.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise.html#IoTFleetWise.Client.list_decoder_manifests)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotfleetwise/client/#list_decoder_manifests)
        """

    async def list_fleets(
        self, *, nextToken: str = ..., maxResults: int = ...
    ) -> ListFleetsResponseTypeDef:
        """
        Retrieves information for each created fleet in an Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise.html#IoTFleetWise.Client.list_fleets)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotfleetwise/client/#list_fleets)
        """

    async def list_fleets_for_vehicle(
        self, *, vehicleName: str, nextToken: str = ..., maxResults: int = ...
    ) -> ListFleetsForVehicleResponseTypeDef:
        """
        Retrieves a list of IDs for all fleets that the vehicle is associated with.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise.html#IoTFleetWise.Client.list_fleets_for_vehicle)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotfleetwise/client/#list_fleets_for_vehicle)
        """

    async def list_model_manifest_nodes(
        self, *, name: str, nextToken: str = ..., maxResults: int = ...
    ) -> ListModelManifestNodesResponseTypeDef:
        """
        Lists information about nodes specified in a vehicle model (model manifest).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise.html#IoTFleetWise.Client.list_model_manifest_nodes)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotfleetwise/client/#list_model_manifest_nodes)
        """

    async def list_model_manifests(
        self, *, signalCatalogArn: str = ..., nextToken: str = ..., maxResults: int = ...
    ) -> ListModelManifestsResponseTypeDef:
        """
        Retrieves a list of vehicle models (model manifests).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise.html#IoTFleetWise.Client.list_model_manifests)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotfleetwise/client/#list_model_manifests)
        """

    async def list_signal_catalog_nodes(
        self,
        *,
        name: str,
        nextToken: str = ...,
        maxResults: int = ...,
        signalNodeType: SignalNodeTypeType = ...,
    ) -> ListSignalCatalogNodesResponseTypeDef:
        """
        Lists of information about the signals (nodes) specified in a signal catalog.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise.html#IoTFleetWise.Client.list_signal_catalog_nodes)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotfleetwise/client/#list_signal_catalog_nodes)
        """

    async def list_signal_catalogs(
        self, *, nextToken: str = ..., maxResults: int = ...
    ) -> ListSignalCatalogsResponseTypeDef:
        """
        Lists all the created signal catalogs in an Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise.html#IoTFleetWise.Client.list_signal_catalogs)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotfleetwise/client/#list_signal_catalogs)
        """

    async def list_tags_for_resource(
        self, *, ResourceARN: str
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists the tags (metadata) you have assigned to the resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise.html#IoTFleetWise.Client.list_tags_for_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotfleetwise/client/#list_tags_for_resource)
        """

    async def list_vehicles(
        self, *, modelManifestArn: str = ..., nextToken: str = ..., maxResults: int = ...
    ) -> ListVehiclesResponseTypeDef:
        """
        Retrieves a list of summaries of created vehicles.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise.html#IoTFleetWise.Client.list_vehicles)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotfleetwise/client/#list_vehicles)
        """

    async def list_vehicles_in_fleet(
        self, *, fleetId: str, nextToken: str = ..., maxResults: int = ...
    ) -> ListVehiclesInFleetResponseTypeDef:
        """
        Retrieves a list of summaries of all vehicles associated with a fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise.html#IoTFleetWise.Client.list_vehicles_in_fleet)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotfleetwise/client/#list_vehicles_in_fleet)
        """

    async def put_encryption_configuration(
        self, *, encryptionType: EncryptionTypeType, kmsKeyId: str = ...
    ) -> PutEncryptionConfigurationResponseTypeDef:
        """
        Creates or updates the encryption configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise.html#IoTFleetWise.Client.put_encryption_configuration)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotfleetwise/client/#put_encryption_configuration)
        """

    async def put_logging_options(
        self, *, cloudWatchLogDelivery: CloudWatchLogDeliveryOptionsTypeDef
    ) -> Dict[str, Any]:
        """
        Creates or updates the logging option.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise.html#IoTFleetWise.Client.put_logging_options)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotfleetwise/client/#put_logging_options)
        """

    async def register_account(
        self,
        *,
        timestreamResources: TimestreamResourcesTypeDef = ...,
        iamResources: IamResourcesTypeDef = ...,
    ) -> RegisterAccountResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise.html#IoTFleetWise.Client.register_account)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotfleetwise/client/#register_account)
        """

    async def tag_resource(self, *, ResourceARN: str, Tags: Sequence[TagTypeDef]) -> Dict[str, Any]:
        """
        Adds to or modifies the tags of the given resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise.html#IoTFleetWise.Client.tag_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotfleetwise/client/#tag_resource)
        """

    async def untag_resource(self, *, ResourceARN: str, TagKeys: Sequence[str]) -> Dict[str, Any]:
        """
        Removes the given tags (metadata) from the resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise.html#IoTFleetWise.Client.untag_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotfleetwise/client/#untag_resource)
        """

    async def update_campaign(
        self,
        *,
        name: str,
        action: UpdateCampaignActionType,
        description: str = ...,
        dataExtraDimensions: Sequence[str] = ...,
    ) -> UpdateCampaignResponseTypeDef:
        """
        Updates a campaign.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise.html#IoTFleetWise.Client.update_campaign)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotfleetwise/client/#update_campaign)
        """

    async def update_decoder_manifest(
        self,
        *,
        name: str,
        description: str = ...,
        signalDecodersToAdd: Sequence[SignalDecoderTypeDef] = ...,
        signalDecodersToUpdate: Sequence[SignalDecoderTypeDef] = ...,
        signalDecodersToRemove: Sequence[str] = ...,
        networkInterfacesToAdd: Sequence[NetworkInterfaceTypeDef] = ...,
        networkInterfacesToUpdate: Sequence[NetworkInterfaceTypeDef] = ...,
        networkInterfacesToRemove: Sequence[str] = ...,
        status: ManifestStatusType = ...,
    ) -> UpdateDecoderManifestResponseTypeDef:
        """
        Updates a decoder manifest.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise.html#IoTFleetWise.Client.update_decoder_manifest)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotfleetwise/client/#update_decoder_manifest)
        """

    async def update_fleet(
        self, *, fleetId: str, description: str = ...
    ) -> UpdateFleetResponseTypeDef:
        """
        Updates the description of an existing fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise.html#IoTFleetWise.Client.update_fleet)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotfleetwise/client/#update_fleet)
        """

    async def update_model_manifest(
        self,
        *,
        name: str,
        description: str = ...,
        nodesToAdd: Sequence[str] = ...,
        nodesToRemove: Sequence[str] = ...,
        status: ManifestStatusType = ...,
    ) -> UpdateModelManifestResponseTypeDef:
        """
        Updates a vehicle model (model manifest).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise.html#IoTFleetWise.Client.update_model_manifest)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotfleetwise/client/#update_model_manifest)
        """

    async def update_signal_catalog(
        self,
        *,
        name: str,
        description: str = ...,
        nodesToAdd: Sequence[NodeTypeDef] = ...,
        nodesToUpdate: Sequence[NodeTypeDef] = ...,
        nodesToRemove: Sequence[str] = ...,
    ) -> UpdateSignalCatalogResponseTypeDef:
        """
        Updates a signal catalog.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise.html#IoTFleetWise.Client.update_signal_catalog)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotfleetwise/client/#update_signal_catalog)
        """

    async def update_vehicle(
        self,
        *,
        vehicleName: str,
        modelManifestArn: str = ...,
        decoderManifestArn: str = ...,
        attributes: Mapping[str, str] = ...,
        attributeUpdateMode: UpdateModeType = ...,
    ) -> UpdateVehicleResponseTypeDef:
        """
        Updates a vehicle.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise.html#IoTFleetWise.Client.update_vehicle)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotfleetwise/client/#update_vehicle)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_vehicle_status"]
    ) -> GetVehicleStatusPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise.html#IoTFleetWise.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotfleetwise/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_campaigns"]) -> ListCampaignsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise.html#IoTFleetWise.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotfleetwise/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_decoder_manifest_network_interfaces"]
    ) -> ListDecoderManifestNetworkInterfacesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise.html#IoTFleetWise.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotfleetwise/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_decoder_manifest_signals"]
    ) -> ListDecoderManifestSignalsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise.html#IoTFleetWise.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotfleetwise/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_decoder_manifests"]
    ) -> ListDecoderManifestsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise.html#IoTFleetWise.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotfleetwise/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_fleets"]) -> ListFleetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise.html#IoTFleetWise.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotfleetwise/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_fleets_for_vehicle"]
    ) -> ListFleetsForVehiclePaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise.html#IoTFleetWise.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotfleetwise/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_model_manifest_nodes"]
    ) -> ListModelManifestNodesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise.html#IoTFleetWise.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotfleetwise/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_model_manifests"]
    ) -> ListModelManifestsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise.html#IoTFleetWise.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotfleetwise/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_signal_catalog_nodes"]
    ) -> ListSignalCatalogNodesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise.html#IoTFleetWise.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotfleetwise/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_signal_catalogs"]
    ) -> ListSignalCatalogsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise.html#IoTFleetWise.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotfleetwise/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_vehicles"]) -> ListVehiclesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise.html#IoTFleetWise.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotfleetwise/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_vehicles_in_fleet"]
    ) -> ListVehiclesInFleetPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise.html#IoTFleetWise.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotfleetwise/client/#get_paginator)
        """

    async def __aenter__(self) -> "IoTFleetWiseClient":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise.html#IoTFleetWise.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotfleetwise/client/)
        """

    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> Any:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise.html#IoTFleetWise.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotfleetwise/client/)
        """
