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

        def run(**params)
          task = create(**params)
          poll_until_complete { get(task.id) }
        end

        def create(**params)
          params = compact_params(params)
          validate_params!(params)
          request(:post, ENDPOINT, body: params)
        end

        def get(id)
          request(:get, "#{ENDPOINT}/#{id}")
        end

        private

        def validate_params!(params)
          model = param(params, :model)
          raise Core::ValidationError, "model is required" unless model
          unless Types::MODELS.include?(model)
            raise Core::ValidationError, "Invalid model: #{model}. Must be one of: #{Types::MODELS.join(", ")}"
          end

          validate_required!(params, :source_image_url)
          validate_required!(params, :source_audio_url)
          prompt = param(params, :prompt)
          raise Core::ValidationError, "prompt is required" unless prompt.is_a?(String) && !prompt.empty?
          if prompt.length > PROMPT_MAX_LENGTH
            raise Core::ValidationError, "prompt must be at most #{PROMPT_MAX_LENGTH} characters"
          end

          validate_optional!(params, :output_resolution, Types::RESOLUTIONS)

          seed = param(params, :seed)
          return if seed.nil?

          seed = Integer(seed, exception: false)
          return if seed && SEED_RANGE.cover?(seed)

          raise Core::ValidationError, "seed must be an integer between #{SEED_RANGE.min} and #{SEED_RANGE.max}"
        end

        def validate_required!(params, key)
          value = param(params, key)
          return if value.is_a?(String) ? !value.empty? : !value.nil?

          raise Core::ValidationError, "#{key} is required"
        end
      end
    end
  end
end
