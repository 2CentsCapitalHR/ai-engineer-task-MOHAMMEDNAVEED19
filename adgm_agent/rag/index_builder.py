from pathlib import Path
from ..utils.text_io import extract_text_from_file
from ..utils.text_io import extract_text_from_file as _extract
from ..utils.text_io import extract_text_from_docx

from ..utils.text_io import extract_text_from_file

from .vector_db import SimpleVectorDB


def chunk_text(text: str, chunk_size_words: int = 300, overlap: int = 60):
    words = text.split()
    chunks = []
    i = 0
    n = len(words)
    while i < n:
        chunk = words[i:i+chunk_size_words]
        chunks.append(" ".join(chunk))
        i += chunk_size_words - overlap
    return chunks


def build_rag_index(reference_dir: Path, embedder: SimpleVectorDB):
    all_texts = []
    all_meta = []
    for file in sorted(reference_dir.glob("*")):
        if file.is_dir():
            for nested in sorted(file.glob("*")):
                if nested.is_file():
                    txt = extract_text_from_file(nested)
                    if txt.strip():
                        chunks = chunk_text(txt)
                        for i, c in enumerate(chunks):
                            all_texts.append(c)
                            all_meta.append({"source_file": nested.name, "chunk_index": i})
        else:
            if file.is_file():
                txt = extract_text_from_file(file)
                if txt.strip():
                    chunks = chunk_text(txt)
                    for i, c in enumerate(chunks):
                        all_texts.append(c)
                        all_meta.append({"source_file": file.name, "chunk_index": i})
    db = SimpleVectorDB(embedder)
    if len(all_texts) == 0:
        print("[RAG] No reference texts found in", reference_dir)
    else:
        db.build(all_texts, all_meta)
        print(f"[RAG] Built index with {len(all_texts)} chunks.")
    return db
