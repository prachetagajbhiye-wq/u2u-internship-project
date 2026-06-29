from flask import Blueprint, jsonify, request
import random
from services import (
    get_all_questions,
    get_subjects,
    get_questions_by_subject,
    get_random_question,
    search_questions,
    get_answer
)

api = Blueprint("api", __name__)

@api.route("/")
def home():
    return jsonify({
        "message": "Welcome to the AI-Powered Educational Learning Platform",
        "status": "Backend is running"
    })

@api.route("/subjects")
def subjects():
    subjects = get_subjects()

    return jsonify({
        "count": len(subjects),
        "subjects": subjects
    })

@api.route("/questions")
def get_questions():

    subject = request.args.get("subject")

    if subject:
        return jsonify(get_questions_by_subject(subject))

    return jsonify(get_all_questions())


@api.route("/random-question")
def random_question():

    return jsonify(get_random_question())

@api.route("/search")
def search():

    keyword = request.args.get("keyword")

    if not keyword:
        return jsonify({
            "error": "Please provide a keyword."
        }), 400

    return jsonify(search_questions(keyword))

@api.route("/answer")
def answer():

    question = request.args.get("question")

    if not question:
        return jsonify({
            "error": "Please provide a question."
        }), 400

    return jsonify(get_answer(question))

