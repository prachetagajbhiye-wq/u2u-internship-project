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
    Use the provided context whenever it is relevant.
    If the context contains the answer,
    answer from it in a clear and friendly way.
    If the context does NOT contain the answer,
    use your own knowledge to answer correctly.

    At the end, mention whether the answer came from:
    - Knowledge Base
    - AI Knowledge
    
    Context:
    {context}

    Question:
    {question}
    """

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )

        return response.text

    except Exception:
        return (
            "⚠️ AI service is currently unavailable. Please try again."
        )