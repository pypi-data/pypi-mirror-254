"""
Type annotations for pca-connector-ad service type definitions.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pca_connector_ad/type_defs/)

Usage::

    ```python
    from types_aiobotocore_pca_connector_ad.type_defs import AccessRightsTypeDef

    data: AccessRightsTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from .literals import (
    AccessRightType,
    ApplicationPolicyTypeType,
    ClientCompatibilityV2Type,
    ClientCompatibilityV3Type,
    ClientCompatibilityV4Type,
    ConnectorStatusReasonType,
    ConnectorStatusType,
    DirectoryRegistrationStatusReasonType,
    DirectoryRegistrationStatusType,
    HashAlgorithmType,
    KeySpecType,
    PrivateKeyAlgorithmType,
    ServicePrincipalNameStatusReasonType,
    ServicePrincipalNameStatusType,
    TemplateStatusType,
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
    "AccessRightsTypeDef",
    "ApplicationPolicyTypeDef",
    "ValidityPeriodTypeDef",
    "VpcInformationPaginatorTypeDef",
    "VpcInformationTypeDef",
    "ResponseMetadataTypeDef",
    "CreateDirectoryRegistrationRequestRequestTypeDef",
    "CreateServicePrincipalNameRequestRequestTypeDef",
    "DeleteConnectorRequestRequestTypeDef",
    "DeleteDirectoryRegistrationRequestRequestTypeDef",
    "DeleteServicePrincipalNameRequestRequestTypeDef",
    "DeleteTemplateGroupAccessControlEntryRequestRequestTypeDef",
    "DeleteTemplateRequestRequestTypeDef",
    "DirectoryRegistrationSummaryTypeDef",
    "DirectoryRegistrationTypeDef",
    "EnrollmentFlagsV2TypeDef",
    "EnrollmentFlagsV3TypeDef",
    "EnrollmentFlagsV4TypeDef",
    "GeneralFlagsV2TypeDef",
    "GeneralFlagsV3TypeDef",
    "GeneralFlagsV4TypeDef",
    "GetConnectorRequestRequestTypeDef",
    "GetDirectoryRegistrationRequestRequestTypeDef",
    "GetServicePrincipalNameRequestRequestTypeDef",
    "ServicePrincipalNameTypeDef",
    "GetTemplateGroupAccessControlEntryRequestRequestTypeDef",
    "GetTemplateRequestRequestTypeDef",
    "KeyUsageFlagsTypeDef",
    "KeyUsagePropertyFlagsTypeDef",
    "PaginatorConfigTypeDef",
    "ListConnectorsRequestRequestTypeDef",
    "ListDirectoryRegistrationsRequestRequestTypeDef",
    "ListServicePrincipalNamesRequestRequestTypeDef",
    "ServicePrincipalNameSummaryTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTemplateGroupAccessControlEntriesRequestRequestTypeDef",
    "ListTemplatesRequestRequestTypeDef",
    "PrivateKeyAttributesV2PaginatorTypeDef",
    "PrivateKeyAttributesV2TypeDef",
    "PrivateKeyFlagsV2TypeDef",
    "PrivateKeyFlagsV3TypeDef",
    "PrivateKeyFlagsV4TypeDef",
    "SubjectNameFlagsV2TypeDef",
    "SubjectNameFlagsV3TypeDef",
    "SubjectNameFlagsV4TypeDef",
    "TagResourceRequestRequestTypeDef",
    "TemplateRevisionTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "AccessControlEntrySummaryTypeDef",
    "AccessControlEntryTypeDef",
    "CreateTemplateGroupAccessControlEntryRequestRequestTypeDef",
    "UpdateTemplateGroupAccessControlEntryRequestRequestTypeDef",
    "ApplicationPoliciesPaginatorTypeDef",
    "ApplicationPoliciesTypeDef",
    "CertificateValidityTypeDef",
    "ConnectorSummaryPaginatorTypeDef",
    "ConnectorSummaryTypeDef",
    "ConnectorTypeDef",
    "CreateConnectorRequestRequestTypeDef",
    "CreateConnectorResponseTypeDef",
    "CreateDirectoryRegistrationResponseTypeDef",
    "CreateTemplateResponseTypeDef",
    "EmptyResponseMetadataTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListDirectoryRegistrationsResponseTypeDef",
    "GetDirectoryRegistrationResponseTypeDef",
    "GetServicePrincipalNameResponseTypeDef",
    "KeyUsageTypeDef",
    "KeyUsagePropertyTypeDef",
    "ListConnectorsRequestListConnectorsPaginateTypeDef",
    "ListDirectoryRegistrationsRequestListDirectoryRegistrationsPaginateTypeDef",
    "ListServicePrincipalNamesRequestListServicePrincipalNamesPaginateTypeDef",
    "ListTemplateGroupAccessControlEntriesRequestListTemplateGroupAccessControlEntriesPaginateTypeDef",
    "ListTemplatesRequestListTemplatesPaginateTypeDef",
    "ListServicePrincipalNamesResponseTypeDef",
    "ListTemplateGroupAccessControlEntriesResponseTypeDef",
    "GetTemplateGroupAccessControlEntryResponseTypeDef",
    "ListConnectorsResponsePaginatorTypeDef",
    "ListConnectorsResponseTypeDef",
    "GetConnectorResponseTypeDef",
    "ExtensionsV2PaginatorTypeDef",
    "ExtensionsV2TypeDef",
    "ExtensionsV3PaginatorTypeDef",
    "ExtensionsV3TypeDef",
    "ExtensionsV4PaginatorTypeDef",
    "ExtensionsV4TypeDef",
    "PrivateKeyAttributesV3PaginatorTypeDef",
    "PrivateKeyAttributesV3TypeDef",
    "PrivateKeyAttributesV4PaginatorTypeDef",
    "PrivateKeyAttributesV4TypeDef",
    "TemplateV2PaginatorTypeDef",
    "TemplateV2TypeDef",
    "TemplateV3PaginatorTypeDef",
    "TemplateV3TypeDef",
    "TemplateV4PaginatorTypeDef",
    "TemplateV4TypeDef",
    "TemplateDefinitionPaginatorTypeDef",
    "TemplateDefinitionTypeDef",
    "TemplateSummaryPaginatorTypeDef",
    "CreateTemplateRequestRequestTypeDef",
    "TemplateSummaryTypeDef",
    "TemplateTypeDef",
    "UpdateTemplateRequestRequestTypeDef",
    "ListTemplatesResponsePaginatorTypeDef",
    "ListTemplatesResponseTypeDef",
    "GetTemplateResponseTypeDef",
)

AccessRightsTypeDef = TypedDict(
    "AccessRightsTypeDef",
    {
        "AutoEnroll": NotRequired[AccessRightType],
        "Enroll": NotRequired[AccessRightType],
    },
)
ApplicationPolicyTypeDef = TypedDict(
    "ApplicationPolicyTypeDef",
    {
        "PolicyObjectIdentifier": NotRequired[str],
        "PolicyType": NotRequired[ApplicationPolicyTypeType],
    },
)
ValidityPeriodTypeDef = TypedDict(
    "ValidityPeriodTypeDef",
    {
        "Period": int,
        "PeriodType": ValidityPeriodTypeType,
    },
)
VpcInformationPaginatorTypeDef = TypedDict(
    "VpcInformationPaginatorTypeDef",
    {
        "SecurityGroupIds": List[str],
    },
)
VpcInformationTypeDef = TypedDict(
    "VpcInformationTypeDef",
    {
        "SecurityGroupIds": Sequence[str],
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
CreateDirectoryRegistrationRequestRequestTypeDef = TypedDict(
    "CreateDirectoryRegistrationRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "ClientToken": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
CreateServicePrincipalNameRequestRequestTypeDef = TypedDict(
    "CreateServicePrincipalNameRequestRequestTypeDef",
    {
        "ConnectorArn": str,
        "DirectoryRegistrationArn": str,
        "ClientToken": NotRequired[str],
    },
)
DeleteConnectorRequestRequestTypeDef = TypedDict(
    "DeleteConnectorRequestRequestTypeDef",
    {
        "ConnectorArn": str,
    },
)
DeleteDirectoryRegistrationRequestRequestTypeDef = TypedDict(
    "DeleteDirectoryRegistrationRequestRequestTypeDef",
    {
        "DirectoryRegistrationArn": str,
    },
)
DeleteServicePrincipalNameRequestRequestTypeDef = TypedDict(
    "DeleteServicePrincipalNameRequestRequestTypeDef",
    {
        "ConnectorArn": str,
        "DirectoryRegistrationArn": str,
    },
)
DeleteTemplateGroupAccessControlEntryRequestRequestTypeDef = TypedDict(
    "DeleteTemplateGroupAccessControlEntryRequestRequestTypeDef",
    {
        "GroupSecurityIdentifier": str,
        "TemplateArn": str,
    },
)
DeleteTemplateRequestRequestTypeDef = TypedDict(
    "DeleteTemplateRequestRequestTypeDef",
    {
        "TemplateArn": str,
    },
)
DirectoryRegistrationSummaryTypeDef = TypedDict(
    "DirectoryRegistrationSummaryTypeDef",
    {
        "Arn": NotRequired[str],
        "CreatedAt": NotRequired[datetime],
        "DirectoryId": NotRequired[str],
        "Status": NotRequired[DirectoryRegistrationStatusType],
        "StatusReason": NotRequired[DirectoryRegistrationStatusReasonType],
        "UpdatedAt": NotRequired[datetime],
    },
)
DirectoryRegistrationTypeDef = TypedDict(
    "DirectoryRegistrationTypeDef",
    {
        "Arn": NotRequired[str],
        "CreatedAt": NotRequired[datetime],
        "DirectoryId": NotRequired[str],
        "Status": NotRequired[DirectoryRegistrationStatusType],
        "StatusReason": NotRequired[DirectoryRegistrationStatusReasonType],
        "UpdatedAt": NotRequired[datetime],
    },
)
EnrollmentFlagsV2TypeDef = TypedDict(
    "EnrollmentFlagsV2TypeDef",
    {
        "EnableKeyReuseOnNtTokenKeysetStorageFull": NotRequired[bool],
        "IncludeSymmetricAlgorithms": NotRequired[bool],
        "NoSecurityExtension": NotRequired[bool],
        "RemoveInvalidCertificateFromPersonalStore": NotRequired[bool],
        "UserInteractionRequired": NotRequired[bool],
    },
)
EnrollmentFlagsV3TypeDef = TypedDict(
    "EnrollmentFlagsV3TypeDef",
    {
        "EnableKeyReuseOnNtTokenKeysetStorageFull": NotRequired[bool],
        "IncludeSymmetricAlgorithms": NotRequired[bool],
        "NoSecurityExtension": NotRequired[bool],
        "RemoveInvalidCertificateFromPersonalStore": NotRequired[bool],
        "UserInteractionRequired": NotRequired[bool],
    },
)
EnrollmentFlagsV4TypeDef = TypedDict(
    "EnrollmentFlagsV4TypeDef",
    {
        "EnableKeyReuseOnNtTokenKeysetStorageFull": NotRequired[bool],
        "IncludeSymmetricAlgorithms": NotRequired[bool],
        "NoSecurityExtension": NotRequired[bool],
        "RemoveInvalidCertificateFromPersonalStore": NotRequired[bool],
        "UserInteractionRequired": NotRequired[bool],
    },
)
GeneralFlagsV2TypeDef = TypedDict(
    "GeneralFlagsV2TypeDef",
    {
        "AutoEnrollment": NotRequired[bool],
        "MachineType": NotRequired[bool],
    },
)
GeneralFlagsV3TypeDef = TypedDict(
    "GeneralFlagsV3TypeDef",
    {
        "AutoEnrollment": NotRequired[bool],
        "MachineType": NotRequired[bool],
    },
)
GeneralFlagsV4TypeDef = TypedDict(
    "GeneralFlagsV4TypeDef",
    {
        "AutoEnrollment": NotRequired[bool],
        "MachineType": NotRequired[bool],
    },
)
GetConnectorRequestRequestTypeDef = TypedDict(
    "GetConnectorRequestRequestTypeDef",
    {
        "ConnectorArn": str,
    },
)
GetDirectoryRegistrationRequestRequestTypeDef = TypedDict(
    "GetDirectoryRegistrationRequestRequestTypeDef",
    {
        "DirectoryRegistrationArn": str,
    },
)
GetServicePrincipalNameRequestRequestTypeDef = TypedDict(
    "GetServicePrincipalNameRequestRequestTypeDef",
    {
        "ConnectorArn": str,
        "DirectoryRegistrationArn": str,
    },
)
ServicePrincipalNameTypeDef = TypedDict(
    "ServicePrincipalNameTypeDef",
    {
        "ConnectorArn": NotRequired[str],
        "CreatedAt": NotRequired[datetime],
        "DirectoryRegistrationArn": NotRequired[str],
        "Status": NotRequired[ServicePrincipalNameStatusType],
        "StatusReason": NotRequired[ServicePrincipalNameStatusReasonType],
        "UpdatedAt": NotRequired[datetime],
    },
)
GetTemplateGroupAccessControlEntryRequestRequestTypeDef = TypedDict(
    "GetTemplateGroupAccessControlEntryRequestRequestTypeDef",
    {
        "GroupSecurityIdentifier": str,
        "TemplateArn": str,
    },
)
GetTemplateRequestRequestTypeDef = TypedDict(
    "GetTemplateRequestRequestTypeDef",
    {
        "TemplateArn": str,
    },
)
KeyUsageFlagsTypeDef = TypedDict(
    "KeyUsageFlagsTypeDef",
    {
        "DataEncipherment": NotRequired[bool],
        "DigitalSignature": NotRequired[bool],
        "KeyAgreement": NotRequired[bool],
        "KeyEncipherment": NotRequired[bool],
        "NonRepudiation": NotRequired[bool],
    },
)
KeyUsagePropertyFlagsTypeDef = TypedDict(
    "KeyUsagePropertyFlagsTypeDef",
    {
        "Decrypt": NotRequired[bool],
        "KeyAgreement": NotRequired[bool],
        "Sign": NotRequired[bool],
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
ListConnectorsRequestRequestTypeDef = TypedDict(
    "ListConnectorsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListDirectoryRegistrationsRequestRequestTypeDef = TypedDict(
    "ListDirectoryRegistrationsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListServicePrincipalNamesRequestRequestTypeDef = TypedDict(
    "ListServicePrincipalNamesRequestRequestTypeDef",
    {
        "DirectoryRegistrationArn": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ServicePrincipalNameSummaryTypeDef = TypedDict(
    "ServicePrincipalNameSummaryTypeDef",
    {
        "ConnectorArn": NotRequired[str],
        "CreatedAt": NotRequired[datetime],
        "DirectoryRegistrationArn": NotRequired[str],
        "Status": NotRequired[ServicePrincipalNameStatusType],
        "StatusReason": NotRequired[ServicePrincipalNameStatusReasonType],
        "UpdatedAt": NotRequired[datetime],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
ListTemplateGroupAccessControlEntriesRequestRequestTypeDef = TypedDict(
    "ListTemplateGroupAccessControlEntriesRequestRequestTypeDef",
    {
        "TemplateArn": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListTemplatesRequestRequestTypeDef = TypedDict(
    "ListTemplatesRequestRequestTypeDef",
    {
        "ConnectorArn": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
PrivateKeyAttributesV2PaginatorTypeDef = TypedDict(
    "PrivateKeyAttributesV2PaginatorTypeDef",
    {
        "KeySpec": KeySpecType,
        "MinimalKeyLength": int,
        "CryptoProviders": NotRequired[List[str]],
    },
)
PrivateKeyAttributesV2TypeDef = TypedDict(
    "PrivateKeyAttributesV2TypeDef",
    {
        "KeySpec": KeySpecType,
        "MinimalKeyLength": int,
        "CryptoProviders": NotRequired[Sequence[str]],
    },
)
PrivateKeyFlagsV2TypeDef = TypedDict(
    "PrivateKeyFlagsV2TypeDef",
    {
        "ClientVersion": ClientCompatibilityV2Type,
        "ExportableKey": NotRequired[bool],
        "StrongKeyProtectionRequired": NotRequired[bool],
    },
)
PrivateKeyFlagsV3TypeDef = TypedDict(
    "PrivateKeyFlagsV3TypeDef",
    {
        "ClientVersion": ClientCompatibilityV3Type,
        "ExportableKey": NotRequired[bool],
        "RequireAlternateSignatureAlgorithm": NotRequired[bool],
        "StrongKeyProtectionRequired": NotRequired[bool],
    },
)
PrivateKeyFlagsV4TypeDef = TypedDict(
    "PrivateKeyFlagsV4TypeDef",
    {
        "ClientVersion": ClientCompatibilityV4Type,
        "ExportableKey": NotRequired[bool],
        "RequireAlternateSignatureAlgorithm": NotRequired[bool],
        "RequireSameKeyRenewal": NotRequired[bool],
        "StrongKeyProtectionRequired": NotRequired[bool],
        "UseLegacyProvider": NotRequired[bool],
    },
)
SubjectNameFlagsV2TypeDef = TypedDict(
    "SubjectNameFlagsV2TypeDef",
    {
        "RequireCommonName": NotRequired[bool],
        "RequireDirectoryPath": NotRequired[bool],
        "RequireDnsAsCn": NotRequired[bool],
        "RequireEmail": NotRequired[bool],
        "SanRequireDirectoryGuid": NotRequired[bool],
        "SanRequireDns": NotRequired[bool],
        "SanRequireDomainDns": NotRequired[bool],
        "SanRequireEmail": NotRequired[bool],
        "SanRequireSpn": NotRequired[bool],
        "SanRequireUpn": NotRequired[bool],
    },
)
SubjectNameFlagsV3TypeDef = TypedDict(
    "SubjectNameFlagsV3TypeDef",
    {
        "RequireCommonName": NotRequired[bool],
        "RequireDirectoryPath": NotRequired[bool],
        "RequireDnsAsCn": NotRequired[bool],
        "RequireEmail": NotRequired[bool],
        "SanRequireDirectoryGuid": NotRequired[bool],
        "SanRequireDns": NotRequired[bool],
        "SanRequireDomainDns": NotRequired[bool],
        "SanRequireEmail": NotRequired[bool],
        "SanRequireSpn": NotRequired[bool],
        "SanRequireUpn": NotRequired[bool],
    },
)
SubjectNameFlagsV4TypeDef = TypedDict(
    "SubjectNameFlagsV4TypeDef",
    {
        "RequireCommonName": NotRequired[bool],
        "RequireDirectoryPath": NotRequired[bool],
        "RequireDnsAsCn": NotRequired[bool],
        "RequireEmail": NotRequired[bool],
        "SanRequireDirectoryGuid": NotRequired[bool],
        "SanRequireDns": NotRequired[bool],
        "SanRequireDomainDns": NotRequired[bool],
        "SanRequireEmail": NotRequired[bool],
        "SanRequireSpn": NotRequired[bool],
        "SanRequireUpn": NotRequired[bool],
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Mapping[str, str],
    },
)
TemplateRevisionTypeDef = TypedDict(
    "TemplateRevisionTypeDef",
    {
        "MajorRevision": int,
        "MinorRevision": int,
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)
AccessControlEntrySummaryTypeDef = TypedDict(
    "AccessControlEntrySummaryTypeDef",
    {
        "AccessRights": NotRequired[AccessRightsTypeDef],
        "CreatedAt": NotRequired[datetime],
        "GroupDisplayName": NotRequired[str],
        "GroupSecurityIdentifier": NotRequired[str],
        "TemplateArn": NotRequired[str],
        "UpdatedAt": NotRequired[datetime],
    },
)
AccessControlEntryTypeDef = TypedDict(
    "AccessControlEntryTypeDef",
    {
        "AccessRights": NotRequired[AccessRightsTypeDef],
        "CreatedAt": NotRequired[datetime],
        "GroupDisplayName": NotRequired[str],
        "GroupSecurityIdentifier": NotRequired[str],
        "TemplateArn": NotRequired[str],
        "UpdatedAt": NotRequired[datetime],
    },
)
CreateTemplateGroupAccessControlEntryRequestRequestTypeDef = TypedDict(
    "CreateTemplateGroupAccessControlEntryRequestRequestTypeDef",
    {
        "AccessRights": AccessRightsTypeDef,
        "GroupDisplayName": str,
        "GroupSecurityIdentifier": str,
        "TemplateArn": str,
        "ClientToken": NotRequired[str],
    },
)
UpdateTemplateGroupAccessControlEntryRequestRequestTypeDef = TypedDict(
    "UpdateTemplateGroupAccessControlEntryRequestRequestTypeDef",
    {
        "GroupSecurityIdentifier": str,
        "TemplateArn": str,
        "AccessRights": NotRequired[AccessRightsTypeDef],
        "GroupDisplayName": NotRequired[str],
    },
)
ApplicationPoliciesPaginatorTypeDef = TypedDict(
    "ApplicationPoliciesPaginatorTypeDef",
    {
        "Policies": List[ApplicationPolicyTypeDef],
        "Critical": NotRequired[bool],
    },
)
ApplicationPoliciesTypeDef = TypedDict(
    "ApplicationPoliciesTypeDef",
    {
        "Policies": Sequence[ApplicationPolicyTypeDef],
        "Critical": NotRequired[bool],
    },
)
CertificateValidityTypeDef = TypedDict(
    "CertificateValidityTypeDef",
    {
        "RenewalPeriod": ValidityPeriodTypeDef,
        "ValidityPeriod": ValidityPeriodTypeDef,
    },
)
ConnectorSummaryPaginatorTypeDef = TypedDict(
    "ConnectorSummaryPaginatorTypeDef",
    {
        "Arn": NotRequired[str],
        "CertificateAuthorityArn": NotRequired[str],
        "CertificateEnrollmentPolicyServerEndpoint": NotRequired[str],
        "CreatedAt": NotRequired[datetime],
        "DirectoryId": NotRequired[str],
        "Status": NotRequired[ConnectorStatusType],
        "StatusReason": NotRequired[ConnectorStatusReasonType],
        "UpdatedAt": NotRequired[datetime],
        "VpcInformation": NotRequired[VpcInformationPaginatorTypeDef],
    },
)
ConnectorSummaryTypeDef = TypedDict(
    "ConnectorSummaryTypeDef",
    {
        "Arn": NotRequired[str],
        "CertificateAuthorityArn": NotRequired[str],
        "CertificateEnrollmentPolicyServerEndpoint": NotRequired[str],
        "CreatedAt": NotRequired[datetime],
        "DirectoryId": NotRequired[str],
        "Status": NotRequired[ConnectorStatusType],
        "StatusReason": NotRequired[ConnectorStatusReasonType],
        "UpdatedAt": NotRequired[datetime],
        "VpcInformation": NotRequired[VpcInformationTypeDef],
    },
)
ConnectorTypeDef = TypedDict(
    "ConnectorTypeDef",
    {
        "Arn": NotRequired[str],
        "CertificateAuthorityArn": NotRequired[str],
        "CertificateEnrollmentPolicyServerEndpoint": NotRequired[str],
        "CreatedAt": NotRequired[datetime],
        "DirectoryId": NotRequired[str],
        "Status": NotRequired[ConnectorStatusType],
        "StatusReason": NotRequired[ConnectorStatusReasonType],
        "UpdatedAt": NotRequired[datetime],
        "VpcInformation": NotRequired[VpcInformationTypeDef],
    },
)
CreateConnectorRequestRequestTypeDef = TypedDict(
    "CreateConnectorRequestRequestTypeDef",
    {
        "CertificateAuthorityArn": str,
        "DirectoryId": str,
        "VpcInformation": VpcInformationTypeDef,
        "ClientToken": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
CreateConnectorResponseTypeDef = TypedDict(
    "CreateConnectorResponseTypeDef",
    {
        "ConnectorArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDirectoryRegistrationResponseTypeDef = TypedDict(
    "CreateDirectoryRegistrationResponseTypeDef",
    {
        "DirectoryRegistrationArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateTemplateResponseTypeDef = TypedDict(
    "CreateTemplateResponseTypeDef",
    {
        "TemplateArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
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
ListDirectoryRegistrationsResponseTypeDef = TypedDict(
    "ListDirectoryRegistrationsResponseTypeDef",
    {
        "DirectoryRegistrations": List[DirectoryRegistrationSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetDirectoryRegistrationResponseTypeDef = TypedDict(
    "GetDirectoryRegistrationResponseTypeDef",
    {
        "DirectoryRegistration": DirectoryRegistrationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetServicePrincipalNameResponseTypeDef = TypedDict(
    "GetServicePrincipalNameResponseTypeDef",
    {
        "ServicePrincipalName": ServicePrincipalNameTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
KeyUsageTypeDef = TypedDict(
    "KeyUsageTypeDef",
    {
        "UsageFlags": KeyUsageFlagsTypeDef,
        "Critical": NotRequired[bool],
    },
)
KeyUsagePropertyTypeDef = TypedDict(
    "KeyUsagePropertyTypeDef",
    {
        "PropertyFlags": NotRequired[KeyUsagePropertyFlagsTypeDef],
        "PropertyType": NotRequired[Literal["ALL"]],
    },
)
ListConnectorsRequestListConnectorsPaginateTypeDef = TypedDict(
    "ListConnectorsRequestListConnectorsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDirectoryRegistrationsRequestListDirectoryRegistrationsPaginateTypeDef = TypedDict(
    "ListDirectoryRegistrationsRequestListDirectoryRegistrationsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListServicePrincipalNamesRequestListServicePrincipalNamesPaginateTypeDef = TypedDict(
    "ListServicePrincipalNamesRequestListServicePrincipalNamesPaginateTypeDef",
    {
        "DirectoryRegistrationArn": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListTemplateGroupAccessControlEntriesRequestListTemplateGroupAccessControlEntriesPaginateTypeDef = TypedDict(
    "ListTemplateGroupAccessControlEntriesRequestListTemplateGroupAccessControlEntriesPaginateTypeDef",
    {
        "TemplateArn": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListTemplatesRequestListTemplatesPaginateTypeDef = TypedDict(
    "ListTemplatesRequestListTemplatesPaginateTypeDef",
    {
        "ConnectorArn": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListServicePrincipalNamesResponseTypeDef = TypedDict(
    "ListServicePrincipalNamesResponseTypeDef",
    {
        "NextToken": str,
        "ServicePrincipalNames": List[ServicePrincipalNameSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTemplateGroupAccessControlEntriesResponseTypeDef = TypedDict(
    "ListTemplateGroupAccessControlEntriesResponseTypeDef",
    {
        "AccessControlEntries": List[AccessControlEntrySummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetTemplateGroupAccessControlEntryResponseTypeDef = TypedDict(
    "GetTemplateGroupAccessControlEntryResponseTypeDef",
    {
        "AccessControlEntry": AccessControlEntryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListConnectorsResponsePaginatorTypeDef = TypedDict(
    "ListConnectorsResponsePaginatorTypeDef",
    {
        "Connectors": List[ConnectorSummaryPaginatorTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListConnectorsResponseTypeDef = TypedDict(
    "ListConnectorsResponseTypeDef",
    {
        "Connectors": List[ConnectorSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetConnectorResponseTypeDef = TypedDict(
    "GetConnectorResponseTypeDef",
    {
        "Connector": ConnectorTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ExtensionsV2PaginatorTypeDef = TypedDict(
    "ExtensionsV2PaginatorTypeDef",
    {
        "KeyUsage": KeyUsageTypeDef,
        "ApplicationPolicies": NotRequired[ApplicationPoliciesPaginatorTypeDef],
    },
)
ExtensionsV2TypeDef = TypedDict(
    "ExtensionsV2TypeDef",
    {
        "KeyUsage": KeyUsageTypeDef,
        "ApplicationPolicies": NotRequired[ApplicationPoliciesTypeDef],
    },
)
ExtensionsV3PaginatorTypeDef = TypedDict(
    "ExtensionsV3PaginatorTypeDef",
    {
        "KeyUsage": KeyUsageTypeDef,
        "ApplicationPolicies": NotRequired[ApplicationPoliciesPaginatorTypeDef],
    },
)
ExtensionsV3TypeDef = TypedDict(
    "ExtensionsV3TypeDef",
    {
        "KeyUsage": KeyUsageTypeDef,
        "ApplicationPolicies": NotRequired[ApplicationPoliciesTypeDef],
    },
)
ExtensionsV4PaginatorTypeDef = TypedDict(
    "ExtensionsV4PaginatorTypeDef",
    {
        "KeyUsage": KeyUsageTypeDef,
        "ApplicationPolicies": NotRequired[ApplicationPoliciesPaginatorTypeDef],
    },
)
ExtensionsV4TypeDef = TypedDict(
    "ExtensionsV4TypeDef",
    {
        "KeyUsage": KeyUsageTypeDef,
        "ApplicationPolicies": NotRequired[ApplicationPoliciesTypeDef],
    },
)
PrivateKeyAttributesV3PaginatorTypeDef = TypedDict(
    "PrivateKeyAttributesV3PaginatorTypeDef",
    {
        "Algorithm": PrivateKeyAlgorithmType,
        "KeySpec": KeySpecType,
        "KeyUsageProperty": KeyUsagePropertyTypeDef,
        "MinimalKeyLength": int,
        "CryptoProviders": NotRequired[List[str]],
    },
)
PrivateKeyAttributesV3TypeDef = TypedDict(
    "PrivateKeyAttributesV3TypeDef",
    {
        "Algorithm": PrivateKeyAlgorithmType,
        "KeySpec": KeySpecType,
        "KeyUsageProperty": KeyUsagePropertyTypeDef,
        "MinimalKeyLength": int,
        "CryptoProviders": NotRequired[Sequence[str]],
    },
)
PrivateKeyAttributesV4PaginatorTypeDef = TypedDict(
    "PrivateKeyAttributesV4PaginatorTypeDef",
    {
        "KeySpec": KeySpecType,
        "MinimalKeyLength": int,
        "Algorithm": NotRequired[PrivateKeyAlgorithmType],
        "CryptoProviders": NotRequired[List[str]],
        "KeyUsageProperty": NotRequired[KeyUsagePropertyTypeDef],
    },
)
PrivateKeyAttributesV4TypeDef = TypedDict(
    "PrivateKeyAttributesV4TypeDef",
    {
        "KeySpec": KeySpecType,
        "MinimalKeyLength": int,
        "Algorithm": NotRequired[PrivateKeyAlgorithmType],
        "CryptoProviders": NotRequired[Sequence[str]],
        "KeyUsageProperty": NotRequired[KeyUsagePropertyTypeDef],
    },
)
TemplateV2PaginatorTypeDef = TypedDict(
    "TemplateV2PaginatorTypeDef",
    {
        "CertificateValidity": CertificateValidityTypeDef,
        "EnrollmentFlags": EnrollmentFlagsV2TypeDef,
        "Extensions": ExtensionsV2PaginatorTypeDef,
        "GeneralFlags": GeneralFlagsV2TypeDef,
        "PrivateKeyAttributes": PrivateKeyAttributesV2PaginatorTypeDef,
        "PrivateKeyFlags": PrivateKeyFlagsV2TypeDef,
        "SubjectNameFlags": SubjectNameFlagsV2TypeDef,
        "SupersededTemplates": NotRequired[List[str]],
    },
)
TemplateV2TypeDef = TypedDict(
    "TemplateV2TypeDef",
    {
        "CertificateValidity": CertificateValidityTypeDef,
        "EnrollmentFlags": EnrollmentFlagsV2TypeDef,
        "Extensions": ExtensionsV2TypeDef,
        "GeneralFlags": GeneralFlagsV2TypeDef,
        "PrivateKeyAttributes": PrivateKeyAttributesV2TypeDef,
        "PrivateKeyFlags": PrivateKeyFlagsV2TypeDef,
        "SubjectNameFlags": SubjectNameFlagsV2TypeDef,
        "SupersededTemplates": NotRequired[Sequence[str]],
    },
)
TemplateV3PaginatorTypeDef = TypedDict(
    "TemplateV3PaginatorTypeDef",
    {
        "CertificateValidity": CertificateValidityTypeDef,
        "EnrollmentFlags": EnrollmentFlagsV3TypeDef,
        "Extensions": ExtensionsV3PaginatorTypeDef,
        "GeneralFlags": GeneralFlagsV3TypeDef,
        "HashAlgorithm": HashAlgorithmType,
        "PrivateKeyAttributes": PrivateKeyAttributesV3PaginatorTypeDef,
        "PrivateKeyFlags": PrivateKeyFlagsV3TypeDef,
        "SubjectNameFlags": SubjectNameFlagsV3TypeDef,
        "SupersededTemplates": NotRequired[List[str]],
    },
)
TemplateV3TypeDef = TypedDict(
    "TemplateV3TypeDef",
    {
        "CertificateValidity": CertificateValidityTypeDef,
        "EnrollmentFlags": EnrollmentFlagsV3TypeDef,
        "Extensions": ExtensionsV3TypeDef,
        "GeneralFlags": GeneralFlagsV3TypeDef,
        "HashAlgorithm": HashAlgorithmType,
        "PrivateKeyAttributes": PrivateKeyAttributesV3TypeDef,
        "PrivateKeyFlags": PrivateKeyFlagsV3TypeDef,
        "SubjectNameFlags": SubjectNameFlagsV3TypeDef,
        "SupersededTemplates": NotRequired[Sequence[str]],
    },
)
TemplateV4PaginatorTypeDef = TypedDict(
    "TemplateV4PaginatorTypeDef",
    {
        "CertificateValidity": CertificateValidityTypeDef,
        "EnrollmentFlags": EnrollmentFlagsV4TypeDef,
        "Extensions": ExtensionsV4PaginatorTypeDef,
        "GeneralFlags": GeneralFlagsV4TypeDef,
        "PrivateKeyAttributes": PrivateKeyAttributesV4PaginatorTypeDef,
        "PrivateKeyFlags": PrivateKeyFlagsV4TypeDef,
        "SubjectNameFlags": SubjectNameFlagsV4TypeDef,
        "HashAlgorithm": NotRequired[HashAlgorithmType],
        "SupersededTemplates": NotRequired[List[str]],
    },
)
TemplateV4TypeDef = TypedDict(
    "TemplateV4TypeDef",
    {
        "CertificateValidity": CertificateValidityTypeDef,
        "EnrollmentFlags": EnrollmentFlagsV4TypeDef,
        "Extensions": ExtensionsV4TypeDef,
        "GeneralFlags": GeneralFlagsV4TypeDef,
        "PrivateKeyAttributes": PrivateKeyAttributesV4TypeDef,
        "PrivateKeyFlags": PrivateKeyFlagsV4TypeDef,
        "SubjectNameFlags": SubjectNameFlagsV4TypeDef,
        "HashAlgorithm": NotRequired[HashAlgorithmType],
        "SupersededTemplates": NotRequired[Sequence[str]],
    },
)
TemplateDefinitionPaginatorTypeDef = TypedDict(
    "TemplateDefinitionPaginatorTypeDef",
    {
        "TemplateV2": NotRequired[TemplateV2PaginatorTypeDef],
        "TemplateV3": NotRequired[TemplateV3PaginatorTypeDef],
        "TemplateV4": NotRequired[TemplateV4PaginatorTypeDef],
    },
)
TemplateDefinitionTypeDef = TypedDict(
    "TemplateDefinitionTypeDef",
    {
        "TemplateV2": NotRequired[TemplateV2TypeDef],
        "TemplateV3": NotRequired[TemplateV3TypeDef],
        "TemplateV4": NotRequired[TemplateV4TypeDef],
    },
)
TemplateSummaryPaginatorTypeDef = TypedDict(
    "TemplateSummaryPaginatorTypeDef",
    {
        "Arn": NotRequired[str],
        "ConnectorArn": NotRequired[str],
        "CreatedAt": NotRequired[datetime],
        "Definition": NotRequired[TemplateDefinitionPaginatorTypeDef],
        "Name": NotRequired[str],
        "ObjectIdentifier": NotRequired[str],
        "PolicySchema": NotRequired[int],
        "Revision": NotRequired[TemplateRevisionTypeDef],
        "Status": NotRequired[TemplateStatusType],
        "UpdatedAt": NotRequired[datetime],
    },
)
CreateTemplateRequestRequestTypeDef = TypedDict(
    "CreateTemplateRequestRequestTypeDef",
    {
        "ConnectorArn": str,
        "Definition": TemplateDefinitionTypeDef,
        "Name": str,
        "ClientToken": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
TemplateSummaryTypeDef = TypedDict(
    "TemplateSummaryTypeDef",
    {
        "Arn": NotRequired[str],
        "ConnectorArn": NotRequired[str],
        "CreatedAt": NotRequired[datetime],
        "Definition": NotRequired[TemplateDefinitionTypeDef],
        "Name": NotRequired[str],
        "ObjectIdentifier": NotRequired[str],
        "PolicySchema": NotRequired[int],
        "Revision": NotRequired[TemplateRevisionTypeDef],
        "Status": NotRequired[TemplateStatusType],
        "UpdatedAt": NotRequired[datetime],
    },
)
TemplateTypeDef = TypedDict(
    "TemplateTypeDef",
    {
        "Arn": NotRequired[str],
        "ConnectorArn": NotRequired[str],
        "CreatedAt": NotRequired[datetime],
        "Definition": NotRequired[TemplateDefinitionTypeDef],
        "Name": NotRequired[str],
        "ObjectIdentifier": NotRequired[str],
        "PolicySchema": NotRequired[int],
        "Revision": NotRequired[TemplateRevisionTypeDef],
        "Status": NotRequired[TemplateStatusType],
        "UpdatedAt": NotRequired[datetime],
    },
)
UpdateTemplateRequestRequestTypeDef = TypedDict(
    "UpdateTemplateRequestRequestTypeDef",
    {
        "TemplateArn": str,
        "Definition": NotRequired[TemplateDefinitionTypeDef],
        "ReenrollAllCertificateHolders": NotRequired[bool],
    },
)
ListTemplatesResponsePaginatorTypeDef = TypedDict(
    "ListTemplatesResponsePaginatorTypeDef",
    {
        "NextToken": str,
        "Templates": List[TemplateSummaryPaginatorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTemplatesResponseTypeDef = TypedDict(
    "ListTemplatesResponseTypeDef",
    {
        "NextToken": str,
        "Templates": List[TemplateSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetTemplateResponseTypeDef = TypedDict(
    "GetTemplateResponseTypeDef",
    {
        "Template": TemplateTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
