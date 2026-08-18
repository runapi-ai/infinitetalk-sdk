plugins {
  `java-library`
  `maven-publish`
}

extra["runapiSlug"] = "infinitetalk"

description = "RunAPI InfiniteTalk Java SDK for InfiniteTalk workflows."

java {
  withSourcesJar()
  withJavadocJar()
}

dependencies {
  api("ai.runapi:runapi-core:0.5.0")

  testImplementation(platform("org.junit:junit-bom:5.10.3"))
  testImplementation("org.junit.jupiter:junit-jupiter")
}

publishing {
  publications {
    create<MavenPublication>("mavenJava") {
      from(components["java"])
      artifactId = "runapi-infinitetalk"
      pom {
        name = "RunAPI InfiniteTalk Java SDK"
        description = "RunAPI InfiniteTalk Java SDK for InfiniteTalk workflows."
        url = "https://runapi.ai/models/infinitetalk"
        licenses {
          license {
            name = "Apache License, Version 2.0"
            url = "https://www.apache.org/licenses/LICENSE-2.0"
          }
        }
        developers {
          developer {
            id = "runapi"
            name = "RunAPI"
            email = "contact@runapi.ai"
          }
        }
        scm {
          url = "https://github.com/runapi-ai/infinitetalk-sdk"
          connection = "scm:git:https://github.com/runapi-ai/infinitetalk-sdk.git"
          developerConnection = "scm:git:ssh://git@github.com/runapi-ai/infinitetalk-sdk.git"
        }
      }
    }
  }
}
