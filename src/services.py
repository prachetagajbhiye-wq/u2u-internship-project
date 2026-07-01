from data_loader import df
from ai_service import generate_ai_answer


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

    search = question.lower()

    # Remove punctuation
    for char in ["?", ".", ",", "!", ":"]:
        search = search.replace(char, "")

    # Remove common words
    stop_words = [
        "what",
        "is",
        "the",
        "a",
        "an",
        "explain",
        "tell",
        "me",
        "about",
        "define",
        "please",
        "of"
    ]

    words = []

    for word in search.split():
        if word not in stop_words:
            words.append(word)

    if len(words) == 0:
        return {
            "message": "Please ask a meaningful question."
        }

    best_match = None
    best_score = 0

    for _, row in df.iterrows():

        db_question = row["question"].lower()

        score = 0

        for word in words:
            if word in db_question:
                score += 1

        if score > best_score:
            best_score = score
            best_match = row

    # If we found a good match in CSV, return it
    if best_match is not None and best_score > 0:
        return {
            "source": "CSV",
            "question": best_match["question"],
            "answer": best_match["answer"],
            "subject": best_match["subject"],
            "difficulty": best_match["difficulty"]
        }

    # Otherwise ask Gemini
    ai_answer = generate_ai_answer(question)

    return {
        "source": "Gemini AI",
        "question": question,
        "answer": ai_answer,
        "subject": "AI Generated",
        "difficulty": "-"
    }