"""
Type annotations for lookoutequipment service client.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lookoutequipment/client/)

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_lookoutequipment.client import LookoutEquipmentClient

    session = get_session()
    async with session.create_client("lookoutequipment") as client:
        client: LookoutEquipmentClient
    ```
"""

from typing import Any, Dict, Mapping, Sequence, Type

from aiobotocore.client import AioBaseClient
from botocore.client import ClientMeta

from .literals import (
    DataUploadFrequencyType,
    InferenceDataImportStrategyType,
    InferenceExecutionStatusType,
    InferenceSchedulerStatusType,
    IngestionJobStatusType,
    LabelRatingType,
    ModelPromoteModeType,
    ModelStatusType,
    ModelVersionSourceTypeType,
    ModelVersionStatusType,
    RetrainingSchedulerStatusType,
)
from .type_defs import (
    CreateDatasetResponseTypeDef,
    CreateInferenceSchedulerResponseTypeDef,
    CreateLabelGroupResponseTypeDef,
    CreateLabelResponseTypeDef,
    CreateModelResponseTypeDef,
    CreateRetrainingSchedulerResponseTypeDef,
    DataPreProcessingConfigurationTypeDef,
    DatasetSchemaTypeDef,
    DescribeDataIngestionJobResponseTypeDef,
    DescribeDatasetResponseTypeDef,
    DescribeInferenceSchedulerResponseTypeDef,
    DescribeLabelGroupResponseTypeDef,
    DescribeLabelResponseTypeDef,
    DescribeModelResponseTypeDef,
    DescribeModelVersionResponseTypeDef,
    DescribeResourcePolicyResponseTypeDef,
    DescribeRetrainingSchedulerResponseTypeDef,
    EmptyResponseMetadataTypeDef,
    ImportDatasetResponseTypeDef,
    ImportModelVersionResponseTypeDef,
    InferenceInputConfigurationTypeDef,
    InferenceOutputConfigurationTypeDef,
    IngestionInputConfigurationTypeDef,
    LabelsInputConfigurationTypeDef,
    ListDataIngestionJobsResponseTypeDef,
    ListDatasetsResponseTypeDef,
    ListInferenceEventsResponseTypeDef,
    ListInferenceExecutionsResponseTypeDef,
    ListInferenceSchedulersResponseTypeDef,
    ListLabelGroupsResponseTypeDef,
    ListLabelsResponseTypeDef,
    ListModelsResponseTypeDef,
    ListModelVersionsResponseTypeDef,
    ListRetrainingSchedulersResponseTypeDef,
    ListSensorStatisticsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    PutResourcePolicyResponseTypeDef,
    StartDataIngestionJobResponseTypeDef,
    StartInferenceSchedulerResponseTypeDef,
    StartRetrainingSchedulerResponseTypeDef,
    StopInferenceSchedulerResponseTypeDef,
    StopRetrainingSchedulerResponseTypeDef,
    TagTypeDef,
    TimestampTypeDef,
    UpdateActiveModelVersionResponseTypeDef,
)

__all__ = ("LookoutEquipmentClient",)


class BotocoreClientError(Exception):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class LookoutEquipmentClient(AioBaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutequipment.html#LookoutEquipment.Client)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lookoutequipment/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        LookoutEquipmentClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutequipment.html#LookoutEquipment.Client.exceptions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lookoutequipment/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutequipment.html#LookoutEquipment.Client.can_paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lookoutequipment/client/#can_paginate)
        """

    async def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutequipment.html#LookoutEquipment.Client.close)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lookoutequipment/client/#close)
        """

    async def create_dataset(
        self,
        *,
        DatasetName: str,
        ClientToken: str,
        DatasetSchema: DatasetSchemaTypeDef = ...,
        ServerSideKmsKeyId: str = ...,
        Tags: Sequence[TagTypeDef] = ...,
    ) -> CreateDatasetResponseTypeDef:
        """
        Creates a container for a collection of data being ingested for analysis.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutequipment.html#LookoutEquipment.Client.create_dataset)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lookoutequipment/client/#create_dataset)
        """

    async def create_inference_scheduler(
        self,
        *,
        ModelName: str,
        InferenceSchedulerName: str,
        DataUploadFrequency: DataUploadFrequencyType,
        DataInputConfiguration: InferenceInputConfigurationTypeDef,
        DataOutputConfiguration: InferenceOutputConfigurationTypeDef,
        RoleArn: str,
        ClientToken: str,
        DataDelayOffsetInMinutes: int = ...,
        ServerSideKmsKeyId: str = ...,
        Tags: Sequence[TagTypeDef] = ...,
    ) -> CreateInferenceSchedulerResponseTypeDef:
        """
        Creates a scheduled inference.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutequipment.html#LookoutEquipment.Client.create_inference_scheduler)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lookoutequipment/client/#create_inference_scheduler)
        """

    async def create_label(
        self,
        *,
        LabelGroupName: str,
        StartTime: TimestampTypeDef,
        EndTime: TimestampTypeDef,
        Rating: LabelRatingType,
        ClientToken: str,
        FaultCode: str = ...,
        Notes: str = ...,
        Equipment: str = ...,
    ) -> CreateLabelResponseTypeDef:
        """
        Creates a label for an event.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutequipment.html#LookoutEquipment.Client.create_label)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lookoutequipment/client/#create_label)
        """

    async def create_label_group(
        self,
        *,
        LabelGroupName: str,
        ClientToken: str,
        FaultCodes: Sequence[str] = ...,
        Tags: Sequence[TagTypeDef] = ...,
    ) -> CreateLabelGroupResponseTypeDef:
        """
        Creates a group of labels.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutequipment.html#LookoutEquipment.Client.create_label_group)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lookoutequipment/client/#create_label_group)
        """

    async def create_model(
        self,
        *,
        ModelName: str,
        DatasetName: str,
        ClientToken: str,
        DatasetSchema: DatasetSchemaTypeDef = ...,
        LabelsInputConfiguration: LabelsInputConfigurationTypeDef = ...,
        TrainingDataStartTime: TimestampTypeDef = ...,
        TrainingDataEndTime: TimestampTypeDef = ...,
        EvaluationDataStartTime: TimestampTypeDef = ...,
        EvaluationDataEndTime: TimestampTypeDef = ...,
        RoleArn: str = ...,
        DataPreProcessingConfiguration: DataPreProcessingConfigurationTypeDef = ...,
        ServerSideKmsKeyId: str = ...,
        Tags: Sequence[TagTypeDef] = ...,
        OffCondition: str = ...,
    ) -> CreateModelResponseTypeDef:
        """
        Creates a machine learning model for data inference.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutequipment.html#LookoutEquipment.Client.create_model)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lookoutequipment/client/#create_model)
        """

    async def create_retraining_scheduler(
        self,
        *,
        ModelName: str,
        RetrainingFrequency: str,
        LookbackWindow: str,
        ClientToken: str,
        RetrainingStartDate: TimestampTypeDef = ...,
        PromoteMode: ModelPromoteModeType = ...,
    ) -> CreateRetrainingSchedulerResponseTypeDef:
        """
        Creates a retraining scheduler on the specified model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutequipment.html#LookoutEquipment.Client.create_retraining_scheduler)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lookoutequipment/client/#create_retraining_scheduler)
        """

    async def delete_dataset(self, *, DatasetName: str) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a dataset and associated artifacts.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutequipment.html#LookoutEquipment.Client.delete_dataset)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lookoutequipment/client/#delete_dataset)
        """

    async def delete_inference_scheduler(
        self, *, InferenceSchedulerName: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes an inference scheduler that has been set up.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutequipment.html#LookoutEquipment.Client.delete_inference_scheduler)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lookoutequipment/client/#delete_inference_scheduler)
        """

    async def delete_label(
        self, *, LabelGroupName: str, LabelId: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a label.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutequipment.html#LookoutEquipment.Client.delete_label)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lookoutequipment/client/#delete_label)
        """

    async def delete_label_group(self, *, LabelGroupName: str) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a group of labels.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutequipment.html#LookoutEquipment.Client.delete_label_group)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lookoutequipment/client/#delete_label_group)
        """

    async def delete_model(self, *, ModelName: str) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a machine learning model currently available for Amazon Lookout for
        Equipment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutequipment.html#LookoutEquipment.Client.delete_model)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lookoutequipment/client/#delete_model)
        """

    async def delete_resource_policy(self, *, ResourceArn: str) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the resource policy attached to the resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutequipment.html#LookoutEquipment.Client.delete_resource_policy)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lookoutequipment/client/#delete_resource_policy)
        """

    async def delete_retraining_scheduler(self, *, ModelName: str) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a retraining scheduler from a model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutequipment.html#LookoutEquipment.Client.delete_retraining_scheduler)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lookoutequipment/client/#delete_retraining_scheduler)
        """

    async def describe_data_ingestion_job(
        self, *, JobId: str
    ) -> DescribeDataIngestionJobResponseTypeDef:
        """
        Provides information on a specific data ingestion job such as creation time,
        dataset ARN, and
        status.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutequipment.html#LookoutEquipment.Client.describe_data_ingestion_job)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lookoutequipment/client/#describe_data_ingestion_job)
        """

    async def describe_dataset(self, *, DatasetName: str) -> DescribeDatasetResponseTypeDef:
        """
        Provides a JSON description of the data in each time series dataset, including
        names, column names, and data
        types.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutequipment.html#LookoutEquipment.Client.describe_dataset)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lookoutequipment/client/#describe_dataset)
        """

    async def describe_inference_scheduler(
        self, *, InferenceSchedulerName: str
    ) -> DescribeInferenceSchedulerResponseTypeDef:
        """
        Specifies information about the inference scheduler being used, including name,
        model, status, and associated metadata See also: [AWS API
        Documentation](https://docs.aws.amazon.com/goto/WebAPI/lookoutequipment-2020-12-15/DescribeInferenceScheduler).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutequipment.html#LookoutEquipment.Client.describe_inference_scheduler)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lookoutequipment/client/#describe_inference_scheduler)
        """

    async def describe_label(
        self, *, LabelGroupName: str, LabelId: str
    ) -> DescribeLabelResponseTypeDef:
        """
        Returns the name of the label.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutequipment.html#LookoutEquipment.Client.describe_label)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lookoutequipment/client/#describe_label)
        """

    async def describe_label_group(
        self, *, LabelGroupName: str
    ) -> DescribeLabelGroupResponseTypeDef:
        """
        Returns information about the label group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutequipment.html#LookoutEquipment.Client.describe_label_group)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lookoutequipment/client/#describe_label_group)
        """

    async def describe_model(self, *, ModelName: str) -> DescribeModelResponseTypeDef:
        """
        Provides a JSON containing the overall information about a specific machine
        learning model, including model name and ARN, dataset, training and evaluation
        information, status, and so
        on.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutequipment.html#LookoutEquipment.Client.describe_model)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lookoutequipment/client/#describe_model)
        """

    async def describe_model_version(
        self, *, ModelName: str, ModelVersion: int
    ) -> DescribeModelVersionResponseTypeDef:
        """
        Retrieves information about a specific machine learning model version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutequipment.html#LookoutEquipment.Client.describe_model_version)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lookoutequipment/client/#describe_model_version)
        """

    async def describe_resource_policy(
        self, *, ResourceArn: str
    ) -> DescribeResourcePolicyResponseTypeDef:
        """
        Provides the details of a resource policy attached to a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutequipment.html#LookoutEquipment.Client.describe_resource_policy)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lookoutequipment/client/#describe_resource_policy)
        """

    async def describe_retraining_scheduler(
        self, *, ModelName: str
    ) -> DescribeRetrainingSchedulerResponseTypeDef:
        """
        Provides a description of the retraining scheduler, including information such
        as the model name and retraining
        parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutequipment.html#LookoutEquipment.Client.describe_retraining_scheduler)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lookoutequipment/client/#describe_retraining_scheduler)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutequipment.html#LookoutEquipment.Client.generate_presigned_url)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lookoutequipment/client/#generate_presigned_url)
        """

    async def import_dataset(
        self,
        *,
        SourceDatasetArn: str,
        ClientToken: str,
        DatasetName: str = ...,
        ServerSideKmsKeyId: str = ...,
        Tags: Sequence[TagTypeDef] = ...,
    ) -> ImportDatasetResponseTypeDef:
        """
        Imports a dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutequipment.html#LookoutEquipment.Client.import_dataset)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lookoutequipment/client/#import_dataset)
        """

    async def import_model_version(
        self,
        *,
        SourceModelVersionArn: str,
        DatasetName: str,
        ClientToken: str,
        ModelName: str = ...,
        LabelsInputConfiguration: LabelsInputConfigurationTypeDef = ...,
        RoleArn: str = ...,
        ServerSideKmsKeyId: str = ...,
        Tags: Sequence[TagTypeDef] = ...,
        InferenceDataImportStrategy: InferenceDataImportStrategyType = ...,
    ) -> ImportModelVersionResponseTypeDef:
        """
        Imports a model that has been trained successfully.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutequipment.html#LookoutEquipment.Client.import_model_version)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lookoutequipment/client/#import_model_version)
        """

    async def list_data_ingestion_jobs(
        self,
        *,
        DatasetName: str = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
        Status: IngestionJobStatusType = ...,
    ) -> ListDataIngestionJobsResponseTypeDef:
        """
        Provides a list of all data ingestion jobs, including dataset name and ARN, S3
        location of the input data, status, and so
        on.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutequipment.html#LookoutEquipment.Client.list_data_ingestion_jobs)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lookoutequipment/client/#list_data_ingestion_jobs)
        """

    async def list_datasets(
        self, *, NextToken: str = ..., MaxResults: int = ..., DatasetNameBeginsWith: str = ...
    ) -> ListDatasetsResponseTypeDef:
        """
        Lists all datasets currently available in your account, filtering on the
        dataset
        name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutequipment.html#LookoutEquipment.Client.list_datasets)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lookoutequipment/client/#list_datasets)
        """

    async def list_inference_events(
        self,
        *,
        InferenceSchedulerName: str,
        IntervalStartTime: TimestampTypeDef,
        IntervalEndTime: TimestampTypeDef,
        NextToken: str = ...,
        MaxResults: int = ...,
    ) -> ListInferenceEventsResponseTypeDef:
        """
        Lists all inference events that have been found for the specified inference
        scheduler.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutequipment.html#LookoutEquipment.Client.list_inference_events)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lookoutequipment/client/#list_inference_events)
        """

    async def list_inference_executions(
        self,
        *,
        InferenceSchedulerName: str,
        NextToken: str = ...,
        MaxResults: int = ...,
        DataStartTimeAfter: TimestampTypeDef = ...,
        DataEndTimeBefore: TimestampTypeDef = ...,
        Status: InferenceExecutionStatusType = ...,
    ) -> ListInferenceExecutionsResponseTypeDef:
        """
        Lists all inference executions that have been performed by the specified
        inference
        scheduler.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutequipment.html#LookoutEquipment.Client.list_inference_executions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lookoutequipment/client/#list_inference_executions)
        """

    async def list_inference_schedulers(
        self,
        *,
        NextToken: str = ...,
        MaxResults: int = ...,
        InferenceSchedulerNameBeginsWith: str = ...,
        ModelName: str = ...,
        Status: InferenceSchedulerStatusType = ...,
    ) -> ListInferenceSchedulersResponseTypeDef:
        """
        Retrieves a list of all inference schedulers currently available for your
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutequipment.html#LookoutEquipment.Client.list_inference_schedulers)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lookoutequipment/client/#list_inference_schedulers)
        """

    async def list_label_groups(
        self, *, LabelGroupNameBeginsWith: str = ..., NextToken: str = ..., MaxResults: int = ...
    ) -> ListLabelGroupsResponseTypeDef:
        """
        Returns a list of the label groups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutequipment.html#LookoutEquipment.Client.list_label_groups)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lookoutequipment/client/#list_label_groups)
        """

    async def list_labels(
        self,
        *,
        LabelGroupName: str,
        IntervalStartTime: TimestampTypeDef = ...,
        IntervalEndTime: TimestampTypeDef = ...,
        FaultCode: str = ...,
        Equipment: str = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
    ) -> ListLabelsResponseTypeDef:
        """
        Provides a list of labels.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutequipment.html#LookoutEquipment.Client.list_labels)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lookoutequipment/client/#list_labels)
        """

    async def list_model_versions(
        self,
        *,
        ModelName: str,
        NextToken: str = ...,
        MaxResults: int = ...,
        Status: ModelVersionStatusType = ...,
        SourceType: ModelVersionSourceTypeType = ...,
        CreatedAtEndTime: TimestampTypeDef = ...,
        CreatedAtStartTime: TimestampTypeDef = ...,
        MaxModelVersion: int = ...,
        MinModelVersion: int = ...,
    ) -> ListModelVersionsResponseTypeDef:
        """
        Generates a list of all model versions for a given model, including the model
        version, model version ARN, and
        status.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutequipment.html#LookoutEquipment.Client.list_model_versions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lookoutequipment/client/#list_model_versions)
        """

    async def list_models(
        self,
        *,
        NextToken: str = ...,
        MaxResults: int = ...,
        Status: ModelStatusType = ...,
        ModelNameBeginsWith: str = ...,
        DatasetNameBeginsWith: str = ...,
    ) -> ListModelsResponseTypeDef:
        """
        Generates a list of all models in the account, including model name and ARN,
        dataset, and
        status.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutequipment.html#LookoutEquipment.Client.list_models)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lookoutequipment/client/#list_models)
        """

    async def list_retraining_schedulers(
        self,
        *,
        ModelNameBeginsWith: str = ...,
        Status: RetrainingSchedulerStatusType = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
    ) -> ListRetrainingSchedulersResponseTypeDef:
        """
        Lists all retraining schedulers in your account, filtering by model name prefix
        and
        status.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutequipment.html#LookoutEquipment.Client.list_retraining_schedulers)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lookoutequipment/client/#list_retraining_schedulers)
        """

    async def list_sensor_statistics(
        self,
        *,
        DatasetName: str,
        IngestionJobId: str = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
    ) -> ListSensorStatisticsResponseTypeDef:
        """
        Lists statistics about the data collected for each of the sensors that have
        been successfully ingested in the particular
        dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutequipment.html#LookoutEquipment.Client.list_sensor_statistics)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lookoutequipment/client/#list_sensor_statistics)
        """

    async def list_tags_for_resource(
        self, *, ResourceArn: str
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists all the tags for a specified resource, including key and value.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutequipment.html#LookoutEquipment.Client.list_tags_for_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lookoutequipment/client/#list_tags_for_resource)
        """

    async def put_resource_policy(
        self,
        *,
        ResourceArn: str,
        ResourcePolicy: str,
        ClientToken: str,
        PolicyRevisionId: str = ...,
    ) -> PutResourcePolicyResponseTypeDef:
        """
        Creates a resource control policy for a given resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutequipment.html#LookoutEquipment.Client.put_resource_policy)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lookoutequipment/client/#put_resource_policy)
        """

    async def start_data_ingestion_job(
        self,
        *,
        DatasetName: str,
        IngestionInputConfiguration: IngestionInputConfigurationTypeDef,
        RoleArn: str,
        ClientToken: str,
    ) -> StartDataIngestionJobResponseTypeDef:
        """
        Starts a data ingestion job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutequipment.html#LookoutEquipment.Client.start_data_ingestion_job)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lookoutequipment/client/#start_data_ingestion_job)
        """

    async def start_inference_scheduler(
        self, *, InferenceSchedulerName: str
    ) -> StartInferenceSchedulerResponseTypeDef:
        """
        Starts an inference scheduler.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutequipment.html#LookoutEquipment.Client.start_inference_scheduler)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lookoutequipment/client/#start_inference_scheduler)
        """

    async def start_retraining_scheduler(
        self, *, ModelName: str
    ) -> StartRetrainingSchedulerResponseTypeDef:
        """
        Starts a retraining scheduler.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutequipment.html#LookoutEquipment.Client.start_retraining_scheduler)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lookoutequipment/client/#start_retraining_scheduler)
        """

    async def stop_inference_scheduler(
        self, *, InferenceSchedulerName: str
    ) -> StopInferenceSchedulerResponseTypeDef:
        """
        Stops an inference scheduler.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutequipment.html#LookoutEquipment.Client.stop_inference_scheduler)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lookoutequipment/client/#stop_inference_scheduler)
        """

    async def stop_retraining_scheduler(
        self, *, ModelName: str
    ) -> StopRetrainingSchedulerResponseTypeDef:
        """
        Stops a retraining scheduler.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutequipment.html#LookoutEquipment.Client.stop_retraining_scheduler)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lookoutequipment/client/#stop_retraining_scheduler)
        """

    async def tag_resource(self, *, ResourceArn: str, Tags: Sequence[TagTypeDef]) -> Dict[str, Any]:
        """
        Associates a given tag to a resource in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutequipment.html#LookoutEquipment.Client.tag_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lookoutequipment/client/#tag_resource)
        """

    async def untag_resource(self, *, ResourceArn: str, TagKeys: Sequence[str]) -> Dict[str, Any]:
        """
        Removes a specific tag from a given resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutequipment.html#LookoutEquipment.Client.untag_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lookoutequipment/client/#untag_resource)
        """

    async def update_active_model_version(
        self, *, ModelName: str, ModelVersion: int
    ) -> UpdateActiveModelVersionResponseTypeDef:
        """
        Sets the active model version for a given machine learning model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutequipment.html#LookoutEquipment.Client.update_active_model_version)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lookoutequipment/client/#update_active_model_version)
        """

    async def update_inference_scheduler(
        self,
        *,
        InferenceSchedulerName: str,
        DataDelayOffsetInMinutes: int = ...,
        DataUploadFrequency: DataUploadFrequencyType = ...,
        DataInputConfiguration: InferenceInputConfigurationTypeDef = ...,
        DataOutputConfiguration: InferenceOutputConfigurationTypeDef = ...,
        RoleArn: str = ...,
    ) -> EmptyResponseMetadataTypeDef:
        """
        Updates an inference scheduler.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutequipment.html#LookoutEquipment.Client.update_inference_scheduler)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lookoutequipment/client/#update_inference_scheduler)
        """

    async def update_label_group(
        self, *, LabelGroupName: str, FaultCodes: Sequence[str] = ...
    ) -> EmptyResponseMetadataTypeDef:
        """
        Updates the label group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutequipment.html#LookoutEquipment.Client.update_label_group)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lookoutequipment/client/#update_label_group)
        """

    async def update_model(
        self,
        *,
        ModelName: str,
        LabelsInputConfiguration: LabelsInputConfigurationTypeDef = ...,
        RoleArn: str = ...,
    ) -> EmptyResponseMetadataTypeDef:
        """
        Updates a model in the account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutequipment.html#LookoutEquipment.Client.update_model)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lookoutequipment/client/#update_model)
        """

    async def update_retraining_scheduler(
        self,
        *,
        ModelName: str,
        RetrainingStartDate: TimestampTypeDef = ...,
        RetrainingFrequency: str = ...,
        LookbackWindow: str = ...,
        PromoteMode: ModelPromoteModeType = ...,
    ) -> EmptyResponseMetadataTypeDef:
        """
        Updates a retraining scheduler.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutequipment.html#LookoutEquipment.Client.update_retraining_scheduler)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lookoutequipment/client/#update_retraining_scheduler)
        """

    async def __aenter__(self) -> "LookoutEquipmentClient":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutequipment.html#LookoutEquipment.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lookoutequipment/client/)
        """

    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> Any:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutequipment.html#LookoutEquipment.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lookoutequipment/client/)
        """
