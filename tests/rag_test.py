from rag.embedder import embed
from rag.vector_store import VectorStore

tcp = "TCP is a reliable transport protocol."
udp = "UDP is a connectionless protocol."

tcp_embedding = embed(tcp)

store = VectorStore(
    dimension=len(tcp_embedding)
)

store.add(
    tcp_embedding,
    tcp
)

store.add(
    embed(udp),
    udp
)

results = store.search(
    embed("Explain TCP"),
    k=1
)

print(results)
