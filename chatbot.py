import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

class GrammarAutomataProcessor:
    def __init__(self):
        # Cargamos variables de entorno
        load_dotenv(override=True)

        # Cargamos la base de datos
        self.context = self._load_context()

        # Inicializamos el modelo Llama 3.3 en Groq
        self.client = self._initialize_groq()

        # Plantilla de prompt para responder preguntas
        self.TEMPLATE_ANSWER = """
        You are an expert in the subject of Regular Grammars, Context-Free Grammars, and Finite Automata.
        Respond only with information related to this subject, relying on the provided context.

        Critical Instructions:
        - GIC stands for: Gramática Independiente de Contexto
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


        Context from files:
        {context}

        User Question: {user_input}

        Based on the provided context, answer the user's question as accurately and concisely as possible. Ensure that:
        1. If the user asks about a term (e.g., "What is an AP?" or "Define what a MT is" or "Explain APV"), provide a detailed explanation of the term based on the context.
        2. The answer is directly derived from the context.
        3. Technical terms are preserved exactly as they appear.
        4. The answer is clear and actionable.

        Answer:
        """

    def _initialize_groq(self):
        """
        Inicializa el cliente Groq con la clave API desde las variables de entorno.
        """
        return Groq(api_key=os.getenv("GROQ_API_KEY"))

    def _load_context(self):
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

    def answer_question(self, user_input: str) -> str:
        """
        Responde a la pregunta del usuario basándose en el contenido cargado desde los archivos .md.
        
        Args:
            user_input (str): Pregunta del usuario.
        
        Returns:
            str: Respuesta generada por el modelo.
        """
        completion = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "user", "content": self.TEMPLATE_ANSWER.format(
                    context=self.context,
                    user_input=user_input
                )}
            ],
            temperature=0.1,
            max_completion_tokens=1024,
            top_p=1,
            stream=False,
            stop=None,
        )
        
        # Acceder al contenido correctamente
        return completion.choices[0].message.content.strip()
