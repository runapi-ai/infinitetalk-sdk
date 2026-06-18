package infinitetalk

// AudioToVideoModel identifies which InfiniteTalk model variant to use for generation.
type AudioToVideoModel string

// Resolution controls the output video dimensions.
type Resolution string

// TaskStatus represents the processing state of an asynchronous generation task.
type TaskStatus string

const (
	// ModelAudioToVideo is the InfiniteTalk v1 model that generates lip-synced video
	// from a portrait image and audio track.
	ModelAudioToVideo AudioToVideoModel = "infinitetalk-from-audio"

	// Resolution480P produces 480p output, faster to generate and lower cost.
	Resolution480P Resolution = "480p"
	// Resolution720P produces 720p output with higher visual fidelity.
	Resolution720P Resolution = "720p"
)

// AsyncTaskResponse contains the common fields shared by all asynchronous task responses.
type AsyncTaskResponse struct {
	ID     string     `json:"id"`
	Status TaskStatus `json:"status"`
	Error  string     `json:"error,omitempty"`
}

func (r AsyncTaskResponse) GetID() string     { return r.ID }
func (r AsyncTaskResponse) GetStatus() string { return string(r.Status) }
func (r AsyncTaskResponse) GetError() string  { return r.Error }

// Video holds the URL of a generated video asset.
type Video struct {
	URL string `json:"url"`
}

// AudioToVideoResponse is the result of an audio-to-video generation task.
// Once the task completes successfully, Videos contains the generated lip-synced video(s).
type AudioToVideoResponse struct {
	AsyncTaskResponse
	Videos []Video `json:"videos,omitempty"`
}

// AudioToVideoParams configures an audio-to-video lip-sync generation request.
// Model, SourceImageURL, SourceAudioURL, and Prompt are all required.
// The source image should be a clear frontal portrait; the audio track drives the lip movements
// and determines the output video duration.
type AudioToVideoParams struct {
	Model            AudioToVideoModel `json:"model" help:"required; model slug"`
	SourceImageURL   string            `json:"source_image_url" help:"required; source image URL"`
	SourceAudioURL   string            `json:"source_audio_url" help:"required; source audio URL"`
	Prompt           string            `json:"prompt" help:"required; max 5000 chars"`
	CallbackURL      string            `json:"callback_url,omitempty" help:"optional; webhook URL"`
	OutputResolution Resolution        `json:"output_resolution,omitempty" help:"optional; output resolution"`
	Seed             *int              `json:"seed,omitempty" help:"optional; integer between 10000 and 1000000"`
}
