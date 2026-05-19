# frozen_string_literal: true

module RunApi
  module Infinitetalk
    module Types
      MODELS = %w[infinitetalk-from-audio].freeze
      RESOLUTIONS = %w[480p 720p].freeze

      class Video < RunApi::Core::BaseModel
        optional :url, String
      end

      class AudioToVideoResponse < RunApi::Core::TaskResponse
        required :id, String
        optional :status, String, enum: -> { RunApi::Core::TaskResponse::Status::ALL }
        optional :videos, [ -> { Video } ]
        optional :error, String
      end

      class CompletedAudioToVideoResponse < AudioToVideoResponse
        required :videos, [ -> { Video } ]
      end
    end
  end
end
