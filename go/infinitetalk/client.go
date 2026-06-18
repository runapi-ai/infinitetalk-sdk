// Package infinitetalk provides the Infinitetalk lip-sync video API client.
//
//	client, err := infinitetalk.NewClient(option.WithAPIKey("sk-your-api-key"))
//	result, err := client.AudioToVideo.Run(ctx, infinitetalk.AudioToVideoParams{
//	    Model: infinitetalk.ModelAudioToVideo,
//	    SourceImageURL: "https://cdn.runapi.ai/public/samples/portrait.jpg",
//	    SourceAudioURL: "https://cdn.runapi.ai/public/samples/voice.mp3",
//	    Prompt: "A young woman with long dark hair talking on a podcast.",
//	})
package infinitetalk

import (
	"context"

	"github.com/runapi-ai/core-sdk/go/base"
	"github.com/runapi-ai/core-sdk/go/core"
	"github.com/runapi-ai/core-sdk/go/option"
)

const audioToVideoPath = "/api/v1/infinitetalk/audio_to_video"

// Client provides access to InfiniteTalk lip-sync video generation.
type Client struct {
	base.Base
	AudioToVideo *AudioToVideo
}

// NewClient creates an InfiniteTalk client with the given options.
// At minimum an API key is required (via option.WithAPIKey or the RUNAPI_API_KEY environment variable).
func NewClient(opts ...option.ClientOption) (*Client, error) {
	resolved, err := option.ResolveClientOptions(opts...)
	if err != nil {
		return nil, err
	}
	httpClient, err := core.NewHTTPClient(resolved)
	if err != nil {
		return nil, err
	}
	return NewClientWithHTTP(httpClient), nil
}

// NewClientWithHTTP creates an InfiniteTalk client using a pre-configured HTTP client,
// useful for shared connection pooling or custom transport settings.
func NewClientWithHTTP(httpClient core.HTTPClient) *Client {
	return &Client{Base: base.New(httpClient), AudioToVideo: &AudioToVideo{http: httpClient}}
}

// AudioToVideo generates lip-synced talking-head videos from a portrait image and an audio track.
// The generated video shows the person speaking or singing in sync with the audio.
type AudioToVideo struct{ http core.HTTPClient }

// Create submits an audio-to-video generation task and returns immediately with a task ID.
// Use Get to poll for the result, or use Run for a blocking helper that polls automatically.
func (r *AudioToVideo) Create(ctx context.Context, params AudioToVideoParams, opts ...option.RequestOption) (*core.TaskCreateResponse, error) {
	requestOptions, _ := option.ResolveRequestOptions(opts...)
	return core.PostJSON[core.TaskCreateResponse](ctx, r.http, audioToVideoPath, core.CompactParams(params), requestOptions)
}

// Get retrieves the current status and result of an audio-to-video task by its ID.
func (r *AudioToVideo) Get(ctx context.Context, id string, opts ...option.RequestOption) (*AudioToVideoResponse, error) {
	requestOptions, _ := option.ResolveRequestOptions(opts...)
	return core.GetJSON[AudioToVideoResponse](ctx, r.http, core.ResourcePath(audioToVideoPath, id), requestOptions)
}

// Run submits an audio-to-video task and polls until it completes or fails, returning the final result.
// This is a convenience wrapper around Create + Get polling. Use option.WithPollingInterval to adjust timing.
func (r *AudioToVideo) Run(ctx context.Context, params AudioToVideoParams, opts ...option.RequestOption) (*AudioToVideoResponse, error) {
	_, pollingOptions := option.ResolveRequestOptions(opts...)
	return core.RunAsync(ctx, func(ctx context.Context) (*core.TaskCreateResponse, error) { return r.Create(ctx, params, opts...) }, func(ctx context.Context, id string) (*AudioToVideoResponse, error) { return r.Get(ctx, id, opts...) }, pollingOptions)
}
