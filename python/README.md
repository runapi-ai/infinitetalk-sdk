# InfiniteTalk Python SDK for RunAPI

The InfiniteTalk Python SDK is the language-specific package for InfiniteTalk on RunAPI. Use this package for video generation, animation, and video editing workflows when your application needs request bodies, task status lookup, and consistent RunAPI errors in Python.

This README is the Python package guide inside the public `infinitetalk-sdk` repository. For the repository overview, start at `../README.md`; for model details, use https://runapi.ai/models/infinitetalk; for API reference, use https://runapi.ai/docs/api/infinitetalk/audio-to-video; for SDK docs, use https://runapi.ai/docs/resources/sdks.

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
    source_image_url="https://cdn.runapi.ai/public/samples/portrait.jpg",
    source_audio_url="https://cdn.runapi.ai/public/samples/voice.mp3",
    prompt="A person speaking to the camera",
    output_resolution="720p",
)
status = client.audio_to_video.get(task.id)
```

Use `create` to submit a task and return quickly, `get` to fetch the latest task state, and `run` to create and poll until completion:

```python
result = client.audio_to_video.run(
    model="infinitetalk-from-audio",
    source_image_url="https://cdn.runapi.ai/public/samples/portrait.jpg",
    source_audio_url="https://cdn.runapi.ai/public/samples/voice.mp3",
    prompt="A person speaking to the camera",
)
print(result.videos[0].url)
```

In web request handlers, prefer `create` plus webhook or later `get` polling so a worker is not held open.

RunAPI-generated file URLs are temporary. Download and store generated images, videos, audio, or other files in your own durable storage within 7 days; do not treat returned URLs as long-term assets.

## Language notes

Pass parameters as keyword arguments and catch the `runapi.infinitetalk` error classes when building video jobs or scripts. The available resource is `audio_to_video`. Keep `RUNAPI_API_KEY` in the environment or your secret manager; never commit API keys or callback secrets.

## Links

- Model page: https://runapi.ai/models/infinitetalk
- SDK docs: https://runapi.ai/docs/resources/sdks
- Product docs: https://runapi.ai/docs/api/infinitetalk/audio-to-video
- Pricing and rate limits: https://runapi.ai/models/infinitetalk
- Provider comparison: https://runapi.ai/providers/meigen-ai
- Full catalog: https://runapi.ai/models
- Repository: https://github.com/runapi-ai/infinitetalk-sdk

## License

Licensed under the Apache License, Version 2.0.
