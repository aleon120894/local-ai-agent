from rag.embedder import embed
from rag.vector_store import VectorStore

# тимчасово глобальний індекс (для v0.5 OK)
store = None


def init_store(vector_store: VectorStore):
    global store
    store = vector_store


def search(query: str) -> list[str]:
    if store is None:
        raise Exception("Vector store not initialized")

    query_embedding = embed(query)

    return store.search(query_embedding, k=1)
