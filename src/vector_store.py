import chromadb

client = chromadb.PersistentClient(path="../chroma_db")

collection = client.get_or_create_collection(
    name="education"
)


def store_embeddings(chunks, embeddings):

    ids = []
    documents = []
    metadatas = []

    for i, chunk in enumerate(chunks):

        ids.append(str(i))
        documents.append(chunk["text"])

        metadatas.append({
            "source": chunk["source"]
        })

    collection.upsert(
        ids=ids,
        documents=documents,
        embeddings=embeddings.tolist(),
        metadatas=metadatas
    )


def search(query_embedding, top_k=5):

    results = collection.query(
        query_embeddings=[query_embedding.tolist()],
        n_results=top_k
    )

    return results