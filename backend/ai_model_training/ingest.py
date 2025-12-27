#Ingest file is for chunking and embedding

from ocr import extract_text
from rag import add_to_vector_db

def ingest_file(path):
    try:
        print(f"Processing file: {path}")
        text = extract_text(path)
        print(f"Extracted text length: {len(text)}")
        add_to_vector_db(text)
        print(f"Added to vector DB successfully")
        return text
    except Exception as e:
        print(f"Ingest error: {e}")
        return f"Error processing file: {str(e)}"