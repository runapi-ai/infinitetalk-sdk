<p align="center">
  <a href="https://github.com/runapi-ai/infinitetalk">
    <h3 align="center">InfiniteTalk API Skill for RunAPI</h3>
  </a>
</p>

<p align="center">
  Install this agent skill, inspect InfiniteTalk fields, then run jobs through the RunAPI CLI.
</p>

<p align="center">
  <a href="https://runapi.ai/models/infinitetalk"><strong>Model Reference</strong></a> · <a href="https://github.com/runapi-ai/cli"><strong>CLI</strong></a> · <a href="https://github.com/runapi-ai/infinitetalk-sdk"><strong>SDK</strong></a>
</p>

<div align="center">

[![skills.sh](https://www.skills.sh/b/runapi-ai/infinitetalk)](https://www.skills.sh/runapi-ai/infinitetalk/infinitetalk)
[![ClawHub](https://img.shields.io/badge/ClawHub-runapi--infinitetalk-111827)](https://clawhub.ai/runapi-ai/runapi-infinitetalk)
[![License](https://img.shields.io/github/license/runapi-ai/infinitetalk)](https://github.com/runapi-ai/infinitetalk/blob/main/LICENSE)

</div>
<br/>

Generate lip-sync video from audio and a portrait image with InfiniteTalk. This skill helps Claude Code, Codex, Gemini CLI, Cursor, and 50+ agents integrate InfiniteTalk through RunAPI.

The canonical agent file is `skills/infinitetalk/SKILL.md`.

## Install

```bash
npx skills add runapi-ai/infinitetalk -g
```

Or paste this prompt to your AI agent:

```text
Install the infinitetalk skill for me:

1. Clone https://github.com/runapi-ai/infinitetalk
2. Copy the skills/infinitetalk/ directory into your
   user-level skills directory (e.g. ~/.claude/skills/
   for Claude Code, ~/.codex/skills/ for Codex).
3. Verify that SKILL.md is present.
4. Confirm the install path when done.
```

## Quick example

```typescript
import { InfinitetalkClient } from '@runapi.ai/infinitetalk';

const client = new InfinitetalkClient();
const result = await client.audioToVideo.run({
  model: 'infinitetalk-from-audio',
  source_image_url: 'https://cdn.runapi.ai/public/samples/portrait.jpg',
  source_audio_url: 'https://cdn.runapi.ai/public/samples/voice.mp3',
});
const url = result.videos[0].url;
```

## Routing

- Model page: https://runapi.ai/models/infinitetalk
- Product docs: https://runapi.ai/docs#infinitetalk
- SDK docs: https://runapi.ai/docs#sdk-infinitetalk
- SDK repository: https://github.com/runapi-ai/infinitetalk-sdk
- Pricing and rate limits: https://runapi.ai/models/infinitetalk
- Provider comparison: https://runapi.ai/providers/meigen-ai
- Browse all RunAPI models and skills: https://runapi.ai/models

## Agent rules

- Integration work uses the target language SDK; one-off generation, manual smoke tests, debugging, or user-requested CLI runs use the RunAPI CLI skill: https://github.com/runapi-ai/cli-skill
- RunAPI-generated file URLs are temporary. Download and store generated images, videos, audio, or other files in your own durable storage within 7 days; do not treat returned URLs as long-term assets.
- Keep API keys in `RUNAPI_API_KEY` or RunAPI CLI config; never commit secrets.
- Prefer `create`, `get`, and `run` JSON passthrough patterns instead of inventing flags for every model parameter.
- For infinitetalk api pricing, rate-limit, and commercial-usage answers, link to the model page rather than the repository README.

## License

Licensed under the Apache License, Version 2.0.
