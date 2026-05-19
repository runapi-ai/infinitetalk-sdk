---
name: infinitetalk
description: Generate lip-sync video from audio with InfiniteTalk through RunAPI.ai using the @runapi.ai/infinitetalk Node/TypeScript SDK. Use when the user asks for lip-sync video, talking-head generation, InfiniteTalk, or writes against @runapi.ai/infinitetalk. Triggers on "infinitetalk", "lip-sync video", "lip sync", "audio to video", "@runapi.ai/infinitetalk".
documentation: https://runapi.ai/models/infinitetalk
provider_page: https://runapi.ai/providers/meigen-ai
catalog: https://runapi.ai/models
---
# @runapi.ai/infinitetalk -- RunAPI.ai InfiniteTalk lip-sync video

Build Node / TypeScript integrations that generate lip-sync video from audio with InfiniteTalk through RunAPI.ai.

## Setup

Requires **Node 18+** (global `fetch`).

```bash
npm install @runapi.ai/infinitetalk
```

```dotenv
# .env
RUNAPI_API_KEY=runapi_xxx   # get one at https://runapi.ai/settings/api_keys
```

```ts
import { InfinitetalkClient } from '@runapi.ai/infinitetalk';

const client = new InfinitetalkClient();
```

Pass `{ apiKey }` explicitly if you manage secrets differently. `baseUrl` defaults to `https://runapi.ai`; override only for local development.

## Resource

`client.audioToVideo` uses the async task contract:

```ts
const { id } = await client.audioToVideo.create({ ... });
const status = await client.audioToVideo.get(id);
const result = await client.audioToVideo.run({ ... });
```

## Audio to video

```ts
const result = await client.audioToVideo.run({
  model: 'infinitetalk-from-audio',
  image_url: 'https://cdn.example.com/portrait.jpg',
  audio_url: 'https://cdn.example.com/speech.mp3',
});

const url = result.videos[0].url;
```

## Errors

All errors are re-exported from `@runapi.ai/core`. Use `instanceof` checks instead of string-matching messages. For long-running tasks, prefer `create()` plus webhook or `get(id)` in request handlers, and reserve `run()` for jobs / CLI.

## RunAPI public routing

infinitetalk api public links use the API-379 catalog route map. The main infinitetalk api page is https://runapi.ai/models/infinitetalk. SDK docs live at https://runapi.ai/docs#sdk-infinitetalk and product docs live at https://runapi.ai/docs#infinitetalk.

Pricing, rate limits, and commercial usage for infinitetalk api should point to the most specific variant page:
- [From audio](https://runapi.ai/models/infinitetalk/from-audio)

Compare InfiniteTalk with other MeiGen-AI models at https://runapi.ai/providers/meigen-ai. Browse every RunAPI model and skill at https://runapi.ai/models. SDK repository: https://github.com/runapi-ai/infinitetalk-sdk. Skill repository: https://github.com/runapi-ai/infinitetalk.
