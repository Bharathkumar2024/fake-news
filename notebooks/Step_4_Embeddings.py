"""
STEP 4: Generate Embeddings
Creates semantic embeddings using Sentence Transformers

Command: python notebooks/Step_4_Embeddings.py
"""

import pandas as pd
import numpy as np
import os
import sys
import pickle

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config
from src.embedder import get_embeddings

print("=" * 60)
print("🤖 STEP 4: Generating Embeddings")
print("=" * 60)

# Load cleaned data
cleaned_csv = os.path.join(config.DATA_DIR, "cleaned_data.csv")
print(f"\n📥 Loading: {cleaned_csv}")

try:
    data = pd.read_csv(cleaned_csv)
    texts = data['text_cleaned'].tolist()
    labels = data['label'].tolist()
    print(f"✅ Loaded {len(texts)} records")
except Exception as e:
    print(f"❌ Error: {e}")
    sys.exit(1)

# Generate embeddings
print(f"\n🔄 Generating embeddings for {len(texts)} texts...")
print(f"   Model: all-MiniLM-L6-v2")
print(f"   Dimension: {config.EMBEDDING_DIMENSION}")

try:
    embeddings = get_embeddings(texts, show_progress=True)
    
    if embeddings is None:
        print("❌ Embeddings generation returned None. Check if sentence-transformers is installed.")
        sys.exit(1)
    
    print(f"\n✅ Embeddings generated!")
    print(f"   Shape: {embeddings.shape}")
    print(f"   Data type: {embeddings.dtype}")
except Exception as e:
    print(f"❌ Error generating embeddings: {e}")
    sys.exit(1)

# Display embedding statistics
print("\n" + "=" * 60)
print("📊 Embedding Statistics")
print("=" * 60)
print(f"Min value: {embeddings.min():.6f}")
print(f"Max value: {embeddings.max():.6f}")
print(f"Mean value: {embeddings.mean():.6f}")
print(f"Std deviation: {embeddings.std():.6f}")

# Save embeddings
embeddings_path = os.path.join(config.DATA_DIR, "embeddings.pkl")
with open(embeddings_path, 'wb') as f:
    pickle.dump(embeddings, f)
print(f"\n✅ Embeddings saved to: {embeddings_path}")

# Save labels
with open(os.path.join(config.DATA_DIR, "labels.pkl"), 'wb') as f:
    pickle.dump(labels, f)
print(f"✅ Labels saved")

print("\n" + "=" * 60)
print("👉 Next Step: Run Step_5_FAISS_Index.py")
print("=" * 60)
