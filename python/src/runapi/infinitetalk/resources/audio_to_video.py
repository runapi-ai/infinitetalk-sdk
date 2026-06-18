"""InfiniteTalk audio-to-video resource."""

from __future__ import annotations

from typing import Any, Dict

from runapi.core import Resource, ValidationError

from ..types import (
    MODELS,
    RESOLUTIONS,
    AudioToVideoResponse,
    CompletedAudioToVideoResponse,
)

PROMPT_MAX_LENGTH = 5000
SEED_RANGE = range(10_000, 1_000_001)


class AudioToVideo(Resource):
    """Generate a talking-head video from a source image and audio track."""

    ENDPOINT = "/api/v1/infinitetalk/audio_to_video"

    RESPONSE_CLASS = AudioToVideoResponse
    COMPLETED_RESPONSE_CLASS = CompletedAudioToVideoResponse

    def run(self, **params: Any) -> Any:
        """Create a task and poll until it completes."""
        task = self.create(**params)
        return self._poll_until_complete(lambda: self.get(task.id))

    def create(self, **params: Any) -> Any:
        """Create an audio-to-video task and return immediately with an ``id``."""
        compacted = self._compact_params(params)
        self._validate_params(compacted)
        return self._request("post", self.ENDPOINT, body=compacted)

    def get(self, id: str) -> Any:
        """Fetch the current status of an audio-to-video task."""
        return self._request("get", f"{self.ENDPOINT}/{id}")

    def _validate_params(self, params: Dict[str, Any]) -> None:
        model = params.get("model")
        if not model:
            raise ValidationError("model is required")
        if model not in MODELS:
            joined = ", ".join(MODELS)
            raise ValidationError(f"Invalid model: {model}. Must be one of: {joined}")

        self._validate_required(params, "source_image_url")
        self._validate_required(params, "source_audio_url")

        prompt = params.get("prompt")
        if not (isinstance(prompt, str) and prompt != ""):
            raise ValidationError("prompt is required")
        if len(prompt) > PROMPT_MAX_LENGTH:
            raise ValidationError(f"prompt must be at most {PROMPT_MAX_LENGTH} characters")

        self._validate_optional(params, "output_resolution", RESOLUTIONS)

        seed = params.get("seed")
        if seed is None:
            return

        parsed = self._parse_integer(seed)
        if parsed is not None and parsed in SEED_RANGE:
            return

        raise ValidationError(
            f"seed must be an integer between {SEED_RANGE.start} and {SEED_RANGE.stop - 1}"
        )

    @staticmethod
    def _validate_required(params: Dict[str, Any], key: str) -> None:
        value = params.get(key)
        present = (value != "") if isinstance(value, str) else (value is not None)
        if not present:
            raise ValidationError(f"{key} is required")

    @staticmethod
    def _parse_integer(value: Any) -> Any:
        """Mirror Ruby ``Integer(value, exception: false)``.

        Accepts ints and integer-looking strings; rejects bools and anything
        non-coercible by returning ``None``.
        """
        if isinstance(value, bool):
            return None
        if isinstance(value, int):
            return value
        if isinstance(value, str):
            try:
                return int(value.strip(), 10)
            except ValueError:
                return None
        return None
