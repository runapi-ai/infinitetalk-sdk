<p align="center">
  <a href="https://runapi.ai"><img src="https://runapi.ai/icon.svg" height="56" alt="RunAPI"></a>
</p>

<h3 align="center">
  <a href="https://github.com/runapi-ai/infinitetalk-sdk">InfiniteTalk API SDK for RunAPI</a>
</h3>

<p align="center">
  InfiniteTalk API SDKs for JavaScript, Ruby, and Go on RunAPI.
</p>

<div align="center">

[![npm](https://img.shields.io/npm/v/@runapi.ai/infinitetalk)](https://www.npmjs.com/package/@runapi.ai/infinitetalk)
[![RubyGems](https://img.shields.io/gem/v/runapi-infinitetalk)](https://rubygems.org/gems/runapi-infinitetalk)
[![Go Reference](https://pkg.go.dev/badge/github.com/runapi-ai/infinitetalk-sdk/go.svg)](https://pkg.go.dev/github.com/runapi-ai/infinitetalk-sdk/go)
[![License](https://img.shields.io/github/license/runapi-ai/infinitetalk-sdk)](https://github.com/runapi-ai/infinitetalk-sdk/blob/main/LICENSE)

</div>
<br/>

The infinitetalk api SDK packages JavaScript, Ruby, and Go clients for InfiniteTalk on RunAPI. Use this infinitetalk api SDK for audio-driven lip-sync video generation workflows that need typed installs, JSON request bodies, task polling, and consistent RunAPI errors across services.

InfiniteTalk belongs to the MeiGen-AI catalog on RunAPI. The public model page is https://runapi.ai/models/infinitetalk; variant pages below carry pricing, rate-limit, and commercial-usage details. The public `infinitetalk-sdk` repository groups the JavaScript, Ruby, and Go packages for this model.

## Install

```bash
npm install @runapi.ai/infinitetalk
gem install runapi-infinitetalk
go get github.com/runapi-ai/infinitetalk-sdk/go@latest
```

## What you can build

- Build creative tools, agent pipelines, and production integrations with the infinitetalk api SDK.
- Keep one model-specific repository while installing only the language package your app needs.
- Use `create` for submit-only jobs, `get` for status lookup, and `run` for submit-and-poll scripts.
- Handle authentication, validation, rate limits, insufficient credits, task failures, and polling timeouts through RunAPI SDK errors.

The JavaScript client exposes audio to video resources, and the Ruby and Go packages mirror the same RunAPI task lifecycle.

## JavaScript quick start

```typescript
import { InfinitetalkClient } from '@runapi.ai/infinitetalk';

const client = new InfinitetalkClient();

const task = await client.audioToVideo.create({
  // Pass the InfiniteTalk request body documented at https://runapi.ai/docs#infinitetalk.
});

const status = await client.audioToVideo.get(task.id);
```

For short scripts, use `run` with the same JSON body to create the task and wait for completion. For web request handlers, prefer `create` plus webhook or later `get` polling so the server does not hold a worker open.

## Repository layout

- `js/` publishes `@runapi.ai/infinitetalk`.
- `ruby/` publishes `runapi-infinitetalk` when RubyGems publishing resumes.
- `go/` publishes `github.com/runapi-ai/infinitetalk-sdk/go` and depends on `github.com/runapi-ai/core-sdk/go`.

## Public links

- Model page: https://runapi.ai/models/infinitetalk
- SDK docs: https://runapi.ai/docs#sdk-infinitetalk
- Product docs: https://runapi.ai/docs#infinitetalk
- SDK repository: https://github.com/runapi-ai/infinitetalk-sdk
- Skill repository: https://github.com/runapi-ai/infinitetalk
- Provider comparison: https://runapi.ai/providers/meigen-ai
- Full catalog: https://runapi.ai/models

## Pricing and variants

Use the most specific infinitetalk api variant page for pricing, rate limits, and commercial usage:
- [From audio](https://runapi.ai/models/infinitetalk)

Default pricing link for the infinitetalk api SDK: https://runapi.ai/models/infinitetalk

## Generated file storage

RunAPI-generated file URLs are temporary. Download and store generated images, videos, audio, or other files in your own durable storage within 7 days; do not treat returned URLs as long-term assets.

## FAQ

### Which package should I install for infinitetalk api work?

Install the model package for your language: `@runapi.ai/infinitetalk`, `runapi-infinitetalk`, or `github.com/runapi-ai/infinitetalk-sdk/go`. Install core SDK packages only when you are building shared SDK infrastructure.

### Where should public links point?

Primary infinitetalk api links point to https://runapi.ai/models/infinitetalk. Pricing and usage-policy links point to variant pages such as https://runapi.ai/models/infinitetalk. Provider comparisons point to https://runapi.ai/providers/meigen-ai, and broad browsing points to https://runapi.ai/models.

## License

Licensed under the Apache License, Version 2.0.
