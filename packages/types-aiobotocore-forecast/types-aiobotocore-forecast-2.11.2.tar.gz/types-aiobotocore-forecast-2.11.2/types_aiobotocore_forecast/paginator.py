"""
Type annotations for forecast service client paginators.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/paginators/)

Usage::

    ```python
    from aiobotocore.session import get_session

    from types_aiobotocore_forecast.client import ForecastServiceClient
    from types_aiobotocore_forecast.paginator import (
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

    session = get_session()
    with session.create_client("forecast") as client:
        client: ForecastServiceClient

        list_dataset_groups_paginator: ListDatasetGroupsPaginator = client.get_paginator("list_dataset_groups")
        list_dataset_import_jobs_paginator: ListDatasetImportJobsPaginator = client.get_paginator("list_dataset_import_jobs")
        list_datasets_paginator: ListDatasetsPaginator = client.get_paginator("list_datasets")
        list_explainabilities_paginator: ListExplainabilitiesPaginator = client.get_paginator("list_explainabilities")
        list_explainability_exports_paginator: ListExplainabilityExportsPaginator = client.get_paginator("list_explainability_exports")
        list_forecast_export_jobs_paginator: ListForecastExportJobsPaginator = client.get_paginator("list_forecast_export_jobs")
        list_forecasts_paginator: ListForecastsPaginator = client.get_paginator("list_forecasts")
        list_monitor_evaluations_paginator: ListMonitorEvaluationsPaginator = client.get_paginator("list_monitor_evaluations")
        list_monitors_paginator: ListMonitorsPaginator = client.get_paginator("list_monitors")
        list_predictor_backtest_export_jobs_paginator: ListPredictorBacktestExportJobsPaginator = client.get_paginator("list_predictor_backtest_export_jobs")
        list_predictors_paginator: ListPredictorsPaginator = client.get_paginator("list_predictors")
        list_what_if_analyses_paginator: ListWhatIfAnalysesPaginator = client.get_paginator("list_what_if_analyses")
        list_what_if_forecast_exports_paginator: ListWhatIfForecastExportsPaginator = client.get_paginator("list_what_if_forecast_exports")
        list_what_if_forecasts_paginator: ListWhatIfForecastsPaginator = client.get_paginator("list_what_if_forecasts")
    ```
"""

from typing import AsyncIterator, Generic, Iterator, Sequence, TypeVar

from aiobotocore.paginate import AioPaginator
from botocore.paginate import PageIterator

from .type_defs import (
    FilterTypeDef,
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
    ListWhatIfAnalysesResponseTypeDef,
    ListWhatIfForecastExportsResponseTypeDef,
    ListWhatIfForecastsResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "ListDatasetGroupsPaginator",
    "ListDatasetImportJobsPaginator",
    "ListDatasetsPaginator",
    "ListExplainabilitiesPaginator",
    "ListExplainabilityExportsPaginator",
    "ListForecastExportJobsPaginator",
    "ListForecastsPaginator",
    "ListMonitorEvaluationsPaginator",
    "ListMonitorsPaginator",
    "ListPredictorBacktestExportJobsPaginator",
    "ListPredictorsPaginator",
    "ListWhatIfAnalysesPaginator",
    "ListWhatIfForecastExportsPaginator",
    "ListWhatIfForecastsPaginator",
)

_ItemTypeDef = TypeVar("_ItemTypeDef")


class _PageIterator(Generic[_ItemTypeDef], PageIterator):
    def __iter__(self) -> Iterator[_ItemTypeDef]:
        """
        Proxy method to specify iterator item type.
        """


class ListDatasetGroupsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Paginator.ListDatasetGroups)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/paginators/#listdatasetgroupspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListDatasetGroupsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Paginator.ListDatasetGroups.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/paginators/#listdatasetgroupspaginator)
        """


class ListDatasetImportJobsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Paginator.ListDatasetImportJobs)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/paginators/#listdatasetimportjobspaginator)
    """

    def paginate(
        self,
        *,
        Filters: Sequence[FilterTypeDef] = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListDatasetImportJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Paginator.ListDatasetImportJobs.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/paginators/#listdatasetimportjobspaginator)
        """


class ListDatasetsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Paginator.ListDatasets)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/paginators/#listdatasetspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListDatasetsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Paginator.ListDatasets.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/paginators/#listdatasetspaginator)
        """


class ListExplainabilitiesPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Paginator.ListExplainabilities)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/paginators/#listexplainabilitiespaginator)
    """

    def paginate(
        self,
        *,
        Filters: Sequence[FilterTypeDef] = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListExplainabilitiesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Paginator.ListExplainabilities.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/paginators/#listexplainabilitiespaginator)
        """


class ListExplainabilityExportsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Paginator.ListExplainabilityExports)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/paginators/#listexplainabilityexportspaginator)
    """

    def paginate(
        self,
        *,
        Filters: Sequence[FilterTypeDef] = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListExplainabilityExportsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Paginator.ListExplainabilityExports.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/paginators/#listexplainabilityexportspaginator)
        """


class ListForecastExportJobsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Paginator.ListForecastExportJobs)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/paginators/#listforecastexportjobspaginator)
    """

    def paginate(
        self,
        *,
        Filters: Sequence[FilterTypeDef] = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListForecastExportJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Paginator.ListForecastExportJobs.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/paginators/#listforecastexportjobspaginator)
        """


class ListForecastsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Paginator.ListForecasts)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/paginators/#listforecastspaginator)
    """

    def paginate(
        self,
        *,
        Filters: Sequence[FilterTypeDef] = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListForecastsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Paginator.ListForecasts.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/paginators/#listforecastspaginator)
        """


class ListMonitorEvaluationsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Paginator.ListMonitorEvaluations)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/paginators/#listmonitorevaluationspaginator)
    """

    def paginate(
        self,
        *,
        MonitorArn: str,
        Filters: Sequence[FilterTypeDef] = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListMonitorEvaluationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Paginator.ListMonitorEvaluations.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/paginators/#listmonitorevaluationspaginator)
        """


class ListMonitorsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Paginator.ListMonitors)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/paginators/#listmonitorspaginator)
    """

    def paginate(
        self,
        *,
        Filters: Sequence[FilterTypeDef] = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListMonitorsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Paginator.ListMonitors.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/paginators/#listmonitorspaginator)
        """


class ListPredictorBacktestExportJobsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Paginator.ListPredictorBacktestExportJobs)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/paginators/#listpredictorbacktestexportjobspaginator)
    """

    def paginate(
        self,
        *,
        Filters: Sequence[FilterTypeDef] = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListPredictorBacktestExportJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Paginator.ListPredictorBacktestExportJobs.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/paginators/#listpredictorbacktestexportjobspaginator)
        """


class ListPredictorsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Paginator.ListPredictors)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/paginators/#listpredictorspaginator)
    """

    def paginate(
        self,
        *,
        Filters: Sequence[FilterTypeDef] = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListPredictorsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Paginator.ListPredictors.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/paginators/#listpredictorspaginator)
        """


class ListWhatIfAnalysesPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Paginator.ListWhatIfAnalyses)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/paginators/#listwhatifanalysespaginator)
    """

    def paginate(
        self,
        *,
        Filters: Sequence[FilterTypeDef] = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListWhatIfAnalysesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Paginator.ListWhatIfAnalyses.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/paginators/#listwhatifanalysespaginator)
        """


class ListWhatIfForecastExportsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Paginator.ListWhatIfForecastExports)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/paginators/#listwhatifforecastexportspaginator)
    """

    def paginate(
        self,
        *,
        Filters: Sequence[FilterTypeDef] = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListWhatIfForecastExportsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Paginator.ListWhatIfForecastExports.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/paginators/#listwhatifforecastexportspaginator)
        """


class ListWhatIfForecastsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Paginator.ListWhatIfForecasts)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/paginators/#listwhatifforecastspaginator)
    """

    def paginate(
        self,
        *,
        Filters: Sequence[FilterTypeDef] = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListWhatIfForecastsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Paginator.ListWhatIfForecasts.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_forecast/paginators/#listwhatifforecastspaginator)
        """
