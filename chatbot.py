import os
from dotenv import load_dotenv
from groq import Groq
from RAG import query_qdrant  

class GrammarAutomataProcessor:
    def __init__(self):
        # Cargamos variables de entorno
        load_dotenv(override=True)

        # Inicializamos las colecciones en Qdrant
        self.exercise_collection = "exercise_vectors"
        self.documentation_collection = "documentation_vectors"

        # Almacena la pregunta anterior
        self.prev_question = None

        # Inicializamos el modelo Llama 3.3 en Groq
        self.client = self._initialize_groq()

        # Plantilla de prompt para responder preguntas
        self.TEMPLATE_ANSWER = """
        You are an expert in the subject of Regular Grammars, Context-Free Grammars, and Finite Automata.
        Always answer in Sapnish.
        Context from files: {context_docu}

        User Question: {user_input}

        Ensure that:
        - The answer is directly derived from the context.
        - Technical terms are preserved exactly as they appear in the context.
        - The answer is clear, precise, and actionable.
        - Avoid unnecessary repetition.
        - If the user asks about a term (e.g., "What is an AP?" or "Define what a MT is" or "Explain APV"), provide a detailed explanation of the term based on the context.

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
        - AFD stands for: Autómatas Finitos Deterministas
        - AFND stands for: Autómatas Finitos No Deterministas
        - LR stands for: Lenguaje Regular  
        - G0 stands for: Gramática sin restricciones
        - G1 stands for: Gramática sensible al contexto  
        - ERD stands for: Expresión Regular Determinista
        2. Do not use abbreviations in your response.

        Answer:
        """

        # Plantilla para evaluar problemas
        self.TEMPLATE_PROBLEM = """
        You are a virtual tutor specializing in Regular Grammars, Context-Free Grammars, and Finite Automata.
        Always answer in Spanish.
        Context from Exercises:
        {context_exercises}

        Problem Statement:
        {problem_statement}

        User Solution:
        {user_solution}

        Instructions:
        1. Evaluate the user's solution to the given problem statement step by step.
        2. Use the provided context as a guide to identify any errors and explain where the user went wrong.
        3. Provide hints or guidance to help the user correct their mistakes without directly giving the solution.
        4. If the solution is correct, confirm it and explain why it works.
        5. Avoid unnecessary repetition.

        Feedback:
        """

        # Plantilla para analizar contexto entre preguntas
        self.TEMPLATE_CONTEXT_ANALYSIS = """
        Determine if the current question is self-contained and complete.
        
        If the current question does not contain ambiguous references (such as pronouns or terms like "este" o "eso") and is fully understandable on its own, output the current question exactly as provided.
        
        If the current question is ambiguous or incomplete, incorporate only the minimal essential context from the previous question to remove that ambiguity.
        
        Previous Question: {previous_question}
        
        Current Question: {current_question}
        
        Important:
        - Only include context that is absolutely necessary to clarify ambiguous references in the current question.
        - If the current question is fully self-contained, do not add any context from the previous question.
        - Do not include any explanation, analysis, or any additional information in the output.

        Output:
        A single, standalone question that incorporates additional context only if needed; otherwise, output the current question unchanged.
        """

    def _initialize_groq(self):
        """
        Inicializa el cliente Groq con la clave API desde las variables de entorno.
        """
        return Groq(api_key=os.getenv("GROQ_API_KEY"))
        
    def analyze_context(self, previous_question: str, current_question: str) -> str:
        """
        Analiza si la pregunta actual necesita contexto de la pregunta anterior para ser comprensible.

        Args:
            previous_question (str): La pregunta anterior realizada por el usuario.
            current_question (str): La pregunta actual realizada por el usuario.

        Returns:
            str: Una pregunta autónoma que incluye contexto adicional si es necesario.
        """
        if not previous_question:
            # Si no hay pregunta anterior, devolvemos la pregunta actual sin cambios
            return current_question

        # Generamos el prompt para analizar el contexto
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
            stop=None,
        )

        # Retornamos la pregunta autónoma generada
        return completion.choices[0].message.content.strip()
    
    def answer_question(self, user_input: str) -> dict:
        """
        Responde preguntas del usuario utilizando contexto recuperado desde Qdrant.

        Args:
            user_input (str): Pregunta realizada por el usuario.

        Returns:
            dict: Diccionario con la respuesta generada y el nombre del archivo relevante.
        """
        # Analizamos si es necesario incorporar contexto de la pregunta anterior
        standalone_question = self.analyze_context(self.prev_question, user_input)

        # Recuperar el documento más relevante desde la colección de documentación en Qdrant
        best_doc = query_qdrant(self.documentation_collection, standalone_question)

        # Si no se encuentra información relevante en Qdrant, devolvemos un mensaje predeterminado
        if not best_doc:
            return {"response": "No se encontró información relevante en la base de datos.", "source_file": None}

        # Construimos el contexto basado únicamente en el contenido del documento más relevante
        context_docs = best_doc["content"]

        # Generamos la respuesta utilizando el modelo Llama 3.3
        completion = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "user", "content": self.TEMPLATE_ANSWER.format(
                    context_docu=context_docs,
                    user_input=standalone_question,
                    glossary=self.glossary
                )}
            ],
            temperature=0.1,
            max_completion_tokens=1024,
            top_p=1,
            stream=False,
            stop=None,
        )

        response = completion.choices[0].message.content.strip()

        # Actualizamos la pregunta anterior con la pregunta actual
        self.prev_question = user_input

        # Retornamos tanto la respuesta generada como el nombre del archivo relevante
        return {"response": response, "source_file": best_doc["source_file"]}
    
    def evaluate_problem(self, problem_statement: str, user_solution: str) -> dict:
        """
        Evalúa un problema y la solución proporcionada por el usuario utilizando contexto recuperado desde Qdrant.

        Args:
            problem_statement (str): Enunciado del problema.
            user_solution (str): Solución completa proporcionada por el usuario.

        Returns:
            dict: Diccionario con el feedback generado y el nombre del archivo relevante.
        """
        # Recuperar el documento más relevante desde la colección de ejercicios en Qdrant
        best_exercise = query_qdrant(self.exercise_collection, problem_statement)

        # Si no se encuentra información relevante en Qdrant, devolvemos un mensaje predeterminado
        if not best_exercise:
            return {"response": "No se encontró información relevante en la base de datos.", "source_file": None}

        # Construimos el contexto basado únicamente en el contenido del ejercicio más relevante
        context_exercises = best_exercise["content"]

        # Generamos el feedback utilizando el modelo Llama 3.3
        completion = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "user", "content": self.TEMPLATE_PROBLEM.format(
                    context_exercises=context_exercises,
                    problem_statement=problem_statement,
                    user_solution=user_solution
                )}
            ],
            temperature=0.1,
            max_completion_tokens=1024,
            top_p=1,
            stream=False,
            stop=None,
        )
        response = completion.choices[0].message.content.strip()

        # Retornamos tanto la respuesta generada como el nombre del archivo relevante
        return {"response": response, "source_file": best_exercise["source_file"]}

