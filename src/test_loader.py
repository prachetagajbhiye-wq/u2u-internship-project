from document_loader import load_documents

docs = load_documents()

print(f"Loaded {len(docs)} documents\n")

for doc in docs[:5]:

    print(doc["source"])

    print(doc["text"][:120])

    print("-" * 60)