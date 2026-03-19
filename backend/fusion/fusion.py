# backend/fusion/fusion.py

from backend.rag.retriever import retriever
from backend.knowledge_graph.dosha import infer_dosha

def build_context(user_input):
    docs = retriever.search(user_input)
    context = "\n".join(docs)

    dosha = infer_dosha(user_input)

    return context, dosha