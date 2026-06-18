# InfiniteTalk Python SDK for RunAPI

The InfiniteTalk Python SDK is the language-specific package for InfiniteTalk on RunAPI. Use this infinitetalk api package for audio-to-video, talking-portrait, and animation flows when your application needs JSON request bodies, task status lookup, and consistent RunAPI errors in Python.

This infinitetalk api README is the Python package guide inside the public `infinitalk-sdk` repository. For the repository overview, start at `../README.md`; for model details, use https://runapi.ai/models/infinitalk; for API reference, use https://runapi.ai/docs#infinitalk; for SDK docs, use https://runapi.ai/docs#sdk-infinitalk.

## Install

```bash
pip install runapi-infinitetalk
```

## Quick start

```python
from runapi.infinitetalk import InfinitetalkClient

client = InfinitetalkClient()  # reads RUNAPI_API_KEY, or pass api_key="sk-..."

task = client.audio_to_video.create(
    model="infinitetalk-from-audio",
    source_image_url="https://example.com/face.jpg",
    source_audio_url="https://example.com/voice.mp3",
    prompt="A person speaking to the camera",
    output_resolution="720p",
)
status = client.audio_to_video.get(task.id)
```

Use `create` to submit a task and return quickly, `get` to fetch the latest task state, and `run` to create and poll until completion:

```python
result = client.audio_to_video.run(
    model="infinitetalk-from-audio",
    source_image_url="https://example.com/face.jpg",
    source_audio_url="https://example.com/voice.mp3",
    prompt="A person speaking to the camera",
)
print(result.videos[0].url)
```

In web request handlers, prefer `create` plus webhook or later `get` polling so a worker is not held open.

RunAPI-generated file URLs are temporary. Download and store generated images, videos, audio, or other files in your own durable storage within 7 days; do not treat returned URLs as long-term assets.

## Language notes

Pass parameters as keyword arguments and catch the `runapi.infinitetalk` error classes when building video jobs or scripts. The available resource is `audio_to_video`. Keep `RUNAPI_API_KEY` in the environment or your secret manager; never commit API keys or callback secrets.

## Links

- Model page: https://runapi.ai/models/infinitalk
- SDK docs: https://runapi.ai/docs#sdk-infinitalk
- Product docs: https://runapi.ai/docs#infinitalk
- Pricing and rate limits: https://runapi.ai/models/infinitalk
- Provider comparison: https://runapi.ai/providers/meigen-ai
- Full catalog: https://runapi.ai/models
- Repository: https://github.com/runapi-ai/infinitalk-sdk

## License

Licensed under the Apache License, Version 2.0.
