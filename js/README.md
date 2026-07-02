# InfiniteTalk JavaScript SDK for RunAPI

The InfiniteTalk JavaScript SDK is the language-specific package for InfiniteTalk on RunAPI. Use this package for video generation, animation, and video editing workflows when your application needs request bodies, task status lookup, and consistent RunAPI errors in JavaScript.

This README is the JavaScript package guide inside the public `infinitetalk-sdk` repository. For the repository overview, start at `../README.md`; for model details, use https://runapi.ai/models/infinitetalk; for API reference, use https://runapi.ai/docs#infinitetalk; for SDK docs, use https://runapi.ai/docs#sdk-infinitetalk.

## Install

```bash
npm install @runapi.ai/infinitetalk
```

## Quick start

```typescript
import { InfinitetalkClient } from '@runapi.ai/infinitetalk';

const client = new InfinitetalkClient();
const task = await client.audioToVideo.create({
  // Pass the InfiniteTalk JSON request body from https://runapi.ai/docs#infinitetalk.
});
const status = await client.audioToVideo.get(task.id);
```

Use `create` when you want to submit a task and return quickly, `get` when you need the latest task state, and `run` when a script should create and poll until completion. In web request handlers, prefer `create` plus webhook or later `get` polling so a worker is not held open.

RunAPI-generated file URLs are temporary. Download and store generated images, videos, audio, or other files in your own durable storage within 7 days; do not treat returned URLs as long-term assets.

## Language notes

Use the TypeScript types in `src/types.ts` and the resource classes under `src/resources` when building video applications. The available resources are `audioToVideo`. Keep `RUNAPI_API_KEY` in the environment or your secret manager; never commit API keys or callback secrets.

## Links

- Model page: https://runapi.ai/models/infinitetalk
- SDK docs: https://runapi.ai/docs#sdk-infinitetalk
- Product docs: https://runapi.ai/docs#infinitetalk
- Pricing and rate limits: https://runapi.ai/models/infinitetalk
- Provider comparison: https://runapi.ai/providers/meigen-ai
- Full catalog: https://runapi.ai/models
- Repository: https://github.com/runapi-ai/infinitetalk-sdk

## License

Licensed under the Apache License, Version 2.0.
