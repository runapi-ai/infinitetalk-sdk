# frozen_string_literal: true

module RunApi
  module Infinitetalk
    module Resources
      # Generates lip-synced talking-head videos from a portrait image and an audio track.
      # The output video shows the person speaking or singing in sync with the audio.
      class AudioToVideo
        include RunApi::Core::ResourceHelpers

        ENDPOINT = "/api/v1/infinitetalk/audio_to_video"
        RESPONSE_CLASS = Types::AudioToVideoResponse
        COMPLETED_RESPONSE_CLASS = Types::CompletedAudioToVideoResponse

        def initialize(http)
          @http = http
        end

        def run(options: nil, **params)
          task = create(options: options, **params)
          poll_until_complete { get(task.id, options: options) }
        end

        def create(options: nil, **params)
          params = compact_params(params)
          request(:post, ENDPOINT, body: params, options: options)
        end

        def get(id, options: nil)
          request(:get, "#{ENDPOINT}/#{id}", options: options)
        end
      end
    end
  end
end
