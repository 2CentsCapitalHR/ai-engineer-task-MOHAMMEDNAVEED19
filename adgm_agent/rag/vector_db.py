import numpy as np

class SimpleVectorDB:
    def __init__(self, embedding_model):
        self.embedder = embedding_model
        self.vectors = None
        self.texts = []
        self.metadatas = []
        self.D = None

    def build(self, texts, metadatas):
        if len(texts) == 0:
            self.vectors = np.zeros((0, 384), dtype=np.float32)
            self.D = 384
            return
        batch_size = 32
        embeddings = []
        for i in range(0, len(texts), batch_size):
            batch = texts[i:i+batch_size]
            emb = self.embedder.embed(batch)
            embeddings.append(emb)
        self.vectors = np.concatenate(embeddings, axis=0)
        self.texts = texts
        self.metadatas = metadatas
        self.D = self.vectors.shape[1]

    def query(self, q, top_k=3):
        if self.vectors is None or self.vectors.shape[0] == 0:
            return []
        q_emb = self.embedder.embed([q])[0]
        dots = np.dot(self.vectors, q_emb)
        norms = np.linalg.norm(self.vectors, axis=1)
        q_norm = np.linalg.norm(q_emb)
        sims = dots / (norms * q_norm + 1e-12)
        idx = np.argsort(-sims)[:top_k]
        results = []
        for i in idx:
            results.append({"text": self.texts[i], "metadata": self.metadatas[i], "score": float(sims[i])})
        return results
