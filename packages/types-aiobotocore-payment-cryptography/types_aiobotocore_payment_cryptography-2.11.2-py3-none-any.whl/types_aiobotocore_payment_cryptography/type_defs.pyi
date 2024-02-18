"""
Type annotations for payment-cryptography service type definitions.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_payment_cryptography/type_defs/)

Usage::

    ```python
    from types_aiobotocore_payment_cryptography.type_defs import AliasTypeDef

    data: AliasTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Sequence

from .literals import (
    KeyAlgorithmType,
    KeyCheckValueAlgorithmType,
    KeyClassType,
    KeyMaterialTypeType,
    KeyOriginType,
    KeyStateType,
    KeyUsageType,
    WrappedKeyMaterialFormatType,
    WrappingKeySpecType,
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
    "AliasTypeDef",
    "CreateAliasInputRequestTypeDef",
    "ResponseMetadataTypeDef",
    "TagTypeDef",
    "DeleteAliasInputRequestTypeDef",
    "DeleteKeyInputRequestTypeDef",
    "ExportDukptInitialKeyTypeDef",
    "ExportKeyCryptogramTypeDef",
    "ExportTr31KeyBlockTypeDef",
    "ExportTr34KeyBlockTypeDef",
    "WrappedKeyTypeDef",
    "GetAliasInputRequestTypeDef",
    "GetKeyInputRequestTypeDef",
    "GetParametersForExportInputRequestTypeDef",
    "GetParametersForImportInputRequestTypeDef",
    "GetPublicKeyCertificateInputRequestTypeDef",
    "ImportTr31KeyBlockTypeDef",
    "ImportTr34KeyBlockTypeDef",
    "KeyModesOfUseTypeDef",
    "PaginatorConfigTypeDef",
    "ListAliasesInputRequestTypeDef",
    "ListKeysInputRequestTypeDef",
    "ListTagsForResourceInputRequestTypeDef",
    "RestoreKeyInputRequestTypeDef",
    "StartKeyUsageInputRequestTypeDef",
    "StopKeyUsageInputRequestTypeDef",
    "UntagResourceInputRequestTypeDef",
    "UpdateAliasInputRequestTypeDef",
    "CreateAliasOutputTypeDef",
    "GetAliasOutputTypeDef",
    "GetParametersForExportOutputTypeDef",
    "GetParametersForImportOutputTypeDef",
    "GetPublicKeyCertificateOutputTypeDef",
    "ListAliasesOutputTypeDef",
    "UpdateAliasOutputTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "TagResourceInputRequestTypeDef",
    "ExportAttributesTypeDef",
    "ExportKeyMaterialTypeDef",
    "ExportKeyOutputTypeDef",
    "KeyAttributesTypeDef",
    "ListAliasesInputListAliasesPaginateTypeDef",
    "ListKeysInputListKeysPaginateTypeDef",
    "ListTagsForResourceInputListTagsForResourcePaginateTypeDef",
    "ExportKeyInputRequestTypeDef",
    "CreateKeyInputRequestTypeDef",
    "ImportKeyCryptogramTypeDef",
    "KeySummaryTypeDef",
    "KeyTypeDef",
    "RootCertificatePublicKeyTypeDef",
    "TrustedCertificatePublicKeyTypeDef",
    "ListKeysOutputTypeDef",
    "CreateKeyOutputTypeDef",
    "DeleteKeyOutputTypeDef",
    "GetKeyOutputTypeDef",
    "ImportKeyOutputTypeDef",
    "RestoreKeyOutputTypeDef",
    "StartKeyUsageOutputTypeDef",
    "StopKeyUsageOutputTypeDef",
    "ImportKeyMaterialTypeDef",
    "ImportKeyInputRequestTypeDef",
)

AliasTypeDef = TypedDict(
    "AliasTypeDef",
    {
        "AliasName": str,
        "KeyArn": NotRequired[str],
    },
)
CreateAliasInputRequestTypeDef = TypedDict(
    "CreateAliasInputRequestTypeDef",
    {
        "AliasName": str,
        "KeyArn": NotRequired[str],
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
DeleteAliasInputRequestTypeDef = TypedDict(
    "DeleteAliasInputRequestTypeDef",
    {
        "AliasName": str,
    },
)
DeleteKeyInputRequestTypeDef = TypedDict(
    "DeleteKeyInputRequestTypeDef",
    {
        "KeyIdentifier": str,
        "DeleteKeyInDays": NotRequired[int],
    },
)
ExportDukptInitialKeyTypeDef = TypedDict(
    "ExportDukptInitialKeyTypeDef",
    {
        "KeySerialNumber": str,
    },
)
ExportKeyCryptogramTypeDef = TypedDict(
    "ExportKeyCryptogramTypeDef",
    {
        "CertificateAuthorityPublicKeyIdentifier": str,
        "WrappingKeyCertificate": str,
        "WrappingSpec": NotRequired[WrappingKeySpecType],
    },
)
ExportTr31KeyBlockTypeDef = TypedDict(
    "ExportTr31KeyBlockTypeDef",
    {
        "WrappingKeyIdentifier": str,
    },
)
ExportTr34KeyBlockTypeDef = TypedDict(
    "ExportTr34KeyBlockTypeDef",
    {
        "CertificateAuthorityPublicKeyIdentifier": str,
        "ExportToken": str,
        "KeyBlockFormat": Literal["X9_TR34_2012"],
        "WrappingKeyCertificate": str,
        "RandomNonce": NotRequired[str],
    },
)
WrappedKeyTypeDef = TypedDict(
    "WrappedKeyTypeDef",
    {
        "KeyMaterial": str,
        "WrappedKeyMaterialFormat": WrappedKeyMaterialFormatType,
        "WrappingKeyArn": str,
        "KeyCheckValue": NotRequired[str],
        "KeyCheckValueAlgorithm": NotRequired[KeyCheckValueAlgorithmType],
    },
)
GetAliasInputRequestTypeDef = TypedDict(
    "GetAliasInputRequestTypeDef",
    {
        "AliasName": str,
    },
)
GetKeyInputRequestTypeDef = TypedDict(
    "GetKeyInputRequestTypeDef",
    {
        "KeyIdentifier": str,
    },
)
GetParametersForExportInputRequestTypeDef = TypedDict(
    "GetParametersForExportInputRequestTypeDef",
    {
        "KeyMaterialType": KeyMaterialTypeType,
        "SigningKeyAlgorithm": KeyAlgorithmType,
    },
)
GetParametersForImportInputRequestTypeDef = TypedDict(
    "GetParametersForImportInputRequestTypeDef",
    {
        "KeyMaterialType": KeyMaterialTypeType,
        "WrappingKeyAlgorithm": KeyAlgorithmType,
    },
)
GetPublicKeyCertificateInputRequestTypeDef = TypedDict(
    "GetPublicKeyCertificateInputRequestTypeDef",
    {
        "KeyIdentifier": str,
    },
)
ImportTr31KeyBlockTypeDef = TypedDict(
    "ImportTr31KeyBlockTypeDef",
    {
        "WrappedKeyBlock": str,
        "WrappingKeyIdentifier": str,
    },
)
ImportTr34KeyBlockTypeDef = TypedDict(
    "ImportTr34KeyBlockTypeDef",
    {
        "CertificateAuthorityPublicKeyIdentifier": str,
        "ImportToken": str,
        "KeyBlockFormat": Literal["X9_TR34_2012"],
        "SigningKeyCertificate": str,
        "WrappedKeyBlock": str,
        "RandomNonce": NotRequired[str],
    },
)
KeyModesOfUseTypeDef = TypedDict(
    "KeyModesOfUseTypeDef",
    {
        "Decrypt": NotRequired[bool],
        "DeriveKey": NotRequired[bool],
        "Encrypt": NotRequired[bool],
        "Generate": NotRequired[bool],
        "NoRestrictions": NotRequired[bool],
        "Sign": NotRequired[bool],
        "Unwrap": NotRequired[bool],
        "Verify": NotRequired[bool],
        "Wrap": NotRequired[bool],
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
ListAliasesInputRequestTypeDef = TypedDict(
    "ListAliasesInputRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListKeysInputRequestTypeDef = TypedDict(
    "ListKeysInputRequestTypeDef",
    {
        "KeyState": NotRequired[KeyStateType],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListTagsForResourceInputRequestTypeDef = TypedDict(
    "ListTagsForResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
RestoreKeyInputRequestTypeDef = TypedDict(
    "RestoreKeyInputRequestTypeDef",
    {
        "KeyIdentifier": str,
    },
)
StartKeyUsageInputRequestTypeDef = TypedDict(
    "StartKeyUsageInputRequestTypeDef",
    {
        "KeyIdentifier": str,
    },
)
StopKeyUsageInputRequestTypeDef = TypedDict(
    "StopKeyUsageInputRequestTypeDef",
    {
        "KeyIdentifier": str,
    },
)
UntagResourceInputRequestTypeDef = TypedDict(
    "UntagResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)
UpdateAliasInputRequestTypeDef = TypedDict(
    "UpdateAliasInputRequestTypeDef",
    {
        "AliasName": str,
        "KeyArn": NotRequired[str],
    },
)
CreateAliasOutputTypeDef = TypedDict(
    "CreateAliasOutputTypeDef",
    {
        "Alias": AliasTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAliasOutputTypeDef = TypedDict(
    "GetAliasOutputTypeDef",
    {
        "Alias": AliasTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetParametersForExportOutputTypeDef = TypedDict(
    "GetParametersForExportOutputTypeDef",
    {
        "ExportToken": str,
        "ParametersValidUntilTimestamp": datetime,
        "SigningKeyAlgorithm": KeyAlgorithmType,
        "SigningKeyCertificate": str,
        "SigningKeyCertificateChain": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetParametersForImportOutputTypeDef = TypedDict(
    "GetParametersForImportOutputTypeDef",
    {
        "ImportToken": str,
        "ParametersValidUntilTimestamp": datetime,
        "WrappingKeyAlgorithm": KeyAlgorithmType,
        "WrappingKeyCertificate": str,
        "WrappingKeyCertificateChain": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetPublicKeyCertificateOutputTypeDef = TypedDict(
    "GetPublicKeyCertificateOutputTypeDef",
    {
        "KeyCertificate": str,
        "KeyCertificateChain": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAliasesOutputTypeDef = TypedDict(
    "ListAliasesOutputTypeDef",
    {
        "Aliases": List[AliasTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateAliasOutputTypeDef = TypedDict(
    "UpdateAliasOutputTypeDef",
    {
        "Alias": AliasTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {
        "NextToken": str,
        "Tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TagResourceInputRequestTypeDef = TypedDict(
    "TagResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Sequence[TagTypeDef],
    },
)
ExportAttributesTypeDef = TypedDict(
    "ExportAttributesTypeDef",
    {
        "ExportDukptInitialKey": NotRequired[ExportDukptInitialKeyTypeDef],
        "KeyCheckValueAlgorithm": NotRequired[KeyCheckValueAlgorithmType],
    },
)
ExportKeyMaterialTypeDef = TypedDict(
    "ExportKeyMaterialTypeDef",
    {
        "KeyCryptogram": NotRequired[ExportKeyCryptogramTypeDef],
        "Tr31KeyBlock": NotRequired[ExportTr31KeyBlockTypeDef],
        "Tr34KeyBlock": NotRequired[ExportTr34KeyBlockTypeDef],
    },
)
ExportKeyOutputTypeDef = TypedDict(
    "ExportKeyOutputTypeDef",
    {
        "WrappedKey": WrappedKeyTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
KeyAttributesTypeDef = TypedDict(
    "KeyAttributesTypeDef",
    {
        "KeyAlgorithm": KeyAlgorithmType,
        "KeyClass": KeyClassType,
        "KeyModesOfUse": KeyModesOfUseTypeDef,
        "KeyUsage": KeyUsageType,
    },
)
ListAliasesInputListAliasesPaginateTypeDef = TypedDict(
    "ListAliasesInputListAliasesPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListKeysInputListKeysPaginateTypeDef = TypedDict(
    "ListKeysInputListKeysPaginateTypeDef",
    {
        "KeyState": NotRequired[KeyStateType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListTagsForResourceInputListTagsForResourcePaginateTypeDef = TypedDict(
    "ListTagsForResourceInputListTagsForResourcePaginateTypeDef",
    {
        "ResourceArn": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ExportKeyInputRequestTypeDef = TypedDict(
    "ExportKeyInputRequestTypeDef",
    {
        "ExportKeyIdentifier": str,
        "KeyMaterial": ExportKeyMaterialTypeDef,
        "ExportAttributes": NotRequired[ExportAttributesTypeDef],
    },
)
CreateKeyInputRequestTypeDef = TypedDict(
    "CreateKeyInputRequestTypeDef",
    {
        "Exportable": bool,
        "KeyAttributes": KeyAttributesTypeDef,
        "Enabled": NotRequired[bool],
        "KeyCheckValueAlgorithm": NotRequired[KeyCheckValueAlgorithmType],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
ImportKeyCryptogramTypeDef = TypedDict(
    "ImportKeyCryptogramTypeDef",
    {
        "Exportable": bool,
        "ImportToken": str,
        "KeyAttributes": KeyAttributesTypeDef,
        "WrappedKeyCryptogram": str,
        "WrappingSpec": NotRequired[WrappingKeySpecType],
    },
)
KeySummaryTypeDef = TypedDict(
    "KeySummaryTypeDef",
    {
        "Enabled": bool,
        "Exportable": bool,
        "KeyArn": str,
        "KeyAttributes": KeyAttributesTypeDef,
        "KeyCheckValue": str,
        "KeyState": KeyStateType,
    },
)
KeyTypeDef = TypedDict(
    "KeyTypeDef",
    {
        "CreateTimestamp": datetime,
        "Enabled": bool,
        "Exportable": bool,
        "KeyArn": str,
        "KeyAttributes": KeyAttributesTypeDef,
        "KeyCheckValue": str,
        "KeyCheckValueAlgorithm": KeyCheckValueAlgorithmType,
        "KeyOrigin": KeyOriginType,
        "KeyState": KeyStateType,
        "DeletePendingTimestamp": NotRequired[datetime],
        "DeleteTimestamp": NotRequired[datetime],
        "UsageStartTimestamp": NotRequired[datetime],
        "UsageStopTimestamp": NotRequired[datetime],
    },
)
RootCertificatePublicKeyTypeDef = TypedDict(
    "RootCertificatePublicKeyTypeDef",
    {
        "KeyAttributes": KeyAttributesTypeDef,
        "PublicKeyCertificate": str,
    },
)
TrustedCertificatePublicKeyTypeDef = TypedDict(
    "TrustedCertificatePublicKeyTypeDef",
    {
        "CertificateAuthorityPublicKeyIdentifier": str,
        "KeyAttributes": KeyAttributesTypeDef,
        "PublicKeyCertificate": str,
    },
)
ListKeysOutputTypeDef = TypedDict(
    "ListKeysOutputTypeDef",
    {
        "Keys": List[KeySummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateKeyOutputTypeDef = TypedDict(
    "CreateKeyOutputTypeDef",
    {
        "Key": KeyTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteKeyOutputTypeDef = TypedDict(
    "DeleteKeyOutputTypeDef",
    {
        "Key": KeyTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetKeyOutputTypeDef = TypedDict(
    "GetKeyOutputTypeDef",
    {
        "Key": KeyTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ImportKeyOutputTypeDef = TypedDict(
    "ImportKeyOutputTypeDef",
    {
        "Key": KeyTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RestoreKeyOutputTypeDef = TypedDict(
    "RestoreKeyOutputTypeDef",
    {
        "Key": KeyTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartKeyUsageOutputTypeDef = TypedDict(
    "StartKeyUsageOutputTypeDef",
    {
        "Key": KeyTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StopKeyUsageOutputTypeDef = TypedDict(
    "StopKeyUsageOutputTypeDef",
    {
        "Key": KeyTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ImportKeyMaterialTypeDef = TypedDict(
    "ImportKeyMaterialTypeDef",
    {
        "KeyCryptogram": NotRequired[ImportKeyCryptogramTypeDef],
        "RootCertificatePublicKey": NotRequired[RootCertificatePublicKeyTypeDef],
        "Tr31KeyBlock": NotRequired[ImportTr31KeyBlockTypeDef],
        "Tr34KeyBlock": NotRequired[ImportTr34KeyBlockTypeDef],
        "TrustedCertificatePublicKey": NotRequired[TrustedCertificatePublicKeyTypeDef],
    },
)
ImportKeyInputRequestTypeDef = TypedDict(
    "ImportKeyInputRequestTypeDef",
    {
        "KeyMaterial": ImportKeyMaterialTypeDef,
        "Enabled": NotRequired[bool],
        "KeyCheckValueAlgorithm": NotRequired[KeyCheckValueAlgorithmType],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
