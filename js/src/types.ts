import type { AsyncTaskStatus, TaskBillingResponse, TaskResponse } from '@runapi.ai/core';

/** Model identifier for InfiniteTalk audio-to-video generation. */
export type InfinitetalkModel = 'infinitetalk-from-audio';

/** Output video resolution. Higher resolution increases visual fidelity but takes longer to generate. */
export type Resolution = '480p' | '720p';

/** Acknowledgement returned when a generation task is accepted. */
export interface TaskCreateResponse extends TaskBillingResponse {
  /** Unique task identifier used to poll for results. */
  id: string;
  status?: AsyncTaskStatus;
}

/** A generated video asset. */
export interface Video {
  /** Temporary download URL for the generated video. */
  url: string;
}

/**
 * Parameters for an audio-to-video lip-sync generation request.
 * The source image should be a clear frontal portrait; the audio track drives
 * the lip movements and determines the output video duration.
 */
export interface AudioToVideoParams {
  /** Model variant to use for generation. */
  model: InfinitetalkModel;
  /** URL of the portrait image to animate. Must show a clear, frontal face. */
  source_image_url: string;
  /** URL of the audio track that drives lip-sync. Determines video duration. */
  source_audio_url: string;
  /** Scene description guiding facial expression and body motion (max 5 000 chars). */
  prompt: string;
  /** Optional webhook URL to receive a POST notification when the task completes. */
  callback_url?: string;
  /** Output video resolution. Defaults to 480p if omitted. */
  output_resolution?: Resolution;
  /** Reproducibility seed (10 000 -- 1 000 000). Same seed with identical inputs produces the same output. */
  seed?: number;
}

/**
 * Result of an audio-to-video generation task.
 * While processing, `videos` is absent; once `status` is `'completed'`,
 * `videos` contains the generated lip-synced video(s).
 */
export interface AudioToVideoResponse extends TaskResponse {
  id: string;
  status: AsyncTaskStatus;
  /** Present only when the task has completed successfully. */
  videos?: Video[];
  /** Human-readable error message, present only when the task has failed. */
  error?: string;
  [key: string]: unknown;
}

/** Narrowed response type guaranteed to contain completed videos. */
export type CompletedAudioToVideoResponse = AudioToVideoResponse & {
  status: 'completed';
  videos: Video[];
};
