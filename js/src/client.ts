import { BaseClient, type ClientOptions } from '@runapi.ai/core';
import { AudioToVideo } from './resources/audio-to-video';

/**
 * InfiniteTalk lip-sync video generation client. Produces talking-head videos
 * by animating a portrait image to match an audio track's speech or singing.
 *
 * @example
 * ```typescript
 * import { InfinitetalkClient } from '@runapi.ai/infinitetalk';
 * const client = new InfinitetalkClient({ apiKey: 'sk-...' });
 * const result = await client.audioToVideo.run({
 *   model: 'infinitetalk-from-audio',
 *   source_image_url: 'https://example.com/portrait.jpg',
 *   source_audio_url: 'https://example.com/voice.mp3',
 *   prompt: 'A young woman talking on a podcast',
 * });
 * console.log(result.videos[0].url);
 * ```
 */
export class InfinitetalkClient extends BaseClient {
  /** Lip-synced video generation from a portrait image and audio track. */
  public readonly audioToVideo: AudioToVideo;

  constructor(options: ClientOptions = {}) {
    super(options);
    this.audioToVideo = new AudioToVideo(this.http);
  }
}
