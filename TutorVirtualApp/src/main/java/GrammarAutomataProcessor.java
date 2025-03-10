import java.io.IOException;
import java.net.URISyntaxException;
import java.nio.file.DirectoryStream;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.lang.reflect.Method;


import com.fasterxml.jackson.databind.ObjectMapper;

import okhttp3.MediaType;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.RequestBody;
import okhttp3.Response;

public class GrammarAutomataProcessor {
    private final String apiKey;
    private final OkHttpClient client;
    private String context;
    private String context2;
    private String glossary;

    public GrammarAutomataProcessor(String apiKey) {
        this.apiKey = apiKey;
        this.client = new OkHttpClient();

        try {
            this.context = loadDocuContext();
            this.context2 = loadExerciseContext();
            this.glossary = loadGlossary();
        } catch (IOException e) {
            System.err.println("Error al cargar los contextos: " + e.getMessage());
        }
    }

    private String loadDocuContext() throws IOException {
        StringBuilder contextData = new StringBuilder();
        try {
            Path docuPath = Paths.get(getClass().getClassLoader().getResource("Docu").toURI());
            try (DirectoryStream<Path> stream = Files.newDirectoryStream(docuPath, "*.md")) {
                for (Path file : stream) {
                    contextData.append(Files.readString(file)).append("\n");
                }
            }
        } catch (URISyntaxException e) {
            throw new IOException("Error al cargar la carpeta 'Docu': " + e.getMessage());
        }
        return contextData.toString();
    }

    private String loadExerciseContext() throws IOException {
        StringBuilder exerciseData = new StringBuilder();
        try {
            Path ejerciciosPath = Paths.get(getClass().getClassLoader().getResource("Ejercicios").toURI());
            try (DirectoryStream<Path> stream = Files.newDirectoryStream(ejerciciosPath, "*.md")) {
                for (Path file : stream) {
                    exerciseData.append(Files.readString(file)).append("\n");
                }
            }
        } catch (URISyntaxException e) {
            throw new IOException("Error al cargar la carpeta 'Ejercicios': " + e.getMessage());
        }
        return exerciseData.toString();
    }

    private String loadGlossary() throws IOException {
        try {
            Path glossaryPath = Paths.get(getClass().getClassLoader().getResource("glosario.md").toURI());
            return Files.readString(glossaryPath);
        } catch (NullPointerException | URISyntaxException e) {
            throw new IOException("El archivo 'glosario.md' no existe en el directorio 'resources'.");
        }
    }

    /**
     * Analiza el contexto entre la pregunta anterior y la actual.
     * Si la pregunta anterior es nula o vacía, se devuelve la pregunta actual.
     */
    public String analyzeContext(String previousQuestion, String currentQuestion) {
        if (currentQuestion == null || currentQuestion.isEmpty()) {
            return "Error: La pregunta actual está vacía.";
        }

        if (previousQuestion == null || previousQuestion.isEmpty()) {
            return currentQuestion;
        }

        try {
            Map<String, Object> requestBody = new HashMap<>();
            requestBody.put("model", "llama-3.3-70b-versatile");
            requestBody.put("messages", List.of(
                Map.of("role", "user", "content", formatTemplateContextAnalysis(previousQuestion, currentQuestion))
            ));
            requestBody.put("temperature", 0.1);
            requestBody.put("max_tokens", 256);

            String json = new ObjectMapper().writeValueAsString(requestBody);
            RequestBody body = RequestBody.create(json, MediaType.parse("application/json"));

            Request request = new Request.Builder()
                    .url("https://api.groq.com/openai/v1/chat/completions")
                    .post(body)
                    .addHeader("Authorization", "Bearer " + apiKey)
                    .build();

            try (Response response = client.newCall(request).execute()) {
                if (!response.isSuccessful()) {
                    throw new IOException("Error en la solicitud: Código HTTP " 
                        + response.code() + " - " + response.body().string());
                }
                return new ObjectMapper().readTree(response.body().string())
                        .get("choices").get(0).get("message").get("content").asText();
            }
        } catch (Exception e) {
            return "Error al analizar el contexto: " + e.getMessage();
        }
    }

    /**
     * Responde a la pregunta actual utilizando la pregunta anterior como contexto.
     */
    public String answerQuestion(String userInput, String previousQuestion) {
        if (userInput == null || userInput.isEmpty()) {
            return "Error: La entrada del usuario está vacía.";
        }

        try {
            String analyzedQuestion = analyzeContext(previousQuestion, userInput);
            Map<String, Object> requestBody = new HashMap<>();
            requestBody.put("model", "llama-3.3-70b-versatile");
            requestBody.put("messages", List.of(
                Map.of("role", "user", "content", formatTemplateAnswer(analyzedQuestion))
            ));
            requestBody.put("temperature", 0.1);
            requestBody.put("max_tokens", 1024);

            String json = new ObjectMapper().writeValueAsString(requestBody);
            RequestBody body = RequestBody.create(json, MediaType.parse("application/json"));

            Request request = new Request.Builder()
                    .url("https://api.groq.com/openai/v1/chat/completions")
                    .post(body)
                    .addHeader("Authorization", "Bearer " + apiKey)
                    .build();

            try (Response response = client.newCall(request).execute()) {
                if (!response.isSuccessful()) {
                    throw new IOException("Error en la solicitud: Código HTTP " 
                        + response.code() + " - " + response.body().string());
                }
                return response.body().string();
            }
        } catch (Exception e) {
            return "Error al procesar la consulta: " + e.getMessage();
        }
    }

    /**
     * Evalúa la solución del usuario para un problema específico.
     */
    public String evaluateProblem(String problemStatement, String userSolution) {
        try {
            Map<String, Object> requestBody = new HashMap<>();
            requestBody.put("model", "llama-3.3-70b-versatile"); 
            requestBody.put("messages", List.of(
                Map.of("role", "user", "content", formatTemplateProblem(problemStatement, userSolution))
            ));
            requestBody.put("temperature", 0.1);
            requestBody.put("max_tokens", 1024);

            String json = new ObjectMapper().writeValueAsString(requestBody);
            RequestBody body = RequestBody.create(json, MediaType.parse("application/json"));
            Request request = new Request.Builder()
                    .url("https://api.groq.com/openai/v1/chat/completions")
                    .post(body)
                    .addHeader("Authorization", "Bearer " + apiKey)
                    .build();

            try (Response response = client.newCall(request).execute()) {
                if (!response.isSuccessful()) {
                    throw new IOException("Error en la solicitud: Código HTTP " 
                        + response.code() + " - " + response.body().string());
                }
                return response.body().string();
            }
        } catch (Exception e) {
            return "Error al evaluar el problema: " + e.getMessage();
        }
    }

    private String formatTemplateContextAnalysis(String previousQuestion, String currentQuestion) {
        return """
                Determine if the current question is self-contained and complete.
                If the current question does not contain ambiguous references (such as pronouns or terms like "este" o "eso") and is fully understandable on its own, output the current question exactly as provided.
                If the current question is ambiguous or incomplete, incorporate only the minimal essential context from the previous question to remove that ambiguity.
                Previous Question:
                %s
                Current Question:
                %s
                Important:
                - Only include context that is absolutely necessary to clarify ambiguous references in the current question.
                - If the current question is fully self-contained, do not add any context from the previous question.
                - Do not include any explanation, analysis, or any additional information in the output.
                Output:
                A single, standalone question that incorporates additional context only if needed; otherwise, output the current question unchanged.
                """.formatted(previousQuestion, currentQuestion);
    }

    private String formatTemplateAnswer(String userInput) {
        return """
                You are an expert in the subject of Regular Grammars, Context-Free Grammars, and Finite Automata.
                Context from files:
                %s
                User Question:
                %s
                Ensure that:
                1. The answer is directly derived from the context.
                2. Technical terms are preserved exactly as they appear in the context.
                3. The answer is clear, precise, and actionable.
                4. Unnecessary repetition is avoided.
                5. If the user asks about a term (e.g., "What is an AP?" or "Define what a MT is" or "Explain APV"), provide a detailed explanation of the term based on the context.

                Critical Instructions:
                1. Always replace the abbreviations (e.g., "GIC", "MT") with their full terms as defined below:
                - GIC stands for: Gramática Independiente de Contexto
                - G2 stands for: Gramática Independiente de Contexto  
                - LIC stands for: Lenguaje Independiente de contexto
                - GR stands for: Gramática Regular
                - G3 stands for: Gramática Regular  
                - G3LD stands for: Gramática Regular (G3) Lineal por la Derecha
                - G3LI stands for: Gramática Regular (G3) Lineal por la Izquierda
                - MT stands for: Máquina de Turing
                - AP stands for: Autómata a Pila
                - AF stands for: Autómata finito
                - APF stands for: Autómata a pila por estados finales
                - APV stands for: Autómata a pila por vaciado
                - FNC stands for: Forma Normal de Chomsky
                - FNG stands for: Forma Normal de Greibach
                - ER stands for: Expresión regular
                - APD stands for: Autómata a Pila Determinista  
                - APND stands for: Autómata a Pila No Determinista  
                - GICD stands for: Gramática Independiente de Contexto Determinista  
                - GICND stands for: Gramática Independiente de Contexto No Determinista  
                - LICD stands for: Lenguaje Independiente de contexto Determinista
                - LICND stands for: Lenguaje Independiente de contexto No Determinista
                - AFD stands for: Autómata Finito Determinista
                - AFND stands for: Autómata Finito No Determinista
                - LR stands for: Lenguaje Regular  
                - G0 stands for: Gramática sin restricciones
                - G1 stands for: Gramática sensible al contexto  
                - ERD stands for: Expresión Regular Determinista
                2. Do not use abbreviations in your response.
                3. Use only plain text symbols as specified in the glossary below. Do not use LaTeX or non-plain text formats.
                Glossary of Plain Text Symbols:
                %s
            
                Answer:
                """.formatted(context, userInput, glossary);
    }

    private String formatTemplateProblem(String problemStatement, String userSolution) {
        return """
                You are a virtual tutor specializing in Regular Grammars, Context-Free Grammars, and Finite Automata.
                Your task is to evaluate the user's solution to the given problem statement step by step.
    
                Context from Exercises:
                %s
    
                Problem Statement:
                %s
    
                User Solution:
                %s
    
                Instructions:
                - Analyze the solution step by step.
                - Identify any errors and explain where the user went wrong.
                - Provide hints or guidance to help the user correct their mistakes without directly giving the solution.
                - If the solution is correct, confirm it and explain why it works.
    
                Critical Note: Use only plain text symbols as specified in the glossary below. Do not use LaTeX or non-plain text formats.
    
                Glossary of Plain Text Symbols:
                %s
    
                Feedback:
                """.formatted(context2, problemStatement, userSolution, glossary);
    }

    public String processJflap(String input) {
        try {
            // Ejemplo: Usar JFLAP para procesar una gramática o un autómata
            Class<?> jflapMain = Class.forName("edu.duke.cs.jflap.file.ParseFile");
            Method parseMethod = jflapMain.getMethod("parse", String.class);
    
            // Invocar el método parse con la entrada proporcionada
            Object result = parseMethod.invoke(null, input);
    
            // Procesar el resultado (puedes personalizar según lo que necesites)
            return "Resultado procesado por JFLAP: " + result.toString();
        } catch (Exception e) {
            return "Error en procesamiento JFLAP: " + e.getMessage();
        }
    }
    
}
