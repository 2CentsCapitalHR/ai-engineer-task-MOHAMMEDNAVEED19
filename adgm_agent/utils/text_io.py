from pathlib import Path
from docx import Document
import pdfplumber


def extract_text_from_docx(path: Path) -> str:
    try:
        doc = Document(path)
        paras = [p.text.strip() for p in doc.paragraphs if p.text.strip()]
        return "\n".join(paras)
    except Exception as e:
        print(f"[WARN] Failed to read {path.name} as DOCX: {e}")
        try:
            return path.read_text(encoding='utf-8', errors='ignore')
        except Exception as e2:
            print(f"[WARN] Also failed to read {path.name} as plain text: {e2}")
            return ""


def extract_text_from_pdf(path: Path) -> str:
    texts = []
    try:
        with pdfplumber.open(path) as pdf:
            for page in pdf.pages:
                t = page.extract_text()
                if t:
                    texts.append(t)
    except Exception as e:
        print(f"[WARN] pdfplumber failed for {path.name}: {e}")
    return "\n".join(texts)


def extract_text_from_file(path: Path) -> str:
    s = path.suffix.lower()
    if s in [".docx", ".doc"]:
        return extract_text_from_docx(path)
    elif s == ".pdf":
        return extract_text_from_pdf(path)
    else:
        try:
            return path.read_text(encoding="utf-8", errors="ignore")
        except:
            return ""
