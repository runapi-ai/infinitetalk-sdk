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

	"github.com/runapi-ai/core-sdk/go/core"
	"github.com/runapi-ai/core-sdk/go/option"
)

const audioToVideoPath = "/api/v1/infinitetalk/audio_to_video"

type Client struct {
	AudioToVideo *AudioToVideo
}

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

func NewClientWithHTTP(httpClient core.HTTPClient) *Client {
	return &Client{AudioToVideo: &AudioToVideo{http: httpClient}}
}

type AudioToVideo struct{ http core.HTTPClient }

func (r *AudioToVideo) Create(ctx context.Context, params AudioToVideoParams, opts ...option.RequestOption) (*core.TaskCreateResponse, error) {
	requestOptions, _ := option.ResolveRequestOptions(opts...)
	return core.PostJSON[core.TaskCreateResponse](ctx, r.http, audioToVideoPath, core.CompactParams(params), requestOptions)
}
func (r *AudioToVideo) Get(ctx context.Context, id string, opts ...option.RequestOption) (*AudioToVideoResponse, error) {
	requestOptions, _ := option.ResolveRequestOptions(opts...)
	return core.GetJSON[AudioToVideoResponse](ctx, r.http, core.ResourcePath(audioToVideoPath, id), requestOptions)
}
func (r *AudioToVideo) Run(ctx context.Context, params AudioToVideoParams, opts ...option.RequestOption) (*AudioToVideoResponse, error) {
	_, pollingOptions := option.ResolveRequestOptions(opts...)
	return core.RunAsync(ctx, func(ctx context.Context) (*core.TaskCreateResponse, error) { return r.Create(ctx, params, opts...) }, func(ctx context.Context, id string) (*AudioToVideoResponse, error) { return r.Get(ctx, id, opts...) }, pollingOptions)
}
