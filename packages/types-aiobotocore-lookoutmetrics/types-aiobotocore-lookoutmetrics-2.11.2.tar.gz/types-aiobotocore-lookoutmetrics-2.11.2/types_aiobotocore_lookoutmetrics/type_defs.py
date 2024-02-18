"""
Type annotations for lookoutmetrics service type definitions.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lookoutmetrics/type_defs/)

Usage::

    ```python
    from types_aiobotocore_lookoutmetrics.type_defs import LambdaConfigurationTypeDef

    data: LambdaConfigurationTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from .literals import (
    AggregationFunctionType,
    AlertStatusType,
    AlertTypeType,
    AnomalyDetectionTaskStatusType,
    AnomalyDetectorFailureTypeType,
    AnomalyDetectorStatusType,
    ConfidenceType,
    CSVFileCompressionType,
    DataQualityMetricTypeType,
    FrequencyType,
    JsonFileCompressionType,
    RelationshipTypeType,
    SnsFormatType,
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
    "LambdaConfigurationTypeDef",
    "SNSConfigurationTypeDef",
    "ActivateAnomalyDetectorRequestRequestTypeDef",
    "DimensionFilterTypeDef",
    "AlertSummaryTypeDef",
    "AnomalyDetectorConfigSummaryTypeDef",
    "AnomalyDetectorConfigTypeDef",
    "AnomalyDetectorSummaryTypeDef",
    "ItemizedMetricStatsTypeDef",
    "AnomalyGroupSummaryTypeDef",
    "AnomalyGroupTimeSeriesFeedbackTypeDef",
    "AnomalyGroupTimeSeriesTypeDef",
    "AppFlowConfigTypeDef",
    "BackTestConfigurationTypeDef",
    "AttributeValueTypeDef",
    "AutoDetectionS3SourceConfigTypeDef",
    "BackTestAnomalyDetectorRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "MetricTypeDef",
    "TimestampColumnTypeDef",
    "CsvFormatDescriptorTypeDef",
    "DataQualityMetricTypeDef",
    "DeactivateAnomalyDetectorRequestRequestTypeDef",
    "DeleteAlertRequestRequestTypeDef",
    "DeleteAnomalyDetectorRequestRequestTypeDef",
    "DescribeAlertRequestRequestTypeDef",
    "DescribeAnomalyDetectionExecutionsRequestRequestTypeDef",
    "ExecutionStatusTypeDef",
    "DescribeAnomalyDetectorRequestRequestTypeDef",
    "DescribeMetricSetRequestRequestTypeDef",
    "DimensionValueContributionTypeDef",
    "DimensionNameValueTypeDef",
    "JsonFormatDescriptorTypeDef",
    "FilterTypeDef",
    "GetAnomalyGroupRequestRequestTypeDef",
    "GetDataQualityMetricsRequestRequestTypeDef",
    "TimeSeriesFeedbackTypeDef",
    "InterMetricImpactDetailsTypeDef",
    "ListAlertsRequestRequestTypeDef",
    "ListAnomalyDetectorsRequestRequestTypeDef",
    "ListAnomalyGroupRelatedMetricsRequestRequestTypeDef",
    "ListAnomalyGroupSummariesRequestRequestTypeDef",
    "ListAnomalyGroupTimeSeriesRequestRequestTypeDef",
    "ListMetricSetsRequestRequestTypeDef",
    "MetricSetSummaryTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "VpcConfigurationTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "ActionTypeDef",
    "AlertFiltersTypeDef",
    "CreateAnomalyDetectorRequestRequestTypeDef",
    "UpdateAnomalyDetectorRequestRequestTypeDef",
    "AnomalyGroupStatisticsTypeDef",
    "PutFeedbackRequestRequestTypeDef",
    "GetFeedbackRequestRequestTypeDef",
    "AthenaSourceConfigTypeDef",
    "CloudWatchConfigTypeDef",
    "DetectedFieldTypeDef",
    "AutoDetectionMetricSourceTypeDef",
    "CreateAlertResponseTypeDef",
    "CreateAnomalyDetectorResponseTypeDef",
    "CreateMetricSetResponseTypeDef",
    "DescribeAnomalyDetectorResponseTypeDef",
    "GetSampleDataResponseTypeDef",
    "ListAlertsResponseTypeDef",
    "ListAnomalyDetectorsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "UpdateAlertResponseTypeDef",
    "UpdateAnomalyDetectorResponseTypeDef",
    "UpdateMetricSetResponseTypeDef",
    "MetricSetDataQualityMetricTypeDef",
    "DescribeAnomalyDetectionExecutionsResponseTypeDef",
    "DimensionContributionTypeDef",
    "TimeSeriesTypeDef",
    "FileFormatDescriptorTypeDef",
    "MetricSetDimensionFilterTypeDef",
    "GetFeedbackResponseTypeDef",
    "ListAnomalyGroupRelatedMetricsResponseTypeDef",
    "ListMetricSetsResponseTypeDef",
    "RDSSourceConfigTypeDef",
    "RedshiftSourceConfigTypeDef",
    "AlertTypeDef",
    "CreateAlertRequestRequestTypeDef",
    "UpdateAlertRequestRequestTypeDef",
    "ListAnomalyGroupSummariesResponseTypeDef",
    "DetectedCsvFormatDescriptorTypeDef",
    "DetectedJsonFormatDescriptorTypeDef",
    "DetectMetricSetConfigRequestRequestTypeDef",
    "AnomalyDetectorDataQualityMetricTypeDef",
    "ContributionMatrixTypeDef",
    "ListAnomalyGroupTimeSeriesResponseTypeDef",
    "S3SourceConfigTypeDef",
    "SampleDataS3SourceConfigTypeDef",
    "DescribeAlertResponseTypeDef",
    "DetectedFileFormatDescriptorTypeDef",
    "GetDataQualityMetricsResponseTypeDef",
    "MetricLevelImpactTypeDef",
    "MetricSourceTypeDef",
    "GetSampleDataRequestRequestTypeDef",
    "DetectedS3SourceConfigTypeDef",
    "AnomalyGroupTypeDef",
    "CreateMetricSetRequestRequestTypeDef",
    "DescribeMetricSetResponseTypeDef",
    "UpdateMetricSetRequestRequestTypeDef",
    "DetectedMetricSourceTypeDef",
    "GetAnomalyGroupResponseTypeDef",
    "DetectedMetricSetConfigTypeDef",
    "DetectMetricSetConfigResponseTypeDef",
)

LambdaConfigurationTypeDef = TypedDict(
    "LambdaConfigurationTypeDef",
    {
        "RoleArn": str,
        "LambdaArn": str,
    },
)
SNSConfigurationTypeDef = TypedDict(
    "SNSConfigurationTypeDef",
    {
        "RoleArn": str,
        "SnsTopicArn": str,
        "SnsFormat": NotRequired[SnsFormatType],
    },
)
ActivateAnomalyDetectorRequestRequestTypeDef = TypedDict(
    "ActivateAnomalyDetectorRequestRequestTypeDef",
    {
        "AnomalyDetectorArn": str,
    },
)
DimensionFilterTypeDef = TypedDict(
    "DimensionFilterTypeDef",
    {
        "DimensionName": NotRequired[str],
        "DimensionValueList": NotRequired[Sequence[str]],
    },
)
AlertSummaryTypeDef = TypedDict(
    "AlertSummaryTypeDef",
    {
        "AlertArn": NotRequired[str],
        "AnomalyDetectorArn": NotRequired[str],
        "AlertName": NotRequired[str],
        "AlertSensitivityThreshold": NotRequired[int],
        "AlertType": NotRequired[AlertTypeType],
        "AlertStatus": NotRequired[AlertStatusType],
        "LastModificationTime": NotRequired[datetime],
        "CreationTime": NotRequired[datetime],
        "Tags": NotRequired[Dict[str, str]],
    },
)
AnomalyDetectorConfigSummaryTypeDef = TypedDict(
    "AnomalyDetectorConfigSummaryTypeDef",
    {
        "AnomalyDetectorFrequency": NotRequired[FrequencyType],
    },
)
AnomalyDetectorConfigTypeDef = TypedDict(
    "AnomalyDetectorConfigTypeDef",
    {
        "AnomalyDetectorFrequency": NotRequired[FrequencyType],
    },
)
AnomalyDetectorSummaryTypeDef = TypedDict(
    "AnomalyDetectorSummaryTypeDef",
    {
        "AnomalyDetectorArn": NotRequired[str],
        "AnomalyDetectorName": NotRequired[str],
        "AnomalyDetectorDescription": NotRequired[str],
        "CreationTime": NotRequired[datetime],
        "LastModificationTime": NotRequired[datetime],
        "Status": NotRequired[AnomalyDetectorStatusType],
        "Tags": NotRequired[Dict[str, str]],
    },
)
ItemizedMetricStatsTypeDef = TypedDict(
    "ItemizedMetricStatsTypeDef",
    {
        "MetricName": NotRequired[str],
        "OccurrenceCount": NotRequired[int],
    },
)
AnomalyGroupSummaryTypeDef = TypedDict(
    "AnomalyGroupSummaryTypeDef",
    {
        "StartTime": NotRequired[str],
        "EndTime": NotRequired[str],
        "AnomalyGroupId": NotRequired[str],
        "AnomalyGroupScore": NotRequired[float],
        "PrimaryMetricName": NotRequired[str],
    },
)
AnomalyGroupTimeSeriesFeedbackTypeDef = TypedDict(
    "AnomalyGroupTimeSeriesFeedbackTypeDef",
    {
        "AnomalyGroupId": str,
        "TimeSeriesId": str,
        "IsAnomaly": bool,
    },
)
AnomalyGroupTimeSeriesTypeDef = TypedDict(
    "AnomalyGroupTimeSeriesTypeDef",
    {
        "AnomalyGroupId": str,
        "TimeSeriesId": NotRequired[str],
    },
)
AppFlowConfigTypeDef = TypedDict(
    "AppFlowConfigTypeDef",
    {
        "RoleArn": NotRequired[str],
        "FlowName": NotRequired[str],
    },
)
BackTestConfigurationTypeDef = TypedDict(
    "BackTestConfigurationTypeDef",
    {
        "RunBackTestMode": bool,
    },
)
AttributeValueTypeDef = TypedDict(
    "AttributeValueTypeDef",
    {
        "S": NotRequired[str],
        "N": NotRequired[str],
        "B": NotRequired[str],
        "SS": NotRequired[List[str]],
        "NS": NotRequired[List[str]],
        "BS": NotRequired[List[str]],
    },
)
AutoDetectionS3SourceConfigTypeDef = TypedDict(
    "AutoDetectionS3SourceConfigTypeDef",
    {
        "TemplatedPathList": NotRequired[Sequence[str]],
        "HistoricalDataPathList": NotRequired[Sequence[str]],
    },
)
BackTestAnomalyDetectorRequestRequestTypeDef = TypedDict(
    "BackTestAnomalyDetectorRequestRequestTypeDef",
    {
        "AnomalyDetectorArn": str,
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
MetricTypeDef = TypedDict(
    "MetricTypeDef",
    {
        "MetricName": str,
        "AggregationFunction": AggregationFunctionType,
        "Namespace": NotRequired[str],
    },
)
TimestampColumnTypeDef = TypedDict(
    "TimestampColumnTypeDef",
    {
        "ColumnName": NotRequired[str],
        "ColumnFormat": NotRequired[str],
    },
)
CsvFormatDescriptorTypeDef = TypedDict(
    "CsvFormatDescriptorTypeDef",
    {
        "FileCompression": NotRequired[CSVFileCompressionType],
        "Charset": NotRequired[str],
        "ContainsHeader": NotRequired[bool],
        "Delimiter": NotRequired[str],
        "HeaderList": NotRequired[Sequence[str]],
        "QuoteSymbol": NotRequired[str],
    },
)
DataQualityMetricTypeDef = TypedDict(
    "DataQualityMetricTypeDef",
    {
        "MetricType": NotRequired[DataQualityMetricTypeType],
        "MetricDescription": NotRequired[str],
        "RelatedColumnName": NotRequired[str],
        "MetricValue": NotRequired[float],
    },
)
DeactivateAnomalyDetectorRequestRequestTypeDef = TypedDict(
    "DeactivateAnomalyDetectorRequestRequestTypeDef",
    {
        "AnomalyDetectorArn": str,
    },
)
DeleteAlertRequestRequestTypeDef = TypedDict(
    "DeleteAlertRequestRequestTypeDef",
    {
        "AlertArn": str,
    },
)
DeleteAnomalyDetectorRequestRequestTypeDef = TypedDict(
    "DeleteAnomalyDetectorRequestRequestTypeDef",
    {
        "AnomalyDetectorArn": str,
    },
)
DescribeAlertRequestRequestTypeDef = TypedDict(
    "DescribeAlertRequestRequestTypeDef",
    {
        "AlertArn": str,
    },
)
DescribeAnomalyDetectionExecutionsRequestRequestTypeDef = TypedDict(
    "DescribeAnomalyDetectionExecutionsRequestRequestTypeDef",
    {
        "AnomalyDetectorArn": str,
        "Timestamp": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ExecutionStatusTypeDef = TypedDict(
    "ExecutionStatusTypeDef",
    {
        "Timestamp": NotRequired[str],
        "Status": NotRequired[AnomalyDetectionTaskStatusType],
        "FailureReason": NotRequired[str],
    },
)
DescribeAnomalyDetectorRequestRequestTypeDef = TypedDict(
    "DescribeAnomalyDetectorRequestRequestTypeDef",
    {
        "AnomalyDetectorArn": str,
    },
)
DescribeMetricSetRequestRequestTypeDef = TypedDict(
    "DescribeMetricSetRequestRequestTypeDef",
    {
        "MetricSetArn": str,
    },
)
DimensionValueContributionTypeDef = TypedDict(
    "DimensionValueContributionTypeDef",
    {
        "DimensionValue": NotRequired[str],
        "ContributionScore": NotRequired[float],
    },
)
DimensionNameValueTypeDef = TypedDict(
    "DimensionNameValueTypeDef",
    {
        "DimensionName": str,
        "DimensionValue": str,
    },
)
JsonFormatDescriptorTypeDef = TypedDict(
    "JsonFormatDescriptorTypeDef",
    {
        "FileCompression": NotRequired[JsonFileCompressionType],
        "Charset": NotRequired[str],
    },
)
FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "DimensionValue": NotRequired[str],
        "FilterOperation": NotRequired[Literal["EQUALS"]],
    },
)
GetAnomalyGroupRequestRequestTypeDef = TypedDict(
    "GetAnomalyGroupRequestRequestTypeDef",
    {
        "AnomalyGroupId": str,
        "AnomalyDetectorArn": str,
    },
)
GetDataQualityMetricsRequestRequestTypeDef = TypedDict(
    "GetDataQualityMetricsRequestRequestTypeDef",
    {
        "AnomalyDetectorArn": str,
        "MetricSetArn": NotRequired[str],
    },
)
TimeSeriesFeedbackTypeDef = TypedDict(
    "TimeSeriesFeedbackTypeDef",
    {
        "TimeSeriesId": NotRequired[str],
        "IsAnomaly": NotRequired[bool],
    },
)
InterMetricImpactDetailsTypeDef = TypedDict(
    "InterMetricImpactDetailsTypeDef",
    {
        "MetricName": NotRequired[str],
        "AnomalyGroupId": NotRequired[str],
        "RelationshipType": NotRequired[RelationshipTypeType],
        "ContributionPercentage": NotRequired[float],
    },
)
ListAlertsRequestRequestTypeDef = TypedDict(
    "ListAlertsRequestRequestTypeDef",
    {
        "AnomalyDetectorArn": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListAnomalyDetectorsRequestRequestTypeDef = TypedDict(
    "ListAnomalyDetectorsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListAnomalyGroupRelatedMetricsRequestRequestTypeDef = TypedDict(
    "ListAnomalyGroupRelatedMetricsRequestRequestTypeDef",
    {
        "AnomalyDetectorArn": str,
        "AnomalyGroupId": str,
        "RelationshipTypeFilter": NotRequired[RelationshipTypeType],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListAnomalyGroupSummariesRequestRequestTypeDef = TypedDict(
    "ListAnomalyGroupSummariesRequestRequestTypeDef",
    {
        "AnomalyDetectorArn": str,
        "SensitivityThreshold": int,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListAnomalyGroupTimeSeriesRequestRequestTypeDef = TypedDict(
    "ListAnomalyGroupTimeSeriesRequestRequestTypeDef",
    {
        "AnomalyDetectorArn": str,
        "AnomalyGroupId": str,
        "MetricName": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListMetricSetsRequestRequestTypeDef = TypedDict(
    "ListMetricSetsRequestRequestTypeDef",
    {
        "AnomalyDetectorArn": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
MetricSetSummaryTypeDef = TypedDict(
    "MetricSetSummaryTypeDef",
    {
        "MetricSetArn": NotRequired[str],
        "AnomalyDetectorArn": NotRequired[str],
        "MetricSetDescription": NotRequired[str],
        "MetricSetName": NotRequired[str],
        "CreationTime": NotRequired[datetime],
        "LastModificationTime": NotRequired[datetime],
        "Tags": NotRequired[Dict[str, str]],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
VpcConfigurationTypeDef = TypedDict(
    "VpcConfigurationTypeDef",
    {
        "SubnetIdList": Sequence[str],
        "SecurityGroupIdList": Sequence[str],
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
ActionTypeDef = TypedDict(
    "ActionTypeDef",
    {
        "SNSConfiguration": NotRequired[SNSConfigurationTypeDef],
        "LambdaConfiguration": NotRequired[LambdaConfigurationTypeDef],
    },
)
AlertFiltersTypeDef = TypedDict(
    "AlertFiltersTypeDef",
    {
        "MetricList": NotRequired[Sequence[str]],
        "DimensionFilterList": NotRequired[Sequence[DimensionFilterTypeDef]],
    },
)
CreateAnomalyDetectorRequestRequestTypeDef = TypedDict(
    "CreateAnomalyDetectorRequestRequestTypeDef",
    {
        "AnomalyDetectorName": str,
        "AnomalyDetectorConfig": AnomalyDetectorConfigTypeDef,
        "AnomalyDetectorDescription": NotRequired[str],
        "KmsKeyArn": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
UpdateAnomalyDetectorRequestRequestTypeDef = TypedDict(
    "UpdateAnomalyDetectorRequestRequestTypeDef",
    {
        "AnomalyDetectorArn": str,
        "KmsKeyArn": NotRequired[str],
        "AnomalyDetectorDescription": NotRequired[str],
        "AnomalyDetectorConfig": NotRequired[AnomalyDetectorConfigTypeDef],
    },
)
AnomalyGroupStatisticsTypeDef = TypedDict(
    "AnomalyGroupStatisticsTypeDef",
    {
        "EvaluationStartDate": NotRequired[str],
        "TotalCount": NotRequired[int],
        "ItemizedMetricStatsList": NotRequired[List[ItemizedMetricStatsTypeDef]],
    },
)
PutFeedbackRequestRequestTypeDef = TypedDict(
    "PutFeedbackRequestRequestTypeDef",
    {
        "AnomalyDetectorArn": str,
        "AnomalyGroupTimeSeriesFeedback": AnomalyGroupTimeSeriesFeedbackTypeDef,
    },
)
GetFeedbackRequestRequestTypeDef = TypedDict(
    "GetFeedbackRequestRequestTypeDef",
    {
        "AnomalyDetectorArn": str,
        "AnomalyGroupTimeSeriesFeedback": AnomalyGroupTimeSeriesTypeDef,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
AthenaSourceConfigTypeDef = TypedDict(
    "AthenaSourceConfigTypeDef",
    {
        "RoleArn": NotRequired[str],
        "DatabaseName": NotRequired[str],
        "DataCatalog": NotRequired[str],
        "TableName": NotRequired[str],
        "WorkGroupName": NotRequired[str],
        "S3ResultsPath": NotRequired[str],
        "BackTestConfiguration": NotRequired[BackTestConfigurationTypeDef],
    },
)
CloudWatchConfigTypeDef = TypedDict(
    "CloudWatchConfigTypeDef",
    {
        "RoleArn": NotRequired[str],
        "BackTestConfiguration": NotRequired[BackTestConfigurationTypeDef],
    },
)
DetectedFieldTypeDef = TypedDict(
    "DetectedFieldTypeDef",
    {
        "Value": NotRequired[AttributeValueTypeDef],
        "Confidence": NotRequired[ConfidenceType],
        "Message": NotRequired[str],
    },
)
AutoDetectionMetricSourceTypeDef = TypedDict(
    "AutoDetectionMetricSourceTypeDef",
    {
        "S3SourceConfig": NotRequired[AutoDetectionS3SourceConfigTypeDef],
    },
)
CreateAlertResponseTypeDef = TypedDict(
    "CreateAlertResponseTypeDef",
    {
        "AlertArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateAnomalyDetectorResponseTypeDef = TypedDict(
    "CreateAnomalyDetectorResponseTypeDef",
    {
        "AnomalyDetectorArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateMetricSetResponseTypeDef = TypedDict(
    "CreateMetricSetResponseTypeDef",
    {
        "MetricSetArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeAnomalyDetectorResponseTypeDef = TypedDict(
    "DescribeAnomalyDetectorResponseTypeDef",
    {
        "AnomalyDetectorArn": str,
        "AnomalyDetectorName": str,
        "AnomalyDetectorDescription": str,
        "AnomalyDetectorConfig": AnomalyDetectorConfigSummaryTypeDef,
        "CreationTime": datetime,
        "LastModificationTime": datetime,
        "Status": AnomalyDetectorStatusType,
        "FailureReason": str,
        "KmsKeyArn": str,
        "FailureType": AnomalyDetectorFailureTypeType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSampleDataResponseTypeDef = TypedDict(
    "GetSampleDataResponseTypeDef",
    {
        "HeaderValues": List[str],
        "SampleRows": List[List[str]],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAlertsResponseTypeDef = TypedDict(
    "ListAlertsResponseTypeDef",
    {
        "AlertSummaryList": List[AlertSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAnomalyDetectorsResponseTypeDef = TypedDict(
    "ListAnomalyDetectorsResponseTypeDef",
    {
        "AnomalyDetectorSummaryList": List[AnomalyDetectorSummaryTypeDef],
        "NextToken": str,
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
UpdateAlertResponseTypeDef = TypedDict(
    "UpdateAlertResponseTypeDef",
    {
        "AlertArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateAnomalyDetectorResponseTypeDef = TypedDict(
    "UpdateAnomalyDetectorResponseTypeDef",
    {
        "AnomalyDetectorArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateMetricSetResponseTypeDef = TypedDict(
    "UpdateMetricSetResponseTypeDef",
    {
        "MetricSetArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
MetricSetDataQualityMetricTypeDef = TypedDict(
    "MetricSetDataQualityMetricTypeDef",
    {
        "MetricSetArn": NotRequired[str],
        "DataQualityMetricList": NotRequired[List[DataQualityMetricTypeDef]],
    },
)
DescribeAnomalyDetectionExecutionsResponseTypeDef = TypedDict(
    "DescribeAnomalyDetectionExecutionsResponseTypeDef",
    {
        "ExecutionList": List[ExecutionStatusTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DimensionContributionTypeDef = TypedDict(
    "DimensionContributionTypeDef",
    {
        "DimensionName": NotRequired[str],
        "DimensionValueContributionList": NotRequired[List[DimensionValueContributionTypeDef]],
    },
)
TimeSeriesTypeDef = TypedDict(
    "TimeSeriesTypeDef",
    {
        "TimeSeriesId": str,
        "DimensionList": List[DimensionNameValueTypeDef],
        "MetricValueList": List[float],
    },
)
FileFormatDescriptorTypeDef = TypedDict(
    "FileFormatDescriptorTypeDef",
    {
        "CsvFormatDescriptor": NotRequired[CsvFormatDescriptorTypeDef],
        "JsonFormatDescriptor": NotRequired[JsonFormatDescriptorTypeDef],
    },
)
MetricSetDimensionFilterTypeDef = TypedDict(
    "MetricSetDimensionFilterTypeDef",
    {
        "Name": NotRequired[str],
        "FilterList": NotRequired[Sequence[FilterTypeDef]],
    },
)
GetFeedbackResponseTypeDef = TypedDict(
    "GetFeedbackResponseTypeDef",
    {
        "AnomalyGroupTimeSeriesFeedback": List[TimeSeriesFeedbackTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAnomalyGroupRelatedMetricsResponseTypeDef = TypedDict(
    "ListAnomalyGroupRelatedMetricsResponseTypeDef",
    {
        "InterMetricImpactList": List[InterMetricImpactDetailsTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListMetricSetsResponseTypeDef = TypedDict(
    "ListMetricSetsResponseTypeDef",
    {
        "MetricSetSummaryList": List[MetricSetSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RDSSourceConfigTypeDef = TypedDict(
    "RDSSourceConfigTypeDef",
    {
        "DBInstanceIdentifier": NotRequired[str],
        "DatabaseHost": NotRequired[str],
        "DatabasePort": NotRequired[int],
        "SecretManagerArn": NotRequired[str],
        "DatabaseName": NotRequired[str],
        "TableName": NotRequired[str],
        "RoleArn": NotRequired[str],
        "VpcConfiguration": NotRequired[VpcConfigurationTypeDef],
    },
)
RedshiftSourceConfigTypeDef = TypedDict(
    "RedshiftSourceConfigTypeDef",
    {
        "ClusterIdentifier": NotRequired[str],
        "DatabaseHost": NotRequired[str],
        "DatabasePort": NotRequired[int],
        "SecretManagerArn": NotRequired[str],
        "DatabaseName": NotRequired[str],
        "TableName": NotRequired[str],
        "RoleArn": NotRequired[str],
        "VpcConfiguration": NotRequired[VpcConfigurationTypeDef],
    },
)
AlertTypeDef = TypedDict(
    "AlertTypeDef",
    {
        "Action": NotRequired[ActionTypeDef],
        "AlertDescription": NotRequired[str],
        "AlertArn": NotRequired[str],
        "AnomalyDetectorArn": NotRequired[str],
        "AlertName": NotRequired[str],
        "AlertSensitivityThreshold": NotRequired[int],
        "AlertType": NotRequired[AlertTypeType],
        "AlertStatus": NotRequired[AlertStatusType],
        "LastModificationTime": NotRequired[datetime],
        "CreationTime": NotRequired[datetime],
        "AlertFilters": NotRequired[AlertFiltersTypeDef],
    },
)
CreateAlertRequestRequestTypeDef = TypedDict(
    "CreateAlertRequestRequestTypeDef",
    {
        "AlertName": str,
        "AnomalyDetectorArn": str,
        "Action": ActionTypeDef,
        "AlertSensitivityThreshold": NotRequired[int],
        "AlertDescription": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
        "AlertFilters": NotRequired[AlertFiltersTypeDef],
    },
)
UpdateAlertRequestRequestTypeDef = TypedDict(
    "UpdateAlertRequestRequestTypeDef",
    {
        "AlertArn": str,
        "AlertDescription": NotRequired[str],
        "AlertSensitivityThreshold": NotRequired[int],
        "Action": NotRequired[ActionTypeDef],
        "AlertFilters": NotRequired[AlertFiltersTypeDef],
    },
)
ListAnomalyGroupSummariesResponseTypeDef = TypedDict(
    "ListAnomalyGroupSummariesResponseTypeDef",
    {
        "AnomalyGroupSummaryList": List[AnomalyGroupSummaryTypeDef],
        "AnomalyGroupStatistics": AnomalyGroupStatisticsTypeDef,
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DetectedCsvFormatDescriptorTypeDef = TypedDict(
    "DetectedCsvFormatDescriptorTypeDef",
    {
        "FileCompression": NotRequired[DetectedFieldTypeDef],
        "Charset": NotRequired[DetectedFieldTypeDef],
        "ContainsHeader": NotRequired[DetectedFieldTypeDef],
        "Delimiter": NotRequired[DetectedFieldTypeDef],
        "HeaderList": NotRequired[DetectedFieldTypeDef],
        "QuoteSymbol": NotRequired[DetectedFieldTypeDef],
    },
)
DetectedJsonFormatDescriptorTypeDef = TypedDict(
    "DetectedJsonFormatDescriptorTypeDef",
    {
        "FileCompression": NotRequired[DetectedFieldTypeDef],
        "Charset": NotRequired[DetectedFieldTypeDef],
    },
)
DetectMetricSetConfigRequestRequestTypeDef = TypedDict(
    "DetectMetricSetConfigRequestRequestTypeDef",
    {
        "AnomalyDetectorArn": str,
        "AutoDetectionMetricSource": AutoDetectionMetricSourceTypeDef,
    },
)
AnomalyDetectorDataQualityMetricTypeDef = TypedDict(
    "AnomalyDetectorDataQualityMetricTypeDef",
    {
        "StartTimestamp": NotRequired[datetime],
        "MetricSetDataQualityMetricList": NotRequired[List[MetricSetDataQualityMetricTypeDef]],
    },
)
ContributionMatrixTypeDef = TypedDict(
    "ContributionMatrixTypeDef",
    {
        "DimensionContributionList": NotRequired[List[DimensionContributionTypeDef]],
    },
)
ListAnomalyGroupTimeSeriesResponseTypeDef = TypedDict(
    "ListAnomalyGroupTimeSeriesResponseTypeDef",
    {
        "AnomalyGroupId": str,
        "MetricName": str,
        "TimestampList": List[str],
        "NextToken": str,
        "TimeSeriesList": List[TimeSeriesTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
S3SourceConfigTypeDef = TypedDict(
    "S3SourceConfigTypeDef",
    {
        "RoleArn": NotRequired[str],
        "TemplatedPathList": NotRequired[Sequence[str]],
        "HistoricalDataPathList": NotRequired[Sequence[str]],
        "FileFormatDescriptor": NotRequired[FileFormatDescriptorTypeDef],
    },
)
SampleDataS3SourceConfigTypeDef = TypedDict(
    "SampleDataS3SourceConfigTypeDef",
    {
        "RoleArn": str,
        "FileFormatDescriptor": FileFormatDescriptorTypeDef,
        "TemplatedPathList": NotRequired[Sequence[str]],
        "HistoricalDataPathList": NotRequired[Sequence[str]],
    },
)
DescribeAlertResponseTypeDef = TypedDict(
    "DescribeAlertResponseTypeDef",
    {
        "Alert": AlertTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DetectedFileFormatDescriptorTypeDef = TypedDict(
    "DetectedFileFormatDescriptorTypeDef",
    {
        "CsvFormatDescriptor": NotRequired[DetectedCsvFormatDescriptorTypeDef],
        "JsonFormatDescriptor": NotRequired[DetectedJsonFormatDescriptorTypeDef],
    },
)
GetDataQualityMetricsResponseTypeDef = TypedDict(
    "GetDataQualityMetricsResponseTypeDef",
    {
        "AnomalyDetectorDataQualityMetricList": List[AnomalyDetectorDataQualityMetricTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
MetricLevelImpactTypeDef = TypedDict(
    "MetricLevelImpactTypeDef",
    {
        "MetricName": NotRequired[str],
        "NumTimeSeries": NotRequired[int],
        "ContributionMatrix": NotRequired[ContributionMatrixTypeDef],
    },
)
MetricSourceTypeDef = TypedDict(
    "MetricSourceTypeDef",
    {
        "S3SourceConfig": NotRequired[S3SourceConfigTypeDef],
        "AppFlowConfig": NotRequired[AppFlowConfigTypeDef],
        "CloudWatchConfig": NotRequired[CloudWatchConfigTypeDef],
        "RDSSourceConfig": NotRequired[RDSSourceConfigTypeDef],
        "RedshiftSourceConfig": NotRequired[RedshiftSourceConfigTypeDef],
        "AthenaSourceConfig": NotRequired[AthenaSourceConfigTypeDef],
    },
)
GetSampleDataRequestRequestTypeDef = TypedDict(
    "GetSampleDataRequestRequestTypeDef",
    {
        "S3SourceConfig": NotRequired[SampleDataS3SourceConfigTypeDef],
    },
)
DetectedS3SourceConfigTypeDef = TypedDict(
    "DetectedS3SourceConfigTypeDef",
    {
        "FileFormatDescriptor": NotRequired[DetectedFileFormatDescriptorTypeDef],
    },
)
AnomalyGroupTypeDef = TypedDict(
    "AnomalyGroupTypeDef",
    {
        "StartTime": NotRequired[str],
        "EndTime": NotRequired[str],
        "AnomalyGroupId": NotRequired[str],
        "AnomalyGroupScore": NotRequired[float],
        "PrimaryMetricName": NotRequired[str],
        "MetricLevelImpactList": NotRequired[List[MetricLevelImpactTypeDef]],
    },
)
CreateMetricSetRequestRequestTypeDef = TypedDict(
    "CreateMetricSetRequestRequestTypeDef",
    {
        "AnomalyDetectorArn": str,
        "MetricSetName": str,
        "MetricList": Sequence[MetricTypeDef],
        "MetricSource": MetricSourceTypeDef,
        "MetricSetDescription": NotRequired[str],
        "Offset": NotRequired[int],
        "TimestampColumn": NotRequired[TimestampColumnTypeDef],
        "DimensionList": NotRequired[Sequence[str]],
        "MetricSetFrequency": NotRequired[FrequencyType],
        "Timezone": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
        "DimensionFilterList": NotRequired[Sequence[MetricSetDimensionFilterTypeDef]],
    },
)
DescribeMetricSetResponseTypeDef = TypedDict(
    "DescribeMetricSetResponseTypeDef",
    {
        "MetricSetArn": str,
        "AnomalyDetectorArn": str,
        "MetricSetName": str,
        "MetricSetDescription": str,
        "CreationTime": datetime,
        "LastModificationTime": datetime,
        "Offset": int,
        "MetricList": List[MetricTypeDef],
        "TimestampColumn": TimestampColumnTypeDef,
        "DimensionList": List[str],
        "MetricSetFrequency": FrequencyType,
        "Timezone": str,
        "MetricSource": MetricSourceTypeDef,
        "DimensionFilterList": List[MetricSetDimensionFilterTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateMetricSetRequestRequestTypeDef = TypedDict(
    "UpdateMetricSetRequestRequestTypeDef",
    {
        "MetricSetArn": str,
        "MetricSetDescription": NotRequired[str],
        "MetricList": NotRequired[Sequence[MetricTypeDef]],
        "Offset": NotRequired[int],
        "TimestampColumn": NotRequired[TimestampColumnTypeDef],
        "DimensionList": NotRequired[Sequence[str]],
        "MetricSetFrequency": NotRequired[FrequencyType],
        "MetricSource": NotRequired[MetricSourceTypeDef],
        "DimensionFilterList": NotRequired[Sequence[MetricSetDimensionFilterTypeDef]],
    },
)
DetectedMetricSourceTypeDef = TypedDict(
    "DetectedMetricSourceTypeDef",
    {
        "S3SourceConfig": NotRequired[DetectedS3SourceConfigTypeDef],
    },
)
GetAnomalyGroupResponseTypeDef = TypedDict(
    "GetAnomalyGroupResponseTypeDef",
    {
        "AnomalyGroup": AnomalyGroupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DetectedMetricSetConfigTypeDef = TypedDict(
    "DetectedMetricSetConfigTypeDef",
    {
        "Offset": NotRequired[DetectedFieldTypeDef],
        "MetricSetFrequency": NotRequired[DetectedFieldTypeDef],
        "MetricSource": NotRequired[DetectedMetricSourceTypeDef],
    },
)
DetectMetricSetConfigResponseTypeDef = TypedDict(
    "DetectMetricSetConfigResponseTypeDef",
    {
        "DetectedMetricSetConfig": DetectedMetricSetConfigTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
