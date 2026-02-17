# Fluxo

**Virtual Assistant for the Study of Regular Grammars, Context-Free Grammars, and Finite Automata**

[![UFV](https://img.shields.io/badge/University-Francisco%20de%20Vitoria-blue)](https://www.ufv.es)
[![Degree](https://img.shields.io/badge/Degree-Mathematical%20Engineering-success)](https://www.ufv.es)
[![TFG](https://img.shields.io/badge/Final%20Project-June%202025-orange)](https://github.com/nachodele/TFG)

Web application developed as Final Degree Project (TFG) in Mathematical Engineering at Universidad Francisco de Vitoria.  
Author: **Ignacio de Lecea Jiménez**

## Table of Contents

- [Description](#description)
- [Main Features](#main-features)
- [Technologies Used](#technologies-used)
- [Quick Access](#quick-access)
- [Local Installation (Development)](#local-installation-development)
- [Deployment on Hugging Face Spaces](#deployment-on-hugging-face-spaces)
- [Best Practices for Optimal Use](#best-practices-for-optimal-use)
- [Acknowledgments](#acknowledgments)
- [License](#license)

## Description

Fluxo is an educational virtual assistant designed to support students and teachers in learning and solving exercises related to:

- Regular grammars (RG)
- Context-free grammars (CFG)
- Finite automata (DFA / NFA)
- Conversions between models (regular expressions, grammars, automata, etc.)
- Classic algorithms in automata theory and formal languages

## Main Features

1. **Specialized Chatbot**  
   Instant and accurate consultation of theoretical concepts and technical documentation.

2. **Educational Copilot**  
   Detailed, step-by-step feedback on solutions proposed by the student:  
   - Error identification  
   - Improvement suggestions  
   - Property verification  
   - Guidance toward the correct solution

## Technologies Used

- Interface: **Streamlit**
- Language Model: **Llama 4 Maverick** via **GroqCloud**
- Retrieval-Augmented Generation (RAG): **Qdrant** (vector database)
- Deployment: **Hugging Face Spaces**
- Knowledge Format: **Markdown**

## Quick Access

🌐 **Deployed Version (Recommended)**  
→ [Fluxo](https://huggingface.co/spaces/nachodele/Fluxo)

## Local Installation (Development)

1. Clone the repository
   ```bash
   git clone https://github.com/nachodele/TFG.git

2. Install dependencies (make sure you have pip installed):
    ```bash
    pip install -r requirements.  
    ``` 
3. Set up environment variables:
Create a .env file in the project root with the following content:
- GROQ_API_KEY=your_groq_api_key
- QDRANT_API_KEY=your_qdrant_api_key
- QDRANT_URL=https://your-cluster.qdrant.io

4. Run the application:
   ```bash
    streamlit run app.py
    ```

## Deployment on Hugging Face Spaces

1. Create a new Space on Hugging Face Spaces and upload the repository code.
2. Configure the Secrets in the Space settings with your API keys:
GROQ_API_KEY, QDRANT_API_KEY, QDRANT_URL
3. Deployment is automatic. Access the URL provided by Hugging Face.

Note: The deployed version ensures cross-platform access. If you experience issues, check your API quotas on Groq and Qdrant.

For proper use of the tool, please consult the full User Manual.
## Best Practices for Optimal Use
To obtain complete, accurate, and reliable responses, follow the guidelines in the User Manual:

   - Always structure your input using Markdown
   - Use clear headings: # Problem and ## Statement
   - Present automata in Markdown tables
   - Use plain-text mathematical symbols according to Fluxo's glossary
   - Break down solutions into numbered steps with headings (# Step 1, ## 1.1, etc.)
   - Always include an explicit verification step
   - Specify in the statement the properties or conditions you want Fluxo to check

### Supported algorithms (implemented in the knowledge base):

   NFA → DFA conversion (subset construction)  
   Cocke-Younger-Kasami (CYK) algorithm  
   Left recursion elimination (direct and indirect)  
   Regular Expression → Regular Grammar → Finite Automaton (derivatives / Thompson)  
   CFG simplification (useless, unreachable, λ-productions, unit productions)  
   Chomsky Normal Form (CNF)  
   Greibach Normal Form (GNF)  
   CFG → Pushdown Automaton (PDA)  
   DFA minimization  
   Left factoring  

## Acknowledgments

- Juan José Escribano – Precursor, continuous guidance, human evaluation of the Copilot
- Elena Gutiérrez Cruz – Expert in RAG, vector databases, and Markdown format
- Moisés Martínez – Key technical support (from Java attempts to Hugging Face deployment)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for full details.
