"""
Type annotations for lakeformation service type definitions.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lakeformation/type_defs/)

Usage::

    ```python
    from types_aiobotocore_lakeformation.type_defs import LFTagPairTypeDef

    data: LFTagPairTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List, Mapping, Sequence, Union

from aiobotocore.response import StreamingBody

from .literals import (
    ApplicationStatusType,
    ComparisonOperatorType,
    DataLakeResourceTypeType,
    EnableStatusType,
    FieldNameStringType,
    OptimizerTypeType,
    PermissionType,
    PermissionTypeType,
    QueryStateStringType,
    ResourceShareTypeType,
    ResourceTypeType,
    TransactionStatusFilterType,
    TransactionStatusType,
    TransactionTypeType,
)

if sys.version_info >= (3, 12):
    from typing import NotRequired
else:
    from typing_extensions import NotRequired
if sys.version_info >= (3, 12):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "LFTagPairTypeDef",
    "ResponseMetadataTypeDef",
    "AddObjectInputTypeDef",
    "AssumeDecoratedRoleWithSAMLRequestRequestTypeDef",
    "AuditContextTypeDef",
    "ErrorDetailTypeDef",
    "DataLakePrincipalTypeDef",
    "CancelTransactionRequestRequestTypeDef",
    "LFTagPairPaginatorTypeDef",
    "ColumnWildcardPaginatorTypeDef",
    "ColumnWildcardTypeDef",
    "CommitTransactionRequestRequestTypeDef",
    "CreateLFTagRequestRequestTypeDef",
    "ExternalFilteringConfigurationTypeDef",
    "RowFilterPaginatorTypeDef",
    "DataCellsFilterResourceTypeDef",
    "RowFilterTypeDef",
    "DataLocationResourceTypeDef",
    "DatabaseResourceTypeDef",
    "DeleteDataCellsFilterRequestRequestTypeDef",
    "DeleteLFTagRequestRequestTypeDef",
    "DeleteLakeFormationIdentityCenterConfigurationRequestRequestTypeDef",
    "DeleteObjectInputTypeDef",
    "VirtualObjectTypeDef",
    "DeregisterResourceRequestRequestTypeDef",
    "DescribeLakeFormationIdentityCenterConfigurationRequestRequestTypeDef",
    "DescribeResourceRequestRequestTypeDef",
    "ResourceInfoTypeDef",
    "DescribeTransactionRequestRequestTypeDef",
    "TransactionDescriptionTypeDef",
    "DetailsMapTypeDef",
    "ExecutionStatisticsTypeDef",
    "ExtendTransactionRequestRequestTypeDef",
    "FilterConditionTypeDef",
    "GetDataCellsFilterRequestRequestTypeDef",
    "GetDataLakeSettingsRequestRequestTypeDef",
    "GetEffectivePermissionsForPathRequestRequestTypeDef",
    "GetLFTagRequestRequestTypeDef",
    "GetQueryStateRequestRequestTypeDef",
    "GetQueryStatisticsRequestRequestTypeDef",
    "PlanningStatisticsTypeDef",
    "TimestampTypeDef",
    "PartitionValueListTypeDef",
    "GetWorkUnitResultsRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "GetWorkUnitsRequestRequestTypeDef",
    "WorkUnitRangeTypeDef",
    "LFTagKeyResourceTypeDef",
    "LFTagTypeDef",
    "TableResourceTypeDef",
    "ListLFTagsRequestRequestTypeDef",
    "ListTableStorageOptimizersRequestRequestTypeDef",
    "StorageOptimizerTypeDef",
    "ListTransactionsRequestRequestTypeDef",
    "TableObjectTypeDef",
    "RegisterResourceRequestRequestTypeDef",
    "StartTransactionRequestRequestTypeDef",
    "UpdateLFTagRequestRequestTypeDef",
    "UpdateResourceRequestRequestTypeDef",
    "UpdateTableStorageOptimizerRequestRequestTypeDef",
    "ColumnLFTagTypeDef",
    "AssumeDecoratedRoleWithSAMLResponseTypeDef",
    "CommitTransactionResponseTypeDef",
    "CreateLakeFormationIdentityCenterConfigurationResponseTypeDef",
    "GetLFTagResponseTypeDef",
    "GetQueryStateResponseTypeDef",
    "GetTemporaryGluePartitionCredentialsResponseTypeDef",
    "GetTemporaryGlueTableCredentialsResponseTypeDef",
    "GetWorkUnitResultsResponseTypeDef",
    "ListLFTagsResponseTypeDef",
    "StartQueryPlanningResponseTypeDef",
    "StartTransactionResponseTypeDef",
    "UpdateTableStorageOptimizerResponseTypeDef",
    "LFTagErrorTypeDef",
    "PrincipalPermissionsTypeDef",
    "ColumnLFTagPaginatorTypeDef",
    "ListLFTagsResponsePaginatorTypeDef",
    "TableWithColumnsResourceTypeDef",
    "CreateLakeFormationIdentityCenterConfigurationRequestRequestTypeDef",
    "DescribeLakeFormationIdentityCenterConfigurationResponseTypeDef",
    "UpdateLakeFormationIdentityCenterConfigurationRequestRequestTypeDef",
    "DataCellsFilterPaginatorTypeDef",
    "DataCellsFilterTypeDef",
    "TaggedDatabasePaginatorTypeDef",
    "TaggedDatabaseTypeDef",
    "WriteOperationTypeDef",
    "DeleteObjectsOnCancelRequestRequestTypeDef",
    "DescribeResourceResponseTypeDef",
    "ListResourcesResponseTypeDef",
    "DescribeTransactionResponseTypeDef",
    "ListTransactionsResponseTypeDef",
    "ListResourcesRequestRequestTypeDef",
    "GetQueryStatisticsResponseTypeDef",
    "GetTableObjectsRequestRequestTypeDef",
    "QueryPlanningContextTypeDef",
    "QuerySessionContextTypeDef",
    "GetTemporaryGluePartitionCredentialsRequestRequestTypeDef",
    "GetWorkUnitsRequestGetWorkUnitsPaginateTypeDef",
    "ListLFTagsRequestListLFTagsPaginateTypeDef",
    "GetWorkUnitsResponseTypeDef",
    "LFTagPolicyResourceTypeDef",
    "SearchDatabasesByLFTagsRequestRequestTypeDef",
    "SearchDatabasesByLFTagsRequestSearchDatabasesByLFTagsPaginateTypeDef",
    "SearchTablesByLFTagsRequestRequestTypeDef",
    "SearchTablesByLFTagsRequestSearchTablesByLFTagsPaginateTypeDef",
    "ListDataCellsFilterRequestListDataCellsFilterPaginateTypeDef",
    "ListDataCellsFilterRequestRequestTypeDef",
    "ListTableStorageOptimizersResponseTypeDef",
    "PartitionObjectsTypeDef",
    "GetResourceLFTagsResponseTypeDef",
    "TaggedTableTypeDef",
    "AddLFTagsToResourceResponseTypeDef",
    "RemoveLFTagsFromResourceResponseTypeDef",
    "DataLakeSettingsTypeDef",
    "TaggedTablePaginatorTypeDef",
    "ListDataCellsFilterResponsePaginatorTypeDef",
    "CreateDataCellsFilterRequestRequestTypeDef",
    "GetDataCellsFilterResponseTypeDef",
    "ListDataCellsFilterResponseTypeDef",
    "UpdateDataCellsFilterRequestRequestTypeDef",
    "SearchDatabasesByLFTagsResponsePaginatorTypeDef",
    "SearchDatabasesByLFTagsResponseTypeDef",
    "UpdateTableObjectsRequestRequestTypeDef",
    "StartQueryPlanningRequestRequestTypeDef",
    "GetTemporaryGlueTableCredentialsRequestRequestTypeDef",
    "ResourceTypeDef",
    "GetTableObjectsResponseTypeDef",
    "SearchTablesByLFTagsResponseTypeDef",
    "GetDataLakeSettingsResponseTypeDef",
    "PutDataLakeSettingsRequestRequestTypeDef",
    "SearchTablesByLFTagsResponsePaginatorTypeDef",
    "AddLFTagsToResourceRequestRequestTypeDef",
    "BatchPermissionsRequestEntryTypeDef",
    "CreateLakeFormationOptInRequestRequestTypeDef",
    "DeleteLakeFormationOptInRequestRequestTypeDef",
    "GetResourceLFTagsRequestRequestTypeDef",
    "GrantPermissionsRequestRequestTypeDef",
    "LakeFormationOptInsInfoTypeDef",
    "ListLakeFormationOptInsRequestRequestTypeDef",
    "ListPermissionsRequestRequestTypeDef",
    "PrincipalResourcePermissionsTypeDef",
    "RemoveLFTagsFromResourceRequestRequestTypeDef",
    "RevokePermissionsRequestRequestTypeDef",
    "BatchGrantPermissionsRequestRequestTypeDef",
    "BatchPermissionsFailureEntryTypeDef",
    "BatchRevokePermissionsRequestRequestTypeDef",
    "ListLakeFormationOptInsResponseTypeDef",
    "GetEffectivePermissionsForPathResponseTypeDef",
    "ListPermissionsResponseTypeDef",
    "BatchGrantPermissionsResponseTypeDef",
    "BatchRevokePermissionsResponseTypeDef",
)

LFTagPairTypeDef = TypedDict(
    "LFTagPairTypeDef",
    {
        "TagKey": str,
        "TagValues": Sequence[str],
        "CatalogId": NotRequired[str],
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
AddObjectInputTypeDef = TypedDict(
    "AddObjectInputTypeDef",
    {
        "Uri": str,
        "ETag": str,
        "Size": int,
        "PartitionValues": NotRequired[Sequence[str]],
    },
)
AssumeDecoratedRoleWithSAMLRequestRequestTypeDef = TypedDict(
    "AssumeDecoratedRoleWithSAMLRequestRequestTypeDef",
    {
        "SAMLAssertion": str,
        "RoleArn": str,
        "PrincipalArn": str,
        "DurationSeconds": NotRequired[int],
    },
)
AuditContextTypeDef = TypedDict(
    "AuditContextTypeDef",
    {
        "AdditionalAuditContext": NotRequired[str],
    },
)
ErrorDetailTypeDef = TypedDict(
    "ErrorDetailTypeDef",
    {
        "ErrorCode": NotRequired[str],
        "ErrorMessage": NotRequired[str],
    },
)
DataLakePrincipalTypeDef = TypedDict(
    "DataLakePrincipalTypeDef",
    {
        "DataLakePrincipalIdentifier": NotRequired[str],
    },
)
CancelTransactionRequestRequestTypeDef = TypedDict(
    "CancelTransactionRequestRequestTypeDef",
    {
        "TransactionId": str,
    },
)
LFTagPairPaginatorTypeDef = TypedDict(
    "LFTagPairPaginatorTypeDef",
    {
        "TagKey": str,
        "TagValues": List[str],
        "CatalogId": NotRequired[str],
    },
)
ColumnWildcardPaginatorTypeDef = TypedDict(
    "ColumnWildcardPaginatorTypeDef",
    {
        "ExcludedColumnNames": NotRequired[List[str]],
    },
)
ColumnWildcardTypeDef = TypedDict(
    "ColumnWildcardTypeDef",
    {
        "ExcludedColumnNames": NotRequired[Sequence[str]],
    },
)
CommitTransactionRequestRequestTypeDef = TypedDict(
    "CommitTransactionRequestRequestTypeDef",
    {
        "TransactionId": str,
    },
)
CreateLFTagRequestRequestTypeDef = TypedDict(
    "CreateLFTagRequestRequestTypeDef",
    {
        "TagKey": str,
        "TagValues": Sequence[str],
        "CatalogId": NotRequired[str],
    },
)
ExternalFilteringConfigurationTypeDef = TypedDict(
    "ExternalFilteringConfigurationTypeDef",
    {
        "Status": EnableStatusType,
        "AuthorizedTargets": Sequence[str],
    },
)
RowFilterPaginatorTypeDef = TypedDict(
    "RowFilterPaginatorTypeDef",
    {
        "FilterExpression": NotRequired[str],
        "AllRowsWildcard": NotRequired[Dict[str, Any]],
    },
)
DataCellsFilterResourceTypeDef = TypedDict(
    "DataCellsFilterResourceTypeDef",
    {
        "TableCatalogId": NotRequired[str],
        "DatabaseName": NotRequired[str],
        "TableName": NotRequired[str],
        "Name": NotRequired[str],
    },
)
RowFilterTypeDef = TypedDict(
    "RowFilterTypeDef",
    {
        "FilterExpression": NotRequired[str],
        "AllRowsWildcard": NotRequired[Mapping[str, Any]],
    },
)
DataLocationResourceTypeDef = TypedDict(
    "DataLocationResourceTypeDef",
    {
        "ResourceArn": str,
        "CatalogId": NotRequired[str],
    },
)
DatabaseResourceTypeDef = TypedDict(
    "DatabaseResourceTypeDef",
    {
        "Name": str,
        "CatalogId": NotRequired[str],
    },
)
DeleteDataCellsFilterRequestRequestTypeDef = TypedDict(
    "DeleteDataCellsFilterRequestRequestTypeDef",
    {
        "TableCatalogId": NotRequired[str],
        "DatabaseName": NotRequired[str],
        "TableName": NotRequired[str],
        "Name": NotRequired[str],
    },
)
DeleteLFTagRequestRequestTypeDef = TypedDict(
    "DeleteLFTagRequestRequestTypeDef",
    {
        "TagKey": str,
        "CatalogId": NotRequired[str],
    },
)
DeleteLakeFormationIdentityCenterConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteLakeFormationIdentityCenterConfigurationRequestRequestTypeDef",
    {
        "CatalogId": NotRequired[str],
    },
)
DeleteObjectInputTypeDef = TypedDict(
    "DeleteObjectInputTypeDef",
    {
        "Uri": str,
        "ETag": NotRequired[str],
        "PartitionValues": NotRequired[Sequence[str]],
    },
)
VirtualObjectTypeDef = TypedDict(
    "VirtualObjectTypeDef",
    {
        "Uri": str,
        "ETag": NotRequired[str],
    },
)
DeregisterResourceRequestRequestTypeDef = TypedDict(
    "DeregisterResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
DescribeLakeFormationIdentityCenterConfigurationRequestRequestTypeDef = TypedDict(
    "DescribeLakeFormationIdentityCenterConfigurationRequestRequestTypeDef",
    {
        "CatalogId": NotRequired[str],
    },
)
DescribeResourceRequestRequestTypeDef = TypedDict(
    "DescribeResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
ResourceInfoTypeDef = TypedDict(
    "ResourceInfoTypeDef",
    {
        "ResourceArn": NotRequired[str],
        "RoleArn": NotRequired[str],
        "LastModified": NotRequired[datetime],
        "WithFederation": NotRequired[bool],
        "HybridAccessEnabled": NotRequired[bool],
    },
)
DescribeTransactionRequestRequestTypeDef = TypedDict(
    "DescribeTransactionRequestRequestTypeDef",
    {
        "TransactionId": str,
    },
)
TransactionDescriptionTypeDef = TypedDict(
    "TransactionDescriptionTypeDef",
    {
        "TransactionId": NotRequired[str],
        "TransactionStatus": NotRequired[TransactionStatusType],
        "TransactionStartTime": NotRequired[datetime],
        "TransactionEndTime": NotRequired[datetime],
    },
)
DetailsMapTypeDef = TypedDict(
    "DetailsMapTypeDef",
    {
        "ResourceShare": NotRequired[List[str]],
    },
)
ExecutionStatisticsTypeDef = TypedDict(
    "ExecutionStatisticsTypeDef",
    {
        "AverageExecutionTimeMillis": NotRequired[int],
        "DataScannedBytes": NotRequired[int],
        "WorkUnitsExecutedCount": NotRequired[int],
    },
)
ExtendTransactionRequestRequestTypeDef = TypedDict(
    "ExtendTransactionRequestRequestTypeDef",
    {
        "TransactionId": NotRequired[str],
    },
)
FilterConditionTypeDef = TypedDict(
    "FilterConditionTypeDef",
    {
        "Field": NotRequired[FieldNameStringType],
        "ComparisonOperator": NotRequired[ComparisonOperatorType],
        "StringValueList": NotRequired[Sequence[str]],
    },
)
GetDataCellsFilterRequestRequestTypeDef = TypedDict(
    "GetDataCellsFilterRequestRequestTypeDef",
    {
        "TableCatalogId": str,
        "DatabaseName": str,
        "TableName": str,
        "Name": str,
    },
)
GetDataLakeSettingsRequestRequestTypeDef = TypedDict(
    "GetDataLakeSettingsRequestRequestTypeDef",
    {
        "CatalogId": NotRequired[str],
    },
)
GetEffectivePermissionsForPathRequestRequestTypeDef = TypedDict(
    "GetEffectivePermissionsForPathRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "CatalogId": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
GetLFTagRequestRequestTypeDef = TypedDict(
    "GetLFTagRequestRequestTypeDef",
    {
        "TagKey": str,
        "CatalogId": NotRequired[str],
    },
)
GetQueryStateRequestRequestTypeDef = TypedDict(
    "GetQueryStateRequestRequestTypeDef",
    {
        "QueryId": str,
    },
)
GetQueryStatisticsRequestRequestTypeDef = TypedDict(
    "GetQueryStatisticsRequestRequestTypeDef",
    {
        "QueryId": str,
    },
)
PlanningStatisticsTypeDef = TypedDict(
    "PlanningStatisticsTypeDef",
    {
        "EstimatedDataToScanBytes": NotRequired[int],
        "PlanningTimeMillis": NotRequired[int],
        "QueueTimeMillis": NotRequired[int],
        "WorkUnitsGeneratedCount": NotRequired[int],
    },
)
TimestampTypeDef = Union[datetime, str]
PartitionValueListTypeDef = TypedDict(
    "PartitionValueListTypeDef",
    {
        "Values": Sequence[str],
    },
)
GetWorkUnitResultsRequestRequestTypeDef = TypedDict(
    "GetWorkUnitResultsRequestRequestTypeDef",
    {
        "QueryId": str,
        "WorkUnitId": int,
        "WorkUnitToken": str,
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
GetWorkUnitsRequestRequestTypeDef = TypedDict(
    "GetWorkUnitsRequestRequestTypeDef",
    {
        "QueryId": str,
        "NextToken": NotRequired[str],
        "PageSize": NotRequired[int],
    },
)
WorkUnitRangeTypeDef = TypedDict(
    "WorkUnitRangeTypeDef",
    {
        "WorkUnitIdMax": int,
        "WorkUnitIdMin": int,
        "WorkUnitToken": str,
    },
)
LFTagKeyResourceTypeDef = TypedDict(
    "LFTagKeyResourceTypeDef",
    {
        "TagKey": str,
        "TagValues": Sequence[str],
        "CatalogId": NotRequired[str],
    },
)
LFTagTypeDef = TypedDict(
    "LFTagTypeDef",
    {
        "TagKey": str,
        "TagValues": Sequence[str],
    },
)
TableResourceTypeDef = TypedDict(
    "TableResourceTypeDef",
    {
        "DatabaseName": str,
        "CatalogId": NotRequired[str],
        "Name": NotRequired[str],
        "TableWildcard": NotRequired[Mapping[str, Any]],
    },
)
ListLFTagsRequestRequestTypeDef = TypedDict(
    "ListLFTagsRequestRequestTypeDef",
    {
        "CatalogId": NotRequired[str],
        "ResourceShareType": NotRequired[ResourceShareTypeType],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListTableStorageOptimizersRequestRequestTypeDef = TypedDict(
    "ListTableStorageOptimizersRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "CatalogId": NotRequired[str],
        "StorageOptimizerType": NotRequired[OptimizerTypeType],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
StorageOptimizerTypeDef = TypedDict(
    "StorageOptimizerTypeDef",
    {
        "StorageOptimizerType": NotRequired[OptimizerTypeType],
        "Config": NotRequired[Dict[str, str]],
        "ErrorMessage": NotRequired[str],
        "Warnings": NotRequired[str],
        "LastRunDetails": NotRequired[str],
    },
)
ListTransactionsRequestRequestTypeDef = TypedDict(
    "ListTransactionsRequestRequestTypeDef",
    {
        "CatalogId": NotRequired[str],
        "StatusFilter": NotRequired[TransactionStatusFilterType],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
TableObjectTypeDef = TypedDict(
    "TableObjectTypeDef",
    {
        "Uri": NotRequired[str],
        "ETag": NotRequired[str],
        "Size": NotRequired[int],
    },
)
RegisterResourceRequestRequestTypeDef = TypedDict(
    "RegisterResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "UseServiceLinkedRole": NotRequired[bool],
        "RoleArn": NotRequired[str],
        "WithFederation": NotRequired[bool],
        "HybridAccessEnabled": NotRequired[bool],
    },
)
StartTransactionRequestRequestTypeDef = TypedDict(
    "StartTransactionRequestRequestTypeDef",
    {
        "TransactionType": NotRequired[TransactionTypeType],
    },
)
UpdateLFTagRequestRequestTypeDef = TypedDict(
    "UpdateLFTagRequestRequestTypeDef",
    {
        "TagKey": str,
        "CatalogId": NotRequired[str],
        "TagValuesToDelete": NotRequired[Sequence[str]],
        "TagValuesToAdd": NotRequired[Sequence[str]],
    },
)
UpdateResourceRequestRequestTypeDef = TypedDict(
    "UpdateResourceRequestRequestTypeDef",
    {
        "RoleArn": str,
        "ResourceArn": str,
        "WithFederation": NotRequired[bool],
        "HybridAccessEnabled": NotRequired[bool],
    },
)
UpdateTableStorageOptimizerRequestRequestTypeDef = TypedDict(
    "UpdateTableStorageOptimizerRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "StorageOptimizerConfig": Mapping[OptimizerTypeType, Mapping[str, str]],
        "CatalogId": NotRequired[str],
    },
)
ColumnLFTagTypeDef = TypedDict(
    "ColumnLFTagTypeDef",
    {
        "Name": NotRequired[str],
        "LFTags": NotRequired[List[LFTagPairTypeDef]],
    },
)
AssumeDecoratedRoleWithSAMLResponseTypeDef = TypedDict(
    "AssumeDecoratedRoleWithSAMLResponseTypeDef",
    {
        "AccessKeyId": str,
        "SecretAccessKey": str,
        "SessionToken": str,
        "Expiration": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CommitTransactionResponseTypeDef = TypedDict(
    "CommitTransactionResponseTypeDef",
    {
        "TransactionStatus": TransactionStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateLakeFormationIdentityCenterConfigurationResponseTypeDef = TypedDict(
    "CreateLakeFormationIdentityCenterConfigurationResponseTypeDef",
    {
        "ApplicationArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetLFTagResponseTypeDef = TypedDict(
    "GetLFTagResponseTypeDef",
    {
        "CatalogId": str,
        "TagKey": str,
        "TagValues": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetQueryStateResponseTypeDef = TypedDict(
    "GetQueryStateResponseTypeDef",
    {
        "Error": str,
        "State": QueryStateStringType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetTemporaryGluePartitionCredentialsResponseTypeDef = TypedDict(
    "GetTemporaryGluePartitionCredentialsResponseTypeDef",
    {
        "AccessKeyId": str,
        "SecretAccessKey": str,
        "SessionToken": str,
        "Expiration": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetTemporaryGlueTableCredentialsResponseTypeDef = TypedDict(
    "GetTemporaryGlueTableCredentialsResponseTypeDef",
    {
        "AccessKeyId": str,
        "SecretAccessKey": str,
        "SessionToken": str,
        "Expiration": datetime,
        "VendedS3Path": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetWorkUnitResultsResponseTypeDef = TypedDict(
    "GetWorkUnitResultsResponseTypeDef",
    {
        "ResultStream": StreamingBody,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListLFTagsResponseTypeDef = TypedDict(
    "ListLFTagsResponseTypeDef",
    {
        "LFTags": List[LFTagPairTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartQueryPlanningResponseTypeDef = TypedDict(
    "StartQueryPlanningResponseTypeDef",
    {
        "QueryId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartTransactionResponseTypeDef = TypedDict(
    "StartTransactionResponseTypeDef",
    {
        "TransactionId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateTableStorageOptimizerResponseTypeDef = TypedDict(
    "UpdateTableStorageOptimizerResponseTypeDef",
    {
        "Result": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
LFTagErrorTypeDef = TypedDict(
    "LFTagErrorTypeDef",
    {
        "LFTag": NotRequired[LFTagPairTypeDef],
        "Error": NotRequired[ErrorDetailTypeDef],
    },
)
PrincipalPermissionsTypeDef = TypedDict(
    "PrincipalPermissionsTypeDef",
    {
        "Principal": NotRequired[DataLakePrincipalTypeDef],
        "Permissions": NotRequired[List[PermissionType]],
    },
)
ColumnLFTagPaginatorTypeDef = TypedDict(
    "ColumnLFTagPaginatorTypeDef",
    {
        "Name": NotRequired[str],
        "LFTags": NotRequired[List[LFTagPairPaginatorTypeDef]],
    },
)
ListLFTagsResponsePaginatorTypeDef = TypedDict(
    "ListLFTagsResponsePaginatorTypeDef",
    {
        "LFTags": List[LFTagPairPaginatorTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TableWithColumnsResourceTypeDef = TypedDict(
    "TableWithColumnsResourceTypeDef",
    {
        "DatabaseName": str,
        "Name": str,
        "CatalogId": NotRequired[str],
        "ColumnNames": NotRequired[Sequence[str]],
        "ColumnWildcard": NotRequired[ColumnWildcardTypeDef],
    },
)
CreateLakeFormationIdentityCenterConfigurationRequestRequestTypeDef = TypedDict(
    "CreateLakeFormationIdentityCenterConfigurationRequestRequestTypeDef",
    {
        "CatalogId": NotRequired[str],
        "InstanceArn": NotRequired[str],
        "ExternalFiltering": NotRequired[ExternalFilteringConfigurationTypeDef],
    },
)
DescribeLakeFormationIdentityCenterConfigurationResponseTypeDef = TypedDict(
    "DescribeLakeFormationIdentityCenterConfigurationResponseTypeDef",
    {
        "CatalogId": str,
        "InstanceArn": str,
        "ApplicationArn": str,
        "ExternalFiltering": ExternalFilteringConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateLakeFormationIdentityCenterConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateLakeFormationIdentityCenterConfigurationRequestRequestTypeDef",
    {
        "CatalogId": NotRequired[str],
        "ApplicationStatus": NotRequired[ApplicationStatusType],
        "ExternalFiltering": NotRequired[ExternalFilteringConfigurationTypeDef],
    },
)
DataCellsFilterPaginatorTypeDef = TypedDict(
    "DataCellsFilterPaginatorTypeDef",
    {
        "TableCatalogId": str,
        "DatabaseName": str,
        "TableName": str,
        "Name": str,
        "RowFilter": NotRequired[RowFilterPaginatorTypeDef],
        "ColumnNames": NotRequired[List[str]],
        "ColumnWildcard": NotRequired[ColumnWildcardPaginatorTypeDef],
        "VersionId": NotRequired[str],
    },
)
DataCellsFilterTypeDef = TypedDict(
    "DataCellsFilterTypeDef",
    {
        "TableCatalogId": str,
        "DatabaseName": str,
        "TableName": str,
        "Name": str,
        "RowFilter": NotRequired[RowFilterTypeDef],
        "ColumnNames": NotRequired[Sequence[str]],
        "ColumnWildcard": NotRequired[ColumnWildcardTypeDef],
        "VersionId": NotRequired[str],
    },
)
TaggedDatabasePaginatorTypeDef = TypedDict(
    "TaggedDatabasePaginatorTypeDef",
    {
        "Database": NotRequired[DatabaseResourceTypeDef],
        "LFTags": NotRequired[List[LFTagPairPaginatorTypeDef]],
    },
)
TaggedDatabaseTypeDef = TypedDict(
    "TaggedDatabaseTypeDef",
    {
        "Database": NotRequired[DatabaseResourceTypeDef],
        "LFTags": NotRequired[List[LFTagPairTypeDef]],
    },
)
WriteOperationTypeDef = TypedDict(
    "WriteOperationTypeDef",
    {
        "AddObject": NotRequired[AddObjectInputTypeDef],
        "DeleteObject": NotRequired[DeleteObjectInputTypeDef],
    },
)
DeleteObjectsOnCancelRequestRequestTypeDef = TypedDict(
    "DeleteObjectsOnCancelRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "TransactionId": str,
        "Objects": Sequence[VirtualObjectTypeDef],
        "CatalogId": NotRequired[str],
    },
)
DescribeResourceResponseTypeDef = TypedDict(
    "DescribeResourceResponseTypeDef",
    {
        "ResourceInfo": ResourceInfoTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListResourcesResponseTypeDef = TypedDict(
    "ListResourcesResponseTypeDef",
    {
        "ResourceInfoList": List[ResourceInfoTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeTransactionResponseTypeDef = TypedDict(
    "DescribeTransactionResponseTypeDef",
    {
        "TransactionDescription": TransactionDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTransactionsResponseTypeDef = TypedDict(
    "ListTransactionsResponseTypeDef",
    {
        "Transactions": List[TransactionDescriptionTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListResourcesRequestRequestTypeDef = TypedDict(
    "ListResourcesRequestRequestTypeDef",
    {
        "FilterConditionList": NotRequired[Sequence[FilterConditionTypeDef]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
GetQueryStatisticsResponseTypeDef = TypedDict(
    "GetQueryStatisticsResponseTypeDef",
    {
        "ExecutionStatistics": ExecutionStatisticsTypeDef,
        "PlanningStatistics": PlanningStatisticsTypeDef,
        "QuerySubmissionTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetTableObjectsRequestRequestTypeDef = TypedDict(
    "GetTableObjectsRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "CatalogId": NotRequired[str],
        "TransactionId": NotRequired[str],
        "QueryAsOfTime": NotRequired[TimestampTypeDef],
        "PartitionPredicate": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
QueryPlanningContextTypeDef = TypedDict(
    "QueryPlanningContextTypeDef",
    {
        "DatabaseName": str,
        "CatalogId": NotRequired[str],
        "QueryAsOfTime": NotRequired[TimestampTypeDef],
        "QueryParameters": NotRequired[Mapping[str, str]],
        "TransactionId": NotRequired[str],
    },
)
QuerySessionContextTypeDef = TypedDict(
    "QuerySessionContextTypeDef",
    {
        "QueryId": NotRequired[str],
        "QueryStartTime": NotRequired[TimestampTypeDef],
        "ClusterId": NotRequired[str],
        "QueryAuthorizationId": NotRequired[str],
        "AdditionalContext": NotRequired[Mapping[str, str]],
    },
)
GetTemporaryGluePartitionCredentialsRequestRequestTypeDef = TypedDict(
    "GetTemporaryGluePartitionCredentialsRequestRequestTypeDef",
    {
        "TableArn": str,
        "Partition": PartitionValueListTypeDef,
        "Permissions": NotRequired[Sequence[PermissionType]],
        "DurationSeconds": NotRequired[int],
        "AuditContext": NotRequired[AuditContextTypeDef],
        "SupportedPermissionTypes": NotRequired[Sequence[PermissionTypeType]],
    },
)
GetWorkUnitsRequestGetWorkUnitsPaginateTypeDef = TypedDict(
    "GetWorkUnitsRequestGetWorkUnitsPaginateTypeDef",
    {
        "QueryId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListLFTagsRequestListLFTagsPaginateTypeDef = TypedDict(
    "ListLFTagsRequestListLFTagsPaginateTypeDef",
    {
        "CatalogId": NotRequired[str],
        "ResourceShareType": NotRequired[ResourceShareTypeType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetWorkUnitsResponseTypeDef = TypedDict(
    "GetWorkUnitsResponseTypeDef",
    {
        "NextToken": str,
        "QueryId": str,
        "WorkUnitRanges": List[WorkUnitRangeTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
LFTagPolicyResourceTypeDef = TypedDict(
    "LFTagPolicyResourceTypeDef",
    {
        "ResourceType": ResourceTypeType,
        "Expression": Sequence[LFTagTypeDef],
        "CatalogId": NotRequired[str],
    },
)
SearchDatabasesByLFTagsRequestRequestTypeDef = TypedDict(
    "SearchDatabasesByLFTagsRequestRequestTypeDef",
    {
        "Expression": Sequence[LFTagTypeDef],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "CatalogId": NotRequired[str],
    },
)
SearchDatabasesByLFTagsRequestSearchDatabasesByLFTagsPaginateTypeDef = TypedDict(
    "SearchDatabasesByLFTagsRequestSearchDatabasesByLFTagsPaginateTypeDef",
    {
        "Expression": Sequence[LFTagTypeDef],
        "CatalogId": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
SearchTablesByLFTagsRequestRequestTypeDef = TypedDict(
    "SearchTablesByLFTagsRequestRequestTypeDef",
    {
        "Expression": Sequence[LFTagTypeDef],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "CatalogId": NotRequired[str],
    },
)
SearchTablesByLFTagsRequestSearchTablesByLFTagsPaginateTypeDef = TypedDict(
    "SearchTablesByLFTagsRequestSearchTablesByLFTagsPaginateTypeDef",
    {
        "Expression": Sequence[LFTagTypeDef],
        "CatalogId": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDataCellsFilterRequestListDataCellsFilterPaginateTypeDef = TypedDict(
    "ListDataCellsFilterRequestListDataCellsFilterPaginateTypeDef",
    {
        "Table": NotRequired[TableResourceTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDataCellsFilterRequestRequestTypeDef = TypedDict(
    "ListDataCellsFilterRequestRequestTypeDef",
    {
        "Table": NotRequired[TableResourceTypeDef],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListTableStorageOptimizersResponseTypeDef = TypedDict(
    "ListTableStorageOptimizersResponseTypeDef",
    {
        "StorageOptimizerList": List[StorageOptimizerTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PartitionObjectsTypeDef = TypedDict(
    "PartitionObjectsTypeDef",
    {
        "PartitionValues": NotRequired[List[str]],
        "Objects": NotRequired[List[TableObjectTypeDef]],
    },
)
GetResourceLFTagsResponseTypeDef = TypedDict(
    "GetResourceLFTagsResponseTypeDef",
    {
        "LFTagOnDatabase": List[LFTagPairTypeDef],
        "LFTagsOnTable": List[LFTagPairTypeDef],
        "LFTagsOnColumns": List[ColumnLFTagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TaggedTableTypeDef = TypedDict(
    "TaggedTableTypeDef",
    {
        "Table": NotRequired[TableResourceTypeDef],
        "LFTagOnDatabase": NotRequired[List[LFTagPairTypeDef]],
        "LFTagsOnTable": NotRequired[List[LFTagPairTypeDef]],
        "LFTagsOnColumns": NotRequired[List[ColumnLFTagTypeDef]],
    },
)
AddLFTagsToResourceResponseTypeDef = TypedDict(
    "AddLFTagsToResourceResponseTypeDef",
    {
        "Failures": List[LFTagErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RemoveLFTagsFromResourceResponseTypeDef = TypedDict(
    "RemoveLFTagsFromResourceResponseTypeDef",
    {
        "Failures": List[LFTagErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DataLakeSettingsTypeDef = TypedDict(
    "DataLakeSettingsTypeDef",
    {
        "DataLakeAdmins": NotRequired[List[DataLakePrincipalTypeDef]],
        "ReadOnlyAdmins": NotRequired[List[DataLakePrincipalTypeDef]],
        "CreateDatabaseDefaultPermissions": NotRequired[List[PrincipalPermissionsTypeDef]],
        "CreateTableDefaultPermissions": NotRequired[List[PrincipalPermissionsTypeDef]],
        "Parameters": NotRequired[Dict[str, str]],
        "TrustedResourceOwners": NotRequired[List[str]],
        "AllowExternalDataFiltering": NotRequired[bool],
        "AllowFullTableExternalDataAccess": NotRequired[bool],
        "ExternalDataFilteringAllowList": NotRequired[List[DataLakePrincipalTypeDef]],
        "AuthorizedSessionTagValueList": NotRequired[List[str]],
    },
)
TaggedTablePaginatorTypeDef = TypedDict(
    "TaggedTablePaginatorTypeDef",
    {
        "Table": NotRequired[TableResourceTypeDef],
        "LFTagOnDatabase": NotRequired[List[LFTagPairPaginatorTypeDef]],
        "LFTagsOnTable": NotRequired[List[LFTagPairPaginatorTypeDef]],
        "LFTagsOnColumns": NotRequired[List[ColumnLFTagPaginatorTypeDef]],
    },
)
ListDataCellsFilterResponsePaginatorTypeDef = TypedDict(
    "ListDataCellsFilterResponsePaginatorTypeDef",
    {
        "DataCellsFilters": List[DataCellsFilterPaginatorTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDataCellsFilterRequestRequestTypeDef = TypedDict(
    "CreateDataCellsFilterRequestRequestTypeDef",
    {
        "TableData": DataCellsFilterTypeDef,
    },
)
GetDataCellsFilterResponseTypeDef = TypedDict(
    "GetDataCellsFilterResponseTypeDef",
    {
        "DataCellsFilter": DataCellsFilterTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListDataCellsFilterResponseTypeDef = TypedDict(
    "ListDataCellsFilterResponseTypeDef",
    {
        "DataCellsFilters": List[DataCellsFilterTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateDataCellsFilterRequestRequestTypeDef = TypedDict(
    "UpdateDataCellsFilterRequestRequestTypeDef",
    {
        "TableData": DataCellsFilterTypeDef,
    },
)
SearchDatabasesByLFTagsResponsePaginatorTypeDef = TypedDict(
    "SearchDatabasesByLFTagsResponsePaginatorTypeDef",
    {
        "NextToken": str,
        "DatabaseList": List[TaggedDatabasePaginatorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SearchDatabasesByLFTagsResponseTypeDef = TypedDict(
    "SearchDatabasesByLFTagsResponseTypeDef",
    {
        "NextToken": str,
        "DatabaseList": List[TaggedDatabaseTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateTableObjectsRequestRequestTypeDef = TypedDict(
    "UpdateTableObjectsRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "WriteOperations": Sequence[WriteOperationTypeDef],
        "CatalogId": NotRequired[str],
        "TransactionId": NotRequired[str],
    },
)
StartQueryPlanningRequestRequestTypeDef = TypedDict(
    "StartQueryPlanningRequestRequestTypeDef",
    {
        "QueryPlanningContext": QueryPlanningContextTypeDef,
        "QueryString": str,
    },
)
GetTemporaryGlueTableCredentialsRequestRequestTypeDef = TypedDict(
    "GetTemporaryGlueTableCredentialsRequestRequestTypeDef",
    {
        "TableArn": str,
        "Permissions": NotRequired[Sequence[PermissionType]],
        "DurationSeconds": NotRequired[int],
        "AuditContext": NotRequired[AuditContextTypeDef],
        "SupportedPermissionTypes": NotRequired[Sequence[PermissionTypeType]],
        "S3Path": NotRequired[str],
        "QuerySessionContext": NotRequired[QuerySessionContextTypeDef],
    },
)
ResourceTypeDef = TypedDict(
    "ResourceTypeDef",
    {
        "Catalog": NotRequired[Mapping[str, Any]],
        "Database": NotRequired[DatabaseResourceTypeDef],
        "Table": NotRequired[TableResourceTypeDef],
        "TableWithColumns": NotRequired[TableWithColumnsResourceTypeDef],
        "DataLocation": NotRequired[DataLocationResourceTypeDef],
        "DataCellsFilter": NotRequired[DataCellsFilterResourceTypeDef],
        "LFTag": NotRequired[LFTagKeyResourceTypeDef],
        "LFTagPolicy": NotRequired[LFTagPolicyResourceTypeDef],
    },
)
GetTableObjectsResponseTypeDef = TypedDict(
    "GetTableObjectsResponseTypeDef",
    {
        "Objects": List[PartitionObjectsTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SearchTablesByLFTagsResponseTypeDef = TypedDict(
    "SearchTablesByLFTagsResponseTypeDef",
    {
        "NextToken": str,
        "TableList": List[TaggedTableTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetDataLakeSettingsResponseTypeDef = TypedDict(
    "GetDataLakeSettingsResponseTypeDef",
    {
        "DataLakeSettings": DataLakeSettingsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutDataLakeSettingsRequestRequestTypeDef = TypedDict(
    "PutDataLakeSettingsRequestRequestTypeDef",
    {
        "DataLakeSettings": DataLakeSettingsTypeDef,
        "CatalogId": NotRequired[str],
    },
)
SearchTablesByLFTagsResponsePaginatorTypeDef = TypedDict(
    "SearchTablesByLFTagsResponsePaginatorTypeDef",
    {
        "NextToken": str,
        "TableList": List[TaggedTablePaginatorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AddLFTagsToResourceRequestRequestTypeDef = TypedDict(
    "AddLFTagsToResourceRequestRequestTypeDef",
    {
        "Resource": ResourceTypeDef,
        "LFTags": Sequence[LFTagPairTypeDef],
        "CatalogId": NotRequired[str],
    },
)
BatchPermissionsRequestEntryTypeDef = TypedDict(
    "BatchPermissionsRequestEntryTypeDef",
    {
        "Id": str,
        "Principal": NotRequired[DataLakePrincipalTypeDef],
        "Resource": NotRequired[ResourceTypeDef],
        "Permissions": NotRequired[Sequence[PermissionType]],
        "PermissionsWithGrantOption": NotRequired[Sequence[PermissionType]],
    },
)
CreateLakeFormationOptInRequestRequestTypeDef = TypedDict(
    "CreateLakeFormationOptInRequestRequestTypeDef",
    {
        "Principal": DataLakePrincipalTypeDef,
        "Resource": ResourceTypeDef,
    },
)
DeleteLakeFormationOptInRequestRequestTypeDef = TypedDict(
    "DeleteLakeFormationOptInRequestRequestTypeDef",
    {
        "Principal": DataLakePrincipalTypeDef,
        "Resource": ResourceTypeDef,
    },
)
GetResourceLFTagsRequestRequestTypeDef = TypedDict(
    "GetResourceLFTagsRequestRequestTypeDef",
    {
        "Resource": ResourceTypeDef,
        "CatalogId": NotRequired[str],
        "ShowAssignedLFTags": NotRequired[bool],
    },
)
GrantPermissionsRequestRequestTypeDef = TypedDict(
    "GrantPermissionsRequestRequestTypeDef",
    {
        "Principal": DataLakePrincipalTypeDef,
        "Resource": ResourceTypeDef,
        "Permissions": Sequence[PermissionType],
        "CatalogId": NotRequired[str],
        "PermissionsWithGrantOption": NotRequired[Sequence[PermissionType]],
    },
)
LakeFormationOptInsInfoTypeDef = TypedDict(
    "LakeFormationOptInsInfoTypeDef",
    {
        "Resource": NotRequired[ResourceTypeDef],
        "Principal": NotRequired[DataLakePrincipalTypeDef],
        "LastModified": NotRequired[datetime],
        "LastUpdatedBy": NotRequired[str],
    },
)
ListLakeFormationOptInsRequestRequestTypeDef = TypedDict(
    "ListLakeFormationOptInsRequestRequestTypeDef",
    {
        "Principal": NotRequired[DataLakePrincipalTypeDef],
        "Resource": NotRequired[ResourceTypeDef],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListPermissionsRequestRequestTypeDef = TypedDict(
    "ListPermissionsRequestRequestTypeDef",
    {
        "CatalogId": NotRequired[str],
        "Principal": NotRequired[DataLakePrincipalTypeDef],
        "ResourceType": NotRequired[DataLakeResourceTypeType],
        "Resource": NotRequired[ResourceTypeDef],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "IncludeRelated": NotRequired[str],
    },
)
PrincipalResourcePermissionsTypeDef = TypedDict(
    "PrincipalResourcePermissionsTypeDef",
    {
        "Principal": NotRequired[DataLakePrincipalTypeDef],
        "Resource": NotRequired[ResourceTypeDef],
        "Permissions": NotRequired[List[PermissionType]],
        "PermissionsWithGrantOption": NotRequired[List[PermissionType]],
        "AdditionalDetails": NotRequired[DetailsMapTypeDef],
        "LastUpdated": NotRequired[datetime],
        "LastUpdatedBy": NotRequired[str],
    },
)
RemoveLFTagsFromResourceRequestRequestTypeDef = TypedDict(
    "RemoveLFTagsFromResourceRequestRequestTypeDef",
    {
        "Resource": ResourceTypeDef,
        "LFTags": Sequence[LFTagPairTypeDef],
        "CatalogId": NotRequired[str],
    },
)
RevokePermissionsRequestRequestTypeDef = TypedDict(
    "RevokePermissionsRequestRequestTypeDef",
    {
        "Principal": DataLakePrincipalTypeDef,
        "Resource": ResourceTypeDef,
        "Permissions": Sequence[PermissionType],
        "CatalogId": NotRequired[str],
        "PermissionsWithGrantOption": NotRequired[Sequence[PermissionType]],
    },
)
BatchGrantPermissionsRequestRequestTypeDef = TypedDict(
    "BatchGrantPermissionsRequestRequestTypeDef",
    {
        "Entries": Sequence[BatchPermissionsRequestEntryTypeDef],
        "CatalogId": NotRequired[str],
    },
)
BatchPermissionsFailureEntryTypeDef = TypedDict(
    "BatchPermissionsFailureEntryTypeDef",
    {
        "RequestEntry": NotRequired[BatchPermissionsRequestEntryTypeDef],
        "Error": NotRequired[ErrorDetailTypeDef],
    },
)
BatchRevokePermissionsRequestRequestTypeDef = TypedDict(
    "BatchRevokePermissionsRequestRequestTypeDef",
    {
        "Entries": Sequence[BatchPermissionsRequestEntryTypeDef],
        "CatalogId": NotRequired[str],
    },
)
ListLakeFormationOptInsResponseTypeDef = TypedDict(
    "ListLakeFormationOptInsResponseTypeDef",
    {
        "LakeFormationOptInsInfoList": List[LakeFormationOptInsInfoTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetEffectivePermissionsForPathResponseTypeDef = TypedDict(
    "GetEffectivePermissionsForPathResponseTypeDef",
    {
        "Permissions": List[PrincipalResourcePermissionsTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListPermissionsResponseTypeDef = TypedDict(
    "ListPermissionsResponseTypeDef",
    {
        "PrincipalResourcePermissions": List[PrincipalResourcePermissionsTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchGrantPermissionsResponseTypeDef = TypedDict(
    "BatchGrantPermissionsResponseTypeDef",
    {
        "Failures": List[BatchPermissionsFailureEntryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchRevokePermissionsResponseTypeDef = TypedDict(
    "BatchRevokePermissionsResponseTypeDef",
    {
        "Failures": List[BatchPermissionsFailureEntryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
