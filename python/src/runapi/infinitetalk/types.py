"""InfiniteTalk model lists, enums, and response models."""

from __future__ import annotations

from runapi.core import BaseModel, TaskResponse, optional, required

MODELS = ["infinitetalk-from-audio"]
RESOLUTIONS = ["480p", "720p"]


class Video(BaseModel):
    url = optional(str)


class AudioToVideoResponse(TaskResponse):
    """Response for an audio-to-video task."""

    id = required(str)
    status = optional(str, enum=lambda: TaskResponse.Status.ALL)
    videos = optional([lambda: Video])
    error = optional(str)


class CompletedAudioToVideoResponse(AudioToVideoResponse):
    """Returned by ``audio_to_video.run()`` once polling observes completion.

    ``videos`` is required so callers never have to null-check it on success.
    """

    videos = required([lambda: Video])
