from document_loader import load_documents

docs = load_documents()

print("Loaded", len(docs), "documents")

for doc in docs:

    print(doc["source"])

    print(doc["text"][:500])

    print("-" * 60)