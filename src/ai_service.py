import os

from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Read API key from .env
api_key = os.getenv("GEMINI_API_KEY")

# Create Gemini client
client = genai.Client(api_key=api_key)


def generate_ai_answer(question):

    prompt = f"""
You are an educational AI assistant.

Explain concepts clearly and simply.

Keep the answer under 200 words.

Question:
{question}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    return response.text