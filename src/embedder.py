"""
Embedding Generation Module
Uses Sentence Transformers for semantic understanding
"""

import numpy as np

try:
    from sentence_transformers import SentenceTransformer
    # Load pre-trained embedding model
    embedder = SentenceTransformer('all-MiniLM-L6-v2')
except ImportError:
    print("⚠️  Sentence Transformers not installed. Embeddings disabled.")
    embedder = None

def get_embeddings(texts, show_progress=False):
    """
    Generate embeddings for list of texts
    Returns: numpy array of shape (len(texts), 384)
    """
    if not embedder:
        print("❌ Embedder not available. Install sentence-transformers.")
        return None
        
    if not texts:
        return None
    
    try:
        embeddings = embedder.encode(texts, show_progress_bar=show_progress)
        return embeddings
    except Exception as e:
        print(f"❌ Embedding Error: {e}")
        return None

def get_single_embedding(text):
    """
    Generate embedding for single text
    Returns: numpy array of shape (384,)
    """
    if not embedder:
        return None
        
    if not text or len(text) < 2:
        return None
    
    try:
        embedding = embedder.encode([text])
        return embedding[0] if embedding is not None and len(embedding) > 0 else None
    except Exception as e:
        print(f"❌ Embedding Error: {e}")
        return None

def cosine_similarity(vec1, vec2):
    """
    Calculate cosine similarity between two vectors
    """
    if vec1 is None or vec2 is None:
        return 0.0
        
    try:
        dot_product = np.dot(vec1, vec2)
        norm_vec1 = np.linalg.norm(vec1)
        norm_vec2 = np.linalg.norm(vec2)
        
        if norm_vec1 == 0 or norm_vec2 == 0:
            return 0.0
            
        similarity = dot_product / (norm_vec1 * norm_vec2)
        return float(similarity)
    except Exception as e:
        print(f"❌ Similarity Error: {e}")
        return 0.0
