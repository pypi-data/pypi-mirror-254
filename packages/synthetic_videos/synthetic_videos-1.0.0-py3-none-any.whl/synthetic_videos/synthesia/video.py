from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from io import BytesIO
import json
from pathlib import Path
import time
from typing import Any, Optional

from loguru import logger
import requests

from synthetic_videos.pjlogging.logger import init_pjlogger
from synthetic_videos.synthesia.models import (
    DownloadFileError,
    UploadFileError,
    VideoGenerationResult,
    VideoGenerationStatus,
)
from synthetic_videos.synthesia.models import GetVideoParams as SynthesiaVideoParams
from synthetic_videos.synthetic_videos_interface import SyntheticVideosInterface
from synthetic_videos.utils.utils import requests_retry_session

init_pjlogger()

API_Key = "c277290dd73f5fe39029e071ac9bd671"


class Synthesia(SyntheticVideosInterface):
    """
    SyntheticVideosInterface implementation for Synthesia.
    """

    def __init__(self) -> None:
        """
        Initialize the Synthesia instance.
        """

        logger.info("Initializing Synthesia instance.")

    @logger.catch(reraise=True)
    def get_videos(self, params: list[SynthesiaVideoParams]) -> list[VideoGenerationResult]:
        """
        Generate synthetic videos using Synthesia.

        Parameters:
        params list[SynthesiaVideoParams]: The parameters for the videos to be generated.

        Returns:
        str | None: The URL of the generated video, or None if the video could not be generated.
        """
        logger.info("Generating synthetic videos with Synthesia.")
        logger.info("Params: {params}", params=len(params))
        # results = execute_in_parallel(self.__get_video, params, 10)
        # result = self.__get_video(params[0])
        results: list[VideoGenerationResult] = self.get_videos_in_parallel(params)
        return results

    def get_videos_in_parallel(
        self, video_params: list[SynthesiaVideoParams]
    ) -> list[VideoGenerationResult]:
        with ThreadPoolExecutor(max_workers=10) as executor:
            futures = [executor.submit(self.__get_video, param) for param in video_params]
        return [future.result() for future in futures]

    @logger.catch(reraise=True)
    def __prepare_get_video_payload(self, params: SynthesiaVideoParams) -> Any:
        """
        Prepare the payload with video details.

        Parameters:
            params (GetVideoParams): The parameters for the video.

        Returns:
            dict: The prepared payload.
        """
        payload: Any = {}

        # Check and set optional parameters in the payload
        if params.test is not None:
            payload["test"] = params.test
        if params.title is not None:
            payload["title"] = params.title
        if params.description is not None:
            payload["description"] = params.description

        # Check if 'input' parameter is provided and not empty
        if params.input is not None and len(params.input) > 0:
            payload["input"] = []
            for input in params.input:
                input_params = {}  # Dictionary to store individual input parameters

                # Handle audio script input
                if input.script_audio or input.local_audio_file_path:
                    uploaded_audio_result = self.__upload_audio(
                        input.script_audio, input.local_audio_file_path
                    )
                    logger.info(
                        "Uploaded audio result: {uploaded_audio_result}",
                        uploaded_audio_result=uploaded_audio_result,
                    )

                    # Add audio script ID to input parameters if upload was successful
                    if uploaded_audio_result is not None:
                        input_params["scriptAudio"] = uploaded_audio_result.get("id")
                        if input.local_audio_file_path:
                            input_params["scriptLanguage"] = "en-US"

                elif input.script_text is not None:
                    # Add script text directly if audio script is not provided
                    input_params["scriptText"] = input.script_text

                # Set language for the script if the field is provided
                if input.script_language is not None:
                    input_params["scriptLanguage"] = input.script_language

                # Check and set avatar settings if provided
                if input.avatar_settings is not None and (
                    input.avatar_settings.voice is not None
                    or input.avatar_settings.style is not None
                    or input.avatar_settings.scale is not None
                    or input.avatar_settings.horizontal_align is not None
                ):
                    input_params["avatarSettings"] = {}  # Initialize avatar settings dict

                    # Set individual avatar settings if they are provided
                    if input.avatar_settings.voice is not None:
                        input_params["avatarSettings"]["voice"] = input.avatar_settings.voice
                    if input.avatar_settings.style is not None:
                        input_params["avatarSettings"]["style"] = input.avatar_settings.style
                    if input.avatar_settings.scale is not None:
                        input_params["avatarSettings"]["scale"] = input.avatar_settings.scale
                    if input.avatar_settings.horizontal_align is not None:
                        input_params["avatarSettings"][
                            "horizontalAlign"
                        ] = input.avatar_settings.horizontal_align

                # Set background and avatar parameters if they are provided
                if input.background is not None:
                    input_params["background"] = input.background
                if input.avatar is not None:
                    input_params["avatar"] = input.avatar

                # Append the processed input parameters to the payload's 'input' list
                payload["input"].append(input_params)

        # Return the fully constructed payload
        return payload

    @logger.catch(reraise=True)
    def __retrieve_video(self, video_id: str) -> Any:
        """
        Periodically checks the status of a video creation process by calling the Synthesia API every 60 seconds.
        Continues until the JSON response has a status field with the value "complete". Will timeout if video
        could not be generated even agter after 60 minutes.

        Parameters:
        video_id (str): The ID of the video whose status is to be checked.

        Returns:
        dict: The final JSON response when the video status is "complete".
        """
        url = f"https://api.synthesia.io/v2/videos/{video_id}"

        headers = {"Authorization": API_Key, "Content-Type": "application/json"}
        max_timeout_minutes = 60
        start_time = datetime.now()

        # Make the GET  request to retrieve a video status
        session = requests_retry_session(retries=10)

        # Poll periodically until the video is generated or timeout is reached
        while True:
            # Retry upto 10 times in case of common errors or rate limiting errors

            response = session.get(url, headers=headers)

            # Log exceptions if the status code is not 200
            if response.status_code != 200:
                logger.exception(
                    "Error retrieving video. Status code: {status_code}",
                    status_code=response.status_code,
                )
                logger.exception("Error retrieving video. Response: {response}", response=response)
                return None

            # Parse the response content as JSON
            data = response.json()

            # If the status is complete, return the data
            if data.get("status") == "complete":
                return data
            elif data.get("status") == "error":
                # Log an error message if the status is error
                logger.exception(
                    "Error retrieving video. Response: {response}", response=response.text
                )
                return None

            # Log the ID of the video being generated
            logger.info(
                "Video generation in progress. Waiting for 60 seconds before next check. video ID: {video_id}",
                video_id=video_id,
            )

            time.sleep(60)  # Wait for 60 seconds before next check

            time_difference = (datetime.now() - start_time).total_seconds() / 60

            # We've exceed timeout minutes without any success, so we should exit
            if time_difference > max_timeout_minutes:
                logger.exception("Timeout while waiting for video to be generated.")
                return None

    @logger.catch(reraise=True)
    def __upload_audio(
        self, source_audio_url: Optional[str] = None, local_audio_file_path: Optional[str] = None
    ) -> Any:
        """
        Downloads an audio file from a given URL and uploads it to the Synthesia API.
        Retries up to 5 times in case of certain HTTP errors.

        Parameters:
        source_audio_url (str): The URL of the audio file to be downloaded.
        local_audio_file_path (str, optional): The local path of the audio file to be uploaded.

        Returns:
        dict: The response from the Synthesia API.
        """

        logger.info("Invoked.")

        logger.info(
            "Uploading audio from URL: {source_audio_url}", source_audio_url=source_audio_url
        )
        session = requests_retry_session(retries=5)
        headers = {"Authorization": API_Key, "Content-Type": "audio/mpeg"}

        # If local_file_path is provided, upload the local file
        if local_audio_file_path:
            logger.info(
                "Uploading audio from local file: {local_file_path}",
                local_file_path=local_audio_file_path,
            )
            with open(local_audio_file_path, "rb") as f:
                audio_data = f.read()

        # Otherwise, download the audio file from source_audio_url and upload it
        else:
            logger.info(
                "Uploading audio from URL: {source_audio_url}", source_audio_url=source_audio_url
            )
            # Step 1: Download the audio file
            response = session.get(source_audio_url)
            if response.status_code != 200:
                logger.exception(
                    "Error downloading audio file. Status code: {status_code}",
                    status_code=response.status_code,
                )
                raise DownloadFileError(
                    f"Failed to download audio file: {source_audio_url}. Status code: {response.status_code} "
                )
            audio_data = response.content

        # Step 2: Upload the audio file to Synthesia
        audio_data = BytesIO(audio_data)
        upload_response = session.post(
            "https://upload.api.synthesia.io/v2/scriptAudio", headers=headers, data=audio_data
        )

        if upload_response.status_code != 200 and upload_response.status_code != 201:
            logger.exception(
                "Error uploading audio file. Status code: {status_code}",
                status_code=upload_response.status_code,
            )
            logger.exception(
                "Error uploading audio file. Response text: {response_text}",
                response_text=upload_response.text,
            )
            raise UploadFileError(
                f"Failed to upload audio file: {source_audio_url}. Status code: {response.status_code}"
            )

        return upload_response.json()

    @logger.catch(reraise=True)
    def __get_video(self, params: SynthesiaVideoParams) -> VideoGenerationResult:
        """
        Returns generated video with status.
        """

        logger.info("Invoked.")
        video_generation_result: VideoGenerationResult = VideoGenerationResult(
            status=VideoGenerationStatus.ERROR,
            slide_id=params.slide_id,
            narration_id=params.narration_id,
        )
        logger.info(
            "Generating video for Slide ID: {slideid}, Narration ID: {narrationid}.",
            slideid=params.slide_id,
            narrationid=params.narration_id,
        )

        # URL for creating a video in Synthesia
        url = "https://api.synthesia.io/v2/videos"

        # Prepare the headers with the API key
        headers = {"Authorization": API_Key, "Content-Type": "application/json"}

        try:
            # Prepare the payload with video details
            payload = self.__prepare_get_video_payload(params)
            logger.info("Payload: {payload}", payload=payload)
            # Make the POST request to create a video
            session = requests_retry_session(retries=5)

            # logger.info("Payload: {payload}", payload=json.dumps(payload))
            response = session.post(url, headers=headers, data=json.dumps(payload))
            response.raise_for_status()  # Raises an HTTPError for bad responses
            if response.status_code == 200 or response.status_code == 201:
                # Parse the response content as JSON
                response_json = response.json()

                if response_json.get("status") == "in_progress" and response_json.get("id"):
                    # Log the ID of the video being generated
                    logger.info(
                        "Video generation queued successfulully, waiting for completion of video ID: {video_id}",
                        video_id=response_json.get("id"),
                    )

                    # Wait for 60 seconds before checking the status of the video
                    time.sleep(60)

                    # Retrieve the video using the ID from the response
                    video_data = self.__retrieve_video(response_json.get("id"))

                    if video_data is not None:
                        # Log the response and update the video generation result
                        logger.info("Video generation complete.")
                        video_generation_result.slide_id = params.slide_id
                        video_generation_result.narration_id = params.narration_id
                        video_generation_result.status = VideoGenerationStatus.SUCCESS
                        video_generation_result.video_url = video_data["download"]
                        video_generation_result.video_id = video_data["id"]
                        return video_generation_result
                    else:
                        # Log an error message and update the video generation result
                        logger.exception("Error retrieving video.")
                        video_generation_result.status = VideoGenerationStatus.ERROR
                        video_generation_result.error_message = "Error retrieving video."
                        return video_generation_result
                else:
                    # Log an error message if the response is unexpected
                    logger.exception(
                        "Unexpected response when generating video: {response}", response=response
                    )
            else:
                # Log an error message if the status code is unexpected
                logger.exception(
                    "Unexpected status when generating video: {response}", response=response
                )

        # Handle specific exceptions that can occur during the request
        except requests.exceptions.HTTPError as errh:
            # Log the error and update the video generation result
            video_generation_result.status = VideoGenerationStatus.ERROR
            video_generation_result.error_code = str(errh.response.status_code)
            video_generation_result.error_message = f"HTTP Error: {errh}"
            logger.exception("HTTP Error: {errh}", errh=errh)
            logger.exception("Response: {response}", response=response.text)
        except requests.exceptions.ConnectionError as errc:
            # Log the error and update the video generation result
            video_generation_result.status = VideoGenerationStatus.ERROR
            video_generation_result.error_message = f"ConnectionError Error: {errc}"
            logger.exception("Connection Error: {errc}", errc=errc)
        except requests.exceptions.Timeout as errt:
            # Log the error and update the video generation result
            video_generation_result.status = VideoGenerationStatus.ERROR
            video_generation_result.error_message = f"Timeout Error: {errt}"
            logger.exception("Timeout Error: {errt}", errt=errt)
        except requests.exceptions.RequestException as err:
            # Log the error and update the video generation result
            video_generation_result.status = VideoGenerationStatus.ERROR
            video_generation_result.error_message = f"RequestException Error: {err}"
            logger.exception("RequestException Error: {err}", err=err)
        except UploadFileError as upex:
            # Log the error and update the video generation result
            video_generation_result.status = VideoGenerationStatus.ERROR
            video_generation_result.error_message = f"UploadFileException Error: {upex}"
            logger.exception("UploadFileException Error: {err}", err=upex)
        except DownloadFileError as dlex:
            # Log the error and update the video generation result
            video_generation_result.status = VideoGenerationStatus.ERROR
            video_generation_result.error_message = f"DownloadFileException Error: {dlex}"
            logger.exception("DownloadFileException Error: {err}", err=dlex)
        except Exception as ex:
            # Log the error and update the video generation result
            video_generation_result.status = VideoGenerationStatus.ERROR
            video_generation_result.error_message = f"Exception Error: {ex}"
            logger.exception("Exception Error: {err}", err=ex)

        return video_generation_result
