from sentence_transformers import SentenceTransformer

# Load the embedding model once
model = SentenceTransformer("all-MiniLM-L6-v2")


def create_embeddings(chunks):
    """
    Creates embeddings for all document chunks.
    """

    texts = [chunk["text"] for chunk in chunks]

    embeddings = model.encode(
        texts,
        show_progress_bar=True,
        convert_to_numpy=True
    )

    return embeddings


def create_query_embedding(query):
    """
    Creates an embedding for a user's question.
    """

    embedding = model.encode(
        query,
        convert_to_numpy=True
    )

    return embedding