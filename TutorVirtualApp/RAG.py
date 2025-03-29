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
