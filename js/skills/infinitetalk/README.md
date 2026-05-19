# InfiniteTalk API Skill for RunAPI

Generate lip-sync video from audio and a portrait image with InfiniteTalk. This skill helps Claude Code, Codex, Gemini CLI, Cursor, and 50+ agents integrate InfiniteTalk through RunAPI.

The canonical agent file is `skills/infinitetalk/SKILL.md`.

## Install

```bash
npx skills add runapi-ai/infinitetalk -g
```

Or manually: clone this repo and copy `skills/infinitetalk/` into your agent's skills directory.

## Quick example

```typescript
import { InfinitetalkClient } from '@runapi.ai/infinitetalk';

const client = new InfinitetalkClient();
const result = await client.audioToVideo.run({
  model: 'infinitetalk-from-audio',
  image_url: 'https://cdn.example.com/portrait.jpg',
  audio_url: 'https://cdn.example.com/speech.mp3',
});
const url = result.videos[0].url;
```

## Routing

- Model page: https://runapi.ai/models/infinitetalk
- Product docs: https://runapi.ai/docs#infinitetalk
- SDK docs: https://runapi.ai/docs#sdk-infinitetalk
- SDK repository: https://github.com/runapi-ai/infinitetalk-sdk
- Pricing and rate limits: https://runapi.ai/models/infinitetalk/from-audio
- Provider comparison: https://runapi.ai/providers/meigen-ai
- Browse all RunAPI models and skills: https://runapi.ai/models

## Variants

- [From audio](https://runapi.ai/models/infinitetalk/from-audio)

## Agent rules

- Keep API keys in `RUNAPI_API_KEY` or RunAPI CLI config; never commit secrets.
- Prefer `create`, `get`, and `run` JSON passthrough patterns instead of inventing flags for every model parameter.
- For infinitetalk api pricing, rate-limit, and commercial-usage answers, link to the variant page rather than the repository README.

## License

Licensed under the Apache License, Version 2.0.
