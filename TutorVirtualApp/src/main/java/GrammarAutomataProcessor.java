import java.io.IOException;
import java.net.URISyntaxException;
import java.nio.file.DirectoryStream;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

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
    private String historyContext;

    public GrammarAutomataProcessor(String apiKey) {
        this.apiKey = apiKey;
        this.client = new OkHttpClient();

        // Cargar los contextos necesarios
        try {
            this.context = loadDocuContext();
            this.context2 = loadExerciseContext();
            this.glossary = loadGlossary();
            this.historyContext = loadHistoryContext(); // Cargar el contexto histórico
        } catch (IOException e) {
            System.err.println("Error al cargar los contextos: " + e.getMessage());
        }
    }

    private String loadDocuContext() throws IOException {
        StringBuilder contextData = new StringBuilder();
        try (DirectoryStream<Path> stream = Files.newDirectoryStream(
                Paths.get(getClass().getClassLoader().getResource("Docu").toURI()), "*.md")) {
            for (Path file : stream) {
                contextData.append(Files.readString(file)).append("\n");
            }
        } catch (URISyntaxException e) {
            throw new IOException("Error al cargar la carpeta 'Docu': " + e.getMessage());
        }
        return contextData.toString();
    }

    private String loadExerciseContext() throws IOException {
        StringBuilder exerciseData = new StringBuilder();
        try (DirectoryStream<Path> stream = Files.newDirectoryStream(
                Paths.get(getClass().getClassLoader().getResource("Ejercicios").toURI()), "*.md")) {
            for (Path file : stream) {
                exerciseData.append(Files.readString(file)).append("\n");
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

    private String loadHistoryContext() throws IOException {
        try {
            Path historyPath = Paths.get(getClass().getClassLoader().getResource("Historia_de_las_ciencias_de_la_computacion.md").toURI());
            return Files.readString(historyPath);
        } catch (NullPointerException | URISyntaxException e) {
            throw new IOException("El archivo 'Historia_de_las_ciencias_de_la_computacion.md' no existe en el directorio 'resources'.");
        }
    }

    public String answerQuestion(String userInput) {
        try {
            Map<String, Object> requestBody = new HashMap<>();
            requestBody.put("model", "llama-3.3-70b-versatile"); // Incluye el modelo aquí
            requestBody.put("messages", List.of(
                Map.of("role", "user", "content", formatTemplateAnswer(userInput))
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

            Response response = client.newCall(request).execute();
            if (!response.isSuccessful()) {
                throw new IOException("Error en la solicitud: Código HTTP " + response.code() + " - " + response.body().string());
            }

            return response.body().string();

        } catch (Exception e) {
            return "Error al procesar la consulta: " + e.getMessage();
        }
    }

    // Método para evaluar problemas y soluciones
    public String evaluateProblem(String problemStatement, String userSolution) {
        try {
            Map<String, Object> requestBody = new HashMap<>();
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

            Response response = client.newCall(request).execute();
            return response.body().string();

        } catch (Exception e) {
            return "Error al evaluar el problema: " + e.getMessage();
        }
    }

    // Formatear plantilla para responder preguntas con instrucciones detalladas
    private String formatTemplateAnswer(String userInput) {
        return """
               You are an expert in the subject of Regular Grammars, Context-Free Grammars, and Finite Automata.
               Respond only with information related to this subject relying on the provided context.

               Critical Instructions:
               1. Always replace the abbreviations (e.g., "GIC", "MT") with their full terms as defined below:
               - GIC stands for: Gramática Independiente de Contexto
               - G2 stands for: Gramática Independiente de Contexto  
               - LIC stands for: Lenguaje Independiente de contexto
               - LICD stands for: Lenguaje Independiente de contexto Determinista
               - LICND stands for: Lenguaje Independiente de contexto No Determinista
               - GR stands for: Gramática Regular
               - G3 stands for: Gramática Regular  
               - G3LD stands for: Gramática Regular (G3) Lineal por la Derecha
               - G3LI stands for: Gramática Regular (G3) Lineal por la Izquierda
               - MT stands for: Máquina de Turing
               - AP stands for: Autómata a Pila
               - AF stands for: Autómata finito
               - AFD stands for: Autómatas Finitos Deterministas
               - AFND stands for: Autómatas Finitos No Deterministas
               - APF stands for: Autómata a pila por estados finales
               - APV stands for: Autómata a pila por vaciado
               - FNC stands for: Forma Normal de Chomsky
               - FNG stands for: Forma Normal de Greibach
               - ER stands for: Expresión regular
               - APD stands for: Autómata a Pila Determinista  
               - APND stands for: Autómata a Pila No Determinista  
               - GICD stands for: Gramática Independiente de Contexto Determinista  
               - GICND stands for: Gramática Independiente de Contexto No Determinista  
               - LR stands for: Lenguaje Regular  
               - G0 stands for: Gramática sin restricciones
               - G1 stands for: Gramática sensible al contexto  
               - ERD stands for: Expresión Regular Determinista

               2. Do not use abbreviations in your response.

               3. If the user asks about any of the following figures:
                  Alan Turing, Stephen Kleene, Von Neumann, Noam Chomsky, Grace Murray Hopper, Ada Byron, Alfred Aho, Brian Kernighan,
                  Dennis Ritchie, Hedy Lamarr, Evelyn Berezin, Frances E. Allen, Anita Borg, Top Secret Rosies, Lynn Conway, Jude Milhon,
                  Ángela Ruíz Robles.

                  Always prioritize content from the Document about history of computational science:
                  %s

               Context from files:
               %s

               User Question:
               %s

               Based on the provided context, answer the user's question as accurately and concisely as possible. Ensure that:

               1. If the user asks about a term (e.g., "What is an AP?" or "Define what a MT is" or "Explain APV"), provide a detailed explanation of the term based on the context.

               2. If the user asks about any of the specified historical figures, ensure that your response is derived primarily from the historical context.

               3. The answer is directly derived from the context.

               4. Technical terms are preserved exactly as they appear.

               5. The answer is clear and actionable.

               Answer:
               """.formatted(historyContext, context, userInput);
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
    
    
    // Método de ejemplo para integrar la API de JFLAP usando jflap‑lib.
    // Se debe adaptar según la documentación de jflap-lib.
    public String processJflap(String input) {
        try {
            // Ejemplo: inicializar la clase JflapProcessor (suponiendo que exista en la librería) y procesar la entrada.
            // JflapProcessor jflapProcessor = new JflapProcessor();
            // return jflapProcessor.process(input);
            return "Resultado de JFLAP para: " + input;
        } catch(Exception e) {
            return "Error en procesamiento JFLAP: " + e.getMessage();
        }
    }
}
