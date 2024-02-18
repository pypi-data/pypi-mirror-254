"""
Type annotations for databrew service type definitions.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_databrew/type_defs/)

Usage::

    ```python
    from types_aiobotocore_databrew.type_defs import AllowedStatisticsTypeDef

    data: AllowedStatisticsTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from .literals import (
    AnalyticsModeType,
    CompressionFormatType,
    EncryptionModeType,
    InputFormatType,
    JobRunStateType,
    JobTypeType,
    LogSubscriptionType,
    OrderType,
    OutputFormatType,
    ParameterTypeType,
    SampleModeType,
    SampleTypeType,
    SessionStatusType,
    SourceType,
    ThresholdTypeType,
    ThresholdUnitType,
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
    "AllowedStatisticsTypeDef",
    "BatchDeleteRecipeVersionRequestRequestTypeDef",
    "RecipeVersionErrorDetailTypeDef",
    "ResponseMetadataTypeDef",
    "ColumnSelectorTypeDef",
    "ConditionExpressionTypeDef",
    "JobSampleTypeDef",
    "S3LocationTypeDef",
    "ValidationConfigurationTypeDef",
    "SampleTypeDef",
    "RecipeReferenceTypeDef",
    "CreateScheduleRequestRequestTypeDef",
    "CsvOptionsTypeDef",
    "CsvOutputOptionsTypeDef",
    "DatetimeOptionsTypeDef",
    "FilterExpressionPaginatorTypeDef",
    "FilterExpressionTypeDef",
    "DeleteDatasetRequestRequestTypeDef",
    "DeleteJobRequestRequestTypeDef",
    "DeleteProjectRequestRequestTypeDef",
    "DeleteRecipeVersionRequestRequestTypeDef",
    "DeleteRulesetRequestRequestTypeDef",
    "DeleteScheduleRequestRequestTypeDef",
    "DescribeDatasetRequestRequestTypeDef",
    "DescribeJobRequestRequestTypeDef",
    "DescribeJobRunRequestRequestTypeDef",
    "DescribeProjectRequestRequestTypeDef",
    "DescribeRecipeRequestRequestTypeDef",
    "DescribeRulesetRequestRequestTypeDef",
    "DescribeScheduleRequestRequestTypeDef",
    "ExcelOptionsPaginatorTypeDef",
    "ExcelOptionsTypeDef",
    "FilesLimitTypeDef",
    "JsonOptionsTypeDef",
    "MetadataTypeDef",
    "PaginatorConfigTypeDef",
    "ListDatasetsRequestRequestTypeDef",
    "ListJobRunsRequestRequestTypeDef",
    "ListJobsRequestRequestTypeDef",
    "ListProjectsRequestRequestTypeDef",
    "ListRecipeVersionsRequestRequestTypeDef",
    "ListRecipesRequestRequestTypeDef",
    "ListRulesetsRequestRequestTypeDef",
    "RulesetItemTypeDef",
    "ListSchedulesRequestRequestTypeDef",
    "ScheduleTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "PublishRecipeRequestRequestTypeDef",
    "RecipeActionPaginatorTypeDef",
    "RecipeActionTypeDef",
    "ThresholdTypeDef",
    "ViewFrameTypeDef",
    "StartJobRunRequestRequestTypeDef",
    "StartProjectSessionRequestRequestTypeDef",
    "StatisticOverrideTypeDef",
    "StopJobRunRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateScheduleRequestRequestTypeDef",
    "EntityDetectorConfigurationTypeDef",
    "BatchDeleteRecipeVersionResponseTypeDef",
    "CreateDatasetResponseTypeDef",
    "CreateProfileJobResponseTypeDef",
    "CreateProjectResponseTypeDef",
    "CreateRecipeJobResponseTypeDef",
    "CreateRecipeResponseTypeDef",
    "CreateRulesetResponseTypeDef",
    "CreateScheduleResponseTypeDef",
    "DeleteDatasetResponseTypeDef",
    "DeleteJobResponseTypeDef",
    "DeleteProjectResponseTypeDef",
    "DeleteRecipeVersionResponseTypeDef",
    "DeleteRulesetResponseTypeDef",
    "DeleteScheduleResponseTypeDef",
    "DescribeScheduleResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PublishRecipeResponseTypeDef",
    "SendProjectSessionActionResponseTypeDef",
    "StartJobRunResponseTypeDef",
    "StartProjectSessionResponseTypeDef",
    "StopJobRunResponseTypeDef",
    "UpdateDatasetResponseTypeDef",
    "UpdateProfileJobResponseTypeDef",
    "UpdateProjectResponseTypeDef",
    "UpdateRecipeJobResponseTypeDef",
    "UpdateRecipeResponseTypeDef",
    "UpdateRulesetResponseTypeDef",
    "UpdateScheduleResponseTypeDef",
    "DataCatalogInputDefinitionTypeDef",
    "DatabaseInputDefinitionTypeDef",
    "DatabaseTableOutputOptionsTypeDef",
    "S3TableOutputOptionsTypeDef",
    "CreateProjectRequestRequestTypeDef",
    "DescribeProjectResponseTypeDef",
    "ProjectTypeDef",
    "UpdateProjectRequestRequestTypeDef",
    "OutputFormatOptionsTypeDef",
    "DatasetParameterPaginatorTypeDef",
    "DatasetParameterTypeDef",
    "FormatOptionsPaginatorTypeDef",
    "FormatOptionsTypeDef",
    "ListDatasetsRequestListDatasetsPaginateTypeDef",
    "ListJobRunsRequestListJobRunsPaginateTypeDef",
    "ListJobsRequestListJobsPaginateTypeDef",
    "ListProjectsRequestListProjectsPaginateTypeDef",
    "ListRecipeVersionsRequestListRecipeVersionsPaginateTypeDef",
    "ListRecipesRequestListRecipesPaginateTypeDef",
    "ListRulesetsRequestListRulesetsPaginateTypeDef",
    "ListSchedulesRequestListSchedulesPaginateTypeDef",
    "ListRulesetsResponseTypeDef",
    "ListSchedulesResponseTypeDef",
    "RecipeStepPaginatorTypeDef",
    "RecipeStepTypeDef",
    "RuleTypeDef",
    "StatisticsConfigurationTypeDef",
    "InputTypeDef",
    "DatabaseOutputTypeDef",
    "DataCatalogOutputTypeDef",
    "ListProjectsResponseTypeDef",
    "OutputPaginatorTypeDef",
    "OutputTypeDef",
    "PathOptionsPaginatorTypeDef",
    "PathOptionsTypeDef",
    "RecipePaginatorTypeDef",
    "CreateRecipeRequestRequestTypeDef",
    "DescribeRecipeResponseTypeDef",
    "RecipeTypeDef",
    "SendProjectSessionActionRequestRequestTypeDef",
    "UpdateRecipeRequestRequestTypeDef",
    "CreateRulesetRequestRequestTypeDef",
    "DescribeRulesetResponseTypeDef",
    "UpdateRulesetRequestRequestTypeDef",
    "ColumnStatisticsConfigurationTypeDef",
    "JobPaginatorTypeDef",
    "JobRunPaginatorTypeDef",
    "CreateRecipeJobRequestRequestTypeDef",
    "JobRunTypeDef",
    "JobTypeDef",
    "UpdateRecipeJobRequestRequestTypeDef",
    "DatasetPaginatorTypeDef",
    "CreateDatasetRequestRequestTypeDef",
    "DatasetTypeDef",
    "DescribeDatasetResponseTypeDef",
    "UpdateDatasetRequestRequestTypeDef",
    "ListRecipeVersionsResponsePaginatorTypeDef",
    "ListRecipesResponsePaginatorTypeDef",
    "ListRecipeVersionsResponseTypeDef",
    "ListRecipesResponseTypeDef",
    "ProfileConfigurationTypeDef",
    "ListJobsResponsePaginatorTypeDef",
    "ListJobRunsResponsePaginatorTypeDef",
    "ListJobRunsResponseTypeDef",
    "ListJobsResponseTypeDef",
    "ListDatasetsResponsePaginatorTypeDef",
    "ListDatasetsResponseTypeDef",
    "CreateProfileJobRequestRequestTypeDef",
    "DescribeJobResponseTypeDef",
    "DescribeJobRunResponseTypeDef",
    "UpdateProfileJobRequestRequestTypeDef",
)

AllowedStatisticsTypeDef = TypedDict(
    "AllowedStatisticsTypeDef",
    {
        "Statistics": Sequence[str],
    },
)
BatchDeleteRecipeVersionRequestRequestTypeDef = TypedDict(
    "BatchDeleteRecipeVersionRequestRequestTypeDef",
    {
        "Name": str,
        "RecipeVersions": Sequence[str],
    },
)
RecipeVersionErrorDetailTypeDef = TypedDict(
    "RecipeVersionErrorDetailTypeDef",
    {
        "ErrorCode": NotRequired[str],
        "ErrorMessage": NotRequired[str],
        "RecipeVersion": NotRequired[str],
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
ColumnSelectorTypeDef = TypedDict(
    "ColumnSelectorTypeDef",
    {
        "Regex": NotRequired[str],
        "Name": NotRequired[str],
    },
)
ConditionExpressionTypeDef = TypedDict(
    "ConditionExpressionTypeDef",
    {
        "Condition": str,
        "TargetColumn": str,
        "Value": NotRequired[str],
    },
)
JobSampleTypeDef = TypedDict(
    "JobSampleTypeDef",
    {
        "Mode": NotRequired[SampleModeType],
        "Size": NotRequired[int],
    },
)
S3LocationTypeDef = TypedDict(
    "S3LocationTypeDef",
    {
        "Bucket": str,
        "Key": NotRequired[str],
        "BucketOwner": NotRequired[str],
    },
)
ValidationConfigurationTypeDef = TypedDict(
    "ValidationConfigurationTypeDef",
    {
        "RulesetArn": str,
        "ValidationMode": NotRequired[Literal["CHECK_ALL"]],
    },
)
SampleTypeDef = TypedDict(
    "SampleTypeDef",
    {
        "Type": SampleTypeType,
        "Size": NotRequired[int],
    },
)
RecipeReferenceTypeDef = TypedDict(
    "RecipeReferenceTypeDef",
    {
        "Name": str,
        "RecipeVersion": NotRequired[str],
    },
)
CreateScheduleRequestRequestTypeDef = TypedDict(
    "CreateScheduleRequestRequestTypeDef",
    {
        "CronExpression": str,
        "Name": str,
        "JobNames": NotRequired[Sequence[str]],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
CsvOptionsTypeDef = TypedDict(
    "CsvOptionsTypeDef",
    {
        "Delimiter": NotRequired[str],
        "HeaderRow": NotRequired[bool],
    },
)
CsvOutputOptionsTypeDef = TypedDict(
    "CsvOutputOptionsTypeDef",
    {
        "Delimiter": NotRequired[str],
    },
)
DatetimeOptionsTypeDef = TypedDict(
    "DatetimeOptionsTypeDef",
    {
        "Format": str,
        "TimezoneOffset": NotRequired[str],
        "LocaleCode": NotRequired[str],
    },
)
FilterExpressionPaginatorTypeDef = TypedDict(
    "FilterExpressionPaginatorTypeDef",
    {
        "Expression": str,
        "ValuesMap": Dict[str, str],
    },
)
FilterExpressionTypeDef = TypedDict(
    "FilterExpressionTypeDef",
    {
        "Expression": str,
        "ValuesMap": Mapping[str, str],
    },
)
DeleteDatasetRequestRequestTypeDef = TypedDict(
    "DeleteDatasetRequestRequestTypeDef",
    {
        "Name": str,
    },
)
DeleteJobRequestRequestTypeDef = TypedDict(
    "DeleteJobRequestRequestTypeDef",
    {
        "Name": str,
    },
)
DeleteProjectRequestRequestTypeDef = TypedDict(
    "DeleteProjectRequestRequestTypeDef",
    {
        "Name": str,
    },
)
DeleteRecipeVersionRequestRequestTypeDef = TypedDict(
    "DeleteRecipeVersionRequestRequestTypeDef",
    {
        "Name": str,
        "RecipeVersion": str,
    },
)
DeleteRulesetRequestRequestTypeDef = TypedDict(
    "DeleteRulesetRequestRequestTypeDef",
    {
        "Name": str,
    },
)
DeleteScheduleRequestRequestTypeDef = TypedDict(
    "DeleteScheduleRequestRequestTypeDef",
    {
        "Name": str,
    },
)
DescribeDatasetRequestRequestTypeDef = TypedDict(
    "DescribeDatasetRequestRequestTypeDef",
    {
        "Name": str,
    },
)
DescribeJobRequestRequestTypeDef = TypedDict(
    "DescribeJobRequestRequestTypeDef",
    {
        "Name": str,
    },
)
DescribeJobRunRequestRequestTypeDef = TypedDict(
    "DescribeJobRunRequestRequestTypeDef",
    {
        "Name": str,
        "RunId": str,
    },
)
DescribeProjectRequestRequestTypeDef = TypedDict(
    "DescribeProjectRequestRequestTypeDef",
    {
        "Name": str,
    },
)
DescribeRecipeRequestRequestTypeDef = TypedDict(
    "DescribeRecipeRequestRequestTypeDef",
    {
        "Name": str,
        "RecipeVersion": NotRequired[str],
    },
)
DescribeRulesetRequestRequestTypeDef = TypedDict(
    "DescribeRulesetRequestRequestTypeDef",
    {
        "Name": str,
    },
)
DescribeScheduleRequestRequestTypeDef = TypedDict(
    "DescribeScheduleRequestRequestTypeDef",
    {
        "Name": str,
    },
)
ExcelOptionsPaginatorTypeDef = TypedDict(
    "ExcelOptionsPaginatorTypeDef",
    {
        "SheetNames": NotRequired[List[str]],
        "SheetIndexes": NotRequired[List[int]],
        "HeaderRow": NotRequired[bool],
    },
)
ExcelOptionsTypeDef = TypedDict(
    "ExcelOptionsTypeDef",
    {
        "SheetNames": NotRequired[Sequence[str]],
        "SheetIndexes": NotRequired[Sequence[int]],
        "HeaderRow": NotRequired[bool],
    },
)
FilesLimitTypeDef = TypedDict(
    "FilesLimitTypeDef",
    {
        "MaxFiles": int,
        "OrderedBy": NotRequired[Literal["LAST_MODIFIED_DATE"]],
        "Order": NotRequired[OrderType],
    },
)
JsonOptionsTypeDef = TypedDict(
    "JsonOptionsTypeDef",
    {
        "MultiLine": NotRequired[bool],
    },
)
MetadataTypeDef = TypedDict(
    "MetadataTypeDef",
    {
        "SourceArn": NotRequired[str],
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
ListDatasetsRequestRequestTypeDef = TypedDict(
    "ListDatasetsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListJobRunsRequestRequestTypeDef = TypedDict(
    "ListJobRunsRequestRequestTypeDef",
    {
        "Name": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListJobsRequestRequestTypeDef = TypedDict(
    "ListJobsRequestRequestTypeDef",
    {
        "DatasetName": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "ProjectName": NotRequired[str],
    },
)
ListProjectsRequestRequestTypeDef = TypedDict(
    "ListProjectsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListRecipeVersionsRequestRequestTypeDef = TypedDict(
    "ListRecipeVersionsRequestRequestTypeDef",
    {
        "Name": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListRecipesRequestRequestTypeDef = TypedDict(
    "ListRecipesRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "RecipeVersion": NotRequired[str],
    },
)
ListRulesetsRequestRequestTypeDef = TypedDict(
    "ListRulesetsRequestRequestTypeDef",
    {
        "TargetArn": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
RulesetItemTypeDef = TypedDict(
    "RulesetItemTypeDef",
    {
        "Name": str,
        "TargetArn": str,
        "AccountId": NotRequired[str],
        "CreatedBy": NotRequired[str],
        "CreateDate": NotRequired[datetime],
        "Description": NotRequired[str],
        "LastModifiedBy": NotRequired[str],
        "LastModifiedDate": NotRequired[datetime],
        "ResourceArn": NotRequired[str],
        "RuleCount": NotRequired[int],
        "Tags": NotRequired[Dict[str, str]],
    },
)
ListSchedulesRequestRequestTypeDef = TypedDict(
    "ListSchedulesRequestRequestTypeDef",
    {
        "JobName": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ScheduleTypeDef = TypedDict(
    "ScheduleTypeDef",
    {
        "Name": str,
        "AccountId": NotRequired[str],
        "CreatedBy": NotRequired[str],
        "CreateDate": NotRequired[datetime],
        "JobNames": NotRequired[List[str]],
        "LastModifiedBy": NotRequired[str],
        "LastModifiedDate": NotRequired[datetime],
        "ResourceArn": NotRequired[str],
        "CronExpression": NotRequired[str],
        "Tags": NotRequired[Dict[str, str]],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
PublishRecipeRequestRequestTypeDef = TypedDict(
    "PublishRecipeRequestRequestTypeDef",
    {
        "Name": str,
        "Description": NotRequired[str],
    },
)
RecipeActionPaginatorTypeDef = TypedDict(
    "RecipeActionPaginatorTypeDef",
    {
        "Operation": str,
        "Parameters": NotRequired[Dict[str, str]],
    },
)
RecipeActionTypeDef = TypedDict(
    "RecipeActionTypeDef",
    {
        "Operation": str,
        "Parameters": NotRequired[Mapping[str, str]],
    },
)
ThresholdTypeDef = TypedDict(
    "ThresholdTypeDef",
    {
        "Value": float,
        "Type": NotRequired[ThresholdTypeType],
        "Unit": NotRequired[ThresholdUnitType],
    },
)
ViewFrameTypeDef = TypedDict(
    "ViewFrameTypeDef",
    {
        "StartColumnIndex": int,
        "ColumnRange": NotRequired[int],
        "HiddenColumns": NotRequired[Sequence[str]],
        "StartRowIndex": NotRequired[int],
        "RowRange": NotRequired[int],
        "Analytics": NotRequired[AnalyticsModeType],
    },
)
StartJobRunRequestRequestTypeDef = TypedDict(
    "StartJobRunRequestRequestTypeDef",
    {
        "Name": str,
    },
)
StartProjectSessionRequestRequestTypeDef = TypedDict(
    "StartProjectSessionRequestRequestTypeDef",
    {
        "Name": str,
        "AssumeControl": NotRequired[bool],
    },
)
StatisticOverrideTypeDef = TypedDict(
    "StatisticOverrideTypeDef",
    {
        "Statistic": str,
        "Parameters": Mapping[str, str],
    },
)
StopJobRunRequestRequestTypeDef = TypedDict(
    "StopJobRunRequestRequestTypeDef",
    {
        "Name": str,
        "RunId": str,
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Mapping[str, str],
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)
UpdateScheduleRequestRequestTypeDef = TypedDict(
    "UpdateScheduleRequestRequestTypeDef",
    {
        "CronExpression": str,
        "Name": str,
        "JobNames": NotRequired[Sequence[str]],
    },
)
EntityDetectorConfigurationTypeDef = TypedDict(
    "EntityDetectorConfigurationTypeDef",
    {
        "EntityTypes": Sequence[str],
        "AllowedStatistics": NotRequired[Sequence[AllowedStatisticsTypeDef]],
    },
)
BatchDeleteRecipeVersionResponseTypeDef = TypedDict(
    "BatchDeleteRecipeVersionResponseTypeDef",
    {
        "Name": str,
        "Errors": List[RecipeVersionErrorDetailTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDatasetResponseTypeDef = TypedDict(
    "CreateDatasetResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateProfileJobResponseTypeDef = TypedDict(
    "CreateProfileJobResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateProjectResponseTypeDef = TypedDict(
    "CreateProjectResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateRecipeJobResponseTypeDef = TypedDict(
    "CreateRecipeJobResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateRecipeResponseTypeDef = TypedDict(
    "CreateRecipeResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateRulesetResponseTypeDef = TypedDict(
    "CreateRulesetResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateScheduleResponseTypeDef = TypedDict(
    "CreateScheduleResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteDatasetResponseTypeDef = TypedDict(
    "DeleteDatasetResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteJobResponseTypeDef = TypedDict(
    "DeleteJobResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteProjectResponseTypeDef = TypedDict(
    "DeleteProjectResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteRecipeVersionResponseTypeDef = TypedDict(
    "DeleteRecipeVersionResponseTypeDef",
    {
        "Name": str,
        "RecipeVersion": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteRulesetResponseTypeDef = TypedDict(
    "DeleteRulesetResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteScheduleResponseTypeDef = TypedDict(
    "DeleteScheduleResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeScheduleResponseTypeDef = TypedDict(
    "DescribeScheduleResponseTypeDef",
    {
        "CreateDate": datetime,
        "CreatedBy": str,
        "JobNames": List[str],
        "LastModifiedBy": str,
        "LastModifiedDate": datetime,
        "ResourceArn": str,
        "CronExpression": str,
        "Tags": Dict[str, str],
        "Name": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PublishRecipeResponseTypeDef = TypedDict(
    "PublishRecipeResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SendProjectSessionActionResponseTypeDef = TypedDict(
    "SendProjectSessionActionResponseTypeDef",
    {
        "Result": str,
        "Name": str,
        "ActionId": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartJobRunResponseTypeDef = TypedDict(
    "StartJobRunResponseTypeDef",
    {
        "RunId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartProjectSessionResponseTypeDef = TypedDict(
    "StartProjectSessionResponseTypeDef",
    {
        "Name": str,
        "ClientSessionId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StopJobRunResponseTypeDef = TypedDict(
    "StopJobRunResponseTypeDef",
    {
        "RunId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateDatasetResponseTypeDef = TypedDict(
    "UpdateDatasetResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateProfileJobResponseTypeDef = TypedDict(
    "UpdateProfileJobResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateProjectResponseTypeDef = TypedDict(
    "UpdateProjectResponseTypeDef",
    {
        "LastModifiedDate": datetime,
        "Name": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateRecipeJobResponseTypeDef = TypedDict(
    "UpdateRecipeJobResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateRecipeResponseTypeDef = TypedDict(
    "UpdateRecipeResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateRulesetResponseTypeDef = TypedDict(
    "UpdateRulesetResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateScheduleResponseTypeDef = TypedDict(
    "UpdateScheduleResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DataCatalogInputDefinitionTypeDef = TypedDict(
    "DataCatalogInputDefinitionTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "CatalogId": NotRequired[str],
        "TempDirectory": NotRequired[S3LocationTypeDef],
    },
)
DatabaseInputDefinitionTypeDef = TypedDict(
    "DatabaseInputDefinitionTypeDef",
    {
        "GlueConnectionName": str,
        "DatabaseTableName": NotRequired[str],
        "TempDirectory": NotRequired[S3LocationTypeDef],
        "QueryString": NotRequired[str],
    },
)
DatabaseTableOutputOptionsTypeDef = TypedDict(
    "DatabaseTableOutputOptionsTypeDef",
    {
        "TableName": str,
        "TempDirectory": NotRequired[S3LocationTypeDef],
    },
)
S3TableOutputOptionsTypeDef = TypedDict(
    "S3TableOutputOptionsTypeDef",
    {
        "Location": S3LocationTypeDef,
    },
)
CreateProjectRequestRequestTypeDef = TypedDict(
    "CreateProjectRequestRequestTypeDef",
    {
        "DatasetName": str,
        "Name": str,
        "RecipeName": str,
        "RoleArn": str,
        "Sample": NotRequired[SampleTypeDef],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
DescribeProjectResponseTypeDef = TypedDict(
    "DescribeProjectResponseTypeDef",
    {
        "CreateDate": datetime,
        "CreatedBy": str,
        "DatasetName": str,
        "LastModifiedDate": datetime,
        "LastModifiedBy": str,
        "Name": str,
        "RecipeName": str,
        "ResourceArn": str,
        "Sample": SampleTypeDef,
        "RoleArn": str,
        "Tags": Dict[str, str],
        "SessionStatus": SessionStatusType,
        "OpenedBy": str,
        "OpenDate": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ProjectTypeDef = TypedDict(
    "ProjectTypeDef",
    {
        "Name": str,
        "RecipeName": str,
        "AccountId": NotRequired[str],
        "CreateDate": NotRequired[datetime],
        "CreatedBy": NotRequired[str],
        "DatasetName": NotRequired[str],
        "LastModifiedDate": NotRequired[datetime],
        "LastModifiedBy": NotRequired[str],
        "ResourceArn": NotRequired[str],
        "Sample": NotRequired[SampleTypeDef],
        "Tags": NotRequired[Dict[str, str]],
        "RoleArn": NotRequired[str],
        "OpenedBy": NotRequired[str],
        "OpenDate": NotRequired[datetime],
    },
)
UpdateProjectRequestRequestTypeDef = TypedDict(
    "UpdateProjectRequestRequestTypeDef",
    {
        "RoleArn": str,
        "Name": str,
        "Sample": NotRequired[SampleTypeDef],
    },
)
OutputFormatOptionsTypeDef = TypedDict(
    "OutputFormatOptionsTypeDef",
    {
        "Csv": NotRequired[CsvOutputOptionsTypeDef],
    },
)
DatasetParameterPaginatorTypeDef = TypedDict(
    "DatasetParameterPaginatorTypeDef",
    {
        "Name": str,
        "Type": ParameterTypeType,
        "DatetimeOptions": NotRequired[DatetimeOptionsTypeDef],
        "CreateColumn": NotRequired[bool],
        "Filter": NotRequired[FilterExpressionPaginatorTypeDef],
    },
)
DatasetParameterTypeDef = TypedDict(
    "DatasetParameterTypeDef",
    {
        "Name": str,
        "Type": ParameterTypeType,
        "DatetimeOptions": NotRequired[DatetimeOptionsTypeDef],
        "CreateColumn": NotRequired[bool],
        "Filter": NotRequired[FilterExpressionTypeDef],
    },
)
FormatOptionsPaginatorTypeDef = TypedDict(
    "FormatOptionsPaginatorTypeDef",
    {
        "Json": NotRequired[JsonOptionsTypeDef],
        "Excel": NotRequired[ExcelOptionsPaginatorTypeDef],
        "Csv": NotRequired[CsvOptionsTypeDef],
    },
)
FormatOptionsTypeDef = TypedDict(
    "FormatOptionsTypeDef",
    {
        "Json": NotRequired[JsonOptionsTypeDef],
        "Excel": NotRequired[ExcelOptionsTypeDef],
        "Csv": NotRequired[CsvOptionsTypeDef],
    },
)
ListDatasetsRequestListDatasetsPaginateTypeDef = TypedDict(
    "ListDatasetsRequestListDatasetsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListJobRunsRequestListJobRunsPaginateTypeDef = TypedDict(
    "ListJobRunsRequestListJobRunsPaginateTypeDef",
    {
        "Name": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListJobsRequestListJobsPaginateTypeDef = TypedDict(
    "ListJobsRequestListJobsPaginateTypeDef",
    {
        "DatasetName": NotRequired[str],
        "ProjectName": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListProjectsRequestListProjectsPaginateTypeDef = TypedDict(
    "ListProjectsRequestListProjectsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListRecipeVersionsRequestListRecipeVersionsPaginateTypeDef = TypedDict(
    "ListRecipeVersionsRequestListRecipeVersionsPaginateTypeDef",
    {
        "Name": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListRecipesRequestListRecipesPaginateTypeDef = TypedDict(
    "ListRecipesRequestListRecipesPaginateTypeDef",
    {
        "RecipeVersion": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListRulesetsRequestListRulesetsPaginateTypeDef = TypedDict(
    "ListRulesetsRequestListRulesetsPaginateTypeDef",
    {
        "TargetArn": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListSchedulesRequestListSchedulesPaginateTypeDef = TypedDict(
    "ListSchedulesRequestListSchedulesPaginateTypeDef",
    {
        "JobName": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListRulesetsResponseTypeDef = TypedDict(
    "ListRulesetsResponseTypeDef",
    {
        "Rulesets": List[RulesetItemTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListSchedulesResponseTypeDef = TypedDict(
    "ListSchedulesResponseTypeDef",
    {
        "Schedules": List[ScheduleTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RecipeStepPaginatorTypeDef = TypedDict(
    "RecipeStepPaginatorTypeDef",
    {
        "Action": RecipeActionPaginatorTypeDef,
        "ConditionExpressions": NotRequired[List[ConditionExpressionTypeDef]],
    },
)
RecipeStepTypeDef = TypedDict(
    "RecipeStepTypeDef",
    {
        "Action": RecipeActionTypeDef,
        "ConditionExpressions": NotRequired[Sequence[ConditionExpressionTypeDef]],
    },
)
RuleTypeDef = TypedDict(
    "RuleTypeDef",
    {
        "Name": str,
        "CheckExpression": str,
        "Disabled": NotRequired[bool],
        "SubstitutionMap": NotRequired[Mapping[str, str]],
        "Threshold": NotRequired[ThresholdTypeDef],
        "ColumnSelectors": NotRequired[Sequence[ColumnSelectorTypeDef]],
    },
)
StatisticsConfigurationTypeDef = TypedDict(
    "StatisticsConfigurationTypeDef",
    {
        "IncludedStatistics": NotRequired[Sequence[str]],
        "Overrides": NotRequired[Sequence[StatisticOverrideTypeDef]],
    },
)
InputTypeDef = TypedDict(
    "InputTypeDef",
    {
        "S3InputDefinition": NotRequired[S3LocationTypeDef],
        "DataCatalogInputDefinition": NotRequired[DataCatalogInputDefinitionTypeDef],
        "DatabaseInputDefinition": NotRequired[DatabaseInputDefinitionTypeDef],
        "Metadata": NotRequired[MetadataTypeDef],
    },
)
DatabaseOutputTypeDef = TypedDict(
    "DatabaseOutputTypeDef",
    {
        "GlueConnectionName": str,
        "DatabaseOptions": DatabaseTableOutputOptionsTypeDef,
        "DatabaseOutputMode": NotRequired[Literal["NEW_TABLE"]],
    },
)
DataCatalogOutputTypeDef = TypedDict(
    "DataCatalogOutputTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "CatalogId": NotRequired[str],
        "S3Options": NotRequired[S3TableOutputOptionsTypeDef],
        "DatabaseOptions": NotRequired[DatabaseTableOutputOptionsTypeDef],
        "Overwrite": NotRequired[bool],
    },
)
ListProjectsResponseTypeDef = TypedDict(
    "ListProjectsResponseTypeDef",
    {
        "Projects": List[ProjectTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
OutputPaginatorTypeDef = TypedDict(
    "OutputPaginatorTypeDef",
    {
        "Location": S3LocationTypeDef,
        "CompressionFormat": NotRequired[CompressionFormatType],
        "Format": NotRequired[OutputFormatType],
        "PartitionColumns": NotRequired[List[str]],
        "Overwrite": NotRequired[bool],
        "FormatOptions": NotRequired[OutputFormatOptionsTypeDef],
        "MaxOutputFiles": NotRequired[int],
    },
)
OutputTypeDef = TypedDict(
    "OutputTypeDef",
    {
        "Location": S3LocationTypeDef,
        "CompressionFormat": NotRequired[CompressionFormatType],
        "Format": NotRequired[OutputFormatType],
        "PartitionColumns": NotRequired[Sequence[str]],
        "Overwrite": NotRequired[bool],
        "FormatOptions": NotRequired[OutputFormatOptionsTypeDef],
        "MaxOutputFiles": NotRequired[int],
    },
)
PathOptionsPaginatorTypeDef = TypedDict(
    "PathOptionsPaginatorTypeDef",
    {
        "LastModifiedDateCondition": NotRequired[FilterExpressionPaginatorTypeDef],
        "FilesLimit": NotRequired[FilesLimitTypeDef],
        "Parameters": NotRequired[Dict[str, DatasetParameterPaginatorTypeDef]],
    },
)
PathOptionsTypeDef = TypedDict(
    "PathOptionsTypeDef",
    {
        "LastModifiedDateCondition": NotRequired[FilterExpressionTypeDef],
        "FilesLimit": NotRequired[FilesLimitTypeDef],
        "Parameters": NotRequired[Mapping[str, DatasetParameterTypeDef]],
    },
)
RecipePaginatorTypeDef = TypedDict(
    "RecipePaginatorTypeDef",
    {
        "Name": str,
        "CreatedBy": NotRequired[str],
        "CreateDate": NotRequired[datetime],
        "LastModifiedBy": NotRequired[str],
        "LastModifiedDate": NotRequired[datetime],
        "ProjectName": NotRequired[str],
        "PublishedBy": NotRequired[str],
        "PublishedDate": NotRequired[datetime],
        "Description": NotRequired[str],
        "ResourceArn": NotRequired[str],
        "Steps": NotRequired[List[RecipeStepPaginatorTypeDef]],
        "Tags": NotRequired[Dict[str, str]],
        "RecipeVersion": NotRequired[str],
    },
)
CreateRecipeRequestRequestTypeDef = TypedDict(
    "CreateRecipeRequestRequestTypeDef",
    {
        "Name": str,
        "Steps": Sequence[RecipeStepTypeDef],
        "Description": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
DescribeRecipeResponseTypeDef = TypedDict(
    "DescribeRecipeResponseTypeDef",
    {
        "CreatedBy": str,
        "CreateDate": datetime,
        "LastModifiedBy": str,
        "LastModifiedDate": datetime,
        "ProjectName": str,
        "PublishedBy": str,
        "PublishedDate": datetime,
        "Description": str,
        "Name": str,
        "Steps": List[RecipeStepTypeDef],
        "Tags": Dict[str, str],
        "ResourceArn": str,
        "RecipeVersion": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RecipeTypeDef = TypedDict(
    "RecipeTypeDef",
    {
        "Name": str,
        "CreatedBy": NotRequired[str],
        "CreateDate": NotRequired[datetime],
        "LastModifiedBy": NotRequired[str],
        "LastModifiedDate": NotRequired[datetime],
        "ProjectName": NotRequired[str],
        "PublishedBy": NotRequired[str],
        "PublishedDate": NotRequired[datetime],
        "Description": NotRequired[str],
        "ResourceArn": NotRequired[str],
        "Steps": NotRequired[List[RecipeStepTypeDef]],
        "Tags": NotRequired[Dict[str, str]],
        "RecipeVersion": NotRequired[str],
    },
)
SendProjectSessionActionRequestRequestTypeDef = TypedDict(
    "SendProjectSessionActionRequestRequestTypeDef",
    {
        "Name": str,
        "Preview": NotRequired[bool],
        "RecipeStep": NotRequired[RecipeStepTypeDef],
        "StepIndex": NotRequired[int],
        "ClientSessionId": NotRequired[str],
        "ViewFrame": NotRequired[ViewFrameTypeDef],
    },
)
UpdateRecipeRequestRequestTypeDef = TypedDict(
    "UpdateRecipeRequestRequestTypeDef",
    {
        "Name": str,
        "Description": NotRequired[str],
        "Steps": NotRequired[Sequence[RecipeStepTypeDef]],
    },
)
CreateRulesetRequestRequestTypeDef = TypedDict(
    "CreateRulesetRequestRequestTypeDef",
    {
        "Name": str,
        "TargetArn": str,
        "Rules": Sequence[RuleTypeDef],
        "Description": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
DescribeRulesetResponseTypeDef = TypedDict(
    "DescribeRulesetResponseTypeDef",
    {
        "Name": str,
        "Description": str,
        "TargetArn": str,
        "Rules": List[RuleTypeDef],
        "CreateDate": datetime,
        "CreatedBy": str,
        "LastModifiedBy": str,
        "LastModifiedDate": datetime,
        "ResourceArn": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateRulesetRequestRequestTypeDef = TypedDict(
    "UpdateRulesetRequestRequestTypeDef",
    {
        "Name": str,
        "Rules": Sequence[RuleTypeDef],
        "Description": NotRequired[str],
    },
)
ColumnStatisticsConfigurationTypeDef = TypedDict(
    "ColumnStatisticsConfigurationTypeDef",
    {
        "Statistics": StatisticsConfigurationTypeDef,
        "Selectors": NotRequired[Sequence[ColumnSelectorTypeDef]],
    },
)
JobPaginatorTypeDef = TypedDict(
    "JobPaginatorTypeDef",
    {
        "Name": str,
        "AccountId": NotRequired[str],
        "CreatedBy": NotRequired[str],
        "CreateDate": NotRequired[datetime],
        "DatasetName": NotRequired[str],
        "EncryptionKeyArn": NotRequired[str],
        "EncryptionMode": NotRequired[EncryptionModeType],
        "Type": NotRequired[JobTypeType],
        "LastModifiedBy": NotRequired[str],
        "LastModifiedDate": NotRequired[datetime],
        "LogSubscription": NotRequired[LogSubscriptionType],
        "MaxCapacity": NotRequired[int],
        "MaxRetries": NotRequired[int],
        "Outputs": NotRequired[List[OutputPaginatorTypeDef]],
        "DataCatalogOutputs": NotRequired[List[DataCatalogOutputTypeDef]],
        "DatabaseOutputs": NotRequired[List[DatabaseOutputTypeDef]],
        "ProjectName": NotRequired[str],
        "RecipeReference": NotRequired[RecipeReferenceTypeDef],
        "ResourceArn": NotRequired[str],
        "RoleArn": NotRequired[str],
        "Timeout": NotRequired[int],
        "Tags": NotRequired[Dict[str, str]],
        "JobSample": NotRequired[JobSampleTypeDef],
        "ValidationConfigurations": NotRequired[List[ValidationConfigurationTypeDef]],
    },
)
JobRunPaginatorTypeDef = TypedDict(
    "JobRunPaginatorTypeDef",
    {
        "Attempt": NotRequired[int],
        "CompletedOn": NotRequired[datetime],
        "DatasetName": NotRequired[str],
        "ErrorMessage": NotRequired[str],
        "ExecutionTime": NotRequired[int],
        "JobName": NotRequired[str],
        "RunId": NotRequired[str],
        "State": NotRequired[JobRunStateType],
        "LogSubscription": NotRequired[LogSubscriptionType],
        "LogGroupName": NotRequired[str],
        "Outputs": NotRequired[List[OutputPaginatorTypeDef]],
        "DataCatalogOutputs": NotRequired[List[DataCatalogOutputTypeDef]],
        "DatabaseOutputs": NotRequired[List[DatabaseOutputTypeDef]],
        "RecipeReference": NotRequired[RecipeReferenceTypeDef],
        "StartedBy": NotRequired[str],
        "StartedOn": NotRequired[datetime],
        "JobSample": NotRequired[JobSampleTypeDef],
        "ValidationConfigurations": NotRequired[List[ValidationConfigurationTypeDef]],
    },
)
CreateRecipeJobRequestRequestTypeDef = TypedDict(
    "CreateRecipeJobRequestRequestTypeDef",
    {
        "Name": str,
        "RoleArn": str,
        "DatasetName": NotRequired[str],
        "EncryptionKeyArn": NotRequired[str],
        "EncryptionMode": NotRequired[EncryptionModeType],
        "LogSubscription": NotRequired[LogSubscriptionType],
        "MaxCapacity": NotRequired[int],
        "MaxRetries": NotRequired[int],
        "Outputs": NotRequired[Sequence[OutputTypeDef]],
        "DataCatalogOutputs": NotRequired[Sequence[DataCatalogOutputTypeDef]],
        "DatabaseOutputs": NotRequired[Sequence[DatabaseOutputTypeDef]],
        "ProjectName": NotRequired[str],
        "RecipeReference": NotRequired[RecipeReferenceTypeDef],
        "Tags": NotRequired[Mapping[str, str]],
        "Timeout": NotRequired[int],
    },
)
JobRunTypeDef = TypedDict(
    "JobRunTypeDef",
    {
        "Attempt": NotRequired[int],
        "CompletedOn": NotRequired[datetime],
        "DatasetName": NotRequired[str],
        "ErrorMessage": NotRequired[str],
        "ExecutionTime": NotRequired[int],
        "JobName": NotRequired[str],
        "RunId": NotRequired[str],
        "State": NotRequired[JobRunStateType],
        "LogSubscription": NotRequired[LogSubscriptionType],
        "LogGroupName": NotRequired[str],
        "Outputs": NotRequired[List[OutputTypeDef]],
        "DataCatalogOutputs": NotRequired[List[DataCatalogOutputTypeDef]],
        "DatabaseOutputs": NotRequired[List[DatabaseOutputTypeDef]],
        "RecipeReference": NotRequired[RecipeReferenceTypeDef],
        "StartedBy": NotRequired[str],
        "StartedOn": NotRequired[datetime],
        "JobSample": NotRequired[JobSampleTypeDef],
        "ValidationConfigurations": NotRequired[List[ValidationConfigurationTypeDef]],
    },
)
JobTypeDef = TypedDict(
    "JobTypeDef",
    {
        "Name": str,
        "AccountId": NotRequired[str],
        "CreatedBy": NotRequired[str],
        "CreateDate": NotRequired[datetime],
        "DatasetName": NotRequired[str],
        "EncryptionKeyArn": NotRequired[str],
        "EncryptionMode": NotRequired[EncryptionModeType],
        "Type": NotRequired[JobTypeType],
        "LastModifiedBy": NotRequired[str],
        "LastModifiedDate": NotRequired[datetime],
        "LogSubscription": NotRequired[LogSubscriptionType],
        "MaxCapacity": NotRequired[int],
        "MaxRetries": NotRequired[int],
        "Outputs": NotRequired[List[OutputTypeDef]],
        "DataCatalogOutputs": NotRequired[List[DataCatalogOutputTypeDef]],
        "DatabaseOutputs": NotRequired[List[DatabaseOutputTypeDef]],
        "ProjectName": NotRequired[str],
        "RecipeReference": NotRequired[RecipeReferenceTypeDef],
        "ResourceArn": NotRequired[str],
        "RoleArn": NotRequired[str],
        "Timeout": NotRequired[int],
        "Tags": NotRequired[Dict[str, str]],
        "JobSample": NotRequired[JobSampleTypeDef],
        "ValidationConfigurations": NotRequired[List[ValidationConfigurationTypeDef]],
    },
)
UpdateRecipeJobRequestRequestTypeDef = TypedDict(
    "UpdateRecipeJobRequestRequestTypeDef",
    {
        "Name": str,
        "RoleArn": str,
        "EncryptionKeyArn": NotRequired[str],
        "EncryptionMode": NotRequired[EncryptionModeType],
        "LogSubscription": NotRequired[LogSubscriptionType],
        "MaxCapacity": NotRequired[int],
        "MaxRetries": NotRequired[int],
        "Outputs": NotRequired[Sequence[OutputTypeDef]],
        "DataCatalogOutputs": NotRequired[Sequence[DataCatalogOutputTypeDef]],
        "DatabaseOutputs": NotRequired[Sequence[DatabaseOutputTypeDef]],
        "Timeout": NotRequired[int],
    },
)
DatasetPaginatorTypeDef = TypedDict(
    "DatasetPaginatorTypeDef",
    {
        "Name": str,
        "Input": InputTypeDef,
        "AccountId": NotRequired[str],
        "CreatedBy": NotRequired[str],
        "CreateDate": NotRequired[datetime],
        "Format": NotRequired[InputFormatType],
        "FormatOptions": NotRequired[FormatOptionsPaginatorTypeDef],
        "LastModifiedDate": NotRequired[datetime],
        "LastModifiedBy": NotRequired[str],
        "Source": NotRequired[SourceType],
        "PathOptions": NotRequired[PathOptionsPaginatorTypeDef],
        "Tags": NotRequired[Dict[str, str]],
        "ResourceArn": NotRequired[str],
    },
)
CreateDatasetRequestRequestTypeDef = TypedDict(
    "CreateDatasetRequestRequestTypeDef",
    {
        "Name": str,
        "Input": InputTypeDef,
        "Format": NotRequired[InputFormatType],
        "FormatOptions": NotRequired[FormatOptionsTypeDef],
        "PathOptions": NotRequired[PathOptionsTypeDef],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
DatasetTypeDef = TypedDict(
    "DatasetTypeDef",
    {
        "Name": str,
        "Input": InputTypeDef,
        "AccountId": NotRequired[str],
        "CreatedBy": NotRequired[str],
        "CreateDate": NotRequired[datetime],
        "Format": NotRequired[InputFormatType],
        "FormatOptions": NotRequired[FormatOptionsTypeDef],
        "LastModifiedDate": NotRequired[datetime],
        "LastModifiedBy": NotRequired[str],
        "Source": NotRequired[SourceType],
        "PathOptions": NotRequired[PathOptionsTypeDef],
        "Tags": NotRequired[Dict[str, str]],
        "ResourceArn": NotRequired[str],
    },
)
DescribeDatasetResponseTypeDef = TypedDict(
    "DescribeDatasetResponseTypeDef",
    {
        "CreatedBy": str,
        "CreateDate": datetime,
        "Name": str,
        "Format": InputFormatType,
        "FormatOptions": FormatOptionsTypeDef,
        "Input": InputTypeDef,
        "LastModifiedDate": datetime,
        "LastModifiedBy": str,
        "Source": SourceType,
        "PathOptions": PathOptionsTypeDef,
        "Tags": Dict[str, str],
        "ResourceArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateDatasetRequestRequestTypeDef = TypedDict(
    "UpdateDatasetRequestRequestTypeDef",
    {
        "Name": str,
        "Input": InputTypeDef,
        "Format": NotRequired[InputFormatType],
        "FormatOptions": NotRequired[FormatOptionsTypeDef],
        "PathOptions": NotRequired[PathOptionsTypeDef],
    },
)
ListRecipeVersionsResponsePaginatorTypeDef = TypedDict(
    "ListRecipeVersionsResponsePaginatorTypeDef",
    {
        "NextToken": str,
        "Recipes": List[RecipePaginatorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListRecipesResponsePaginatorTypeDef = TypedDict(
    "ListRecipesResponsePaginatorTypeDef",
    {
        "Recipes": List[RecipePaginatorTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListRecipeVersionsResponseTypeDef = TypedDict(
    "ListRecipeVersionsResponseTypeDef",
    {
        "NextToken": str,
        "Recipes": List[RecipeTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListRecipesResponseTypeDef = TypedDict(
    "ListRecipesResponseTypeDef",
    {
        "Recipes": List[RecipeTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ProfileConfigurationTypeDef = TypedDict(
    "ProfileConfigurationTypeDef",
    {
        "DatasetStatisticsConfiguration": NotRequired[StatisticsConfigurationTypeDef],
        "ProfileColumns": NotRequired[Sequence[ColumnSelectorTypeDef]],
        "ColumnStatisticsConfigurations": NotRequired[
            Sequence[ColumnStatisticsConfigurationTypeDef]
        ],
        "EntityDetectorConfiguration": NotRequired[EntityDetectorConfigurationTypeDef],
    },
)
ListJobsResponsePaginatorTypeDef = TypedDict(
    "ListJobsResponsePaginatorTypeDef",
    {
        "Jobs": List[JobPaginatorTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListJobRunsResponsePaginatorTypeDef = TypedDict(
    "ListJobRunsResponsePaginatorTypeDef",
    {
        "JobRuns": List[JobRunPaginatorTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListJobRunsResponseTypeDef = TypedDict(
    "ListJobRunsResponseTypeDef",
    {
        "JobRuns": List[JobRunTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListJobsResponseTypeDef = TypedDict(
    "ListJobsResponseTypeDef",
    {
        "Jobs": List[JobTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListDatasetsResponsePaginatorTypeDef = TypedDict(
    "ListDatasetsResponsePaginatorTypeDef",
    {
        "Datasets": List[DatasetPaginatorTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListDatasetsResponseTypeDef = TypedDict(
    "ListDatasetsResponseTypeDef",
    {
        "Datasets": List[DatasetTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateProfileJobRequestRequestTypeDef = TypedDict(
    "CreateProfileJobRequestRequestTypeDef",
    {
        "DatasetName": str,
        "Name": str,
        "OutputLocation": S3LocationTypeDef,
        "RoleArn": str,
        "EncryptionKeyArn": NotRequired[str],
        "EncryptionMode": NotRequired[EncryptionModeType],
        "LogSubscription": NotRequired[LogSubscriptionType],
        "MaxCapacity": NotRequired[int],
        "MaxRetries": NotRequired[int],
        "Configuration": NotRequired[ProfileConfigurationTypeDef],
        "ValidationConfigurations": NotRequired[Sequence[ValidationConfigurationTypeDef]],
        "Tags": NotRequired[Mapping[str, str]],
        "Timeout": NotRequired[int],
        "JobSample": NotRequired[JobSampleTypeDef],
    },
)
DescribeJobResponseTypeDef = TypedDict(
    "DescribeJobResponseTypeDef",
    {
        "CreateDate": datetime,
        "CreatedBy": str,
        "DatasetName": str,
        "EncryptionKeyArn": str,
        "EncryptionMode": EncryptionModeType,
        "Name": str,
        "Type": JobTypeType,
        "LastModifiedBy": str,
        "LastModifiedDate": datetime,
        "LogSubscription": LogSubscriptionType,
        "MaxCapacity": int,
        "MaxRetries": int,
        "Outputs": List[OutputTypeDef],
        "DataCatalogOutputs": List[DataCatalogOutputTypeDef],
        "DatabaseOutputs": List[DatabaseOutputTypeDef],
        "ProjectName": str,
        "ProfileConfiguration": ProfileConfigurationTypeDef,
        "ValidationConfigurations": List[ValidationConfigurationTypeDef],
        "RecipeReference": RecipeReferenceTypeDef,
        "ResourceArn": str,
        "RoleArn": str,
        "Tags": Dict[str, str],
        "Timeout": int,
        "JobSample": JobSampleTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeJobRunResponseTypeDef = TypedDict(
    "DescribeJobRunResponseTypeDef",
    {
        "Attempt": int,
        "CompletedOn": datetime,
        "DatasetName": str,
        "ErrorMessage": str,
        "ExecutionTime": int,
        "JobName": str,
        "ProfileConfiguration": ProfileConfigurationTypeDef,
        "ValidationConfigurations": List[ValidationConfigurationTypeDef],
        "RunId": str,
        "State": JobRunStateType,
        "LogSubscription": LogSubscriptionType,
        "LogGroupName": str,
        "Outputs": List[OutputTypeDef],
        "DataCatalogOutputs": List[DataCatalogOutputTypeDef],
        "DatabaseOutputs": List[DatabaseOutputTypeDef],
        "RecipeReference": RecipeReferenceTypeDef,
        "StartedBy": str,
        "StartedOn": datetime,
        "JobSample": JobSampleTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateProfileJobRequestRequestTypeDef = TypedDict(
    "UpdateProfileJobRequestRequestTypeDef",
    {
        "Name": str,
        "OutputLocation": S3LocationTypeDef,
        "RoleArn": str,
        "Configuration": NotRequired[ProfileConfigurationTypeDef],
        "EncryptionKeyArn": NotRequired[str],
        "EncryptionMode": NotRequired[EncryptionModeType],
        "LogSubscription": NotRequired[LogSubscriptionType],
        "MaxCapacity": NotRequired[int],
        "MaxRetries": NotRequired[int],
        "ValidationConfigurations": NotRequired[Sequence[ValidationConfigurationTypeDef]],
        "Timeout": NotRequired[int],
        "JobSample": NotRequired[JobSampleTypeDef],
    },
)
