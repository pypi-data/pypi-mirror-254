"""
Type annotations for entityresolution service type definitions.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_entityresolution/type_defs/)

Usage::

    ```python
    from types_aiobotocore_entityresolution.type_defs import IdMappingWorkflowInputSourceTypeDef

    data: IdMappingWorkflowInputSourceTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List, Mapping, Sequence

from .literals import (
    AttributeMatchingModelType,
    JobStatusType,
    ResolutionTypeType,
    SchemaAttributeTypeType,
    ServiceTypeType,
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
    "IdMappingWorkflowInputSourceTypeDef",
    "IdMappingWorkflowOutputSourceTypeDef",
    "ResponseMetadataTypeDef",
    "IncrementalRunConfigTypeDef",
    "InputSourceTypeDef",
    "SchemaInputAttributeTypeDef",
    "DeleteIdMappingWorkflowInputRequestTypeDef",
    "DeleteMatchingWorkflowInputRequestTypeDef",
    "DeleteSchemaMappingInputRequestTypeDef",
    "ErrorDetailsTypeDef",
    "GetIdMappingJobInputRequestTypeDef",
    "IdMappingJobMetricsTypeDef",
    "GetIdMappingWorkflowInputRequestTypeDef",
    "GetMatchIdInputRequestTypeDef",
    "GetMatchingJobInputRequestTypeDef",
    "JobMetricsTypeDef",
    "GetMatchingWorkflowInputRequestTypeDef",
    "GetProviderServiceInputRequestTypeDef",
    "ProviderIntermediateDataAccessConfigurationTypeDef",
    "GetSchemaMappingInputRequestTypeDef",
    "IdMappingWorkflowSummaryTypeDef",
    "IntermediateSourceConfigurationTypeDef",
    "JobSummaryTypeDef",
    "PaginatorConfigTypeDef",
    "ListIdMappingJobsInputRequestTypeDef",
    "ListIdMappingWorkflowsInputRequestTypeDef",
    "ListMatchingJobsInputRequestTypeDef",
    "ListMatchingWorkflowsInputRequestTypeDef",
    "MatchingWorkflowSummaryTypeDef",
    "ListProviderServicesInputRequestTypeDef",
    "ProviderServiceSummaryTypeDef",
    "ListSchemaMappingsInputRequestTypeDef",
    "SchemaMappingSummaryTypeDef",
    "ListTagsForResourceInputRequestTypeDef",
    "OutputAttributeTypeDef",
    "ProviderMarketplaceConfigurationTypeDef",
    "RuleTypeDef",
    "StartIdMappingJobInputRequestTypeDef",
    "StartMatchingJobInputRequestTypeDef",
    "TagResourceInputRequestTypeDef",
    "UntagResourceInputRequestTypeDef",
    "DeleteIdMappingWorkflowOutputTypeDef",
    "DeleteMatchingWorkflowOutputTypeDef",
    "DeleteSchemaMappingOutputTypeDef",
    "GetMatchIdOutputTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "StartIdMappingJobOutputTypeDef",
    "StartMatchingJobOutputTypeDef",
    "CreateSchemaMappingInputRequestTypeDef",
    "CreateSchemaMappingOutputTypeDef",
    "GetSchemaMappingOutputTypeDef",
    "UpdateSchemaMappingInputRequestTypeDef",
    "UpdateSchemaMappingOutputTypeDef",
    "GetIdMappingJobOutputTypeDef",
    "GetMatchingJobOutputTypeDef",
    "ListIdMappingWorkflowsOutputTypeDef",
    "ProviderPropertiesTypeDef",
    "ListIdMappingJobsOutputTypeDef",
    "ListMatchingJobsOutputTypeDef",
    "ListIdMappingJobsInputListIdMappingJobsPaginateTypeDef",
    "ListIdMappingWorkflowsInputListIdMappingWorkflowsPaginateTypeDef",
    "ListMatchingJobsInputListMatchingJobsPaginateTypeDef",
    "ListMatchingWorkflowsInputListMatchingWorkflowsPaginateTypeDef",
    "ListProviderServicesInputListProviderServicesPaginateTypeDef",
    "ListSchemaMappingsInputListSchemaMappingsPaginateTypeDef",
    "ListMatchingWorkflowsOutputTypeDef",
    "ListProviderServicesOutputTypeDef",
    "ListSchemaMappingsOutputTypeDef",
    "OutputSourceTypeDef",
    "ProviderEndpointConfigurationTypeDef",
    "RuleBasedPropertiesTypeDef",
    "IdMappingTechniquesTypeDef",
    "GetProviderServiceOutputTypeDef",
    "ResolutionTechniquesTypeDef",
    "CreateIdMappingWorkflowInputRequestTypeDef",
    "CreateIdMappingWorkflowOutputTypeDef",
    "GetIdMappingWorkflowOutputTypeDef",
    "UpdateIdMappingWorkflowInputRequestTypeDef",
    "UpdateIdMappingWorkflowOutputTypeDef",
    "CreateMatchingWorkflowInputRequestTypeDef",
    "CreateMatchingWorkflowOutputTypeDef",
    "GetMatchingWorkflowOutputTypeDef",
    "UpdateMatchingWorkflowInputRequestTypeDef",
    "UpdateMatchingWorkflowOutputTypeDef",
)

IdMappingWorkflowInputSourceTypeDef = TypedDict(
    "IdMappingWorkflowInputSourceTypeDef",
    {
        "inputSourceARN": str,
        "schemaName": str,
    },
)
IdMappingWorkflowOutputSourceTypeDef = TypedDict(
    "IdMappingWorkflowOutputSourceTypeDef",
    {
        "outputS3Path": str,
        "KMSArn": NotRequired[str],
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
IncrementalRunConfigTypeDef = TypedDict(
    "IncrementalRunConfigTypeDef",
    {
        "incrementalRunType": NotRequired[Literal["IMMEDIATE"]],
    },
)
InputSourceTypeDef = TypedDict(
    "InputSourceTypeDef",
    {
        "inputSourceARN": str,
        "schemaName": str,
        "applyNormalization": NotRequired[bool],
    },
)
SchemaInputAttributeTypeDef = TypedDict(
    "SchemaInputAttributeTypeDef",
    {
        "fieldName": str,
        "type": SchemaAttributeTypeType,
        "groupName": NotRequired[str],
        "matchKey": NotRequired[str],
        "subType": NotRequired[str],
    },
)
DeleteIdMappingWorkflowInputRequestTypeDef = TypedDict(
    "DeleteIdMappingWorkflowInputRequestTypeDef",
    {
        "workflowName": str,
    },
)
DeleteMatchingWorkflowInputRequestTypeDef = TypedDict(
    "DeleteMatchingWorkflowInputRequestTypeDef",
    {
        "workflowName": str,
    },
)
DeleteSchemaMappingInputRequestTypeDef = TypedDict(
    "DeleteSchemaMappingInputRequestTypeDef",
    {
        "schemaName": str,
    },
)
ErrorDetailsTypeDef = TypedDict(
    "ErrorDetailsTypeDef",
    {
        "errorMessage": NotRequired[str],
    },
)
GetIdMappingJobInputRequestTypeDef = TypedDict(
    "GetIdMappingJobInputRequestTypeDef",
    {
        "jobId": str,
        "workflowName": str,
    },
)
IdMappingJobMetricsTypeDef = TypedDict(
    "IdMappingJobMetricsTypeDef",
    {
        "inputRecords": NotRequired[int],
        "recordsNotProcessed": NotRequired[int],
        "totalRecordsProcessed": NotRequired[int],
    },
)
GetIdMappingWorkflowInputRequestTypeDef = TypedDict(
    "GetIdMappingWorkflowInputRequestTypeDef",
    {
        "workflowName": str,
    },
)
GetMatchIdInputRequestTypeDef = TypedDict(
    "GetMatchIdInputRequestTypeDef",
    {
        "record": Mapping[str, str],
        "workflowName": str,
    },
)
GetMatchingJobInputRequestTypeDef = TypedDict(
    "GetMatchingJobInputRequestTypeDef",
    {
        "jobId": str,
        "workflowName": str,
    },
)
JobMetricsTypeDef = TypedDict(
    "JobMetricsTypeDef",
    {
        "inputRecords": NotRequired[int],
        "matchIDs": NotRequired[int],
        "recordsNotProcessed": NotRequired[int],
        "totalRecordsProcessed": NotRequired[int],
    },
)
GetMatchingWorkflowInputRequestTypeDef = TypedDict(
    "GetMatchingWorkflowInputRequestTypeDef",
    {
        "workflowName": str,
    },
)
GetProviderServiceInputRequestTypeDef = TypedDict(
    "GetProviderServiceInputRequestTypeDef",
    {
        "providerName": str,
        "providerServiceName": str,
    },
)
ProviderIntermediateDataAccessConfigurationTypeDef = TypedDict(
    "ProviderIntermediateDataAccessConfigurationTypeDef",
    {
        "awsAccountIds": NotRequired[List[str]],
        "requiredBucketActions": NotRequired[List[str]],
    },
)
GetSchemaMappingInputRequestTypeDef = TypedDict(
    "GetSchemaMappingInputRequestTypeDef",
    {
        "schemaName": str,
    },
)
IdMappingWorkflowSummaryTypeDef = TypedDict(
    "IdMappingWorkflowSummaryTypeDef",
    {
        "createdAt": datetime,
        "updatedAt": datetime,
        "workflowArn": str,
        "workflowName": str,
    },
)
IntermediateSourceConfigurationTypeDef = TypedDict(
    "IntermediateSourceConfigurationTypeDef",
    {
        "intermediateS3Path": str,
    },
)
JobSummaryTypeDef = TypedDict(
    "JobSummaryTypeDef",
    {
        "jobId": str,
        "startTime": datetime,
        "status": JobStatusType,
        "endTime": NotRequired[datetime],
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
ListIdMappingJobsInputRequestTypeDef = TypedDict(
    "ListIdMappingJobsInputRequestTypeDef",
    {
        "workflowName": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListIdMappingWorkflowsInputRequestTypeDef = TypedDict(
    "ListIdMappingWorkflowsInputRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListMatchingJobsInputRequestTypeDef = TypedDict(
    "ListMatchingJobsInputRequestTypeDef",
    {
        "workflowName": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListMatchingWorkflowsInputRequestTypeDef = TypedDict(
    "ListMatchingWorkflowsInputRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
MatchingWorkflowSummaryTypeDef = TypedDict(
    "MatchingWorkflowSummaryTypeDef",
    {
        "createdAt": datetime,
        "resolutionType": ResolutionTypeType,
        "updatedAt": datetime,
        "workflowArn": str,
        "workflowName": str,
    },
)
ListProviderServicesInputRequestTypeDef = TypedDict(
    "ListProviderServicesInputRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "providerName": NotRequired[str],
    },
)
ProviderServiceSummaryTypeDef = TypedDict(
    "ProviderServiceSummaryTypeDef",
    {
        "providerName": str,
        "providerServiceArn": str,
        "providerServiceDisplayName": str,
        "providerServiceName": str,
        "providerServiceType": ServiceTypeType,
    },
)
ListSchemaMappingsInputRequestTypeDef = TypedDict(
    "ListSchemaMappingsInputRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
SchemaMappingSummaryTypeDef = TypedDict(
    "SchemaMappingSummaryTypeDef",
    {
        "createdAt": datetime,
        "hasWorkflows": bool,
        "schemaArn": str,
        "schemaName": str,
        "updatedAt": datetime,
    },
)
ListTagsForResourceInputRequestTypeDef = TypedDict(
    "ListTagsForResourceInputRequestTypeDef",
    {
        "resourceArn": str,
    },
)
OutputAttributeTypeDef = TypedDict(
    "OutputAttributeTypeDef",
    {
        "name": str,
        "hashed": NotRequired[bool],
    },
)
ProviderMarketplaceConfigurationTypeDef = TypedDict(
    "ProviderMarketplaceConfigurationTypeDef",
    {
        "assetId": str,
        "dataSetId": str,
        "listingId": str,
        "revisionId": str,
    },
)
RuleTypeDef = TypedDict(
    "RuleTypeDef",
    {
        "matchingKeys": Sequence[str],
        "ruleName": str,
    },
)
StartIdMappingJobInputRequestTypeDef = TypedDict(
    "StartIdMappingJobInputRequestTypeDef",
    {
        "workflowName": str,
    },
)
StartMatchingJobInputRequestTypeDef = TypedDict(
    "StartMatchingJobInputRequestTypeDef",
    {
        "workflowName": str,
    },
)
TagResourceInputRequestTypeDef = TypedDict(
    "TagResourceInputRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Mapping[str, str],
    },
)
UntagResourceInputRequestTypeDef = TypedDict(
    "UntagResourceInputRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)
DeleteIdMappingWorkflowOutputTypeDef = TypedDict(
    "DeleteIdMappingWorkflowOutputTypeDef",
    {
        "message": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteMatchingWorkflowOutputTypeDef = TypedDict(
    "DeleteMatchingWorkflowOutputTypeDef",
    {
        "message": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteSchemaMappingOutputTypeDef = TypedDict(
    "DeleteSchemaMappingOutputTypeDef",
    {
        "message": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetMatchIdOutputTypeDef = TypedDict(
    "GetMatchIdOutputTypeDef",
    {
        "matchId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartIdMappingJobOutputTypeDef = TypedDict(
    "StartIdMappingJobOutputTypeDef",
    {
        "jobId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartMatchingJobOutputTypeDef = TypedDict(
    "StartMatchingJobOutputTypeDef",
    {
        "jobId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateSchemaMappingInputRequestTypeDef = TypedDict(
    "CreateSchemaMappingInputRequestTypeDef",
    {
        "mappedInputFields": Sequence[SchemaInputAttributeTypeDef],
        "schemaName": str,
        "description": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)
CreateSchemaMappingOutputTypeDef = TypedDict(
    "CreateSchemaMappingOutputTypeDef",
    {
        "description": str,
        "mappedInputFields": List[SchemaInputAttributeTypeDef],
        "schemaArn": str,
        "schemaName": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSchemaMappingOutputTypeDef = TypedDict(
    "GetSchemaMappingOutputTypeDef",
    {
        "createdAt": datetime,
        "description": str,
        "hasWorkflows": bool,
        "mappedInputFields": List[SchemaInputAttributeTypeDef],
        "schemaArn": str,
        "schemaName": str,
        "tags": Dict[str, str],
        "updatedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateSchemaMappingInputRequestTypeDef = TypedDict(
    "UpdateSchemaMappingInputRequestTypeDef",
    {
        "mappedInputFields": Sequence[SchemaInputAttributeTypeDef],
        "schemaName": str,
        "description": NotRequired[str],
    },
)
UpdateSchemaMappingOutputTypeDef = TypedDict(
    "UpdateSchemaMappingOutputTypeDef",
    {
        "description": str,
        "mappedInputFields": List[SchemaInputAttributeTypeDef],
        "schemaArn": str,
        "schemaName": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetIdMappingJobOutputTypeDef = TypedDict(
    "GetIdMappingJobOutputTypeDef",
    {
        "endTime": datetime,
        "errorDetails": ErrorDetailsTypeDef,
        "jobId": str,
        "metrics": IdMappingJobMetricsTypeDef,
        "startTime": datetime,
        "status": JobStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetMatchingJobOutputTypeDef = TypedDict(
    "GetMatchingJobOutputTypeDef",
    {
        "endTime": datetime,
        "errorDetails": ErrorDetailsTypeDef,
        "jobId": str,
        "metrics": JobMetricsTypeDef,
        "startTime": datetime,
        "status": JobStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListIdMappingWorkflowsOutputTypeDef = TypedDict(
    "ListIdMappingWorkflowsOutputTypeDef",
    {
        "nextToken": str,
        "workflowSummaries": List[IdMappingWorkflowSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ProviderPropertiesTypeDef = TypedDict(
    "ProviderPropertiesTypeDef",
    {
        "providerServiceArn": str,
        "intermediateSourceConfiguration": NotRequired[IntermediateSourceConfigurationTypeDef],
        "providerConfiguration": NotRequired[Mapping[str, Any]],
    },
)
ListIdMappingJobsOutputTypeDef = TypedDict(
    "ListIdMappingJobsOutputTypeDef",
    {
        "jobs": List[JobSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListMatchingJobsOutputTypeDef = TypedDict(
    "ListMatchingJobsOutputTypeDef",
    {
        "jobs": List[JobSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListIdMappingJobsInputListIdMappingJobsPaginateTypeDef = TypedDict(
    "ListIdMappingJobsInputListIdMappingJobsPaginateTypeDef",
    {
        "workflowName": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListIdMappingWorkflowsInputListIdMappingWorkflowsPaginateTypeDef = TypedDict(
    "ListIdMappingWorkflowsInputListIdMappingWorkflowsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListMatchingJobsInputListMatchingJobsPaginateTypeDef = TypedDict(
    "ListMatchingJobsInputListMatchingJobsPaginateTypeDef",
    {
        "workflowName": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListMatchingWorkflowsInputListMatchingWorkflowsPaginateTypeDef = TypedDict(
    "ListMatchingWorkflowsInputListMatchingWorkflowsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListProviderServicesInputListProviderServicesPaginateTypeDef = TypedDict(
    "ListProviderServicesInputListProviderServicesPaginateTypeDef",
    {
        "providerName": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListSchemaMappingsInputListSchemaMappingsPaginateTypeDef = TypedDict(
    "ListSchemaMappingsInputListSchemaMappingsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListMatchingWorkflowsOutputTypeDef = TypedDict(
    "ListMatchingWorkflowsOutputTypeDef",
    {
        "nextToken": str,
        "workflowSummaries": List[MatchingWorkflowSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListProviderServicesOutputTypeDef = TypedDict(
    "ListProviderServicesOutputTypeDef",
    {
        "nextToken": str,
        "providerServiceSummaries": List[ProviderServiceSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListSchemaMappingsOutputTypeDef = TypedDict(
    "ListSchemaMappingsOutputTypeDef",
    {
        "nextToken": str,
        "schemaList": List[SchemaMappingSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
OutputSourceTypeDef = TypedDict(
    "OutputSourceTypeDef",
    {
        "output": Sequence[OutputAttributeTypeDef],
        "outputS3Path": str,
        "KMSArn": NotRequired[str],
        "applyNormalization": NotRequired[bool],
    },
)
ProviderEndpointConfigurationTypeDef = TypedDict(
    "ProviderEndpointConfigurationTypeDef",
    {
        "marketplaceConfiguration": NotRequired[ProviderMarketplaceConfigurationTypeDef],
    },
)
RuleBasedPropertiesTypeDef = TypedDict(
    "RuleBasedPropertiesTypeDef",
    {
        "attributeMatchingModel": AttributeMatchingModelType,
        "rules": Sequence[RuleTypeDef],
    },
)
IdMappingTechniquesTypeDef = TypedDict(
    "IdMappingTechniquesTypeDef",
    {
        "idMappingType": Literal["PROVIDER"],
        "providerProperties": ProviderPropertiesTypeDef,
    },
)
GetProviderServiceOutputTypeDef = TypedDict(
    "GetProviderServiceOutputTypeDef",
    {
        "anonymizedOutput": bool,
        "providerConfigurationDefinition": Dict[str, Any],
        "providerEndpointConfiguration": ProviderEndpointConfigurationTypeDef,
        "providerEntityOutputDefinition": Dict[str, Any],
        "providerIntermediateDataAccessConfiguration": ProviderIntermediateDataAccessConfigurationTypeDef,
        "providerName": str,
        "providerServiceArn": str,
        "providerServiceDisplayName": str,
        "providerServiceName": str,
        "providerServiceType": ServiceTypeType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ResolutionTechniquesTypeDef = TypedDict(
    "ResolutionTechniquesTypeDef",
    {
        "resolutionType": ResolutionTypeType,
        "providerProperties": NotRequired[ProviderPropertiesTypeDef],
        "ruleBasedProperties": NotRequired[RuleBasedPropertiesTypeDef],
    },
)
CreateIdMappingWorkflowInputRequestTypeDef = TypedDict(
    "CreateIdMappingWorkflowInputRequestTypeDef",
    {
        "idMappingTechniques": IdMappingTechniquesTypeDef,
        "inputSourceConfig": Sequence[IdMappingWorkflowInputSourceTypeDef],
        "outputSourceConfig": Sequence[IdMappingWorkflowOutputSourceTypeDef],
        "roleArn": str,
        "workflowName": str,
        "description": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)
CreateIdMappingWorkflowOutputTypeDef = TypedDict(
    "CreateIdMappingWorkflowOutputTypeDef",
    {
        "description": str,
        "idMappingTechniques": IdMappingTechniquesTypeDef,
        "inputSourceConfig": List[IdMappingWorkflowInputSourceTypeDef],
        "outputSourceConfig": List[IdMappingWorkflowOutputSourceTypeDef],
        "roleArn": str,
        "workflowArn": str,
        "workflowName": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetIdMappingWorkflowOutputTypeDef = TypedDict(
    "GetIdMappingWorkflowOutputTypeDef",
    {
        "createdAt": datetime,
        "description": str,
        "idMappingTechniques": IdMappingTechniquesTypeDef,
        "inputSourceConfig": List[IdMappingWorkflowInputSourceTypeDef],
        "outputSourceConfig": List[IdMappingWorkflowOutputSourceTypeDef],
        "roleArn": str,
        "tags": Dict[str, str],
        "updatedAt": datetime,
        "workflowArn": str,
        "workflowName": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateIdMappingWorkflowInputRequestTypeDef = TypedDict(
    "UpdateIdMappingWorkflowInputRequestTypeDef",
    {
        "idMappingTechniques": IdMappingTechniquesTypeDef,
        "inputSourceConfig": Sequence[IdMappingWorkflowInputSourceTypeDef],
        "outputSourceConfig": Sequence[IdMappingWorkflowOutputSourceTypeDef],
        "roleArn": str,
        "workflowName": str,
        "description": NotRequired[str],
    },
)
UpdateIdMappingWorkflowOutputTypeDef = TypedDict(
    "UpdateIdMappingWorkflowOutputTypeDef",
    {
        "description": str,
        "idMappingTechniques": IdMappingTechniquesTypeDef,
        "inputSourceConfig": List[IdMappingWorkflowInputSourceTypeDef],
        "outputSourceConfig": List[IdMappingWorkflowOutputSourceTypeDef],
        "roleArn": str,
        "workflowArn": str,
        "workflowName": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateMatchingWorkflowInputRequestTypeDef = TypedDict(
    "CreateMatchingWorkflowInputRequestTypeDef",
    {
        "inputSourceConfig": Sequence[InputSourceTypeDef],
        "outputSourceConfig": Sequence[OutputSourceTypeDef],
        "resolutionTechniques": ResolutionTechniquesTypeDef,
        "roleArn": str,
        "workflowName": str,
        "description": NotRequired[str],
        "incrementalRunConfig": NotRequired[IncrementalRunConfigTypeDef],
        "tags": NotRequired[Mapping[str, str]],
    },
)
CreateMatchingWorkflowOutputTypeDef = TypedDict(
    "CreateMatchingWorkflowOutputTypeDef",
    {
        "description": str,
        "incrementalRunConfig": IncrementalRunConfigTypeDef,
        "inputSourceConfig": List[InputSourceTypeDef],
        "outputSourceConfig": List[OutputSourceTypeDef],
        "resolutionTechniques": ResolutionTechniquesTypeDef,
        "roleArn": str,
        "workflowArn": str,
        "workflowName": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetMatchingWorkflowOutputTypeDef = TypedDict(
    "GetMatchingWorkflowOutputTypeDef",
    {
        "createdAt": datetime,
        "description": str,
        "incrementalRunConfig": IncrementalRunConfigTypeDef,
        "inputSourceConfig": List[InputSourceTypeDef],
        "outputSourceConfig": List[OutputSourceTypeDef],
        "resolutionTechniques": ResolutionTechniquesTypeDef,
        "roleArn": str,
        "tags": Dict[str, str],
        "updatedAt": datetime,
        "workflowArn": str,
        "workflowName": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateMatchingWorkflowInputRequestTypeDef = TypedDict(
    "UpdateMatchingWorkflowInputRequestTypeDef",
    {
        "inputSourceConfig": Sequence[InputSourceTypeDef],
        "outputSourceConfig": Sequence[OutputSourceTypeDef],
        "resolutionTechniques": ResolutionTechniquesTypeDef,
        "roleArn": str,
        "workflowName": str,
        "description": NotRequired[str],
        "incrementalRunConfig": NotRequired[IncrementalRunConfigTypeDef],
    },
)
UpdateMatchingWorkflowOutputTypeDef = TypedDict(
    "UpdateMatchingWorkflowOutputTypeDef",
    {
        "description": str,
        "incrementalRunConfig": IncrementalRunConfigTypeDef,
        "inputSourceConfig": List[InputSourceTypeDef],
        "outputSourceConfig": List[OutputSourceTypeDef],
        "resolutionTechniques": ResolutionTechniquesTypeDef,
        "roleArn": str,
        "workflowName": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
