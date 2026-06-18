# frozen_string_literal: true

module RunApi
  module Infinitetalk
    module Types
      # Available model identifiers for audio-to-video generation.
      MODELS = %w[infinitetalk-from-audio].freeze
      # Output resolution options. Higher resolution increases fidelity but takes longer.
      RESOLUTIONS = %w[480p 720p].freeze

      # A generated video asset.
      class Video < RunApi::Core::BaseModel
        optional :url, String
      end

      # Result of an audio-to-video generation task.
      # While processing, +videos+ is nil; once completed, it contains the generated lip-synced video(s).
      class AudioToVideoResponse < RunApi::Core::TaskResponse
        required :id, String
        optional :status, String, enum: -> { RunApi::Core::TaskResponse::Status::ALL }
        optional :videos, [-> { Video }]
        optional :error, String
      end

      # Narrowed response type guaranteed to contain completed videos.
      class CompletedAudioToVideoResponse < AudioToVideoResponse
        required :videos, [-> { Video }]
      end
    end
  end
end
