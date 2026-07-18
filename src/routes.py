from flask import Blueprint, jsonify, request
from services import (
    get_all_questions,
    get_subjects,
    get_questions_by_subject,
    get_random_question,
    search_questions,
    get_answer
)

from upload_service import process_uploaded_file

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


# ==========================
# Upload Route
# ==========================

@api.route("/upload", methods=["POST"])
def upload_file():

    if "file" not in request.files:
        return jsonify({
            "success": False,
            "message": "No file selected."
        }), 400

    file = request.files["file"]

    if file.filename == "":
        return jsonify({
            "success": False,
            "message": "No file selected."
        }), 400

    result = process_uploaded_file(file)

    return jsonify(result)