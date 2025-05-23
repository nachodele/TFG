import os
import json
import numpy as np
from transformers import AutoTokenizer, AutoModel
import torch
import markdown
from bs4 import BeautifulSoup
import warnings
import transformers

# Deshabilitar todos los warnings de Hugging Face
transformers.logging.set_verbosity_error()
warnings.filterwarnings("ignore", category=UserWarning)

class MarkdownProcessor:
    def __init__(self, model_name="sentence-transformers/all-MiniLM-L6-v2"):
        self.model_name = model_name
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModel.from_pretrained(model_name)
        self.model.eval()

    def _html_to_text(self, html_content):
        soup = BeautifulSoup(html_content, 'html.parser')
        return soup.get_text(separator=' ', strip=True)

    def _split_by_headers(self, md_content):
        html_content = markdown.markdown(md_content)
        soup = BeautifulSoup(html_content, 'html.parser')
        chunks = []
        current_header = "Root"
        current_level = 0
        current_content = []
        
        elements = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'ul', 'ol', 'code', 'pre', 'blockquote'])
        for element in elements:
            tag_name = element.name
            if tag_name.startswith('h') and len(tag_name) == 2:
                level = int(tag_name[1])
                if current_content:
                    chunks.append({
                        'title': current_header,
                        'content': ' '.join(current_content),
                        'level': current_level
                    })
                current_content = []
                current_header = element.get_text()
                current_level = level
            else:
                current_content.append(self._html_to_text(str(element)))
        if current_content:
            chunks.append({
                'title': current_header,
                'content': ' '.join(current_content),
                'level': current_level
            })
        return chunks

    def _split_text_by_tokens(self, text, chunk_size=500, overlap=100):
        """División robusta con control exacto de tokens"""
        tokens = self.tokenizer.tokenize(text)
        chunks = []
        i = 0
        
        while i < len(tokens):
            # Ajuste dinámico del chunk size
            adjusted_size = chunk_size
            while True:
                end = min(i + adjusted_size, len(tokens))
                chunk_tokens = tokens[i:end]
                chunk_text = self.tokenizer.convert_tokens_to_string(chunk_tokens)
                
                # Codificación con special tokens
                encoded = self.tokenizer(
                    chunk_text,
                    add_special_tokens=True,
                    max_length=512,
                    truncation=True
                )
                
                if len(encoded['input_ids']) <= 512:
                    chunks.append(chunk_text)
                    i += (adjusted_size - overlap)
                    break
                else:
                    adjusted_size -= 10
                
                if adjusted_size < 100:
                    chunks.append(chunk_text)  # Forzar último chunk
                    i = len(tokens)
                    break

        return chunks

    def _get_embeddings(self, text):
        """Generación de embeddings con parámetros validados"""
        inputs = self.tokenizer(
            text,
            padding='max_length',
            truncation=True,
            max_length=512,
            return_tensors="pt",
            add_special_tokens=True
        )
        
        with torch.no_grad():
            outputs = self.model(**inputs)
        
        token_embeddings = outputs.last_hidden_state
        attention_mask = inputs['attention_mask']
        
        input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
        sum_embeddings = torch.sum(token_embeddings * input_mask_expanded, 1)
        sum_mask = torch.sum(input_mask_expanded, 1)
        sum_mask = torch.clamp(sum_mask, min=1e-9)
        
        return (sum_embeddings / sum_mask).numpy()[0]

    def process_markdown_file(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            md_content = f.read()
        
        chunks = self._split_by_headers(md_content)
        result = []
        
        for i, chunk in enumerate(chunks):
            full_text = f"{chunk['title']} {chunk['content']}"
            subchunks = self._split_text_by_tokens(full_text)
            
            for j, subchunk_text in enumerate(subchunks):
                embedding = self._get_embeddings(subchunk_text)
                result.append({
                    'id': f"{os.path.basename(file_path)}_{i}_{j}",
                    'file_path': file_path,
                    'title': chunk['title'],
                    'content': subchunk_text,
                    'level': chunk['level'],
                    'embedding': embedding.tolist()
                })
        
        return result

    def save_embeddings(self, chunks, output_file):
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(chunks, f, ensure_ascii=False, indent=2)

def main():
    processor = MarkdownProcessor()
    
    input_dirs = ["Docu", "Ejercicios", "Algoritmos"]
    
    for dir_name in input_dirs:
        output_dir = f"vectors_{dir_name}"
        os.makedirs(output_dir, exist_ok=True)
        
        for filename in os.listdir(dir_name):
            if filename.endswith('.md'):
                file_path = os.path.join(dir_name, filename)
                output_file = os.path.join(output_dir, f"{filename[:-3]}_embeddings.json")
                
                try:
                    chunks = processor.process_markdown_file(file_path)
                    processor.save_embeddings(chunks, output_file)
                except Exception as e:
                    print(f"Archivo {filename} omitido: {str(e)}")

if __name__ == "__main__":
    main()
