from rag.embedder import embed
from rag.vector_store import VectorStore
from rag.retriever import init_store

import os


def build_index():

    files = os.listdir("data")
    dimension = len(embed("test"))
    store = VectorStore(dimension)

    for filename in files:
        path = os.path.join("data", filename)

        with open(path, "r") as f:
            content = f.read()

        store.add(
            embed(content),
            content
        )

    init_store(store)

    return store
