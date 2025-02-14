import java.awt.BorderLayout;
import java.awt.CardLayout;
import java.awt.Dimension;
import java.awt.FlowLayout;
import java.awt.Font;

import javax.swing.Box;
import javax.swing.BoxLayout;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTextArea;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;

public class AppGUI {
    public static void main(String[] args) {
        // Inicializar el procesador conectado a la API de JFLAP
        String apiKey = System.getenv("GROQ_API_KEY");
        GrammarAutomataProcessor processor = new GrammarAutomataProcessor(apiKey);

        // Crear el marco principal
        JFrame frame = new JFrame("Aplicación");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(1000, 900);

        // Contenedor principal con CardLayout para cambiar de panel completo
        JPanel cardPanel = new JPanel(new CardLayout());

        // --- Panel MENÚ: Contiene título, botones y apartado de información ---
        JPanel menuPanel = new JPanel(new BorderLayout());

        // Título de la aplicación (cabecera)
        JLabel titleLabel = new JLabel("Gramáticas regulares e independientes de contexto y autómatas finitos");
        titleLabel.setFont(new Font("Serif", Font.BOLD, 18));
        titleLabel.setHorizontalAlignment(JLabel.CENTER);
        menuPanel.add(titleLabel, BorderLayout.NORTH);

        // Panel central con los botones que acceden a las funcionalidades
        JPanel buttonPanel = new JPanel(new FlowLayout());
        JButton docButton = new JButton("Consulta de Documentación");
        JButton tutorButton = new JButton("Tutor Virtual");
        docButton.setPreferredSize(new Dimension(250, 50));
        tutorButton.setPreferredSize(new Dimension(200, 50));
        buttonPanel.add(docButton);
        buttonPanel.add(tutorButton);
        menuPanel.add(buttonPanel, BorderLayout.CENTER);

        // Información de la herramienta (pie de página)
        String infoText = "<html><body style='text-align: center;'>"
                + "<b>Acerca de esta herramienta</b><br>"
                + "Proyecto: CHATBOT para JFLAP<br>"
                + "Profesor: Juan José Escribano<br>"
                + "Autor: Ignacio de Lecea Jiménez<br>"
                + "Fecha: 2024/2025<br>"
                + "Estado: En desarrollo<br><br>"
                + "Esta herramienta permite analizar consultas relacionadas con gramáticas regulares, "
                + "gramáticas independientes de contexto y autómatas finitos.<br>"
                + "También proporciona el servicio de un tutor virtual para facilitar la resolución de problemas."
                + "</body></html>";
        JLabel infoLabel = new JLabel(infoText);
        infoLabel.setHorizontalAlignment(JLabel.CENTER);
        menuPanel.add(infoLabel, BorderLayout.SOUTH);

        // --- Panel Consulta de Documentación (DOC): Sin cabecera ni pie ---
        JPanel docPanel = new JPanel();
        docPanel.setLayout(new BoxLayout(docPanel, BoxLayout.Y_AXIS));

        JLabel queryLabel = new JLabel("Consulta:");
        queryLabel.setFont(new Font("Serif", Font.BOLD, 14));

        JTextArea queryInput = new JTextArea(5, 40);
        queryInput.setLineWrap(true);
        queryInput.setWrapStyleWord(true);
        JScrollPane queryScroll = new JScrollPane(queryInput);

        JButton processButton = new JButton("Procesar Consulta");

        JLabel responseLabel = new JLabel("Respuesta:");
        responseLabel.setFont(new Font("Serif", Font.BOLD, 14));

        JTextArea responseArea = new JTextArea(15, 60);
        responseArea.setEditable(false);
        responseArea.setLineWrap(true);
        responseArea.setWrapStyleWord(true);
        JScrollPane responseScroll = new JScrollPane(responseArea);

        JButton backFromDocButton = new JButton("Volver al menú");

        processButton.addActionListener(e -> {
            String userQuery = queryInput.getText();
            String rawResponse = processor.answerQuestion(userQuery);
            String cleanedResponse = cleanResponse(rawResponse); // Limpiar la respuesta
            responseArea.setText("Respuesta:\n" + cleanedResponse);
        });

        backFromDocButton.addActionListener(e -> {
            CardLayout cl = (CardLayout) (cardPanel.getLayout());
            cl.show(cardPanel, "MENU");
        });

        docPanel.add(queryLabel);       // Agregar el título "Consulta"
        docPanel.add(queryScroll);      // Agregar área de texto para la consulta
        docPanel.add(Box.createVerticalStrut(10)); // Espacio entre consulta y botón
        docPanel.add(processButton);    // Botón para procesar la consulta
        docPanel.add(Box.createVerticalStrut(20)); // Espacio entre el botón y "Respuesta"
        docPanel.add(responseLabel);    // Agregar el título "Respuesta"
        docPanel.add(responseScroll);   // Agregar área de texto para mostrar la respuesta
        docPanel.add(Box.createVerticalStrut(10)); // Espacio antes del botón de volver
        docPanel.add(backFromDocButton); // Botón para volver al menú

       // --- Panel Tutor Virtual ---
       JPanel tutorPanel = new JPanel();
       tutorPanel.setLayout(new BoxLayout(tutorPanel, BoxLayout.Y_AXIS));

       JLabel problemStatementLabel = new JLabel("Enunciado:");
       problemStatementLabel.setFont(new Font("Serif", Font.BOLD, 14));

       JTextArea problemStatementInput = new JTextArea(10, 60);
       problemStatementInput.setLineWrap(true);
       problemStatementInput.setWrapStyleWord(true);
       JScrollPane problemScroll = new JScrollPane(problemStatementInput);

       JLabel userSolutionLabel = new JLabel("Escribe tu solución:");
       userSolutionLabel.setFont(new Font("Serif", Font.BOLD, 14));

       JTextArea userSolutionInput = new JTextArea(10, 60);
       userSolutionInput.setLineWrap(true);
       userSolutionInput.setWrapStyleWord(true);
       JScrollPane solutionScroll = new JScrollPane(userSolutionInput);

       JButton evaluateButton = new JButton("Evaluar Solución");

       JLabel tutorResponseLabel = new JLabel("Feedback:");
       tutorResponseLabel.setFont(new Font("Serif", Font.BOLD, 14));

       JTextArea tutorResponseArea = new JTextArea(15, 60);
       tutorResponseArea.setEditable(false);
       tutorResponseArea.setLineWrap(true);
       tutorResponseArea.setWrapStyleWord(true);
       JScrollPane tutorResponseScroll = new JScrollPane(tutorResponseArea);

       JButton backFromTutorButton = new JButton("Volver al menú");

       evaluateButton.addActionListener(e -> {
           String problem = problemStatementInput.getText();
           String solution = userSolutionInput.getText();
           String rawFeedback = processor.evaluateProblem(problem, solution);
           String cleanedFeedback = cleanResponse(rawFeedback); // Limpiar la respuesta
           tutorResponseArea.setText("Feedback:\n" + cleanedFeedback);
       });

       backFromTutorButton.addActionListener(e -> {
           CardLayout cl = (CardLayout) (cardPanel.getLayout());
           cl.show(cardPanel, "MENU");
       });

       tutorPanel.add(problemStatementLabel); 
       tutorPanel.add(problemScroll);         
       tutorPanel.add(userSolutionLabel);     
       tutorPanel.add(solutionScroll);        
       tutorPanel.add(Box.createVerticalStrut(10)); 
       tutorPanel.add(evaluateButton);        
       tutorPanel.add(Box.createVerticalStrut(20)); 
       tutorPanel.add(tutorResponseLabel);    
       tutorPanel.add(tutorResponseScroll);   
       tutorPanel.add(backFromTutorButton);

        // --- Agregar los tres paneles al contenedor de tarjetas ---
        cardPanel.add(menuPanel, "MENU");
        cardPanel.add(docPanel, "DOC");
        cardPanel.add(tutorPanel, "TUTOR");

        // Asignar cardPanel como contenido del marco
        frame.setContentPane(cardPanel);

        // Acciones para cambiar entre paneles
        docButton.addActionListener(e -> {
            CardLayout cl = (CardLayout) (cardPanel.getLayout());
            queryInput.setText(""); // Limpiar el campo de consulta
            responseArea.setText(""); // Limpiar el área de respuesta
            cl.show(cardPanel, "DOC"); // Cambiar al panel de documentación
        });

        tutorButton.addActionListener(e -> {
            CardLayout cl = (CardLayout) (cardPanel.getLayout());
            problemStatementInput.setText(""); // Limpiar el enunciado del problema
            userSolutionInput.setText(""); // Limpiar la solución del usuario
            tutorResponseArea.setText(""); // Limpiar el feedback
            cl.show(cardPanel, "TUTOR"); // Cambiar al panel de tutor virtual
            
        });

        frame.setVisible(true); // Hacer visible la ventana principal
    }

    /**
     * Método para limpiar la respuesta eliminando metadatos JSON y extrayendo solo el contenido relevante.
     */
    private static String cleanResponse(String rawResponse) {
        try {
            // Crear un ObjectMapper para analizar el JSON
            ObjectMapper objectMapper = new ObjectMapper();

            // Convertir la respuesta cruda en un árbol JSON
            JsonNode rootNode = objectMapper.readTree(rawResponse);

            // Navegar hasta el contenido relevante: choices[0].message.content
            JsonNode choicesNode = rootNode.path("choices");
            if (choicesNode.isArray() && choicesNode.size() > 0) {
                JsonNode messageNode = choicesNode.get(0).path("message");
                String content = messageNode.path("content").asText();

                // Reemplazar saltos de línea codificados con saltos reales y limpiar espacios adicionales
                return content.replace("\\n", "\n").trim();
            } else {
                return "Error: No se pudo procesar la respuesta.";
            }
        } catch (Exception e) {
            return "Error: Respuesta no válida.";
        }
    }
}

