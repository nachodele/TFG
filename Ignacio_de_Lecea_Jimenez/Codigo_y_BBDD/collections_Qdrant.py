from qdrant_client import QdrantClient, models
from qdrant_client.models import VectorParams, Distance
import json
import numpy as np
from sentence_transformers import SentenceTransformer
import os
from dotenv import load_dotenv
import logging
from tenacity import retry, stop_after_attempt, wait_exponential, before_log
from uuid import uuid4


# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Cargar variables de entorno
load_dotenv()

# Configuración avanzada del cliente
def create_qdrant_client():
    return QdrantClient(
        url=os.getenv("QDRANT_URL"),
        api_key=os.getenv("QDRANT_API_KEY"),
        https=True,
        timeout=10  # Reactiva timeout con valor adecuado
    )


client = create_qdrant_client()

# Nombres de colecciones
COLLECTIONS = {
    "exercise": "exercise_vectors",
    "documentation": "documentation_vectors",
    "algorithm": "algorithm_vectors"
}

# Verificación de conexión
def verify_connection():
    try:
        # Método actualizado para verificar conexión
        client.get_collections()
        logger.info("Conexión exitosa con Qdrant")
        return True
    except Exception as e:
        logger.error(f"Error de conexión: {str(e)}")
        return False

# Creación de colección optimizada
def create_collection(collection_name, vector_size=384):
    if not client.collection_exists(collection_name):
        client.create_collection(
            collection_name=collection_name,
            vectors_config=VectorParams(
                size=vector_size,
                distance=Distance.COSINE
            ),
            optimizers_config=models.OptimizersConfigDiff(
                indexing_threshold=0,
                memmap_threshold=20000
            )
        )
        logger.info(f"Colección {collection_name} creada")

# Procesamiento de archivos con manejo de errores
def process_json_file(file_path):
    encodings = ['utf-8', 'cp1252', 'iso-8859-1']
    for encoding in encodings:
        try:
            with open(file_path, 'r', encoding=encoding) as f:
                return json.load(f)
        except (UnicodeDecodeError, json.JSONDecodeError):
            continue
    raise ValueError(f"No se pudo decodificar {file_path}")



# Función principal de carga con reintentos
@retry(stop=stop_after_attempt(5),
       wait=wait_exponential(multiplier=1, min=2, max=30),
       before=before_log(logger, logging.DEBUG))
def load_and_upload_vectors(json_folder_path, collection_name):
    if not verify_connection():
        raise ConnectionError("No se pudo establecer conexión con Qdrant")
    
    model = SentenceTransformer('all-MiniLM-L6-v2')
    vector_size = model.get_sentence_embedding_dimension()
    
    # Crear colección con tamaño correcto
    create_collection(collection_name, vector_size)
    
    vectors = []
    payloads = []
    
    # Procesar archivos
    for json_file in os.listdir(json_folder_path):
        if json_file.endswith(".json"):
            file_path = os.path.join(json_folder_path, json_file)
            try:
                data = process_json_file(file_path)
                for item in data:
                    text = item.get("content", "")
                    if text:
                        vector = model.encode(text).astype(np.float32).tolist()
                        vectors.append(vector)
                        # Generar ID único automáticamente
                        point_id = item.get("id")
                        if not (isinstance(point_id, int) and point_id >= 0):
                            point_id = uuid4().hex  # Genera UUID tipo 4 (aleatorio)

                        payloads.append({
                            "id": point_id,  # Ahora es válido
                            "metadata": item,
                            "source_file": json_file
                        })
            except Exception as e:
                logger.error(f"Error procesando {json_file}: {str(e)}")
                continue

    # Carga en lotes con manejo de memoria
    batch_size = 16
    logger.info(f"Iniciando carga de {len(vectors)} vectores con batch size {batch_size}")

    for i in range(0, len(vectors), batch_size):
        batch_vectors = vectors[i:i+batch_size]
        batch_payloads = payloads[i:i+batch_size]
        
        points = [
            models.PointStruct(
                id=payload["id"],
                vector=vector,
                payload=payload
            ) for vector, payload in zip(batch_vectors, batch_payloads)
        ]

        try:
            client.upsert(
                collection_name=collection_name,
                points=points,
                wait=True
            )
            logger.info(f"Lote {i//batch_size + 1}/{(len(vectors)//batch_size)+1} cargado")
        except Exception as e:
            logger.error(f"Error en lote {i//batch_size + 1}: {str(e)}")
            raise

    # Optimizar colección después de carga
    client.update_collection(
        collection_name=collection_name,
        optimizer_config=models.OptimizersConfigDiff(
            indexing_threshold=20000
        )
    )

if __name__ == "__main__":
    # Limpieza inicial
    for col in COLLECTIONS.values():
        try:
            client.delete_collection(col)
            logger.info(f"Colección {col} eliminada")
        except Exception as e:
            logger.warning(f"No se pudo eliminar {col}: {str(e)}")
    
    # Crear nuevas colecciones
    for col in COLLECTIONS.values():
        create_collection(col)

    # Cargar datos
    try:
        load_and_upload_vectors("./vectors_Ejercicios", COLLECTIONS["exercise"])
        load_and_upload_vectors("./vectors_Docu", COLLECTIONS["documentation"])
        load_and_upload_vectors("./vectors_Algoritmos", COLLECTIONS["algorithm"])
        logger.info("Carga completa exitosamente")
    except Exception as e:
        logger.error(f"Error fatal: {str(e)}")
        exit(1)