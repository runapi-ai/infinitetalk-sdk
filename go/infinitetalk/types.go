package infinitetalk

type AudioToVideoModel string

type Resolution string

type TaskStatus string

const (
	ModelAudioToVideo AudioToVideoModel = "infinitetalk-from-audio"
	Resolution480P    Resolution        = "480p"
	Resolution720P    Resolution        = "720p"
)

type AsyncTaskResponse struct {
	ID     string     `json:"id"`
	Status TaskStatus `json:"status"`
	Error  string     `json:"error,omitempty"`
}

func (r AsyncTaskResponse) GetID() string     { return r.ID }
func (r AsyncTaskResponse) GetStatus() string { return string(r.Status) }
func (r AsyncTaskResponse) GetError() string  { return r.Error }

type Video struct {
	URL string `json:"url"`
}

type AudioToVideoResponse struct {
	AsyncTaskResponse
	Videos []Video `json:"videos,omitempty"`
}

type AudioToVideoParams struct {
	Model            AudioToVideoModel `json:"model" help:"required; model slug"`
	SourceImageURL   string            `json:"source_image_url" help:"required; source image URL"`
	SourceAudioURL   string            `json:"source_audio_url" help:"required; source audio URL"`
	Prompt           string            `json:"prompt" help:"required; max 5000 chars"`
	CallbackURL      string            `json:"callback_url,omitempty" help:"optional; webhook URL"`
	OutputResolution Resolution        `json:"output_resolution,omitempty" help:"optional; output resolution"`
	Seed             *int              `json:"seed,omitempty" help:"optional; integer between 10000 and 1000000"`
}
