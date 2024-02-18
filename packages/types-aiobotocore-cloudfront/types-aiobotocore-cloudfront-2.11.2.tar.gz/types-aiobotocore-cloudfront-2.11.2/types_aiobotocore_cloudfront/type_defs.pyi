"""
Type annotations for cloudfront service type definitions.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudfront/type_defs/)

Usage::

    ```python
    from types_aiobotocore_cloudfront.type_defs import AliasICPRecordalTypeDef

    data: AliasICPRecordalTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Sequence, Union

from aiobotocore.response import StreamingBody

from .literals import (
    CachePolicyCookieBehaviorType,
    CachePolicyHeaderBehaviorType,
    CachePolicyQueryStringBehaviorType,
    CachePolicyTypeType,
    CertificateSourceType,
    ContinuousDeploymentPolicyTypeType,
    EventTypeType,
    FrameOptionsListType,
    FunctionRuntimeType,
    FunctionStageType,
    GeoRestrictionTypeType,
    HttpVersionType,
    ICPRecordalStatusType,
    ItemSelectionType,
    MethodType,
    MinimumProtocolVersionType,
    OriginAccessControlOriginTypesType,
    OriginAccessControlSigningBehaviorsType,
    OriginProtocolPolicyType,
    OriginRequestPolicyCookieBehaviorType,
    OriginRequestPolicyHeaderBehaviorType,
    OriginRequestPolicyQueryStringBehaviorType,
    OriginRequestPolicyTypeType,
    PriceClassType,
    RealtimeMetricsSubscriptionStatusType,
    ReferrerPolicyListType,
    ResponseHeadersPolicyAccessControlAllowMethodsValuesType,
    ResponseHeadersPolicyTypeType,
    SslProtocolType,
    SSLSupportMethodType,
    ViewerProtocolPolicyType,
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
    "AliasICPRecordalTypeDef",
    "AliasesTypeDef",
    "CachedMethodsTypeDef",
    "AssociateAliasRequestRequestTypeDef",
    "BlobTypeDef",
    "TrustedKeyGroupsTypeDef",
    "TrustedSignersTypeDef",
    "CookieNamesTypeDef",
    "HeadersTypeDef",
    "QueryStringNamesTypeDef",
    "CloudFrontOriginAccessIdentityConfigTypeDef",
    "CloudFrontOriginAccessIdentitySummaryTypeDef",
    "ConflictingAliasTypeDef",
    "ContentTypeProfileTypeDef",
    "StagingDistributionDnsNamesTypeDef",
    "ContinuousDeploymentSingleHeaderConfigTypeDef",
    "SessionStickinessConfigTypeDef",
    "CopyDistributionRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "KeyGroupConfigTypeDef",
    "ImportSourceTypeDef",
    "KeyValueStoreTypeDef",
    "OriginAccessControlConfigTypeDef",
    "PublicKeyConfigTypeDef",
    "CustomErrorResponseTypeDef",
    "OriginCustomHeaderTypeDef",
    "OriginSslProtocolsTypeDef",
    "DeleteCachePolicyRequestRequestTypeDef",
    "DeleteCloudFrontOriginAccessIdentityRequestRequestTypeDef",
    "DeleteContinuousDeploymentPolicyRequestRequestTypeDef",
    "DeleteDistributionRequestRequestTypeDef",
    "DeleteFieldLevelEncryptionConfigRequestRequestTypeDef",
    "DeleteFieldLevelEncryptionProfileRequestRequestTypeDef",
    "DeleteFunctionRequestRequestTypeDef",
    "DeleteKeyGroupRequestRequestTypeDef",
    "DeleteKeyValueStoreRequestRequestTypeDef",
    "DeleteMonitoringSubscriptionRequestRequestTypeDef",
    "DeleteOriginAccessControlRequestRequestTypeDef",
    "DeleteOriginRequestPolicyRequestRequestTypeDef",
    "DeletePublicKeyRequestRequestTypeDef",
    "DeleteRealtimeLogConfigRequestRequestTypeDef",
    "DeleteResponseHeadersPolicyRequestRequestTypeDef",
    "DeleteStreamingDistributionRequestRequestTypeDef",
    "DescribeFunctionRequestRequestTypeDef",
    "DescribeKeyValueStoreRequestRequestTypeDef",
    "LoggingConfigTypeDef",
    "ViewerCertificateTypeDef",
    "DistributionIdListTypeDef",
    "FieldPatternsTypeDef",
    "KinesisStreamConfigTypeDef",
    "QueryStringCacheKeysTypeDef",
    "FunctionAssociationTypeDef",
    "FunctionMetadataTypeDef",
    "GeoRestrictionTypeDef",
    "GetCachePolicyConfigRequestRequestTypeDef",
    "GetCachePolicyRequestRequestTypeDef",
    "GetCloudFrontOriginAccessIdentityConfigRequestRequestTypeDef",
    "GetCloudFrontOriginAccessIdentityRequestRequestTypeDef",
    "GetContinuousDeploymentPolicyConfigRequestRequestTypeDef",
    "GetContinuousDeploymentPolicyRequestRequestTypeDef",
    "GetDistributionConfigRequestRequestTypeDef",
    "WaiterConfigTypeDef",
    "GetDistributionRequestRequestTypeDef",
    "GetFieldLevelEncryptionConfigRequestRequestTypeDef",
    "GetFieldLevelEncryptionProfileConfigRequestRequestTypeDef",
    "GetFieldLevelEncryptionProfileRequestRequestTypeDef",
    "GetFieldLevelEncryptionRequestRequestTypeDef",
    "GetFunctionRequestRequestTypeDef",
    "GetInvalidationRequestRequestTypeDef",
    "GetKeyGroupConfigRequestRequestTypeDef",
    "GetKeyGroupRequestRequestTypeDef",
    "GetMonitoringSubscriptionRequestRequestTypeDef",
    "GetOriginAccessControlConfigRequestRequestTypeDef",
    "GetOriginAccessControlRequestRequestTypeDef",
    "GetOriginRequestPolicyConfigRequestRequestTypeDef",
    "GetOriginRequestPolicyRequestRequestTypeDef",
    "GetPublicKeyConfigRequestRequestTypeDef",
    "GetPublicKeyRequestRequestTypeDef",
    "GetRealtimeLogConfigRequestRequestTypeDef",
    "GetResponseHeadersPolicyConfigRequestRequestTypeDef",
    "GetResponseHeadersPolicyRequestRequestTypeDef",
    "GetStreamingDistributionConfigRequestRequestTypeDef",
    "GetStreamingDistributionRequestRequestTypeDef",
    "PathsTypeDef",
    "InvalidationSummaryTypeDef",
    "KeyPairIdsTypeDef",
    "KeyValueStoreAssociationTypeDef",
    "LambdaFunctionAssociationTypeDef",
    "ListCachePoliciesRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "ListCloudFrontOriginAccessIdentitiesRequestRequestTypeDef",
    "ListConflictingAliasesRequestRequestTypeDef",
    "ListContinuousDeploymentPoliciesRequestRequestTypeDef",
    "ListDistributionsByCachePolicyIdRequestRequestTypeDef",
    "ListDistributionsByKeyGroupRequestRequestTypeDef",
    "ListDistributionsByOriginRequestPolicyIdRequestRequestTypeDef",
    "ListDistributionsByRealtimeLogConfigRequestRequestTypeDef",
    "ListDistributionsByResponseHeadersPolicyIdRequestRequestTypeDef",
    "ListDistributionsByWebACLIdRequestRequestTypeDef",
    "ListDistributionsRequestRequestTypeDef",
    "ListFieldLevelEncryptionConfigsRequestRequestTypeDef",
    "ListFieldLevelEncryptionProfilesRequestRequestTypeDef",
    "ListFunctionsRequestRequestTypeDef",
    "ListInvalidationsRequestRequestTypeDef",
    "ListKeyGroupsRequestRequestTypeDef",
    "ListKeyValueStoresRequestRequestTypeDef",
    "ListOriginAccessControlsRequestRequestTypeDef",
    "ListOriginRequestPoliciesRequestRequestTypeDef",
    "ListPublicKeysRequestRequestTypeDef",
    "ListRealtimeLogConfigsRequestRequestTypeDef",
    "ListResponseHeadersPoliciesRequestRequestTypeDef",
    "ListStreamingDistributionsRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "RealtimeMetricsSubscriptionConfigTypeDef",
    "OriginAccessControlSummaryTypeDef",
    "StatusCodesTypeDef",
    "OriginGroupMemberTypeDef",
    "OriginShieldTypeDef",
    "S3OriginConfigTypeDef",
    "PublicKeySummaryTypeDef",
    "PublishFunctionRequestRequestTypeDef",
    "QueryArgProfileTypeDef",
    "ResponseHeadersPolicyAccessControlAllowHeadersTypeDef",
    "ResponseHeadersPolicyAccessControlAllowMethodsTypeDef",
    "ResponseHeadersPolicyAccessControlAllowOriginsTypeDef",
    "ResponseHeadersPolicyAccessControlExposeHeadersTypeDef",
    "ResponseHeadersPolicyServerTimingHeadersConfigTypeDef",
    "ResponseHeadersPolicyContentSecurityPolicyTypeDef",
    "ResponseHeadersPolicyContentTypeOptionsTypeDef",
    "ResponseHeadersPolicyCustomHeaderTypeDef",
    "ResponseHeadersPolicyFrameOptionsTypeDef",
    "ResponseHeadersPolicyReferrerPolicyTypeDef",
    "ResponseHeadersPolicyRemoveHeaderTypeDef",
    "ResponseHeadersPolicyStrictTransportSecurityTypeDef",
    "ResponseHeadersPolicyXSSProtectionTypeDef",
    "S3OriginTypeDef",
    "StreamingLoggingConfigTypeDef",
    "TagKeysTypeDef",
    "TagTypeDef",
    "UpdateDistributionWithStagingConfigRequestRequestTypeDef",
    "UpdateKeyValueStoreRequestRequestTypeDef",
    "AllowedMethodsTypeDef",
    "TestFunctionRequestRequestTypeDef",
    "CachePolicyCookiesConfigTypeDef",
    "CookiePreferenceTypeDef",
    "OriginRequestPolicyCookiesConfigTypeDef",
    "CachePolicyHeadersConfigTypeDef",
    "OriginRequestPolicyHeadersConfigTypeDef",
    "CachePolicyQueryStringsConfigTypeDef",
    "OriginRequestPolicyQueryStringsConfigTypeDef",
    "CloudFrontOriginAccessIdentityTypeDef",
    "CreateCloudFrontOriginAccessIdentityRequestRequestTypeDef",
    "UpdateCloudFrontOriginAccessIdentityRequestRequestTypeDef",
    "CloudFrontOriginAccessIdentityListTypeDef",
    "ConflictingAliasesListTypeDef",
    "ContentTypeProfilesTypeDef",
    "ContinuousDeploymentSingleWeightConfigTypeDef",
    "EmptyResponseMetadataTypeDef",
    "GetCloudFrontOriginAccessIdentityConfigResultTypeDef",
    "GetFunctionResultTypeDef",
    "CreateKeyGroupRequestRequestTypeDef",
    "GetKeyGroupConfigResultTypeDef",
    "KeyGroupTypeDef",
    "UpdateKeyGroupRequestRequestTypeDef",
    "CreateKeyValueStoreRequestRequestTypeDef",
    "CreateKeyValueStoreResultTypeDef",
    "DescribeKeyValueStoreResultTypeDef",
    "KeyValueStoreListTypeDef",
    "UpdateKeyValueStoreResultTypeDef",
    "CreateOriginAccessControlRequestRequestTypeDef",
    "GetOriginAccessControlConfigResultTypeDef",
    "OriginAccessControlTypeDef",
    "UpdateOriginAccessControlRequestRequestTypeDef",
    "CreatePublicKeyRequestRequestTypeDef",
    "GetPublicKeyConfigResultTypeDef",
    "PublicKeyTypeDef",
    "UpdatePublicKeyRequestRequestTypeDef",
    "CustomErrorResponsesTypeDef",
    "CustomHeadersTypeDef",
    "CustomOriginConfigTypeDef",
    "ListDistributionsByCachePolicyIdResultTypeDef",
    "ListDistributionsByKeyGroupResultTypeDef",
    "ListDistributionsByOriginRequestPolicyIdResultTypeDef",
    "ListDistributionsByResponseHeadersPolicyIdResultTypeDef",
    "EncryptionEntityTypeDef",
    "EndPointTypeDef",
    "FunctionAssociationsTypeDef",
    "RestrictionsTypeDef",
    "GetDistributionRequestDistributionDeployedWaitTypeDef",
    "GetInvalidationRequestInvalidationCompletedWaitTypeDef",
    "GetStreamingDistributionRequestStreamingDistributionDeployedWaitTypeDef",
    "InvalidationBatchTypeDef",
    "InvalidationListTypeDef",
    "KGKeyPairIdsTypeDef",
    "SignerTypeDef",
    "KeyValueStoreAssociationsTypeDef",
    "LambdaFunctionAssociationsTypeDef",
    "ListCloudFrontOriginAccessIdentitiesRequestListCloudFrontOriginAccessIdentitiesPaginateTypeDef",
    "ListDistributionsRequestListDistributionsPaginateTypeDef",
    "ListInvalidationsRequestListInvalidationsPaginateTypeDef",
    "ListKeyValueStoresRequestListKeyValueStoresPaginateTypeDef",
    "ListStreamingDistributionsRequestListStreamingDistributionsPaginateTypeDef",
    "MonitoringSubscriptionTypeDef",
    "OriginAccessControlListTypeDef",
    "OriginGroupFailoverCriteriaTypeDef",
    "OriginGroupMembersTypeDef",
    "PublicKeyListTypeDef",
    "QueryArgProfilesTypeDef",
    "ResponseHeadersPolicyCorsConfigTypeDef",
    "ResponseHeadersPolicyCustomHeadersConfigTypeDef",
    "ResponseHeadersPolicyRemoveHeadersConfigTypeDef",
    "ResponseHeadersPolicySecurityHeadersConfigTypeDef",
    "StreamingDistributionSummaryTypeDef",
    "StreamingDistributionConfigTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "TagsTypeDef",
    "ForwardedValuesTypeDef",
    "ParametersInCacheKeyAndForwardedToOriginTypeDef",
    "OriginRequestPolicyConfigTypeDef",
    "CreateCloudFrontOriginAccessIdentityResultTypeDef",
    "GetCloudFrontOriginAccessIdentityResultTypeDef",
    "UpdateCloudFrontOriginAccessIdentityResultTypeDef",
    "ListCloudFrontOriginAccessIdentitiesResultTypeDef",
    "ListConflictingAliasesResultTypeDef",
    "ContentTypeProfileConfigTypeDef",
    "TrafficConfigTypeDef",
    "CreateKeyGroupResultTypeDef",
    "GetKeyGroupResultTypeDef",
    "KeyGroupSummaryTypeDef",
    "UpdateKeyGroupResultTypeDef",
    "ListKeyValueStoresResultTypeDef",
    "CreateOriginAccessControlResultTypeDef",
    "GetOriginAccessControlResultTypeDef",
    "UpdateOriginAccessControlResultTypeDef",
    "CreatePublicKeyResultTypeDef",
    "GetPublicKeyResultTypeDef",
    "UpdatePublicKeyResultTypeDef",
    "OriginTypeDef",
    "EncryptionEntitiesTypeDef",
    "CreateRealtimeLogConfigRequestRequestTypeDef",
    "RealtimeLogConfigTypeDef",
    "UpdateRealtimeLogConfigRequestRequestTypeDef",
    "CreateInvalidationRequestRequestTypeDef",
    "InvalidationTypeDef",
    "ListInvalidationsResultTypeDef",
    "ActiveTrustedKeyGroupsTypeDef",
    "ActiveTrustedSignersTypeDef",
    "FunctionConfigTypeDef",
    "CreateMonitoringSubscriptionRequestRequestTypeDef",
    "CreateMonitoringSubscriptionResultTypeDef",
    "GetMonitoringSubscriptionResultTypeDef",
    "ListOriginAccessControlsResultTypeDef",
    "OriginGroupTypeDef",
    "ListPublicKeysResultTypeDef",
    "QueryArgProfileConfigTypeDef",
    "ResponseHeadersPolicyConfigTypeDef",
    "StreamingDistributionListTypeDef",
    "CreateStreamingDistributionRequestRequestTypeDef",
    "GetStreamingDistributionConfigResultTypeDef",
    "UpdateStreamingDistributionRequestRequestTypeDef",
    "ListTagsForResourceResultTypeDef",
    "StreamingDistributionConfigWithTagsTypeDef",
    "TagResourceRequestRequestTypeDef",
    "CacheBehaviorTypeDef",
    "DefaultCacheBehaviorTypeDef",
    "CachePolicyConfigTypeDef",
    "CreateOriginRequestPolicyRequestRequestTypeDef",
    "GetOriginRequestPolicyConfigResultTypeDef",
    "OriginRequestPolicyTypeDef",
    "UpdateOriginRequestPolicyRequestRequestTypeDef",
    "ContinuousDeploymentPolicyConfigTypeDef",
    "KeyGroupListTypeDef",
    "OriginsTypeDef",
    "FieldLevelEncryptionProfileConfigTypeDef",
    "FieldLevelEncryptionProfileSummaryTypeDef",
    "CreateRealtimeLogConfigResultTypeDef",
    "GetRealtimeLogConfigResultTypeDef",
    "RealtimeLogConfigsTypeDef",
    "UpdateRealtimeLogConfigResultTypeDef",
    "CreateInvalidationResultTypeDef",
    "GetInvalidationResultTypeDef",
    "StreamingDistributionTypeDef",
    "CreateFunctionRequestRequestTypeDef",
    "FunctionSummaryTypeDef",
    "UpdateFunctionRequestRequestTypeDef",
    "OriginGroupsTypeDef",
    "FieldLevelEncryptionConfigTypeDef",
    "FieldLevelEncryptionSummaryTypeDef",
    "CreateResponseHeadersPolicyRequestRequestTypeDef",
    "GetResponseHeadersPolicyConfigResultTypeDef",
    "ResponseHeadersPolicyTypeDef",
    "UpdateResponseHeadersPolicyRequestRequestTypeDef",
    "ListStreamingDistributionsResultTypeDef",
    "CreateStreamingDistributionWithTagsRequestRequestTypeDef",
    "CacheBehaviorsTypeDef",
    "CachePolicyTypeDef",
    "CreateCachePolicyRequestRequestTypeDef",
    "GetCachePolicyConfigResultTypeDef",
    "UpdateCachePolicyRequestRequestTypeDef",
    "CreateOriginRequestPolicyResultTypeDef",
    "GetOriginRequestPolicyResultTypeDef",
    "OriginRequestPolicySummaryTypeDef",
    "UpdateOriginRequestPolicyResultTypeDef",
    "ContinuousDeploymentPolicyTypeDef",
    "CreateContinuousDeploymentPolicyRequestRequestTypeDef",
    "GetContinuousDeploymentPolicyConfigResultTypeDef",
    "UpdateContinuousDeploymentPolicyRequestRequestTypeDef",
    "ListKeyGroupsResultTypeDef",
    "CreateFieldLevelEncryptionProfileRequestRequestTypeDef",
    "FieldLevelEncryptionProfileTypeDef",
    "GetFieldLevelEncryptionProfileConfigResultTypeDef",
    "UpdateFieldLevelEncryptionProfileRequestRequestTypeDef",
    "FieldLevelEncryptionProfileListTypeDef",
    "ListRealtimeLogConfigsResultTypeDef",
    "CreateStreamingDistributionResultTypeDef",
    "CreateStreamingDistributionWithTagsResultTypeDef",
    "GetStreamingDistributionResultTypeDef",
    "UpdateStreamingDistributionResultTypeDef",
    "CreateFunctionResultTypeDef",
    "DescribeFunctionResultTypeDef",
    "FunctionListTypeDef",
    "PublishFunctionResultTypeDef",
    "TestResultTypeDef",
    "UpdateFunctionResultTypeDef",
    "CreateFieldLevelEncryptionConfigRequestRequestTypeDef",
    "FieldLevelEncryptionTypeDef",
    "GetFieldLevelEncryptionConfigResultTypeDef",
    "UpdateFieldLevelEncryptionConfigRequestRequestTypeDef",
    "FieldLevelEncryptionListTypeDef",
    "CreateResponseHeadersPolicyResultTypeDef",
    "GetResponseHeadersPolicyResultTypeDef",
    "ResponseHeadersPolicySummaryTypeDef",
    "UpdateResponseHeadersPolicyResultTypeDef",
    "DistributionConfigTypeDef",
    "DistributionSummaryTypeDef",
    "CachePolicySummaryTypeDef",
    "CreateCachePolicyResultTypeDef",
    "GetCachePolicyResultTypeDef",
    "UpdateCachePolicyResultTypeDef",
    "OriginRequestPolicyListTypeDef",
    "ContinuousDeploymentPolicySummaryTypeDef",
    "CreateContinuousDeploymentPolicyResultTypeDef",
    "GetContinuousDeploymentPolicyResultTypeDef",
    "UpdateContinuousDeploymentPolicyResultTypeDef",
    "CreateFieldLevelEncryptionProfileResultTypeDef",
    "GetFieldLevelEncryptionProfileResultTypeDef",
    "UpdateFieldLevelEncryptionProfileResultTypeDef",
    "ListFieldLevelEncryptionProfilesResultTypeDef",
    "ListFunctionsResultTypeDef",
    "TestFunctionResultTypeDef",
    "CreateFieldLevelEncryptionConfigResultTypeDef",
    "GetFieldLevelEncryptionResultTypeDef",
    "UpdateFieldLevelEncryptionConfigResultTypeDef",
    "ListFieldLevelEncryptionConfigsResultTypeDef",
    "ResponseHeadersPolicyListTypeDef",
    "CreateDistributionRequestRequestTypeDef",
    "DistributionConfigWithTagsTypeDef",
    "DistributionTypeDef",
    "GetDistributionConfigResultTypeDef",
    "UpdateDistributionRequestRequestTypeDef",
    "DistributionListTypeDef",
    "CachePolicyListTypeDef",
    "ListOriginRequestPoliciesResultTypeDef",
    "ContinuousDeploymentPolicyListTypeDef",
    "ListResponseHeadersPoliciesResultTypeDef",
    "CreateDistributionWithTagsRequestRequestTypeDef",
    "CopyDistributionResultTypeDef",
    "CreateDistributionResultTypeDef",
    "CreateDistributionWithTagsResultTypeDef",
    "GetDistributionResultTypeDef",
    "UpdateDistributionResultTypeDef",
    "UpdateDistributionWithStagingConfigResultTypeDef",
    "ListDistributionsByRealtimeLogConfigResultTypeDef",
    "ListDistributionsByWebACLIdResultTypeDef",
    "ListDistributionsResultTypeDef",
    "ListCachePoliciesResultTypeDef",
    "ListContinuousDeploymentPoliciesResultTypeDef",
)

AliasICPRecordalTypeDef = TypedDict(
    "AliasICPRecordalTypeDef",
    {
        "CNAME": NotRequired[str],
        "ICPRecordalStatus": NotRequired[ICPRecordalStatusType],
    },
)
AliasesTypeDef = TypedDict(
    "AliasesTypeDef",
    {
        "Quantity": int,
        "Items": NotRequired[List[str]],
    },
)
CachedMethodsTypeDef = TypedDict(
    "CachedMethodsTypeDef",
    {
        "Quantity": int,
        "Items": List[MethodType],
    },
)
AssociateAliasRequestRequestTypeDef = TypedDict(
    "AssociateAliasRequestRequestTypeDef",
    {
        "TargetDistributionId": str,
        "Alias": str,
    },
)
BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]
TrustedKeyGroupsTypeDef = TypedDict(
    "TrustedKeyGroupsTypeDef",
    {
        "Enabled": bool,
        "Quantity": int,
        "Items": NotRequired[List[str]],
    },
)
TrustedSignersTypeDef = TypedDict(
    "TrustedSignersTypeDef",
    {
        "Enabled": bool,
        "Quantity": int,
        "Items": NotRequired[List[str]],
    },
)
CookieNamesTypeDef = TypedDict(
    "CookieNamesTypeDef",
    {
        "Quantity": int,
        "Items": NotRequired[List[str]],
    },
)
HeadersTypeDef = TypedDict(
    "HeadersTypeDef",
    {
        "Quantity": int,
        "Items": NotRequired[List[str]],
    },
)
QueryStringNamesTypeDef = TypedDict(
    "QueryStringNamesTypeDef",
    {
        "Quantity": int,
        "Items": NotRequired[Sequence[str]],
    },
)
CloudFrontOriginAccessIdentityConfigTypeDef = TypedDict(
    "CloudFrontOriginAccessIdentityConfigTypeDef",
    {
        "CallerReference": str,
        "Comment": str,
    },
)
CloudFrontOriginAccessIdentitySummaryTypeDef = TypedDict(
    "CloudFrontOriginAccessIdentitySummaryTypeDef",
    {
        "Id": str,
        "S3CanonicalUserId": str,
        "Comment": str,
    },
)
ConflictingAliasTypeDef = TypedDict(
    "ConflictingAliasTypeDef",
    {
        "Alias": NotRequired[str],
        "DistributionId": NotRequired[str],
        "AccountId": NotRequired[str],
    },
)
ContentTypeProfileTypeDef = TypedDict(
    "ContentTypeProfileTypeDef",
    {
        "Format": Literal["URLEncoded"],
        "ContentType": str,
        "ProfileId": NotRequired[str],
    },
)
StagingDistributionDnsNamesTypeDef = TypedDict(
    "StagingDistributionDnsNamesTypeDef",
    {
        "Quantity": int,
        "Items": NotRequired[Sequence[str]],
    },
)
ContinuousDeploymentSingleHeaderConfigTypeDef = TypedDict(
    "ContinuousDeploymentSingleHeaderConfigTypeDef",
    {
        "Header": str,
        "Value": str,
    },
)
SessionStickinessConfigTypeDef = TypedDict(
    "SessionStickinessConfigTypeDef",
    {
        "IdleTTL": int,
        "MaximumTTL": int,
    },
)
CopyDistributionRequestRequestTypeDef = TypedDict(
    "CopyDistributionRequestRequestTypeDef",
    {
        "PrimaryDistributionId": str,
        "CallerReference": str,
        "Staging": NotRequired[bool],
        "IfMatch": NotRequired[str],
        "Enabled": NotRequired[bool],
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
KeyGroupConfigTypeDef = TypedDict(
    "KeyGroupConfigTypeDef",
    {
        "Name": str,
        "Items": Sequence[str],
        "Comment": NotRequired[str],
    },
)
ImportSourceTypeDef = TypedDict(
    "ImportSourceTypeDef",
    {
        "SourceType": Literal["S3"],
        "SourceARN": str,
    },
)
KeyValueStoreTypeDef = TypedDict(
    "KeyValueStoreTypeDef",
    {
        "Name": str,
        "Id": str,
        "Comment": str,
        "ARN": str,
        "LastModifiedTime": datetime,
        "Status": NotRequired[str],
    },
)
OriginAccessControlConfigTypeDef = TypedDict(
    "OriginAccessControlConfigTypeDef",
    {
        "Name": str,
        "SigningProtocol": Literal["sigv4"],
        "SigningBehavior": OriginAccessControlSigningBehaviorsType,
        "OriginAccessControlOriginType": OriginAccessControlOriginTypesType,
        "Description": NotRequired[str],
    },
)
PublicKeyConfigTypeDef = TypedDict(
    "PublicKeyConfigTypeDef",
    {
        "CallerReference": str,
        "Name": str,
        "EncodedKey": str,
        "Comment": NotRequired[str],
    },
)
CustomErrorResponseTypeDef = TypedDict(
    "CustomErrorResponseTypeDef",
    {
        "ErrorCode": int,
        "ResponsePagePath": NotRequired[str],
        "ResponseCode": NotRequired[str],
        "ErrorCachingMinTTL": NotRequired[int],
    },
)
OriginCustomHeaderTypeDef = TypedDict(
    "OriginCustomHeaderTypeDef",
    {
        "HeaderName": str,
        "HeaderValue": str,
    },
)
OriginSslProtocolsTypeDef = TypedDict(
    "OriginSslProtocolsTypeDef",
    {
        "Quantity": int,
        "Items": List[SslProtocolType],
    },
)
DeleteCachePolicyRequestRequestTypeDef = TypedDict(
    "DeleteCachePolicyRequestRequestTypeDef",
    {
        "Id": str,
        "IfMatch": NotRequired[str],
    },
)
DeleteCloudFrontOriginAccessIdentityRequestRequestTypeDef = TypedDict(
    "DeleteCloudFrontOriginAccessIdentityRequestRequestTypeDef",
    {
        "Id": str,
        "IfMatch": NotRequired[str],
    },
)
DeleteContinuousDeploymentPolicyRequestRequestTypeDef = TypedDict(
    "DeleteContinuousDeploymentPolicyRequestRequestTypeDef",
    {
        "Id": str,
        "IfMatch": NotRequired[str],
    },
)
DeleteDistributionRequestRequestTypeDef = TypedDict(
    "DeleteDistributionRequestRequestTypeDef",
    {
        "Id": str,
        "IfMatch": NotRequired[str],
    },
)
DeleteFieldLevelEncryptionConfigRequestRequestTypeDef = TypedDict(
    "DeleteFieldLevelEncryptionConfigRequestRequestTypeDef",
    {
        "Id": str,
        "IfMatch": NotRequired[str],
    },
)
DeleteFieldLevelEncryptionProfileRequestRequestTypeDef = TypedDict(
    "DeleteFieldLevelEncryptionProfileRequestRequestTypeDef",
    {
        "Id": str,
        "IfMatch": NotRequired[str],
    },
)
DeleteFunctionRequestRequestTypeDef = TypedDict(
    "DeleteFunctionRequestRequestTypeDef",
    {
        "Name": str,
        "IfMatch": str,
    },
)
DeleteKeyGroupRequestRequestTypeDef = TypedDict(
    "DeleteKeyGroupRequestRequestTypeDef",
    {
        "Id": str,
        "IfMatch": NotRequired[str],
    },
)
DeleteKeyValueStoreRequestRequestTypeDef = TypedDict(
    "DeleteKeyValueStoreRequestRequestTypeDef",
    {
        "Name": str,
        "IfMatch": str,
    },
)
DeleteMonitoringSubscriptionRequestRequestTypeDef = TypedDict(
    "DeleteMonitoringSubscriptionRequestRequestTypeDef",
    {
        "DistributionId": str,
    },
)
DeleteOriginAccessControlRequestRequestTypeDef = TypedDict(
    "DeleteOriginAccessControlRequestRequestTypeDef",
    {
        "Id": str,
        "IfMatch": NotRequired[str],
    },
)
DeleteOriginRequestPolicyRequestRequestTypeDef = TypedDict(
    "DeleteOriginRequestPolicyRequestRequestTypeDef",
    {
        "Id": str,
        "IfMatch": NotRequired[str],
    },
)
DeletePublicKeyRequestRequestTypeDef = TypedDict(
    "DeletePublicKeyRequestRequestTypeDef",
    {
        "Id": str,
        "IfMatch": NotRequired[str],
    },
)
DeleteRealtimeLogConfigRequestRequestTypeDef = TypedDict(
    "DeleteRealtimeLogConfigRequestRequestTypeDef",
    {
        "Name": NotRequired[str],
        "ARN": NotRequired[str],
    },
)
DeleteResponseHeadersPolicyRequestRequestTypeDef = TypedDict(
    "DeleteResponseHeadersPolicyRequestRequestTypeDef",
    {
        "Id": str,
        "IfMatch": NotRequired[str],
    },
)
DeleteStreamingDistributionRequestRequestTypeDef = TypedDict(
    "DeleteStreamingDistributionRequestRequestTypeDef",
    {
        "Id": str,
        "IfMatch": NotRequired[str],
    },
)
DescribeFunctionRequestRequestTypeDef = TypedDict(
    "DescribeFunctionRequestRequestTypeDef",
    {
        "Name": str,
        "Stage": NotRequired[FunctionStageType],
    },
)
DescribeKeyValueStoreRequestRequestTypeDef = TypedDict(
    "DescribeKeyValueStoreRequestRequestTypeDef",
    {
        "Name": str,
    },
)
LoggingConfigTypeDef = TypedDict(
    "LoggingConfigTypeDef",
    {
        "Enabled": bool,
        "IncludeCookies": bool,
        "Bucket": str,
        "Prefix": str,
    },
)
ViewerCertificateTypeDef = TypedDict(
    "ViewerCertificateTypeDef",
    {
        "CloudFrontDefaultCertificate": NotRequired[bool],
        "IAMCertificateId": NotRequired[str],
        "ACMCertificateArn": NotRequired[str],
        "SSLSupportMethod": NotRequired[SSLSupportMethodType],
        "MinimumProtocolVersion": NotRequired[MinimumProtocolVersionType],
        "Certificate": NotRequired[str],
        "CertificateSource": NotRequired[CertificateSourceType],
    },
)
DistributionIdListTypeDef = TypedDict(
    "DistributionIdListTypeDef",
    {
        "Marker": str,
        "MaxItems": int,
        "IsTruncated": bool,
        "Quantity": int,
        "NextMarker": NotRequired[str],
        "Items": NotRequired[List[str]],
    },
)
FieldPatternsTypeDef = TypedDict(
    "FieldPatternsTypeDef",
    {
        "Quantity": int,
        "Items": NotRequired[Sequence[str]],
    },
)
KinesisStreamConfigTypeDef = TypedDict(
    "KinesisStreamConfigTypeDef",
    {
        "RoleARN": str,
        "StreamARN": str,
    },
)
QueryStringCacheKeysTypeDef = TypedDict(
    "QueryStringCacheKeysTypeDef",
    {
        "Quantity": int,
        "Items": NotRequired[List[str]],
    },
)
FunctionAssociationTypeDef = TypedDict(
    "FunctionAssociationTypeDef",
    {
        "FunctionARN": str,
        "EventType": EventTypeType,
    },
)
FunctionMetadataTypeDef = TypedDict(
    "FunctionMetadataTypeDef",
    {
        "FunctionARN": str,
        "LastModifiedTime": datetime,
        "Stage": NotRequired[FunctionStageType],
        "CreatedTime": NotRequired[datetime],
    },
)
GeoRestrictionTypeDef = TypedDict(
    "GeoRestrictionTypeDef",
    {
        "RestrictionType": GeoRestrictionTypeType,
        "Quantity": int,
        "Items": NotRequired[List[str]],
    },
)
GetCachePolicyConfigRequestRequestTypeDef = TypedDict(
    "GetCachePolicyConfigRequestRequestTypeDef",
    {
        "Id": str,
    },
)
GetCachePolicyRequestRequestTypeDef = TypedDict(
    "GetCachePolicyRequestRequestTypeDef",
    {
        "Id": str,
    },
)
GetCloudFrontOriginAccessIdentityConfigRequestRequestTypeDef = TypedDict(
    "GetCloudFrontOriginAccessIdentityConfigRequestRequestTypeDef",
    {
        "Id": str,
    },
)
GetCloudFrontOriginAccessIdentityRequestRequestTypeDef = TypedDict(
    "GetCloudFrontOriginAccessIdentityRequestRequestTypeDef",
    {
        "Id": str,
    },
)
GetContinuousDeploymentPolicyConfigRequestRequestTypeDef = TypedDict(
    "GetContinuousDeploymentPolicyConfigRequestRequestTypeDef",
    {
        "Id": str,
    },
)
GetContinuousDeploymentPolicyRequestRequestTypeDef = TypedDict(
    "GetContinuousDeploymentPolicyRequestRequestTypeDef",
    {
        "Id": str,
    },
)
GetDistributionConfigRequestRequestTypeDef = TypedDict(
    "GetDistributionConfigRequestRequestTypeDef",
    {
        "Id": str,
    },
)
WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": NotRequired[int],
        "MaxAttempts": NotRequired[int],
    },
)
GetDistributionRequestRequestTypeDef = TypedDict(
    "GetDistributionRequestRequestTypeDef",
    {
        "Id": str,
    },
)
GetFieldLevelEncryptionConfigRequestRequestTypeDef = TypedDict(
    "GetFieldLevelEncryptionConfigRequestRequestTypeDef",
    {
        "Id": str,
    },
)
GetFieldLevelEncryptionProfileConfigRequestRequestTypeDef = TypedDict(
    "GetFieldLevelEncryptionProfileConfigRequestRequestTypeDef",
    {
        "Id": str,
    },
)
GetFieldLevelEncryptionProfileRequestRequestTypeDef = TypedDict(
    "GetFieldLevelEncryptionProfileRequestRequestTypeDef",
    {
        "Id": str,
    },
)
GetFieldLevelEncryptionRequestRequestTypeDef = TypedDict(
    "GetFieldLevelEncryptionRequestRequestTypeDef",
    {
        "Id": str,
    },
)
GetFunctionRequestRequestTypeDef = TypedDict(
    "GetFunctionRequestRequestTypeDef",
    {
        "Name": str,
        "Stage": NotRequired[FunctionStageType],
    },
)
GetInvalidationRequestRequestTypeDef = TypedDict(
    "GetInvalidationRequestRequestTypeDef",
    {
        "DistributionId": str,
        "Id": str,
    },
)
GetKeyGroupConfigRequestRequestTypeDef = TypedDict(
    "GetKeyGroupConfigRequestRequestTypeDef",
    {
        "Id": str,
    },
)
GetKeyGroupRequestRequestTypeDef = TypedDict(
    "GetKeyGroupRequestRequestTypeDef",
    {
        "Id": str,
    },
)
GetMonitoringSubscriptionRequestRequestTypeDef = TypedDict(
    "GetMonitoringSubscriptionRequestRequestTypeDef",
    {
        "DistributionId": str,
    },
)
GetOriginAccessControlConfigRequestRequestTypeDef = TypedDict(
    "GetOriginAccessControlConfigRequestRequestTypeDef",
    {
        "Id": str,
    },
)
GetOriginAccessControlRequestRequestTypeDef = TypedDict(
    "GetOriginAccessControlRequestRequestTypeDef",
    {
        "Id": str,
    },
)
GetOriginRequestPolicyConfigRequestRequestTypeDef = TypedDict(
    "GetOriginRequestPolicyConfigRequestRequestTypeDef",
    {
        "Id": str,
    },
)
GetOriginRequestPolicyRequestRequestTypeDef = TypedDict(
    "GetOriginRequestPolicyRequestRequestTypeDef",
    {
        "Id": str,
    },
)
GetPublicKeyConfigRequestRequestTypeDef = TypedDict(
    "GetPublicKeyConfigRequestRequestTypeDef",
    {
        "Id": str,
    },
)
GetPublicKeyRequestRequestTypeDef = TypedDict(
    "GetPublicKeyRequestRequestTypeDef",
    {
        "Id": str,
    },
)
GetRealtimeLogConfigRequestRequestTypeDef = TypedDict(
    "GetRealtimeLogConfigRequestRequestTypeDef",
    {
        "Name": NotRequired[str],
        "ARN": NotRequired[str],
    },
)
GetResponseHeadersPolicyConfigRequestRequestTypeDef = TypedDict(
    "GetResponseHeadersPolicyConfigRequestRequestTypeDef",
    {
        "Id": str,
    },
)
GetResponseHeadersPolicyRequestRequestTypeDef = TypedDict(
    "GetResponseHeadersPolicyRequestRequestTypeDef",
    {
        "Id": str,
    },
)
GetStreamingDistributionConfigRequestRequestTypeDef = TypedDict(
    "GetStreamingDistributionConfigRequestRequestTypeDef",
    {
        "Id": str,
    },
)
GetStreamingDistributionRequestRequestTypeDef = TypedDict(
    "GetStreamingDistributionRequestRequestTypeDef",
    {
        "Id": str,
    },
)
PathsTypeDef = TypedDict(
    "PathsTypeDef",
    {
        "Quantity": int,
        "Items": NotRequired[Sequence[str]],
    },
)
InvalidationSummaryTypeDef = TypedDict(
    "InvalidationSummaryTypeDef",
    {
        "Id": str,
        "CreateTime": datetime,
        "Status": str,
    },
)
KeyPairIdsTypeDef = TypedDict(
    "KeyPairIdsTypeDef",
    {
        "Quantity": int,
        "Items": NotRequired[List[str]],
    },
)
KeyValueStoreAssociationTypeDef = TypedDict(
    "KeyValueStoreAssociationTypeDef",
    {
        "KeyValueStoreARN": str,
    },
)
LambdaFunctionAssociationTypeDef = TypedDict(
    "LambdaFunctionAssociationTypeDef",
    {
        "LambdaFunctionARN": str,
        "EventType": EventTypeType,
        "IncludeBody": NotRequired[bool],
    },
)
ListCachePoliciesRequestRequestTypeDef = TypedDict(
    "ListCachePoliciesRequestRequestTypeDef",
    {
        "Type": NotRequired[CachePolicyTypeType],
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[str],
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
ListCloudFrontOriginAccessIdentitiesRequestRequestTypeDef = TypedDict(
    "ListCloudFrontOriginAccessIdentitiesRequestRequestTypeDef",
    {
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[str],
    },
)
ListConflictingAliasesRequestRequestTypeDef = TypedDict(
    "ListConflictingAliasesRequestRequestTypeDef",
    {
        "DistributionId": str,
        "Alias": str,
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[int],
    },
)
ListContinuousDeploymentPoliciesRequestRequestTypeDef = TypedDict(
    "ListContinuousDeploymentPoliciesRequestRequestTypeDef",
    {
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[str],
    },
)
ListDistributionsByCachePolicyIdRequestRequestTypeDef = TypedDict(
    "ListDistributionsByCachePolicyIdRequestRequestTypeDef",
    {
        "CachePolicyId": str,
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[str],
    },
)
ListDistributionsByKeyGroupRequestRequestTypeDef = TypedDict(
    "ListDistributionsByKeyGroupRequestRequestTypeDef",
    {
        "KeyGroupId": str,
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[str],
    },
)
ListDistributionsByOriginRequestPolicyIdRequestRequestTypeDef = TypedDict(
    "ListDistributionsByOriginRequestPolicyIdRequestRequestTypeDef",
    {
        "OriginRequestPolicyId": str,
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[str],
    },
)
ListDistributionsByRealtimeLogConfigRequestRequestTypeDef = TypedDict(
    "ListDistributionsByRealtimeLogConfigRequestRequestTypeDef",
    {
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[str],
        "RealtimeLogConfigName": NotRequired[str],
        "RealtimeLogConfigArn": NotRequired[str],
    },
)
ListDistributionsByResponseHeadersPolicyIdRequestRequestTypeDef = TypedDict(
    "ListDistributionsByResponseHeadersPolicyIdRequestRequestTypeDef",
    {
        "ResponseHeadersPolicyId": str,
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[str],
    },
)
ListDistributionsByWebACLIdRequestRequestTypeDef = TypedDict(
    "ListDistributionsByWebACLIdRequestRequestTypeDef",
    {
        "WebACLId": str,
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[str],
    },
)
ListDistributionsRequestRequestTypeDef = TypedDict(
    "ListDistributionsRequestRequestTypeDef",
    {
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[str],
    },
)
ListFieldLevelEncryptionConfigsRequestRequestTypeDef = TypedDict(
    "ListFieldLevelEncryptionConfigsRequestRequestTypeDef",
    {
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[str],
    },
)
ListFieldLevelEncryptionProfilesRequestRequestTypeDef = TypedDict(
    "ListFieldLevelEncryptionProfilesRequestRequestTypeDef",
    {
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[str],
    },
)
ListFunctionsRequestRequestTypeDef = TypedDict(
    "ListFunctionsRequestRequestTypeDef",
    {
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[str],
        "Stage": NotRequired[FunctionStageType],
    },
)
ListInvalidationsRequestRequestTypeDef = TypedDict(
    "ListInvalidationsRequestRequestTypeDef",
    {
        "DistributionId": str,
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[str],
    },
)
ListKeyGroupsRequestRequestTypeDef = TypedDict(
    "ListKeyGroupsRequestRequestTypeDef",
    {
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[str],
    },
)
ListKeyValueStoresRequestRequestTypeDef = TypedDict(
    "ListKeyValueStoresRequestRequestTypeDef",
    {
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[str],
        "Status": NotRequired[str],
    },
)
ListOriginAccessControlsRequestRequestTypeDef = TypedDict(
    "ListOriginAccessControlsRequestRequestTypeDef",
    {
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[str],
    },
)
ListOriginRequestPoliciesRequestRequestTypeDef = TypedDict(
    "ListOriginRequestPoliciesRequestRequestTypeDef",
    {
        "Type": NotRequired[OriginRequestPolicyTypeType],
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[str],
    },
)
ListPublicKeysRequestRequestTypeDef = TypedDict(
    "ListPublicKeysRequestRequestTypeDef",
    {
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[str],
    },
)
ListRealtimeLogConfigsRequestRequestTypeDef = TypedDict(
    "ListRealtimeLogConfigsRequestRequestTypeDef",
    {
        "MaxItems": NotRequired[str],
        "Marker": NotRequired[str],
    },
)
ListResponseHeadersPoliciesRequestRequestTypeDef = TypedDict(
    "ListResponseHeadersPoliciesRequestRequestTypeDef",
    {
        "Type": NotRequired[ResponseHeadersPolicyTypeType],
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[str],
    },
)
ListStreamingDistributionsRequestRequestTypeDef = TypedDict(
    "ListStreamingDistributionsRequestRequestTypeDef",
    {
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[str],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "Resource": str,
    },
)
RealtimeMetricsSubscriptionConfigTypeDef = TypedDict(
    "RealtimeMetricsSubscriptionConfigTypeDef",
    {
        "RealtimeMetricsSubscriptionStatus": RealtimeMetricsSubscriptionStatusType,
    },
)
OriginAccessControlSummaryTypeDef = TypedDict(
    "OriginAccessControlSummaryTypeDef",
    {
        "Id": str,
        "Description": str,
        "Name": str,
        "SigningProtocol": Literal["sigv4"],
        "SigningBehavior": OriginAccessControlSigningBehaviorsType,
        "OriginAccessControlOriginType": OriginAccessControlOriginTypesType,
    },
)
StatusCodesTypeDef = TypedDict(
    "StatusCodesTypeDef",
    {
        "Quantity": int,
        "Items": List[int],
    },
)
OriginGroupMemberTypeDef = TypedDict(
    "OriginGroupMemberTypeDef",
    {
        "OriginId": str,
    },
)
OriginShieldTypeDef = TypedDict(
    "OriginShieldTypeDef",
    {
        "Enabled": bool,
        "OriginShieldRegion": NotRequired[str],
    },
)
S3OriginConfigTypeDef = TypedDict(
    "S3OriginConfigTypeDef",
    {
        "OriginAccessIdentity": str,
    },
)
PublicKeySummaryTypeDef = TypedDict(
    "PublicKeySummaryTypeDef",
    {
        "Id": str,
        "Name": str,
        "CreatedTime": datetime,
        "EncodedKey": str,
        "Comment": NotRequired[str],
    },
)
PublishFunctionRequestRequestTypeDef = TypedDict(
    "PublishFunctionRequestRequestTypeDef",
    {
        "Name": str,
        "IfMatch": str,
    },
)
QueryArgProfileTypeDef = TypedDict(
    "QueryArgProfileTypeDef",
    {
        "QueryArg": str,
        "ProfileId": str,
    },
)
ResponseHeadersPolicyAccessControlAllowHeadersTypeDef = TypedDict(
    "ResponseHeadersPolicyAccessControlAllowHeadersTypeDef",
    {
        "Quantity": int,
        "Items": Sequence[str],
    },
)
ResponseHeadersPolicyAccessControlAllowMethodsTypeDef = TypedDict(
    "ResponseHeadersPolicyAccessControlAllowMethodsTypeDef",
    {
        "Quantity": int,
        "Items": Sequence[ResponseHeadersPolicyAccessControlAllowMethodsValuesType],
    },
)
ResponseHeadersPolicyAccessControlAllowOriginsTypeDef = TypedDict(
    "ResponseHeadersPolicyAccessControlAllowOriginsTypeDef",
    {
        "Quantity": int,
        "Items": Sequence[str],
    },
)
ResponseHeadersPolicyAccessControlExposeHeadersTypeDef = TypedDict(
    "ResponseHeadersPolicyAccessControlExposeHeadersTypeDef",
    {
        "Quantity": int,
        "Items": NotRequired[Sequence[str]],
    },
)
ResponseHeadersPolicyServerTimingHeadersConfigTypeDef = TypedDict(
    "ResponseHeadersPolicyServerTimingHeadersConfigTypeDef",
    {
        "Enabled": bool,
        "SamplingRate": NotRequired[float],
    },
)
ResponseHeadersPolicyContentSecurityPolicyTypeDef = TypedDict(
    "ResponseHeadersPolicyContentSecurityPolicyTypeDef",
    {
        "Override": bool,
        "ContentSecurityPolicy": str,
    },
)
ResponseHeadersPolicyContentTypeOptionsTypeDef = TypedDict(
    "ResponseHeadersPolicyContentTypeOptionsTypeDef",
    {
        "Override": bool,
    },
)
ResponseHeadersPolicyCustomHeaderTypeDef = TypedDict(
    "ResponseHeadersPolicyCustomHeaderTypeDef",
    {
        "Header": str,
        "Value": str,
        "Override": bool,
    },
)
ResponseHeadersPolicyFrameOptionsTypeDef = TypedDict(
    "ResponseHeadersPolicyFrameOptionsTypeDef",
    {
        "Override": bool,
        "FrameOption": FrameOptionsListType,
    },
)
ResponseHeadersPolicyReferrerPolicyTypeDef = TypedDict(
    "ResponseHeadersPolicyReferrerPolicyTypeDef",
    {
        "Override": bool,
        "ReferrerPolicy": ReferrerPolicyListType,
    },
)
ResponseHeadersPolicyRemoveHeaderTypeDef = TypedDict(
    "ResponseHeadersPolicyRemoveHeaderTypeDef",
    {
        "Header": str,
    },
)
ResponseHeadersPolicyStrictTransportSecurityTypeDef = TypedDict(
    "ResponseHeadersPolicyStrictTransportSecurityTypeDef",
    {
        "Override": bool,
        "AccessControlMaxAgeSec": int,
        "IncludeSubdomains": NotRequired[bool],
        "Preload": NotRequired[bool],
    },
)
ResponseHeadersPolicyXSSProtectionTypeDef = TypedDict(
    "ResponseHeadersPolicyXSSProtectionTypeDef",
    {
        "Override": bool,
        "Protection": bool,
        "ModeBlock": NotRequired[bool],
        "ReportUri": NotRequired[str],
    },
)
S3OriginTypeDef = TypedDict(
    "S3OriginTypeDef",
    {
        "DomainName": str,
        "OriginAccessIdentity": str,
    },
)
StreamingLoggingConfigTypeDef = TypedDict(
    "StreamingLoggingConfigTypeDef",
    {
        "Enabled": bool,
        "Bucket": str,
        "Prefix": str,
    },
)
TagKeysTypeDef = TypedDict(
    "TagKeysTypeDef",
    {
        "Items": NotRequired[Sequence[str]],
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": NotRequired[str],
    },
)
UpdateDistributionWithStagingConfigRequestRequestTypeDef = TypedDict(
    "UpdateDistributionWithStagingConfigRequestRequestTypeDef",
    {
        "Id": str,
        "StagingDistributionId": NotRequired[str],
        "IfMatch": NotRequired[str],
    },
)
UpdateKeyValueStoreRequestRequestTypeDef = TypedDict(
    "UpdateKeyValueStoreRequestRequestTypeDef",
    {
        "Name": str,
        "Comment": str,
        "IfMatch": str,
    },
)
AllowedMethodsTypeDef = TypedDict(
    "AllowedMethodsTypeDef",
    {
        "Quantity": int,
        "Items": List[MethodType],
        "CachedMethods": NotRequired[CachedMethodsTypeDef],
    },
)
TestFunctionRequestRequestTypeDef = TypedDict(
    "TestFunctionRequestRequestTypeDef",
    {
        "Name": str,
        "IfMatch": str,
        "EventObject": BlobTypeDef,
        "Stage": NotRequired[FunctionStageType],
    },
)
CachePolicyCookiesConfigTypeDef = TypedDict(
    "CachePolicyCookiesConfigTypeDef",
    {
        "CookieBehavior": CachePolicyCookieBehaviorType,
        "Cookies": NotRequired[CookieNamesTypeDef],
    },
)
CookiePreferenceTypeDef = TypedDict(
    "CookiePreferenceTypeDef",
    {
        "Forward": ItemSelectionType,
        "WhitelistedNames": NotRequired[CookieNamesTypeDef],
    },
)
OriginRequestPolicyCookiesConfigTypeDef = TypedDict(
    "OriginRequestPolicyCookiesConfigTypeDef",
    {
        "CookieBehavior": OriginRequestPolicyCookieBehaviorType,
        "Cookies": NotRequired[CookieNamesTypeDef],
    },
)
CachePolicyHeadersConfigTypeDef = TypedDict(
    "CachePolicyHeadersConfigTypeDef",
    {
        "HeaderBehavior": CachePolicyHeaderBehaviorType,
        "Headers": NotRequired[HeadersTypeDef],
    },
)
OriginRequestPolicyHeadersConfigTypeDef = TypedDict(
    "OriginRequestPolicyHeadersConfigTypeDef",
    {
        "HeaderBehavior": OriginRequestPolicyHeaderBehaviorType,
        "Headers": NotRequired[HeadersTypeDef],
    },
)
CachePolicyQueryStringsConfigTypeDef = TypedDict(
    "CachePolicyQueryStringsConfigTypeDef",
    {
        "QueryStringBehavior": CachePolicyQueryStringBehaviorType,
        "QueryStrings": NotRequired[QueryStringNamesTypeDef],
    },
)
OriginRequestPolicyQueryStringsConfigTypeDef = TypedDict(
    "OriginRequestPolicyQueryStringsConfigTypeDef",
    {
        "QueryStringBehavior": OriginRequestPolicyQueryStringBehaviorType,
        "QueryStrings": NotRequired[QueryStringNamesTypeDef],
    },
)
CloudFrontOriginAccessIdentityTypeDef = TypedDict(
    "CloudFrontOriginAccessIdentityTypeDef",
    {
        "Id": str,
        "S3CanonicalUserId": str,
        "CloudFrontOriginAccessIdentityConfig": NotRequired[
            CloudFrontOriginAccessIdentityConfigTypeDef
        ],
    },
)
CreateCloudFrontOriginAccessIdentityRequestRequestTypeDef = TypedDict(
    "CreateCloudFrontOriginAccessIdentityRequestRequestTypeDef",
    {
        "CloudFrontOriginAccessIdentityConfig": CloudFrontOriginAccessIdentityConfigTypeDef,
    },
)
UpdateCloudFrontOriginAccessIdentityRequestRequestTypeDef = TypedDict(
    "UpdateCloudFrontOriginAccessIdentityRequestRequestTypeDef",
    {
        "CloudFrontOriginAccessIdentityConfig": CloudFrontOriginAccessIdentityConfigTypeDef,
        "Id": str,
        "IfMatch": NotRequired[str],
    },
)
CloudFrontOriginAccessIdentityListTypeDef = TypedDict(
    "CloudFrontOriginAccessIdentityListTypeDef",
    {
        "Marker": str,
        "MaxItems": int,
        "IsTruncated": bool,
        "Quantity": int,
        "NextMarker": NotRequired[str],
        "Items": NotRequired[List[CloudFrontOriginAccessIdentitySummaryTypeDef]],
    },
)
ConflictingAliasesListTypeDef = TypedDict(
    "ConflictingAliasesListTypeDef",
    {
        "NextMarker": NotRequired[str],
        "MaxItems": NotRequired[int],
        "Quantity": NotRequired[int],
        "Items": NotRequired[List[ConflictingAliasTypeDef]],
    },
)
ContentTypeProfilesTypeDef = TypedDict(
    "ContentTypeProfilesTypeDef",
    {
        "Quantity": int,
        "Items": NotRequired[Sequence[ContentTypeProfileTypeDef]],
    },
)
ContinuousDeploymentSingleWeightConfigTypeDef = TypedDict(
    "ContinuousDeploymentSingleWeightConfigTypeDef",
    {
        "Weight": float,
        "SessionStickinessConfig": NotRequired[SessionStickinessConfigTypeDef],
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetCloudFrontOriginAccessIdentityConfigResultTypeDef = TypedDict(
    "GetCloudFrontOriginAccessIdentityConfigResultTypeDef",
    {
        "CloudFrontOriginAccessIdentityConfig": CloudFrontOriginAccessIdentityConfigTypeDef,
        "ETag": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetFunctionResultTypeDef = TypedDict(
    "GetFunctionResultTypeDef",
    {
        "FunctionCode": StreamingBody,
        "ETag": str,
        "ContentType": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateKeyGroupRequestRequestTypeDef = TypedDict(
    "CreateKeyGroupRequestRequestTypeDef",
    {
        "KeyGroupConfig": KeyGroupConfigTypeDef,
    },
)
GetKeyGroupConfigResultTypeDef = TypedDict(
    "GetKeyGroupConfigResultTypeDef",
    {
        "KeyGroupConfig": KeyGroupConfigTypeDef,
        "ETag": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
KeyGroupTypeDef = TypedDict(
    "KeyGroupTypeDef",
    {
        "Id": str,
        "LastModifiedTime": datetime,
        "KeyGroupConfig": KeyGroupConfigTypeDef,
    },
)
UpdateKeyGroupRequestRequestTypeDef = TypedDict(
    "UpdateKeyGroupRequestRequestTypeDef",
    {
        "KeyGroupConfig": KeyGroupConfigTypeDef,
        "Id": str,
        "IfMatch": NotRequired[str],
    },
)
CreateKeyValueStoreRequestRequestTypeDef = TypedDict(
    "CreateKeyValueStoreRequestRequestTypeDef",
    {
        "Name": str,
        "Comment": NotRequired[str],
        "ImportSource": NotRequired[ImportSourceTypeDef],
    },
)
CreateKeyValueStoreResultTypeDef = TypedDict(
    "CreateKeyValueStoreResultTypeDef",
    {
        "KeyValueStore": KeyValueStoreTypeDef,
        "ETag": str,
        "Location": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeKeyValueStoreResultTypeDef = TypedDict(
    "DescribeKeyValueStoreResultTypeDef",
    {
        "KeyValueStore": KeyValueStoreTypeDef,
        "ETag": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
KeyValueStoreListTypeDef = TypedDict(
    "KeyValueStoreListTypeDef",
    {
        "MaxItems": int,
        "Quantity": int,
        "NextMarker": NotRequired[str],
        "Items": NotRequired[List[KeyValueStoreTypeDef]],
    },
)
UpdateKeyValueStoreResultTypeDef = TypedDict(
    "UpdateKeyValueStoreResultTypeDef",
    {
        "KeyValueStore": KeyValueStoreTypeDef,
        "ETag": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateOriginAccessControlRequestRequestTypeDef = TypedDict(
    "CreateOriginAccessControlRequestRequestTypeDef",
    {
        "OriginAccessControlConfig": OriginAccessControlConfigTypeDef,
    },
)
GetOriginAccessControlConfigResultTypeDef = TypedDict(
    "GetOriginAccessControlConfigResultTypeDef",
    {
        "OriginAccessControlConfig": OriginAccessControlConfigTypeDef,
        "ETag": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
OriginAccessControlTypeDef = TypedDict(
    "OriginAccessControlTypeDef",
    {
        "Id": str,
        "OriginAccessControlConfig": NotRequired[OriginAccessControlConfigTypeDef],
    },
)
UpdateOriginAccessControlRequestRequestTypeDef = TypedDict(
    "UpdateOriginAccessControlRequestRequestTypeDef",
    {
        "OriginAccessControlConfig": OriginAccessControlConfigTypeDef,
        "Id": str,
        "IfMatch": NotRequired[str],
    },
)
CreatePublicKeyRequestRequestTypeDef = TypedDict(
    "CreatePublicKeyRequestRequestTypeDef",
    {
        "PublicKeyConfig": PublicKeyConfigTypeDef,
    },
)
GetPublicKeyConfigResultTypeDef = TypedDict(
    "GetPublicKeyConfigResultTypeDef",
    {
        "PublicKeyConfig": PublicKeyConfigTypeDef,
        "ETag": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PublicKeyTypeDef = TypedDict(
    "PublicKeyTypeDef",
    {
        "Id": str,
        "CreatedTime": datetime,
        "PublicKeyConfig": PublicKeyConfigTypeDef,
    },
)
UpdatePublicKeyRequestRequestTypeDef = TypedDict(
    "UpdatePublicKeyRequestRequestTypeDef",
    {
        "PublicKeyConfig": PublicKeyConfigTypeDef,
        "Id": str,
        "IfMatch": NotRequired[str],
    },
)
CustomErrorResponsesTypeDef = TypedDict(
    "CustomErrorResponsesTypeDef",
    {
        "Quantity": int,
        "Items": NotRequired[List[CustomErrorResponseTypeDef]],
    },
)
CustomHeadersTypeDef = TypedDict(
    "CustomHeadersTypeDef",
    {
        "Quantity": int,
        "Items": NotRequired[List[OriginCustomHeaderTypeDef]],
    },
)
CustomOriginConfigTypeDef = TypedDict(
    "CustomOriginConfigTypeDef",
    {
        "HTTPPort": int,
        "HTTPSPort": int,
        "OriginProtocolPolicy": OriginProtocolPolicyType,
        "OriginSslProtocols": NotRequired[OriginSslProtocolsTypeDef],
        "OriginReadTimeout": NotRequired[int],
        "OriginKeepaliveTimeout": NotRequired[int],
    },
)
ListDistributionsByCachePolicyIdResultTypeDef = TypedDict(
    "ListDistributionsByCachePolicyIdResultTypeDef",
    {
        "DistributionIdList": DistributionIdListTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListDistributionsByKeyGroupResultTypeDef = TypedDict(
    "ListDistributionsByKeyGroupResultTypeDef",
    {
        "DistributionIdList": DistributionIdListTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListDistributionsByOriginRequestPolicyIdResultTypeDef = TypedDict(
    "ListDistributionsByOriginRequestPolicyIdResultTypeDef",
    {
        "DistributionIdList": DistributionIdListTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListDistributionsByResponseHeadersPolicyIdResultTypeDef = TypedDict(
    "ListDistributionsByResponseHeadersPolicyIdResultTypeDef",
    {
        "DistributionIdList": DistributionIdListTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EncryptionEntityTypeDef = TypedDict(
    "EncryptionEntityTypeDef",
    {
        "PublicKeyId": str,
        "ProviderId": str,
        "FieldPatterns": FieldPatternsTypeDef,
    },
)
EndPointTypeDef = TypedDict(
    "EndPointTypeDef",
    {
        "StreamType": str,
        "KinesisStreamConfig": NotRequired[KinesisStreamConfigTypeDef],
    },
)
FunctionAssociationsTypeDef = TypedDict(
    "FunctionAssociationsTypeDef",
    {
        "Quantity": int,
        "Items": NotRequired[List[FunctionAssociationTypeDef]],
    },
)
RestrictionsTypeDef = TypedDict(
    "RestrictionsTypeDef",
    {
        "GeoRestriction": GeoRestrictionTypeDef,
    },
)
GetDistributionRequestDistributionDeployedWaitTypeDef = TypedDict(
    "GetDistributionRequestDistributionDeployedWaitTypeDef",
    {
        "Id": str,
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
GetInvalidationRequestInvalidationCompletedWaitTypeDef = TypedDict(
    "GetInvalidationRequestInvalidationCompletedWaitTypeDef",
    {
        "DistributionId": str,
        "Id": str,
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
GetStreamingDistributionRequestStreamingDistributionDeployedWaitTypeDef = TypedDict(
    "GetStreamingDistributionRequestStreamingDistributionDeployedWaitTypeDef",
    {
        "Id": str,
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
InvalidationBatchTypeDef = TypedDict(
    "InvalidationBatchTypeDef",
    {
        "Paths": PathsTypeDef,
        "CallerReference": str,
    },
)
InvalidationListTypeDef = TypedDict(
    "InvalidationListTypeDef",
    {
        "Marker": str,
        "MaxItems": int,
        "IsTruncated": bool,
        "Quantity": int,
        "NextMarker": NotRequired[str],
        "Items": NotRequired[List[InvalidationSummaryTypeDef]],
    },
)
KGKeyPairIdsTypeDef = TypedDict(
    "KGKeyPairIdsTypeDef",
    {
        "KeyGroupId": NotRequired[str],
        "KeyPairIds": NotRequired[KeyPairIdsTypeDef],
    },
)
SignerTypeDef = TypedDict(
    "SignerTypeDef",
    {
        "AwsAccountNumber": NotRequired[str],
        "KeyPairIds": NotRequired[KeyPairIdsTypeDef],
    },
)
KeyValueStoreAssociationsTypeDef = TypedDict(
    "KeyValueStoreAssociationsTypeDef",
    {
        "Quantity": int,
        "Items": NotRequired[Sequence[KeyValueStoreAssociationTypeDef]],
    },
)
LambdaFunctionAssociationsTypeDef = TypedDict(
    "LambdaFunctionAssociationsTypeDef",
    {
        "Quantity": int,
        "Items": NotRequired[List[LambdaFunctionAssociationTypeDef]],
    },
)
ListCloudFrontOriginAccessIdentitiesRequestListCloudFrontOriginAccessIdentitiesPaginateTypeDef = TypedDict(
    "ListCloudFrontOriginAccessIdentitiesRequestListCloudFrontOriginAccessIdentitiesPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDistributionsRequestListDistributionsPaginateTypeDef = TypedDict(
    "ListDistributionsRequestListDistributionsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListInvalidationsRequestListInvalidationsPaginateTypeDef = TypedDict(
    "ListInvalidationsRequestListInvalidationsPaginateTypeDef",
    {
        "DistributionId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListKeyValueStoresRequestListKeyValueStoresPaginateTypeDef = TypedDict(
    "ListKeyValueStoresRequestListKeyValueStoresPaginateTypeDef",
    {
        "Status": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListStreamingDistributionsRequestListStreamingDistributionsPaginateTypeDef = TypedDict(
    "ListStreamingDistributionsRequestListStreamingDistributionsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
MonitoringSubscriptionTypeDef = TypedDict(
    "MonitoringSubscriptionTypeDef",
    {
        "RealtimeMetricsSubscriptionConfig": NotRequired[RealtimeMetricsSubscriptionConfigTypeDef],
    },
)
OriginAccessControlListTypeDef = TypedDict(
    "OriginAccessControlListTypeDef",
    {
        "Marker": str,
        "MaxItems": int,
        "IsTruncated": bool,
        "Quantity": int,
        "NextMarker": NotRequired[str],
        "Items": NotRequired[List[OriginAccessControlSummaryTypeDef]],
    },
)
OriginGroupFailoverCriteriaTypeDef = TypedDict(
    "OriginGroupFailoverCriteriaTypeDef",
    {
        "StatusCodes": StatusCodesTypeDef,
    },
)
OriginGroupMembersTypeDef = TypedDict(
    "OriginGroupMembersTypeDef",
    {
        "Quantity": int,
        "Items": List[OriginGroupMemberTypeDef],
    },
)
PublicKeyListTypeDef = TypedDict(
    "PublicKeyListTypeDef",
    {
        "MaxItems": int,
        "Quantity": int,
        "NextMarker": NotRequired[str],
        "Items": NotRequired[List[PublicKeySummaryTypeDef]],
    },
)
QueryArgProfilesTypeDef = TypedDict(
    "QueryArgProfilesTypeDef",
    {
        "Quantity": int,
        "Items": NotRequired[Sequence[QueryArgProfileTypeDef]],
    },
)
ResponseHeadersPolicyCorsConfigTypeDef = TypedDict(
    "ResponseHeadersPolicyCorsConfigTypeDef",
    {
        "AccessControlAllowOrigins": ResponseHeadersPolicyAccessControlAllowOriginsTypeDef,
        "AccessControlAllowHeaders": ResponseHeadersPolicyAccessControlAllowHeadersTypeDef,
        "AccessControlAllowMethods": ResponseHeadersPolicyAccessControlAllowMethodsTypeDef,
        "AccessControlAllowCredentials": bool,
        "OriginOverride": bool,
        "AccessControlExposeHeaders": NotRequired[
            ResponseHeadersPolicyAccessControlExposeHeadersTypeDef
        ],
        "AccessControlMaxAgeSec": NotRequired[int],
    },
)
ResponseHeadersPolicyCustomHeadersConfigTypeDef = TypedDict(
    "ResponseHeadersPolicyCustomHeadersConfigTypeDef",
    {
        "Quantity": int,
        "Items": NotRequired[Sequence[ResponseHeadersPolicyCustomHeaderTypeDef]],
    },
)
ResponseHeadersPolicyRemoveHeadersConfigTypeDef = TypedDict(
    "ResponseHeadersPolicyRemoveHeadersConfigTypeDef",
    {
        "Quantity": int,
        "Items": NotRequired[Sequence[ResponseHeadersPolicyRemoveHeaderTypeDef]],
    },
)
ResponseHeadersPolicySecurityHeadersConfigTypeDef = TypedDict(
    "ResponseHeadersPolicySecurityHeadersConfigTypeDef",
    {
        "XSSProtection": NotRequired[ResponseHeadersPolicyXSSProtectionTypeDef],
        "FrameOptions": NotRequired[ResponseHeadersPolicyFrameOptionsTypeDef],
        "ReferrerPolicy": NotRequired[ResponseHeadersPolicyReferrerPolicyTypeDef],
        "ContentSecurityPolicy": NotRequired[ResponseHeadersPolicyContentSecurityPolicyTypeDef],
        "ContentTypeOptions": NotRequired[ResponseHeadersPolicyContentTypeOptionsTypeDef],
        "StrictTransportSecurity": NotRequired[ResponseHeadersPolicyStrictTransportSecurityTypeDef],
    },
)
StreamingDistributionSummaryTypeDef = TypedDict(
    "StreamingDistributionSummaryTypeDef",
    {
        "Id": str,
        "ARN": str,
        "Status": str,
        "LastModifiedTime": datetime,
        "DomainName": str,
        "S3Origin": S3OriginTypeDef,
        "Aliases": AliasesTypeDef,
        "TrustedSigners": TrustedSignersTypeDef,
        "Comment": str,
        "PriceClass": PriceClassType,
        "Enabled": bool,
    },
)
StreamingDistributionConfigTypeDef = TypedDict(
    "StreamingDistributionConfigTypeDef",
    {
        "CallerReference": str,
        "S3Origin": S3OriginTypeDef,
        "Comment": str,
        "TrustedSigners": TrustedSignersTypeDef,
        "Enabled": bool,
        "Aliases": NotRequired[AliasesTypeDef],
        "Logging": NotRequired[StreamingLoggingConfigTypeDef],
        "PriceClass": NotRequired[PriceClassType],
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "Resource": str,
        "TagKeys": TagKeysTypeDef,
    },
)
TagsTypeDef = TypedDict(
    "TagsTypeDef",
    {
        "Items": NotRequired[Sequence[TagTypeDef]],
    },
)
ForwardedValuesTypeDef = TypedDict(
    "ForwardedValuesTypeDef",
    {
        "QueryString": bool,
        "Cookies": CookiePreferenceTypeDef,
        "Headers": NotRequired[HeadersTypeDef],
        "QueryStringCacheKeys": NotRequired[QueryStringCacheKeysTypeDef],
    },
)
ParametersInCacheKeyAndForwardedToOriginTypeDef = TypedDict(
    "ParametersInCacheKeyAndForwardedToOriginTypeDef",
    {
        "EnableAcceptEncodingGzip": bool,
        "HeadersConfig": CachePolicyHeadersConfigTypeDef,
        "CookiesConfig": CachePolicyCookiesConfigTypeDef,
        "QueryStringsConfig": CachePolicyQueryStringsConfigTypeDef,
        "EnableAcceptEncodingBrotli": NotRequired[bool],
    },
)
OriginRequestPolicyConfigTypeDef = TypedDict(
    "OriginRequestPolicyConfigTypeDef",
    {
        "Name": str,
        "HeadersConfig": OriginRequestPolicyHeadersConfigTypeDef,
        "CookiesConfig": OriginRequestPolicyCookiesConfigTypeDef,
        "QueryStringsConfig": OriginRequestPolicyQueryStringsConfigTypeDef,
        "Comment": NotRequired[str],
    },
)
CreateCloudFrontOriginAccessIdentityResultTypeDef = TypedDict(
    "CreateCloudFrontOriginAccessIdentityResultTypeDef",
    {
        "CloudFrontOriginAccessIdentity": CloudFrontOriginAccessIdentityTypeDef,
        "Location": str,
        "ETag": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetCloudFrontOriginAccessIdentityResultTypeDef = TypedDict(
    "GetCloudFrontOriginAccessIdentityResultTypeDef",
    {
        "CloudFrontOriginAccessIdentity": CloudFrontOriginAccessIdentityTypeDef,
        "ETag": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateCloudFrontOriginAccessIdentityResultTypeDef = TypedDict(
    "UpdateCloudFrontOriginAccessIdentityResultTypeDef",
    {
        "CloudFrontOriginAccessIdentity": CloudFrontOriginAccessIdentityTypeDef,
        "ETag": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListCloudFrontOriginAccessIdentitiesResultTypeDef = TypedDict(
    "ListCloudFrontOriginAccessIdentitiesResultTypeDef",
    {
        "CloudFrontOriginAccessIdentityList": CloudFrontOriginAccessIdentityListTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListConflictingAliasesResultTypeDef = TypedDict(
    "ListConflictingAliasesResultTypeDef",
    {
        "ConflictingAliasesList": ConflictingAliasesListTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ContentTypeProfileConfigTypeDef = TypedDict(
    "ContentTypeProfileConfigTypeDef",
    {
        "ForwardWhenContentTypeIsUnknown": bool,
        "ContentTypeProfiles": NotRequired[ContentTypeProfilesTypeDef],
    },
)
TrafficConfigTypeDef = TypedDict(
    "TrafficConfigTypeDef",
    {
        "Type": ContinuousDeploymentPolicyTypeType,
        "SingleWeightConfig": NotRequired[ContinuousDeploymentSingleWeightConfigTypeDef],
        "SingleHeaderConfig": NotRequired[ContinuousDeploymentSingleHeaderConfigTypeDef],
    },
)
CreateKeyGroupResultTypeDef = TypedDict(
    "CreateKeyGroupResultTypeDef",
    {
        "KeyGroup": KeyGroupTypeDef,
        "Location": str,
        "ETag": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetKeyGroupResultTypeDef = TypedDict(
    "GetKeyGroupResultTypeDef",
    {
        "KeyGroup": KeyGroupTypeDef,
        "ETag": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
KeyGroupSummaryTypeDef = TypedDict(
    "KeyGroupSummaryTypeDef",
    {
        "KeyGroup": KeyGroupTypeDef,
    },
)
UpdateKeyGroupResultTypeDef = TypedDict(
    "UpdateKeyGroupResultTypeDef",
    {
        "KeyGroup": KeyGroupTypeDef,
        "ETag": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListKeyValueStoresResultTypeDef = TypedDict(
    "ListKeyValueStoresResultTypeDef",
    {
        "KeyValueStoreList": KeyValueStoreListTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateOriginAccessControlResultTypeDef = TypedDict(
    "CreateOriginAccessControlResultTypeDef",
    {
        "OriginAccessControl": OriginAccessControlTypeDef,
        "Location": str,
        "ETag": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetOriginAccessControlResultTypeDef = TypedDict(
    "GetOriginAccessControlResultTypeDef",
    {
        "OriginAccessControl": OriginAccessControlTypeDef,
        "ETag": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateOriginAccessControlResultTypeDef = TypedDict(
    "UpdateOriginAccessControlResultTypeDef",
    {
        "OriginAccessControl": OriginAccessControlTypeDef,
        "ETag": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreatePublicKeyResultTypeDef = TypedDict(
    "CreatePublicKeyResultTypeDef",
    {
        "PublicKey": PublicKeyTypeDef,
        "Location": str,
        "ETag": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetPublicKeyResultTypeDef = TypedDict(
    "GetPublicKeyResultTypeDef",
    {
        "PublicKey": PublicKeyTypeDef,
        "ETag": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdatePublicKeyResultTypeDef = TypedDict(
    "UpdatePublicKeyResultTypeDef",
    {
        "PublicKey": PublicKeyTypeDef,
        "ETag": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
OriginTypeDef = TypedDict(
    "OriginTypeDef",
    {
        "Id": str,
        "DomainName": str,
        "OriginPath": NotRequired[str],
        "CustomHeaders": NotRequired[CustomHeadersTypeDef],
        "S3OriginConfig": NotRequired[S3OriginConfigTypeDef],
        "CustomOriginConfig": NotRequired[CustomOriginConfigTypeDef],
        "ConnectionAttempts": NotRequired[int],
        "ConnectionTimeout": NotRequired[int],
        "OriginShield": NotRequired[OriginShieldTypeDef],
        "OriginAccessControlId": NotRequired[str],
    },
)
EncryptionEntitiesTypeDef = TypedDict(
    "EncryptionEntitiesTypeDef",
    {
        "Quantity": int,
        "Items": NotRequired[Sequence[EncryptionEntityTypeDef]],
    },
)
CreateRealtimeLogConfigRequestRequestTypeDef = TypedDict(
    "CreateRealtimeLogConfigRequestRequestTypeDef",
    {
        "EndPoints": Sequence[EndPointTypeDef],
        "Fields": Sequence[str],
        "Name": str,
        "SamplingRate": int,
    },
)
RealtimeLogConfigTypeDef = TypedDict(
    "RealtimeLogConfigTypeDef",
    {
        "ARN": str,
        "Name": str,
        "SamplingRate": int,
        "EndPoints": List[EndPointTypeDef],
        "Fields": List[str],
    },
)
UpdateRealtimeLogConfigRequestRequestTypeDef = TypedDict(
    "UpdateRealtimeLogConfigRequestRequestTypeDef",
    {
        "EndPoints": NotRequired[Sequence[EndPointTypeDef]],
        "Fields": NotRequired[Sequence[str]],
        "Name": NotRequired[str],
        "ARN": NotRequired[str],
        "SamplingRate": NotRequired[int],
    },
)
CreateInvalidationRequestRequestTypeDef = TypedDict(
    "CreateInvalidationRequestRequestTypeDef",
    {
        "DistributionId": str,
        "InvalidationBatch": InvalidationBatchTypeDef,
    },
)
InvalidationTypeDef = TypedDict(
    "InvalidationTypeDef",
    {
        "Id": str,
        "Status": str,
        "CreateTime": datetime,
        "InvalidationBatch": InvalidationBatchTypeDef,
    },
)
ListInvalidationsResultTypeDef = TypedDict(
    "ListInvalidationsResultTypeDef",
    {
        "InvalidationList": InvalidationListTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ActiveTrustedKeyGroupsTypeDef = TypedDict(
    "ActiveTrustedKeyGroupsTypeDef",
    {
        "Enabled": bool,
        "Quantity": int,
        "Items": NotRequired[List[KGKeyPairIdsTypeDef]],
    },
)
ActiveTrustedSignersTypeDef = TypedDict(
    "ActiveTrustedSignersTypeDef",
    {
        "Enabled": bool,
        "Quantity": int,
        "Items": NotRequired[List[SignerTypeDef]],
    },
)
FunctionConfigTypeDef = TypedDict(
    "FunctionConfigTypeDef",
    {
        "Comment": str,
        "Runtime": FunctionRuntimeType,
        "KeyValueStoreAssociations": NotRequired[KeyValueStoreAssociationsTypeDef],
    },
)
CreateMonitoringSubscriptionRequestRequestTypeDef = TypedDict(
    "CreateMonitoringSubscriptionRequestRequestTypeDef",
    {
        "DistributionId": str,
        "MonitoringSubscription": MonitoringSubscriptionTypeDef,
    },
)
CreateMonitoringSubscriptionResultTypeDef = TypedDict(
    "CreateMonitoringSubscriptionResultTypeDef",
    {
        "MonitoringSubscription": MonitoringSubscriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetMonitoringSubscriptionResultTypeDef = TypedDict(
    "GetMonitoringSubscriptionResultTypeDef",
    {
        "MonitoringSubscription": MonitoringSubscriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListOriginAccessControlsResultTypeDef = TypedDict(
    "ListOriginAccessControlsResultTypeDef",
    {
        "OriginAccessControlList": OriginAccessControlListTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
OriginGroupTypeDef = TypedDict(
    "OriginGroupTypeDef",
    {
        "Id": str,
        "FailoverCriteria": OriginGroupFailoverCriteriaTypeDef,
        "Members": OriginGroupMembersTypeDef,
    },
)
ListPublicKeysResultTypeDef = TypedDict(
    "ListPublicKeysResultTypeDef",
    {
        "PublicKeyList": PublicKeyListTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
QueryArgProfileConfigTypeDef = TypedDict(
    "QueryArgProfileConfigTypeDef",
    {
        "ForwardWhenQueryArgProfileIsUnknown": bool,
        "QueryArgProfiles": NotRequired[QueryArgProfilesTypeDef],
    },
)
ResponseHeadersPolicyConfigTypeDef = TypedDict(
    "ResponseHeadersPolicyConfigTypeDef",
    {
        "Name": str,
        "Comment": NotRequired[str],
        "CorsConfig": NotRequired[ResponseHeadersPolicyCorsConfigTypeDef],
        "SecurityHeadersConfig": NotRequired[ResponseHeadersPolicySecurityHeadersConfigTypeDef],
        "ServerTimingHeadersConfig": NotRequired[
            ResponseHeadersPolicyServerTimingHeadersConfigTypeDef
        ],
        "CustomHeadersConfig": NotRequired[ResponseHeadersPolicyCustomHeadersConfigTypeDef],
        "RemoveHeadersConfig": NotRequired[ResponseHeadersPolicyRemoveHeadersConfigTypeDef],
    },
)
StreamingDistributionListTypeDef = TypedDict(
    "StreamingDistributionListTypeDef",
    {
        "Marker": str,
        "MaxItems": int,
        "IsTruncated": bool,
        "Quantity": int,
        "NextMarker": NotRequired[str],
        "Items": NotRequired[List[StreamingDistributionSummaryTypeDef]],
    },
)
CreateStreamingDistributionRequestRequestTypeDef = TypedDict(
    "CreateStreamingDistributionRequestRequestTypeDef",
    {
        "StreamingDistributionConfig": StreamingDistributionConfigTypeDef,
    },
)
GetStreamingDistributionConfigResultTypeDef = TypedDict(
    "GetStreamingDistributionConfigResultTypeDef",
    {
        "StreamingDistributionConfig": StreamingDistributionConfigTypeDef,
        "ETag": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateStreamingDistributionRequestRequestTypeDef = TypedDict(
    "UpdateStreamingDistributionRequestRequestTypeDef",
    {
        "StreamingDistributionConfig": StreamingDistributionConfigTypeDef,
        "Id": str,
        "IfMatch": NotRequired[str],
    },
)
ListTagsForResourceResultTypeDef = TypedDict(
    "ListTagsForResourceResultTypeDef",
    {
        "Tags": TagsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StreamingDistributionConfigWithTagsTypeDef = TypedDict(
    "StreamingDistributionConfigWithTagsTypeDef",
    {
        "StreamingDistributionConfig": StreamingDistributionConfigTypeDef,
        "Tags": TagsTypeDef,
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "Resource": str,
        "Tags": TagsTypeDef,
    },
)
CacheBehaviorTypeDef = TypedDict(
    "CacheBehaviorTypeDef",
    {
        "PathPattern": str,
        "TargetOriginId": str,
        "ViewerProtocolPolicy": ViewerProtocolPolicyType,
        "TrustedSigners": NotRequired[TrustedSignersTypeDef],
        "TrustedKeyGroups": NotRequired[TrustedKeyGroupsTypeDef],
        "AllowedMethods": NotRequired[AllowedMethodsTypeDef],
        "SmoothStreaming": NotRequired[bool],
        "Compress": NotRequired[bool],
        "LambdaFunctionAssociations": NotRequired[LambdaFunctionAssociationsTypeDef],
        "FunctionAssociations": NotRequired[FunctionAssociationsTypeDef],
        "FieldLevelEncryptionId": NotRequired[str],
        "RealtimeLogConfigArn": NotRequired[str],
        "CachePolicyId": NotRequired[str],
        "OriginRequestPolicyId": NotRequired[str],
        "ResponseHeadersPolicyId": NotRequired[str],
        "ForwardedValues": NotRequired[ForwardedValuesTypeDef],
        "MinTTL": NotRequired[int],
        "DefaultTTL": NotRequired[int],
        "MaxTTL": NotRequired[int],
    },
)
DefaultCacheBehaviorTypeDef = TypedDict(
    "DefaultCacheBehaviorTypeDef",
    {
        "TargetOriginId": str,
        "ViewerProtocolPolicy": ViewerProtocolPolicyType,
        "TrustedSigners": NotRequired[TrustedSignersTypeDef],
        "TrustedKeyGroups": NotRequired[TrustedKeyGroupsTypeDef],
        "AllowedMethods": NotRequired[AllowedMethodsTypeDef],
        "SmoothStreaming": NotRequired[bool],
        "Compress": NotRequired[bool],
        "LambdaFunctionAssociations": NotRequired[LambdaFunctionAssociationsTypeDef],
        "FunctionAssociations": NotRequired[FunctionAssociationsTypeDef],
        "FieldLevelEncryptionId": NotRequired[str],
        "RealtimeLogConfigArn": NotRequired[str],
        "CachePolicyId": NotRequired[str],
        "OriginRequestPolicyId": NotRequired[str],
        "ResponseHeadersPolicyId": NotRequired[str],
        "ForwardedValues": NotRequired[ForwardedValuesTypeDef],
        "MinTTL": NotRequired[int],
        "DefaultTTL": NotRequired[int],
        "MaxTTL": NotRequired[int],
    },
)
CachePolicyConfigTypeDef = TypedDict(
    "CachePolicyConfigTypeDef",
    {
        "Name": str,
        "MinTTL": int,
        "Comment": NotRequired[str],
        "DefaultTTL": NotRequired[int],
        "MaxTTL": NotRequired[int],
        "ParametersInCacheKeyAndForwardedToOrigin": NotRequired[
            ParametersInCacheKeyAndForwardedToOriginTypeDef
        ],
    },
)
CreateOriginRequestPolicyRequestRequestTypeDef = TypedDict(
    "CreateOriginRequestPolicyRequestRequestTypeDef",
    {
        "OriginRequestPolicyConfig": OriginRequestPolicyConfigTypeDef,
    },
)
GetOriginRequestPolicyConfigResultTypeDef = TypedDict(
    "GetOriginRequestPolicyConfigResultTypeDef",
    {
        "OriginRequestPolicyConfig": OriginRequestPolicyConfigTypeDef,
        "ETag": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
OriginRequestPolicyTypeDef = TypedDict(
    "OriginRequestPolicyTypeDef",
    {
        "Id": str,
        "LastModifiedTime": datetime,
        "OriginRequestPolicyConfig": OriginRequestPolicyConfigTypeDef,
    },
)
UpdateOriginRequestPolicyRequestRequestTypeDef = TypedDict(
    "UpdateOriginRequestPolicyRequestRequestTypeDef",
    {
        "OriginRequestPolicyConfig": OriginRequestPolicyConfigTypeDef,
        "Id": str,
        "IfMatch": NotRequired[str],
    },
)
ContinuousDeploymentPolicyConfigTypeDef = TypedDict(
    "ContinuousDeploymentPolicyConfigTypeDef",
    {
        "StagingDistributionDnsNames": StagingDistributionDnsNamesTypeDef,
        "Enabled": bool,
        "TrafficConfig": NotRequired[TrafficConfigTypeDef],
    },
)
KeyGroupListTypeDef = TypedDict(
    "KeyGroupListTypeDef",
    {
        "MaxItems": int,
        "Quantity": int,
        "NextMarker": NotRequired[str],
        "Items": NotRequired[List[KeyGroupSummaryTypeDef]],
    },
)
OriginsTypeDef = TypedDict(
    "OriginsTypeDef",
    {
        "Quantity": int,
        "Items": List[OriginTypeDef],
    },
)
FieldLevelEncryptionProfileConfigTypeDef = TypedDict(
    "FieldLevelEncryptionProfileConfigTypeDef",
    {
        "Name": str,
        "CallerReference": str,
        "EncryptionEntities": EncryptionEntitiesTypeDef,
        "Comment": NotRequired[str],
    },
)
FieldLevelEncryptionProfileSummaryTypeDef = TypedDict(
    "FieldLevelEncryptionProfileSummaryTypeDef",
    {
        "Id": str,
        "LastModifiedTime": datetime,
        "Name": str,
        "EncryptionEntities": EncryptionEntitiesTypeDef,
        "Comment": NotRequired[str],
    },
)
CreateRealtimeLogConfigResultTypeDef = TypedDict(
    "CreateRealtimeLogConfigResultTypeDef",
    {
        "RealtimeLogConfig": RealtimeLogConfigTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetRealtimeLogConfigResultTypeDef = TypedDict(
    "GetRealtimeLogConfigResultTypeDef",
    {
        "RealtimeLogConfig": RealtimeLogConfigTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RealtimeLogConfigsTypeDef = TypedDict(
    "RealtimeLogConfigsTypeDef",
    {
        "MaxItems": int,
        "IsTruncated": bool,
        "Marker": str,
        "Items": NotRequired[List[RealtimeLogConfigTypeDef]],
        "NextMarker": NotRequired[str],
    },
)
UpdateRealtimeLogConfigResultTypeDef = TypedDict(
    "UpdateRealtimeLogConfigResultTypeDef",
    {
        "RealtimeLogConfig": RealtimeLogConfigTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateInvalidationResultTypeDef = TypedDict(
    "CreateInvalidationResultTypeDef",
    {
        "Location": str,
        "Invalidation": InvalidationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetInvalidationResultTypeDef = TypedDict(
    "GetInvalidationResultTypeDef",
    {
        "Invalidation": InvalidationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StreamingDistributionTypeDef = TypedDict(
    "StreamingDistributionTypeDef",
    {
        "Id": str,
        "ARN": str,
        "Status": str,
        "DomainName": str,
        "ActiveTrustedSigners": ActiveTrustedSignersTypeDef,
        "StreamingDistributionConfig": StreamingDistributionConfigTypeDef,
        "LastModifiedTime": NotRequired[datetime],
    },
)
CreateFunctionRequestRequestTypeDef = TypedDict(
    "CreateFunctionRequestRequestTypeDef",
    {
        "Name": str,
        "FunctionConfig": FunctionConfigTypeDef,
        "FunctionCode": BlobTypeDef,
    },
)
FunctionSummaryTypeDef = TypedDict(
    "FunctionSummaryTypeDef",
    {
        "Name": str,
        "FunctionConfig": FunctionConfigTypeDef,
        "FunctionMetadata": FunctionMetadataTypeDef,
        "Status": NotRequired[str],
    },
)
UpdateFunctionRequestRequestTypeDef = TypedDict(
    "UpdateFunctionRequestRequestTypeDef",
    {
        "Name": str,
        "IfMatch": str,
        "FunctionConfig": FunctionConfigTypeDef,
        "FunctionCode": BlobTypeDef,
    },
)
OriginGroupsTypeDef = TypedDict(
    "OriginGroupsTypeDef",
    {
        "Quantity": int,
        "Items": NotRequired[List[OriginGroupTypeDef]],
    },
)
FieldLevelEncryptionConfigTypeDef = TypedDict(
    "FieldLevelEncryptionConfigTypeDef",
    {
        "CallerReference": str,
        "Comment": NotRequired[str],
        "QueryArgProfileConfig": NotRequired[QueryArgProfileConfigTypeDef],
        "ContentTypeProfileConfig": NotRequired[ContentTypeProfileConfigTypeDef],
    },
)
FieldLevelEncryptionSummaryTypeDef = TypedDict(
    "FieldLevelEncryptionSummaryTypeDef",
    {
        "Id": str,
        "LastModifiedTime": datetime,
        "Comment": NotRequired[str],
        "QueryArgProfileConfig": NotRequired[QueryArgProfileConfigTypeDef],
        "ContentTypeProfileConfig": NotRequired[ContentTypeProfileConfigTypeDef],
    },
)
CreateResponseHeadersPolicyRequestRequestTypeDef = TypedDict(
    "CreateResponseHeadersPolicyRequestRequestTypeDef",
    {
        "ResponseHeadersPolicyConfig": ResponseHeadersPolicyConfigTypeDef,
    },
)
GetResponseHeadersPolicyConfigResultTypeDef = TypedDict(
    "GetResponseHeadersPolicyConfigResultTypeDef",
    {
        "ResponseHeadersPolicyConfig": ResponseHeadersPolicyConfigTypeDef,
        "ETag": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ResponseHeadersPolicyTypeDef = TypedDict(
    "ResponseHeadersPolicyTypeDef",
    {
        "Id": str,
        "LastModifiedTime": datetime,
        "ResponseHeadersPolicyConfig": ResponseHeadersPolicyConfigTypeDef,
    },
)
UpdateResponseHeadersPolicyRequestRequestTypeDef = TypedDict(
    "UpdateResponseHeadersPolicyRequestRequestTypeDef",
    {
        "ResponseHeadersPolicyConfig": ResponseHeadersPolicyConfigTypeDef,
        "Id": str,
        "IfMatch": NotRequired[str],
    },
)
ListStreamingDistributionsResultTypeDef = TypedDict(
    "ListStreamingDistributionsResultTypeDef",
    {
        "StreamingDistributionList": StreamingDistributionListTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateStreamingDistributionWithTagsRequestRequestTypeDef = TypedDict(
    "CreateStreamingDistributionWithTagsRequestRequestTypeDef",
    {
        "StreamingDistributionConfigWithTags": StreamingDistributionConfigWithTagsTypeDef,
    },
)
CacheBehaviorsTypeDef = TypedDict(
    "CacheBehaviorsTypeDef",
    {
        "Quantity": int,
        "Items": NotRequired[List[CacheBehaviorTypeDef]],
    },
)
CachePolicyTypeDef = TypedDict(
    "CachePolicyTypeDef",
    {
        "Id": str,
        "LastModifiedTime": datetime,
        "CachePolicyConfig": CachePolicyConfigTypeDef,
    },
)
CreateCachePolicyRequestRequestTypeDef = TypedDict(
    "CreateCachePolicyRequestRequestTypeDef",
    {
        "CachePolicyConfig": CachePolicyConfigTypeDef,
    },
)
GetCachePolicyConfigResultTypeDef = TypedDict(
    "GetCachePolicyConfigResultTypeDef",
    {
        "CachePolicyConfig": CachePolicyConfigTypeDef,
        "ETag": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateCachePolicyRequestRequestTypeDef = TypedDict(
    "UpdateCachePolicyRequestRequestTypeDef",
    {
        "CachePolicyConfig": CachePolicyConfigTypeDef,
        "Id": str,
        "IfMatch": NotRequired[str],
    },
)
CreateOriginRequestPolicyResultTypeDef = TypedDict(
    "CreateOriginRequestPolicyResultTypeDef",
    {
        "OriginRequestPolicy": OriginRequestPolicyTypeDef,
        "Location": str,
        "ETag": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetOriginRequestPolicyResultTypeDef = TypedDict(
    "GetOriginRequestPolicyResultTypeDef",
    {
        "OriginRequestPolicy": OriginRequestPolicyTypeDef,
        "ETag": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
OriginRequestPolicySummaryTypeDef = TypedDict(
    "OriginRequestPolicySummaryTypeDef",
    {
        "Type": OriginRequestPolicyTypeType,
        "OriginRequestPolicy": OriginRequestPolicyTypeDef,
    },
)
UpdateOriginRequestPolicyResultTypeDef = TypedDict(
    "UpdateOriginRequestPolicyResultTypeDef",
    {
        "OriginRequestPolicy": OriginRequestPolicyTypeDef,
        "ETag": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ContinuousDeploymentPolicyTypeDef = TypedDict(
    "ContinuousDeploymentPolicyTypeDef",
    {
        "Id": str,
        "LastModifiedTime": datetime,
        "ContinuousDeploymentPolicyConfig": ContinuousDeploymentPolicyConfigTypeDef,
    },
)
CreateContinuousDeploymentPolicyRequestRequestTypeDef = TypedDict(
    "CreateContinuousDeploymentPolicyRequestRequestTypeDef",
    {
        "ContinuousDeploymentPolicyConfig": ContinuousDeploymentPolicyConfigTypeDef,
    },
)
GetContinuousDeploymentPolicyConfigResultTypeDef = TypedDict(
    "GetContinuousDeploymentPolicyConfigResultTypeDef",
    {
        "ContinuousDeploymentPolicyConfig": ContinuousDeploymentPolicyConfigTypeDef,
        "ETag": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateContinuousDeploymentPolicyRequestRequestTypeDef = TypedDict(
    "UpdateContinuousDeploymentPolicyRequestRequestTypeDef",
    {
        "ContinuousDeploymentPolicyConfig": ContinuousDeploymentPolicyConfigTypeDef,
        "Id": str,
        "IfMatch": NotRequired[str],
    },
)
ListKeyGroupsResultTypeDef = TypedDict(
    "ListKeyGroupsResultTypeDef",
    {
        "KeyGroupList": KeyGroupListTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateFieldLevelEncryptionProfileRequestRequestTypeDef = TypedDict(
    "CreateFieldLevelEncryptionProfileRequestRequestTypeDef",
    {
        "FieldLevelEncryptionProfileConfig": FieldLevelEncryptionProfileConfigTypeDef,
    },
)
FieldLevelEncryptionProfileTypeDef = TypedDict(
    "FieldLevelEncryptionProfileTypeDef",
    {
        "Id": str,
        "LastModifiedTime": datetime,
        "FieldLevelEncryptionProfileConfig": FieldLevelEncryptionProfileConfigTypeDef,
    },
)
GetFieldLevelEncryptionProfileConfigResultTypeDef = TypedDict(
    "GetFieldLevelEncryptionProfileConfigResultTypeDef",
    {
        "FieldLevelEncryptionProfileConfig": FieldLevelEncryptionProfileConfigTypeDef,
        "ETag": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateFieldLevelEncryptionProfileRequestRequestTypeDef = TypedDict(
    "UpdateFieldLevelEncryptionProfileRequestRequestTypeDef",
    {
        "FieldLevelEncryptionProfileConfig": FieldLevelEncryptionProfileConfigTypeDef,
        "Id": str,
        "IfMatch": NotRequired[str],
    },
)
FieldLevelEncryptionProfileListTypeDef = TypedDict(
    "FieldLevelEncryptionProfileListTypeDef",
    {
        "MaxItems": int,
        "Quantity": int,
        "NextMarker": NotRequired[str],
        "Items": NotRequired[List[FieldLevelEncryptionProfileSummaryTypeDef]],
    },
)
ListRealtimeLogConfigsResultTypeDef = TypedDict(
    "ListRealtimeLogConfigsResultTypeDef",
    {
        "RealtimeLogConfigs": RealtimeLogConfigsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateStreamingDistributionResultTypeDef = TypedDict(
    "CreateStreamingDistributionResultTypeDef",
    {
        "StreamingDistribution": StreamingDistributionTypeDef,
        "Location": str,
        "ETag": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateStreamingDistributionWithTagsResultTypeDef = TypedDict(
    "CreateStreamingDistributionWithTagsResultTypeDef",
    {
        "StreamingDistribution": StreamingDistributionTypeDef,
        "Location": str,
        "ETag": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetStreamingDistributionResultTypeDef = TypedDict(
    "GetStreamingDistributionResultTypeDef",
    {
        "StreamingDistribution": StreamingDistributionTypeDef,
        "ETag": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateStreamingDistributionResultTypeDef = TypedDict(
    "UpdateStreamingDistributionResultTypeDef",
    {
        "StreamingDistribution": StreamingDistributionTypeDef,
        "ETag": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateFunctionResultTypeDef = TypedDict(
    "CreateFunctionResultTypeDef",
    {
        "FunctionSummary": FunctionSummaryTypeDef,
        "Location": str,
        "ETag": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeFunctionResultTypeDef = TypedDict(
    "DescribeFunctionResultTypeDef",
    {
        "FunctionSummary": FunctionSummaryTypeDef,
        "ETag": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
FunctionListTypeDef = TypedDict(
    "FunctionListTypeDef",
    {
        "MaxItems": int,
        "Quantity": int,
        "NextMarker": NotRequired[str],
        "Items": NotRequired[List[FunctionSummaryTypeDef]],
    },
)
PublishFunctionResultTypeDef = TypedDict(
    "PublishFunctionResultTypeDef",
    {
        "FunctionSummary": FunctionSummaryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TestResultTypeDef = TypedDict(
    "TestResultTypeDef",
    {
        "FunctionSummary": NotRequired[FunctionSummaryTypeDef],
        "ComputeUtilization": NotRequired[str],
        "FunctionExecutionLogs": NotRequired[List[str]],
        "FunctionErrorMessage": NotRequired[str],
        "FunctionOutput": NotRequired[str],
    },
)
UpdateFunctionResultTypeDef = TypedDict(
    "UpdateFunctionResultTypeDef",
    {
        "FunctionSummary": FunctionSummaryTypeDef,
        "ETag": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateFieldLevelEncryptionConfigRequestRequestTypeDef = TypedDict(
    "CreateFieldLevelEncryptionConfigRequestRequestTypeDef",
    {
        "FieldLevelEncryptionConfig": FieldLevelEncryptionConfigTypeDef,
    },
)
FieldLevelEncryptionTypeDef = TypedDict(
    "FieldLevelEncryptionTypeDef",
    {
        "Id": str,
        "LastModifiedTime": datetime,
        "FieldLevelEncryptionConfig": FieldLevelEncryptionConfigTypeDef,
    },
)
GetFieldLevelEncryptionConfigResultTypeDef = TypedDict(
    "GetFieldLevelEncryptionConfigResultTypeDef",
    {
        "FieldLevelEncryptionConfig": FieldLevelEncryptionConfigTypeDef,
        "ETag": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateFieldLevelEncryptionConfigRequestRequestTypeDef = TypedDict(
    "UpdateFieldLevelEncryptionConfigRequestRequestTypeDef",
    {
        "FieldLevelEncryptionConfig": FieldLevelEncryptionConfigTypeDef,
        "Id": str,
        "IfMatch": NotRequired[str],
    },
)
FieldLevelEncryptionListTypeDef = TypedDict(
    "FieldLevelEncryptionListTypeDef",
    {
        "MaxItems": int,
        "Quantity": int,
        "NextMarker": NotRequired[str],
        "Items": NotRequired[List[FieldLevelEncryptionSummaryTypeDef]],
    },
)
CreateResponseHeadersPolicyResultTypeDef = TypedDict(
    "CreateResponseHeadersPolicyResultTypeDef",
    {
        "ResponseHeadersPolicy": ResponseHeadersPolicyTypeDef,
        "Location": str,
        "ETag": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetResponseHeadersPolicyResultTypeDef = TypedDict(
    "GetResponseHeadersPolicyResultTypeDef",
    {
        "ResponseHeadersPolicy": ResponseHeadersPolicyTypeDef,
        "ETag": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ResponseHeadersPolicySummaryTypeDef = TypedDict(
    "ResponseHeadersPolicySummaryTypeDef",
    {
        "Type": ResponseHeadersPolicyTypeType,
        "ResponseHeadersPolicy": ResponseHeadersPolicyTypeDef,
    },
)
UpdateResponseHeadersPolicyResultTypeDef = TypedDict(
    "UpdateResponseHeadersPolicyResultTypeDef",
    {
        "ResponseHeadersPolicy": ResponseHeadersPolicyTypeDef,
        "ETag": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DistributionConfigTypeDef = TypedDict(
    "DistributionConfigTypeDef",
    {
        "CallerReference": str,
        "Origins": OriginsTypeDef,
        "DefaultCacheBehavior": DefaultCacheBehaviorTypeDef,
        "Comment": str,
        "Enabled": bool,
        "Aliases": NotRequired[AliasesTypeDef],
        "DefaultRootObject": NotRequired[str],
        "OriginGroups": NotRequired[OriginGroupsTypeDef],
        "CacheBehaviors": NotRequired[CacheBehaviorsTypeDef],
        "CustomErrorResponses": NotRequired[CustomErrorResponsesTypeDef],
        "Logging": NotRequired[LoggingConfigTypeDef],
        "PriceClass": NotRequired[PriceClassType],
        "ViewerCertificate": NotRequired[ViewerCertificateTypeDef],
        "Restrictions": NotRequired[RestrictionsTypeDef],
        "WebACLId": NotRequired[str],
        "HttpVersion": NotRequired[HttpVersionType],
        "IsIPV6Enabled": NotRequired[bool],
        "ContinuousDeploymentPolicyId": NotRequired[str],
        "Staging": NotRequired[bool],
    },
)
DistributionSummaryTypeDef = TypedDict(
    "DistributionSummaryTypeDef",
    {
        "Id": str,
        "ARN": str,
        "Status": str,
        "LastModifiedTime": datetime,
        "DomainName": str,
        "Aliases": AliasesTypeDef,
        "Origins": OriginsTypeDef,
        "DefaultCacheBehavior": DefaultCacheBehaviorTypeDef,
        "CacheBehaviors": CacheBehaviorsTypeDef,
        "CustomErrorResponses": CustomErrorResponsesTypeDef,
        "Comment": str,
        "PriceClass": PriceClassType,
        "Enabled": bool,
        "ViewerCertificate": ViewerCertificateTypeDef,
        "Restrictions": RestrictionsTypeDef,
        "WebACLId": str,
        "HttpVersion": HttpVersionType,
        "IsIPV6Enabled": bool,
        "Staging": bool,
        "OriginGroups": NotRequired[OriginGroupsTypeDef],
        "AliasICPRecordals": NotRequired[List[AliasICPRecordalTypeDef]],
    },
)
CachePolicySummaryTypeDef = TypedDict(
    "CachePolicySummaryTypeDef",
    {
        "Type": CachePolicyTypeType,
        "CachePolicy": CachePolicyTypeDef,
    },
)
CreateCachePolicyResultTypeDef = TypedDict(
    "CreateCachePolicyResultTypeDef",
    {
        "CachePolicy": CachePolicyTypeDef,
        "Location": str,
        "ETag": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetCachePolicyResultTypeDef = TypedDict(
    "GetCachePolicyResultTypeDef",
    {
        "CachePolicy": CachePolicyTypeDef,
        "ETag": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateCachePolicyResultTypeDef = TypedDict(
    "UpdateCachePolicyResultTypeDef",
    {
        "CachePolicy": CachePolicyTypeDef,
        "ETag": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
OriginRequestPolicyListTypeDef = TypedDict(
    "OriginRequestPolicyListTypeDef",
    {
        "MaxItems": int,
        "Quantity": int,
        "NextMarker": NotRequired[str],
        "Items": NotRequired[List[OriginRequestPolicySummaryTypeDef]],
    },
)
ContinuousDeploymentPolicySummaryTypeDef = TypedDict(
    "ContinuousDeploymentPolicySummaryTypeDef",
    {
        "ContinuousDeploymentPolicy": ContinuousDeploymentPolicyTypeDef,
    },
)
CreateContinuousDeploymentPolicyResultTypeDef = TypedDict(
    "CreateContinuousDeploymentPolicyResultTypeDef",
    {
        "ContinuousDeploymentPolicy": ContinuousDeploymentPolicyTypeDef,
        "Location": str,
        "ETag": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetContinuousDeploymentPolicyResultTypeDef = TypedDict(
    "GetContinuousDeploymentPolicyResultTypeDef",
    {
        "ContinuousDeploymentPolicy": ContinuousDeploymentPolicyTypeDef,
        "ETag": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateContinuousDeploymentPolicyResultTypeDef = TypedDict(
    "UpdateContinuousDeploymentPolicyResultTypeDef",
    {
        "ContinuousDeploymentPolicy": ContinuousDeploymentPolicyTypeDef,
        "ETag": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateFieldLevelEncryptionProfileResultTypeDef = TypedDict(
    "CreateFieldLevelEncryptionProfileResultTypeDef",
    {
        "FieldLevelEncryptionProfile": FieldLevelEncryptionProfileTypeDef,
        "Location": str,
        "ETag": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetFieldLevelEncryptionProfileResultTypeDef = TypedDict(
    "GetFieldLevelEncryptionProfileResultTypeDef",
    {
        "FieldLevelEncryptionProfile": FieldLevelEncryptionProfileTypeDef,
        "ETag": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateFieldLevelEncryptionProfileResultTypeDef = TypedDict(
    "UpdateFieldLevelEncryptionProfileResultTypeDef",
    {
        "FieldLevelEncryptionProfile": FieldLevelEncryptionProfileTypeDef,
        "ETag": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListFieldLevelEncryptionProfilesResultTypeDef = TypedDict(
    "ListFieldLevelEncryptionProfilesResultTypeDef",
    {
        "FieldLevelEncryptionProfileList": FieldLevelEncryptionProfileListTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListFunctionsResultTypeDef = TypedDict(
    "ListFunctionsResultTypeDef",
    {
        "FunctionList": FunctionListTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TestFunctionResultTypeDef = TypedDict(
    "TestFunctionResultTypeDef",
    {
        "TestResult": TestResultTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateFieldLevelEncryptionConfigResultTypeDef = TypedDict(
    "CreateFieldLevelEncryptionConfigResultTypeDef",
    {
        "FieldLevelEncryption": FieldLevelEncryptionTypeDef,
        "Location": str,
        "ETag": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetFieldLevelEncryptionResultTypeDef = TypedDict(
    "GetFieldLevelEncryptionResultTypeDef",
    {
        "FieldLevelEncryption": FieldLevelEncryptionTypeDef,
        "ETag": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateFieldLevelEncryptionConfigResultTypeDef = TypedDict(
    "UpdateFieldLevelEncryptionConfigResultTypeDef",
    {
        "FieldLevelEncryption": FieldLevelEncryptionTypeDef,
        "ETag": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListFieldLevelEncryptionConfigsResultTypeDef = TypedDict(
    "ListFieldLevelEncryptionConfigsResultTypeDef",
    {
        "FieldLevelEncryptionList": FieldLevelEncryptionListTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ResponseHeadersPolicyListTypeDef = TypedDict(
    "ResponseHeadersPolicyListTypeDef",
    {
        "MaxItems": int,
        "Quantity": int,
        "NextMarker": NotRequired[str],
        "Items": NotRequired[List[ResponseHeadersPolicySummaryTypeDef]],
    },
)
CreateDistributionRequestRequestTypeDef = TypedDict(
    "CreateDistributionRequestRequestTypeDef",
    {
        "DistributionConfig": DistributionConfigTypeDef,
    },
)
DistributionConfigWithTagsTypeDef = TypedDict(
    "DistributionConfigWithTagsTypeDef",
    {
        "DistributionConfig": DistributionConfigTypeDef,
        "Tags": TagsTypeDef,
    },
)
DistributionTypeDef = TypedDict(
    "DistributionTypeDef",
    {
        "Id": str,
        "ARN": str,
        "Status": str,
        "LastModifiedTime": datetime,
        "InProgressInvalidationBatches": int,
        "DomainName": str,
        "DistributionConfig": DistributionConfigTypeDef,
        "ActiveTrustedSigners": NotRequired[ActiveTrustedSignersTypeDef],
        "ActiveTrustedKeyGroups": NotRequired[ActiveTrustedKeyGroupsTypeDef],
        "AliasICPRecordals": NotRequired[List[AliasICPRecordalTypeDef]],
    },
)
GetDistributionConfigResultTypeDef = TypedDict(
    "GetDistributionConfigResultTypeDef",
    {
        "DistributionConfig": DistributionConfigTypeDef,
        "ETag": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateDistributionRequestRequestTypeDef = TypedDict(
    "UpdateDistributionRequestRequestTypeDef",
    {
        "DistributionConfig": DistributionConfigTypeDef,
        "Id": str,
        "IfMatch": NotRequired[str],
    },
)
DistributionListTypeDef = TypedDict(
    "DistributionListTypeDef",
    {
        "Marker": str,
        "MaxItems": int,
        "IsTruncated": bool,
        "Quantity": int,
        "NextMarker": NotRequired[str],
        "Items": NotRequired[List[DistributionSummaryTypeDef]],
    },
)
CachePolicyListTypeDef = TypedDict(
    "CachePolicyListTypeDef",
    {
        "MaxItems": int,
        "Quantity": int,
        "NextMarker": NotRequired[str],
        "Items": NotRequired[List[CachePolicySummaryTypeDef]],
    },
)
ListOriginRequestPoliciesResultTypeDef = TypedDict(
    "ListOriginRequestPoliciesResultTypeDef",
    {
        "OriginRequestPolicyList": OriginRequestPolicyListTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ContinuousDeploymentPolicyListTypeDef = TypedDict(
    "ContinuousDeploymentPolicyListTypeDef",
    {
        "MaxItems": int,
        "Quantity": int,
        "NextMarker": NotRequired[str],
        "Items": NotRequired[List[ContinuousDeploymentPolicySummaryTypeDef]],
    },
)
ListResponseHeadersPoliciesResultTypeDef = TypedDict(
    "ListResponseHeadersPoliciesResultTypeDef",
    {
        "ResponseHeadersPolicyList": ResponseHeadersPolicyListTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDistributionWithTagsRequestRequestTypeDef = TypedDict(
    "CreateDistributionWithTagsRequestRequestTypeDef",
    {
        "DistributionConfigWithTags": DistributionConfigWithTagsTypeDef,
    },
)
CopyDistributionResultTypeDef = TypedDict(
    "CopyDistributionResultTypeDef",
    {
        "Distribution": DistributionTypeDef,
        "Location": str,
        "ETag": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDistributionResultTypeDef = TypedDict(
    "CreateDistributionResultTypeDef",
    {
        "Distribution": DistributionTypeDef,
        "Location": str,
        "ETag": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDistributionWithTagsResultTypeDef = TypedDict(
    "CreateDistributionWithTagsResultTypeDef",
    {
        "Distribution": DistributionTypeDef,
        "Location": str,
        "ETag": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetDistributionResultTypeDef = TypedDict(
    "GetDistributionResultTypeDef",
    {
        "Distribution": DistributionTypeDef,
        "ETag": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateDistributionResultTypeDef = TypedDict(
    "UpdateDistributionResultTypeDef",
    {
        "Distribution": DistributionTypeDef,
        "ETag": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateDistributionWithStagingConfigResultTypeDef = TypedDict(
    "UpdateDistributionWithStagingConfigResultTypeDef",
    {
        "Distribution": DistributionTypeDef,
        "ETag": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListDistributionsByRealtimeLogConfigResultTypeDef = TypedDict(
    "ListDistributionsByRealtimeLogConfigResultTypeDef",
    {
        "DistributionList": DistributionListTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListDistributionsByWebACLIdResultTypeDef = TypedDict(
    "ListDistributionsByWebACLIdResultTypeDef",
    {
        "DistributionList": DistributionListTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListDistributionsResultTypeDef = TypedDict(
    "ListDistributionsResultTypeDef",
    {
        "DistributionList": DistributionListTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListCachePoliciesResultTypeDef = TypedDict(
    "ListCachePoliciesResultTypeDef",
    {
        "CachePolicyList": CachePolicyListTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListContinuousDeploymentPoliciesResultTypeDef = TypedDict(
    "ListContinuousDeploymentPoliciesResultTypeDef",
    {
        "ContinuousDeploymentPolicyList": ContinuousDeploymentPolicyListTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
