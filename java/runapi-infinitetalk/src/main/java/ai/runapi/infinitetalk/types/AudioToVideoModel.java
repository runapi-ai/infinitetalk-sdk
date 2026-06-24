package ai.runapi.infinitetalk.types;

import com.fasterxml.jackson.annotation.JsonCreator;

/** Model slug for audio to video operations. */
public final class AudioToVideoModel extends InfinitetalkValue {
  /** infinitetalk-from-audio model slug. */
  public static final AudioToVideoModel INFINITETALK_FROM_AUDIO = new AudioToVideoModel("infinitetalk-from-audio");

  /** Creates a model value from a literal model slug. */
  @JsonCreator
  public AudioToVideoModel(String value) {
    super(value);
  }
}
