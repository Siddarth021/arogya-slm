# backend/core/llm.py

from transformers import pipeline

class LLM:
    def __init__(self):
        self.generator = pipeline(
            "text-generation",
            model="tiiuae/falcon-rw-1b",   # lightweight model
            max_new_tokens=200
        )

    def generate(self, prompt):
        output = self.generator(prompt)[0]["generated_text"]
        return output


llm = LLM()