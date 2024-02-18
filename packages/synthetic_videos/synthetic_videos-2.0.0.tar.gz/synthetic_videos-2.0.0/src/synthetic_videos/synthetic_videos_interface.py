"""Interface that all specialized synthetic video generators need to implement"""
from abc import ABC, abstractmethod
from typing import List

from synthetic_videos.synthesia.models import GetVideoParams as SynthesiaVideoParams
from synthetic_videos.synthesia.models import VideoGenerationResult

from synthetic_videos.heygen.models import GetVideoParams as HeyGenVideoParams
from synthetic_videos.heygen.models import VideoGenerationResult

class SyntheticVideosInterface(ABC):
    """Minimum set of properties that all concrete classes need to implement
    to generate a standardized output"""

    @abstractmethod
    def get_videos(self, params: List[SynthesiaVideoParams]) -> list[VideoGenerationResult]:
        """Generate synthetic videos based on the input parameters

        Args:
            params (List[SynthesiaVideoParams]): List of parameters to generate the synthetic videos

        Returns:
            list[VideoGenerationResult]: List of results for each video generated"""

class HeyGenVideosInterface(ABC):
    """Minimum set of properties that all concrete classes need to implement
    to generate a standardized output"""

    @abstractmethod
    def get_videos(self, params: List[HeyGenVideoParams]) -> list[VideoGenerationResult]:
        """Generate synthetic videos based on the input parameters

        Args:
            params (List[HeyGenVideoParams]): List of parameters to generate the synthetic videos

        Returns:
            list[VideoGenerationResult]: List of results for each video generated"""