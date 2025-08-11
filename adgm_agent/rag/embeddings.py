import numpy as np

class LocalEmbeddings:
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        try:
            from sentence_transformers import SentenceTransformer
            self.model = SentenceTransformer(model_name)
            print(f"[EMBED] Loaded local embedding model: {model_name}")
        except ImportError as e:
            raise ImportError("Please install sentence-transformers: pip install sentence-transformers")

    def embed(self, texts):
        return self.model.encode(texts, convert_to_numpy=True)
