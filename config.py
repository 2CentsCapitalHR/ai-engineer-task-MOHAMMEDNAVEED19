from pathlib import Path
ROOT = Path(__file__).parent
USER_UPLOADS = ROOT / "data" / "user_uploads"
REFERENCE_DIR = ROOT / "data" / "adgm_refs"
CHECKLIST_PATH = ROOT / "data" / "checklist_mapping.json"
OUTPUT_DIR = ROOT / "output"

# Local model config
USE_LOCAL_LLM = False
LOCAL_LLM_PATH = ""
EMBEDDING_MODEL = "all-MiniLM-L6-v2"

# Create dirs (runtime)
for p in [USER_UPLOADS, REFERENCE_DIR, OUTPUT_DIR]:
    p.mkdir(parents=True, exist_ok=True)
