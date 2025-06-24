from app.vector_store import query_notes
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-pro")

def generate_quiz(topic):
    context = query_notes(topic)
    prompt = f"""Create 3 multiple-choice questions based on the following content:\n\n{context}"""
    return model.generate_content(prompt).text