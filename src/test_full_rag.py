from rag_service import retrieve_context
from ai_service import generate_ai_answer

question = "Explain process scheduling."

context, sources = retrieve_context(question)

answer = generate_ai_answer(question, context)

print("\nAnswer:\n")
print(answer)

print("\nSources:")
print(sources)