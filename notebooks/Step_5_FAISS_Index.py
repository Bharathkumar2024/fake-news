"""
STEP 5: Build FAISS Index for Vector Search
Creates fast similarity search index

Command: python notebooks/Step_5_FAISS_Index.py
"""

import os
import sys
import pickle
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config

print("=" * 60)
print("🔎 STEP 5: Building FAISS Index")
print("=" * 60)

# Load embeddings
embeddings_path = os.path.join(config.DATA_DIR, "embeddings.pkl")
print(f"\n📥 Loading embeddings from: {embeddings_path}")

try:
    with open(embeddings_path, 'rb') as f:
        embeddings = pickle.load(f)
    print(f"✅ Embeddings loaded: {embeddings.shape}")
except Exception as e:
    print(f"❌ Error loading embeddings: {e}")
    sys.exit(1)

# Load texts (facts)
cleaned_csv = os.path.join(config.DATA_DIR, "cleaned_data.csv")
try:
    import pandas as pd
    data = pd.read_csv(cleaned_csv)
    facts = data['text'].tolist()  # Original text for display
    print(f"✅ Facts loaded: {len(facts)} records")
except Exception as e:
    print(f"❌ Error loading facts: {e}")
    sys.exit(1)

# Build FAISS index
print(f"\n🔄 Building FAISS index...")
print(f"   Dimension: {embeddings.shape[1]}")
print(f"   Records: {embeddings.shape[0]}")

try:
    try:
        import faiss
    except ImportError:
        print("❌ faiss-cpu not installed. Install with: pip install faiss-cpu")
        sys.exit(1)
    
    # Convert to float32 (required by FAISS)
    embeddings = embeddings.astype('float32')
    
    # Create index
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)
    
    print(f"✅ FAISS index created!")
    print(f"   Total vectors: {index.ntotal}")
    
except Exception as e:
    print(f"❌ Error building FAISS index: {e}")
    sys.exit(1)

# Test the index
print(f"\n✅ Testing index with sample query...")
query = embeddings[0:1]  # First embedding as test query
D, I = index.search(query, k=5)
print(f"   Top 5 similar facts:")
for i, idx in enumerate(I[0]):
    print(f"   {i+1}. Similarity: {D[0][i]:.4f} | Text: {facts[idx][:100]}...")

# Save index
index_path = config.FAISS_INDEX_PATH
with open(index_path, 'wb') as f:
    pickle.dump(index, f)
print(f"\n✅ FAISS index saved to: {index_path}")

# Save facts
facts_path = config.FACTS_PATH
with open(facts_path, 'wb') as f:
    pickle.dump(facts, f)
print(f"✅ Facts saved to: {facts_path}")

print("\n" + "=" * 60)
print("👉 Next Step: Run Step_6_Train_Model.py")
print("=" * 60)
