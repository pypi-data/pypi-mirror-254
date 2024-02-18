"""
Type annotations for ivs-realtime service type definitions.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ivs_realtime/type_defs/)

Usage::

    ```python
    from types_aiobotocore_ivs_realtime.type_defs import ChannelDestinationConfigurationTypeDef

    data: ChannelDestinationConfigurationTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from .literals import (
    CompositionStateType,
    DestinationStateType,
    EventErrorCodeType,
    EventNameType,
    ParticipantStateType,
    ParticipantTokenCapabilityType,
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
    "ChannelDestinationConfigurationTypeDef",
    "DestinationSummaryTypeDef",
    "VideoTypeDef",
    "ResponseMetadataTypeDef",
    "CreateParticipantTokenRequestRequestTypeDef",
    "ParticipantTokenTypeDef",
    "ParticipantTokenConfigurationTypeDef",
    "StageTypeDef",
    "S3StorageConfigurationTypeDef",
    "DeleteEncoderConfigurationRequestRequestTypeDef",
    "DeleteStageRequestRequestTypeDef",
    "DeleteStorageConfigurationRequestRequestTypeDef",
    "S3DetailTypeDef",
    "DisconnectParticipantRequestRequestTypeDef",
    "EncoderConfigurationSummaryTypeDef",
    "EventTypeDef",
    "GetCompositionRequestRequestTypeDef",
    "GetEncoderConfigurationRequestRequestTypeDef",
    "GetParticipantRequestRequestTypeDef",
    "ParticipantTypeDef",
    "GetStageRequestRequestTypeDef",
    "GetStageSessionRequestRequestTypeDef",
    "StageSessionTypeDef",
    "GetStorageConfigurationRequestRequestTypeDef",
    "GridConfigurationTypeDef",
    "ListCompositionsRequestRequestTypeDef",
    "ListEncoderConfigurationsRequestRequestTypeDef",
    "ListParticipantEventsRequestRequestTypeDef",
    "ListParticipantsRequestRequestTypeDef",
    "ParticipantSummaryTypeDef",
    "ListStageSessionsRequestRequestTypeDef",
    "StageSessionSummaryTypeDef",
    "ListStagesRequestRequestTypeDef",
    "StageSummaryTypeDef",
    "ListStorageConfigurationsRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "RecordingConfigurationTypeDef",
    "StopCompositionRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateStageRequestRequestTypeDef",
    "CompositionSummaryTypeDef",
    "CreateEncoderConfigurationRequestRequestTypeDef",
    "EncoderConfigurationTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "CreateParticipantTokenResponseTypeDef",
    "CreateStageRequestRequestTypeDef",
    "CreateStageResponseTypeDef",
    "GetStageResponseTypeDef",
    "UpdateStageResponseTypeDef",
    "CreateStorageConfigurationRequestRequestTypeDef",
    "StorageConfigurationSummaryTypeDef",
    "StorageConfigurationTypeDef",
    "DestinationDetailTypeDef",
    "ListEncoderConfigurationsResponseTypeDef",
    "ListParticipantEventsResponseTypeDef",
    "GetParticipantResponseTypeDef",
    "GetStageSessionResponseTypeDef",
    "LayoutConfigurationTypeDef",
    "ListParticipantsResponseTypeDef",
    "ListStageSessionsResponseTypeDef",
    "ListStagesResponseTypeDef",
    "S3DestinationConfigurationTypeDef",
    "ListCompositionsResponseTypeDef",
    "CreateEncoderConfigurationResponseTypeDef",
    "GetEncoderConfigurationResponseTypeDef",
    "ListStorageConfigurationsResponseTypeDef",
    "CreateStorageConfigurationResponseTypeDef",
    "GetStorageConfigurationResponseTypeDef",
    "DestinationConfigurationTypeDef",
    "DestinationTypeDef",
    "StartCompositionRequestRequestTypeDef",
    "CompositionTypeDef",
    "GetCompositionResponseTypeDef",
    "StartCompositionResponseTypeDef",
)

ChannelDestinationConfigurationTypeDef = TypedDict(
    "ChannelDestinationConfigurationTypeDef",
    {
        "channelArn": str,
        "encoderConfigurationArn": NotRequired[str],
    },
)
DestinationSummaryTypeDef = TypedDict(
    "DestinationSummaryTypeDef",
    {
        "id": str,
        "state": DestinationStateType,
        "endTime": NotRequired[datetime],
        "startTime": NotRequired[datetime],
    },
)
VideoTypeDef = TypedDict(
    "VideoTypeDef",
    {
        "bitrate": NotRequired[int],
        "framerate": NotRequired[float],
        "height": NotRequired[int],
        "width": NotRequired[int],
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
CreateParticipantTokenRequestRequestTypeDef = TypedDict(
    "CreateParticipantTokenRequestRequestTypeDef",
    {
        "stageArn": str,
        "attributes": NotRequired[Mapping[str, str]],
        "capabilities": NotRequired[Sequence[ParticipantTokenCapabilityType]],
        "duration": NotRequired[int],
        "userId": NotRequired[str],
    },
)
ParticipantTokenTypeDef = TypedDict(
    "ParticipantTokenTypeDef",
    {
        "attributes": NotRequired[Dict[str, str]],
        "capabilities": NotRequired[List[ParticipantTokenCapabilityType]],
        "duration": NotRequired[int],
        "expirationTime": NotRequired[datetime],
        "participantId": NotRequired[str],
        "token": NotRequired[str],
        "userId": NotRequired[str],
    },
)
ParticipantTokenConfigurationTypeDef = TypedDict(
    "ParticipantTokenConfigurationTypeDef",
    {
        "attributes": NotRequired[Mapping[str, str]],
        "capabilities": NotRequired[Sequence[ParticipantTokenCapabilityType]],
        "duration": NotRequired[int],
        "userId": NotRequired[str],
    },
)
StageTypeDef = TypedDict(
    "StageTypeDef",
    {
        "arn": str,
        "activeSessionId": NotRequired[str],
        "name": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
    },
)
S3StorageConfigurationTypeDef = TypedDict(
    "S3StorageConfigurationTypeDef",
    {
        "bucketName": str,
    },
)
DeleteEncoderConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteEncoderConfigurationRequestRequestTypeDef",
    {
        "arn": str,
    },
)
DeleteStageRequestRequestTypeDef = TypedDict(
    "DeleteStageRequestRequestTypeDef",
    {
        "arn": str,
    },
)
DeleteStorageConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteStorageConfigurationRequestRequestTypeDef",
    {
        "arn": str,
    },
)
S3DetailTypeDef = TypedDict(
    "S3DetailTypeDef",
    {
        "recordingPrefix": str,
    },
)
DisconnectParticipantRequestRequestTypeDef = TypedDict(
    "DisconnectParticipantRequestRequestTypeDef",
    {
        "participantId": str,
        "stageArn": str,
        "reason": NotRequired[str],
    },
)
EncoderConfigurationSummaryTypeDef = TypedDict(
    "EncoderConfigurationSummaryTypeDef",
    {
        "arn": str,
        "name": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
    },
)
EventTypeDef = TypedDict(
    "EventTypeDef",
    {
        "errorCode": NotRequired[EventErrorCodeType],
        "eventTime": NotRequired[datetime],
        "name": NotRequired[EventNameType],
        "participantId": NotRequired[str],
        "remoteParticipantId": NotRequired[str],
    },
)
GetCompositionRequestRequestTypeDef = TypedDict(
    "GetCompositionRequestRequestTypeDef",
    {
        "arn": str,
    },
)
GetEncoderConfigurationRequestRequestTypeDef = TypedDict(
    "GetEncoderConfigurationRequestRequestTypeDef",
    {
        "arn": str,
    },
)
GetParticipantRequestRequestTypeDef = TypedDict(
    "GetParticipantRequestRequestTypeDef",
    {
        "participantId": str,
        "sessionId": str,
        "stageArn": str,
    },
)
ParticipantTypeDef = TypedDict(
    "ParticipantTypeDef",
    {
        "attributes": NotRequired[Dict[str, str]],
        "browserName": NotRequired[str],
        "browserVersion": NotRequired[str],
        "firstJoinTime": NotRequired[datetime],
        "ispName": NotRequired[str],
        "osName": NotRequired[str],
        "osVersion": NotRequired[str],
        "participantId": NotRequired[str],
        "published": NotRequired[bool],
        "sdkVersion": NotRequired[str],
        "state": NotRequired[ParticipantStateType],
        "userId": NotRequired[str],
    },
)
GetStageRequestRequestTypeDef = TypedDict(
    "GetStageRequestRequestTypeDef",
    {
        "arn": str,
    },
)
GetStageSessionRequestRequestTypeDef = TypedDict(
    "GetStageSessionRequestRequestTypeDef",
    {
        "sessionId": str,
        "stageArn": str,
    },
)
StageSessionTypeDef = TypedDict(
    "StageSessionTypeDef",
    {
        "endTime": NotRequired[datetime],
        "sessionId": NotRequired[str],
        "startTime": NotRequired[datetime],
    },
)
GetStorageConfigurationRequestRequestTypeDef = TypedDict(
    "GetStorageConfigurationRequestRequestTypeDef",
    {
        "arn": str,
    },
)
GridConfigurationTypeDef = TypedDict(
    "GridConfigurationTypeDef",
    {
        "featuredParticipantAttribute": NotRequired[str],
    },
)
ListCompositionsRequestRequestTypeDef = TypedDict(
    "ListCompositionsRequestRequestTypeDef",
    {
        "filterByEncoderConfigurationArn": NotRequired[str],
        "filterByStageArn": NotRequired[str],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListEncoderConfigurationsRequestRequestTypeDef = TypedDict(
    "ListEncoderConfigurationsRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListParticipantEventsRequestRequestTypeDef = TypedDict(
    "ListParticipantEventsRequestRequestTypeDef",
    {
        "participantId": str,
        "sessionId": str,
        "stageArn": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListParticipantsRequestRequestTypeDef = TypedDict(
    "ListParticipantsRequestRequestTypeDef",
    {
        "sessionId": str,
        "stageArn": str,
        "filterByPublished": NotRequired[bool],
        "filterByState": NotRequired[ParticipantStateType],
        "filterByUserId": NotRequired[str],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ParticipantSummaryTypeDef = TypedDict(
    "ParticipantSummaryTypeDef",
    {
        "firstJoinTime": NotRequired[datetime],
        "participantId": NotRequired[str],
        "published": NotRequired[bool],
        "state": NotRequired[ParticipantStateType],
        "userId": NotRequired[str],
    },
)
ListStageSessionsRequestRequestTypeDef = TypedDict(
    "ListStageSessionsRequestRequestTypeDef",
    {
        "stageArn": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
StageSessionSummaryTypeDef = TypedDict(
    "StageSessionSummaryTypeDef",
    {
        "endTime": NotRequired[datetime],
        "sessionId": NotRequired[str],
        "startTime": NotRequired[datetime],
    },
)
ListStagesRequestRequestTypeDef = TypedDict(
    "ListStagesRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
StageSummaryTypeDef = TypedDict(
    "StageSummaryTypeDef",
    {
        "arn": str,
        "activeSessionId": NotRequired[str],
        "name": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
    },
)
ListStorageConfigurationsRequestRequestTypeDef = TypedDict(
    "ListStorageConfigurationsRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)
RecordingConfigurationTypeDef = TypedDict(
    "RecordingConfigurationTypeDef",
    {
        "format": NotRequired[Literal["HLS"]],
    },
)
StopCompositionRequestRequestTypeDef = TypedDict(
    "StopCompositionRequestRequestTypeDef",
    {
        "arn": str,
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
UpdateStageRequestRequestTypeDef = TypedDict(
    "UpdateStageRequestRequestTypeDef",
    {
        "arn": str,
        "name": NotRequired[str],
    },
)
CompositionSummaryTypeDef = TypedDict(
    "CompositionSummaryTypeDef",
    {
        "arn": str,
        "destinations": List[DestinationSummaryTypeDef],
        "stageArn": str,
        "state": CompositionStateType,
        "endTime": NotRequired[datetime],
        "startTime": NotRequired[datetime],
        "tags": NotRequired[Dict[str, str]],
    },
)
CreateEncoderConfigurationRequestRequestTypeDef = TypedDict(
    "CreateEncoderConfigurationRequestRequestTypeDef",
    {
        "name": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
        "video": NotRequired[VideoTypeDef],
    },
)
EncoderConfigurationTypeDef = TypedDict(
    "EncoderConfigurationTypeDef",
    {
        "arn": str,
        "name": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
        "video": NotRequired[VideoTypeDef],
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateParticipantTokenResponseTypeDef = TypedDict(
    "CreateParticipantTokenResponseTypeDef",
    {
        "participantToken": ParticipantTokenTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateStageRequestRequestTypeDef = TypedDict(
    "CreateStageRequestRequestTypeDef",
    {
        "name": NotRequired[str],
        "participantTokenConfigurations": NotRequired[
            Sequence[ParticipantTokenConfigurationTypeDef]
        ],
        "tags": NotRequired[Mapping[str, str]],
    },
)
CreateStageResponseTypeDef = TypedDict(
    "CreateStageResponseTypeDef",
    {
        "participantTokens": List[ParticipantTokenTypeDef],
        "stage": StageTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetStageResponseTypeDef = TypedDict(
    "GetStageResponseTypeDef",
    {
        "stage": StageTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateStageResponseTypeDef = TypedDict(
    "UpdateStageResponseTypeDef",
    {
        "stage": StageTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateStorageConfigurationRequestRequestTypeDef = TypedDict(
    "CreateStorageConfigurationRequestRequestTypeDef",
    {
        "s3": S3StorageConfigurationTypeDef,
        "name": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)
StorageConfigurationSummaryTypeDef = TypedDict(
    "StorageConfigurationSummaryTypeDef",
    {
        "arn": str,
        "name": NotRequired[str],
        "s3": NotRequired[S3StorageConfigurationTypeDef],
        "tags": NotRequired[Dict[str, str]],
    },
)
StorageConfigurationTypeDef = TypedDict(
    "StorageConfigurationTypeDef",
    {
        "arn": str,
        "name": NotRequired[str],
        "s3": NotRequired[S3StorageConfigurationTypeDef],
        "tags": NotRequired[Dict[str, str]],
    },
)
DestinationDetailTypeDef = TypedDict(
    "DestinationDetailTypeDef",
    {
        "s3": NotRequired[S3DetailTypeDef],
    },
)
ListEncoderConfigurationsResponseTypeDef = TypedDict(
    "ListEncoderConfigurationsResponseTypeDef",
    {
        "encoderConfigurations": List[EncoderConfigurationSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListParticipantEventsResponseTypeDef = TypedDict(
    "ListParticipantEventsResponseTypeDef",
    {
        "events": List[EventTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetParticipantResponseTypeDef = TypedDict(
    "GetParticipantResponseTypeDef",
    {
        "participant": ParticipantTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetStageSessionResponseTypeDef = TypedDict(
    "GetStageSessionResponseTypeDef",
    {
        "stageSession": StageSessionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
LayoutConfigurationTypeDef = TypedDict(
    "LayoutConfigurationTypeDef",
    {
        "grid": NotRequired[GridConfigurationTypeDef],
    },
)
ListParticipantsResponseTypeDef = TypedDict(
    "ListParticipantsResponseTypeDef",
    {
        "nextToken": str,
        "participants": List[ParticipantSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListStageSessionsResponseTypeDef = TypedDict(
    "ListStageSessionsResponseTypeDef",
    {
        "nextToken": str,
        "stageSessions": List[StageSessionSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListStagesResponseTypeDef = TypedDict(
    "ListStagesResponseTypeDef",
    {
        "nextToken": str,
        "stages": List[StageSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
S3DestinationConfigurationTypeDef = TypedDict(
    "S3DestinationConfigurationTypeDef",
    {
        "encoderConfigurationArns": List[str],
        "storageConfigurationArn": str,
        "recordingConfiguration": NotRequired[RecordingConfigurationTypeDef],
    },
)
ListCompositionsResponseTypeDef = TypedDict(
    "ListCompositionsResponseTypeDef",
    {
        "compositions": List[CompositionSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateEncoderConfigurationResponseTypeDef = TypedDict(
    "CreateEncoderConfigurationResponseTypeDef",
    {
        "encoderConfiguration": EncoderConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetEncoderConfigurationResponseTypeDef = TypedDict(
    "GetEncoderConfigurationResponseTypeDef",
    {
        "encoderConfiguration": EncoderConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListStorageConfigurationsResponseTypeDef = TypedDict(
    "ListStorageConfigurationsResponseTypeDef",
    {
        "nextToken": str,
        "storageConfigurations": List[StorageConfigurationSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateStorageConfigurationResponseTypeDef = TypedDict(
    "CreateStorageConfigurationResponseTypeDef",
    {
        "storageConfiguration": StorageConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetStorageConfigurationResponseTypeDef = TypedDict(
    "GetStorageConfigurationResponseTypeDef",
    {
        "storageConfiguration": StorageConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DestinationConfigurationTypeDef = TypedDict(
    "DestinationConfigurationTypeDef",
    {
        "channel": NotRequired[ChannelDestinationConfigurationTypeDef],
        "name": NotRequired[str],
        "s3": NotRequired[S3DestinationConfigurationTypeDef],
    },
)
DestinationTypeDef = TypedDict(
    "DestinationTypeDef",
    {
        "configuration": DestinationConfigurationTypeDef,
        "id": str,
        "state": DestinationStateType,
        "detail": NotRequired[DestinationDetailTypeDef],
        "endTime": NotRequired[datetime],
        "startTime": NotRequired[datetime],
    },
)
StartCompositionRequestRequestTypeDef = TypedDict(
    "StartCompositionRequestRequestTypeDef",
    {
        "destinations": Sequence[DestinationConfigurationTypeDef],
        "stageArn": str,
        "idempotencyToken": NotRequired[str],
        "layout": NotRequired[LayoutConfigurationTypeDef],
        "tags": NotRequired[Mapping[str, str]],
    },
)
CompositionTypeDef = TypedDict(
    "CompositionTypeDef",
    {
        "arn": str,
        "destinations": List[DestinationTypeDef],
        "layout": LayoutConfigurationTypeDef,
        "stageArn": str,
        "state": CompositionStateType,
        "endTime": NotRequired[datetime],
        "startTime": NotRequired[datetime],
        "tags": NotRequired[Dict[str, str]],
    },
)
GetCompositionResponseTypeDef = TypedDict(
    "GetCompositionResponseTypeDef",
    {
        "composition": CompositionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartCompositionResponseTypeDef = TypedDict(
    "StartCompositionResponseTypeDef",
    {
        "composition": CompositionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
