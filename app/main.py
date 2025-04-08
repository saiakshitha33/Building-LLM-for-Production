from fastapi import FastAPI, File, UploadFile
from app.ocr import extract_text_from_pdf
from app.summarizer import summarize_text
from app.question_answerer import answer_question
try:
    from app.vector_store import ingest_document
except ImportError:
    raise ImportError("The module 'app.vector_store' or 'ingest_document' function could not be found. Ensure the file exists and is in the correct directory.")
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class QARequest(BaseModel):
    question: str

@app.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    content = await file.read()
    text = extract_text_from_pdf(content)
    ingest_document(text)
    summary = summarize_text(text)
    return {"summary": summary}

@app.post("/ask")
async def ask_question(data: QARequest):
    answer = answer_question(data.question)
    return {"answer": answer}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
