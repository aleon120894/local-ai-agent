from rag.embedder import embed
from rag.vector_store import VectorStore
from rag.retriever import init_store

import os


def build_index():

    files = os.listdir("data")

    dimension = len(embed("test"))
    store = VectorStore(dimension)

    indexed = 0

    for filename in files:

        path = os.path.join("data", filename)

        with open(path, "r") as f:
            content = f.read()

        if not content.strip():
            print(f"Skipping empty file: {filename}")
            continue

        store.add(
            embed(content),
            content
        )

        indexed += 1

    print(f"Indexed {indexed} documents")

    init_store(store)

    return store
