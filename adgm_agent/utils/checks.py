import re

ADGM_KEYWORDS = ["adgm", "abu dhabi global market", "abu dhabi global", "abudhabi"]
SIGNATURE_KEYWORDS = ["signature", "signed by", "for and on behalf", "name:", "signature:"]
UBO_KEYWORDS = ["ubo", "ultimate beneficial owner", "ultimate beneficial owners"]


def check_jurisdiction(paragraph: str) -> bool:
    low = paragraph.lower()
    if ("court" in low or "jurisdiction" in low) and not any(k in low for k in ADGM_KEYWORDS):
        return True
    return False


def check_placeholders(paragraph: str) -> bool:
    return bool(re.search(r"_{3,}|___+|tbd|to be decided|to be confirmed", paragraph, flags=re.I))


def check_ambiguous_language(paragraph: str) -> bool:
    low = paragraph.lower()
    if "may" in low and ("shall" not in low and "must" not in low):
        if any(w in low for w in ["oblig", "respons", "right", "entitl", "require", "liabil"]):
            return True
    return False


def check_signature_block(paragraphs: list) -> bool:
    joined = " ".join(paragraphs[-12:]).lower()
    return any(k in joined for k in SIGNATURE_KEYWORDS)


def check_ubo_present(paragraphs: list) -> bool:
    joined = " ".join(paragraphs).lower()
    return any(k in joined for k in UBO_KEYWORDS)
