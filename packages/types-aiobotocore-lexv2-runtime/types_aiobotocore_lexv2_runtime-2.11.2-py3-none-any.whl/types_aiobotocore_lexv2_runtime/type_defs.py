"""
Type annotations for lexv2-runtime service type definitions.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_runtime/type_defs/)

Usage::

    ```python
    from types_aiobotocore_lexv2_runtime.type_defs import ActiveContextTimeToLiveTypeDef

    data: ActiveContextTimeToLiveTypeDef = ...
    ```
"""

import sys
from typing import IO, Any, Dict, List, Mapping, Sequence, Union

from aiobotocore.response import StreamingBody

from .literals import (
    ConfirmationStateType,
    DialogActionTypeType,
    IntentStateType,
    InterpretationSourceType,
    MessageContentTypeType,
    SentimentTypeType,
    ShapeType,
    StyleTypeType,
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
    "ActiveContextTimeToLiveTypeDef",
    "BlobTypeDef",
    "ButtonTypeDef",
    "ConfidenceScoreTypeDef",
    "DeleteSessionRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "DialogActionTypeDef",
    "ElicitSubSlotTypeDef",
    "GetSessionRequestRequestTypeDef",
    "IntentTypeDef",
    "RecognizedBotMemberTypeDef",
    "RuntimeHintValueTypeDef",
    "RuntimeHintsTypeDef",
    "SentimentScoreTypeDef",
    "ValueTypeDef",
    "ActiveContextTypeDef",
    "RecognizeUtteranceRequestRequestTypeDef",
    "ImageResponseCardTypeDef",
    "DeleteSessionResponseTypeDef",
    "PutSessionResponseTypeDef",
    "RecognizeUtteranceResponseTypeDef",
    "RuntimeHintDetailsTypeDef",
    "SentimentResponseTypeDef",
    "SlotTypeDef",
    "SessionStateTypeDef",
    "MessageTypeDef",
    "InterpretationTypeDef",
    "RecognizeTextRequestRequestTypeDef",
    "PutSessionRequestRequestTypeDef",
    "GetSessionResponseTypeDef",
    "RecognizeTextResponseTypeDef",
)

ActiveContextTimeToLiveTypeDef = TypedDict(
    "ActiveContextTimeToLiveTypeDef",
    {
        "timeToLiveInSeconds": int,
        "turnsToLive": int,
    },
)
BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]
ButtonTypeDef = TypedDict(
    "ButtonTypeDef",
    {
        "text": str,
        "value": str,
    },
)
ConfidenceScoreTypeDef = TypedDict(
    "ConfidenceScoreTypeDef",
    {
        "score": NotRequired[float],
    },
)
DeleteSessionRequestRequestTypeDef = TypedDict(
    "DeleteSessionRequestRequestTypeDef",
    {
        "botId": str,
        "botAliasId": str,
        "localeId": str,
        "sessionId": str,
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
DialogActionTypeDef = TypedDict(
    "DialogActionTypeDef",
    {
        "type": DialogActionTypeType,
        "slotToElicit": NotRequired[str],
        "slotElicitationStyle": NotRequired[StyleTypeType],
        "subSlotToElicit": NotRequired["ElicitSubSlotTypeDef"],
    },
)
ElicitSubSlotTypeDef = TypedDict(
    "ElicitSubSlotTypeDef",
    {
        "name": str,
        "subSlotToElicit": NotRequired[Dict[str, Any]],
    },
)
GetSessionRequestRequestTypeDef = TypedDict(
    "GetSessionRequestRequestTypeDef",
    {
        "botId": str,
        "botAliasId": str,
        "localeId": str,
        "sessionId": str,
    },
)
IntentTypeDef = TypedDict(
    "IntentTypeDef",
    {
        "name": str,
        "slots": NotRequired[Dict[str, "SlotTypeDef"]],
        "state": NotRequired[IntentStateType],
        "confirmationState": NotRequired[ConfirmationStateType],
    },
)
RecognizedBotMemberTypeDef = TypedDict(
    "RecognizedBotMemberTypeDef",
    {
        "botId": str,
        "botName": NotRequired[str],
    },
)
RuntimeHintValueTypeDef = TypedDict(
    "RuntimeHintValueTypeDef",
    {
        "phrase": str,
    },
)
RuntimeHintsTypeDef = TypedDict(
    "RuntimeHintsTypeDef",
    {
        "slotHints": NotRequired[Dict[str, Dict[str, "RuntimeHintDetailsTypeDef"]]],
    },
)
SentimentScoreTypeDef = TypedDict(
    "SentimentScoreTypeDef",
    {
        "positive": NotRequired[float],
        "negative": NotRequired[float],
        "neutral": NotRequired[float],
        "mixed": NotRequired[float],
    },
)
ValueTypeDef = TypedDict(
    "ValueTypeDef",
    {
        "interpretedValue": str,
        "originalValue": NotRequired[str],
        "resolvedValues": NotRequired[List[str]],
    },
)
ActiveContextTypeDef = TypedDict(
    "ActiveContextTypeDef",
    {
        "name": str,
        "timeToLive": ActiveContextTimeToLiveTypeDef,
        "contextAttributes": Dict[str, str],
    },
)
RecognizeUtteranceRequestRequestTypeDef = TypedDict(
    "RecognizeUtteranceRequestRequestTypeDef",
    {
        "botId": str,
        "botAliasId": str,
        "localeId": str,
        "sessionId": str,
        "requestContentType": str,
        "sessionState": NotRequired[str],
        "requestAttributes": NotRequired[str],
        "responseContentType": NotRequired[str],
        "inputStream": NotRequired[BlobTypeDef],
    },
)
ImageResponseCardTypeDef = TypedDict(
    "ImageResponseCardTypeDef",
    {
        "title": str,
        "subtitle": NotRequired[str],
        "imageUrl": NotRequired[str],
        "buttons": NotRequired[List[ButtonTypeDef]],
    },
)
DeleteSessionResponseTypeDef = TypedDict(
    "DeleteSessionResponseTypeDef",
    {
        "botId": str,
        "botAliasId": str,
        "localeId": str,
        "sessionId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutSessionResponseTypeDef = TypedDict(
    "PutSessionResponseTypeDef",
    {
        "contentType": str,
        "messages": str,
        "sessionState": str,
        "requestAttributes": str,
        "sessionId": str,
        "audioStream": StreamingBody,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RecognizeUtteranceResponseTypeDef = TypedDict(
    "RecognizeUtteranceResponseTypeDef",
    {
        "inputMode": str,
        "contentType": str,
        "messages": str,
        "interpretations": str,
        "sessionState": str,
        "requestAttributes": str,
        "sessionId": str,
        "inputTranscript": str,
        "audioStream": StreamingBody,
        "recognizedBotMember": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RuntimeHintDetailsTypeDef = TypedDict(
    "RuntimeHintDetailsTypeDef",
    {
        "runtimeHintValues": NotRequired[List[RuntimeHintValueTypeDef]],
        "subSlotHints": NotRequired[Dict[str, Dict[str, Any]]],
    },
)
SentimentResponseTypeDef = TypedDict(
    "SentimentResponseTypeDef",
    {
        "sentiment": NotRequired[SentimentTypeType],
        "sentimentScore": NotRequired[SentimentScoreTypeDef],
    },
)
SlotTypeDef = TypedDict(
    "SlotTypeDef",
    {
        "value": NotRequired[ValueTypeDef],
        "shape": NotRequired[ShapeType],
        "values": NotRequired[List[Dict[str, Any]]],
        "subSlots": NotRequired[Dict[str, Dict[str, Any]]],
    },
)
SessionStateTypeDef = TypedDict(
    "SessionStateTypeDef",
    {
        "dialogAction": NotRequired[DialogActionTypeDef],
        "intent": NotRequired[IntentTypeDef],
        "activeContexts": NotRequired[List[ActiveContextTypeDef]],
        "sessionAttributes": NotRequired[Dict[str, str]],
        "originatingRequestId": NotRequired[str],
        "runtimeHints": NotRequired[RuntimeHintsTypeDef],
    },
)
MessageTypeDef = TypedDict(
    "MessageTypeDef",
    {
        "contentType": MessageContentTypeType,
        "content": NotRequired[str],
        "imageResponseCard": NotRequired[ImageResponseCardTypeDef],
    },
)
InterpretationTypeDef = TypedDict(
    "InterpretationTypeDef",
    {
        "nluConfidence": NotRequired[ConfidenceScoreTypeDef],
        "sentimentResponse": NotRequired[SentimentResponseTypeDef],
        "intent": NotRequired[IntentTypeDef],
        "interpretationSource": NotRequired[InterpretationSourceType],
    },
)
RecognizeTextRequestRequestTypeDef = TypedDict(
    "RecognizeTextRequestRequestTypeDef",
    {
        "botId": str,
        "botAliasId": str,
        "localeId": str,
        "sessionId": str,
        "text": str,
        "sessionState": NotRequired[SessionStateTypeDef],
        "requestAttributes": NotRequired[Mapping[str, str]],
    },
)
PutSessionRequestRequestTypeDef = TypedDict(
    "PutSessionRequestRequestTypeDef",
    {
        "botId": str,
        "botAliasId": str,
        "localeId": str,
        "sessionId": str,
        "sessionState": SessionStateTypeDef,
        "messages": NotRequired[Sequence[MessageTypeDef]],
        "requestAttributes": NotRequired[Mapping[str, str]],
        "responseContentType": NotRequired[str],
    },
)
GetSessionResponseTypeDef = TypedDict(
    "GetSessionResponseTypeDef",
    {
        "sessionId": str,
        "messages": List[MessageTypeDef],
        "interpretations": List[InterpretationTypeDef],
        "sessionState": SessionStateTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RecognizeTextResponseTypeDef = TypedDict(
    "RecognizeTextResponseTypeDef",
    {
        "messages": List[MessageTypeDef],
        "sessionState": SessionStateTypeDef,
        "interpretations": List[InterpretationTypeDef],
        "requestAttributes": Dict[str, str],
        "sessionId": str,
        "recognizedBotMember": RecognizedBotMemberTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
