package infinitetalk

import (
	"context"
	"encoding/json"
	"testing"

	"github.com/runapi-ai/core-sdk/go/core"
)

type stubHTTPClient struct {
	method string
	path   string
	body   any
}

func (s *stubHTTPClient) Request(_ context.Context, method, path string, opts *core.HTTPRequestOptions) (json.RawMessage, error) {
	s.method = method
	s.path = path
	if opts != nil {
		s.body = opts.Body
	}
	return json.RawMessage(`{"id":"task_123","status":"processing"}`), nil
}

func TestAudioToVideoCreateSendsCorrectRequest(t *testing.T) {
	stub := &stubHTTPClient{}
	client := NewClientWithHTTP(stub)
	seed := 12345
	_, err := client.AudioToVideo.Create(context.Background(), AudioToVideoParams{
		Model:            ModelAudioToVideo,
		SourceImageURL:   "https://cdn.runapi.ai/public/samples/portrait.jpg",
		SourceAudioURL:   "https://cdn.runapi.ai/public/samples/voice.mp3",
		Prompt:           "A young woman with long dark hair talking on a podcast.",
		OutputResolution: Resolution480P,
		Seed:             &seed,
	})
	if err != nil {
		t.Fatal(err)
	}
	if stub.method != "POST" || stub.path != "/api/v1/infinitetalk/audio_to_video" {
		t.Fatalf("unexpected request: %s %s", stub.method, stub.path)
	}
	body, ok := stub.body.(map[string]any)
	if !ok {
		t.Fatalf("expected flat body map, got %T", stub.body)
	}
	if body["model"] != string(ModelAudioToVideo) || body["output_resolution"] != string(Resolution480P) {
		t.Fatalf("unexpected body: %#v", body)
	}
	if body["source_image_url"] == nil || body["source_audio_url"] == nil {
		t.Fatalf("expected snake_case media fields in body: %#v", body)
	}
	if body["image_url"] != nil || body["audio_url"] != nil {
		t.Fatalf("expected provider media fields to be absent from public body: %#v", body)
	}
}

func TestAudioToVideoGetSendsCorrectPath(t *testing.T) {
	stub := &stubHTTPClient{}
	client := NewClientWithHTTP(stub)
	_, err := client.AudioToVideo.Get(context.Background(), "task_abc")
	if err != nil {
		t.Fatal(err)
	}
	if stub.method != "GET" || stub.path != "/api/v1/infinitetalk/audio_to_video/task_abc" {
		t.Fatalf("unexpected request: %s %s", stub.method, stub.path)
	}
}
