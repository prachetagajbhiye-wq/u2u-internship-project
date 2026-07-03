from document_loader import load_documents
from chunker import chunk_documents

docs = load_documents()

chunks = chunk_documents(docs)

print(f"Loaded {len(docs)} documents")
print(f"Created {len(chunks)} chunks")

print()

print(chunks[0])