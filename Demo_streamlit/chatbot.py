import os
from dotenv import load_dotenv
from groq import Groq
from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient
from qdrant_client import models  # Asegúrate de tener esta importación


class GrammarAutomataProcessor:
    def __init__(self):
        # Cargamos variables de entorno
        load_dotenv(override=True)
        
        # Inicializamos las colecciones en Qdrant
        self.exercise_collection = "exercise_vectors"
        self.documentation_collection = "documentation_vectors"
        self.algorithm_collection = "algorithm_vectors"

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
2. Do not include abbreviations in your answer.

Answer:
"""

        # Plantilla para evaluar problemas
        self.TEMPLATE_PROBLEM = """
You are a virtual tutor specializing in Regular Grammars, Context-Free Grammars, and Finite Automata.
Always answer in Spanish.

Reference exercises:
{context_exercises}

Reference Algorithm:
{context_algorithm}

Problem Statement:
{problem_statement}

User Solution:
{user_solution}

Evaluation Instructions:
Step-by-step analysis:
1. Break down the user's solution into clearly identifiable steps.
2. Compare each step with the procedure described in the reference algorithm.
3. Explicitly classify each step as "correct" or "incorrect", avoiding ambiguity in your evaluations.
4. Use the reference exercises as a guide to identify any errors.
5. For each incorrect step:
    * Explain why it does not follow the standard procedure.
    * Clearly indicate where the deviation occurs.
    * Provide a counterexample or relevant theoretical reference if possible.
    * Offer specific hints or suggestions to help the user correct the erroneous step.
6. Do not provide complete solutions or rewrite the entire answer.  
7. If the solution is correct, confirm it and explain why it works.

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

        self.client2 = QdrantClient(
            url=os.getenv("QDRANT_URL"),
            api_key=os.getenv("QDRANT_API_KEY")
        )


    # Modificar la sección de query_qdrant
    def query_qdrant(self, collection_name, question, search_type="default"):
        model = SentenceTransformer('all-MiniLM-L6-v2')
        query_vector = model.encode(question)
        
        # Configurar parámetros de búsqueda según el tipo
        if search_type == "algorithm":
            search_params = models.SearchParams(
                hnsw_ef=128,
                exact=False
            )
        else:
            search_params = None  # Usar parámetros por defecto
        
        search_results = self.client2.search(
            collection_name=collection_name,
            query_vector=query_vector,
            query_filter=None,  # Añadir si necesitas filtros
            search_params=search_params,  # Parámetro correcto
            limit=3
        )

        
        if not search_results:
            return None
            
        return [{
            "content": result.payload["metadata"]["content"],
            "source_file": result.payload.get("source_file", "Desconocido"),
            "algorithm_type": result.payload.get("algorithm_type", None)
        } for result in search_results]

    def _initialize_groq(self):
        """Inicializa el cliente Groq con la clave API desde las variables de entorno."""
        return Groq(api_key=os.getenv("GROQ_API_KEY"))

    def analyze_context(self, previous_question: str, current_question: str) -> str:
        """Analiza si la pregunta actual necesita contexto de la pregunta anterior para ser comprensible."""
        if not previous_question:
            return current_question
            
        completion = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{
                "role": "user",
                "content": self.TEMPLATE_CONTEXT_ANALYSIS.format(
                    previous_question=previous_question,
                    current_question=current_question
                )
            }],
            temperature=0.1,
            max_completion_tokens=256,
            top_p=1,
            stream=False,
            stop=None,
        )
        return completion.choices[0].message.content.strip()

    def answer_question(self, user_input: str) -> dict:
        """Responde preguntas del usuario utilizando contexto recuperado desde Qdrant."""
        standalone_question = self.analyze_context(self.prev_question, user_input)
        docs = self.query_qdrant(self.documentation_collection, standalone_question)
        
        if not docs:
            return {"response": "No se encontró información relevante.", "source_files": []}
        
        # Combina contenido de los 3 documentos
        context_docs = "\n\n".join(doc["content"] for doc in docs)
        source_files = list({doc["source_file"] for doc in docs})  

        completion = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{
                "role": "user",
                "content": self.TEMPLATE_ANSWER.format(
                    context_docu=context_docs,
                    user_input=standalone_question,
                )
            }],
            temperature=0.1,
            max_completion_tokens=1024,
            top_p=1,
            stream=False,
            stop=None,
        )
        
        self.prev_question = user_input
        return {
            "response": completion.choices[0].message.content.strip(),
            "source_files": source_files
        }
    
    def evaluate_problem(self, problem_statement: str, user_solution: str) -> dict:
        """Evalúa un problema y la solución proporcionada por el usuario."""
        exercises  = self.query_qdrant(self.exercise_collection, problem_statement)
        
        # Obtener algoritmos relevantes
        algorithms = self.query_qdrant(
            self.algorithm_collection, 
            problem_statement,
            search_type="algorithm"
        )

        if not exercises and not algorithms:
            return {"response": "No se encontró información relevante.", "source_files": []}
        
        context_exercises = "\n\n".join(ex["content"] for ex in exercises)
        context_algorithms = "\n\n".join(
            f"Algoritmo para {alg['algorithm_type']}:\n{alg['content']}" 
            for alg in algorithms
        )
        
        # Obtener nombres de archivos únicos
        source_files = list({
            doc["source_file"] 
            for doc in exercises + algorithms
            if doc["source_file"]
        })

        completion = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            #model="meta-llama/llama-4-maverick-17b-128e-instruct",
            messages=[{
                "role": "user",
                "content": self.TEMPLATE_PROBLEM.format(
                    context_exercises=context_exercises,
                    context_algorithm=context_algorithms,
                    problem_statement=problem_statement,
                    user_solution=user_solution
                )
            }],
            temperature=0.1,
            max_completion_tokens=1024,
            top_p=1,
            stream=False,
            stop=None,
        )
        
        return {
            "response": completion.choices[0].message.content.strip(),
            "source_files": source_files
        }