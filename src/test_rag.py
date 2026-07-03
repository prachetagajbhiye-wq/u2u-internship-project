from rag_service import retrieve_context

context, sources = retrieve_context(
    "What is a process?"
)

print("Context:\n")
print(context)

print("\nSources:")
print(sources)