package ai.runapi.infinitetalk.types;

import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

/** Parameters for audio to video operations. */
public final class AudioToVideoParams {
  private final String model;
  private final String sourceImageUrl;
  private final String sourceAudioUrl;
  private final String prompt;
  private final String callbackUrl;
  private final String outputResolution;
  private final Integer seed;

  private AudioToVideoParams(Builder builder) {
    this.model = builder.model;
    this.sourceImageUrl = InfinitetalkParamUtils.requireNonBlank(builder.sourceImageUrl, "sourceImageUrl");
    this.sourceAudioUrl = InfinitetalkParamUtils.requireNonBlank(builder.sourceAudioUrl, "sourceAudioUrl");
    this.prompt = builder.prompt;
    this.callbackUrl = builder.callbackUrl;
    this.outputResolution = builder.outputResolution;
    this.seed = builder.seed;
  }

  /** Creates a new AudioToVideoParams builder. */
  public static Builder builder() {
    return new Builder();
  }

  /** Returns the RunAPI action key for this request. */
  public String action() {
    return "infinitetalk/audio-to-video";
  }

  /** Converts these parameters to the JSON request body shape. */
  public Map<String, Object> toMap() {
    Map<String, Object> raw = new LinkedHashMap<String, Object>();
    raw.put("model", InfinitetalkParamUtils.wireValue(model));
    raw.put("source_image_url", InfinitetalkParamUtils.wireValue(sourceImageUrl));
    raw.put("source_audio_url", InfinitetalkParamUtils.wireValue(sourceAudioUrl));
    raw.put("prompt", InfinitetalkParamUtils.wireValue(prompt));
    raw.put("callback_url", InfinitetalkParamUtils.wireValue(callbackUrl));
    raw.put("output_resolution", InfinitetalkParamUtils.wireValue(outputResolution));
    raw.put("seed", InfinitetalkParamUtils.wireValue(seed));
    return InfinitetalkParamUtils.compact(raw);
  }



  /** Builder for {@link AudioToVideoParams}. */
  public static final class Builder {
    private String model;
    private String sourceImageUrl;
    private String sourceAudioUrl;
    private String prompt;
    private String callbackUrl;
    private String outputResolution;
    private Integer seed;

    private Builder() {}

    /** Sets the model slug using a typed model value. */
    public Builder model(AudioToVideoModel value) {
      this.model = java.util.Objects.requireNonNull(value, "model").value();
      return this;
    }

    /** Sets the model slug using a string value. */
    public Builder model(String value) {
      this.model = InfinitetalkParamUtils.requireNonBlankTrim(value, "model");
      return this;
    }


    /** Sets the source image URL. */
    public Builder sourceImageUrl(String value) {
      this.sourceImageUrl = InfinitetalkParamUtils.requireNonBlank(value, "sourceImageUrl");
      return this;
    }

    /** Sets the source audio URL. */
    public Builder sourceAudioUrl(String value) {
      this.sourceAudioUrl = InfinitetalkParamUtils.requireNonBlank(value, "sourceAudioUrl");
      return this;
    }

    /** Sets the text prompt. */
    public Builder prompt(String value) {
      this.prompt = InfinitetalkParamUtils.requireNonBlank(value, "prompt");
      return this;
    }

    /** Sets the webhook URL for task completion notifications. */
    public Builder callbackUrl(String value) {
      this.callbackUrl = InfinitetalkParamUtils.requireNonBlank(value, "callbackUrl");
      return this;
    }

    /** Sets the output resolution. */
    public Builder outputResolution(String value) {
      this.outputResolution = InfinitetalkParamUtils.requireNonBlank(value, "outputResolution");
      return this;
    }

    /** Sets the random seed. */
    public Builder seed(int value) {
      this.seed = value;
      return this;
    }

    /** Builds immutable audio to video parameters. */
    public AudioToVideoParams build() {
      return new AudioToVideoParams(this);
    }
  }
}
