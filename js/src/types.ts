import type { AsyncTaskStatus } from '@runapi.ai/core';

export type InfinitetalkModel = 'infinitetalk-from-audio';
export type Resolution = '480p' | '720p';

export interface TaskCreateResponse {
  id: string;
  status?: AsyncTaskStatus;
}

export interface Video {
  url: string;
}

export interface AudioToVideoParams {
  model: InfinitetalkModel;
  image_url: string;
  audio_url: string;
  prompt: string;
  callback_url?: string;
  resolution?: Resolution;
  seed?: number;
}

export interface AudioToVideoResponse {
  id: string;
  status: AsyncTaskStatus;
  videos?: Video[];
  error?: string;
  [key: string]: unknown;
}

export type CompletedAudioToVideoResponse = AudioToVideoResponse & {
  status: 'completed';
  videos: Video[];
};
