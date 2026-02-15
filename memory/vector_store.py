import chromadb
from chromadb.utils import embedding_functions

class VectorMemory:

    def __init__(self):
        self.client = chromadb.Client()
        self.collection = self.client.create_collection("qa_memory")

    def store(self, doc_id, text):
        self.collection.add(
            documents=[text],
            ids=[doc_id]
        )

    def search(self, query):
        return self.collection.query(
            query_texts=[query],
            n_results=3
        )
