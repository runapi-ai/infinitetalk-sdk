package ai.runapi.infinitetalk;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNotNull;
import static org.junit.jupiter.api.Assertions.assertThrows;

import ai.runapi.core.RequestOptions;
import ai.runapi.core.errors.ValidationException;
import ai.runapi.core.http.HttpRequest;
import ai.runapi.core.http.HttpResponse;
import ai.runapi.core.http.HttpTransport;
import ai.runapi.core.http.JsonRequestBody;
import ai.runapi.core.json.Json;
import ai.runapi.infinitetalk.types.CompletedAudioToVideoResponse;
import ai.runapi.infinitetalk.types.AudioToVideoResponse;
import ai.runapi.infinitetalk.types.AudioToVideoModel;
import ai.runapi.infinitetalk.types.AudioToVideoParams;
import ai.runapi.infinitetalk.types.AudioToVideoResponse;
import ai.runapi.infinitetalk.types.CompletedAudioToVideoResponse;
import com.fasterxml.jackson.databind.JsonNode;
import java.io.ByteArrayOutputStream;
import java.time.Duration;
import java.util.Collections;
import org.junit.jupiter.api.Test;

class InfiniteTalkClientTest {
  @Test
  void builderCreatesClientAndUniversalResources() {
    InfiniteTalkClient client = InfiniteTalkClient.builder().apiKey("sk-test").build();

    assertNotNull(client.audioToVideo());
    assertNotNull(client.files());
    assertNotNull(client.account());
  }

  @Test
  void openValueClassesSerializeAsScalarStrings() throws Exception {
    String json = Json.mapper().writeValueAsString(new AudioToVideoModel("infinitetalk-from-audio"));

    assertEquals("\"infinitetalk-from-audio\"", json);
    assertEquals(new AudioToVideoModel("infinitetalk-from-audio"), Json.mapper().readValue(json, AudioToVideoModel.class));
  }

  @Test
  void createSendsExpectedRequestShape() throws Exception {
    CapturingTransport transport = new CapturingTransport("{\"id\":\"task_123\",\"status\":\"processing\"}");
    InfiniteTalkClient client = InfiniteTalkClient.builder().apiKey("sk-test").transport(transport).build();

    client.audioToVideo().create(
        AudioToVideoParams.builder()
            .model(AudioToVideoModel.INFINITETALK_FROM_AUDIO)
            .sourceImageUrl("https://cdn.runapi.ai/public/samples/image.jpg")
            .sourceAudioUrl("https://cdn.runapi.ai/public/samples/music.mp3")
            .prompt("A small red cube on a plain white table, studio product photo")
            .build()
    );

    assertEquals("POST", transport.request.getMethod().name());
    assertEquals("/api/v1/infinitetalk/audio_to_video", transport.request.getPath());
    JsonNode body = bodyJson(transport.request);
    assertNotNull(body);
  }

  @Test
  void getDecodesTaskResponseAndExtraFields() {
    CapturingTransport transport = new CapturingTransport("{\"id\":\"task_456\",\"status\":\"completed\",\"videos\":[{\"url\":\"https://file.runapi.ai/generated\"}],\"custom\":\"kept\"}");
    InfiniteTalkClient client = InfiniteTalkClient.builder().apiKey("sk-test").transport(transport).build();

    AudioToVideoResponse response = client.audioToVideo().get("task_456");

    assertEquals("GET", transport.request.getMethod().name());
    assertEquals("/api/v1/infinitetalk/audio_to_video/task_456", transport.request.getPath());
    assertEquals("completed", response.getStatus().value());
    assertNotNull(response.getVideos());
    assertEquals("kept", response.extraFields().get("custom").asText());
  }

  @Test
  void runPollsUntilCompletedAndKeepsExtraFields() {
    SequenceTransport transport = new SequenceTransport(
        "{\"id\":\"task_789\",\"status\":\"processing\"}",
        "{\"id\":\"task_789\",\"status\":\"completed\",\"videos\":[{\"url\":\"https://file.runapi.ai/generated\"}],\"custom\":\"kept\"}");
    InfiniteTalkClient client = InfiniteTalkClient.builder().apiKey("sk-test").transport(transport).build();

    CompletedAudioToVideoResponse response = client.audioToVideo().run(
        AudioToVideoParams.builder()
            .model(AudioToVideoModel.INFINITETALK_FROM_AUDIO)
            .sourceImageUrl("https://cdn.runapi.ai/public/samples/image.jpg")
            .sourceAudioUrl("https://cdn.runapi.ai/public/samples/music.mp3")
            .prompt("A small red cube on a plain white table, studio product photo")
            .build(),
        RequestOptions.builder().pollingInterval(Duration.ofMillis(1)).pollingMaxWait(Duration.ofSeconds(1)).build());

    assertEquals("completed", response.getStatus().value());
    assertNotNull(response.getVideos());
    assertEquals("kept", response.extraFields().get("custom").asText());
    assertEquals(2, transport.calls);
  }

  @Test
  void runRejectsCompletedResponseMissingResultField() {
    SequenceTransport transport = new SequenceTransport(
        "{\"id\":\"task_missing\",\"status\":\"processing\"}",
        "{\"id\":\"task_missing\",\"status\":\"completed\"}");
    InfiniteTalkClient client = InfiniteTalkClient.builder().apiKey("sk-test").transport(transport).build();

    assertThrows(
        ValidationException.class,
        () -> client.audioToVideo().run(
                AudioToVideoParams.builder()
                    .model(AudioToVideoModel.INFINITETALK_FROM_AUDIO)
                    .sourceImageUrl("https://cdn.runapi.ai/public/samples/image.jpg")
                    .sourceAudioUrl("https://cdn.runapi.ai/public/samples/music.mp3")
                    .prompt("A small red cube on a plain white table, studio product photo")
                    .build(),
            RequestOptions.builder().pollingInterval(Duration.ofMillis(1)).pollingMaxWait(Duration.ofSeconds(1)).build()));
  }

    @Test
    void coversAudiotovideoResourceMethods() {
      CapturingTransport createTransport = new CapturingTransport("{\"id\":\"task_audio_to_video\",\"status\":\"processing\"}");
      InfiniteTalkClient createClient = InfiniteTalkClient.builder().apiKey("sk-test").transport(createTransport).build();
      assertNotNull(createClient.audioToVideo().create(
              AudioToVideoParams.builder()
                  .model(AudioToVideoModel.INFINITETALK_FROM_AUDIO)
                  .sourceImageUrl("https://cdn.runapi.ai/public/samples/image.jpg")
                  .sourceAudioUrl("https://cdn.runapi.ai/public/samples/music.mp3")
                  .prompt("A small red cube on a plain white table, studio product photo")
                  .build()
      ));

      CapturingTransport createWithOptionsTransport = new CapturingTransport("{\"id\":\"task_audio_to_video_options\",\"status\":\"processing\"}");
      InfiniteTalkClient createWithOptionsClient = InfiniteTalkClient.builder().apiKey("sk-test").transport(createWithOptionsTransport).build();
      assertNotNull(createWithOptionsClient.audioToVideo().create(
              AudioToVideoParams.builder()
                  .model(AudioToVideoModel.INFINITETALK_FROM_AUDIO)
                  .sourceImageUrl("https://cdn.runapi.ai/public/samples/image.jpg")
                  .sourceAudioUrl("https://cdn.runapi.ai/public/samples/music.mp3")
                  .prompt("A small red cube on a plain white table, studio product photo")
                  .build(),
          RequestOptions.none()));

      CapturingTransport getTransport = new CapturingTransport("{\"id\":\"task_audio_to_video\",\"status\":\"completed\",\"videos\":[{\"url\":\"https://file.runapi.ai/generated\"}]}");
      InfiniteTalkClient getClient = InfiniteTalkClient.builder().apiKey("sk-test").transport(getTransport).build();
      assertNotNull(getClient.audioToVideo().get("task_audio_to_video"));

      CapturingTransport getWithOptionsTransport = new CapturingTransport("{\"id\":\"task_audio_to_video_options\",\"status\":\"completed\",\"videos\":[{\"url\":\"https://file.runapi.ai/generated\"}]}");
      InfiniteTalkClient getWithOptionsClient = InfiniteTalkClient.builder().apiKey("sk-test").transport(getWithOptionsTransport).build();
      assertNotNull(getWithOptionsClient.audioToVideo().get("task_audio_to_video_options", RequestOptions.none()));

      SequenceTransport runTransport = new SequenceTransport(
          "{\"id\":\"task_audio_to_video_run\",\"status\":\"processing\"}",
          "{\"id\":\"task_audio_to_video_run\",\"status\":\"completed\",\"videos\":[{\"url\":\"https://file.runapi.ai/generated\"}]}");
      InfiniteTalkClient runClient = InfiniteTalkClient.builder().apiKey("sk-test").transport(runTransport).build();
      CompletedAudioToVideoResponse runResponse = runClient.audioToVideo().run(
              AudioToVideoParams.builder()
                  .model(AudioToVideoModel.INFINITETALK_FROM_AUDIO)
                  .sourceImageUrl("https://cdn.runapi.ai/public/samples/image.jpg")
                  .sourceAudioUrl("https://cdn.runapi.ai/public/samples/music.mp3")
                  .prompt("A small red cube on a plain white table, studio product photo")
                  .build(),
          RequestOptions.builder().pollingInterval(Duration.ofMillis(1)).pollingMaxWait(Duration.ofSeconds(1)).build());
      assertNotNull(runResponse);

      SequenceTransport runWithOptionsTransport = new SequenceTransport(
          "{\"id\":\"task_audio_to_video_run_options\",\"status\":\"processing\"}",
          "{\"id\":\"task_audio_to_video_run_options\",\"status\":\"completed\",\"videos\":[{\"url\":\"https://file.runapi.ai/generated\"}]}");
      InfiniteTalkClient runWithOptionsClient = InfiniteTalkClient.builder().apiKey("sk-test").transport(runWithOptionsTransport).build();
      assertNotNull(runWithOptionsClient.audioToVideo().run(
              AudioToVideoParams.builder()
                  .model(AudioToVideoModel.INFINITETALK_FROM_AUDIO)
                  .sourceImageUrl("https://cdn.runapi.ai/public/samples/image.jpg")
                  .sourceAudioUrl("https://cdn.runapi.ai/public/samples/music.mp3")
                  .prompt("A small red cube on a plain white table, studio product photo")
                  .build(),
          RequestOptions.builder().pollingInterval(Duration.ofMillis(1)).pollingMaxWait(Duration.ofSeconds(1)).build()));
    }

  private static JsonNode bodyJson(HttpRequest request) throws Exception {
    JsonRequestBody body = (JsonRequestBody) request.getBody();
    ByteArrayOutputStream out = new ByteArrayOutputStream();
    body.writeTo(out);
    return Json.mapper().readTree(out.toByteArray());
  }

  private static final class CapturingTransport implements HttpTransport {
    private final String body;
    private HttpRequest request;

    private CapturingTransport(String body) {
      this.body = body;
    }

    public HttpResponse send(HttpRequest request) {
      this.request = request;
      return new HttpResponse(200, body, Collections.<String, java.util.List<String>>emptyMap());
    }

    public void close() {}
  }

  private static final class SequenceTransport implements HttpTransport {
    private final String[] responses;
    private int calls;

    private SequenceTransport(String... responses) {
      this.responses = responses;
    }

    public HttpResponse send(HttpRequest request) {
      String response = responses[Math.min(calls, responses.length - 1)];
      calls++;
      return new HttpResponse(200, response, Collections.<String, java.util.List<String>>emptyMap());
    }

    public void close() {}
  }
}
