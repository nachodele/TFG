from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance
import json
import numpy as np
from sentence_transformers import SentenceTransformer
import os
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Inicializa el cliente con URL y clave API desde variables de entorno
client = QdrantClient(
    url=os.getenv("QDRANT_URL"),  # URL del clúster
    api_key=os.getenv("QDRANT_API_KEY")  # Clave API
)

# Nombres de las colecciones en Qdrant
exercise_collection_name = "exercise_vectors"
documentation_collection_name = "documentation_vectors"

# Creación de una colección en Qdrant (si no existe)
def create_collection(collection_name):
    if not client.collection_exists(collection_name):
        client.create_collection(
            collection_name=collection_name,
            vectors_config=VectorParams(size=384, distance=Distance.COSINE)  # Ajusta el tamaño según tus embeddings
        )

# Carga y subida de vectores a una colección específica en Qdrant
def load_and_upload_vectors(json_folder_path, collection_name):
    model = SentenceTransformer('all-MiniLM-L6-v2')  # Modelo para generar embeddings
    vectors = []
    payloads = []

    # Procesa cada archivo JSON en la carpeta especificada
    for json_file in os.listdir(json_folder_path):
        if json_file.endswith(".json"):
            with open(os.path.join(json_folder_path, json_file)) as f:
                data = json.load(f)
                for item in data:
                    text = item["content"]  # Ajusta según la estructura de tu JSON
                    vector = model.encode(text)
                    vectors.append(vector)
                    # Incluye el nombre del archivo en el payload
                    payloads.append({
                        "id": item["id"],
                        "metadata": item,
                        "source_file": json_file  # Agrega el nombre del archivo como parte del payload
                    })

    vectors = np.array(vectors)

    # Subida de datos a Qdrant
    client.upload_collection(
        collection_name=collection_name,
        vectors=vectors,
        payload=payloads,
        ids=None,
        batch_size=256  # Número máximo de puntos por lote
    )
    
def query_qdrant(collection_name, question):
    model = SentenceTransformer('all-MiniLM-L6-v2')  # Modelo para vectorizar la consulta
    query_vector = model.encode(question)  # Vectoriza tu consulta

    # Realiza la búsqueda en Qdrant
    search_results = client.search(
        collection_name=collection_name,
        query_vector=query_vector,
        limit=5  # Recupera los 5 resultados más relevantes
    )

    # Si no hay resultados, devuelve None
    if not search_results:
        return None

    # Selecciona el resultado con mayor puntuación
    best_result = max(search_results, key=lambda x: x.score)

    # Devuelve el contenido y el archivo del resultado más relevante
    return {
        "content": best_result.payload["metadata"]["content"],
        "source_file": best_result.payload.get("source_file", "Desconocido")
    }


if __name__ == "__main__":
    # Eliminar colecciones existentes (si ya existen)
    client.delete_collection(exercise_collection_name)
    client.delete_collection(documentation_collection_name)

    # Crear colecciones nuevamente
    create_collection(exercise_collection_name)
    create_collection(documentation_collection_name)

    # Cargar y subir vectores a las colecciones
    load_and_upload_vectors("./vectors", exercise_collection_name)  # Ruta a la carpeta con los archivos JSON de ejercicios
    load_and_upload_vectors("./vectors_docu", documentation_collection_name)  # Ruta a la carpeta con los archivos JSON de documentación
