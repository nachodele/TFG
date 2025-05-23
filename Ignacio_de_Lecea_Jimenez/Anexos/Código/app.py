import streamlit as st
from chatbot import GrammarAutomataProcessor
from PIL import Image
import pandas as pd

# CSS personalizado para botones y área general
st.markdown("""
    <style>
    .main {
        background-color: #f7f9fa;
    }
    .stButton > button {
        background-color: #4F8BF9;
        color: white;
        border-radius: 8px;
        height: 48px;
        font-size: 18px;
        font-weight: 600;
        margin: 8px 0px;
        width: 100% !important;
    }
    .stButton > button:hover {
        background-color: #3761c2;
        color: #fff;
    }
    .stTextArea textarea {
        border-radius: 8px;
        font-size: 16px;
    }
    .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# Inicializar el procesador con estado persistente
@st.cache_resource
def get_processor():
    return GrammarAutomataProcessor()

processor = get_processor()

# Variables de sesión
for key in ["prev_question", "consulta_text", "problema_text", "solucion_text"]:
    if key not in st.session_state:
        st.session_state[key] = "" if "text" in key else None

def insertar_contenido(contenido, campo):
    st.session_state[f"{campo}_text"] += contenido

def generar_tabla(filas, columnas):
    tabla = "| " + " | ".join([f"Columna {i+1}" for i in range(columnas)]) + " |\n"
    tabla += "|" + "|".join(["-----" for _ in range(columnas)]) + "|\n"
    for _ in range(filas):
        tabla += "| " + " | ".join([" " for _ in range(columnas)]) + " |\n"
    return tabla

st.title("📚 FLUXO")

option = st.selectbox(
    "Seleccione el tipo de consulta:",
    ("Consulta de Documentación", "Asistente Virtual")
)

st.markdown("---")

# Herramientas de edición
st.header("🛠️ Herramientas de escritura")
col1, col2 = st.columns(2)

with col1:
    with st.expander("Glosario de Símbolos Matemáticos"):
        try:
            df = pd.read_csv("glosario.csv")
            st.dataframe(df, height=220, use_container_width=True, hide_index=True)
        except FileNotFoundError:
            st.error("Error: No se encontró el archivo glosario.csv")
        except Exception as e:
            st.error(f"Error al cargar el glosario: {str(e)}")


with col2:
    if option == "Asistente Virtual":
        st.subheader("Generador de Tablas")
        filas, columnas = st.columns(2)
        with filas:
            n_filas = st.number_input("Filas", min_value=1, max_value=20, value=3)
        with columnas:
            n_columnas = st.number_input("Columnas", min_value=1, max_value=10, value=3)
        st.markdown("¿Dónde insertar la tabla?")
        bcol1, bcol2 = st.columns(2)
        with bcol1:
            if st.button("Insertar en Enunciado"):
                tabla_generada = generar_tabla(n_filas, n_columnas)
                insertar_contenido(tabla_generada, "problema")
        with bcol2:
            if st.button("Insertar en Solución"):
                tabla_generada = generar_tabla(n_filas, n_columnas)
                insertar_contenido(tabla_generada, "solucion")

st.markdown("---")

# Funcionalidad 1
if option == "Consulta de Documentación":
    st.subheader("Consulta de Documentación")
    user_input = st.text_area("Ingrese su consulta:", height=100, key="consulta", value=st.session_state["consulta_text"])
    st.session_state["consulta_text"] = user_input
    if st.button("Procesar Consulta"):
        if user_input:
            with st.spinner("Analizando y procesando..."):
                result = processor.answer_question(user_input)
                response = result["response"]
                source_files = result["source_files"]
            # En la sección de Consulta de Documentación:
            if source_files:
                st.write("Archivos fuente:")
                for file in source_files:
                    st.write(f"- {file}")

            st.write(f"Respuesta:\n\n{response}")
        else:
            st.warning("Por favor, ingrese una consulta para procesar.")

# Funcionalidad 2
elif option == "Asistente Virtual":
    st.subheader("Asistente Virtual")
    problem_statement = st.text_area("Ingrese el enunciado del problema:", height=200, key="problema", value=st.session_state["problema_text"])
    st.session_state["problema_text"] = problem_statement
    user_solution = st.text_area("Ingrese su solución completa:", height=200, key="solucion", value=st.session_state["solucion_text"])
    st.session_state["solucion_text"] = user_solution
    if st.button("Evaluar Solución"):
        if problem_statement and user_solution:
            with st.spinner("Evaluando la solución..."):
                result = processor.evaluate_problem(problem_statement, user_solution)
                response = result["response"]
                source_files = result["source_files"]
            if source_files:
                st.write("Archivos fuente:")
                for file in source_files:
                    st.write(f"- {file}")
            st.write(f"Feedback:\n\n{response}")
        else:
            st.warning("Por favor, ingrese tanto el enunciado como la solución.")

# Sidebar
image = Image.open("ufv.png")
st.sidebar.image(image, use_container_width=True)
st.sidebar.markdown("""
## Acerca de esta herramienta
- Proyecto: Asistente Virtual
- Profesor: Juan José Escribano
- Autor: Ignacio de Lecea Jiménez
- Fecha: 2024/2025
- Estado: En desarrollo

Esta herramienta permite analizar consultas relacionadas con gramáticas regulares, gramáticas independientes de contexto y autómatas finitos.

También proporciona el servicio de un tutor virtual que te ayude a resolver problemas relacionados con esta materia.

Utiliza un modelo avanzado para reformular preguntas y proporcionar respuestas concisas basadas en el contexto.
""")
