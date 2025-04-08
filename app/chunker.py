from typing import List
import textwrap

CHUNK_SIZE = 500

def chunk_text(text: str) -> List[str]:
    paragraphs = text.split("\n")
    chunks = []
    chunk = ""
    for para in paragraphs:
        if len(chunk + para) < CHUNK_SIZE:
            chunk += para + "\n"
        else:
            chunks.append(chunk.strip())
            chunk = para + "\n"
    if chunk:
        chunks.append(chunk.strip())
    return chunks