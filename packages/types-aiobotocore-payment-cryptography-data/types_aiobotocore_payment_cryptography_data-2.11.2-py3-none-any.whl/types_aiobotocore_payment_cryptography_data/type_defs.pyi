"""
Type annotations for payment-cryptography-data service type definitions.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_payment_cryptography_data/type_defs/)

Usage::

    ```python
    from types_aiobotocore_payment_cryptography_data.type_defs import AmexCardSecurityCodeVersion1TypeDef

    data: AmexCardSecurityCodeVersion1TypeDef = ...
    ```
"""

import sys
from typing import Any, Dict, Mapping

from .literals import (
    DukptDerivationTypeType,
    DukptEncryptionModeType,
    DukptKeyVariantType,
    EncryptionModeType,
    MacAlgorithmType,
    MajorKeyDerivationModeType,
    PaddingTypeType,
    PinBlockFormatForPinDataType,
    SessionKeyDerivationModeType,
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
    "AmexCardSecurityCodeVersion1TypeDef",
    "AmexCardSecurityCodeVersion2TypeDef",
    "AsymmetricEncryptionAttributesTypeDef",
    "CardHolderVerificationValueTypeDef",
    "CardVerificationValue1TypeDef",
    "CardVerificationValue2TypeDef",
    "DynamicCardVerificationCodeTypeDef",
    "DynamicCardVerificationValueTypeDef",
    "DiscoverDynamicCardVerificationCodeTypeDef",
    "CryptogramVerificationArpcMethod1TypeDef",
    "CryptogramVerificationArpcMethod2TypeDef",
    "ResponseMetadataTypeDef",
    "DukptAttributesTypeDef",
    "DukptDerivationAttributesTypeDef",
    "DukptEncryptionAttributesTypeDef",
    "SymmetricEncryptionAttributesTypeDef",
    "PinDataTypeDef",
    "Ibm3624NaturalPinTypeDef",
    "Ibm3624PinFromOffsetTypeDef",
    "Ibm3624PinOffsetTypeDef",
    "Ibm3624PinVerificationTypeDef",
    "Ibm3624RandomPinTypeDef",
    "MacAlgorithmDukptTypeDef",
    "SessionKeyDerivationValueTypeDef",
    "VisaPinTypeDef",
    "VisaPinVerificationValueTypeDef",
    "VisaPinVerificationTypeDef",
    "SessionKeyAmexTypeDef",
    "SessionKeyEmv2000TypeDef",
    "SessionKeyEmvCommonTypeDef",
    "SessionKeyMastercardTypeDef",
    "SessionKeyVisaTypeDef",
    "TranslationPinDataIsoFormat034TypeDef",
    "CardGenerationAttributesTypeDef",
    "CardVerificationAttributesTypeDef",
    "CryptogramAuthResponseTypeDef",
    "DecryptDataOutputTypeDef",
    "EncryptDataOutputTypeDef",
    "GenerateCardValidationDataOutputTypeDef",
    "GenerateMacOutputTypeDef",
    "ReEncryptDataOutputTypeDef",
    "TranslatePinDataOutputTypeDef",
    "VerifyAuthRequestCryptogramOutputTypeDef",
    "VerifyCardValidationDataOutputTypeDef",
    "VerifyMacOutputTypeDef",
    "VerifyPinDataOutputTypeDef",
    "EncryptionDecryptionAttributesTypeDef",
    "ReEncryptionAttributesTypeDef",
    "GeneratePinDataOutputTypeDef",
    "MacAlgorithmEmvTypeDef",
    "PinGenerationAttributesTypeDef",
    "PinVerificationAttributesTypeDef",
    "SessionKeyDerivationTypeDef",
    "TranslationIsoFormatsTypeDef",
    "GenerateCardValidationDataInputRequestTypeDef",
    "VerifyCardValidationDataInputRequestTypeDef",
    "DecryptDataInputRequestTypeDef",
    "EncryptDataInputRequestTypeDef",
    "ReEncryptDataInputRequestTypeDef",
    "MacAttributesTypeDef",
    "GeneratePinDataInputRequestTypeDef",
    "VerifyPinDataInputRequestTypeDef",
    "VerifyAuthRequestCryptogramInputRequestTypeDef",
    "TranslatePinDataInputRequestTypeDef",
    "GenerateMacInputRequestTypeDef",
    "VerifyMacInputRequestTypeDef",
)

AmexCardSecurityCodeVersion1TypeDef = TypedDict(
    "AmexCardSecurityCodeVersion1TypeDef",
    {
        "CardExpiryDate": str,
    },
)
AmexCardSecurityCodeVersion2TypeDef = TypedDict(
    "AmexCardSecurityCodeVersion2TypeDef",
    {
        "CardExpiryDate": str,
        "ServiceCode": str,
    },
)
AsymmetricEncryptionAttributesTypeDef = TypedDict(
    "AsymmetricEncryptionAttributesTypeDef",
    {
        "PaddingType": NotRequired[PaddingTypeType],
    },
)
CardHolderVerificationValueTypeDef = TypedDict(
    "CardHolderVerificationValueTypeDef",
    {
        "ApplicationTransactionCounter": str,
        "PanSequenceNumber": str,
        "UnpredictableNumber": str,
    },
)
CardVerificationValue1TypeDef = TypedDict(
    "CardVerificationValue1TypeDef",
    {
        "CardExpiryDate": str,
        "ServiceCode": str,
    },
)
CardVerificationValue2TypeDef = TypedDict(
    "CardVerificationValue2TypeDef",
    {
        "CardExpiryDate": str,
    },
)
DynamicCardVerificationCodeTypeDef = TypedDict(
    "DynamicCardVerificationCodeTypeDef",
    {
        "ApplicationTransactionCounter": str,
        "PanSequenceNumber": str,
        "TrackData": str,
        "UnpredictableNumber": str,
    },
)
DynamicCardVerificationValueTypeDef = TypedDict(
    "DynamicCardVerificationValueTypeDef",
    {
        "ApplicationTransactionCounter": str,
        "CardExpiryDate": str,
        "PanSequenceNumber": str,
        "ServiceCode": str,
    },
)
DiscoverDynamicCardVerificationCodeTypeDef = TypedDict(
    "DiscoverDynamicCardVerificationCodeTypeDef",
    {
        "ApplicationTransactionCounter": str,
        "CardExpiryDate": str,
        "UnpredictableNumber": str,
    },
)
CryptogramVerificationArpcMethod1TypeDef = TypedDict(
    "CryptogramVerificationArpcMethod1TypeDef",
    {
        "AuthResponseCode": str,
    },
)
CryptogramVerificationArpcMethod2TypeDef = TypedDict(
    "CryptogramVerificationArpcMethod2TypeDef",
    {
        "CardStatusUpdate": str,
        "ProprietaryAuthenticationData": NotRequired[str],
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
DukptAttributesTypeDef = TypedDict(
    "DukptAttributesTypeDef",
    {
        "DukptDerivationType": DukptDerivationTypeType,
        "KeySerialNumber": str,
    },
)
DukptDerivationAttributesTypeDef = TypedDict(
    "DukptDerivationAttributesTypeDef",
    {
        "KeySerialNumber": str,
        "DukptKeyDerivationType": NotRequired[DukptDerivationTypeType],
        "DukptKeyVariant": NotRequired[DukptKeyVariantType],
    },
)
DukptEncryptionAttributesTypeDef = TypedDict(
    "DukptEncryptionAttributesTypeDef",
    {
        "KeySerialNumber": str,
        "DukptKeyDerivationType": NotRequired[DukptDerivationTypeType],
        "DukptKeyVariant": NotRequired[DukptKeyVariantType],
        "InitializationVector": NotRequired[str],
        "Mode": NotRequired[DukptEncryptionModeType],
    },
)
SymmetricEncryptionAttributesTypeDef = TypedDict(
    "SymmetricEncryptionAttributesTypeDef",
    {
        "Mode": EncryptionModeType,
        "InitializationVector": NotRequired[str],
        "PaddingType": NotRequired[PaddingTypeType],
    },
)
PinDataTypeDef = TypedDict(
    "PinDataTypeDef",
    {
        "PinOffset": NotRequired[str],
        "VerificationValue": NotRequired[str],
    },
)
Ibm3624NaturalPinTypeDef = TypedDict(
    "Ibm3624NaturalPinTypeDef",
    {
        "DecimalizationTable": str,
        "PinValidationData": str,
        "PinValidationDataPadCharacter": str,
    },
)
Ibm3624PinFromOffsetTypeDef = TypedDict(
    "Ibm3624PinFromOffsetTypeDef",
    {
        "DecimalizationTable": str,
        "PinOffset": str,
        "PinValidationData": str,
        "PinValidationDataPadCharacter": str,
    },
)
Ibm3624PinOffsetTypeDef = TypedDict(
    "Ibm3624PinOffsetTypeDef",
    {
        "DecimalizationTable": str,
        "EncryptedPinBlock": str,
        "PinValidationData": str,
        "PinValidationDataPadCharacter": str,
    },
)
Ibm3624PinVerificationTypeDef = TypedDict(
    "Ibm3624PinVerificationTypeDef",
    {
        "DecimalizationTable": str,
        "PinOffset": str,
        "PinValidationData": str,
        "PinValidationDataPadCharacter": str,
    },
)
Ibm3624RandomPinTypeDef = TypedDict(
    "Ibm3624RandomPinTypeDef",
    {
        "DecimalizationTable": str,
        "PinValidationData": str,
        "PinValidationDataPadCharacter": str,
    },
)
MacAlgorithmDukptTypeDef = TypedDict(
    "MacAlgorithmDukptTypeDef",
    {
        "DukptKeyVariant": DukptKeyVariantType,
        "KeySerialNumber": str,
        "DukptDerivationType": NotRequired[DukptDerivationTypeType],
    },
)
SessionKeyDerivationValueTypeDef = TypedDict(
    "SessionKeyDerivationValueTypeDef",
    {
        "ApplicationCryptogram": NotRequired[str],
        "ApplicationTransactionCounter": NotRequired[str],
    },
)
VisaPinTypeDef = TypedDict(
    "VisaPinTypeDef",
    {
        "PinVerificationKeyIndex": int,
    },
)
VisaPinVerificationValueTypeDef = TypedDict(
    "VisaPinVerificationValueTypeDef",
    {
        "EncryptedPinBlock": str,
        "PinVerificationKeyIndex": int,
    },
)
VisaPinVerificationTypeDef = TypedDict(
    "VisaPinVerificationTypeDef",
    {
        "PinVerificationKeyIndex": int,
        "VerificationValue": str,
    },
)
SessionKeyAmexTypeDef = TypedDict(
    "SessionKeyAmexTypeDef",
    {
        "PanSequenceNumber": str,
        "PrimaryAccountNumber": str,
    },
)
SessionKeyEmv2000TypeDef = TypedDict(
    "SessionKeyEmv2000TypeDef",
    {
        "ApplicationTransactionCounter": str,
        "PanSequenceNumber": str,
        "PrimaryAccountNumber": str,
    },
)
SessionKeyEmvCommonTypeDef = TypedDict(
    "SessionKeyEmvCommonTypeDef",
    {
        "ApplicationTransactionCounter": str,
        "PanSequenceNumber": str,
        "PrimaryAccountNumber": str,
    },
)
SessionKeyMastercardTypeDef = TypedDict(
    "SessionKeyMastercardTypeDef",
    {
        "ApplicationTransactionCounter": str,
        "PanSequenceNumber": str,
        "PrimaryAccountNumber": str,
        "UnpredictableNumber": str,
    },
)
SessionKeyVisaTypeDef = TypedDict(
    "SessionKeyVisaTypeDef",
    {
        "PanSequenceNumber": str,
        "PrimaryAccountNumber": str,
    },
)
TranslationPinDataIsoFormat034TypeDef = TypedDict(
    "TranslationPinDataIsoFormat034TypeDef",
    {
        "PrimaryAccountNumber": str,
    },
)
CardGenerationAttributesTypeDef = TypedDict(
    "CardGenerationAttributesTypeDef",
    {
        "AmexCardSecurityCodeVersion1": NotRequired[AmexCardSecurityCodeVersion1TypeDef],
        "AmexCardSecurityCodeVersion2": NotRequired[AmexCardSecurityCodeVersion2TypeDef],
        "CardHolderVerificationValue": NotRequired[CardHolderVerificationValueTypeDef],
        "CardVerificationValue1": NotRequired[CardVerificationValue1TypeDef],
        "CardVerificationValue2": NotRequired[CardVerificationValue2TypeDef],
        "DynamicCardVerificationCode": NotRequired[DynamicCardVerificationCodeTypeDef],
        "DynamicCardVerificationValue": NotRequired[DynamicCardVerificationValueTypeDef],
    },
)
CardVerificationAttributesTypeDef = TypedDict(
    "CardVerificationAttributesTypeDef",
    {
        "AmexCardSecurityCodeVersion1": NotRequired[AmexCardSecurityCodeVersion1TypeDef],
        "AmexCardSecurityCodeVersion2": NotRequired[AmexCardSecurityCodeVersion2TypeDef],
        "CardHolderVerificationValue": NotRequired[CardHolderVerificationValueTypeDef],
        "CardVerificationValue1": NotRequired[CardVerificationValue1TypeDef],
        "CardVerificationValue2": NotRequired[CardVerificationValue2TypeDef],
        "DiscoverDynamicCardVerificationCode": NotRequired[
            DiscoverDynamicCardVerificationCodeTypeDef
        ],
        "DynamicCardVerificationCode": NotRequired[DynamicCardVerificationCodeTypeDef],
        "DynamicCardVerificationValue": NotRequired[DynamicCardVerificationValueTypeDef],
    },
)
CryptogramAuthResponseTypeDef = TypedDict(
    "CryptogramAuthResponseTypeDef",
    {
        "ArpcMethod1": NotRequired[CryptogramVerificationArpcMethod1TypeDef],
        "ArpcMethod2": NotRequired[CryptogramVerificationArpcMethod2TypeDef],
    },
)
DecryptDataOutputTypeDef = TypedDict(
    "DecryptDataOutputTypeDef",
    {
        "KeyArn": str,
        "KeyCheckValue": str,
        "PlainText": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EncryptDataOutputTypeDef = TypedDict(
    "EncryptDataOutputTypeDef",
    {
        "CipherText": str,
        "KeyArn": str,
        "KeyCheckValue": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GenerateCardValidationDataOutputTypeDef = TypedDict(
    "GenerateCardValidationDataOutputTypeDef",
    {
        "KeyArn": str,
        "KeyCheckValue": str,
        "ValidationData": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GenerateMacOutputTypeDef = TypedDict(
    "GenerateMacOutputTypeDef",
    {
        "KeyArn": str,
        "KeyCheckValue": str,
        "Mac": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ReEncryptDataOutputTypeDef = TypedDict(
    "ReEncryptDataOutputTypeDef",
    {
        "CipherText": str,
        "KeyArn": str,
        "KeyCheckValue": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TranslatePinDataOutputTypeDef = TypedDict(
    "TranslatePinDataOutputTypeDef",
    {
        "KeyArn": str,
        "KeyCheckValue": str,
        "PinBlock": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
VerifyAuthRequestCryptogramOutputTypeDef = TypedDict(
    "VerifyAuthRequestCryptogramOutputTypeDef",
    {
        "AuthResponseValue": str,
        "KeyArn": str,
        "KeyCheckValue": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
VerifyCardValidationDataOutputTypeDef = TypedDict(
    "VerifyCardValidationDataOutputTypeDef",
    {
        "KeyArn": str,
        "KeyCheckValue": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
VerifyMacOutputTypeDef = TypedDict(
    "VerifyMacOutputTypeDef",
    {
        "KeyArn": str,
        "KeyCheckValue": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
VerifyPinDataOutputTypeDef = TypedDict(
    "VerifyPinDataOutputTypeDef",
    {
        "EncryptionKeyArn": str,
        "EncryptionKeyCheckValue": str,
        "VerificationKeyArn": str,
        "VerificationKeyCheckValue": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EncryptionDecryptionAttributesTypeDef = TypedDict(
    "EncryptionDecryptionAttributesTypeDef",
    {
        "Asymmetric": NotRequired[AsymmetricEncryptionAttributesTypeDef],
        "Dukpt": NotRequired[DukptEncryptionAttributesTypeDef],
        "Symmetric": NotRequired[SymmetricEncryptionAttributesTypeDef],
    },
)
ReEncryptionAttributesTypeDef = TypedDict(
    "ReEncryptionAttributesTypeDef",
    {
        "Dukpt": NotRequired[DukptEncryptionAttributesTypeDef],
        "Symmetric": NotRequired[SymmetricEncryptionAttributesTypeDef],
    },
)
GeneratePinDataOutputTypeDef = TypedDict(
    "GeneratePinDataOutputTypeDef",
    {
        "EncryptedPinBlock": str,
        "EncryptionKeyArn": str,
        "EncryptionKeyCheckValue": str,
        "GenerationKeyArn": str,
        "GenerationKeyCheckValue": str,
        "PinData": PinDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
MacAlgorithmEmvTypeDef = TypedDict(
    "MacAlgorithmEmvTypeDef",
    {
        "MajorKeyDerivationMode": MajorKeyDerivationModeType,
        "PanSequenceNumber": str,
        "PrimaryAccountNumber": str,
        "SessionKeyDerivationMode": SessionKeyDerivationModeType,
        "SessionKeyDerivationValue": SessionKeyDerivationValueTypeDef,
    },
)
PinGenerationAttributesTypeDef = TypedDict(
    "PinGenerationAttributesTypeDef",
    {
        "Ibm3624NaturalPin": NotRequired[Ibm3624NaturalPinTypeDef],
        "Ibm3624PinFromOffset": NotRequired[Ibm3624PinFromOffsetTypeDef],
        "Ibm3624PinOffset": NotRequired[Ibm3624PinOffsetTypeDef],
        "Ibm3624RandomPin": NotRequired[Ibm3624RandomPinTypeDef],
        "VisaPin": NotRequired[VisaPinTypeDef],
        "VisaPinVerificationValue": NotRequired[VisaPinVerificationValueTypeDef],
    },
)
PinVerificationAttributesTypeDef = TypedDict(
    "PinVerificationAttributesTypeDef",
    {
        "Ibm3624Pin": NotRequired[Ibm3624PinVerificationTypeDef],
        "VisaPin": NotRequired[VisaPinVerificationTypeDef],
    },
)
SessionKeyDerivationTypeDef = TypedDict(
    "SessionKeyDerivationTypeDef",
    {
        "Amex": NotRequired[SessionKeyAmexTypeDef],
        "Emv2000": NotRequired[SessionKeyEmv2000TypeDef],
        "EmvCommon": NotRequired[SessionKeyEmvCommonTypeDef],
        "Mastercard": NotRequired[SessionKeyMastercardTypeDef],
        "Visa": NotRequired[SessionKeyVisaTypeDef],
    },
)
TranslationIsoFormatsTypeDef = TypedDict(
    "TranslationIsoFormatsTypeDef",
    {
        "IsoFormat0": NotRequired[TranslationPinDataIsoFormat034TypeDef],
        "IsoFormat1": NotRequired[Mapping[str, Any]],
        "IsoFormat3": NotRequired[TranslationPinDataIsoFormat034TypeDef],
        "IsoFormat4": NotRequired[TranslationPinDataIsoFormat034TypeDef],
    },
)
GenerateCardValidationDataInputRequestTypeDef = TypedDict(
    "GenerateCardValidationDataInputRequestTypeDef",
    {
        "GenerationAttributes": CardGenerationAttributesTypeDef,
        "KeyIdentifier": str,
        "PrimaryAccountNumber": str,
        "ValidationDataLength": NotRequired[int],
    },
)
VerifyCardValidationDataInputRequestTypeDef = TypedDict(
    "VerifyCardValidationDataInputRequestTypeDef",
    {
        "KeyIdentifier": str,
        "PrimaryAccountNumber": str,
        "ValidationData": str,
        "VerificationAttributes": CardVerificationAttributesTypeDef,
    },
)
DecryptDataInputRequestTypeDef = TypedDict(
    "DecryptDataInputRequestTypeDef",
    {
        "CipherText": str,
        "DecryptionAttributes": EncryptionDecryptionAttributesTypeDef,
        "KeyIdentifier": str,
    },
)
EncryptDataInputRequestTypeDef = TypedDict(
    "EncryptDataInputRequestTypeDef",
    {
        "EncryptionAttributes": EncryptionDecryptionAttributesTypeDef,
        "KeyIdentifier": str,
        "PlainText": str,
    },
)
ReEncryptDataInputRequestTypeDef = TypedDict(
    "ReEncryptDataInputRequestTypeDef",
    {
        "CipherText": str,
        "IncomingEncryptionAttributes": ReEncryptionAttributesTypeDef,
        "IncomingKeyIdentifier": str,
        "OutgoingEncryptionAttributes": ReEncryptionAttributesTypeDef,
        "OutgoingKeyIdentifier": str,
    },
)
MacAttributesTypeDef = TypedDict(
    "MacAttributesTypeDef",
    {
        "Algorithm": NotRequired[MacAlgorithmType],
        "DukptCmac": NotRequired[MacAlgorithmDukptTypeDef],
        "DukptIso9797Algorithm1": NotRequired[MacAlgorithmDukptTypeDef],
        "DukptIso9797Algorithm3": NotRequired[MacAlgorithmDukptTypeDef],
        "EmvMac": NotRequired[MacAlgorithmEmvTypeDef],
    },
)
GeneratePinDataInputRequestTypeDef = TypedDict(
    "GeneratePinDataInputRequestTypeDef",
    {
        "EncryptionKeyIdentifier": str,
        "GenerationAttributes": PinGenerationAttributesTypeDef,
        "GenerationKeyIdentifier": str,
        "PinBlockFormat": PinBlockFormatForPinDataType,
        "PrimaryAccountNumber": str,
        "PinDataLength": NotRequired[int],
    },
)
VerifyPinDataInputRequestTypeDef = TypedDict(
    "VerifyPinDataInputRequestTypeDef",
    {
        "EncryptedPinBlock": str,
        "EncryptionKeyIdentifier": str,
        "PinBlockFormat": PinBlockFormatForPinDataType,
        "PrimaryAccountNumber": str,
        "VerificationAttributes": PinVerificationAttributesTypeDef,
        "VerificationKeyIdentifier": str,
        "DukptAttributes": NotRequired[DukptAttributesTypeDef],
        "PinDataLength": NotRequired[int],
    },
)
VerifyAuthRequestCryptogramInputRequestTypeDef = TypedDict(
    "VerifyAuthRequestCryptogramInputRequestTypeDef",
    {
        "AuthRequestCryptogram": str,
        "KeyIdentifier": str,
        "MajorKeyDerivationMode": MajorKeyDerivationModeType,
        "SessionKeyDerivationAttributes": SessionKeyDerivationTypeDef,
        "TransactionData": str,
        "AuthResponseAttributes": NotRequired[CryptogramAuthResponseTypeDef],
    },
)
TranslatePinDataInputRequestTypeDef = TypedDict(
    "TranslatePinDataInputRequestTypeDef",
    {
        "EncryptedPinBlock": str,
        "IncomingKeyIdentifier": str,
        "IncomingTranslationAttributes": TranslationIsoFormatsTypeDef,
        "OutgoingKeyIdentifier": str,
        "OutgoingTranslationAttributes": TranslationIsoFormatsTypeDef,
        "IncomingDukptAttributes": NotRequired[DukptDerivationAttributesTypeDef],
        "OutgoingDukptAttributes": NotRequired[DukptDerivationAttributesTypeDef],
    },
)
GenerateMacInputRequestTypeDef = TypedDict(
    "GenerateMacInputRequestTypeDef",
    {
        "GenerationAttributes": MacAttributesTypeDef,
        "KeyIdentifier": str,
        "MessageData": str,
        "MacLength": NotRequired[int],
    },
)
VerifyMacInputRequestTypeDef = TypedDict(
    "VerifyMacInputRequestTypeDef",
    {
        "KeyIdentifier": str,
        "Mac": str,
        "MessageData": str,
        "VerificationAttributes": MacAttributesTypeDef,
        "MacLength": NotRequired[int],
    },
)
