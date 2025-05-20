import os
from dotenv import load_dotenv
from groq import Groq
from sentence_transformers import SentenceTransformer, CrossEncoder
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
# 1.Break down the solution into clearly identifiable steps.
# 2. Validation by categories
 ## 2.1 Step-by-step procedure
- Compare each step with the procedure described in the reference algorithm and exercises.
- Ensure the solution follows the correct sequence and logic
 ## 2.2 Rules and Productions
 ### Grammar Type Validation:
    1. Regular Grammar (RG) Requirements:
    * Valid forms ONLY:
        - A → aB (one terminal followed by one non-terminal)
        - A → a (single terminal)
        - A → λ (empty string, only when necessary)
    * Invalid forms (flag immediately):
        - Unit productions (A → B, where B is non-terminal)
        - Multiple terminals (A → ab)
        - Multiple non-terminals (A → BC)
        - Mixed terminals with wrong order (A → Ba)
        - Any right side with more than 2 symbols
    2. Common Regular Grammar Errors (flag immediately):
    * Example error: T → aT | bT | V (where V → a), S → T
        - This are unit productions (non-terminal to non-terminal) and must be replaced
    * Example error: S → AB
        - Multiple non-terminals are not allowed
        - Must be rewritten as S → aX where X produces remaining part
    3. Chomsky Normal Form (CNF) Requirements:
    * Valid forms ONLY:
        - A → BC (exactly two non-terminals)
        - A → a (exactly one terminal)
        - S → λ (only for start symbol if λ ∈ L(G))
    * Invalid forms (flag immediately):
        - Any mix of terminals and non-terminals (A → aB, S → bC)
        - More than two symbols (A → BCD)
        - Unit productions (A → B)
    4. Greibach Normal Form (GNF) Requirements: Grammar must first be "clean" (no useless symbols, no unreachable productions)
    * Valid forms ONLY:
     - A → aα (one terminal followed by zero or more non-terminals)
     - Where α represents any sequence of non-terminals (including empty)
    * Invalid forms (flag immediately):
     - Rules starting with non-terminals (A → Bα)
     - Rules with no terminals (A → B)
     - Multiple terminals at beginning (A → abα)
* Before applying the CYK algorithm, verify if the problem statement grammar is in CNF
* For CNF: Ensure all rules are `A → BC`,`A → a`, or `S → λ`
* Always check recursion in Derivation trees ensuring it is in CNF.
### **Recursion analysis: When cleaning a grammar always check for recursion**
  * **Detection:**
    - Direct recursion: Rules of the form X → Xα (e.g., S → Sa)
    - Indirect recursion: Derivation chains like X → Yα → ... → Xβ (e.g., S → A, A → S)
    - If a single-non-terminal grammar allows two-level trees, it must contain recursion.
  * **Consequences:**
    - With recursion: Infinite language
    - Without recursion: Finite language
  * **Left recursion elimination:**
    - Order non-terminals
    - Replace indirect dependencies. Example: `C → SaaB` becomes `C → abS'SaaB` after processing `S → abS'`.
    - Eliminate direct recursion with appropriate transformations
 ## 2.3 Transition tables (for automata)
- Verify completeness (all states and symbols covered)
- Check determinism (for DFAs)
- Look for missing or ambiguous transitions
 ## 2.4 Validate grammar cleaning process:
   ### a) Critical generative test:
    - Correct initialization: Verify Σ_N' starts only with non-terminals that directly derive terminals
    - Rigorous iterative process: Verify each step adds only non-terminals whose productions derive completely to terminals or to non-terminals already in Σ_N'
    - Infinite recursion detection:
        * Critical alert: Identify non-terminals like B → aB without alternative rules
        * Critical alert: Identify cycles like A → BC, B → AD (no derivation to terminals exists)
    - Complete application: Every non-terminal not included in the final Σ_N' is NON-generative
    - Mandatory elimination: All rules containing non-generative symbols MUST be eliminated
   ### b) Verify proper application of algorithms in sequence:
      1. Remove all non-generative symbols and their productions
      2. Remove unreachable productions
      3. Eliminate λ-productions
      4. Eliminate unit productions
   ### c) Critical errors to detect:
    - False generatives: Non-terminal marked as generative when it is not
    - False nullables: Non-terminal incorrectly marked as nullable
    - Missing productions: Not generating all necessary combinations when removing λ-productions
    - Excess productions: Adding productions that do not correspond to the algorithm
## 2.5 Additional checks
- Confirm correct use of formal definitions and terminology
- Verify handling of edge cases (empty strings, unreachable states, invalid symbols)
 ## 2.6 Semantic Validation of Language Properties:
    a) Always verify if a language satisfies the pumping lemma, if it does not no context-free grammar (CFG) can generate it
    b) Match Grammar to Language Constraints:
    - Verify the grammar enforces all stated conditions (e.g., m ≥ n, symbol ordering)
    - Each non-terminal should have a clear purpose in maintaining these constraints
    c) Test with Examples and Counterexamples:
    - Confirm the grammar generates all valid strings
    - Verify the grammar rejects invalid strings
    - Pay special attention to boundary cases (e.g., equal counts, minimum lengths)
    d) Common Errors to Flag:
    - Grammar that generates strings outside the language definition
    - Missing constraints
    - Production rules that allow constraint violations (e.g., premature termination)
# 3. Classify each step as "correct" or "incorrect", avoiding ambiguity
# 4. Feedback for incorrect steps
- Explain why it doesn't follow the standard procedure
- Clearly indicate where the deviation occurs
- Provide a counterexample or theoretical reference when possible
- Offer specific suggestions to correct the error
- Do not be redundant
# 5. Do not provide complete solutions or rewrite the entire answer
# 6. If the solution is correct, confirm it and explain why it works
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

    def rerank_results(self, question, docs):
        cross_encoder = CrossEncoder('cross-encoder/ms-marco-MiniLM-L-6-v2')
        pairs = [[question, doc['content']] for doc in docs]
        scores = cross_encoder.predict(pairs)
        for doc, score in zip(docs, scores):
            doc['score'] = float(score)
        docs.sort(key=lambda x: x['score'], reverse=True)
        return docs


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
        docs = self.rerank_results(standalone_question, docs)
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
        # Recuperar documentos
        exercises = self.query_qdrant(self.exercise_collection, problem_statement)
        algorithms = self.query_qdrant(
            self.algorithm_collection, 
            problem_statement,
            search_type="algorithm"
        )
        
        all_docs = exercises + algorithms
        if not all_docs:
            return {"response": "No se encontró información relevante.", "source_files": []}
        
        # Paso crítico: Rerank de documentos combinados
        reranked_docs = self.rerank_results(problem_statement, all_docs)
        
        # Separar en ejercicios y algoritmos después del rerank
        context_exercises = "\n\n".join(doc["content"] for doc in reranked_docs if 'algorithm_type' not in doc)
        context_algorithms = "\n\n".join(
            f"Algoritmo para {doc['algorithm_type']}:\n{doc['content']}" 
            for doc in reranked_docs if 'algorithm_type' in doc
        )
        
        # Obtener nombres de archivos únicos de documentos rerankeados
        source_files = list({
            doc["source_file"] 
            for doc in reranked_docs 
            if doc.get("source_file")
        })
        
        completion = self.client.chat.completions.create(
            model="meta-llama/llama-4-maverick-17b-128e-instruct",
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
        
        