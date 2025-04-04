import javax.swing.*;
import java.awt.*;
import java.io.*;
import java.net.HttpURLConnection;
import java.net.Socket;
import java.net.URL;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.Map;
import java.util.concurrent.TimeUnit;
import java.util.stream.Collectors;
import java.lang.reflect.Method;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import okhttp3.*;

public class AppGUI {
    private static final String API_URL = "http://localhost:5050/api";
    
    private static final OkHttpClient client = new OkHttpClient.Builder()
        .connectTimeout(30, TimeUnit.SECONDS)
        .readTimeout(30, TimeUnit.SECONDS)
        .writeTimeout(30, TimeUnit.SECONDS)
        .build();
    
    private static final ObjectMapper mapper = new ObjectMapper();
    private static Process apiProcess;

    public static void main(String[] args) {
        startFlaskAPI();

        final String[] previousQuestion = { null };

        JFrame frame = new JFrame("Aplicación");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(1000, 900);

        JPanel cardPanel = new JPanel(new CardLayout());

        // Panel MENÚ
        JPanel menuPanel = new JPanel(new BorderLayout());
        JLabel titleLabel = new JLabel("Gramáticas regulares e independientes de contexto y autómatas finitos");
        titleLabel.setFont(new Font("Serif", Font.BOLD, 22));
        titleLabel.setHorizontalAlignment(JLabel.CENTER);
        menuPanel.add(titleLabel, BorderLayout.NORTH);
        menuPanel.setBorder(BorderFactory.createEmptyBorder(25, 0, 0, 0));

        JPanel buttonPanel = new JPanel(new FlowLayout());
        JButton docButton = new JButton("Consulta de Documentación");
        JButton tutorButton = new JButton("Tutor Virtual");
        JButton jflapButton = new JButton("JFLAP");

        Font buttonFont = new Font("Serif", Font.BOLD, 20);
        docButton.setFont(buttonFont);
        tutorButton.setFont(buttonFont);
        jflapButton.setFont(buttonFont);

        docButton.setPreferredSize(new Dimension(350, 100));
        tutorButton.setPreferredSize(new Dimension(300, 100));
        jflapButton.setPreferredSize(new Dimension(350, 100));

        buttonPanel.add(docButton);
        buttonPanel.add(tutorButton);
        buttonPanel.add(jflapButton);
        buttonPanel.add(Box.createVerticalStrut(200));
        menuPanel.add(buttonPanel, BorderLayout.CENTER);

        JPanel southPanel = new JPanel();
        southPanel.setLayout(new BoxLayout(southPanel, BoxLayout.Y_AXIS));
        ImageIcon ufvIcon = new ImageIcon(AppGUI.class.getClassLoader().getResource("ufv.png"));
        JLabel imageLabel = new JLabel(ufvIcon);
        imageLabel.setAlignmentX(JLabel.CENTER_ALIGNMENT);
        southPanel.add(imageLabel);
        southPanel.add(Box.createVerticalStrut(50));

        String infoText = "<html><body style='text-align: center; font-size: 11px; line-height: 1.4;'>"
                + "<b>Acerca de esta herramienta</b><br>"
                + "Proyecto CHATBOT para JFLAP<br>"
                + "Profesor: Juan José Escribano<br>"
                + "Autor: Ignacio de Lecea Jiménez<br>"
                + "Fecha: 2024-2025<br>"
                + "Estado: En desarrollo<br><br>"
                + "Esta herramienta permite analizar consultas relacionadas con gramáticas regulares, "
                + "gramáticas independientes de contexto y autómatas finitos.<br>"
                + "También proporciona el servicio de un tutor virtual para facilitar la resolución de problemas."
                + "</body></html>";
        JLabel infoLabel = new JLabel(infoText);
        infoLabel.setAlignmentX(JLabel.CENTER_ALIGNMENT);
        southPanel.add(infoLabel);
        southPanel.setBorder(BorderFactory.createEmptyBorder(0, 0, 20, 0));
        menuPanel.add(southPanel, BorderLayout.SOUTH);

        // Panel Documentación
        JPanel docPanel = new JPanel();
        docPanel.setLayout(new BoxLayout(docPanel, BoxLayout.Y_AXIS));
        JLabel queryLabel = new JLabel("Ingrese su consulta:");
        queryLabel.setFont(new Font("Serif", Font.BOLD, 14));
        JTextArea queryInput = new JTextArea(5, 40);
        queryInput.setLineWrap(true);
        queryInput.setWrapStyleWord(true);
        JScrollPane queryScroll = new JScrollPane(queryInput);
        JButton processButton = new JButton("Procesar Consulta");
        JLabel responseLabel = new JLabel("Respuesta:");
        responseLabel.setFont(new Font("Serif", Font.BOLD, 15));
        JTextArea responseArea = new JTextArea(15, 60);
        responseArea.setEditable(false);
        responseArea.setLineWrap(true);
        responseArea.setWrapStyleWord(true);
        JScrollPane responseScroll = new JScrollPane(responseArea);
        JButton backFromDocButton = new JButton("Volver al menú");

        processButton.addActionListener(e -> {
            String userQuery = queryInput.getText().trim();
            if (userQuery.isEmpty()) {
                responseArea.setText("Por favor, ingrese una consulta.");
                return;
            }
            
            String rawResponse;
            try {
                rawResponse = sendApiRequest("/answer", 
                    "{\"question\":\"" + userQuery + "\", \"previous_question\":\"" 
                    + (previousQuestion[0] == null ? "" : previousQuestion[0]) + "\"}");
                previousQuestion[0] = userQuery;
            } catch (Exception ex) {
                rawResponse = "Error al procesar la consulta: " + ex.getMessage();
            }
            String cleanedResponse = cleanResponse(rawResponse);
            responseArea.setText(cleanedResponse);
        });

        backFromDocButton.addActionListener(e -> {
            CardLayout cl = (CardLayout) (cardPanel.getLayout());
            cl.show(cardPanel, "MENU");
        });

        docPanel.add(queryLabel);
        docPanel.add(queryScroll);
        docPanel.add(Box.createVerticalStrut(10));
        docPanel.add(processButton);
        docPanel.add(Box.createVerticalStrut(20));
        docPanel.add(responseLabel);
        docPanel.add(responseScroll);
        docPanel.add(Box.createVerticalStrut(10));
        docPanel.add(backFromDocButton);

        // Panel Tutor
        JPanel tutorPanel = new JPanel();
        tutorPanel.setLayout(new BoxLayout(tutorPanel, BoxLayout.Y_AXIS));
        JLabel problemStatementLabel = new JLabel("Enunciado:");
        problemStatementLabel.setFont(new Font("Serif", Font.BOLD, 15));
        problemStatementLabel.setAlignmentX(JLabel.LEFT_ALIGNMENT);
        JButton glossaryButton = new JButton("Glosario");
        glossaryButton.setAlignmentX(JButton.LEFT_ALIGNMENT);

        glossaryButton.addActionListener(e -> {
            try {
                Path glossaryPath = Paths.get(AppGUI.class.getClassLoader().getResource("glosario.md").toURI());
                String glossaryContent = Files.readString(glossaryPath);
                String[] lines = glossaryContent.split("\n");
                StringBuilder htmlTable = new StringBuilder("<html><body><table border='1' style='border-collapse: collapse; width: 100%;'>");
                for (String line : lines) {
                    if (line.startsWith("|")) {
                        String[] cells = line.split("\\|");
                        htmlTable.append("<tr>");
                        for (String cell : cells) {
                            if (!cell.trim().isEmpty()) {
                                String cellContent = cell.trim().replace("**", "");
                                htmlTable.append("<td>").append(cellContent).append("</td>");
                            }
                        }
                        htmlTable.append("</tr>");
                    }
                }
                htmlTable.append("</table></body></html>");
                JEditorPane editorPane = new JEditorPane("text/html", htmlTable.toString());
                editorPane.setEditable(false);
                JScrollPane scrollPane = new JScrollPane(editorPane);
                scrollPane.setPreferredSize(new Dimension(600, 400));
                JOptionPane.showMessageDialog(null, scrollPane, "Glosario", JOptionPane.INFORMATION_MESSAGE);
            } catch (Exception ex) {
                ex.printStackTrace();
                JOptionPane.showMessageDialog(null, "Error al cargar el glosario", "Error", JOptionPane.ERROR_MESSAGE);
            }
        });

        JPanel enunciadoPanel = new JPanel(new FlowLayout(FlowLayout.LEFT));
        enunciadoPanel.add(glossaryButton);
        enunciadoPanel.add(problemStatementLabel);
        enunciadoPanel.setAlignmentX(JPanel.LEFT_ALIGNMENT);
        tutorPanel.add(enunciadoPanel);

        JTextArea problemStatementInput = new JTextArea(10, 60);
        problemStatementInput.setLineWrap(true);
        problemStatementInput.setWrapStyleWord(true);
        JScrollPane problemScroll = new JScrollPane(problemStatementInput);
        problemScroll.setAlignmentX(JScrollPane.LEFT_ALIGNMENT);
        tutorPanel.add(problemScroll);

        JLabel userSolutionLabel = new JLabel("Ingrese su solución:");
        userSolutionLabel.setFont(new Font("Serif", Font.BOLD, 15));
        userSolutionLabel.setAlignmentX(JLabel.LEFT_ALIGNMENT);
        tutorPanel.add(userSolutionLabel);

        JTextArea userSolutionInput = new JTextArea(10, 60);
        userSolutionInput.setLineWrap(true);
        userSolutionInput.setWrapStyleWord(true);
        JScrollPane solutionScroll = new JScrollPane(userSolutionInput);
        solutionScroll.setAlignmentX(JScrollPane.LEFT_ALIGNMENT);
        tutorPanel.add(solutionScroll);

        JButton evaluateButton = new JButton("Evaluar Solución");
        JPanel buttonRowPanel = new JPanel(new FlowLayout(FlowLayout.LEFT));
        buttonRowPanel.add(evaluateButton);
        buttonRowPanel.setAlignmentX(JPanel.LEFT_ALIGNMENT);
        tutorPanel.add(Box.createVerticalStrut(10));
        tutorPanel.add(buttonRowPanel);

        JLabel tutorResponseLabel = new JLabel("Feedback:");
        tutorResponseLabel.setFont(new Font("Serif", Font.BOLD, 15));
        tutorResponseLabel.setAlignmentX(JLabel.LEFT_ALIGNMENT);
        tutorPanel.add(tutorResponseLabel);

        JTextArea tutorResponseArea = new JTextArea(15, 60);
        tutorResponseArea.setEditable(false);
        tutorResponseArea.setLineWrap(true);
        tutorResponseArea.setWrapStyleWord(true);
        JScrollPane tutorResponseScroll = new JScrollPane(tutorResponseArea);
        tutorResponseScroll.setAlignmentX(JScrollPane.LEFT_ALIGNMENT);
        tutorPanel.add(tutorResponseScroll);

        JButton backFromTutorButton = new JButton("Volver al menú");
        backFromTutorButton.setAlignmentX(JButton.LEFT_ALIGNMENT);
        tutorPanel.add(backFromTutorButton);

        backFromTutorButton.addActionListener(e -> {
            CardLayout cl = (CardLayout) (cardPanel.getLayout());
            cl.show(cardPanel, "MENU");
        });

        evaluateButton.addActionListener(e -> {
            String problemStatement = problemStatementInput.getText();
            String userSolution = userSolutionInput.getText();
            if (problemStatement.isEmpty() || userSolution.isEmpty()) {
                tutorResponseArea.setText("Por favor, complete ambos campos antes de evaluar.");
                return;
            }
            try {
                String rawResponse = sendApiRequest("/evaluate", 
                    "{\"problem\":\"" + problemStatement + "\", \"solution\":\"" + userSolution + "\"}");
                String cleanedResponse = cleanResponse(rawResponse);
                tutorResponseArea.setText(cleanedResponse);
            } catch (IOException ex) {
                tutorResponseArea.setText("Error al evaluar la solución: " + ex.getMessage());
            }
        });

        cardPanel.add(menuPanel, "MENU");
        cardPanel.add(docPanel, "DOC");
        cardPanel.add(tutorPanel, "TUTOR");

        docButton.addActionListener(e -> {
            CardLayout cl = (CardLayout) (cardPanel.getLayout());
            queryInput.setText("");
            responseArea.setText("");
            cl.show(cardPanel, "DOC");
        });

        tutorButton.addActionListener(e -> {
            CardLayout cl = (CardLayout) (cardPanel.getLayout());
            problemStatementInput.setText("");
            userSolutionInput.setText("");
            tutorResponseArea.setText("");
            cl.show(cardPanel, "TUTOR");
        });
        
        jflapButton.addActionListener(e -> launchJFLAP());

        frame.setContentPane(cardPanel);
        frame.setVisible(true);
    }

    private static void startFlaskAPI() {
        new Thread(() -> {
            try {
                String pythonCmd = System.getProperty("os.name").toLowerCase().contains("win") 
                        ? "python" 
                        : "python3";
                
                ProcessBuilder pb = new ProcessBuilder(
                    pythonCmd,
                    new File("src/main/python/api.py").getAbsolutePath(),
                    "--port", "5050"
                );
                
                pb.directory(new File(System.getProperty("user.dir")));
                pb.redirectErrorStream(true);
                Map<String, String> env = pb.environment();
                env.put("PYTHONUNBUFFERED", "1");
                
                apiProcess = pb.start();
                
                new Thread(() -> {
                    try (BufferedReader reader = new BufferedReader(
                            new InputStreamReader(apiProcess.getInputStream()))) {
                        String line;
                        while ((line = reader.readLine()) != null) {
                            System.out.println("[API] " + line);
                        }
                    } catch (IOException e) {
                        e.printStackTrace();
                    }
                }).start();
                
                waitForApiReady(5050, 30);

            } catch (IOException | InterruptedException e) {
                JOptionPane.showMessageDialog(null, 
                    "Error crítico al iniciar API: " + e.getMessage(), 
                    "Error de Inicio", 
                    JOptionPane.ERROR_MESSAGE);
                System.exit(1);
            }
        }).start();
    }

    private static void waitForApiReady(int port, int maxAttempts) throws InterruptedException {
        for (int i = 0; i < maxAttempts; i++) {
            try (Socket s = new Socket("localhost", port)) {
                return;
            } catch (IOException e) {
                Thread.sleep(1000);
            }
        }
        throw new RuntimeException("Timeout: API no iniciada después de " + maxAttempts + " segundos");
    }

    private static String sendApiRequest(String endpoint, String json) throws IOException {
        RequestBody body = RequestBody.create(json, MediaType.parse("application/json"));
        Request request = new Request.Builder()
            .url(API_URL + endpoint)
            .post(body)
            .build();

        try (Response response = client.newCall(request).execute()) {
            if (!response.isSuccessful()) throw new IOException("Error HTTP: " + response.code());
            return response.body().string();
        }
    }

    private static String cleanResponse(String rawResponse) {
        try {
            JsonNode rootNode = mapper.readTree(rawResponse);
            return rootNode.has("response") 
                ? rootNode.get("response").asText().replace("\\n", "\n") 
                : rootNode.toString();
        } catch (IOException e) {
            return rawResponse;
        }
    }

    private static void launchJFLAP() {
        try {
            Class<?> jflapClass = Class.forName("edu.duke.cs.jflap.JFLAP");
            Method mainMethod = jflapClass.getMethod("main", String[].class);
            mainMethod.invoke(null, (Object) new String[]{});
        } catch (Exception ex) {
            JOptionPane.showMessageDialog(null,
                "Error al iniciar JFLAP: " + ex.getMessage(),
                "Error", JOptionPane.ERROR_MESSAGE);
        }
    }
}
