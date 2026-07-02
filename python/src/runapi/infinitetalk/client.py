"""InfiniteTalk client."""

from __future__ import annotations

from typing import Any, Optional

from runapi.core import ClientOptions, HttpClient, resolve_api_key

from .resources.audio_to_video import AudioToVideo


class InfinitetalkClient:
    """InfiniteTalk audio-to-video client.

    Example::

        client = InfinitetalkClient(api_key="sk-...")
        result = client.audio_to_video.run(
            model="infinitetalk-from-audio",
            source_image_url="https://cdn.runapi.ai/public/samples/portrait.jpg",
            source_audio_url="https://cdn.runapi.ai/public/samples/voice.mp3",
            prompt="A person speaking to the camera",
        )
    """

    def __init__(self, api_key: Optional[str] = None, **options: Any) -> None:
        resolved_api_key = resolve_api_key(api_key)
        client_options = ClientOptions(api_key=resolved_api_key, **options)
        http = client_options.http_client or HttpClient(client_options)
        self.audio_to_video = AudioToVideo(http)
