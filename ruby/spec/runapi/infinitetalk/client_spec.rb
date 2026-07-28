# frozen_string_literal: true

require "spec_helper"

RSpec.describe RunApi::Infinitetalk::Client do
  before do
    allow(ConnectionPool).to receive(:new).and_return(instance_double(ConnectionPool))
  end

  after { RunApi.api_key = nil }

  it "accepts api_key as parameter" do
    client = described_class.new(api_key: "param-key")
    expect(client).to be_a(described_class)
  end

  it "falls back to global RunApi.api_key" do
    RunApi.api_key = "global-key"
    client = described_class.new
    expect(client).to be_a(described_class)
  end

  it "exposes audio_to_video accessor" do
    client = described_class.new(api_key: "test-key")
    expect(client.audio_to_video).to be_a(RunApi::Infinitetalk::Resources::AudioToVideo)
  end
end
