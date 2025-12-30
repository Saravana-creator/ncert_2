#Ingest file is for chunking and embedding

from ocr import extract_text
from rag import add_to_vector_db

def ingest_file(path):
    try:
        print(f"Processing file: {path}")
        # Returns list of dicts [{'text':..., 'page':..., 'source':...}]
        content_items = extract_text(path)
        
        if not content_items:
            print("No text extracted")
            return "No text extracted from file"
            
        print(f"Extracted {len(content_items)} content items (pages/images)")
        
        add_to_vector_db(content_items)
        
        total_chars = sum(len(item['text']) for item in content_items)
        print(f"Added to vector DB successfully. Total chars: {total_chars}")
        
        return f"Processed {len(content_items)} pages/items with {total_chars} characters"
        
    except Exception as e:
        print(f"Ingest error: {e}")
        return f"Error processing file: {str(e)}"