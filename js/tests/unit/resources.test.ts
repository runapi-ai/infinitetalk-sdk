import { beforeEach, describe, expect, it, vi } from 'vitest';
import type { HttpClient } from '@runapi.ai/core';
import { AudioToVideo } from '../../src/resources/audio-to-video';

describe('Infinitetalk resources', () => {
  const mockHttp: HttpClient = {
    request: vi.fn(),
  };

  beforeEach(() => {
    vi.clearAllMocks();
  });

  it('creates audio-to-video tasks with flat params', async () => {
    vi.mocked(mockHttp.request).mockResolvedValueOnce({ id: 'task-1' });
    const audioToVideo = new AudioToVideo(mockHttp);

    await audioToVideo.create({
      model: 'infinitetalk-from-audio',
      source_image_url: 'https://cdn.runapi.ai/public/samples/portrait.jpg',
      source_audio_url: 'https://cdn.runapi.ai/public/samples/voice.mp3',
      prompt: 'A young woman with long dark hair talking on a podcast.',
      output_resolution: '480p',
      seed: 12345,
    });

    expect(mockHttp.request).toHaveBeenCalledWith('POST', '/api/v1/infinitetalk/audio_to_video', {
      body: {
        model: 'infinitetalk-from-audio',
        source_image_url: 'https://cdn.runapi.ai/public/samples/portrait.jpg',
        source_audio_url: 'https://cdn.runapi.ai/public/samples/voice.mp3',
        prompt: 'A young woman with long dark hair talking on a podcast.',
        output_resolution: '480p',
        seed: 12345,
      },
    });
  });

  it('gets audio-to-video tasks by id', async () => {
    vi.mocked(mockHttp.request).mockResolvedValueOnce({
      id: 'task-2',
      status: 'completed',
      videos: [{ url: 'https://file.runapi.ai/infinitetalk/video.mp4' }],
    });
    const audioToVideo = new AudioToVideo(mockHttp);

    const result = await audioToVideo.get('task-2');

    expect(mockHttp.request).toHaveBeenCalledWith('GET', '/api/v1/infinitetalk/audio_to_video/task-2', {});
    expect(result.videos?.[0]?.url).toBe('https://file.runapi.ai/infinitetalk/video.mp4');
  });
});
