import faiss
import os
import pickle
from app.chunker import chunk_text
from sentence_transformers import SentenceTransformer

EMBED_MODEL = SentenceTransformer("all-MiniLM-L6-v2")
VECTOR_PATH = "data/index.faiss"
DOC_PATH = "data/docs.pkl"

def ingest_document(text: str):
    chunks = chunk_text(text)
    embeddings = EMBED_MODEL.encode(chunks)
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)
    faiss.write_index(index, VECTOR_PATH)
    with open(DOC_PATH, "wb") as f:
        pickle.dump(chunks, f)