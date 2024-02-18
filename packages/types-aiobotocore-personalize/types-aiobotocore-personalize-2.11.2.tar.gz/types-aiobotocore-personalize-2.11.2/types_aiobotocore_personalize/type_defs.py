"""
Type annotations for personalize service type definitions.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_personalize/type_defs/)

Usage::

    ```python
    from types_aiobotocore_personalize.type_defs import AlgorithmImageTypeDef

    data: AlgorithmImageTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from .literals import (
    BatchInferenceJobModeType,
    DomainType,
    ImportModeType,
    IngestionModeType,
    ObjectiveSensitivityType,
    TrainingModeType,
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
    "AlgorithmImageTypeDef",
    "AutoMLConfigTypeDef",
    "AutoMLResultTypeDef",
    "BatchInferenceJobConfigTypeDef",
    "S3DataConfigTypeDef",
    "BatchInferenceJobSummaryTypeDef",
    "BatchSegmentJobSummaryTypeDef",
    "CampaignConfigTypeDef",
    "CampaignSummaryTypeDef",
    "CategoricalHyperParameterRangeTypeDef",
    "ContinuousHyperParameterRangeTypeDef",
    "TagTypeDef",
    "ResponseMetadataTypeDef",
    "DataSourceTypeDef",
    "MetricAttributeTypeDef",
    "CreateSchemaRequestRequestTypeDef",
    "DatasetExportJobSummaryTypeDef",
    "DatasetGroupSummaryTypeDef",
    "DatasetGroupTypeDef",
    "DatasetImportJobSummaryTypeDef",
    "DatasetSchemaSummaryTypeDef",
    "DatasetSchemaTypeDef",
    "DatasetSummaryTypeDef",
    "DatasetUpdateSummaryTypeDef",
    "DefaultCategoricalHyperParameterRangeTypeDef",
    "DefaultContinuousHyperParameterRangeTypeDef",
    "DefaultIntegerHyperParameterRangeTypeDef",
    "DeleteCampaignRequestRequestTypeDef",
    "DeleteDatasetGroupRequestRequestTypeDef",
    "DeleteDatasetRequestRequestTypeDef",
    "DeleteEventTrackerRequestRequestTypeDef",
    "DeleteFilterRequestRequestTypeDef",
    "DeleteMetricAttributionRequestRequestTypeDef",
    "DeleteRecommenderRequestRequestTypeDef",
    "DeleteSchemaRequestRequestTypeDef",
    "DeleteSolutionRequestRequestTypeDef",
    "DescribeAlgorithmRequestRequestTypeDef",
    "DescribeBatchInferenceJobRequestRequestTypeDef",
    "DescribeBatchSegmentJobRequestRequestTypeDef",
    "DescribeCampaignRequestRequestTypeDef",
    "DescribeDatasetExportJobRequestRequestTypeDef",
    "DescribeDatasetGroupRequestRequestTypeDef",
    "DescribeDatasetImportJobRequestRequestTypeDef",
    "DescribeDatasetRequestRequestTypeDef",
    "DescribeEventTrackerRequestRequestTypeDef",
    "EventTrackerTypeDef",
    "DescribeFeatureTransformationRequestRequestTypeDef",
    "FeatureTransformationTypeDef",
    "DescribeFilterRequestRequestTypeDef",
    "FilterTypeDef",
    "DescribeMetricAttributionRequestRequestTypeDef",
    "DescribeRecipeRequestRequestTypeDef",
    "RecipeTypeDef",
    "DescribeRecommenderRequestRequestTypeDef",
    "DescribeSchemaRequestRequestTypeDef",
    "DescribeSolutionRequestRequestTypeDef",
    "DescribeSolutionVersionRequestRequestTypeDef",
    "EventTrackerSummaryTypeDef",
    "FieldsForThemeGenerationTypeDef",
    "FilterSummaryTypeDef",
    "GetSolutionMetricsRequestRequestTypeDef",
    "HPOObjectiveTypeDef",
    "HPOResourceConfigTypeDef",
    "IntegerHyperParameterRangeTypeDef",
    "PaginatorConfigTypeDef",
    "ListBatchInferenceJobsRequestRequestTypeDef",
    "ListBatchSegmentJobsRequestRequestTypeDef",
    "ListCampaignsRequestRequestTypeDef",
    "ListDatasetExportJobsRequestRequestTypeDef",
    "ListDatasetGroupsRequestRequestTypeDef",
    "ListDatasetImportJobsRequestRequestTypeDef",
    "ListDatasetsRequestRequestTypeDef",
    "ListEventTrackersRequestRequestTypeDef",
    "ListFiltersRequestRequestTypeDef",
    "ListMetricAttributionMetricsRequestRequestTypeDef",
    "ListMetricAttributionsRequestRequestTypeDef",
    "MetricAttributionSummaryTypeDef",
    "ListRecipesRequestRequestTypeDef",
    "RecipeSummaryTypeDef",
    "ListRecommendersRequestRequestTypeDef",
    "ListSchemasRequestRequestTypeDef",
    "ListSolutionVersionsRequestRequestTypeDef",
    "SolutionVersionSummaryTypeDef",
    "ListSolutionsRequestRequestTypeDef",
    "SolutionSummaryTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "OptimizationObjectiveTypeDef",
    "TrainingDataConfigPaginatorTypeDef",
    "TrainingDataConfigTypeDef",
    "TunedHPOParamsTypeDef",
    "StartRecommenderRequestRequestTypeDef",
    "StopRecommenderRequestRequestTypeDef",
    "StopSolutionVersionCreationRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateDatasetRequestRequestTypeDef",
    "BatchInferenceJobInputTypeDef",
    "BatchInferenceJobOutputTypeDef",
    "BatchSegmentJobInputTypeDef",
    "BatchSegmentJobOutputTypeDef",
    "DatasetExportJobOutputTypeDef",
    "MetricAttributionOutputTypeDef",
    "CampaignUpdateSummaryTypeDef",
    "UpdateCampaignRequestRequestTypeDef",
    "CreateCampaignRequestRequestTypeDef",
    "CreateDatasetGroupRequestRequestTypeDef",
    "CreateDatasetRequestRequestTypeDef",
    "CreateEventTrackerRequestRequestTypeDef",
    "CreateFilterRequestRequestTypeDef",
    "CreateSolutionVersionRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "CreateBatchInferenceJobResponseTypeDef",
    "CreateBatchSegmentJobResponseTypeDef",
    "CreateCampaignResponseTypeDef",
    "CreateDatasetExportJobResponseTypeDef",
    "CreateDatasetGroupResponseTypeDef",
    "CreateDatasetImportJobResponseTypeDef",
    "CreateDatasetResponseTypeDef",
    "CreateEventTrackerResponseTypeDef",
    "CreateFilterResponseTypeDef",
    "CreateMetricAttributionResponseTypeDef",
    "CreateRecommenderResponseTypeDef",
    "CreateSchemaResponseTypeDef",
    "CreateSolutionResponseTypeDef",
    "CreateSolutionVersionResponseTypeDef",
    "EmptyResponseMetadataTypeDef",
    "GetSolutionMetricsResponseTypeDef",
    "ListBatchInferenceJobsResponseTypeDef",
    "ListBatchSegmentJobsResponseTypeDef",
    "ListCampaignsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "StartRecommenderResponseTypeDef",
    "StopRecommenderResponseTypeDef",
    "UpdateCampaignResponseTypeDef",
    "UpdateDatasetResponseTypeDef",
    "UpdateMetricAttributionResponseTypeDef",
    "UpdateRecommenderResponseTypeDef",
    "CreateDatasetImportJobRequestRequestTypeDef",
    "DatasetImportJobTypeDef",
    "ListMetricAttributionMetricsResponseTypeDef",
    "ListDatasetExportJobsResponseTypeDef",
    "ListDatasetGroupsResponseTypeDef",
    "DescribeDatasetGroupResponseTypeDef",
    "ListDatasetImportJobsResponseTypeDef",
    "ListSchemasResponseTypeDef",
    "DescribeSchemaResponseTypeDef",
    "ListDatasetsResponseTypeDef",
    "DatasetTypeDef",
    "DefaultHyperParameterRangesTypeDef",
    "DescribeEventTrackerResponseTypeDef",
    "DescribeFeatureTransformationResponseTypeDef",
    "DescribeFilterResponseTypeDef",
    "DescribeRecipeResponseTypeDef",
    "ListEventTrackersResponseTypeDef",
    "ThemeGenerationConfigTypeDef",
    "ListFiltersResponseTypeDef",
    "HyperParameterRangesTypeDef",
    "ListBatchInferenceJobsRequestListBatchInferenceJobsPaginateTypeDef",
    "ListBatchSegmentJobsRequestListBatchSegmentJobsPaginateTypeDef",
    "ListCampaignsRequestListCampaignsPaginateTypeDef",
    "ListDatasetExportJobsRequestListDatasetExportJobsPaginateTypeDef",
    "ListDatasetGroupsRequestListDatasetGroupsPaginateTypeDef",
    "ListDatasetImportJobsRequestListDatasetImportJobsPaginateTypeDef",
    "ListDatasetsRequestListDatasetsPaginateTypeDef",
    "ListEventTrackersRequestListEventTrackersPaginateTypeDef",
    "ListFiltersRequestListFiltersPaginateTypeDef",
    "ListMetricAttributionMetricsRequestListMetricAttributionMetricsPaginateTypeDef",
    "ListMetricAttributionsRequestListMetricAttributionsPaginateTypeDef",
    "ListRecipesRequestListRecipesPaginateTypeDef",
    "ListRecommendersRequestListRecommendersPaginateTypeDef",
    "ListSchemasRequestListSchemasPaginateTypeDef",
    "ListSolutionVersionsRequestListSolutionVersionsPaginateTypeDef",
    "ListSolutionsRequestListSolutionsPaginateTypeDef",
    "ListMetricAttributionsResponseTypeDef",
    "ListRecipesResponseTypeDef",
    "ListSolutionVersionsResponseTypeDef",
    "ListSolutionsResponseTypeDef",
    "RecommenderConfigPaginatorTypeDef",
    "RecommenderConfigTypeDef",
    "BatchSegmentJobTypeDef",
    "CreateBatchSegmentJobRequestRequestTypeDef",
    "CreateDatasetExportJobRequestRequestTypeDef",
    "DatasetExportJobTypeDef",
    "CreateMetricAttributionRequestRequestTypeDef",
    "MetricAttributionTypeDef",
    "UpdateMetricAttributionRequestRequestTypeDef",
    "CampaignTypeDef",
    "DescribeDatasetImportJobResponseTypeDef",
    "DescribeDatasetResponseTypeDef",
    "AlgorithmTypeDef",
    "BatchInferenceJobTypeDef",
    "CreateBatchInferenceJobRequestRequestTypeDef",
    "HPOConfigTypeDef",
    "RecommenderSummaryPaginatorTypeDef",
    "CreateRecommenderRequestRequestTypeDef",
    "RecommenderSummaryTypeDef",
    "RecommenderUpdateSummaryTypeDef",
    "UpdateRecommenderRequestRequestTypeDef",
    "DescribeBatchSegmentJobResponseTypeDef",
    "DescribeDatasetExportJobResponseTypeDef",
    "DescribeMetricAttributionResponseTypeDef",
    "DescribeCampaignResponseTypeDef",
    "DescribeAlgorithmResponseTypeDef",
    "DescribeBatchInferenceJobResponseTypeDef",
    "SolutionConfigTypeDef",
    "ListRecommendersResponsePaginatorTypeDef",
    "ListRecommendersResponseTypeDef",
    "RecommenderTypeDef",
    "CreateSolutionRequestRequestTypeDef",
    "SolutionTypeDef",
    "SolutionVersionTypeDef",
    "DescribeRecommenderResponseTypeDef",
    "DescribeSolutionResponseTypeDef",
    "DescribeSolutionVersionResponseTypeDef",
)

AlgorithmImageTypeDef = TypedDict(
    "AlgorithmImageTypeDef",
    {
        "dockerURI": str,
        "name": NotRequired[str],
    },
)
AutoMLConfigTypeDef = TypedDict(
    "AutoMLConfigTypeDef",
    {
        "metricName": NotRequired[str],
        "recipeList": NotRequired[Sequence[str]],
    },
)
AutoMLResultTypeDef = TypedDict(
    "AutoMLResultTypeDef",
    {
        "bestRecipeArn": NotRequired[str],
    },
)
BatchInferenceJobConfigTypeDef = TypedDict(
    "BatchInferenceJobConfigTypeDef",
    {
        "itemExplorationConfig": NotRequired[Mapping[str, str]],
    },
)
S3DataConfigTypeDef = TypedDict(
    "S3DataConfigTypeDef",
    {
        "path": str,
        "kmsKeyArn": NotRequired[str],
    },
)
BatchInferenceJobSummaryTypeDef = TypedDict(
    "BatchInferenceJobSummaryTypeDef",
    {
        "batchInferenceJobArn": NotRequired[str],
        "jobName": NotRequired[str],
        "status": NotRequired[str],
        "creationDateTime": NotRequired[datetime],
        "lastUpdatedDateTime": NotRequired[datetime],
        "failureReason": NotRequired[str],
        "solutionVersionArn": NotRequired[str],
        "batchInferenceJobMode": NotRequired[BatchInferenceJobModeType],
    },
)
BatchSegmentJobSummaryTypeDef = TypedDict(
    "BatchSegmentJobSummaryTypeDef",
    {
        "batchSegmentJobArn": NotRequired[str],
        "jobName": NotRequired[str],
        "status": NotRequired[str],
        "creationDateTime": NotRequired[datetime],
        "lastUpdatedDateTime": NotRequired[datetime],
        "failureReason": NotRequired[str],
        "solutionVersionArn": NotRequired[str],
    },
)
CampaignConfigTypeDef = TypedDict(
    "CampaignConfigTypeDef",
    {
        "itemExplorationConfig": NotRequired[Mapping[str, str]],
        "enableMetadataWithRecommendations": NotRequired[bool],
    },
)
CampaignSummaryTypeDef = TypedDict(
    "CampaignSummaryTypeDef",
    {
        "name": NotRequired[str],
        "campaignArn": NotRequired[str],
        "status": NotRequired[str],
        "creationDateTime": NotRequired[datetime],
        "lastUpdatedDateTime": NotRequired[datetime],
        "failureReason": NotRequired[str],
    },
)
CategoricalHyperParameterRangeTypeDef = TypedDict(
    "CategoricalHyperParameterRangeTypeDef",
    {
        "name": NotRequired[str],
        "values": NotRequired[Sequence[str]],
    },
)
ContinuousHyperParameterRangeTypeDef = TypedDict(
    "ContinuousHyperParameterRangeTypeDef",
    {
        "name": NotRequired[str],
        "minValue": NotRequired[float],
        "maxValue": NotRequired[float],
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "tagKey": str,
        "tagValue": str,
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
DataSourceTypeDef = TypedDict(
    "DataSourceTypeDef",
    {
        "dataLocation": NotRequired[str],
    },
)
MetricAttributeTypeDef = TypedDict(
    "MetricAttributeTypeDef",
    {
        "eventType": str,
        "metricName": str,
        "expression": str,
    },
)
CreateSchemaRequestRequestTypeDef = TypedDict(
    "CreateSchemaRequestRequestTypeDef",
    {
        "name": str,
        "schema": str,
        "domain": NotRequired[DomainType],
    },
)
DatasetExportJobSummaryTypeDef = TypedDict(
    "DatasetExportJobSummaryTypeDef",
    {
        "datasetExportJobArn": NotRequired[str],
        "jobName": NotRequired[str],
        "status": NotRequired[str],
        "creationDateTime": NotRequired[datetime],
        "lastUpdatedDateTime": NotRequired[datetime],
        "failureReason": NotRequired[str],
    },
)
DatasetGroupSummaryTypeDef = TypedDict(
    "DatasetGroupSummaryTypeDef",
    {
        "name": NotRequired[str],
        "datasetGroupArn": NotRequired[str],
        "status": NotRequired[str],
        "creationDateTime": NotRequired[datetime],
        "lastUpdatedDateTime": NotRequired[datetime],
        "failureReason": NotRequired[str],
        "domain": NotRequired[DomainType],
    },
)
DatasetGroupTypeDef = TypedDict(
    "DatasetGroupTypeDef",
    {
        "name": NotRequired[str],
        "datasetGroupArn": NotRequired[str],
        "status": NotRequired[str],
        "roleArn": NotRequired[str],
        "kmsKeyArn": NotRequired[str],
        "creationDateTime": NotRequired[datetime],
        "lastUpdatedDateTime": NotRequired[datetime],
        "failureReason": NotRequired[str],
        "domain": NotRequired[DomainType],
    },
)
DatasetImportJobSummaryTypeDef = TypedDict(
    "DatasetImportJobSummaryTypeDef",
    {
        "datasetImportJobArn": NotRequired[str],
        "jobName": NotRequired[str],
        "status": NotRequired[str],
        "creationDateTime": NotRequired[datetime],
        "lastUpdatedDateTime": NotRequired[datetime],
        "failureReason": NotRequired[str],
        "importMode": NotRequired[ImportModeType],
    },
)
DatasetSchemaSummaryTypeDef = TypedDict(
    "DatasetSchemaSummaryTypeDef",
    {
        "name": NotRequired[str],
        "schemaArn": NotRequired[str],
        "creationDateTime": NotRequired[datetime],
        "lastUpdatedDateTime": NotRequired[datetime],
        "domain": NotRequired[DomainType],
    },
)
DatasetSchemaTypeDef = TypedDict(
    "DatasetSchemaTypeDef",
    {
        "name": NotRequired[str],
        "schemaArn": NotRequired[str],
        "schema": NotRequired[str],
        "creationDateTime": NotRequired[datetime],
        "lastUpdatedDateTime": NotRequired[datetime],
        "domain": NotRequired[DomainType],
    },
)
DatasetSummaryTypeDef = TypedDict(
    "DatasetSummaryTypeDef",
    {
        "name": NotRequired[str],
        "datasetArn": NotRequired[str],
        "datasetType": NotRequired[str],
        "status": NotRequired[str],
        "creationDateTime": NotRequired[datetime],
        "lastUpdatedDateTime": NotRequired[datetime],
    },
)
DatasetUpdateSummaryTypeDef = TypedDict(
    "DatasetUpdateSummaryTypeDef",
    {
        "schemaArn": NotRequired[str],
        "status": NotRequired[str],
        "failureReason": NotRequired[str],
        "creationDateTime": NotRequired[datetime],
        "lastUpdatedDateTime": NotRequired[datetime],
    },
)
DefaultCategoricalHyperParameterRangeTypeDef = TypedDict(
    "DefaultCategoricalHyperParameterRangeTypeDef",
    {
        "name": NotRequired[str],
        "values": NotRequired[List[str]],
        "isTunable": NotRequired[bool],
    },
)
DefaultContinuousHyperParameterRangeTypeDef = TypedDict(
    "DefaultContinuousHyperParameterRangeTypeDef",
    {
        "name": NotRequired[str],
        "minValue": NotRequired[float],
        "maxValue": NotRequired[float],
        "isTunable": NotRequired[bool],
    },
)
DefaultIntegerHyperParameterRangeTypeDef = TypedDict(
    "DefaultIntegerHyperParameterRangeTypeDef",
    {
        "name": NotRequired[str],
        "minValue": NotRequired[int],
        "maxValue": NotRequired[int],
        "isTunable": NotRequired[bool],
    },
)
DeleteCampaignRequestRequestTypeDef = TypedDict(
    "DeleteCampaignRequestRequestTypeDef",
    {
        "campaignArn": str,
    },
)
DeleteDatasetGroupRequestRequestTypeDef = TypedDict(
    "DeleteDatasetGroupRequestRequestTypeDef",
    {
        "datasetGroupArn": str,
    },
)
DeleteDatasetRequestRequestTypeDef = TypedDict(
    "DeleteDatasetRequestRequestTypeDef",
    {
        "datasetArn": str,
    },
)
DeleteEventTrackerRequestRequestTypeDef = TypedDict(
    "DeleteEventTrackerRequestRequestTypeDef",
    {
        "eventTrackerArn": str,
    },
)
DeleteFilterRequestRequestTypeDef = TypedDict(
    "DeleteFilterRequestRequestTypeDef",
    {
        "filterArn": str,
    },
)
DeleteMetricAttributionRequestRequestTypeDef = TypedDict(
    "DeleteMetricAttributionRequestRequestTypeDef",
    {
        "metricAttributionArn": str,
    },
)
DeleteRecommenderRequestRequestTypeDef = TypedDict(
    "DeleteRecommenderRequestRequestTypeDef",
    {
        "recommenderArn": str,
    },
)
DeleteSchemaRequestRequestTypeDef = TypedDict(
    "DeleteSchemaRequestRequestTypeDef",
    {
        "schemaArn": str,
    },
)
DeleteSolutionRequestRequestTypeDef = TypedDict(
    "DeleteSolutionRequestRequestTypeDef",
    {
        "solutionArn": str,
    },
)
DescribeAlgorithmRequestRequestTypeDef = TypedDict(
    "DescribeAlgorithmRequestRequestTypeDef",
    {
        "algorithmArn": str,
    },
)
DescribeBatchInferenceJobRequestRequestTypeDef = TypedDict(
    "DescribeBatchInferenceJobRequestRequestTypeDef",
    {
        "batchInferenceJobArn": str,
    },
)
DescribeBatchSegmentJobRequestRequestTypeDef = TypedDict(
    "DescribeBatchSegmentJobRequestRequestTypeDef",
    {
        "batchSegmentJobArn": str,
    },
)
DescribeCampaignRequestRequestTypeDef = TypedDict(
    "DescribeCampaignRequestRequestTypeDef",
    {
        "campaignArn": str,
    },
)
DescribeDatasetExportJobRequestRequestTypeDef = TypedDict(
    "DescribeDatasetExportJobRequestRequestTypeDef",
    {
        "datasetExportJobArn": str,
    },
)
DescribeDatasetGroupRequestRequestTypeDef = TypedDict(
    "DescribeDatasetGroupRequestRequestTypeDef",
    {
        "datasetGroupArn": str,
    },
)
DescribeDatasetImportJobRequestRequestTypeDef = TypedDict(
    "DescribeDatasetImportJobRequestRequestTypeDef",
    {
        "datasetImportJobArn": str,
    },
)
DescribeDatasetRequestRequestTypeDef = TypedDict(
    "DescribeDatasetRequestRequestTypeDef",
    {
        "datasetArn": str,
    },
)
DescribeEventTrackerRequestRequestTypeDef = TypedDict(
    "DescribeEventTrackerRequestRequestTypeDef",
    {
        "eventTrackerArn": str,
    },
)
EventTrackerTypeDef = TypedDict(
    "EventTrackerTypeDef",
    {
        "name": NotRequired[str],
        "eventTrackerArn": NotRequired[str],
        "accountId": NotRequired[str],
        "trackingId": NotRequired[str],
        "datasetGroupArn": NotRequired[str],
        "status": NotRequired[str],
        "creationDateTime": NotRequired[datetime],
        "lastUpdatedDateTime": NotRequired[datetime],
    },
)
DescribeFeatureTransformationRequestRequestTypeDef = TypedDict(
    "DescribeFeatureTransformationRequestRequestTypeDef",
    {
        "featureTransformationArn": str,
    },
)
FeatureTransformationTypeDef = TypedDict(
    "FeatureTransformationTypeDef",
    {
        "name": NotRequired[str],
        "featureTransformationArn": NotRequired[str],
        "defaultParameters": NotRequired[Dict[str, str]],
        "creationDateTime": NotRequired[datetime],
        "lastUpdatedDateTime": NotRequired[datetime],
        "status": NotRequired[str],
    },
)
DescribeFilterRequestRequestTypeDef = TypedDict(
    "DescribeFilterRequestRequestTypeDef",
    {
        "filterArn": str,
    },
)
FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "name": NotRequired[str],
        "filterArn": NotRequired[str],
        "creationDateTime": NotRequired[datetime],
        "lastUpdatedDateTime": NotRequired[datetime],
        "datasetGroupArn": NotRequired[str],
        "failureReason": NotRequired[str],
        "filterExpression": NotRequired[str],
        "status": NotRequired[str],
    },
)
DescribeMetricAttributionRequestRequestTypeDef = TypedDict(
    "DescribeMetricAttributionRequestRequestTypeDef",
    {
        "metricAttributionArn": str,
    },
)
DescribeRecipeRequestRequestTypeDef = TypedDict(
    "DescribeRecipeRequestRequestTypeDef",
    {
        "recipeArn": str,
    },
)
RecipeTypeDef = TypedDict(
    "RecipeTypeDef",
    {
        "name": NotRequired[str],
        "recipeArn": NotRequired[str],
        "algorithmArn": NotRequired[str],
        "featureTransformationArn": NotRequired[str],
        "status": NotRequired[str],
        "description": NotRequired[str],
        "creationDateTime": NotRequired[datetime],
        "recipeType": NotRequired[str],
        "lastUpdatedDateTime": NotRequired[datetime],
    },
)
DescribeRecommenderRequestRequestTypeDef = TypedDict(
    "DescribeRecommenderRequestRequestTypeDef",
    {
        "recommenderArn": str,
    },
)
DescribeSchemaRequestRequestTypeDef = TypedDict(
    "DescribeSchemaRequestRequestTypeDef",
    {
        "schemaArn": str,
    },
)
DescribeSolutionRequestRequestTypeDef = TypedDict(
    "DescribeSolutionRequestRequestTypeDef",
    {
        "solutionArn": str,
    },
)
DescribeSolutionVersionRequestRequestTypeDef = TypedDict(
    "DescribeSolutionVersionRequestRequestTypeDef",
    {
        "solutionVersionArn": str,
    },
)
EventTrackerSummaryTypeDef = TypedDict(
    "EventTrackerSummaryTypeDef",
    {
        "name": NotRequired[str],
        "eventTrackerArn": NotRequired[str],
        "status": NotRequired[str],
        "creationDateTime": NotRequired[datetime],
        "lastUpdatedDateTime": NotRequired[datetime],
    },
)
FieldsForThemeGenerationTypeDef = TypedDict(
    "FieldsForThemeGenerationTypeDef",
    {
        "itemName": str,
    },
)
FilterSummaryTypeDef = TypedDict(
    "FilterSummaryTypeDef",
    {
        "name": NotRequired[str],
        "filterArn": NotRequired[str],
        "creationDateTime": NotRequired[datetime],
        "lastUpdatedDateTime": NotRequired[datetime],
        "datasetGroupArn": NotRequired[str],
        "failureReason": NotRequired[str],
        "status": NotRequired[str],
    },
)
GetSolutionMetricsRequestRequestTypeDef = TypedDict(
    "GetSolutionMetricsRequestRequestTypeDef",
    {
        "solutionVersionArn": str,
    },
)
HPOObjectiveTypeDef = TypedDict(
    "HPOObjectiveTypeDef",
    {
        "type": NotRequired[str],
        "metricName": NotRequired[str],
        "metricRegex": NotRequired[str],
    },
)
HPOResourceConfigTypeDef = TypedDict(
    "HPOResourceConfigTypeDef",
    {
        "maxNumberOfTrainingJobs": NotRequired[str],
        "maxParallelTrainingJobs": NotRequired[str],
    },
)
IntegerHyperParameterRangeTypeDef = TypedDict(
    "IntegerHyperParameterRangeTypeDef",
    {
        "name": NotRequired[str],
        "minValue": NotRequired[int],
        "maxValue": NotRequired[int],
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
ListBatchInferenceJobsRequestRequestTypeDef = TypedDict(
    "ListBatchInferenceJobsRequestRequestTypeDef",
    {
        "solutionVersionArn": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListBatchSegmentJobsRequestRequestTypeDef = TypedDict(
    "ListBatchSegmentJobsRequestRequestTypeDef",
    {
        "solutionVersionArn": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListCampaignsRequestRequestTypeDef = TypedDict(
    "ListCampaignsRequestRequestTypeDef",
    {
        "solutionArn": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListDatasetExportJobsRequestRequestTypeDef = TypedDict(
    "ListDatasetExportJobsRequestRequestTypeDef",
    {
        "datasetArn": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListDatasetGroupsRequestRequestTypeDef = TypedDict(
    "ListDatasetGroupsRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListDatasetImportJobsRequestRequestTypeDef = TypedDict(
    "ListDatasetImportJobsRequestRequestTypeDef",
    {
        "datasetArn": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListDatasetsRequestRequestTypeDef = TypedDict(
    "ListDatasetsRequestRequestTypeDef",
    {
        "datasetGroupArn": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListEventTrackersRequestRequestTypeDef = TypedDict(
    "ListEventTrackersRequestRequestTypeDef",
    {
        "datasetGroupArn": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListFiltersRequestRequestTypeDef = TypedDict(
    "ListFiltersRequestRequestTypeDef",
    {
        "datasetGroupArn": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListMetricAttributionMetricsRequestRequestTypeDef = TypedDict(
    "ListMetricAttributionMetricsRequestRequestTypeDef",
    {
        "metricAttributionArn": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListMetricAttributionsRequestRequestTypeDef = TypedDict(
    "ListMetricAttributionsRequestRequestTypeDef",
    {
        "datasetGroupArn": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
MetricAttributionSummaryTypeDef = TypedDict(
    "MetricAttributionSummaryTypeDef",
    {
        "name": NotRequired[str],
        "metricAttributionArn": NotRequired[str],
        "status": NotRequired[str],
        "creationDateTime": NotRequired[datetime],
        "lastUpdatedDateTime": NotRequired[datetime],
        "failureReason": NotRequired[str],
    },
)
ListRecipesRequestRequestTypeDef = TypedDict(
    "ListRecipesRequestRequestTypeDef",
    {
        "recipeProvider": NotRequired[Literal["SERVICE"]],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "domain": NotRequired[DomainType],
    },
)
RecipeSummaryTypeDef = TypedDict(
    "RecipeSummaryTypeDef",
    {
        "name": NotRequired[str],
        "recipeArn": NotRequired[str],
        "status": NotRequired[str],
        "creationDateTime": NotRequired[datetime],
        "lastUpdatedDateTime": NotRequired[datetime],
        "domain": NotRequired[DomainType],
    },
)
ListRecommendersRequestRequestTypeDef = TypedDict(
    "ListRecommendersRequestRequestTypeDef",
    {
        "datasetGroupArn": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListSchemasRequestRequestTypeDef = TypedDict(
    "ListSchemasRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListSolutionVersionsRequestRequestTypeDef = TypedDict(
    "ListSolutionVersionsRequestRequestTypeDef",
    {
        "solutionArn": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
SolutionVersionSummaryTypeDef = TypedDict(
    "SolutionVersionSummaryTypeDef",
    {
        "solutionVersionArn": NotRequired[str],
        "status": NotRequired[str],
        "creationDateTime": NotRequired[datetime],
        "lastUpdatedDateTime": NotRequired[datetime],
        "failureReason": NotRequired[str],
    },
)
ListSolutionsRequestRequestTypeDef = TypedDict(
    "ListSolutionsRequestRequestTypeDef",
    {
        "datasetGroupArn": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
SolutionSummaryTypeDef = TypedDict(
    "SolutionSummaryTypeDef",
    {
        "name": NotRequired[str],
        "solutionArn": NotRequired[str],
        "status": NotRequired[str],
        "creationDateTime": NotRequired[datetime],
        "lastUpdatedDateTime": NotRequired[datetime],
        "recipeArn": NotRequired[str],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)
OptimizationObjectiveTypeDef = TypedDict(
    "OptimizationObjectiveTypeDef",
    {
        "itemAttribute": NotRequired[str],
        "objectiveSensitivity": NotRequired[ObjectiveSensitivityType],
    },
)
TrainingDataConfigPaginatorTypeDef = TypedDict(
    "TrainingDataConfigPaginatorTypeDef",
    {
        "excludedDatasetColumns": NotRequired[Dict[str, List[str]]],
    },
)
TrainingDataConfigTypeDef = TypedDict(
    "TrainingDataConfigTypeDef",
    {
        "excludedDatasetColumns": NotRequired[Mapping[str, Sequence[str]]],
    },
)
TunedHPOParamsTypeDef = TypedDict(
    "TunedHPOParamsTypeDef",
    {
        "algorithmHyperParameters": NotRequired[Dict[str, str]],
    },
)
StartRecommenderRequestRequestTypeDef = TypedDict(
    "StartRecommenderRequestRequestTypeDef",
    {
        "recommenderArn": str,
    },
)
StopRecommenderRequestRequestTypeDef = TypedDict(
    "StopRecommenderRequestRequestTypeDef",
    {
        "recommenderArn": str,
    },
)
StopSolutionVersionCreationRequestRequestTypeDef = TypedDict(
    "StopSolutionVersionCreationRequestRequestTypeDef",
    {
        "solutionVersionArn": str,
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)
UpdateDatasetRequestRequestTypeDef = TypedDict(
    "UpdateDatasetRequestRequestTypeDef",
    {
        "datasetArn": str,
        "schemaArn": str,
    },
)
BatchInferenceJobInputTypeDef = TypedDict(
    "BatchInferenceJobInputTypeDef",
    {
        "s3DataSource": S3DataConfigTypeDef,
    },
)
BatchInferenceJobOutputTypeDef = TypedDict(
    "BatchInferenceJobOutputTypeDef",
    {
        "s3DataDestination": S3DataConfigTypeDef,
    },
)
BatchSegmentJobInputTypeDef = TypedDict(
    "BatchSegmentJobInputTypeDef",
    {
        "s3DataSource": S3DataConfigTypeDef,
    },
)
BatchSegmentJobOutputTypeDef = TypedDict(
    "BatchSegmentJobOutputTypeDef",
    {
        "s3DataDestination": S3DataConfigTypeDef,
    },
)
DatasetExportJobOutputTypeDef = TypedDict(
    "DatasetExportJobOutputTypeDef",
    {
        "s3DataDestination": S3DataConfigTypeDef,
    },
)
MetricAttributionOutputTypeDef = TypedDict(
    "MetricAttributionOutputTypeDef",
    {
        "roleArn": str,
        "s3DataDestination": NotRequired[S3DataConfigTypeDef],
    },
)
CampaignUpdateSummaryTypeDef = TypedDict(
    "CampaignUpdateSummaryTypeDef",
    {
        "solutionVersionArn": NotRequired[str],
        "minProvisionedTPS": NotRequired[int],
        "campaignConfig": NotRequired[CampaignConfigTypeDef],
        "status": NotRequired[str],
        "failureReason": NotRequired[str],
        "creationDateTime": NotRequired[datetime],
        "lastUpdatedDateTime": NotRequired[datetime],
    },
)
UpdateCampaignRequestRequestTypeDef = TypedDict(
    "UpdateCampaignRequestRequestTypeDef",
    {
        "campaignArn": str,
        "solutionVersionArn": NotRequired[str],
        "minProvisionedTPS": NotRequired[int],
        "campaignConfig": NotRequired[CampaignConfigTypeDef],
    },
)
CreateCampaignRequestRequestTypeDef = TypedDict(
    "CreateCampaignRequestRequestTypeDef",
    {
        "name": str,
        "solutionVersionArn": str,
        "minProvisionedTPS": NotRequired[int],
        "campaignConfig": NotRequired[CampaignConfigTypeDef],
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateDatasetGroupRequestRequestTypeDef = TypedDict(
    "CreateDatasetGroupRequestRequestTypeDef",
    {
        "name": str,
        "roleArn": NotRequired[str],
        "kmsKeyArn": NotRequired[str],
        "domain": NotRequired[DomainType],
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateDatasetRequestRequestTypeDef = TypedDict(
    "CreateDatasetRequestRequestTypeDef",
    {
        "name": str,
        "schemaArn": str,
        "datasetGroupArn": str,
        "datasetType": str,
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateEventTrackerRequestRequestTypeDef = TypedDict(
    "CreateEventTrackerRequestRequestTypeDef",
    {
        "name": str,
        "datasetGroupArn": str,
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateFilterRequestRequestTypeDef = TypedDict(
    "CreateFilterRequestRequestTypeDef",
    {
        "name": str,
        "datasetGroupArn": str,
        "filterExpression": str,
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateSolutionVersionRequestRequestTypeDef = TypedDict(
    "CreateSolutionVersionRequestRequestTypeDef",
    {
        "solutionArn": str,
        "name": NotRequired[str],
        "trainingMode": NotRequired[TrainingModeType],
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Sequence[TagTypeDef],
    },
)
CreateBatchInferenceJobResponseTypeDef = TypedDict(
    "CreateBatchInferenceJobResponseTypeDef",
    {
        "batchInferenceJobArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateBatchSegmentJobResponseTypeDef = TypedDict(
    "CreateBatchSegmentJobResponseTypeDef",
    {
        "batchSegmentJobArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateCampaignResponseTypeDef = TypedDict(
    "CreateCampaignResponseTypeDef",
    {
        "campaignArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDatasetExportJobResponseTypeDef = TypedDict(
    "CreateDatasetExportJobResponseTypeDef",
    {
        "datasetExportJobArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDatasetGroupResponseTypeDef = TypedDict(
    "CreateDatasetGroupResponseTypeDef",
    {
        "datasetGroupArn": str,
        "domain": DomainType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDatasetImportJobResponseTypeDef = TypedDict(
    "CreateDatasetImportJobResponseTypeDef",
    {
        "datasetImportJobArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDatasetResponseTypeDef = TypedDict(
    "CreateDatasetResponseTypeDef",
    {
        "datasetArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateEventTrackerResponseTypeDef = TypedDict(
    "CreateEventTrackerResponseTypeDef",
    {
        "eventTrackerArn": str,
        "trackingId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateFilterResponseTypeDef = TypedDict(
    "CreateFilterResponseTypeDef",
    {
        "filterArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateMetricAttributionResponseTypeDef = TypedDict(
    "CreateMetricAttributionResponseTypeDef",
    {
        "metricAttributionArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateRecommenderResponseTypeDef = TypedDict(
    "CreateRecommenderResponseTypeDef",
    {
        "recommenderArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateSchemaResponseTypeDef = TypedDict(
    "CreateSchemaResponseTypeDef",
    {
        "schemaArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateSolutionResponseTypeDef = TypedDict(
    "CreateSolutionResponseTypeDef",
    {
        "solutionArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateSolutionVersionResponseTypeDef = TypedDict(
    "CreateSolutionVersionResponseTypeDef",
    {
        "solutionVersionArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSolutionMetricsResponseTypeDef = TypedDict(
    "GetSolutionMetricsResponseTypeDef",
    {
        "solutionVersionArn": str,
        "metrics": Dict[str, float],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListBatchInferenceJobsResponseTypeDef = TypedDict(
    "ListBatchInferenceJobsResponseTypeDef",
    {
        "batchInferenceJobs": List[BatchInferenceJobSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListBatchSegmentJobsResponseTypeDef = TypedDict(
    "ListBatchSegmentJobsResponseTypeDef",
    {
        "batchSegmentJobs": List[BatchSegmentJobSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListCampaignsResponseTypeDef = TypedDict(
    "ListCampaignsResponseTypeDef",
    {
        "campaigns": List[CampaignSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartRecommenderResponseTypeDef = TypedDict(
    "StartRecommenderResponseTypeDef",
    {
        "recommenderArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StopRecommenderResponseTypeDef = TypedDict(
    "StopRecommenderResponseTypeDef",
    {
        "recommenderArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateCampaignResponseTypeDef = TypedDict(
    "UpdateCampaignResponseTypeDef",
    {
        "campaignArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateDatasetResponseTypeDef = TypedDict(
    "UpdateDatasetResponseTypeDef",
    {
        "datasetArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateMetricAttributionResponseTypeDef = TypedDict(
    "UpdateMetricAttributionResponseTypeDef",
    {
        "metricAttributionArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateRecommenderResponseTypeDef = TypedDict(
    "UpdateRecommenderResponseTypeDef",
    {
        "recommenderArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDatasetImportJobRequestRequestTypeDef = TypedDict(
    "CreateDatasetImportJobRequestRequestTypeDef",
    {
        "jobName": str,
        "datasetArn": str,
        "dataSource": DataSourceTypeDef,
        "roleArn": str,
        "tags": NotRequired[Sequence[TagTypeDef]],
        "importMode": NotRequired[ImportModeType],
        "publishAttributionMetricsToS3": NotRequired[bool],
    },
)
DatasetImportJobTypeDef = TypedDict(
    "DatasetImportJobTypeDef",
    {
        "jobName": NotRequired[str],
        "datasetImportJobArn": NotRequired[str],
        "datasetArn": NotRequired[str],
        "dataSource": NotRequired[DataSourceTypeDef],
        "roleArn": NotRequired[str],
        "status": NotRequired[str],
        "creationDateTime": NotRequired[datetime],
        "lastUpdatedDateTime": NotRequired[datetime],
        "failureReason": NotRequired[str],
        "importMode": NotRequired[ImportModeType],
        "publishAttributionMetricsToS3": NotRequired[bool],
    },
)
ListMetricAttributionMetricsResponseTypeDef = TypedDict(
    "ListMetricAttributionMetricsResponseTypeDef",
    {
        "metrics": List[MetricAttributeTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListDatasetExportJobsResponseTypeDef = TypedDict(
    "ListDatasetExportJobsResponseTypeDef",
    {
        "datasetExportJobs": List[DatasetExportJobSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListDatasetGroupsResponseTypeDef = TypedDict(
    "ListDatasetGroupsResponseTypeDef",
    {
        "datasetGroups": List[DatasetGroupSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeDatasetGroupResponseTypeDef = TypedDict(
    "DescribeDatasetGroupResponseTypeDef",
    {
        "datasetGroup": DatasetGroupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListDatasetImportJobsResponseTypeDef = TypedDict(
    "ListDatasetImportJobsResponseTypeDef",
    {
        "datasetImportJobs": List[DatasetImportJobSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListSchemasResponseTypeDef = TypedDict(
    "ListSchemasResponseTypeDef",
    {
        "schemas": List[DatasetSchemaSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeSchemaResponseTypeDef = TypedDict(
    "DescribeSchemaResponseTypeDef",
    {
        "schema": DatasetSchemaTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListDatasetsResponseTypeDef = TypedDict(
    "ListDatasetsResponseTypeDef",
    {
        "datasets": List[DatasetSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DatasetTypeDef = TypedDict(
    "DatasetTypeDef",
    {
        "name": NotRequired[str],
        "datasetArn": NotRequired[str],
        "datasetGroupArn": NotRequired[str],
        "datasetType": NotRequired[str],
        "schemaArn": NotRequired[str],
        "status": NotRequired[str],
        "creationDateTime": NotRequired[datetime],
        "lastUpdatedDateTime": NotRequired[datetime],
        "latestDatasetUpdate": NotRequired[DatasetUpdateSummaryTypeDef],
        "trackingId": NotRequired[str],
    },
)
DefaultHyperParameterRangesTypeDef = TypedDict(
    "DefaultHyperParameterRangesTypeDef",
    {
        "integerHyperParameterRanges": NotRequired[List[DefaultIntegerHyperParameterRangeTypeDef]],
        "continuousHyperParameterRanges": NotRequired[
            List[DefaultContinuousHyperParameterRangeTypeDef]
        ],
        "categoricalHyperParameterRanges": NotRequired[
            List[DefaultCategoricalHyperParameterRangeTypeDef]
        ],
    },
)
DescribeEventTrackerResponseTypeDef = TypedDict(
    "DescribeEventTrackerResponseTypeDef",
    {
        "eventTracker": EventTrackerTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeFeatureTransformationResponseTypeDef = TypedDict(
    "DescribeFeatureTransformationResponseTypeDef",
    {
        "featureTransformation": FeatureTransformationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeFilterResponseTypeDef = TypedDict(
    "DescribeFilterResponseTypeDef",
    {
        "filter": FilterTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeRecipeResponseTypeDef = TypedDict(
    "DescribeRecipeResponseTypeDef",
    {
        "recipe": RecipeTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListEventTrackersResponseTypeDef = TypedDict(
    "ListEventTrackersResponseTypeDef",
    {
        "eventTrackers": List[EventTrackerSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ThemeGenerationConfigTypeDef = TypedDict(
    "ThemeGenerationConfigTypeDef",
    {
        "fieldsForThemeGeneration": FieldsForThemeGenerationTypeDef,
    },
)
ListFiltersResponseTypeDef = TypedDict(
    "ListFiltersResponseTypeDef",
    {
        "Filters": List[FilterSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
HyperParameterRangesTypeDef = TypedDict(
    "HyperParameterRangesTypeDef",
    {
        "integerHyperParameterRanges": NotRequired[Sequence[IntegerHyperParameterRangeTypeDef]],
        "continuousHyperParameterRanges": NotRequired[
            Sequence[ContinuousHyperParameterRangeTypeDef]
        ],
        "categoricalHyperParameterRanges": NotRequired[
            Sequence[CategoricalHyperParameterRangeTypeDef]
        ],
    },
)
ListBatchInferenceJobsRequestListBatchInferenceJobsPaginateTypeDef = TypedDict(
    "ListBatchInferenceJobsRequestListBatchInferenceJobsPaginateTypeDef",
    {
        "solutionVersionArn": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListBatchSegmentJobsRequestListBatchSegmentJobsPaginateTypeDef = TypedDict(
    "ListBatchSegmentJobsRequestListBatchSegmentJobsPaginateTypeDef",
    {
        "solutionVersionArn": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListCampaignsRequestListCampaignsPaginateTypeDef = TypedDict(
    "ListCampaignsRequestListCampaignsPaginateTypeDef",
    {
        "solutionArn": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDatasetExportJobsRequestListDatasetExportJobsPaginateTypeDef = TypedDict(
    "ListDatasetExportJobsRequestListDatasetExportJobsPaginateTypeDef",
    {
        "datasetArn": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
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
        "datasetArn": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDatasetsRequestListDatasetsPaginateTypeDef = TypedDict(
    "ListDatasetsRequestListDatasetsPaginateTypeDef",
    {
        "datasetGroupArn": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListEventTrackersRequestListEventTrackersPaginateTypeDef = TypedDict(
    "ListEventTrackersRequestListEventTrackersPaginateTypeDef",
    {
        "datasetGroupArn": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListFiltersRequestListFiltersPaginateTypeDef = TypedDict(
    "ListFiltersRequestListFiltersPaginateTypeDef",
    {
        "datasetGroupArn": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListMetricAttributionMetricsRequestListMetricAttributionMetricsPaginateTypeDef = TypedDict(
    "ListMetricAttributionMetricsRequestListMetricAttributionMetricsPaginateTypeDef",
    {
        "metricAttributionArn": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListMetricAttributionsRequestListMetricAttributionsPaginateTypeDef = TypedDict(
    "ListMetricAttributionsRequestListMetricAttributionsPaginateTypeDef",
    {
        "datasetGroupArn": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListRecipesRequestListRecipesPaginateTypeDef = TypedDict(
    "ListRecipesRequestListRecipesPaginateTypeDef",
    {
        "recipeProvider": NotRequired[Literal["SERVICE"]],
        "domain": NotRequired[DomainType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListRecommendersRequestListRecommendersPaginateTypeDef = TypedDict(
    "ListRecommendersRequestListRecommendersPaginateTypeDef",
    {
        "datasetGroupArn": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListSchemasRequestListSchemasPaginateTypeDef = TypedDict(
    "ListSchemasRequestListSchemasPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListSolutionVersionsRequestListSolutionVersionsPaginateTypeDef = TypedDict(
    "ListSolutionVersionsRequestListSolutionVersionsPaginateTypeDef",
    {
        "solutionArn": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListSolutionsRequestListSolutionsPaginateTypeDef = TypedDict(
    "ListSolutionsRequestListSolutionsPaginateTypeDef",
    {
        "datasetGroupArn": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListMetricAttributionsResponseTypeDef = TypedDict(
    "ListMetricAttributionsResponseTypeDef",
    {
        "metricAttributions": List[MetricAttributionSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListRecipesResponseTypeDef = TypedDict(
    "ListRecipesResponseTypeDef",
    {
        "recipes": List[RecipeSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListSolutionVersionsResponseTypeDef = TypedDict(
    "ListSolutionVersionsResponseTypeDef",
    {
        "solutionVersions": List[SolutionVersionSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListSolutionsResponseTypeDef = TypedDict(
    "ListSolutionsResponseTypeDef",
    {
        "solutions": List[SolutionSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RecommenderConfigPaginatorTypeDef = TypedDict(
    "RecommenderConfigPaginatorTypeDef",
    {
        "itemExplorationConfig": NotRequired[Dict[str, str]],
        "minRecommendationRequestsPerSecond": NotRequired[int],
        "trainingDataConfig": NotRequired[TrainingDataConfigPaginatorTypeDef],
        "enableMetadataWithRecommendations": NotRequired[bool],
    },
)
RecommenderConfigTypeDef = TypedDict(
    "RecommenderConfigTypeDef",
    {
        "itemExplorationConfig": NotRequired[Mapping[str, str]],
        "minRecommendationRequestsPerSecond": NotRequired[int],
        "trainingDataConfig": NotRequired[TrainingDataConfigTypeDef],
        "enableMetadataWithRecommendations": NotRequired[bool],
    },
)
BatchSegmentJobTypeDef = TypedDict(
    "BatchSegmentJobTypeDef",
    {
        "jobName": NotRequired[str],
        "batchSegmentJobArn": NotRequired[str],
        "filterArn": NotRequired[str],
        "failureReason": NotRequired[str],
        "solutionVersionArn": NotRequired[str],
        "numResults": NotRequired[int],
        "jobInput": NotRequired[BatchSegmentJobInputTypeDef],
        "jobOutput": NotRequired[BatchSegmentJobOutputTypeDef],
        "roleArn": NotRequired[str],
        "status": NotRequired[str],
        "creationDateTime": NotRequired[datetime],
        "lastUpdatedDateTime": NotRequired[datetime],
    },
)
CreateBatchSegmentJobRequestRequestTypeDef = TypedDict(
    "CreateBatchSegmentJobRequestRequestTypeDef",
    {
        "jobName": str,
        "solutionVersionArn": str,
        "jobInput": BatchSegmentJobInputTypeDef,
        "jobOutput": BatchSegmentJobOutputTypeDef,
        "roleArn": str,
        "filterArn": NotRequired[str],
        "numResults": NotRequired[int],
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateDatasetExportJobRequestRequestTypeDef = TypedDict(
    "CreateDatasetExportJobRequestRequestTypeDef",
    {
        "jobName": str,
        "datasetArn": str,
        "roleArn": str,
        "jobOutput": DatasetExportJobOutputTypeDef,
        "ingestionMode": NotRequired[IngestionModeType],
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
DatasetExportJobTypeDef = TypedDict(
    "DatasetExportJobTypeDef",
    {
        "jobName": NotRequired[str],
        "datasetExportJobArn": NotRequired[str],
        "datasetArn": NotRequired[str],
        "ingestionMode": NotRequired[IngestionModeType],
        "roleArn": NotRequired[str],
        "status": NotRequired[str],
        "jobOutput": NotRequired[DatasetExportJobOutputTypeDef],
        "creationDateTime": NotRequired[datetime],
        "lastUpdatedDateTime": NotRequired[datetime],
        "failureReason": NotRequired[str],
    },
)
CreateMetricAttributionRequestRequestTypeDef = TypedDict(
    "CreateMetricAttributionRequestRequestTypeDef",
    {
        "name": str,
        "datasetGroupArn": str,
        "metrics": Sequence[MetricAttributeTypeDef],
        "metricsOutputConfig": MetricAttributionOutputTypeDef,
    },
)
MetricAttributionTypeDef = TypedDict(
    "MetricAttributionTypeDef",
    {
        "name": NotRequired[str],
        "metricAttributionArn": NotRequired[str],
        "datasetGroupArn": NotRequired[str],
        "metricsOutputConfig": NotRequired[MetricAttributionOutputTypeDef],
        "status": NotRequired[str],
        "creationDateTime": NotRequired[datetime],
        "lastUpdatedDateTime": NotRequired[datetime],
        "failureReason": NotRequired[str],
    },
)
UpdateMetricAttributionRequestRequestTypeDef = TypedDict(
    "UpdateMetricAttributionRequestRequestTypeDef",
    {
        "addMetrics": NotRequired[Sequence[MetricAttributeTypeDef]],
        "removeMetrics": NotRequired[Sequence[str]],
        "metricsOutputConfig": NotRequired[MetricAttributionOutputTypeDef],
        "metricAttributionArn": NotRequired[str],
    },
)
CampaignTypeDef = TypedDict(
    "CampaignTypeDef",
    {
        "name": NotRequired[str],
        "campaignArn": NotRequired[str],
        "solutionVersionArn": NotRequired[str],
        "minProvisionedTPS": NotRequired[int],
        "campaignConfig": NotRequired[CampaignConfigTypeDef],
        "status": NotRequired[str],
        "failureReason": NotRequired[str],
        "creationDateTime": NotRequired[datetime],
        "lastUpdatedDateTime": NotRequired[datetime],
        "latestCampaignUpdate": NotRequired[CampaignUpdateSummaryTypeDef],
    },
)
DescribeDatasetImportJobResponseTypeDef = TypedDict(
    "DescribeDatasetImportJobResponseTypeDef",
    {
        "datasetImportJob": DatasetImportJobTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeDatasetResponseTypeDef = TypedDict(
    "DescribeDatasetResponseTypeDef",
    {
        "dataset": DatasetTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AlgorithmTypeDef = TypedDict(
    "AlgorithmTypeDef",
    {
        "name": NotRequired[str],
        "algorithmArn": NotRequired[str],
        "algorithmImage": NotRequired[AlgorithmImageTypeDef],
        "defaultHyperParameters": NotRequired[Dict[str, str]],
        "defaultHyperParameterRanges": NotRequired[DefaultHyperParameterRangesTypeDef],
        "defaultResourceConfig": NotRequired[Dict[str, str]],
        "trainingInputMode": NotRequired[str],
        "roleArn": NotRequired[str],
        "creationDateTime": NotRequired[datetime],
        "lastUpdatedDateTime": NotRequired[datetime],
    },
)
BatchInferenceJobTypeDef = TypedDict(
    "BatchInferenceJobTypeDef",
    {
        "jobName": NotRequired[str],
        "batchInferenceJobArn": NotRequired[str],
        "filterArn": NotRequired[str],
        "failureReason": NotRequired[str],
        "solutionVersionArn": NotRequired[str],
        "numResults": NotRequired[int],
        "jobInput": NotRequired[BatchInferenceJobInputTypeDef],
        "jobOutput": NotRequired[BatchInferenceJobOutputTypeDef],
        "batchInferenceJobConfig": NotRequired[BatchInferenceJobConfigTypeDef],
        "roleArn": NotRequired[str],
        "batchInferenceJobMode": NotRequired[BatchInferenceJobModeType],
        "themeGenerationConfig": NotRequired[ThemeGenerationConfigTypeDef],
        "status": NotRequired[str],
        "creationDateTime": NotRequired[datetime],
        "lastUpdatedDateTime": NotRequired[datetime],
    },
)
CreateBatchInferenceJobRequestRequestTypeDef = TypedDict(
    "CreateBatchInferenceJobRequestRequestTypeDef",
    {
        "jobName": str,
        "solutionVersionArn": str,
        "jobInput": BatchInferenceJobInputTypeDef,
        "jobOutput": BatchInferenceJobOutputTypeDef,
        "roleArn": str,
        "filterArn": NotRequired[str],
        "numResults": NotRequired[int],
        "batchInferenceJobConfig": NotRequired[BatchInferenceJobConfigTypeDef],
        "tags": NotRequired[Sequence[TagTypeDef]],
        "batchInferenceJobMode": NotRequired[BatchInferenceJobModeType],
        "themeGenerationConfig": NotRequired[ThemeGenerationConfigTypeDef],
    },
)
HPOConfigTypeDef = TypedDict(
    "HPOConfigTypeDef",
    {
        "hpoObjective": NotRequired[HPOObjectiveTypeDef],
        "hpoResourceConfig": NotRequired[HPOResourceConfigTypeDef],
        "algorithmHyperParameterRanges": NotRequired[HyperParameterRangesTypeDef],
    },
)
RecommenderSummaryPaginatorTypeDef = TypedDict(
    "RecommenderSummaryPaginatorTypeDef",
    {
        "name": NotRequired[str],
        "recommenderArn": NotRequired[str],
        "datasetGroupArn": NotRequired[str],
        "recipeArn": NotRequired[str],
        "recommenderConfig": NotRequired[RecommenderConfigPaginatorTypeDef],
        "status": NotRequired[str],
        "creationDateTime": NotRequired[datetime],
        "lastUpdatedDateTime": NotRequired[datetime],
    },
)
CreateRecommenderRequestRequestTypeDef = TypedDict(
    "CreateRecommenderRequestRequestTypeDef",
    {
        "name": str,
        "datasetGroupArn": str,
        "recipeArn": str,
        "recommenderConfig": NotRequired[RecommenderConfigTypeDef],
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
RecommenderSummaryTypeDef = TypedDict(
    "RecommenderSummaryTypeDef",
    {
        "name": NotRequired[str],
        "recommenderArn": NotRequired[str],
        "datasetGroupArn": NotRequired[str],
        "recipeArn": NotRequired[str],
        "recommenderConfig": NotRequired[RecommenderConfigTypeDef],
        "status": NotRequired[str],
        "creationDateTime": NotRequired[datetime],
        "lastUpdatedDateTime": NotRequired[datetime],
    },
)
RecommenderUpdateSummaryTypeDef = TypedDict(
    "RecommenderUpdateSummaryTypeDef",
    {
        "recommenderConfig": NotRequired[RecommenderConfigTypeDef],
        "creationDateTime": NotRequired[datetime],
        "lastUpdatedDateTime": NotRequired[datetime],
        "status": NotRequired[str],
        "failureReason": NotRequired[str],
    },
)
UpdateRecommenderRequestRequestTypeDef = TypedDict(
    "UpdateRecommenderRequestRequestTypeDef",
    {
        "recommenderArn": str,
        "recommenderConfig": RecommenderConfigTypeDef,
    },
)
DescribeBatchSegmentJobResponseTypeDef = TypedDict(
    "DescribeBatchSegmentJobResponseTypeDef",
    {
        "batchSegmentJob": BatchSegmentJobTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeDatasetExportJobResponseTypeDef = TypedDict(
    "DescribeDatasetExportJobResponseTypeDef",
    {
        "datasetExportJob": DatasetExportJobTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeMetricAttributionResponseTypeDef = TypedDict(
    "DescribeMetricAttributionResponseTypeDef",
    {
        "metricAttribution": MetricAttributionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeCampaignResponseTypeDef = TypedDict(
    "DescribeCampaignResponseTypeDef",
    {
        "campaign": CampaignTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeAlgorithmResponseTypeDef = TypedDict(
    "DescribeAlgorithmResponseTypeDef",
    {
        "algorithm": AlgorithmTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeBatchInferenceJobResponseTypeDef = TypedDict(
    "DescribeBatchInferenceJobResponseTypeDef",
    {
        "batchInferenceJob": BatchInferenceJobTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SolutionConfigTypeDef = TypedDict(
    "SolutionConfigTypeDef",
    {
        "eventValueThreshold": NotRequired[str],
        "hpoConfig": NotRequired[HPOConfigTypeDef],
        "algorithmHyperParameters": NotRequired[Mapping[str, str]],
        "featureTransformationParameters": NotRequired[Mapping[str, str]],
        "autoMLConfig": NotRequired[AutoMLConfigTypeDef],
        "optimizationObjective": NotRequired[OptimizationObjectiveTypeDef],
        "trainingDataConfig": NotRequired[TrainingDataConfigTypeDef],
    },
)
ListRecommendersResponsePaginatorTypeDef = TypedDict(
    "ListRecommendersResponsePaginatorTypeDef",
    {
        "recommenders": List[RecommenderSummaryPaginatorTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListRecommendersResponseTypeDef = TypedDict(
    "ListRecommendersResponseTypeDef",
    {
        "recommenders": List[RecommenderSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RecommenderTypeDef = TypedDict(
    "RecommenderTypeDef",
    {
        "recommenderArn": NotRequired[str],
        "datasetGroupArn": NotRequired[str],
        "name": NotRequired[str],
        "recipeArn": NotRequired[str],
        "recommenderConfig": NotRequired[RecommenderConfigTypeDef],
        "creationDateTime": NotRequired[datetime],
        "lastUpdatedDateTime": NotRequired[datetime],
        "status": NotRequired[str],
        "failureReason": NotRequired[str],
        "latestRecommenderUpdate": NotRequired[RecommenderUpdateSummaryTypeDef],
        "modelMetrics": NotRequired[Dict[str, float]],
    },
)
CreateSolutionRequestRequestTypeDef = TypedDict(
    "CreateSolutionRequestRequestTypeDef",
    {
        "name": str,
        "datasetGroupArn": str,
        "performHPO": NotRequired[bool],
        "performAutoML": NotRequired[bool],
        "recipeArn": NotRequired[str],
        "eventType": NotRequired[str],
        "solutionConfig": NotRequired[SolutionConfigTypeDef],
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
SolutionTypeDef = TypedDict(
    "SolutionTypeDef",
    {
        "name": NotRequired[str],
        "solutionArn": NotRequired[str],
        "performHPO": NotRequired[bool],
        "performAutoML": NotRequired[bool],
        "recipeArn": NotRequired[str],
        "datasetGroupArn": NotRequired[str],
        "eventType": NotRequired[str],
        "solutionConfig": NotRequired[SolutionConfigTypeDef],
        "autoMLResult": NotRequired[AutoMLResultTypeDef],
        "status": NotRequired[str],
        "creationDateTime": NotRequired[datetime],
        "lastUpdatedDateTime": NotRequired[datetime],
        "latestSolutionVersion": NotRequired[SolutionVersionSummaryTypeDef],
    },
)
SolutionVersionTypeDef = TypedDict(
    "SolutionVersionTypeDef",
    {
        "name": NotRequired[str],
        "solutionVersionArn": NotRequired[str],
        "solutionArn": NotRequired[str],
        "performHPO": NotRequired[bool],
        "performAutoML": NotRequired[bool],
        "recipeArn": NotRequired[str],
        "eventType": NotRequired[str],
        "datasetGroupArn": NotRequired[str],
        "solutionConfig": NotRequired[SolutionConfigTypeDef],
        "trainingHours": NotRequired[float],
        "trainingMode": NotRequired[TrainingModeType],
        "tunedHPOParams": NotRequired[TunedHPOParamsTypeDef],
        "status": NotRequired[str],
        "failureReason": NotRequired[str],
        "creationDateTime": NotRequired[datetime],
        "lastUpdatedDateTime": NotRequired[datetime],
    },
)
DescribeRecommenderResponseTypeDef = TypedDict(
    "DescribeRecommenderResponseTypeDef",
    {
        "recommender": RecommenderTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeSolutionResponseTypeDef = TypedDict(
    "DescribeSolutionResponseTypeDef",
    {
        "solution": SolutionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeSolutionVersionResponseTypeDef = TypedDict(
    "DescribeSolutionVersionResponseTypeDef",
    {
        "solutionVersion": SolutionVersionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
