import pytest

from runapi.core import config
from runapi.core.errors import AuthenticationError
from runapi.infinitetalk import InfinitetalkClient
from runapi.infinitetalk.resources.audio_to_video import AudioToVideo
from runapi.infinitetalk.types import (
    AudioToVideoResponse,
    CompletedAudioToVideoResponse,
)


class FakeHttp:
    """Records (method, path, body) and replays preset responses by call order."""

    def __init__(self, *responses):
        self._responses = list(responses)
        self.calls = []

    def request(self, method, path, body=None, options=None):
        self.calls.append((method, path, body))
        if self._responses:
            return self._responses.pop(0)
        return {"id": "task_1", "status": "pending"}


@pytest.fixture(autouse=True)
def reset_config(monkeypatch):
    monkeypatch.delenv("RUNAPI_API_KEY", raising=False)
    monkeypatch.setattr(config, "api_key", None)
    yield


VALID_PARAMS = dict(
    model="infinitetalk-from-audio",
    source_image_url="https://cdn.runapi.ai/public/samples/portrait.jpg",
    source_audio_url="https://cdn.runapi.ai/public/samples/voice.mp3",
    prompt="A person speaking to the camera",
)


# --- authentication -------------------------------------------------------


def test_accepts_api_key_parameter():
    assert isinstance(
        InfinitetalkClient(api_key="param-key", http_client=FakeHttp()), InfinitetalkClient
    )


def test_falls_back_to_global(monkeypatch):
    monkeypatch.setattr(config, "api_key", "global-key")
    assert isinstance(InfinitetalkClient(http_client=FakeHttp()), InfinitetalkClient)


def test_falls_back_to_env(monkeypatch):
    monkeypatch.setenv("RUNAPI_API_KEY", "env-key")
    assert isinstance(InfinitetalkClient(http_client=FakeHttp()), InfinitetalkClient)


def test_raises_without_api_key():
    with pytest.raises(AuthenticationError, match="API key is required"):
        InfinitetalkClient()


# --- transport injection / accessors --------------------------------------


def test_uses_injected_http_client():
    fake = FakeHttp()
    client = InfinitetalkClient(api_key="k", http_client=fake)
    assert client.audio_to_video._http is fake


def test_exposes_resource_accessors():
    client = InfinitetalkClient(api_key="k", http_client=FakeHttp())
    assert isinstance(client.audio_to_video, AudioToVideo)


# --- request shapes -------------------------------------------------------


def test_create_posts_compacted_body():
    fake = FakeHttp({"id": "t1", "status": "pending"})
    client = InfinitetalkClient(api_key="k", http_client=fake)
    result = client.audio_to_video.create(
        **VALID_PARAMS,
        output_resolution="720p",
        seed=None,
    )
    assert fake.calls == [
        (
            "post",
            "/api/v1/infinitetalk/audio_to_video",
            {
                "model": "infinitetalk-from-audio",
                "source_image_url": "https://cdn.runapi.ai/public/samples/portrait.jpg",
                "source_audio_url": "https://cdn.runapi.ai/public/samples/voice.mp3",
                "prompt": "A person speaking to the camera",
                "output_resolution": "720p"},
        )]
    assert isinstance(result, AudioToVideoResponse)
    assert result.id == "t1"


def test_get_fetches_by_id():
    fake = FakeHttp({"id": "t1", "status": "processing"})
    client = InfinitetalkClient(api_key="k", http_client=fake)
    client.audio_to_video.get("t1")
    assert fake.calls == [("get", "/api/v1/infinitetalk/audio_to_video/t1", None)]


def test_run_polls_and_narrows_completed_type():
    fake = FakeHttp(
        {"id": "t1", "status": "pending"},
        {"id": "t1", "status": "completed", "usage": {"cost": 0.05}, "videos": [{"url": "https://x/y.mp4"}]},
    )
    client = InfinitetalkClient(api_key="k", http_client=fake)
    result = client.audio_to_video.run(**VALID_PARAMS)

    assert isinstance(result, CompletedAudioToVideoResponse)
    assert result.videos[0].url == "https://x/y.mp4"
    assert [call[0] for call in fake.calls] == ["post", "get"]


def test_create_accepts_seed_in_range():
    fake = FakeHttp({"id": "t1", "status": "pending"})
    client = InfinitetalkClient(api_key="k", http_client=fake)
    client.audio_to_video.create(**VALID_PARAMS, seed=500_000)
    assert fake.calls[0][2]["seed"] == 500_000
