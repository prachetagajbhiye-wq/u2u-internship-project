from embedding_service import create_query_embedding
from vector_store import search
from ai_service import generate_ai_answer


def retrieve_context(question, top_k=5):

    query_embedding = create_query_embedding(question)

    results = search(query_embedding, top_k)

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]

    context = ""

    sources = []

    for doc, metadata in zip(documents, metadatas):

        context += doc + "\n\n"

        source = metadata["source"]

        if source not in sources:
            sources.append(source)

    return context, sources


def get_rag_answer(question):

    context, sources = retrieve_context(question)

    answer = generate_ai_answer(
        question,
        context
    )

    return {
        "answer": answer,
        "sources": sources
    }