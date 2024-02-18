"""
Type annotations for chime-sdk-media-pipelines service client.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_chime_sdk_media_pipelines/client/)

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_chime_sdk_media_pipelines.client import ChimeSDKMediaPipelinesClient

    session = get_session()
    async with session.create_client("chime-sdk-media-pipelines") as client:
        client: ChimeSDKMediaPipelinesClient
    ```
"""

import sys
from typing import Any, Dict, Mapping, Sequence, Type

from aiobotocore.client import AioBaseClient
from botocore.client import ClientMeta

from .literals import MediaPipelineStatusUpdateType
from .type_defs import (
    ChimeSdkMeetingConfigurationTypeDef,
    ConcatenationSinkTypeDef,
    ConcatenationSourceTypeDef,
    CreateMediaCapturePipelineResponseTypeDef,
    CreateMediaConcatenationPipelineResponseTypeDef,
    CreateMediaInsightsPipelineConfigurationResponseTypeDef,
    CreateMediaInsightsPipelineResponseTypeDef,
    CreateMediaLiveConnectorPipelineResponseTypeDef,
    CreateMediaPipelineKinesisVideoStreamPoolResponseTypeDef,
    CreateMediaStreamPipelineResponseTypeDef,
    EmptyResponseMetadataTypeDef,
    GetMediaCapturePipelineResponseTypeDef,
    GetMediaInsightsPipelineConfigurationResponseTypeDef,
    GetMediaPipelineKinesisVideoStreamPoolResponseTypeDef,
    GetMediaPipelineResponseTypeDef,
    GetSpeakerSearchTaskResponseTypeDef,
    GetVoiceToneAnalysisTaskResponseTypeDef,
    KinesisVideoStreamConfigurationTypeDef,
    KinesisVideoStreamConfigurationUpdateTypeDef,
    KinesisVideoStreamRecordingSourceRuntimeConfigurationTypeDef,
    KinesisVideoStreamSourceRuntimeConfigurationTypeDef,
    KinesisVideoStreamSourceTaskConfigurationTypeDef,
    ListMediaCapturePipelinesResponseTypeDef,
    ListMediaInsightsPipelineConfigurationsResponseTypeDef,
    ListMediaPipelineKinesisVideoStreamPoolsResponseTypeDef,
    ListMediaPipelinesResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    LiveConnectorSinkConfigurationTypeDef,
    LiveConnectorSourceConfigurationTypeDef,
    MediaInsightsPipelineConfigurationElementTypeDef,
    MediaStreamSinkTypeDef,
    MediaStreamSourceTypeDef,
    RealTimeAlertConfigurationTypeDef,
    S3RecordingSinkRuntimeConfigurationTypeDef,
    StartSpeakerSearchTaskResponseTypeDef,
    StartVoiceToneAnalysisTaskResponseTypeDef,
    TagTypeDef,
    UpdateMediaInsightsPipelineConfigurationResponseTypeDef,
    UpdateMediaPipelineKinesisVideoStreamPoolResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("ChimeSDKMediaPipelinesClient",)


class BotocoreClientError(Exception):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    BadRequestException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    ForbiddenException: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]
    ResourceLimitExceededException: Type[BotocoreClientError]
    ServiceFailureException: Type[BotocoreClientError]
    ServiceUnavailableException: Type[BotocoreClientError]
    ThrottledClientException: Type[BotocoreClientError]
    UnauthorizedClientException: Type[BotocoreClientError]


class ChimeSDKMediaPipelinesClient(AioBaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-media-pipelines.html#ChimeSDKMediaPipelines.Client)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_chime_sdk_media_pipelines/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        ChimeSDKMediaPipelinesClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-media-pipelines.html#ChimeSDKMediaPipelines.Client.exceptions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_chime_sdk_media_pipelines/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-media-pipelines.html#ChimeSDKMediaPipelines.Client.can_paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_chime_sdk_media_pipelines/client/#can_paginate)
        """

    async def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-media-pipelines.html#ChimeSDKMediaPipelines.Client.close)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_chime_sdk_media_pipelines/client/#close)
        """

    async def create_media_capture_pipeline(
        self,
        *,
        SourceType: Literal["ChimeSdkMeeting"],
        SourceArn: str,
        SinkType: Literal["S3Bucket"],
        SinkArn: str,
        ClientRequestToken: str = ...,
        ChimeSdkMeetingConfiguration: ChimeSdkMeetingConfigurationTypeDef = ...,
        Tags: Sequence[TagTypeDef] = ...,
    ) -> CreateMediaCapturePipelineResponseTypeDef:
        """
        Creates a media pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-media-pipelines.html#ChimeSDKMediaPipelines.Client.create_media_capture_pipeline)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_chime_sdk_media_pipelines/client/#create_media_capture_pipeline)
        """

    async def create_media_concatenation_pipeline(
        self,
        *,
        Sources: Sequence[ConcatenationSourceTypeDef],
        Sinks: Sequence[ConcatenationSinkTypeDef],
        ClientRequestToken: str = ...,
        Tags: Sequence[TagTypeDef] = ...,
    ) -> CreateMediaConcatenationPipelineResponseTypeDef:
        """
        Creates a media concatenation pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-media-pipelines.html#ChimeSDKMediaPipelines.Client.create_media_concatenation_pipeline)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_chime_sdk_media_pipelines/client/#create_media_concatenation_pipeline)
        """

    async def create_media_insights_pipeline(
        self,
        *,
        MediaInsightsPipelineConfigurationArn: str,
        KinesisVideoStreamSourceRuntimeConfiguration: KinesisVideoStreamSourceRuntimeConfigurationTypeDef = ...,
        MediaInsightsRuntimeMetadata: Mapping[str, str] = ...,
        KinesisVideoStreamRecordingSourceRuntimeConfiguration: KinesisVideoStreamRecordingSourceRuntimeConfigurationTypeDef = ...,
        S3RecordingSinkRuntimeConfiguration: S3RecordingSinkRuntimeConfigurationTypeDef = ...,
        Tags: Sequence[TagTypeDef] = ...,
        ClientRequestToken: str = ...,
    ) -> CreateMediaInsightsPipelineResponseTypeDef:
        """
        Creates a media insights pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-media-pipelines.html#ChimeSDKMediaPipelines.Client.create_media_insights_pipeline)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_chime_sdk_media_pipelines/client/#create_media_insights_pipeline)
        """

    async def create_media_insights_pipeline_configuration(
        self,
        *,
        MediaInsightsPipelineConfigurationName: str,
        ResourceAccessRoleArn: str,
        Elements: Sequence[MediaInsightsPipelineConfigurationElementTypeDef],
        RealTimeAlertConfiguration: RealTimeAlertConfigurationTypeDef = ...,
        Tags: Sequence[TagTypeDef] = ...,
        ClientRequestToken: str = ...,
    ) -> CreateMediaInsightsPipelineConfigurationResponseTypeDef:
        """
        A structure that contains the static configurations for a media insights
        pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-media-pipelines.html#ChimeSDKMediaPipelines.Client.create_media_insights_pipeline_configuration)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_chime_sdk_media_pipelines/client/#create_media_insights_pipeline_configuration)
        """

    async def create_media_live_connector_pipeline(
        self,
        *,
        Sources: Sequence[LiveConnectorSourceConfigurationTypeDef],
        Sinks: Sequence[LiveConnectorSinkConfigurationTypeDef],
        ClientRequestToken: str = ...,
        Tags: Sequence[TagTypeDef] = ...,
    ) -> CreateMediaLiveConnectorPipelineResponseTypeDef:
        """
        Creates a media live connector pipeline in an Amazon Chime SDK meeting.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-media-pipelines.html#ChimeSDKMediaPipelines.Client.create_media_live_connector_pipeline)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_chime_sdk_media_pipelines/client/#create_media_live_connector_pipeline)
        """

    async def create_media_pipeline_kinesis_video_stream_pool(
        self,
        *,
        StreamConfiguration: KinesisVideoStreamConfigurationTypeDef,
        PoolName: str,
        ClientRequestToken: str = ...,
        Tags: Sequence[TagTypeDef] = ...,
    ) -> CreateMediaPipelineKinesisVideoStreamPoolResponseTypeDef:
        """
        Creates an Kinesis video stream pool for the media pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-media-pipelines.html#ChimeSDKMediaPipelines.Client.create_media_pipeline_kinesis_video_stream_pool)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_chime_sdk_media_pipelines/client/#create_media_pipeline_kinesis_video_stream_pool)
        """

    async def create_media_stream_pipeline(
        self,
        *,
        Sources: Sequence[MediaStreamSourceTypeDef],
        Sinks: Sequence[MediaStreamSinkTypeDef],
        ClientRequestToken: str = ...,
        Tags: Sequence[TagTypeDef] = ...,
    ) -> CreateMediaStreamPipelineResponseTypeDef:
        """
        Creates a streaming media pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-media-pipelines.html#ChimeSDKMediaPipelines.Client.create_media_stream_pipeline)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_chime_sdk_media_pipelines/client/#create_media_stream_pipeline)
        """

    async def delete_media_capture_pipeline(
        self, *, MediaPipelineId: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the media pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-media-pipelines.html#ChimeSDKMediaPipelines.Client.delete_media_capture_pipeline)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_chime_sdk_media_pipelines/client/#delete_media_capture_pipeline)
        """

    async def delete_media_insights_pipeline_configuration(
        self, *, Identifier: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified configuration settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-media-pipelines.html#ChimeSDKMediaPipelines.Client.delete_media_insights_pipeline_configuration)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_chime_sdk_media_pipelines/client/#delete_media_insights_pipeline_configuration)
        """

    async def delete_media_pipeline(self, *, MediaPipelineId: str) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the media pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-media-pipelines.html#ChimeSDKMediaPipelines.Client.delete_media_pipeline)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_chime_sdk_media_pipelines/client/#delete_media_pipeline)
        """

    async def delete_media_pipeline_kinesis_video_stream_pool(
        self, *, Identifier: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes an Kinesis video stream pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-media-pipelines.html#ChimeSDKMediaPipelines.Client.delete_media_pipeline_kinesis_video_stream_pool)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_chime_sdk_media_pipelines/client/#delete_media_pipeline_kinesis_video_stream_pool)
        """

    async def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-media-pipelines.html#ChimeSDKMediaPipelines.Client.generate_presigned_url)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_chime_sdk_media_pipelines/client/#generate_presigned_url)
        """

    async def get_media_capture_pipeline(
        self, *, MediaPipelineId: str
    ) -> GetMediaCapturePipelineResponseTypeDef:
        """
        Gets an existing media pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-media-pipelines.html#ChimeSDKMediaPipelines.Client.get_media_capture_pipeline)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_chime_sdk_media_pipelines/client/#get_media_capture_pipeline)
        """

    async def get_media_insights_pipeline_configuration(
        self, *, Identifier: str
    ) -> GetMediaInsightsPipelineConfigurationResponseTypeDef:
        """
        Gets the configuration settings for a media insights pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-media-pipelines.html#ChimeSDKMediaPipelines.Client.get_media_insights_pipeline_configuration)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_chime_sdk_media_pipelines/client/#get_media_insights_pipeline_configuration)
        """

    async def get_media_pipeline(self, *, MediaPipelineId: str) -> GetMediaPipelineResponseTypeDef:
        """
        Gets an existing media pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-media-pipelines.html#ChimeSDKMediaPipelines.Client.get_media_pipeline)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_chime_sdk_media_pipelines/client/#get_media_pipeline)
        """

    async def get_media_pipeline_kinesis_video_stream_pool(
        self, *, Identifier: str
    ) -> GetMediaPipelineKinesisVideoStreamPoolResponseTypeDef:
        """
        Gets an Kinesis video stream pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-media-pipelines.html#ChimeSDKMediaPipelines.Client.get_media_pipeline_kinesis_video_stream_pool)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_chime_sdk_media_pipelines/client/#get_media_pipeline_kinesis_video_stream_pool)
        """

    async def get_speaker_search_task(
        self, *, Identifier: str, SpeakerSearchTaskId: str
    ) -> GetSpeakerSearchTaskResponseTypeDef:
        """
        Retrieves the details of the specified speaker search task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-media-pipelines.html#ChimeSDKMediaPipelines.Client.get_speaker_search_task)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_chime_sdk_media_pipelines/client/#get_speaker_search_task)
        """

    async def get_voice_tone_analysis_task(
        self, *, Identifier: str, VoiceToneAnalysisTaskId: str
    ) -> GetVoiceToneAnalysisTaskResponseTypeDef:
        """
        Retrieves the details of a voice tone analysis task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-media-pipelines.html#ChimeSDKMediaPipelines.Client.get_voice_tone_analysis_task)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_chime_sdk_media_pipelines/client/#get_voice_tone_analysis_task)
        """

    async def list_media_capture_pipelines(
        self, *, NextToken: str = ..., MaxResults: int = ...
    ) -> ListMediaCapturePipelinesResponseTypeDef:
        """
        Returns a list of media pipelines.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-media-pipelines.html#ChimeSDKMediaPipelines.Client.list_media_capture_pipelines)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_chime_sdk_media_pipelines/client/#list_media_capture_pipelines)
        """

    async def list_media_insights_pipeline_configurations(
        self, *, NextToken: str = ..., MaxResults: int = ...
    ) -> ListMediaInsightsPipelineConfigurationsResponseTypeDef:
        """
        Lists the available media insights pipeline configurations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-media-pipelines.html#ChimeSDKMediaPipelines.Client.list_media_insights_pipeline_configurations)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_chime_sdk_media_pipelines/client/#list_media_insights_pipeline_configurations)
        """

    async def list_media_pipeline_kinesis_video_stream_pools(
        self, *, NextToken: str = ..., MaxResults: int = ...
    ) -> ListMediaPipelineKinesisVideoStreamPoolsResponseTypeDef:
        """
        Lists the video stream pools in the media pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-media-pipelines.html#ChimeSDKMediaPipelines.Client.list_media_pipeline_kinesis_video_stream_pools)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_chime_sdk_media_pipelines/client/#list_media_pipeline_kinesis_video_stream_pools)
        """

    async def list_media_pipelines(
        self, *, NextToken: str = ..., MaxResults: int = ...
    ) -> ListMediaPipelinesResponseTypeDef:
        """
        Returns a list of media pipelines.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-media-pipelines.html#ChimeSDKMediaPipelines.Client.list_media_pipelines)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_chime_sdk_media_pipelines/client/#list_media_pipelines)
        """

    async def list_tags_for_resource(
        self, *, ResourceARN: str
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists the tags available for a media pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-media-pipelines.html#ChimeSDKMediaPipelines.Client.list_tags_for_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_chime_sdk_media_pipelines/client/#list_tags_for_resource)
        """

    async def start_speaker_search_task(
        self,
        *,
        Identifier: str,
        VoiceProfileDomainArn: str,
        KinesisVideoStreamSourceTaskConfiguration: KinesisVideoStreamSourceTaskConfigurationTypeDef = ...,
        ClientRequestToken: str = ...,
    ) -> StartSpeakerSearchTaskResponseTypeDef:
        """
        Starts a speaker search task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-media-pipelines.html#ChimeSDKMediaPipelines.Client.start_speaker_search_task)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_chime_sdk_media_pipelines/client/#start_speaker_search_task)
        """

    async def start_voice_tone_analysis_task(
        self,
        *,
        Identifier: str,
        LanguageCode: Literal["en-US"],
        KinesisVideoStreamSourceTaskConfiguration: KinesisVideoStreamSourceTaskConfigurationTypeDef = ...,
        ClientRequestToken: str = ...,
    ) -> StartVoiceToneAnalysisTaskResponseTypeDef:
        """
        Starts a voice tone analysis task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-media-pipelines.html#ChimeSDKMediaPipelines.Client.start_voice_tone_analysis_task)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_chime_sdk_media_pipelines/client/#start_voice_tone_analysis_task)
        """

    async def stop_speaker_search_task(
        self, *, Identifier: str, SpeakerSearchTaskId: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Stops a speaker search task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-media-pipelines.html#ChimeSDKMediaPipelines.Client.stop_speaker_search_task)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_chime_sdk_media_pipelines/client/#stop_speaker_search_task)
        """

    async def stop_voice_tone_analysis_task(
        self, *, Identifier: str, VoiceToneAnalysisTaskId: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Stops a voice tone analysis task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-media-pipelines.html#ChimeSDKMediaPipelines.Client.stop_voice_tone_analysis_task)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_chime_sdk_media_pipelines/client/#stop_voice_tone_analysis_task)
        """

    async def tag_resource(self, *, ResourceARN: str, Tags: Sequence[TagTypeDef]) -> Dict[str, Any]:
        """
        The ARN of the media pipeline that you want to tag.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-media-pipelines.html#ChimeSDKMediaPipelines.Client.tag_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_chime_sdk_media_pipelines/client/#tag_resource)
        """

    async def untag_resource(self, *, ResourceARN: str, TagKeys: Sequence[str]) -> Dict[str, Any]:
        """
        Removes any tags from a media pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-media-pipelines.html#ChimeSDKMediaPipelines.Client.untag_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_chime_sdk_media_pipelines/client/#untag_resource)
        """

    async def update_media_insights_pipeline_configuration(
        self,
        *,
        Identifier: str,
        ResourceAccessRoleArn: str,
        Elements: Sequence[MediaInsightsPipelineConfigurationElementTypeDef],
        RealTimeAlertConfiguration: RealTimeAlertConfigurationTypeDef = ...,
    ) -> UpdateMediaInsightsPipelineConfigurationResponseTypeDef:
        """
        Updates the media insights pipeline's configuration settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-media-pipelines.html#ChimeSDKMediaPipelines.Client.update_media_insights_pipeline_configuration)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_chime_sdk_media_pipelines/client/#update_media_insights_pipeline_configuration)
        """

    async def update_media_insights_pipeline_status(
        self, *, Identifier: str, UpdateStatus: MediaPipelineStatusUpdateType
    ) -> EmptyResponseMetadataTypeDef:
        """
        Updates the status of a media insights pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-media-pipelines.html#ChimeSDKMediaPipelines.Client.update_media_insights_pipeline_status)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_chime_sdk_media_pipelines/client/#update_media_insights_pipeline_status)
        """

    async def update_media_pipeline_kinesis_video_stream_pool(
        self,
        *,
        Identifier: str,
        StreamConfiguration: KinesisVideoStreamConfigurationUpdateTypeDef = ...,
    ) -> UpdateMediaPipelineKinesisVideoStreamPoolResponseTypeDef:
        """
        Updates an Kinesis video stream pool in a media pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-media-pipelines.html#ChimeSDKMediaPipelines.Client.update_media_pipeline_kinesis_video_stream_pool)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_chime_sdk_media_pipelines/client/#update_media_pipeline_kinesis_video_stream_pool)
        """

    async def __aenter__(self) -> "ChimeSDKMediaPipelinesClient":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-media-pipelines.html#ChimeSDKMediaPipelines.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_chime_sdk_media_pipelines/client/)
        """

    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> Any:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-media-pipelines.html#ChimeSDKMediaPipelines.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_chime_sdk_media_pipelines/client/)
        """
