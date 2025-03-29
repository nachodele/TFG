// Versión CORREGIDA con cambios necesarios:
plugins {
    id("java")
    id("application")
}

group = "com.example"
version = "1.0-SNAPSHOT"

java {
    sourceCompatibility = JavaVersion.VERSION_21
    targetCompatibility = JavaVersion.VERSION_21
}

application {
    mainClass.set("AppGUI")
}

repositories {
    mavenCentral()
}

// Configuración única de tareas de compilación
tasks.withType<JavaCompile> {
    options.compilerArgs.addAll(listOf(
        "-Xlint:deprecation",
        "-Xlint:unchecked"
    ))
    options.encoding = "UTF-8"
}

dependencies {
    // Jackson (ya correcto)
    implementation("com.fasterxml.jackson.core:jackson-databind:2.15.2")
    implementation("com.fasterxml.jackson.core:jackson-core:2.15.2")
    implementation("com.fasterxml.jackson.core:jackson-annotations:2.15.2")
    
    // OkHttp (ya correcto)
    implementation("com.squareup.okhttp3:okhttp:4.9.3")
    implementation("com.squareup.okio:okio:2.10.0")
    
    // JFLAP (ya correcto)
    implementation(files("lib/jflaplib-cli-1.3-bundle.jar"))
    implementation(files("lib/jflaplib-core-1.3-bundle.jar"))
    
    // AÑADIR para logs (necesario para debug Qdrant)
    implementation("org.slf4j:slf4j-api:2.0.7")
    implementation("ch.qos.logback:logback-classic:1.4.11")
}
