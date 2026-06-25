export const contract = {
  "audio-to-video": {
    "models": [
      "infinitetalk-from-audio"
    ],
    "fields_by_model": {
      "infinitetalk-from-audio": {
        "output_resolution": {
          "enum": [
            "480p",
            "720p"
          ]
        },
        "seed": {
          "type": "integer"
        },
        "source_audio_url": {
          "required": true
        },
        "source_image_url": {
          "required": true
        }
      }
    }
  }
} as const;
