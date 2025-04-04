from flask import Flask, request, jsonify
from flask_cors import CORS
from chatbot import GrammarAutomataProcessor
from sentence_transformers import SentenceTransformer

# Configuración inicial
app = Flask(__name__)
CORS(app)  # Habilitar CORS para integración con frontend
processor = GrammarAutomataProcessor()
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')  # Cargar modelo una vez

# Endpoint para responder preguntas
@app.route('/api/answer', methods=['POST'])
def handle_answer():
    try:
        data = request.json
        user_input = data.get('question')
        
        if not user_input:
            return jsonify({"error": "El campo 'question' es requerido"}), 400
            
        response_data = processor.answer_question(user_input)
        return jsonify({
            "response": response_data["response"],
            "source": response_data["source_file"]
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint para evaluar soluciones
@app.route('/api/evaluate', methods=['POST'])
def handle_evaluation():
    try:
        data = request.json
        problem = data.get('problem')
        solution = data.get('solution')
        
        if not problem or not solution:
            return jsonify({"error": "Los campos 'problem' y 'solution' son requeridos"}), 400
            
        evaluation = processor.evaluate_problem(problem, solution)
        return jsonify({
            "feedback": evaluation["response"],
            "source": evaluation["source_file"]
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint para embeddings
@app.route('/api/embedding', methods=['POST'])
def get_embedding():
    try:
        data = request.json
        text = data.get('text')
        
        if not text:
            return jsonify({"error": "El campo 'text' es requerido"}), 400
            
        embedding = embedding_model.encode(text).tolist()
        return jsonify({
            "embedding": embedding,
            "model": "all-MiniLM-L6-v2"
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

# Endpoint de verificación de salud
@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({
        "status": "ok",
        "service": "Grammar Automata Processor API",
        "version": "1.0"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=False)