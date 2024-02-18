"""
Type annotations for dms service client.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/)

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_dms.client import DatabaseMigrationServiceClient

    session = get_session()
    async with session.create_client("dms") as client:
        client: DatabaseMigrationServiceClient
    ```
"""

import sys
from typing import Any, Dict, Mapping, Sequence, Type, overload

from aiobotocore.client import AioBaseClient
from botocore.client import ClientMeta

from .literals import (
    AssessmentReportTypeType,
    DmsSslModeValueType,
    MigrationTypeValueType,
    OriginTypeValueType,
    ReloadOptionValueType,
    ReplicationEndpointTypeValueType,
    StartReplicationTaskTypeValueType,
)
from .paginator import (
    DescribeCertificatesPaginator,
    DescribeConnectionsPaginator,
    DescribeEndpointsPaginator,
    DescribeEndpointTypesPaginator,
    DescribeEventsPaginator,
    DescribeEventSubscriptionsPaginator,
    DescribeOrderableReplicationInstancesPaginator,
    DescribeReplicationInstancesPaginator,
    DescribeReplicationSubnetGroupsPaginator,
    DescribeReplicationTaskAssessmentResultsPaginator,
    DescribeReplicationTasksPaginator,
    DescribeSchemasPaginator,
    DescribeTableStatisticsPaginator,
)
from .type_defs import (
    ApplyPendingMaintenanceActionResponseTypeDef,
    BatchStartRecommendationsResponseTypeDef,
    BlobTypeDef,
    CancelReplicationTaskAssessmentRunResponseTypeDef,
    ComputeConfigTypeDef,
    CreateDataProviderResponseTypeDef,
    CreateEndpointResponseTypeDef,
    CreateEventSubscriptionResponseTypeDef,
    CreateFleetAdvisorCollectorResponseTypeDef,
    CreateInstanceProfileResponseTypeDef,
    CreateMigrationProjectResponseTypeDef,
    CreateReplicationConfigResponseTypeDef,
    CreateReplicationInstanceResponseTypeDef,
    CreateReplicationSubnetGroupResponseTypeDef,
    CreateReplicationTaskResponseTypeDef,
    DataProviderDescriptorDefinitionTypeDef,
    DataProviderSettingsTypeDef,
    DeleteCertificateResponseTypeDef,
    DeleteConnectionResponseTypeDef,
    DeleteDataProviderResponseTypeDef,
    DeleteEndpointResponseTypeDef,
    DeleteEventSubscriptionResponseTypeDef,
    DeleteFleetAdvisorDatabasesResponseTypeDef,
    DeleteInstanceProfileResponseTypeDef,
    DeleteMigrationProjectResponseTypeDef,
    DeleteReplicationConfigResponseTypeDef,
    DeleteReplicationInstanceResponseTypeDef,
    DeleteReplicationTaskAssessmentRunResponseTypeDef,
    DeleteReplicationTaskResponseTypeDef,
    DescribeAccountAttributesResponseTypeDef,
    DescribeApplicableIndividualAssessmentsResponseTypeDef,
    DescribeCertificatesResponseTypeDef,
    DescribeConnectionsResponseTypeDef,
    DescribeConversionConfigurationResponseTypeDef,
    DescribeDataProvidersResponseTypeDef,
    DescribeEndpointSettingsResponseTypeDef,
    DescribeEndpointsResponseTypeDef,
    DescribeEndpointTypesResponseTypeDef,
    DescribeEngineVersionsResponseTypeDef,
    DescribeEventCategoriesResponseTypeDef,
    DescribeEventsResponseTypeDef,
    DescribeEventSubscriptionsResponseTypeDef,
    DescribeExtensionPackAssociationsResponseTypeDef,
    DescribeFleetAdvisorCollectorsResponseTypeDef,
    DescribeFleetAdvisorDatabasesResponseTypeDef,
    DescribeFleetAdvisorLsaAnalysisResponseTypeDef,
    DescribeFleetAdvisorSchemaObjectSummaryResponseTypeDef,
    DescribeFleetAdvisorSchemasResponseTypeDef,
    DescribeInstanceProfilesResponseTypeDef,
    DescribeMetadataModelAssessmentsResponseTypeDef,
    DescribeMetadataModelConversionsResponseTypeDef,
    DescribeMetadataModelExportsAsScriptResponseTypeDef,
    DescribeMetadataModelExportsToTargetResponseTypeDef,
    DescribeMetadataModelImportsResponseTypeDef,
    DescribeMigrationProjectsResponseTypeDef,
    DescribeOrderableReplicationInstancesResponseTypeDef,
    DescribePendingMaintenanceActionsResponseTypeDef,
    DescribeRecommendationLimitationsResponseTypeDef,
    DescribeRecommendationsResponseTypeDef,
    DescribeRefreshSchemasStatusResponseTypeDef,
    DescribeReplicationConfigsResponseTypeDef,
    DescribeReplicationInstancesResponseTypeDef,
    DescribeReplicationInstanceTaskLogsResponseTypeDef,
    DescribeReplicationsResponseTypeDef,
    DescribeReplicationSubnetGroupsResponseTypeDef,
    DescribeReplicationTableStatisticsResponseTypeDef,
    DescribeReplicationTaskAssessmentResultsResponseTypeDef,
    DescribeReplicationTaskAssessmentRunsResponseTypeDef,
    DescribeReplicationTaskIndividualAssessmentsResponseTypeDef,
    DescribeReplicationTasksResponseTypeDef,
    DescribeSchemasResponseTypeDef,
    DescribeTableStatisticsResponseTypeDef,
    DmsTransferSettingsTypeDef,
    DocDbSettingsTypeDef,
    DynamoDbSettingsTypeDef,
    ElasticsearchSettingsTypeDef,
    EmptyResponseMetadataTypeDef,
    ExportMetadataModelAssessmentResponseTypeDef,
    FilterTypeDef,
    GcpMySQLSettingsTypeDef,
    IBMDb2SettingsTypeDef,
    ImportCertificateResponseTypeDef,
    KafkaSettingsTypeDef,
    KinesisSettingsTypeDef,
    ListTagsForResourceResponseTypeDef,
    MicrosoftSQLServerSettingsTypeDef,
    ModifyConversionConfigurationResponseTypeDef,
    ModifyDataProviderResponseTypeDef,
    ModifyEndpointResponseTypeDef,
    ModifyEventSubscriptionResponseTypeDef,
    ModifyInstanceProfileResponseTypeDef,
    ModifyMigrationProjectResponseTypeDef,
    ModifyReplicationConfigResponseTypeDef,
    ModifyReplicationInstanceResponseTypeDef,
    ModifyReplicationSubnetGroupResponseTypeDef,
    ModifyReplicationTaskResponseTypeDef,
    MongoDbSettingsTypeDef,
    MoveReplicationTaskResponseTypeDef,
    MySQLSettingsTypeDef,
    NeptuneSettingsTypeDef,
    OracleSettingsTypeDef,
    PostgreSQLSettingsTypeDef,
    RebootReplicationInstanceResponseTypeDef,
    RecommendationSettingsTypeDef,
    RedisSettingsTypeDef,
    RedshiftSettingsTypeDef,
    RefreshSchemasResponseTypeDef,
    ReloadReplicationTablesResponseTypeDef,
    ReloadTablesResponseTypeDef,
    RunFleetAdvisorLsaAnalysisResponseTypeDef,
    S3SettingsTypeDef,
    SCApplicationAttributesTypeDef,
    StartExtensionPackAssociationResponseTypeDef,
    StartMetadataModelAssessmentResponseTypeDef,
    StartMetadataModelConversionResponseTypeDef,
    StartMetadataModelExportAsScriptResponseTypeDef,
    StartMetadataModelExportToTargetResponseTypeDef,
    StartMetadataModelImportResponseTypeDef,
    StartRecommendationsRequestEntryTypeDef,
    StartReplicationResponseTypeDef,
    StartReplicationTaskAssessmentResponseTypeDef,
    StartReplicationTaskAssessmentRunResponseTypeDef,
    StartReplicationTaskResponseTypeDef,
    StopReplicationResponseTypeDef,
    StopReplicationTaskResponseTypeDef,
    SybaseSettingsTypeDef,
    TableToReloadTypeDef,
    TagTypeDef,
    TestConnectionResponseTypeDef,
    TimestampTypeDef,
    TimestreamSettingsTypeDef,
    UpdateSubscriptionsToEventBridgeResponseTypeDef,
)
from .waiter import (
    EndpointDeletedWaiter,
    ReplicationInstanceAvailableWaiter,
    ReplicationInstanceDeletedWaiter,
    ReplicationTaskDeletedWaiter,
    ReplicationTaskReadyWaiter,
    ReplicationTaskRunningWaiter,
    ReplicationTaskStoppedWaiter,
    TestConnectionSucceedsWaiter,
)

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("DatabaseMigrationServiceClient",)


class BotocoreClientError(Exception):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedFault: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    CollectorNotFoundFault: Type[BotocoreClientError]
    InsufficientResourceCapacityFault: Type[BotocoreClientError]
    InvalidCertificateFault: Type[BotocoreClientError]
    InvalidOperationFault: Type[BotocoreClientError]
    InvalidResourceStateFault: Type[BotocoreClientError]
    InvalidSubnet: Type[BotocoreClientError]
    KMSAccessDeniedFault: Type[BotocoreClientError]
    KMSDisabledFault: Type[BotocoreClientError]
    KMSFault: Type[BotocoreClientError]
    KMSInvalidStateFault: Type[BotocoreClientError]
    KMSKeyNotAccessibleFault: Type[BotocoreClientError]
    KMSNotFoundFault: Type[BotocoreClientError]
    KMSThrottlingFault: Type[BotocoreClientError]
    ReplicationSubnetGroupDoesNotCoverEnoughAZs: Type[BotocoreClientError]
    ResourceAlreadyExistsFault: Type[BotocoreClientError]
    ResourceNotFoundFault: Type[BotocoreClientError]
    ResourceQuotaExceededFault: Type[BotocoreClientError]
    S3AccessDeniedFault: Type[BotocoreClientError]
    S3ResourceNotFoundFault: Type[BotocoreClientError]
    SNSInvalidTopicFault: Type[BotocoreClientError]
    SNSNoAuthorizationFault: Type[BotocoreClientError]
    StorageQuotaExceededFault: Type[BotocoreClientError]
    SubnetAlreadyInUse: Type[BotocoreClientError]
    UpgradeDependencyFailureFault: Type[BotocoreClientError]


class DatabaseMigrationServiceClient(AioBaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        DatabaseMigrationServiceClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.exceptions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#exceptions)
        """

    async def add_tags_to_resource(
        self, *, ResourceArn: str, Tags: Sequence[TagTypeDef]
    ) -> Dict[str, Any]:
        """
        Adds metadata tags to an DMS resource, including replication instance,
        endpoint, subnet group, and migration
        task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.add_tags_to_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#add_tags_to_resource)
        """

    async def apply_pending_maintenance_action(
        self, *, ReplicationInstanceArn: str, ApplyAction: str, OptInType: str
    ) -> ApplyPendingMaintenanceActionResponseTypeDef:
        """
        Applies a pending maintenance action to a resource (for example, to a
        replication
        instance).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.apply_pending_maintenance_action)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#apply_pending_maintenance_action)
        """

    async def batch_start_recommendations(
        self, *, Data: Sequence[StartRecommendationsRequestEntryTypeDef] = ...
    ) -> BatchStartRecommendationsResponseTypeDef:
        """
        Starts the analysis of up to 20 source databases to recommend target engines
        for each source
        database.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.batch_start_recommendations)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#batch_start_recommendations)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.can_paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#can_paginate)
        """

    async def cancel_replication_task_assessment_run(
        self, *, ReplicationTaskAssessmentRunArn: str
    ) -> CancelReplicationTaskAssessmentRunResponseTypeDef:
        """
        Cancels a single premigration assessment run.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.cancel_replication_task_assessment_run)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#cancel_replication_task_assessment_run)
        """

    async def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.close)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#close)
        """

    async def create_data_provider(
        self,
        *,
        Engine: str,
        Settings: DataProviderSettingsTypeDef,
        DataProviderName: str = ...,
        Description: str = ...,
        Tags: Sequence[TagTypeDef] = ...,
    ) -> CreateDataProviderResponseTypeDef:
        """
        Creates a data provider using the provided settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.create_data_provider)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#create_data_provider)
        """

    async def create_endpoint(
        self,
        *,
        EndpointIdentifier: str,
        EndpointType: ReplicationEndpointTypeValueType,
        EngineName: str,
        Username: str = ...,
        Password: str = ...,
        ServerName: str = ...,
        Port: int = ...,
        DatabaseName: str = ...,
        ExtraConnectionAttributes: str = ...,
        KmsKeyId: str = ...,
        Tags: Sequence[TagTypeDef] = ...,
        CertificateArn: str = ...,
        SslMode: DmsSslModeValueType = ...,
        ServiceAccessRoleArn: str = ...,
        ExternalTableDefinition: str = ...,
        DynamoDbSettings: DynamoDbSettingsTypeDef = ...,
        S3Settings: S3SettingsTypeDef = ...,
        DmsTransferSettings: DmsTransferSettingsTypeDef = ...,
        MongoDbSettings: MongoDbSettingsTypeDef = ...,
        KinesisSettings: KinesisSettingsTypeDef = ...,
        KafkaSettings: KafkaSettingsTypeDef = ...,
        ElasticsearchSettings: ElasticsearchSettingsTypeDef = ...,
        NeptuneSettings: NeptuneSettingsTypeDef = ...,
        RedshiftSettings: RedshiftSettingsTypeDef = ...,
        PostgreSQLSettings: PostgreSQLSettingsTypeDef = ...,
        MySQLSettings: MySQLSettingsTypeDef = ...,
        OracleSettings: OracleSettingsTypeDef = ...,
        SybaseSettings: SybaseSettingsTypeDef = ...,
        MicrosoftSQLServerSettings: MicrosoftSQLServerSettingsTypeDef = ...,
        IBMDb2Settings: IBMDb2SettingsTypeDef = ...,
        ResourceIdentifier: str = ...,
        DocDbSettings: DocDbSettingsTypeDef = ...,
        RedisSettings: RedisSettingsTypeDef = ...,
        GcpMySQLSettings: GcpMySQLSettingsTypeDef = ...,
        TimestreamSettings: TimestreamSettingsTypeDef = ...,
    ) -> CreateEndpointResponseTypeDef:
        """
        Creates an endpoint using the provided settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.create_endpoint)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#create_endpoint)
        """

    async def create_event_subscription(
        self,
        *,
        SubscriptionName: str,
        SnsTopicArn: str,
        SourceType: str = ...,
        EventCategories: Sequence[str] = ...,
        SourceIds: Sequence[str] = ...,
        Enabled: bool = ...,
        Tags: Sequence[TagTypeDef] = ...,
    ) -> CreateEventSubscriptionResponseTypeDef:
        """
        Creates an DMS event notification subscription.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.create_event_subscription)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#create_event_subscription)
        """

    async def create_fleet_advisor_collector(
        self,
        *,
        CollectorName: str,
        ServiceAccessRoleArn: str,
        S3BucketName: str,
        Description: str = ...,
    ) -> CreateFleetAdvisorCollectorResponseTypeDef:
        """
        Creates a Fleet Advisor collector using the specified parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.create_fleet_advisor_collector)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#create_fleet_advisor_collector)
        """

    async def create_instance_profile(
        self,
        *,
        AvailabilityZone: str = ...,
        KmsKeyArn: str = ...,
        PubliclyAccessible: bool = ...,
        Tags: Sequence[TagTypeDef] = ...,
        NetworkType: str = ...,
        InstanceProfileName: str = ...,
        Description: str = ...,
        SubnetGroupIdentifier: str = ...,
        VpcSecurityGroups: Sequence[str] = ...,
    ) -> CreateInstanceProfileResponseTypeDef:
        """
        Creates the instance profile using the specified parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.create_instance_profile)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#create_instance_profile)
        """

    async def create_migration_project(
        self,
        *,
        SourceDataProviderDescriptors: Sequence[DataProviderDescriptorDefinitionTypeDef],
        TargetDataProviderDescriptors: Sequence[DataProviderDescriptorDefinitionTypeDef],
        InstanceProfileIdentifier: str,
        MigrationProjectName: str = ...,
        TransformationRules: str = ...,
        Description: str = ...,
        Tags: Sequence[TagTypeDef] = ...,
        SchemaConversionApplicationAttributes: SCApplicationAttributesTypeDef = ...,
    ) -> CreateMigrationProjectResponseTypeDef:
        """
        Creates the migration project using the specified parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.create_migration_project)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#create_migration_project)
        """

    async def create_replication_config(
        self,
        *,
        ReplicationConfigIdentifier: str,
        SourceEndpointArn: str,
        TargetEndpointArn: str,
        ComputeConfig: ComputeConfigTypeDef,
        ReplicationType: MigrationTypeValueType,
        TableMappings: str,
        ReplicationSettings: str = ...,
        SupplementalSettings: str = ...,
        ResourceIdentifier: str = ...,
        Tags: Sequence[TagTypeDef] = ...,
    ) -> CreateReplicationConfigResponseTypeDef:
        """
        Creates a configuration that you can later provide to configure and start an
        DMS Serverless
        replication.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.create_replication_config)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#create_replication_config)
        """

    async def create_replication_instance(
        self,
        *,
        ReplicationInstanceIdentifier: str,
        ReplicationInstanceClass: str,
        AllocatedStorage: int = ...,
        VpcSecurityGroupIds: Sequence[str] = ...,
        AvailabilityZone: str = ...,
        ReplicationSubnetGroupIdentifier: str = ...,
        PreferredMaintenanceWindow: str = ...,
        MultiAZ: bool = ...,
        EngineVersion: str = ...,
        AutoMinorVersionUpgrade: bool = ...,
        Tags: Sequence[TagTypeDef] = ...,
        KmsKeyId: str = ...,
        PubliclyAccessible: bool = ...,
        DnsNameServers: str = ...,
        ResourceIdentifier: str = ...,
        NetworkType: str = ...,
    ) -> CreateReplicationInstanceResponseTypeDef:
        """
        Creates the replication instance using the specified parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.create_replication_instance)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#create_replication_instance)
        """

    async def create_replication_subnet_group(
        self,
        *,
        ReplicationSubnetGroupIdentifier: str,
        ReplicationSubnetGroupDescription: str,
        SubnetIds: Sequence[str],
        Tags: Sequence[TagTypeDef] = ...,
    ) -> CreateReplicationSubnetGroupResponseTypeDef:
        """
        Creates a replication subnet group given a list of the subnet IDs in a VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.create_replication_subnet_group)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#create_replication_subnet_group)
        """

    async def create_replication_task(
        self,
        *,
        ReplicationTaskIdentifier: str,
        SourceEndpointArn: str,
        TargetEndpointArn: str,
        ReplicationInstanceArn: str,
        MigrationType: MigrationTypeValueType,
        TableMappings: str,
        ReplicationTaskSettings: str = ...,
        CdcStartTime: TimestampTypeDef = ...,
        CdcStartPosition: str = ...,
        CdcStopPosition: str = ...,
        Tags: Sequence[TagTypeDef] = ...,
        TaskData: str = ...,
        ResourceIdentifier: str = ...,
    ) -> CreateReplicationTaskResponseTypeDef:
        """
        Creates a replication task using the specified parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.create_replication_task)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#create_replication_task)
        """

    async def delete_certificate(self, *, CertificateArn: str) -> DeleteCertificateResponseTypeDef:
        """
        Deletes the specified certificate.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.delete_certificate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#delete_certificate)
        """

    async def delete_connection(
        self, *, EndpointArn: str, ReplicationInstanceArn: str
    ) -> DeleteConnectionResponseTypeDef:
        """
        Deletes the connection between a replication instance and an endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.delete_connection)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#delete_connection)
        """

    async def delete_data_provider(
        self, *, DataProviderIdentifier: str
    ) -> DeleteDataProviderResponseTypeDef:
        """
        Deletes the specified data provider.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.delete_data_provider)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#delete_data_provider)
        """

    async def delete_endpoint(self, *, EndpointArn: str) -> DeleteEndpointResponseTypeDef:
        """
        Deletes the specified endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.delete_endpoint)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#delete_endpoint)
        """

    async def delete_event_subscription(
        self, *, SubscriptionName: str
    ) -> DeleteEventSubscriptionResponseTypeDef:
        """
        Deletes an DMS event subscription.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.delete_event_subscription)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#delete_event_subscription)
        """

    async def delete_fleet_advisor_collector(
        self, *, CollectorReferencedId: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified Fleet Advisor collector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.delete_fleet_advisor_collector)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#delete_fleet_advisor_collector)
        """

    async def delete_fleet_advisor_databases(
        self, *, DatabaseIds: Sequence[str]
    ) -> DeleteFleetAdvisorDatabasesResponseTypeDef:
        """
        Deletes the specified Fleet Advisor collector databases.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.delete_fleet_advisor_databases)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#delete_fleet_advisor_databases)
        """

    async def delete_instance_profile(
        self, *, InstanceProfileIdentifier: str
    ) -> DeleteInstanceProfileResponseTypeDef:
        """
        Deletes the specified instance profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.delete_instance_profile)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#delete_instance_profile)
        """

    async def delete_migration_project(
        self, *, MigrationProjectIdentifier: str
    ) -> DeleteMigrationProjectResponseTypeDef:
        """
        Deletes the specified migration project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.delete_migration_project)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#delete_migration_project)
        """

    async def delete_replication_config(
        self, *, ReplicationConfigArn: str
    ) -> DeleteReplicationConfigResponseTypeDef:
        """
        Deletes an DMS Serverless replication configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.delete_replication_config)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#delete_replication_config)
        """

    async def delete_replication_instance(
        self, *, ReplicationInstanceArn: str
    ) -> DeleteReplicationInstanceResponseTypeDef:
        """
        Deletes the specified replication instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.delete_replication_instance)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#delete_replication_instance)
        """

    async def delete_replication_subnet_group(
        self, *, ReplicationSubnetGroupIdentifier: str
    ) -> Dict[str, Any]:
        """
        Deletes a subnet group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.delete_replication_subnet_group)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#delete_replication_subnet_group)
        """

    async def delete_replication_task(
        self, *, ReplicationTaskArn: str
    ) -> DeleteReplicationTaskResponseTypeDef:
        """
        Deletes the specified replication task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.delete_replication_task)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#delete_replication_task)
        """

    async def delete_replication_task_assessment_run(
        self, *, ReplicationTaskAssessmentRunArn: str
    ) -> DeleteReplicationTaskAssessmentRunResponseTypeDef:
        """
        Deletes the record of a single premigration assessment run.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.delete_replication_task_assessment_run)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#delete_replication_task_assessment_run)
        """

    async def describe_account_attributes(self) -> DescribeAccountAttributesResponseTypeDef:
        """
        Lists all of the DMS attributes for a customer account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.describe_account_attributes)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#describe_account_attributes)
        """

    async def describe_applicable_individual_assessments(
        self,
        *,
        ReplicationTaskArn: str = ...,
        ReplicationInstanceArn: str = ...,
        SourceEngineName: str = ...,
        TargetEngineName: str = ...,
        MigrationType: MigrationTypeValueType = ...,
        MaxRecords: int = ...,
        Marker: str = ...,
    ) -> DescribeApplicableIndividualAssessmentsResponseTypeDef:
        """
        Provides a list of individual assessments that you can specify for a new
        premigration assessment run, given one or more
        parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.describe_applicable_individual_assessments)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#describe_applicable_individual_assessments)
        """

    async def describe_certificates(
        self, *, Filters: Sequence[FilterTypeDef] = ..., MaxRecords: int = ..., Marker: str = ...
    ) -> DescribeCertificatesResponseTypeDef:
        """
        Provides a description of the certificate.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.describe_certificates)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#describe_certificates)
        """

    async def describe_connections(
        self, *, Filters: Sequence[FilterTypeDef] = ..., MaxRecords: int = ..., Marker: str = ...
    ) -> DescribeConnectionsResponseTypeDef:
        """
        Describes the status of the connections that have been made between the
        replication instance and an
        endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.describe_connections)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#describe_connections)
        """

    async def describe_conversion_configuration(
        self, *, MigrationProjectIdentifier: str
    ) -> DescribeConversionConfigurationResponseTypeDef:
        """
        Returns configuration parameters for a schema conversion project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.describe_conversion_configuration)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#describe_conversion_configuration)
        """

    async def describe_data_providers(
        self, *, Filters: Sequence[FilterTypeDef] = ..., MaxRecords: int = ..., Marker: str = ...
    ) -> DescribeDataProvidersResponseTypeDef:
        """
        Returns a paginated list of data providers for your account in the current
        region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.describe_data_providers)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#describe_data_providers)
        """

    async def describe_endpoint_settings(
        self, *, EngineName: str, MaxRecords: int = ..., Marker: str = ...
    ) -> DescribeEndpointSettingsResponseTypeDef:
        """
        Returns information about the possible endpoint settings available when you
        create an endpoint for a specific database
        engine.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.describe_endpoint_settings)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#describe_endpoint_settings)
        """

    async def describe_endpoint_types(
        self, *, Filters: Sequence[FilterTypeDef] = ..., MaxRecords: int = ..., Marker: str = ...
    ) -> DescribeEndpointTypesResponseTypeDef:
        """
        Returns information about the type of endpoints available.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.describe_endpoint_types)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#describe_endpoint_types)
        """

    async def describe_endpoints(
        self, *, Filters: Sequence[FilterTypeDef] = ..., MaxRecords: int = ..., Marker: str = ...
    ) -> DescribeEndpointsResponseTypeDef:
        """
        Returns information about the endpoints for your account in the current region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.describe_endpoints)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#describe_endpoints)
        """

    async def describe_engine_versions(
        self, *, MaxRecords: int = ..., Marker: str = ...
    ) -> DescribeEngineVersionsResponseTypeDef:
        """
        Returns information about the replication instance versions used in the project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.describe_engine_versions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#describe_engine_versions)
        """

    async def describe_event_categories(
        self, *, SourceType: str = ..., Filters: Sequence[FilterTypeDef] = ...
    ) -> DescribeEventCategoriesResponseTypeDef:
        """
        Lists categories for all event source types, or, if specified, for a specified
        source
        type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.describe_event_categories)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#describe_event_categories)
        """

    async def describe_event_subscriptions(
        self,
        *,
        SubscriptionName: str = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxRecords: int = ...,
        Marker: str = ...,
    ) -> DescribeEventSubscriptionsResponseTypeDef:
        """
        Lists all the event subscriptions for a customer account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.describe_event_subscriptions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#describe_event_subscriptions)
        """

    async def describe_events(
        self,
        *,
        SourceIdentifier: str = ...,
        SourceType: Literal["replication-instance"] = ...,
        StartTime: TimestampTypeDef = ...,
        EndTime: TimestampTypeDef = ...,
        Duration: int = ...,
        EventCategories: Sequence[str] = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxRecords: int = ...,
        Marker: str = ...,
    ) -> DescribeEventsResponseTypeDef:
        """
        Lists events for a given source identifier and source type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.describe_events)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#describe_events)
        """

    async def describe_extension_pack_associations(
        self,
        *,
        MigrationProjectIdentifier: str,
        Filters: Sequence[FilterTypeDef] = ...,
        Marker: str = ...,
        MaxRecords: int = ...,
    ) -> DescribeExtensionPackAssociationsResponseTypeDef:
        """
        Returns a paginated list of extension pack associations for the specified
        migration
        project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.describe_extension_pack_associations)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#describe_extension_pack_associations)
        """

    async def describe_fleet_advisor_collectors(
        self, *, Filters: Sequence[FilterTypeDef] = ..., MaxRecords: int = ..., NextToken: str = ...
    ) -> DescribeFleetAdvisorCollectorsResponseTypeDef:
        """
        Returns a list of the Fleet Advisor collectors in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.describe_fleet_advisor_collectors)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#describe_fleet_advisor_collectors)
        """

    async def describe_fleet_advisor_databases(
        self, *, Filters: Sequence[FilterTypeDef] = ..., MaxRecords: int = ..., NextToken: str = ...
    ) -> DescribeFleetAdvisorDatabasesResponseTypeDef:
        """
        Returns a list of Fleet Advisor databases in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.describe_fleet_advisor_databases)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#describe_fleet_advisor_databases)
        """

    async def describe_fleet_advisor_lsa_analysis(
        self, *, MaxRecords: int = ..., NextToken: str = ...
    ) -> DescribeFleetAdvisorLsaAnalysisResponseTypeDef:
        """
        Provides descriptions of large-scale assessment (LSA) analyses produced by your
        Fleet Advisor
        collectors.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.describe_fleet_advisor_lsa_analysis)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#describe_fleet_advisor_lsa_analysis)
        """

    async def describe_fleet_advisor_schema_object_summary(
        self, *, Filters: Sequence[FilterTypeDef] = ..., MaxRecords: int = ..., NextToken: str = ...
    ) -> DescribeFleetAdvisorSchemaObjectSummaryResponseTypeDef:
        """
        Provides descriptions of the schemas discovered by your Fleet Advisor
        collectors.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.describe_fleet_advisor_schema_object_summary)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#describe_fleet_advisor_schema_object_summary)
        """

    async def describe_fleet_advisor_schemas(
        self, *, Filters: Sequence[FilterTypeDef] = ..., MaxRecords: int = ..., NextToken: str = ...
    ) -> DescribeFleetAdvisorSchemasResponseTypeDef:
        """
        Returns a list of schemas detected by Fleet Advisor Collectors in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.describe_fleet_advisor_schemas)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#describe_fleet_advisor_schemas)
        """

    async def describe_instance_profiles(
        self, *, Filters: Sequence[FilterTypeDef] = ..., MaxRecords: int = ..., Marker: str = ...
    ) -> DescribeInstanceProfilesResponseTypeDef:
        """
        Returns a paginated list of instance profiles for your account in the current
        region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.describe_instance_profiles)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#describe_instance_profiles)
        """

    async def describe_metadata_model_assessments(
        self,
        *,
        MigrationProjectIdentifier: str,
        Filters: Sequence[FilterTypeDef] = ...,
        Marker: str = ...,
        MaxRecords: int = ...,
    ) -> DescribeMetadataModelAssessmentsResponseTypeDef:
        """
        Returns a paginated list of metadata model assessments for your account in the
        current
        region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.describe_metadata_model_assessments)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#describe_metadata_model_assessments)
        """

    async def describe_metadata_model_conversions(
        self,
        *,
        MigrationProjectIdentifier: str,
        Filters: Sequence[FilterTypeDef] = ...,
        Marker: str = ...,
        MaxRecords: int = ...,
    ) -> DescribeMetadataModelConversionsResponseTypeDef:
        """
        Returns a paginated list of metadata model conversions for a migration project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.describe_metadata_model_conversions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#describe_metadata_model_conversions)
        """

    async def describe_metadata_model_exports_as_script(
        self,
        *,
        MigrationProjectIdentifier: str,
        Filters: Sequence[FilterTypeDef] = ...,
        Marker: str = ...,
        MaxRecords: int = ...,
    ) -> DescribeMetadataModelExportsAsScriptResponseTypeDef:
        """
        Returns a paginated list of metadata model exports.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.describe_metadata_model_exports_as_script)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#describe_metadata_model_exports_as_script)
        """

    async def describe_metadata_model_exports_to_target(
        self,
        *,
        MigrationProjectIdentifier: str,
        Filters: Sequence[FilterTypeDef] = ...,
        Marker: str = ...,
        MaxRecords: int = ...,
    ) -> DescribeMetadataModelExportsToTargetResponseTypeDef:
        """
        Returns a paginated list of metadata model exports.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.describe_metadata_model_exports_to_target)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#describe_metadata_model_exports_to_target)
        """

    async def describe_metadata_model_imports(
        self,
        *,
        MigrationProjectIdentifier: str,
        Filters: Sequence[FilterTypeDef] = ...,
        Marker: str = ...,
        MaxRecords: int = ...,
    ) -> DescribeMetadataModelImportsResponseTypeDef:
        """
        Returns a paginated list of metadata model imports.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.describe_metadata_model_imports)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#describe_metadata_model_imports)
        """

    async def describe_migration_projects(
        self, *, Filters: Sequence[FilterTypeDef] = ..., MaxRecords: int = ..., Marker: str = ...
    ) -> DescribeMigrationProjectsResponseTypeDef:
        """
        Returns a paginated list of migration projects for your account in the current
        region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.describe_migration_projects)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#describe_migration_projects)
        """

    async def describe_orderable_replication_instances(
        self, *, MaxRecords: int = ..., Marker: str = ...
    ) -> DescribeOrderableReplicationInstancesResponseTypeDef:
        """
        Returns information about the replication instance types that can be created in
        the specified
        region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.describe_orderable_replication_instances)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#describe_orderable_replication_instances)
        """

    async def describe_pending_maintenance_actions(
        self,
        *,
        ReplicationInstanceArn: str = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        Marker: str = ...,
        MaxRecords: int = ...,
    ) -> DescribePendingMaintenanceActionsResponseTypeDef:
        """
        For internal use only See also: [AWS API
        Documentation](https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/DescribePendingMaintenanceActions).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.describe_pending_maintenance_actions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#describe_pending_maintenance_actions)
        """

    async def describe_recommendation_limitations(
        self, *, Filters: Sequence[FilterTypeDef] = ..., MaxRecords: int = ..., NextToken: str = ...
    ) -> DescribeRecommendationLimitationsResponseTypeDef:
        """
        Returns a paginated list of limitations for recommendations of target Amazon
        Web Services
        engines.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.describe_recommendation_limitations)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#describe_recommendation_limitations)
        """

    async def describe_recommendations(
        self, *, Filters: Sequence[FilterTypeDef] = ..., MaxRecords: int = ..., NextToken: str = ...
    ) -> DescribeRecommendationsResponseTypeDef:
        """
        Returns a paginated list of target engine recommendations for your source
        databases.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.describe_recommendations)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#describe_recommendations)
        """

    async def describe_refresh_schemas_status(
        self, *, EndpointArn: str
    ) -> DescribeRefreshSchemasStatusResponseTypeDef:
        """
        Returns the status of the RefreshSchemas operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.describe_refresh_schemas_status)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#describe_refresh_schemas_status)
        """

    async def describe_replication_configs(
        self, *, Filters: Sequence[FilterTypeDef] = ..., MaxRecords: int = ..., Marker: str = ...
    ) -> DescribeReplicationConfigsResponseTypeDef:
        """
        Returns one or more existing DMS Serverless replication configurations as a
        list of
        structures.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.describe_replication_configs)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#describe_replication_configs)
        """

    async def describe_replication_instance_task_logs(
        self, *, ReplicationInstanceArn: str, MaxRecords: int = ..., Marker: str = ...
    ) -> DescribeReplicationInstanceTaskLogsResponseTypeDef:
        """
        Returns information about the task logs for the specified task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.describe_replication_instance_task_logs)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#describe_replication_instance_task_logs)
        """

    async def describe_replication_instances(
        self, *, Filters: Sequence[FilterTypeDef] = ..., MaxRecords: int = ..., Marker: str = ...
    ) -> DescribeReplicationInstancesResponseTypeDef:
        """
        Returns information about replication instances for your account in the current
        region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.describe_replication_instances)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#describe_replication_instances)
        """

    async def describe_replication_subnet_groups(
        self, *, Filters: Sequence[FilterTypeDef] = ..., MaxRecords: int = ..., Marker: str = ...
    ) -> DescribeReplicationSubnetGroupsResponseTypeDef:
        """
        Returns information about the replication subnet groups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.describe_replication_subnet_groups)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#describe_replication_subnet_groups)
        """

    async def describe_replication_table_statistics(
        self,
        *,
        ReplicationConfigArn: str,
        MaxRecords: int = ...,
        Marker: str = ...,
        Filters: Sequence[FilterTypeDef] = ...,
    ) -> DescribeReplicationTableStatisticsResponseTypeDef:
        """
        Returns table and schema statistics for one or more provisioned replications
        that use a given DMS Serverless replication
        configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.describe_replication_table_statistics)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#describe_replication_table_statistics)
        """

    async def describe_replication_task_assessment_results(
        self, *, ReplicationTaskArn: str = ..., MaxRecords: int = ..., Marker: str = ...
    ) -> DescribeReplicationTaskAssessmentResultsResponseTypeDef:
        """
        Returns the task assessment results from the Amazon S3 bucket that DMS creates
        in your Amazon Web Services
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.describe_replication_task_assessment_results)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#describe_replication_task_assessment_results)
        """

    async def describe_replication_task_assessment_runs(
        self, *, Filters: Sequence[FilterTypeDef] = ..., MaxRecords: int = ..., Marker: str = ...
    ) -> DescribeReplicationTaskAssessmentRunsResponseTypeDef:
        """
        Returns a paginated list of premigration assessment runs based on filter
        settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.describe_replication_task_assessment_runs)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#describe_replication_task_assessment_runs)
        """

    async def describe_replication_task_individual_assessments(
        self, *, Filters: Sequence[FilterTypeDef] = ..., MaxRecords: int = ..., Marker: str = ...
    ) -> DescribeReplicationTaskIndividualAssessmentsResponseTypeDef:
        """
        Returns a paginated list of individual assessments based on filter settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.describe_replication_task_individual_assessments)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#describe_replication_task_individual_assessments)
        """

    async def describe_replication_tasks(
        self,
        *,
        Filters: Sequence[FilterTypeDef] = ...,
        MaxRecords: int = ...,
        Marker: str = ...,
        WithoutSettings: bool = ...,
    ) -> DescribeReplicationTasksResponseTypeDef:
        """
        Returns information about replication tasks for your account in the current
        region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.describe_replication_tasks)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#describe_replication_tasks)
        """

    async def describe_replications(
        self, *, Filters: Sequence[FilterTypeDef] = ..., MaxRecords: int = ..., Marker: str = ...
    ) -> DescribeReplicationsResponseTypeDef:
        """
        Provides details on replication progress by returning status information for
        one or more provisioned DMS Serverless
        replications.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.describe_replications)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#describe_replications)
        """

    async def describe_schemas(
        self, *, EndpointArn: str, MaxRecords: int = ..., Marker: str = ...
    ) -> DescribeSchemasResponseTypeDef:
        """
        Returns information about the schema for the specified endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.describe_schemas)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#describe_schemas)
        """

    async def describe_table_statistics(
        self,
        *,
        ReplicationTaskArn: str,
        MaxRecords: int = ...,
        Marker: str = ...,
        Filters: Sequence[FilterTypeDef] = ...,
    ) -> DescribeTableStatisticsResponseTypeDef:
        """
        Returns table statistics on the database migration task, including table name,
        rows inserted, rows updated, and rows
        deleted.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.describe_table_statistics)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#describe_table_statistics)
        """

    async def export_metadata_model_assessment(
        self,
        *,
        MigrationProjectIdentifier: str,
        SelectionRules: str,
        FileName: str = ...,
        AssessmentReportTypes: Sequence[AssessmentReportTypeType] = ...,
    ) -> ExportMetadataModelAssessmentResponseTypeDef:
        """
        Saves a copy of a database migration assessment report to your Amazon S3 bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.export_metadata_model_assessment)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#export_metadata_model_assessment)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.generate_presigned_url)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#generate_presigned_url)
        """

    async def import_certificate(
        self,
        *,
        CertificateIdentifier: str,
        CertificatePem: str = ...,
        CertificateWallet: BlobTypeDef = ...,
        Tags: Sequence[TagTypeDef] = ...,
    ) -> ImportCertificateResponseTypeDef:
        """
        Uploads the specified certificate.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.import_certificate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#import_certificate)
        """

    async def list_tags_for_resource(
        self, *, ResourceArn: str = ..., ResourceArnList: Sequence[str] = ...
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists all metadata tags attached to an DMS resource, including replication
        instance, endpoint, subnet group, and migration
        task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.list_tags_for_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#list_tags_for_resource)
        """

    async def modify_conversion_configuration(
        self, *, MigrationProjectIdentifier: str, ConversionConfiguration: str
    ) -> ModifyConversionConfigurationResponseTypeDef:
        """
        Modifies the specified schema conversion configuration using the provided
        parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.modify_conversion_configuration)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#modify_conversion_configuration)
        """

    async def modify_data_provider(
        self,
        *,
        DataProviderIdentifier: str,
        DataProviderName: str = ...,
        Description: str = ...,
        Engine: str = ...,
        ExactSettings: bool = ...,
        Settings: DataProviderSettingsTypeDef = ...,
    ) -> ModifyDataProviderResponseTypeDef:
        """
        Modifies the specified data provider using the provided settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.modify_data_provider)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#modify_data_provider)
        """

    async def modify_endpoint(
        self,
        *,
        EndpointArn: str,
        EndpointIdentifier: str = ...,
        EndpointType: ReplicationEndpointTypeValueType = ...,
        EngineName: str = ...,
        Username: str = ...,
        Password: str = ...,
        ServerName: str = ...,
        Port: int = ...,
        DatabaseName: str = ...,
        ExtraConnectionAttributes: str = ...,
        CertificateArn: str = ...,
        SslMode: DmsSslModeValueType = ...,
        ServiceAccessRoleArn: str = ...,
        ExternalTableDefinition: str = ...,
        DynamoDbSettings: DynamoDbSettingsTypeDef = ...,
        S3Settings: S3SettingsTypeDef = ...,
        DmsTransferSettings: DmsTransferSettingsTypeDef = ...,
        MongoDbSettings: MongoDbSettingsTypeDef = ...,
        KinesisSettings: KinesisSettingsTypeDef = ...,
        KafkaSettings: KafkaSettingsTypeDef = ...,
        ElasticsearchSettings: ElasticsearchSettingsTypeDef = ...,
        NeptuneSettings: NeptuneSettingsTypeDef = ...,
        RedshiftSettings: RedshiftSettingsTypeDef = ...,
        PostgreSQLSettings: PostgreSQLSettingsTypeDef = ...,
        MySQLSettings: MySQLSettingsTypeDef = ...,
        OracleSettings: OracleSettingsTypeDef = ...,
        SybaseSettings: SybaseSettingsTypeDef = ...,
        MicrosoftSQLServerSettings: MicrosoftSQLServerSettingsTypeDef = ...,
        IBMDb2Settings: IBMDb2SettingsTypeDef = ...,
        DocDbSettings: DocDbSettingsTypeDef = ...,
        RedisSettings: RedisSettingsTypeDef = ...,
        ExactSettings: bool = ...,
        GcpMySQLSettings: GcpMySQLSettingsTypeDef = ...,
        TimestreamSettings: TimestreamSettingsTypeDef = ...,
    ) -> ModifyEndpointResponseTypeDef:
        """
        Modifies the specified endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.modify_endpoint)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#modify_endpoint)
        """

    async def modify_event_subscription(
        self,
        *,
        SubscriptionName: str,
        SnsTopicArn: str = ...,
        SourceType: str = ...,
        EventCategories: Sequence[str] = ...,
        Enabled: bool = ...,
    ) -> ModifyEventSubscriptionResponseTypeDef:
        """
        Modifies an existing DMS event notification subscription.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.modify_event_subscription)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#modify_event_subscription)
        """

    async def modify_instance_profile(
        self,
        *,
        InstanceProfileIdentifier: str,
        AvailabilityZone: str = ...,
        KmsKeyArn: str = ...,
        PubliclyAccessible: bool = ...,
        NetworkType: str = ...,
        InstanceProfileName: str = ...,
        Description: str = ...,
        SubnetGroupIdentifier: str = ...,
        VpcSecurityGroups: Sequence[str] = ...,
    ) -> ModifyInstanceProfileResponseTypeDef:
        """
        Modifies the specified instance profile using the provided parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.modify_instance_profile)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#modify_instance_profile)
        """

    async def modify_migration_project(
        self,
        *,
        MigrationProjectIdentifier: str,
        MigrationProjectName: str = ...,
        SourceDataProviderDescriptors: Sequence[DataProviderDescriptorDefinitionTypeDef] = ...,
        TargetDataProviderDescriptors: Sequence[DataProviderDescriptorDefinitionTypeDef] = ...,
        InstanceProfileIdentifier: str = ...,
        TransformationRules: str = ...,
        Description: str = ...,
        SchemaConversionApplicationAttributes: SCApplicationAttributesTypeDef = ...,
    ) -> ModifyMigrationProjectResponseTypeDef:
        """
        Modifies the specified migration project using the provided parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.modify_migration_project)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#modify_migration_project)
        """

    async def modify_replication_config(
        self,
        *,
        ReplicationConfigArn: str,
        ReplicationConfigIdentifier: str = ...,
        ReplicationType: MigrationTypeValueType = ...,
        TableMappings: str = ...,
        ReplicationSettings: str = ...,
        SupplementalSettings: str = ...,
        ComputeConfig: ComputeConfigTypeDef = ...,
        SourceEndpointArn: str = ...,
        TargetEndpointArn: str = ...,
    ) -> ModifyReplicationConfigResponseTypeDef:
        """
        Modifies an existing DMS Serverless replication configuration that you can use
        to start a
        replication.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.modify_replication_config)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#modify_replication_config)
        """

    async def modify_replication_instance(
        self,
        *,
        ReplicationInstanceArn: str,
        AllocatedStorage: int = ...,
        ApplyImmediately: bool = ...,
        ReplicationInstanceClass: str = ...,
        VpcSecurityGroupIds: Sequence[str] = ...,
        PreferredMaintenanceWindow: str = ...,
        MultiAZ: bool = ...,
        EngineVersion: str = ...,
        AllowMajorVersionUpgrade: bool = ...,
        AutoMinorVersionUpgrade: bool = ...,
        ReplicationInstanceIdentifier: str = ...,
        NetworkType: str = ...,
    ) -> ModifyReplicationInstanceResponseTypeDef:
        """
        Modifies the replication instance to apply new settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.modify_replication_instance)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#modify_replication_instance)
        """

    async def modify_replication_subnet_group(
        self,
        *,
        ReplicationSubnetGroupIdentifier: str,
        SubnetIds: Sequence[str],
        ReplicationSubnetGroupDescription: str = ...,
    ) -> ModifyReplicationSubnetGroupResponseTypeDef:
        """
        Modifies the settings for the specified replication subnet group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.modify_replication_subnet_group)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#modify_replication_subnet_group)
        """

    async def modify_replication_task(
        self,
        *,
        ReplicationTaskArn: str,
        ReplicationTaskIdentifier: str = ...,
        MigrationType: MigrationTypeValueType = ...,
        TableMappings: str = ...,
        ReplicationTaskSettings: str = ...,
        CdcStartTime: TimestampTypeDef = ...,
        CdcStartPosition: str = ...,
        CdcStopPosition: str = ...,
        TaskData: str = ...,
    ) -> ModifyReplicationTaskResponseTypeDef:
        """
        Modifies the specified replication task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.modify_replication_task)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#modify_replication_task)
        """

    async def move_replication_task(
        self, *, ReplicationTaskArn: str, TargetReplicationInstanceArn: str
    ) -> MoveReplicationTaskResponseTypeDef:
        """
        Moves a replication task from its current replication instance to a different
        target replication instance using the specified
        parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.move_replication_task)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#move_replication_task)
        """

    async def reboot_replication_instance(
        self,
        *,
        ReplicationInstanceArn: str,
        ForceFailover: bool = ...,
        ForcePlannedFailover: bool = ...,
    ) -> RebootReplicationInstanceResponseTypeDef:
        """
        Reboots a replication instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.reboot_replication_instance)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#reboot_replication_instance)
        """

    async def refresh_schemas(
        self, *, EndpointArn: str, ReplicationInstanceArn: str
    ) -> RefreshSchemasResponseTypeDef:
        """
        Populates the schema for the specified endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.refresh_schemas)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#refresh_schemas)
        """

    async def reload_replication_tables(
        self,
        *,
        ReplicationConfigArn: str,
        TablesToReload: Sequence[TableToReloadTypeDef],
        ReloadOption: ReloadOptionValueType = ...,
    ) -> ReloadReplicationTablesResponseTypeDef:
        """
        Reloads the target database table with the source data for a given DMS
        Serverless replication
        configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.reload_replication_tables)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#reload_replication_tables)
        """

    async def reload_tables(
        self,
        *,
        ReplicationTaskArn: str,
        TablesToReload: Sequence[TableToReloadTypeDef],
        ReloadOption: ReloadOptionValueType = ...,
    ) -> ReloadTablesResponseTypeDef:
        """
        Reloads the target database table with the source data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.reload_tables)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#reload_tables)
        """

    async def remove_tags_from_resource(
        self, *, ResourceArn: str, TagKeys: Sequence[str]
    ) -> Dict[str, Any]:
        """
        Removes metadata tags from an DMS resource, including replication instance,
        endpoint, subnet group, and migration
        task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.remove_tags_from_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#remove_tags_from_resource)
        """

    async def run_fleet_advisor_lsa_analysis(self) -> RunFleetAdvisorLsaAnalysisResponseTypeDef:
        """
        Runs large-scale assessment (LSA) analysis on every Fleet Advisor collector in
        your
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.run_fleet_advisor_lsa_analysis)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#run_fleet_advisor_lsa_analysis)
        """

    async def start_extension_pack_association(
        self, *, MigrationProjectIdentifier: str
    ) -> StartExtensionPackAssociationResponseTypeDef:
        """
        Applies the extension pack to your target database.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.start_extension_pack_association)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#start_extension_pack_association)
        """

    async def start_metadata_model_assessment(
        self, *, MigrationProjectIdentifier: str, SelectionRules: str
    ) -> StartMetadataModelAssessmentResponseTypeDef:
        """
        Creates a database migration assessment report by assessing the migration
        complexity for your source
        database.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.start_metadata_model_assessment)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#start_metadata_model_assessment)
        """

    async def start_metadata_model_conversion(
        self, *, MigrationProjectIdentifier: str, SelectionRules: str
    ) -> StartMetadataModelConversionResponseTypeDef:
        """
        Converts your source database objects to a format compatible with the target
        database.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.start_metadata_model_conversion)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#start_metadata_model_conversion)
        """

    async def start_metadata_model_export_as_script(
        self,
        *,
        MigrationProjectIdentifier: str,
        SelectionRules: str,
        Origin: OriginTypeValueType,
        FileName: str = ...,
    ) -> StartMetadataModelExportAsScriptResponseTypeDef:
        """
        Saves your converted code to a file as a SQL script, and stores this file on
        your Amazon S3
        bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.start_metadata_model_export_as_script)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#start_metadata_model_export_as_script)
        """

    async def start_metadata_model_export_to_target(
        self,
        *,
        MigrationProjectIdentifier: str,
        SelectionRules: str,
        OverwriteExtensionPack: bool = ...,
    ) -> StartMetadataModelExportToTargetResponseTypeDef:
        """
        Applies converted database objects to your target database.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.start_metadata_model_export_to_target)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#start_metadata_model_export_to_target)
        """

    async def start_metadata_model_import(
        self,
        *,
        MigrationProjectIdentifier: str,
        SelectionRules: str,
        Origin: OriginTypeValueType,
        Refresh: bool = ...,
    ) -> StartMetadataModelImportResponseTypeDef:
        """
        Loads the metadata for all the dependent database objects of the parent object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.start_metadata_model_import)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#start_metadata_model_import)
        """

    async def start_recommendations(
        self, *, DatabaseId: str, Settings: RecommendationSettingsTypeDef
    ) -> EmptyResponseMetadataTypeDef:
        """
        Starts the analysis of your source database to provide recommendations of
        target
        engines.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.start_recommendations)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#start_recommendations)
        """

    async def start_replication(
        self,
        *,
        ReplicationConfigArn: str,
        StartReplicationType: str,
        CdcStartTime: TimestampTypeDef = ...,
        CdcStartPosition: str = ...,
        CdcStopPosition: str = ...,
    ) -> StartReplicationResponseTypeDef:
        """
        For a given DMS Serverless replication configuration, DMS connects to the
        source endpoint and collects the metadata to analyze the replication
        workload.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.start_replication)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#start_replication)
        """

    async def start_replication_task(
        self,
        *,
        ReplicationTaskArn: str,
        StartReplicationTaskType: StartReplicationTaskTypeValueType,
        CdcStartTime: TimestampTypeDef = ...,
        CdcStartPosition: str = ...,
        CdcStopPosition: str = ...,
    ) -> StartReplicationTaskResponseTypeDef:
        """
        Starts the replication task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.start_replication_task)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#start_replication_task)
        """

    async def start_replication_task_assessment(
        self, *, ReplicationTaskArn: str
    ) -> StartReplicationTaskAssessmentResponseTypeDef:
        """
        Starts the replication task assessment for unsupported data types in the source
        database.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.start_replication_task_assessment)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#start_replication_task_assessment)
        """

    async def start_replication_task_assessment_run(
        self,
        *,
        ReplicationTaskArn: str,
        ServiceAccessRoleArn: str,
        ResultLocationBucket: str,
        AssessmentRunName: str,
        ResultLocationFolder: str = ...,
        ResultEncryptionMode: str = ...,
        ResultKmsKeyArn: str = ...,
        IncludeOnly: Sequence[str] = ...,
        Exclude: Sequence[str] = ...,
    ) -> StartReplicationTaskAssessmentRunResponseTypeDef:
        """
        Starts a new premigration assessment run for one or more individual assessments
        of a migration
        task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.start_replication_task_assessment_run)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#start_replication_task_assessment_run)
        """

    async def stop_replication(
        self, *, ReplicationConfigArn: str
    ) -> StopReplicationResponseTypeDef:
        """
        For a given DMS Serverless replication configuration, DMS stops any and all
        ongoing DMS Serverless
        replications.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.stop_replication)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#stop_replication)
        """

    async def stop_replication_task(
        self, *, ReplicationTaskArn: str
    ) -> StopReplicationTaskResponseTypeDef:
        """
        Stops the replication task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.stop_replication_task)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#stop_replication_task)
        """

    async def test_connection(
        self, *, ReplicationInstanceArn: str, EndpointArn: str
    ) -> TestConnectionResponseTypeDef:
        """
        Tests the connection between the replication instance and the endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.test_connection)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#test_connection)
        """

    async def update_subscriptions_to_event_bridge(
        self, *, ForceMove: bool = ...
    ) -> UpdateSubscriptionsToEventBridgeResponseTypeDef:
        """
        Migrates 10 active and enabled Amazon SNS subscriptions at a time and converts
        them to corresponding Amazon EventBridge
        rules.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.update_subscriptions_to_event_bridge)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#update_subscriptions_to_event_bridge)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_certificates"]
    ) -> DescribeCertificatesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_connections"]
    ) -> DescribeConnectionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_endpoint_types"]
    ) -> DescribeEndpointTypesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_endpoints"]
    ) -> DescribeEndpointsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_event_subscriptions"]
    ) -> DescribeEventSubscriptionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["describe_events"]) -> DescribeEventsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_orderable_replication_instances"]
    ) -> DescribeOrderableReplicationInstancesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_replication_instances"]
    ) -> DescribeReplicationInstancesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_replication_subnet_groups"]
    ) -> DescribeReplicationSubnetGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_replication_task_assessment_results"]
    ) -> DescribeReplicationTaskAssessmentResultsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_replication_tasks"]
    ) -> DescribeReplicationTasksPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_schemas"]
    ) -> DescribeSchemasPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_table_statistics"]
    ) -> DescribeTableStatisticsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#get_paginator)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["endpoint_deleted"]) -> EndpointDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.get_waiter)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#get_waiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["replication_instance_available"]
    ) -> ReplicationInstanceAvailableWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.get_waiter)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#get_waiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["replication_instance_deleted"]
    ) -> ReplicationInstanceDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.get_waiter)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#get_waiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["replication_task_deleted"]
    ) -> ReplicationTaskDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.get_waiter)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#get_waiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["replication_task_ready"]
    ) -> ReplicationTaskReadyWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.get_waiter)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#get_waiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["replication_task_running"]
    ) -> ReplicationTaskRunningWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.get_waiter)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#get_waiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["replication_task_stopped"]
    ) -> ReplicationTaskStoppedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.get_waiter)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#get_waiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["test_connection_succeeds"]
    ) -> TestConnectionSucceedsWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.get_waiter)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/#get_waiter)
        """

    async def __aenter__(self) -> "DatabaseMigrationServiceClient":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/)
        """

    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> Any:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dms/client/)
        """
