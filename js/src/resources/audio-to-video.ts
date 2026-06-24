import type { HttpClient, PollingOptions, RequestOptions, ActionSchema } from '@runapi.ai/core';
import { compactParams, validateParams } from '@runapi.ai/core';
import { pollUntilComplete } from '@runapi.ai/core/internal';
import { contract } from '../contract_gen';
import type { CompletedAudioToVideoResponse, AudioToVideoParams, AudioToVideoResponse, TaskCreateResponse } from '../types';

const ENDPOINT = '/api/v1/infinitetalk/audio_to_video';

/**
 * Generates lip-synced talking-head videos from a portrait image and an audio track.
 * The output video shows the person speaking or singing in sync with the audio.
 */
export class AudioToVideo {
  constructor(private readonly http: HttpClient) {}

  /**
   * Generate a lip-synced talking-head video from a portrait image and an audio track and wait until complete.
   * @param params Audio-to-video parameters.
   * @param options Per-request and polling overrides.
   * @returns The completed task with videos.
   */
  async run(params: AudioToVideoParams, options?: RequestOptions & PollingOptions): Promise<CompletedAudioToVideoResponse> {
    const { id } = await this.create(params, options);
    const response = await pollUntilComplete<AudioToVideoResponse>(() => this.get(id, options), {
      maxWaitMs: options?.maxWaitMs,
      pollIntervalMs: options?.pollIntervalMs,
    });
    return response as CompletedAudioToVideoResponse;
  }

  /**
   * Generate a lip-synced talking-head video from a portrait image and an audio track; returns immediately with a task id.
   * @param params Audio-to-video parameters.
   * @param options Per-request overrides.
   * @returns The task creation result with id.
   */
  async create(params: AudioToVideoParams, options?: RequestOptions): Promise<TaskCreateResponse> {
    const body = compactParams(params);
    validateParams(contract['audio-to-video'] as ActionSchema, body as Record<string, unknown>);
    return this.http.request<TaskCreateResponse>('POST', ENDPOINT, {
      body,
      ...options,
    });
  }

  /**
   * Fetch the current status of an audio-to-video task.
   * @param id The task id.
   * @param options Per-request overrides.
   * @returns The current audio-to-video task status.
   */
  async get(id: string, options?: RequestOptions): Promise<AudioToVideoResponse> {
    return this.http.request<AudioToVideoResponse>('GET', `${ENDPOINT}/${id}`, options ?? {});
  }
}
