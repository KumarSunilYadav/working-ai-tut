import streamlit as st
import sys
import os
import sys
import os
from .tutor import answer_question

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from dotenv import load_dotenv
from PIL import Image

# Add app folder to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from app.tutor import answer_question
from app.vector_store import load_and_embed

# Load environment variables
load_dotenv()

# Streamlit page config
st.set_page_config(page_title="AI Tutor", page_icon="📚", layout="centered")

# Custom CSS for styling
st.markdown("""
    <style>
    .main {
        background-color: #f9f9f9;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        padding: 10px 24px;
        border: none;
        border-radius: 8px;
        font-size: 16px;
    }
    .stTextInput>div>div>input {
        border: 1px solid #ccc;
        border-radius: 8px;
        padding: 8px;
        font-size: 16px;
    }
    </style>
""", unsafe_allow_html=True)

# App title
st.markdown("""
# 🤖 AI Tutor
Upload your notes and get smart answers instantly. Powered by **Gemini Pro** and AI search.
""")

# File uploader
with st.expander("📁 Upload your PDF notes"):
    uploaded_file = st.file_uploader("Upload a PDF", type="pdf")
    if uploaded_file:
        file_path = os.path.join("data", "uploaded_notes", uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        load_and_embed(file_path)
        st.success("✅ Notes uploaded and indexed successfully!")

st.markdown("---")

# Q&A interface
st.subheader("💬 Ask Your Tutor")
question = st.text_input("What do you want to learn or clarify?")

if st.button("🎓 Get Answer") and question:
    with st.spinner("Thinking with AI..."):
        answer = answer_question(question)
        st.markdown(f"### 🧠 Answer:\n{answer}")
