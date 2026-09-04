<p align="center">
  <a href="https://runapi.ai"><img src="https://runapi.ai/icon.svg" height="56" alt="RunAPI"></a>
</p>

<h3 align="center">
  <a href="https://github.com/runapi-ai/infinitetalk-sdk">InfiniteTalk API SDK for RunAPI</a>
</h3>

<p align="center">
  InfiniteTalk API SDKs for JavaScript, Python, Ruby, Go, Java, and PHP on RunAPI.
</p>

<div align="center">

[![npm](https://img.shields.io/npm/v/@runapi.ai/infinitetalk)](https://www.npmjs.com/package/@runapi.ai/infinitetalk)
[![PyPI](https://img.shields.io/pypi/v/runapi-infinitetalk)](https://pypi.org/project/runapi-infinitetalk/)
[![RubyGems](https://img.shields.io/gem/v/runapi-infinitetalk)](https://rubygems.org/gems/runapi-infinitetalk)
[![Go Reference](https://pkg.go.dev/badge/github.com/runapi-ai/infinitetalk-sdk/go.svg)](https://pkg.go.dev/github.com/runapi-ai/infinitetalk-sdk/go)
[![Maven Central](https://img.shields.io/maven-central/v/ai.runapi/runapi-infinitetalk)](https://central.sonatype.com/artifact/ai.runapi/runapi-infinitetalk)
[![License](https://img.shields.io/github/license/runapi-ai/infinitetalk-sdk)](https://github.com/runapi-ai/infinitetalk-sdk/blob/main/LICENSE)

</div>
<br/>

The InfiniteTalk API SDK packages JavaScript, Python, Ruby, Go, Java, and PHP clients for InfiniteTalk on RunAPI. Use it for audio-driven talking video workflows when your app needs typed request builders, predictable task polling, file upload helpers, account helpers, and consistent RunAPI errors.

InfiniteTalk is listed in the RunAPI model catalog at https://runapi.ai/models/infinitetalk. Variant pages below carry pricing, rate-limit, and commercial-usage details. The public `infinitetalk-sdk` repository groups the non-PHP language packages, examples, CI, and release tags for this model. The PHP package is released from a split Composer repository.

## Install

```bash
npm install @runapi.ai/infinitetalk
pip install runapi-infinitetalk
gem install runapi-infinitetalk
go get github.com/runapi-ai/infinitetalk-sdk/go@latest
```

Gradle:

```kotlin
dependencies {
  implementation("ai.runapi:runapi-infinitetalk:0.1.1")
}
```

Maven:

```xml
<dependency>
  <groupId>ai.runapi</groupId>
  <artifactId>runapi-infinitetalk</artifactId>
  <version>0.1.1</version>
</dependency>
```

Use the Java BOM when installing multiple RunAPI Java modules:

```kotlin
dependencies {
  implementation(platform("ai.runapi:runapi-bom:0.6.2"))
  implementation("ai.runapi:runapi-infinitetalk")
}
```

The PHP package is published from the split Composer repository as `runapi-ai/infinitetalk`; see https://github.com/runapi-ai/infinitetalk-php for PHP install and examples.

## What you can build

- Build apps, agent workflows, batch jobs, and production services around InfiniteTalk requests.
- Install only the language package your app needs while keeping one model-specific repository for docs and releases.
- Use `create` for submit-only jobs, `get` for status lookup, and `run` for submit-and-poll scripts.
- Upload local files, URL files, or base64 files through shared RunAPI file helpers.
- Handle validation, authentication, rate limits, insufficient credits, task failures, and polling timeouts through RunAPI SDK errors.

## Java quick start

```java
import ai.runapi.infinitetalk.InfiniteTalkClient;
import ai.runapi.infinitetalk.types.AudioToVideoParams;
import ai.runapi.infinitetalk.types.CompletedAudioToVideoResponse;
import ai.runapi.infinitetalk.types.AudioToVideoModel;

InfiniteTalkClient client = InfiniteTalkClient.builder()
    .apiKey(System.getenv("RUNAPI_API_KEY"))
    .build();

CompletedAudioToVideoResponse result = client.audioToVideo().run(
    AudioToVideoParams.builder()
        .model(AudioToVideoModel.INFINITETALK_FROM_AUDIO)
        .sourceImageUrl("https://cdn.runapi.ai/public/samples/image.jpg")
        .sourceAudioUrl("https://cdn.runapi.ai/public/samples/music.mp3")
        .prompt("A cinematic product shot with soft studio lighting")
        .outputResolution("480p")
        .build()
);
```

Java packages target Java 8 bytecode and are tested on Java 8, 11, 17, and 21. Each model artifact depends on `ai.runapi:runapi-core`, so application code normally installs only `ai.runapi:runapi-infinitetalk`.

## Task lifecycle

Most media endpoints are asynchronous. `create()` submits a task and returns its id, `get(id)` fetches the latest task state, and `run(params)` creates the task and polls until it reaches a terminal state. In web request handlers, prefer `create()` plus webhook or later `get()` polling so the server does not hold a worker open.

## Repository layout

- `js/` publishes `@runapi.ai/infinitetalk`.
- `python/` publishes `runapi-infinitetalk`.
- `ruby/` publishes `runapi-infinitetalk`.
- `go/` publishes `github.com/runapi-ai/infinitetalk-sdk/go`.
- `java/` publishes `ai.runapi:runapi-infinitetalk` and uses `ai.runapi:runapi-core`.

## Public links

- Model page: https://runapi.ai/models/infinitetalk
- SDK docs: https://runapi.ai/docs/resources/sdks
- Product docs: https://runapi.ai/docs/api/infinitetalk/audio-to-video
- SDK repository: https://github.com/runapi-ai/infinitetalk-sdk
- PHP package repository: https://github.com/runapi-ai/infinitetalk-php
- Skill repository: https://github.com/runapi-ai/infinitetalk
- Provider comparison: https://runapi.ai/providers/meigen-ai
- Full catalog: https://runapi.ai/models

## Pricing and variants

Use the most specific InfiniteTalk variant page for pricing, rate limits, and commercial usage:
- [From audio](https://runapi.ai/models/infinitetalk)

Default pricing link for the InfiniteTalk SDK: https://runapi.ai/models/infinitetalk

## File storage

RunAPI-generated file URLs are temporary. Download and store generated images, videos, audio, or other files in your own durable storage within 7 days; do not treat returned URLs as long-term assets.

## FAQ

### Which package should I install for InfiniteTalk work?

Install the model package for your language: `@runapi.ai/infinitetalk` on npm, `runapi-infinitetalk` on PyPI, `runapi-infinitetalk` on RubyGems, `github.com/runapi-ai/infinitetalk-sdk/go`, `ai.runapi:runapi-infinitetalk` on Maven Central, or `runapi-ai/infinitetalk` on Packagist. Install core SDK packages only when you are building shared SDK infrastructure.

### Where should public links point?

Primary InfiniteTalk links point to https://runapi.ai/models/infinitetalk. Pricing and usage-policy links point to variant pages such as https://runapi.ai/models/infinitetalk. Provider comparisons point to https://runapi.ai/providers/meigen-ai, and broad browsing points to https://runapi.ai/models.

## License

Licensed under the Apache License, Version 2.0.
