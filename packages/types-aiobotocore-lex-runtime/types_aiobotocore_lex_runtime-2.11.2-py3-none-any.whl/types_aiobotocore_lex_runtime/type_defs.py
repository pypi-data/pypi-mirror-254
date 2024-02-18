"""
Type annotations for lex-runtime service type definitions.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lex_runtime/type_defs/)

Usage::

    ```python
    from types_aiobotocore_lex_runtime.type_defs import ActiveContextTimeToLiveTypeDef

    data: ActiveContextTimeToLiveTypeDef = ...
    ```
"""

import sys
from typing import IO, Any, Dict, List, Mapping, Sequence, Union

from aiobotocore.response import StreamingBody

from .literals import (
    ConfirmationStatusType,
    DialogActionTypeType,
    DialogStateType,
    FulfillmentStateType,
    MessageFormatTypeType,
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
    "ActiveContextTimeToLiveTypeDef",
    "BlobTypeDef",
    "ButtonTypeDef",
    "DeleteSessionRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "DialogActionTypeDef",
    "GetSessionRequestRequestTypeDef",
    "IntentSummaryTypeDef",
    "IntentConfidenceTypeDef",
    "SentimentResponseTypeDef",
    "ActiveContextTypeDef",
    "PostContentRequestRequestTypeDef",
    "GenericAttachmentTypeDef",
    "DeleteSessionResponseTypeDef",
    "PostContentResponseTypeDef",
    "PutSessionResponseTypeDef",
    "PredictedIntentTypeDef",
    "GetSessionResponseTypeDef",
    "PostTextRequestRequestTypeDef",
    "PutSessionRequestRequestTypeDef",
    "ResponseCardTypeDef",
    "PostTextResponseTypeDef",
)

ActiveContextTimeToLiveTypeDef = TypedDict(
    "ActiveContextTimeToLiveTypeDef",
    {
        "timeToLiveInSeconds": NotRequired[int],
        "turnsToLive": NotRequired[int],
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
DeleteSessionRequestRequestTypeDef = TypedDict(
    "DeleteSessionRequestRequestTypeDef",
    {
        "botName": str,
        "botAlias": str,
        "userId": str,
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
        "intentName": NotRequired[str],
        "slots": NotRequired[Dict[str, str]],
        "slotToElicit": NotRequired[str],
        "fulfillmentState": NotRequired[FulfillmentStateType],
        "message": NotRequired[str],
        "messageFormat": NotRequired[MessageFormatTypeType],
    },
)
GetSessionRequestRequestTypeDef = TypedDict(
    "GetSessionRequestRequestTypeDef",
    {
        "botName": str,
        "botAlias": str,
        "userId": str,
        "checkpointLabelFilter": NotRequired[str],
    },
)
IntentSummaryTypeDef = TypedDict(
    "IntentSummaryTypeDef",
    {
        "dialogActionType": DialogActionTypeType,
        "intentName": NotRequired[str],
        "checkpointLabel": NotRequired[str],
        "slots": NotRequired[Dict[str, str]],
        "confirmationStatus": NotRequired[ConfirmationStatusType],
        "fulfillmentState": NotRequired[FulfillmentStateType],
        "slotToElicit": NotRequired[str],
    },
)
IntentConfidenceTypeDef = TypedDict(
    "IntentConfidenceTypeDef",
    {
        "score": NotRequired[float],
    },
)
SentimentResponseTypeDef = TypedDict(
    "SentimentResponseTypeDef",
    {
        "sentimentLabel": NotRequired[str],
        "sentimentScore": NotRequired[str],
    },
)
ActiveContextTypeDef = TypedDict(
    "ActiveContextTypeDef",
    {
        "name": str,
        "timeToLive": ActiveContextTimeToLiveTypeDef,
        "parameters": Dict[str, str],
    },
)
PostContentRequestRequestTypeDef = TypedDict(
    "PostContentRequestRequestTypeDef",
    {
        "botName": str,
        "botAlias": str,
        "userId": str,
        "contentType": str,
        "inputStream": BlobTypeDef,
        "sessionAttributes": NotRequired[str],
        "requestAttributes": NotRequired[str],
        "accept": NotRequired[str],
        "activeContexts": NotRequired[str],
    },
)
GenericAttachmentTypeDef = TypedDict(
    "GenericAttachmentTypeDef",
    {
        "title": NotRequired[str],
        "subTitle": NotRequired[str],
        "attachmentLinkUrl": NotRequired[str],
        "imageUrl": NotRequired[str],
        "buttons": NotRequired[List[ButtonTypeDef]],
    },
)
DeleteSessionResponseTypeDef = TypedDict(
    "DeleteSessionResponseTypeDef",
    {
        "botName": str,
        "botAlias": str,
        "userId": str,
        "sessionId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PostContentResponseTypeDef = TypedDict(
    "PostContentResponseTypeDef",
    {
        "contentType": str,
        "intentName": str,
        "nluIntentConfidence": str,
        "alternativeIntents": str,
        "slots": str,
        "sessionAttributes": str,
        "sentimentResponse": str,
        "message": str,
        "encodedMessage": str,
        "messageFormat": MessageFormatTypeType,
        "dialogState": DialogStateType,
        "slotToElicit": str,
        "inputTranscript": str,
        "encodedInputTranscript": str,
        "audioStream": StreamingBody,
        "botVersion": str,
        "sessionId": str,
        "activeContexts": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutSessionResponseTypeDef = TypedDict(
    "PutSessionResponseTypeDef",
    {
        "contentType": str,
        "intentName": str,
        "slots": str,
        "sessionAttributes": str,
        "message": str,
        "encodedMessage": str,
        "messageFormat": MessageFormatTypeType,
        "dialogState": DialogStateType,
        "slotToElicit": str,
        "audioStream": StreamingBody,
        "sessionId": str,
        "activeContexts": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PredictedIntentTypeDef = TypedDict(
    "PredictedIntentTypeDef",
    {
        "intentName": NotRequired[str],
        "nluIntentConfidence": NotRequired[IntentConfidenceTypeDef],
        "slots": NotRequired[Dict[str, str]],
    },
)
GetSessionResponseTypeDef = TypedDict(
    "GetSessionResponseTypeDef",
    {
        "recentIntentSummaryView": List[IntentSummaryTypeDef],
        "sessionAttributes": Dict[str, str],
        "sessionId": str,
        "dialogAction": DialogActionTypeDef,
        "activeContexts": List[ActiveContextTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PostTextRequestRequestTypeDef = TypedDict(
    "PostTextRequestRequestTypeDef",
    {
        "botName": str,
        "botAlias": str,
        "userId": str,
        "inputText": str,
        "sessionAttributes": NotRequired[Mapping[str, str]],
        "requestAttributes": NotRequired[Mapping[str, str]],
        "activeContexts": NotRequired[Sequence[ActiveContextTypeDef]],
    },
)
PutSessionRequestRequestTypeDef = TypedDict(
    "PutSessionRequestRequestTypeDef",
    {
        "botName": str,
        "botAlias": str,
        "userId": str,
        "sessionAttributes": NotRequired[Mapping[str, str]],
        "dialogAction": NotRequired[DialogActionTypeDef],
        "recentIntentSummaryView": NotRequired[Sequence[IntentSummaryTypeDef]],
        "accept": NotRequired[str],
        "activeContexts": NotRequired[Sequence[ActiveContextTypeDef]],
    },
)
ResponseCardTypeDef = TypedDict(
    "ResponseCardTypeDef",
    {
        "version": NotRequired[str],
        "contentType": NotRequired[Literal["application/vnd.amazonaws.card.generic"]],
        "genericAttachments": NotRequired[List[GenericAttachmentTypeDef]],
    },
)
PostTextResponseTypeDef = TypedDict(
    "PostTextResponseTypeDef",
    {
        "intentName": str,
        "nluIntentConfidence": IntentConfidenceTypeDef,
        "alternativeIntents": List[PredictedIntentTypeDef],
        "slots": Dict[str, str],
        "sessionAttributes": Dict[str, str],
        "message": str,
        "sentimentResponse": SentimentResponseTypeDef,
        "messageFormat": MessageFormatTypeType,
        "dialogState": DialogStateType,
        "slotToElicit": str,
        "responseCard": ResponseCardTypeDef,
        "sessionId": str,
        "botVersion": str,
        "activeContexts": List[ActiveContextTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
