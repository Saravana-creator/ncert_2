#This file is for RAG(Retrieval Augmented Generation) with Semantic Search

try:
    from sentence_transformers import SentenceTransformer
    import numpy as np
    
    print("Loading BAAI/bge-m3 embedding model...")
    embedding_model = SentenceTransformer("BAAI/bge-m3")
    print("✓ BAAI/bge-m3 loaded successfully")
    use_embeddings = True
except Exception as e:
    print(f"✗ Embedding model failed: {e}")
    use_embeddings = False
    embedding_model = None

# Dynamic vector storage with embeddings
VECTOR_DB = []  # List of (embedding, text) tuples

def add_to_vector_db(text):
    """Add text chunks with embeddings to vector database"""
    if not text or len(text.strip()) < 10:
        print("Text too short, skipping...")
        return
        
    # Create chunks of 500 characters
    chunks = [text[i:i+500] for i in range(0, len(text), 500)]
    
    added_count = 0
    for chunk in chunks:
        if len(chunk.strip()) > 20:
            if use_embeddings and embedding_model:
                embedding = embedding_model.encode(chunk.strip())
                VECTOR_DB.append((embedding, chunk.strip()))
            else:
                VECTOR_DB.append((None, chunk.strip()))
            added_count += 1
    
    print(f"✓ Added {added_count} chunks. Total: {len(VECTOR_DB)}")

def retrieve(query):
    """Semantic search using embeddings"""
    if not VECTOR_DB:
        print("✗ Vector DB is empty")
        return []
    
    if use_embeddings and embedding_model:
        # Semantic search
        query_embedding = embedding_model.encode(query)
        
        similarities = []
        for embedding, chunk in VECTOR_DB:
            if embedding is not None:
                similarity = np.dot(query_embedding, embedding) / (
                    np.linalg.norm(query_embedding) * np.linalg.norm(embedding)
                )
                similarities.append((similarity, chunk))
        
        similarities.sort(key=lambda x: x[0], reverse=True)
        result = [chunk for _, chunk in similarities[:5]]
        
        print(f"✓ Found {len(result)} chunks (semantic search)")
        return result
    
    else:
        # Keyword fallback
        query_words = [word for word in query.lower().split() if len(word) > 2]
        relevant_chunks = []
        
        for _, chunk in VECTOR_DB:
            chunk_lower = chunk.lower()
            score = sum(1 for word in query_words if word in chunk_lower)
            if score > 0:
                relevant_chunks.append((score, chunk))
        
        relevant_chunks.sort(key=lambda x: x[0], reverse=True)
        result = [chunk for _, chunk in relevant_chunks[:5]]
        
        print(f"✓ Found {len(result)} chunks (keyword search)")
        return result