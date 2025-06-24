import google.generativeai as genai
from app.vector_store import query_notes
import os
from dotenv import load_dotenv

# Load .env and configure Gemini
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize Gemini Pro model
model = genai.GenerativeModel("gemini-2.0-flash")


def answer_question(query):
    context = query_notes(query)
    prompt = f"""Answer this question using the notes below.

Notes:
{context}

Question: {query}"""

    response = model.generate_content(prompt)
    return response.text.strip()
