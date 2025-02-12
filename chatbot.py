import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

class GrammarAutomataProcessor:
    def __init__(self):

        # Cargamos variables de entorno
        load_dotenv(override=True)

        # Cargamos el contexto de la Docu
        self.context = self._load_docu_context()

        # Cargamos el contexto de Ejercicios
        self.context2 = self._load_exercise_context()

        # Cargamos el glosario
        self.glossary = self._load_glossary()

        self.prev_question = None  # Almacena la pregunta anterior

         # Cargar el contexto de historia de las ciencias de la computación
        self.history_context = self._load_history_context()

        # Inicializamos el modelo Llama 3.3 en Groq
        self.client = self._initialize_groq()

        # Plantilla de prompt para responder preguntas
        self.TEMPLATE_ANSWER = """
        You are an expert in the subject of Regular Grammars, Context-Free Grammars, and Finite Automata.
        Respond only with information related to this subject relying on the provided context.

        Critical Instructions:
        1. Always replace the abbreviations (e.g., "GIC", "MT") with their full terms as defined below.

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
        - Alan Turing
        - Stephen Kleene
        - Von Neumann
        - Noam Chomsky
        - Grace Murray Hopper
        - Ada Byron
        - Alfred Aho
        - Brian Kernighan
        - Dennis Ritchie
        - Hedy Lamarr
        - Evelyn Berezin
        - Frances E. Allen
        - Anita Borg
        - Top Secret Rosies
        - Lynn Conway
        - Jude Milhon
        - Ángela Ruíz Robles
        
        Always prioritize content from the Document about history of computational science.
        {history_context}


        Context from files:
        {context}

        User Question: {user_input}

        Based on the provided context, answer the user's question as accurately and concisely as possible. Ensure that:
        1. If the user asks about a term (e.g., "What is an AP?" or "Define what a MT is" or "Explain APV"), provide a detailed explanation of the term based on the context.
        2. If the user asks about any of the specified historical figures, ensure that your response is derived primarily from {history_context}.
        3. The answer is directly derived from the context.
        4. Technical terms are preserved exactly as they appear.
        5. The answer is clear and actionable.

        Answer:
        """


        # Plantilla para evaluar problemas
        self.TEMPLATE_PROBLEM = """
        You are a virtual tutor specializing in Regular Grammars, Context-Free Grammars, and Finite Automata.
        Your task is to evaluate the user's solution to the given problem statement step by step.

        Context from Exercises:
        {context2}

        Problem Statement:
        {problem_statement}

        User Solution:
        {user_solution}

        Instructions:
        - Analyze the solution step by step.
        - Identify any errors and explain where the user went wrong.
        - Provide hints or guidance to help the user correct their mistakes without directly giving the solution.
        - If the solution is correct, confirm it and explain why it works.

        Critical Note: Use only plain text symbols as specified in the glossary below. Do not use LaTeX or non-plain text formats.

        Glossary of Plain Text Symbols:
        {glossary}

        Feedback:
        """
        self.TEMPLATE_CONTEXT_ANALYSIS = """
         Previous Question: {previous_question}
         Current Question: {current_question}

         Analyze if the current question is related to the previous one. If it is related, incorporate only the essential context from the previous question to make the current question complete and standalone.

         Important:
         - Only include context that is absolutely necessary to understand the current question.
         - Do not add any explanations or additional information.
         - The output should be a single, concise question that can stand on its own.
         """

    def _initialize_groq(self):
        """
        Inicializa el cliente Groq con la clave API desde las variables de entorno.
        """
        return Groq(api_key=os.getenv("GROQ_API_KEY"))

    def _load_docu_context(self):
        """
        Carga el contenido de los archivos .md en un único string para ser usado como contexto.

        Los archivos deben estar en una carpeta llamada 'Docu' en el directorio actual.
        """
        context_dir = Path.cwd() / "Docu"
        context_data = []

        if not context_dir.exists():
            raise FileNotFoundError("La carpeta 'Docu' no existe en el directorio actual.")

        for file in context_dir.glob("*.md"):
            with file.open(encoding="utf-8") as f:
                context_data.append(f.read())

        return "\n\n".join(context_data)
    
    def _load_glossary(self) -> str:
        """
        Carga el contenido del archivo glosario.md como texto plano.
        
        Returns:
            str: Contenido del glosario.
        """
        glossary_path = Path.cwd() / "glosario.md"

        if not glossary_path.exists():
            raise FileNotFoundError("El archivo 'glosario.md' no existe en el directorio actual.")

        with glossary_path.open(encoding="utf-8") as f:
            return f.read()

    def _load_history_context(self) -> str:
        """
        Carga el contenido del archivo 'Historia_de_las_ciencias_de_la_computación.md'.
        Returns:
            str: Contenido del archivo.
        """
        history_path = Path.cwd() / "Historia_de_las_ciencias_de_la_computacion.md"
        if not history_path.exists():
            raise FileNotFoundError("El archivo 'Historia_de_las_ciencias_de_la_computación.md' no existe.")
        
        with history_path.open(encoding="utf-8") as f:
            return f.read()
    
    def _load_exercise_context(self) -> str:
        """
        Carga el contenido de los archivos .md en la carpeta 'Ejercicios' como contexto para evaluar problemas.
        
        Returns:
            str: Contexto combinado de todos los archivos en la carpeta 'Ejercicios'.
        """
        exercise_dir = Path.cwd() / "Ejercicios"
        exercise_data = []

        if not exercise_dir.exists():
            raise FileNotFoundError("La carpeta 'Ejercicios' no existe en el directorio actual.")

        for file in exercise_dir.glob("*.md"):
            with file.open(encoding="utf-8") as f:
                exercise_data.append(f.read())

        return "\n\n".join(exercise_data)

    def analyze_context(self, previous_question: str, current_question: str) -> str:
       """
       Analiza el contexto entre la pregunta anterior y la actual para determinar si están relacionadas.
       
       Args:
           previous_question (str): La pregunta anterior realizada por el usuario.
           current_question (str): La pregunta actual realizada por el usuario.
       
       Returns:
           str: Una pregunta autónoma que incorpora el contexto esencial si es necesario.
       """
       completion = self.client.chat.completions.create(
           model="llama-3.3-70b-versatile",
           messages=[
               {"role": "user", "content": self.TEMPLATE_CONTEXT_ANALYSIS.format(
                   previous_question=previous_question,
                   current_question=current_question
               )}
           ],
           temperature=0.1,
           max_completion_tokens=256,
           top_p=1,
           stream=False,
       )
       
       # Retornar la pregunta analizada
       return completion.choices[0].message.content.strip()

    def answer_question(self, user_input: str) -> str:
        # Analizar contexto si hay una pregunta anterior.
        if self.prev_question:
            user_input = self.analyze_context(self.prev_question, user_input)
        
        # Procesar la respuesta.
        completion = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "user",
                "content": self.TEMPLATE_ANSWER.format(
                    history_context=self.history_context,
                    context=self.context,
                    user_input=user_input)}
            ],
            temperature=0.1,
            max_completion_tokens=1024,
            top_p=1,
            stream=False,
            stop=None,
        )
        
        response = completion.choices[0].message.content.strip()
        
        # Actualizar prev_question con la pregunta actual.
        self.prev_question = user_input
        
        return response



    def evaluate_problem(self, problem_statement: str, user_solution: str) -> str:
        """
        Evalúa un problema y la solución proporcionada por el usuario.
        Args:
            problem_statement (str): Enunciado del problema.
            user_solution (str): Solución completa proporcionada por el usuario.
        Returns:
            str: Feedback detallado sobre los pasos correctos e incorrectos.
        """

        # Generar la retroalimentación usando el modelo
        completion = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": self.TEMPLATE_PROBLEM.format(
                context2=self.context2,
                problem_statement=problem_statement,
                user_solution=user_solution,
                glossary=self.glossary
                
            )}],
            temperature=0.1,
            max_completion_tokens=1024,
            top_p=1,
            stream=False,
            stop=None,
        )

        return completion.choices[0].message.content.strip()
