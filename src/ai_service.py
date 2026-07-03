import os

from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Read API key from .env
api_key = os.getenv("GEMINI_API_KEY")

# Create Gemini client
client = genai.Client(api_key=api_key)


def generate_ai_answer(question, context=""):

    prompt = f"""
You are an educational AI assistant.

Answer ONLY using the provided context.

If the context is insufficient,
say that the knowledge base does not contain enough information.

Context:

{context}

Question:

{question}

Give a clear explanation.
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )

        return response.text

    except Exception:
        return (
            "⚠️ The AI service is currently busy. "
            "Please try again in a few moments."
        )