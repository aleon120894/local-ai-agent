from rag.embedder import embed
from rag.vector_store import VectorStore
from rag.retriever import init_store


def build_index():

    tcp = "TCP is a reliable transport protocol."
    udp = "UDP is a connectionless protocol."

    dimension = len(embed(tcp))

    store = VectorStore(dimension)

    store.add(
        embed(tcp),
        tcp
    )

    store.add(
        embed(udp),
        udp
    )

    init_store(store)

    return store
