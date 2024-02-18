"""
Type annotations for acm-pca service type definitions.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_acm_pca/type_defs/)

Usage::

    ```python
    from types_aiobotocore_acm_pca.type_defs import CustomAttributeTypeDef

    data: CustomAttributeTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Sequence, Union

from aiobotocore.response import StreamingBody

from .literals import (
    AccessMethodTypeType,
    ActionTypeType,
    AuditReportResponseFormatType,
    AuditReportStatusType,
    CertificateAuthorityStatusType,
    CertificateAuthorityTypeType,
    CertificateAuthorityUsageModeType,
    ExtendedKeyUsageTypeType,
    FailureReasonType,
    KeyAlgorithmType,
    KeyStorageSecurityStandardType,
    ResourceOwnerType,
    RevocationReasonType,
    S3ObjectAclType,
    SigningAlgorithmType,
    ValidityPeriodTypeType,
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
    "CustomAttributeTypeDef",
    "AccessMethodTypeDef",
    "BlobTypeDef",
    "CreateCertificateAuthorityAuditReportRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "TagTypeDef",
    "CreatePermissionRequestRequestTypeDef",
    "CrlDistributionPointExtensionConfigurationTypeDef",
    "KeyUsageTypeDef",
    "CustomExtensionTypeDef",
    "DeleteCertificateAuthorityRequestRequestTypeDef",
    "DeletePermissionRequestRequestTypeDef",
    "DeletePolicyRequestRequestTypeDef",
    "WaiterConfigTypeDef",
    "DescribeCertificateAuthorityAuditReportRequestRequestTypeDef",
    "DescribeCertificateAuthorityRequestRequestTypeDef",
    "EdiPartyNameTypeDef",
    "ExtendedKeyUsageTypeDef",
    "OtherNameTypeDef",
    "GetCertificateAuthorityCertificateRequestRequestTypeDef",
    "GetCertificateAuthorityCsrRequestRequestTypeDef",
    "GetCertificateRequestRequestTypeDef",
    "GetPolicyRequestRequestTypeDef",
    "ValidityTypeDef",
    "PaginatorConfigTypeDef",
    "ListCertificateAuthoritiesRequestRequestTypeDef",
    "ListPermissionsRequestRequestTypeDef",
    "PermissionTypeDef",
    "ListTagsRequestRequestTypeDef",
    "OcspConfigurationTypeDef",
    "QualifierTypeDef",
    "PutPolicyRequestRequestTypeDef",
    "RestoreCertificateAuthorityRequestRequestTypeDef",
    "RevokeCertificateRequestRequestTypeDef",
    "ASN1SubjectPaginatorTypeDef",
    "ASN1SubjectTypeDef",
    "ImportCertificateAuthorityCertificateRequestRequestTypeDef",
    "CreateCertificateAuthorityAuditReportResponseTypeDef",
    "CreateCertificateAuthorityResponseTypeDef",
    "DescribeCertificateAuthorityAuditReportResponseTypeDef",
    "EmptyResponseMetadataTypeDef",
    "GetCertificateAuthorityCertificateResponseTypeDef",
    "GetCertificateAuthorityCsrResponseTypeDef",
    "GetCertificateResponseTypeDef",
    "GetPolicyResponseTypeDef",
    "IssueCertificateResponseTypeDef",
    "ListTagsResponseTypeDef",
    "TagCertificateAuthorityRequestRequestTypeDef",
    "UntagCertificateAuthorityRequestRequestTypeDef",
    "CrlConfigurationTypeDef",
    "DescribeCertificateAuthorityAuditReportRequestAuditReportCreatedWaitTypeDef",
    "GetCertificateAuthorityCsrRequestCertificateAuthorityCSRCreatedWaitTypeDef",
    "GetCertificateRequestCertificateIssuedWaitTypeDef",
    "ListCertificateAuthoritiesRequestListCertificateAuthoritiesPaginateTypeDef",
    "ListPermissionsRequestListPermissionsPaginateTypeDef",
    "ListTagsRequestListTagsPaginateTypeDef",
    "ListPermissionsResponseTypeDef",
    "PolicyQualifierInfoTypeDef",
    "GeneralNamePaginatorTypeDef",
    "GeneralNameTypeDef",
    "RevocationConfigurationTypeDef",
    "PolicyInformationTypeDef",
    "AccessDescriptionPaginatorTypeDef",
    "AccessDescriptionTypeDef",
    "UpdateCertificateAuthorityRequestRequestTypeDef",
    "ExtensionsTypeDef",
    "CsrExtensionsPaginatorTypeDef",
    "CsrExtensionsTypeDef",
    "ApiPassthroughTypeDef",
    "CertificateAuthorityConfigurationPaginatorTypeDef",
    "CertificateAuthorityConfigurationTypeDef",
    "IssueCertificateRequestRequestTypeDef",
    "CertificateAuthorityPaginatorTypeDef",
    "CertificateAuthorityTypeDef",
    "CreateCertificateAuthorityRequestRequestTypeDef",
    "ListCertificateAuthoritiesResponsePaginatorTypeDef",
    "DescribeCertificateAuthorityResponseTypeDef",
    "ListCertificateAuthoritiesResponseTypeDef",
)

CustomAttributeTypeDef = TypedDict(
    "CustomAttributeTypeDef",
    {
        "ObjectIdentifier": str,
        "Value": str,
    },
)
AccessMethodTypeDef = TypedDict(
    "AccessMethodTypeDef",
    {
        "CustomObjectIdentifier": NotRequired[str],
        "AccessMethodType": NotRequired[AccessMethodTypeType],
    },
)
BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]
CreateCertificateAuthorityAuditReportRequestRequestTypeDef = TypedDict(
    "CreateCertificateAuthorityAuditReportRequestRequestTypeDef",
    {
        "CertificateAuthorityArn": str,
        "S3BucketName": str,
        "AuditReportResponseFormat": AuditReportResponseFormatType,
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
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": NotRequired[str],
    },
)
CreatePermissionRequestRequestTypeDef = TypedDict(
    "CreatePermissionRequestRequestTypeDef",
    {
        "CertificateAuthorityArn": str,
        "Principal": str,
        "Actions": Sequence[ActionTypeType],
        "SourceAccount": NotRequired[str],
    },
)
CrlDistributionPointExtensionConfigurationTypeDef = TypedDict(
    "CrlDistributionPointExtensionConfigurationTypeDef",
    {
        "OmitExtension": bool,
    },
)
KeyUsageTypeDef = TypedDict(
    "KeyUsageTypeDef",
    {
        "DigitalSignature": NotRequired[bool],
        "NonRepudiation": NotRequired[bool],
        "KeyEncipherment": NotRequired[bool],
        "DataEncipherment": NotRequired[bool],
        "KeyAgreement": NotRequired[bool],
        "KeyCertSign": NotRequired[bool],
        "CRLSign": NotRequired[bool],
        "EncipherOnly": NotRequired[bool],
        "DecipherOnly": NotRequired[bool],
    },
)
CustomExtensionTypeDef = TypedDict(
    "CustomExtensionTypeDef",
    {
        "ObjectIdentifier": str,
        "Value": str,
        "Critical": NotRequired[bool],
    },
)
DeleteCertificateAuthorityRequestRequestTypeDef = TypedDict(
    "DeleteCertificateAuthorityRequestRequestTypeDef",
    {
        "CertificateAuthorityArn": str,
        "PermanentDeletionTimeInDays": NotRequired[int],
    },
)
DeletePermissionRequestRequestTypeDef = TypedDict(
    "DeletePermissionRequestRequestTypeDef",
    {
        "CertificateAuthorityArn": str,
        "Principal": str,
        "SourceAccount": NotRequired[str],
    },
)
DeletePolicyRequestRequestTypeDef = TypedDict(
    "DeletePolicyRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": NotRequired[int],
        "MaxAttempts": NotRequired[int],
    },
)
DescribeCertificateAuthorityAuditReportRequestRequestTypeDef = TypedDict(
    "DescribeCertificateAuthorityAuditReportRequestRequestTypeDef",
    {
        "CertificateAuthorityArn": str,
        "AuditReportId": str,
    },
)
DescribeCertificateAuthorityRequestRequestTypeDef = TypedDict(
    "DescribeCertificateAuthorityRequestRequestTypeDef",
    {
        "CertificateAuthorityArn": str,
    },
)
EdiPartyNameTypeDef = TypedDict(
    "EdiPartyNameTypeDef",
    {
        "PartyName": str,
        "NameAssigner": NotRequired[str],
    },
)
ExtendedKeyUsageTypeDef = TypedDict(
    "ExtendedKeyUsageTypeDef",
    {
        "ExtendedKeyUsageType": NotRequired[ExtendedKeyUsageTypeType],
        "ExtendedKeyUsageObjectIdentifier": NotRequired[str],
    },
)
OtherNameTypeDef = TypedDict(
    "OtherNameTypeDef",
    {
        "TypeId": str,
        "Value": str,
    },
)
GetCertificateAuthorityCertificateRequestRequestTypeDef = TypedDict(
    "GetCertificateAuthorityCertificateRequestRequestTypeDef",
    {
        "CertificateAuthorityArn": str,
    },
)
GetCertificateAuthorityCsrRequestRequestTypeDef = TypedDict(
    "GetCertificateAuthorityCsrRequestRequestTypeDef",
    {
        "CertificateAuthorityArn": str,
    },
)
GetCertificateRequestRequestTypeDef = TypedDict(
    "GetCertificateRequestRequestTypeDef",
    {
        "CertificateAuthorityArn": str,
        "CertificateArn": str,
    },
)
GetPolicyRequestRequestTypeDef = TypedDict(
    "GetPolicyRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
ValidityTypeDef = TypedDict(
    "ValidityTypeDef",
    {
        "Value": int,
        "Type": ValidityPeriodTypeType,
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
ListCertificateAuthoritiesRequestRequestTypeDef = TypedDict(
    "ListCertificateAuthoritiesRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "ResourceOwner": NotRequired[ResourceOwnerType],
    },
)
ListPermissionsRequestRequestTypeDef = TypedDict(
    "ListPermissionsRequestRequestTypeDef",
    {
        "CertificateAuthorityArn": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
PermissionTypeDef = TypedDict(
    "PermissionTypeDef",
    {
        "CertificateAuthorityArn": NotRequired[str],
        "CreatedAt": NotRequired[datetime],
        "Principal": NotRequired[str],
        "SourceAccount": NotRequired[str],
        "Actions": NotRequired[List[ActionTypeType]],
        "Policy": NotRequired[str],
    },
)
ListTagsRequestRequestTypeDef = TypedDict(
    "ListTagsRequestRequestTypeDef",
    {
        "CertificateAuthorityArn": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
OcspConfigurationTypeDef = TypedDict(
    "OcspConfigurationTypeDef",
    {
        "Enabled": bool,
        "OcspCustomCname": NotRequired[str],
    },
)
QualifierTypeDef = TypedDict(
    "QualifierTypeDef",
    {
        "CpsUri": str,
    },
)
PutPolicyRequestRequestTypeDef = TypedDict(
    "PutPolicyRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Policy": str,
    },
)
RestoreCertificateAuthorityRequestRequestTypeDef = TypedDict(
    "RestoreCertificateAuthorityRequestRequestTypeDef",
    {
        "CertificateAuthorityArn": str,
    },
)
RevokeCertificateRequestRequestTypeDef = TypedDict(
    "RevokeCertificateRequestRequestTypeDef",
    {
        "CertificateAuthorityArn": str,
        "CertificateSerial": str,
        "RevocationReason": RevocationReasonType,
    },
)
ASN1SubjectPaginatorTypeDef = TypedDict(
    "ASN1SubjectPaginatorTypeDef",
    {
        "Country": NotRequired[str],
        "Organization": NotRequired[str],
        "OrganizationalUnit": NotRequired[str],
        "DistinguishedNameQualifier": NotRequired[str],
        "State": NotRequired[str],
        "CommonName": NotRequired[str],
        "SerialNumber": NotRequired[str],
        "Locality": NotRequired[str],
        "Title": NotRequired[str],
        "Surname": NotRequired[str],
        "GivenName": NotRequired[str],
        "Initials": NotRequired[str],
        "Pseudonym": NotRequired[str],
        "GenerationQualifier": NotRequired[str],
        "CustomAttributes": NotRequired[List[CustomAttributeTypeDef]],
    },
)
ASN1SubjectTypeDef = TypedDict(
    "ASN1SubjectTypeDef",
    {
        "Country": NotRequired[str],
        "Organization": NotRequired[str],
        "OrganizationalUnit": NotRequired[str],
        "DistinguishedNameQualifier": NotRequired[str],
        "State": NotRequired[str],
        "CommonName": NotRequired[str],
        "SerialNumber": NotRequired[str],
        "Locality": NotRequired[str],
        "Title": NotRequired[str],
        "Surname": NotRequired[str],
        "GivenName": NotRequired[str],
        "Initials": NotRequired[str],
        "Pseudonym": NotRequired[str],
        "GenerationQualifier": NotRequired[str],
        "CustomAttributes": NotRequired[Sequence[CustomAttributeTypeDef]],
    },
)
ImportCertificateAuthorityCertificateRequestRequestTypeDef = TypedDict(
    "ImportCertificateAuthorityCertificateRequestRequestTypeDef",
    {
        "CertificateAuthorityArn": str,
        "Certificate": BlobTypeDef,
        "CertificateChain": NotRequired[BlobTypeDef],
    },
)
CreateCertificateAuthorityAuditReportResponseTypeDef = TypedDict(
    "CreateCertificateAuthorityAuditReportResponseTypeDef",
    {
        "AuditReportId": str,
        "S3Key": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateCertificateAuthorityResponseTypeDef = TypedDict(
    "CreateCertificateAuthorityResponseTypeDef",
    {
        "CertificateAuthorityArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeCertificateAuthorityAuditReportResponseTypeDef = TypedDict(
    "DescribeCertificateAuthorityAuditReportResponseTypeDef",
    {
        "AuditReportStatus": AuditReportStatusType,
        "S3BucketName": str,
        "S3Key": str,
        "CreatedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetCertificateAuthorityCertificateResponseTypeDef = TypedDict(
    "GetCertificateAuthorityCertificateResponseTypeDef",
    {
        "Certificate": str,
        "CertificateChain": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetCertificateAuthorityCsrResponseTypeDef = TypedDict(
    "GetCertificateAuthorityCsrResponseTypeDef",
    {
        "Csr": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetCertificateResponseTypeDef = TypedDict(
    "GetCertificateResponseTypeDef",
    {
        "Certificate": str,
        "CertificateChain": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetPolicyResponseTypeDef = TypedDict(
    "GetPolicyResponseTypeDef",
    {
        "Policy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
IssueCertificateResponseTypeDef = TypedDict(
    "IssueCertificateResponseTypeDef",
    {
        "CertificateArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTagsResponseTypeDef = TypedDict(
    "ListTagsResponseTypeDef",
    {
        "Tags": List[TagTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TagCertificateAuthorityRequestRequestTypeDef = TypedDict(
    "TagCertificateAuthorityRequestRequestTypeDef",
    {
        "CertificateAuthorityArn": str,
        "Tags": Sequence[TagTypeDef],
    },
)
UntagCertificateAuthorityRequestRequestTypeDef = TypedDict(
    "UntagCertificateAuthorityRequestRequestTypeDef",
    {
        "CertificateAuthorityArn": str,
        "Tags": Sequence[TagTypeDef],
    },
)
CrlConfigurationTypeDef = TypedDict(
    "CrlConfigurationTypeDef",
    {
        "Enabled": bool,
        "ExpirationInDays": NotRequired[int],
        "CustomCname": NotRequired[str],
        "S3BucketName": NotRequired[str],
        "S3ObjectAcl": NotRequired[S3ObjectAclType],
        "CrlDistributionPointExtensionConfiguration": NotRequired[
            CrlDistributionPointExtensionConfigurationTypeDef
        ],
    },
)
DescribeCertificateAuthorityAuditReportRequestAuditReportCreatedWaitTypeDef = TypedDict(
    "DescribeCertificateAuthorityAuditReportRequestAuditReportCreatedWaitTypeDef",
    {
        "CertificateAuthorityArn": str,
        "AuditReportId": str,
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
GetCertificateAuthorityCsrRequestCertificateAuthorityCSRCreatedWaitTypeDef = TypedDict(
    "GetCertificateAuthorityCsrRequestCertificateAuthorityCSRCreatedWaitTypeDef",
    {
        "CertificateAuthorityArn": str,
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
GetCertificateRequestCertificateIssuedWaitTypeDef = TypedDict(
    "GetCertificateRequestCertificateIssuedWaitTypeDef",
    {
        "CertificateAuthorityArn": str,
        "CertificateArn": str,
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
ListCertificateAuthoritiesRequestListCertificateAuthoritiesPaginateTypeDef = TypedDict(
    "ListCertificateAuthoritiesRequestListCertificateAuthoritiesPaginateTypeDef",
    {
        "ResourceOwner": NotRequired[ResourceOwnerType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListPermissionsRequestListPermissionsPaginateTypeDef = TypedDict(
    "ListPermissionsRequestListPermissionsPaginateTypeDef",
    {
        "CertificateAuthorityArn": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListTagsRequestListTagsPaginateTypeDef = TypedDict(
    "ListTagsRequestListTagsPaginateTypeDef",
    {
        "CertificateAuthorityArn": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListPermissionsResponseTypeDef = TypedDict(
    "ListPermissionsResponseTypeDef",
    {
        "Permissions": List[PermissionTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PolicyQualifierInfoTypeDef = TypedDict(
    "PolicyQualifierInfoTypeDef",
    {
        "PolicyQualifierId": Literal["CPS"],
        "Qualifier": QualifierTypeDef,
    },
)
GeneralNamePaginatorTypeDef = TypedDict(
    "GeneralNamePaginatorTypeDef",
    {
        "OtherName": NotRequired[OtherNameTypeDef],
        "Rfc822Name": NotRequired[str],
        "DnsName": NotRequired[str],
        "DirectoryName": NotRequired[ASN1SubjectPaginatorTypeDef],
        "EdiPartyName": NotRequired[EdiPartyNameTypeDef],
        "UniformResourceIdentifier": NotRequired[str],
        "IpAddress": NotRequired[str],
        "RegisteredId": NotRequired[str],
    },
)
GeneralNameTypeDef = TypedDict(
    "GeneralNameTypeDef",
    {
        "OtherName": NotRequired[OtherNameTypeDef],
        "Rfc822Name": NotRequired[str],
        "DnsName": NotRequired[str],
        "DirectoryName": NotRequired[ASN1SubjectTypeDef],
        "EdiPartyName": NotRequired[EdiPartyNameTypeDef],
        "UniformResourceIdentifier": NotRequired[str],
        "IpAddress": NotRequired[str],
        "RegisteredId": NotRequired[str],
    },
)
RevocationConfigurationTypeDef = TypedDict(
    "RevocationConfigurationTypeDef",
    {
        "CrlConfiguration": NotRequired[CrlConfigurationTypeDef],
        "OcspConfiguration": NotRequired[OcspConfigurationTypeDef],
    },
)
PolicyInformationTypeDef = TypedDict(
    "PolicyInformationTypeDef",
    {
        "CertPolicyId": str,
        "PolicyQualifiers": NotRequired[Sequence[PolicyQualifierInfoTypeDef]],
    },
)
AccessDescriptionPaginatorTypeDef = TypedDict(
    "AccessDescriptionPaginatorTypeDef",
    {
        "AccessMethod": AccessMethodTypeDef,
        "AccessLocation": GeneralNamePaginatorTypeDef,
    },
)
AccessDescriptionTypeDef = TypedDict(
    "AccessDescriptionTypeDef",
    {
        "AccessMethod": AccessMethodTypeDef,
        "AccessLocation": GeneralNameTypeDef,
    },
)
UpdateCertificateAuthorityRequestRequestTypeDef = TypedDict(
    "UpdateCertificateAuthorityRequestRequestTypeDef",
    {
        "CertificateAuthorityArn": str,
        "RevocationConfiguration": NotRequired[RevocationConfigurationTypeDef],
        "Status": NotRequired[CertificateAuthorityStatusType],
    },
)
ExtensionsTypeDef = TypedDict(
    "ExtensionsTypeDef",
    {
        "CertificatePolicies": NotRequired[Sequence[PolicyInformationTypeDef]],
        "ExtendedKeyUsage": NotRequired[Sequence[ExtendedKeyUsageTypeDef]],
        "KeyUsage": NotRequired[KeyUsageTypeDef],
        "SubjectAlternativeNames": NotRequired[Sequence[GeneralNameTypeDef]],
        "CustomExtensions": NotRequired[Sequence[CustomExtensionTypeDef]],
    },
)
CsrExtensionsPaginatorTypeDef = TypedDict(
    "CsrExtensionsPaginatorTypeDef",
    {
        "KeyUsage": NotRequired[KeyUsageTypeDef],
        "SubjectInformationAccess": NotRequired[List[AccessDescriptionPaginatorTypeDef]],
    },
)
CsrExtensionsTypeDef = TypedDict(
    "CsrExtensionsTypeDef",
    {
        "KeyUsage": NotRequired[KeyUsageTypeDef],
        "SubjectInformationAccess": NotRequired[Sequence[AccessDescriptionTypeDef]],
    },
)
ApiPassthroughTypeDef = TypedDict(
    "ApiPassthroughTypeDef",
    {
        "Extensions": NotRequired[ExtensionsTypeDef],
        "Subject": NotRequired[ASN1SubjectTypeDef],
    },
)
CertificateAuthorityConfigurationPaginatorTypeDef = TypedDict(
    "CertificateAuthorityConfigurationPaginatorTypeDef",
    {
        "KeyAlgorithm": KeyAlgorithmType,
        "SigningAlgorithm": SigningAlgorithmType,
        "Subject": ASN1SubjectPaginatorTypeDef,
        "CsrExtensions": NotRequired[CsrExtensionsPaginatorTypeDef],
    },
)
CertificateAuthorityConfigurationTypeDef = TypedDict(
    "CertificateAuthorityConfigurationTypeDef",
    {
        "KeyAlgorithm": KeyAlgorithmType,
        "SigningAlgorithm": SigningAlgorithmType,
        "Subject": ASN1SubjectTypeDef,
        "CsrExtensions": NotRequired[CsrExtensionsTypeDef],
    },
)
IssueCertificateRequestRequestTypeDef = TypedDict(
    "IssueCertificateRequestRequestTypeDef",
    {
        "CertificateAuthorityArn": str,
        "Csr": BlobTypeDef,
        "SigningAlgorithm": SigningAlgorithmType,
        "Validity": ValidityTypeDef,
        "ApiPassthrough": NotRequired[ApiPassthroughTypeDef],
        "TemplateArn": NotRequired[str],
        "ValidityNotBefore": NotRequired[ValidityTypeDef],
        "IdempotencyToken": NotRequired[str],
    },
)
CertificateAuthorityPaginatorTypeDef = TypedDict(
    "CertificateAuthorityPaginatorTypeDef",
    {
        "Arn": NotRequired[str],
        "OwnerAccount": NotRequired[str],
        "CreatedAt": NotRequired[datetime],
        "LastStateChangeAt": NotRequired[datetime],
        "Type": NotRequired[CertificateAuthorityTypeType],
        "Serial": NotRequired[str],
        "Status": NotRequired[CertificateAuthorityStatusType],
        "NotBefore": NotRequired[datetime],
        "NotAfter": NotRequired[datetime],
        "FailureReason": NotRequired[FailureReasonType],
        "CertificateAuthorityConfiguration": NotRequired[
            CertificateAuthorityConfigurationPaginatorTypeDef
        ],
        "RevocationConfiguration": NotRequired[RevocationConfigurationTypeDef],
        "RestorableUntil": NotRequired[datetime],
        "KeyStorageSecurityStandard": NotRequired[KeyStorageSecurityStandardType],
        "UsageMode": NotRequired[CertificateAuthorityUsageModeType],
    },
)
CertificateAuthorityTypeDef = TypedDict(
    "CertificateAuthorityTypeDef",
    {
        "Arn": NotRequired[str],
        "OwnerAccount": NotRequired[str],
        "CreatedAt": NotRequired[datetime],
        "LastStateChangeAt": NotRequired[datetime],
        "Type": NotRequired[CertificateAuthorityTypeType],
        "Serial": NotRequired[str],
        "Status": NotRequired[CertificateAuthorityStatusType],
        "NotBefore": NotRequired[datetime],
        "NotAfter": NotRequired[datetime],
        "FailureReason": NotRequired[FailureReasonType],
        "CertificateAuthorityConfiguration": NotRequired[CertificateAuthorityConfigurationTypeDef],
        "RevocationConfiguration": NotRequired[RevocationConfigurationTypeDef],
        "RestorableUntil": NotRequired[datetime],
        "KeyStorageSecurityStandard": NotRequired[KeyStorageSecurityStandardType],
        "UsageMode": NotRequired[CertificateAuthorityUsageModeType],
    },
)
CreateCertificateAuthorityRequestRequestTypeDef = TypedDict(
    "CreateCertificateAuthorityRequestRequestTypeDef",
    {
        "CertificateAuthorityConfiguration": CertificateAuthorityConfigurationTypeDef,
        "CertificateAuthorityType": CertificateAuthorityTypeType,
        "RevocationConfiguration": NotRequired[RevocationConfigurationTypeDef],
        "IdempotencyToken": NotRequired[str],
        "KeyStorageSecurityStandard": NotRequired[KeyStorageSecurityStandardType],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "UsageMode": NotRequired[CertificateAuthorityUsageModeType],
    },
)
ListCertificateAuthoritiesResponsePaginatorTypeDef = TypedDict(
    "ListCertificateAuthoritiesResponsePaginatorTypeDef",
    {
        "CertificateAuthorities": List[CertificateAuthorityPaginatorTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeCertificateAuthorityResponseTypeDef = TypedDict(
    "DescribeCertificateAuthorityResponseTypeDef",
    {
        "CertificateAuthority": CertificateAuthorityTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListCertificateAuthoritiesResponseTypeDef = TypedDict(
    "ListCertificateAuthoritiesResponseTypeDef",
    {
        "CertificateAuthorities": List[CertificateAuthorityTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
