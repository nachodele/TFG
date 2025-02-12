import streamlit as st
from chatbot import GrammarAutomataProcessor 
from PIL import Image  # Para cargar imágenes


# Inicializar el procesador con estado persistente
@st.cache_resource
def get_processor():
    return GrammarAutomataProcessor()

processor = get_processor()

# Variable de sesión para almacenar la pregunta anterior
if "prev_question" not in st.session_state:
    st.session_state["prev_question"] = None

st.title("Gramáticas regulares e independientes de contexto y autómatas finitos.")

option = st.selectbox(
    "Seleccione el tipo de consulta:",
    ("Consulta de Documentación", "Tutor Virtual")
)

if option == "Consulta de Documentación":
    user_input = st.text_area("Ingrese su consulta:", height=100)
    if st.button("Procesar Consulta"):
        if user_input:
            with st.spinner("Analizando y procesando..."):
                # Llamar al método sin pasar 'prev_question'
                response = processor.answer_question(user_input)
                st.success("Consulta procesada exitosamente!")
                st.write(f"**Respuesta:**\n\n{response}")

        else:
            st.warning("Por favor, ingrese una consulta para procesar.")


# Funcionalidad 2: Tutor Virtual
elif option == "Tutor Virtual":
    problem_statement = st.text_area("Ingrese el enunciado del problema:", height=300)
    user_solution = st.text_area("Ingrese su solución completa:", height=300)
    
    if st.button("Evaluar Solución"):
        if problem_statement and user_solution:
            with st.spinner("Evaluando la solución..."):
                feedback = processor.evaluate_problem(problem_statement, user_solution)
            st.success("Evaluación completada!")
            st.write(f"**Feedback:**\n\n{feedback}")
        else:
            st.warning("Por favor, ingrese tanto el enunciado como la solución.")


# Cargar y mostrar la imagen encima del sidebar

image = Image.open("ufv.png")  
st.sidebar.image(image, use_container_width=True)  


# Barra lateral con información adicional
st.sidebar.markdown("""
## Acerca de esta herramienta
- **Proyecto:** CHATBOT para JFLAP
- **Profesor:** Juan José Escribano
- **Autor:** Ignacio de Lecea Jiménez
- **Fecha:** 2024/2025
- **Estado:** En desarrollo

Esta herramienta permite analizar consultas relacionadas con gramáticas regulares, gramáticas independientes de contexto y autómatas finitos.
También proporciona el servicio de un tutor virtual que te ayude a resolver problemas relacionados con esta materia.
Utiliza un modelo avanzado para reformular preguntas y proporcionar respuestas concisas basadas en el contexto.
""")
