from embedding_service import create_query_embedding
from vector_store import search

query = "What is a process?"

embedding = create_query_embedding(query)

results = search(embedding)

print("Search Results:\n")

for i in range(len(results["documents"][0])):

    print("Document:")
    print(results["documents"][0][i])

    print()

    print("Source:")
    print(results["metadatas"][0][i]["source"])

    print("-" * 60)