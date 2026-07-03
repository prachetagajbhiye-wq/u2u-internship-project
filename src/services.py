from data_loader import df
from ai_service import generate_ai_answer
from rag_service import retrieve_context

def get_all_questions():
    return df.to_dict(orient="records")


def get_subjects():
    return sorted(df["subject"].unique().tolist())


def get_questions_by_subject(subject):
    filtered_df = df[df["subject"] == subject]
    return filtered_df.to_dict(orient="records")


def get_random_question():
    random_row = df.sample(n=1)
    return random_row.to_dict(orient="records")[0]


def search_questions(keyword):

    filtered_df = df[
        df["question"].str.contains(keyword, case=False, na=False)
    ]

    return filtered_df.to_dict(orient="records")

def get_answer(question):

    context, sources = retrieve_context(question)

    answer = generate_ai_answer(
        question,
        context
    )

    return {
        "source": "RAG + Gemini",
        "question": question,
        "answer": answer,
        "sources": sources
    }