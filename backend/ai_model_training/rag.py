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
# Structure: {'embedding': np.array, 'text': str, 'source': str, 'page': int}
VECTOR_DB = []

def add_to_vector_db(content_list):
    """
    Add list of content dicts to vector database.
    Input: [{'text': str, 'page': int, 'source': str}]
    """
    if not content_list:
        return
        
    added_count = 0
    
    for item in content_list:
        text = item.get('text', '')
        if len(text.strip()) < 20:
            continue
            
        # Chunk large pages into smaller segments for better retrieval
        chunks = [text[i:i+600] for i in range(0, len(text), 500)] # 100 char overlap
        
        for chunk in chunks:
            if len(chunk.strip()) < 30:
                continue
                
            entry = {
                'text': chunk.strip(),
                'source': item.get('source', 'Unknown'),
                'page': item.get('page', 0),
                'embedding': None
            }
            
            if use_embeddings and embedding_model:
                try:
                    entry['embedding'] = embedding_model.encode(chunk.strip())
                except Exception as e:
                    print(f"Encoding error: {e}")
            
            VECTOR_DB.append(entry)
            added_count += 1
    
    print(f"✓ Added {added_count} chunks. Total: {len(VECTOR_DB)}")

def retrieve(query):
    """
    Semantic search using embeddings.
    Returns: [{'text': str, 'source': str, 'page': int, 'score': float}]
    """
    if not VECTOR_DB:
        print("✗ Vector DB is empty")
        return []
        
    results = []
    
    if use_embeddings and embedding_model:
        # Semantic search
        try:
            query_embedding = embedding_model.encode(query)
            
            # Filter entries with embeddings
            valid_entries = [e for e in VECTOR_DB if e['embedding'] is not None]
            
            if not valid_entries:
                return []
                
            # Convert to numpy arrays for matrix operation
            embeddings = np.array([e['embedding'] for e in valid_entries])
            
            # Compute cosine similarity
            norms = np.linalg.norm(embeddings, axis=1) * np.linalg.norm(query_embedding)
            norms[norms == 0] = 1e-10 
            
            scores = np.dot(embeddings, query_embedding) / norms
            
            # Filter by threshold (0.4 is a good balance for BGE-M3)
            THRESHOLD = 0.35
            
            # Get indices where score > THRESHOLD
            relevant_indices = np.where(scores > THRESHOLD)[0]
            
            if len(relevant_indices) == 0:
                print(f"✗ No chunks exceeded threshold {THRESHOLD}")
                return []
                
            # Sort only relevant indices
            relevant_scores = scores[relevant_indices]
            top_k_indices = relevant_indices[np.argsort(relevant_scores)[::-1][:5]]
            
            for idx in top_k_indices:
                entry = valid_entries[idx]
                results.append({
                    'text': entry['text'],
                    'source': entry['source'],
                    'page': entry['page'],
                    'score': float(scores[idx])
                })
                
            print(f"✓ Found {len(results)} chunks above threshold")
            
        except Exception as e:
            print(f"Retrieval error: {e}")
            return []
            
    else:
        # Keyword fallback
        query_words = [word for word in query.lower().split() if len(word) > 2]
        
        for entry in VECTOR_DB:
            chunk_lower = entry['text'].lower()
            score = sum(1 for word in query_words if word in chunk_lower)
            if score > 0:
                results.append({
                    'text': entry['text'],
                    'source': entry['source'],
                    'page': entry['page'],
                    'score': float(score)
                })
        
        results.sort(key=lambda x: x['score'], reverse=True)
        results = results[:5]
        print(f"✓ Found {len(results)} chunks (keyword search)")
        
    return results