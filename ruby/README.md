# Infinitetalk API Ruby SDK for RunAPI

The infinitetalk api Ruby SDK is the language-specific package for InfiniteTalk on RunAPI. Use this infinitetalk api package for text-to-video, image-to-video, video editing, and animation flows when your application needs JSON request bodies, task status lookup, and consistent RunAPI errors in Ruby.

This infinitetalk api README is the Ruby package guide inside the public `infinitalk-sdk` repository. For the repository overview, start at `../README.md`; for model details, use https://runapi.ai/models/infinitalk; for API reference, use https://runapi.ai/docs#infinitalk; for SDK docs, use https://runapi.ai/docs#sdk-infinitalk.

## Install

```bash
gem install runapi-infinitalk
```

## Quick start

```ruby
require "runapi-infinitalk"

client = RunApi::Infinitalk::Client.new
task = client.from_audios.create(
  # Pass the InfiniteTalk JSON request body from https://runapi.ai/docs#infinitalk.
)
status = client.from_audios.get(task.id)
```

Use `create` when you want to submit a task and return quickly, `get` when you need the latest task state, and `run` when a script should create and poll until completion. In web request handlers, prefer `create` plus webhook or later `get` polling so a worker is not held open.

RunAPI-generated file URLs are temporary. Download and store generated images, videos, audio, or other files in your own durable storage within 7 days; do not treat returned URLs as long-term assets.

## Language notes

Use Ruby keyword arguments and the `RunApi::Infinitalk` error classes when building video jobs, Rails workers, or scripts. The available resources include from audios. Keep `RUNAPI_API_KEY` in the environment or your secret manager; never commit API keys or callback secrets.

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
