package infinitetalk

var contractSchema = map[string]any{"audio-to-video": map[string]any{"models": []any{"infinitetalk-from-audio"}, "fields_by_model": map[string]any{"infinitetalk-from-audio": map[string]any{"output_resolution": map[string]any{"enum": []any{"480p", "720p"}}, "seed": map[string]any{"type": "integer"}, "source_audio_url": map[string]any{"required": true}, "source_image_url": map[string]any{"required": true}}}}}
