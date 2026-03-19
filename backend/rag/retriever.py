# backend/rag/retriever.py

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings


class Retriever:
    def __init__(self, data_path="data/raw/ayurveda_texts.txt"):
        self.embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )
        self.texts = self.load_data(data_path)
        self.db = FAISS.from_texts(self.texts, self.embeddings)

    def load_data(self, path):
        with open(path, "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f.readlines()]
            return [line for line in lines if line]  # remove empty lines

    def search(self, query, k=3):
        docs = self.db.similarity_search(query, k=k)
        return [doc.page_content for doc in docs]


# singleton
retriever = Retriever()