DOC_TYPE_KEYWORDS = {
    "Articles of Association": ["articles of association", "articles of association (", "aoa", "article of association"],
    "Memorandum of Association": ["memorandum of association", "memorandum", "moa"],
    "Resolution": ["resolution", "resolutions", "shareholder resolution"],
    "Incorporation Application Form": ["incorporation application", "application for incorporation", "incorporation form"],
    "UBO Declaration Form": ["ubo declaration", "ultimate beneficial owner", "ubo"],
    "Register of Members and Directors": ["register of members", "register of directors", "register of members and directors"],
    "Employment Contract": ["employment contract", "employee", "employer"],
}


def classify_document(text: str) -> str:
    t = text.lower()
    scores = {name: sum(1 for k in keys if k in t) for name, keys in DOC_TYPE_KEYWORDS.items()}
    best = max(scores.items(), key=lambda x: x[1])
    if best[1] == 0:
        return "Unknown"
    return best[0]
