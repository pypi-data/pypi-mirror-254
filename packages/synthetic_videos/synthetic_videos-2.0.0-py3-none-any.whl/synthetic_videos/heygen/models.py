"""Constants, enums and data transfer classes"""
from __future__ import annotations

from dataclasses import dataclass
from enum import IntEnum


@dataclass
class GetVideoParams:
    """
    A dataclass for storing information required to create a video using the HeyGen API.

    Attributes:
        slide_id (str): The ID of the slide to which this video belongs.
        narration_id (str): The ID of the narration on the slide to be used for this video.
        title (str): The title of the video.
        description (str): The description of the video.
        input (List[VideoSegment]): The list of video segments for the video.
        test (bool, optional): Test videos are free and not counted towards your quota. Defaults to False.
        background (str): The background of the video
    """

    slide_id: str
    narration_id: str
    title: str
    description: str
    input: list[VideoSegment]
    test: bool = False
    background: str = "#17BF8D"


@dataclass
class AvatarSettings:
    """
    A dataclass representing the settings for an avatar.

    Attributes:
        voice (str): The ID of the avatar voice to be used for speaking the script.
        horizontal_align (str): The horizontal alignment of the avatar, with supported values 'left', 'center', 'right'. Defaults to "center".
        scale (float): The scale of the avatar. Optional. Defaults to 1.0.
        style (str): The style of the avatar. Optional. Defaults to "rectangular".
    """

    voice: str
    horizontal_align: str = "center"
    scale: float = 1.0
    style: str = "rectangular"


@dataclass
class VideoSegment:
    """
    A dataclass representing a segment of a video.

    Attributes:
        script_text (str): The text of the script.
        script_audio (str): The audio of the script.
        avatar_settings (AvatarSettings): The settings for the avatar.
        script_language (str, optional): The language of the script. Defaults to "en-US".
        avatar (str, optional): The avatar used. Defaults to "anna_costume1_cameraA".
        background (str, optional): The background used. Defaults to "green_screen".
    """

    avatar_id: str = "Daisy-inskirt-20220818"
    avatar_style: str = "normal"
    input_text: str | None = None
    input_audio: str | None = None
    scale: float = 1
    local_audio_file_path: str = None
    # add offset default


@dataclass
class VideoGenerationStatus(IntEnum):
    """Enum for the type of content in a node"""

    SUCCESS = 1
    ERROR = 2


@dataclass
class VideoGenerationResult:
    """
    A dataclass representing the result of a video generation operation.

    Attributes:
        status (VideoGenerationStatus): The status of the video generation operation.
        error_message (str, optional): An error message, if any, from the video generation operation.
        error_code (str, optional): An error code, if any, from the video generation operation.
        video_url (str, optional): The URL of the generated video, if the operation was successful.
        video_id (str, optional): The ID of the generated video, if the operation was successful.
        slide_id (str, optional): The ID of the slide used in the video generation operation.
        narration_id (str, optional): The ID of the narration used in the video generation operation.
    """

    status: VideoGenerationStatus
    error_message: str | None = None
    error_code: str | None = None
    video_url: str | None = None
    video_id: str | None = None
    slide_id: str | None = None
    narration_id: str | None = None


class DownloadFileError(Exception):
    def __init__(self, message: str = "Error downloading file"):
        # Call the base class constructor with the parameters it needs
        super().__init__(message)


class UploadFileError(Exception):
    def __init__(self, message: str = "Error uploading file"):
        # Call the base class constructor with the parameters it needs
        super().__init__(message)
