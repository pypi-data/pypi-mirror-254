"""
Type annotations for migrationhubstrategy service type definitions.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_migrationhubstrategy/type_defs/)

Usage::

    ```python
    from types_aiobotocore_migrationhubstrategy.type_defs import AnalysisStatusUnionTypeDef

    data: AnalysisStatusUnionTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Sequence

from .literals import (
    AnalysisTypeType,
    AntipatternReportStatusType,
    ApplicationComponentCriteriaType,
    ApplicationModeType,
    AppTypeType,
    AppUnitErrorCategoryType,
    AssessmentDataSourceTypeType,
    AssessmentStatusType,
    AuthTypeType,
    AwsManagedTargetDestinationType,
    BinaryAnalyzerNameType,
    CollectorHealthType,
    ConditionType,
    DatabaseManagementPreferenceType,
    DataSourceTypeType,
    GroupNameType,
    HeterogeneousTargetDatabaseEngineType,
    ImportFileTaskStatusType,
    InclusionStatusType,
    NoPreferenceTargetDestinationType,
    OSTypeType,
    OutputFormatType,
    RecommendationReportStatusType,
    ResourceSubTypeType,
    RuntimeAnalysisStatusType,
    RunTimeAnalyzerNameType,
    RunTimeAssessmentStatusType,
    SelfManageTargetDestinationType,
    ServerCriteriaType,
    ServerErrorCategoryType,
    ServerOsTypeType,
    SeverityType,
    SortOrderType,
    SourceCodeAnalyzerNameType,
    SrcCodeOrDbAnalysisStatusType,
    StrategyRecommendationType,
    StrategyType,
    TargetDatabaseEngineType,
    TargetDestinationType,
    TransformationToolNameType,
    VersionControlType,
    VersionControlTypeType,
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
    "AnalysisStatusUnionTypeDef",
    "AnalyzableServerSummaryTypeDef",
    "AnalyzerNameUnionTypeDef",
    "S3ObjectTypeDef",
    "AntipatternSeveritySummaryTypeDef",
    "AppUnitErrorTypeDef",
    "DatabaseConfigDetailTypeDef",
    "SourceCodeRepositoryTypeDef",
    "ApplicationComponentStatusSummaryTypeDef",
    "ApplicationComponentSummaryTypeDef",
    "ServerStatusSummaryTypeDef",
    "ServerSummaryTypeDef",
    "StrategySummaryTypeDef",
    "AssessmentTargetTypeDef",
    "AssociatedApplicationTypeDef",
    "AwsManagedResourcesTypeDef",
    "BusinessGoalsTypeDef",
    "IPAddressBasedRemoteInfoTypeDef",
    "PipelineInfoTypeDef",
    "RemoteSourceCodeAnalysisServerInfoTypeDef",
    "VcenterBasedRemoteInfoTypeDef",
    "VersionControlInfoTypeDef",
    "DataCollectionDetailsTypeDef",
    "HeterogeneousTypeDef",
    "HomogeneousTypeDef",
    "NoDatabaseMigrationPreferenceTypeDef",
    "GetApplicationComponentDetailsRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "GetApplicationComponentStrategiesRequestRequestTypeDef",
    "GetAssessmentRequestRequestTypeDef",
    "GetImportFileTaskRequestRequestTypeDef",
    "GetRecommendationReportDetailsRequestRequestTypeDef",
    "RecommendationReportDetailsTypeDef",
    "PaginatorConfigTypeDef",
    "GetServerDetailsRequestRequestTypeDef",
    "GetServerStrategiesRequestRequestTypeDef",
    "GroupTypeDef",
    "ImportFileTaskInformationTypeDef",
    "ListAnalyzableServersRequestRequestTypeDef",
    "ListCollectorsRequestRequestTypeDef",
    "ListImportFileTaskRequestRequestTypeDef",
    "NoManagementPreferenceTypeDef",
    "SelfManageResourcesTypeDef",
    "NetworkInfoTypeDef",
    "OSInfoTypeDef",
    "TransformationToolTypeDef",
    "ServerErrorTypeDef",
    "SourceCodeTypeDef",
    "StopAssessmentRequestRequestTypeDef",
    "StrategyOptionTypeDef",
    "AntipatternReportResultTypeDef",
    "AssessmentSummaryTypeDef",
    "StartAssessmentRequestRequestTypeDef",
    "PrioritizeBusinessGoalsTypeDef",
    "ConfigurationSummaryTypeDef",
    "DatabaseMigrationPreferenceTypeDef",
    "GetAssessmentResponseTypeDef",
    "GetImportFileTaskResponseTypeDef",
    "GetLatestAssessmentIdResponseTypeDef",
    "ListAnalyzableServersResponseTypeDef",
    "StartAssessmentResponseTypeDef",
    "StartImportFileTaskResponseTypeDef",
    "StartRecommendationReportGenerationResponseTypeDef",
    "GetRecommendationReportDetailsResponseTypeDef",
    "GetServerDetailsRequestGetServerDetailsPaginateTypeDef",
    "ListAnalyzableServersRequestListAnalyzableServersPaginateTypeDef",
    "ListCollectorsRequestListCollectorsPaginateTypeDef",
    "ListImportFileTaskRequestListImportFileTaskPaginateTypeDef",
    "ListApplicationComponentsRequestListApplicationComponentsPaginateTypeDef",
    "ListApplicationComponentsRequestRequestTypeDef",
    "ListServersRequestListServersPaginateTypeDef",
    "ListServersRequestRequestTypeDef",
    "StartImportFileTaskRequestRequestTypeDef",
    "StartRecommendationReportGenerationRequestRequestTypeDef",
    "ListImportFileTaskResponseTypeDef",
    "ManagementPreferenceTypeDef",
    "SystemInfoTypeDef",
    "RecommendationSetTypeDef",
    "UpdateApplicationComponentConfigRequestRequestTypeDef",
    "UpdateServerConfigRequestRequestTypeDef",
    "ResultTypeDef",
    "GetPortfolioSummaryResponseTypeDef",
    "CollectorTypeDef",
    "DatabasePreferencesTypeDef",
    "ApplicationPreferencesTypeDef",
    "ApplicationComponentStrategyTypeDef",
    "ServerDetailTypeDef",
    "ServerStrategyTypeDef",
    "ApplicationComponentDetailTypeDef",
    "ListCollectorsResponseTypeDef",
    "GetPortfolioPreferencesResponseTypeDef",
    "PutPortfolioPreferencesRequestRequestTypeDef",
    "GetApplicationComponentStrategiesResponseTypeDef",
    "GetServerDetailsResponseTypeDef",
    "ListServersResponseTypeDef",
    "GetServerStrategiesResponseTypeDef",
    "GetApplicationComponentDetailsResponseTypeDef",
    "ListApplicationComponentsResponseTypeDef",
)

AnalysisStatusUnionTypeDef = TypedDict(
    "AnalysisStatusUnionTypeDef",
    {
        "runtimeAnalysisStatus": NotRequired[RuntimeAnalysisStatusType],
        "srcCodeOrDbAnalysisStatus": NotRequired[SrcCodeOrDbAnalysisStatusType],
    },
)
AnalyzableServerSummaryTypeDef = TypedDict(
    "AnalyzableServerSummaryTypeDef",
    {
        "hostname": NotRequired[str],
        "ipAddress": NotRequired[str],
        "source": NotRequired[str],
        "vmId": NotRequired[str],
    },
)
AnalyzerNameUnionTypeDef = TypedDict(
    "AnalyzerNameUnionTypeDef",
    {
        "binaryAnalyzerName": NotRequired[BinaryAnalyzerNameType],
        "runTimeAnalyzerName": NotRequired[RunTimeAnalyzerNameType],
        "sourceCodeAnalyzerName": NotRequired[SourceCodeAnalyzerNameType],
    },
)
S3ObjectTypeDef = TypedDict(
    "S3ObjectTypeDef",
    {
        "s3Bucket": NotRequired[str],
        "s3key": NotRequired[str],
    },
)
AntipatternSeveritySummaryTypeDef = TypedDict(
    "AntipatternSeveritySummaryTypeDef",
    {
        "count": NotRequired[int],
        "severity": NotRequired[SeverityType],
    },
)
AppUnitErrorTypeDef = TypedDict(
    "AppUnitErrorTypeDef",
    {
        "appUnitErrorCategory": NotRequired[AppUnitErrorCategoryType],
    },
)
DatabaseConfigDetailTypeDef = TypedDict(
    "DatabaseConfigDetailTypeDef",
    {
        "secretName": NotRequired[str],
    },
)
SourceCodeRepositoryTypeDef = TypedDict(
    "SourceCodeRepositoryTypeDef",
    {
        "branch": NotRequired[str],
        "projectName": NotRequired[str],
        "repository": NotRequired[str],
        "versionControlType": NotRequired[str],
    },
)
ApplicationComponentStatusSummaryTypeDef = TypedDict(
    "ApplicationComponentStatusSummaryTypeDef",
    {
        "count": NotRequired[int],
        "srcCodeOrDbAnalysisStatus": NotRequired[SrcCodeOrDbAnalysisStatusType],
    },
)
ApplicationComponentSummaryTypeDef = TypedDict(
    "ApplicationComponentSummaryTypeDef",
    {
        "appType": NotRequired[AppTypeType],
        "count": NotRequired[int],
    },
)
ServerStatusSummaryTypeDef = TypedDict(
    "ServerStatusSummaryTypeDef",
    {
        "count": NotRequired[int],
        "runTimeAssessmentStatus": NotRequired[RunTimeAssessmentStatusType],
    },
)
ServerSummaryTypeDef = TypedDict(
    "ServerSummaryTypeDef",
    {
        "ServerOsType": NotRequired[ServerOsTypeType],
        "count": NotRequired[int],
    },
)
StrategySummaryTypeDef = TypedDict(
    "StrategySummaryTypeDef",
    {
        "count": NotRequired[int],
        "strategy": NotRequired[StrategyType],
    },
)
AssessmentTargetTypeDef = TypedDict(
    "AssessmentTargetTypeDef",
    {
        "condition": ConditionType,
        "name": str,
        "values": List[str],
    },
)
AssociatedApplicationTypeDef = TypedDict(
    "AssociatedApplicationTypeDef",
    {
        "id": NotRequired[str],
        "name": NotRequired[str],
    },
)
AwsManagedResourcesTypeDef = TypedDict(
    "AwsManagedResourcesTypeDef",
    {
        "targetDestination": List[AwsManagedTargetDestinationType],
    },
)
BusinessGoalsTypeDef = TypedDict(
    "BusinessGoalsTypeDef",
    {
        "licenseCostReduction": NotRequired[int],
        "modernizeInfrastructureWithCloudNativeTechnologies": NotRequired[int],
        "reduceOperationalOverheadWithManagedServices": NotRequired[int],
        "speedOfMigration": NotRequired[int],
    },
)
IPAddressBasedRemoteInfoTypeDef = TypedDict(
    "IPAddressBasedRemoteInfoTypeDef",
    {
        "authType": NotRequired[AuthTypeType],
        "ipAddressConfigurationTimeStamp": NotRequired[str],
        "osType": NotRequired[OSTypeType],
    },
)
PipelineInfoTypeDef = TypedDict(
    "PipelineInfoTypeDef",
    {
        "pipelineConfigurationTimeStamp": NotRequired[str],
        "pipelineType": NotRequired[Literal["AZURE_DEVOPS"]],
    },
)
RemoteSourceCodeAnalysisServerInfoTypeDef = TypedDict(
    "RemoteSourceCodeAnalysisServerInfoTypeDef",
    {
        "remoteSourceCodeAnalysisServerConfigurationTimestamp": NotRequired[str],
    },
)
VcenterBasedRemoteInfoTypeDef = TypedDict(
    "VcenterBasedRemoteInfoTypeDef",
    {
        "osType": NotRequired[OSTypeType],
        "vcenterConfigurationTimeStamp": NotRequired[str],
    },
)
VersionControlInfoTypeDef = TypedDict(
    "VersionControlInfoTypeDef",
    {
        "versionControlConfigurationTimeStamp": NotRequired[str],
        "versionControlType": NotRequired[VersionControlTypeType],
    },
)
DataCollectionDetailsTypeDef = TypedDict(
    "DataCollectionDetailsTypeDef",
    {
        "completionTime": NotRequired[datetime],
        "failed": NotRequired[int],
        "inProgress": NotRequired[int],
        "servers": NotRequired[int],
        "startTime": NotRequired[datetime],
        "status": NotRequired[AssessmentStatusType],
        "statusMessage": NotRequired[str],
        "success": NotRequired[int],
    },
)
HeterogeneousTypeDef = TypedDict(
    "HeterogeneousTypeDef",
    {
        "targetDatabaseEngine": List[HeterogeneousTargetDatabaseEngineType],
    },
)
HomogeneousTypeDef = TypedDict(
    "HomogeneousTypeDef",
    {
        "targetDatabaseEngine": NotRequired[List[Literal["None specified"]]],
    },
)
NoDatabaseMigrationPreferenceTypeDef = TypedDict(
    "NoDatabaseMigrationPreferenceTypeDef",
    {
        "targetDatabaseEngine": List[TargetDatabaseEngineType],
    },
)
GetApplicationComponentDetailsRequestRequestTypeDef = TypedDict(
    "GetApplicationComponentDetailsRequestRequestTypeDef",
    {
        "applicationComponentId": str,
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
GetApplicationComponentStrategiesRequestRequestTypeDef = TypedDict(
    "GetApplicationComponentStrategiesRequestRequestTypeDef",
    {
        "applicationComponentId": str,
    },
)
GetAssessmentRequestRequestTypeDef = TypedDict(
    "GetAssessmentRequestRequestTypeDef",
    {
        "id": str,
    },
)
GetImportFileTaskRequestRequestTypeDef = TypedDict(
    "GetImportFileTaskRequestRequestTypeDef",
    {
        "id": str,
    },
)
GetRecommendationReportDetailsRequestRequestTypeDef = TypedDict(
    "GetRecommendationReportDetailsRequestRequestTypeDef",
    {
        "id": str,
    },
)
RecommendationReportDetailsTypeDef = TypedDict(
    "RecommendationReportDetailsTypeDef",
    {
        "completionTime": NotRequired[datetime],
        "s3Bucket": NotRequired[str],
        "s3Keys": NotRequired[List[str]],
        "startTime": NotRequired[datetime],
        "status": NotRequired[RecommendationReportStatusType],
        "statusMessage": NotRequired[str],
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
GetServerDetailsRequestRequestTypeDef = TypedDict(
    "GetServerDetailsRequestRequestTypeDef",
    {
        "serverId": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
GetServerStrategiesRequestRequestTypeDef = TypedDict(
    "GetServerStrategiesRequestRequestTypeDef",
    {
        "serverId": str,
    },
)
GroupTypeDef = TypedDict(
    "GroupTypeDef",
    {
        "name": NotRequired[GroupNameType],
        "value": NotRequired[str],
    },
)
ImportFileTaskInformationTypeDef = TypedDict(
    "ImportFileTaskInformationTypeDef",
    {
        "completionTime": NotRequired[datetime],
        "id": NotRequired[str],
        "importName": NotRequired[str],
        "inputS3Bucket": NotRequired[str],
        "inputS3Key": NotRequired[str],
        "numberOfRecordsFailed": NotRequired[int],
        "numberOfRecordsSuccess": NotRequired[int],
        "startTime": NotRequired[datetime],
        "status": NotRequired[ImportFileTaskStatusType],
        "statusReportS3Bucket": NotRequired[str],
        "statusReportS3Key": NotRequired[str],
    },
)
ListAnalyzableServersRequestRequestTypeDef = TypedDict(
    "ListAnalyzableServersRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "sort": NotRequired[SortOrderType],
    },
)
ListCollectorsRequestRequestTypeDef = TypedDict(
    "ListCollectorsRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListImportFileTaskRequestRequestTypeDef = TypedDict(
    "ListImportFileTaskRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
NoManagementPreferenceTypeDef = TypedDict(
    "NoManagementPreferenceTypeDef",
    {
        "targetDestination": List[NoPreferenceTargetDestinationType],
    },
)
SelfManageResourcesTypeDef = TypedDict(
    "SelfManageResourcesTypeDef",
    {
        "targetDestination": List[SelfManageTargetDestinationType],
    },
)
NetworkInfoTypeDef = TypedDict(
    "NetworkInfoTypeDef",
    {
        "interfaceName": str,
        "ipAddress": str,
        "macAddress": str,
        "netMask": str,
    },
)
OSInfoTypeDef = TypedDict(
    "OSInfoTypeDef",
    {
        "type": NotRequired[OSTypeType],
        "version": NotRequired[str],
    },
)
TransformationToolTypeDef = TypedDict(
    "TransformationToolTypeDef",
    {
        "description": NotRequired[str],
        "name": NotRequired[TransformationToolNameType],
        "tranformationToolInstallationLink": NotRequired[str],
    },
)
ServerErrorTypeDef = TypedDict(
    "ServerErrorTypeDef",
    {
        "serverErrorCategory": NotRequired[ServerErrorCategoryType],
    },
)
SourceCodeTypeDef = TypedDict(
    "SourceCodeTypeDef",
    {
        "location": NotRequired[str],
        "projectName": NotRequired[str],
        "sourceVersion": NotRequired[str],
        "versionControl": NotRequired[VersionControlType],
    },
)
StopAssessmentRequestRequestTypeDef = TypedDict(
    "StopAssessmentRequestRequestTypeDef",
    {
        "assessmentId": str,
    },
)
StrategyOptionTypeDef = TypedDict(
    "StrategyOptionTypeDef",
    {
        "isPreferred": NotRequired[bool],
        "strategy": NotRequired[StrategyType],
        "targetDestination": NotRequired[TargetDestinationType],
        "toolName": NotRequired[TransformationToolNameType],
    },
)
AntipatternReportResultTypeDef = TypedDict(
    "AntipatternReportResultTypeDef",
    {
        "analyzerName": NotRequired[AnalyzerNameUnionTypeDef],
        "antiPatternReportS3Object": NotRequired[S3ObjectTypeDef],
        "antipatternReportStatus": NotRequired[AntipatternReportStatusType],
        "antipatternReportStatusMessage": NotRequired[str],
    },
)
AssessmentSummaryTypeDef = TypedDict(
    "AssessmentSummaryTypeDef",
    {
        "antipatternReportS3Object": NotRequired[S3ObjectTypeDef],
        "antipatternReportStatus": NotRequired[AntipatternReportStatusType],
        "antipatternReportStatusMessage": NotRequired[str],
        "lastAnalyzedTimestamp": NotRequired[datetime],
        "listAntipatternSeveritySummary": NotRequired[List[AntipatternSeveritySummaryTypeDef]],
        "listApplicationComponentStatusSummary": NotRequired[
            List[ApplicationComponentStatusSummaryTypeDef]
        ],
        "listApplicationComponentStrategySummary": NotRequired[List[StrategySummaryTypeDef]],
        "listApplicationComponentSummary": NotRequired[List[ApplicationComponentSummaryTypeDef]],
        "listServerStatusSummary": NotRequired[List[ServerStatusSummaryTypeDef]],
        "listServerStrategySummary": NotRequired[List[StrategySummaryTypeDef]],
        "listServerSummary": NotRequired[List[ServerSummaryTypeDef]],
    },
)
StartAssessmentRequestRequestTypeDef = TypedDict(
    "StartAssessmentRequestRequestTypeDef",
    {
        "assessmentDataSourceType": NotRequired[AssessmentDataSourceTypeType],
        "assessmentTargets": NotRequired[Sequence[AssessmentTargetTypeDef]],
        "s3bucketForAnalysisData": NotRequired[str],
        "s3bucketForReportData": NotRequired[str],
    },
)
PrioritizeBusinessGoalsTypeDef = TypedDict(
    "PrioritizeBusinessGoalsTypeDef",
    {
        "businessGoals": NotRequired[BusinessGoalsTypeDef],
    },
)
ConfigurationSummaryTypeDef = TypedDict(
    "ConfigurationSummaryTypeDef",
    {
        "ipAddressBasedRemoteInfoList": NotRequired[List[IPAddressBasedRemoteInfoTypeDef]],
        "pipelineInfoList": NotRequired[List[PipelineInfoTypeDef]],
        "remoteSourceCodeAnalysisServerInfo": NotRequired[
            RemoteSourceCodeAnalysisServerInfoTypeDef
        ],
        "vcenterBasedRemoteInfoList": NotRequired[List[VcenterBasedRemoteInfoTypeDef]],
        "versionControlInfoList": NotRequired[List[VersionControlInfoTypeDef]],
    },
)
DatabaseMigrationPreferenceTypeDef = TypedDict(
    "DatabaseMigrationPreferenceTypeDef",
    {
        "heterogeneous": NotRequired[HeterogeneousTypeDef],
        "homogeneous": NotRequired[HomogeneousTypeDef],
        "noPreference": NotRequired[NoDatabaseMigrationPreferenceTypeDef],
    },
)
GetAssessmentResponseTypeDef = TypedDict(
    "GetAssessmentResponseTypeDef",
    {
        "assessmentTargets": List[AssessmentTargetTypeDef],
        "dataCollectionDetails": DataCollectionDetailsTypeDef,
        "id": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetImportFileTaskResponseTypeDef = TypedDict(
    "GetImportFileTaskResponseTypeDef",
    {
        "completionTime": datetime,
        "id": str,
        "importName": str,
        "inputS3Bucket": str,
        "inputS3Key": str,
        "numberOfRecordsFailed": int,
        "numberOfRecordsSuccess": int,
        "startTime": datetime,
        "status": ImportFileTaskStatusType,
        "statusReportS3Bucket": str,
        "statusReportS3Key": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetLatestAssessmentIdResponseTypeDef = TypedDict(
    "GetLatestAssessmentIdResponseTypeDef",
    {
        "id": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAnalyzableServersResponseTypeDef = TypedDict(
    "ListAnalyzableServersResponseTypeDef",
    {
        "analyzableServers": List[AnalyzableServerSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartAssessmentResponseTypeDef = TypedDict(
    "StartAssessmentResponseTypeDef",
    {
        "assessmentId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartImportFileTaskResponseTypeDef = TypedDict(
    "StartImportFileTaskResponseTypeDef",
    {
        "id": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartRecommendationReportGenerationResponseTypeDef = TypedDict(
    "StartRecommendationReportGenerationResponseTypeDef",
    {
        "id": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetRecommendationReportDetailsResponseTypeDef = TypedDict(
    "GetRecommendationReportDetailsResponseTypeDef",
    {
        "id": str,
        "recommendationReportDetails": RecommendationReportDetailsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetServerDetailsRequestGetServerDetailsPaginateTypeDef = TypedDict(
    "GetServerDetailsRequestGetServerDetailsPaginateTypeDef",
    {
        "serverId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListAnalyzableServersRequestListAnalyzableServersPaginateTypeDef = TypedDict(
    "ListAnalyzableServersRequestListAnalyzableServersPaginateTypeDef",
    {
        "sort": NotRequired[SortOrderType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListCollectorsRequestListCollectorsPaginateTypeDef = TypedDict(
    "ListCollectorsRequestListCollectorsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListImportFileTaskRequestListImportFileTaskPaginateTypeDef = TypedDict(
    "ListImportFileTaskRequestListImportFileTaskPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListApplicationComponentsRequestListApplicationComponentsPaginateTypeDef = TypedDict(
    "ListApplicationComponentsRequestListApplicationComponentsPaginateTypeDef",
    {
        "applicationComponentCriteria": NotRequired[ApplicationComponentCriteriaType],
        "filterValue": NotRequired[str],
        "groupIdFilter": NotRequired[Sequence[GroupTypeDef]],
        "sort": NotRequired[SortOrderType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListApplicationComponentsRequestRequestTypeDef = TypedDict(
    "ListApplicationComponentsRequestRequestTypeDef",
    {
        "applicationComponentCriteria": NotRequired[ApplicationComponentCriteriaType],
        "filterValue": NotRequired[str],
        "groupIdFilter": NotRequired[Sequence[GroupTypeDef]],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "sort": NotRequired[SortOrderType],
    },
)
ListServersRequestListServersPaginateTypeDef = TypedDict(
    "ListServersRequestListServersPaginateTypeDef",
    {
        "filterValue": NotRequired[str],
        "groupIdFilter": NotRequired[Sequence[GroupTypeDef]],
        "serverCriteria": NotRequired[ServerCriteriaType],
        "sort": NotRequired[SortOrderType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListServersRequestRequestTypeDef = TypedDict(
    "ListServersRequestRequestTypeDef",
    {
        "filterValue": NotRequired[str],
        "groupIdFilter": NotRequired[Sequence[GroupTypeDef]],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "serverCriteria": NotRequired[ServerCriteriaType],
        "sort": NotRequired[SortOrderType],
    },
)
StartImportFileTaskRequestRequestTypeDef = TypedDict(
    "StartImportFileTaskRequestRequestTypeDef",
    {
        "S3Bucket": str,
        "name": str,
        "s3key": str,
        "dataSourceType": NotRequired[DataSourceTypeType],
        "groupId": NotRequired[Sequence[GroupTypeDef]],
        "s3bucketForReportData": NotRequired[str],
    },
)
StartRecommendationReportGenerationRequestRequestTypeDef = TypedDict(
    "StartRecommendationReportGenerationRequestRequestTypeDef",
    {
        "groupIdFilter": NotRequired[Sequence[GroupTypeDef]],
        "outputFormat": NotRequired[OutputFormatType],
    },
)
ListImportFileTaskResponseTypeDef = TypedDict(
    "ListImportFileTaskResponseTypeDef",
    {
        "nextToken": str,
        "taskInfos": List[ImportFileTaskInformationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ManagementPreferenceTypeDef = TypedDict(
    "ManagementPreferenceTypeDef",
    {
        "awsManagedResources": NotRequired[AwsManagedResourcesTypeDef],
        "noPreference": NotRequired[NoManagementPreferenceTypeDef],
        "selfManageResources": NotRequired[SelfManageResourcesTypeDef],
    },
)
SystemInfoTypeDef = TypedDict(
    "SystemInfoTypeDef",
    {
        "cpuArchitecture": NotRequired[str],
        "fileSystemType": NotRequired[str],
        "networkInfoList": NotRequired[List[NetworkInfoTypeDef]],
        "osInfo": NotRequired[OSInfoTypeDef],
    },
)
RecommendationSetTypeDef = TypedDict(
    "RecommendationSetTypeDef",
    {
        "strategy": NotRequired[StrategyType],
        "targetDestination": NotRequired[TargetDestinationType],
        "transformationTool": NotRequired[TransformationToolTypeDef],
    },
)
UpdateApplicationComponentConfigRequestRequestTypeDef = TypedDict(
    "UpdateApplicationComponentConfigRequestRequestTypeDef",
    {
        "applicationComponentId": str,
        "appType": NotRequired[AppTypeType],
        "configureOnly": NotRequired[bool],
        "inclusionStatus": NotRequired[InclusionStatusType],
        "secretsManagerKey": NotRequired[str],
        "sourceCodeList": NotRequired[Sequence[SourceCodeTypeDef]],
        "strategyOption": NotRequired[StrategyOptionTypeDef],
    },
)
UpdateServerConfigRequestRequestTypeDef = TypedDict(
    "UpdateServerConfigRequestRequestTypeDef",
    {
        "serverId": str,
        "strategyOption": NotRequired[StrategyOptionTypeDef],
    },
)
ResultTypeDef = TypedDict(
    "ResultTypeDef",
    {
        "analysisStatus": NotRequired[AnalysisStatusUnionTypeDef],
        "analysisType": NotRequired[AnalysisTypeType],
        "antipatternReportResultList": NotRequired[List[AntipatternReportResultTypeDef]],
        "statusMessage": NotRequired[str],
    },
)
GetPortfolioSummaryResponseTypeDef = TypedDict(
    "GetPortfolioSummaryResponseTypeDef",
    {
        "assessmentSummary": AssessmentSummaryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CollectorTypeDef = TypedDict(
    "CollectorTypeDef",
    {
        "collectorHealth": NotRequired[CollectorHealthType],
        "collectorId": NotRequired[str],
        "collectorVersion": NotRequired[str],
        "configurationSummary": NotRequired[ConfigurationSummaryTypeDef],
        "hostName": NotRequired[str],
        "ipAddress": NotRequired[str],
        "lastActivityTimeStamp": NotRequired[str],
        "registeredTimeStamp": NotRequired[str],
    },
)
DatabasePreferencesTypeDef = TypedDict(
    "DatabasePreferencesTypeDef",
    {
        "databaseManagementPreference": NotRequired[DatabaseManagementPreferenceType],
        "databaseMigrationPreference": NotRequired[DatabaseMigrationPreferenceTypeDef],
    },
)
ApplicationPreferencesTypeDef = TypedDict(
    "ApplicationPreferencesTypeDef",
    {
        "managementPreference": NotRequired[ManagementPreferenceTypeDef],
    },
)
ApplicationComponentStrategyTypeDef = TypedDict(
    "ApplicationComponentStrategyTypeDef",
    {
        "isPreferred": NotRequired[bool],
        "recommendation": NotRequired[RecommendationSetTypeDef],
        "status": NotRequired[StrategyRecommendationType],
    },
)
ServerDetailTypeDef = TypedDict(
    "ServerDetailTypeDef",
    {
        "antipatternReportS3Object": NotRequired[S3ObjectTypeDef],
        "antipatternReportStatus": NotRequired[AntipatternReportStatusType],
        "antipatternReportStatusMessage": NotRequired[str],
        "applicationComponentStrategySummary": NotRequired[List[StrategySummaryTypeDef]],
        "dataCollectionStatus": NotRequired[RunTimeAssessmentStatusType],
        "id": NotRequired[str],
        "lastAnalyzedTimestamp": NotRequired[datetime],
        "listAntipatternSeveritySummary": NotRequired[List[AntipatternSeveritySummaryTypeDef]],
        "name": NotRequired[str],
        "recommendationSet": NotRequired[RecommendationSetTypeDef],
        "serverError": NotRequired[ServerErrorTypeDef],
        "serverType": NotRequired[str],
        "statusMessage": NotRequired[str],
        "systemInfo": NotRequired[SystemInfoTypeDef],
    },
)
ServerStrategyTypeDef = TypedDict(
    "ServerStrategyTypeDef",
    {
        "isPreferred": NotRequired[bool],
        "numberOfApplicationComponents": NotRequired[int],
        "recommendation": NotRequired[RecommendationSetTypeDef],
        "status": NotRequired[StrategyRecommendationType],
    },
)
ApplicationComponentDetailTypeDef = TypedDict(
    "ApplicationComponentDetailTypeDef",
    {
        "analysisStatus": NotRequired[SrcCodeOrDbAnalysisStatusType],
        "antipatternReportS3Object": NotRequired[S3ObjectTypeDef],
        "antipatternReportStatus": NotRequired[AntipatternReportStatusType],
        "antipatternReportStatusMessage": NotRequired[str],
        "appType": NotRequired[AppTypeType],
        "appUnitError": NotRequired[AppUnitErrorTypeDef],
        "associatedServerId": NotRequired[str],
        "databaseConfigDetail": NotRequired[DatabaseConfigDetailTypeDef],
        "id": NotRequired[str],
        "inclusionStatus": NotRequired[InclusionStatusType],
        "lastAnalyzedTimestamp": NotRequired[datetime],
        "listAntipatternSeveritySummary": NotRequired[List[AntipatternSeveritySummaryTypeDef]],
        "moreServerAssociationExists": NotRequired[bool],
        "name": NotRequired[str],
        "osDriver": NotRequired[str],
        "osVersion": NotRequired[str],
        "recommendationSet": NotRequired[RecommendationSetTypeDef],
        "resourceSubType": NotRequired[ResourceSubTypeType],
        "resultList": NotRequired[List[ResultTypeDef]],
        "runtimeStatus": NotRequired[RuntimeAnalysisStatusType],
        "runtimeStatusMessage": NotRequired[str],
        "sourceCodeRepositories": NotRequired[List[SourceCodeRepositoryTypeDef]],
        "statusMessage": NotRequired[str],
    },
)
ListCollectorsResponseTypeDef = TypedDict(
    "ListCollectorsResponseTypeDef",
    {
        "Collectors": List[CollectorTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetPortfolioPreferencesResponseTypeDef = TypedDict(
    "GetPortfolioPreferencesResponseTypeDef",
    {
        "applicationMode": ApplicationModeType,
        "applicationPreferences": ApplicationPreferencesTypeDef,
        "databasePreferences": DatabasePreferencesTypeDef,
        "prioritizeBusinessGoals": PrioritizeBusinessGoalsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutPortfolioPreferencesRequestRequestTypeDef = TypedDict(
    "PutPortfolioPreferencesRequestRequestTypeDef",
    {
        "applicationMode": NotRequired[ApplicationModeType],
        "applicationPreferences": NotRequired[ApplicationPreferencesTypeDef],
        "databasePreferences": NotRequired[DatabasePreferencesTypeDef],
        "prioritizeBusinessGoals": NotRequired[PrioritizeBusinessGoalsTypeDef],
    },
)
GetApplicationComponentStrategiesResponseTypeDef = TypedDict(
    "GetApplicationComponentStrategiesResponseTypeDef",
    {
        "applicationComponentStrategies": List[ApplicationComponentStrategyTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetServerDetailsResponseTypeDef = TypedDict(
    "GetServerDetailsResponseTypeDef",
    {
        "associatedApplications": List[AssociatedApplicationTypeDef],
        "nextToken": str,
        "serverDetail": ServerDetailTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListServersResponseTypeDef = TypedDict(
    "ListServersResponseTypeDef",
    {
        "nextToken": str,
        "serverInfos": List[ServerDetailTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetServerStrategiesResponseTypeDef = TypedDict(
    "GetServerStrategiesResponseTypeDef",
    {
        "serverStrategies": List[ServerStrategyTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetApplicationComponentDetailsResponseTypeDef = TypedDict(
    "GetApplicationComponentDetailsResponseTypeDef",
    {
        "applicationComponentDetail": ApplicationComponentDetailTypeDef,
        "associatedApplications": List[AssociatedApplicationTypeDef],
        "associatedServerIds": List[str],
        "moreApplicationResource": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListApplicationComponentsResponseTypeDef = TypedDict(
    "ListApplicationComponentsResponseTypeDef",
    {
        "applicationComponentInfos": List[ApplicationComponentDetailTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
