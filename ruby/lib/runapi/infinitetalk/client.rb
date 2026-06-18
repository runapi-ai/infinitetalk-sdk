# frozen_string_literal: true

module RunApi
  module Infinitetalk
    # InfiniteTalk lip-sync video generation client. Produces talking-head videos
    # by animating a portrait image to match an audio track's speech or singing.
    #
    # @example
    #   client = RunApi::Infinitetalk::Client.new(api_key: "sk-...")
    #   result = client.audio_to_video.run(
    #     model: "infinitetalk-from-audio",
    #     source_image_url: "https://example.com/portrait.jpg",
    #     source_audio_url: "https://example.com/voice.mp3",
    #     prompt: "A young woman talking on a podcast"
    #   )
    #   puts result.videos.first.url
    class Client < RunApi::Core::Client
      # @return [Resources::AudioToVideo] Lip-synced video generation from a portrait image and audio track.
      attr_reader :audio_to_video

      def initialize(api_key: nil, **options)
        super
        @audio_to_video = Resources::AudioToVideo.new(http)
      end
    end
  end
end
