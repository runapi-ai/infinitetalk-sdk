"""InfiniteTalk audio-to-video resource."""

from __future__ import annotations

from typing import Any, Dict

from runapi.core import Resource, ValidationError

from ..contract_gen import CONTRACT
from ..types import (
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
        self._validate_contract(CONTRACT["audio-to-video"], params)

        prompt = params.get("prompt")
        if not (isinstance(prompt, str) and prompt != ""):
            raise ValidationError("prompt is required")
        if len(prompt) > PROMPT_MAX_LENGTH:
            raise ValidationError(f"prompt must be at most {PROMPT_MAX_LENGTH} characters")

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
