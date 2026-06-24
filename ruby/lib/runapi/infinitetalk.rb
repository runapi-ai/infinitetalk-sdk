# frozen_string_literal: true

require "runapi/core"
require_relative "infinitetalk/types"
require_relative "infinitetalk/contract_gen"
require_relative "infinitetalk/resources/audio_to_video"
require_relative "infinitetalk/client"

module RunApi
  module Infinitetalk
    AuthenticationError = RunApi::Core::AuthenticationError
    RateLimitError = RunApi::Core::RateLimitError
    InsufficientCreditsError = RunApi::Core::InsufficientCreditsError
    NotFoundError = RunApi::Core::NotFoundError
    ValidationError = RunApi::Core::ValidationError
    TaskFailedError = RunApi::Core::TaskFailedError
    TaskTimeoutError = RunApi::Core::TaskTimeoutError
  end
end
