plugins {
    id("java")
    application
    id("com.github.johnrengelman.shadow") version "8.1.1" // Última versión estable
}

group = "com.example"
version = "1.0-SNAPSHOT"

java {
    toolchain {
        languageVersion.set(JavaLanguageVersion.of(21))
    }
}

application {
    mainClass.set("AppGUI")
}

repositories {
    mavenCentral()
}

dependencies {
    implementation("com.squareup.okhttp3:okhttp:4.12.0")
    implementation("com.fasterxml.jackson.core:jackson-databind:2.16.1")
    implementation(files("lib/jflaplib-cli-1.3-bundle.jar"))
    implementation(files("lib/jflaplib-core-1.3-bundle.jar"))
}

tasks.named<com.github.jengelman.gradle.plugins.shadow.tasks.ShadowJar>("shadowJar") {
    archiveBaseName.set("GrammarAutomata")
    archiveClassifier.set("")
    mergeServiceFiles()
    
    manifest {
        attributes("Main-Class" to "AppGUI")
    }
    
    exclude("META-INF/*.DSA", "META-INF/*.RSA", "META-INF/*.SF")
}
