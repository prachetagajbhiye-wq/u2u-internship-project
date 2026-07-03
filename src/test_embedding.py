from document_loader import load_documents
from chunker import chunk_documents
from embedding_service import create_embeddings
from vector_store import store_embeddings

docs = load_documents()

chunks = chunk_documents(docs)

embeddings = create_embeddings(chunks)

print(f"Created {len(embeddings)} embeddings")

store_embeddings(chunks, embeddings)

print("Embeddings stored successfully in ChromaDB!")