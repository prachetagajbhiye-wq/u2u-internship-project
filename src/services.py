from data_loader import df
from rag_service import get_rag_answer


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

    result = get_rag_answer(question)

    return {
        "source": result["sources"],
        "question": question,
        "answer": result["answer"],
        "subject": "Knowledge Base",
        "difficulty": "-"
    }