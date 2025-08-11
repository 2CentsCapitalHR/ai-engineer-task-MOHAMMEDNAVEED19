[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/vgbm4cZ0)

# ADGM Corporate Agent (Modular)

This repo contains a modular refactor of your provided single-file agent.  

What's present (ported from your original file):
- Text extraction for DOCX & PDF
- Rule-based checks (jurisdiction, placeholders, ambiguous language, signature & UBO detection)
- Local embeddings wrapper using sentence-transformers
- Simple in-memory vector DB & RAG index builder
- Local LLM wrapper (llama.cpp integration points)
- DOCX annotator that saves a reviewed file
- Gradio UI wrapper

What's missing / needs your input:
- Actual ADGM reference documents placed under `data/adgm_refs/` (RAG requires these)
- `data/checklist_mapping.json` (example provided)
- Installation of runtime dependencies: python-docx, pdfplumber, sentence-transformers, gradio, llama-cpp-python (optional)
- Optional: a local llama model file and `USE_LOCAL_LLM = True` to enable LLM validations

Next steps:
1. Split the blocks above into files as suggested.
2. Populate `data/adgm_refs/` with official ADGM PDFs / DOCX files.
3. Set up a Python virtualenv and install requirements.
4. Run `python -m adgm_agent.main` to launch the Gradio UI.
