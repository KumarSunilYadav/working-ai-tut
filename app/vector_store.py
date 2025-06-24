import chromadb
from sentence_transformers import SentenceTransformer
from app.loader import extract_text_from_pdf, split_text
import os

model = SentenceTransformer("all-MiniLM-L6-v2")
db = chromadb.Client()
collection = db.get_or_create_collection("notes")

def load_and_embed(path):
    text = extract_text_from_pdf(path)
    chunks = split_text(text)
    embeddings = model.encode(chunks)
    for chunk, embedding in zip(chunks, embeddings):
        collection.add(documents=[chunk], embeddings=[embedding], ids=[chunk[:10]])

def query_notes(query):
    query_embedding = model.encode([query])[0]
    results = collection.query(query_embeddings=[query_embedding], n_results=3)
    return "\n".join(results["documents"][0])