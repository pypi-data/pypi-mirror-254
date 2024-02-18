"""
Type annotations for route53-recovery-readiness service type definitions.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_route53_recovery_readiness/type_defs/)

Usage::

    ```python
    from types_aiobotocore_route53_recovery_readiness.type_defs import CellOutputTypeDef

    data: CellOutputTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from .literals import ReadinessType

if sys.version_info >= (3, 12):
    from typing import NotRequired
else:
    from typing_extensions import NotRequired
if sys.version_info >= (3, 12):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "CellOutputTypeDef",
    "CreateCellRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "CreateCrossAccountAuthorizationRequestRequestTypeDef",
    "CreateReadinessCheckRequestRequestTypeDef",
    "CreateRecoveryGroupRequestRequestTypeDef",
    "DeleteCellRequestRequestTypeDef",
    "DeleteCrossAccountAuthorizationRequestRequestTypeDef",
    "DeleteReadinessCheckRequestRequestTypeDef",
    "DeleteRecoveryGroupRequestRequestTypeDef",
    "DeleteResourceSetRequestRequestTypeDef",
    "GetArchitectureRecommendationsRequestRequestTypeDef",
    "RecommendationTypeDef",
    "PaginatorConfigTypeDef",
    "GetCellReadinessSummaryRequestRequestTypeDef",
    "ReadinessCheckSummaryTypeDef",
    "GetCellRequestRequestTypeDef",
    "GetReadinessCheckRequestRequestTypeDef",
    "GetReadinessCheckResourceStatusRequestRequestTypeDef",
    "GetReadinessCheckStatusRequestRequestTypeDef",
    "MessageTypeDef",
    "ResourceResultTypeDef",
    "GetRecoveryGroupReadinessSummaryRequestRequestTypeDef",
    "GetRecoveryGroupRequestRequestTypeDef",
    "GetResourceSetRequestRequestTypeDef",
    "ListCellsRequestRequestTypeDef",
    "ListCrossAccountAuthorizationsRequestRequestTypeDef",
    "ListReadinessChecksRequestRequestTypeDef",
    "ReadinessCheckOutputTypeDef",
    "ListRecoveryGroupsRequestRequestTypeDef",
    "RecoveryGroupOutputTypeDef",
    "ListResourceSetsRequestRequestTypeDef",
    "ListRulesOutputTypeDef",
    "ListRulesRequestRequestTypeDef",
    "ListTagsForResourcesRequestRequestTypeDef",
    "NLBResourceTypeDef",
    "R53ResourceRecordTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateCellRequestRequestTypeDef",
    "UpdateReadinessCheckRequestRequestTypeDef",
    "UpdateRecoveryGroupRequestRequestTypeDef",
    "CreateCellResponseTypeDef",
    "CreateCrossAccountAuthorizationResponseTypeDef",
    "CreateReadinessCheckResponseTypeDef",
    "CreateRecoveryGroupResponseTypeDef",
    "EmptyResponseMetadataTypeDef",
    "GetCellResponseTypeDef",
    "GetReadinessCheckResponseTypeDef",
    "GetRecoveryGroupResponseTypeDef",
    "ListCellsResponseTypeDef",
    "ListCrossAccountAuthorizationsResponseTypeDef",
    "ListTagsForResourcesResponseTypeDef",
    "UpdateCellResponseTypeDef",
    "UpdateReadinessCheckResponseTypeDef",
    "UpdateRecoveryGroupResponseTypeDef",
    "GetArchitectureRecommendationsResponseTypeDef",
    "GetCellReadinessSummaryRequestGetCellReadinessSummaryPaginateTypeDef",
    "GetReadinessCheckResourceStatusRequestGetReadinessCheckResourceStatusPaginateTypeDef",
    "GetReadinessCheckStatusRequestGetReadinessCheckStatusPaginateTypeDef",
    "GetRecoveryGroupReadinessSummaryRequestGetRecoveryGroupReadinessSummaryPaginateTypeDef",
    "ListCellsRequestListCellsPaginateTypeDef",
    "ListCrossAccountAuthorizationsRequestListCrossAccountAuthorizationsPaginateTypeDef",
    "ListReadinessChecksRequestListReadinessChecksPaginateTypeDef",
    "ListRecoveryGroupsRequestListRecoveryGroupsPaginateTypeDef",
    "ListResourceSetsRequestListResourceSetsPaginateTypeDef",
    "ListRulesRequestListRulesPaginateTypeDef",
    "GetCellReadinessSummaryResponseTypeDef",
    "GetRecoveryGroupReadinessSummaryResponseTypeDef",
    "RuleResultTypeDef",
    "GetReadinessCheckStatusResponseTypeDef",
    "ListReadinessChecksResponseTypeDef",
    "ListRecoveryGroupsResponseTypeDef",
    "ListRulesResponseTypeDef",
    "TargetResourceTypeDef",
    "GetReadinessCheckResourceStatusResponseTypeDef",
    "DNSTargetResourceTypeDef",
    "ResourcePaginatorTypeDef",
    "ResourceTypeDef",
    "ResourceSetOutputPaginatorTypeDef",
    "CreateResourceSetRequestRequestTypeDef",
    "CreateResourceSetResponseTypeDef",
    "GetResourceSetResponseTypeDef",
    "ResourceSetOutputTypeDef",
    "UpdateResourceSetRequestRequestTypeDef",
    "UpdateResourceSetResponseTypeDef",
    "ListResourceSetsResponsePaginatorTypeDef",
    "ListResourceSetsResponseTypeDef",
)

CellOutputTypeDef = TypedDict(
    "CellOutputTypeDef",
    {
        "CellArn": str,
        "CellName": str,
        "Cells": List[str],
        "ParentReadinessScopes": List[str],
        "Tags": NotRequired[Dict[str, str]],
    },
)
CreateCellRequestRequestTypeDef = TypedDict(
    "CreateCellRequestRequestTypeDef",
    {
        "CellName": str,
        "Cells": NotRequired[Sequence[str]],
        "Tags": NotRequired[Mapping[str, str]],
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
CreateCrossAccountAuthorizationRequestRequestTypeDef = TypedDict(
    "CreateCrossAccountAuthorizationRequestRequestTypeDef",
    {
        "CrossAccountAuthorization": str,
    },
)
CreateReadinessCheckRequestRequestTypeDef = TypedDict(
    "CreateReadinessCheckRequestRequestTypeDef",
    {
        "ReadinessCheckName": str,
        "ResourceSetName": str,
        "Tags": NotRequired[Mapping[str, str]],
    },
)
CreateRecoveryGroupRequestRequestTypeDef = TypedDict(
    "CreateRecoveryGroupRequestRequestTypeDef",
    {
        "RecoveryGroupName": str,
        "Cells": NotRequired[Sequence[str]],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
DeleteCellRequestRequestTypeDef = TypedDict(
    "DeleteCellRequestRequestTypeDef",
    {
        "CellName": str,
    },
)
DeleteCrossAccountAuthorizationRequestRequestTypeDef = TypedDict(
    "DeleteCrossAccountAuthorizationRequestRequestTypeDef",
    {
        "CrossAccountAuthorization": str,
    },
)
DeleteReadinessCheckRequestRequestTypeDef = TypedDict(
    "DeleteReadinessCheckRequestRequestTypeDef",
    {
        "ReadinessCheckName": str,
    },
)
DeleteRecoveryGroupRequestRequestTypeDef = TypedDict(
    "DeleteRecoveryGroupRequestRequestTypeDef",
    {
        "RecoveryGroupName": str,
    },
)
DeleteResourceSetRequestRequestTypeDef = TypedDict(
    "DeleteResourceSetRequestRequestTypeDef",
    {
        "ResourceSetName": str,
    },
)
GetArchitectureRecommendationsRequestRequestTypeDef = TypedDict(
    "GetArchitectureRecommendationsRequestRequestTypeDef",
    {
        "RecoveryGroupName": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
RecommendationTypeDef = TypedDict(
    "RecommendationTypeDef",
    {
        "RecommendationText": str,
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
GetCellReadinessSummaryRequestRequestTypeDef = TypedDict(
    "GetCellReadinessSummaryRequestRequestTypeDef",
    {
        "CellName": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ReadinessCheckSummaryTypeDef = TypedDict(
    "ReadinessCheckSummaryTypeDef",
    {
        "Readiness": NotRequired[ReadinessType],
        "ReadinessCheckName": NotRequired[str],
    },
)
GetCellRequestRequestTypeDef = TypedDict(
    "GetCellRequestRequestTypeDef",
    {
        "CellName": str,
    },
)
GetReadinessCheckRequestRequestTypeDef = TypedDict(
    "GetReadinessCheckRequestRequestTypeDef",
    {
        "ReadinessCheckName": str,
    },
)
GetReadinessCheckResourceStatusRequestRequestTypeDef = TypedDict(
    "GetReadinessCheckResourceStatusRequestRequestTypeDef",
    {
        "ReadinessCheckName": str,
        "ResourceIdentifier": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
GetReadinessCheckStatusRequestRequestTypeDef = TypedDict(
    "GetReadinessCheckStatusRequestRequestTypeDef",
    {
        "ReadinessCheckName": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
MessageTypeDef = TypedDict(
    "MessageTypeDef",
    {
        "MessageText": NotRequired[str],
    },
)
ResourceResultTypeDef = TypedDict(
    "ResourceResultTypeDef",
    {
        "LastCheckedTimestamp": datetime,
        "Readiness": ReadinessType,
        "ComponentId": NotRequired[str],
        "ResourceArn": NotRequired[str],
    },
)
GetRecoveryGroupReadinessSummaryRequestRequestTypeDef = TypedDict(
    "GetRecoveryGroupReadinessSummaryRequestRequestTypeDef",
    {
        "RecoveryGroupName": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
GetRecoveryGroupRequestRequestTypeDef = TypedDict(
    "GetRecoveryGroupRequestRequestTypeDef",
    {
        "RecoveryGroupName": str,
    },
)
GetResourceSetRequestRequestTypeDef = TypedDict(
    "GetResourceSetRequestRequestTypeDef",
    {
        "ResourceSetName": str,
    },
)
ListCellsRequestRequestTypeDef = TypedDict(
    "ListCellsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListCrossAccountAuthorizationsRequestRequestTypeDef = TypedDict(
    "ListCrossAccountAuthorizationsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListReadinessChecksRequestRequestTypeDef = TypedDict(
    "ListReadinessChecksRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ReadinessCheckOutputTypeDef = TypedDict(
    "ReadinessCheckOutputTypeDef",
    {
        "ReadinessCheckArn": str,
        "ResourceSet": str,
        "ReadinessCheckName": NotRequired[str],
        "Tags": NotRequired[Dict[str, str]],
    },
)
ListRecoveryGroupsRequestRequestTypeDef = TypedDict(
    "ListRecoveryGroupsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
RecoveryGroupOutputTypeDef = TypedDict(
    "RecoveryGroupOutputTypeDef",
    {
        "Cells": List[str],
        "RecoveryGroupArn": str,
        "RecoveryGroupName": str,
        "Tags": NotRequired[Dict[str, str]],
    },
)
ListResourceSetsRequestRequestTypeDef = TypedDict(
    "ListResourceSetsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListRulesOutputTypeDef = TypedDict(
    "ListRulesOutputTypeDef",
    {
        "ResourceType": str,
        "RuleDescription": str,
        "RuleId": str,
    },
)
ListRulesRequestRequestTypeDef = TypedDict(
    "ListRulesRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "ResourceType": NotRequired[str],
    },
)
ListTagsForResourcesRequestRequestTypeDef = TypedDict(
    "ListTagsForResourcesRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
NLBResourceTypeDef = TypedDict(
    "NLBResourceTypeDef",
    {
        "Arn": NotRequired[str],
    },
)
R53ResourceRecordTypeDef = TypedDict(
    "R53ResourceRecordTypeDef",
    {
        "DomainName": NotRequired[str],
        "RecordSetId": NotRequired[str],
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
UpdateCellRequestRequestTypeDef = TypedDict(
    "UpdateCellRequestRequestTypeDef",
    {
        "CellName": str,
        "Cells": Sequence[str],
    },
)
UpdateReadinessCheckRequestRequestTypeDef = TypedDict(
    "UpdateReadinessCheckRequestRequestTypeDef",
    {
        "ReadinessCheckName": str,
        "ResourceSetName": str,
    },
)
UpdateRecoveryGroupRequestRequestTypeDef = TypedDict(
    "UpdateRecoveryGroupRequestRequestTypeDef",
    {
        "Cells": Sequence[str],
        "RecoveryGroupName": str,
    },
)
CreateCellResponseTypeDef = TypedDict(
    "CreateCellResponseTypeDef",
    {
        "CellArn": str,
        "CellName": str,
        "Cells": List[str],
        "ParentReadinessScopes": List[str],
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateCrossAccountAuthorizationResponseTypeDef = TypedDict(
    "CreateCrossAccountAuthorizationResponseTypeDef",
    {
        "CrossAccountAuthorization": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateReadinessCheckResponseTypeDef = TypedDict(
    "CreateReadinessCheckResponseTypeDef",
    {
        "ReadinessCheckArn": str,
        "ReadinessCheckName": str,
        "ResourceSet": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateRecoveryGroupResponseTypeDef = TypedDict(
    "CreateRecoveryGroupResponseTypeDef",
    {
        "Cells": List[str],
        "RecoveryGroupArn": str,
        "RecoveryGroupName": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetCellResponseTypeDef = TypedDict(
    "GetCellResponseTypeDef",
    {
        "CellArn": str,
        "CellName": str,
        "Cells": List[str],
        "ParentReadinessScopes": List[str],
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetReadinessCheckResponseTypeDef = TypedDict(
    "GetReadinessCheckResponseTypeDef",
    {
        "ReadinessCheckArn": str,
        "ReadinessCheckName": str,
        "ResourceSet": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetRecoveryGroupResponseTypeDef = TypedDict(
    "GetRecoveryGroupResponseTypeDef",
    {
        "Cells": List[str],
        "RecoveryGroupArn": str,
        "RecoveryGroupName": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListCellsResponseTypeDef = TypedDict(
    "ListCellsResponseTypeDef",
    {
        "Cells": List[CellOutputTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListCrossAccountAuthorizationsResponseTypeDef = TypedDict(
    "ListCrossAccountAuthorizationsResponseTypeDef",
    {
        "CrossAccountAuthorizations": List[str],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTagsForResourcesResponseTypeDef = TypedDict(
    "ListTagsForResourcesResponseTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateCellResponseTypeDef = TypedDict(
    "UpdateCellResponseTypeDef",
    {
        "CellArn": str,
        "CellName": str,
        "Cells": List[str],
        "ParentReadinessScopes": List[str],
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateReadinessCheckResponseTypeDef = TypedDict(
    "UpdateReadinessCheckResponseTypeDef",
    {
        "ReadinessCheckArn": str,
        "ReadinessCheckName": str,
        "ResourceSet": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateRecoveryGroupResponseTypeDef = TypedDict(
    "UpdateRecoveryGroupResponseTypeDef",
    {
        "Cells": List[str],
        "RecoveryGroupArn": str,
        "RecoveryGroupName": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetArchitectureRecommendationsResponseTypeDef = TypedDict(
    "GetArchitectureRecommendationsResponseTypeDef",
    {
        "LastAuditTimestamp": datetime,
        "NextToken": str,
        "Recommendations": List[RecommendationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetCellReadinessSummaryRequestGetCellReadinessSummaryPaginateTypeDef = TypedDict(
    "GetCellReadinessSummaryRequestGetCellReadinessSummaryPaginateTypeDef",
    {
        "CellName": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetReadinessCheckResourceStatusRequestGetReadinessCheckResourceStatusPaginateTypeDef = TypedDict(
    "GetReadinessCheckResourceStatusRequestGetReadinessCheckResourceStatusPaginateTypeDef",
    {
        "ReadinessCheckName": str,
        "ResourceIdentifier": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetReadinessCheckStatusRequestGetReadinessCheckStatusPaginateTypeDef = TypedDict(
    "GetReadinessCheckStatusRequestGetReadinessCheckStatusPaginateTypeDef",
    {
        "ReadinessCheckName": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetRecoveryGroupReadinessSummaryRequestGetRecoveryGroupReadinessSummaryPaginateTypeDef = TypedDict(
    "GetRecoveryGroupReadinessSummaryRequestGetRecoveryGroupReadinessSummaryPaginateTypeDef",
    {
        "RecoveryGroupName": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListCellsRequestListCellsPaginateTypeDef = TypedDict(
    "ListCellsRequestListCellsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListCrossAccountAuthorizationsRequestListCrossAccountAuthorizationsPaginateTypeDef = TypedDict(
    "ListCrossAccountAuthorizationsRequestListCrossAccountAuthorizationsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListReadinessChecksRequestListReadinessChecksPaginateTypeDef = TypedDict(
    "ListReadinessChecksRequestListReadinessChecksPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListRecoveryGroupsRequestListRecoveryGroupsPaginateTypeDef = TypedDict(
    "ListRecoveryGroupsRequestListRecoveryGroupsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListResourceSetsRequestListResourceSetsPaginateTypeDef = TypedDict(
    "ListResourceSetsRequestListResourceSetsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListRulesRequestListRulesPaginateTypeDef = TypedDict(
    "ListRulesRequestListRulesPaginateTypeDef",
    {
        "ResourceType": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetCellReadinessSummaryResponseTypeDef = TypedDict(
    "GetCellReadinessSummaryResponseTypeDef",
    {
        "NextToken": str,
        "Readiness": ReadinessType,
        "ReadinessChecks": List[ReadinessCheckSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetRecoveryGroupReadinessSummaryResponseTypeDef = TypedDict(
    "GetRecoveryGroupReadinessSummaryResponseTypeDef",
    {
        "NextToken": str,
        "Readiness": ReadinessType,
        "ReadinessChecks": List[ReadinessCheckSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RuleResultTypeDef = TypedDict(
    "RuleResultTypeDef",
    {
        "LastCheckedTimestamp": datetime,
        "Messages": List[MessageTypeDef],
        "Readiness": ReadinessType,
        "RuleId": str,
    },
)
GetReadinessCheckStatusResponseTypeDef = TypedDict(
    "GetReadinessCheckStatusResponseTypeDef",
    {
        "Messages": List[MessageTypeDef],
        "NextToken": str,
        "Readiness": ReadinessType,
        "Resources": List[ResourceResultTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListReadinessChecksResponseTypeDef = TypedDict(
    "ListReadinessChecksResponseTypeDef",
    {
        "NextToken": str,
        "ReadinessChecks": List[ReadinessCheckOutputTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListRecoveryGroupsResponseTypeDef = TypedDict(
    "ListRecoveryGroupsResponseTypeDef",
    {
        "NextToken": str,
        "RecoveryGroups": List[RecoveryGroupOutputTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListRulesResponseTypeDef = TypedDict(
    "ListRulesResponseTypeDef",
    {
        "NextToken": str,
        "Rules": List[ListRulesOutputTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TargetResourceTypeDef = TypedDict(
    "TargetResourceTypeDef",
    {
        "NLBResource": NotRequired[NLBResourceTypeDef],
        "R53Resource": NotRequired[R53ResourceRecordTypeDef],
    },
)
GetReadinessCheckResourceStatusResponseTypeDef = TypedDict(
    "GetReadinessCheckResourceStatusResponseTypeDef",
    {
        "NextToken": str,
        "Readiness": ReadinessType,
        "Rules": List[RuleResultTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DNSTargetResourceTypeDef = TypedDict(
    "DNSTargetResourceTypeDef",
    {
        "DomainName": NotRequired[str],
        "HostedZoneArn": NotRequired[str],
        "RecordSetId": NotRequired[str],
        "RecordType": NotRequired[str],
        "TargetResource": NotRequired[TargetResourceTypeDef],
    },
)
ResourcePaginatorTypeDef = TypedDict(
    "ResourcePaginatorTypeDef",
    {
        "ComponentId": NotRequired[str],
        "DnsTargetResource": NotRequired[DNSTargetResourceTypeDef],
        "ReadinessScopes": NotRequired[List[str]],
        "ResourceArn": NotRequired[str],
    },
)
ResourceTypeDef = TypedDict(
    "ResourceTypeDef",
    {
        "ComponentId": NotRequired[str],
        "DnsTargetResource": NotRequired[DNSTargetResourceTypeDef],
        "ReadinessScopes": NotRequired[Sequence[str]],
        "ResourceArn": NotRequired[str],
    },
)
ResourceSetOutputPaginatorTypeDef = TypedDict(
    "ResourceSetOutputPaginatorTypeDef",
    {
        "ResourceSetArn": str,
        "ResourceSetName": str,
        "ResourceSetType": str,
        "Resources": List[ResourcePaginatorTypeDef],
        "Tags": NotRequired[Dict[str, str]],
    },
)
CreateResourceSetRequestRequestTypeDef = TypedDict(
    "CreateResourceSetRequestRequestTypeDef",
    {
        "ResourceSetName": str,
        "ResourceSetType": str,
        "Resources": Sequence[ResourceTypeDef],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
CreateResourceSetResponseTypeDef = TypedDict(
    "CreateResourceSetResponseTypeDef",
    {
        "ResourceSetArn": str,
        "ResourceSetName": str,
        "ResourceSetType": str,
        "Resources": List[ResourceTypeDef],
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetResourceSetResponseTypeDef = TypedDict(
    "GetResourceSetResponseTypeDef",
    {
        "ResourceSetArn": str,
        "ResourceSetName": str,
        "ResourceSetType": str,
        "Resources": List[ResourceTypeDef],
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ResourceSetOutputTypeDef = TypedDict(
    "ResourceSetOutputTypeDef",
    {
        "ResourceSetArn": str,
        "ResourceSetName": str,
        "ResourceSetType": str,
        "Resources": List[ResourceTypeDef],
        "Tags": NotRequired[Dict[str, str]],
    },
)
UpdateResourceSetRequestRequestTypeDef = TypedDict(
    "UpdateResourceSetRequestRequestTypeDef",
    {
        "ResourceSetName": str,
        "ResourceSetType": str,
        "Resources": Sequence[ResourceTypeDef],
    },
)
UpdateResourceSetResponseTypeDef = TypedDict(
    "UpdateResourceSetResponseTypeDef",
    {
        "ResourceSetArn": str,
        "ResourceSetName": str,
        "ResourceSetType": str,
        "Resources": List[ResourceTypeDef],
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListResourceSetsResponsePaginatorTypeDef = TypedDict(
    "ListResourceSetsResponsePaginatorTypeDef",
    {
        "NextToken": str,
        "ResourceSets": List[ResourceSetOutputPaginatorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListResourceSetsResponseTypeDef = TypedDict(
    "ListResourceSetsResponseTypeDef",
    {
        "NextToken": str,
        "ResourceSets": List[ResourceSetOutputTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
