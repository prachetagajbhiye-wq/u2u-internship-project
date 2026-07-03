from embedding_service import create_query_embedding
from vector_store import search


def retrieve_context(question):
    """
    Searches ChromaDB and returns context + sources.
    """

    embedding = create_query_embedding(question)

    results = search(embedding)

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]

    context = "\n\n".join(documents)

    sources = []

    for item in metadatas:
        source = item["source"]

        if source not in sources:
            sources.append(source)

    return context, sources