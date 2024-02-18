"""
Type annotations for forecast service type definitions.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/type_defs/)

Usage::

    ```python
    from types_aiobotocore_forecast.type_defs import ActionTypeDef

    data: ActionTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from .literals import (
    AttributeTypeType,
    AutoMLOverrideStrategyType,
    ConditionType,
    DatasetTypeType,
    DayOfWeekType,
    DomainType,
    EvaluationTypeType,
    FilterConditionStringType,
    ImportModeType,
    MonthType,
    OperationType,
    OptimizationMetricType,
    ScalingTypeType,
    StateType,
    TimePointGranularityType,
    TimeSeriesGranularityType,
)

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 12):
    from typing import NotRequired
else:
    from typing_extensions import NotRequired
if sys.version_info >= (3, 12):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "ActionTypeDef",
    "AdditionalDatasetTypeDef",
    "AttributeConfigTypeDef",
    "BaselineMetricTypeDef",
    "CategoricalParameterRangeTypeDef",
    "ContinuousParameterRangeTypeDef",
    "EncryptionConfigTypeDef",
    "MonitorConfigTypeDef",
    "TagTypeDef",
    "TimeAlignmentBoundaryTypeDef",
    "ResponseMetadataTypeDef",
    "ExplainabilityConfigTypeDef",
    "EvaluationParametersTypeDef",
    "S3ConfigTypeDef",
    "DatasetGroupSummaryTypeDef",
    "DatasetSummaryTypeDef",
    "DeleteDatasetGroupRequestRequestTypeDef",
    "DeleteDatasetImportJobRequestRequestTypeDef",
    "DeleteDatasetRequestRequestTypeDef",
    "DeleteExplainabilityExportRequestRequestTypeDef",
    "DeleteExplainabilityRequestRequestTypeDef",
    "DeleteForecastExportJobRequestRequestTypeDef",
    "DeleteForecastRequestRequestTypeDef",
    "DeleteMonitorRequestRequestTypeDef",
    "DeletePredictorBacktestExportJobRequestRequestTypeDef",
    "DeletePredictorRequestRequestTypeDef",
    "DeleteResourceTreeRequestRequestTypeDef",
    "DeleteWhatIfAnalysisRequestRequestTypeDef",
    "DeleteWhatIfForecastExportRequestRequestTypeDef",
    "DeleteWhatIfForecastRequestRequestTypeDef",
    "DescribeAutoPredictorRequestRequestTypeDef",
    "ExplainabilityInfoTypeDef",
    "MonitorInfoTypeDef",
    "ReferencePredictorSummaryTypeDef",
    "DescribeDatasetGroupRequestRequestTypeDef",
    "DescribeDatasetImportJobRequestRequestTypeDef",
    "StatisticsTypeDef",
    "DescribeDatasetRequestRequestTypeDef",
    "DescribeExplainabilityExportRequestRequestTypeDef",
    "DescribeExplainabilityRequestRequestTypeDef",
    "DescribeForecastExportJobRequestRequestTypeDef",
    "DescribeForecastRequestRequestTypeDef",
    "DescribeMonitorRequestRequestTypeDef",
    "DescribePredictorBacktestExportJobRequestRequestTypeDef",
    "DescribePredictorRequestRequestTypeDef",
    "DescribeWhatIfAnalysisRequestRequestTypeDef",
    "DescribeWhatIfForecastExportRequestRequestTypeDef",
    "DescribeWhatIfForecastRequestRequestTypeDef",
    "ErrorMetricTypeDef",
    "FeaturizationMethodTypeDef",
    "FilterTypeDef",
    "ForecastSummaryTypeDef",
    "GetAccuracyMetricsRequestRequestTypeDef",
    "SupplementaryFeatureTypeDef",
    "IntegerParameterRangeTypeDef",
    "PaginatorConfigTypeDef",
    "ListDatasetGroupsRequestRequestTypeDef",
    "ListDatasetsRequestRequestTypeDef",
    "MonitorSummaryTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "WhatIfAnalysisSummaryTypeDef",
    "WhatIfForecastSummaryTypeDef",
    "MetricResultTypeDef",
    "WeightedQuantileLossTypeDef",
    "MonitorDataSourceTypeDef",
    "PredictorEventTypeDef",
    "TestWindowSummaryTypeDef",
    "ResumeResourceRequestRequestTypeDef",
    "SchemaAttributeTypeDef",
    "StopResourceRequestRequestTypeDef",
    "TimeSeriesConditionTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateDatasetGroupRequestRequestTypeDef",
    "DataConfigTypeDef",
    "PredictorBaselineTypeDef",
    "CreateDatasetGroupRequestRequestTypeDef",
    "CreateMonitorRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "CreateAutoPredictorResponseTypeDef",
    "CreateDatasetGroupResponseTypeDef",
    "CreateDatasetImportJobResponseTypeDef",
    "CreateDatasetResponseTypeDef",
    "CreateExplainabilityExportResponseTypeDef",
    "CreateExplainabilityResponseTypeDef",
    "CreateForecastExportJobResponseTypeDef",
    "CreateForecastResponseTypeDef",
    "CreateMonitorResponseTypeDef",
    "CreatePredictorBacktestExportJobResponseTypeDef",
    "CreatePredictorResponseTypeDef",
    "CreateWhatIfAnalysisResponseTypeDef",
    "CreateWhatIfForecastExportResponseTypeDef",
    "CreateWhatIfForecastResponseTypeDef",
    "DescribeDatasetGroupResponseTypeDef",
    "EmptyResponseMetadataTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ExplainabilitySummaryTypeDef",
    "DataDestinationTypeDef",
    "DataSourceTypeDef",
    "ListDatasetGroupsResponseTypeDef",
    "ListDatasetsResponseTypeDef",
    "PredictorSummaryTypeDef",
    "FeaturizationTypeDef",
    "ListDatasetImportJobsRequestRequestTypeDef",
    "ListExplainabilitiesRequestRequestTypeDef",
    "ListExplainabilityExportsRequestRequestTypeDef",
    "ListForecastExportJobsRequestRequestTypeDef",
    "ListForecastsRequestRequestTypeDef",
    "ListMonitorEvaluationsRequestRequestTypeDef",
    "ListMonitorsRequestRequestTypeDef",
    "ListPredictorBacktestExportJobsRequestRequestTypeDef",
    "ListPredictorsRequestRequestTypeDef",
    "ListWhatIfAnalysesRequestRequestTypeDef",
    "ListWhatIfForecastExportsRequestRequestTypeDef",
    "ListWhatIfForecastsRequestRequestTypeDef",
    "ListForecastsResponseTypeDef",
    "InputDataConfigTypeDef",
    "ParameterRangesTypeDef",
    "ListDatasetGroupsRequestListDatasetGroupsPaginateTypeDef",
    "ListDatasetImportJobsRequestListDatasetImportJobsPaginateTypeDef",
    "ListDatasetsRequestListDatasetsPaginateTypeDef",
    "ListExplainabilitiesRequestListExplainabilitiesPaginateTypeDef",
    "ListExplainabilityExportsRequestListExplainabilityExportsPaginateTypeDef",
    "ListForecastExportJobsRequestListForecastExportJobsPaginateTypeDef",
    "ListForecastsRequestListForecastsPaginateTypeDef",
    "ListMonitorEvaluationsRequestListMonitorEvaluationsPaginateTypeDef",
    "ListMonitorsRequestListMonitorsPaginateTypeDef",
    "ListPredictorBacktestExportJobsRequestListPredictorBacktestExportJobsPaginateTypeDef",
    "ListPredictorsRequestListPredictorsPaginateTypeDef",
    "ListWhatIfAnalysesRequestListWhatIfAnalysesPaginateTypeDef",
    "ListWhatIfForecastExportsRequestListWhatIfForecastExportsPaginateTypeDef",
    "ListWhatIfForecastsRequestListWhatIfForecastsPaginateTypeDef",
    "ListMonitorsResponseTypeDef",
    "ListWhatIfAnalysesResponseTypeDef",
    "ListWhatIfForecastsResponseTypeDef",
    "MetricsTypeDef",
    "PredictorMonitorEvaluationTypeDef",
    "PredictorExecutionTypeDef",
    "SchemaTypeDef",
    "TimeSeriesTransformationTypeDef",
    "CreateAutoPredictorRequestRequestTypeDef",
    "DescribeAutoPredictorResponseTypeDef",
    "BaselineTypeDef",
    "ListExplainabilitiesResponseTypeDef",
    "CreateExplainabilityExportRequestRequestTypeDef",
    "CreateForecastExportJobRequestRequestTypeDef",
    "CreatePredictorBacktestExportJobRequestRequestTypeDef",
    "CreateWhatIfForecastExportRequestRequestTypeDef",
    "DescribeExplainabilityExportResponseTypeDef",
    "DescribeForecastExportJobResponseTypeDef",
    "DescribePredictorBacktestExportJobResponseTypeDef",
    "DescribeWhatIfForecastExportResponseTypeDef",
    "ExplainabilityExportSummaryTypeDef",
    "ForecastExportJobSummaryTypeDef",
    "PredictorBacktestExportJobSummaryTypeDef",
    "WhatIfForecastExportSummaryTypeDef",
    "CreateDatasetImportJobRequestRequestTypeDef",
    "DatasetImportJobSummaryTypeDef",
    "DescribeDatasetImportJobResponseTypeDef",
    "ListPredictorsResponseTypeDef",
    "FeaturizationConfigTypeDef",
    "HyperParameterTuningJobConfigTypeDef",
    "WindowSummaryTypeDef",
    "ListMonitorEvaluationsResponseTypeDef",
    "PredictorExecutionDetailsTypeDef",
    "CreateDatasetRequestRequestTypeDef",
    "CreateExplainabilityRequestRequestTypeDef",
    "DescribeDatasetResponseTypeDef",
    "DescribeExplainabilityResponseTypeDef",
    "TimeSeriesIdentifiersTypeDef",
    "TimeSeriesReplacementsDataSourceTypeDef",
    "DescribeMonitorResponseTypeDef",
    "ListExplainabilityExportsResponseTypeDef",
    "ListForecastExportJobsResponseTypeDef",
    "ListPredictorBacktestExportJobsResponseTypeDef",
    "ListWhatIfForecastExportsResponseTypeDef",
    "ListDatasetImportJobsResponseTypeDef",
    "CreatePredictorRequestRequestTypeDef",
    "EvaluationResultTypeDef",
    "DescribePredictorResponseTypeDef",
    "TimeSeriesSelectorTypeDef",
    "CreateWhatIfForecastRequestRequestTypeDef",
    "DescribeWhatIfForecastResponseTypeDef",
    "GetAccuracyMetricsResponseTypeDef",
    "CreateForecastRequestRequestTypeDef",
    "CreateWhatIfAnalysisRequestRequestTypeDef",
    "DescribeForecastResponseTypeDef",
    "DescribeWhatIfAnalysisResponseTypeDef",
)

ActionTypeDef = TypedDict(
    "ActionTypeDef",
    {
        "AttributeName": str,
        "Operation": OperationType,
        "Value": float,
    },
)
AdditionalDatasetTypeDef = TypedDict(
    "AdditionalDatasetTypeDef",
    {
        "Name": str,
        "Configuration": NotRequired[Mapping[str, Sequence[str]]],
    },
)
AttributeConfigTypeDef = TypedDict(
    "AttributeConfigTypeDef",
    {
        "AttributeName": str,
        "Transformations": Mapping[str, str],
    },
)
BaselineMetricTypeDef = TypedDict(
    "BaselineMetricTypeDef",
    {
        "Name": NotRequired[str],
        "Value": NotRequired[float],
    },
)
CategoricalParameterRangeTypeDef = TypedDict(
    "CategoricalParameterRangeTypeDef",
    {
        "Name": str,
        "Values": Sequence[str],
    },
)
ContinuousParameterRangeTypeDef = TypedDict(
    "ContinuousParameterRangeTypeDef",
    {
        "Name": str,
        "MaxValue": float,
        "MinValue": float,
        "ScalingType": NotRequired[ScalingTypeType],
    },
)
EncryptionConfigTypeDef = TypedDict(
    "EncryptionConfigTypeDef",
    {
        "RoleArn": str,
        "KMSKeyArn": str,
    },
)
MonitorConfigTypeDef = TypedDict(
    "MonitorConfigTypeDef",
    {
        "MonitorName": str,
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)
TimeAlignmentBoundaryTypeDef = TypedDict(
    "TimeAlignmentBoundaryTypeDef",
    {
        "Month": NotRequired[MonthType],
        "DayOfMonth": NotRequired[int],
        "DayOfWeek": NotRequired[DayOfWeekType],
        "Hour": NotRequired[int],
    },
)
ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, str],
        "RetryAttempts": int,
    },
)
ExplainabilityConfigTypeDef = TypedDict(
    "ExplainabilityConfigTypeDef",
    {
        "TimeSeriesGranularity": TimeSeriesGranularityType,
        "TimePointGranularity": TimePointGranularityType,
    },
)
EvaluationParametersTypeDef = TypedDict(
    "EvaluationParametersTypeDef",
    {
        "NumberOfBacktestWindows": NotRequired[int],
        "BackTestWindowOffset": NotRequired[int],
    },
)
S3ConfigTypeDef = TypedDict(
    "S3ConfigTypeDef",
    {
        "Path": str,
        "RoleArn": str,
        "KMSKeyArn": NotRequired[str],
    },
)
DatasetGroupSummaryTypeDef = TypedDict(
    "DatasetGroupSummaryTypeDef",
    {
        "DatasetGroupArn": NotRequired[str],
        "DatasetGroupName": NotRequired[str],
        "CreationTime": NotRequired[datetime],
        "LastModificationTime": NotRequired[datetime],
    },
)
DatasetSummaryTypeDef = TypedDict(
    "DatasetSummaryTypeDef",
    {
        "DatasetArn": NotRequired[str],
        "DatasetName": NotRequired[str],
        "DatasetType": NotRequired[DatasetTypeType],
        "Domain": NotRequired[DomainType],
        "CreationTime": NotRequired[datetime],
        "LastModificationTime": NotRequired[datetime],
    },
)
DeleteDatasetGroupRequestRequestTypeDef = TypedDict(
    "DeleteDatasetGroupRequestRequestTypeDef",
    {
        "DatasetGroupArn": str,
    },
)
DeleteDatasetImportJobRequestRequestTypeDef = TypedDict(
    "DeleteDatasetImportJobRequestRequestTypeDef",
    {
        "DatasetImportJobArn": str,
    },
)
DeleteDatasetRequestRequestTypeDef = TypedDict(
    "DeleteDatasetRequestRequestTypeDef",
    {
        "DatasetArn": str,
    },
)
DeleteExplainabilityExportRequestRequestTypeDef = TypedDict(
    "DeleteExplainabilityExportRequestRequestTypeDef",
    {
        "ExplainabilityExportArn": str,
    },
)
DeleteExplainabilityRequestRequestTypeDef = TypedDict(
    "DeleteExplainabilityRequestRequestTypeDef",
    {
        "ExplainabilityArn": str,
    },
)
DeleteForecastExportJobRequestRequestTypeDef = TypedDict(
    "DeleteForecastExportJobRequestRequestTypeDef",
    {
        "ForecastExportJobArn": str,
    },
)
DeleteForecastRequestRequestTypeDef = TypedDict(
    "DeleteForecastRequestRequestTypeDef",
    {
        "ForecastArn": str,
    },
)
DeleteMonitorRequestRequestTypeDef = TypedDict(
    "DeleteMonitorRequestRequestTypeDef",
    {
        "MonitorArn": str,
    },
)
DeletePredictorBacktestExportJobRequestRequestTypeDef = TypedDict(
    "DeletePredictorBacktestExportJobRequestRequestTypeDef",
    {
        "PredictorBacktestExportJobArn": str,
    },
)
DeletePredictorRequestRequestTypeDef = TypedDict(
    "DeletePredictorRequestRequestTypeDef",
    {
        "PredictorArn": str,
    },
)
DeleteResourceTreeRequestRequestTypeDef = TypedDict(
    "DeleteResourceTreeRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
DeleteWhatIfAnalysisRequestRequestTypeDef = TypedDict(
    "DeleteWhatIfAnalysisRequestRequestTypeDef",
    {
        "WhatIfAnalysisArn": str,
    },
)
DeleteWhatIfForecastExportRequestRequestTypeDef = TypedDict(
    "DeleteWhatIfForecastExportRequestRequestTypeDef",
    {
        "WhatIfForecastExportArn": str,
    },
)
DeleteWhatIfForecastRequestRequestTypeDef = TypedDict(
    "DeleteWhatIfForecastRequestRequestTypeDef",
    {
        "WhatIfForecastArn": str,
    },
)
DescribeAutoPredictorRequestRequestTypeDef = TypedDict(
    "DescribeAutoPredictorRequestRequestTypeDef",
    {
        "PredictorArn": str,
    },
)
ExplainabilityInfoTypeDef = TypedDict(
    "ExplainabilityInfoTypeDef",
    {
        "ExplainabilityArn": NotRequired[str],
        "Status": NotRequired[str],
    },
)
MonitorInfoTypeDef = TypedDict(
    "MonitorInfoTypeDef",
    {
        "MonitorArn": NotRequired[str],
        "Status": NotRequired[str],
    },
)
ReferencePredictorSummaryTypeDef = TypedDict(
    "ReferencePredictorSummaryTypeDef",
    {
        "Arn": NotRequired[str],
        "State": NotRequired[StateType],
    },
)
DescribeDatasetGroupRequestRequestTypeDef = TypedDict(
    "DescribeDatasetGroupRequestRequestTypeDef",
    {
        "DatasetGroupArn": str,
    },
)
DescribeDatasetImportJobRequestRequestTypeDef = TypedDict(
    "DescribeDatasetImportJobRequestRequestTypeDef",
    {
        "DatasetImportJobArn": str,
    },
)
StatisticsTypeDef = TypedDict(
    "StatisticsTypeDef",
    {
        "Count": NotRequired[int],
        "CountDistinct": NotRequired[int],
        "CountNull": NotRequired[int],
        "CountNan": NotRequired[int],
        "Min": NotRequired[str],
        "Max": NotRequired[str],
        "Avg": NotRequired[float],
        "Stddev": NotRequired[float],
        "CountLong": NotRequired[int],
        "CountDistinctLong": NotRequired[int],
        "CountNullLong": NotRequired[int],
        "CountNanLong": NotRequired[int],
    },
)
DescribeDatasetRequestRequestTypeDef = TypedDict(
    "DescribeDatasetRequestRequestTypeDef",
    {
        "DatasetArn": str,
    },
)
DescribeExplainabilityExportRequestRequestTypeDef = TypedDict(
    "DescribeExplainabilityExportRequestRequestTypeDef",
    {
        "ExplainabilityExportArn": str,
    },
)
DescribeExplainabilityRequestRequestTypeDef = TypedDict(
    "DescribeExplainabilityRequestRequestTypeDef",
    {
        "ExplainabilityArn": str,
    },
)
DescribeForecastExportJobRequestRequestTypeDef = TypedDict(
    "DescribeForecastExportJobRequestRequestTypeDef",
    {
        "ForecastExportJobArn": str,
    },
)
DescribeForecastRequestRequestTypeDef = TypedDict(
    "DescribeForecastRequestRequestTypeDef",
    {
        "ForecastArn": str,
    },
)
DescribeMonitorRequestRequestTypeDef = TypedDict(
    "DescribeMonitorRequestRequestTypeDef",
    {
        "MonitorArn": str,
    },
)
DescribePredictorBacktestExportJobRequestRequestTypeDef = TypedDict(
    "DescribePredictorBacktestExportJobRequestRequestTypeDef",
    {
        "PredictorBacktestExportJobArn": str,
    },
)
DescribePredictorRequestRequestTypeDef = TypedDict(
    "DescribePredictorRequestRequestTypeDef",
    {
        "PredictorArn": str,
    },
)
DescribeWhatIfAnalysisRequestRequestTypeDef = TypedDict(
    "DescribeWhatIfAnalysisRequestRequestTypeDef",
    {
        "WhatIfAnalysisArn": str,
    },
)
DescribeWhatIfForecastExportRequestRequestTypeDef = TypedDict(
    "DescribeWhatIfForecastExportRequestRequestTypeDef",
    {
        "WhatIfForecastExportArn": str,
    },
)
DescribeWhatIfForecastRequestRequestTypeDef = TypedDict(
    "DescribeWhatIfForecastRequestRequestTypeDef",
    {
        "WhatIfForecastArn": str,
    },
)
ErrorMetricTypeDef = TypedDict(
    "ErrorMetricTypeDef",
    {
        "ForecastType": NotRequired[str],
        "WAPE": NotRequired[float],
        "RMSE": NotRequired[float],
        "MASE": NotRequired[float],
        "MAPE": NotRequired[float],
    },
)
FeaturizationMethodTypeDef = TypedDict(
    "FeaturizationMethodTypeDef",
    {
        "FeaturizationMethodName": Literal["filling"],
        "FeaturizationMethodParameters": NotRequired[Mapping[str, str]],
    },
)
FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "Key": str,
        "Value": str,
        "Condition": FilterConditionStringType,
    },
)
ForecastSummaryTypeDef = TypedDict(
    "ForecastSummaryTypeDef",
    {
        "ForecastArn": NotRequired[str],
        "ForecastName": NotRequired[str],
        "PredictorArn": NotRequired[str],
        "CreatedUsingAutoPredictor": NotRequired[bool],
        "DatasetGroupArn": NotRequired[str],
        "Status": NotRequired[str],
        "Message": NotRequired[str],
        "CreationTime": NotRequired[datetime],
        "LastModificationTime": NotRequired[datetime],
    },
)
GetAccuracyMetricsRequestRequestTypeDef = TypedDict(
    "GetAccuracyMetricsRequestRequestTypeDef",
    {
        "PredictorArn": str,
    },
)
SupplementaryFeatureTypeDef = TypedDict(
    "SupplementaryFeatureTypeDef",
    {
        "Name": str,
        "Value": str,
    },
)
IntegerParameterRangeTypeDef = TypedDict(
    "IntegerParameterRangeTypeDef",
    {
        "Name": str,
        "MaxValue": int,
        "MinValue": int,
        "ScalingType": NotRequired[ScalingTypeType],
    },
)
PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": NotRequired[int],
        "PageSize": NotRequired[int],
        "StartingToken": NotRequired[str],
    },
)
ListDatasetGroupsRequestRequestTypeDef = TypedDict(
    "ListDatasetGroupsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListDatasetsRequestRequestTypeDef = TypedDict(
    "ListDatasetsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
MonitorSummaryTypeDef = TypedDict(
    "MonitorSummaryTypeDef",
    {
        "MonitorArn": NotRequired[str],
        "MonitorName": NotRequired[str],
        "ResourceArn": NotRequired[str],
        "Status": NotRequired[str],
        "CreationTime": NotRequired[datetime],
        "LastModificationTime": NotRequired[datetime],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
WhatIfAnalysisSummaryTypeDef = TypedDict(
    "WhatIfAnalysisSummaryTypeDef",
    {
        "WhatIfAnalysisArn": NotRequired[str],
        "WhatIfAnalysisName": NotRequired[str],
        "ForecastArn": NotRequired[str],
        "Status": NotRequired[str],
        "Message": NotRequired[str],
        "CreationTime": NotRequired[datetime],
        "LastModificationTime": NotRequired[datetime],
    },
)
WhatIfForecastSummaryTypeDef = TypedDict(
    "WhatIfForecastSummaryTypeDef",
    {
        "WhatIfForecastArn": NotRequired[str],
        "WhatIfForecastName": NotRequired[str],
        "WhatIfAnalysisArn": NotRequired[str],
        "Status": NotRequired[str],
        "Message": NotRequired[str],
        "CreationTime": NotRequired[datetime],
        "LastModificationTime": NotRequired[datetime],
    },
)
MetricResultTypeDef = TypedDict(
    "MetricResultTypeDef",
    {
        "MetricName": NotRequired[str],
        "MetricValue": NotRequired[float],
    },
)
WeightedQuantileLossTypeDef = TypedDict(
    "WeightedQuantileLossTypeDef",
    {
        "Quantile": NotRequired[float],
        "LossValue": NotRequired[float],
    },
)
MonitorDataSourceTypeDef = TypedDict(
    "MonitorDataSourceTypeDef",
    {
        "DatasetImportJobArn": NotRequired[str],
        "ForecastArn": NotRequired[str],
        "PredictorArn": NotRequired[str],
    },
)
PredictorEventTypeDef = TypedDict(
    "PredictorEventTypeDef",
    {
        "Detail": NotRequired[str],
        "Datetime": NotRequired[datetime],
    },
)
TestWindowSummaryTypeDef = TypedDict(
    "TestWindowSummaryTypeDef",
    {
        "TestWindowStart": NotRequired[datetime],
        "TestWindowEnd": NotRequired[datetime],
        "Status": NotRequired[str],
        "Message": NotRequired[str],
    },
)
ResumeResourceRequestRequestTypeDef = TypedDict(
    "ResumeResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
SchemaAttributeTypeDef = TypedDict(
    "SchemaAttributeTypeDef",
    {
        "AttributeName": NotRequired[str],
        "AttributeType": NotRequired[AttributeTypeType],
    },
)
StopResourceRequestRequestTypeDef = TypedDict(
    "StopResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
TimeSeriesConditionTypeDef = TypedDict(
    "TimeSeriesConditionTypeDef",
    {
        "AttributeName": str,
        "AttributeValue": str,
        "Condition": ConditionType,
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)
UpdateDatasetGroupRequestRequestTypeDef = TypedDict(
    "UpdateDatasetGroupRequestRequestTypeDef",
    {
        "DatasetGroupArn": str,
        "DatasetArns": Sequence[str],
    },
)
DataConfigTypeDef = TypedDict(
    "DataConfigTypeDef",
    {
        "DatasetGroupArn": str,
        "AttributeConfigs": NotRequired[Sequence[AttributeConfigTypeDef]],
        "AdditionalDatasets": NotRequired[Sequence[AdditionalDatasetTypeDef]],
    },
)
PredictorBaselineTypeDef = TypedDict(
    "PredictorBaselineTypeDef",
    {
        "BaselineMetrics": NotRequired[List[BaselineMetricTypeDef]],
    },
)
CreateDatasetGroupRequestRequestTypeDef = TypedDict(
    "CreateDatasetGroupRequestRequestTypeDef",
    {
        "DatasetGroupName": str,
        "Domain": DomainType,
        "DatasetArns": NotRequired[Sequence[str]],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateMonitorRequestRequestTypeDef = TypedDict(
    "CreateMonitorRequestRequestTypeDef",
    {
        "MonitorName": str,
        "ResourceArn": str,
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Sequence[TagTypeDef],
    },
)
CreateAutoPredictorResponseTypeDef = TypedDict(
    "CreateAutoPredictorResponseTypeDef",
    {
        "PredictorArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDatasetGroupResponseTypeDef = TypedDict(
    "CreateDatasetGroupResponseTypeDef",
    {
        "DatasetGroupArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDatasetImportJobResponseTypeDef = TypedDict(
    "CreateDatasetImportJobResponseTypeDef",
    {
        "DatasetImportJobArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDatasetResponseTypeDef = TypedDict(
    "CreateDatasetResponseTypeDef",
    {
        "DatasetArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateExplainabilityExportResponseTypeDef = TypedDict(
    "CreateExplainabilityExportResponseTypeDef",
    {
        "ExplainabilityExportArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateExplainabilityResponseTypeDef = TypedDict(
    "CreateExplainabilityResponseTypeDef",
    {
        "ExplainabilityArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateForecastExportJobResponseTypeDef = TypedDict(
    "CreateForecastExportJobResponseTypeDef",
    {
        "ForecastExportJobArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateForecastResponseTypeDef = TypedDict(
    "CreateForecastResponseTypeDef",
    {
        "ForecastArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateMonitorResponseTypeDef = TypedDict(
    "CreateMonitorResponseTypeDef",
    {
        "MonitorArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreatePredictorBacktestExportJobResponseTypeDef = TypedDict(
    "CreatePredictorBacktestExportJobResponseTypeDef",
    {
        "PredictorBacktestExportJobArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreatePredictorResponseTypeDef = TypedDict(
    "CreatePredictorResponseTypeDef",
    {
        "PredictorArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateWhatIfAnalysisResponseTypeDef = TypedDict(
    "CreateWhatIfAnalysisResponseTypeDef",
    {
        "WhatIfAnalysisArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateWhatIfForecastExportResponseTypeDef = TypedDict(
    "CreateWhatIfForecastExportResponseTypeDef",
    {
        "WhatIfForecastExportArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateWhatIfForecastResponseTypeDef = TypedDict(
    "CreateWhatIfForecastResponseTypeDef",
    {
        "WhatIfForecastArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeDatasetGroupResponseTypeDef = TypedDict(
    "DescribeDatasetGroupResponseTypeDef",
    {
        "DatasetGroupName": str,
        "DatasetGroupArn": str,
        "DatasetArns": List[str],
        "Domain": DomainType,
        "Status": str,
        "CreationTime": datetime,
        "LastModificationTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ExplainabilitySummaryTypeDef = TypedDict(
    "ExplainabilitySummaryTypeDef",
    {
        "ExplainabilityArn": NotRequired[str],
        "ExplainabilityName": NotRequired[str],
        "ResourceArn": NotRequired[str],
        "ExplainabilityConfig": NotRequired[ExplainabilityConfigTypeDef],
        "Status": NotRequired[str],
        "Message": NotRequired[str],
        "CreationTime": NotRequired[datetime],
        "LastModificationTime": NotRequired[datetime],
    },
)
DataDestinationTypeDef = TypedDict(
    "DataDestinationTypeDef",
    {
        "S3Config": S3ConfigTypeDef,
    },
)
DataSourceTypeDef = TypedDict(
    "DataSourceTypeDef",
    {
        "S3Config": S3ConfigTypeDef,
    },
)
ListDatasetGroupsResponseTypeDef = TypedDict(
    "ListDatasetGroupsResponseTypeDef",
    {
        "DatasetGroups": List[DatasetGroupSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListDatasetsResponseTypeDef = TypedDict(
    "ListDatasetsResponseTypeDef",
    {
        "Datasets": List[DatasetSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PredictorSummaryTypeDef = TypedDict(
    "PredictorSummaryTypeDef",
    {
        "PredictorArn": NotRequired[str],
        "PredictorName": NotRequired[str],
        "DatasetGroupArn": NotRequired[str],
        "IsAutoPredictor": NotRequired[bool],
        "ReferencePredictorSummary": NotRequired[ReferencePredictorSummaryTypeDef],
        "Status": NotRequired[str],
        "Message": NotRequired[str],
        "CreationTime": NotRequired[datetime],
        "LastModificationTime": NotRequired[datetime],
    },
)
FeaturizationTypeDef = TypedDict(
    "FeaturizationTypeDef",
    {
        "AttributeName": str,
        "FeaturizationPipeline": NotRequired[Sequence[FeaturizationMethodTypeDef]],
    },
)
ListDatasetImportJobsRequestRequestTypeDef = TypedDict(
    "ListDatasetImportJobsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
    },
)
ListExplainabilitiesRequestRequestTypeDef = TypedDict(
    "ListExplainabilitiesRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
    },
)
ListExplainabilityExportsRequestRequestTypeDef = TypedDict(
    "ListExplainabilityExportsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
    },
)
ListForecastExportJobsRequestRequestTypeDef = TypedDict(
    "ListForecastExportJobsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
    },
)
ListForecastsRequestRequestTypeDef = TypedDict(
    "ListForecastsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
    },
)
ListMonitorEvaluationsRequestRequestTypeDef = TypedDict(
    "ListMonitorEvaluationsRequestRequestTypeDef",
    {
        "MonitorArn": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
    },
)
ListMonitorsRequestRequestTypeDef = TypedDict(
    "ListMonitorsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
    },
)
ListPredictorBacktestExportJobsRequestRequestTypeDef = TypedDict(
    "ListPredictorBacktestExportJobsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
    },
)
ListPredictorsRequestRequestTypeDef = TypedDict(
    "ListPredictorsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
    },
)
ListWhatIfAnalysesRequestRequestTypeDef = TypedDict(
    "ListWhatIfAnalysesRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
    },
)
ListWhatIfForecastExportsRequestRequestTypeDef = TypedDict(
    "ListWhatIfForecastExportsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
    },
)
ListWhatIfForecastsRequestRequestTypeDef = TypedDict(
    "ListWhatIfForecastsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
    },
)
ListForecastsResponseTypeDef = TypedDict(
    "ListForecastsResponseTypeDef",
    {
        "Forecasts": List[ForecastSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
InputDataConfigTypeDef = TypedDict(
    "InputDataConfigTypeDef",
    {
        "DatasetGroupArn": str,
        "SupplementaryFeatures": NotRequired[Sequence[SupplementaryFeatureTypeDef]],
    },
)
ParameterRangesTypeDef = TypedDict(
    "ParameterRangesTypeDef",
    {
        "CategoricalParameterRanges": NotRequired[Sequence[CategoricalParameterRangeTypeDef]],
        "ContinuousParameterRanges": NotRequired[Sequence[ContinuousParameterRangeTypeDef]],
        "IntegerParameterRanges": NotRequired[Sequence[IntegerParameterRangeTypeDef]],
    },
)
ListDatasetGroupsRequestListDatasetGroupsPaginateTypeDef = TypedDict(
    "ListDatasetGroupsRequestListDatasetGroupsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDatasetImportJobsRequestListDatasetImportJobsPaginateTypeDef = TypedDict(
    "ListDatasetImportJobsRequestListDatasetImportJobsPaginateTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDatasetsRequestListDatasetsPaginateTypeDef = TypedDict(
    "ListDatasetsRequestListDatasetsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListExplainabilitiesRequestListExplainabilitiesPaginateTypeDef = TypedDict(
    "ListExplainabilitiesRequestListExplainabilitiesPaginateTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListExplainabilityExportsRequestListExplainabilityExportsPaginateTypeDef = TypedDict(
    "ListExplainabilityExportsRequestListExplainabilityExportsPaginateTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListForecastExportJobsRequestListForecastExportJobsPaginateTypeDef = TypedDict(
    "ListForecastExportJobsRequestListForecastExportJobsPaginateTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListForecastsRequestListForecastsPaginateTypeDef = TypedDict(
    "ListForecastsRequestListForecastsPaginateTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListMonitorEvaluationsRequestListMonitorEvaluationsPaginateTypeDef = TypedDict(
    "ListMonitorEvaluationsRequestListMonitorEvaluationsPaginateTypeDef",
    {
        "MonitorArn": str,
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListMonitorsRequestListMonitorsPaginateTypeDef = TypedDict(
    "ListMonitorsRequestListMonitorsPaginateTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListPredictorBacktestExportJobsRequestListPredictorBacktestExportJobsPaginateTypeDef = TypedDict(
    "ListPredictorBacktestExportJobsRequestListPredictorBacktestExportJobsPaginateTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListPredictorsRequestListPredictorsPaginateTypeDef = TypedDict(
    "ListPredictorsRequestListPredictorsPaginateTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListWhatIfAnalysesRequestListWhatIfAnalysesPaginateTypeDef = TypedDict(
    "ListWhatIfAnalysesRequestListWhatIfAnalysesPaginateTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListWhatIfForecastExportsRequestListWhatIfForecastExportsPaginateTypeDef = TypedDict(
    "ListWhatIfForecastExportsRequestListWhatIfForecastExportsPaginateTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListWhatIfForecastsRequestListWhatIfForecastsPaginateTypeDef = TypedDict(
    "ListWhatIfForecastsRequestListWhatIfForecastsPaginateTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListMonitorsResponseTypeDef = TypedDict(
    "ListMonitorsResponseTypeDef",
    {
        "Monitors": List[MonitorSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListWhatIfAnalysesResponseTypeDef = TypedDict(
    "ListWhatIfAnalysesResponseTypeDef",
    {
        "WhatIfAnalyses": List[WhatIfAnalysisSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListWhatIfForecastsResponseTypeDef = TypedDict(
    "ListWhatIfForecastsResponseTypeDef",
    {
        "WhatIfForecasts": List[WhatIfForecastSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
MetricsTypeDef = TypedDict(
    "MetricsTypeDef",
    {
        "RMSE": NotRequired[float],
        "WeightedQuantileLosses": NotRequired[List[WeightedQuantileLossTypeDef]],
        "ErrorMetrics": NotRequired[List[ErrorMetricTypeDef]],
        "AverageWeightedQuantileLoss": NotRequired[float],
    },
)
PredictorMonitorEvaluationTypeDef = TypedDict(
    "PredictorMonitorEvaluationTypeDef",
    {
        "ResourceArn": NotRequired[str],
        "MonitorArn": NotRequired[str],
        "EvaluationTime": NotRequired[datetime],
        "EvaluationState": NotRequired[str],
        "WindowStartDatetime": NotRequired[datetime],
        "WindowEndDatetime": NotRequired[datetime],
        "PredictorEvent": NotRequired[PredictorEventTypeDef],
        "MonitorDataSource": NotRequired[MonitorDataSourceTypeDef],
        "MetricResults": NotRequired[List[MetricResultTypeDef]],
        "NumItemsEvaluated": NotRequired[int],
        "Message": NotRequired[str],
    },
)
PredictorExecutionTypeDef = TypedDict(
    "PredictorExecutionTypeDef",
    {
        "AlgorithmArn": NotRequired[str],
        "TestWindows": NotRequired[List[TestWindowSummaryTypeDef]],
    },
)
SchemaTypeDef = TypedDict(
    "SchemaTypeDef",
    {
        "Attributes": NotRequired[Sequence[SchemaAttributeTypeDef]],
    },
)
TimeSeriesTransformationTypeDef = TypedDict(
    "TimeSeriesTransformationTypeDef",
    {
        "Action": NotRequired[ActionTypeDef],
        "TimeSeriesConditions": NotRequired[Sequence[TimeSeriesConditionTypeDef]],
    },
)
CreateAutoPredictorRequestRequestTypeDef = TypedDict(
    "CreateAutoPredictorRequestRequestTypeDef",
    {
        "PredictorName": str,
        "ForecastHorizon": NotRequired[int],
        "ForecastTypes": NotRequired[Sequence[str]],
        "ForecastDimensions": NotRequired[Sequence[str]],
        "ForecastFrequency": NotRequired[str],
        "DataConfig": NotRequired[DataConfigTypeDef],
        "EncryptionConfig": NotRequired[EncryptionConfigTypeDef],
        "ReferencePredictorArn": NotRequired[str],
        "OptimizationMetric": NotRequired[OptimizationMetricType],
        "ExplainPredictor": NotRequired[bool],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "MonitorConfig": NotRequired[MonitorConfigTypeDef],
        "TimeAlignmentBoundary": NotRequired[TimeAlignmentBoundaryTypeDef],
    },
)
DescribeAutoPredictorResponseTypeDef = TypedDict(
    "DescribeAutoPredictorResponseTypeDef",
    {
        "PredictorArn": str,
        "PredictorName": str,
        "ForecastHorizon": int,
        "ForecastTypes": List[str],
        "ForecastFrequency": str,
        "ForecastDimensions": List[str],
        "DatasetImportJobArns": List[str],
        "DataConfig": DataConfigTypeDef,
        "EncryptionConfig": EncryptionConfigTypeDef,
        "ReferencePredictorSummary": ReferencePredictorSummaryTypeDef,
        "EstimatedTimeRemainingInMinutes": int,
        "Status": str,
        "Message": str,
        "CreationTime": datetime,
        "LastModificationTime": datetime,
        "OptimizationMetric": OptimizationMetricType,
        "ExplainabilityInfo": ExplainabilityInfoTypeDef,
        "MonitorInfo": MonitorInfoTypeDef,
        "TimeAlignmentBoundary": TimeAlignmentBoundaryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BaselineTypeDef = TypedDict(
    "BaselineTypeDef",
    {
        "PredictorBaseline": NotRequired[PredictorBaselineTypeDef],
    },
)
ListExplainabilitiesResponseTypeDef = TypedDict(
    "ListExplainabilitiesResponseTypeDef",
    {
        "Explainabilities": List[ExplainabilitySummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateExplainabilityExportRequestRequestTypeDef = TypedDict(
    "CreateExplainabilityExportRequestRequestTypeDef",
    {
        "ExplainabilityExportName": str,
        "ExplainabilityArn": str,
        "Destination": DataDestinationTypeDef,
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "Format": NotRequired[str],
    },
)
CreateForecastExportJobRequestRequestTypeDef = TypedDict(
    "CreateForecastExportJobRequestRequestTypeDef",
    {
        "ForecastExportJobName": str,
        "ForecastArn": str,
        "Destination": DataDestinationTypeDef,
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "Format": NotRequired[str],
    },
)
CreatePredictorBacktestExportJobRequestRequestTypeDef = TypedDict(
    "CreatePredictorBacktestExportJobRequestRequestTypeDef",
    {
        "PredictorBacktestExportJobName": str,
        "PredictorArn": str,
        "Destination": DataDestinationTypeDef,
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "Format": NotRequired[str],
    },
)
CreateWhatIfForecastExportRequestRequestTypeDef = TypedDict(
    "CreateWhatIfForecastExportRequestRequestTypeDef",
    {
        "WhatIfForecastExportName": str,
        "WhatIfForecastArns": Sequence[str],
        "Destination": DataDestinationTypeDef,
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "Format": NotRequired[str],
    },
)
DescribeExplainabilityExportResponseTypeDef = TypedDict(
    "DescribeExplainabilityExportResponseTypeDef",
    {
        "ExplainabilityExportArn": str,
        "ExplainabilityExportName": str,
        "ExplainabilityArn": str,
        "Destination": DataDestinationTypeDef,
        "Message": str,
        "Status": str,
        "CreationTime": datetime,
        "LastModificationTime": datetime,
        "Format": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeForecastExportJobResponseTypeDef = TypedDict(
    "DescribeForecastExportJobResponseTypeDef",
    {
        "ForecastExportJobArn": str,
        "ForecastExportJobName": str,
        "ForecastArn": str,
        "Destination": DataDestinationTypeDef,
        "Message": str,
        "Status": str,
        "CreationTime": datetime,
        "LastModificationTime": datetime,
        "Format": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribePredictorBacktestExportJobResponseTypeDef = TypedDict(
    "DescribePredictorBacktestExportJobResponseTypeDef",
    {
        "PredictorBacktestExportJobArn": str,
        "PredictorBacktestExportJobName": str,
        "PredictorArn": str,
        "Destination": DataDestinationTypeDef,
        "Message": str,
        "Status": str,
        "CreationTime": datetime,
        "LastModificationTime": datetime,
        "Format": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeWhatIfForecastExportResponseTypeDef = TypedDict(
    "DescribeWhatIfForecastExportResponseTypeDef",
    {
        "WhatIfForecastExportArn": str,
        "WhatIfForecastExportName": str,
        "WhatIfForecastArns": List[str],
        "Destination": DataDestinationTypeDef,
        "Message": str,
        "Status": str,
        "CreationTime": datetime,
        "EstimatedTimeRemainingInMinutes": int,
        "LastModificationTime": datetime,
        "Format": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ExplainabilityExportSummaryTypeDef = TypedDict(
    "ExplainabilityExportSummaryTypeDef",
    {
        "ExplainabilityExportArn": NotRequired[str],
        "ExplainabilityExportName": NotRequired[str],
        "Destination": NotRequired[DataDestinationTypeDef],
        "Status": NotRequired[str],
        "Message": NotRequired[str],
        "CreationTime": NotRequired[datetime],
        "LastModificationTime": NotRequired[datetime],
    },
)
ForecastExportJobSummaryTypeDef = TypedDict(
    "ForecastExportJobSummaryTypeDef",
    {
        "ForecastExportJobArn": NotRequired[str],
        "ForecastExportJobName": NotRequired[str],
        "Destination": NotRequired[DataDestinationTypeDef],
        "Status": NotRequired[str],
        "Message": NotRequired[str],
        "CreationTime": NotRequired[datetime],
        "LastModificationTime": NotRequired[datetime],
    },
)
PredictorBacktestExportJobSummaryTypeDef = TypedDict(
    "PredictorBacktestExportJobSummaryTypeDef",
    {
        "PredictorBacktestExportJobArn": NotRequired[str],
        "PredictorBacktestExportJobName": NotRequired[str],
        "Destination": NotRequired[DataDestinationTypeDef],
        "Status": NotRequired[str],
        "Message": NotRequired[str],
        "CreationTime": NotRequired[datetime],
        "LastModificationTime": NotRequired[datetime],
    },
)
WhatIfForecastExportSummaryTypeDef = TypedDict(
    "WhatIfForecastExportSummaryTypeDef",
    {
        "WhatIfForecastExportArn": NotRequired[str],
        "WhatIfForecastArns": NotRequired[List[str]],
        "WhatIfForecastExportName": NotRequired[str],
        "Destination": NotRequired[DataDestinationTypeDef],
        "Status": NotRequired[str],
        "Message": NotRequired[str],
        "CreationTime": NotRequired[datetime],
        "LastModificationTime": NotRequired[datetime],
    },
)
CreateDatasetImportJobRequestRequestTypeDef = TypedDict(
    "CreateDatasetImportJobRequestRequestTypeDef",
    {
        "DatasetImportJobName": str,
        "DatasetArn": str,
        "DataSource": DataSourceTypeDef,
        "TimestampFormat": NotRequired[str],
        "TimeZone": NotRequired[str],
        "UseGeolocationForTimeZone": NotRequired[bool],
        "GeolocationFormat": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "Format": NotRequired[str],
        "ImportMode": NotRequired[ImportModeType],
    },
)
DatasetImportJobSummaryTypeDef = TypedDict(
    "DatasetImportJobSummaryTypeDef",
    {
        "DatasetImportJobArn": NotRequired[str],
        "DatasetImportJobName": NotRequired[str],
        "DataSource": NotRequired[DataSourceTypeDef],
        "Status": NotRequired[str],
        "Message": NotRequired[str],
        "CreationTime": NotRequired[datetime],
        "LastModificationTime": NotRequired[datetime],
        "ImportMode": NotRequired[ImportModeType],
    },
)
DescribeDatasetImportJobResponseTypeDef = TypedDict(
    "DescribeDatasetImportJobResponseTypeDef",
    {
        "DatasetImportJobName": str,
        "DatasetImportJobArn": str,
        "DatasetArn": str,
        "TimestampFormat": str,
        "TimeZone": str,
        "UseGeolocationForTimeZone": bool,
        "GeolocationFormat": str,
        "DataSource": DataSourceTypeDef,
        "EstimatedTimeRemainingInMinutes": int,
        "FieldStatistics": Dict[str, StatisticsTypeDef],
        "DataSize": float,
        "Status": str,
        "Message": str,
        "CreationTime": datetime,
        "LastModificationTime": datetime,
        "Format": str,
        "ImportMode": ImportModeType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListPredictorsResponseTypeDef = TypedDict(
    "ListPredictorsResponseTypeDef",
    {
        "Predictors": List[PredictorSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
FeaturizationConfigTypeDef = TypedDict(
    "FeaturizationConfigTypeDef",
    {
        "ForecastFrequency": str,
        "ForecastDimensions": NotRequired[Sequence[str]],
        "Featurizations": NotRequired[Sequence[FeaturizationTypeDef]],
    },
)
HyperParameterTuningJobConfigTypeDef = TypedDict(
    "HyperParameterTuningJobConfigTypeDef",
    {
        "ParameterRanges": NotRequired[ParameterRangesTypeDef],
    },
)
WindowSummaryTypeDef = TypedDict(
    "WindowSummaryTypeDef",
    {
        "TestWindowStart": NotRequired[datetime],
        "TestWindowEnd": NotRequired[datetime],
        "ItemCount": NotRequired[int],
        "EvaluationType": NotRequired[EvaluationTypeType],
        "Metrics": NotRequired[MetricsTypeDef],
    },
)
ListMonitorEvaluationsResponseTypeDef = TypedDict(
    "ListMonitorEvaluationsResponseTypeDef",
    {
        "NextToken": str,
        "PredictorMonitorEvaluations": List[PredictorMonitorEvaluationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PredictorExecutionDetailsTypeDef = TypedDict(
    "PredictorExecutionDetailsTypeDef",
    {
        "PredictorExecutions": NotRequired[List[PredictorExecutionTypeDef]],
    },
)
CreateDatasetRequestRequestTypeDef = TypedDict(
    "CreateDatasetRequestRequestTypeDef",
    {
        "DatasetName": str,
        "Domain": DomainType,
        "DatasetType": DatasetTypeType,
        "Schema": SchemaTypeDef,
        "DataFrequency": NotRequired[str],
        "EncryptionConfig": NotRequired[EncryptionConfigTypeDef],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateExplainabilityRequestRequestTypeDef = TypedDict(
    "CreateExplainabilityRequestRequestTypeDef",
    {
        "ExplainabilityName": str,
        "ResourceArn": str,
        "ExplainabilityConfig": ExplainabilityConfigTypeDef,
        "DataSource": NotRequired[DataSourceTypeDef],
        "Schema": NotRequired[SchemaTypeDef],
        "EnableVisualization": NotRequired[bool],
        "StartDateTime": NotRequired[str],
        "EndDateTime": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
DescribeDatasetResponseTypeDef = TypedDict(
    "DescribeDatasetResponseTypeDef",
    {
        "DatasetArn": str,
        "DatasetName": str,
        "Domain": DomainType,
        "DatasetType": DatasetTypeType,
        "DataFrequency": str,
        "Schema": SchemaTypeDef,
        "EncryptionConfig": EncryptionConfigTypeDef,
        "Status": str,
        "CreationTime": datetime,
        "LastModificationTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeExplainabilityResponseTypeDef = TypedDict(
    "DescribeExplainabilityResponseTypeDef",
    {
        "ExplainabilityArn": str,
        "ExplainabilityName": str,
        "ResourceArn": str,
        "ExplainabilityConfig": ExplainabilityConfigTypeDef,
        "EnableVisualization": bool,
        "DataSource": DataSourceTypeDef,
        "Schema": SchemaTypeDef,
        "StartDateTime": str,
        "EndDateTime": str,
        "EstimatedTimeRemainingInMinutes": int,
        "Message": str,
        "Status": str,
        "CreationTime": datetime,
        "LastModificationTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TimeSeriesIdentifiersTypeDef = TypedDict(
    "TimeSeriesIdentifiersTypeDef",
    {
        "DataSource": NotRequired[DataSourceTypeDef],
        "Schema": NotRequired[SchemaTypeDef],
        "Format": NotRequired[str],
    },
)
TimeSeriesReplacementsDataSourceTypeDef = TypedDict(
    "TimeSeriesReplacementsDataSourceTypeDef",
    {
        "S3Config": S3ConfigTypeDef,
        "Schema": SchemaTypeDef,
        "Format": NotRequired[str],
        "TimestampFormat": NotRequired[str],
    },
)
DescribeMonitorResponseTypeDef = TypedDict(
    "DescribeMonitorResponseTypeDef",
    {
        "MonitorName": str,
        "MonitorArn": str,
        "ResourceArn": str,
        "Status": str,
        "LastEvaluationTime": datetime,
        "LastEvaluationState": str,
        "Baseline": BaselineTypeDef,
        "Message": str,
        "CreationTime": datetime,
        "LastModificationTime": datetime,
        "EstimatedEvaluationTimeRemainingInMinutes": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListExplainabilityExportsResponseTypeDef = TypedDict(
    "ListExplainabilityExportsResponseTypeDef",
    {
        "ExplainabilityExports": List[ExplainabilityExportSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListForecastExportJobsResponseTypeDef = TypedDict(
    "ListForecastExportJobsResponseTypeDef",
    {
        "ForecastExportJobs": List[ForecastExportJobSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListPredictorBacktestExportJobsResponseTypeDef = TypedDict(
    "ListPredictorBacktestExportJobsResponseTypeDef",
    {
        "PredictorBacktestExportJobs": List[PredictorBacktestExportJobSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListWhatIfForecastExportsResponseTypeDef = TypedDict(
    "ListWhatIfForecastExportsResponseTypeDef",
    {
        "WhatIfForecastExports": List[WhatIfForecastExportSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListDatasetImportJobsResponseTypeDef = TypedDict(
    "ListDatasetImportJobsResponseTypeDef",
    {
        "DatasetImportJobs": List[DatasetImportJobSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreatePredictorRequestRequestTypeDef = TypedDict(
    "CreatePredictorRequestRequestTypeDef",
    {
        "PredictorName": str,
        "ForecastHorizon": int,
        "InputDataConfig": InputDataConfigTypeDef,
        "FeaturizationConfig": FeaturizationConfigTypeDef,
        "AlgorithmArn": NotRequired[str],
        "ForecastTypes": NotRequired[Sequence[str]],
        "PerformAutoML": NotRequired[bool],
        "AutoMLOverrideStrategy": NotRequired[AutoMLOverrideStrategyType],
        "PerformHPO": NotRequired[bool],
        "TrainingParameters": NotRequired[Mapping[str, str]],
        "EvaluationParameters": NotRequired[EvaluationParametersTypeDef],
        "HPOConfig": NotRequired[HyperParameterTuningJobConfigTypeDef],
        "EncryptionConfig": NotRequired[EncryptionConfigTypeDef],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "OptimizationMetric": NotRequired[OptimizationMetricType],
    },
)
EvaluationResultTypeDef = TypedDict(
    "EvaluationResultTypeDef",
    {
        "AlgorithmArn": NotRequired[str],
        "TestWindows": NotRequired[List[WindowSummaryTypeDef]],
    },
)
DescribePredictorResponseTypeDef = TypedDict(
    "DescribePredictorResponseTypeDef",
    {
        "PredictorArn": str,
        "PredictorName": str,
        "AlgorithmArn": str,
        "AutoMLAlgorithmArns": List[str],
        "ForecastHorizon": int,
        "ForecastTypes": List[str],
        "PerformAutoML": bool,
        "AutoMLOverrideStrategy": AutoMLOverrideStrategyType,
        "PerformHPO": bool,
        "TrainingParameters": Dict[str, str],
        "EvaluationParameters": EvaluationParametersTypeDef,
        "HPOConfig": HyperParameterTuningJobConfigTypeDef,
        "InputDataConfig": InputDataConfigTypeDef,
        "FeaturizationConfig": FeaturizationConfigTypeDef,
        "EncryptionConfig": EncryptionConfigTypeDef,
        "PredictorExecutionDetails": PredictorExecutionDetailsTypeDef,
        "EstimatedTimeRemainingInMinutes": int,
        "IsAutoPredictor": bool,
        "DatasetImportJobArns": List[str],
        "Status": str,
        "Message": str,
        "CreationTime": datetime,
        "LastModificationTime": datetime,
        "OptimizationMetric": OptimizationMetricType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TimeSeriesSelectorTypeDef = TypedDict(
    "TimeSeriesSelectorTypeDef",
    {
        "TimeSeriesIdentifiers": NotRequired[TimeSeriesIdentifiersTypeDef],
    },
)
CreateWhatIfForecastRequestRequestTypeDef = TypedDict(
    "CreateWhatIfForecastRequestRequestTypeDef",
    {
        "WhatIfForecastName": str,
        "WhatIfAnalysisArn": str,
        "TimeSeriesTransformations": NotRequired[Sequence[TimeSeriesTransformationTypeDef]],
        "TimeSeriesReplacementsDataSource": NotRequired[TimeSeriesReplacementsDataSourceTypeDef],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
DescribeWhatIfForecastResponseTypeDef = TypedDict(
    "DescribeWhatIfForecastResponseTypeDef",
    {
        "WhatIfForecastName": str,
        "WhatIfForecastArn": str,
        "WhatIfAnalysisArn": str,
        "EstimatedTimeRemainingInMinutes": int,
        "Status": str,
        "Message": str,
        "CreationTime": datetime,
        "LastModificationTime": datetime,
        "TimeSeriesTransformations": List[TimeSeriesTransformationTypeDef],
        "TimeSeriesReplacementsDataSource": TimeSeriesReplacementsDataSourceTypeDef,
        "ForecastTypes": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAccuracyMetricsResponseTypeDef = TypedDict(
    "GetAccuracyMetricsResponseTypeDef",
    {
        "PredictorEvaluationResults": List[EvaluationResultTypeDef],
        "IsAutoPredictor": bool,
        "AutoMLOverrideStrategy": AutoMLOverrideStrategyType,
        "OptimizationMetric": OptimizationMetricType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateForecastRequestRequestTypeDef = TypedDict(
    "CreateForecastRequestRequestTypeDef",
    {
        "ForecastName": str,
        "PredictorArn": str,
        "ForecastTypes": NotRequired[Sequence[str]],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "TimeSeriesSelector": NotRequired[TimeSeriesSelectorTypeDef],
    },
)
CreateWhatIfAnalysisRequestRequestTypeDef = TypedDict(
    "CreateWhatIfAnalysisRequestRequestTypeDef",
    {
        "WhatIfAnalysisName": str,
        "ForecastArn": str,
        "TimeSeriesSelector": NotRequired[TimeSeriesSelectorTypeDef],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
DescribeForecastResponseTypeDef = TypedDict(
    "DescribeForecastResponseTypeDef",
    {
        "ForecastArn": str,
        "ForecastName": str,
        "ForecastTypes": List[str],
        "PredictorArn": str,
        "DatasetGroupArn": str,
        "EstimatedTimeRemainingInMinutes": int,
        "Status": str,
        "Message": str,
        "CreationTime": datetime,
        "LastModificationTime": datetime,
        "TimeSeriesSelector": TimeSeriesSelectorTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeWhatIfAnalysisResponseTypeDef = TypedDict(
    "DescribeWhatIfAnalysisResponseTypeDef",
    {
        "WhatIfAnalysisName": str,
        "WhatIfAnalysisArn": str,
        "ForecastArn": str,
        "EstimatedTimeRemainingInMinutes": int,
        "Status": str,
        "Message": str,
        "CreationTime": datetime,
        "LastModificationTime": datetime,
        "TimeSeriesSelector": TimeSeriesSelectorTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
