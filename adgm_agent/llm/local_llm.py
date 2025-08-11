import json

class LocalLLM:
    def __init__(self, model_path: str = "", use_local: bool = False):
        self.initialized = False
        self.use_local = use_local
        if model_path and use_local:
            try:
                from llama_cpp import Llama
                self.llm = Llama(model_path=model_path)
                self.initialized = True
                print(f"[LLM] Loaded local LLM from {model_path}")
            except ImportError:
                print("[LLM] llama-cpp-python not installed. Falling back to rule-based only.")

    def validate_paragraph(self, paragraph: str, context: str = "") -> dict:
        if not self.initialized:
            return {"issue_found": False, "findings": "Local LLM not available", "suggestion": None, "citations": []}

        prompt = (
            "You are an assistant that checks ADGM legal compliance..."  # truncated for brevity
        )
        try:
            response = self.llm.create_chat_completion(messages=[{"role": "user", "content": prompt}], max_tokens=400, temperature=0.0)
            output = response["choices"][0]["message"]["content"]
            try:
                return json.loads(output)
            except json.JSONDecodeError:
                return {"issue_found": True, "findings": output[:800], "suggestion": None, "citations": []}
        except Exception as e:
            print(f"[LLM] Error: {e}")
            return {"issue_found": False, "findings": f"LLM error: {e}", "suggestion": None, "citations": []}
