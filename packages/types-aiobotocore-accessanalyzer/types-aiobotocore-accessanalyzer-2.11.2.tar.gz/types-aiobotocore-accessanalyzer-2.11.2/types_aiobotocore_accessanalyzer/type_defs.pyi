"""
Type annotations for accessanalyzer service type definitions.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_accessanalyzer/type_defs/)

Usage::

    ```python
    from types_aiobotocore_accessanalyzer.type_defs import AccessPreviewStatusReasonTypeDef

    data: AccessPreviewStatusReasonTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List, Mapping, Sequence, Union

from .literals import (
    AccessCheckPolicyTypeType,
    AccessPreviewStatusReasonCodeType,
    AccessPreviewStatusType,
    AclPermissionType,
    AnalyzerStatusType,
    CheckAccessNotGrantedResultType,
    CheckNoNewAccessResultType,
    FindingChangeTypeType,
    FindingSourceTypeType,
    FindingStatusType,
    FindingStatusUpdateType,
    FindingTypeType,
    JobErrorCodeType,
    JobStatusType,
    KmsGrantOperationType,
    LocaleType,
    OrderByType,
    PolicyTypeType,
    ReasonCodeType,
    ResourceTypeType,
    TypeType,
    ValidatePolicyFindingTypeType,
    ValidatePolicyResourceTypeType,
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
    "AccessPreviewStatusReasonTypeDef",
    "AccessTypeDef",
    "AclGranteeTypeDef",
    "AnalyzedResourceSummaryTypeDef",
    "AnalyzedResourceTypeDef",
    "UnusedAccessConfigurationTypeDef",
    "StatusReasonTypeDef",
    "ApplyArchiveRuleRequestRequestTypeDef",
    "CriterionTypeDef",
    "CancelPolicyGenerationRequestRequestTypeDef",
    "ReasonSummaryTypeDef",
    "ResponseMetadataTypeDef",
    "CheckNoNewAccessRequestRequestTypeDef",
    "TimestampTypeDef",
    "TrailTypeDef",
    "TrailPropertiesTypeDef",
    "EbsSnapshotConfigurationTypeDef",
    "EcrRepositoryConfigurationTypeDef",
    "EfsFileSystemConfigurationTypeDef",
    "IamRoleConfigurationTypeDef",
    "S3ExpressDirectoryBucketConfigurationTypeDef",
    "SecretsManagerSecretConfigurationTypeDef",
    "SnsTopicConfigurationTypeDef",
    "SqsQueueConfigurationTypeDef",
    "DeleteAnalyzerRequestRequestTypeDef",
    "DeleteArchiveRuleRequestRequestTypeDef",
    "UnusedIamRoleDetailsTypeDef",
    "UnusedIamUserAccessKeyDetailsTypeDef",
    "UnusedIamUserPasswordDetailsTypeDef",
    "FindingSourceDetailTypeDef",
    "FindingSummaryV2TypeDef",
    "GeneratedPolicyTypeDef",
    "GetAccessPreviewRequestRequestTypeDef",
    "GetAnalyzedResourceRequestRequestTypeDef",
    "GetAnalyzerRequestRequestTypeDef",
    "GetArchiveRuleRequestRequestTypeDef",
    "GetFindingRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "GetFindingV2RequestRequestTypeDef",
    "GetGeneratedPolicyRequestRequestTypeDef",
    "JobErrorTypeDef",
    "KmsGrantConstraintsTypeDef",
    "ListAccessPreviewsRequestRequestTypeDef",
    "ListAnalyzedResourcesRequestRequestTypeDef",
    "ListAnalyzersRequestRequestTypeDef",
    "ListArchiveRulesRequestRequestTypeDef",
    "SortCriteriaTypeDef",
    "ListPolicyGenerationsRequestRequestTypeDef",
    "PolicyGenerationTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "VpcConfigurationTypeDef",
    "SubstringTypeDef",
    "PolicyGenerationDetailsTypeDef",
    "PositionTypeDef",
    "RdsDbClusterSnapshotAttributeValueTypeDef",
    "RdsDbSnapshotAttributeValueTypeDef",
    "S3PublicAccessBlockConfigurationTypeDef",
    "StartResourceScanRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UnusedActionTypeDef",
    "UpdateFindingsRequestRequestTypeDef",
    "ValidatePolicyRequestRequestTypeDef",
    "AccessPreviewSummaryTypeDef",
    "CheckAccessNotGrantedRequestRequestTypeDef",
    "S3BucketAclGrantConfigurationTypeDef",
    "AnalyzerConfigurationTypeDef",
    "ArchiveRuleSummaryTypeDef",
    "CreateArchiveRuleRequestRequestTypeDef",
    "InlineArchiveRuleTypeDef",
    "ListAccessPreviewFindingsRequestRequestTypeDef",
    "UpdateArchiveRuleRequestRequestTypeDef",
    "CheckAccessNotGrantedResponseTypeDef",
    "CheckNoNewAccessResponseTypeDef",
    "CreateAccessPreviewResponseTypeDef",
    "CreateAnalyzerResponseTypeDef",
    "EmptyResponseMetadataTypeDef",
    "GetAnalyzedResourceResponseTypeDef",
    "ListAnalyzedResourcesResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "StartPolicyGenerationResponseTypeDef",
    "CloudTrailDetailsTypeDef",
    "CloudTrailPropertiesTypeDef",
    "FindingSourceTypeDef",
    "ListFindingsV2ResponseTypeDef",
    "GetFindingV2RequestGetFindingV2PaginateTypeDef",
    "ListAccessPreviewFindingsRequestListAccessPreviewFindingsPaginateTypeDef",
    "ListAccessPreviewsRequestListAccessPreviewsPaginateTypeDef",
    "ListAnalyzedResourcesRequestListAnalyzedResourcesPaginateTypeDef",
    "ListAnalyzersRequestListAnalyzersPaginateTypeDef",
    "ListArchiveRulesRequestListArchiveRulesPaginateTypeDef",
    "ListPolicyGenerationsRequestListPolicyGenerationsPaginateTypeDef",
    "ValidatePolicyRequestValidatePolicyPaginateTypeDef",
    "JobDetailsTypeDef",
    "KmsGrantConfigurationTypeDef",
    "ListFindingsRequestListFindingsPaginateTypeDef",
    "ListFindingsRequestRequestTypeDef",
    "ListFindingsV2RequestListFindingsV2PaginateTypeDef",
    "ListFindingsV2RequestRequestTypeDef",
    "ListPolicyGenerationsResponseTypeDef",
    "NetworkOriginConfigurationTypeDef",
    "PathElementTypeDef",
    "SpanTypeDef",
    "RdsDbClusterSnapshotConfigurationTypeDef",
    "RdsDbSnapshotConfigurationTypeDef",
    "UnusedPermissionDetailsTypeDef",
    "ListAccessPreviewsResponseTypeDef",
    "AnalyzerSummaryTypeDef",
    "GetArchiveRuleResponseTypeDef",
    "ListArchiveRulesResponseTypeDef",
    "CreateAnalyzerRequestRequestTypeDef",
    "StartPolicyGenerationRequestRequestTypeDef",
    "GeneratedPolicyPropertiesTypeDef",
    "AccessPreviewFindingTypeDef",
    "ExternalAccessDetailsTypeDef",
    "FindingSummaryTypeDef",
    "FindingTypeDef",
    "KmsKeyConfigurationTypeDef",
    "S3AccessPointConfigurationTypeDef",
    "LocationTypeDef",
    "GetAnalyzerResponseTypeDef",
    "ListAnalyzersResponseTypeDef",
    "GeneratedPolicyResultTypeDef",
    "ListAccessPreviewFindingsResponseTypeDef",
    "FindingDetailsTypeDef",
    "ListFindingsResponseTypeDef",
    "GetFindingResponseTypeDef",
    "S3BucketConfigurationTypeDef",
    "ValidatePolicyFindingTypeDef",
    "GetGeneratedPolicyResponseTypeDef",
    "GetFindingV2ResponseTypeDef",
    "ConfigurationTypeDef",
    "ValidatePolicyResponseTypeDef",
    "AccessPreviewTypeDef",
    "CreateAccessPreviewRequestRequestTypeDef",
    "GetAccessPreviewResponseTypeDef",
)

AccessPreviewStatusReasonTypeDef = TypedDict(
    "AccessPreviewStatusReasonTypeDef",
    {
        "code": AccessPreviewStatusReasonCodeType,
    },
)
AccessTypeDef = TypedDict(
    "AccessTypeDef",
    {
        "actions": Sequence[str],
    },
)
AclGranteeTypeDef = TypedDict(
    "AclGranteeTypeDef",
    {
        "id": NotRequired[str],
        "uri": NotRequired[str],
    },
)
AnalyzedResourceSummaryTypeDef = TypedDict(
    "AnalyzedResourceSummaryTypeDef",
    {
        "resourceArn": str,
        "resourceOwnerAccount": str,
        "resourceType": ResourceTypeType,
    },
)
AnalyzedResourceTypeDef = TypedDict(
    "AnalyzedResourceTypeDef",
    {
        "resourceArn": str,
        "resourceType": ResourceTypeType,
        "createdAt": datetime,
        "analyzedAt": datetime,
        "updatedAt": datetime,
        "isPublic": bool,
        "resourceOwnerAccount": str,
        "actions": NotRequired[List[str]],
        "sharedVia": NotRequired[List[str]],
        "status": NotRequired[FindingStatusType],
        "error": NotRequired[str],
    },
)
UnusedAccessConfigurationTypeDef = TypedDict(
    "UnusedAccessConfigurationTypeDef",
    {
        "unusedAccessAge": NotRequired[int],
    },
)
StatusReasonTypeDef = TypedDict(
    "StatusReasonTypeDef",
    {
        "code": ReasonCodeType,
    },
)
ApplyArchiveRuleRequestRequestTypeDef = TypedDict(
    "ApplyArchiveRuleRequestRequestTypeDef",
    {
        "analyzerArn": str,
        "ruleName": str,
        "clientToken": NotRequired[str],
    },
)
CriterionTypeDef = TypedDict(
    "CriterionTypeDef",
    {
        "eq": NotRequired[Sequence[str]],
        "neq": NotRequired[Sequence[str]],
        "contains": NotRequired[Sequence[str]],
        "exists": NotRequired[bool],
    },
)
CancelPolicyGenerationRequestRequestTypeDef = TypedDict(
    "CancelPolicyGenerationRequestRequestTypeDef",
    {
        "jobId": str,
    },
)
ReasonSummaryTypeDef = TypedDict(
    "ReasonSummaryTypeDef",
    {
        "description": NotRequired[str],
        "statementIndex": NotRequired[int],
        "statementId": NotRequired[str],
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
CheckNoNewAccessRequestRequestTypeDef = TypedDict(
    "CheckNoNewAccessRequestRequestTypeDef",
    {
        "newPolicyDocument": str,
        "existingPolicyDocument": str,
        "policyType": AccessCheckPolicyTypeType,
    },
)
TimestampTypeDef = Union[datetime, str]
TrailTypeDef = TypedDict(
    "TrailTypeDef",
    {
        "cloudTrailArn": str,
        "regions": NotRequired[Sequence[str]],
        "allRegions": NotRequired[bool],
    },
)
TrailPropertiesTypeDef = TypedDict(
    "TrailPropertiesTypeDef",
    {
        "cloudTrailArn": str,
        "regions": NotRequired[List[str]],
        "allRegions": NotRequired[bool],
    },
)
EbsSnapshotConfigurationTypeDef = TypedDict(
    "EbsSnapshotConfigurationTypeDef",
    {
        "userIds": NotRequired[Sequence[str]],
        "groups": NotRequired[Sequence[str]],
        "kmsKeyId": NotRequired[str],
    },
)
EcrRepositoryConfigurationTypeDef = TypedDict(
    "EcrRepositoryConfigurationTypeDef",
    {
        "repositoryPolicy": NotRequired[str],
    },
)
EfsFileSystemConfigurationTypeDef = TypedDict(
    "EfsFileSystemConfigurationTypeDef",
    {
        "fileSystemPolicy": NotRequired[str],
    },
)
IamRoleConfigurationTypeDef = TypedDict(
    "IamRoleConfigurationTypeDef",
    {
        "trustPolicy": NotRequired[str],
    },
)
S3ExpressDirectoryBucketConfigurationTypeDef = TypedDict(
    "S3ExpressDirectoryBucketConfigurationTypeDef",
    {
        "bucketPolicy": NotRequired[str],
    },
)
SecretsManagerSecretConfigurationTypeDef = TypedDict(
    "SecretsManagerSecretConfigurationTypeDef",
    {
        "kmsKeyId": NotRequired[str],
        "secretPolicy": NotRequired[str],
    },
)
SnsTopicConfigurationTypeDef = TypedDict(
    "SnsTopicConfigurationTypeDef",
    {
        "topicPolicy": NotRequired[str],
    },
)
SqsQueueConfigurationTypeDef = TypedDict(
    "SqsQueueConfigurationTypeDef",
    {
        "queuePolicy": NotRequired[str],
    },
)
DeleteAnalyzerRequestRequestTypeDef = TypedDict(
    "DeleteAnalyzerRequestRequestTypeDef",
    {
        "analyzerName": str,
        "clientToken": NotRequired[str],
    },
)
DeleteArchiveRuleRequestRequestTypeDef = TypedDict(
    "DeleteArchiveRuleRequestRequestTypeDef",
    {
        "analyzerName": str,
        "ruleName": str,
        "clientToken": NotRequired[str],
    },
)
UnusedIamRoleDetailsTypeDef = TypedDict(
    "UnusedIamRoleDetailsTypeDef",
    {
        "lastAccessed": NotRequired[datetime],
    },
)
UnusedIamUserAccessKeyDetailsTypeDef = TypedDict(
    "UnusedIamUserAccessKeyDetailsTypeDef",
    {
        "accessKeyId": str,
        "lastAccessed": NotRequired[datetime],
    },
)
UnusedIamUserPasswordDetailsTypeDef = TypedDict(
    "UnusedIamUserPasswordDetailsTypeDef",
    {
        "lastAccessed": NotRequired[datetime],
    },
)
FindingSourceDetailTypeDef = TypedDict(
    "FindingSourceDetailTypeDef",
    {
        "accessPointArn": NotRequired[str],
        "accessPointAccount": NotRequired[str],
    },
)
FindingSummaryV2TypeDef = TypedDict(
    "FindingSummaryV2TypeDef",
    {
        "analyzedAt": datetime,
        "createdAt": datetime,
        "id": str,
        "resourceType": ResourceTypeType,
        "resourceOwnerAccount": str,
        "status": FindingStatusType,
        "updatedAt": datetime,
        "error": NotRequired[str],
        "resource": NotRequired[str],
        "findingType": NotRequired[FindingTypeType],
    },
)
GeneratedPolicyTypeDef = TypedDict(
    "GeneratedPolicyTypeDef",
    {
        "policy": str,
    },
)
GetAccessPreviewRequestRequestTypeDef = TypedDict(
    "GetAccessPreviewRequestRequestTypeDef",
    {
        "accessPreviewId": str,
        "analyzerArn": str,
    },
)
GetAnalyzedResourceRequestRequestTypeDef = TypedDict(
    "GetAnalyzedResourceRequestRequestTypeDef",
    {
        "analyzerArn": str,
        "resourceArn": str,
    },
)
GetAnalyzerRequestRequestTypeDef = TypedDict(
    "GetAnalyzerRequestRequestTypeDef",
    {
        "analyzerName": str,
    },
)
GetArchiveRuleRequestRequestTypeDef = TypedDict(
    "GetArchiveRuleRequestRequestTypeDef",
    {
        "analyzerName": str,
        "ruleName": str,
    },
)
GetFindingRequestRequestTypeDef = TypedDict(
    "GetFindingRequestRequestTypeDef",
    {
        "analyzerArn": str,
        "id": str,
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
GetFindingV2RequestRequestTypeDef = TypedDict(
    "GetFindingV2RequestRequestTypeDef",
    {
        "analyzerArn": str,
        "id": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
GetGeneratedPolicyRequestRequestTypeDef = TypedDict(
    "GetGeneratedPolicyRequestRequestTypeDef",
    {
        "jobId": str,
        "includeResourcePlaceholders": NotRequired[bool],
        "includeServiceLevelTemplate": NotRequired[bool],
    },
)
JobErrorTypeDef = TypedDict(
    "JobErrorTypeDef",
    {
        "code": JobErrorCodeType,
        "message": str,
    },
)
KmsGrantConstraintsTypeDef = TypedDict(
    "KmsGrantConstraintsTypeDef",
    {
        "encryptionContextEquals": NotRequired[Mapping[str, str]],
        "encryptionContextSubset": NotRequired[Mapping[str, str]],
    },
)
ListAccessPreviewsRequestRequestTypeDef = TypedDict(
    "ListAccessPreviewsRequestRequestTypeDef",
    {
        "analyzerArn": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListAnalyzedResourcesRequestRequestTypeDef = TypedDict(
    "ListAnalyzedResourcesRequestRequestTypeDef",
    {
        "analyzerArn": str,
        "resourceType": NotRequired[ResourceTypeType],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListAnalyzersRequestRequestTypeDef = TypedDict(
    "ListAnalyzersRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "type": NotRequired[TypeType],
    },
)
ListArchiveRulesRequestRequestTypeDef = TypedDict(
    "ListArchiveRulesRequestRequestTypeDef",
    {
        "analyzerName": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
SortCriteriaTypeDef = TypedDict(
    "SortCriteriaTypeDef",
    {
        "attributeName": NotRequired[str],
        "orderBy": NotRequired[OrderByType],
    },
)
ListPolicyGenerationsRequestRequestTypeDef = TypedDict(
    "ListPolicyGenerationsRequestRequestTypeDef",
    {
        "principalArn": NotRequired[str],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
PolicyGenerationTypeDef = TypedDict(
    "PolicyGenerationTypeDef",
    {
        "jobId": str,
        "principalArn": str,
        "status": JobStatusType,
        "startedOn": datetime,
        "completedOn": NotRequired[datetime],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)
VpcConfigurationTypeDef = TypedDict(
    "VpcConfigurationTypeDef",
    {
        "vpcId": str,
    },
)
SubstringTypeDef = TypedDict(
    "SubstringTypeDef",
    {
        "start": int,
        "length": int,
    },
)
PolicyGenerationDetailsTypeDef = TypedDict(
    "PolicyGenerationDetailsTypeDef",
    {
        "principalArn": str,
    },
)
PositionTypeDef = TypedDict(
    "PositionTypeDef",
    {
        "line": int,
        "column": int,
        "offset": int,
    },
)
RdsDbClusterSnapshotAttributeValueTypeDef = TypedDict(
    "RdsDbClusterSnapshotAttributeValueTypeDef",
    {
        "accountIds": NotRequired[Sequence[str]],
    },
)
RdsDbSnapshotAttributeValueTypeDef = TypedDict(
    "RdsDbSnapshotAttributeValueTypeDef",
    {
        "accountIds": NotRequired[Sequence[str]],
    },
)
S3PublicAccessBlockConfigurationTypeDef = TypedDict(
    "S3PublicAccessBlockConfigurationTypeDef",
    {
        "ignorePublicAcls": bool,
        "restrictPublicBuckets": bool,
    },
)
StartResourceScanRequestRequestTypeDef = TypedDict(
    "StartResourceScanRequestRequestTypeDef",
    {
        "analyzerArn": str,
        "resourceArn": str,
        "resourceOwnerAccount": NotRequired[str],
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Mapping[str, str],
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)
UnusedActionTypeDef = TypedDict(
    "UnusedActionTypeDef",
    {
        "action": str,
        "lastAccessed": NotRequired[datetime],
    },
)
UpdateFindingsRequestRequestTypeDef = TypedDict(
    "UpdateFindingsRequestRequestTypeDef",
    {
        "analyzerArn": str,
        "status": FindingStatusUpdateType,
        "ids": NotRequired[Sequence[str]],
        "resourceArn": NotRequired[str],
        "clientToken": NotRequired[str],
    },
)
ValidatePolicyRequestRequestTypeDef = TypedDict(
    "ValidatePolicyRequestRequestTypeDef",
    {
        "policyDocument": str,
        "policyType": PolicyTypeType,
        "locale": NotRequired[LocaleType],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "validatePolicyResourceType": NotRequired[ValidatePolicyResourceTypeType],
    },
)
AccessPreviewSummaryTypeDef = TypedDict(
    "AccessPreviewSummaryTypeDef",
    {
        "id": str,
        "analyzerArn": str,
        "createdAt": datetime,
        "status": AccessPreviewStatusType,
        "statusReason": NotRequired[AccessPreviewStatusReasonTypeDef],
    },
)
CheckAccessNotGrantedRequestRequestTypeDef = TypedDict(
    "CheckAccessNotGrantedRequestRequestTypeDef",
    {
        "policyDocument": str,
        "access": Sequence[AccessTypeDef],
        "policyType": AccessCheckPolicyTypeType,
    },
)
S3BucketAclGrantConfigurationTypeDef = TypedDict(
    "S3BucketAclGrantConfigurationTypeDef",
    {
        "permission": AclPermissionType,
        "grantee": AclGranteeTypeDef,
    },
)
AnalyzerConfigurationTypeDef = TypedDict(
    "AnalyzerConfigurationTypeDef",
    {
        "unusedAccess": NotRequired[UnusedAccessConfigurationTypeDef],
    },
)
ArchiveRuleSummaryTypeDef = TypedDict(
    "ArchiveRuleSummaryTypeDef",
    {
        "ruleName": str,
        "filter": Dict[str, CriterionTypeDef],
        "createdAt": datetime,
        "updatedAt": datetime,
    },
)
CreateArchiveRuleRequestRequestTypeDef = TypedDict(
    "CreateArchiveRuleRequestRequestTypeDef",
    {
        "analyzerName": str,
        "ruleName": str,
        "filter": Mapping[str, CriterionTypeDef],
        "clientToken": NotRequired[str],
    },
)
InlineArchiveRuleTypeDef = TypedDict(
    "InlineArchiveRuleTypeDef",
    {
        "ruleName": str,
        "filter": Mapping[str, CriterionTypeDef],
    },
)
ListAccessPreviewFindingsRequestRequestTypeDef = TypedDict(
    "ListAccessPreviewFindingsRequestRequestTypeDef",
    {
        "accessPreviewId": str,
        "analyzerArn": str,
        "filter": NotRequired[Mapping[str, CriterionTypeDef]],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
UpdateArchiveRuleRequestRequestTypeDef = TypedDict(
    "UpdateArchiveRuleRequestRequestTypeDef",
    {
        "analyzerName": str,
        "ruleName": str,
        "filter": Mapping[str, CriterionTypeDef],
        "clientToken": NotRequired[str],
    },
)
CheckAccessNotGrantedResponseTypeDef = TypedDict(
    "CheckAccessNotGrantedResponseTypeDef",
    {
        "result": CheckAccessNotGrantedResultType,
        "message": str,
        "reasons": List[ReasonSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CheckNoNewAccessResponseTypeDef = TypedDict(
    "CheckNoNewAccessResponseTypeDef",
    {
        "result": CheckNoNewAccessResultType,
        "message": str,
        "reasons": List[ReasonSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateAccessPreviewResponseTypeDef = TypedDict(
    "CreateAccessPreviewResponseTypeDef",
    {
        "id": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateAnalyzerResponseTypeDef = TypedDict(
    "CreateAnalyzerResponseTypeDef",
    {
        "arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAnalyzedResourceResponseTypeDef = TypedDict(
    "GetAnalyzedResourceResponseTypeDef",
    {
        "resource": AnalyzedResourceTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAnalyzedResourcesResponseTypeDef = TypedDict(
    "ListAnalyzedResourcesResponseTypeDef",
    {
        "analyzedResources": List[AnalyzedResourceSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartPolicyGenerationResponseTypeDef = TypedDict(
    "StartPolicyGenerationResponseTypeDef",
    {
        "jobId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CloudTrailDetailsTypeDef = TypedDict(
    "CloudTrailDetailsTypeDef",
    {
        "trails": Sequence[TrailTypeDef],
        "accessRole": str,
        "startTime": TimestampTypeDef,
        "endTime": NotRequired[TimestampTypeDef],
    },
)
CloudTrailPropertiesTypeDef = TypedDict(
    "CloudTrailPropertiesTypeDef",
    {
        "trailProperties": List[TrailPropertiesTypeDef],
        "startTime": datetime,
        "endTime": datetime,
    },
)
FindingSourceTypeDef = TypedDict(
    "FindingSourceTypeDef",
    {
        "type": FindingSourceTypeType,
        "detail": NotRequired[FindingSourceDetailTypeDef],
    },
)
ListFindingsV2ResponseTypeDef = TypedDict(
    "ListFindingsV2ResponseTypeDef",
    {
        "findings": List[FindingSummaryV2TypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetFindingV2RequestGetFindingV2PaginateTypeDef = TypedDict(
    "GetFindingV2RequestGetFindingV2PaginateTypeDef",
    {
        "analyzerArn": str,
        "id": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListAccessPreviewFindingsRequestListAccessPreviewFindingsPaginateTypeDef = TypedDict(
    "ListAccessPreviewFindingsRequestListAccessPreviewFindingsPaginateTypeDef",
    {
        "accessPreviewId": str,
        "analyzerArn": str,
        "filter": NotRequired[Mapping[str, CriterionTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListAccessPreviewsRequestListAccessPreviewsPaginateTypeDef = TypedDict(
    "ListAccessPreviewsRequestListAccessPreviewsPaginateTypeDef",
    {
        "analyzerArn": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListAnalyzedResourcesRequestListAnalyzedResourcesPaginateTypeDef = TypedDict(
    "ListAnalyzedResourcesRequestListAnalyzedResourcesPaginateTypeDef",
    {
        "analyzerArn": str,
        "resourceType": NotRequired[ResourceTypeType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListAnalyzersRequestListAnalyzersPaginateTypeDef = TypedDict(
    "ListAnalyzersRequestListAnalyzersPaginateTypeDef",
    {
        "type": NotRequired[TypeType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListArchiveRulesRequestListArchiveRulesPaginateTypeDef = TypedDict(
    "ListArchiveRulesRequestListArchiveRulesPaginateTypeDef",
    {
        "analyzerName": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListPolicyGenerationsRequestListPolicyGenerationsPaginateTypeDef = TypedDict(
    "ListPolicyGenerationsRequestListPolicyGenerationsPaginateTypeDef",
    {
        "principalArn": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ValidatePolicyRequestValidatePolicyPaginateTypeDef = TypedDict(
    "ValidatePolicyRequestValidatePolicyPaginateTypeDef",
    {
        "policyDocument": str,
        "policyType": PolicyTypeType,
        "locale": NotRequired[LocaleType],
        "validatePolicyResourceType": NotRequired[ValidatePolicyResourceTypeType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
JobDetailsTypeDef = TypedDict(
    "JobDetailsTypeDef",
    {
        "jobId": str,
        "status": JobStatusType,
        "startedOn": datetime,
        "completedOn": NotRequired[datetime],
        "jobError": NotRequired[JobErrorTypeDef],
    },
)
KmsGrantConfigurationTypeDef = TypedDict(
    "KmsGrantConfigurationTypeDef",
    {
        "operations": Sequence[KmsGrantOperationType],
        "granteePrincipal": str,
        "issuingAccount": str,
        "retiringPrincipal": NotRequired[str],
        "constraints": NotRequired[KmsGrantConstraintsTypeDef],
    },
)
ListFindingsRequestListFindingsPaginateTypeDef = TypedDict(
    "ListFindingsRequestListFindingsPaginateTypeDef",
    {
        "analyzerArn": str,
        "filter": NotRequired[Mapping[str, CriterionTypeDef]],
        "sort": NotRequired[SortCriteriaTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListFindingsRequestRequestTypeDef = TypedDict(
    "ListFindingsRequestRequestTypeDef",
    {
        "analyzerArn": str,
        "filter": NotRequired[Mapping[str, CriterionTypeDef]],
        "sort": NotRequired[SortCriteriaTypeDef],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListFindingsV2RequestListFindingsV2PaginateTypeDef = TypedDict(
    "ListFindingsV2RequestListFindingsV2PaginateTypeDef",
    {
        "analyzerArn": str,
        "filter": NotRequired[Mapping[str, CriterionTypeDef]],
        "sort": NotRequired[SortCriteriaTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListFindingsV2RequestRequestTypeDef = TypedDict(
    "ListFindingsV2RequestRequestTypeDef",
    {
        "analyzerArn": str,
        "filter": NotRequired[Mapping[str, CriterionTypeDef]],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "sort": NotRequired[SortCriteriaTypeDef],
    },
)
ListPolicyGenerationsResponseTypeDef = TypedDict(
    "ListPolicyGenerationsResponseTypeDef",
    {
        "policyGenerations": List[PolicyGenerationTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
NetworkOriginConfigurationTypeDef = TypedDict(
    "NetworkOriginConfigurationTypeDef",
    {
        "vpcConfiguration": NotRequired[VpcConfigurationTypeDef],
        "internetConfiguration": NotRequired[Mapping[str, Any]],
    },
)
PathElementTypeDef = TypedDict(
    "PathElementTypeDef",
    {
        "index": NotRequired[int],
        "key": NotRequired[str],
        "substring": NotRequired[SubstringTypeDef],
        "value": NotRequired[str],
    },
)
SpanTypeDef = TypedDict(
    "SpanTypeDef",
    {
        "start": PositionTypeDef,
        "end": PositionTypeDef,
    },
)
RdsDbClusterSnapshotConfigurationTypeDef = TypedDict(
    "RdsDbClusterSnapshotConfigurationTypeDef",
    {
        "attributes": NotRequired[Mapping[str, RdsDbClusterSnapshotAttributeValueTypeDef]],
        "kmsKeyId": NotRequired[str],
    },
)
RdsDbSnapshotConfigurationTypeDef = TypedDict(
    "RdsDbSnapshotConfigurationTypeDef",
    {
        "attributes": NotRequired[Mapping[str, RdsDbSnapshotAttributeValueTypeDef]],
        "kmsKeyId": NotRequired[str],
    },
)
UnusedPermissionDetailsTypeDef = TypedDict(
    "UnusedPermissionDetailsTypeDef",
    {
        "serviceNamespace": str,
        "actions": NotRequired[List[UnusedActionTypeDef]],
        "lastAccessed": NotRequired[datetime],
    },
)
ListAccessPreviewsResponseTypeDef = TypedDict(
    "ListAccessPreviewsResponseTypeDef",
    {
        "accessPreviews": List[AccessPreviewSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AnalyzerSummaryTypeDef = TypedDict(
    "AnalyzerSummaryTypeDef",
    {
        "arn": str,
        "name": str,
        "type": TypeType,
        "createdAt": datetime,
        "status": AnalyzerStatusType,
        "lastResourceAnalyzed": NotRequired[str],
        "lastResourceAnalyzedAt": NotRequired[datetime],
        "tags": NotRequired[Dict[str, str]],
        "statusReason": NotRequired[StatusReasonTypeDef],
        "configuration": NotRequired[AnalyzerConfigurationTypeDef],
    },
)
GetArchiveRuleResponseTypeDef = TypedDict(
    "GetArchiveRuleResponseTypeDef",
    {
        "archiveRule": ArchiveRuleSummaryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListArchiveRulesResponseTypeDef = TypedDict(
    "ListArchiveRulesResponseTypeDef",
    {
        "archiveRules": List[ArchiveRuleSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateAnalyzerRequestRequestTypeDef = TypedDict(
    "CreateAnalyzerRequestRequestTypeDef",
    {
        "analyzerName": str,
        "type": TypeType,
        "archiveRules": NotRequired[Sequence[InlineArchiveRuleTypeDef]],
        "tags": NotRequired[Mapping[str, str]],
        "clientToken": NotRequired[str],
        "configuration": NotRequired[AnalyzerConfigurationTypeDef],
    },
)
StartPolicyGenerationRequestRequestTypeDef = TypedDict(
    "StartPolicyGenerationRequestRequestTypeDef",
    {
        "policyGenerationDetails": PolicyGenerationDetailsTypeDef,
        "cloudTrailDetails": NotRequired[CloudTrailDetailsTypeDef],
        "clientToken": NotRequired[str],
    },
)
GeneratedPolicyPropertiesTypeDef = TypedDict(
    "GeneratedPolicyPropertiesTypeDef",
    {
        "principalArn": str,
        "isComplete": NotRequired[bool],
        "cloudTrailProperties": NotRequired[CloudTrailPropertiesTypeDef],
    },
)
AccessPreviewFindingTypeDef = TypedDict(
    "AccessPreviewFindingTypeDef",
    {
        "id": str,
        "resourceType": ResourceTypeType,
        "createdAt": datetime,
        "changeType": FindingChangeTypeType,
        "status": FindingStatusType,
        "resourceOwnerAccount": str,
        "existingFindingId": NotRequired[str],
        "existingFindingStatus": NotRequired[FindingStatusType],
        "principal": NotRequired[Dict[str, str]],
        "action": NotRequired[List[str]],
        "condition": NotRequired[Dict[str, str]],
        "resource": NotRequired[str],
        "isPublic": NotRequired[bool],
        "error": NotRequired[str],
        "sources": NotRequired[List[FindingSourceTypeDef]],
    },
)
ExternalAccessDetailsTypeDef = TypedDict(
    "ExternalAccessDetailsTypeDef",
    {
        "condition": Dict[str, str],
        "action": NotRequired[List[str]],
        "isPublic": NotRequired[bool],
        "principal": NotRequired[Dict[str, str]],
        "sources": NotRequired[List[FindingSourceTypeDef]],
    },
)
FindingSummaryTypeDef = TypedDict(
    "FindingSummaryTypeDef",
    {
        "id": str,
        "resourceType": ResourceTypeType,
        "condition": Dict[str, str],
        "createdAt": datetime,
        "analyzedAt": datetime,
        "updatedAt": datetime,
        "status": FindingStatusType,
        "resourceOwnerAccount": str,
        "principal": NotRequired[Dict[str, str]],
        "action": NotRequired[List[str]],
        "resource": NotRequired[str],
        "isPublic": NotRequired[bool],
        "error": NotRequired[str],
        "sources": NotRequired[List[FindingSourceTypeDef]],
    },
)
FindingTypeDef = TypedDict(
    "FindingTypeDef",
    {
        "id": str,
        "resourceType": ResourceTypeType,
        "condition": Dict[str, str],
        "createdAt": datetime,
        "analyzedAt": datetime,
        "updatedAt": datetime,
        "status": FindingStatusType,
        "resourceOwnerAccount": str,
        "principal": NotRequired[Dict[str, str]],
        "action": NotRequired[List[str]],
        "resource": NotRequired[str],
        "isPublic": NotRequired[bool],
        "error": NotRequired[str],
        "sources": NotRequired[List[FindingSourceTypeDef]],
    },
)
KmsKeyConfigurationTypeDef = TypedDict(
    "KmsKeyConfigurationTypeDef",
    {
        "keyPolicies": NotRequired[Mapping[str, str]],
        "grants": NotRequired[Sequence[KmsGrantConfigurationTypeDef]],
    },
)
S3AccessPointConfigurationTypeDef = TypedDict(
    "S3AccessPointConfigurationTypeDef",
    {
        "accessPointPolicy": NotRequired[str],
        "publicAccessBlock": NotRequired[S3PublicAccessBlockConfigurationTypeDef],
        "networkOrigin": NotRequired[NetworkOriginConfigurationTypeDef],
    },
)
LocationTypeDef = TypedDict(
    "LocationTypeDef",
    {
        "path": List[PathElementTypeDef],
        "span": SpanTypeDef,
    },
)
GetAnalyzerResponseTypeDef = TypedDict(
    "GetAnalyzerResponseTypeDef",
    {
        "analyzer": AnalyzerSummaryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAnalyzersResponseTypeDef = TypedDict(
    "ListAnalyzersResponseTypeDef",
    {
        "analyzers": List[AnalyzerSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GeneratedPolicyResultTypeDef = TypedDict(
    "GeneratedPolicyResultTypeDef",
    {
        "properties": GeneratedPolicyPropertiesTypeDef,
        "generatedPolicies": NotRequired[List[GeneratedPolicyTypeDef]],
    },
)
ListAccessPreviewFindingsResponseTypeDef = TypedDict(
    "ListAccessPreviewFindingsResponseTypeDef",
    {
        "findings": List[AccessPreviewFindingTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
FindingDetailsTypeDef = TypedDict(
    "FindingDetailsTypeDef",
    {
        "externalAccessDetails": NotRequired[ExternalAccessDetailsTypeDef],
        "unusedPermissionDetails": NotRequired[UnusedPermissionDetailsTypeDef],
        "unusedIamUserAccessKeyDetails": NotRequired[UnusedIamUserAccessKeyDetailsTypeDef],
        "unusedIamRoleDetails": NotRequired[UnusedIamRoleDetailsTypeDef],
        "unusedIamUserPasswordDetails": NotRequired[UnusedIamUserPasswordDetailsTypeDef],
    },
)
ListFindingsResponseTypeDef = TypedDict(
    "ListFindingsResponseTypeDef",
    {
        "findings": List[FindingSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetFindingResponseTypeDef = TypedDict(
    "GetFindingResponseTypeDef",
    {
        "finding": FindingTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
S3BucketConfigurationTypeDef = TypedDict(
    "S3BucketConfigurationTypeDef",
    {
        "bucketPolicy": NotRequired[str],
        "bucketAclGrants": NotRequired[Sequence[S3BucketAclGrantConfigurationTypeDef]],
        "bucketPublicAccessBlock": NotRequired[S3PublicAccessBlockConfigurationTypeDef],
        "accessPoints": NotRequired[Mapping[str, S3AccessPointConfigurationTypeDef]],
    },
)
ValidatePolicyFindingTypeDef = TypedDict(
    "ValidatePolicyFindingTypeDef",
    {
        "findingDetails": str,
        "findingType": ValidatePolicyFindingTypeType,
        "issueCode": str,
        "learnMoreLink": str,
        "locations": List[LocationTypeDef],
    },
)
GetGeneratedPolicyResponseTypeDef = TypedDict(
    "GetGeneratedPolicyResponseTypeDef",
    {
        "jobDetails": JobDetailsTypeDef,
        "generatedPolicyResult": GeneratedPolicyResultTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetFindingV2ResponseTypeDef = TypedDict(
    "GetFindingV2ResponseTypeDef",
    {
        "analyzedAt": datetime,
        "createdAt": datetime,
        "error": str,
        "id": str,
        "nextToken": str,
        "resource": str,
        "resourceType": ResourceTypeType,
        "resourceOwnerAccount": str,
        "status": FindingStatusType,
        "updatedAt": datetime,
        "findingDetails": List[FindingDetailsTypeDef],
        "findingType": FindingTypeType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ConfigurationTypeDef = TypedDict(
    "ConfigurationTypeDef",
    {
        "ebsSnapshot": NotRequired[EbsSnapshotConfigurationTypeDef],
        "ecrRepository": NotRequired[EcrRepositoryConfigurationTypeDef],
        "iamRole": NotRequired[IamRoleConfigurationTypeDef],
        "efsFileSystem": NotRequired[EfsFileSystemConfigurationTypeDef],
        "kmsKey": NotRequired[KmsKeyConfigurationTypeDef],
        "rdsDbClusterSnapshot": NotRequired[RdsDbClusterSnapshotConfigurationTypeDef],
        "rdsDbSnapshot": NotRequired[RdsDbSnapshotConfigurationTypeDef],
        "secretsManagerSecret": NotRequired[SecretsManagerSecretConfigurationTypeDef],
        "s3Bucket": NotRequired[S3BucketConfigurationTypeDef],
        "snsTopic": NotRequired[SnsTopicConfigurationTypeDef],
        "sqsQueue": NotRequired[SqsQueueConfigurationTypeDef],
        "s3ExpressDirectoryBucket": NotRequired[S3ExpressDirectoryBucketConfigurationTypeDef],
    },
)
ValidatePolicyResponseTypeDef = TypedDict(
    "ValidatePolicyResponseTypeDef",
    {
        "findings": List[ValidatePolicyFindingTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AccessPreviewTypeDef = TypedDict(
    "AccessPreviewTypeDef",
    {
        "id": str,
        "analyzerArn": str,
        "configurations": Dict[str, ConfigurationTypeDef],
        "createdAt": datetime,
        "status": AccessPreviewStatusType,
        "statusReason": NotRequired[AccessPreviewStatusReasonTypeDef],
    },
)
CreateAccessPreviewRequestRequestTypeDef = TypedDict(
    "CreateAccessPreviewRequestRequestTypeDef",
    {
        "analyzerArn": str,
        "configurations": Mapping[str, ConfigurationTypeDef],
        "clientToken": NotRequired[str],
    },
)
GetAccessPreviewResponseTypeDef = TypedDict(
    "GetAccessPreviewResponseTypeDef",
    {
        "accessPreview": AccessPreviewTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
