import pdfplumber
from langchain.text_splitter import RecursiveCharacterTextSplitter

def extract_text_from_pdf(path):
    with pdfplumber.open(path) as pdf:
        return "\n".join([page.extract_text() or "" for page in pdf.pages])

def split_text(text):
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    return splitter.split_text(text)