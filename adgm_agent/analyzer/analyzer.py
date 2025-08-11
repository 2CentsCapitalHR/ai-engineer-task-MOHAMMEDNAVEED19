from ..utils.text_io import extract_text_from_docx
from ..utils.classification import classify_document
from ..utils.checks import *


def validate_paragraph(paragraph: str, retrieved, local_llm):
    if not retrieved:
        return {"issue_found": False, "findings": "No relevant ADGM references found", "suggestion": None, "citations": []}
    context = "\n\n---\n\n".join([r["text"][:1500] for r in retrieved])
    citations = list({r["metadata"]["source_file"] for r in retrieved})
    if local_llm and getattr(local_llm, 'initialized', False):
        return local_llm.validate_paragraph(paragraph, context)
    else:
        issues = []
        if check_jurisdiction(paragraph):
            issues.append("Jurisdiction issue: ADGM not specified")
        if check_placeholders(paragraph):
            issues.append("Placeholder detected")
        if check_ambiguous_language(paragraph):
            issues.append("Ambiguous language detected")
        if issues:
            return {"issue_found": True, "findings": "; ".join(issues), "suggestion": "Review and clarify based on ADGM requirements", "citations": citations}
        else:
            return {"issue_found": False, "findings": "No rule-based issues detected", "suggestion": None, "citations": []}


def analyze_docx(path, rag_db, checklist_map, local_llm):
    text = extract_text_from_docx(path)
    if not text.strip():
        return {"filename": path.name, "document_type": "Invalid/Could not read", "num_paragraphs": 0, "issues_found": [{"document": path.name, "issue": "Could not read document", "severity": "High"}], "reviewed_path": None}
    paras = [p for p in text.split("\n") if p.strip()]
    doc_type = classify_document(text)
    findings = []
    for idx, p in enumerate(paras):
        issues_here = []
        if check_jurisdiction(p):
            issues_here.append(("Jurisdiction reference to courts/jurisdiction but ADGM not specified", "High"))
        if check_placeholders(p):
            issues_here.append(("Placeholder (____ / TBD) detected", "Medium"))
        if check_ambiguous_language(p):
            issues_here.append(("Ambiguous obligation language (uses 'may' where binding language expected)", "Medium"))
        for issue_text, severity in issues_here:
            retrieved = rag_db.query(p, top_k=3) if rag_db else []
            validation = validate_paragraph(p, retrieved, local_llm)
            if validation["issue_found"]:
                findings.append({"document": path.name, "document_type": doc_type, "para_index": idx, "snippet": p[:300], "issue": issue_text, "severity": severity, "suggestion": validation.get("suggestion"), "citations": validation.get("citations", [])})
    if not check_signature_block(paras):
        findings.append({"document": path.name, "document_type": doc_type, "para_index": -1, "snippet": "", "issue": "Missing signature block / signatory details near end of document", "severity": "High", "suggestion": "Add signature block with name, title, and date.", "citations": []})
    if not check_ubo_present(paras):
        findings.append({"document": path.name, "document_type": doc_type, "para_index": -1, "snippet": "", "issue": "No UBO declaration or UBO reference found", "severity": "Medium", "suggestion": "Include or upload UBO Declaration Form or mention UBO in filings.", "citations": []})
    # Prepare annotation items
    annotate_items = []
    for it in findings:
        if it.get("para_index", -2) >= 0:
            annotate_items.append({"para_index": it["para_index"], "issue": it["issue"], "severity": it["severity"], "suggestion": it.get("suggestion"), "citations": it.get("citations", [])})
    return {"filename": path.name, "document_type": doc_type, "num_paragraphs": len(paras), "issues_found": findings, "annotation_items": annotate_items}
