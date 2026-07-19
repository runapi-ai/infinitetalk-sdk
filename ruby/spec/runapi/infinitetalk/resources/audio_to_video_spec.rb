# frozen_string_literal: true

require "spec_helper"

RSpec.describe RunApi::Infinitetalk::Resources::AudioToVideo do
  let(:http) { instance_double(RunApi::Core::HttpClient) }
  let(:resource) { described_class.new(http) }
  let(:endpoint) { "/api/v1/infinitetalk/audio_to_video" }

  it "POSTs to the correct endpoint" do
    params = {
      model: "infinitetalk-from-audio",
      source_image_url: "https://cdn.runapi.ai/public/samples/portrait.jpg",
      source_audio_url: "https://cdn.runapi.ai/public/samples/voice.mp3",
      prompt: "A young woman with long dark hair talking on a podcast.",
      output_resolution: "480p"
    }
    expect(http).to receive(:request).with(:post, endpoint, body: params).and_return("id" => "task-1")

    result = resource.create(**params)
    expect(result.id).to eq("task-1")
  end

  it "GETs the correct endpoint" do
    expect(http).to receive(:request).with(:get, "#{endpoint}/task-1")
      .and_return("id" => "task-1", "status" => "completed")

    result = resource.get("task-1")
    expect(result.status).to eq("completed")
  end

  it "raises ValidationError for invalid output_resolution" do
    expect {
      resource.create(
        model: "infinitetalk-from-audio",
        source_image_url: "https://cdn.runapi.ai/public/samples/portrait.jpg",
        source_audio_url: "https://cdn.runapi.ai/public/samples/voice.mp3",
        prompt: "A young woman with long dark hair talking on a podcast.",
        output_resolution: "1080p"
      )
    }.to raise_error(RunApi::Core::ValidationError, /output_resolution must be one of: 480p, 720p/)
  end
end
