import { createHttpClient, type ClientOptions } from '@runapi.ai/core';
import { AudioToVideo } from './resources/audio-to-video';

export class InfinitetalkClient {
  public readonly audioToVideo: AudioToVideo;

  constructor(options: ClientOptions = {}) {
    const http = createHttpClient(options);
    this.audioToVideo = new AudioToVideo(http);
  }
}
