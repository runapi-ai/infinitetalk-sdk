import pytest

from runapi.core import config
from runapi.core.errors import AuthenticationError, ValidationError
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
    source_image_url="https://example.com/face.jpg",
    source_audio_url="https://example.com/voice.mp3",
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
                "source_image_url": "https://example.com/face.jpg",
                "source_audio_url": "https://example.com/voice.mp3",
                "prompt": "A person speaking to the camera",
                "output_resolution": "720p",
            },
        ),
    ]
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
        {"id": "t1", "status": "completed", "videos": [{"url": "https://x/y.mp4"}]},
    )
    client = InfinitetalkClient(api_key="k", http_client=fake)
    result = client.audio_to_video.run(**VALID_PARAMS)

    assert isinstance(result, CompletedAudioToVideoResponse)
    assert result.videos[0].url == "https://x/y.mp4"
    assert [call[0] for call in fake.calls] == ["post", "get"]


# --- validation -----------------------------------------------------------


def test_create_requires_model():
    client = InfinitetalkClient(api_key="k", http_client=FakeHttp())
    params = {k: v for k, v in VALID_PARAMS.items() if k != "model"}
    with pytest.raises(ValidationError, match="model is required"):
        client.audio_to_video.create(**params)


def test_create_rejects_unknown_model():
    client = InfinitetalkClient(api_key="k", http_client=FakeHttp())
    params = {**VALID_PARAMS, "model": "not-a-model"}
    with pytest.raises(ValidationError, match="Invalid model"):
        client.audio_to_video.create(**params)


def test_create_requires_source_image_url():
    client = InfinitetalkClient(api_key="k", http_client=FakeHttp())
    params = {k: v for k, v in VALID_PARAMS.items() if k != "source_image_url"}
    with pytest.raises(ValidationError, match="source_image_url is required"):
        client.audio_to_video.create(**params)


def test_create_requires_source_audio_url():
    client = InfinitetalkClient(api_key="k", http_client=FakeHttp())
    params = {k: v for k, v in VALID_PARAMS.items() if k != "source_audio_url"}
    with pytest.raises(ValidationError, match="source_audio_url is required"):
        client.audio_to_video.create(**params)


def test_create_requires_prompt():
    client = InfinitetalkClient(api_key="k", http_client=FakeHttp())
    params = {k: v for k, v in VALID_PARAMS.items() if k != "prompt"}
    with pytest.raises(ValidationError, match="prompt is required"):
        client.audio_to_video.create(**params)


def test_create_rejects_overlong_prompt():
    client = InfinitetalkClient(api_key="k", http_client=FakeHttp())
    params = {**VALID_PARAMS, "prompt": "x" * 5001}
    with pytest.raises(ValidationError, match="prompt must be at most 5000 characters"):
        client.audio_to_video.create(**params)


def test_create_rejects_invalid_resolution():
    client = InfinitetalkClient(api_key="k", http_client=FakeHttp())
    params = {**VALID_PARAMS, "output_resolution": "1080p"}
    with pytest.raises(ValidationError, match="Invalid output_resolution"):
        client.audio_to_video.create(**params)


def test_create_rejects_seed_below_range():
    client = InfinitetalkClient(api_key="k", http_client=FakeHttp())
    params = {**VALID_PARAMS, "seed": 9999}
    with pytest.raises(
        ValidationError, match="seed must be an integer between 10000 and 1000000"
    ):
        client.audio_to_video.create(**params)


def test_create_rejects_seed_above_range():
    client = InfinitetalkClient(api_key="k", http_client=FakeHttp())
    params = {**VALID_PARAMS, "seed": 1_000_001}
    with pytest.raises(
        ValidationError, match="seed must be an integer between 10000 and 1000000"
    ):
        client.audio_to_video.create(**params)


def test_create_rejects_non_integer_seed():
    client = InfinitetalkClient(api_key="k", http_client=FakeHttp())
    params = {**VALID_PARAMS, "seed": "not-a-number"}
    with pytest.raises(
        ValidationError, match="seed must be an integer between 10000 and 1000000"
    ):
        client.audio_to_video.create(**params)


def test_create_rejects_bool_seed():
    client = InfinitetalkClient(api_key="k", http_client=FakeHttp())
    params = {**VALID_PARAMS, "seed": True}
    with pytest.raises(
        ValidationError, match="seed must be an integer between 10000 and 1000000"
    ):
        client.audio_to_video.create(**params)


def test_create_accepts_seed_in_range():
    fake = FakeHttp({"id": "t1", "status": "pending"})
    client = InfinitetalkClient(api_key="k", http_client=fake)
    client.audio_to_video.create(**VALID_PARAMS, seed=500_000)
    assert fake.calls[0][2]["seed"] == 500_000


def test_create_accepts_integer_string_seed():
    fake = FakeHttp({"id": "t1", "status": "pending"})
    client = InfinitetalkClient(api_key="k", http_client=fake)
    client.audio_to_video.create(**VALID_PARAMS, seed="500000")
    assert fake.calls[0][2]["seed"] == "500000"
