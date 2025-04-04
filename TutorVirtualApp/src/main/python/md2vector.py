import os
import re
import json
import numpy as np
from transformers import AutoTokenizer, AutoModel
import torch
import markdown
from bs4 import BeautifulSoup

class MarkdownProcessor:
    def __init__(self, model_name="sentence-transformers/all-MiniLM-L6-v2"):
        """
        Inicializa el procesador de Markdown con el modelo de embeddings especificado.
        
        Args:
            model_name (str): Nombre del modelo de embeddings a utilizar
        """
        self.model_name = model_name
        # Carga el tokenizador y el modelo
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModel.from_pretrained(model_name)
        self.model.eval()  # Poner el modelo en modo evaluación

    def _html_to_text(self, html_content):
        """
        Convierte contenido HTML a texto plano.
        
        Args:
            html_content (str): Contenido HTML
            
        Returns:
            str: Texto plano
        """
        soup = BeautifulSoup(html_content, 'html.parser')
        return soup.get_text(separator=' ', strip=True)

    def _split_by_headers(self, md_content):
        """
        Divide el contenido de Markdown en chunks basados en encabezados.
        
        Args:
            md_content (str): Contenido del archivo Markdown
            
        Returns:
            list: Lista de diccionarios con {title, content, level}
        """
        # Convertir Markdown a HTML para análisis estructural
        html_content = markdown.markdown(md_content)
        soup = BeautifulSoup(html_content, 'html.parser')
        
        chunks = []
        current_header = "Root"
        current_level = 0
        current_content = []
        
        # Encuentra todos los elementos
        elements = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'ul', 'ol', 'code', 'pre', 'blockquote'])
        
        for element in elements:
            tag_name = element.name
            
            # Si es un encabezado, guarda el chunk anterior y comienza uno nuevo
            if tag_name.startswith('h') and len(tag_name) == 2:
                level = int(tag_name[1])
                
                # Guardar el chunk anterior si hay contenido
                if current_content:
                    chunks.append({
                        'title': current_header,
                        'content': ' '.join(current_content),
                        'level': current_level
                    })
                    current_content = []
                
                # Comenzar un nuevo chunk
                current_header = element.get_text()
                current_level = level
            else:
                # Agregar contenido al chunk actual
                current_content.append(self._html_to_text(str(element)))
        
        # Guardar el último chunk
        if current_content:
            chunks.append({
                'title': current_header,
                'content': ' '.join(current_content),
                'level': current_level
            })
        
        return chunks

    def _get_embeddings(self, text):
        """
        Genera embeddings para un texto dado utilizando el modelo cargado.
        
        Args:
            text (str): Texto para generar embeddings
            
        Returns:
            np.ndarray: Vector de embeddings
        """
        # Tokenizar el texto
        inputs = self.tokenizer(text, padding=True, truncation=True, return_tensors="pt", max_length=512)
        
        # Generar embeddings
        with torch.no_grad():
            outputs = self.model(**inputs)
        
        # Usar mean pooling para obtener el embedding a nivel de frase
        token_embeddings = outputs.last_hidden_state
        attention_mask = inputs['attention_mask']
        
        # Multiplicar por la máscara de atención para ignorar los tokens de padding
        input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
        sum_embeddings = torch.sum(token_embeddings * input_mask_expanded, 1)
        sum_mask = torch.sum(input_mask_expanded, 1)
        sum_mask = torch.clamp(sum_mask, min=1e-9)
        
        # Dividir para obtener el embedding promedio
        sentence_embeddings = sum_embeddings / sum_mask
        
        # Convertir a numpy para su uso posterior
        return sentence_embeddings.numpy()[0]

    def process_markdown_file(self, file_path):
        """
        Procesa un archivo Markdown para generar chunks y sus embeddings.
        
        Args:
            file_path (str): Ruta al archivo Markdown
            
        Returns:
            list: Lista de diccionarios con información de chunks y sus embeddings
        """
        # Leer el archivo Markdown
        with open(file_path, 'r', encoding='utf-8') as f:
            md_content = f.read()
        
        # Dividir en chunks
        chunks = self._split_by_headers(md_content)
        
        # Generar embeddings para cada chunk
        result = []
        for i, chunk in enumerate(chunks):
            # Combinamos título y contenido para el embedding
            full_text = f"{chunk['title']} {chunk['content']}"
            
            # Generamos el embedding
            embedding = self._get_embeddings(full_text)
            
            # Creamos el objeto resultado
            chunk_obj = {
                'id': f"chunk_{i}",
                'file_path': file_path,
                'title': chunk['title'],
                'content': chunk['content'],
                'level': chunk['level'],
                'embedding': embedding.tolist()  # Convertimos a lista para serialización
            }
            
            result.append(chunk_obj)
        
        return result

    def save_embeddings(self, chunks, output_file):
        """
        Guarda los chunks y sus embeddings en un archivo JSON.
        
        Args:
            chunks (list): Lista de chunks con embeddings
            output_file (str): Ruta al archivo de salida
        """
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(chunks, f, ensure_ascii=False, indent=2)
        
        print(f"Embeddings guardados en {output_file}")

def main():
    # Ejemplo de uso
    processor = MarkdownProcessor()
    
    # Directorio con archivos Markdown
    md_dir = "Docu"
    output_dir = "vectors_docu"
    
    # Crear directorio de salida si no existe
    os.makedirs(output_dir, exist_ok=True)
    
    # Procesar cada archivo Markdown
    for filename in os.listdir(md_dir):
        if filename.endswith('.md'):
            file_path = os.path.join(md_dir, filename)
            output_file = os.path.join(output_dir, f"{os.path.splitext(filename)[0]}_embeddings.json")
            
            print(f"Procesando {file_path}...")
            chunks = processor.process_markdown_file(file_path)
            processor.save_embeddings(chunks, output_file)

if __name__ == "__main__":
    main()