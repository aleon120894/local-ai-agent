import faiss
import numpy as np


class VectorStore:

    def __init__(self, dimension):
        self.index = faiss.IndexFlatL2(dimension)
        self.documents = []

    def add(self, embedding, document):
        vector = np.array([embedding], dtype="float32")

        self.index.add(vector)

        self.documents.append(document)

    def search(self, embedding, k=3):
        vector = np.array([embedding], dtype="float32")

        distances, indices = self.index.search(vector, k)

        return [
            self.documents[i]
            for i in indices[0]
            if i < len(self.documents)
        ]
