import type { HttpClient, PollingOptions, RequestOptions } from '@runapi.ai/core';
import { compactParams } from '@runapi.ai/core';
import { pollUntilComplete } from '@runapi.ai/core/internal';
import type { CompletedAudioToVideoResponse, AudioToVideoParams, AudioToVideoResponse, TaskCreateResponse } from '../types';

const ENDPOINT = '/api/v1/infinitetalk/audio_to_video';

export class AudioToVideo {
  constructor(private readonly http: HttpClient) {}

  async run(params: AudioToVideoParams, options?: RequestOptions & PollingOptions): Promise<CompletedAudioToVideoResponse> {
    const { id } = await this.create(params, options);
    const response = await pollUntilComplete<AudioToVideoResponse>(() => this.get(id, options), {
      maxWaitMs: options?.maxWaitMs,
      pollIntervalMs: options?.pollIntervalMs,
    });
    return response as CompletedAudioToVideoResponse;
  }

  async create(params: AudioToVideoParams, options?: RequestOptions): Promise<TaskCreateResponse> {
    return this.http.request<TaskCreateResponse>('POST', ENDPOINT, {
      body: compactParams(params),
      ...options,
    });
  }

  async get(id: string, options?: RequestOptions): Promise<AudioToVideoResponse> {
    return this.http.request<AudioToVideoResponse>('GET', `${ENDPOINT}/${id}`, options ?? {});
  }
}
