#  RAGent – AI Document Summarizer Powered by RAG

RAGent is a modular, production-ready LLM pipeline that uses **Retrieval-Augmented Generation (RAG)** to intelligently parse, summarize, and answer questions from large, unstructured documents — including scanned PDFs.

Whether it's legal, medical, or policy documentation, RAGent leverages OCR, vector search, and LLM reasoning to extract key insights and enable natural language interaction.

---

### 🔧 Features

- 📄 **OCR-based Extraction** – Extracts text from scanned or image-based documents  
- ✂️ **Chunking** – Splits text into structured, overlapping segments for context-aware processing  
- 🔍 **Vector Search** – Embeds chunks into a vector DB (FAISS/Chroma) for efficient retrieval  
- 🧠 **Summarization** – Generates concise section summaries using OpenAI or Cohere  
- 💬 **Question Answering** – Answers user queries using context pulled from relevant chunks  
- 🧱 **Modular Design** – Separated components for OCR, chunking, LLM utils, QA, and more  
- 🔐 **.env Support** – Secure credential management with `.env` for API keys and configs

---

### ⚙️ Stack

| Type            | Tools & Libraries                                                           |
|------------------|------------------------------------------------------------------------------|
| **Language**     | Python                                                                       |
| **LLMs**         | OpenAI GPT, Cohere, Hugging Face Transformers                               |
| **RAG**          | FAISS / Chroma + OpenAI APIs                                                 |
| **OCR**          | Tesseract OCR                                                                |
| **Vector DB**    | FAISS, pgvector, Qdrant (pluggable)                                          |
| **Chunking**     | Overlapping sliding window w/ metadata                                       |
| **MLOps Ready**  | `.env`, modular utils, ready for API deployment via FastAPI/Streamlit        |

---

### 📁 Project Structure

```text
📂 RAGent/
├── main.py                # Orchestration logic
├── ocr.py                 # OCR text extraction from scanned docs
├── chunker.py             # Document chunking with windowing
├── vector_store.py        # Embedding + storage using FAISS
├── summarizer.py          # LLM-based summarization
├── question_answerer.py   # QA pipeline using RAG
├── llm_utils.py           # Shared helper functions for LLMs
├── requirements.txt       # Python dependencies
└── .env                   # API keys and config variables

**How to run**

# 1. Install dependencies
pip install -r requirements.txt

# 2. Add your keys to .env
echo "OPENAI_API_KEY=sk-..." > .env

# 3. Run the pipeline
python main.py

