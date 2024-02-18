"""
Type annotations for forecast service client.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/client/)

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_forecast.client import ForecastServiceClient

    session = get_session()
    async with session.create_client("forecast") as client:
        client: ForecastServiceClient
    ```
"""

import sys
from typing import Any, Dict, Mapping, Sequence, Type, overload

from aiobotocore.client import AioBaseClient
from botocore.client import ClientMeta

from .literals import (
    AutoMLOverrideStrategyType,
    DatasetTypeType,
    DomainType,
    ImportModeType,
    OptimizationMetricType,
)
from .paginator import (
    ListDatasetGroupsPaginator,
    ListDatasetImportJobsPaginator,
    ListDatasetsPaginator,
    ListExplainabilitiesPaginator,
    ListExplainabilityExportsPaginator,
    ListForecastExportJobsPaginator,
    ListForecastsPaginator,
    ListMonitorEvaluationsPaginator,
    ListMonitorsPaginator,
    ListPredictorBacktestExportJobsPaginator,
    ListPredictorsPaginator,
    ListWhatIfAnalysesPaginator,
    ListWhatIfForecastExportsPaginator,
    ListWhatIfForecastsPaginator,
)
from .type_defs import (
    CreateAutoPredictorResponseTypeDef,
    CreateDatasetGroupResponseTypeDef,
    CreateDatasetImportJobResponseTypeDef,
    CreateDatasetResponseTypeDef,
    CreateExplainabilityExportResponseTypeDef,
    CreateExplainabilityResponseTypeDef,
    CreateForecastExportJobResponseTypeDef,
    CreateForecastResponseTypeDef,
    CreateMonitorResponseTypeDef,
    CreatePredictorBacktestExportJobResponseTypeDef,
    CreatePredictorResponseTypeDef,
    CreateWhatIfAnalysisResponseTypeDef,
    CreateWhatIfForecastExportResponseTypeDef,
    CreateWhatIfForecastResponseTypeDef,
    DataConfigTypeDef,
    DataDestinationTypeDef,
    DataSourceTypeDef,
    DescribeAutoPredictorResponseTypeDef,
    DescribeDatasetGroupResponseTypeDef,
    DescribeDatasetImportJobResponseTypeDef,
    DescribeDatasetResponseTypeDef,
    DescribeExplainabilityExportResponseTypeDef,
    DescribeExplainabilityResponseTypeDef,
    DescribeForecastExportJobResponseTypeDef,
    DescribeForecastResponseTypeDef,
    DescribeMonitorResponseTypeDef,
    DescribePredictorBacktestExportJobResponseTypeDef,
    DescribePredictorResponseTypeDef,
    DescribeWhatIfAnalysisResponseTypeDef,
    DescribeWhatIfForecastExportResponseTypeDef,
    DescribeWhatIfForecastResponseTypeDef,
    EmptyResponseMetadataTypeDef,
    EncryptionConfigTypeDef,
    EvaluationParametersTypeDef,
    ExplainabilityConfigTypeDef,
    FeaturizationConfigTypeDef,
    FilterTypeDef,
    GetAccuracyMetricsResponseTypeDef,
    HyperParameterTuningJobConfigTypeDef,
    InputDataConfigTypeDef,
    ListDatasetGroupsResponseTypeDef,
    ListDatasetImportJobsResponseTypeDef,
    ListDatasetsResponseTypeDef,
    ListExplainabilitiesResponseTypeDef,
    ListExplainabilityExportsResponseTypeDef,
    ListForecastExportJobsResponseTypeDef,
    ListForecastsResponseTypeDef,
    ListMonitorEvaluationsResponseTypeDef,
    ListMonitorsResponseTypeDef,
    ListPredictorBacktestExportJobsResponseTypeDef,
    ListPredictorsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListWhatIfAnalysesResponseTypeDef,
    ListWhatIfForecastExportsResponseTypeDef,
    ListWhatIfForecastsResponseTypeDef,
    MonitorConfigTypeDef,
    SchemaTypeDef,
    TagTypeDef,
    TimeAlignmentBoundaryTypeDef,
    TimeSeriesReplacementsDataSourceTypeDef,
    TimeSeriesSelectorTypeDef,
    TimeSeriesTransformationTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("ForecastServiceClient",)

class BotocoreClientError(Exception):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    ClientError: Type[BotocoreClientError]
    InvalidInputException: Type[BotocoreClientError]
    InvalidNextTokenException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ResourceAlreadyExistsException: Type[BotocoreClientError]
    ResourceInUseException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]

class ForecastServiceClient(AioBaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        ForecastServiceClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.exceptions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.can_paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/client/#can_paginate)
        """

    async def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.close)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/client/#close)
        """

    async def create_auto_predictor(
        self,
        *,
        PredictorName: str,
        ForecastHorizon: int = ...,
        ForecastTypes: Sequence[str] = ...,
        ForecastDimensions: Sequence[str] = ...,
        ForecastFrequency: str = ...,
        DataConfig: DataConfigTypeDef = ...,
        EncryptionConfig: EncryptionConfigTypeDef = ...,
        ReferencePredictorArn: str = ...,
        OptimizationMetric: OptimizationMetricType = ...,
        ExplainPredictor: bool = ...,
        Tags: Sequence[TagTypeDef] = ...,
        MonitorConfig: MonitorConfigTypeDef = ...,
        TimeAlignmentBoundary: TimeAlignmentBoundaryTypeDef = ...,
    ) -> CreateAutoPredictorResponseTypeDef:
        """
        Creates an Amazon Forecast predictor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.create_auto_predictor)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/client/#create_auto_predictor)
        """

    async def create_dataset(
        self,
        *,
        DatasetName: str,
        Domain: DomainType,
        DatasetType: DatasetTypeType,
        Schema: SchemaTypeDef,
        DataFrequency: str = ...,
        EncryptionConfig: EncryptionConfigTypeDef = ...,
        Tags: Sequence[TagTypeDef] = ...,
    ) -> CreateDatasetResponseTypeDef:
        """
        Creates an Amazon Forecast dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.create_dataset)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/client/#create_dataset)
        """

    async def create_dataset_group(
        self,
        *,
        DatasetGroupName: str,
        Domain: DomainType,
        DatasetArns: Sequence[str] = ...,
        Tags: Sequence[TagTypeDef] = ...,
    ) -> CreateDatasetGroupResponseTypeDef:
        """
        Creates a dataset group, which holds a collection of related datasets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.create_dataset_group)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/client/#create_dataset_group)
        """

    async def create_dataset_import_job(
        self,
        *,
        DatasetImportJobName: str,
        DatasetArn: str,
        DataSource: DataSourceTypeDef,
        TimestampFormat: str = ...,
        TimeZone: str = ...,
        UseGeolocationForTimeZone: bool = ...,
        GeolocationFormat: str = ...,
        Tags: Sequence[TagTypeDef] = ...,
        Format: str = ...,
        ImportMode: ImportModeType = ...,
    ) -> CreateDatasetImportJobResponseTypeDef:
        """
        Imports your training data to an Amazon Forecast dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.create_dataset_import_job)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/client/#create_dataset_import_job)
        """

    async def create_explainability(
        self,
        *,
        ExplainabilityName: str,
        ResourceArn: str,
        ExplainabilityConfig: ExplainabilityConfigTypeDef,
        DataSource: DataSourceTypeDef = ...,
        Schema: SchemaTypeDef = ...,
        EnableVisualization: bool = ...,
        StartDateTime: str = ...,
        EndDateTime: str = ...,
        Tags: Sequence[TagTypeDef] = ...,
    ) -> CreateExplainabilityResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.create_explainability)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/client/#create_explainability)
        """

    async def create_explainability_export(
        self,
        *,
        ExplainabilityExportName: str,
        ExplainabilityArn: str,
        Destination: DataDestinationTypeDef,
        Tags: Sequence[TagTypeDef] = ...,
        Format: str = ...,
    ) -> CreateExplainabilityExportResponseTypeDef:
        """
        Exports an Explainability resource created by the  CreateExplainability
        operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.create_explainability_export)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/client/#create_explainability_export)
        """

    async def create_forecast(
        self,
        *,
        ForecastName: str,
        PredictorArn: str,
        ForecastTypes: Sequence[str] = ...,
        Tags: Sequence[TagTypeDef] = ...,
        TimeSeriesSelector: TimeSeriesSelectorTypeDef = ...,
    ) -> CreateForecastResponseTypeDef:
        """
        Creates a forecast for each item in the `TARGET_TIME_SERIES` dataset that was
        used to train the
        predictor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.create_forecast)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/client/#create_forecast)
        """

    async def create_forecast_export_job(
        self,
        *,
        ForecastExportJobName: str,
        ForecastArn: str,
        Destination: DataDestinationTypeDef,
        Tags: Sequence[TagTypeDef] = ...,
        Format: str = ...,
    ) -> CreateForecastExportJobResponseTypeDef:
        """
        Exports a forecast created by the  CreateForecast operation to your Amazon
        Simple Storage Service (Amazon S3)
        bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.create_forecast_export_job)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/client/#create_forecast_export_job)
        """

    async def create_monitor(
        self, *, MonitorName: str, ResourceArn: str, Tags: Sequence[TagTypeDef] = ...
    ) -> CreateMonitorResponseTypeDef:
        """
        Creates a predictor monitor resource for an existing auto predictor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.create_monitor)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/client/#create_monitor)
        """

    async def create_predictor(
        self,
        *,
        PredictorName: str,
        ForecastHorizon: int,
        InputDataConfig: InputDataConfigTypeDef,
        FeaturizationConfig: FeaturizationConfigTypeDef,
        AlgorithmArn: str = ...,
        ForecastTypes: Sequence[str] = ...,
        PerformAutoML: bool = ...,
        AutoMLOverrideStrategy: AutoMLOverrideStrategyType = ...,
        PerformHPO: bool = ...,
        TrainingParameters: Mapping[str, str] = ...,
        EvaluationParameters: EvaluationParametersTypeDef = ...,
        HPOConfig: HyperParameterTuningJobConfigTypeDef = ...,
        EncryptionConfig: EncryptionConfigTypeDef = ...,
        Tags: Sequence[TagTypeDef] = ...,
        OptimizationMetric: OptimizationMetricType = ...,
    ) -> CreatePredictorResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.create_predictor)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/client/#create_predictor)
        """

    async def create_predictor_backtest_export_job(
        self,
        *,
        PredictorBacktestExportJobName: str,
        PredictorArn: str,
        Destination: DataDestinationTypeDef,
        Tags: Sequence[TagTypeDef] = ...,
        Format: str = ...,
    ) -> CreatePredictorBacktestExportJobResponseTypeDef:
        """
        Exports backtest forecasts and accuracy metrics generated by the
        CreateAutoPredictor or  CreatePredictor
        operations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.create_predictor_backtest_export_job)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/client/#create_predictor_backtest_export_job)
        """

    async def create_what_if_analysis(
        self,
        *,
        WhatIfAnalysisName: str,
        ForecastArn: str,
        TimeSeriesSelector: TimeSeriesSelectorTypeDef = ...,
        Tags: Sequence[TagTypeDef] = ...,
    ) -> CreateWhatIfAnalysisResponseTypeDef:
        """
        What-if analysis is a scenario modeling technique where you make a hypothetical
        change to a time series and compare the forecasts generated by these changes
        against the baseline, unchanged time
        series.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.create_what_if_analysis)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/client/#create_what_if_analysis)
        """

    async def create_what_if_forecast(
        self,
        *,
        WhatIfForecastName: str,
        WhatIfAnalysisArn: str,
        TimeSeriesTransformations: Sequence[TimeSeriesTransformationTypeDef] = ...,
        TimeSeriesReplacementsDataSource: TimeSeriesReplacementsDataSourceTypeDef = ...,
        Tags: Sequence[TagTypeDef] = ...,
    ) -> CreateWhatIfForecastResponseTypeDef:
        """
        A what-if forecast is a forecast that is created from a modified version of the
        baseline
        forecast.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.create_what_if_forecast)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/client/#create_what_if_forecast)
        """

    async def create_what_if_forecast_export(
        self,
        *,
        WhatIfForecastExportName: str,
        WhatIfForecastArns: Sequence[str],
        Destination: DataDestinationTypeDef,
        Tags: Sequence[TagTypeDef] = ...,
        Format: str = ...,
    ) -> CreateWhatIfForecastExportResponseTypeDef:
        """
        Exports a forecast created by the  CreateWhatIfForecast operation to your
        Amazon Simple Storage Service (Amazon S3)
        bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.create_what_if_forecast_export)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/client/#create_what_if_forecast_export)
        """

    async def delete_dataset(self, *, DatasetArn: str) -> EmptyResponseMetadataTypeDef:
        """
        Deletes an Amazon Forecast dataset that was created using the
        [CreateDataset](https://docs.aws.amazon.com/forecast/latest/dg/API_CreateDataset.html)
        operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.delete_dataset)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/client/#delete_dataset)
        """

    async def delete_dataset_group(self, *, DatasetGroupArn: str) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a dataset group created using the
        [CreateDatasetGroup](https://docs.aws.amazon.com/forecast/latest/dg/API_CreateDatasetGroup.html)
        operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.delete_dataset_group)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/client/#delete_dataset_group)
        """

    async def delete_dataset_import_job(
        self, *, DatasetImportJobArn: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a dataset import job created using the
        [CreateDatasetImportJob](https://docs.aws.amazon.com/forecast/latest/dg/API_CreateDatasetImportJob.html)
        operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.delete_dataset_import_job)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/client/#delete_dataset_import_job)
        """

    async def delete_explainability(
        self, *, ExplainabilityArn: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes an Explainability resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.delete_explainability)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/client/#delete_explainability)
        """

    async def delete_explainability_export(
        self, *, ExplainabilityExportArn: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes an Explainability export.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.delete_explainability_export)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/client/#delete_explainability_export)
        """

    async def delete_forecast(self, *, ForecastArn: str) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a forecast created using the  CreateForecast operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.delete_forecast)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/client/#delete_forecast)
        """

    async def delete_forecast_export_job(
        self, *, ForecastExportJobArn: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a forecast export job created using the  CreateForecastExportJob
        operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.delete_forecast_export_job)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/client/#delete_forecast_export_job)
        """

    async def delete_monitor(self, *, MonitorArn: str) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a monitor resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.delete_monitor)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/client/#delete_monitor)
        """

    async def delete_predictor(self, *, PredictorArn: str) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a predictor created using the  DescribePredictor or  CreatePredictor
        operations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.delete_predictor)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/client/#delete_predictor)
        """

    async def delete_predictor_backtest_export_job(
        self, *, PredictorBacktestExportJobArn: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a predictor backtest export job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.delete_predictor_backtest_export_job)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/client/#delete_predictor_backtest_export_job)
        """

    async def delete_resource_tree(self, *, ResourceArn: str) -> EmptyResponseMetadataTypeDef:
        """
        Deletes an entire resource tree.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.delete_resource_tree)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/client/#delete_resource_tree)
        """

    async def delete_what_if_analysis(
        self, *, WhatIfAnalysisArn: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a what-if analysis created using the  CreateWhatIfAnalysis operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.delete_what_if_analysis)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/client/#delete_what_if_analysis)
        """

    async def delete_what_if_forecast(
        self, *, WhatIfForecastArn: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a what-if forecast created using the  CreateWhatIfForecast operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.delete_what_if_forecast)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/client/#delete_what_if_forecast)
        """

    async def delete_what_if_forecast_export(
        self, *, WhatIfForecastExportArn: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a what-if forecast export created using the  CreateWhatIfForecastExport
        operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.delete_what_if_forecast_export)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/client/#delete_what_if_forecast_export)
        """

    async def describe_auto_predictor(
        self, *, PredictorArn: str
    ) -> DescribeAutoPredictorResponseTypeDef:
        """
        Describes a predictor created using the CreateAutoPredictor operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.describe_auto_predictor)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/client/#describe_auto_predictor)
        """

    async def describe_dataset(self, *, DatasetArn: str) -> DescribeDatasetResponseTypeDef:
        """
        Describes an Amazon Forecast dataset created using the
        [CreateDataset](https://docs.aws.amazon.com/forecast/latest/dg/API_CreateDataset.html)
        operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.describe_dataset)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/client/#describe_dataset)
        """

    async def describe_dataset_group(
        self, *, DatasetGroupArn: str
    ) -> DescribeDatasetGroupResponseTypeDef:
        """
        Describes a dataset group created using the
        [CreateDatasetGroup](https://docs.aws.amazon.com/forecast/latest/dg/API_CreateDatasetGroup.html)
        operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.describe_dataset_group)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/client/#describe_dataset_group)
        """

    async def describe_dataset_import_job(
        self, *, DatasetImportJobArn: str
    ) -> DescribeDatasetImportJobResponseTypeDef:
        """
        Describes a dataset import job created using the
        [CreateDatasetImportJob](https://docs.aws.amazon.com/forecast/latest/dg/API_CreateDatasetImportJob.html)
        operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.describe_dataset_import_job)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/client/#describe_dataset_import_job)
        """

    async def describe_explainability(
        self, *, ExplainabilityArn: str
    ) -> DescribeExplainabilityResponseTypeDef:
        """
        Describes an Explainability resource created using the  CreateExplainability
        operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.describe_explainability)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/client/#describe_explainability)
        """

    async def describe_explainability_export(
        self, *, ExplainabilityExportArn: str
    ) -> DescribeExplainabilityExportResponseTypeDef:
        """
        Describes an Explainability export created using the
        CreateExplainabilityExport
        operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.describe_explainability_export)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/client/#describe_explainability_export)
        """

    async def describe_forecast(self, *, ForecastArn: str) -> DescribeForecastResponseTypeDef:
        """
        Describes a forecast created using the  CreateForecast operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.describe_forecast)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/client/#describe_forecast)
        """

    async def describe_forecast_export_job(
        self, *, ForecastExportJobArn: str
    ) -> DescribeForecastExportJobResponseTypeDef:
        """
        Describes a forecast export job created using the  CreateForecastExportJob
        operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.describe_forecast_export_job)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/client/#describe_forecast_export_job)
        """

    async def describe_monitor(self, *, MonitorArn: str) -> DescribeMonitorResponseTypeDef:
        """
        Describes a monitor resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.describe_monitor)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/client/#describe_monitor)
        """

    async def describe_predictor(self, *, PredictorArn: str) -> DescribePredictorResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.describe_predictor)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/client/#describe_predictor)
        """

    async def describe_predictor_backtest_export_job(
        self, *, PredictorBacktestExportJobArn: str
    ) -> DescribePredictorBacktestExportJobResponseTypeDef:
        """
        Describes a predictor backtest export job created using the
        CreatePredictorBacktestExportJob
        operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.describe_predictor_backtest_export_job)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/client/#describe_predictor_backtest_export_job)
        """

    async def describe_what_if_analysis(
        self, *, WhatIfAnalysisArn: str
    ) -> DescribeWhatIfAnalysisResponseTypeDef:
        """
        Describes the what-if analysis created using the  CreateWhatIfAnalysis
        operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.describe_what_if_analysis)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/client/#describe_what_if_analysis)
        """

    async def describe_what_if_forecast(
        self, *, WhatIfForecastArn: str
    ) -> DescribeWhatIfForecastResponseTypeDef:
        """
        Describes the what-if forecast created using the  CreateWhatIfForecast
        operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.describe_what_if_forecast)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/client/#describe_what_if_forecast)
        """

    async def describe_what_if_forecast_export(
        self, *, WhatIfForecastExportArn: str
    ) -> DescribeWhatIfForecastExportResponseTypeDef:
        """
        Describes the what-if forecast export created using the
        CreateWhatIfForecastExport
        operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.describe_what_if_forecast_export)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/client/#describe_what_if_forecast_export)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.generate_presigned_url)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/client/#generate_presigned_url)
        """

    async def get_accuracy_metrics(self, *, PredictorArn: str) -> GetAccuracyMetricsResponseTypeDef:
        """
        Provides metrics on the accuracy of the models that were trained by the
        CreatePredictor
        operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.get_accuracy_metrics)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/client/#get_accuracy_metrics)
        """

    async def list_dataset_groups(
        self, *, NextToken: str = ..., MaxResults: int = ...
    ) -> ListDatasetGroupsResponseTypeDef:
        """
        Returns a list of dataset groups created using the
        [CreateDatasetGroup](https://docs.aws.amazon.com/forecast/latest/dg/API_CreateDatasetGroup.html)
        operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.list_dataset_groups)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/client/#list_dataset_groups)
        """

    async def list_dataset_import_jobs(
        self, *, NextToken: str = ..., MaxResults: int = ..., Filters: Sequence[FilterTypeDef] = ...
    ) -> ListDatasetImportJobsResponseTypeDef:
        """
        Returns a list of dataset import jobs created using the
        [CreateDatasetImportJob](https://docs.aws.amazon.com/forecast/latest/dg/API_CreateDatasetImportJob.html)
        operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.list_dataset_import_jobs)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/client/#list_dataset_import_jobs)
        """

    async def list_datasets(
        self, *, NextToken: str = ..., MaxResults: int = ...
    ) -> ListDatasetsResponseTypeDef:
        """
        Returns a list of datasets created using the
        [CreateDataset](https://docs.aws.amazon.com/forecast/latest/dg/API_CreateDataset.html)
        operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.list_datasets)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/client/#list_datasets)
        """

    async def list_explainabilities(
        self, *, NextToken: str = ..., MaxResults: int = ..., Filters: Sequence[FilterTypeDef] = ...
    ) -> ListExplainabilitiesResponseTypeDef:
        """
        Returns a list of Explainability resources created using the
        CreateExplainability
        operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.list_explainabilities)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/client/#list_explainabilities)
        """

    async def list_explainability_exports(
        self, *, NextToken: str = ..., MaxResults: int = ..., Filters: Sequence[FilterTypeDef] = ...
    ) -> ListExplainabilityExportsResponseTypeDef:
        """
        Returns a list of Explainability exports created using the
        CreateExplainabilityExport
        operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.list_explainability_exports)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/client/#list_explainability_exports)
        """

    async def list_forecast_export_jobs(
        self, *, NextToken: str = ..., MaxResults: int = ..., Filters: Sequence[FilterTypeDef] = ...
    ) -> ListForecastExportJobsResponseTypeDef:
        """
        Returns a list of forecast export jobs created using the
        CreateForecastExportJob
        operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.list_forecast_export_jobs)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/client/#list_forecast_export_jobs)
        """

    async def list_forecasts(
        self, *, NextToken: str = ..., MaxResults: int = ..., Filters: Sequence[FilterTypeDef] = ...
    ) -> ListForecastsResponseTypeDef:
        """
        Returns a list of forecasts created using the  CreateForecast operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.list_forecasts)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/client/#list_forecasts)
        """

    async def list_monitor_evaluations(
        self,
        *,
        MonitorArn: str,
        NextToken: str = ...,
        MaxResults: int = ...,
        Filters: Sequence[FilterTypeDef] = ...,
    ) -> ListMonitorEvaluationsResponseTypeDef:
        """
        Returns a list of the monitoring evaluation results and predictor events
        collected by the monitor resource during different windows of
        time.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.list_monitor_evaluations)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/client/#list_monitor_evaluations)
        """

    async def list_monitors(
        self, *, NextToken: str = ..., MaxResults: int = ..., Filters: Sequence[FilterTypeDef] = ...
    ) -> ListMonitorsResponseTypeDef:
        """
        Returns a list of monitors created with the  CreateMonitor operation and
        CreateAutoPredictor
        operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.list_monitors)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/client/#list_monitors)
        """

    async def list_predictor_backtest_export_jobs(
        self, *, NextToken: str = ..., MaxResults: int = ..., Filters: Sequence[FilterTypeDef] = ...
    ) -> ListPredictorBacktestExportJobsResponseTypeDef:
        """
        Returns a list of predictor backtest export jobs created using the
        CreatePredictorBacktestExportJob
        operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.list_predictor_backtest_export_jobs)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/client/#list_predictor_backtest_export_jobs)
        """

    async def list_predictors(
        self, *, NextToken: str = ..., MaxResults: int = ..., Filters: Sequence[FilterTypeDef] = ...
    ) -> ListPredictorsResponseTypeDef:
        """
        Returns a list of predictors created using the  CreateAutoPredictor or
        CreatePredictor
        operations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.list_predictors)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/client/#list_predictors)
        """

    async def list_tags_for_resource(
        self, *, ResourceArn: str
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists the tags for an Amazon Forecast resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.list_tags_for_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/client/#list_tags_for_resource)
        """

    async def list_what_if_analyses(
        self, *, NextToken: str = ..., MaxResults: int = ..., Filters: Sequence[FilterTypeDef] = ...
    ) -> ListWhatIfAnalysesResponseTypeDef:
        """
        Returns a list of what-if analyses created using the  CreateWhatIfAnalysis
        operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.list_what_if_analyses)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/client/#list_what_if_analyses)
        """

    async def list_what_if_forecast_exports(
        self, *, NextToken: str = ..., MaxResults: int = ..., Filters: Sequence[FilterTypeDef] = ...
    ) -> ListWhatIfForecastExportsResponseTypeDef:
        """
        Returns a list of what-if forecast exports created using the
        CreateWhatIfForecastExport
        operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.list_what_if_forecast_exports)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/client/#list_what_if_forecast_exports)
        """

    async def list_what_if_forecasts(
        self, *, NextToken: str = ..., MaxResults: int = ..., Filters: Sequence[FilterTypeDef] = ...
    ) -> ListWhatIfForecastsResponseTypeDef:
        """
        Returns a list of what-if forecasts created using the  CreateWhatIfForecast
        operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.list_what_if_forecasts)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/client/#list_what_if_forecasts)
        """

    async def resume_resource(self, *, ResourceArn: str) -> EmptyResponseMetadataTypeDef:
        """
        Resumes a stopped monitor resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.resume_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/client/#resume_resource)
        """

    async def stop_resource(self, *, ResourceArn: str) -> EmptyResponseMetadataTypeDef:
        """
        Stops a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.stop_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/client/#stop_resource)
        """

    async def tag_resource(self, *, ResourceArn: str, Tags: Sequence[TagTypeDef]) -> Dict[str, Any]:
        """
        Associates the specified tags to a resource with the specified `resourceArn`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.tag_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/client/#tag_resource)
        """

    async def untag_resource(self, *, ResourceArn: str, TagKeys: Sequence[str]) -> Dict[str, Any]:
        """
        Deletes the specified tags from a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.untag_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/client/#untag_resource)
        """

    async def update_dataset_group(
        self, *, DatasetGroupArn: str, DatasetArns: Sequence[str]
    ) -> Dict[str, Any]:
        """
        Replaces the datasets in a dataset group with the specified datasets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.update_dataset_group)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/client/#update_dataset_group)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_dataset_groups"]
    ) -> ListDatasetGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_dataset_import_jobs"]
    ) -> ListDatasetImportJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_datasets"]) -> ListDatasetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_explainabilities"]
    ) -> ListExplainabilitiesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_explainability_exports"]
    ) -> ListExplainabilityExportsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_forecast_export_jobs"]
    ) -> ListForecastExportJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_forecasts"]) -> ListForecastsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_monitor_evaluations"]
    ) -> ListMonitorEvaluationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_monitors"]) -> ListMonitorsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_predictor_backtest_export_jobs"]
    ) -> ListPredictorBacktestExportJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_predictors"]) -> ListPredictorsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_what_if_analyses"]
    ) -> ListWhatIfAnalysesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_what_if_forecast_exports"]
    ) -> ListWhatIfForecastExportsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_what_if_forecasts"]
    ) -> ListWhatIfForecastsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/client/#get_paginator)
        """

    async def __aenter__(self) -> "ForecastServiceClient":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/client/)
        """

    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> Any:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/client/)
        """
