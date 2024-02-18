"""
Type annotations for service-quotas service type definitions.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_service_quotas/type_defs/)

Usage::

    ```python
    from types_aiobotocore_service_quotas.type_defs import DeleteServiceQuotaIncreaseRequestFromTemplateRequestRequestTypeDef

    data: DeleteServiceQuotaIncreaseRequestFromTemplateRequestRequestTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Sequence

from .literals import (
    AppliedLevelEnumType,
    ErrorCodeType,
    PeriodUnitType,
    QuotaContextScopeType,
    RequestStatusType,
    ServiceQuotaTemplateAssociationStatusType,
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
    "DeleteServiceQuotaIncreaseRequestFromTemplateRequestRequestTypeDef",
    "ErrorReasonTypeDef",
    "GetAWSDefaultServiceQuotaRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "GetRequestedServiceQuotaChangeRequestRequestTypeDef",
    "GetServiceQuotaIncreaseRequestFromTemplateRequestRequestTypeDef",
    "ServiceQuotaIncreaseRequestInTemplateTypeDef",
    "GetServiceQuotaRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "ListAWSDefaultServiceQuotasRequestRequestTypeDef",
    "ListRequestedServiceQuotaChangeHistoryByQuotaRequestRequestTypeDef",
    "ListRequestedServiceQuotaChangeHistoryRequestRequestTypeDef",
    "ListServiceQuotaIncreaseRequestsInTemplateRequestRequestTypeDef",
    "ListServiceQuotasRequestRequestTypeDef",
    "ListServicesRequestRequestTypeDef",
    "ServiceInfoTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "TagTypeDef",
    "MetricInfoTypeDef",
    "PutServiceQuotaIncreaseRequestIntoTemplateRequestRequestTypeDef",
    "QuotaContextInfoTypeDef",
    "QuotaPeriodTypeDef",
    "RequestServiceQuotaIncreaseRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "GetAssociationForServiceQuotaTemplateResponseTypeDef",
    "GetServiceQuotaIncreaseRequestFromTemplateResponseTypeDef",
    "ListServiceQuotaIncreaseRequestsInTemplateResponseTypeDef",
    "PutServiceQuotaIncreaseRequestIntoTemplateResponseTypeDef",
    "ListAWSDefaultServiceQuotasRequestListAWSDefaultServiceQuotasPaginateTypeDef",
    "ListRequestedServiceQuotaChangeHistoryByQuotaRequestListRequestedServiceQuotaChangeHistoryByQuotaPaginateTypeDef",
    "ListRequestedServiceQuotaChangeHistoryRequestListRequestedServiceQuotaChangeHistoryPaginateTypeDef",
    "ListServiceQuotaIncreaseRequestsInTemplateRequestListServiceQuotaIncreaseRequestsInTemplatePaginateTypeDef",
    "ListServiceQuotasRequestListServiceQuotasPaginateTypeDef",
    "ListServicesRequestListServicesPaginateTypeDef",
    "ListServicesResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "RequestedServiceQuotaChangeTypeDef",
    "ServiceQuotaTypeDef",
    "GetRequestedServiceQuotaChangeResponseTypeDef",
    "ListRequestedServiceQuotaChangeHistoryByQuotaResponseTypeDef",
    "ListRequestedServiceQuotaChangeHistoryResponseTypeDef",
    "RequestServiceQuotaIncreaseResponseTypeDef",
    "GetAWSDefaultServiceQuotaResponseTypeDef",
    "GetServiceQuotaResponseTypeDef",
    "ListAWSDefaultServiceQuotasResponseTypeDef",
    "ListServiceQuotasResponseTypeDef",
)

DeleteServiceQuotaIncreaseRequestFromTemplateRequestRequestTypeDef = TypedDict(
    "DeleteServiceQuotaIncreaseRequestFromTemplateRequestRequestTypeDef",
    {
        "ServiceCode": str,
        "QuotaCode": str,
        "AwsRegion": str,
    },
)
ErrorReasonTypeDef = TypedDict(
    "ErrorReasonTypeDef",
    {
        "ErrorCode": NotRequired[ErrorCodeType],
        "ErrorMessage": NotRequired[str],
    },
)
GetAWSDefaultServiceQuotaRequestRequestTypeDef = TypedDict(
    "GetAWSDefaultServiceQuotaRequestRequestTypeDef",
    {
        "ServiceCode": str,
        "QuotaCode": str,
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
GetRequestedServiceQuotaChangeRequestRequestTypeDef = TypedDict(
    "GetRequestedServiceQuotaChangeRequestRequestTypeDef",
    {
        "RequestId": str,
    },
)
GetServiceQuotaIncreaseRequestFromTemplateRequestRequestTypeDef = TypedDict(
    "GetServiceQuotaIncreaseRequestFromTemplateRequestRequestTypeDef",
    {
        "ServiceCode": str,
        "QuotaCode": str,
        "AwsRegion": str,
    },
)
ServiceQuotaIncreaseRequestInTemplateTypeDef = TypedDict(
    "ServiceQuotaIncreaseRequestInTemplateTypeDef",
    {
        "ServiceCode": NotRequired[str],
        "ServiceName": NotRequired[str],
        "QuotaCode": NotRequired[str],
        "QuotaName": NotRequired[str],
        "DesiredValue": NotRequired[float],
        "AwsRegion": NotRequired[str],
        "Unit": NotRequired[str],
        "GlobalQuota": NotRequired[bool],
    },
)
GetServiceQuotaRequestRequestTypeDef = TypedDict(
    "GetServiceQuotaRequestRequestTypeDef",
    {
        "ServiceCode": str,
        "QuotaCode": str,
        "ContextId": NotRequired[str],
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
ListAWSDefaultServiceQuotasRequestRequestTypeDef = TypedDict(
    "ListAWSDefaultServiceQuotasRequestRequestTypeDef",
    {
        "ServiceCode": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListRequestedServiceQuotaChangeHistoryByQuotaRequestRequestTypeDef = TypedDict(
    "ListRequestedServiceQuotaChangeHistoryByQuotaRequestRequestTypeDef",
    {
        "ServiceCode": str,
        "QuotaCode": str,
        "Status": NotRequired[RequestStatusType],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "QuotaRequestedAtLevel": NotRequired[AppliedLevelEnumType],
    },
)
ListRequestedServiceQuotaChangeHistoryRequestRequestTypeDef = TypedDict(
    "ListRequestedServiceQuotaChangeHistoryRequestRequestTypeDef",
    {
        "ServiceCode": NotRequired[str],
        "Status": NotRequired[RequestStatusType],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "QuotaRequestedAtLevel": NotRequired[AppliedLevelEnumType],
    },
)
ListServiceQuotaIncreaseRequestsInTemplateRequestRequestTypeDef = TypedDict(
    "ListServiceQuotaIncreaseRequestsInTemplateRequestRequestTypeDef",
    {
        "ServiceCode": NotRequired[str],
        "AwsRegion": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListServiceQuotasRequestRequestTypeDef = TypedDict(
    "ListServiceQuotasRequestRequestTypeDef",
    {
        "ServiceCode": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "QuotaCode": NotRequired[str],
        "QuotaAppliedAtLevel": NotRequired[AppliedLevelEnumType],
    },
)
ListServicesRequestRequestTypeDef = TypedDict(
    "ListServicesRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ServiceInfoTypeDef = TypedDict(
    "ServiceInfoTypeDef",
    {
        "ServiceCode": NotRequired[str],
        "ServiceName": NotRequired[str],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)
MetricInfoTypeDef = TypedDict(
    "MetricInfoTypeDef",
    {
        "MetricNamespace": NotRequired[str],
        "MetricName": NotRequired[str],
        "MetricDimensions": NotRequired[Dict[str, str]],
        "MetricStatisticRecommendation": NotRequired[str],
    },
)
PutServiceQuotaIncreaseRequestIntoTemplateRequestRequestTypeDef = TypedDict(
    "PutServiceQuotaIncreaseRequestIntoTemplateRequestRequestTypeDef",
    {
        "QuotaCode": str,
        "ServiceCode": str,
        "AwsRegion": str,
        "DesiredValue": float,
    },
)
QuotaContextInfoTypeDef = TypedDict(
    "QuotaContextInfoTypeDef",
    {
        "ContextScope": NotRequired[QuotaContextScopeType],
        "ContextScopeType": NotRequired[str],
        "ContextId": NotRequired[str],
    },
)
QuotaPeriodTypeDef = TypedDict(
    "QuotaPeriodTypeDef",
    {
        "PeriodValue": NotRequired[int],
        "PeriodUnit": NotRequired[PeriodUnitType],
    },
)
RequestServiceQuotaIncreaseRequestRequestTypeDef = TypedDict(
    "RequestServiceQuotaIncreaseRequestRequestTypeDef",
    {
        "ServiceCode": str,
        "QuotaCode": str,
        "DesiredValue": float,
        "ContextId": NotRequired[str],
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": Sequence[str],
    },
)
GetAssociationForServiceQuotaTemplateResponseTypeDef = TypedDict(
    "GetAssociationForServiceQuotaTemplateResponseTypeDef",
    {
        "ServiceQuotaTemplateAssociationStatus": ServiceQuotaTemplateAssociationStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetServiceQuotaIncreaseRequestFromTemplateResponseTypeDef = TypedDict(
    "GetServiceQuotaIncreaseRequestFromTemplateResponseTypeDef",
    {
        "ServiceQuotaIncreaseRequestInTemplate": ServiceQuotaIncreaseRequestInTemplateTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListServiceQuotaIncreaseRequestsInTemplateResponseTypeDef = TypedDict(
    "ListServiceQuotaIncreaseRequestsInTemplateResponseTypeDef",
    {
        "ServiceQuotaIncreaseRequestInTemplateList": List[
            ServiceQuotaIncreaseRequestInTemplateTypeDef
        ],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutServiceQuotaIncreaseRequestIntoTemplateResponseTypeDef = TypedDict(
    "PutServiceQuotaIncreaseRequestIntoTemplateResponseTypeDef",
    {
        "ServiceQuotaIncreaseRequestInTemplate": ServiceQuotaIncreaseRequestInTemplateTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAWSDefaultServiceQuotasRequestListAWSDefaultServiceQuotasPaginateTypeDef = TypedDict(
    "ListAWSDefaultServiceQuotasRequestListAWSDefaultServiceQuotasPaginateTypeDef",
    {
        "ServiceCode": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListRequestedServiceQuotaChangeHistoryByQuotaRequestListRequestedServiceQuotaChangeHistoryByQuotaPaginateTypeDef = TypedDict(
    "ListRequestedServiceQuotaChangeHistoryByQuotaRequestListRequestedServiceQuotaChangeHistoryByQuotaPaginateTypeDef",
    {
        "ServiceCode": str,
        "QuotaCode": str,
        "Status": NotRequired[RequestStatusType],
        "QuotaRequestedAtLevel": NotRequired[AppliedLevelEnumType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListRequestedServiceQuotaChangeHistoryRequestListRequestedServiceQuotaChangeHistoryPaginateTypeDef = TypedDict(
    "ListRequestedServiceQuotaChangeHistoryRequestListRequestedServiceQuotaChangeHistoryPaginateTypeDef",
    {
        "ServiceCode": NotRequired[str],
        "Status": NotRequired[RequestStatusType],
        "QuotaRequestedAtLevel": NotRequired[AppliedLevelEnumType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListServiceQuotaIncreaseRequestsInTemplateRequestListServiceQuotaIncreaseRequestsInTemplatePaginateTypeDef = TypedDict(
    "ListServiceQuotaIncreaseRequestsInTemplateRequestListServiceQuotaIncreaseRequestsInTemplatePaginateTypeDef",
    {
        "ServiceCode": NotRequired[str],
        "AwsRegion": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListServiceQuotasRequestListServiceQuotasPaginateTypeDef = TypedDict(
    "ListServiceQuotasRequestListServiceQuotasPaginateTypeDef",
    {
        "ServiceCode": str,
        "QuotaCode": NotRequired[str],
        "QuotaAppliedAtLevel": NotRequired[AppliedLevelEnumType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListServicesRequestListServicesPaginateTypeDef = TypedDict(
    "ListServicesRequestListServicesPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListServicesResponseTypeDef = TypedDict(
    "ListServicesResponseTypeDef",
    {
        "NextToken": str,
        "Services": List[ServiceInfoTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "Tags": Sequence[TagTypeDef],
    },
)
RequestedServiceQuotaChangeTypeDef = TypedDict(
    "RequestedServiceQuotaChangeTypeDef",
    {
        "Id": NotRequired[str],
        "CaseId": NotRequired[str],
        "ServiceCode": NotRequired[str],
        "ServiceName": NotRequired[str],
        "QuotaCode": NotRequired[str],
        "QuotaName": NotRequired[str],
        "DesiredValue": NotRequired[float],
        "Status": NotRequired[RequestStatusType],
        "Created": NotRequired[datetime],
        "LastUpdated": NotRequired[datetime],
        "Requester": NotRequired[str],
        "QuotaArn": NotRequired[str],
        "GlobalQuota": NotRequired[bool],
        "Unit": NotRequired[str],
        "QuotaRequestedAtLevel": NotRequired[AppliedLevelEnumType],
        "QuotaContext": NotRequired[QuotaContextInfoTypeDef],
    },
)
ServiceQuotaTypeDef = TypedDict(
    "ServiceQuotaTypeDef",
    {
        "ServiceCode": NotRequired[str],
        "ServiceName": NotRequired[str],
        "QuotaArn": NotRequired[str],
        "QuotaCode": NotRequired[str],
        "QuotaName": NotRequired[str],
        "Value": NotRequired[float],
        "Unit": NotRequired[str],
        "Adjustable": NotRequired[bool],
        "GlobalQuota": NotRequired[bool],
        "UsageMetric": NotRequired[MetricInfoTypeDef],
        "Period": NotRequired[QuotaPeriodTypeDef],
        "ErrorReason": NotRequired[ErrorReasonTypeDef],
        "QuotaAppliedAtLevel": NotRequired[AppliedLevelEnumType],
        "QuotaContext": NotRequired[QuotaContextInfoTypeDef],
    },
)
GetRequestedServiceQuotaChangeResponseTypeDef = TypedDict(
    "GetRequestedServiceQuotaChangeResponseTypeDef",
    {
        "RequestedQuota": RequestedServiceQuotaChangeTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListRequestedServiceQuotaChangeHistoryByQuotaResponseTypeDef = TypedDict(
    "ListRequestedServiceQuotaChangeHistoryByQuotaResponseTypeDef",
    {
        "NextToken": str,
        "RequestedQuotas": List[RequestedServiceQuotaChangeTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListRequestedServiceQuotaChangeHistoryResponseTypeDef = TypedDict(
    "ListRequestedServiceQuotaChangeHistoryResponseTypeDef",
    {
        "NextToken": str,
        "RequestedQuotas": List[RequestedServiceQuotaChangeTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RequestServiceQuotaIncreaseResponseTypeDef = TypedDict(
    "RequestServiceQuotaIncreaseResponseTypeDef",
    {
        "RequestedQuota": RequestedServiceQuotaChangeTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAWSDefaultServiceQuotaResponseTypeDef = TypedDict(
    "GetAWSDefaultServiceQuotaResponseTypeDef",
    {
        "Quota": ServiceQuotaTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetServiceQuotaResponseTypeDef = TypedDict(
    "GetServiceQuotaResponseTypeDef",
    {
        "Quota": ServiceQuotaTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAWSDefaultServiceQuotasResponseTypeDef = TypedDict(
    "ListAWSDefaultServiceQuotasResponseTypeDef",
    {
        "NextToken": str,
        "Quotas": List[ServiceQuotaTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListServiceQuotasResponseTypeDef = TypedDict(
    "ListServiceQuotasResponseTypeDef",
    {
        "NextToken": str,
        "Quotas": List[ServiceQuotaTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
