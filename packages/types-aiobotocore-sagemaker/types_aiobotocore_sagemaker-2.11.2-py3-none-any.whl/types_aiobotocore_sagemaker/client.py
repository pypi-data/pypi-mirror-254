"""
Type annotations for sagemaker service client.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/)

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_sagemaker.client import SageMakerClient

    session = get_session()
    async with session.create_client("sagemaker") as client:
        client: SageMakerClient
    ```
"""

import sys
from typing import Any, Dict, Mapping, Sequence, Type, overload

from aiobotocore.client import AioBaseClient
from botocore.client import ClientMeta

from .literals import (
    ActionStatusType,
    AlgorithmSortByType,
    AppImageConfigSortKeyType,
    AppNetworkAccessTypeType,
    AppSecurityGroupManagementType,
    AppTypeType,
    AssociationEdgeTypeType,
    AuthModeType,
    AutoMLJobStatusType,
    AutoMLSortByType,
    AutoMLSortOrderType,
    BatchStrategyType,
    CandidateSortByType,
    CandidateStatusType,
    ClusterSortByType,
    CodeRepositorySortByType,
    CodeRepositorySortOrderType,
    CompilationJobStatusType,
    CrossAccountFilterOptionType,
    DirectInternetAccessType,
    DirectionType,
    EdgePackagingJobStatusType,
    EndpointConfigSortKeyType,
    EndpointSortKeyType,
    EndpointStatusType,
    ExecutionStatusType,
    FeatureGroupSortByType,
    FeatureGroupSortOrderType,
    FeatureGroupStatusType,
    HubContentSortByType,
    HubContentTypeType,
    HubSortByType,
    HyperParameterTuningJobSortByOptionsType,
    HyperParameterTuningJobStatusType,
    ImageSortByType,
    ImageSortOrderType,
    ImageVersionSortByType,
    ImageVersionSortOrderType,
    InferenceComponentSortKeyType,
    InferenceComponentStatusType,
    InferenceExperimentStatusType,
    InferenceExperimentStopDesiredStateType,
    InstanceTypeType,
    JobTypeType,
    LabelingJobStatusType,
    ListCompilationJobsSortByType,
    ListDeviceFleetsSortByType,
    ListEdgeDeploymentPlansSortByType,
    ListEdgePackagingJobsSortByType,
    ListInferenceRecommendationsJobsSortByType,
    ListWorkforcesSortByOptionsType,
    ListWorkteamsSortByOptionsType,
    ModelApprovalStatusType,
    ModelCardExportJobSortByType,
    ModelCardExportJobSortOrderType,
    ModelCardExportJobStatusType,
    ModelCardSortByType,
    ModelCardSortOrderType,
    ModelCardStatusType,
    ModelPackageGroupSortByType,
    ModelPackageSortByType,
    ModelPackageTypeType,
    ModelSortKeyType,
    ModelVariantActionType,
    MonitoringAlertHistorySortKeyType,
    MonitoringAlertStatusType,
    MonitoringExecutionSortKeyType,
    MonitoringJobDefinitionSortKeyType,
    MonitoringScheduleSortKeyType,
    MonitoringTypeType,
    NotebookInstanceAcceleratorTypeType,
    NotebookInstanceLifecycleConfigSortKeyType,
    NotebookInstanceLifecycleConfigSortOrderType,
    NotebookInstanceSortKeyType,
    NotebookInstanceSortOrderType,
    NotebookInstanceStatusType,
    OfflineStoreStatusValueType,
    OrderKeyType,
    ProblemTypeType,
    ProcessingJobStatusType,
    ProcessorType,
    ProjectSortByType,
    ProjectSortOrderType,
    RecommendationJobStatusType,
    RecommendationJobTypeType,
    ResourceCatalogSortOrderType,
    ResourceTypeType,
    RootAccessType,
    ScheduleStatusType,
    SearchSortOrderType,
    SkipModelValidationType,
    SortActionsByType,
    SortAssociationsByType,
    SortByType,
    SortContextsByType,
    SortExperimentsByType,
    SortInferenceExperimentsByType,
    SortLineageGroupsByType,
    SortOrderType,
    SortPipelineExecutionsByType,
    SortPipelinesByType,
    SortTrialComponentsByType,
    SortTrialsByType,
    SpaceSortKeyType,
    StudioLifecycleConfigAppTypeType,
    StudioLifecycleConfigSortKeyType,
    TrainingJobSortByOptionsType,
    TrainingJobStatusType,
    TransformJobStatusType,
    UserProfileSortKeyType,
    VendorGuidanceType,
    WarmPoolResourceStatusType,
)
from .paginator import (
    ListActionsPaginator,
    ListAlgorithmsPaginator,
    ListAliasesPaginator,
    ListAppImageConfigsPaginator,
    ListAppsPaginator,
    ListArtifactsPaginator,
    ListAssociationsPaginator,
    ListAutoMLJobsPaginator,
    ListCandidatesForAutoMLJobPaginator,
    ListClusterNodesPaginator,
    ListClustersPaginator,
    ListCodeRepositoriesPaginator,
    ListCompilationJobsPaginator,
    ListContextsPaginator,
    ListDataQualityJobDefinitionsPaginator,
    ListDeviceFleetsPaginator,
    ListDevicesPaginator,
    ListDomainsPaginator,
    ListEdgeDeploymentPlansPaginator,
    ListEdgePackagingJobsPaginator,
    ListEndpointConfigsPaginator,
    ListEndpointsPaginator,
    ListExperimentsPaginator,
    ListFeatureGroupsPaginator,
    ListFlowDefinitionsPaginator,
    ListHumanTaskUisPaginator,
    ListHyperParameterTuningJobsPaginator,
    ListImagesPaginator,
    ListImageVersionsPaginator,
    ListInferenceComponentsPaginator,
    ListInferenceExperimentsPaginator,
    ListInferenceRecommendationsJobsPaginator,
    ListInferenceRecommendationsJobStepsPaginator,
    ListLabelingJobsForWorkteamPaginator,
    ListLabelingJobsPaginator,
    ListLineageGroupsPaginator,
    ListModelBiasJobDefinitionsPaginator,
    ListModelCardExportJobsPaginator,
    ListModelCardsPaginator,
    ListModelCardVersionsPaginator,
    ListModelExplainabilityJobDefinitionsPaginator,
    ListModelMetadataPaginator,
    ListModelPackageGroupsPaginator,
    ListModelPackagesPaginator,
    ListModelQualityJobDefinitionsPaginator,
    ListModelsPaginator,
    ListMonitoringAlertHistoryPaginator,
    ListMonitoringAlertsPaginator,
    ListMonitoringExecutionsPaginator,
    ListMonitoringSchedulesPaginator,
    ListNotebookInstanceLifecycleConfigsPaginator,
    ListNotebookInstancesPaginator,
    ListPipelineExecutionsPaginator,
    ListPipelineExecutionStepsPaginator,
    ListPipelineParametersForExecutionPaginator,
    ListPipelinesPaginator,
    ListProcessingJobsPaginator,
    ListResourceCatalogsPaginator,
    ListSpacesPaginator,
    ListStageDevicesPaginator,
    ListStudioLifecycleConfigsPaginator,
    ListSubscribedWorkteamsPaginator,
    ListTagsPaginator,
    ListTrainingJobsForHyperParameterTuningJobPaginator,
    ListTrainingJobsPaginator,
    ListTransformJobsPaginator,
    ListTrialComponentsPaginator,
    ListTrialsPaginator,
    ListUserProfilesPaginator,
    ListWorkforcesPaginator,
    ListWorkteamsPaginator,
    SearchPaginator,
)
from .type_defs import (
    ActionSourceTypeDef,
    AddAssociationResponseTypeDef,
    AdditionalInferenceSpecificationDefinitionTypeDef,
    AddTagsOutputTypeDef,
    AlgorithmSpecificationTypeDef,
    AlgorithmValidationSpecificationTypeDef,
    AppSpecificationTypeDef,
    ArtifactSourceTypeDef,
    AssociateTrialComponentResponseTypeDef,
    AsyncInferenceConfigTypeDef,
    AutoMLChannelTypeDef,
    AutoMLDataSplitConfigTypeDef,
    AutoMLJobChannelTypeDef,
    AutoMLJobConfigTypeDef,
    AutoMLJobObjectiveTypeDef,
    AutoMLOutputDataConfigTypeDef,
    AutoMLProblemTypeConfigTypeDef,
    AutoMLSecurityConfigTypeDef,
    AutotuneTypeDef,
    BatchDataCaptureConfigTypeDef,
    BatchDescribeModelPackageOutputTypeDef,
    ChannelTypeDef,
    CheckpointConfigTypeDef,
    ClusterInstanceGroupSpecificationTypeDef,
    CognitoConfigTypeDef,
    ContainerDefinitionTypeDef,
    ContextSourceTypeDef,
    CreateActionResponseTypeDef,
    CreateAlgorithmOutputTypeDef,
    CreateAppImageConfigResponseTypeDef,
    CreateAppResponseTypeDef,
    CreateArtifactResponseTypeDef,
    CreateAutoMLJobResponseTypeDef,
    CreateAutoMLJobV2ResponseTypeDef,
    CreateClusterResponseTypeDef,
    CreateCodeRepositoryOutputTypeDef,
    CreateCompilationJobResponseTypeDef,
    CreateContextResponseTypeDef,
    CreateDataQualityJobDefinitionResponseTypeDef,
    CreateDomainResponseTypeDef,
    CreateEdgeDeploymentPlanResponseTypeDef,
    CreateEndpointConfigOutputTypeDef,
    CreateEndpointOutputTypeDef,
    CreateExperimentResponseTypeDef,
    CreateFeatureGroupResponseTypeDef,
    CreateFlowDefinitionResponseTypeDef,
    CreateHubResponseTypeDef,
    CreateHumanTaskUiResponseTypeDef,
    CreateHyperParameterTuningJobResponseTypeDef,
    CreateImageResponseTypeDef,
    CreateImageVersionResponseTypeDef,
    CreateInferenceComponentOutputTypeDef,
    CreateInferenceExperimentResponseTypeDef,
    CreateInferenceRecommendationsJobResponseTypeDef,
    CreateLabelingJobResponseTypeDef,
    CreateModelBiasJobDefinitionResponseTypeDef,
    CreateModelCardExportJobResponseTypeDef,
    CreateModelCardResponseTypeDef,
    CreateModelExplainabilityJobDefinitionResponseTypeDef,
    CreateModelOutputTypeDef,
    CreateModelPackageGroupOutputTypeDef,
    CreateModelPackageOutputTypeDef,
    CreateModelQualityJobDefinitionResponseTypeDef,
    CreateMonitoringScheduleResponseTypeDef,
    CreateNotebookInstanceLifecycleConfigOutputTypeDef,
    CreateNotebookInstanceOutputTypeDef,
    CreatePipelineResponseTypeDef,
    CreatePresignedDomainUrlResponseTypeDef,
    CreatePresignedNotebookInstanceUrlOutputTypeDef,
    CreateProcessingJobResponseTypeDef,
    CreateProjectOutputTypeDef,
    CreateSpaceResponseTypeDef,
    CreateStudioLifecycleConfigResponseTypeDef,
    CreateTrainingJobResponseTypeDef,
    CreateTransformJobResponseTypeDef,
    CreateTrialComponentResponseTypeDef,
    CreateTrialResponseTypeDef,
    CreateUserProfileResponseTypeDef,
    CreateWorkforceResponseTypeDef,
    CreateWorkteamResponseTypeDef,
    DataCaptureConfigTypeDef,
    DataProcessingTypeDef,
    DataQualityAppSpecificationTypeDef,
    DataQualityBaselineConfigTypeDef,
    DataQualityJobInputTypeDef,
    DebugHookConfigTypeDef,
    DebugRuleConfigurationTypeDef,
    DefaultSpaceSettingsTypeDef,
    DeleteActionResponseTypeDef,
    DeleteArtifactResponseTypeDef,
    DeleteAssociationResponseTypeDef,
    DeleteClusterResponseTypeDef,
    DeleteContextResponseTypeDef,
    DeleteExperimentResponseTypeDef,
    DeleteInferenceExperimentResponseTypeDef,
    DeletePipelineResponseTypeDef,
    DeleteTrialComponentResponseTypeDef,
    DeleteTrialResponseTypeDef,
    DeleteWorkteamResponseTypeDef,
    DeploymentConfigTypeDef,
    DeploymentStageTypeDef,
    DescribeActionResponseTypeDef,
    DescribeAlgorithmOutputTypeDef,
    DescribeAppImageConfigResponseTypeDef,
    DescribeAppResponseTypeDef,
    DescribeArtifactResponseTypeDef,
    DescribeAutoMLJobResponseTypeDef,
    DescribeAutoMLJobV2ResponseTypeDef,
    DescribeClusterNodeResponseTypeDef,
    DescribeClusterResponseTypeDef,
    DescribeCodeRepositoryOutputTypeDef,
    DescribeCompilationJobResponseTypeDef,
    DescribeContextResponseTypeDef,
    DescribeDataQualityJobDefinitionResponseTypeDef,
    DescribeDeviceFleetResponseTypeDef,
    DescribeDeviceResponseTypeDef,
    DescribeDomainResponseTypeDef,
    DescribeEdgeDeploymentPlanResponseTypeDef,
    DescribeEdgePackagingJobResponseTypeDef,
    DescribeEndpointConfigOutputTypeDef,
    DescribeEndpointOutputTypeDef,
    DescribeExperimentResponseTypeDef,
    DescribeFeatureGroupResponseTypeDef,
    DescribeFeatureMetadataResponseTypeDef,
    DescribeFlowDefinitionResponseTypeDef,
    DescribeHubContentResponseTypeDef,
    DescribeHubResponseTypeDef,
    DescribeHumanTaskUiResponseTypeDef,
    DescribeHyperParameterTuningJobResponseTypeDef,
    DescribeImageResponseTypeDef,
    DescribeImageVersionResponseTypeDef,
    DescribeInferenceComponentOutputTypeDef,
    DescribeInferenceExperimentResponseTypeDef,
    DescribeInferenceRecommendationsJobResponseTypeDef,
    DescribeLabelingJobResponseTypeDef,
    DescribeLineageGroupResponseTypeDef,
    DescribeModelBiasJobDefinitionResponseTypeDef,
    DescribeModelCardExportJobResponseTypeDef,
    DescribeModelCardResponseTypeDef,
    DescribeModelExplainabilityJobDefinitionResponseTypeDef,
    DescribeModelOutputTypeDef,
    DescribeModelPackageGroupOutputTypeDef,
    DescribeModelPackageOutputTypeDef,
    DescribeModelQualityJobDefinitionResponseTypeDef,
    DescribeMonitoringScheduleResponseTypeDef,
    DescribeNotebookInstanceLifecycleConfigOutputTypeDef,
    DescribeNotebookInstanceOutputTypeDef,
    DescribePipelineDefinitionForExecutionResponseTypeDef,
    DescribePipelineExecutionResponseTypeDef,
    DescribePipelineResponseTypeDef,
    DescribeProcessingJobResponseTypeDef,
    DescribeProjectOutputTypeDef,
    DescribeSpaceResponseTypeDef,
    DescribeStudioLifecycleConfigResponseTypeDef,
    DescribeSubscribedWorkteamResponseTypeDef,
    DescribeTrainingJobResponseTypeDef,
    DescribeTransformJobResponseTypeDef,
    DescribeTrialComponentResponseTypeDef,
    DescribeTrialResponseTypeDef,
    DescribeUserProfileResponseTypeDef,
    DescribeWorkforceResponseTypeDef,
    DescribeWorkteamResponseTypeDef,
    DesiredWeightAndCapacityTypeDef,
    DeviceTypeDef,
    DisassociateTrialComponentResponseTypeDef,
    DomainSettingsForUpdateTypeDef,
    DomainSettingsTypeDef,
    DriftCheckBaselinesTypeDef,
    EdgeDeploymentModelConfigTypeDef,
    EdgeOutputConfigTypeDef,
    EmptyResponseMetadataTypeDef,
    ExperimentConfigTypeDef,
    ExplainerConfigTypeDef,
    FeatureDefinitionTypeDef,
    FeatureParameterTypeDef,
    FlowDefinitionOutputConfigTypeDef,
    GetDeviceFleetReportResponseTypeDef,
    GetLineageGroupPolicyResponseTypeDef,
    GetModelPackageGroupPolicyOutputTypeDef,
    GetSagemakerServicecatalogPortfolioStatusOutputTypeDef,
    GetScalingConfigurationRecommendationResponseTypeDef,
    GetSearchSuggestionsResponseTypeDef,
    GitConfigForUpdateTypeDef,
    GitConfigTypeDef,
    HubS3StorageConfigTypeDef,
    HumanLoopActivationConfigTypeDef,
    HumanLoopConfigTypeDef,
    HumanLoopRequestSourceTypeDef,
    HumanTaskConfigTypeDef,
    HyperParameterTrainingJobDefinitionTypeDef,
    HyperParameterTuningJobConfigTypeDef,
    HyperParameterTuningJobWarmStartConfigTypeDef,
    ImportHubContentResponseTypeDef,
    InferenceComponentRuntimeConfigTypeDef,
    InferenceComponentSpecificationTypeDef,
    InferenceExecutionConfigTypeDef,
    InferenceExperimentDataStorageConfigTypeDef,
    InferenceExperimentScheduleTypeDef,
    InferenceSpecificationTypeDef,
    InfraCheckConfigTypeDef,
    InputConfigTypeDef,
    InstanceMetadataServiceConfigurationTypeDef,
    JupyterLabAppImageConfigTypeDef,
    KernelGatewayImageConfigTypeDef,
    LabelingJobAlgorithmsConfigTypeDef,
    LabelingJobInputConfigTypeDef,
    LabelingJobOutputConfigTypeDef,
    LabelingJobStoppingConditionsTypeDef,
    ListActionsResponseTypeDef,
    ListAlgorithmsOutputTypeDef,
    ListAliasesResponseTypeDef,
    ListAppImageConfigsResponseTypeDef,
    ListAppsResponseTypeDef,
    ListArtifactsResponseTypeDef,
    ListAssociationsResponseTypeDef,
    ListAutoMLJobsResponseTypeDef,
    ListCandidatesForAutoMLJobResponseTypeDef,
    ListClusterNodesResponseTypeDef,
    ListClustersResponseTypeDef,
    ListCodeRepositoriesOutputTypeDef,
    ListCompilationJobsResponseTypeDef,
    ListContextsResponseTypeDef,
    ListDataQualityJobDefinitionsResponseTypeDef,
    ListDeviceFleetsResponseTypeDef,
    ListDevicesResponseTypeDef,
    ListDomainsResponseTypeDef,
    ListEdgeDeploymentPlansResponseTypeDef,
    ListEdgePackagingJobsResponseTypeDef,
    ListEndpointConfigsOutputTypeDef,
    ListEndpointsOutputTypeDef,
    ListExperimentsResponseTypeDef,
    ListFeatureGroupsResponseTypeDef,
    ListFlowDefinitionsResponseTypeDef,
    ListHubContentsResponseTypeDef,
    ListHubContentVersionsResponseTypeDef,
    ListHubsResponseTypeDef,
    ListHumanTaskUisResponseTypeDef,
    ListHyperParameterTuningJobsResponseTypeDef,
    ListImagesResponseTypeDef,
    ListImageVersionsResponseTypeDef,
    ListInferenceComponentsOutputTypeDef,
    ListInferenceExperimentsResponseTypeDef,
    ListInferenceRecommendationsJobsResponseTypeDef,
    ListInferenceRecommendationsJobStepsResponseTypeDef,
    ListLabelingJobsForWorkteamResponseTypeDef,
    ListLabelingJobsResponseTypeDef,
    ListLineageGroupsResponseTypeDef,
    ListModelBiasJobDefinitionsResponseTypeDef,
    ListModelCardExportJobsResponseTypeDef,
    ListModelCardsResponseTypeDef,
    ListModelCardVersionsResponseTypeDef,
    ListModelExplainabilityJobDefinitionsResponseTypeDef,
    ListModelMetadataResponseTypeDef,
    ListModelPackageGroupsOutputTypeDef,
    ListModelPackagesOutputTypeDef,
    ListModelQualityJobDefinitionsResponseTypeDef,
    ListModelsOutputTypeDef,
    ListMonitoringAlertHistoryResponseTypeDef,
    ListMonitoringAlertsResponseTypeDef,
    ListMonitoringExecutionsResponseTypeDef,
    ListMonitoringSchedulesResponseTypeDef,
    ListNotebookInstanceLifecycleConfigsOutputTypeDef,
    ListNotebookInstancesOutputTypeDef,
    ListPipelineExecutionsResponseTypeDef,
    ListPipelineExecutionStepsResponseTypeDef,
    ListPipelineParametersForExecutionResponseTypeDef,
    ListPipelinesResponseTypeDef,
    ListProcessingJobsResponseTypeDef,
    ListProjectsOutputTypeDef,
    ListResourceCatalogsResponseTypeDef,
    ListSpacesResponseTypeDef,
    ListStageDevicesResponseTypeDef,
    ListStudioLifecycleConfigsResponseTypeDef,
    ListSubscribedWorkteamsResponseTypeDef,
    ListTagsOutputTypeDef,
    ListTrainingJobsForHyperParameterTuningJobResponseTypeDef,
    ListTrainingJobsResponseTypeDef,
    ListTransformJobsResponseTypeDef,
    ListTrialComponentsResponseTypeDef,
    ListTrialsResponseTypeDef,
    ListUserProfilesResponseTypeDef,
    ListWorkforcesResponseTypeDef,
    ListWorkteamsResponseTypeDef,
    MemberDefinitionTypeDef,
    MetadataPropertiesTypeDef,
    ModelBiasAppSpecificationTypeDef,
    ModelBiasBaselineConfigTypeDef,
    ModelBiasJobInputTypeDef,
    ModelCardExportOutputConfigTypeDef,
    ModelCardSecurityConfigTypeDef,
    ModelClientConfigTypeDef,
    ModelDeployConfigTypeDef,
    ModelExplainabilityAppSpecificationTypeDef,
    ModelExplainabilityBaselineConfigTypeDef,
    ModelExplainabilityJobInputTypeDef,
    ModelMetadataSearchExpressionTypeDef,
    ModelMetricsTypeDef,
    ModelPackageValidationSpecificationTypeDef,
    ModelQualityAppSpecificationTypeDef,
    ModelQualityBaselineConfigTypeDef,
    ModelQualityJobInputTypeDef,
    ModelVariantConfigTypeDef,
    MonitoringNetworkConfigTypeDef,
    MonitoringOutputConfigTypeDef,
    MonitoringResourcesTypeDef,
    MonitoringScheduleConfigTypeDef,
    MonitoringStoppingConditionTypeDef,
    NeoVpcConfigTypeDef,
    NetworkConfigTypeDef,
    NotebookInstanceLifecycleHookTypeDef,
    NotificationConfigurationTypeDef,
    OfflineStoreConfigTypeDef,
    OidcConfigTypeDef,
    OnlineStoreConfigTypeDef,
    OnlineStoreConfigUpdateTypeDef,
    OutputConfigTypeDef,
    OutputDataConfigTypeDef,
    OutputParameterTypeDef,
    OwnershipSettingsTypeDef,
    ParallelismConfigurationTypeDef,
    ParameterTypeDef,
    PipelineDefinitionS3LocationTypeDef,
    ProcessingInputTypeDef,
    ProcessingOutputConfigTypeDef,
    ProcessingResourcesTypeDef,
    ProcessingStoppingConditionTypeDef,
    ProductionVariantTypeDef,
    ProfilerConfigForUpdateTypeDef,
    ProfilerConfigTypeDef,
    ProfilerRuleConfigurationTypeDef,
    PutModelPackageGroupPolicyOutputTypeDef,
    QueryFiltersTypeDef,
    QueryLineageResponseTypeDef,
    RecommendationJobInputConfigTypeDef,
    RecommendationJobOutputConfigTypeDef,
    RecommendationJobStoppingConditionsTypeDef,
    RemoteDebugConfigForUpdateTypeDef,
    RemoteDebugConfigTypeDef,
    RenderableTaskTypeDef,
    RenderUiTemplateResponseTypeDef,
    ResourceConfigForUpdateTypeDef,
    ResourceConfigTypeDef,
    ResourceSpecTypeDef,
    RetentionPolicyTypeDef,
    RetryPipelineExecutionResponseTypeDef,
    RetryStrategyTypeDef,
    ScalingPolicyObjectiveTypeDef,
    SearchExpressionTypeDef,
    SearchResponseTypeDef,
    SelectiveExecutionConfigTypeDef,
    SendPipelineExecutionStepFailureResponseTypeDef,
    SendPipelineExecutionStepSuccessResponseTypeDef,
    ServiceCatalogProvisioningDetailsTypeDef,
    ServiceCatalogProvisioningUpdateDetailsTypeDef,
    ShadowModeConfigTypeDef,
    SourceAlgorithmSpecificationTypeDef,
    SourceIpConfigTypeDef,
    SpaceSettingsTypeDef,
    SpaceSharingSettingsTypeDef,
    StartInferenceExperimentResponseTypeDef,
    StartPipelineExecutionResponseTypeDef,
    StopInferenceExperimentResponseTypeDef,
    StoppingConditionTypeDef,
    StopPipelineExecutionResponseTypeDef,
    SuggestionQueryTypeDef,
    TagTypeDef,
    TensorBoardOutputConfigTypeDef,
    ThroughputConfigTypeDef,
    ThroughputConfigUpdateTypeDef,
    TimestampTypeDef,
    TrainingSpecificationTypeDef,
    TransformInputTypeDef,
    TransformOutputTypeDef,
    TransformResourcesTypeDef,
    TrialComponentArtifactTypeDef,
    TrialComponentParameterValueTypeDef,
    TrialComponentStatusTypeDef,
    UiTemplateTypeDef,
    UpdateActionResponseTypeDef,
    UpdateAppImageConfigResponseTypeDef,
    UpdateArtifactResponseTypeDef,
    UpdateClusterResponseTypeDef,
    UpdateCodeRepositoryOutputTypeDef,
    UpdateContextResponseTypeDef,
    UpdateDomainResponseTypeDef,
    UpdateEndpointOutputTypeDef,
    UpdateEndpointWeightsAndCapacitiesOutputTypeDef,
    UpdateExperimentResponseTypeDef,
    UpdateFeatureGroupResponseTypeDef,
    UpdateHubResponseTypeDef,
    UpdateImageResponseTypeDef,
    UpdateImageVersionResponseTypeDef,
    UpdateInferenceComponentOutputTypeDef,
    UpdateInferenceComponentRuntimeConfigOutputTypeDef,
    UpdateInferenceExperimentResponseTypeDef,
    UpdateModelCardResponseTypeDef,
    UpdateModelPackageOutputTypeDef,
    UpdateMonitoringAlertResponseTypeDef,
    UpdateMonitoringScheduleResponseTypeDef,
    UpdatePipelineExecutionResponseTypeDef,
    UpdatePipelineResponseTypeDef,
    UpdateProjectOutputTypeDef,
    UpdateSpaceResponseTypeDef,
    UpdateTrainingJobResponseTypeDef,
    UpdateTrialComponentResponseTypeDef,
    UpdateTrialResponseTypeDef,
    UpdateUserProfileResponseTypeDef,
    UpdateWorkforceResponseTypeDef,
    UpdateWorkteamResponseTypeDef,
    UserSettingsTypeDef,
    VariantPropertyTypeDef,
    VisibilityConditionsTypeDef,
    VpcConfigTypeDef,
    WorkforceVpcConfigRequestTypeDef,
)
from .waiter import (
    EndpointDeletedWaiter,
    EndpointInServiceWaiter,
    ImageCreatedWaiter,
    ImageDeletedWaiter,
    ImageUpdatedWaiter,
    ImageVersionCreatedWaiter,
    ImageVersionDeletedWaiter,
    NotebookInstanceDeletedWaiter,
    NotebookInstanceInServiceWaiter,
    NotebookInstanceStoppedWaiter,
    ProcessingJobCompletedOrStoppedWaiter,
    TrainingJobCompletedOrStoppedWaiter,
    TransformJobCompletedOrStoppedWaiter,
)

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("SageMakerClient",)


class BotocoreClientError(Exception):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    ResourceInUse: Type[BotocoreClientError]
    ResourceLimitExceeded: Type[BotocoreClientError]
    ResourceNotFound: Type[BotocoreClientError]


class SageMakerClient(AioBaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        SageMakerClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.exceptions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#exceptions)
        """

    async def add_association(
        self, *, SourceArn: str, DestinationArn: str, AssociationType: AssociationEdgeTypeType = ...
    ) -> AddAssociationResponseTypeDef:
        """
        Creates an *association* between the source and the destination.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.add_association)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#add_association)
        """

    async def add_tags(
        self, *, ResourceArn: str, Tags: Sequence[TagTypeDef]
    ) -> AddTagsOutputTypeDef:
        """
        Adds or overwrites one or more tags for the specified SageMaker resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.add_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#add_tags)
        """

    async def associate_trial_component(
        self, *, TrialComponentName: str, TrialName: str
    ) -> AssociateTrialComponentResponseTypeDef:
        """
        Associates a trial component with a trial.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.associate_trial_component)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#associate_trial_component)
        """

    async def batch_describe_model_package(
        self, *, ModelPackageArnList: Sequence[str]
    ) -> BatchDescribeModelPackageOutputTypeDef:
        """
        This action batch describes a list of versioned model packages See also: [AWS
        API
        Documentation](https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/BatchDescribeModelPackage).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.batch_describe_model_package)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#batch_describe_model_package)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.can_paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#can_paginate)
        """

    async def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.close)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#close)
        """

    async def create_action(
        self,
        *,
        ActionName: str,
        Source: ActionSourceTypeDef,
        ActionType: str,
        Description: str = ...,
        Status: ActionStatusType = ...,
        Properties: Mapping[str, str] = ...,
        MetadataProperties: MetadataPropertiesTypeDef = ...,
        Tags: Sequence[TagTypeDef] = ...,
    ) -> CreateActionResponseTypeDef:
        """
        Creates an *action*.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_action)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#create_action)
        """

    async def create_algorithm(
        self,
        *,
        AlgorithmName: str,
        TrainingSpecification: TrainingSpecificationTypeDef,
        AlgorithmDescription: str = ...,
        InferenceSpecification: InferenceSpecificationTypeDef = ...,
        ValidationSpecification: AlgorithmValidationSpecificationTypeDef = ...,
        CertifyForMarketplace: bool = ...,
        Tags: Sequence[TagTypeDef] = ...,
    ) -> CreateAlgorithmOutputTypeDef:
        """
        Create a machine learning algorithm that you can use in SageMaker and list in
        the Amazon Web Services
        Marketplace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_algorithm)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#create_algorithm)
        """

    async def create_app(
        self,
        *,
        DomainId: str,
        AppType: AppTypeType,
        AppName: str,
        UserProfileName: str = ...,
        SpaceName: str = ...,
        Tags: Sequence[TagTypeDef] = ...,
        ResourceSpec: ResourceSpecTypeDef = ...,
    ) -> CreateAppResponseTypeDef:
        """
        Creates a running app for the specified UserProfile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_app)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#create_app)
        """

    async def create_app_image_config(
        self,
        *,
        AppImageConfigName: str,
        Tags: Sequence[TagTypeDef] = ...,
        KernelGatewayImageConfig: KernelGatewayImageConfigTypeDef = ...,
        JupyterLabAppImageConfig: JupyterLabAppImageConfigTypeDef = ...,
    ) -> CreateAppImageConfigResponseTypeDef:
        """
        Creates a configuration for running a SageMaker image as a KernelGateway app.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_app_image_config)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#create_app_image_config)
        """

    async def create_artifact(
        self,
        *,
        Source: ArtifactSourceTypeDef,
        ArtifactType: str,
        ArtifactName: str = ...,
        Properties: Mapping[str, str] = ...,
        MetadataProperties: MetadataPropertiesTypeDef = ...,
        Tags: Sequence[TagTypeDef] = ...,
    ) -> CreateArtifactResponseTypeDef:
        """
        Creates an *artifact*.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_artifact)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#create_artifact)
        """

    async def create_auto_ml_job(
        self,
        *,
        AutoMLJobName: str,
        InputDataConfig: Sequence[AutoMLChannelTypeDef],
        OutputDataConfig: AutoMLOutputDataConfigTypeDef,
        RoleArn: str,
        ProblemType: ProblemTypeType = ...,
        AutoMLJobObjective: AutoMLJobObjectiveTypeDef = ...,
        AutoMLJobConfig: AutoMLJobConfigTypeDef = ...,
        GenerateCandidateDefinitionsOnly: bool = ...,
        Tags: Sequence[TagTypeDef] = ...,
        ModelDeployConfig: ModelDeployConfigTypeDef = ...,
    ) -> CreateAutoMLJobResponseTypeDef:
        """
        Creates an Autopilot job also referred to as Autopilot experiment or AutoML job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_auto_ml_job)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#create_auto_ml_job)
        """

    async def create_auto_ml_job_v2(
        self,
        *,
        AutoMLJobName: str,
        AutoMLJobInputDataConfig: Sequence[AutoMLJobChannelTypeDef],
        OutputDataConfig: AutoMLOutputDataConfigTypeDef,
        AutoMLProblemTypeConfig: AutoMLProblemTypeConfigTypeDef,
        RoleArn: str,
        Tags: Sequence[TagTypeDef] = ...,
        SecurityConfig: AutoMLSecurityConfigTypeDef = ...,
        AutoMLJobObjective: AutoMLJobObjectiveTypeDef = ...,
        ModelDeployConfig: ModelDeployConfigTypeDef = ...,
        DataSplitConfig: AutoMLDataSplitConfigTypeDef = ...,
    ) -> CreateAutoMLJobV2ResponseTypeDef:
        """
        Creates an Autopilot job also referred to as Autopilot experiment or AutoML job
        V2.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_auto_ml_job_v2)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#create_auto_ml_job_v2)
        """

    async def create_cluster(
        self,
        *,
        ClusterName: str,
        InstanceGroups: Sequence[ClusterInstanceGroupSpecificationTypeDef],
        VpcConfig: VpcConfigTypeDef = ...,
        Tags: Sequence[TagTypeDef] = ...,
    ) -> CreateClusterResponseTypeDef:
        """
        Creates a SageMaker HyperPod cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_cluster)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#create_cluster)
        """

    async def create_code_repository(
        self,
        *,
        CodeRepositoryName: str,
        GitConfig: GitConfigTypeDef,
        Tags: Sequence[TagTypeDef] = ...,
    ) -> CreateCodeRepositoryOutputTypeDef:
        """
        Creates a Git repository as a resource in your SageMaker account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_code_repository)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#create_code_repository)
        """

    async def create_compilation_job(
        self,
        *,
        CompilationJobName: str,
        RoleArn: str,
        OutputConfig: OutputConfigTypeDef,
        StoppingCondition: StoppingConditionTypeDef,
        ModelPackageVersionArn: str = ...,
        InputConfig: InputConfigTypeDef = ...,
        VpcConfig: NeoVpcConfigTypeDef = ...,
        Tags: Sequence[TagTypeDef] = ...,
    ) -> CreateCompilationJobResponseTypeDef:
        """
        Starts a model compilation job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_compilation_job)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#create_compilation_job)
        """

    async def create_context(
        self,
        *,
        ContextName: str,
        Source: ContextSourceTypeDef,
        ContextType: str,
        Description: str = ...,
        Properties: Mapping[str, str] = ...,
        Tags: Sequence[TagTypeDef] = ...,
    ) -> CreateContextResponseTypeDef:
        """
        Creates a *context*.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_context)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#create_context)
        """

    async def create_data_quality_job_definition(
        self,
        *,
        JobDefinitionName: str,
        DataQualityAppSpecification: DataQualityAppSpecificationTypeDef,
        DataQualityJobInput: DataQualityJobInputTypeDef,
        DataQualityJobOutputConfig: MonitoringOutputConfigTypeDef,
        JobResources: MonitoringResourcesTypeDef,
        RoleArn: str,
        DataQualityBaselineConfig: DataQualityBaselineConfigTypeDef = ...,
        NetworkConfig: MonitoringNetworkConfigTypeDef = ...,
        StoppingCondition: MonitoringStoppingConditionTypeDef = ...,
        Tags: Sequence[TagTypeDef] = ...,
    ) -> CreateDataQualityJobDefinitionResponseTypeDef:
        """
        Creates a definition for a job that monitors data quality and drift.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_data_quality_job_definition)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#create_data_quality_job_definition)
        """

    async def create_device_fleet(
        self,
        *,
        DeviceFleetName: str,
        OutputConfig: EdgeOutputConfigTypeDef,
        RoleArn: str = ...,
        Description: str = ...,
        Tags: Sequence[TagTypeDef] = ...,
        EnableIotRoleAlias: bool = ...,
    ) -> EmptyResponseMetadataTypeDef:
        """
        Creates a device fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_device_fleet)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#create_device_fleet)
        """

    async def create_domain(
        self,
        *,
        DomainName: str,
        AuthMode: AuthModeType,
        DefaultUserSettings: UserSettingsTypeDef,
        SubnetIds: Sequence[str],
        VpcId: str,
        DomainSettings: DomainSettingsTypeDef = ...,
        Tags: Sequence[TagTypeDef] = ...,
        AppNetworkAccessType: AppNetworkAccessTypeType = ...,
        HomeEfsFileSystemKmsKeyId: str = ...,
        KmsKeyId: str = ...,
        AppSecurityGroupManagement: AppSecurityGroupManagementType = ...,
        DefaultSpaceSettings: DefaultSpaceSettingsTypeDef = ...,
    ) -> CreateDomainResponseTypeDef:
        """
        Creates a `Domain`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_domain)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#create_domain)
        """

    async def create_edge_deployment_plan(
        self,
        *,
        EdgeDeploymentPlanName: str,
        ModelConfigs: Sequence[EdgeDeploymentModelConfigTypeDef],
        DeviceFleetName: str,
        Stages: Sequence[DeploymentStageTypeDef] = ...,
        Tags: Sequence[TagTypeDef] = ...,
    ) -> CreateEdgeDeploymentPlanResponseTypeDef:
        """
        Creates an edge deployment plan, consisting of multiple stages.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_edge_deployment_plan)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#create_edge_deployment_plan)
        """

    async def create_edge_deployment_stage(
        self, *, EdgeDeploymentPlanName: str, Stages: Sequence[DeploymentStageTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Creates a new stage in an existing edge deployment plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_edge_deployment_stage)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#create_edge_deployment_stage)
        """

    async def create_edge_packaging_job(
        self,
        *,
        EdgePackagingJobName: str,
        CompilationJobName: str,
        ModelName: str,
        ModelVersion: str,
        RoleArn: str,
        OutputConfig: EdgeOutputConfigTypeDef,
        ResourceKey: str = ...,
        Tags: Sequence[TagTypeDef] = ...,
    ) -> EmptyResponseMetadataTypeDef:
        """
        Starts a SageMaker Edge Manager model packaging job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_edge_packaging_job)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#create_edge_packaging_job)
        """

    async def create_endpoint(
        self,
        *,
        EndpointName: str,
        EndpointConfigName: str,
        DeploymentConfig: DeploymentConfigTypeDef = ...,
        Tags: Sequence[TagTypeDef] = ...,
    ) -> CreateEndpointOutputTypeDef:
        """
        Creates an endpoint using the endpoint configuration specified in the request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_endpoint)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#create_endpoint)
        """

    async def create_endpoint_config(
        self,
        *,
        EndpointConfigName: str,
        ProductionVariants: Sequence[ProductionVariantTypeDef],
        DataCaptureConfig: DataCaptureConfigTypeDef = ...,
        Tags: Sequence[TagTypeDef] = ...,
        KmsKeyId: str = ...,
        AsyncInferenceConfig: AsyncInferenceConfigTypeDef = ...,
        ExplainerConfig: ExplainerConfigTypeDef = ...,
        ShadowProductionVariants: Sequence[ProductionVariantTypeDef] = ...,
        ExecutionRoleArn: str = ...,
        VpcConfig: VpcConfigTypeDef = ...,
        EnableNetworkIsolation: bool = ...,
    ) -> CreateEndpointConfigOutputTypeDef:
        """
        Creates an endpoint configuration that SageMaker hosting services uses to
        deploy
        models.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_endpoint_config)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#create_endpoint_config)
        """

    async def create_experiment(
        self,
        *,
        ExperimentName: str,
        DisplayName: str = ...,
        Description: str = ...,
        Tags: Sequence[TagTypeDef] = ...,
    ) -> CreateExperimentResponseTypeDef:
        """
        Creates a SageMaker *experiment*.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_experiment)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#create_experiment)
        """

    async def create_feature_group(
        self,
        *,
        FeatureGroupName: str,
        RecordIdentifierFeatureName: str,
        EventTimeFeatureName: str,
        FeatureDefinitions: Sequence[FeatureDefinitionTypeDef],
        OnlineStoreConfig: OnlineStoreConfigTypeDef = ...,
        OfflineStoreConfig: OfflineStoreConfigTypeDef = ...,
        ThroughputConfig: ThroughputConfigTypeDef = ...,
        RoleArn: str = ...,
        Description: str = ...,
        Tags: Sequence[TagTypeDef] = ...,
    ) -> CreateFeatureGroupResponseTypeDef:
        """
        Create a new `FeatureGroup`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_feature_group)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#create_feature_group)
        """

    async def create_flow_definition(
        self,
        *,
        FlowDefinitionName: str,
        OutputConfig: FlowDefinitionOutputConfigTypeDef,
        RoleArn: str,
        HumanLoopRequestSource: HumanLoopRequestSourceTypeDef = ...,
        HumanLoopActivationConfig: HumanLoopActivationConfigTypeDef = ...,
        HumanLoopConfig: HumanLoopConfigTypeDef = ...,
        Tags: Sequence[TagTypeDef] = ...,
    ) -> CreateFlowDefinitionResponseTypeDef:
        """
        Creates a flow definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_flow_definition)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#create_flow_definition)
        """

    async def create_hub(
        self,
        *,
        HubName: str,
        HubDescription: str,
        HubDisplayName: str = ...,
        HubSearchKeywords: Sequence[str] = ...,
        S3StorageConfig: HubS3StorageConfigTypeDef = ...,
        Tags: Sequence[TagTypeDef] = ...,
    ) -> CreateHubResponseTypeDef:
        """
        Create a hub.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_hub)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#create_hub)
        """

    async def create_human_task_ui(
        self,
        *,
        HumanTaskUiName: str,
        UiTemplate: UiTemplateTypeDef,
        Tags: Sequence[TagTypeDef] = ...,
    ) -> CreateHumanTaskUiResponseTypeDef:
        """
        Defines the settings you will use for the human review workflow user interface.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_human_task_ui)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#create_human_task_ui)
        """

    async def create_hyper_parameter_tuning_job(
        self,
        *,
        HyperParameterTuningJobName: str,
        HyperParameterTuningJobConfig: HyperParameterTuningJobConfigTypeDef,
        TrainingJobDefinition: HyperParameterTrainingJobDefinitionTypeDef = ...,
        TrainingJobDefinitions: Sequence[HyperParameterTrainingJobDefinitionTypeDef] = ...,
        WarmStartConfig: HyperParameterTuningJobWarmStartConfigTypeDef = ...,
        Tags: Sequence[TagTypeDef] = ...,
        Autotune: AutotuneTypeDef = ...,
    ) -> CreateHyperParameterTuningJobResponseTypeDef:
        """
        Starts a hyperparameter tuning job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_hyper_parameter_tuning_job)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#create_hyper_parameter_tuning_job)
        """

    async def create_image(
        self,
        *,
        ImageName: str,
        RoleArn: str,
        Description: str = ...,
        DisplayName: str = ...,
        Tags: Sequence[TagTypeDef] = ...,
    ) -> CreateImageResponseTypeDef:
        """
        Creates a custom SageMaker image.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_image)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#create_image)
        """

    async def create_image_version(
        self,
        *,
        BaseImage: str,
        ClientToken: str,
        ImageName: str,
        Aliases: Sequence[str] = ...,
        VendorGuidance: VendorGuidanceType = ...,
        JobType: JobTypeType = ...,
        MLFramework: str = ...,
        ProgrammingLang: str = ...,
        Processor: ProcessorType = ...,
        Horovod: bool = ...,
        ReleaseNotes: str = ...,
    ) -> CreateImageVersionResponseTypeDef:
        """
        Creates a version of the SageMaker image specified by `ImageName`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_image_version)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#create_image_version)
        """

    async def create_inference_component(
        self,
        *,
        InferenceComponentName: str,
        EndpointName: str,
        VariantName: str,
        Specification: InferenceComponentSpecificationTypeDef,
        RuntimeConfig: InferenceComponentRuntimeConfigTypeDef,
        Tags: Sequence[TagTypeDef] = ...,
    ) -> CreateInferenceComponentOutputTypeDef:
        """
        Creates an inference component, which is a SageMaker hosting object that you
        can use to deploy a model to an
        endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_inference_component)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#create_inference_component)
        """

    async def create_inference_experiment(
        self,
        *,
        Name: str,
        Type: Literal["ShadowMode"],
        RoleArn: str,
        EndpointName: str,
        ModelVariants: Sequence[ModelVariantConfigTypeDef],
        ShadowModeConfig: ShadowModeConfigTypeDef,
        Schedule: InferenceExperimentScheduleTypeDef = ...,
        Description: str = ...,
        DataStorageConfig: InferenceExperimentDataStorageConfigTypeDef = ...,
        KmsKey: str = ...,
        Tags: Sequence[TagTypeDef] = ...,
    ) -> CreateInferenceExperimentResponseTypeDef:
        """
        Creates an inference experiment using the configurations specified in the
        request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_inference_experiment)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#create_inference_experiment)
        """

    async def create_inference_recommendations_job(
        self,
        *,
        JobName: str,
        JobType: RecommendationJobTypeType,
        RoleArn: str,
        InputConfig: RecommendationJobInputConfigTypeDef,
        JobDescription: str = ...,
        StoppingConditions: RecommendationJobStoppingConditionsTypeDef = ...,
        OutputConfig: RecommendationJobOutputConfigTypeDef = ...,
        Tags: Sequence[TagTypeDef] = ...,
    ) -> CreateInferenceRecommendationsJobResponseTypeDef:
        """
        Starts a recommendation job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_inference_recommendations_job)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#create_inference_recommendations_job)
        """

    async def create_labeling_job(
        self,
        *,
        LabelingJobName: str,
        LabelAttributeName: str,
        InputConfig: LabelingJobInputConfigTypeDef,
        OutputConfig: LabelingJobOutputConfigTypeDef,
        RoleArn: str,
        HumanTaskConfig: HumanTaskConfigTypeDef,
        LabelCategoryConfigS3Uri: str = ...,
        StoppingConditions: LabelingJobStoppingConditionsTypeDef = ...,
        LabelingJobAlgorithmsConfig: LabelingJobAlgorithmsConfigTypeDef = ...,
        Tags: Sequence[TagTypeDef] = ...,
    ) -> CreateLabelingJobResponseTypeDef:
        """
        Creates a job that uses workers to label the data objects in your input dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_labeling_job)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#create_labeling_job)
        """

    async def create_model(
        self,
        *,
        ModelName: str,
        PrimaryContainer: ContainerDefinitionTypeDef = ...,
        Containers: Sequence[ContainerDefinitionTypeDef] = ...,
        InferenceExecutionConfig: InferenceExecutionConfigTypeDef = ...,
        ExecutionRoleArn: str = ...,
        Tags: Sequence[TagTypeDef] = ...,
        VpcConfig: VpcConfigTypeDef = ...,
        EnableNetworkIsolation: bool = ...,
    ) -> CreateModelOutputTypeDef:
        """
        Creates a model in SageMaker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_model)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#create_model)
        """

    async def create_model_bias_job_definition(
        self,
        *,
        JobDefinitionName: str,
        ModelBiasAppSpecification: ModelBiasAppSpecificationTypeDef,
        ModelBiasJobInput: ModelBiasJobInputTypeDef,
        ModelBiasJobOutputConfig: MonitoringOutputConfigTypeDef,
        JobResources: MonitoringResourcesTypeDef,
        RoleArn: str,
        ModelBiasBaselineConfig: ModelBiasBaselineConfigTypeDef = ...,
        NetworkConfig: MonitoringNetworkConfigTypeDef = ...,
        StoppingCondition: MonitoringStoppingConditionTypeDef = ...,
        Tags: Sequence[TagTypeDef] = ...,
    ) -> CreateModelBiasJobDefinitionResponseTypeDef:
        """
        Creates the definition for a model bias job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_model_bias_job_definition)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#create_model_bias_job_definition)
        """

    async def create_model_card(
        self,
        *,
        ModelCardName: str,
        Content: str,
        ModelCardStatus: ModelCardStatusType,
        SecurityConfig: ModelCardSecurityConfigTypeDef = ...,
        Tags: Sequence[TagTypeDef] = ...,
    ) -> CreateModelCardResponseTypeDef:
        """
        Creates an Amazon SageMaker Model Card.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_model_card)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#create_model_card)
        """

    async def create_model_card_export_job(
        self,
        *,
        ModelCardName: str,
        ModelCardExportJobName: str,
        OutputConfig: ModelCardExportOutputConfigTypeDef,
        ModelCardVersion: int = ...,
    ) -> CreateModelCardExportJobResponseTypeDef:
        """
        Creates an Amazon SageMaker Model Card export job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_model_card_export_job)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#create_model_card_export_job)
        """

    async def create_model_explainability_job_definition(
        self,
        *,
        JobDefinitionName: str,
        ModelExplainabilityAppSpecification: ModelExplainabilityAppSpecificationTypeDef,
        ModelExplainabilityJobInput: ModelExplainabilityJobInputTypeDef,
        ModelExplainabilityJobOutputConfig: MonitoringOutputConfigTypeDef,
        JobResources: MonitoringResourcesTypeDef,
        RoleArn: str,
        ModelExplainabilityBaselineConfig: ModelExplainabilityBaselineConfigTypeDef = ...,
        NetworkConfig: MonitoringNetworkConfigTypeDef = ...,
        StoppingCondition: MonitoringStoppingConditionTypeDef = ...,
        Tags: Sequence[TagTypeDef] = ...,
    ) -> CreateModelExplainabilityJobDefinitionResponseTypeDef:
        """
        Creates the definition for a model explainability job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_model_explainability_job_definition)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#create_model_explainability_job_definition)
        """

    async def create_model_package(
        self,
        *,
        ModelPackageName: str = ...,
        ModelPackageGroupName: str = ...,
        ModelPackageDescription: str = ...,
        InferenceSpecification: InferenceSpecificationTypeDef = ...,
        ValidationSpecification: ModelPackageValidationSpecificationTypeDef = ...,
        SourceAlgorithmSpecification: SourceAlgorithmSpecificationTypeDef = ...,
        CertifyForMarketplace: bool = ...,
        Tags: Sequence[TagTypeDef] = ...,
        ModelApprovalStatus: ModelApprovalStatusType = ...,
        MetadataProperties: MetadataPropertiesTypeDef = ...,
        ModelMetrics: ModelMetricsTypeDef = ...,
        ClientToken: str = ...,
        Domain: str = ...,
        Task: str = ...,
        SamplePayloadUrl: str = ...,
        CustomerMetadataProperties: Mapping[str, str] = ...,
        DriftCheckBaselines: DriftCheckBaselinesTypeDef = ...,
        AdditionalInferenceSpecifications: Sequence[
            AdditionalInferenceSpecificationDefinitionTypeDef
        ] = ...,
        SkipModelValidation: SkipModelValidationType = ...,
    ) -> CreateModelPackageOutputTypeDef:
        """
        Creates a model package that you can use to create SageMaker models or list on
        Amazon Web Services Marketplace, or a versioned model that is part of a model
        group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_model_package)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#create_model_package)
        """

    async def create_model_package_group(
        self,
        *,
        ModelPackageGroupName: str,
        ModelPackageGroupDescription: str = ...,
        Tags: Sequence[TagTypeDef] = ...,
    ) -> CreateModelPackageGroupOutputTypeDef:
        """
        Creates a model group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_model_package_group)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#create_model_package_group)
        """

    async def create_model_quality_job_definition(
        self,
        *,
        JobDefinitionName: str,
        ModelQualityAppSpecification: ModelQualityAppSpecificationTypeDef,
        ModelQualityJobInput: ModelQualityJobInputTypeDef,
        ModelQualityJobOutputConfig: MonitoringOutputConfigTypeDef,
        JobResources: MonitoringResourcesTypeDef,
        RoleArn: str,
        ModelQualityBaselineConfig: ModelQualityBaselineConfigTypeDef = ...,
        NetworkConfig: MonitoringNetworkConfigTypeDef = ...,
        StoppingCondition: MonitoringStoppingConditionTypeDef = ...,
        Tags: Sequence[TagTypeDef] = ...,
    ) -> CreateModelQualityJobDefinitionResponseTypeDef:
        """
        Creates a definition for a job that monitors model quality and drift.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_model_quality_job_definition)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#create_model_quality_job_definition)
        """

    async def create_monitoring_schedule(
        self,
        *,
        MonitoringScheduleName: str,
        MonitoringScheduleConfig: MonitoringScheduleConfigTypeDef,
        Tags: Sequence[TagTypeDef] = ...,
    ) -> CreateMonitoringScheduleResponseTypeDef:
        """
        Creates a schedule that regularly starts Amazon SageMaker Processing Jobs to
        monitor the data captured for an Amazon SageMaker
        Endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_monitoring_schedule)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#create_monitoring_schedule)
        """

    async def create_notebook_instance(
        self,
        *,
        NotebookInstanceName: str,
        InstanceType: InstanceTypeType,
        RoleArn: str,
        SubnetId: str = ...,
        SecurityGroupIds: Sequence[str] = ...,
        KmsKeyId: str = ...,
        Tags: Sequence[TagTypeDef] = ...,
        LifecycleConfigName: str = ...,
        DirectInternetAccess: DirectInternetAccessType = ...,
        VolumeSizeInGB: int = ...,
        AcceleratorTypes: Sequence[NotebookInstanceAcceleratorTypeType] = ...,
        DefaultCodeRepository: str = ...,
        AdditionalCodeRepositories: Sequence[str] = ...,
        RootAccess: RootAccessType = ...,
        PlatformIdentifier: str = ...,
        InstanceMetadataServiceConfiguration: InstanceMetadataServiceConfigurationTypeDef = ...,
    ) -> CreateNotebookInstanceOutputTypeDef:
        """
        Creates an SageMaker notebook instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_notebook_instance)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#create_notebook_instance)
        """

    async def create_notebook_instance_lifecycle_config(
        self,
        *,
        NotebookInstanceLifecycleConfigName: str,
        OnCreate: Sequence[NotebookInstanceLifecycleHookTypeDef] = ...,
        OnStart: Sequence[NotebookInstanceLifecycleHookTypeDef] = ...,
    ) -> CreateNotebookInstanceLifecycleConfigOutputTypeDef:
        """
        Creates a lifecycle configuration that you can associate with a notebook
        instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_notebook_instance_lifecycle_config)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#create_notebook_instance_lifecycle_config)
        """

    async def create_pipeline(
        self,
        *,
        PipelineName: str,
        ClientRequestToken: str,
        RoleArn: str,
        PipelineDisplayName: str = ...,
        PipelineDefinition: str = ...,
        PipelineDefinitionS3Location: PipelineDefinitionS3LocationTypeDef = ...,
        PipelineDescription: str = ...,
        Tags: Sequence[TagTypeDef] = ...,
        ParallelismConfiguration: ParallelismConfigurationTypeDef = ...,
    ) -> CreatePipelineResponseTypeDef:
        """
        Creates a pipeline using a JSON pipeline definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_pipeline)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#create_pipeline)
        """

    async def create_presigned_domain_url(
        self,
        *,
        DomainId: str,
        UserProfileName: str,
        SessionExpirationDurationInSeconds: int = ...,
        ExpiresInSeconds: int = ...,
        SpaceName: str = ...,
        LandingUri: str = ...,
    ) -> CreatePresignedDomainUrlResponseTypeDef:
        """
        Creates a URL for a specified UserProfile in a Domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_presigned_domain_url)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#create_presigned_domain_url)
        """

    async def create_presigned_notebook_instance_url(
        self, *, NotebookInstanceName: str, SessionExpirationDurationInSeconds: int = ...
    ) -> CreatePresignedNotebookInstanceUrlOutputTypeDef:
        """
        Returns a URL that you can use to connect to the Jupyter server from a notebook
        instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_presigned_notebook_instance_url)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#create_presigned_notebook_instance_url)
        """

    async def create_processing_job(
        self,
        *,
        ProcessingJobName: str,
        ProcessingResources: ProcessingResourcesTypeDef,
        AppSpecification: AppSpecificationTypeDef,
        RoleArn: str,
        ProcessingInputs: Sequence[ProcessingInputTypeDef] = ...,
        ProcessingOutputConfig: ProcessingOutputConfigTypeDef = ...,
        StoppingCondition: ProcessingStoppingConditionTypeDef = ...,
        Environment: Mapping[str, str] = ...,
        NetworkConfig: NetworkConfigTypeDef = ...,
        Tags: Sequence[TagTypeDef] = ...,
        ExperimentConfig: ExperimentConfigTypeDef = ...,
    ) -> CreateProcessingJobResponseTypeDef:
        """
        Creates a processing job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_processing_job)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#create_processing_job)
        """

    async def create_project(
        self,
        *,
        ProjectName: str,
        ServiceCatalogProvisioningDetails: ServiceCatalogProvisioningDetailsTypeDef,
        ProjectDescription: str = ...,
        Tags: Sequence[TagTypeDef] = ...,
    ) -> CreateProjectOutputTypeDef:
        """
        Creates a machine learning (ML) project that can contain one or more templates
        that set up an ML pipeline from training to deploying an approved
        model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_project)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#create_project)
        """

    async def create_space(
        self,
        *,
        DomainId: str,
        SpaceName: str,
        Tags: Sequence[TagTypeDef] = ...,
        SpaceSettings: SpaceSettingsTypeDef = ...,
        OwnershipSettings: OwnershipSettingsTypeDef = ...,
        SpaceSharingSettings: SpaceSharingSettingsTypeDef = ...,
        SpaceDisplayName: str = ...,
    ) -> CreateSpaceResponseTypeDef:
        """
        Creates a space used for real time collaboration in a domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_space)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#create_space)
        """

    async def create_studio_lifecycle_config(
        self,
        *,
        StudioLifecycleConfigName: str,
        StudioLifecycleConfigContent: str,
        StudioLifecycleConfigAppType: StudioLifecycleConfigAppTypeType,
        Tags: Sequence[TagTypeDef] = ...,
    ) -> CreateStudioLifecycleConfigResponseTypeDef:
        """
        Creates a new Amazon SageMaker Studio Lifecycle Configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_studio_lifecycle_config)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#create_studio_lifecycle_config)
        """

    async def create_training_job(
        self,
        *,
        TrainingJobName: str,
        AlgorithmSpecification: AlgorithmSpecificationTypeDef,
        RoleArn: str,
        OutputDataConfig: OutputDataConfigTypeDef,
        ResourceConfig: ResourceConfigTypeDef,
        StoppingCondition: StoppingConditionTypeDef,
        HyperParameters: Mapping[str, str] = ...,
        InputDataConfig: Sequence[ChannelTypeDef] = ...,
        VpcConfig: VpcConfigTypeDef = ...,
        Tags: Sequence[TagTypeDef] = ...,
        EnableNetworkIsolation: bool = ...,
        EnableInterContainerTrafficEncryption: bool = ...,
        EnableManagedSpotTraining: bool = ...,
        CheckpointConfig: CheckpointConfigTypeDef = ...,
        DebugHookConfig: DebugHookConfigTypeDef = ...,
        DebugRuleConfigurations: Sequence[DebugRuleConfigurationTypeDef] = ...,
        TensorBoardOutputConfig: TensorBoardOutputConfigTypeDef = ...,
        ExperimentConfig: ExperimentConfigTypeDef = ...,
        ProfilerConfig: ProfilerConfigTypeDef = ...,
        ProfilerRuleConfigurations: Sequence[ProfilerRuleConfigurationTypeDef] = ...,
        Environment: Mapping[str, str] = ...,
        RetryStrategy: RetryStrategyTypeDef = ...,
        RemoteDebugConfig: RemoteDebugConfigTypeDef = ...,
        InfraCheckConfig: InfraCheckConfigTypeDef = ...,
    ) -> CreateTrainingJobResponseTypeDef:
        """
        Starts a model training job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_training_job)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#create_training_job)
        """

    async def create_transform_job(
        self,
        *,
        TransformJobName: str,
        ModelName: str,
        TransformInput: TransformInputTypeDef,
        TransformOutput: TransformOutputTypeDef,
        TransformResources: TransformResourcesTypeDef,
        MaxConcurrentTransforms: int = ...,
        ModelClientConfig: ModelClientConfigTypeDef = ...,
        MaxPayloadInMB: int = ...,
        BatchStrategy: BatchStrategyType = ...,
        Environment: Mapping[str, str] = ...,
        DataCaptureConfig: BatchDataCaptureConfigTypeDef = ...,
        DataProcessing: DataProcessingTypeDef = ...,
        Tags: Sequence[TagTypeDef] = ...,
        ExperimentConfig: ExperimentConfigTypeDef = ...,
    ) -> CreateTransformJobResponseTypeDef:
        """
        Starts a transform job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_transform_job)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#create_transform_job)
        """

    async def create_trial(
        self,
        *,
        TrialName: str,
        ExperimentName: str,
        DisplayName: str = ...,
        MetadataProperties: MetadataPropertiesTypeDef = ...,
        Tags: Sequence[TagTypeDef] = ...,
    ) -> CreateTrialResponseTypeDef:
        """
        Creates an SageMaker *trial*.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_trial)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#create_trial)
        """

    async def create_trial_component(
        self,
        *,
        TrialComponentName: str,
        DisplayName: str = ...,
        Status: TrialComponentStatusTypeDef = ...,
        StartTime: TimestampTypeDef = ...,
        EndTime: TimestampTypeDef = ...,
        Parameters: Mapping[str, TrialComponentParameterValueTypeDef] = ...,
        InputArtifacts: Mapping[str, TrialComponentArtifactTypeDef] = ...,
        OutputArtifacts: Mapping[str, TrialComponentArtifactTypeDef] = ...,
        MetadataProperties: MetadataPropertiesTypeDef = ...,
        Tags: Sequence[TagTypeDef] = ...,
    ) -> CreateTrialComponentResponseTypeDef:
        """
        Creates a *trial component*, which is a stage of a machine learning *trial*.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_trial_component)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#create_trial_component)
        """

    async def create_user_profile(
        self,
        *,
        DomainId: str,
        UserProfileName: str,
        SingleSignOnUserIdentifier: str = ...,
        SingleSignOnUserValue: str = ...,
        Tags: Sequence[TagTypeDef] = ...,
        UserSettings: UserSettingsTypeDef = ...,
    ) -> CreateUserProfileResponseTypeDef:
        """
        Creates a user profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_user_profile)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#create_user_profile)
        """

    async def create_workforce(
        self,
        *,
        WorkforceName: str,
        CognitoConfig: CognitoConfigTypeDef = ...,
        OidcConfig: OidcConfigTypeDef = ...,
        SourceIpConfig: SourceIpConfigTypeDef = ...,
        Tags: Sequence[TagTypeDef] = ...,
        WorkforceVpcConfig: WorkforceVpcConfigRequestTypeDef = ...,
    ) -> CreateWorkforceResponseTypeDef:
        """
        Use this operation to create a workforce.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_workforce)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#create_workforce)
        """

    async def create_workteam(
        self,
        *,
        WorkteamName: str,
        MemberDefinitions: Sequence[MemberDefinitionTypeDef],
        Description: str,
        WorkforceName: str = ...,
        NotificationConfiguration: NotificationConfigurationTypeDef = ...,
        Tags: Sequence[TagTypeDef] = ...,
    ) -> CreateWorkteamResponseTypeDef:
        """
        Creates a new work team for labeling your data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_workteam)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#create_workteam)
        """

    async def delete_action(self, *, ActionName: str) -> DeleteActionResponseTypeDef:
        """
        Deletes an action.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_action)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#delete_action)
        """

    async def delete_algorithm(self, *, AlgorithmName: str) -> EmptyResponseMetadataTypeDef:
        """
        Removes the specified algorithm from your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_algorithm)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#delete_algorithm)
        """

    async def delete_app(
        self,
        *,
        DomainId: str,
        AppType: AppTypeType,
        AppName: str,
        UserProfileName: str = ...,
        SpaceName: str = ...,
    ) -> EmptyResponseMetadataTypeDef:
        """
        Used to stop and delete an app.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_app)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#delete_app)
        """

    async def delete_app_image_config(
        self, *, AppImageConfigName: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes an AppImageConfig.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_app_image_config)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#delete_app_image_config)
        """

    async def delete_artifact(
        self, *, ArtifactArn: str = ..., Source: ArtifactSourceTypeDef = ...
    ) -> DeleteArtifactResponseTypeDef:
        """
        Deletes an artifact.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_artifact)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#delete_artifact)
        """

    async def delete_association(
        self, *, SourceArn: str, DestinationArn: str
    ) -> DeleteAssociationResponseTypeDef:
        """
        Deletes an association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_association)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#delete_association)
        """

    async def delete_cluster(self, *, ClusterName: str) -> DeleteClusterResponseTypeDef:
        """
        Delete a SageMaker HyperPod cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_cluster)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#delete_cluster)
        """

    async def delete_code_repository(
        self, *, CodeRepositoryName: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified Git repository from your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_code_repository)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#delete_code_repository)
        """

    async def delete_compilation_job(
        self, *, CompilationJobName: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified compilation job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_compilation_job)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#delete_compilation_job)
        """

    async def delete_context(self, *, ContextName: str) -> DeleteContextResponseTypeDef:
        """
        Deletes an context.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_context)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#delete_context)
        """

    async def delete_data_quality_job_definition(
        self, *, JobDefinitionName: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a data quality monitoring job definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_data_quality_job_definition)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#delete_data_quality_job_definition)
        """

    async def delete_device_fleet(self, *, DeviceFleetName: str) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_device_fleet)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#delete_device_fleet)
        """

    async def delete_domain(
        self, *, DomainId: str, RetentionPolicy: RetentionPolicyTypeDef = ...
    ) -> EmptyResponseMetadataTypeDef:
        """
        Used to delete a domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_domain)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#delete_domain)
        """

    async def delete_edge_deployment_plan(
        self, *, EdgeDeploymentPlanName: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes an edge deployment plan if (and only if) all the stages in the plan are
        inactive or there are no stages in the
        plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_edge_deployment_plan)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#delete_edge_deployment_plan)
        """

    async def delete_edge_deployment_stage(
        self, *, EdgeDeploymentPlanName: str, StageName: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Delete a stage in an edge deployment plan if (and only if) the stage is
        inactive.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_edge_deployment_stage)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#delete_edge_deployment_stage)
        """

    async def delete_endpoint(self, *, EndpointName: str) -> EmptyResponseMetadataTypeDef:
        """
        Deletes an endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_endpoint)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#delete_endpoint)
        """

    async def delete_endpoint_config(
        self, *, EndpointConfigName: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes an endpoint configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_endpoint_config)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#delete_endpoint_config)
        """

    async def delete_experiment(self, *, ExperimentName: str) -> DeleteExperimentResponseTypeDef:
        """
        Deletes an SageMaker experiment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_experiment)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#delete_experiment)
        """

    async def delete_feature_group(self, *, FeatureGroupName: str) -> EmptyResponseMetadataTypeDef:
        """
        Delete the `FeatureGroup` and any data that was written to the `OnlineStore` of
        the
        `FeatureGroup`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_feature_group)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#delete_feature_group)
        """

    async def delete_flow_definition(self, *, FlowDefinitionName: str) -> Dict[str, Any]:
        """
        Deletes the specified flow definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_flow_definition)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#delete_flow_definition)
        """

    async def delete_hub(self, *, HubName: str) -> EmptyResponseMetadataTypeDef:
        """
        Delete a hub.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_hub)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#delete_hub)
        """

    async def delete_hub_content(
        self,
        *,
        HubName: str,
        HubContentType: HubContentTypeType,
        HubContentName: str,
        HubContentVersion: str,
    ) -> EmptyResponseMetadataTypeDef:
        """
        Delete the contents of a hub.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_hub_content)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#delete_hub_content)
        """

    async def delete_human_task_ui(self, *, HumanTaskUiName: str) -> Dict[str, Any]:
        """
        Use this operation to delete a human task user interface (worker task template).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_human_task_ui)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#delete_human_task_ui)
        """

    async def delete_hyper_parameter_tuning_job(
        self, *, HyperParameterTuningJobName: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a hyperparameter tuning job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_hyper_parameter_tuning_job)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#delete_hyper_parameter_tuning_job)
        """

    async def delete_image(self, *, ImageName: str) -> Dict[str, Any]:
        """
        Deletes a SageMaker image and all versions of the image.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_image)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#delete_image)
        """

    async def delete_image_version(
        self, *, ImageName: str, Version: int = ..., Alias: str = ...
    ) -> Dict[str, Any]:
        """
        Deletes a version of a SageMaker image.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_image_version)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#delete_image_version)
        """

    async def delete_inference_component(
        self, *, InferenceComponentName: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes an inference component.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_inference_component)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#delete_inference_component)
        """

    async def delete_inference_experiment(
        self, *, Name: str
    ) -> DeleteInferenceExperimentResponseTypeDef:
        """
        Deletes an inference experiment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_inference_experiment)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#delete_inference_experiment)
        """

    async def delete_model(self, *, ModelName: str) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_model)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#delete_model)
        """

    async def delete_model_bias_job_definition(
        self, *, JobDefinitionName: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes an Amazon SageMaker model bias job definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_model_bias_job_definition)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#delete_model_bias_job_definition)
        """

    async def delete_model_card(self, *, ModelCardName: str) -> EmptyResponseMetadataTypeDef:
        """
        Deletes an Amazon SageMaker Model Card.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_model_card)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#delete_model_card)
        """

    async def delete_model_explainability_job_definition(
        self, *, JobDefinitionName: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes an Amazon SageMaker model explainability job definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_model_explainability_job_definition)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#delete_model_explainability_job_definition)
        """

    async def delete_model_package(self, *, ModelPackageName: str) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a model package.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_model_package)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#delete_model_package)
        """

    async def delete_model_package_group(
        self, *, ModelPackageGroupName: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified model group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_model_package_group)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#delete_model_package_group)
        """

    async def delete_model_package_group_policy(
        self, *, ModelPackageGroupName: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a model group resource policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_model_package_group_policy)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#delete_model_package_group_policy)
        """

    async def delete_model_quality_job_definition(
        self, *, JobDefinitionName: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the secified model quality monitoring job definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_model_quality_job_definition)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#delete_model_quality_job_definition)
        """

    async def delete_monitoring_schedule(
        self, *, MonitoringScheduleName: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a monitoring schedule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_monitoring_schedule)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#delete_monitoring_schedule)
        """

    async def delete_notebook_instance(
        self, *, NotebookInstanceName: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes an SageMaker notebook instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_notebook_instance)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#delete_notebook_instance)
        """

    async def delete_notebook_instance_lifecycle_config(
        self, *, NotebookInstanceLifecycleConfigName: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a notebook instance lifecycle configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_notebook_instance_lifecycle_config)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#delete_notebook_instance_lifecycle_config)
        """

    async def delete_pipeline(
        self, *, PipelineName: str, ClientRequestToken: str
    ) -> DeletePipelineResponseTypeDef:
        """
        Deletes a pipeline if there are no running instances of the pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_pipeline)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#delete_pipeline)
        """

    async def delete_project(self, *, ProjectName: str) -> EmptyResponseMetadataTypeDef:
        """
        Delete the specified project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_project)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#delete_project)
        """

    async def delete_space(self, *, DomainId: str, SpaceName: str) -> EmptyResponseMetadataTypeDef:
        """
        Used to delete a space.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_space)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#delete_space)
        """

    async def delete_studio_lifecycle_config(
        self, *, StudioLifecycleConfigName: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the Amazon SageMaker Studio Lifecycle Configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_studio_lifecycle_config)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#delete_studio_lifecycle_config)
        """

    async def delete_tags(self, *, ResourceArn: str, TagKeys: Sequence[str]) -> Dict[str, Any]:
        """
        Deletes the specified tags from an SageMaker resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#delete_tags)
        """

    async def delete_trial(self, *, TrialName: str) -> DeleteTrialResponseTypeDef:
        """
        Deletes the specified trial.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_trial)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#delete_trial)
        """

    async def delete_trial_component(
        self, *, TrialComponentName: str
    ) -> DeleteTrialComponentResponseTypeDef:
        """
        Deletes the specified trial component.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_trial_component)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#delete_trial_component)
        """

    async def delete_user_profile(
        self, *, DomainId: str, UserProfileName: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a user profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_user_profile)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#delete_user_profile)
        """

    async def delete_workforce(self, *, WorkforceName: str) -> Dict[str, Any]:
        """
        Use this operation to delete a workforce.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_workforce)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#delete_workforce)
        """

    async def delete_workteam(self, *, WorkteamName: str) -> DeleteWorkteamResponseTypeDef:
        """
        Deletes an existing work team.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_workteam)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#delete_workteam)
        """

    async def deregister_devices(
        self, *, DeviceFleetName: str, DeviceNames: Sequence[str]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deregisters the specified devices.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.deregister_devices)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#deregister_devices)
        """

    async def describe_action(self, *, ActionName: str) -> DescribeActionResponseTypeDef:
        """
        Describes an action.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_action)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#describe_action)
        """

    async def describe_algorithm(self, *, AlgorithmName: str) -> DescribeAlgorithmOutputTypeDef:
        """
        Returns a description of the specified algorithm that is in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_algorithm)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#describe_algorithm)
        """

    async def describe_app(
        self,
        *,
        DomainId: str,
        AppType: AppTypeType,
        AppName: str,
        UserProfileName: str = ...,
        SpaceName: str = ...,
    ) -> DescribeAppResponseTypeDef:
        """
        Describes the app.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_app)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#describe_app)
        """

    async def describe_app_image_config(
        self, *, AppImageConfigName: str
    ) -> DescribeAppImageConfigResponseTypeDef:
        """
        Describes an AppImageConfig.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_app_image_config)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#describe_app_image_config)
        """

    async def describe_artifact(self, *, ArtifactArn: str) -> DescribeArtifactResponseTypeDef:
        """
        Describes an artifact.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_artifact)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#describe_artifact)
        """

    async def describe_auto_ml_job(self, *, AutoMLJobName: str) -> DescribeAutoMLJobResponseTypeDef:
        """
        Returns information about an AutoML job created by calling
        [CreateAutoMLJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateAutoMLJob.html).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_auto_ml_job)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#describe_auto_ml_job)
        """

    async def describe_auto_ml_job_v2(
        self, *, AutoMLJobName: str
    ) -> DescribeAutoMLJobV2ResponseTypeDef:
        """
        Returns information about an AutoML job created by calling
        [CreateAutoMLJobV2](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateAutoMLJobV2.html)
        or
        [CreateAutoMLJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateAutoMLJob.html).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_auto_ml_job_v2)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#describe_auto_ml_job_v2)
        """

    async def describe_cluster(self, *, ClusterName: str) -> DescribeClusterResponseTypeDef:
        """
        Retrieves information of a SageMaker HyperPod cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_cluster)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#describe_cluster)
        """

    async def describe_cluster_node(
        self, *, ClusterName: str, NodeId: str
    ) -> DescribeClusterNodeResponseTypeDef:
        """
        Retrieves information of an instance (also called a *node* interchangeably) of
        a SageMaker HyperPod
        cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_cluster_node)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#describe_cluster_node)
        """

    async def describe_code_repository(
        self, *, CodeRepositoryName: str
    ) -> DescribeCodeRepositoryOutputTypeDef:
        """
        Gets details about the specified Git repository.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_code_repository)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#describe_code_repository)
        """

    async def describe_compilation_job(
        self, *, CompilationJobName: str
    ) -> DescribeCompilationJobResponseTypeDef:
        """
        Returns information about a model compilation job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_compilation_job)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#describe_compilation_job)
        """

    async def describe_context(self, *, ContextName: str) -> DescribeContextResponseTypeDef:
        """
        Describes a context.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_context)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#describe_context)
        """

    async def describe_data_quality_job_definition(
        self, *, JobDefinitionName: str
    ) -> DescribeDataQualityJobDefinitionResponseTypeDef:
        """
        Gets the details of a data quality monitoring job definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_data_quality_job_definition)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#describe_data_quality_job_definition)
        """

    async def describe_device(
        self, *, DeviceName: str, DeviceFleetName: str, NextToken: str = ...
    ) -> DescribeDeviceResponseTypeDef:
        """
        Describes the device.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_device)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#describe_device)
        """

    async def describe_device_fleet(
        self, *, DeviceFleetName: str
    ) -> DescribeDeviceFleetResponseTypeDef:
        """
        A description of the fleet the device belongs to.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_device_fleet)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#describe_device_fleet)
        """

    async def describe_domain(self, *, DomainId: str) -> DescribeDomainResponseTypeDef:
        """
        The description of the domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_domain)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#describe_domain)
        """

    async def describe_edge_deployment_plan(
        self, *, EdgeDeploymentPlanName: str, NextToken: str = ..., MaxResults: int = ...
    ) -> DescribeEdgeDeploymentPlanResponseTypeDef:
        """
        Describes an edge deployment plan with deployment status per stage.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_edge_deployment_plan)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#describe_edge_deployment_plan)
        """

    async def describe_edge_packaging_job(
        self, *, EdgePackagingJobName: str
    ) -> DescribeEdgePackagingJobResponseTypeDef:
        """
        A description of edge packaging jobs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_edge_packaging_job)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#describe_edge_packaging_job)
        """

    async def describe_endpoint(self, *, EndpointName: str) -> DescribeEndpointOutputTypeDef:
        """
        Returns the description of an endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_endpoint)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#describe_endpoint)
        """

    async def describe_endpoint_config(
        self, *, EndpointConfigName: str
    ) -> DescribeEndpointConfigOutputTypeDef:
        """
        Returns the description of an endpoint configuration created using the
        `CreateEndpointConfig`
        API.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_endpoint_config)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#describe_endpoint_config)
        """

    async def describe_experiment(
        self, *, ExperimentName: str
    ) -> DescribeExperimentResponseTypeDef:
        """
        Provides a list of an experiment's properties.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_experiment)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#describe_experiment)
        """

    async def describe_feature_group(
        self, *, FeatureGroupName: str, NextToken: str = ...
    ) -> DescribeFeatureGroupResponseTypeDef:
        """
        Use this operation to describe a `FeatureGroup`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_feature_group)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#describe_feature_group)
        """

    async def describe_feature_metadata(
        self, *, FeatureGroupName: str, FeatureName: str
    ) -> DescribeFeatureMetadataResponseTypeDef:
        """
        Shows the metadata for a feature within a feature group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_feature_metadata)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#describe_feature_metadata)
        """

    async def describe_flow_definition(
        self, *, FlowDefinitionName: str
    ) -> DescribeFlowDefinitionResponseTypeDef:
        """
        Returns information about the specified flow definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_flow_definition)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#describe_flow_definition)
        """

    async def describe_hub(self, *, HubName: str) -> DescribeHubResponseTypeDef:
        """
        Describe a hub.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_hub)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#describe_hub)
        """

    async def describe_hub_content(
        self,
        *,
        HubName: str,
        HubContentType: HubContentTypeType,
        HubContentName: str,
        HubContentVersion: str = ...,
    ) -> DescribeHubContentResponseTypeDef:
        """
        Describe the content of a hub.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_hub_content)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#describe_hub_content)
        """

    async def describe_human_task_ui(
        self, *, HumanTaskUiName: str
    ) -> DescribeHumanTaskUiResponseTypeDef:
        """
        Returns information about the requested human task user interface (worker task
        template).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_human_task_ui)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#describe_human_task_ui)
        """

    async def describe_hyper_parameter_tuning_job(
        self, *, HyperParameterTuningJobName: str
    ) -> DescribeHyperParameterTuningJobResponseTypeDef:
        """
        Returns a description of a hyperparameter tuning job, depending on the fields
        selected.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_hyper_parameter_tuning_job)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#describe_hyper_parameter_tuning_job)
        """

    async def describe_image(self, *, ImageName: str) -> DescribeImageResponseTypeDef:
        """
        Describes a SageMaker image.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_image)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#describe_image)
        """

    async def describe_image_version(
        self, *, ImageName: str, Version: int = ..., Alias: str = ...
    ) -> DescribeImageVersionResponseTypeDef:
        """
        Describes a version of a SageMaker image.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_image_version)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#describe_image_version)
        """

    async def describe_inference_component(
        self, *, InferenceComponentName: str
    ) -> DescribeInferenceComponentOutputTypeDef:
        """
        Returns information about an inference component.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_inference_component)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#describe_inference_component)
        """

    async def describe_inference_experiment(
        self, *, Name: str
    ) -> DescribeInferenceExperimentResponseTypeDef:
        """
        Returns details about an inference experiment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_inference_experiment)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#describe_inference_experiment)
        """

    async def describe_inference_recommendations_job(
        self, *, JobName: str
    ) -> DescribeInferenceRecommendationsJobResponseTypeDef:
        """
        Provides the results of the Inference Recommender job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_inference_recommendations_job)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#describe_inference_recommendations_job)
        """

    async def describe_labeling_job(
        self, *, LabelingJobName: str
    ) -> DescribeLabelingJobResponseTypeDef:
        """
        Gets information about a labeling job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_labeling_job)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#describe_labeling_job)
        """

    async def describe_lineage_group(
        self, *, LineageGroupName: str
    ) -> DescribeLineageGroupResponseTypeDef:
        """
        Provides a list of properties for the requested lineage group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_lineage_group)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#describe_lineage_group)
        """

    async def describe_model(self, *, ModelName: str) -> DescribeModelOutputTypeDef:
        """
        Describes a model that you created using the `CreateModel` API.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_model)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#describe_model)
        """

    async def describe_model_bias_job_definition(
        self, *, JobDefinitionName: str
    ) -> DescribeModelBiasJobDefinitionResponseTypeDef:
        """
        Returns a description of a model bias job definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_model_bias_job_definition)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#describe_model_bias_job_definition)
        """

    async def describe_model_card(
        self, *, ModelCardName: str, ModelCardVersion: int = ...
    ) -> DescribeModelCardResponseTypeDef:
        """
        Describes the content, creation time, and security configuration of an Amazon
        SageMaker Model
        Card.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_model_card)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#describe_model_card)
        """

    async def describe_model_card_export_job(
        self, *, ModelCardExportJobArn: str
    ) -> DescribeModelCardExportJobResponseTypeDef:
        """
        Describes an Amazon SageMaker Model Card export job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_model_card_export_job)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#describe_model_card_export_job)
        """

    async def describe_model_explainability_job_definition(
        self, *, JobDefinitionName: str
    ) -> DescribeModelExplainabilityJobDefinitionResponseTypeDef:
        """
        Returns a description of a model explainability job definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_model_explainability_job_definition)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#describe_model_explainability_job_definition)
        """

    async def describe_model_package(
        self, *, ModelPackageName: str
    ) -> DescribeModelPackageOutputTypeDef:
        """
        Returns a description of the specified model package, which is used to create
        SageMaker models or list them on Amazon Web Services
        Marketplace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_model_package)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#describe_model_package)
        """

    async def describe_model_package_group(
        self, *, ModelPackageGroupName: str
    ) -> DescribeModelPackageGroupOutputTypeDef:
        """
        Gets a description for the specified model group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_model_package_group)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#describe_model_package_group)
        """

    async def describe_model_quality_job_definition(
        self, *, JobDefinitionName: str
    ) -> DescribeModelQualityJobDefinitionResponseTypeDef:
        """
        Returns a description of a model quality job definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_model_quality_job_definition)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#describe_model_quality_job_definition)
        """

    async def describe_monitoring_schedule(
        self, *, MonitoringScheduleName: str
    ) -> DescribeMonitoringScheduleResponseTypeDef:
        """
        Describes the schedule for a monitoring job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_monitoring_schedule)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#describe_monitoring_schedule)
        """

    async def describe_notebook_instance(
        self, *, NotebookInstanceName: str
    ) -> DescribeNotebookInstanceOutputTypeDef:
        """
        Returns information about a notebook instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_notebook_instance)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#describe_notebook_instance)
        """

    async def describe_notebook_instance_lifecycle_config(
        self, *, NotebookInstanceLifecycleConfigName: str
    ) -> DescribeNotebookInstanceLifecycleConfigOutputTypeDef:
        """
        Returns a description of a notebook instance lifecycle configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_notebook_instance_lifecycle_config)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#describe_notebook_instance_lifecycle_config)
        """

    async def describe_pipeline(self, *, PipelineName: str) -> DescribePipelineResponseTypeDef:
        """
        Describes the details of a pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_pipeline)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#describe_pipeline)
        """

    async def describe_pipeline_definition_for_execution(
        self, *, PipelineExecutionArn: str
    ) -> DescribePipelineDefinitionForExecutionResponseTypeDef:
        """
        Describes the details of an execution's pipeline definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_pipeline_definition_for_execution)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#describe_pipeline_definition_for_execution)
        """

    async def describe_pipeline_execution(
        self, *, PipelineExecutionArn: str
    ) -> DescribePipelineExecutionResponseTypeDef:
        """
        Describes the details of a pipeline execution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_pipeline_execution)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#describe_pipeline_execution)
        """

    async def describe_processing_job(
        self, *, ProcessingJobName: str
    ) -> DescribeProcessingJobResponseTypeDef:
        """
        Returns a description of a processing job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_processing_job)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#describe_processing_job)
        """

    async def describe_project(self, *, ProjectName: str) -> DescribeProjectOutputTypeDef:
        """
        Describes the details of a project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_project)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#describe_project)
        """

    async def describe_space(
        self, *, DomainId: str, SpaceName: str
    ) -> DescribeSpaceResponseTypeDef:
        """
        Describes the space.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_space)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#describe_space)
        """

    async def describe_studio_lifecycle_config(
        self, *, StudioLifecycleConfigName: str
    ) -> DescribeStudioLifecycleConfigResponseTypeDef:
        """
        Describes the Amazon SageMaker Studio Lifecycle Configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_studio_lifecycle_config)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#describe_studio_lifecycle_config)
        """

    async def describe_subscribed_workteam(
        self, *, WorkteamArn: str
    ) -> DescribeSubscribedWorkteamResponseTypeDef:
        """
        Gets information about a work team provided by a vendor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_subscribed_workteam)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#describe_subscribed_workteam)
        """

    async def describe_training_job(
        self, *, TrainingJobName: str
    ) -> DescribeTrainingJobResponseTypeDef:
        """
        Returns information about a training job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_training_job)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#describe_training_job)
        """

    async def describe_transform_job(
        self, *, TransformJobName: str
    ) -> DescribeTransformJobResponseTypeDef:
        """
        Returns information about a transform job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_transform_job)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#describe_transform_job)
        """

    async def describe_trial(self, *, TrialName: str) -> DescribeTrialResponseTypeDef:
        """
        Provides a list of a trial's properties.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_trial)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#describe_trial)
        """

    async def describe_trial_component(
        self, *, TrialComponentName: str
    ) -> DescribeTrialComponentResponseTypeDef:
        """
        Provides a list of a trials component's properties.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_trial_component)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#describe_trial_component)
        """

    async def describe_user_profile(
        self, *, DomainId: str, UserProfileName: str
    ) -> DescribeUserProfileResponseTypeDef:
        """
        Describes a user profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_user_profile)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#describe_user_profile)
        """

    async def describe_workforce(self, *, WorkforceName: str) -> DescribeWorkforceResponseTypeDef:
        """
        Lists private workforce information, including workforce name, Amazon Resource
        Name (ARN), and, if applicable, allowed IP address ranges (
        [CIDRs](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html)).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_workforce)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#describe_workforce)
        """

    async def describe_workteam(self, *, WorkteamName: str) -> DescribeWorkteamResponseTypeDef:
        """
        Gets information about a specific work team.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_workteam)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#describe_workteam)
        """

    async def disable_sagemaker_servicecatalog_portfolio(self) -> Dict[str, Any]:
        """
        Disables using Service Catalog in SageMaker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.disable_sagemaker_servicecatalog_portfolio)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#disable_sagemaker_servicecatalog_portfolio)
        """

    async def disassociate_trial_component(
        self, *, TrialComponentName: str, TrialName: str
    ) -> DisassociateTrialComponentResponseTypeDef:
        """
        Disassociates a trial component from a trial.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.disassociate_trial_component)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#disassociate_trial_component)
        """

    async def enable_sagemaker_servicecatalog_portfolio(self) -> Dict[str, Any]:
        """
        Enables using Service Catalog in SageMaker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.enable_sagemaker_servicecatalog_portfolio)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#enable_sagemaker_servicecatalog_portfolio)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.generate_presigned_url)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#generate_presigned_url)
        """

    async def get_device_fleet_report(
        self, *, DeviceFleetName: str
    ) -> GetDeviceFleetReportResponseTypeDef:
        """
        Describes a fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_device_fleet_report)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#get_device_fleet_report)
        """

    async def get_lineage_group_policy(
        self, *, LineageGroupName: str
    ) -> GetLineageGroupPolicyResponseTypeDef:
        """
        The resource policy for the lineage group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_lineage_group_policy)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#get_lineage_group_policy)
        """

    async def get_model_package_group_policy(
        self, *, ModelPackageGroupName: str
    ) -> GetModelPackageGroupPolicyOutputTypeDef:
        """
        Gets a resource policy that manages access for a model group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_model_package_group_policy)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#get_model_package_group_policy)
        """

    async def get_sagemaker_servicecatalog_portfolio_status(
        self,
    ) -> GetSagemakerServicecatalogPortfolioStatusOutputTypeDef:
        """
        Gets the status of Service Catalog in SageMaker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_sagemaker_servicecatalog_portfolio_status)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#get_sagemaker_servicecatalog_portfolio_status)
        """

    async def get_scaling_configuration_recommendation(
        self,
        *,
        InferenceRecommendationsJobName: str,
        RecommendationId: str = ...,
        EndpointName: str = ...,
        TargetCpuUtilizationPerCore: int = ...,
        ScalingPolicyObjective: ScalingPolicyObjectiveTypeDef = ...,
    ) -> GetScalingConfigurationRecommendationResponseTypeDef:
        """
        Starts an Amazon SageMaker Inference Recommender autoscaling recommendation job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_scaling_configuration_recommendation)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#get_scaling_configuration_recommendation)
        """

    async def get_search_suggestions(
        self, *, Resource: ResourceTypeType, SuggestionQuery: SuggestionQueryTypeDef = ...
    ) -> GetSearchSuggestionsResponseTypeDef:
        """
        An auto-complete API for the search functionality in the SageMaker console.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_search_suggestions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#get_search_suggestions)
        """

    async def import_hub_content(
        self,
        *,
        HubContentName: str,
        HubContentType: HubContentTypeType,
        DocumentSchemaVersion: str,
        HubName: str,
        HubContentDocument: str,
        HubContentVersion: str = ...,
        HubContentDisplayName: str = ...,
        HubContentDescription: str = ...,
        HubContentMarkdown: str = ...,
        HubContentSearchKeywords: Sequence[str] = ...,
        Tags: Sequence[TagTypeDef] = ...,
    ) -> ImportHubContentResponseTypeDef:
        """
        Import hub content.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.import_hub_content)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#import_hub_content)
        """

    async def list_actions(
        self,
        *,
        SourceUri: str = ...,
        ActionType: str = ...,
        CreatedAfter: TimestampTypeDef = ...,
        CreatedBefore: TimestampTypeDef = ...,
        SortBy: SortActionsByType = ...,
        SortOrder: SortOrderType = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
    ) -> ListActionsResponseTypeDef:
        """
        Lists the actions in your account and their properties.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_actions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#list_actions)
        """

    async def list_algorithms(
        self,
        *,
        CreationTimeAfter: TimestampTypeDef = ...,
        CreationTimeBefore: TimestampTypeDef = ...,
        MaxResults: int = ...,
        NameContains: str = ...,
        NextToken: str = ...,
        SortBy: AlgorithmSortByType = ...,
        SortOrder: SortOrderType = ...,
    ) -> ListAlgorithmsOutputTypeDef:
        """
        Lists the machine learning algorithms that have been created.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_algorithms)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#list_algorithms)
        """

    async def list_aliases(
        self,
        *,
        ImageName: str,
        Alias: str = ...,
        Version: int = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
    ) -> ListAliasesResponseTypeDef:
        """
        Lists the aliases of a specified image or image version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_aliases)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#list_aliases)
        """

    async def list_app_image_configs(
        self,
        *,
        MaxResults: int = ...,
        NextToken: str = ...,
        NameContains: str = ...,
        CreationTimeBefore: TimestampTypeDef = ...,
        CreationTimeAfter: TimestampTypeDef = ...,
        ModifiedTimeBefore: TimestampTypeDef = ...,
        ModifiedTimeAfter: TimestampTypeDef = ...,
        SortBy: AppImageConfigSortKeyType = ...,
        SortOrder: SortOrderType = ...,
    ) -> ListAppImageConfigsResponseTypeDef:
        """
        Lists the AppImageConfigs in your account and their properties.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_app_image_configs)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#list_app_image_configs)
        """

    async def list_apps(
        self,
        *,
        NextToken: str = ...,
        MaxResults: int = ...,
        SortOrder: SortOrderType = ...,
        SortBy: Literal["CreationTime"] = ...,
        DomainIdEquals: str = ...,
        UserProfileNameEquals: str = ...,
        SpaceNameEquals: str = ...,
    ) -> ListAppsResponseTypeDef:
        """
        Lists apps.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_apps)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#list_apps)
        """

    async def list_artifacts(
        self,
        *,
        SourceUri: str = ...,
        ArtifactType: str = ...,
        CreatedAfter: TimestampTypeDef = ...,
        CreatedBefore: TimestampTypeDef = ...,
        SortBy: Literal["CreationTime"] = ...,
        SortOrder: SortOrderType = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
    ) -> ListArtifactsResponseTypeDef:
        """
        Lists the artifacts in your account and their properties.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_artifacts)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#list_artifacts)
        """

    async def list_associations(
        self,
        *,
        SourceArn: str = ...,
        DestinationArn: str = ...,
        SourceType: str = ...,
        DestinationType: str = ...,
        AssociationType: AssociationEdgeTypeType = ...,
        CreatedAfter: TimestampTypeDef = ...,
        CreatedBefore: TimestampTypeDef = ...,
        SortBy: SortAssociationsByType = ...,
        SortOrder: SortOrderType = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
    ) -> ListAssociationsResponseTypeDef:
        """
        Lists the associations in your account and their properties.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_associations)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#list_associations)
        """

    async def list_auto_ml_jobs(
        self,
        *,
        CreationTimeAfter: TimestampTypeDef = ...,
        CreationTimeBefore: TimestampTypeDef = ...,
        LastModifiedTimeAfter: TimestampTypeDef = ...,
        LastModifiedTimeBefore: TimestampTypeDef = ...,
        NameContains: str = ...,
        StatusEquals: AutoMLJobStatusType = ...,
        SortOrder: AutoMLSortOrderType = ...,
        SortBy: AutoMLSortByType = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
    ) -> ListAutoMLJobsResponseTypeDef:
        """
        Request a list of jobs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_auto_ml_jobs)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#list_auto_ml_jobs)
        """

    async def list_candidates_for_auto_ml_job(
        self,
        *,
        AutoMLJobName: str,
        StatusEquals: CandidateStatusType = ...,
        CandidateNameEquals: str = ...,
        SortOrder: AutoMLSortOrderType = ...,
        SortBy: CandidateSortByType = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
    ) -> ListCandidatesForAutoMLJobResponseTypeDef:
        """
        List the candidates created for the job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_candidates_for_auto_ml_job)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#list_candidates_for_auto_ml_job)
        """

    async def list_cluster_nodes(
        self,
        *,
        ClusterName: str,
        CreationTimeAfter: TimestampTypeDef = ...,
        CreationTimeBefore: TimestampTypeDef = ...,
        InstanceGroupNameContains: str = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
        SortBy: ClusterSortByType = ...,
        SortOrder: SortOrderType = ...,
    ) -> ListClusterNodesResponseTypeDef:
        """
        Retrieves the list of instances (also called *nodes* interchangeably) in a
        SageMaker HyperPod
        cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_cluster_nodes)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#list_cluster_nodes)
        """

    async def list_clusters(
        self,
        *,
        CreationTimeAfter: TimestampTypeDef = ...,
        CreationTimeBefore: TimestampTypeDef = ...,
        MaxResults: int = ...,
        NameContains: str = ...,
        NextToken: str = ...,
        SortBy: ClusterSortByType = ...,
        SortOrder: SortOrderType = ...,
    ) -> ListClustersResponseTypeDef:
        """
        Retrieves the list of SageMaker HyperPod clusters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_clusters)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#list_clusters)
        """

    async def list_code_repositories(
        self,
        *,
        CreationTimeAfter: TimestampTypeDef = ...,
        CreationTimeBefore: TimestampTypeDef = ...,
        LastModifiedTimeAfter: TimestampTypeDef = ...,
        LastModifiedTimeBefore: TimestampTypeDef = ...,
        MaxResults: int = ...,
        NameContains: str = ...,
        NextToken: str = ...,
        SortBy: CodeRepositorySortByType = ...,
        SortOrder: CodeRepositorySortOrderType = ...,
    ) -> ListCodeRepositoriesOutputTypeDef:
        """
        Gets a list of the Git repositories in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_code_repositories)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#list_code_repositories)
        """

    async def list_compilation_jobs(
        self,
        *,
        NextToken: str = ...,
        MaxResults: int = ...,
        CreationTimeAfter: TimestampTypeDef = ...,
        CreationTimeBefore: TimestampTypeDef = ...,
        LastModifiedTimeAfter: TimestampTypeDef = ...,
        LastModifiedTimeBefore: TimestampTypeDef = ...,
        NameContains: str = ...,
        StatusEquals: CompilationJobStatusType = ...,
        SortBy: ListCompilationJobsSortByType = ...,
        SortOrder: SortOrderType = ...,
    ) -> ListCompilationJobsResponseTypeDef:
        """
        Lists model compilation jobs that satisfy various filters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_compilation_jobs)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#list_compilation_jobs)
        """

    async def list_contexts(
        self,
        *,
        SourceUri: str = ...,
        ContextType: str = ...,
        CreatedAfter: TimestampTypeDef = ...,
        CreatedBefore: TimestampTypeDef = ...,
        SortBy: SortContextsByType = ...,
        SortOrder: SortOrderType = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
    ) -> ListContextsResponseTypeDef:
        """
        Lists the contexts in your account and their properties.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_contexts)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#list_contexts)
        """

    async def list_data_quality_job_definitions(
        self,
        *,
        EndpointName: str = ...,
        SortBy: MonitoringJobDefinitionSortKeyType = ...,
        SortOrder: SortOrderType = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
        NameContains: str = ...,
        CreationTimeBefore: TimestampTypeDef = ...,
        CreationTimeAfter: TimestampTypeDef = ...,
    ) -> ListDataQualityJobDefinitionsResponseTypeDef:
        """
        Lists the data quality job definitions in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_data_quality_job_definitions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#list_data_quality_job_definitions)
        """

    async def list_device_fleets(
        self,
        *,
        NextToken: str = ...,
        MaxResults: int = ...,
        CreationTimeAfter: TimestampTypeDef = ...,
        CreationTimeBefore: TimestampTypeDef = ...,
        LastModifiedTimeAfter: TimestampTypeDef = ...,
        LastModifiedTimeBefore: TimestampTypeDef = ...,
        NameContains: str = ...,
        SortBy: ListDeviceFleetsSortByType = ...,
        SortOrder: SortOrderType = ...,
    ) -> ListDeviceFleetsResponseTypeDef:
        """
        Returns a list of devices in the fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_device_fleets)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#list_device_fleets)
        """

    async def list_devices(
        self,
        *,
        NextToken: str = ...,
        MaxResults: int = ...,
        LatestHeartbeatAfter: TimestampTypeDef = ...,
        ModelName: str = ...,
        DeviceFleetName: str = ...,
    ) -> ListDevicesResponseTypeDef:
        """
        A list of devices.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_devices)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#list_devices)
        """

    async def list_domains(
        self, *, NextToken: str = ..., MaxResults: int = ...
    ) -> ListDomainsResponseTypeDef:
        """
        Lists the domains.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_domains)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#list_domains)
        """

    async def list_edge_deployment_plans(
        self,
        *,
        NextToken: str = ...,
        MaxResults: int = ...,
        CreationTimeAfter: TimestampTypeDef = ...,
        CreationTimeBefore: TimestampTypeDef = ...,
        LastModifiedTimeAfter: TimestampTypeDef = ...,
        LastModifiedTimeBefore: TimestampTypeDef = ...,
        NameContains: str = ...,
        DeviceFleetNameContains: str = ...,
        SortBy: ListEdgeDeploymentPlansSortByType = ...,
        SortOrder: SortOrderType = ...,
    ) -> ListEdgeDeploymentPlansResponseTypeDef:
        """
        Lists all edge deployment plans.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_edge_deployment_plans)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#list_edge_deployment_plans)
        """

    async def list_edge_packaging_jobs(
        self,
        *,
        NextToken: str = ...,
        MaxResults: int = ...,
        CreationTimeAfter: TimestampTypeDef = ...,
        CreationTimeBefore: TimestampTypeDef = ...,
        LastModifiedTimeAfter: TimestampTypeDef = ...,
        LastModifiedTimeBefore: TimestampTypeDef = ...,
        NameContains: str = ...,
        ModelNameContains: str = ...,
        StatusEquals: EdgePackagingJobStatusType = ...,
        SortBy: ListEdgePackagingJobsSortByType = ...,
        SortOrder: SortOrderType = ...,
    ) -> ListEdgePackagingJobsResponseTypeDef:
        """
        Returns a list of edge packaging jobs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_edge_packaging_jobs)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#list_edge_packaging_jobs)
        """

    async def list_endpoint_configs(
        self,
        *,
        SortBy: EndpointConfigSortKeyType = ...,
        SortOrder: OrderKeyType = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
        NameContains: str = ...,
        CreationTimeBefore: TimestampTypeDef = ...,
        CreationTimeAfter: TimestampTypeDef = ...,
    ) -> ListEndpointConfigsOutputTypeDef:
        """
        Lists endpoint configurations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_endpoint_configs)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#list_endpoint_configs)
        """

    async def list_endpoints(
        self,
        *,
        SortBy: EndpointSortKeyType = ...,
        SortOrder: OrderKeyType = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
        NameContains: str = ...,
        CreationTimeBefore: TimestampTypeDef = ...,
        CreationTimeAfter: TimestampTypeDef = ...,
        LastModifiedTimeBefore: TimestampTypeDef = ...,
        LastModifiedTimeAfter: TimestampTypeDef = ...,
        StatusEquals: EndpointStatusType = ...,
    ) -> ListEndpointsOutputTypeDef:
        """
        Lists endpoints.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_endpoints)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#list_endpoints)
        """

    async def list_experiments(
        self,
        *,
        CreatedAfter: TimestampTypeDef = ...,
        CreatedBefore: TimestampTypeDef = ...,
        SortBy: SortExperimentsByType = ...,
        SortOrder: SortOrderType = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
    ) -> ListExperimentsResponseTypeDef:
        """
        Lists all the experiments in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_experiments)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#list_experiments)
        """

    async def list_feature_groups(
        self,
        *,
        NameContains: str = ...,
        FeatureGroupStatusEquals: FeatureGroupStatusType = ...,
        OfflineStoreStatusEquals: OfflineStoreStatusValueType = ...,
        CreationTimeAfter: TimestampTypeDef = ...,
        CreationTimeBefore: TimestampTypeDef = ...,
        SortOrder: FeatureGroupSortOrderType = ...,
        SortBy: FeatureGroupSortByType = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
    ) -> ListFeatureGroupsResponseTypeDef:
        """
        List `FeatureGroup`s based on given filter and order.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_feature_groups)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#list_feature_groups)
        """

    async def list_flow_definitions(
        self,
        *,
        CreationTimeAfter: TimestampTypeDef = ...,
        CreationTimeBefore: TimestampTypeDef = ...,
        SortOrder: SortOrderType = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
    ) -> ListFlowDefinitionsResponseTypeDef:
        """
        Returns information about the flow definitions in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_flow_definitions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#list_flow_definitions)
        """

    async def list_hub_content_versions(
        self,
        *,
        HubName: str,
        HubContentType: HubContentTypeType,
        HubContentName: str,
        MinVersion: str = ...,
        MaxSchemaVersion: str = ...,
        CreationTimeBefore: TimestampTypeDef = ...,
        CreationTimeAfter: TimestampTypeDef = ...,
        SortBy: HubContentSortByType = ...,
        SortOrder: SortOrderType = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
    ) -> ListHubContentVersionsResponseTypeDef:
        """
        List hub content versions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_hub_content_versions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#list_hub_content_versions)
        """

    async def list_hub_contents(
        self,
        *,
        HubName: str,
        HubContentType: HubContentTypeType,
        NameContains: str = ...,
        MaxSchemaVersion: str = ...,
        CreationTimeBefore: TimestampTypeDef = ...,
        CreationTimeAfter: TimestampTypeDef = ...,
        SortBy: HubContentSortByType = ...,
        SortOrder: SortOrderType = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
    ) -> ListHubContentsResponseTypeDef:
        """
        List the contents of a hub.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_hub_contents)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#list_hub_contents)
        """

    async def list_hubs(
        self,
        *,
        NameContains: str = ...,
        CreationTimeBefore: TimestampTypeDef = ...,
        CreationTimeAfter: TimestampTypeDef = ...,
        LastModifiedTimeBefore: TimestampTypeDef = ...,
        LastModifiedTimeAfter: TimestampTypeDef = ...,
        SortBy: HubSortByType = ...,
        SortOrder: SortOrderType = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
    ) -> ListHubsResponseTypeDef:
        """
        List all existing hubs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_hubs)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#list_hubs)
        """

    async def list_human_task_uis(
        self,
        *,
        CreationTimeAfter: TimestampTypeDef = ...,
        CreationTimeBefore: TimestampTypeDef = ...,
        SortOrder: SortOrderType = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
    ) -> ListHumanTaskUisResponseTypeDef:
        """
        Returns information about the human task user interfaces in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_human_task_uis)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#list_human_task_uis)
        """

    async def list_hyper_parameter_tuning_jobs(
        self,
        *,
        NextToken: str = ...,
        MaxResults: int = ...,
        SortBy: HyperParameterTuningJobSortByOptionsType = ...,
        SortOrder: SortOrderType = ...,
        NameContains: str = ...,
        CreationTimeAfter: TimestampTypeDef = ...,
        CreationTimeBefore: TimestampTypeDef = ...,
        LastModifiedTimeAfter: TimestampTypeDef = ...,
        LastModifiedTimeBefore: TimestampTypeDef = ...,
        StatusEquals: HyperParameterTuningJobStatusType = ...,
    ) -> ListHyperParameterTuningJobsResponseTypeDef:
        """
        Gets a list of
        [HyperParameterTuningJobSummary](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterTuningJobSummary.html)
        objects that describe the hyperparameter tuning jobs launched in your
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_hyper_parameter_tuning_jobs)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#list_hyper_parameter_tuning_jobs)
        """

    async def list_image_versions(
        self,
        *,
        ImageName: str,
        CreationTimeAfter: TimestampTypeDef = ...,
        CreationTimeBefore: TimestampTypeDef = ...,
        LastModifiedTimeAfter: TimestampTypeDef = ...,
        LastModifiedTimeBefore: TimestampTypeDef = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
        SortBy: ImageVersionSortByType = ...,
        SortOrder: ImageVersionSortOrderType = ...,
    ) -> ListImageVersionsResponseTypeDef:
        """
        Lists the versions of a specified image and their properties.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_image_versions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#list_image_versions)
        """

    async def list_images(
        self,
        *,
        CreationTimeAfter: TimestampTypeDef = ...,
        CreationTimeBefore: TimestampTypeDef = ...,
        LastModifiedTimeAfter: TimestampTypeDef = ...,
        LastModifiedTimeBefore: TimestampTypeDef = ...,
        MaxResults: int = ...,
        NameContains: str = ...,
        NextToken: str = ...,
        SortBy: ImageSortByType = ...,
        SortOrder: ImageSortOrderType = ...,
    ) -> ListImagesResponseTypeDef:
        """
        Lists the images in your account and their properties.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_images)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#list_images)
        """

    async def list_inference_components(
        self,
        *,
        SortBy: InferenceComponentSortKeyType = ...,
        SortOrder: OrderKeyType = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
        NameContains: str = ...,
        CreationTimeBefore: TimestampTypeDef = ...,
        CreationTimeAfter: TimestampTypeDef = ...,
        LastModifiedTimeBefore: TimestampTypeDef = ...,
        LastModifiedTimeAfter: TimestampTypeDef = ...,
        StatusEquals: InferenceComponentStatusType = ...,
        EndpointNameEquals: str = ...,
        VariantNameEquals: str = ...,
    ) -> ListInferenceComponentsOutputTypeDef:
        """
        Lists the inference components in your account and their properties.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_inference_components)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#list_inference_components)
        """

    async def list_inference_experiments(
        self,
        *,
        NameContains: str = ...,
        Type: Literal["ShadowMode"] = ...,
        StatusEquals: InferenceExperimentStatusType = ...,
        CreationTimeAfter: TimestampTypeDef = ...,
        CreationTimeBefore: TimestampTypeDef = ...,
        LastModifiedTimeAfter: TimestampTypeDef = ...,
        LastModifiedTimeBefore: TimestampTypeDef = ...,
        SortBy: SortInferenceExperimentsByType = ...,
        SortOrder: SortOrderType = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
    ) -> ListInferenceExperimentsResponseTypeDef:
        """
        Returns the list of all inference experiments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_inference_experiments)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#list_inference_experiments)
        """

    async def list_inference_recommendations_job_steps(
        self,
        *,
        JobName: str,
        Status: RecommendationJobStatusType = ...,
        StepType: Literal["BENCHMARK"] = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
    ) -> ListInferenceRecommendationsJobStepsResponseTypeDef:
        """
        Returns a list of the subtasks for an Inference Recommender job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_inference_recommendations_job_steps)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#list_inference_recommendations_job_steps)
        """

    async def list_inference_recommendations_jobs(
        self,
        *,
        CreationTimeAfter: TimestampTypeDef = ...,
        CreationTimeBefore: TimestampTypeDef = ...,
        LastModifiedTimeAfter: TimestampTypeDef = ...,
        LastModifiedTimeBefore: TimestampTypeDef = ...,
        NameContains: str = ...,
        StatusEquals: RecommendationJobStatusType = ...,
        SortBy: ListInferenceRecommendationsJobsSortByType = ...,
        SortOrder: SortOrderType = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
        ModelNameEquals: str = ...,
        ModelPackageVersionArnEquals: str = ...,
    ) -> ListInferenceRecommendationsJobsResponseTypeDef:
        """
        Lists recommendation jobs that satisfy various filters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_inference_recommendations_jobs)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#list_inference_recommendations_jobs)
        """

    async def list_labeling_jobs(
        self,
        *,
        CreationTimeAfter: TimestampTypeDef = ...,
        CreationTimeBefore: TimestampTypeDef = ...,
        LastModifiedTimeAfter: TimestampTypeDef = ...,
        LastModifiedTimeBefore: TimestampTypeDef = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
        NameContains: str = ...,
        SortBy: SortByType = ...,
        SortOrder: SortOrderType = ...,
        StatusEquals: LabelingJobStatusType = ...,
    ) -> ListLabelingJobsResponseTypeDef:
        """
        Gets a list of labeling jobs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_labeling_jobs)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#list_labeling_jobs)
        """

    async def list_labeling_jobs_for_workteam(
        self,
        *,
        WorkteamArn: str,
        MaxResults: int = ...,
        NextToken: str = ...,
        CreationTimeAfter: TimestampTypeDef = ...,
        CreationTimeBefore: TimestampTypeDef = ...,
        JobReferenceCodeContains: str = ...,
        SortBy: Literal["CreationTime"] = ...,
        SortOrder: SortOrderType = ...,
    ) -> ListLabelingJobsForWorkteamResponseTypeDef:
        """
        Gets a list of labeling jobs assigned to a specified work team.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_labeling_jobs_for_workteam)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#list_labeling_jobs_for_workteam)
        """

    async def list_lineage_groups(
        self,
        *,
        CreatedAfter: TimestampTypeDef = ...,
        CreatedBefore: TimestampTypeDef = ...,
        SortBy: SortLineageGroupsByType = ...,
        SortOrder: SortOrderType = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
    ) -> ListLineageGroupsResponseTypeDef:
        """
        A list of lineage groups shared with your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_lineage_groups)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#list_lineage_groups)
        """

    async def list_model_bias_job_definitions(
        self,
        *,
        EndpointName: str = ...,
        SortBy: MonitoringJobDefinitionSortKeyType = ...,
        SortOrder: SortOrderType = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
        NameContains: str = ...,
        CreationTimeBefore: TimestampTypeDef = ...,
        CreationTimeAfter: TimestampTypeDef = ...,
    ) -> ListModelBiasJobDefinitionsResponseTypeDef:
        """
        Lists model bias jobs definitions that satisfy various filters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_model_bias_job_definitions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#list_model_bias_job_definitions)
        """

    async def list_model_card_export_jobs(
        self,
        *,
        ModelCardName: str,
        ModelCardVersion: int = ...,
        CreationTimeAfter: TimestampTypeDef = ...,
        CreationTimeBefore: TimestampTypeDef = ...,
        ModelCardExportJobNameContains: str = ...,
        StatusEquals: ModelCardExportJobStatusType = ...,
        SortBy: ModelCardExportJobSortByType = ...,
        SortOrder: ModelCardExportJobSortOrderType = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
    ) -> ListModelCardExportJobsResponseTypeDef:
        """
        List the export jobs for the Amazon SageMaker Model Card.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_model_card_export_jobs)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#list_model_card_export_jobs)
        """

    async def list_model_card_versions(
        self,
        *,
        ModelCardName: str,
        CreationTimeAfter: TimestampTypeDef = ...,
        CreationTimeBefore: TimestampTypeDef = ...,
        MaxResults: int = ...,
        ModelCardStatus: ModelCardStatusType = ...,
        NextToken: str = ...,
        SortBy: Literal["Version"] = ...,
        SortOrder: ModelCardSortOrderType = ...,
    ) -> ListModelCardVersionsResponseTypeDef:
        """
        List existing versions of an Amazon SageMaker Model Card.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_model_card_versions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#list_model_card_versions)
        """

    async def list_model_cards(
        self,
        *,
        CreationTimeAfter: TimestampTypeDef = ...,
        CreationTimeBefore: TimestampTypeDef = ...,
        MaxResults: int = ...,
        NameContains: str = ...,
        ModelCardStatus: ModelCardStatusType = ...,
        NextToken: str = ...,
        SortBy: ModelCardSortByType = ...,
        SortOrder: ModelCardSortOrderType = ...,
    ) -> ListModelCardsResponseTypeDef:
        """
        List existing model cards.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_model_cards)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#list_model_cards)
        """

    async def list_model_explainability_job_definitions(
        self,
        *,
        EndpointName: str = ...,
        SortBy: MonitoringJobDefinitionSortKeyType = ...,
        SortOrder: SortOrderType = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
        NameContains: str = ...,
        CreationTimeBefore: TimestampTypeDef = ...,
        CreationTimeAfter: TimestampTypeDef = ...,
    ) -> ListModelExplainabilityJobDefinitionsResponseTypeDef:
        """
        Lists model explainability job definitions that satisfy various filters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_model_explainability_job_definitions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#list_model_explainability_job_definitions)
        """

    async def list_model_metadata(
        self,
        *,
        SearchExpression: ModelMetadataSearchExpressionTypeDef = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
    ) -> ListModelMetadataResponseTypeDef:
        """
        Lists the domain, framework, task, and model name of standard machine learning
        models found in common model
        zoos.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_model_metadata)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#list_model_metadata)
        """

    async def list_model_package_groups(
        self,
        *,
        CreationTimeAfter: TimestampTypeDef = ...,
        CreationTimeBefore: TimestampTypeDef = ...,
        MaxResults: int = ...,
        NameContains: str = ...,
        NextToken: str = ...,
        SortBy: ModelPackageGroupSortByType = ...,
        SortOrder: SortOrderType = ...,
    ) -> ListModelPackageGroupsOutputTypeDef:
        """
        Gets a list of the model groups in your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_model_package_groups)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#list_model_package_groups)
        """

    async def list_model_packages(
        self,
        *,
        CreationTimeAfter: TimestampTypeDef = ...,
        CreationTimeBefore: TimestampTypeDef = ...,
        MaxResults: int = ...,
        NameContains: str = ...,
        ModelApprovalStatus: ModelApprovalStatusType = ...,
        ModelPackageGroupName: str = ...,
        ModelPackageType: ModelPackageTypeType = ...,
        NextToken: str = ...,
        SortBy: ModelPackageSortByType = ...,
        SortOrder: SortOrderType = ...,
    ) -> ListModelPackagesOutputTypeDef:
        """
        Lists the model packages that have been created.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_model_packages)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#list_model_packages)
        """

    async def list_model_quality_job_definitions(
        self,
        *,
        EndpointName: str = ...,
        SortBy: MonitoringJobDefinitionSortKeyType = ...,
        SortOrder: SortOrderType = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
        NameContains: str = ...,
        CreationTimeBefore: TimestampTypeDef = ...,
        CreationTimeAfter: TimestampTypeDef = ...,
    ) -> ListModelQualityJobDefinitionsResponseTypeDef:
        """
        Gets a list of model quality monitoring job definitions in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_model_quality_job_definitions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#list_model_quality_job_definitions)
        """

    async def list_models(
        self,
        *,
        SortBy: ModelSortKeyType = ...,
        SortOrder: OrderKeyType = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
        NameContains: str = ...,
        CreationTimeBefore: TimestampTypeDef = ...,
        CreationTimeAfter: TimestampTypeDef = ...,
    ) -> ListModelsOutputTypeDef:
        """
        Lists models created with the `CreateModel` API.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_models)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#list_models)
        """

    async def list_monitoring_alert_history(
        self,
        *,
        MonitoringScheduleName: str = ...,
        MonitoringAlertName: str = ...,
        SortBy: MonitoringAlertHistorySortKeyType = ...,
        SortOrder: SortOrderType = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
        CreationTimeBefore: TimestampTypeDef = ...,
        CreationTimeAfter: TimestampTypeDef = ...,
        StatusEquals: MonitoringAlertStatusType = ...,
    ) -> ListMonitoringAlertHistoryResponseTypeDef:
        """
        Gets a list of past alerts in a model monitoring schedule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_monitoring_alert_history)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#list_monitoring_alert_history)
        """

    async def list_monitoring_alerts(
        self, *, MonitoringScheduleName: str, NextToken: str = ..., MaxResults: int = ...
    ) -> ListMonitoringAlertsResponseTypeDef:
        """
        Gets the alerts for a single monitoring schedule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_monitoring_alerts)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#list_monitoring_alerts)
        """

    async def list_monitoring_executions(
        self,
        *,
        MonitoringScheduleName: str = ...,
        EndpointName: str = ...,
        SortBy: MonitoringExecutionSortKeyType = ...,
        SortOrder: SortOrderType = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
        ScheduledTimeBefore: TimestampTypeDef = ...,
        ScheduledTimeAfter: TimestampTypeDef = ...,
        CreationTimeBefore: TimestampTypeDef = ...,
        CreationTimeAfter: TimestampTypeDef = ...,
        LastModifiedTimeBefore: TimestampTypeDef = ...,
        LastModifiedTimeAfter: TimestampTypeDef = ...,
        StatusEquals: ExecutionStatusType = ...,
        MonitoringJobDefinitionName: str = ...,
        MonitoringTypeEquals: MonitoringTypeType = ...,
    ) -> ListMonitoringExecutionsResponseTypeDef:
        """
        Returns list of all monitoring job executions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_monitoring_executions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#list_monitoring_executions)
        """

    async def list_monitoring_schedules(
        self,
        *,
        EndpointName: str = ...,
        SortBy: MonitoringScheduleSortKeyType = ...,
        SortOrder: SortOrderType = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
        NameContains: str = ...,
        CreationTimeBefore: TimestampTypeDef = ...,
        CreationTimeAfter: TimestampTypeDef = ...,
        LastModifiedTimeBefore: TimestampTypeDef = ...,
        LastModifiedTimeAfter: TimestampTypeDef = ...,
        StatusEquals: ScheduleStatusType = ...,
        MonitoringJobDefinitionName: str = ...,
        MonitoringTypeEquals: MonitoringTypeType = ...,
    ) -> ListMonitoringSchedulesResponseTypeDef:
        """
        Returns list of all monitoring schedules.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_monitoring_schedules)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#list_monitoring_schedules)
        """

    async def list_notebook_instance_lifecycle_configs(
        self,
        *,
        NextToken: str = ...,
        MaxResults: int = ...,
        SortBy: NotebookInstanceLifecycleConfigSortKeyType = ...,
        SortOrder: NotebookInstanceLifecycleConfigSortOrderType = ...,
        NameContains: str = ...,
        CreationTimeBefore: TimestampTypeDef = ...,
        CreationTimeAfter: TimestampTypeDef = ...,
        LastModifiedTimeBefore: TimestampTypeDef = ...,
        LastModifiedTimeAfter: TimestampTypeDef = ...,
    ) -> ListNotebookInstanceLifecycleConfigsOutputTypeDef:
        """
        Lists notebook instance lifestyle configurations created with the
        [CreateNotebookInstanceLifecycleConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateNotebookInstanceLifecycleConfig.html)
        API.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_notebook_instance_lifecycle_configs)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#list_notebook_instance_lifecycle_configs)
        """

    async def list_notebook_instances(
        self,
        *,
        NextToken: str = ...,
        MaxResults: int = ...,
        SortBy: NotebookInstanceSortKeyType = ...,
        SortOrder: NotebookInstanceSortOrderType = ...,
        NameContains: str = ...,
        CreationTimeBefore: TimestampTypeDef = ...,
        CreationTimeAfter: TimestampTypeDef = ...,
        LastModifiedTimeBefore: TimestampTypeDef = ...,
        LastModifiedTimeAfter: TimestampTypeDef = ...,
        StatusEquals: NotebookInstanceStatusType = ...,
        NotebookInstanceLifecycleConfigNameContains: str = ...,
        DefaultCodeRepositoryContains: str = ...,
        AdditionalCodeRepositoryEquals: str = ...,
    ) -> ListNotebookInstancesOutputTypeDef:
        """
        Returns a list of the SageMaker notebook instances in the requester's account
        in an Amazon Web Services
        Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_notebook_instances)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#list_notebook_instances)
        """

    async def list_pipeline_execution_steps(
        self,
        *,
        PipelineExecutionArn: str = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
        SortOrder: SortOrderType = ...,
    ) -> ListPipelineExecutionStepsResponseTypeDef:
        """
        Gets a list of `PipeLineExecutionStep` objects.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_pipeline_execution_steps)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#list_pipeline_execution_steps)
        """

    async def list_pipeline_executions(
        self,
        *,
        PipelineName: str,
        CreatedAfter: TimestampTypeDef = ...,
        CreatedBefore: TimestampTypeDef = ...,
        SortBy: SortPipelineExecutionsByType = ...,
        SortOrder: SortOrderType = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
    ) -> ListPipelineExecutionsResponseTypeDef:
        """
        Gets a list of the pipeline executions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_pipeline_executions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#list_pipeline_executions)
        """

    async def list_pipeline_parameters_for_execution(
        self, *, PipelineExecutionArn: str, NextToken: str = ..., MaxResults: int = ...
    ) -> ListPipelineParametersForExecutionResponseTypeDef:
        """
        Gets a list of parameters for a pipeline execution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_pipeline_parameters_for_execution)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#list_pipeline_parameters_for_execution)
        """

    async def list_pipelines(
        self,
        *,
        PipelineNamePrefix: str = ...,
        CreatedAfter: TimestampTypeDef = ...,
        CreatedBefore: TimestampTypeDef = ...,
        SortBy: SortPipelinesByType = ...,
        SortOrder: SortOrderType = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
    ) -> ListPipelinesResponseTypeDef:
        """
        Gets a list of pipelines.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_pipelines)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#list_pipelines)
        """

    async def list_processing_jobs(
        self,
        *,
        CreationTimeAfter: TimestampTypeDef = ...,
        CreationTimeBefore: TimestampTypeDef = ...,
        LastModifiedTimeAfter: TimestampTypeDef = ...,
        LastModifiedTimeBefore: TimestampTypeDef = ...,
        NameContains: str = ...,
        StatusEquals: ProcessingJobStatusType = ...,
        SortBy: SortByType = ...,
        SortOrder: SortOrderType = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
    ) -> ListProcessingJobsResponseTypeDef:
        """
        Lists processing jobs that satisfy various filters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_processing_jobs)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#list_processing_jobs)
        """

    async def list_projects(
        self,
        *,
        CreationTimeAfter: TimestampTypeDef = ...,
        CreationTimeBefore: TimestampTypeDef = ...,
        MaxResults: int = ...,
        NameContains: str = ...,
        NextToken: str = ...,
        SortBy: ProjectSortByType = ...,
        SortOrder: ProjectSortOrderType = ...,
    ) -> ListProjectsOutputTypeDef:
        """
        Gets a list of the projects in an Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_projects)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#list_projects)
        """

    async def list_resource_catalogs(
        self,
        *,
        NameContains: str = ...,
        CreationTimeAfter: TimestampTypeDef = ...,
        CreationTimeBefore: TimestampTypeDef = ...,
        SortOrder: ResourceCatalogSortOrderType = ...,
        SortBy: Literal["CreationTime"] = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
    ) -> ListResourceCatalogsResponseTypeDef:
        """
        Lists Amazon SageMaker Catalogs based on given filters and orders.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_resource_catalogs)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#list_resource_catalogs)
        """

    async def list_spaces(
        self,
        *,
        NextToken: str = ...,
        MaxResults: int = ...,
        SortOrder: SortOrderType = ...,
        SortBy: SpaceSortKeyType = ...,
        DomainIdEquals: str = ...,
        SpaceNameContains: str = ...,
    ) -> ListSpacesResponseTypeDef:
        """
        Lists spaces.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_spaces)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#list_spaces)
        """

    async def list_stage_devices(
        self,
        *,
        EdgeDeploymentPlanName: str,
        StageName: str,
        NextToken: str = ...,
        MaxResults: int = ...,
        ExcludeDevicesDeployedInOtherStage: bool = ...,
    ) -> ListStageDevicesResponseTypeDef:
        """
        Lists devices allocated to the stage, containing detailed device information
        and deployment
        status.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_stage_devices)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#list_stage_devices)
        """

    async def list_studio_lifecycle_configs(
        self,
        *,
        MaxResults: int = ...,
        NextToken: str = ...,
        NameContains: str = ...,
        AppTypeEquals: StudioLifecycleConfigAppTypeType = ...,
        CreationTimeBefore: TimestampTypeDef = ...,
        CreationTimeAfter: TimestampTypeDef = ...,
        ModifiedTimeBefore: TimestampTypeDef = ...,
        ModifiedTimeAfter: TimestampTypeDef = ...,
        SortBy: StudioLifecycleConfigSortKeyType = ...,
        SortOrder: SortOrderType = ...,
    ) -> ListStudioLifecycleConfigsResponseTypeDef:
        """
        Lists the Amazon SageMaker Studio Lifecycle Configurations in your Amazon Web
        Services
        Account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_studio_lifecycle_configs)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#list_studio_lifecycle_configs)
        """

    async def list_subscribed_workteams(
        self, *, NameContains: str = ..., NextToken: str = ..., MaxResults: int = ...
    ) -> ListSubscribedWorkteamsResponseTypeDef:
        """
        Gets a list of the work teams that you are subscribed to in the Amazon Web
        Services
        Marketplace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_subscribed_workteams)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#list_subscribed_workteams)
        """

    async def list_tags(
        self, *, ResourceArn: str, NextToken: str = ..., MaxResults: int = ...
    ) -> ListTagsOutputTypeDef:
        """
        Returns the tags for the specified SageMaker resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_tags)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#list_tags)
        """

    async def list_training_jobs(
        self,
        *,
        NextToken: str = ...,
        MaxResults: int = ...,
        CreationTimeAfter: TimestampTypeDef = ...,
        CreationTimeBefore: TimestampTypeDef = ...,
        LastModifiedTimeAfter: TimestampTypeDef = ...,
        LastModifiedTimeBefore: TimestampTypeDef = ...,
        NameContains: str = ...,
        StatusEquals: TrainingJobStatusType = ...,
        SortBy: SortByType = ...,
        SortOrder: SortOrderType = ...,
        WarmPoolStatusEquals: WarmPoolResourceStatusType = ...,
    ) -> ListTrainingJobsResponseTypeDef:
        """
        Lists training jobs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_training_jobs)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#list_training_jobs)
        """

    async def list_training_jobs_for_hyper_parameter_tuning_job(
        self,
        *,
        HyperParameterTuningJobName: str,
        NextToken: str = ...,
        MaxResults: int = ...,
        StatusEquals: TrainingJobStatusType = ...,
        SortBy: TrainingJobSortByOptionsType = ...,
        SortOrder: SortOrderType = ...,
    ) -> ListTrainingJobsForHyperParameterTuningJobResponseTypeDef:
        """
        Gets a list of
        [TrainingJobSummary](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TrainingJobSummary.html)
        objects that describe the training jobs that a hyperparameter tuning job
        launched.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_training_jobs_for_hyper_parameter_tuning_job)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#list_training_jobs_for_hyper_parameter_tuning_job)
        """

    async def list_transform_jobs(
        self,
        *,
        CreationTimeAfter: TimestampTypeDef = ...,
        CreationTimeBefore: TimestampTypeDef = ...,
        LastModifiedTimeAfter: TimestampTypeDef = ...,
        LastModifiedTimeBefore: TimestampTypeDef = ...,
        NameContains: str = ...,
        StatusEquals: TransformJobStatusType = ...,
        SortBy: SortByType = ...,
        SortOrder: SortOrderType = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
    ) -> ListTransformJobsResponseTypeDef:
        """
        Lists transform jobs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_transform_jobs)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#list_transform_jobs)
        """

    async def list_trial_components(
        self,
        *,
        ExperimentName: str = ...,
        TrialName: str = ...,
        SourceArn: str = ...,
        CreatedAfter: TimestampTypeDef = ...,
        CreatedBefore: TimestampTypeDef = ...,
        SortBy: SortTrialComponentsByType = ...,
        SortOrder: SortOrderType = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
    ) -> ListTrialComponentsResponseTypeDef:
        """
        Lists the trial components in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_trial_components)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#list_trial_components)
        """

    async def list_trials(
        self,
        *,
        ExperimentName: str = ...,
        TrialComponentName: str = ...,
        CreatedAfter: TimestampTypeDef = ...,
        CreatedBefore: TimestampTypeDef = ...,
        SortBy: SortTrialsByType = ...,
        SortOrder: SortOrderType = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
    ) -> ListTrialsResponseTypeDef:
        """
        Lists the trials in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_trials)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#list_trials)
        """

    async def list_user_profiles(
        self,
        *,
        NextToken: str = ...,
        MaxResults: int = ...,
        SortOrder: SortOrderType = ...,
        SortBy: UserProfileSortKeyType = ...,
        DomainIdEquals: str = ...,
        UserProfileNameContains: str = ...,
    ) -> ListUserProfilesResponseTypeDef:
        """
        Lists user profiles.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_user_profiles)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#list_user_profiles)
        """

    async def list_workforces(
        self,
        *,
        SortBy: ListWorkforcesSortByOptionsType = ...,
        SortOrder: SortOrderType = ...,
        NameContains: str = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
    ) -> ListWorkforcesResponseTypeDef:
        """
        Use this operation to list all private and vendor workforces in an Amazon Web
        Services
        Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_workforces)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#list_workforces)
        """

    async def list_workteams(
        self,
        *,
        SortBy: ListWorkteamsSortByOptionsType = ...,
        SortOrder: SortOrderType = ...,
        NameContains: str = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
    ) -> ListWorkteamsResponseTypeDef:
        """
        Gets a list of private work teams that you have defined in a region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_workteams)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#list_workteams)
        """

    async def put_model_package_group_policy(
        self, *, ModelPackageGroupName: str, ResourcePolicy: str
    ) -> PutModelPackageGroupPolicyOutputTypeDef:
        """
        Adds a resouce policy to control access to a model group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.put_model_package_group_policy)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#put_model_package_group_policy)
        """

    async def query_lineage(
        self,
        *,
        StartArns: Sequence[str] = ...,
        Direction: DirectionType = ...,
        IncludeEdges: bool = ...,
        Filters: QueryFiltersTypeDef = ...,
        MaxDepth: int = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
    ) -> QueryLineageResponseTypeDef:
        """
        Use this action to inspect your lineage and discover relationships between
        entities.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.query_lineage)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#query_lineage)
        """

    async def register_devices(
        self,
        *,
        DeviceFleetName: str,
        Devices: Sequence[DeviceTypeDef],
        Tags: Sequence[TagTypeDef] = ...,
    ) -> EmptyResponseMetadataTypeDef:
        """
        Register devices.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.register_devices)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#register_devices)
        """

    async def render_ui_template(
        self,
        *,
        Task: RenderableTaskTypeDef,
        RoleArn: str,
        UiTemplate: UiTemplateTypeDef = ...,
        HumanTaskUiArn: str = ...,
    ) -> RenderUiTemplateResponseTypeDef:
        """
        Renders the UI template so that you can preview the worker's experience.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.render_ui_template)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#render_ui_template)
        """

    async def retry_pipeline_execution(
        self,
        *,
        PipelineExecutionArn: str,
        ClientRequestToken: str,
        ParallelismConfiguration: ParallelismConfigurationTypeDef = ...,
    ) -> RetryPipelineExecutionResponseTypeDef:
        """
        Retry the execution of the pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.retry_pipeline_execution)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#retry_pipeline_execution)
        """

    async def search(
        self,
        *,
        Resource: ResourceTypeType,
        SearchExpression: "SearchExpressionTypeDef" = ...,
        SortBy: str = ...,
        SortOrder: SearchSortOrderType = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
        CrossAccountFilterOption: CrossAccountFilterOptionType = ...,
        VisibilityConditions: Sequence[VisibilityConditionsTypeDef] = ...,
    ) -> SearchResponseTypeDef:
        """
        Finds SageMaker resources that match a search query.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.search)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#search)
        """

    async def send_pipeline_execution_step_failure(
        self, *, CallbackToken: str, FailureReason: str = ..., ClientRequestToken: str = ...
    ) -> SendPipelineExecutionStepFailureResponseTypeDef:
        """
        Notifies the pipeline that the execution of a callback step failed, along with
        a message describing
        why.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.send_pipeline_execution_step_failure)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#send_pipeline_execution_step_failure)
        """

    async def send_pipeline_execution_step_success(
        self,
        *,
        CallbackToken: str,
        OutputParameters: Sequence[OutputParameterTypeDef] = ...,
        ClientRequestToken: str = ...,
    ) -> SendPipelineExecutionStepSuccessResponseTypeDef:
        """
        Notifies the pipeline that the execution of a callback step succeeded and
        provides a list of the step's output
        parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.send_pipeline_execution_step_success)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#send_pipeline_execution_step_success)
        """

    async def start_edge_deployment_stage(
        self, *, EdgeDeploymentPlanName: str, StageName: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Starts a stage in an edge deployment plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.start_edge_deployment_stage)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#start_edge_deployment_stage)
        """

    async def start_inference_experiment(
        self, *, Name: str
    ) -> StartInferenceExperimentResponseTypeDef:
        """
        Starts an inference experiment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.start_inference_experiment)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#start_inference_experiment)
        """

    async def start_monitoring_schedule(
        self, *, MonitoringScheduleName: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Starts a previously stopped monitoring schedule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.start_monitoring_schedule)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#start_monitoring_schedule)
        """

    async def start_notebook_instance(
        self, *, NotebookInstanceName: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Launches an ML compute instance with the latest version of the libraries and
        attaches your ML storage
        volume.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.start_notebook_instance)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#start_notebook_instance)
        """

    async def start_pipeline_execution(
        self,
        *,
        PipelineName: str,
        ClientRequestToken: str,
        PipelineExecutionDisplayName: str = ...,
        PipelineParameters: Sequence[ParameterTypeDef] = ...,
        PipelineExecutionDescription: str = ...,
        ParallelismConfiguration: ParallelismConfigurationTypeDef = ...,
        SelectiveExecutionConfig: SelectiveExecutionConfigTypeDef = ...,
    ) -> StartPipelineExecutionResponseTypeDef:
        """
        Starts a pipeline execution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.start_pipeline_execution)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#start_pipeline_execution)
        """

    async def stop_auto_ml_job(self, *, AutoMLJobName: str) -> EmptyResponseMetadataTypeDef:
        """
        A method for forcing a running job to shut down.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.stop_auto_ml_job)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#stop_auto_ml_job)
        """

    async def stop_compilation_job(
        self, *, CompilationJobName: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Stops a model compilation job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.stop_compilation_job)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#stop_compilation_job)
        """

    async def stop_edge_deployment_stage(
        self, *, EdgeDeploymentPlanName: str, StageName: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Stops a stage in an edge deployment plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.stop_edge_deployment_stage)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#stop_edge_deployment_stage)
        """

    async def stop_edge_packaging_job(
        self, *, EdgePackagingJobName: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Request to stop an edge packaging job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.stop_edge_packaging_job)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#stop_edge_packaging_job)
        """

    async def stop_hyper_parameter_tuning_job(
        self, *, HyperParameterTuningJobName: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Stops a running hyperparameter tuning job and all running training jobs that
        the tuning job
        launched.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.stop_hyper_parameter_tuning_job)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#stop_hyper_parameter_tuning_job)
        """

    async def stop_inference_experiment(
        self,
        *,
        Name: str,
        ModelVariantActions: Mapping[str, ModelVariantActionType],
        DesiredModelVariants: Sequence[ModelVariantConfigTypeDef] = ...,
        DesiredState: InferenceExperimentStopDesiredStateType = ...,
        Reason: str = ...,
    ) -> StopInferenceExperimentResponseTypeDef:
        """
        Stops an inference experiment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.stop_inference_experiment)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#stop_inference_experiment)
        """

    async def stop_inference_recommendations_job(
        self, *, JobName: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Stops an Inference Recommender job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.stop_inference_recommendations_job)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#stop_inference_recommendations_job)
        """

    async def stop_labeling_job(self, *, LabelingJobName: str) -> EmptyResponseMetadataTypeDef:
        """
        Stops a running labeling job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.stop_labeling_job)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#stop_labeling_job)
        """

    async def stop_monitoring_schedule(
        self, *, MonitoringScheduleName: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Stops a previously started monitoring schedule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.stop_monitoring_schedule)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#stop_monitoring_schedule)
        """

    async def stop_notebook_instance(
        self, *, NotebookInstanceName: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Terminates the ML compute instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.stop_notebook_instance)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#stop_notebook_instance)
        """

    async def stop_pipeline_execution(
        self, *, PipelineExecutionArn: str, ClientRequestToken: str
    ) -> StopPipelineExecutionResponseTypeDef:
        """
        Stops a pipeline execution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.stop_pipeline_execution)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#stop_pipeline_execution)
        """

    async def stop_processing_job(self, *, ProcessingJobName: str) -> EmptyResponseMetadataTypeDef:
        """
        Stops a processing job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.stop_processing_job)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#stop_processing_job)
        """

    async def stop_training_job(self, *, TrainingJobName: str) -> EmptyResponseMetadataTypeDef:
        """
        Stops a training job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.stop_training_job)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#stop_training_job)
        """

    async def stop_transform_job(self, *, TransformJobName: str) -> EmptyResponseMetadataTypeDef:
        """
        Stops a batch transform job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.stop_transform_job)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#stop_transform_job)
        """

    async def update_action(
        self,
        *,
        ActionName: str,
        Description: str = ...,
        Status: ActionStatusType = ...,
        Properties: Mapping[str, str] = ...,
        PropertiesToRemove: Sequence[str] = ...,
    ) -> UpdateActionResponseTypeDef:
        """
        Updates an action.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.update_action)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#update_action)
        """

    async def update_app_image_config(
        self,
        *,
        AppImageConfigName: str,
        KernelGatewayImageConfig: KernelGatewayImageConfigTypeDef = ...,
        JupyterLabAppImageConfig: JupyterLabAppImageConfigTypeDef = ...,
    ) -> UpdateAppImageConfigResponseTypeDef:
        """
        Updates the properties of an AppImageConfig.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.update_app_image_config)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#update_app_image_config)
        """

    async def update_artifact(
        self,
        *,
        ArtifactArn: str,
        ArtifactName: str = ...,
        Properties: Mapping[str, str] = ...,
        PropertiesToRemove: Sequence[str] = ...,
    ) -> UpdateArtifactResponseTypeDef:
        """
        Updates an artifact.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.update_artifact)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#update_artifact)
        """

    async def update_cluster(
        self,
        *,
        ClusterName: str,
        InstanceGroups: Sequence[ClusterInstanceGroupSpecificationTypeDef],
    ) -> UpdateClusterResponseTypeDef:
        """
        Update a SageMaker HyperPod cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.update_cluster)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#update_cluster)
        """

    async def update_code_repository(
        self, *, CodeRepositoryName: str, GitConfig: GitConfigForUpdateTypeDef = ...
    ) -> UpdateCodeRepositoryOutputTypeDef:
        """
        Updates the specified Git repository with the specified values.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.update_code_repository)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#update_code_repository)
        """

    async def update_context(
        self,
        *,
        ContextName: str,
        Description: str = ...,
        Properties: Mapping[str, str] = ...,
        PropertiesToRemove: Sequence[str] = ...,
    ) -> UpdateContextResponseTypeDef:
        """
        Updates a context.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.update_context)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#update_context)
        """

    async def update_device_fleet(
        self,
        *,
        DeviceFleetName: str,
        OutputConfig: EdgeOutputConfigTypeDef,
        RoleArn: str = ...,
        Description: str = ...,
        EnableIotRoleAlias: bool = ...,
    ) -> EmptyResponseMetadataTypeDef:
        """
        Updates a fleet of devices.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.update_device_fleet)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#update_device_fleet)
        """

    async def update_devices(
        self, *, DeviceFleetName: str, Devices: Sequence[DeviceTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Updates one or more devices in a fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.update_devices)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#update_devices)
        """

    async def update_domain(
        self,
        *,
        DomainId: str,
        DefaultUserSettings: UserSettingsTypeDef = ...,
        DomainSettingsForUpdate: DomainSettingsForUpdateTypeDef = ...,
        AppSecurityGroupManagement: AppSecurityGroupManagementType = ...,
        DefaultSpaceSettings: DefaultSpaceSettingsTypeDef = ...,
        SubnetIds: Sequence[str] = ...,
        AppNetworkAccessType: AppNetworkAccessTypeType = ...,
    ) -> UpdateDomainResponseTypeDef:
        """
        Updates the default settings for new user profiles in the domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.update_domain)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#update_domain)
        """

    async def update_endpoint(
        self,
        *,
        EndpointName: str,
        EndpointConfigName: str,
        RetainAllVariantProperties: bool = ...,
        ExcludeRetainedVariantProperties: Sequence[VariantPropertyTypeDef] = ...,
        DeploymentConfig: DeploymentConfigTypeDef = ...,
        RetainDeploymentConfig: bool = ...,
    ) -> UpdateEndpointOutputTypeDef:
        """
        Deploys the `EndpointConfig` specified in the request to a new fleet of
        instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.update_endpoint)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#update_endpoint)
        """

    async def update_endpoint_weights_and_capacities(
        self,
        *,
        EndpointName: str,
        DesiredWeightsAndCapacities: Sequence[DesiredWeightAndCapacityTypeDef],
    ) -> UpdateEndpointWeightsAndCapacitiesOutputTypeDef:
        """
        Updates variant weight of one or more variants associated with an existing
        endpoint, or capacity of one variant associated with an existing
        endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.update_endpoint_weights_and_capacities)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#update_endpoint_weights_and_capacities)
        """

    async def update_experiment(
        self, *, ExperimentName: str, DisplayName: str = ..., Description: str = ...
    ) -> UpdateExperimentResponseTypeDef:
        """
        Adds, updates, or removes the description of an experiment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.update_experiment)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#update_experiment)
        """

    async def update_feature_group(
        self,
        *,
        FeatureGroupName: str,
        FeatureAdditions: Sequence[FeatureDefinitionTypeDef] = ...,
        OnlineStoreConfig: OnlineStoreConfigUpdateTypeDef = ...,
        ThroughputConfig: ThroughputConfigUpdateTypeDef = ...,
    ) -> UpdateFeatureGroupResponseTypeDef:
        """
        Updates the feature group by either adding features or updating the online
        store
        configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.update_feature_group)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#update_feature_group)
        """

    async def update_feature_metadata(
        self,
        *,
        FeatureGroupName: str,
        FeatureName: str,
        Description: str = ...,
        ParameterAdditions: Sequence[FeatureParameterTypeDef] = ...,
        ParameterRemovals: Sequence[str] = ...,
    ) -> EmptyResponseMetadataTypeDef:
        """
        Updates the description and parameters of the feature group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.update_feature_metadata)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#update_feature_metadata)
        """

    async def update_hub(
        self,
        *,
        HubName: str,
        HubDescription: str = ...,
        HubDisplayName: str = ...,
        HubSearchKeywords: Sequence[str] = ...,
    ) -> UpdateHubResponseTypeDef:
        """
        Update a hub.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.update_hub)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#update_hub)
        """

    async def update_image(
        self,
        *,
        ImageName: str,
        DeleteProperties: Sequence[str] = ...,
        Description: str = ...,
        DisplayName: str = ...,
        RoleArn: str = ...,
    ) -> UpdateImageResponseTypeDef:
        """
        Updates the properties of a SageMaker image.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.update_image)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#update_image)
        """

    async def update_image_version(
        self,
        *,
        ImageName: str,
        Alias: str = ...,
        Version: int = ...,
        AliasesToAdd: Sequence[str] = ...,
        AliasesToDelete: Sequence[str] = ...,
        VendorGuidance: VendorGuidanceType = ...,
        JobType: JobTypeType = ...,
        MLFramework: str = ...,
        ProgrammingLang: str = ...,
        Processor: ProcessorType = ...,
        Horovod: bool = ...,
        ReleaseNotes: str = ...,
    ) -> UpdateImageVersionResponseTypeDef:
        """
        Updates the properties of a SageMaker image version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.update_image_version)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#update_image_version)
        """

    async def update_inference_component(
        self,
        *,
        InferenceComponentName: str,
        Specification: InferenceComponentSpecificationTypeDef = ...,
        RuntimeConfig: InferenceComponentRuntimeConfigTypeDef = ...,
    ) -> UpdateInferenceComponentOutputTypeDef:
        """
        Updates an inference component.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.update_inference_component)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#update_inference_component)
        """

    async def update_inference_component_runtime_config(
        self,
        *,
        InferenceComponentName: str,
        DesiredRuntimeConfig: InferenceComponentRuntimeConfigTypeDef,
    ) -> UpdateInferenceComponentRuntimeConfigOutputTypeDef:
        """
        Runtime settings for a model that is deployed with an inference component.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.update_inference_component_runtime_config)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#update_inference_component_runtime_config)
        """

    async def update_inference_experiment(
        self,
        *,
        Name: str,
        Schedule: InferenceExperimentScheduleTypeDef = ...,
        Description: str = ...,
        ModelVariants: Sequence[ModelVariantConfigTypeDef] = ...,
        DataStorageConfig: InferenceExperimentDataStorageConfigTypeDef = ...,
        ShadowModeConfig: ShadowModeConfigTypeDef = ...,
    ) -> UpdateInferenceExperimentResponseTypeDef:
        """
        Updates an inference experiment that you created.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.update_inference_experiment)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#update_inference_experiment)
        """

    async def update_model_card(
        self, *, ModelCardName: str, Content: str = ..., ModelCardStatus: ModelCardStatusType = ...
    ) -> UpdateModelCardResponseTypeDef:
        """
        Update an Amazon SageMaker Model Card.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.update_model_card)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#update_model_card)
        """

    async def update_model_package(
        self,
        *,
        ModelPackageArn: str,
        ModelApprovalStatus: ModelApprovalStatusType = ...,
        ApprovalDescription: str = ...,
        CustomerMetadataProperties: Mapping[str, str] = ...,
        CustomerMetadataPropertiesToRemove: Sequence[str] = ...,
        AdditionalInferenceSpecificationsToAdd: Sequence[
            AdditionalInferenceSpecificationDefinitionTypeDef
        ] = ...,
    ) -> UpdateModelPackageOutputTypeDef:
        """
        Updates a versioned model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.update_model_package)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#update_model_package)
        """

    async def update_monitoring_alert(
        self,
        *,
        MonitoringScheduleName: str,
        MonitoringAlertName: str,
        DatapointsToAlert: int,
        EvaluationPeriod: int,
    ) -> UpdateMonitoringAlertResponseTypeDef:
        """
        Update the parameters of a model monitor alert.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.update_monitoring_alert)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#update_monitoring_alert)
        """

    async def update_monitoring_schedule(
        self,
        *,
        MonitoringScheduleName: str,
        MonitoringScheduleConfig: MonitoringScheduleConfigTypeDef,
    ) -> UpdateMonitoringScheduleResponseTypeDef:
        """
        Updates a previously created schedule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.update_monitoring_schedule)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#update_monitoring_schedule)
        """

    async def update_notebook_instance(
        self,
        *,
        NotebookInstanceName: str,
        InstanceType: InstanceTypeType = ...,
        RoleArn: str = ...,
        LifecycleConfigName: str = ...,
        DisassociateLifecycleConfig: bool = ...,
        VolumeSizeInGB: int = ...,
        DefaultCodeRepository: str = ...,
        AdditionalCodeRepositories: Sequence[str] = ...,
        AcceleratorTypes: Sequence[NotebookInstanceAcceleratorTypeType] = ...,
        DisassociateAcceleratorTypes: bool = ...,
        DisassociateDefaultCodeRepository: bool = ...,
        DisassociateAdditionalCodeRepositories: bool = ...,
        RootAccess: RootAccessType = ...,
        InstanceMetadataServiceConfiguration: InstanceMetadataServiceConfigurationTypeDef = ...,
    ) -> Dict[str, Any]:
        """
        Updates a notebook instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.update_notebook_instance)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#update_notebook_instance)
        """

    async def update_notebook_instance_lifecycle_config(
        self,
        *,
        NotebookInstanceLifecycleConfigName: str,
        OnCreate: Sequence[NotebookInstanceLifecycleHookTypeDef] = ...,
        OnStart: Sequence[NotebookInstanceLifecycleHookTypeDef] = ...,
    ) -> Dict[str, Any]:
        """
        Updates a notebook instance lifecycle configuration created with the
        [CreateNotebookInstanceLifecycleConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateNotebookInstanceLifecycleConfig.html)
        API.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.update_notebook_instance_lifecycle_config)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#update_notebook_instance_lifecycle_config)
        """

    async def update_pipeline(
        self,
        *,
        PipelineName: str,
        PipelineDisplayName: str = ...,
        PipelineDefinition: str = ...,
        PipelineDefinitionS3Location: PipelineDefinitionS3LocationTypeDef = ...,
        PipelineDescription: str = ...,
        RoleArn: str = ...,
        ParallelismConfiguration: ParallelismConfigurationTypeDef = ...,
    ) -> UpdatePipelineResponseTypeDef:
        """
        Updates a pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.update_pipeline)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#update_pipeline)
        """

    async def update_pipeline_execution(
        self,
        *,
        PipelineExecutionArn: str,
        PipelineExecutionDescription: str = ...,
        PipelineExecutionDisplayName: str = ...,
        ParallelismConfiguration: ParallelismConfigurationTypeDef = ...,
    ) -> UpdatePipelineExecutionResponseTypeDef:
        """
        Updates a pipeline execution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.update_pipeline_execution)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#update_pipeline_execution)
        """

    async def update_project(
        self,
        *,
        ProjectName: str,
        ProjectDescription: str = ...,
        ServiceCatalogProvisioningUpdateDetails: ServiceCatalogProvisioningUpdateDetailsTypeDef = ...,
        Tags: Sequence[TagTypeDef] = ...,
    ) -> UpdateProjectOutputTypeDef:
        """
        Updates a machine learning (ML) project that is created from a template that
        sets up an ML pipeline from training to deploying an approved
        model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.update_project)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#update_project)
        """

    async def update_space(
        self,
        *,
        DomainId: str,
        SpaceName: str,
        SpaceSettings: SpaceSettingsTypeDef = ...,
        SpaceDisplayName: str = ...,
    ) -> UpdateSpaceResponseTypeDef:
        """
        Updates the settings of a space.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.update_space)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#update_space)
        """

    async def update_training_job(
        self,
        *,
        TrainingJobName: str,
        ProfilerConfig: ProfilerConfigForUpdateTypeDef = ...,
        ProfilerRuleConfigurations: Sequence[ProfilerRuleConfigurationTypeDef] = ...,
        ResourceConfig: ResourceConfigForUpdateTypeDef = ...,
        RemoteDebugConfig: RemoteDebugConfigForUpdateTypeDef = ...,
    ) -> UpdateTrainingJobResponseTypeDef:
        """
        Update a model training job to request a new Debugger profiling configuration
        or to change warm pool retention
        length.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.update_training_job)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#update_training_job)
        """

    async def update_trial(
        self, *, TrialName: str, DisplayName: str = ...
    ) -> UpdateTrialResponseTypeDef:
        """
        Updates the display name of a trial.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.update_trial)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#update_trial)
        """

    async def update_trial_component(
        self,
        *,
        TrialComponentName: str,
        DisplayName: str = ...,
        Status: TrialComponentStatusTypeDef = ...,
        StartTime: TimestampTypeDef = ...,
        EndTime: TimestampTypeDef = ...,
        Parameters: Mapping[str, TrialComponentParameterValueTypeDef] = ...,
        ParametersToRemove: Sequence[str] = ...,
        InputArtifacts: Mapping[str, TrialComponentArtifactTypeDef] = ...,
        InputArtifactsToRemove: Sequence[str] = ...,
        OutputArtifacts: Mapping[str, TrialComponentArtifactTypeDef] = ...,
        OutputArtifactsToRemove: Sequence[str] = ...,
    ) -> UpdateTrialComponentResponseTypeDef:
        """
        Updates one or more properties of a trial component.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.update_trial_component)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#update_trial_component)
        """

    async def update_user_profile(
        self, *, DomainId: str, UserProfileName: str, UserSettings: UserSettingsTypeDef = ...
    ) -> UpdateUserProfileResponseTypeDef:
        """
        Updates a user profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.update_user_profile)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#update_user_profile)
        """

    async def update_workforce(
        self,
        *,
        WorkforceName: str,
        SourceIpConfig: SourceIpConfigTypeDef = ...,
        OidcConfig: OidcConfigTypeDef = ...,
        WorkforceVpcConfig: WorkforceVpcConfigRequestTypeDef = ...,
    ) -> UpdateWorkforceResponseTypeDef:
        """
        Use this operation to update your workforce.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.update_workforce)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#update_workforce)
        """

    async def update_workteam(
        self,
        *,
        WorkteamName: str,
        MemberDefinitions: Sequence[MemberDefinitionTypeDef] = ...,
        Description: str = ...,
        NotificationConfiguration: NotificationConfigurationTypeDef = ...,
    ) -> UpdateWorkteamResponseTypeDef:
        """
        Updates an existing work team with new member definitions or description.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.update_workteam)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#update_workteam)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_actions"]) -> ListActionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_algorithms"]) -> ListAlgorithmsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_aliases"]) -> ListAliasesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_app_image_configs"]
    ) -> ListAppImageConfigsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_apps"]) -> ListAppsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_artifacts"]) -> ListArtifactsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_associations"]
    ) -> ListAssociationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_auto_ml_jobs"]
    ) -> ListAutoMLJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_candidates_for_auto_ml_job"]
    ) -> ListCandidatesForAutoMLJobPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_cluster_nodes"]
    ) -> ListClusterNodesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_clusters"]) -> ListClustersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_code_repositories"]
    ) -> ListCodeRepositoriesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_compilation_jobs"]
    ) -> ListCompilationJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_contexts"]) -> ListContextsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_data_quality_job_definitions"]
    ) -> ListDataQualityJobDefinitionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_device_fleets"]
    ) -> ListDeviceFleetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_devices"]) -> ListDevicesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_domains"]) -> ListDomainsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_edge_deployment_plans"]
    ) -> ListEdgeDeploymentPlansPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_edge_packaging_jobs"]
    ) -> ListEdgePackagingJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_endpoint_configs"]
    ) -> ListEndpointConfigsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_endpoints"]) -> ListEndpointsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_experiments"]
    ) -> ListExperimentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_feature_groups"]
    ) -> ListFeatureGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_flow_definitions"]
    ) -> ListFlowDefinitionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_human_task_uis"]
    ) -> ListHumanTaskUisPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_hyper_parameter_tuning_jobs"]
    ) -> ListHyperParameterTuningJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_image_versions"]
    ) -> ListImageVersionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_images"]) -> ListImagesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_inference_components"]
    ) -> ListInferenceComponentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_inference_experiments"]
    ) -> ListInferenceExperimentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_inference_recommendations_job_steps"]
    ) -> ListInferenceRecommendationsJobStepsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_inference_recommendations_jobs"]
    ) -> ListInferenceRecommendationsJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_labeling_jobs"]
    ) -> ListLabelingJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_labeling_jobs_for_workteam"]
    ) -> ListLabelingJobsForWorkteamPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_lineage_groups"]
    ) -> ListLineageGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_model_bias_job_definitions"]
    ) -> ListModelBiasJobDefinitionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_model_card_export_jobs"]
    ) -> ListModelCardExportJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_model_card_versions"]
    ) -> ListModelCardVersionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_model_cards"]) -> ListModelCardsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_model_explainability_job_definitions"]
    ) -> ListModelExplainabilityJobDefinitionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_model_metadata"]
    ) -> ListModelMetadataPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_model_package_groups"]
    ) -> ListModelPackageGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_model_packages"]
    ) -> ListModelPackagesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_model_quality_job_definitions"]
    ) -> ListModelQualityJobDefinitionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_models"]) -> ListModelsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_monitoring_alert_history"]
    ) -> ListMonitoringAlertHistoryPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_monitoring_alerts"]
    ) -> ListMonitoringAlertsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_monitoring_executions"]
    ) -> ListMonitoringExecutionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_monitoring_schedules"]
    ) -> ListMonitoringSchedulesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_notebook_instance_lifecycle_configs"]
    ) -> ListNotebookInstanceLifecycleConfigsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_notebook_instances"]
    ) -> ListNotebookInstancesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_pipeline_execution_steps"]
    ) -> ListPipelineExecutionStepsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_pipeline_executions"]
    ) -> ListPipelineExecutionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_pipeline_parameters_for_execution"]
    ) -> ListPipelineParametersForExecutionPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_pipelines"]) -> ListPipelinesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_processing_jobs"]
    ) -> ListProcessingJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_resource_catalogs"]
    ) -> ListResourceCatalogsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_spaces"]) -> ListSpacesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_stage_devices"]
    ) -> ListStageDevicesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_studio_lifecycle_configs"]
    ) -> ListStudioLifecycleConfigsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_subscribed_workteams"]
    ) -> ListSubscribedWorkteamsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_tags"]) -> ListTagsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_training_jobs"]
    ) -> ListTrainingJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_training_jobs_for_hyper_parameter_tuning_job"]
    ) -> ListTrainingJobsForHyperParameterTuningJobPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_transform_jobs"]
    ) -> ListTransformJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_trial_components"]
    ) -> ListTrialComponentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_trials"]) -> ListTrialsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_user_profiles"]
    ) -> ListUserProfilesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_workforces"]) -> ListWorkforcesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_workteams"]) -> ListWorkteamsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["search"]) -> SearchPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#get_paginator)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["endpoint_deleted"]) -> EndpointDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_waiter)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#get_waiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["endpoint_in_service"]) -> EndpointInServiceWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_waiter)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#get_waiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["image_created"]) -> ImageCreatedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_waiter)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#get_waiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["image_deleted"]) -> ImageDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_waiter)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#get_waiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["image_updated"]) -> ImageUpdatedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_waiter)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#get_waiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["image_version_created"]
    ) -> ImageVersionCreatedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_waiter)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#get_waiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["image_version_deleted"]
    ) -> ImageVersionDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_waiter)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#get_waiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["notebook_instance_deleted"]
    ) -> NotebookInstanceDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_waiter)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#get_waiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["notebook_instance_in_service"]
    ) -> NotebookInstanceInServiceWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_waiter)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#get_waiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["notebook_instance_stopped"]
    ) -> NotebookInstanceStoppedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_waiter)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#get_waiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["processing_job_completed_or_stopped"]
    ) -> ProcessingJobCompletedOrStoppedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_waiter)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#get_waiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["training_job_completed_or_stopped"]
    ) -> TrainingJobCompletedOrStoppedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_waiter)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#get_waiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["transform_job_completed_or_stopped"]
    ) -> TransformJobCompletedOrStoppedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_waiter)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/#get_waiter)
        """

    async def __aenter__(self) -> "SageMakerClient":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/)
        """

    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> Any:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/client/)
        """
