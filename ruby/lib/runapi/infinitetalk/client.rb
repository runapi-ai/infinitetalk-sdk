# frozen_string_literal: true

module RunApi
  module Infinitetalk
    class Client
      attr_reader :audio_to_video

      def initialize(api_key: nil, **options)
        @api_key = Core::Auth.resolve_api_key(api_key)

        client_options = Core::ClientOptions.new(api_key: @api_key, **options)
        http = client_options.http_client || Core::HttpClient.new(client_options)
        @audio_to_video = Resources::AudioToVideo.new(http)
      end
    end
  end
end
