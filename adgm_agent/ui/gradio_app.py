import gradio as gr
from ..rag.embeddings import LocalEmbeddings
from ..llm.local_llm import LocalLLM
from ..rag.index_builder import build_rag_index
from ..analyzer.analyzer import analyze_docx
from pathlib import Path
from ..config import USER_UPLOADS, CHECKLIST_PATH, REFERENCE_DIR
import json


def analyze_files_wrapper(files):
    embedder = LocalEmbeddings()
    local_llm = LocalLLM(use_local=False)
    rag_db = build_rag_index(REFERENCE_DIR, embedder)
    checklist_map = json.loads(open(CHECKLIST_PATH).read())
    results = []
    for file_info in files:
        file_path = USER_UPLOADS / Path(file_info.name).name
        with open(file_path, "wb") as f:
            f.write(file_info.read())
        result = analyze_docx(file_path, rag_db, checklist_map, local_llm)
        results.append(result)
    return {"results": results}


def create_gradio_interface():
    with gr.Blocks(title="ADGM Corporate Agent") as demo:
        gr.Markdown("## ADGM Document Analyzer")
        inputs = gr.File(file_count="multiple", file_types=[".docx"], label="Upload Documents")
        outputs = gr.JSON(label="Analysis Results")
        btn = gr.Button("Analyze")
        btn.click(analyze_files_wrapper, inputs=inputs, outputs=outputs)
    return demo
