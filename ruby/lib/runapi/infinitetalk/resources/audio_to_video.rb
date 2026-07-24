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
        PROMPT_MAX_LENGTH = 5000
        SEED_RANGE = (10_000..1_000_000)

        def initialize(http)
          @http = http
        end

        def run(options: nil, **params)
          task = create(options: options, **params)
          poll_until_complete { get(task.id, options: options) }
        end

        def create(options: nil, **params)
          params = compact_params(params)
          validate_params!(params)
          request(:post, ENDPOINT, body: params, options: options)
        end

        def get(id, options: nil)
          request(:get, "#{ENDPOINT}/#{id}", options: options)
        end

        private

        def validate_params!(params)
          validate_contract!(CONTRACT["audio-to-video"], params)

          prompt = param(params, :prompt)
          raise Core::ValidationError, "prompt is required" unless prompt.is_a?(String) && !prompt.empty?
          if prompt.length > PROMPT_MAX_LENGTH
            raise Core::ValidationError, "prompt must be at most #{PROMPT_MAX_LENGTH} characters"
          end

          seed = param(params, :seed)
          return if seed.nil?

          seed = Integer(seed, exception: false)
          return if seed && SEED_RANGE.cover?(seed)

          raise Core::ValidationError, "seed must be an integer between #{SEED_RANGE.min} and #{SEED_RANGE.max}"
        end
      end
    end
  end
end
