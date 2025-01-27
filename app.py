import streamlit as st
from chatbot import GrammarAutomataProcessor 
from PIL import Image  # Para cargar imágenes

# Inicializar la clase GrammarAutomataProcessor
@st.cache_resource
def get_processor():
    return GrammarAutomataProcessor()

processor = get_processor()

st.title("Gramáticas regulares e independientes de contexto y autómatas finitos.")

# Inicializar estado de sesión para almacenar contexto
if 'previous_input' not in st.session_state:
    st.session_state.previous_input = ""

# Entrada del usuario
user_input = st.text_area("Ingrese su consulta:", height=100)

if st.button("Procesar Consulta"):
    if user_input:
        with st.spinner("Analizando y procesando..."):
            # Reformular la entrada del usuario en base al contexto
            reformulated_output = processor.answer_question(user_input)

            # Actualizar estado de sesión
            st.session_state.previous_input = user_input

        st.success("Consulta procesada exitosamente!")
        st.write(f"**Respuesta:**\n\n{reformulated_output}")
    else:
        st.warning("Por favor, ingrese una consulta para procesar.")

# Cargar y mostrar la imagen encima del sidebar

image = Image.open("ufv.png")  
st.sidebar.image(image, use_container_width=True)  


# Barra lateral con información adicional
st.sidebar.markdown("""
## Acerca de esta herramienta
- **Proyecto:** CHATBOT de Gramáticas y Autómatas
- **Profesor:** Juan José Escribano
- **Autor:** Ignacio de Lecea Jiménez
- **Fecha:** 2024/2025
- **Estado:** En desarrollo

Esta herramienta permite analizar consultas relacionadas con gramáticas regulares, gramáticas independientes de contexto y autómatas finitos.
Utiliza un modelo avanzado para reformular preguntas y proporcionar respuestas concisas basadas en el contexto.
""")
