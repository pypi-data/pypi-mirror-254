import logging
from typing import Optional

import numpy

logger = logging.getLogger()


class SocialMediaClient:
    """A client for posting images to social media platforms"""

    def post_image(self, title: str, image: numpy.ndarray) -> None:
        """Given an image array, post that image to social media"""
        logger.warning("Social Media posts are disabled - not posting")

    def upload_media(self, filename: str, thumbnail: Optional[str] = None) -> str:
        """upload media for use in post_status() - this method MUST be implemented by subclasses"""
        logger.warning("Social Media posts are disabled - not posting")
        return "fake media id"

    def upload_media_with_thumbnail(self, filename: str, thumbnail: numpy.ndarray) -> str:
        logger.warning("Social Media posts are disabled - not posting")
        return "fake media id"

    def upload_image(self, image: numpy.ndarray) -> str:
        logger.warning("Social Media posts are disabled - not posting")

    def post_status(self, title: str, media_ids: list[str] = []) -> None:
        """Post a status - this method MUST be implemented by subclasses"""
        logger.warning("Social Media posts are disabled - not posting")
